# Ch 4 (The Framework) — Outline v2 (re-calibrate to orienting altitude)

**Source file:** `chapters/03-the-framework.qmd` · **Branch:** edits/fine-tuning
**Problem:** an orienting chapter that deep-dives each stage instead of scaffolding. Same altitude error the author flagged on the Co-Operating Model chapter.

---

## Thesis / job of this chapter

This chapter is the reader's **map and compass**. It gives them two things and nothing more:
1. **The roadmap** — the six-stage Sequence (Signal → Source → Design → Build → Deliver → Compound), at altitude: what each stage *does* and the *one artifact* it produces. One short beat per stage, not a deep treatment.
2. **The guiding tool** — the **Sprint Planning Canvas**, the book's through-line artifact (its V/TO equivalent). The reader meets the tool, sees the eight questions mapped to the stages, and sees one *completed* example (Meridian). They do NOT complete their own yet — they can't, they lack the tools. The rest of the book fills it in, row by row.

By the end, the reader can name the six stages in order, knows the Canvas is the artifact every later chapter fills, and understands *why the order matters* (each stage feeds the next). Depth lives in the six stage-chapters.

Builds on Ch 3: the Co-Operating Model is what you're building; the Framework is how you build it, one Sprint at a time.

---

## The core reframes (from the author's notes)

- **Scaffold before detail.** Introduce the six stages as a concise roadmap. Cut the per-stage deep dives (the "why it matters / what it produces in full / after X these three things change" treatment) and the per-stage Meridian artifacts (Constraint Statement text, Knowledge Map contents, HAC details, Build Spec, runbooks). Those belong to the stage chapters. Each stage here = ~1–2 sentences: what it does + the artifact it produces + which chapter teaches it.
- **The Canvas is fill-it-as-you-go, not fill-it-now.** Drop "fill in your own now" and "took thirty minutes." Reframe: you'll answer one row per stage as you read; by the last page you'll have a complete Canvas. Meridian's example is what theirs looked like **after** running the process (a finished artifact to aim at), not a first-pass guess.
- **Don't over-direct the tool.** EOS just hands you the V/TO. Give the Canvas (diagram + a download pointer once the file exists); cut "copy this table into a doc/spreadsheet/whiteboard" and the "format doesn't matter much" paragraph.
- **Assume the throughline.** No "Remember Meridian Manufacturing?" — just use it.
- **Fix the specific snags:**
  - Heading "build pays the cost" → reword (awkward).
  - "Jesse ran into this directly… two steps upstream" → make concrete or cut (unclear referent).
  - "Most teams build for the wrong constraint / loudest complaint" → reframe: the move is to build against a *constraint* found by digging beneath a symptom; the loudest complaint isn't a constraint at all. Don't assert most teams build "for the wrong constraint."
  - Diagnose/Execute "two groups" → **Phases** (author's term).
  - "Diagnose is harder to commit to: the output is a piece of paper" → cut/replace; abstract ≠ harder to commit. The honest point: Diagnose is more abstract and takes more thought, and it's where the leverage is.

---

## Section outline (proposed)

> Legend: [KEEP] · [COMPRESS] keep idea, cut length · [NEW] · [CUT] · [REFRAME]

### I. In Brief [REWRITE]
By the end you'll know the six-stage Sequence and the Sprint Planning Canvas — the one-page tool the rest of the book fills in. Drop "you'll have a completed Canvas."

### II. Hook — the "just build it" CEO *(L8–14)* [KEEP, light trim]
Strong orienting hook; lands "you can't start at Build." Keep.

### III. Why the order matters — diagnose before you build *(L16–22)* [COMPRESS + fix notes]
- Reword the heading (no "build pays the cost").
- Keep the dependency chain (each stage produces what the next needs).
- Fix the vague "Jesse ran into this" line (concrete or cut).
- Keep "skip the first two stages and you're buying a tool; run all six and you're changing how the work is owned."

### IV. Four words callout: Framework / Sequence / Sprint / Rhythm *(L24–34)* [KEEP]
Good scaffolding vocabulary. Keep.

### V. The six stages — the roadmap *(L36–106)* [COMPRESS HARD]
- Keep the Sequence diagram (`ch03-the-sequence`).
- Each stage → one tight beat: what it does + the artifact it produces + the chapter that teaches it. Roughly:
  - **Signal** — name and price the constraint → *Constraint Statement*.
  - **Source** — map what the org knows about it → *Knowledge Map*.
  - **Design** — split the work human/agent → *Hybrid Accountability Chart + Design Brief*.
  - **Build** — ship the working system → *Build Spec + Guardrails*.
  - **Deliver** — land it in how work actually gets done → *runbook + Delivery Test*.
  - **Compound** — turn the Sprint into infrastructure → *Sprint Outcome Record + re-ranked queue*.
- Fold in the symptom-vs-constraint idea once, at Signal, reframed per the note (build against a constraint found beneath a symptom; "quoting takes too long" = symptom, "one person holds the pricing logic" = constraint).
- Keep EOS bridges where they're one-liners (Signal↔IDS deeper root-cause; HAC↔Accountability Chart). Cut the per-stage "after X, three things change" lists.
- CUT the per-stage Meridian artifacts (they reappear, appropriately, only in the completed Canvas example).

### VI. The two Phases: Diagnose / Execute & Compound *(L108–119)* [COMPRESS + fix]
- Call them **Phases**. Diagnose = Signal + Source; Execute & Compound = Design + Build + Deliver + Compound.
- Fix the "harder to commit / piece of paper" line. Keep the real point: Diagnose is the abstract, higher-thought half where the leverage is, and the half most teams skip. Keep the information-process-failure-is-invisible point (it's good).
- Keep the diagram + the "when a Sprint stalls in Build, go back to Signal/Source/Design" Pro Tip.

### VII. The Sprint Planning Canvas — the guiding tool *(L121–175)* [REFRAME]
- Introduce it as the book's through-line artifact: one page, eight questions, each previewing a stage and pointing to the chapter that teaches it.
- Show the eight questions mapped to stages (keep) + the blank Canvas diagram.
- CUT the over-direction ("copy this table into a doc…") and the "format doesn't matter much" paragraph. Replace with a download pointer (once the downloadable exists — TODO/bead).
- Keep the three operating fixtures (sponsor, Orchestrator, review date) — but tighten.
- Keep "a Sprint is bounded by scope, not calendar" (good guardrail against scope creep).
- **Decision needed:** the registered `sprint-planning-canvas` moves block ("How to fill in the Canvas") — reframe to a question→chapter map, or keep as-is, or relocate? (It's odd to give a "how to fill it in now" when the book is what fills it in.)

### VIII. Meridian's completed Canvas — the worked example *(L177–210)* [REFRAME → completed, excalidraw]
- Reframe as what Meridian's Canvas looked like **after** they ran the full process — the finished artifact to aim at. Not a "first-pass guess," not "thirty minutes."
- No "Remember Meridian?" — just use it.
- Render as an **excalidraw** (author note), not an inline markdown table. File a diagram bead.
- Cut the "format doesn't matter / thirty minutes" trailing paragraphs.

### IX. Fill in your own — REFRAME *(L212–227)* [REFRAME]
- Don't ask the reader to complete their own now (they lack the tools). Instead: start a blank Canvas if you want, but the real work is that each chapter ahead teaches you one row; by the end you'll have a complete one. Keep the question→chapter mapping (Signal teaches Q1, etc.) — that's the useful orientation.
- Reframe or drop the "Fill in a Sprint Planning Canvas for your company" Action Step accordingly.

### X. Run one Sprint, then another *(L229–233)* [KEEP, tighten]
Rhythm preview: the Canvas + the Sequence run on a cadence; each Sprint cheaper than the last.

### XI. Begin at Signal *(L235–237)* [KEEP] — handoff.

### XII. Reflection Questions *(L239–245)* [REVISE]
Reframe Q2 (don't ask them to "fill in the Canvas for your top constraint right now" — they can't yet). Keep the diagnostic-half question and the Orchestrator question. Pitch at recognition/orientation, not execution.

---

## Diagram impact
- **KEEP** `ch03-the-sequence`, `ch03-diagnose-execute-split`, `ch03-Sprint-planning-canvas-blank`.
- **NEW/CONVERT:** Meridian's completed Canvas → excalidraw (`ch03-Sprint-planning-canvas` exists as a shortcode but currently the inline markdown table is the real content; make the excalidraw the canonical completed example). File a diagram bead.
- Verify the blank-Canvas and completed-Canvas excalidraw files exist and render (some shortcodes are referenced; confirm the files are real, not placeholders).

## Open decisions for the author
- **A. Phases naming** — "Diagnose" and "Execute & Compound" as the two **Phases**? (author suggested Phases). Confirm.
- **B. Stage-depth altitude** — compress each of the six to ~1–2 sentences (what it does + artifact + teaching chapter), cutting the deep per-stage treatment and per-stage Meridian. Confirm this is the right altitude.
- **C. The Canvas as fill-as-you-go** — drop "fill it in now," present Meridian's as the *completed* example, reframe the close to "the book fills it in." Confirm.
- **D. The `sprint-planning-canvas` moves block** — keep / reframe to a question→chapter map / relocate?
- **E. Download link** — we don't have a downloadable Canvas file yet. Point to a download (placeholder + bead), or just show the diagram for now?
- **F. Meridian completed Canvas as excalidraw** — confirm (and it's the one place deep Meridian detail stays).

## Notes
- The deep per-stage content being cut is owned by the six stage-chapters already; verify they cover it (likely yes), so nothing is lost. No holding doc needed (unlike the Co-Op Model design instruments).
- Voice/house rules unchanged; full gate + judgment trio after drafting.
