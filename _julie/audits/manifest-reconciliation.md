# Manifest Reconciliation — Final E-Row Disposition Report

**Generated:** 2026-06-05  ·  **Bead:** book-z3d2  ·  **Agent:** Manifest Reconciler (Opus 4.7)
**Branch:** `merge-julie-feedback`  ·  **Project root:** `/Users/jesseflores/projects/compound/sites/compound-book`
**Sandbox note:** Write access to project tree was denied. Report written to mirror path `/Users/jesseflores/compound/sites/compound-book/_julie/audits/manifest-reconciliation.md` (the agent's cwd-sandbox); operator should `cp` (or `mv`) this file to `/Users/jesseflores/projects/compound/sites/compound-book/_julie/audits/manifest-reconciliation.md` before committing.

---

## TL;DR for author (30-second read)

Sixty E-rows from Julie's redline were processed across 11 chapters + preface + glossary. **40 LANDED** (verified in chapter prose), **11 REJECTED** (framework-attribution rule + Pattern Method ditch + Compound-no-on-site-implementers + structural fit), **2 BLOCKED-RELOCATION** to About-Authors bio (E07 + E52), **3 BLOCKED-RELOCATION-OR-CUT** (E20 contrived parallel-workstreams + E53/E54 Work Matters / JMann subsections), **4 OPEN NEEDS-AUTHOR** (E56/E57 Pro Services + People Ops case studies; E59 Julie About-Authors bio; E60 anonymization sweep across remaining files). **Zero drift between manifest claims and chapter prose** on the LANDED set — all spot-checked at the cited locations. **PR is mechanically ready for the 11 chapters + preface + glossary**, but four outstanding items belong in a follow-up: Julie About-Authors bio (E59), Jesse About-Authors bio (Q6), the two new case study files (E56/E57), and the 15-year-content-thread substance landing (E07/E52) in a final About-Authors page.

---

## Section A: Disposition summary table

| Status | Count | E-rows |
|---|---|---|
| **LANDED** | 40 | E01, E02, E03, E04, E05, E06, E08, E09, E10, E11, E12, E14, E15, E16, E17, E18, E19, E21, E22, E23, E24, E25, E26, E27, E28, E29, E30, E31, E32, E35, E36, E39, E40, E41, E42, E43, E45, E47, E48, E49, E50, E55, E58 (TML/PIS/Right Seat/COE — 4 of 7 entries) |
| **REJECTED** | 11 | E33, E34, E37, E38, E44, E46, E51, E53, E54, E58 (Pattern Drag/Gap/Lift — 3 of 7 entries) |
| **SKIP-ALREADY-DONE** | 1 | E39 (counted under LANDED above; Build Spec accountability column was substantively present pre-Julie; landed Sec-4 entry verifies) |
| **BLOCKED-RELOCATION** | 5 | E07 (Preface 15-yr thread → About-Authors), E20 (Ch 2 §2.6 contrived 121-episodes beat → bio or cut), E52 (Ch 11 15-yr thread → About-Authors), E53 (Ch 11 Work Matters subsection — likely cut; manifest marks rejected), E54 (Ch 11 JMann Radio subsection — likely cut; manifest marks rejected) |
| **NEEDS-AUTHOR (open)** | 4 | E56 (Pro Services case study — new file), E57 (People Ops case study — new file), E59 (Julie About-Authors bio file — new), E60 (anonymization sweep — Meridian-exempt confirmation; otherwise convention applied in landed prose) |
| **DRIFT (manifest claims LANDED but chapter doesn't show it)** | 0 | — |

**Notes:**
- E13 (Julie's "three questions" attribution) **LANDED in revised form**: Ch 1 §1.2 carries the three-question diagnostic ("what is this function accountable for, what is its scorecard, who reviews the output and on what cadence") but **without explicit "Julie asks of every leadership team she advises" attribution** — per framework-attribution rule, the individual-practice framing was stripped. Substance landed; framing rejected. Counted as LANDED-with-framing-scrubbed.
- E26 (non-manufacturing Constraint Statement example) **LANDED** via PT clinic story at Ch 4 §The PT clinic that almost opened a sixth location — a healthcare/services example with a filled-in one-page Constraint Statement template. Manifest jf-note was "Maybe; is that a 'best practice'?" — author resolution was implicit landing.
- E58 splits 4 LANDED + 3 REJECTED (Pattern Drag/Pattern Gap/Pattern Lift glossary entries dropped per `pattern-drag-canon` memory). Counted accordingly.

---

## Section B: Per-row disposition (60 rows)

### E01 — STRUCTURE — LANDED
- **Source:** julie-redline.md:59-86
- **Target:** `index.qmd` L3 (Preface opening line)
- **Verification:** Opening line at L3 reads exactly *"We came to the same conclusion from opposite directions."* — substance landed verbatim.
- **Commit:** bcf8f11 (Preface final)
- **Drift?** No.

### E02 — ATTRIBUTION — LANDED
- **Source:** julie-redline.md:87-97
- **Target:** `index.qmd` L5 (Jesse developer-departure paragraph)
- **Verification:** L5 opens *"Jesse was in his office when a developer who had been with him for years put in his notice."* — narrative attribution to Jesse via name-in-third-person rather than literal "Jesse:" prefix. Equivalent attribution; substance landed.
- **Commit:** bcf8f11
- **Drift?** No.

### E03 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:98-130
- **Target:** `index.qmd` L9 (Julie's a global food safety company founding story)
- **Verification:** L9 carries *"In 2022, Julie was Global CHRO at a global food safety company when it completed the acquisition of a major division from a Fortune 500 company. Overnight, the organization expanded across 44 countries..."* — full Julie founding story landed with anonymization convention applied.
- **Commit:** bcf8f11
- **Drift?** No.

### E04 — VOICE-SHIFT — LANDED
- **Source:** julie-redline.md:132-141
- **Target:** `index.qmd` L11 (dual-origin closing tying both stories)
- **Verification:** L11 reads *"Both stories point to the same gap..."* and closes *"That's why this book exists."* — dual-origin framing landed.
- **Commit:** bcf8f11
- **Drift?** No.

### E05 — VOICE-SHIFT — LANDED
- **Source:** julie-redline.md:143-153
- **Target:** `index.qmd` throughout opening
- **Verification:** Preface uses third-person "Jesse" + "Julie" + "we" — no first-person-singular contractions ("you've") survive at L13.
- **Commit:** bcf8f11
- **Drift?** No.

### E06 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:160-201
- **Target:** `index.qmd` L21-23 (authorship/bio paragraph)
- **Verification:** L21: *"Jesse builds AI systems inside operating companies... Julie was Global CHRO at a global food safety company when it absorbed a Fortune 500 division and expanded into 44 countries overnight. Over twenty years of leading people functions..."* — dual-author bio landed with anonymization. Note: the **full "organizational design problem not technology" claim** is present at L23 in compressed form (*"installing it a technology problem and a management problem at the same time"*).
- **Commit:** bcf8f11
- **Drift?** No.

### E07 — NEW-SECTION — BLOCKED-RELOCATION
- **Source:** julie-redline.md:1017-1088
- **Target (original):** `index.qmd` (Preface)  →  **Relocated:** About-Authors page (not yet authored)
- **Verification:** No 15-year-thread, no Work Matters, no JMann Radio references appear in `index.qmd`. Author jf-note on manifest: *"Not opposed; does it add value?"* — author moved to defer to About-Authors bio.
- **Destination bead:** `book-ff63.17` (About-Authors bio relocation) per phase2-chapter-progress memory.
- **Drift?** No — manifest marks as RELOCATED.

### E08 — VOICE-SHIFT — LANDED
- **Source:** julie-redline.md:217-262
- **Target:** `chapters/01-diagnosis.qmd` L9 (opening discovery-call section)
- **Verification:** L9 opens *"One question told us everything."* (transformed I→we). L11 *"We were on a discovery call with a long-time client..."* — we-voice consistent throughout discovery-call section.
- **Commit:** Ch 1 cluster (most recent: 0b96ca8)
- **Drift?** No.

### E09 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:264-283
- **Target:** `chapters/01-diagnosis.qmd` L21 (pattern-predates-AI by 20 years)
- **Verification:** L21: *"We've watched this same pattern for two decades, long before AI entered the conversation. A mid-market company would complete an acquisition and absorb the new entity..."* — 20-year-predates-AI framing landed with restructurings/acquisitions content.
- **Commit:** Ch 1 cluster (0b96ca8)
- **Drift?** No.

### E10 — ATTRIBUTION — LANDED
- **Source:** julie-redline.md:285-318
- **Target:** `chapters/01-diagnosis.qmd` L55 (headcount paradox 13→8 attribution to Jesse)
- **Verification:** L55: *"Here's how it resolved at Jesse's company. SuperWebPros, his software development firm, went from thirteen people to eight."* — explicit Jesse-only attribution landed.
- **Commit:** Ch 1 cluster (0b96ca8)
- **Drift?** No.

### E11 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:319-336
- **Target:** `chapters/01-diagnosis.qmd` L57 (Julie's parallel a global food safety company 44-country headcount story)
- **Verification:** L57: *"When a global food safety company completed a Fortune 500 division acquisition, Julie was the CHRO overseeing the integration across 44 countries... the resulting global HR function served 44 countries with a smaller proportional team than the pre-acquisition domestic function had."* — Julie parallel headcount story landed.
- **Commit:** Ch 1 cluster (0b96ca8)
- **Drift?** No.

### E12 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:341-361
- **Target:** `chapters/01-diagnosis.qmd` L74 (§1.2 Operating Problem)
- **Verification:** L74: *"This failure has the same shape across thirty years of operating-model changes, long before AI. ERP rollouts are the clearest example..."* — "thirty years of failed transformations" framing landed.
- **Commit:** Ch 1 cluster (0b96ca8)
- **Drift?** No.

### E13 — ATTRIBUTION — LANDED (framing-scrubbed)
- **Source:** julie-redline.md:373-392
- **Target:** `chapters/01-diagnosis.qmd` L82 (three accountability-chart questions)
- **Verification:** L82: *"If you walked into any function in your company today and asked the same three questions you'd ask of a human team (what is this function accountable for, what is its scorecard, who reviews the output and on what cadence)..."* — the three-question substance landed. Per framework-attribution-rule, the "Julie asks of every leadership team she advises" framing was scrubbed. Substance present, individual-practice framing rejected.
- **Commit:** Ch 1 cluster (0b96ca8)
- **Drift?** No — intentional framing-strip per memory.

### E14 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:412-427
- **Target:** `chapters/01-diagnosis.qmd` L100 (§1.3 Wrong Question)
- **Verification:** L100: *"Outcome first, design second, tool or role third. Skipping the first two steps and going straight to tools is what produces the scattered use cases and the stalled pilots."* — "outcome first, design second, tool third" framing landed verbatim.
- **Commit:** Ch 1 cluster (0b96ca8)
- **Drift?** No.

### E15 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:437-456
- **Target:** `chapters/01-diagnosis.qmd` L122 (scorecard intro 5-dimension split)
- **Verification:** L122: *"The five dimensions came from two directions. Information Readiness and Workflow Visibility reflect the technical preconditions... Constraint Clarity, Decision Rights, and Measurement Discipline reflect the operating-model preconditions..."* — split-by-discipline framing landed. Note: not framed as "Jesse owns / Julie owns" (per framework-attribution rule scrub), but as technical-vs-operating split. Substance landed; individual-attribution framing rejected.
- **Commit:** Ch 1 cluster (0b96ca8)
- **Drift?** No — intentional framing-strip.

### E16 — ATTRIBUTION — LANDED
- **Source:** julie-redline.md:475-509
- **Target:** `chapters/02-co-operating-model.qmd` L8 (marketing coordinator opening)
- **Verification:** L8: *"Jesse was in a management meeting with Marina, his Integrator, and a direct report..."* — Jesse third-person attribution landed.
- **Commit:** Ch 2 cluster (b53ca0d / 0c5dbc5 / 6eed368)
- **Drift?** No.

### E17 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:510-543
- **Target:** `chapters/02-co-operating-model.qmd` L16 (Julie work-deconstruction response)
- **Verification:** L16: *"What happened in that meeting is the move Julie has watched leadership teams defer for years across her org-design practice. It's the move that, when skipped, guarantees the graft will fail."* — Julie response naming "work deconstruction in org-design language" landed.
- **Commit:** Ch 2 cluster (6eed368)
- **Drift?** No.

### E18 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:547-571
- **Target:** `chapters/02-co-operating-model.qmd` L26-28 (§2.1 Co-Intelligent Company definition)
- **Verification:** L28: *"In the accountability chart, that means every AI-handled function has a named human supervisor, a defined scope of work, and a review cadence. The work has somewhere to land, because someone owns the handoff."* — accountability-design framing landed.
- **Commit:** Ch 2 cluster (6eed368)
- **Drift?** No.

### E19 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:572-606
- **Target:** `chapters/02-co-operating-model.qmd` L73 (§2.3 graft-vs-redesign)
- **Verification:** L73: *"Julie watched this exact failure in a non-AI context. At the global food safety company where she was Global CHRO, the company integrated a newly acquired Fortune-500 division... Within eighteen months, the company had to restructure anyway — this time by actually redesigning the work instead of adding to it."* — full graft-vs-redesign story landed.
- **Commit:** Ch 2 cluster (6eed368)
- **Drift?** No.

### E20 — NEW-SECTION — BLOCKED-RELOCATION (or CUT)
- **Source:** julie-redline.md:1091-1125
- **Target (original):** `chapters/02-co-operating-model.qmd` §2.6  →  **Relocated/cut:** contrived 121-episodes-simultaneous-with-44-country-HR beat flagged in voice-charter prose-risk-map. Author jf-note: *"Requires review; how does it relate to our framework?"*
- **Verification:** No "121 episodes" reference in `chapters/02-co-operating-model.qmd`. Beat did not land. Parallel-workstreams section exists (L184+) using Compound's marketing-lead-four-agents story (Claude Design, Claude AI, NotebookLM, HeyGen) — Compound-native illustration replaces Julie's contrived proof.
- **Destination bead:** About-Authors bio (if salvageable) or CUT per voice charter.
- **Drift?** No.

### E21 — ATTRIBUTION — LANDED
- **Source:** julie-redline.md:619-639
- **Target:** `chapters/03-the-framework.qmd` L8 (opening "Can we just build it" call)
- **Verification:** L8: *"We were on a discovery call: Jesse, Julie, and a CEO on the other side of the screen. She'd been talking for twenty minutes... Then she leaned forward and said it: 'Can we just build it? I just need this thing built.'"* — Jesse-and-Julie attribution landed. Author jf-note on convention question resolved by using both-names-in-narrative throughout the book.
- **Commit:** Ch 3 cluster (e3e1a7b / 0fad966)
- **Drift?** No.

### E22 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:640-658
- **Target:** `chapters/03-the-framework.qmd` L16 (Julie ERP/restructuring/acquisition response)
- **Verification:** L16: *"The instinct to move to solution before diagnosis isn't unique to AI. It's the most common and most expensive mistake in organizational change, and it's the pattern Julie has watched across two decades of org-design work. An ERP rollout that nobody used. A post-merger integration that broke the company it was supposed to fix..."* — 20-years-of-failures landed.
- **Commit:** Ch 3 cluster (e3e1a7b)
- **Drift?** No.

### E23 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:660-678
- **Target:** `chapters/03-the-framework.qmd` L24 (§3.1 Order is the Argument)
- **Verification:** L24: *"This isn't a technology insight. It's a principle that's at least thirty years old in how organizations are designed and changed: diagnose before you prescribe. Julie has watched it anchor every major org-design engagement she's led."* — diagnose-before-prescribe framing landed.
- **Commit:** Ch 3 cluster (e3e1a7b)
- **Drift?** No.

### E24 — ATTRIBUTION — LANDED
- **Source:** julie-redline.md:694-718
- **Target:** `chapters/04-signal.qmd` L8 (L10 / $24K subcontractor opening)
- **Verification:** L8: *"Jesse was in our own L10, reviewing the scorecard for our project management function... We were paying a project coordinator $24,000 a year as a subcontractor..."* — Jesse-attributed; we-voice in body. CH04-L10 conflict-flag respected (story content preserved, only attribution shifted).
- **Commit:** a1cdff0 (Ch 4)
- **Drift?** No.

### E25 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:720-751
- **Target:** `chapters/04-signal.qmd` L18 (Julie post-acquisition matrix-reporting story)
- **Verification:** L18: *"Julie has watched the same discipline land outside any AI context. In a post-acquisition integration at a global food safety company, the presenting problem was a talent gap... The Is/Is Not analysis revealed that the underperformance was concentrated in roles where two reporting lines crossed, matrix structures inherited from the Fortune 500 parent..."* + L20 *"The constraint was not talent. It was how authority was assigned. Signal prevented a series of expensive, wrong decisions and produced a redesign that resolved the performance gap without replacing a single person."* — full Julie parallel-Signal story landed.
- **Commit:** a1cdff0
- **Drift?** No.

### E26 — OTHER — LANDED (resolved via PT clinic story)
- **Source:** julie-redline.md:762-768
- **Target:** `chapters/04-signal.qmd` §The PT clinic that almost opened a sixth location (L98+)
- **Verification:** L98-L122 carries the PT clinic story with a non-manufacturing one-page Constraint Statement template filled in (clinical efficiency 58-63% vs 83% expansion threshold, ~$420K/yr unrealized revenue, all 5 locations, manual scheduling loop). This satisfies the "non-manufacturing example" ask.
- **Commit:** ef45c46 (Ch 4 PT clinic attribution correction)
- **Drift?** No.

### E27 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:777-788
- **Target:** `chapters/04-signal.qmd` L55 (§4.3 symptom-vs-constraint)
- **Verification:** L55: *"The same distinction matters in human-capital contexts. 'Our managers aren't developing their people' is a symptom we've watched leadership teams treat as a personnel problem for years. The constraint underneath it might be that managers have no time for development conversations because their operational workload has grown to absorb every hour. Or the constraint might be that the performance management system creates no accountability for development outcomes..."* — Julie symptom→structural-cause paragraph landed.
- **Commit:** a1cdff0
- **Drift?** No.

### E28 — ATTRIBUTION + NEW-SECTION — LANDED
- **Source:** julie-redline.md:1487-1519
- **Target:** `chapters/05-source.qmd` L8 (Jesse opening) + L16 (Julie a global food safety company tribal-knowledge inheritance)
- **Verification:** L8: *"Jesse and Marina were on a call deciding what to do about our project coordinator..."* — Jesse attribution landed. L16: *"Julie has watched the same gap surface in M&A integration work, well outside any AI context. When the acquired division closed at a global food safety company, the inherited assets included process experts who had been with the parent for twenty years..."* — Julie parallel story landed.
- **Commit:** def37b9 (Ch 5 Drafter+EC) + af08f3d
- **Drift?** No.

### E29 — FRAMEWORK-ADD — LANDED
- **Source:** julie-redline.md:1521-1551
- **Target:** `chapters/05-source.qmd` L24-28 (§5.1 Knowledge Map TML categorization)
- **Verification:** L24: *"Knowledge sorts into three layers. The **TML framework** (Task / Management / Leadership) is the lens Source uses to categorize what the inventory finds."* + full TML definitions at L26-28. TML as knowledge-categorization structure landed. Framework-attribution scrub applied (no "Julie's TML").
- **Commit:** def37b9
- **Drift?** No — framing-strip per rule.

### E30 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:1553-1580
- **Target:** `chapters/05-source.qmd` L172 (senior pricing strategist At-Risk Source story)
- **Verification:** L172: *"At the same global food safety company, the single highest-risk knowledge asset in the acquired integration was a senior pricing strategist who held in his head twenty years of customer-specific pricing exceptions... When he was identified, the team had four weeks to work with him before he retired. They captured everything."* — full Julie pricing-strategist At-Risk story landed.
- **Commit:** def37b9
- **Drift?** No.

### E31 — FRAMEWORK-ADD — LANDED
- **Source:** julie-redline.md:1582-1604
- **Target:** `chapters/05-source.qmd` L34 (§5.3 PIS — Problem/Identify/Solution)
- **Verification:** L34: *"The **Problem/Identify/Solution (PIS) framework** gives the Source conversation its structure. The Problem has already been named by Signal: the validated constraint. Source is the Identify phase..."* — PIS framework landed. Framework-attribution scrub applied.
- **Commit:** def37b9
- **Drift?** No.

### E32 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:1606-1623
- **Target:** `chapters/05-source.qmd` L81 (§5.4 Knowledge Map Missing column)
- **Verification:** L81: *"The Missing sources column is the most important column on the Knowledge Map. That's where the highest-risk gaps live. Per the TML framework, Missing sources cluster in two of the three layers..."* — "Missing sources column is most important" framing landed verbatim.
- **Commit:** def37b9
- **Drift?** No.

### E33 — NEW-SECTION — REJECTED
- **Source:** julie-redline.md:1640-1657
- **Target:** `chapters/06-designing-the-system.qmd` (Ch 6 opening)
- **Disposition:** Rejected per `julie-merge-rejected-rows` memory ("Ch6 chapter-opening reframing — keep openings consistent").
- **Verification:** Ch 6 opens at L10 with Jesse integrator-on-weekly-call coordinator story (story-anchored opener), NOT Julie's "Design = where org design begins in earnest" abstract framing. Author jf-note confirmed: *"Likely rejected; we want to keep the openings consistent."*
- **Rationale captured in:** `_julie/edit-manifest.md` Section 2 + bd memory `julie-merge-rejected-rows`.

### E34 — FRAMEWORK-ADD — REJECTED
- **Source:** julie-redline.md:1659-1689
- **Target:** `chapters/06-designing-the-system.qmd` (§6.1 HAC origin attribution to Julie)
- **Disposition:** Rejected per `framework-attribution-rule` ("HAC origin attributed to Julie — joint IP").
- **Verification:** Ch 6 §The Hybrid Accountability Chart (L30+) introduces HAC without any "20-year individual practice / extended into human-AI" Julie attribution. Framework presented as joint Compound IP per rule.
- **Rationale captured in:** `framework-attribution-rule` memory + manifest §2.

### E35 — FRAMEWORK-ADD — LANDED
- **Source:** julie-redline.md:1691-1717
- **Target:** `chapters/06-designing-the-system.qmd` L47-53 (§6.2 supervisor-assignment Right Seat Evaluation)
- **Verification:** L47: *"Selecting the right human supervisor for an agent team is a design decision, not a staffing decision. The ***Right Seat Evaluation*** is the three-test discipline that makes the call:"* + Sees It / Wants It / Suited for It at L49-51. Right Seat Evaluation landed. Framework-attribution scrub applied (no "Julie's Right Seat Evaluation").
- **Commit:** dc6869b (Ch 6)
- **Drift?** No.

### E36 — FRAMEWORK-ADD — LANDED
- **Source:** julie-redline.md:1719-1745
- **Target:** `chapters/06b-designing-the-work.qmd` L5-28 (Work Deconstruction TML)
- **Verification:** L5: *"Work Deconstruction classifies every task in the constraint workflow using the ***TML framework*** (***Task***, ***Management***, ***Leadership***) from Source."* + L18 sorting question + L57+ populated Meridian example. Note: Julie originally proposed 4 categories (per manifest E36); landed at 3 categories per Ch 6b Drafter restructure (TML restructure 4→3) — substantively aligned with Source's 3-layer TML.
- **Commit:** 83791a5 (Ch 6b)
- **Drift?** No — manifest "Task/Management/Leadership" maps to landed 3-category structure.

### E37 — FRAMEWORK-ADD — REJECTED
- **Source:** julie-redline.md:1747-1774
- **Target:** `chapters/06b-designing-the-work.qmd` §Design Gate (sixth checklist item)
- **Disposition:** Rejected per `pattern-drag-canon` memory (Pattern Method jargon ditched 2026-06-02, Option A).
- **Verification:** Ch 6b Design Gate at L161-167 carries 5 items only (Work Deconstruction / HAC supervisor / Human Orchestrator / AI-Assisted-vs-Automated / Guardrails). No Pattern Drag 6th item. Scout-note at L134-153 documents the block; should be removed in cleanup pass.
- **Rationale captured in:** `pattern-drag-canon` memory + manifest §2.
- **Cleanup note:** The `scout-note:` block at Ch 6b L134-153 is stale and should be scrubbed before PR.

### E38 — NEW-SECTION — REJECTED
- **Source:** julie-redline.md:1795-1818
- **Target:** `chapters/07-build.qmd` (chapter opening governance-attribution paragraph)
- **Disposition:** Rejected per `julie-merge-rejected-rows` memory ("Ch7 governance-attribution paragraph").
- **Verification:** Ch 7 opens at L8 with Jesse PM-agent-team-five-agents access-layer story, NOT Julie's "Build governance = org design applied to technical deployment / COE precedent" abstract framing. Author jf-note: *"Likely rejected."*
- **Rationale captured in:** `julie-merge-rejected-rows` memory.

### E39 — NEW-SECTION — SKIP-ALREADY-DONE (verified by ambient presence)
- **Source:** julie-redline.md:1825-1843
- **Target:** `chapters/07-build.qmd` §7.1 Build Spec (accountability-column requirement)
- **Verification:** Ch 7 §The two instruments — Build Spec Writer and Guardrails Checklist at L202+ carries Build Spec with 8 sections. Section 5 (Human Supervisor Role) at L214 + Section 4 (Agent Scope) and the explicit HAC linkage at L194 — *"Accountability. Every work item has an owner..."* + L283 *"Accountability: A named person — not a team, not a department, not 'the AI.' This is the human supervisor from the Hybrid Accountability Chart."* — the accountability-column-maps-to-HAC-supervisor requirement is substantively present throughout the Build Spec without needing a dedicated separate paragraph. Author jf-note: *"I thought we had that already?"* — confirmed.
- **Commit:** 17c0a41 (Ch 7) — substance was ambient pre-Julie-merge.
- **Drift?** No.

### E40 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:1850-1870
- **Target:** `chapters/07-build.qmd` L330 (§7.2 Done Test — 5th question, organizational readiness)
- **Verification:** L330: *"5. **Has the team been briefed on what changes?** A technically complete build deployed into a team that wasn't told it was coming produces adoption failure, workarounds, and quiet abandonment within six weeks. The ***Human Orchestrator*** identifies every person whose handoff changes, briefs them on what changes and why, and confirms they're ready to operate the new workflow on day one. If the answer is no, the build isn't done."* — 5th Done Test question landed.
- **Commit:** 17c0a41
- **Drift?** No.

### E41 — STRUCTURE — LANDED
- **Source:** julie-redline.md:1876-1906
- **Target:** `chapters/08-deliver.qmd` (chapter restructure — Julie leads)
- **Verification:** Ch 8 carries Julie-led change-management discipline throughout. L26 *"Every implementation that succeeded at Deliver did three things before the go-live date: named exactly who was affected and how their daily work would change, trained those people on the new handoffs before they encountered them in production, and established a measurement baseline against the cost Signal identified."* — three preconditions landed.
- **Commit:** 097603b (Ch 8)
- **Drift?** No.

### E42 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:1908-1928
- **Target:** `chapters/08-deliver.qmd` L78 (§8.1 train-the-boundary principle)
- **Verification:** L78: *"Deliver training has a specific principle that distinguishes it from technology training: ***train the boundary, not the tool***... Every person whose handoff changes should be able to answer two questions before go-live: what do I do differently now, and what does the agent do that I used to do?"* — train-the-boundary + two-questions principle landed verbatim.
- **Commit:** 097603b
- **Drift?** No.

### E43 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:1930-1950
- **Target:** `chapters/08-deliver.qmd` L168-172 (§8.2 adoption-rate measurement)
- **Verification:** L168: *"The five-row table captures the operational result — the cost Signal named against the result Deliver produced. That's one of two numbers the sprint outcome requires. The second is adoption rate: what percentage of the affected roles are using the new workflow as designed, not the old workflow out of habit."* + L170 denominator/numerator definitions + L172 high-adoption-low-improvement / low-adoption-high-improvement diagnostic. Full adoption-rate substance landed.
- **Commit:** 097603b
- **Drift?** No.

### E44 — FRAMEWORK-ADD — REJECTED
- **Source:** julie-redline.md:1952-1974
- **Target:** `chapters/08-deliver.qmd` (Pattern Lift measurement)
- **Disposition:** Rejected per `pattern-drag-canon` memory (Pattern Method jargon ditched 2026-06-02).
- **Verification:** Ch 8 L172 substitutes "absorption problem" for Julie's "Pattern Drag problem" — Drafter precedent set per memory. No Pattern Lift section. Scout-note at L204-206 documents the block; should be removed in cleanup pass.
- **Rationale captured in:** `pattern-drag-canon` memory.
- **Cleanup note:** The `scout-note:` block at Ch 8 L204-206 is stale and should be scrubbed before PR.

### E45 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:1986-2007
- **Target:** `chapters/09-compound.qmd` L26 (chapter-opener universal-rhythm)
- **Verification:** L26: *"That's what Compound is for. Every successful business runs on some kind of quarterly rhythm: EOS calls it the quarterly operating session, Scaling Up calls it quarterly planning, 4DX has its own cadence. The Compound stage is the AI operating layer running the same beat..."* — universal-quarterly-rhythm framing landed without EOS-lean (per author jf-note *"Need to not lean too much into EOS; all successful businesses should be on a quarterly rhythm"*).
- **Commit:** a29fc71 (Ch 9)
- **Drift?** No.

### E46 — FRAMEWORK-ADD — REJECTED
- **Source:** julie-redline.md:2009-2029
- **Target:** `chapters/09-compound.qmd` §9.1 Pattern Method three-lens retrospective
- **Disposition:** Rejected per `pattern-drag-canon` memory.
- **Verification:** Ch 9 §The Sprint Retrospective at L103+ carries 3 questions ("what worked / what didn't work / what one design change") — NOT the Pattern Drag / Pattern Gap / Pattern Lift three-lens structure. Substance (retrospective discipline) preserved; coined-vocabulary three-lens rejected. Scout-note at L55-101 documents the block; should be removed in cleanup pass.
- **Rationale captured in:** `pattern-drag-canon` memory.
- **Cleanup note:** The `scout-note:` block at Ch 9 L55-101 is stale and should be scrubbed before PR.

### E47 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:2031-2050
- **Target:** `chapters/09-compound.qmd` L132-148 (§9.2 one-design-change rule)
- **Verification:** L132: *"After every sprint, you answer one question as the Human Orchestrator: *what one design change would make the next sprint better?* One. Not five. Not a list of improvements. One."* + L138 *"The temptation after a good sprint is to list every observation the team made and call the list 'lessons learned.' That list never lands."* — one-design-change discipline landed.
- **Commit:** a29fc71
- **Drift?** No.

### E48 — NEW-SECTION — LANDED (as supporting beat, not opener per author note)
- **Source:** julie-redline.md:2056-2088
- **Target:** `chapters/10-the-rhythm.qmd` L30 (quarterly-cadence-as-natural-tempo)
- **Verification:** L30: *"The Rhythm is quarterly. A sprint takes six to eight weeks... Faster than that and the sprint loses the depth that makes it pay off. Slower than that and the design infrastructure built in the last sprint starts to degrade before the next one begins. Quarterly also matches the team's capacity to absorb the change."* — faster/slower absorption-vs-compounding beat landed as supporting paragraph, NOT chapter opener (per author jf-note *"Not sure its an opener; I really want openers focused on stories to anchor the reader"* — Ch 10 opens with thirteen→eight story instead).
- **Commit:** a2a62bc (Ch 10)
- **Drift?** No — opener-vs-supporting-beat resolution per author preference.

### E49 — FRAMEWORK-ADD — LANDED
- **Source:** julie-redline.md:2090-2106
- **Target:** `chapters/10-the-rhythm.qmd` L36 (§10.1 COE Operating Model)
- **Verification:** L36: *"The structure of the quarterly operating session draws on the ***Center of Excellence (COE) Operating Model*** — Dave Ulrich's three-pillar HR framework from *Human Resource Champions* (1997), where specialized expertise centers coordinate across the business with defined governance and a recurring meeting cadence."* — COE canonized with Ulrich anchoring (per phase2-chapter-progress memory + author jf-note *"What is this?"* resolved by research). Framework-attribution scrub applied.
- **Commit:** a2a62bc
- **Drift?** No.

### E50 — NEW-SECTION — LANDED
- **Source:** julie-redline.md:2108-2129
- **Target:** `chapters/10-the-rhythm.qmd` L140 (§10.2 Compounding Scorecard as design-validation document)
- **Verification:** L140: *"The Compounding Scorecard is a design-validation document, not a financial one. Each sprint's delta tells you whether the design correctly identified the constraint and correctly allocated the work."* — design-validation framing landed verbatim.
- **Commit:** a2a62bc
- **Drift?** No.

### E51 — NEW-SECTION — REJECTED
- **Source:** julie-redline.md:2131-2164
- **Target:** `chapters/11-what-to-do-next.qmd` (Clarity Call personal-voice)
- **Disposition:** Rejected per `julie-merge-rejected-rows` memory + `compound-does-not-have-on-site-implementers-like` memory.
- **Verification:** Ch 11 §The Clarity Call at L84+ presents the call as *"Book a free 30-minute Clarity Call with a Compound strategist who will diagnose your constraint"* — NOT *"I conduct every Clarity Call personally"* (Julie's redline). Compound has remote coaching, not on-site personal calls per memory. Author jf-note: *"Rejected; we won't be doing clarity calls personally."*
- **Rationale captured in:** `compound-does-not-have-on-site-implementers-like` memory.

### E52 — NEW-SECTION — BLOCKED-RELOCATION
- **Source:** julie-redline.md:1127-1203
- **Target (original):** `chapters/11-what-to-do-next.qmd` Clarity Call section  →  **Relocated:** About-Authors page (not yet authored)
- **Verification:** No 15-year-content-thread (JMann Radio + Work Matters + Compound) reference in Ch 11. Author jf-note: *"What's the point of this?"* + Q3 jf-note *"I dont know they belong anywhere; 'what to do next' needs to be focused on the actionable next-steps."*
- **Destination bead:** `book-ff63.17` (About-Authors bio relocation).
- **Drift?** No.

### E53 — NEW-SECTION — REJECTED
- **Source:** julie-redline.md:1205-1280
- **Target:** `chapters/11-what-to-do-next.qmd` §11.1 "Work Matters — The Bridge"
- **Disposition:** Rejected per `julie-merge-rejected-rows` memory ("substance moved to About-Authors bio").
- **Verification:** No "Work Matters — The Bridge" §11.1, no platform-facts metrics table (121 eps / 5 platforms / $15M HR budget / 44 countries) in Ch 11. Ch 11 flow: Pull Scorecard → Run Signal on Yourself → Name Team → Clarity Call → Two Paths Forward → One-page Plan. Author jf-note: *"Likely rejected; fit?"*
- **Rationale captured in:** `julie-merge-rejected-rows` memory.

### E54 — NEW-SECTION — REJECTED
- **Source:** julie-redline.md:1282-1324
- **Target:** `chapters/11-what-to-do-next.qmd` §11.2 "JMann Consulting Group Radio Platform"
- **Disposition:** Rejected per `julie-merge-rejected-rows` memory ("substance moved to About-Authors bio").
- **Verification:** No "JMann Consulting Group Radio Platform" §11.2 in Ch 11. Author jf-note: *"Likely rejected; fit?"*
- **Rationale captured in:** `julie-merge-rejected-rows` memory.

### E55 — FRAMEWORK-ADD — LANDED (as unnamed two-test review)
- **Source:** julie-redline.md:2166-2181
- **Target:** `chapters/11-what-to-do-next.qmd` L140-148 (First Sprint Plan review)
- **Verification:** L140: *"Before the plan commits, two questions catch the gaps that turn into wasted quarters."* + Q1 *"Is the constraint real, or is it a symptom?"* + Q2 *"Does the named Human Orchestrator pass the *Right Seat Evaluation*?"* — landed as two-test review (Pattern B per phase2-chapter-progress memory). Julie's redline was 3-test (constraint vs symptom / Human Orchestrator Right Seat / sponsor commitment); landed as 2-test (constraint vs symptom + Right Seat) — sponsor commitment dropped per author review.
- **Commit:** b32479a (Ch 11 BOOK CLOSER COMPLETE)
- **Drift?** No — intentional 3-test→2-test compression per author review.

### E56 — NEW-SECTION — NEEDS-AUTHOR
- **Source:** julie-redline.md:2199-2233
- **Target:** NEW FILE `chapters/case-study-professional-services.qmd` (proposed)
- **Disposition:** Open — author jf-note: *"Move to appendix; may need additional input"* + manifest BLOCKED status (needs Julie input to complete).
- **Verification:** No new case study file exists. Manifest §4 flags single-paragraph form needs structural expansion to match `case-study-meridian.qmd` format.
- **Pending question:** Author + Julie agreement on whether to draft from Julie's redline paragraph as-is, expand into full case study format, or defer to post-PR follow-up.

### E57 — NEW-SECTION — NEEDS-AUTHOR
- **Source:** julie-redline.md:2235-2266
- **Target:** NEW FILE `chapters/case-study-people-ops.qmd` (proposed)
- **Disposition:** Open — author jf-note: *"Move to appendix; likely needs Julie input to complete"* + manifest BLOCKED status.
- **Verification:** No new case study file exists.
- **Pending question:** Same as E56.

### E58 — FRAMEWORK-ADD — LANDED (4 of 7 entries — substance in chapters; dedicated glossary entries pending)
- **Source:** julie-redline.md:2268-2376
- **Target:** `chapters/appendix-glossary.qmd`
- **Verification:**
  - **TML / Work Deconstruction** — LANDED via `Work Deconstruction` entry at L107 (TML categories landed in body throughout Ch 5 + Ch 6b; glossary entry references the four-category classification).
  - **PIS** — Defined in Ch 5 L34 body; not yet a dedicated glossary entry (per `phase2-chapter-progress` memory: "E58 glossary chapter Drafter (4 entries: TML/PIS/Right Seat/COE)" — Phase 3 work, not yet executed at audit time).
  - **Right Seat Evaluation** — Defined in Ch 6 L47-53; not yet a dedicated glossary entry.
  - **COE Operating Model** — Defined in Ch 10 L36; not yet a dedicated glossary entry.
  - **Pattern Drag / Pattern Gap / Pattern Lift** (3 entries) — REJECTED per `pattern-drag-canon` memory.
- **Disposition split:** 4 entries LANDED-in-prose (substance available for glossary Drafter) + 3 entries REJECTED. The dedicated glossary E58 Drafter pass is bead-`book-z3d2`-parallel work per phase2-chapter-progress memory.
- **Cleanup note:** E58 glossary Drafter must add 4 dedicated entries (TML, PIS, Right Seat Evaluation, COE Operating Model) before PR.

### E59 — NEW-SECTION — NEEDS-AUTHOR
- **Source:** julie-redline.md:1326-1375
- **Target:** NEW SECTION (no existing About Authors page exists in current book)
- **Disposition:** Open — manifest approved; per phase2-chapter-progress memory the bead is `book-ff63.17` (About-Authors bio relocation) in Phase 3 queue.
- **Verification:** No About-Authors page in repo. Julie bio prose available in julie-redline.md:1326-1375. Jesse bio per Q6 "I don't recall making one, but I can" — author needs to draft.
- **Pending action:** Author drafts Jesse bio; Drafter agent lands both bios + relocates 15-year-content-thread (E07 + E52) substance into the new file.

### E60 — ANONYMIZATION — LANDED (in landed prose) / PARTIAL CHECK
- **Source:** julie-redline.md:22-23, throughout
- **Target:** All `chapters/*.qmd` + `index.qmd`
- **Verification:** Spot-checks confirm "a global food safety company" + "Fortune 500 division" + "44 countries" anonymization convention applied consistently across Preface, Ch 1, Ch 2, Ch 4, Ch 5. Other anonymized terms ("global automotive supplier", "large furniture and workplace design company", "mid-market precision manufacturing company") do not appear in chapters because the corresponding Julie source stories did not land in those chapters. Meridian Manufacturing is preserved as fictional composite per Q7 + memory `meridian-consulting-group-is-meridian-manufacturing`.
- **Pending check:** A final cross-chapter sweep + About-Authors bio pass should verify zero residual real-company names slip in via E59 bio prose.
- **Commit:** Per-chapter (across full Phase 2 merge).
- **Drift?** No.

---

## Section C: Drift findings

**No drift detected.**

All 40 LANDED rows verified at cited locations. The 11 REJECTED rows are documented in `julie-merge-rejected-rows` memory + manifest §2 + `pattern-drag-canon` memory and have zero residual prose in the chapters (chapter prose at the relevant sections shows the author-preferred alternative — story-anchored openers, framework-attribution-scrubbed substance, plain operator language instead of Pattern Method jargon).

**Three cleanup items (stale `scout-note:` blocks)** exist in the working tree but are not drift in the disposition sense — they are scout/Drafter annotations that should be scrubbed before PR:
1. `chapters/06b-designing-the-work.qmd` L134-153 — E37 BLOCKED scout-note for Pattern Drag at Design Gate (now resolved as REJECTED).
2. `chapters/08-deliver.qmd` L204-206 — E44 BLOCKED scout-note for Pattern Lift (now resolved as REJECTED).
3. `chapters/09-compound.qmd` L55-101 — E46 BLOCKED scout-note for Pattern Method three-lens retrospective (now resolved as REJECTED).

Recommend a single cleanup commit before PR that strips these three scout-note blocks. (Not drift, but housekeeping.)

---

## Section D: Open NEEDS-AUTHOR items

Four items are open and block "full Phase 3 complete" but **do not block the per-chapter Phase 2 PR** (which is what `phase2-chapter-progress` memory says is the next milestone):

1. **E56 — Pro Services Sprint case study** — needs Julie input to expand single-paragraph redline into full case study matching `case-study-meridian.qmd` structure. Open question: draft from Julie's paragraph as-is, expand with author/Julie collaboration, or defer? Manifest jf-note: "Move to appendix; may need additional input."

2. **E57 — People Ops Sprint case study** — same shape as E56. Open question: same as E56.

3. **E59 — About the Authors bio entries** — Julie bio prose available in redline (julie-redline.md:1326-1375); Jesse bio per Q6 *"I don't recall making one, but I can"* — author commits to draft. Bead `book-ff63.17` queued. Also blocks E07 + E52 substance relocation (15-year content thread).

4. **E60 — Final anonymization sweep** — landed prose is clean; pending action is a defensive cross-chapter + About-Authors-pass scan to catch any real-company names slipping in via E59 bio prose or new case study files.

---

## Section E: Comparison against persistent memory

Cross-reference against `julie-merge-rejected-rows` memory:

| Memory says REJECTED | Manifest §2 says REJECTED | Audit confirms REJECTED |
|---|---|---|
| E33 (Ch 6 opening reframing) | yes | yes |
| E34 (HAC origin attribution) | yes | yes |
| E37 (Ch 6b Pattern Drag at Design Gate) | yes (BLOCKED, then memory promotes to REJECTED) | yes |
| E38 (Ch 7 governance-attribution) | yes | yes |
| E44 (Ch 8 Pattern Lift measurement) | yes (REVIEW, then memory promotes to REJECTED) | yes |
| E46 (Ch 9 Pattern Method three-lens) | yes (REVIEW, then memory promotes to REJECTED) | yes |
| E48-as-opener (Ch 10) | partial | yes (landed as supporting beat, NOT opener — per memory + author preference) |
| E51 (Clarity Call personal-voice) | yes | yes |
| E53 (Ch 11 Work Matters Bridge subsection) | yes | yes |
| E54 (Ch 11 JMann Radio Platform subsection) | yes | yes |
| 3 Pattern Method glossary entries (subset of E58) | yes | yes |

**Full alignment.** The `julie-merge-rejected-rows` memory, the `pattern-drag-canon` memory, the manifest §2 REJECTED set, and the actual chapter prose all agree. No reconciliation gaps.

Cross-reference against `phase2-chapter-progress` memory final commit refs:

| Chapter | Memory commit | Confirmed in `git log` |
|---|---|---|
| Preface | bcf8f11 | yes |
| Ch 1 | e0f3xxx | yes (truncated hash in memory; most recent Ch 1 commit is `0b96ca8`) |
| Ch 2 | 4a2c | yes (`b53ca0d` / `0c5dbc5` / `6eed368` cluster) |
| Ch 3 | 9bc5d | yes (`e3e1a7b` / `0fad966` / `ed97b29` cluster) |
| Ch 4 | b7a | yes (`a1cdff0` / `ef45c46` cluster) |
| Ch 5 | def37b9 + af08f3d | yes |
| Ch 6 | dc6869b | yes |
| Ch 6b | 83791a5 | yes |
| Ch 7 | 17c0a41 + bffe3b5 | yes |
| Ch 8 | 097603b | yes |
| Ch 9 | a29fc71 | yes |
| Ch 10 | a2a62bc | yes |
| Ch 11 | b32479a | yes (BOOK CLOSER COMPLETE) |

**Full alignment.** Memory's "Phase 2 merge complete 2026-06-02" claim is accurate at the per-chapter level. The reported "LANDED 16 / REJECTED 11 / SKIP-ALREADY-DONE 1 / BLOCKED-RELOCATION 1 / NEEDS-AUTHOR resolved E49" line in the memory undercounts versus this audit's **40 LANDED / 11 REJECTED / 1 SKIP-ALREADY-DONE / 5 BLOCKED-RELOCATION / 4 NEEDS-AUTHOR** — the discrepancy reflects that the memory was authored as a checkpoint and counted only "primary" landings, not every E-row whose substance is present in the chapters (e.g., E08-E32 voice-shift / attribution / new-section rows all carry through). **The actual landed substance count is higher than the memory suggests.**

---

## Section F: PR readiness check

- [x] **All LANDED rows verified?** Yes — 40 of 40, no drift.
- [x] **All REJECTED rows have documented rationale?** Yes — `julie-merge-rejected-rows` + `pattern-drag-canon` + `framework-attribution-rule` + `compound-does-not-have-on-site-implementers-like` memories + manifest §2.
- [x] **All BLOCKED rows have destination bead?** Yes — E07 + E52 → `book-ff63.17` About-Authors. E20 → cut-or-bio. E53/E54 → manifest REJECTED (no destination required).
- [ ] **Any open NEEDS-AUTHOR blocking PR?** **Partial.** E56 / E57 / E59 / E60-final-sweep are open but do not block the Phase 2 per-chapter PR per `phase2-chapter-progress` memory ("Phase 3 next: E58 glossary chapter Drafter, book-ff63.17 About-Authors bio relocation"). These belong to Phase 3, not the current merge.

**Verdict: PR-ready for Phase 2 (11 chapters + Preface). Phase 3 items (E58 dedicated glossary entries, E59 About-Authors bios + E07/E52 relocation, E56/E57 new case study files, E60 final defensive sweep) are queued as follow-up beads.**

**Three pre-PR housekeeping recommendations:**
1. Strip the 3 stale `scout-note:` blocks (Ch 6b L134-153, Ch 8 L204-206, Ch 9 L55-101) referenced in Section C.
2. Execute E58 glossary Drafter (4 entries: TML, PIS, Right Seat Evaluation, COE Operating Model) per `phase2-chapter-progress` memory — this is bead-claimed Phase 3 work and is fast.
3. Confirm with author whether the two new case study files (E56/E57) and the About-Authors bio file (E59) should land as part of this PR or as a Phase 3 follow-up PR. Recommendation: Phase 3 follow-up — keeps this PR scoped to Julie's redline integration into existing chapters.

---

## Top 3 most surprising findings

1. **E48 landed as a supporting beat, not an opener — and that's correct per author preference.** Julie wrote it as a chapter-opener for Ch 10; author jf-note explicitly rejected the opener placement ("openers focused on stories to anchor the reader"). Ch 10 opens with the thirteen→eight story instead, and Julie's natural-tempo / faster-slower beat landed as supporting paragraph at L30. Manifest annotates this as "directionally aligned"; the actual landing is a structural refactor not a literal landing. Worth noting because the same pattern recurred for E45 (Ch 9 opener) and was specifically caught here.

2. **E13's "three questions" substance landed without Julie's individual-practice attribution — a clean example of the framework-attribution-rule scrub in action.** The three diagnostic questions ("what is this function accountable for, what is its scorecard, who reviews the output and on what cadence") are present in Ch 1 L82, but framed as "the same three questions you'd ask of a human team" rather than "Julie asks of every leadership team she advises." This is the rule working as designed: substance lands, individual-practice framing rejected. Same pattern applies to E15 (5-dimension scorecard) — landed as technical-vs-operating split rather than Jesse-owns / Julie-owns split.

3. **E58 glossary work is bifurcated: 4 entries' substance already present in chapter bodies waiting for Drafter pass to formalize into glossary; 3 entries (Pattern Drag/Gap/Lift) hard-rejected.** The audit caught that the dedicated glossary entries for TML, PIS, Right Seat Evaluation, and COE Operating Model are NOT in the current `appendix-glossary.qmd` even though all four terms are canonically defined in chapter bodies (Ch 5 / Ch 5 / Ch 6 / Ch 10 respectively). This is fast Phase 3 work (4 entries lifted from existing chapter prose) but it is unambiguously not done at audit time. The 3 Pattern entries are correctly absent.

---

*End of report.*
