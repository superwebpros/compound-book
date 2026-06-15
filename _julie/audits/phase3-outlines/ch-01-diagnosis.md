# Phase 3A Outline — Ch 1 (Diagnosis)

**Source file:** `chapters/01-diagnosis.qmd`
**Priority:** 3C #7 (LIGHT TOUCH — already tightened in commit 8a6af0f + deflourish 2b437ab)
**Beads:** `book-68zp` (ARC#10 scorecard math — mechanize scorecard math + tiebreakers; fold dimension-subtotal step into scoring table before bucket descriptions; add interim dimension-prioritization tiebreaker so no number is left blank), `book-tb8h` (ARC#1 cross-refs — handled 3B), `book-ultm` (ARC#2 agent definition — handled 3B; chapter currently has "agent defined earlier" at L110 referencing forward).
**Status:** Light restructure only. Chapter is in good shape after Phase 1 tightening. Primary remaining work: scorecard math mechanization + dimension-subtotal step placement + tiebreaker. Headcount Paradox already owned correctly. HBR already trimmed to one Sadun reference at L25.

## New chapter title (proposed)

**"Diagnosis: Score Your Operating Model Against the AI Divide"**

*(Current title "The diagnosis." Add main-idea clause per Traction pattern. Alternative: "Diagnosis: It's an Operating Problem, Not a Technology Problem" — picks up the chapter's most repeated claim. Either works.)*

## Chapter shape — current vs. proposed

### Current (good after Ch 1 tightening pass)
1. In-Brief (L3-7).
2. Opener: discovery call, three tools, one company (L9-15).
3. "The diagnosis is the operating model" (L17-33).
4. "You've already tried" (L35-47).
5. **The Headcount Paradox** (L49-92) — owned correctly here. Both Jesse and Julie examples.
6. "It looks like a technology problem. It's actually an operating problem." (L94-124).
7. "The wrong question" (L126-146).
8. **Where you actually stand — AI Readiness Scorecard** (L148-301).
   - 5 dimensions, 20 questions, scoring math, bucket descriptions, closing checklist.
9. "Before we hand you the system, there are four things you have to be willing to believe" (L303) — handoff to Ch 2.
10. Reflection Questions (L305+).

**Problems the reading team flagged (ARC#10):**
- **Scorecard math mechanization.** Currently the reader scores 20 questions but the "Score yourself" section at L263-272 jumps directly to bucket descriptions. The dimension-subtotal step at L284 ("Add the four rankings inside each dimension") is BURIED below the bucket descriptions. Reader is told the bucket, then told to compute dimensions. Wrong order.
- **No tiebreaker between dimensions.** If two dimensions tie for lowest, the chapter says "the dimension with the lowest subtotal is where the chapters ahead start" but doesn't say what to do with ties. Reader leaves with a blank.

### Proposed (surgical)

1. **In-Brief** — Keep L3-7.
2. **Opener** — Keep L9-15.
3. **"The diagnosis is the operating model"** — Keep L17-33.
4. **"You've already tried"** — Keep L35-47.
5. **The Headcount Paradox** — Keep L49-92. This chapter owns it; Beliefs/Compound/Rhythm/What-to-Do-Next call back only.
6. **"It looks like a technology problem. It's actually an operating problem."** — Keep L94-124.
7. **"The wrong question"** — Keep L126-146.
8. **AI Readiness Scorecard — REORGANIZE scoring math (ARC#10).** Keep L148-261 (intro, two preconditions framing, 5 dimensions, 20 questions). Then reorganize the scoring section:
   - **Move dimension-subtotal computation UP** — before the bucket descriptions. The reader should compute dimension subtotals as part of completing the scorecard, not as an afterthought.
   - **Then compute total** — current L265-272 math stays.
   - **Then bucket reading** — current L276-284 table stays.
   - **Add tiebreaker** — between subtotal computation and bucket reading: *"If two dimensions tie for lowest, start with the one Chapter 5 names first in the Sequence: Constraint Clarity → Information Readiness → Workflow Visibility → Decision Rights → Measurement Discipline. The order matters because each dimension unlocks the next."* That's the interim tiebreaker so no reader is left blank.
9. **Closing checklist** — Keep L286-295. The four-line write-down is already strong.
10. **"Before we hand you the system, there are four things you have to be willing to believe"** — Keep L303. Tighten the handoff to Ch 2's new title: *"Four things have to be true for the framework to hold — Chapter 2 names them."* (Or with the Traction-style retitle of Ch 2: *"Chapter 2 makes the case that you're already a tech company; three other shifts follow."*)
11. **Reflection Questions** — Keep L305-311. Already 5 questions; consider trimming to 4.

## Concept & context — AI bridge

Already strong. AI explicit throughout, agent vs. chatbot bridge at L107-114. The "agent defined earlier" cross-reference at L110 — wait, L110 says "agents — the kind defined earlier." Cross-cutting `book-ultm` (ARC#2 standard agent definition) sweep will handle adding a plain-English definition on first use. Drafter should not touch.

## How-to — arrival timing

Action Steps appear throughout (L117 — write down scorecard answer; L173-177 — leadership-team poll; L201-204 — workflow handoff; L219-223 — whiteboard workflow; L239-242 — decision rule list; L257-260 — cost math). Good distribution. No timing fix needed.

## Artifacts

| Artifact | Status | Location |
|---|---|---|
| Headcount before/after | Excalidraw L90 | Keep. |
| Wrong vs. Right Question | Excalidraw L146 | Keep. |
| AI Readiness Scorecard (5 dims × 4 Qs) | In-body tables L166-253 | Keep. Best in-body artifact in the chapter. |
| Scoring math (count × multiplier) | In-body table L267-270 | Reorganize per ARC#10 (above). |
| Bucket descriptions | In-body table L276-284 | Keep. |
| Closing 4-line checklist | In-body callout L286-295 | Keep. |

## Closing handoff

L303 currently reads: *"Before we hand you the system, there are four things you have to be willing to believe."* This is the handoff to the old Ch 2 "Four Beliefs" title. With the new Ch 2 title ("You're Already a Tech Company"), revise to: *"Before the framework holds, you have to be convinced you're already a tech company. Chapter 2 makes the case."*

## Headings inventory

### Current (mostly italic-fragment style)
- L1 `# The *diagnosis*.` (H1)
- L17 `## The diagnosis is the *operating model*.` (H2)
- L35 `## You've already *tried*.` (H2)
- L49 `## The Headcount *Paradox*.` (H2)
- L71 `### How the math finally moves.` (H3)
- L94 `## It looks like a *technology* problem. It's actually an *operating* problem.` (H2)
- L126 `## The wrong *question*.` (H2)
- L148 `## Where you actually *stand*.` (H2)
- L162 `### Dimension 1: Constraint Clarity` (H3)
- L187 `### Dimension 2: Information Readiness` (H3)
- L206 `### Dimension 3: Workflow Visibility` (H3)
- L225 `### Dimension 4: Decision Rights` (H3)
- L244 `### Dimension 5: Measurement Discipline` (H3)
- L263 `### Score yourself.` (H3)
- L274 `### Read your bucket.` (H3)

### Proposed (directive)
- H1: `# Diagnosis: It's an Operating Problem, Not a Technology Problem`
- H2: `## The Diagnosis Is the Operating Model`
- H2: `## You've Already Tried` *(keep — the bluntness is the point)*
- H2: `## The Headcount Paradox`
  - H3: `### Redesign the Operating Model Before You Staff It`
- H2: `## It Looks Like a Technology Problem. It's Actually an Operating Problem.`
- H2: `## Ask the Right Question. The Wrong One Produces Scattered Pilots.`
- H2: `## Score Your AI Readiness`
  - H3: `### Dimension 1 — Constraint Clarity`
  - H3: `### Dimension 2 — Information Readiness`
  - H3: `### Dimension 3 — Workflow Visibility`
  - H3: `### Dimension 4 — Decision Rights`
  - H3: `### Dimension 5 — Measurement Discipline`
  - H3: `### Compute Your Dimension Subtotals` *(promoted from buried position)*
  - H3: `### Compute Your Total and Read the Bucket`
  - H3: `### If Two Dimensions Tie, Use the Sequence Order` *(NEW — the tiebreaker)*
- H2: `## Reflection Questions`

## HBR citation discipline

**Current count:** One — Sadun polarization warning at L25. **At the cap. Keep.**

## Meridian weave

Currently zero Meridian in this chapter. Flagged as FLOW#3 candidate (`book-b8yy` — Meridian weave front chapters). Add ONE concrete Meridian sentence in the scorecard section, illustrating what a mid-range bucket score looks like for Meridian. Suggested insertion: in the bucket descriptions, add a sentence like *"Meridian's leadership team scored in the 35-49% bucket on their first read — foundations present, math not yet compounding."* Brief, illustrative, doesn't bloat.

## Time-budget strip (ARC#9)

No procedural time-budget language detected. Keep.

## Notes for the Drafter

- **Drafter model:** Sonnet (light surgical work).
- This chapter has had two recent passes (Ch 1 tightening 8a6af0f + deflourish 2b437ab). Do NOT re-edit prose that's already been tightened.
- Focus narrowly on:
  1. Reorganize the scoring section (dimension subtotal → tiebreaker → bucket reading).
  2. Add the tiebreaker rule (one-paragraph).
  3. Update the Ch 2 handoff at L303 to match the new "Tech Company" title.
  4. Add one Meridian sentence to the scorecard section.
  5. Convert italic-fragment headings to directive language.
- Voice charter applies. No new em-dashes. The prose is already well-tuned.
- Run deflourish.py --apply after drafting (mandatory, even on light-touch chapters).
- ARC#1 cross-reference sweep handles "Chapter 5" / "Chapter 7" links in 3B.
