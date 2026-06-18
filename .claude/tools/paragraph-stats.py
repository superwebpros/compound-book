#!/usr/bin/env python3
"""Paragraph length stats for a .qmd chapter.

Counts sentences per prose paragraph and flags ones above a threshold.

Usage:
    python3 paragraph-stats.py chapters/01-diagnosis.qmd
    python3 paragraph-stats.py chapters/01-diagnosis.qmd --threshold 5
    python3 paragraph-stats.py chapters/01-diagnosis.qmd --all  # show all paragraphs

Skips: code blocks, callouts (the callout body counts but the markers don't),
tables, blockquotes (>), headings, lists, Excalidraw shortcodes.

Compares against Traction's reference: 3-4 sentences per paragraph average,
5-7 sentence paragraphs as occasional exceptions.
"""

import argparse
import re
import sys
from pathlib import Path
from statistics import mean, median


SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(\[*])")


def is_prose_line(line: str) -> bool:
    """Return True if line is a candidate prose line (not headings, lists, tables, etc.)."""
    s = line.strip()
    if not s:
        return False
    # Skip markdown structural elements
    if s.startswith("#"):
        return False  # heading
    if s.startswith(("- ", "* ", "+ ")):
        return False  # bullet list
    if re.match(r"^\d+\.\s", s):
        return False  # numbered list
    if s.startswith("|"):
        return False  # table row
    if s.startswith(">"):
        return False  # blockquote
    if s.startswith(":::"):
        return False  # callout boundary
    if s.startswith("```"):
        return False  # code fence
    if s.startswith("{{<") or s.startswith("{{ <"):
        return False  # shortcode line
    if s.startswith("<!--"):
        return False  # comment
    if s.startswith("---"):
        return False  # frontmatter / hr
    return True


def split_paragraphs(text: str) -> list[tuple[int, str]]:
    """Return list of (starting_line_number, paragraph_text)."""
    lines = text.splitlines()
    paragraphs = []
    current_lines: list[str] = []
    current_start = 0
    in_code_block = False
    in_callout = False
    in_table = False

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Track code-block boundaries
        if stripped.startswith("```"):
            if in_code_block:
                in_code_block = False
            else:
                in_code_block = True
            continue
        if in_code_block:
            continue

        # Track callout-body boundaries (we still count prose INSIDE callouts)
        if stripped.startswith(":::"):
            in_callout = not in_callout
            continue

        # Track table boundaries
        if stripped.startswith("|"):
            in_table = True
            continue
        if in_table and not stripped:
            in_table = False
            continue
        if in_table:
            continue

        # Blank line = paragraph break
        if not stripped:
            if current_lines:
                paragraphs.append((current_start, " ".join(current_lines)))
                current_lines = []
            continue

        # Filter out non-prose lines
        if not is_prose_line(line):
            # If we were building a paragraph, end it
            if current_lines:
                paragraphs.append((current_start, " ".join(current_lines)))
                current_lines = []
            continue

        # Accumulating prose
        if not current_lines:
            current_start = i
        current_lines.append(stripped)

    if current_lines:
        paragraphs.append((current_start, " ".join(current_lines)))

    return paragraphs


def count_sentences(paragraph: str) -> int:
    """Estimate sentence count by splitting on sentence-ending punctuation followed by capital."""
    # Strip markdown emphasis to avoid false positives on things like "see *the*."
    cleaned = re.sub(r"[*_`]", "", paragraph)
    # Strip block-level shortcodes / inline callouts
    cleaned = re.sub(r"\{\{<.*?>\}\}", "", cleaned)
    # Try splitter
    parts = SENTENCE_END.split(cleaned.strip())
    # Final part might be one sentence even without trailing punct
    if not parts:
        return 0
    # Count parts that look like real sentences (have at least one space + some characters)
    n = 0
    for p in parts:
        p = p.strip()
        if not p:
            continue
        # Only count parts with at least 5 characters (filters trailing fragments)
        if len(p) < 5:
            continue
        n += 1
    return max(n, 1)  # at least one sentence if paragraph has any prose


def format_preview(text: str, max_len: int = 60) -> str:
    text = text.strip()
    if len(text) <= max_len:
        return text
    return text[:max_len].rstrip() + "..."


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("chapter", help="path to a .qmd chapter")
    ap.add_argument("--threshold", type=int, default=5, help="flag paragraphs with > this many sentences (default 5)")
    ap.add_argument("--all", action="store_true", help="show every paragraph, not just flagged ones")
    args = ap.parse_args()

    path = Path(args.chapter)
    if not path.exists():
        print(f"error: {path} not found", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    paragraphs = split_paragraphs(text)

    if not paragraphs:
        print(f"no prose paragraphs found in {path}")
        return 0

    sentence_counts = [count_sentences(p) for _, p in paragraphs]

    print(f"# Paragraph stats: {path}")
    print()
    print(f"**Total prose paragraphs:** {len(paragraphs)}")
    print(f"**Sentences per paragraph (mean):** {mean(sentence_counts):.1f}")
    print(f"**Sentences per paragraph (median):** {median(sentence_counts):.0f}")
    print(f"**Longest paragraph:** {max(sentence_counts)} sentences")
    print(f"**Shortest paragraph:** {min(sentence_counts)} sentences")
    print()

    # Distribution
    dist: dict[int, int] = {}
    for n in sentence_counts:
        dist[n] = dist.get(n, 0) + 1
    print("**Distribution:**")
    print()
    print("| Sentences | Count |")
    print("|---|---|")
    for n in sorted(dist):
        bar = "█" * dist[n]
        print(f"| {n} | {dist[n]} {bar} |")
    print()

    # Traction reference
    flagged = sum(1 for n in sentence_counts if n > args.threshold)
    print(f"**Flagged (>{args.threshold} sentences):** {flagged} of {len(paragraphs)} ({100*flagged//len(paragraphs)}%)")
    print()
    print("> Traction reference: 3-4 sentences per paragraph average; 5-7 sentences as occasional exceptions.")
    print()

    # Per-paragraph table
    print("## Per-paragraph detail")
    print()
    print("| Line | Sentences | Preview |")
    print("|---|---|---|")
    for (start, para), n in zip(paragraphs, sentence_counts):
        if not args.all and n <= args.threshold:
            continue
        flag = " ⚠️" if n > args.threshold else ""
        preview = format_preview(para)
        # Escape pipes in preview
        preview = preview.replace("|", "\\|")
        print(f"| L{start} | {n}{flag} | {preview} |")
    if not args.all:
        print()
        print("_(Use `--all` to see every paragraph.)_")

    return 0


if __name__ == "__main__":
    sys.exit(main())
