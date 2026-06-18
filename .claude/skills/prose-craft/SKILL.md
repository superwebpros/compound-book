---
name: prose-craft
description: "Evaluate a book chapter (or the whole book) for clarity, simplicity, and pacing — the craft layer, distinct from voice. Runs the rhythm/craft scan (Provost sentence-variation, Williams nominalization, proselint) then the prose-craft judgment agent, producing a flag report with line numbers and direction. Use when prose feels weak, dense, repetitive, or badly paced, or as a quality gate before author review. Report-only — flags, does not rewrite."
---

# Prose-Craft Review

Standardizes the "is the writing actually good" judgment the way the voice charter standardizes voice.
Grounded in Zinsser / Williams / Provost / Clark and calibrated against *Traction*.

**Voice vs. craft:** voice = "does it sound like us" (use the voice-scanner). Craft = "is it clear,
simple, well-paced" (this skill). North star: **simplify** — the audience is a smart but non-technical
entrepreneur.

## Canonical references (read before judging)
- `_julie/prose-craft-charter.md` — the spec: calibrated Traction targets + the seven rules.
- Memory `book-chapter-flow-and-meridian-thread` — chapter flow (hook→concept→how-to→example) + simplify mandate.

## How to run it

### One chapter
1. Run the scan (it now includes the rhythm/craft section):
   ```bash
   /usr/bin/python3 .claude/tools/voice-scan.py chapters/<NN>-<slug>.qmd
   ```
2. Spawn the `prose-craft` agent (Agent tool, `subagent_type: prose-craft`) pointed at that chapter.
   It reads `.claude/output/voice-scan-<stem>.md` + the chapter, applies the seven rules, and writes
   `.claude/output/prose-craft-<stem>.md`. **Report-only.**
3. Relay the verdict + prioritized fixes. Hand the report to a `voice-implementer` only if the user
   asks for the fixes to be made.

### Whole book (sweep)
Fan out: one `prose-craft` agent per chapter (a Workflow `parallel`/`pipeline` is ideal), then a
synthesis pass that ranks systemic craft issues across chapters (recurring restatement, abstraction
hotspots, pacing offenders) into a backlog. Mirror the ARC / flow-pacing read-throughs.

## The one rule that governs everything
**Metrics-assisted judgment, never a metric gate.** The deterministic layer will pass a weak chapter
(proven on Ch 1: CV 0.67, proselint clean, prose still weak). Numbers find candidates; the agent
decides. Don't pass/fail on a number.

## Standalone tooling (no agent needed)
- `prose_rhythm.py chapters/<file>.qmd` — rhythm/craft metrics for one chapter.
- Recalibrate targets: re-run `/tmp/traction_rhythm.py` (or the equivalent) against the reference text
  and update the bands in `prose-craft-charter.md` + the constants in `prose_rhythm.py`.

## Dependencies
`pip install proselint textstat` (used by the scan). The rhythm layer degrades gracefully if missing.
