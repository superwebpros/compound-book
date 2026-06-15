# Phase 3A Outline — Ch 7 (Designing the System)

**Source file:** `chapters/06-designing-the-system.qmd`
**Priority:** 3C #4
**Beads:** `book-0fq9` (FLOW#1 lead with practice — move info-flow before HAC, Human Orchestrator up), `book-lbd7` (ARC#8 HAC draft Action Step), `book-xqxi` (ARC#3 jargon — handled 3B), `book-g404` (ARC#6 EOS terms scoped — handled 3B), `book-8v6v.32` (ARC#13 Orchestrator/Integrator disambig — handled 3B), HBR citation discipline (memory — Bedard + AWS appear here, trim).
**Status:** Medium-to-heavy restructure. Chapter is comprehensive and well-built but front-loads the Hybrid Accountability Chart before the reader sees what information flow even means. The Human Orchestrator definition arrives at ~80% through the chapter despite being the chapter's load-bearing role concept. FLOW#1 reorder is the dominant move.

## New chapter title (proposed)

**"Designing the System: Build the Hybrid Accountability Chart Before You Build Anything Else"**

*(Alternative: "Designing the System: Every Row Has a Name." More confrontational, mirrors the chapter's repeated "no exceptions" gate language.)*

## Chapter shape — current vs. proposed

### Current
1. In-Brief (L5-8) — names 4 deliverables.
2. COO/coordinator opener (L10-18) — strong.
3. "Design exists to ask what the work actually is" (L20-24).
4. "What Design produces" (L26-36) — the four deliverables.
5. **Hybrid Accountability Chart full section** (L38-74) — Right Seat Evaluation, four questions.
6. **Information flow question** (L76-102) — comes AFTER the HAC. Reader has to imagine the chart populated against accountabilities they haven't yet seen mapped.
7. How AI connects to information — five patterns (L104-138).
8. AI-assisted vs. automated (L140-163).
9. Governance & guardrails (L165-186).
10. Agent mini-spec (L188-203) — **HBR citation: Bedard's 3-agent ceiling at L201 + AWS/Effectual supervisor-capability check at L203**.
11. Tool category selection (L205-244).
12. **Human Orchestrator** (L246-276) — at ~80% through the chapter. This is the chapter's central role concept, arriving very late.
13. Design Team / Design Brief preview (L278-293).
14. Populated example: Meridian (L295+).
15. Reflection Questions (end).

**Problems the reading team flagged:**
- **FLOW#1 — Lead with practice.** The HAC arrives before information flow. Readers don't see what the chart is mapping until 30% later. Reorder.
- **Human Orchestrator demoted by placement.** L246 is too late for the chapter's most important role concept. Move up — ideally after the information-flow section.
- **HBR over-cited.** Bedard at L201 + AWS at L203. Both relate to supervisor capability/oversight load. Cut one or compress to a single reference.
- **ARC#13 disambiguation** — L282 has "the COO (Integrator if you run EOS)" which conflates the Orchestrator role with EOS Integrator. Handled by 3B sweep `book-8v6v.32`; Drafter shouldn't touch.
- **ARC#8** — chapter has Action Steps already; closing Action Step before the Meridian populated example is light. Add HAC-draft Action Step (already exists at L160-161 in slightly weaker form).

### Proposed

1. **In-Brief** — Trim slightly. Lead with the chapter's main claim ("every agent team needs a human supervisor by name") rather than the four-deliverable enumeration.
2. **Opener (COO/coordinator)** — Keep L10-18 verbatim. Strongest narrative moment in the chapter.
3. **Design exists to ask what the work actually is** — Keep L20-24.
4. **What Design produces (four deliverables)** — Keep L26-36 but make the four explicit as a numbered list before the chapter prose develops each one.
5. **The information flow question — PROMOTE.** Move L76-102 up to here. Reader needs to see information flow as the lens BEFORE seeing the chart that maps it. The five patterns at L104-138 fold under this section.
6. **The Hybrid Accountability Chart** — Now arrives after the reader has the information-flow concept and the five patterns. Keep L38-74 content but reframe: HAC is how you assign owners to the flow you just mapped.
7. **The Human Orchestrator — PROMOTE.** Move L246-276 up to immediately after the HAC. Drafter should be careful: this section currently sits next to Design Team / Design Brief. Cleanly extract just the Human Orchestrator content; the Design Team section stays in its current position.
8. **AI-assisted vs. automated** — Keep L140-163. Light touch.
9. **Governance and guardrails** — Keep L165-186. The five questions are excellent in-body fillable artifact.
10. **The agent mini-spec** — Keep L188-203 BUT **trim HBR citations**:
    - **Keep:** ONE of Bedard's 3-agent ceiling OR AWS/Effectual capability check. Recommend keeping Bedard's three-agent ceiling here (it's the more consequential design constraint and gets reused in Ch 7b + Ch 8). Cut AWS supervisor-capability check or compress to one sentence without attribution.
11. **Tool category selection** — Keep L205-244. Light touch.
12. **Design Team / Design Brief preview** — Keep L278-293. ARC#13 sweep handles the COO/Integrator conflation at L282 in 3B.
13. **Populated example: Meridian** — Keep L295+.
14. **Closing Action Step — STRENGTHEN.** Add a closing action that produces the chapter's deliverable: a draft HAC entry. Already partially exists at L160 (autonomy rationale) and L271-274 (Human Orchestrator). Add one more at the end: *"Draft the HAC row for your constraint workflow: four fields filled, supervisor named, autonomy decided. If any cell is empty, the Design isn't done."*
15. **Reflection Questions** — Keep, trim to 3-4.

## Concept & context — AI bridge

The chapter's AI framing is strong throughout. The five patterns section makes the AI bridge concrete. Light touch needed; already serving the bridge well.

## How-to — arrival timing

Currently, first Action Step is at L99-101 (information flow exercise) — about 25% through the chapter. That's reasonable, but the conceptual frame (HAC + Right Seat Evaluation) is dense before it. The FLOW#1 reorder (info flow before HAC) makes the first Action Step land at a more natural position because the reader already has the framing.

## Artifacts

| Artifact | Status | Location |
|---|---|---|
| Hybrid Accountability Chart template (4 columns) | Excalidraw L41 + L57 | Add **in-body fillable table** template. Per consolidated artifact bead. |
| Right Seat Evaluation (3 tests) | Inline prose L63-67 | Make explicit as in-body checklist artifact. |
| Information Flow Specification | Prose L82-87 | Add **in-body fillable template** (4 fields: feeds, transformations, decisions, outputs). |
| Swim lane diagram | Excalidraw L93 | Keep. |
| AI-assisted-to-automated spectrum | Excalidraw L150 | Keep. |
| Five governance questions | Inline prose L173-181 | Already a checklist in prose form. Make explicit as in-body table. |
| Agent mini-spec (6 fields) | Inline prose L192-199 | Add **in-body fillable template** (6 fields per agent). |
| Tool category decision flowchart | Excalidraw L217 | Keep. |
| Current tools table | In-body L231-237 | Keep — solid in-body reference. |
| Populated Meridian HAC | In-body L295+ | Best in-body artifact. |

## Closing handoff

Currently L288 says "The next chapter introduces the Design Brief in detail." Tighten: *"The next chapter designs the work itself: TML deconstruction, populated chart, and the Design Brief that locks the gate."*

## Headings inventory

### Current (italic-fragment + label style)
- L1 `# *Designing the System*.` (H1)
- L26 `## What Design *produces*.` (H2)
- L38 `## The *Hybrid Accountability Chart*.` (H2)
- L76 `## The *information flow* question.` (H2)
- L104 `## How AI connects to *information*.` (H2)
- L140 `## AI-assisted or *automated*.` (H2)
- L165 `## Governance and *guardrails*.` (H2)
- L188 `## The *agent mini-spec*.` (H2)
- L205 `## Tool *category* selection.` (H2)
- L227 `### The current tools.` (H3)
- L246 `## The *Human Orchestrator*.` (H2)
- L257 `### Finding the right *person*.` (H3)
- L278 `## The *Design Team*.` (H2)
- L295 `## The populated *example*.` (H2)

### Proposed (directive, no italic fragments)
- H1: `# Designing the System: Every Row Has a Name`
- H2: `## Design Has Four Deliverables` (was "What Design produces")
- H2: `## See the Work as Information Flow First` (PROMOTED from current position)
- H2: `## Map AI to Information Flow Using Five Patterns` (was "How AI connects to information")
- H2: `## The Hybrid Accountability Chart Assigns Owners to the Flow` (was "The Hybrid Accountability Chart" — directive)
- H2: `## Name the Human Orchestrator Before Build Begins` (PROMOTED from L246)
  - H3: `### Pick the Person Who Owns the Outcome` (was "Finding the right person")
- H2: `## Start AI-Assisted. Earn Automation.` (was "AI-assisted or automated")
- H2: `## Lock Governance Before the Build Begins` (was "Governance and guardrails")
- H2: `## Every Agent Gets a Six-Field Mini-Spec` (was "The agent mini-spec")
- H2: `## Pick the Tool Category Before You Pick the Tool` (was "Tool category selection")
- H2: `## The Design Team Is Functional, Not a Committee` (was "The Design Team")
- H2: `## Meridian's Populated Hybrid Accountability Chart` (was "The populated example")
- H2: `## Reflection Questions`

## HBR citation discipline

**Current count:** 2 HBR citations in this chapter (Bedard 3-agent ceiling at L201 + AWS/Effectual capability check at L203). At the cap, but both clustered in one section, so reads heavy.

**Trim:** Keep Bedard (more consequential, reused downstream in Ch 7b + Ch 8). Cut AWS or compress to one sentence without attribution.

## Meridian weave

Strong — Meridian appears as the populated example at L295+. Light touch.

## Time-budget strip (ARC#9)

Scan for time language: L269 mentions "ramp-up... several Sprints" and "by the second Sprint... by the fourth" — scope language, not time-budget, keep. No edits needed.

## Notes for the Drafter

- **Drafter model:** Sonnet (mostly reorder + heading rewrite + light trim).
- The biggest move is the FLOW#1 reorder: information flow + five patterns BEFORE the HAC. Then Human Orchestrator promoted up after the HAC. Drafter should preserve the existing prose; this is mostly cut-and-paste with section transitions tightened.
- Voice charter applies. Strip italic-fragment heading style. No em-dashes.
- ARC#13 (`book-8v6v.32`) handles the COO/Integrator conflation at L282 in 3B; Drafter should NOT touch.
- Run deflourish.py --apply after drafting.
- Cross-reference: Drafter should verify references to "Chapter 3" / "Chapter 7b" / "Chapter 8" still resolve correctly post-renumbering.
