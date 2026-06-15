# Phase 3A Outline — Ch 8 (Build)

**Source file:** `chapters/07-build.qmd`
**Priority:** 3C #6
**Beads:** `book-0fq9` (FLOW#1 — relocate Technical Literacy + Agile Concepts AFTER Build Spec Writer; pull first action earlier), `book-tb8h` (ARC#1 cross-refs — handled 3B), `book-xqxi` (ARC#3 jargon — handled 3B; chapter is jargon-heavy by necessity), readability (Flesch 58 — dense; sentence-length tightening needed).
**Status:** Medium restructure. The chapter has a great spec discipline structure (Build Spec Writer + Guardrails Checklist) but the meaty how-to (the 8-section spec) arrives at L166 — about 50% through the chapter — after extensive technical-literacy and Agile-concepts framing. FLOW#1 reorder: lead with the spec, then provide literacy as supporting material.

## New chapter title (proposed)

**"Build: A Locked Spec Becomes a Deployed System in Three Weeks"**

*(Alternative: "Build: If It Feels Slow, the Problem Is Upstream." Picks up the chapter's own thesis at L5.)*

## Chapter shape — current vs. proposed

### Current
1. In-Brief (L3-6).
2. Opener: PM agent team build (L8-14) — strong.
3. Canvas connection (L16).
4. "What Build produces" (L18-28) — the one thing.
5. Build scoped to designed workflow / scope drift / design debt (L30-51).
6. **"Build lives outside IT"** (L53-70) — important reframe.
7. **Technical literacy section** (L72-144) — models, tokens, open source vs proprietary, fine-tuning vs RAG vs context windows, deployment options. Long.
8. **Agile concepts for the rest of us** (L146-164) — Sprint, backlog, QA, accountability.
9. **The two instruments — Build Spec Writer + Guardrails Checklist** (L166-219) — 8-section spec, Meridian populated example. **This is the chapter's core how-to**.
10. **Implementation Mistakes Checklist** (L220-241).
11. **Guardrails Checklist** (L243-266) — 7 questions, Meridian table.
12. **Where the agent lives** (L268-298) — environments + span-of-control.
13. Reflection Questions (end).

**Problems the reading team flagged:**
- **FLOW#1.** Build Spec Writer (the chapter's how-to) at L166 is too late. Reader needs the spec discipline framing earlier; technical literacy and Agile concepts can move to AFTER the spec.
- **Readability — Flesch 58.** Dense technical content. Sentence-length tightening needed throughout the technical-literacy section.
- **Cross-references** — "see Chapter 7" loops at L185, L272, L288, L292 (per `book-tb8h` notes). 3B sweep handles.
- **Span-of-control check repeats** — L286-288 essentially restates Ch 7 and Ch 7b. Should be a single cross-reference, not a re-explanation.

### Proposed

1. **In-Brief** — Keep L3-6. Already does the work.
2. **Opener (PM agent team)** — Keep L8-14.
3. **Canvas connection** — Keep L16.
4. **What Build produces** — Keep L18-28.
5. **Build is scoped to the designed workflow** — Keep L30-51. Scope drift / design debt content stays here.
6. **Build lives outside IT** — Keep L53-70. The first Action Step (L67-70) survives at ~30% through the chapter, which is appropriate.
7. **The two instruments — Build Spec Writer + Guardrails Checklist — PROMOTE.** Move L166-219 to here. The 8-section spec is the chapter's how-to and should arrive while the reader is still oriented to the Build mindset. The Meridian populated spec (L193-211) is the best in-body artifact in the chapter; lead with it.
8. **Implementation Mistakes Checklist** — Keep at L220-241 — flows naturally after the spec.
9. **The Guardrails Checklist** — Keep L243-266. The 7-question Meridian table is excellent.
10. **Where the agent lives — environment options** — Keep L268-298 BUT compress the span-of-control section L286-292 to a single cross-reference to Ch 7. Drafter should not re-explain Bedard's ceiling; just cross-reference.
11. **Technical literacy — DEMOTE.** Move L72-144 to AFTER the environment section. Keep the literacy content (models, tokens, RAG vs fine-tuning vs context window, deployment) but reposition as supporting material the reader can refer to when picking an environment. The Pro Tip at L97-100 (token cost estimate) is great and should stay with the spec section as a callout reference.
12. **Agile concepts — DEMOTE further or COMPRESS.** L146-164 is currently a long detour. Compress to a tight one-paragraph reference: "Sprint, backlog, QA, accountability — language software teams use; in Compound terms, the Compound Sprint is the time box, the spec is the backlog, the Done test is QA, and the HAC supervisor is accountable." That's enough. The full detour can move to a glossary appendix entry.
13. **Reflection Questions** — Keep, trim to 3.

## Concept & context — AI bridge

Strong throughout — this is the most AI-technical chapter. No bridge work needed.

## How-to — arrival timing

Currently the 8-section spec arrives at L166 (~50% through). After FLOW#1 reorder, it arrives at ~35-40% through, right after the "Build lives outside IT" reframe. Better.

First Action Step is already at L67-70 (smart placement).

## Artifacts

| Artifact | Status | Location |
|---|---|---|
| 8-section Build Spec | Prose L176-187 + Excalidraw L187 | Add **in-body fillable template** — this is the chapter's central artifact. |
| Meridian populated Build Spec | In-body prose L195-211 | Excellent. Make heading structure clearer with section-number labels. |
| Implementation Mistakes Checklist | In-body L224-241 | Already a numbered list. Make explicit as fillable audit checklist. |
| Guardrails Checklist (7 Qs) | Excalidraw L247 + in-body table L253-259 | Best in-body artifact in chapter. |
| Environment options table | Prose subsections L276-284 | Add summary table at end of section. |
| Data access / API / RAG decision tree | Excalidraw L124 | Keep. |

## Closing handoff

The chapter ends with the span-of-control Action Step at L296-298 and then jumps to ... no closing handoff sentence to Ch 9 Deliver currently. Add: *"With the spec locked and the guardrails answered, Build executes. Chapter 9 is where the deployed system gets put in front of real work."*

## Headings inventory

### Current
- L1 `# *Build*.` (H1)
- L18 `## What *Build* produces.` (H2)
- L30 `## Build is scoped to the *designed* workflow.` (H2)
- L53 `## Build lives outside IT.` (H2)
- L72 `## Technical literacy — what you need to know.` (H2)
- L79 `### Models and providers.` (H3)
- L87 `### Tokens and pricing.` (H3)
- L102 `### Open source vs. proprietary.` (H3)
- L110 `### Making AI work with your data.` (H3)
- L131 `### Deployment: where the build runs.` (H3)
- L145 `## Agile concepts for the rest of us.` (H2)
- L166 `## The two instruments — *Build Spec Writer* and *Guardrails Checklist*.` (H2)
- L220 `## The Implementation Mistakes Checklist.` (H2)
- L243 `## The *Guardrails Checklist*.` (H2)
- L268 `## Where the *agent* lives.` (H2)
- L286 `### The span-of-control constraint.` (H3)

### Proposed (directive)
- H1: `# Build: A Locked Spec Becomes a Deployed System`
- H2: `## Build Produces One Thing: A Deployed Working System` (was "What Build produces")
- H2: `## Build Is Scoped to the Designed Workflow. Anything Else Is a Different Project.` (was "Build is scoped to the designed workflow")
- H2: `## Build Doesn't Require Developers — Just the Person Closest to the Work` (was "Build lives outside IT")
- H2: `## Write the Eight-Section Build Spec` (was "The two instruments..." — split)
- H2: `## Audit the Spec Against Seven Common Failures` (was "The Implementation Mistakes Checklist")
- H2: `## Answer the Seven Guardrails Questions in Writing` (was "The Guardrails Checklist")
- H2: `## Pick the Environment Inside Design's Category` (was "Where the agent lives")
  - H3: `### Verify Span of Control Before You Pick the Environment` (was "The span-of-control constraint")
- H2: `## Know Enough About Models, Tokens, and Deployment to Hold Your Own` (DEMOTED, was "Technical literacy")
  - H3: `### Models and Providers`
  - H3: `### Tokens and Pricing`
  - H3: `### Open Source vs. Proprietary`
  - H3: `### Making AI Work with Your Data`
  - H3: `### Where the Build Runs` (was "Deployment...")
- H2: `## Agile Vocabulary, in One Paragraph` (DEMOTED + COMPRESSED, was "Agile concepts for the rest of us")
- H2: `## Reflection Questions`

## HBR citation discipline

**Current count:** Zero direct HBR citations in this chapter. Bedard's three-agent ceiling appears at L288 as a cross-reference. Keep as cross-reference.

## Meridian weave

Strong — populated Build Spec is Meridian. No fix needed.

## Time-budget strip (ARC#9)

Scan: "three weeks" (L40), "three and a half weeks" (L209, L211) — these are CONCRETE OUTCOMES, not procedural budgets. Keep — they prove the discipline pays off.

## Notes for the Drafter

- **Drafter model:** Sonnet.
- The largest move: relocate Technical Literacy + Agile Concepts to AFTER the Build Spec sections. The chapter currently buries the how-to behind 70 lines of supporting material. Reorder fixes this.
- Compress Agile Concepts section heavily — currently 19 lines (L146-164); target 5-7 lines as a single paragraph reference.
- Replace span-of-control re-explanation at L286-292 with cross-reference to Ch 7.
- Readability: the Technical Literacy section especially has long sentences. Apply paragraph-stats.py after to verify mean sentence count per paragraph is < 4.
- Voice charter applies. Strip italic-fragment headings. No em-dashes.
- Run deflourish.py --apply after drafting.
- Cross-cutting `book-tb8h` (ARC#1) sweep handles the "see Chapter 7" cross-reference cleanup in 3B; Drafter should not solve.
