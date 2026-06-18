#!/usr/bin/env python3
"""
apply_deflourish_report.py — build an edited COPY of a chapter from a deflourish report.

Reads a .claude/output/deflourish-<stem>.md report (the dry-run output of deflourish.py)
and applies each Original->Proposed revision to a copy of the chapter by exact-string
replacement. The original chapter is never touched. Lets you diff before/after in full
context without re-running the API (so the copy matches the exact edits already analyzed).

Usage:
  /usr/bin/python3 .claude/tools/apply_deflourish_report.py \
      .claude/output/deflourish-04-signal.md \
      chapters/04-signal.qmd \
      .claude/output/04-signal.deflourished.qmd
"""

import sys
from pathlib import Path


def collect_blockquote(lines, start_idx):
    """From the line after a '**Original:**'/'**Proposed:**' header, gather the
    blockquoted text (lines starting with '>'), joining with newlines."""
    out = []
    i = start_idx
    # skip blanks until the first '>' line
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    while i < len(lines) and lines[i].lstrip().startswith(">"):
        stripped = lines[i].lstrip()
        # remove leading '>' and a single following space
        text = stripped[1:]
        if text.startswith(" "):
            text = text[1:]
        out.append(text)
        i += 1
    return "\n".join(out)


def parse_pairs(report_text):
    lines = report_text.split("\n")
    pairs = []
    orig = None
    for idx, line in enumerate(lines):
        if line.strip() == "**Original:**":
            orig = collect_blockquote(lines, idx + 1)
        elif line.strip() == "**Proposed:**":
            prop = collect_blockquote(lines, idx + 1)
            if orig is not None:
                pairs.append((orig, prop))
                orig = None
    return pairs


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        return 2
    report_path, chapter_path, out_path = (Path(a) for a in sys.argv[1:])
    report = report_path.read_text(encoding="utf-8")
    text = chapter_path.read_text(encoding="utf-8")
    pairs = parse_pairs(report)

    applied = 0
    misses = []
    for orig, prop in pairs:
        if orig == prop:
            continue  # editor returned unchanged
        count = text.count(orig)
        if count == 1:
            text = text.replace(orig, prop)
            applied += 1
        else:
            misses.append((count, orig[:70]))

    out_path.write_text(text, encoding="utf-8")
    print(f"pairs in report: {len(pairs)}")
    print(f"applied: {applied}")
    if misses:
        print(f"NOT applied ({len(misses)} — original not found uniquely):")
        for count, preview in misses:
            print(f"  [{count}x] {preview}")
    print(f"wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
