---
name: draft-chapter
description: "Assemble the brief and rewrite one book chapter from its Phase 3A outline, reorganizing existing content (not from scratch) under the locked house-rules. Use when drafting/restructuring a chapter of Co-Intelligent Co-Operation, or as the Draft step of the Phase 3C pipeline. Pairs with the drafter agent."
---

# Draft a Chapter

Turns a Phase 3A outline + the existing chapter into a reorganized draft. **Reorganize, don't start
over** — the material is good; the job is structure, clarity, and actionability.

## 1. Assemble the brief (same inputs every time → consistent output)
Gather, in order:
1. **Outline** — `_julie/audits/phase3-outlines/ch-XX-*.md` (chapter syllogism + section plan with
   Assumes/Establishes/Sets-up markers and [NEW]/[CUT]/[MOVE]/[TRIM] tags).
2. **Current chapter** — the `.qmd`.
3. **Chapter beads** — IDs + descriptions (from the dispatch, or `bd show <id>`).
4. **Locked decisions** — `_julie/audits/PHASE3-MASTER-PLAN.md` § "Locked decisions".
5. **Memory house-rules** — `book-chapter-flow-and-meridian-thread`, `beliefs-chapter-identity`,
   `jargon-house-rule`, `eos-positioning`.
6. **Standards** — `_julie/voice-charter.md` (voice), `_julie/prose-craft-charter.md` (craft).

## 2. The constraints (non-negotiable, every chapter)
- **Flow:** hook/story → concept & context → how-to → example. Move the how-to / first action earlier if it lands late.
- **Meridian** = deliberate through-line; weave per the outline, never cut as redundancy.
- **Title:** Traction-style (descriptive + colon + main idea) — propose, don't finalize.
- **Headings:** directive, no numericals.
- **Jargon:** plain-English gloss + forward pointer (named-stage ref, not a bare chapter number) at first use; one canonical "agent vs ChatGPT" line.
- **EOS:** agnostic default; optional familiar-paradigm bridge only.
- **HBR/outside citations:** ≤ 1–2 per chapter.
- **Headcount Paradox:** Ch 1 owns it; others callback only.
- **No time-budgets.** **Don't touch case-study files.** **Don't edit `_quarto.yml`** (propose titles for a collected rename step).
- **Audience:** smart non-technical entrepreneur, often EOS-run, frequently NO in-house engineer / NO ERP — never assume either; always give a no-engineer path.
- North star: **simplify**.

## 3. Output
- Rewritten `.qmd` in place, render-safe (callouts, `{{< excalidraw >}}` shortcodes, tables intact).
- A **Drafter summary** (returned, not written into the chapter): proposed title; section moves/cuts/adds; beads addressed/deferred; judgment calls for the author.

## 4. What this skill does NOT do
The QA gates run AFTER drafting, in the pipeline: `voice-scan.py` (incl. rhythm) → `prose-craft` →
`editorial-coherence` → `ideal-customer-reader` → fix-loop (`voice-implementer` applies clear fixes,
judgment calls surface) → `deflourish.py --apply` (non-negotiable) → render-verify. Do not run them here.

## Heavy chapters
BELIEFS (`book-zsrx`) and Source (`book-3w1t`) are heavy restructures — run a Design-Table
(`substance-lead`/`voice-lead`/`reader-lead`) pass to agree the plan before drafting.
