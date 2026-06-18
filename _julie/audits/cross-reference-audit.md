# Cross-Reference Integrity Audit — Phase 3 Audit 4

**Generated:** 2026-06-05  ·  **Bead:** book-z136  ·  **Agent:** Cross-Reference Auditor (Phase 3 / Audit 4)

## TL;DR

Audited every cross-reference in the merged manuscript: ~155 explicit "Chapter N" references, ~25 "previous/next chapter" links, ~70 numerical references ("the four questions," "the five-item checklist," etc.), and the full glossary "First introduced: Chapter X" set (49 entries). The cross-reference layer is in strong shape overall — most named-chapter pointers resolve cleanly and the "First introduced" metadata in the glossary is internally consistent. **Five real findings** surfaced, ranging from severity HIGH (a four/five mismatch that contradicts the canonical Done Test) to severity LOW (a chapter pointer that names a single chapter for a story now split across two). Net assessment: PR-ready with one mandatory fix (the appendix Done-test count) and four small fixes to land cleanly.

## Per-chapter findings

### Preface (index.qmd)
- Forward references: zero explicit "Chapter N" references. Implicit forward ("six-step Sequence: Signal, Source, Design, Build, Deliver, Compound — and the sprint structure to run it" — L15) — resolves to Ch3.
- Backward references: N/A.
- Verification: **PASS** — no broken references.

### Chapter 1 — Diagnosis (01-diagnosis.qmd)
- Forward references: "Skip to Chapter 4 and run the Sprint" (L240); "The next chapter defines the Co-Intelligent Company" (L278); "the full case study is in the appendix" (L244, points to case-study-meridian.qmd).
- Verification: **PASS**. Ch4 is "Signal" (the right destination for "run the Sprint"); Ch2 is "Co-Operating Model" which defines the Co-Intelligent Company (verified Ch2 L24, glossary L29).
- Five Readiness dimensions named (L122, L256, L288): Constraint Clarity, Information Readiness, Workflow Visibility, Decision Rights, Measurement Discipline. Matches Ch1 scorecard table and appendix-prompts L13. **Internally consistent.**

### Chapter 2 — Co-Operating Model (02-co-operating-model.qmd)
- Forward references: "A Compound Sprint (defined in the next chapter)" (L28) → Ch3 defines Sprint. **PASS.**
- "Chapter 5 introduces the full design instrument — the TML framework" (L259). **PASS** — Ch5 L24-28 introduces TML.
- "The next chapter gives you the *how* — the Framework... the Sequence of six stages..." (L291) → Ch3. **PASS.**
- "Meridian Manufacturing from Chapter 1" (L156). **PASS** — Ch1 L246 introduces Meridian.
- Marketing lead "four agents" / "four-tab setup" (L202, L204, L212, L218). Internally consistent.

### Chapter 3 — The Framework (03-the-framework.qmd)
- "Signal in Chapter 4" (L54). **PASS.**
- "Meridian Manufacturing from Chapter 1" (L153). **PASS.**
- "You will see it in full in Chapter 6" (L196) — refers to the project coordinator story walking all six stages. **PARTIAL** — Ch6 has the Source/Design portions (L10-14, L66, L105, L182) and Ch6b extends with Work Deconstruction (L37-51), but the *full six-stage walkthrough* most thoroughly appears in `case-study-pm-agent-team.qmd`. The "Chapter 6" pointer is structurally OK (Ch6 covers the bulk of the in-narrative story) but reader expecting all-six-stages will find the most complete version in the case study. See cross-cutting finding F5.

### Chapter 4 — Signal (04-signal.qmd)
- "That is Chapter 5" (L226). **PASS** — Ch5 is Source.
- "five constraint questions" (L149, L151, L203, L211): five questions listed L153-168. **PASS.**
- "Step 1" through "Step 5" (L128, L145, L149, L175, L186). All present, all numbered correctly. **PASS.**
- The constraint-statement template (L114-120) has **five fields**: Constraint, Where it lives, Duration, Quantified cost, Validating evidence. Reflection Question 4 (L233) says "all *four* fields... constraint sentence, location, duration, and quantified cost with math" — this omits "Validating evidence." See finding F4.

### Chapter 5 — Source (05-source.qmd)
- "Chapter 6, where TML becomes the lens for deconstructing what each role actually does" (L28). **PASS** — Ch6b L31, L40 use TML for Work Deconstruction.
- "the section 'How systems talk to each other' later in this chapter" (L61). **PASS** — section header at L127 (markdown-emphasized variant: "How systems *talk to each other*").
- Three TML layers (Task, Management, Leadership): consistent across L24-28, L81, and glossary L117.

### Chapter 6 — Designing the System (06-designing-the-system.qmd)
- "Hybrid Accountability Chart" introduced here per glossary L69 ("First introduced: Chapter 6"). **PASS.**
- "You met a version of this role in Chapter 2 — our marketing lead running four agent teams" (L182). **PASS** — Ch2 L202-204 has four agents.
- "Meridian Manufacturing's quoting workflow from the previous chapters" (L225). **PASS** — Meridian introduced Ch1, deepened in Ch3-5.
- "The next chapter introduces the Design Brief in detail" (L216) → Ch6b L101-119 has Design Brief. **PASS.**
- "The next chapter covers the work itself — Work Deconstruction, populated examples, prototyping, the Design Brief, and the gate checklist" (L253) → Ch6b delivers all of these. **PASS.**
- "five connection patterns (skills on SOPs, RAG, data pipelines, low-code integration, service layer)" (L258) → five enumerated L101-109. **PASS.**
- "four questions" for HAC (L34, L60, L257); "five questions to answer for every agent team" (governance, L157); "Right Seat Evaluation" — three tests (L47-51). All counts verified.

### Chapter 6b — Designing the Work (06b-designing-the-work.qmd)
- "The previous chapter designed the system" (L5, L8). **PASS** — Ch6 is "Designing the System."
- "the *Hybrid Accountability Chart* you built in the previous chapter" (L34). **PASS.**
- "TML framework from Source" (L14). **PASS.**
- "The next chapter is Build" (L157); "Design Brief connects directly to the Build Spec in the next chapter" (L117). **PASS** — Ch7 is Build with Build Spec.
- Five-item Design Gate (L140-146, L152, L163). Five items present and verified.
- TML classification: 3 categories (Task / Management / Leadership) consistent with Ch5.

### Chapter 7 — Build (07-build.qmd)
- "from Chapter 2" (L90) re marketing lead's four-agent setup. **PASS.**
- "the Compound Sprint from Chapter 3" (L185, L195). **PASS.**
- "the Design Brief from the previous chapter" (L206) → Ch6b. **PASS.**
- "five questions answered" / "Done test is five questions" (L191, L324, L338). Five questions listed L326-330. **PASS internally** — but appendix-action-steps L245 says "four-question test" for this same Build Done test. See finding F1 (highest priority).
- Eight-section Build Spec (L208-217). Eight sections present and numbered.
- Seven-item Implementation Mistakes Checklist (L250-264). Seven items present and numbered.
- Seven-question Guardrails Checklist (L277-283). Seven items present and numbered.
- TODO comment at L113 (open editorial flag re: formal definition of "agent"). Not a cross-reference failure but flagged for completeness — see finding F3.
- L8 "five agents that replaced our $24,000-a-year coordinator role" then L10 enumerates only three illustrative examples (client-facing, internal reports, subcontractor routing). The case study `case-study-pm-agent-team.qmd` (L273, L302, L355) confirms five agents total. **PASS** — text says "Five agents, five different access levels" and the case study backs the count; the three named examples at L10 are illustrative, not enumerative.

### Chapter 8 — Deliver (08-deliver.qmd)
- "the retrospective belongs to Compound, and that's the next chapter" (L108). **PASS** — Ch9 is Compound.
- "In Chapter 5, I described a client whose AI kept surfacing expired information" (L123). **PASS** — Ch5 L227-229 has this story.
- "That's the next chapter" (L232) re Compound. **PASS.**
- Four-gate Deploy Readiness Audit (L43-50, L236). Four gates verified.
- Four-question per-role check (L71). Four numbered questions L73-76.
- Four log categories (L116-121). Four categories verified.

### Chapter 9 — Compound (09-compound.qmd)
- "the living document I'll describe in the next chapter — the Hybrid Org Today" (L44). **PASS** — Ch10 L82-92 introduces Hybrid Org Today.
- "The coordinator's knowledge base I described in the Design chapter" (L174). **PASS** — Ch6/6b cover the coordinator design.
- "The numbers in the next chapter — thirteen people to eight" (L174). **PASS** — Ch10 L8-10 delivers that detail.
- "the same three questions every time" (L56) — three retro questions listed L58-64. **PASS.**
- "three compounding questions" (Reflection L201) — three listed L75-83. **PASS.**
- "Four questions drive the re-rank" (L114) — four listed L116-122. **PASS.**

### Chapter 10 — The Rhythm (10-the-rhythm.qmd)
- "The Hybrid Accountability Chart from Chapter 6" (L84). **PASS** — Ch6 introduces HAC.
- "The Co-Operating Model from Chapter 2" (L166). **PASS** — Ch2 is the Co-Operating Model.
- "The next chapter is about the one thing Compound does that you should not run alone" (L239). **PASS** — Ch11 is "What to Do Next" with the Clarity Call and Path B (work with Compound).
- "four steps" / "Step 1" through "Step 4" of quarterly session (L34, L38, L40, L42, L44, L57, L114, L134). Four steps verified.
- COE Operating Model — Dave Ulrich, *Human Resource Champions* (1997). Matches glossary L18.

### Chapter 11 — What to Do Next (11-what-to-do-next.qmd)
- "In Chapter 1 you took the AI Readiness Scorecard" (L28). **PASS** — Ch1 L122+ defines it.
- "go back to Chapter 1 and do it now" (L38). **PASS.**
- "the full Signal process from Chapter 4" (L51, L100). **PASS.**
- Sequence chapter map (L114-119): Signal=Ch4, Source=Ch5, Design=Ch6, Build=Ch7, Deliver=Ch8, Compound=Ch9. **PASS** — every mapping verified against `_quarto.yml`.
- "the quarterly rhythm from Chapter 10" (L121). **PASS.**
- "the three-criteria *Right Seat Evaluation* from Chapter 6 (*Sees It*, *Wants It*, *Suited for It*)" (L146). **PASS** — Ch6 L47-51 introduces it.
- "Three questions" minimum viable Signal (L51) — three present at L52-65 (constraint candidate, location, cost).

### Appendix: Glossary (appendix-glossary.qmd)
- All 49 entries with "(First introduced: Chapter X)" tags spot-checked. Examples:
  - **AI Readiness Scorecard** → Ch1 ✓
  - **Co-Operating Model** → Ch2 ✓
  - **Compound (stage)** → Ch3 ✓ (Sequence introduced Ch3)
  - **TML framework** → Ch5 ✓ (L80 dual cite "Ch5 / Ch6b" — correct: Source uses TML on knowledge, Design uses TML on work)
  - **Work Deconstruction** → Ch6b ✓
  - **Design Brief** → Ch6b ✓
  - **Design Gate** → Ch6b ✓
  - **Hybrid Accountability Chart** → Ch6 ✓
  - **Right Seat Evaluation** → Ch6 ✓
  - **Signal Backlog** → Ch9 ✓ (introduced in Compound)
  - **Sprint Retrospective** → Ch9 ✓
  - **Hybrid Org Today** → Ch10 ✓
  - **Compounding Scorecard** → Ch10 ✓
  - **Clarity Call** → Ch11 ✓
  - **Meridian Manufacturing** → "Case Studies" ✓
- **Verification:** PASS for all spot-checked entries. The glossary's "First introduced" metadata is the cleanest part of the cross-reference layer.
- One minor wording: glossary entry for **QA / Quality Assurance** (L196) describes the Done test as "four questions answered against last week's actual data" — but Ch7 defines the Done test as **five** questions. See finding F1.

### Appendix: Action Steps (appendix-action-steps.qmd)
- Per-chapter section headers (## Chapter 1 through ## Chapter 11) all match the canonical chapter titles and sequence in `_quarto.yml`. **PASS.**
- "go back to Chapter 1 and do it now" (L311). **PASS.**
- "you'll sharpen it in Chapter 4" (L100). **PASS.**
- **L196:** "Sort each one into the **four categories**" — describes Work Deconstruction with four categories, but Ch6b (the chapter this index is mirroring) uses **three TML categories** (Task / Management / Leadership). Mismatch with the canonical framework. See finding F2.
- **L245:** "Run the full **four-question** test" — refers to the Build Done test, which Ch7 L324 and L338 define as **five** questions. See finding F1.

### Appendix: Prompts (appendix-prompts.qmd)
- "Chapter 1" through "Chapter 10" pointers for each prompt (L18, L69, L144, L191, L238, L321, L377, L448, L505, L577, L658, L746, L819, L877, L927, L989, L1054, L1113, L1171). All resolve correctly to the right home chapter. **PASS.**
- **L377:** "Work Deconstruction classifies every task in the constraint workflow into **four categories**: Human judgment required, Agent-assisted, Fully automatable, Workflow automation only." The prompt body (L399-412) elaborates these as the four labels.
  Canonical framework in Ch5/Ch6b is the **three-category TML framework** (Task / Management / Leadership). This is the most substantive framework drift in the manuscript. See finding F2 (HIGH).

### Appendix: Prompt Engineering (appendix-prompt-engineering.qmd)
- Five-layer context stack (Layer 1-5). Self-contained, internally consistent.
- "The Knowledge Map tells you what goes in the stack" (L82). **PASS** — Knowledge Map defined in Ch5.
- "Source Classification" axes (L84): "two axes — structured vs. unstructured, durable vs. ephemeral — and the three AI tiers." Matches Ch5 L97-111. **PASS.**

### Case Study — Meridian (case-study-meridian.qmd)
- "what the Source chapter calls the transcript extraction" (L302). **PASS** — Ch5 L178-186 has the transcript discussion.
- Numbers consistent with chapter references: 27 employees, $7.2M revenue, $558K cost, 147 pricing rules cleaned to 112. All match.

### Case Study — PM Agent Team (case-study-pm-agent-team.qmd)
- "If you've read the framework chapters" (L3) — no specific chapter pointer; resolves to whole-book context. **PASS.**
- Five-agent count (L3, L273, L302, L355) consistent with Ch7 L8.

## Cross-cutting findings

### Broken references (must fix)

**(none of the strict "broken" / "404" variety — every named chapter pointer resolves to a real chapter that contains the referenced material at the right level of detail. The findings below are all numeric-count or framework-drift mismatches.)**

### Stale references (wrong chapter number)

**(none)**

### Missing forward-references (promised but not delivered)

**(none)**

### Numerical mismatches

**F1 (HIGH) — Build Done test count mismatch (four vs. five).**
- **Canonical:** Ch7 L324 and L338 define the Done test as **five questions** (listed L326-330). Ch7 L191 also says "five questions answered."
- **Stale references:**
  - `appendix-action-steps.qmd:245` — "Run the full **four-question** test."
  - `appendix-glossary.qmd:196` — Glossary entry for **QA / Quality Assurance** says "the 'Done test' in Build: **four** questions answered against last week's actual data."
- **Recommended fix:** change both to "five-question test" / "five questions answered." Mirrors the L191 cascade-miss spirit of the Ch7 EC catch.

**F2 (HIGH) — Work Deconstruction category count: three TML vs. four legacy.**
- **Canonical:** Ch5 L24-28, Ch6b L31 & L40, and glossary L117-120 all define Work Deconstruction as classifying tasks into **three TML categories** (Task / Management / Leadership).
- **Stale references using the older four-category schema:**
  - `appendix-prompts.qmd:377` — "Work Deconstruction classifies every task in the constraint workflow into **four categories**: Human judgment required, Agent-assisted, Fully automatable, Workflow automation only." The full prompt body L399-412 elaborates the same four labels.
  - `appendix-action-steps.qmd:196` — "Sort each one into the **four categories**" (no labels listed, but matches the legacy schema).
- **Recommended fix:** rewrite both to use the three TML categories (Task / Management / Leadership) and align the labels with the canonical chapter framework. This is the largest substantive framework-drift in the manuscript.

**F4 (LOW) — Constraint statement field count: four vs. five.**
- `04-signal.qmd:233` Reflection Question 4 says "all **four fields** of the one-page constraint statement template — constraint sentence, location, duration, and quantified cost with math."
- Canonical template (L114-120) has **five fields**: Constraint, Where it lives, Duration, Quantified cost, **Validating evidence**.
- **Recommended fix:** change to "all five fields" and add "validating evidence" to the question, or explicitly note "the four data fields" while leaving evidence out as a deliberate framing.

### Section reference drift

**(none — no "§" or numbered-section references appear in the manuscript; the one "later in this chapter" intra-chapter pointer in Ch5 L61 resolves correctly to L127.)**

### Other editorial findings

**F3 (LOW / editorial) — Live TODO in Chapter 7.**
- `07-build.qmd:113` contains an HTML comment: `<!-- TODO: Verify 'agent' is formally defined in Ch02 or glossary. Ch02 has a working definition ("an AI system that holds a goal, takes a sequence of steps toward it...") — confirm this is sufficient or add a formal definition to the glossary. -->`
- Not a broken reference, but a flag the author still owes themselves. Verified Ch2 has the working definition. Glossary at appendix-glossary.qmd does **not** currently have a standalone "Agent" entry. The TODO should be resolved (either by adding a glossary entry or by removing the comment after confirming Ch2's definition suffices).

**F5 (LOW) — "Chapter 6" pointer for full six-stage coordinator walkthrough.**
- `03-the-framework.qmd:196` says the project coordinator story "walks all six stages in sequence. You will see it in full in Chapter 6."
- Ch6 covers Source/Design slices of the story (L10-14, L66, L105, L182). Ch6b adds Work Deconstruction (L37-51). The most complete six-stage walkthrough lives in `case-study-pm-agent-team.qmd`.
- **Recommended fix:** either (a) point to "Chapter 6 and the PM Agent Team case study" or (b) leave as-is on the understanding that Ch6 holds the in-narrative depth and the case study is the deeper-dive companion. Low priority — the reader will not be lost.

## Highest-priority surgical fixes

1. **F1 / appendix-action-steps.qmd:245** — change "four-question test" → "five-question test."
2. **F1 / appendix-glossary.qmd:196** — change glossary QA entry from "four questions answered" → "five questions answered."
3. **F2 / appendix-prompts.qmd:377-412** — rewrite Work Deconstruction prompt header and prompt body to use the three-category TML framework (Task / Management / Leadership) instead of the legacy four-category schema. The prompt is currently teaching a different framework than the chapter it cites.
4. **F2 / appendix-action-steps.qmd:196** — change "Sort each one into the four categories" → "Sort each one into the three TML categories — Task, Management, Leadership" (mirrors Ch6b L31 phrasing).
5. **F4 / 04-signal.qmd:233** — change Reflection Question 4 from "all four fields ... constraint sentence, location, duration, and quantified cost with math" → "all five fields ... constraint sentence, location, duration, quantified cost with math, and validating evidence" (or add "validating evidence" as a fifth item).

## Verdict

**PR-ready with one mandatory framework-drift cleanup.**

The chapter-pointer layer (the explicit "Chapter N" references and the "First introduced" glossary metadata) is in excellent shape — none of the named-chapter pointers resolve to the wrong chapter, and every "next chapter / previous chapter" arrow lands on the right content.

The five real findings are concentrated in the **appendices** (prompts + action steps + glossary) where the canonical numbered frameworks drifted out of sync with the body chapters during the Julie merge. The **highest-impact fix** is F2 — the Work Deconstruction prompt is currently teaching readers a four-category schema that does not appear anywhere in the body chapters; this would actively confuse a reader running the prompt after reading Ch5/Ch6b.

F1 (Done test four vs. five) appears twice (action steps + glossary), so it is also worth landing before PR.

F3-F5 are LOW severity and can be deferred or batched with other editorial passes.

Recommendation: land F1 + F2 before PR (a 5-minute Edit batch). F3-F5 can ride with the next editorial pass.
