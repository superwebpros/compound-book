#!/usr/bin/env python3
"""Prose rhythm & craft metrics for a .qmd chapter — the pacing layer.

Grounds the soft "pacing" judgment in named craft standards:
  - Gary Provost (sentence variety): rhythm = variation in sentence length.
    Monotone length reads as drag; high variance reads as music.
  - Joseph Williams (Style): nominalization density — abstract -tion/-ment/-ness
    nouns that bury the actor and slow the prose.
  - Run-on / staccato detection: over-long sentences and runs of same-length sentences.
  - proselint (optional): lints prose against Zinsser/Garner/Strunk style rules.

Standalone:
    /usr/bin/python3 .claude/tools/prose_rhythm.py chapters/05-source.qmd
Imported (by voice-scan.py):
    import prose_rhythm; out.extend(prose_rhythm.rhythm_section_lines(path))

Thresholds are HEURISTIC starting points (see constants). Calibrate against a
reference text (e.g. Traction) once the prose-craft skill exists.
"""
import re
import sys
import json
import subprocess
import tempfile
import os
from pathlib import Path
from statistics import mean, median, pstdev

# --- Thresholds, calibrated against Traction (audiobook transcript, 2026-06-15) ---
# Traction baseline: per-chapter CV 0.43-0.71 (mean 0.56); nominalization 3.2/100;
# short(<=8w) 21%; long(>=40w) 1.6%; mean sentence 15.5w.
CV_MONOTONE = 0.45        # Traction's per-chapter floor is 0.43; below ~0.45 = drag risk
CV_GOOD = 0.56            # Traction's mean; at/above this = healthy rhythm
RUN_LEN = 5               # N consecutive sentences within RUN_BAND = a monotone run
RUN_BAND = 4              # max(len)-min(len) <= this counts as "same length"
FLAT_PARA_STDEV = 2.5     # paragraph w/ >=3 sentences and stdev below this reads flat
LONG_SENTENCE = 40        # words; run-on flag (Traction keeps these to ~1.6% of sentences)
NOMINAL_PER_100 = 3.6     # Traction sits at 3.2; flag only genuine outliers above ~3.6

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])")
NOMINAL = re.compile(r"\b[A-Za-z]{4,}(?:tion|tions|ment|ments|ness|ity|ities|ance|ence|ancy|ency)\b", re.I)
WORD = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)?")


def extract_prose(path: Path):
    """Return (joined_prose_text, [paragraph_text,...]) skipping non-prose structure."""
    paras, buf, incode = [], [], False
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("```"):
            incode = not incode
            continue
        if incode:
            continue
        if not s:
            if buf:
                paras.append(" ".join(buf)); buf = []
            continue
        if s.startswith(("#", "|", ">", ":::", "{{<", "![", "<!--")) \
           or s.startswith(("- ", "* ", "+ ")) or re.match(r"^\d+\.\s", s) \
           or s.startswith("##"):
            if buf:
                paras.append(" ".join(buf)); buf = []
            continue
        buf.append(s)
    if buf:
        paras.append(" ".join(buf))
    # strip markdown emphasis/inline-code for clean sentence/word counts
    clean = [re.sub(r"[*_`]", "", p) for p in paras]
    clean = [p for p in clean if len(WORD.findall(p)) >= 3]
    return " ".join(clean), clean


def split_sentences(paragraph: str):
    parts = SENTENCE_SPLIT.split(paragraph.strip())
    return [p for p in parts if WORD.findall(p)]


def sentence_lengths(paragraphs):
    lens, per_para = [], []
    for p in paragraphs:
        sl = [len(WORD.findall(s)) for s in split_sentences(p)]
        sl = [n for n in sl if n > 0]
        per_para.append(sl)
        lens.extend(sl)
    return lens, per_para


def monotone_runs(lens):
    """Return list of (start_index, run_length, band) for runs of >=RUN_LEN
    consecutive sentences whose lengths sit within RUN_BAND words."""
    runs, i, n = [], 0, len(lens)
    while i < n:
        j = i + 1
        lo = hi = lens[i]
        while j < n and (max(hi, lens[j]) - min(lo, lens[j])) <= RUN_BAND:
            lo, hi = min(lo, lens[j]), max(hi, lens[j])
            j += 1
        if j - i >= RUN_LEN:
            runs.append((i, j - i, (lo, hi)))
        i = j if j > i + 1 else i + 1
    return runs


def run_proselint(prose_text: str):
    """Lint extracted prose via the proselint Python API. Returns {total, by_check} or None.

    proselint.tools.lint(text) -> list of tuples:
    (check, message, line, col, start, end, extent, severity, replacements)
    """
    try:
        from proselint import tools as _pl
    except ImportError:
        return None
    try:
        results = _pl.lint(prose_text)
    except Exception as e:  # noqa
        return {"error": str(e)}
    by_check = {}
    for r in results:
        check = r[0] if len(r) > 0 else "?"
        message = r[1] if len(r) > 1 else ""
        by_check.setdefault(check, {"count": 0, "example": message})
        by_check[check]["count"] += 1
    return {"total": len(results), "by_check": by_check}


def rhythm_section_lines(chapter_path: Path):
    """Markdown lines for the rhythm/craft section. Importable by voice-scan.py."""
    prose, paras = extract_prose(chapter_path)
    lens, per_para = sentence_lengths(paras)
    out = ["\n## Prose rhythm & craft (Provost / Williams)\n"]
    if not lens:
        out.append("No prose sentences found.\n")
        return out

    cv = pstdev(lens) / mean(lens) if mean(lens) else 0
    short = sum(1 for n in lens if n <= 8)
    long_ = sum(1 for n in lens if n >= LONG_SENTENCE)
    verdict = "monotone (drag risk)" if cv < CV_MONOTONE else ("healthy variety" if cv >= CV_GOOD else "moderate")
    out.append(f"**Sentences:** {len(lens)} | **mean** {mean(lens):.1f}w | **median** {median(lens)}w "
               f"| **range** {min(lens)}–{max(lens)}w")
    out.append(f"**Sentence-length variation (Provost CV):** {cv:.2f} — {verdict} "
               f"_(heuristic: <{CV_MONOTONE} monotone, ≥{CV_GOOD} good)_")
    out.append(f"**Short (≤8w):** {short} ({100*short//len(lens)}%) | **Long (≥{LONG_SENTENCE}w):** {long_}")

    # nominalization density (Williams)
    nwords = len(WORD.findall(prose))
    nnom = len(NOMINAL.findall(prose))
    dens = 100 * nnom / nwords if nwords else 0
    nverd = "heavy" if dens > NOMINAL_PER_100 else "ok"
    out.append(f"**Nominalization density (Williams):** {dens:.1f} per 100 words ({nnom}/{nwords}) — {nverd}")

    # monotone runs
    runs = monotone_runs(lens)
    out.append(f"\n**Monotone runs** (≥{RUN_LEN} consecutive sentences within {RUN_BAND} words): {len(runs)}")
    for start, length, band in sorted(runs, key=lambda r: -r[1])[:5]:
        out.append(f"- run of {length} sentences, lengths {band[0]}–{band[1]}w (sentence #{start+1}+)")

    # flat paragraphs
    flat = []
    for i, sl in enumerate(per_para):
        if len(sl) >= 3 and pstdev(sl) < FLAT_PARA_STDEV:
            flat.append((i, [len(WORD.findall(s)) for s in split_sentences(paras[i])], paras[i][:60]))
    out.append(f"\n**Flat paragraphs** (≥3 sentences, low length variation): {len(flat)}")
    for i, sl, prev in flat[:8]:
        out.append(f"- para {i}: lengths {sl} — \"{prev}…\"")

    # run-on sentences
    longs = []
    for p in paras:
        for s in split_sentences(p):
            n = len(WORD.findall(s))
            if n >= LONG_SENTENCE:
                longs.append((n, s[:70]))
    if longs:
        out.append(f"\n**Run-on sentences (≥{LONG_SENTENCE}w):** {len(longs)}")
        for n, prev in sorted(longs, reverse=True)[:5]:
            out.append(f"- {n}w: \"{prev}…\"")

    # proselint
    pl = run_proselint(prose)
    out.append("\n**proselint (Zinsser/Garner/Strunk rules):**")
    if pl is None:
        out.append("- ⚠ proselint not installed (`pip install proselint`).")
    elif "error" in pl:
        out.append(f"- ⚠ proselint error: {pl['error']}")
    elif pl["total"] == 0:
        out.append("- CLEAN — no proselint flags.")
    else:
        out.append(f"- {pl['total']} flags across {len(pl['by_check'])} checks:")
        for check, info in sorted(pl["by_check"].items(), key=lambda x: -x[1]["count"])[:12]:
            out.append(f"  - `{check}` ×{info['count']} — {info['example'][:90]}")
    out.append("")
    return out


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Prose rhythm & craft metrics (Provost/Williams + proselint).")
    ap.add_argument("chapter", help="Path to chapter .qmd")
    args = ap.parse_args()
    path = Path(args.chapter)
    if not path.exists():
        print(f"Not found: {path}", file=sys.stderr); sys.exit(1)
    lines = rhythm_section_lines(path)
    print(f"# Prose rhythm: {path}")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
