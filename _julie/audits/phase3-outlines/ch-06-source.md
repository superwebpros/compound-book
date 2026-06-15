# Phase 3A Outline — Ch 6 (Source)

**Source file:** `chapters/05-source.qmd`
**Priority:** 3C #2 (heavy restructure)
**Beads:** `book-3w1t` (FLOW#2 simplicity rescue — only Simplicity Fail in main body), `book-n628` (ARC#11 AI Tier inline definition reconciliation), `book-xqxi` (ARC#3 jargon — handled 3B), `book-b8yy` (FLOW#3 Meridian — already present, light check), HBR citation discipline (memory — heavy trim needed), AI Tier terminology (memory — adopt case-study Tier 1/2/3 vocabulary).
**Status:** Heavy restructure. This is the only main-body chapter that scored Simplicity Fail. Three overlapping frameworks (three-layer / TML / PIS / AI tiers), HBR scaffolding in the opener, two near-duplicate knowledge-management sections, and the Meridian vignette arrives at ~70% through the chapter.

## New chapter title (proposed)

**"Source: Map What the Organization Knows About the Constraint"**

*(Current title is just "Source." Match Traction's "main-idea after colon" pattern. Alternative: "Source: A One-Page Knowledge Map or No Design.")*

## Chapter shape — current vs. proposed

### Current (5 frameworks layered, dense, late Meridian)
1. In-Brief (L3-6) — long; names three-layer + Knowledge Map + completeness gate.
2. Three layers section (L8-22) — Systems of Record / Knowledge / Semantics. **HBR-scaffolded** (Argenti L20, Sadun L20, AWS L22).
3. Jesse PM coordinator anecdote (L26-30).
4. Julie M&A example (L34).
5. Canvas connection (L36).
6. "Diagnosis isn't done until you know what you have" + **TML framework** (L38-50).
7. **PIS framework** (L52-58) — Problem / Identify / Solution.
8. Knowledge Map deliverable (L60-78).
9. **Three passes**: Digital / Organic / Missing (L81-113).
10. Classification: structured/unstructured + durable/ephemeral + **AI tiers** (standing context / retrieved / historical) (L115-147).
11. APIs / MCPs / Connectors definitions + terminology note (L149-176).
12. People-don't-have-APIs section — Digital / Organic / At-risk (L178-198). **Redundant with Pass 1-3.**
13. Transcripts as API (L200-217).
14. **Meridian Source vignette** (L219-231) — arrives at ~70% through.
15. **Knowledge management in agentic world** (L233-242).
16. **Knowledge management is the foundation** (L244-256) — near duplicate of preceding section.
17. Knowledge manager role (L258-266).
18. Garbage in, garbage out (L268-279).
19. Completeness test — 8 checks (L281-297).
20. Meridian completed Knowledge Map table (L299-311).
21. Hand off to Design (L313-319).
22. Reflection Questions (L321-327).

**Problems the reading team flagged:**
- **FLOW#2 Simplicity Fail.** Three frameworks (three-layer / TML / PIS) stacked before the deliverable. PIS gets a section heading but only contributes one paragraph of value.
- **HBR over-cited.** Argenti + Sadun + AWS in the opener (L20-22). Plus the chapter contradicts the chapter's voice by leaning on HBR for its core "data is ground truth" claim.
- **Meridian late.** The vignette at L219-231 arrives too far in. Reader experiences ~70% of the chapter as abstract before seeing the worked example.
- **Two duplicate knowledge-management sections** (L233-242 and L244-256). Cut one.
- **AI Tier terminology drift.** Chapter uses "standing context / retrieved / historical" (L131-133). Case studies use "Tier 1 / Tier 2 / Tier 3 / Not AI-tier." Adopt case-study terminology.
- **Vocabulary sequence issue** (FLOW#2). "People don't have APIs" section (L178) introduces Digital / Organic / At-risk *after* the three-pass section already introduced them as Pass 1, 2, 3. Redundant.
- **Dangling 'developer' allusion** at L198 ("if we had mapped where the knowledge lived before that developer left") — references a story not in this chapter. The developer story is in the Preface. Either re-establish or cut.

### Proposed

1. **In-Brief** — Trim to 3-4 lines. Single artifact (Knowledge Map), single gate (completeness test). Drop the three-layer enumeration here; let the chapter make the claim.
2. **Opener: Jesse PM coordinator** — Move L26-30 up to be the chapter's actual opener. Stories first. The three-layer abstract framing should not lead.
3. **The three layers** — Keep L8-22 content but move AFTER the Jesse anecdote. **Strip HBR scaffolding.** Cut Argenti, Sadun, AWS quotes (L20-22) entirely. The three-layer frame stands on its own claim; the HBR appeal is unnecessary scaffolding. (Optional preserve: one Argenti reference if the author wants to keep the data-is-ground-truth language, but trim to one sentence with parenthetical attribution, not block-quoted.)
4. **Julie M&A example** — Keep L34 as the non-AI parallel.
5. **Canvas connection** — Keep L36.
6. **Diagnosis isn't done until you know what you have + TML** — Compress L38-50. The TML framework gets a paragraph here, not its own section heading. Reader sees: three-layer = WHERE knowledge lives; TML = WHAT it lets you do. One paragraph, not two sections.
7. **PIS framework — compress to one sentence.** Currently L52-58 (six lines). The whole point is "Signal named the problem, Source identifies what we have, Design solves." That's one sentence: *"Source is the Identify phase between Signal's Problem and Design's Solution; don't move to solution until identification is complete."* Cut PIS as a named framework — it's a sequencing principle, not a third taxonomy.
8. **The Knowledge Map deliverable** — Keep L60-78. Strong section. Includes Pipeline Audit. Adjust to call out the **in-body fillable template** (per consolidated artifact bead).
9. **Three passes** — Keep L81-113. This is the chapter's how-to. Move the Action Steps slightly earlier in each pass.
10. **Classification (structured / durable / AI tiers)** — Keep L115-147 **but rewrite the AI tier section to match case-study vocabulary**:
    - **Tier 1**: AI can use directly (structured, API-accessible). Maps loosely to current "standing context" but broader — any structured source AI can query.
    - **Tier 2**: AI can process with an extraction pipeline (unstructured but capturable: PDFs, transcripts, documents). Maps to current "retrieved knowledge."
    - **Tier 3**: Human judgment required (not AI-accessible at all). Replaces current "historical record" which is a different distinction.
    - **Not AI-tier**: Stays human, queried in real time (ephemeral or judgment-bound).
    - Update the Pro Tip at L138-140 to match.
11. **APIs / MCPs / Connectors definitions** — Keep L149-176. This is the chapter's jargon-pass section and serves cross-cutting `book-xqxi` (ARC#3) goals. Drafter shouldn't expand — `book-xqxi` 3B sweep adds parenthetical first-use definitions everywhere else in the book.
12. **People-don't-have-APIs section** — **Cut or merge.** Currently L178-198. The Digital / Organic / Missing taxonomy already appeared in the three-pass section. The only new content here is the "at-risk" subcategory and the "developer" callback (which is itself broken — see below). Consolidation move: cut the section header, fold the "at-risk" subcategory into Pass 2 (Organic), and cut the "developer left" sentence at L198 (it dangles).
13. **Transcripts as API** — Keep L200-217. Distinct claim, useful method.
14. **MOVE MERIDIAN EARLIER.** The vignette at L219-231 should appear right after Pass 1-3 (around current L113), not after the classification + jargon + people-don't-have-APIs + transcripts sections. Reader needs the worked example BEFORE the deeper classification work.
15. **Knowledge management sections — COLLAPSE.** Currently two sections (L233-242 and L244-256). Cut the first ("Knowledge management in an agentic world"). Keep the second ("Knowledge management is the foundation"). The two sections cover the same ground from slightly different angles; one is enough.
16. **Knowledge manager role** — Keep L258-266 as a subsection of the consolidated knowledge-management section.
17. **Garbage in, garbage out** — Keep L268-279. Strong section, good ending tone before the completeness test.
18. **Completeness test** — Keep L281-297. The 8-item checklist is excellent in-body fillable artifact. Adjust item 3 (Layer test) and item 4 (TML test) wording to match the streamlined framework presentations earlier in the chapter.
19. **Meridian completed Knowledge Map table** — Keep L299-311. Excellent artifact.
20. **Hand off to Design** — Keep L313-319.
21. **Reflection Questions** — Keep L321-327. Trim from 4 to 3 if possible.

## Concept & context — AI bridge

The chapter's AI framing is good (this is the chapter most explicitly about preparing data for AI consumption). The bridge that needs work is at the front: cut the HBR scaffolding (Argenti, Sadun, AWS at L20-22) so the chapter carries its own claim rather than borrowing authority. The three-layer frame is the chapter's own claim and stands alone.

## How-to — arrival timing

Currently the first Action Step is at L85 (Pass 1, Digital) — about 28% through the chapter. That's reasonable but the conceptual setup before it is dense (three frameworks). With the PIS compression and the Meridian-earlier move, the first Action Step lands at roughly the same position but inside a chapter that's reorganized around its examples.

## Artifacts

| Artifact | Status | Location |
|---|---|---|
| Knowledge Map template (6 columns) | Excalidraw L77 | Add **in-body fillable table** matching the six columns. Per consolidated artifact bead. |
| Knowledge Map (PM Agent case study) | Excalidraw L70 | Keep. |
| Three-pass build diagram | Excalidraw L113 | Keep. |
| Elena's completed Knowledge Map | Excalidraw L221 + in-body table L299-311 | Keep — best in-body artifact in the chapter. |
| Source-to-Design handoff | Excalidraw L317 | Keep. |
| 8-item completeness test | In-body L281-297 | Keep — this is a fillable checklist. Consider making it explicit as such. |
| **NEW: AI Tier classification table** | Add as in-body | When the AI Tier section is rewritten to match case-study vocabulary, the four categories should appear as a small reference table (Tier | What AI can do | Example) so the reader sees it as classification, not prose. |

## Closing handoff

L313-319 is decent. Tighten the final sentence: *"Constraint plus map is the input Design needs. Bring both to Chapter 7."* Adjust chapter number if renumbering finalizes differently.

## Headings inventory

### Current
- L1 `# *Source*.` (H1)
- L8 `## Every organization runs on three *layers*.` (H2)
- L38 `## Diagnosis is not done until you know what you *have*.` (H2)
- L52 `## Source is the *Identify* phase.` (H2)
- L60 `## Create a *Knowledge Map*.` (H2)
- L81 `### Pass 1: *Digital*.` (H3)
- L90 `### Pass 2: *Organic*.` (H3)
- L99 `### Pass 3: *Missing*.` (H3)
- L115 `## Classify what you *find*.` (H2)
- L119 `### Structured vs. *unstructured*.` (H3)
- L123 `### Durable vs. *ephemeral*.` (H3)
- L127 `### AI *tiers*.` (H3)
- L149 `## How systems *talk to each other*.` (H2)
- L153 `### *APIs*.` (H3)
- L157 `### *MCPs*.` (H3)
- L161 `### *Connectors*.` (H3)
- L178 `## People don't have *APIs*.` (H2)
- L182 `### *Digital* sources.` (H3)
- L186 `### *Organic* sources.` (H3)
- L190 `### *At-risk* sources.` (H3)
- L200 `## Transcripts: the *closest thing* a person has to an API.` (H2)
- L219 `### Sprint · Source at Meridian.` (H3)
- L233 `## Knowledge management in an *agentic* world.` (H2)
- L244 `## Knowledge management is the *foundation*.` (H2)
- L258 `### The *knowledge manager*.` (H3)
- L268 `## Garbage in, Garbage Out.` (H2)
- L281 `## The *completeness test*.` (H2)
- L313 `## Hand off to *Design*.` (H2)
- L321 `## Reflection Questions` (H2)

### Proposed (directive, strip italicized-fragment style)

The current chapter heavily uses italic-fragment headings (`## Every organization runs on three *layers*.`). Italic-fragment style is a Compound voice tic — neither directive nor labels. Convert to directive language matching the rest of the book's Phase 3 standard.

- H1: `# Source: Map What the Organization Knows About the Constraint`
- H2: `## Every Organization's Information Lives in Three Layers`
- H2: `## You Aren't Done with Diagnosis Until You Know What You Have`
- H2: `## Build the One-Page Knowledge Map`
  - H3: `### Pass 1 — Digital Sources`
  - H3: `### Pass 2 — Organic Sources (People as Sources)`
  - H3: `### Pass 3 — Missing Sources`
- H2: `## Source at Meridian` *(moved up — was H3, promote to H2 as full case study section)*
- H2: `## Classify What You Found`
  - H3: `### Structured vs. Unstructured`
  - H3: `### Durable vs. Ephemeral`
  - H3: `### Sort by AI Tier (1, 2, 3, or Not AI-Tier)` *(rewritten to match case-study vocabulary)*
- H2: `## How Systems Talk to Each Other`
  - H3: `### APIs — How Systems Talk to Systems`
  - H3: `### MCPs — How AI Talks to Systems`
  - H3: `### Connectors — Pre-Built Integrations`
- H2: `## A Transcript Is the Closest Thing a Person Has to an API`
- H2: `## Treat Knowledge Management as Infrastructure` *(consolidates the two near-duplicate KM sections)*
  - H3: `### Name a Knowledge Manager`
- H2: `## Garbage In, Garbage Out`
- H2: `## Run the Completeness Test Before You Hand Off`
- H2: `## Hand Constraint Plus Map to Design`
- H2: `## Reflection Questions`

## HBR citation discipline (memory rule)

**Current count:** 3 HBR citations in the opener alone (Argenti, Sadun, AWS at L20-22). The author has called Ch 2 Beliefs the worst HBR-scaffold offender, but Ch 6 Source is the second-worst.

**Trim to 1-2 max:**
- **Cut:** Sadun "effective only to the extent" quote at L20 (already overused across chapters; same author cited in Ch 2 and Ch 1).
- **Cut:** AWS framing at L22 ("AI systems lack the contextual awareness..."). This is the AWS/Effectual citation that the user already flagged for Ch 1 as advertorial. Remove from Ch 6 too.
- **Optional keep:** Argenti "data is ground truth" at L20 — trim to one sentence with parenthetical attribution (not block-quote). If author wants the framing, this is the cleanest one to keep.

If the author prefers zero HBR citations in Ch 6 (since Ch 2 keeps the Argenti banker scene), that's also clean. **Surface both options.**

## AI Tier terminology reconciliation (memory rule)

Currently L127-134 names three tiers: standing context / retrieved / historical. The case studies (`case-study-meridian.qmd` L141-150 and `case-study-pm-agent-team.qmd` L76-86) use Tier 1 / Tier 2 / Tier 3 / Not AI-tier.

**Rewrite L127-147 to adopt case-study vocabulary** (Tier 1 = structured/API-accessible; Tier 2 = unstructured but extractable; Tier 3 = human judgment required; Not AI-tier = ephemeral/queried in real time). Verify final language against the case studies after the rewrite lands.

## Meridian weave (FLOW#3)

Already present (L77-81 PT clinic, Elena vignette L219-231, Meridian completed table L299-311). The issue is *placement*, not absence. **Move the Elena vignette earlier** — right after the three-pass section (~L113), not after the classification + jargon + people-don't-have-APIs + transcripts sections.

## Time-budget strip (ARC#9)

No explicit time-budget language detected. The chapter's "this week" in the Action Step at L216 is reasonable urgency; keep.

## Notes for the Drafter

- **Drafter model:** Opus (heavy restructure, multiple framework collapses, terminology reconciliation against case studies).
- This is the chapter most affected by the Phase 3 Simplicity Rescue. The single highest-leverage moves are: (1) cut HBR scaffolding from opener, (2) compress PIS to one sentence, (3) move Meridian vignette earlier, (4) collapse two KM sections into one, (5) merge "people don't have APIs" into Pass 2, (6) adopt case-study AI Tier vocabulary.
- Do not start from scratch. Estimated 70-75% of prose survives the restructure — the move is cut, compress, reorder.
- Voice charter applies. Watch the italic-fragment headings — strip them. No em-dashes.
- After Drafter completes, cross-coherence-check against `case-study-meridian.qmd` L141-150 and `case-study-pm-agent-team.qmd` L76-86 — both Tier tables should use the same vocabulary the chapter now defines.
- Run deflourish.py --apply after drafting (non-negotiable).
- Cross-cutting beads handled separately in 3B: `book-xqxi` adds plain-English parentheticals on first-use jargon (RAG, embeddings, vectorization, ontologies). Drafter should leave the existing jargon in place — the 3B sweep handles the additions.
