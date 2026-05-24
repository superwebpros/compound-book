-- Excalidraw shortcode for Quarto
-- Usage: {{< excalidraw ch01-headcount-paradox "Optional Caption" >}}
--
-- Converts .excalidraw JSON → SVG (HTML) or PNG (PDF/EPUB/DOCX).
-- SVG rendered via Kroki.io API; PNG converted locally from SVG via rsvg-convert.
-- Cache lives in _excalidraw-cache/ (gitignored).

local function file_exists(path)
  local f = io.open(path, "r")
  if f then f:close() return true end
  return false
end

local function file_mtime(path)
  local handle = io.popen('stat -f "%m" "' .. path .. '" 2>/dev/null')
  if not handle then return 0 end
  local result = handle:read("*a")
  handle:close()
  return tonumber(result) or 0
end

local function read_file(path)
  local f = io.open(path, "r")
  if not f then return nil end
  local content = f:read("*a")
  f:close()
  return content
end

local function ensure_cache_dir(project_dir)
  local cache_dir = project_dir .. "/_excalidraw-cache"
  os.execute('mkdir -p "' .. cache_dir .. '"')
  return cache_dir
end

local function render_svg_via_kroki(excalidraw_path, svg_path)
  local url = "https://kroki.io/excalidraw/svg"
  local cmd = string.format(
    'curl -s -X POST "%s" '
    .. '-H "Content-Type: text/plain" '
    .. '--data-binary @"%s" '
    .. '-o "%s" '
    .. '--max-time 30',
    url, excalidraw_path, svg_path
  )
  local ok = os.execute(cmd)
  if not ok then
    io.stderr:write("excalidraw shortcode: curl failed for " .. excalidraw_path .. "\n")
    return false
  end
  local content = read_file(svg_path)
  if not content or #content == 0 then
    io.stderr:write("excalidraw shortcode: Kroki returned empty response for " .. excalidraw_path .. "\n")
    return false
  end
  if not content:match("^<svg") then
    io.stderr:write("excalidraw shortcode: Kroki returned non-SVG for " .. excalidraw_path .. "\n")
    io.stderr:write("  Response: " .. content:sub(1, 200) .. "\n")
    return false
  end
  return true
end

local function has_rsvg_convert()
  local handle = io.popen("which rsvg-convert 2>/dev/null")
  local result = handle:read("*a")
  handle:close()
  return result and result:match("rsvg%-convert") ~= nil
end

local function convert_svg_to_png_local(svg_path, png_path)
  local cmd = string.format(
    'rsvg-convert -o "%s" --dpi-x 192 --dpi-y 192 "%s" 2>&1',
    png_path, svg_path
  )
  local handle = io.popen(cmd)
  local result = handle:read("*a")
  handle:close()
  if not file_exists(png_path) then
    io.stderr:write("excalidraw shortcode: rsvg-convert failed: " .. result .. "\n")
    return false
  end
  return true
end

local function render_png_via_kroki(excalidraw_path, png_path)
  local url = "https://kroki.io/excalidraw/png"
  local cmd = string.format(
    'curl -s -X POST "%s" '
    .. '-H "Content-Type: text/plain" '
    .. '--data-binary @"%s" '
    .. '-o "%s" '
    .. '--max-time 30',
    url, excalidraw_path, png_path
  )
  local ok = os.execute(cmd)
  if not ok then
    io.stderr:write("excalidraw shortcode: curl failed for PNG via Kroki\n")
    return false
  end
  if not file_exists(png_path) then
    io.stderr:write("excalidraw shortcode: Kroki PNG returned empty for " .. excalidraw_path .. "\n")
    return false
  end
  return true
end

local function ensure_svg_cached(source_path, svg_path, name)
  local needs_render = true
  if file_exists(svg_path) then
    local src_time = file_mtime(source_path)
    local cache_time = file_mtime(svg_path)
    if cache_time > 0 and cache_time >= src_time then
      needs_render = false
    end
  end
  if needs_render then
    io.stderr:write("excalidraw: rendering " .. name .. " as svg via Kroki...\n")
    local ok = render_svg_via_kroki(source_path, svg_path)
    if not ok then return false end
    io.stderr:write("excalidraw: cached " .. name .. ".svg\n")
  end
  return true
end

local function ensure_png_cached(source_path, svg_path, png_path, name)
  local needs_convert = true
  if file_exists(png_path) then
    local src_time = file_mtime(source_path)
    local png_time = file_mtime(png_path)
    if png_time > 0 and png_time >= src_time then
      needs_convert = false
    end
  end
  if needs_convert then
    if has_rsvg_convert() then
      -- Local: SVG via Kroki, then PNG via rsvg-convert (higher quality)
      if not ensure_svg_cached(source_path, svg_path, name) then
        return false
      end
      io.stderr:write("excalidraw: converting " .. name .. " svg→png via rsvg-convert...\n")
      local ok = convert_svg_to_png_local(svg_path, png_path)
      if not ok then return false end
    else
      -- CI/remote: PNG directly from Kroki
      io.stderr:write("excalidraw: rendering " .. name .. " as png via Kroki...\n")
      local ok = render_png_via_kroki(source_path, png_path)
      if not ok then return false end
    end
    io.stderr:write("excalidraw: cached " .. name .. ".png\n")
  end
  return true
end

return {
  ["excalidraw"] = function(args, kwargs, meta)
    local name = pandoc.utils.stringify(args[1] or "")
    local caption = ""
    if #args >= 2 then
      caption = pandoc.utils.stringify(args[2])
    end

    if name == "" then
      io.stderr:write("excalidraw shortcode: missing diagram name\n")
      return pandoc.Null()
    end

    local project_dir = quarto.project.directory or "."
    local source_path = project_dir .. "/excalidraw/" .. name .. ".excalidraw"

    if not file_exists(source_path) then
      io.stderr:write("excalidraw shortcode: file not found: " .. source_path .. "\n")
      return pandoc.Strong(pandoc.Str("[MISSING DIAGRAM: " .. name .. "]"))
    end

    local cache_dir = ensure_cache_dir(project_dir)
    local is_html = quarto.doc.is_format("html")

    local svg_path = cache_dir .. "/" .. name .. ".svg"

    if is_html then
      -- HTML: inline SVG for best quality
      if not ensure_svg_cached(source_path, svg_path, name) then
        return pandoc.Strong(pandoc.Str("[RENDER FAILED: " .. name .. "]"))
      end
      local svg_content = read_file(svg_path)
      if svg_content then
        local html = '<figure class="excalidraw-figure">\n'
          .. '<div class="excalidraw-diagram">\n'
          .. svg_content .. '\n'
          .. '</div>\n'
        if caption ~= "" then
          html = html .. '<figcaption>' .. caption .. '</figcaption>\n'
        end
        html = html .. '</figure>'
        return pandoc.RawInline("html", html)
      end
    end

    -- PDF, EPUB, DOCX, markdown: SVG via Kroki, then PNG via rsvg-convert
    local png_path = cache_dir .. "/" .. name .. ".png"
    if not ensure_png_cached(source_path, svg_path, png_path, name) then
      return pandoc.Strong(pandoc.Str("[RENDER FAILED: " .. name .. "]"))
    end
    local rel_png_path = "_excalidraw-cache/" .. name .. ".png"
    local img_caption = caption ~= "" and {pandoc.Str(caption)} or {}
    return pandoc.Image(img_caption, rel_png_path, caption)
  end
}
