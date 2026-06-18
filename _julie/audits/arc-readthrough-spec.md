# ARC Read-Through — Spec (Phase-2 Exit Gate)

**Status:** Defined, not yet run. Runs as the **phase-2 exit gate**, after the structural beads land
(`.19` Framework, `.20` Diagnosis, `.23` Beliefs, `.28` Co-Op Model, `.29` renumbering) and final
chapter numbering is stable.
**Mode:** Report-only. No edits. Findings → `_julie/audits/arc-findings-<chapter>.md` + one synthesis file.
**Date defined:** 2026-06-14

> **ARC = prospect-lens read team.** (Jesse to confirm whether "ARC" stands for something specific —
> e.g., Adoption / Readability / Clarity — and it'll be folded into the rubric framing.)

---

## Why this gate exists

The book can be internally coherent (see `sprint-canvas-coherence-audit.md`) and still fail the only
test that matters commercially: **can a real prospect read it and start moving?** ARC reads the whole
book through one set of eyes — the ideal customer — and reports whether the book clears three bars.

## The reader persona

A **smart but non-technical entrepreneur**: CEO/owner of a 25–100 person company, frequently running
EOS or a similar operating system. Time-poor, outcome-driven, skeptical of AI hype. Not a developer.
Evaluating whether they could actually *do* this in their business — not just whether it's interesting.
(Use the existing `ideal-customer-reader` agent.)

## The rubric — three bars, scored per chapter

Each reader scores every chapter **Pass / Risk / Fail** on each axis, with **specific quoted evidence**
(line references) and the **single highest-impact fix**.

### A — Clarity for a non-technical (but smart) entrepreneur
- Could they follow it without a technical background?
- Jargon walls, undefined terms, coined-term-before-stakes, concept-before-payoff.
- "So what?" moments — passages that don't connect to their business.

### B — Can they ask/answer the right questions to get moving?
- Does the chapter hand them the *questions* they need to ask of their own business?
- Can they actually *answer* enough of them from what the chapter gives — i.e., does it produce
  forward motion, not just comprehension?
- Is the next action unambiguous when they finish?

### C — Can they recognize the helpful artifacts/tools to complete implementation?
- Is the chapter's named tool/artifact obvious and findable?
- Do they understand what it *produces* and what to *do* with it?
- Could they leave the chapter and actually fill the artifact in / run the tool?

## Team structure (Workflow)

Pipeline over the canonical chapter list (`_quarto.yml`, post-renumbering):

1. **Read stage** — one `ideal-customer-reader` per chapter → structured A/B/C verdict
   (schema: `{chapter, A:{score,evidence,topFix}, B:{...}, C:{...}, overall, mustFix[]}`).
2. **Synthesis stage** — one agent over all verdicts → systemic patterns:
   - recurring jargon / undefined terms across chapters (cross-chapter glossary gaps)
   - repeated "so what?" failure modes
   - chapters where a prospect would stall (B-axis fails)
   - artifacts that aren't recognizable as artifacts (C-axis fails)
   - a single **ranked fix backlog** (highest reader-impact first), each mapped to a chapter + bead.

## Output
- `_julie/audits/arc-findings-<chapter>.md` per chapter (or one combined file).
- `_julie/audits/arc-synthesis.md` — systemic patterns + ranked fix backlog.
- Fix backlog items become phase-3 beads under the epic.

## Run conditions (do not run before all true)
- [ ] `.19` Framework restructure landed
- [ ] `.20` Diagnosis repositioning landed
- [ ] `.23` Beliefs chapter drafted (has tool/closing/forward-pointer per coherence audit)
- [ ] `.28` Co-Op Model restructure landed
- [ ] `.29` renumbering sweep landed (chapter numbers + cross-refs stable)
- [ ] Coherence-audit Gap 1–4 fixes (`.24`) at least attempted, so ARC tests the intended structure
