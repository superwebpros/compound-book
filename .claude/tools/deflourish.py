#!/usr/bin/env python3
"""
deflourish.py — paragraph-level flourish detector + de-flourish reviser for the Compound book.

WHY THIS EXISTS
  Voice flourish (cute/clever framing, patronizing setups, false precision) is a
  generation-time behavior the model regresses to when it's *authoring* a business-book
  chapter. Post-hoc charter scanners catch the countable tells (em-dashes, forbidden
  words) but not the judgment classes, because the LLM judge shares the generator's taste.
  This tool turns the gain down at EDIT time, the only place it reliably drops:
    - small context per call (one paragraph) -> the constraint dominates attention
    - editing register, not authoring -> the genre pull is absent
    - an explicit hostile-peer-reader model -> the flourish reads as the flaw it is

PIPELINE (per prose paragraph, in chapter order)
  Stage 0  deterministic (free): em-dash density + antithesis regex (ported from
           .vale/styles/Compound/{EmDashDensity,Antithesis}.yml)
  Stage 1  classifier (CLASSIFIER_MODEL): an adversarial-CEO performance detector.
           Runs on every prose paragraph. Returns clean | flagged + constructions.
  GATE     a paragraph is flagged if Stage 0 OR Stage 1 flags it. Clean paragraphs
           are passed through untouched (protects the voice you already like).
  Stage 2  editor (EDITOR_MODEL): in-place de-flourish of flagged paragraphs only,
           given the previous + next paragraph as FROZEN read-only context and a note
           of which coined terms are first introduced here (so a definition isn't cut).

WHAT IT TOUCHES
  Plain prose paragraphs only. Headings, YAML frontmatter, fenced code, `:::` callout
  interiors (Action Steps / Pro Tips / In Brief), `{{< shortcodes >}}`, tables, block
  quotes, and lists are passed through verbatim. Callout interiors are deliberately
  skipped — their tone is owned by the editorial-coherence agent.

OUTPUT
  Dry-run (default): writes a review report to .claude/output/deflourish-<stem>.md with
  every flagged paragraph's original, the flags, and the proposed revision. The chapter
  file is NOT modified.
  --apply: additionally rewrites flagged paragraphs in the chapter file in place, so the
  diff is reviewable with `git diff`. Nothing is auto-committed.

USAGE
  /usr/bin/python3 .claude/tools/deflourish.py chapters/04-signal.qmd            # dry run -> report
  /usr/bin/python3 .claude/tools/deflourish.py chapters/04-signal.qmd --apply    # rewrite in place
  /usr/bin/python3 .claude/tools/deflourish.py chapters/04-signal.qmd --parse-only  # show segmentation, no API
  /usr/bin/python3 .claude/tools/deflourish.py chapters/04-signal.qmd --max-paragraphs 5  # cap (debugging)

REQUIRES
  ANTHROPIC_API_KEY in .claude/.env (gitignored) or the process environment. The script
  fails with a clear message if it's missing (except under --parse-only, which needs no key).

MODEL CHOICE (see constants below)
  Classifier defaults to Sonnet (high-volume, fast, strong judgment); editor defaults to
  Opus (the rewrite needs capability to cut cleanly without flattening). Haiku is
  deliberately NOT used for the editor — context-free or low-capability rewriting
  re-introduces tells. Both are top-of-file constants; change them if you prefer.

See: _julie/voice-charter.md, .vale/styles/Compound/*.yml
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ENV_FILE = REPO_ROOT / ".claude" / ".env"
OUTPUT_DIR = REPO_ROOT / ".claude" / "output"

API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"

# --- Models ----------------------------------------------------------------
# Classifier runs on EVERY prose paragraph (high volume) -> Sonnet keeps cost/latency sane.
# Editor runs only on flagged paragraphs -> Opus, because the rewrite is where capability
# matters and where a weak model flattens prose into beige or invents new flourish.
CLASSIFIER_MODEL = "claude-sonnet-4-6"
EDITOR_MODEL = "claude-opus-4-8"
CLASSIFIER_EFFORT = "medium"
EDITOR_EFFORT = "high"
# --------------------------------------------------------------------------

# Coined terms whose FIRST appearance in a chapter may carry a definition the editor
# must not cut. Distinctive multi-word terms only — common words (Build, Design, Compound)
# are excluded to avoid noise.
COINED_TERMS = [
    "Co-Intelligent Co-Operation", "Co-Operating Model", "Co-Intelligence",
    "Co-Intelligent Company", "Compound Bench", "Constraint Statement",
    "Hybrid Accountability Chart", "Hybrid Org Today", "Sprint Planning Canvas",
    "Headcount Paradox", "Clarity Call", "Is/Is Not", "Five Whys",
    "Human Orchestrator", "Agent Coordinator", "Deploy Readiness", "Build Spec",
]

# Antithesis patterns ported verbatim from .vale/styles/Compound/Antithesis.yml
ANTITHESIS_PATTERNS = [
    r"It's not [a-z]+\. It's [a-z]+",
    r"It is not [a-z]+\. It is [a-z]+",
    r"[A-Z][a-z]+ isn't [a-z]+\. (?:It's|That's) [a-z]+",
    r"Not [a-z]+(?: [a-z]+){0,3} — [a-z]+(?: [a-z]+){0,3}",
    r"That's not [a-z]+(?: [a-z]+){0,3}\. That's [a-z]+",
    r"The (?:problem|issue|real problem|real issue) (?:isn't|is not)",
]
ANTITHESIS_RE = [re.compile(p) for p in ANTITHESIS_PATTERNS]
EM_DASH = "—"

# Shared voice spec inlined into both prompts (the API call can't read the charter file).
VOICE_SPEC = """\
The book's voice is operator-to-operator: a CEO talking to a peer CEO. Declarative,
unhedged, specific, mechanical/structural. Numbers are load-bearing. Stories are
first-person and embedded. The reader is a smart, busy operator — never lectured,
never flattered, never performed at.

"Flourish" is language reaching for effect over plain operator clarity. Three classes:

  1. CUTE / CLEVER / PERFORMING-INSIGHT — reframing the reader's own words for effect
     ("'our quoting is slow' is not a sentence, it's a complaint"); setup-then-reveal
     beats; pop-culture cleverness; cute section teasers ("Design opens the group for a
     reason"); arbitrary rules dressed as wisdom ("if it takes more than one breath to
     read aloud, it's too long").
  2. PATRONIZING / CONDESCENDING — telling a peer CEO what they already know;
     caricaturing them ("most leadership teams argue for whichever was loudest in the
     room"); hand-holding; belittling ("the AI tool they buy is a toy").
  3. FALSE PRECISION / OVERCLAIMING / AI-SMELL — absolute claims that are oversimplified
     or wrong; semantic dodges ("they weren't eliminated, they were redesigned out of
     existence"); inflated symbolism ("stands as a testament to"); hedged, abstract,
     evidence-free sentences.

Plus countable tells: an em-dash used as a rhetorical reveal; antithesis ("not X — Y",
"It isn't X. It's Y."); triplet pileups ("The pattern is mechanical. The diagnosis is
mechanical. The fix is mechanical."); -ing tag closers ("...ensuring better outcomes");
conjunctive-adverb pileup (however/moreover/furthermore); recap rituals ("In summary...").

THE VOICE FLOOR — never strip, this is the value the reader buys:
  specific numbers and dollar figures; names of people/companies/artifacts; the embedded
  first-person story; the declarative claim itself; the Sequence arrow (Signal → Source
  → ...); markdown emphasis (*word*); contractions.
"""

CLASSIFIER_SYSTEM = """\
You are a skeptical CEO reading a business book a peer wrote for you. You find being
explained-to, performed-at, or flattered insulting, and you have no patience for cleverness
that exists to make the writer look smart. You are NOT the author and you are not precious
about any sentence.

""" + VOICE_SPEC + """

Read ONE paragraph and judge it as a whole construction — not sentence by sentence. Decide
whether it contains flourish (any of the three classes or the countable tells above). Plain,
direct, specific operator prose is CLEAN even if it is plain — do not flag good writing for
being unadorned. Only flag genuine performance.

Respond with the JSON object only."""

EDITOR_SYSTEM = """\
You are revising existing prose in an operator-to-operator business book. You are an EDITOR,
not an author. You are not writing a chapter — you are de-performing one paragraph that a
reviewer flagged for flourish. Recast it as the plainest, most direct version a skeptical
peer CEO would respect.

""" + VOICE_SPEC + """

RULES:
  - Preserve every claim, number, name, and specific, verbatim.
  - Preserve markdown emphasis (*word*), the Sequence arrow (→), and contractions.
  - You MAY delete spans that carry no claim (pure performance — a clever reframe, a
    setup-for-a-reveal, an empty flourish). You MAY restructure cadence, and split or join
    sentences. Plainer and clearer is the goal; shorter is not always the goal.
  - Do NOT introduce any new flourish, metaphor, antithesis, or clever turn.
  - Do NOT add content, hedges, qualifiers, or transitions the paragraph didn't have.
  - Do NOT redefine or cut a coined-term definition if the note says the term is first
    introduced here.
  - If the paragraph is already plain and direct, return it UNCHANGED.

Output ONLY the revised paragraph text. No preamble, no quotation marks, no commentary,
no explanation of what you changed."""

CLASSIFIER_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": ["clean", "flagged"]},
        "constructions": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "cute-clever", "patronizing", "false-precision-overclaim",
                    "antithesis", "triplet-pileup", "ing-tag-closer",
                    "conjunctive-adverb-pileup", "recap-ritual", "inflated-symbolism",
                    "em-dash-reveal", "ai-smell",
                ],
            },
        },
        "reason": {"type": "string"},
    },
    "required": ["verdict", "constructions", "reason"],
    "additionalProperties": False,
}


# --------------------------------------------------------------------------
# env + API
# --------------------------------------------------------------------------
def load_api_key():
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return key.strip()
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("ANTHROPIC_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def call_anthropic(api_key, model, system, user, *, effort, max_tokens, schema=None):
    output_config = {"effort": effort}
    if schema is not None:
        output_config["format"] = {"type": "json_schema", "schema": schema}
    body = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system,
        "thinking": {"type": "adaptive"},
        "output_config": output_config,
        "messages": [{"role": "user", "content": user}],
    }
    data = json.dumps(body).encode("utf-8")
    headers = {
        "content-type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": ANTHROPIC_VERSION,
    }
    delay = 2.0
    last_err = None
    for attempt in range(5):
        req = urllib.request.Request(API_URL, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            stop = payload.get("stop_reason")
            if stop == "refusal":
                raise RuntimeError("model refused the request (stop_reason=refusal)")
            text = "".join(
                b.get("text", "") for b in payload.get("content", []) if b.get("type") == "text"
            ).strip()
            return text
        except urllib.error.HTTPError as e:
            code = e.code
            last_err = e
            if code in (429, 500, 503, 529):
                time.sleep(delay)
                delay *= 2
                continue
            detail = ""
            try:
                detail = e.read().decode("utf-8")
            except Exception:
                pass
            raise RuntimeError(f"HTTP {code} from Anthropic API: {detail[:500]}") from e
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = e
            time.sleep(delay)
            delay *= 2
            continue
    raise RuntimeError(f"Anthropic API failed after retries: {last_err}")


# --------------------------------------------------------------------------
# parsing: .qmd -> ordered segments (passthrough | prose)
# --------------------------------------------------------------------------
LIST_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)")


def is_structural_line(stripped):
    if not stripped:
        return True  # blank
    if stripped.startswith("#"):
        return True  # heading
    if stripped.startswith("|"):
        return True  # table row
    if stripped.startswith(">"):
        return True  # block quote
    if stripped.startswith("{{<") or stripped.startswith("{{%"):
        return True  # shortcode
    if LIST_RE.match(stripped):
        return True  # list item
    return False


def parse_segments(text):
    """Return (segments, trailing_newline).

    segments: ordered list of dicts.
      passthrough: {"type": "passthrough", "lines": [str, ...]}
      prose:       {"type": "prose", "lines": [str, ...], "start_line": int,
                    "heading": str, "text": str}
    Reconstruction = walk segments in order, emit lines (passthrough) or
    revision-or-text (prose).
    """
    trailing_newline = text.endswith("\n")
    lines = text.split("\n")
    if trailing_newline:
        lines = lines[:-1]  # drop the empty element split() leaves after a trailing \n

    segments = []
    pass_buf = []
    prose_buf = []
    prose_start = None
    prose_heading = None

    in_frontmatter = False
    in_code = False
    div_depth = 0
    current_heading = ""

    def flush_pass():
        if pass_buf:
            segments.append({"type": "passthrough", "lines": list(pass_buf)})
            pass_buf.clear()

    def flush_prose():
        nonlocal prose_start, prose_heading
        if not prose_buf:
            return
        joined = "\n".join(prose_buf)
        # Guard: only treat as prose if it really reads like a sentence.
        if len(joined.strip()) >= 30 and any(c.isalpha() for c in joined) and "." in joined:
            segments.append({
                "type": "prose",
                "lines": list(prose_buf),
                "start_line": prose_start,
                "heading": prose_heading,
                "text": joined,
            })
        else:
            segments.append({"type": "passthrough", "lines": list(prose_buf)})
        prose_buf.clear()
        prose_start = None
        prose_heading = None

    for idx, line in enumerate(lines):
        stripped = line.strip()
        is_prose = False  # decided below

        # 1. frontmatter
        if idx == 0 and stripped == "---":
            in_frontmatter = True
        elif in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
        # 2. fenced code
        elif stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
        elif in_code:
            pass
        # 3. div fences (callouts etc.)
        elif stripped == ":::" or re.match(r"^:::+\s*$", stripped):
            div_depth = max(0, div_depth - 1)
        elif stripped.startswith(":::"):
            div_depth += 1
        elif div_depth > 0:
            pass
        # 4. structure
        elif is_structural_line(stripped):
            if stripped.startswith("#"):
                current_heading = stripped.lstrip("#").strip()
        else:
            is_prose = True

        if is_prose:
            flush_pass()
            if not prose_buf:
                prose_start = idx + 1  # 1-based
                prose_heading = current_heading
            prose_buf.append(line)
        else:
            flush_prose()
            pass_buf.append(line)

    flush_prose()
    flush_pass()
    return segments, trailing_newline


def reconstruct(segments, trailing_newline):
    out = []
    for seg in segments:
        if seg["type"] == "prose" and seg.get("revision") is not None:
            out.append(seg["revision"])
        else:
            out.extend(seg["lines"])
    text = "\n".join(out)
    if trailing_newline:
        text += "\n"
    return text


# --------------------------------------------------------------------------
# deterministic flags
# --------------------------------------------------------------------------
def deterministic_flags(paragraph):
    flags = []
    em = paragraph.count(EM_DASH)
    if em > 1:
        flags.append(f"em-dash density ({em} in paragraph; charter max 1)")
    for rx in ANTITHESIS_RE:
        if rx.search(paragraph):
            flags.append("antithesis construction")
            break
    return flags


def first_introduced_terms(paragraph, seen):
    """Coined terms appearing in this paragraph for the first time in the chapter.
    Mutates `seen`."""
    introduced = []
    for term in COINED_TERMS:
        if term in paragraph:
            if term not in seen:
                introduced.append(term)
            seen.add(term)
    return introduced


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def build_classifier_user(seg, det_flags):
    parts = []
    if seg["heading"]:
        parts.append(f"[Section: {seg['heading']}]")
    if det_flags:
        parts.append("[Deterministic flags already found: " + "; ".join(det_flags) + "]")
    parts.append("Paragraph:\n" + seg["text"])
    return "\n\n".join(parts)


def build_editor_user(seg, prev_text, next_text, det_flags, classifier, introduced):
    parts = []
    if seg["heading"]:
        parts.append(f"[Section: {seg['heading']}]")
    flag_lines = []
    if det_flags:
        flag_lines.extend(det_flags)
    if classifier:
        if classifier.get("constructions"):
            flag_lines.append("constructions: " + ", ".join(classifier["constructions"]))
        if classifier.get("reason"):
            flag_lines.append("reviewer note: " + classifier["reason"])
    if flag_lines:
        parts.append("[Why this was flagged:\n- " + "\n- ".join(flag_lines) + "]")
    if introduced:
        parts.append(
            "[Coined terms FIRST introduced in this paragraph — do not cut their "
            "definition: " + ", ".join(introduced) + "]"
        )
    if prev_text:
        parts.append("[FROZEN previous paragraph — read-only context, DO NOT edit or "
                     "repeat:\n" + prev_text + "]")
    if next_text:
        parts.append("[FROZEN next paragraph — read-only context, DO NOT edit or "
                     "repeat:\n" + next_text + "]")
    parts.append("Revise ONLY this paragraph:\n" + seg["text"])
    return "\n\n".join(parts)


def main():
    ap = argparse.ArgumentParser(description="Paragraph-level flourish detector + de-flourish reviser.")
    ap.add_argument("chapter", help="path to a .qmd chapter")
    ap.add_argument("--apply", action="store_true",
                    help="rewrite flagged paragraphs in the chapter file in place (review with git diff)")
    ap.add_argument("--parse-only", action="store_true",
                    help="print segmentation and exit; no API calls, no key required")
    ap.add_argument("--max-paragraphs", type=int, default=0,
                    help="cap number of prose paragraphs processed (0 = no cap; debugging)")
    args = ap.parse_args()

    chapter_path = Path(args.chapter)
    if not chapter_path.exists():
        print(f"error: chapter not found: {chapter_path}", file=sys.stderr)
        return 2
    text = chapter_path.read_text(encoding="utf-8")
    segments, trailing_newline = parse_segments(text)
    prose_segs = [s for s in segments if s["type"] == "prose"]

    if args.parse_only:
        print(f"{chapter_path.name}: {len(prose_segs)} prose paragraphs "
              f"of {len(segments)} segments")
        for s in prose_segs:
            preview = s["text"][:70].replace("\n", " ")
            print(f"  L{s['start_line']:>4}  [{s['heading'][:28]:<28}]  {preview}")
        return 0

    api_key = load_api_key()
    if not api_key:
        print("error: ANTHROPIC_API_KEY not found.\n"
              "  Add it to .claude/.env (gitignored):  ANTHROPIC_API_KEY=sk-ant-...\n"
              "  or export it in your shell. (Not needed for --parse-only.)", file=sys.stderr)
        return 2

    # Build ordered prose list with frozen neighbors.
    prose_texts = [s["text"] for s in prose_segs]
    seen_terms = set()
    flagged_records = []
    processed = 0

    for i, seg in enumerate(prose_segs):
        if args.max_paragraphs and processed >= args.max_paragraphs:
            break
        processed += 1
        para = seg["text"]
        det = deterministic_flags(para)
        introduced = first_introduced_terms(para, seen_terms)

        # Stage 1: classifier (always — it catches the judgment classes regex can't)
        classifier = None
        try:
            raw = call_anthropic(
                api_key, CLASSIFIER_MODEL, CLASSIFIER_SYSTEM,
                build_classifier_user(seg, det),
                effort=CLASSIFIER_EFFORT, max_tokens=2000, schema=CLASSIFIER_SCHEMA,
            )
            classifier = json.loads(raw)
        except Exception as e:
            print(f"  L{seg['start_line']}: classifier error: {e}", file=sys.stderr)

        flagged = bool(det) or (classifier is not None and classifier.get("verdict") == "flagged")
        status = "FLAG" if flagged else "ok  "
        print(f"  L{seg['start_line']:>4}  {status}  {para[:60].replace(chr(10), ' ')}")
        if not flagged:
            continue

        # Stage 2: editor (flagged only) with frozen neighbors
        prev_text = prose_texts[i - 1] if i > 0 else ""
        next_text = prose_texts[i + 1] if i + 1 < len(prose_texts) else ""
        try:
            revision = call_anthropic(
                api_key, EDITOR_MODEL, EDITOR_SYSTEM,
                build_editor_user(seg, prev_text, next_text, det, classifier, introduced),
                effort=EDITOR_EFFORT, max_tokens=3000,
            )
        except Exception as e:
            print(f"  L{seg['start_line']}: editor error: {e}", file=sys.stderr)
            continue
        if not revision:
            continue
        changed = revision.strip() != para.strip()
        if changed:
            seg["revision"] = revision
        flagged_records.append({
            "line": seg["start_line"],
            "heading": seg["heading"],
            "det": det,
            "classifier": classifier,
            "introduced": introduced,
            "original": para,
            "revision": revision,
            "changed": changed,
        })

    # Report
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = OUTPUT_DIR / f"deflourish-{chapter_path.stem}.md"
    changed_n = sum(1 for r in flagged_records if r["changed"])
    lines = [
        f"# De-flourish: {chapter_path.name}",
        "",
        f"**Classifier:** {CLASSIFIER_MODEL} (effort {CLASSIFIER_EFFORT})  ",
        f"**Editor:** {EDITOR_MODEL} (effort {EDITOR_EFFORT})  ",
        f"**Prose paragraphs scanned:** {processed}  ",
        f"**Flagged:** {len(flagged_records)}  ",
        f"**Proposed changes:** {changed_n}  ",
        f"**Mode:** {'APPLIED in place' if args.apply else 'dry run (report only)'}",
        "",
        "---",
        "",
    ]
    for r in flagged_records:
        lines.append(f"## L{r['line']} — {r['heading'] or '(no heading)'}")
        why = list(r["det"])
        if r["classifier"]:
            if r["classifier"].get("constructions"):
                why.append("constructions: " + ", ".join(r["classifier"]["constructions"]))
            if r["classifier"].get("reason"):
                why.append(r["classifier"]["reason"])
        lines.append("**Why flagged:** " + ("; ".join(why) if why else "(deterministic only)"))
        if r["introduced"]:
            lines.append(f"**First-introduced terms preserved:** {', '.join(r['introduced'])}")
        if not r["changed"]:
            lines.append("**Editor returned the paragraph unchanged** (judged already clean).")
        lines.append("")
        lines.append("**Original:**")
        lines.append("")
        lines.append("> " + r["original"].replace("\n", "\n> "))
        lines.append("")
        lines.append("**Proposed:**")
        lines.append("")
        lines.append("> " + r["revision"].replace("\n", "\n> "))
        lines.append("")
        lines.append("---")
        lines.append("")
    report_path.write_text("\n".join(lines), encoding="utf-8")

    if args.apply and changed_n:
        chapter_path.write_text(reconstruct(segments, trailing_newline), encoding="utf-8")

    print()
    print(f"scanned {processed} prose paragraphs, flagged {len(flagged_records)}, "
          f"{changed_n} with proposed changes")
    print(f"report: {report_path}")
    if args.apply and changed_n:
        print(f"APPLIED to {chapter_path} — review with: git diff {chapter_path}")
    elif args.apply:
        print("nothing changed; chapter file untouched")
    else:
        print("dry run — chapter file untouched. Re-run with --apply to write changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
