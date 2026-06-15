# JF R3 Phase 3 — Master Plan & Locked Decisions

**Date:** 2026-06-15
**Status:** Ready to dispatch after Phase 3A outlines are written + reviewed
**Branch:** `merge-julie-feedback`
**Last commit before this plan:** see `git log --oneline -5`

This document captures everything decided in the Phase 3 triage session. It is meant to survive context compaction. If a fresh orchestrator picks this up, read this file in full + the linked audit files before doing anything.

## Read these first (in order)

1. This file (master plan, locked decisions, dispatch order)
2. `_julie/audits/AUTHORING-TEAM-BRIEF.md` — the reading-team consolidated brief (5 cross-cutting + per-chapter punch list)
3. `_julie/audits/arc-synthesis.md` — ARC prospect read-through with author annotations
4. `_julie/audits/flow-pacing-synthesis.md` — internal flow vs canonical template
5. `_julie/audits/opening-arc-six-hats/OPTION-C-OUTLINES.md` — locked Author-Revised Option C structure + 4-belief decisions + SPC 8-question through-line
6. `/Users/jesseflores/.claude/projects/-Users-jesseflores-compound-sites-compound-book/memory/` — all memory entries (deflourish discipline, etc.)

## Locked decisions (do not relitigate)

### Chapter structure & numbering

- **4-chapter opening arc (Author-Revised Option C, 2026-06-14):** Ch 1 Diagnosis → Ch 2 (new mindset chapter) → Ch 3 Co-Operating Model → Ch 4 Framework. Downstream chapters all renumbered +1.
- **Mindset chapter retitle (NEW 2026-06-15):** *"You're Already a Tech Company"* (NOT "The Four Beliefs"). Belief 1 (system company) anchors the chapter; the other three beliefs cascade from it. This is the equivalent of Traction's "Letting Go of the Vine." Bead `book-zsrx`.
- **Sprint Planning Canvas with 8 questions = master through-line artifact.** Every chapter populates 1-2 questions on the Canvas. The Canvas is the coaching-engagement master worksheet.
- **Meridian is the deliberate through-line.** Never cut Meridian for "redundancy." Front chapters that lack Meridian get it woven in (FLOW#3).
- **Headcount Paradox ownership (locked 2026-06-14):** Ch 1 Diagnosis OWNS the definition. Beliefs/Compound/Rhythm/What-to-Do-Next call back to it; they don't redefine. Framed as operating-problem-first, AI-as-accelerator-second. Both Jesse's (SuperWebPros, AI-era) and Julie's (global food safety, pre-AI) examples illustrate the same principle at different scales.

### Chapter naming convention (NEW 2026-06-15)

**Pattern:** Traction-style — descriptive title + colon + one-sentence main idea.

Traction reference examples:
- "Chapter 1: The Entrepreneurial Operating System: Strengthening the Six Key Components"
- "Chapter 2: Letting Go of the Vine"
- "Chapter 3: The Vision Component: Do They See What You Are Saying?"
- "Chapter 4: The People Component: Surround Yourself With Good People"
- "Chapter 5: The Data Component: Safety in Numbers"

**Apply to all chapters** during Phase 3C — rewrite chapter titles to this pattern.

### Heading convention (NEW 2026-06-15)

**Headings must be directive.** Not just labels. Traction examples of subheadings:
- "Building a True Leadership Team"
- "Hitting the Ceiling Is Inevitable"
- "Simplify, Delegate, Predict, Systemize, Structure"
- "You Can Only Run Your Business On One Operating System"
- "You Must Be Open Minded, Growth Oriented, And Vulnerable"

**Strip numericals from headings.** No "§3.5 Sprint Planning Canvas" — use directive language instead.

### HBR / source citation discipline (NEW 2026-06-15)

**Author critique:** "In our rewrite of the earlier chapters, we also leaned a lot more on the Harvard Business Review than I think we needed to. Having a reference or two is fine, but we built one of the chapters almost completely around it."

**Specifically the new Ch 2 Beliefs over-cites Argenti/Sadun/Bedard/AWS.** Trim HBR citations to **1-2 maximum per chapter**. Use them as occasional reinforcement, not as scaffolding.

This affects:
- **Ch 2 Beliefs** — most over-cited (Argenti banker opener + Sadun + Bedard + AWS). Keep the banker scene; trim the others to 1-2 supporting references.
- **Ch 1 Diagnosis** — Sadun polarization line + (already-cut) AWS/Effectual stat. Sadun still in; verify it's not over-leaned.
- **Ch 6 Source** — Argenti + Sadun + AWS cited in three-layer frame opener. Trim.
- **Ch 7 Design / Ch 7b Design Work** — Bedard 3-agent ceiling cited multiple times. Already compressed to cross-references in EC cleanup (commit 614ca87); preserve.

### AI Tier framework (locked 2026-06-15)

The case studies (Meridian + PM Agent Team) use a 3-tier classification (Tier 1 / Tier 2 / Tier 3 / Not AI-tier) in their Knowledge Map tables. Ch 6 Source has a different "AI tiers" section at L127 with three tiers named (standing context / retrieved / historical).

**Decision:** revise Ch 6 to match the case studies' Tier 1/2/3 terminology. Case studies stay as-is. Ch 6 Source adopts:
- **Tier 1** — AI can use directly (structured, API-accessible)
- **Tier 2** — AI can process with extraction pipeline (unstructured but capturable)
- **Tier 3** — Human judgment required (not AI-accessible)
- **Not AI-tier** — stays human, queried in real time (ephemeral, judgment-bound)

Verify against actual case-study usage in `chapters/case-study-meridian.qmd` L141-150 and `chapters/case-study-pm-agent-team.qmd` L76-86.

### Case studies are independent reference material (locked 2026-06-15)

Case studies (Meridian + PM Agent Team) do NOT need reflection questions, reader handoffs, or "do this now" action steps. They are independent — like appendices.

**ARC#4 (book-9cdf) is closed** for this reason.

**Author scope direction:** "I'm only interested in feedback in the core chapters."

When reading-team analyses score case studies as Risk/Fail on Get-Moving, set aside.

### Orchestrator ≠ Integrator (locked 2026-06-15)

- **Orchestrator** (Compound): Sprint-level role, person managing agents.
- **Integrator** (EOS/Traction): full-company-level role, runs day-to-day across Sales/Marketing, Operations, Finance/Admin. Sometimes COO, sometimes VP of Operations. EOS-specific term.
- The Integrator might BE the Orchestrator for some Sprints, but they are not equivalent.

Cross-chapter disambiguation sweep: `book-8v6v.32` (ARC#13). Includes one-paragraph disambiguation block at Human Orchestrator's formal definition site.

### Not strictly an EOS book

EOS terms appear where operator-familiar (Accountability Chart, Scorecard, L10, Rocks). The book is NOT mapping every Compound concept to an EOS equivalent. ARC#6 (`book-g404`) was rescoped to: "EOS terms used where operator-familiar — NOT as equivalence claims."

### Time-budget guidance: stripped (R2 author preference)

R2 F59/F90/F92 stripped all procedural time estimates ("90 minutes," "two weeks for most teams"). ARC#9 (facilitation/session scaffolding) keeps "who's in the room" — DROP the time-budget half.

### Deflourish is non-negotiable

See `memory/deflourish-is-non-negotiable.md`. Run `.claude/tools/deflourish.py --apply` on every chapter the orchestrator touches in this pass. EC and deflourish are complementary, not alternatives.

### Flesch + paragraph pacing targets — set AFTER the pass

The author wants to set Flesch and paragraph-pacing targets AFTER Phase 3 lands, not as Drafter brief inputs. Phase 3A outlines should NOT specify target numbers.

## Phase 3 staged approach

### Phase 3A — Editorial outlines (orchestrator-direct, before any drafting)

Write a one-page outline per chapter that captures (without rewriting):

- **New chapter title** (Traction-style — descriptive + colon + main idea)
- **Opening hook/story** — REFERENCE existing content by line range; do not rewrite
- **Concept & context** — REFERENCE the existing 1-2 paragraphs that frame the chapter's claim; flag the AI-bridge framing if missing
- **How-to** — REFERENCE the existing steps/procedure/exercise; flag if it arrives too late in the chapter
- **Artifacts** — list named artifacts + fillable status + location (in-body table / Excalidraw / appendix)
- **Closing handoff** — single sentence to next chapter
- **Headings inventory** — list current H2/H3 headings + propose directive rewrites (no numericals)
- **Beads applying to this chapter** — with notes on which are addressed by 3B cross-cutting sweeps vs which are chapter-specific

**The outline is reorganization guidance, not a rewrite.** Author note: "We don't need to start from scratch. We've got a lot. It's just that we need to reorganize it in a way that's easier to read and make it more actionable."

Save outlines to `_julie/audits/phase3-outlines/ch-XX-<name>.md`.

Author reviews and annotates outlines before any drafting begins.

### Phase 3B — Cross-cutting sweeps (parallel, before per-chapter)

Run these as parallel Drafter agents. They touch many chapters; doing them once prevents per-chapter Drafters from re-solving the same problem 10 ways.

| Bead | Scope | Drafter model |
|---|---|---|
| `book-tb8h` ARC#1 | Fix broken/circular cross-references (renumbering fallout my `.29` sweep missed) | Sonnet |
| `book-ultm` ARC#2 | Define "agent" plainly + standard "agent vs ChatGPT" line on first use per chapter | Sonnet |
| `book-xqxi` ARC#3 | Glossary/jargon pass (RAG, API, n8n, system prompt, tokens, ontologies, embeddings, chunking, etc.) + builder/decider partition in technical chapters | Sonnet |
| `book-g404` ARC#6 (rescoped) | EOS terms used where operator-familiar — NOT as equivalence claims; remove false Compound→EOS mappings | Sonnet |
| `book-8v6v.32` ARC#13 | Orchestrator vs Integrator disambiguation + one-paragraph distinction block | Sonnet |
| NEW consolidated artifact bead | Merge ARC#5 + `.27` + ARC#12 → one bead with three workstreams: (a) embed in-body fillable templates for named artifacts (SPC, HOT, Signal Backlog, Design Brief, Constraint Statement, HAC rows, mini-spec, AI Tier categories); (b) SPC as master through-line; (c) replace Excalidraw-only templates + "compound.co/resources when launches" hedge | Opus |

### Phase 3C — Per-chapter Drafters (priority order)

Each Drafter gets the Phase 3A outline + chapter-specific beads + the locked-decision list above as universal constraints.

Priority order:

1. **BELIEFS retitle (`book-zsrx`)** — retitle "You're Already a Tech Company"; restructure around Belief 1 as primary identity; demote other 3 beliefs to "other shifts"; **trim HBR citations to 1-2 max**; Meridian sentence per FLOW#3; Headcount Paradox callback only.
2. **Ch 6 Source** — FLOW#2 simplicity rescue (cut/merge KM sections; PIS → 1 sentence; resequence vocab) + AI Tier framework reconciliation (adopt Tier 1/2/3 terminology from case studies) + trim HBR citations.
3. **Ch 5 Signal** — ARC#7 (AI bridge framing AT THE OPENING per author hypothesis: introduce in concept/context section, walk constraint finder, transition) + ARC#9 (who's-in-the-room only, NO time budget) + ARC#8 missing Action Steps.
4. **Ch 7 Designing the System** — FLOW#1 (how-to earlier; pull first action earlier) + ARC#8 (HAC draft Action Step) + readability tightening.
5. **Ch 7b Designing the Work** — FLOW#1 (how-to earlier) + ARC#8 (Design Brief Action Step — central artifact has no "do this now") + readability.
6. **Ch 8 Build** — FLOW#1 (how-to earlier) + readability.
7. **Ch 1 Diagnosis** — ARC#10 (mechanize scorecard math + tiebreakers; fold dimension-subtotal step into scoring table before bucket descriptions; add interim dimension-prioritization tiebreaker so no number is left blank). **Light touch — Ch 1 already tightened in commit 8a6af0f + deflourish.**
8. **Ch 11 Compound / Ch 12 Rhythm / Ch 13 What to Do Next** — FLOW#5 trim outros/dumps/over-caps + FLOW#4 Headcount callbacks (not retreads).
9. **Ch 3 Co-Operating Model** — ARC#8 gut-check as written artifact (if not already addressed in 3B).

### Phase 3D — Final pass

- Deflourish (`.claude/tools/deflourish.py --apply`) on every chapter touched in Phase 3B or 3C — NON-NEGOTIABLE.
- Render verify (`quarto render` per chapter; full book render to verify all chapters land in TOC).
- Run `paragraph-stats.py` across Preface + first 4 chapters + all touched chapters; surface results.
- PDF regen.
- Send PDF to author.

## Bead inventory (Phase 3 active set, post-triage)

### Group A — Clear-to-dispatch (cross-cutting + chapter-specific) 

| Bead | Status | Phase |
|---|---|---|
| `book-tb8h` ARC#1 cross-refs | open | 3B |
| `book-ultm` ARC#2 agent definition | open | 3B |
| `book-xqxi` ARC#3 jargon glossary | open | 3B |
| `book-g404` ARC#6 (rescoped) | open | 3B |
| `book-8v6v.32` ARC#13 Orchestrator/Integrator | open | 3B |
| `book-rhko` ARC#5 fillable templates | open (TO BE MERGED) | 3B |
| `book-8v6v.27` coaching artifact audit | open (TO BE MERGED) | 3B |
| `book-b4do` ARC#12 Excalidraw-only replacement | open (TO BE MERGED) | 3B |
| `book-zsrx` BELIEFS retitle | open | 3C #1 |
| `book-3w1t` FLOW#2 Source simplicity | open | 3C #2 |
| `book-chf3` ARC#7 coined terms + AI bridge | open | 3C #3 (Signal) |
| `book-i91z` ARC#9 facilitation (who's-in-room only) | open | 3C #3 (Signal) |
| `book-lbd7` ARC#8 missing Action Steps | open | 3C #3-#5 + #9 |
| `book-0fq9` FLOW#1 lead with practice | open | 3C #4-#6 |
| `book-68zp` ARC#10 scorecard math | open | 3C #7 |
| `book-o81e` FLOW#5 trim outros | open | 3C #8 |
| `book-bco3` FLOW#4 Headcount retread | open | 3C #8 (callback verification) |
| `book-b8yy` FLOW#3 Meridian weave front chapters | open | 3C #1, #2, #8 |
| `book-8v6v.24` Structural-anchor pass | open | absorbed by 3A outlines + 3C |
| `book-n628` ARC#11 AI Tier inline definition | open | 3C #2 (Ch 6 reconciliation does this) |

### Closed in this triage session

| Bead | Why |
|---|---|
| `book-9cdf` ARC#4 case study activation | Case studies are independent reference material; do not need reflection/handoff. |

## Open questions remaining

1. **Phase 3A outline depth** — how detailed should outlines be? Current proposal: 1 page per chapter, references existing content by line range, doesn't rewrite. Author confirmation needed.

2. **Drafter model choice** — most Phase 3B + 3C work is suitable for Sonnet. The consolidated artifact bead and the BELIEFS retitle might benefit from Opus. Default to Sonnet unless the brief specifies otherwise.

3. **Chapter rename application** — Traction-style chapter titles (descriptive + colon + main idea) get applied as part of Phase 3C per-chapter Drafter passes. Each Drafter proposes new title in the brief; orchestrator collects and proposes the full list to author before any rename commits.

4. **Headings strip-numericals pass** — bundle with Phase 3C per-chapter Drafters OR run as a separate orchestrator-direct mechanical sweep at the end of Phase 3C, before 3D?

## Compaction recovery instructions

If picking this up after compaction:

1. Read this file in full.
2. Run `git log --oneline -20` to see what's been committed.
3. Check `bd list --status open --json` for active beads under `book-8v6v`.
4. Resume at Phase 3A (write the per-chapter outlines) unless work has already started there.
5. Memory entries to load:
   - `memory/deflourish-is-non-negotiable.md`
   - Any new memory entries created post-this-plan (HBR citation discipline, directive headings, Traction-style chapter naming)
6. Coordinate with author before dispatching Phase 3C (per-chapter Drafters) — author should review Phase 3A outlines first.
