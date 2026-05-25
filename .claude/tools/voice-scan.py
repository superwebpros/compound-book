#!/usr/bin/env python3
"""
voice-scan.py — hybrid voice scanner for the Compound book.

Pipeline:
  1. Subprocess vale --output=JSON for deterministic per-paragraph and chapter-level checks
     (em-dash density, antithesis patterns, missing contractions, paragraph length,
      forbidden vocab, inflated symbolism, recap rituals, book-as-location, etc.)
  2. Parse the chapter into prose paragraphs (skip code blocks, callouts, tables).
  3. Cross-paragraph deterministic: n-gram phrase repetition (≥5-word overlap,
     non-adjacent paragraphs).
  4. Cross-paragraph semantic: OpenAI text-embedding-3-small + cosine similarity
     (threshold 0.85). Graceful fallback if OPENAI_API_KEY missing.
  5. Output a unified Markdown report at .claude/output/voice-scan-<chapter>.md.

Usage:
  python3 .claude/tools/voice-scan.py chapters/01-diagnosis.qmd

Reads OPENAI_API_KEY from .claude/.env (gitignored) or from process env.

See: _julie/voice-charter.md, .vale/styles/Compound/*.yml
"""

import sys
import os
import re
import json
import math
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ENV_FILE = REPO_ROOT / ".claude" / ".env"
OUTPUT_DIR = REPO_ROOT / ".claude" / "output"
NGRAM_SIZE = 5
SIMILARITY_THRESHOLD = 0.85
EMBED_MODEL = "text-embedding-3-small"


def load_env() -> dict:
    env = dict(os.environ)
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            env.setdefault(k.strip(), v.strip())
    return env


def split_paragraphs(chapter_text: str) -> list:
    """Return list of dicts: {idx, start_line, end_line, text}.
    Skips code blocks (```...```), callouts (:::...:::), tables (| ... |),
    headings, and blockquote-only lines."""
    lines = chapter_text.splitlines()
    paragraphs = []
    buf = []
    buf_start = None
    in_code = False
    in_callout = False

    def flush():
        nonlocal buf, buf_start
        if buf:
            text = " ".join(buf).strip()
            if text:
                paragraphs.append({
                    "idx": len(paragraphs),
                    "start_line": buf_start,
                    "end_line": buf_start + len(buf) - 1,
                    "text": text,
                })
        buf = []
        buf_start = None

    for i, raw in enumerate(lines, start=1):
        line = raw.rstrip()
        if line.startswith("```"):
            flush()
            in_code = not in_code
            continue
        if line.startswith(":::"):
            flush()
            in_callout = not in_callout
            continue
        if in_code or in_callout:
            continue
        if not line.strip():
            flush()
            continue
        # Skip headings, tables, blockquote-only, list items
        stripped = line.strip()
        if stripped.startswith("#"):
            flush()
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            flush()
            continue
        if stripped.startswith(">"):
            flush()
            continue
        if stripped.startswith("- ") or stripped.startswith("* ") or re.match(r"^\d+\.", stripped):
            flush()
            continue

        if buf_start is None:
            buf_start = i
        buf.append(stripped)

    flush()
    return paragraphs


def line_to_paragraph(paragraphs: list, line: int):
    """Return the paragraph dict containing the given line number, or None."""
    for p in paragraphs:
        if p["start_line"] <= line <= p["end_line"]:
            return p
    return None


def run_vale(chapter_path: Path) -> dict:
    """Run vale --output=JSON and parse."""
    try:
        result = subprocess.run(
            ["vale", "--output=JSON", str(chapter_path)],
            capture_output=True, text=True, cwd=str(REPO_ROOT),
        )
    except FileNotFoundError:
        return {"error": "vale not installed (brew install vale)"}

    if not result.stdout:
        return {}
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": f"vale JSON parse failed: {result.stdout[:200]}"}
    if not data:
        return {}
    # vale wraps results under filename
    key = next(iter(data))
    return {"alerts": data[key]}


def find_ngram_repetition(paragraphs: list, n: int = NGRAM_SIZE) -> list:
    """Return list of (idx_a, idx_b, shared_ngram_text) tuples for non-adjacent
    paragraphs that share an n-gram of length n or more."""
    def words(text):
        return re.findall(r"[A-Za-z']+", text.lower())

    def ngrams(tokens, n):
        return {tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)}

    sets = [ngrams(words(p["text"]), n) for p in paragraphs]
    findings = []
    for i in range(len(paragraphs)):
        for j in range(i + 2, len(paragraphs)):  # skip adjacent
            shared = sets[i] & sets[j]
            if shared:
                # Pick the longest shared sequence
                example = " ".join(next(iter(shared)))
                findings.append({
                    "para_a": i,
                    "para_b": j,
                    "line_a": paragraphs[i]["start_line"],
                    "line_b": paragraphs[j]["start_line"],
                    "shared_phrase": example,
                    "shared_count": len(shared),
                })
    return findings


def embed_paragraphs(paragraphs: list, api_key: str) -> list:
    """Call OpenAI embeddings API. Returns list of vectors or None on failure."""
    texts = [p["text"] for p in paragraphs]
    payload = json.dumps({"input": texts, "model": EMBED_MODEL}).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/embeddings",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read())
        return [d["embedding"] for d in data["data"]]
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "ignore")
        sys.stderr.write(f"OpenAI HTTPError {e.code}: {body[:300]}\n")
        return None
    except Exception as e:
        sys.stderr.write(f"OpenAI embedding error: {e}\n")
        return None


def cosine(a: list, b: list) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def find_semantic_redundancy(paragraphs: list, vectors: list, threshold: float = SIMILARITY_THRESHOLD) -> list:
    """Return list of (idx_a, idx_b, similarity) for non-adjacent paragraphs above threshold."""
    findings = []
    n = len(vectors)
    for i in range(n):
        for j in range(i + 2, n):
            sim = cosine(vectors[i], vectors[j])
            if sim >= threshold:
                findings.append({
                    "para_a": i,
                    "para_b": j,
                    "line_a": paragraphs[i]["start_line"],
                    "line_b": paragraphs[j]["start_line"],
                    "similarity": round(sim, 3),
                })
    return findings


def build_report(chapter_path: Path, paragraphs: list, vale_result: dict,
                 ngram_findings: list, semantic_findings: list,
                 embeddings_used: bool) -> str:
    out = []
    out.append(f"# Voice Scan: {chapter_path}\n")
    out.append(f"**Paragraphs scanned:** {len(paragraphs)}\n")

    # Vale alerts
    alerts = vale_result.get("alerts", [])
    by_rule = defaultdict(list)
    for a in alerts:
        by_rule[a["Check"]].append(a)

    out.append(f"**Vale alerts:** {len(alerts)} total")
    if "error" in vale_result:
        out.append(f"⚠ Vale error: {vale_result['error']}\n")

    out.append("\n## Vale flags by rule\n")
    if not alerts:
        out.append("CLEAN — no Vale flags.\n")
    else:
        for rule, items in sorted(by_rule.items(), key=lambda kv: -len(kv[1])):
            out.append(f"\n### {rule} ({len(items)} occurrences)\n")
            for a in items[:20]:  # cap per rule to avoid runaway
                out.append(f"- Line {a['Line']}, col {a['Span'][0]}: `{a.get('Match','')[:60]}` — {a['Severity']}: {a['Message'][:140]}")
            if len(items) > 20:
                out.append(f"- ... {len(items) - 20} more")

    # N-gram repetition
    out.append(f"\n## Cross-paragraph n-gram repetition ({len(ngram_findings)} findings, n={NGRAM_SIZE})\n")
    if not ngram_findings:
        out.append("CLEAN — no exact-phrase repetition across non-adjacent paragraphs.\n")
    else:
        # Group by paragraph pair, dedupe noise
        for f in sorted(ngram_findings, key=lambda x: -x["shared_count"])[:30]:
            out.append(f"- Para {f['para_a']} (L{f['line_a']}) ↔ Para {f['para_b']} (L{f['line_b']}): `{f['shared_phrase']}` ({f['shared_count']} shared {NGRAM_SIZE}-grams)")
        if len(ngram_findings) > 30:
            out.append(f"- ... {len(ngram_findings) - 30} more")

    # Semantic redundancy
    out.append(f"\n## Cross-paragraph semantic similarity (threshold {SIMILARITY_THRESHOLD})\n")
    if not embeddings_used:
        out.append("⚠ Skipped — OPENAI_API_KEY missing or embeddings failed. Set the key in .claude/.env to enable.\n")
    elif not semantic_findings:
        out.append("CLEAN — no paragraph pairs above similarity threshold.\n")
    else:
        for f in sorted(semantic_findings, key=lambda x: -x["similarity"])[:30]:
            out.append(f"- Para {f['para_a']} (L{f['line_a']}) ↔ Para {f['para_b']} (L{f['line_b']}): cosine = {f['similarity']}")
        if len(semantic_findings) > 30:
            out.append(f"- ... {len(semantic_findings) - 30} more")

    # Paragraph index for the LLM judgment layer
    out.append("\n## Paragraph index (for downstream LLM judgment scan)\n")
    out.append("Patterns deterministic can't catch — pass these paragraph indices to the voice-scanner agent for A1/A2/A4/A5/A12/A13/A14/A15 judgment:\n")
    flagged_para_ids = set()
    for a in alerts:
        p = line_to_paragraph(paragraphs, a["Line"])
        if p:
            flagged_para_ids.add(p["idx"])
    for f in ngram_findings:
        flagged_para_ids.add(f["para_a"])
        flagged_para_ids.add(f["para_b"])
    for f in semantic_findings:
        flagged_para_ids.add(f["para_a"])
        flagged_para_ids.add(f["para_b"])
    if flagged_para_ids:
        out.append(f"\nParagraphs with any flag: {sorted(flagged_para_ids)}")
    out.append(f"\n**LLM scan priority:** all flagged paragraphs above. The LLM scanner should judge whether each carries A1/A2/A4/A5/A12/A13/A14/A15 issues that deterministic scanning can't catch.")

    return "\n".join(out) + "\n"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 .claude/tools/voice-scan.py <chapter.qmd>", file=sys.stderr)
        sys.exit(1)

    chapter_path = Path(sys.argv[1])
    if not chapter_path.is_absolute():
        chapter_path = REPO_ROOT / chapter_path
    if not chapter_path.exists():
        print(f"Chapter not found: {chapter_path}", file=sys.stderr)
        sys.exit(1)

    env = load_env()
    text = chapter_path.read_text()
    paragraphs = split_paragraphs(text)

    # Layer 1: Vale
    vale_result = run_vale(chapter_path)

    # Layer 2: n-gram repetition
    ngram_findings = find_ngram_repetition(paragraphs)

    # Layer 3: semantic similarity
    api_key = env.get("OPENAI_API_KEY")
    semantic_findings = []
    embeddings_used = False
    if api_key and paragraphs:
        vectors = embed_paragraphs(paragraphs, api_key)
        if vectors:
            embeddings_used = True
            semantic_findings = find_semantic_redundancy(paragraphs, vectors)

    # Layer 4: report
    report = build_report(chapter_path, paragraphs, vale_result, ngram_findings,
                          semantic_findings, embeddings_used)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_name = f"voice-scan-{chapter_path.stem}.md"
    out_path = OUTPUT_DIR / out_name
    out_path.write_text(report)
    print(f"Report: {out_path}")
    print(f"Paragraphs: {len(paragraphs)} | Vale alerts: {len(vale_result.get('alerts', []))} | N-gram findings: {len(ngram_findings)} | Semantic findings: {len(semantic_findings) if embeddings_used else 'skipped'}")


if __name__ == "__main__":
    main()
