#!/usr/bin/env bash
# Strip the embedded cover from a Quarto-built EPUB for KDP upload.
# KDP attaches the cover uploaded in the KDP dashboard; an embedded cover
# shows doubled. Quarto's config schema forbids unsetting epub-cover-image
# from a profile, hence this post-processing step.
#
# Usage: bin/strip-epub-cover.sh <in.epub> <out.epub>
set -euo pipefail

IN="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
OUT="$2"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

unzip -q "$IN" -d "$WORK"

# Cover image file is the one flagged properties="cover-image" in the opf.
OPF="$WORK/EPUB/content.opf"
COVER_IMG=$(sed -n 's/.*properties="cover-image"[^>]*href="\([^"]*\)".*/\1/p' "$OPF")

rm -f "$WORK/EPUB/text/cover.xhtml"
[ -n "$COVER_IMG" ] && rm -f "$WORK/EPUB/$COVER_IMG"

# Drop every opf reference to the cover page and cover image.
sed -i '' \
  -e '/id="cover_xhtml"/d' \
  -e '/properties="cover-image"/d' \
  -e '/idref="cover_xhtml"/d' \
  -e '/reference type="cover"/d' \
  -e '/<meta name="cover"/d' \
  "$OPF"

# Drop nav/ncx entries pointing at the cover page.
[ -f "$WORK/EPUB/toc.ncx" ] && perl -0pi -e 's/<navPoint[^>]*>(?:(?!<\/navPoint>).)*cover\.xhtml(?:(?!<\/navPoint>).)*<\/navPoint>//gs' "$WORK/EPUB/toc.ncx"
find "$WORK/EPUB" -name "nav.xhtml" -exec perl -0pi -e 's/<li[^>]*>(?:(?!<\/li>).)*cover\.xhtml(?:(?!<\/li>).)*<\/li>//gs' {} \;

# Repackage: mimetype must be first and stored uncompressed.
OUTABS="$(cd "$(dirname "$OUT")" && pwd)/$(basename "$OUT")"
rm -f "$OUTABS"
(cd "$WORK" && zip -q -X -0 "$OUTABS" mimetype && zip -q -X -9 -r "$OUTABS" META-INF EPUB)

echo "Wrote $OUTABS"
