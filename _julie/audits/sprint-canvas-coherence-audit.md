# Coherence & Utility Audit: Step-by-Step Frameworks + Sprint Planning Canvas Tie-Back

**Date:** 2026-06-14
**Author:** Jesse Flores + Claude (session)
**Purpose:** Phase-2 reference. Tests whether the book holds together the way EOS does — every chapter delivering a named tool that refers back to one central artifact — so a reader finishes with a usable product, not just understanding.

---

## The standard: how EOS achieves coherence

From *Traction* Ch. 1 (ProHQ transcript `6a2ee2c6c72d897f5`). EOS coherence rests on **three structural properties**, repeated in every component chapter:

1. **One named tool per chapter.** Vision → V/TO; People → People Analyzer + Accountability Chart + GWC; Data → Scorecard; Issues → Issues List + IDS; Process → Process Documenter; Traction → Rocks + Level 10 Meeting.
2. **A concrete end-capability.** Each chapter closes on "by the end of this chapter you will be able to *do* X" — stated in parallel structure across chapters.
3. **Two spine artifacts everything refers back to:** the **V/TO** (the plan) and the **Organizational Checkup** (the recurring 20-question assessment, re-scored every 90 days).

### Compound's analogs (already chosen)

| EOS | Compound |
|---|---|
| V/TO (the plan) | **Sprint Planning Canvas** (the eight questions) |
| Organizational Checkup (the assessment) | **AI Readiness Scorecard** (Ch 1, 20 questions) |
| Component chapter → one tool | Stage chapter → one tool (Constraint Statement, Knowledge Map, etc.) |

The test: **does every chapter deliver a named tool, tie back to a specific Canvas section, and close on a usable artifact?**

---

## The matrix (state as of 2026-06-14)

| # | Chapter | Named step-by-step tool | Canvas tie-back | Closing structure |
|---|---|---|---|---|
| 1 | Diagnosis | ✅ AI Readiness Scorecard | ⚠️ ties to *Scorecard*, not Canvas | ✅ 6 action steps + reflection |
| 2 | **Beliefs** | ❌ none (mindset chapter) | ❌ none | ❌ **none** |
| 3 | Co-Operating Model | ⚠️ The Equation (*concept*, not a do-tool) | ❌ none | ✅ 3 action + reflection |
| 4 | Framework | ✅ **Sprint Planning Canvas** | ✅ defines it | ✅ |
| 5 | Signal | ✅ Constraint Statement (+ Five Constraint Questions, Five Whys) | ✅ Constraint row | ✅ |
| 6 | Source | ✅ Knowledge Map (+ PIS) | ✅ Source row | ✅ |
| 7 | Designing the System | ✅ Hybrid Accountability Chart + Right Seat Evaluation | ✅ Design row | ✅ |
| 8 | Designing the Work | ✅ Work Deconstruction (TML) + Design Brief + **Design Gate (checklist)** | ✅ Design row | ✅ |
| 9 | Build | ✅ Build Spec | ✅ Build row | ✅ |
| 10 | Deliver | ⚠️ per-role runbook (weak as a *named* artifact) | ✅ Deliver row | ✅ |
| 11 | Compound | ✅ Sprint Retrospective + Signal Backlog | ✅ Compound row | ✅ |
| 12 | Rhythm | ✅ Compounding Scorecard + Hybrid Org Today | ✅ Quarterly review | ✅ |

*(Chapter numbers reflect the post-Beliefs ordering; renumbering sweep `.29` still pending.)*

**Headline: the spine is ~80% built.** Stage chapters 5–12 hit all three axes. The Canvas tie-back is the EOS pattern done correctly — each stage states "this chapter fills in the [X] row of your Sprint Planning Canvas." That work is done and consistent.

---

## The four real gaps

### Gap 1 — Ch 2 Beliefs has none of the three axes
No named tool, no Canvas tie, no closing structure. The only chapter missing all three. Mindset chapters can legitimately skip a "do-tool" (cf. EOS "Letting Go of the Vine"), but it still needs a closing artifact and at least a forward-pointer to the Canvas. **Coordinate with bead `.23` (the chapter is mid-draft).**

### Gap 2 — No visible "tool map" (biggest *utility* gap)
EOS Ch 1 previews every component's tool + end-capability in one parallel pass, so the reader sees the system before walking it. Compound makes the reader *discover* the tool↔Canvas mapping chapter by chapter. The spine is coherent but **invisible.** Highest-leverage add: a single "what each chapter hands you, and the Canvas section it fills" table, placed in the Framework chapter.

### Gap 3 — The two spine artifacts are never related on the page
Scorecard = *where you are*; Canvas = *the plan*. EOS explicitly pairs Organizational Checkup ↔ V/TO and re-scores the checkup every 90 days. The book never states how the Scorecard feeds the Canvas (or how it's re-run over the Rhythm). Make the relationship explicit.

### Gap 4 — The closing device isn't uniform
Most chapters close on Reflection Questions; only Designing-the-Work closes on a named fillable **checklist** (the Design Gate). If "closing checklist / fillable artifact per chapter" is the standard (per `.24`/`.27`), only one chapter currently models it. Decide: does every chapter end with a fillable artifact in addition to reflection questions?

---

## Reframed scope for bead `.24`

`.24` is **not** "build the spine" — the spine largely exists. It is "**make the existing spine visible and uniform**":

- **(a) Add the tool map** — one-glance table in the Framework chapter: chapter → named tool → Canvas section it fills → end-capability.
- **(b) Standardize the In-Brief device** — every chapter's "In Brief" names its *tool + Canvas section + end-capability* in parallel structure (the EOS preview move).
- **(c) Decide the closing standard** — fillable checklist per chapter (overlaps `.27` coaching-ready artifacts) vs. reflection questions only.
- **(d) Close the front-matter gaps** — Beliefs + Co-Op Model need forward-pointers / closing artifacts (coordinate with `.23`, `.28`).
- **(e) Relate the two spines** — one passage (likely Framework or Rhythm) pairing Scorecard ↔ Canvas.

---

## Method notes
- Canvas tie-back counted via `grep "Sprint Planning Canvas"` per chapter (1 structured reference in each stage chapter; 9 in Framework where it's defined; 0 in pre-framework chapters).
- Named tools mapped from `appendix-glossary.qmd` "First introduced: Chapter N" lines.
- Closing structure counted via `## Reflection Questions` + `## Action Step` callouts per chapter.
