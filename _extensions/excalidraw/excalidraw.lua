-- Excalidraw shortcode for Quarto
-- Usage: {{< excalidraw ch01-headcount-paradox "Optional Caption" >}}
--
-- Converts .excalidraw JSON → SVG (HTML) or PNG (PDF/EPUB/DOCX) via Kroki.io API.
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

local function convert_via_kroki(excalidraw_path, output_path, fmt)
  -- POST the raw .excalidraw JSON to Kroki and save as SVG or PNG
  local url = "https://kroki.io/excalidraw/" .. fmt
  local cmd = string.format(
    'curl -s -X POST "%s" '
    .. '-H "Content-Type: text/plain" '
    .. '--data-binary @"%s" '
    .. '-o "%s" '
    .. '--max-time 30',
    url, excalidraw_path, output_path
  )
  local ok = os.execute(cmd)
  if not ok then
    io.stderr:write("excalidraw shortcode: curl failed for " .. excalidraw_path .. "\n")
    return false
  end
  -- Verify response
  local content = read_file(output_path)
  if not content or #content == 0 then
    io.stderr:write("excalidraw shortcode: Kroki returned empty response for " .. excalidraw_path .. "\n")
    return false
  end
  if fmt == "svg" and not content:match("^<svg") then
    io.stderr:write("excalidraw shortcode: Kroki returned non-SVG for " .. excalidraw_path .. "\n")
    io.stderr:write("  Response: " .. content:sub(1, 200) .. "\n")
    return false
  end
  return true
end

local function render_cached(source_path, cache_path, fmt, name)
  local needs_render = true
  if file_exists(cache_path) then
    local src_time = file_mtime(source_path)
    local cache_time = file_mtime(cache_path)
    if cache_time > 0 and cache_time >= src_time then
      needs_render = false
    end
  end
  if needs_render then
    io.stderr:write("excalidraw: rendering " .. name .. " as " .. fmt .. " via Kroki...\n")
    local ok = convert_via_kroki(source_path, cache_path, fmt)
    if not ok then return false end
    io.stderr:write("excalidraw: cached " .. name .. "." .. fmt .. "\n")
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

    if is_html then
      -- HTML: inline SVG for best quality
      local svg_path = cache_dir .. "/" .. name .. ".svg"
      if not render_cached(source_path, svg_path, "svg", name) then
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

    -- PDF, EPUB, DOCX, markdown: use PNG for maximum compatibility
    local png_path = cache_dir .. "/" .. name .. ".png"
    if not render_cached(source_path, png_path, "png", name) then
      return pandoc.Strong(pandoc.Str("[RENDER FAILED: " .. name .. "]"))
    end
    -- Use relative path from project root so Pandoc can resolve it for DOCX/PDF
    local rel_png_path = "_excalidraw-cache/" .. name .. ".png"
    local img_caption = caption ~= "" and {pandoc.Str(caption)} or {}
    return pandoc.Image(img_caption, rel_png_path, caption)
  end
}
