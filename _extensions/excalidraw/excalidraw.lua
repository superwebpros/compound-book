-- Excalidraw shortcode for Quarto
-- Usage: {{< excalidraw ch01-headcount-paradox "Optional Caption" >}}
--
-- Converts .excalidraw JSON → SVG via Kroki.io API, caches locally.
-- Cache lives in _excalidraw-cache/ (gitignored).

local function file_exists(path)
  local f = io.open(path, "r")
  if f then f:close() return true end
  return false
end

local function file_mtime(path)
  -- Use stat to get modification time as epoch seconds
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

local function convert_to_svg(excalidraw_path, svg_path)
  -- POST the raw .excalidraw JSON to Kroki and save the SVG
  local cmd = string.format(
    'curl -s -X POST "https://kroki.io/excalidraw/svg" '
    .. '-H "Content-Type: text/plain" '
    .. '--data-binary @"%s" '
    .. '-o "%s" '
    .. '--max-time 30',
    excalidraw_path, svg_path
  )
  local ok = os.execute(cmd)
  if not ok then
    io.stderr:write("excalidraw shortcode: curl failed for " .. excalidraw_path .. "\n")
    return false
  end
  -- Verify we got an SVG back (not an error page)
  local content = read_file(svg_path)
  if not content or not content:match("^<svg") then
    io.stderr:write("excalidraw shortcode: Kroki returned non-SVG for " .. excalidraw_path .. "\n")
    if content then io.stderr:write("  Response: " .. content:sub(1, 200) .. "\n") end
    return false
  end
  return true
end

return {
  ["excalidraw"] = function(args, kwargs, meta)
    -- Parse arguments
    local name = pandoc.utils.stringify(args[1] or "")
    local caption = ""
    if #args >= 2 then
      caption = pandoc.utils.stringify(args[2])
    end

    if name == "" then
      io.stderr:write("excalidraw shortcode: missing diagram name\n")
      return pandoc.Null()
    end

    -- Resolve paths relative to project root
    -- quarto.project.directory is available in Quarto 1.4+
    local project_dir = quarto.project.directory or "."
    local excalidraw_dir = project_dir .. "/excalidraw"
    local source_path = excalidraw_dir .. "/" .. name .. ".excalidraw"

    if not file_exists(source_path) then
      io.stderr:write("excalidraw shortcode: file not found: " .. source_path .. "\n")
      return pandoc.Strong(pandoc.Str("[MISSING DIAGRAM: " .. name .. "]"))
    end

    -- Cache directory
    local cache_dir = ensure_cache_dir(project_dir)
    local svg_path = cache_dir .. "/" .. name .. ".svg"

    -- Check if cached SVG is fresh
    local needs_render = true
    if file_exists(svg_path) then
      local src_time = file_mtime(source_path)
      local svg_time = file_mtime(svg_path)
      if svg_time > 0 and svg_time >= src_time then
        needs_render = false
      end
    end

    -- Render if needed
    if needs_render then
      io.stderr:write("excalidraw: rendering " .. name .. " via Kroki...\n")
      local ok = convert_to_svg(source_path, svg_path)
      if not ok then
        return pandoc.Strong(pandoc.Str("[RENDER FAILED: " .. name .. "]"))
      end
      io.stderr:write("excalidraw: cached " .. name .. ".svg\n")
    end

    -- For HTML output, inline the SVG for best quality
    -- For PDF/EPUB, use the file path
    local format = quarto.doc.is_format("html") and "html" or "other"

    if format == "html" then
      local svg_content = read_file(svg_path)
      if svg_content then
        -- Wrap SVG in a figure with optional caption
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

    -- Fallback: use as image
    local img_caption = caption ~= "" and {pandoc.Str(caption)} or {}
    return pandoc.Image(img_caption, svg_path, caption)
  end
}
