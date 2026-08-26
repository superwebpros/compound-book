-- KDP print profile: make pandoc tables survive a 6x9 text block.
--
-- Two failure modes this fixes, both observed in KDP's previewer:
--   1. Proportional widths computed from markdown source give a column less
--      room than its own longest word, so text overprints the next column
--      (the AI Readiness Scorecard's "Dimension" column).
--   2. Tables with no computed widths render at natural width and run off
--      the page edge (the Ch1 snapshot table).
--
-- Strategy: every column gets at least (longest word) + padding; tables that
-- would exceed the text block get widths assigned from longest-line length.
-- Runs only for LaTeX output. Table body is set \small by the KDP preamble,
-- which the character-width constant below assumes.

if not FORMAT:match("latex") then
  return {}
end

local stringify = pandoc.utils.stringify

local CHAR_FRAC = 0.0125 -- fraction of \textwidth per character at \footnotesize
local PAD_FRAC = 0.040   -- 2*tabcolsep + rule allowance, as fraction

local function longest_word(s)
  local m = 0
  for w in s:gmatch("[^%s%-–—/]+") do
    if #w > m then m = #w end
  end
  return m
end

function Table(tbl)
  local ncols = #tbl.colspecs
  if ncols < 2 then return nil end

  local maxword, maxline = {}, {}
  for i = 1, ncols do maxword[i], maxline[i] = 0, 0 end

  local function scan_rows(rows)
    for _, row in ipairs(rows) do
      for i, cell in ipairs(row.cells) do
        if i <= ncols then
          local s = stringify(cell)
          local w = longest_word(s)
          if w > maxword[i] then maxword[i] = w end
          if #s > maxline[i] then maxline[i] = #s end
        end
      end
    end
  end
  scan_rows(tbl.head.rows)
  for _, body in ipairs(tbl.bodies) do
    scan_rows(body.head)
    scan_rows(body.body)
  end
  scan_rows(tbl.foot.rows)

  local widths, has_width = {}, false
  for i, spec in ipairs(tbl.colspecs) do
    if type(spec[2]) == "number" then
      has_width = true
      widths[i] = spec[2]
    else
      widths[i] = 0
    end
  end

  local mins, minsum = {}, 0
  for i = 1, ncols do
    mins[i] = maxword[i] * CHAR_FRAC + PAD_FRAC
    minsum = minsum + mins[i]
  end

  if not has_width then
    -- Auto-width table: only intervene if its natural width would overflow.
    local natural = 0
    for i = 1, ncols do
      natural = natural + maxline[i] * CHAR_FRAC + PAD_FRAC
    end
    if natural <= 0.95 then return nil end
    for i = 1, ncols do
      widths[i] = math.max(mins[i], (maxline[i] * CHAR_FRAC + PAD_FRAC) * 0.95 / natural)
    end
  end

  local MAXTOTAL = 0.97
  if minsum > MAXTOTAL then
    for i = 1, ncols do mins[i] = mins[i] * MAXTOTAL / minsum end
  end

  -- Raise starved columns to their minimum...
  local raised = 0
  for i = 1, ncols do
    if widths[i] < mins[i] then
      raised = raised + (mins[i] - widths[i])
      widths[i] = mins[i]
    end
  end
  -- ...and pay for it out of columns with slack.
  local slack = 0
  for i = 1, ncols do slack = slack + math.max(0, widths[i] - mins[i]) end
  if slack > 0 and raised > 0 then
    local factor = math.min(1, raised / slack)
    for i = 1, ncols do
      widths[i] = widths[i] - math.max(0, widths[i] - mins[i]) * factor
    end
  end

  local total = 0
  for i = 1, ncols do total = total + widths[i] end
  if total > MAXTOTAL then
    for i = 1, ncols do widths[i] = widths[i] * MAXTOTAL / total end
  end

  for i, spec in ipairs(tbl.colspecs) do
    tbl.colspecs[i] = { spec[1], widths[i] }
  end
  return tbl
end
