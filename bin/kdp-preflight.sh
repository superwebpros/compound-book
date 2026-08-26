#!/usr/bin/env bash
# Local KDP preflight for the 6x9 paperback interior.
# Rasterizes every page at 72dpi (1px = 1pt) and measures the VISIBLE ink
# bounding box — matching how KDP's checker behaves (it ignores invisible
# white-painted objects that a gs bbox scan would count).
#
# Rules for a 501-700 page, no-bleed 6x9 book:
#   gutter (inside) >= 0.75in = 54pt; outside/top/bottom >= 0.25in = 18pt
# PDF page 1 is a recto (odd = recto, inner = left). 1pt tolerance.
# Usage: bin/kdp-preflight.sh <interior.pdf>
set -euo pipefail

PDF="$1"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

pdftoppm -r 72 -gray -png "$PDF" "$WORK/p"

fail=0
total=0
for f in "$WORK"/p-*.png; do
  total=$((total+1))
  page=$((10#$(basename "$f" .png | sed 's/^p-//')))
  # %@ = bounding box of non-background content: WxH+X+Y (top-left origin)
  bbox=$(magick "$f" -fuzz 2% -format "%@" info: 2>/dev/null || echo "0x0+0+0")
  W=${bbox%%x*}; rest=${bbox#*x}; H=${rest%%+*}; rest=${rest#*+}; X=${rest%%+*}; Y=${rest##*+}
  [ "$W" = "0" ] && continue   # truly blank page
  xmin=$X; xmax=$((X+W)); top=$Y; bottom=$((648-Y-H))
  bad=""
  if [ $((page % 2)) -eq 1 ]; then  # recto: inner = left
    [ "$xmin" -lt 53 ] && bad="$bad gutter-left=$xmin"
    [ "$xmax" -gt 415 ] && bad="$bad outer-right=$xmax"
  else                              # verso: inner = right
    [ "$xmax" -gt 379 ] && bad="$bad gutter-right=$xmax"
    [ "$xmin" -lt 17 ] && bad="$bad outer-left=$xmin"
  fi
  [ "$top" -lt 17 ] && bad="$bad top=$top"
  [ "$bottom" -lt 17 ] && bad="$bad bottom=$bottom"
  if [ -n "$bad" ]; then
    echo "page $page:$bad"
    fail=$((fail+1))
  fi
done

if [ "$fail" -gt 0 ]; then
  echo "$fail of $total pages in violation"
  exit 1
else
  echo "PREFLIGHT CLEAN: all $total pages within KDP margins"
fi
