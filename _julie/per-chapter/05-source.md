# Scout Plan — `chapters/05-source.qmd` (Ch 5: Source)

**Generated:** 2026-05-31  ·  **Bead:** book-ff63.9.6  ·  **Scout:** Sage

## Chapter context (one paragraph)

Ch 5 is the **second stage chapter** — Ch 4 named the constraint (Signal), Ch 5 maps the information environment around it (Source). The canonical deliverable of Source is the **Knowledge Map** — a one-page six-column table (Source, Type, Owner, Status, Pipeline, Notes) inventorying every digital system, person, and gap relevant to the constraint, defined at §5.1 / L24–L66 and instantiated as Meridian's completed Knowledge Map in §5.6 (Sprint · Source at Meridian) at L151–L163 and the populated table at L205–L213. The chapter opens (per `6c99346` commit, "Cross-book coherence pass: Meridian threading, terminology fixes, fabrication replacement") with the **Marina + $24K project coordinator** scenario at L8–L14 — the canonical polished replacement that came out of the cross-book coherence work. This is the same Marina story that opens Ch 2 at L8–L10 (with E16 attribution already landed) and the same $24K coordinator anchor that opens Ch 4 at L8–L16 (with E24 / E25 attribution already landed). The chapter introduces several canonical artifacts and instruments: **Knowledge Map** (canonical Source deliverable, In Brief at L5 + §5.1 at L24–L66 + Meridian populated table at L205–L213), **Data Pipeline Audit** (Pipeline column / fifth column of the Knowledge Map, defined at L41 + §5.3 "How systems talk to each other" at L96–L116 with API / MCP / Connector / Pipeline status definitions), the **three-pass build discipline** (Pass 1 Digital / Pass 2 Organic / Pass 3 Missing at L41–L62), the **source classification** axes (Structured vs. unstructured, Durable vs. ephemeral, three AI tiers at §5.2 L68–L94), the **People don't have APIs** framing (§5.4 at L118–L130 introducing three source categories: Digital / Organic / At-risk), the **transcripts-as-API-substitute** discipline (§5.5 at L132–L149), the **Sprint · Source at Meridian** worked example (L151–L163), the **Knowledge management in an agentic world** framing (§5.7 at L165–L185 with the "garbage in, garbage out" axiom and the SuperWebPros own-company learning at L177), the **completeness test** (six checks at L189–L201), and the **hand off to Design** closer (L217–L223). The chapter currently has **NO TML framework reference** as a knowledge-categorization structure — that lands via E29 inside §5.1. The chapter currently has **NO PIS framework reference** — that lands via E31 inside what will become §5.3 (Source Diagnostic). The chapter currently has **NO Julie-voice paragraphs** — E28 (parallel global food safety company tribal-knowledge inheritance story), E30 (senior pricing strategist At-Risk Source story), E31 (PIS framework), and E32 (Missing sources column framing) all introduce her voice for the first time in Ch 5. The most recent commits touching this chapter are `124f777` (excalidraw shortcodes wired in — five diagrams across the chapter), `7709ea8` (author review round 2, resolving 33 jf-notes across 8 chapters including Ch 5), `6c99346` (cross-book coherence pass — when the Marina opener and PM Agent Team threading landed), `48cef93` (Bench / Skills Library purge — verified clean), and `7dad7b5` (editorial pass: In Brief placement, callout spacing). Per stale-audit: **Marina opener at L8 is the polished sourced replacement** (no nine-red-weeks / fabricated regressions); Meridian threading at L155–L213 is canonical and cross-references Ch 1 (Headcount Paradox / SuperWebPros 13→8), Ch 3 (Sprint Planning Canvas / Meridian Source row at L165), Ch 4 (PT clinic / $558K quoting bottleneck), Ch 6 (Information flow spec / HAC), and Ch 7 (Build spec). The L130 reference to "the developer who walked out with everything he knew" cross-references the Preface canonical chutes-and-ladders developer story (per `pm-case-study-thread-through-book` and `ahmed-story-is-chutes-and-ladders` persistent memories — Ahmed is the developer's real name, canonically anonymized to "the developer"). Per author manifest annotation: **Overall Approved**; E28 *Approved*; E29 *Requires review*; E30 *Approved*; E31 *Approved*; E32 *Likely approved; requires review*.

## E-row classifications

| E-row | Type | Verdict | Current-chapter target | Notes |
|---|---|---|---|---|
| E28 | ATTRIBUTION + NEW-SECTION | LAND-WITH-MODIFICATION | L8 opener with cascading I→we shifts at L8, L10, L12, L30, L130 (Jesse voice across the chapter); Julie's parallel paragraph lands AFTER L14 (end of Marina opener) and BEFORE L16 (§5.0 "Diagnosis is not done until you know what you *have*" heading) | Apply Q-E21 convention: blended-we with single in-prose attribution; reject inline `Jesse:` and `Julie:` tags; **preserve the Marina / $24K coordinator opener verbatim** (canonical polished replacement per `6c99346`); preserve the L130 chutes-and-ladders developer cross-reference per `ahmed-story-is-chutes-and-ladders` memory (italicize *Chutes and Ladders* as proper noun); Julie's parallel story = global food safety company post-acquisition tribal-knowledge inheritance from senior process experts (twenty-year Fortune-500 institutional memory); HEAVY REWRITE per risk map; **framework-attribution rule N/A** (E28 is biographical parallel, not framework introduction); cross-chapter coherence: must NOT verbatim-echo Preface a global food safety company acquisition phrasing or Ch 1 §1.0 a global food safety company headcount-math phrasing or Ch 2 §2.3 a global food safety company graft-vs-redesign phrasing or Ch 4 §4.0 a global food safety company matrix-reporting phrasing (four prior a global food safety company anchors already established) |
| E29 | FRAMEWORK-ADD | LAND-WITH-MODIFICATION | New paragraph inside §5.1 (Diagnosis is not done until you know what you *have*) AFTER L20 ("Source produces that ground truth..."), BEFORE L22 ("This is why Source belongs in Diagnose..."); OR as a new H3 under §5.1 / §5.2 Knowledge Map titled "Three layers of *knowledge*" or similar | **HIGHEST EC1 canonical-definition risk in the chapter.** TML Framework introduction must match Ch 2 §2.6 reference (L259: "the **TML framework** (Task / Management / Leadership) which sorts work into three categories rather than two") AND manifest E36 canon (Task → Fully Automatable, Management → AI-Assisted, Leadership → Human Judgment). Julie's E29 source presents TML as **knowledge categorization** (Task knowledge = SOPs/process maps, Management knowledge = decision rights/escalation, Leadership knowledge = judgment/relationships/context) — closing clause aligns with canon ("AI can reliably handle Task knowledge, can assist with Management knowledge, and requires human oversight for Leadership knowledge"). **EC1 verdict: PASS WITH MODIFICATION.** The Drafter must: (a) preserve Task/Management/Leadership names exactly; (b) preserve the AI handling mapping (handle/assist/oversight); (c) frame as the **knowledge lens** of the same three-category framework that Ch 6b will apply as the **work lens** (forward reference acceptable). HEAVY REWRITE per risk map; **framework-attribution rule applies directly** (strip "Julie's TML framework" individual attribution per global rule); **A3 triplet risk** (three-layer parallel construction is structurally observational, not constructed — acceptable IF AI-handling mapping uses non-parallel cadence); **A2 risk:** TML is being **first-defined** here in load-bearing form (Ch 2 L259 was a forward-reference), so the definition must be precise enough to support Ch 6b's work-lens application; **forbidden vocab:** "organizational design foundation" → strip per voice charter §3 |
| E30 | NEW-SECTION | LAND-WITH-MODIFICATION | New paragraph inside §5.4 "People don't have *APIs*" AFTER L126 (current at-risk-source paragraph closer "For most operating companies this is the single most consequential thing Source does.") AND BEFORE L128 (the "When you're building your map, ask explicitly..." paragraph) | Julie's senior pricing strategist At-Risk Source story (20 years of customer-specific pricing exceptions captured in 4 weeks before retirement); LIGHT-MED EDIT per risk map analysis (substance is operator-strong: concrete person, concrete window, concrete outcome); **framework-attribution rule applies indirectly** (At-Risk Source is canonical Compound vocabulary at L126 — joint book IP; strip "Julie's M&A integration practice identified a specific pattern" individual framing); **A1 risk:** Julie's source closer "That is what At-Risk Source does: it names what nobody knew they were about to lose." is the AI-tell "this exists to" closer pattern — preserve substance, cut the "That is what" cadence; **A4 (boastful biographical):** moderate risk; mitigated by Preface + Ch 1 + Ch 4 attribution setup; **n-gram coherence:** must NOT verbatim-echo Ch 5 L161 "Dave — Organic, at-risk, four years to retirement with an undocumented estimation method" Meridian beat (parallel structure / "retirement" / "undocumented" risk); **operator-math closer:** the "team had four weeks to work with him before he retired. They captured everything" beat is the load-bearing operator outcome — preserve verbatim or near-verbatim; **E60 anonymization:** "a global food safety company" already conforms |
| E31 | FRAMEWORK-ADD | LAND-WITH-MODIFICATION | New H2 between current §5.2 (source classification) and §5.3 (How systems talk to each other) OR as a paragraph inserted inside the §5.0 / §5.1 framing area, AFTER L22 (the "Once the map exists, it becomes a design problem" paragraph) AND BEFORE L24 (§5.1 H2 "Create a *Knowledge Map*"); **OR** as a paragraph inside §5.1 / before the Building your Knowledge Map paragraph at L41 — Drafter selects landing per cadence. **Recommend landing as a new H2 in §5.0 framing area, between L22 and L24,** to set the PIS lens BEFORE the Knowledge Map deliverable is defined | **EC1 canonical-definition verification.** Per manifest E31 canon: Source = the **I**dentify phase of **P**roblem/**I**dentify/**S**olution. Julie's E31 source aligns: "The Problem has already been named by Signal — the validated constraint. Source is the Identify phase: everything the organization knows about that problem, where the knowledge lives, who holds it, what is at risk if they leave, and what is missing that the Build phase will need. Solution comes later, in Design and Build." **EC1 verdict: PASS.** Julie's source paragraph's PIS naming and phase-mapping matches manifest E31 canon exactly. The Drafter must: (a) preserve P/I/S name and three-phase mapping (Signal=Problem; Source=Identify; Design+Build=Solution) verbatim or near-verbatim; (b) preserve the operator outcome ("you do not move to solution until you have identified what you are actually working with"); (c) preserve the sequencing-discipline parallel ("Running Source without having completed Signal is the organizational design equivalent of prescribing before diagnosing"). HEAVY REWRITE per risk map; **framework-attribution rule applies directly** (strip "Julie's Problem/Identify/Solution framework" individual attribution per global rule); **A2 risk:** PIS is being **first-introduced** here (no prior Ch 1–4 references); **forbidden vocab:** "organizational design equivalent" → strip ("organizational design" in mid-market-operator context is forbidden per voice charter §3); replace with "the same discipline as" or "the structural equivalent of"; **A1 risk:** Julie's source closer "A Source run on the wrong constraint is a well-organized inventory of the wrong problem." is operator-direct declarative — A1 CLEAN; preserve; **MEANS/ENDS-RISK:** PIS introduction reinforces sequencing discipline (means) but closes with operator outcome (wrong-problem inventory = wasted Sprint) — CLEAN |
| E32 | NEW-SECTION | LAND-WITH-MODIFICATION | New paragraph inside §5.1 (Create a *Knowledge Map*) AFTER L57 (the Pass 3 — Missing paragraph "Look at what's absent...") AND BEFORE L59 (the §5.1 Action Step "Review your map from Pass 1 and Pass 2..."); **OR** alternative landing inside §5.4 "People don't have *APIs*" near the at-risk-sources framing at L126 — **Recommend landing inside §5.1 immediately after Pass 3 Missing description** to anchor the "Missing sources column is most important" framing where the column is defined | Julie's "Missing sources column is most important" framing (decisions made by leaders who have since left + customer/market intelligence never captured); HEAVY REWRITE per risk map; **framework-attribution rule applies directly** (strip "From an organizational design perspective" + "Julie's practice in every organizational design engagement" individual attribution); **A3 risk:** Julie's source presents a **two-category split** ("Management knowledge loss" + "Leadership knowledge in individuals no longer available") — observational two-option, NOT a constructed triplet; preserve; verify Drafter does NOT add a third category; **A1 risk:** Julie's source closer "Every missing source is a potential sprint failure mode. Name them before Build begins, not after deployment reveals them." — declarative + operator-direct; A1 CLEAN; preserve; **EC1:** "Missing sources" is canonical Knowledge Map vocabulary (already defined at L57); E32 lands as elaboration of the existing canonical category; verify Drafter does NOT redefine; **forbidden vocab:** "organizational design perspective" / "organizational design engagement" must be reframed to "from a people-systems lens" / "every knowledge-inventory engagement" / "the way the work is set up" / similar plain operator language; **TML cross-reference:** Julie's source explicitly invokes TML categories (Management knowledge loss + Leadership knowledge in individuals) — verify Drafter preserves the TML reference (post-E29 landing, TML vocabulary is canonical) and does NOT redefine TML categories |

**Counts:** 1 ATTRIBUTION+NEW-SECTION LAND-WITH-MODIFICATION (E28) · 2 FRAMEWORK-ADD LAND-WITH-MODIFICATION (E29, E31) · 2 NEW-SECTION LAND-WITH-MODIFICATION (E30, E32) · 0 SKIP-ALREADY-DONE · 0 NEEDS-AUTHOR · 0 CONFLICT (no E-row directly conflicts with stale-audit canonical content; Marina opener at L8 is voice-shift only per E28 ATTRIBUTION component)

**Path verdict:** Default **Path A** (solo Drafter) per AGENT-TEAM §1 lessons-learned default and Ch 2 / Ch 3 / Ch 4 outcome (Path A produced clean Ch 2 in 3 iterations; Ch 4 dispatched on Path A). E29 is the strongest Path B candidate if any bead in this chapter fails voice-gate twice — it is the **highest framework-attribution + EC1 canonical-definition risk in the entire merge** (TML is the framework where the Ch 2 EC1 lesson was first encoded; getting Ch 5's TML introduction right is upstream of Ch 6b's TML work-lens application).

- **E29** because it lands the chapter's first canonical framework introduction with **highest framework-attribution + EC1 canonical-definition verification + A2 first-definition load-bearing + cross-chapter coherence with Ch 2 L259 forward-reference + cross-chapter coherence with Ch 6b work-lens application** (six intersecting controls).
- **E31** is the second-highest-risk landing because it introduces a second framework (PIS) on top of E29's TML, and lands chapter-framing-adjacent (between §5.0 setup and §5.1 deliverable definition). **A2 first-definition + framework-attribution + forbidden-vocab discipline + MEANS/ENDS-RISK** (four controls).
- **E28** is lower-risk than E29 / E31: substance is biographical parallel (not framework), pattern matches the established Preface + Ch 1 + Ch 2 + Ch 4 a global food safety company convention, primary risks are cross-chapter n-gram avoidance + Q-E21 attribution discipline + forbidden-vocab grep.
- **E30** and **E32** are mid-risk: framework-attribution scrub + A1/A3 trap discipline + forbidden-vocab grep + n-gram coherence.

Recommend single solo Drafter pass for all five landing rows (E28 → E29 → E31 → E30 → E32) in the recommended bead order below; escalate to Path B only on second voice-gate fail.

---

## Per-E-row acceptance criteria

### E28 (ATTRIBUTION + NEW-SECTION, LAND-WITH-MODIFICATION) — Jesse Marina/coordinator opener attribution + Julie's parallel global food safety company tribal-knowledge story

**Substance to preserve (current chapter L8–L14 Marina/coordinator opener + L30 + L130 Jesse-voice cross-references):**

- **The Marina + $24K project coordinator opener (L8–L14) is the canonical polished replacement** per commit `6c99346` ("Cross-book coherence pass") and is referenced as the same story-anchor in Ch 2 L8–L10 (E16 attribution already landed) and Ch 4 L8–L16 (E24 attribution already landed). **Do NOT regress to any earlier fabricated opener; do NOT restructure the story; do NOT add or remove specifics.**
- Verbatim preserve: L8 setup ("Marina and I were on a call deciding what to do about our project coordinator. The role was costing us ~$24,000 a year. Work was falling behind. Billing was getting impacted. Signal had validated the constraint — this function was broken and it was costing us real money."), the L10 question discipline ("'We need to understand what she actually does. Not what's in the job description...'"), the L12 information-flow framing ("That question changed the shape of the conversation..."), the L14 "Every modern company is an information company" pivot to the chapter thesis.
- L30 "When Marina and I mapped what our project coordinator did..." — voice-shift only; preserve the operator outcome ("the map didn't catalog every system in the company. It cataloged what the coordinator touched, what she decided, and what would break if she disappeared tomorrow.").
- L130 "Remember the developer who walked out with everything he knew? Source provides context... If I had mapped where the knowledge lived before that developer left, the handoff would have been a step instead of a slide." — voice-shift only; this is the **Preface chutes-and-ladders cross-reference** per `ahmed-story-is-chutes-and-ladders` and `pm-case-study-thread-through-book` memories; preserve the developer-departure story content; **italicize *Chutes and Ladders* as proper noun** (per Preface convention at index.qmd:5).

**Modification from Julie's instruction (Jesse-attribution side):**

- Julie's redline (line 1493) inserts a literal `Jesse:` underline tag at the top of the section. **Reject per Q-E21:** inline author tags are not the book's convention; blended-we + in-prose attribution is canon. The Preface E01/E02, Ch 1 E08–E11, Ch 2 E16, Ch 3 E21, and Ch 4 E24 have all modeled this.
- **Land the attribution differently than Julie's inline tag:** Apply Pattern A (preferred for cross-chapter consistency with Ch 2 L8 "Jesse was in a management meeting with Marina, his Integrator..." and Ch 4 L8 "Jesse was in our own L10..."): Open with "Jesse and Marina were on a call deciding what to do about our project coordinator..." or "Marina and Jesse were on a call deciding..." Then sustain blended-we across L10 → L12 → L14. Cascading: L10 "I stopped the conversation. 'We need to understand what she actually does..." → "We stopped the conversation. 'We need to understand what she actually does..." or restructure to preserve the cadence; L12 already mostly blended-we; L14 already mostly blended-we.
- **L30 cascade:** "When Marina and I mapped what our project coordinator did" → "When Marina and Jesse mapped what our project coordinator did" (third-person blended) OR "When we mapped what our project coordinator did" (collective blended-we, given Jesse-anchor already established at L8 opener). **Recommend collective blended-we** ("When we mapped...") to avoid double-anchoring within the same chapter.
- **L130 cascade:** "If I had mapped where the knowledge lived before that developer left" → "If we had mapped where the knowledge lived before the developer left" (collective blended-we). **Italicize *Chutes and Ladders*** if the proper noun is reintroduced (acceptable not to reintroduce — the cross-reference can land as "the developer who walked out with everything he knew" without re-naming the metaphor, since the Preface establishes it).
- **Contractions:** the existing prose uses contractions throughout. Julie's source (line 1496) is contraction-free. **Preserve current chapter contractions; do not regress to Julie's no-contractions source.**

**Substance to preserve (from `_julie/julie-redline.md:1505–1519` — Julie's parallel global food safety company tribal-knowledge story):**

- The substantive insight: in M&A integration work, the inherited knowledge is **entirely tribal** — process experts who held twenty years of institutional memory that existed nowhere in any system. Their expertise was the documentation.
- The Signal-discipline-as-applied: the first question Julie asked every integration team was the same question Source asks: **"if this person were not here tomorrow, what would stop working?"** This question is **the load-bearing operator beat** — preserve verbatim or near-verbatim. The question maps directly onto the chapter's existing at-risk-source framing at L126 ("who on this list is a single point of failure?").
- The operator outcome: **"The answers were almost always more alarming than anyone expected."** Preserve. This is the load-bearing operator beat.
- The chapter-thesis hook: "The gap between what organizations think they know and what they actually have in documented, accessible form is the single most consistent finding of every organizational design engagement I have run. Source closes that gap before it becomes a sprint failure." **Substance preserved; framing reworked** (see modifications below).

**Modification from Julie's instruction (Julie-parallel-paragraph side):**

- **Framework-attribution rule — INDIRECT APPLICATION:** Julie's source closes with "the single most consistent finding of every organizational design engagement I have run" — individual-credentialing scope ("every... I have run") on what is otherwise observational. Per the framework-attribution rule, the closing must reframe to joint observation: "is what every organizational redesign reveals" / "is what Julie has watched in every post-acquisition integration" / "is the same gap Source closes before it becomes a sprint failure." **Single in-prose attribution at opening** (Pattern from Ch 4 E25: "Julie has watched the same gap land in M&A integration work outside any AI context. At a global food safety company..." or similar).
- **Cross-chapter coherence — FOUR PRIOR a global food safety company ANCHORS:**
  - Preface L9 ("In 2022, Julie was Global CHRO at a global food safety company when it completed the acquisition of a major division from a Fortune 500 company. Overnight, the organization expanded across 44 countries. The challenge wasn't technology. It was that the work — who owned what, how decisions moved, what knowledge lived where — had never been explicitly designed in either company before the acquisition.")
  - Ch 1 L57 ("When a global food safety company completed a Fortune 500 division acquisition, Julie was the CHRO overseeing the integration across 44 countries...") — Headcount Paradox / smaller proportional team.
  - Ch 2 §2.3 (E19, already landed): a global food safety company graft-vs-redesign story.
  - Ch 4 L18 (E25, already landed): a global food safety company matrix-reporting / no-replacement story.
  - **E28 must NOT verbatim-echo any of the four prior anchors.** Differentiate by focus: E28's angle is the **inherited tribal-knowledge** insight — the knowledge that existed nowhere except in long-tenured process experts' heads. Acceptable phrasing: "When the same acquisition closed, Julie inherited not just an org chart but a set of process experts whose expertise was the documentation." / "Julie has watched this exact pattern in M&A integration work. At a global food safety company, when the acquired Fortune-500 division closed, the inherited assets included twenty-year process experts who held institutional memory that existed nowhere in any system." **Verify Drafter does NOT re-introduce 44-country scope or CHRO title** (those are Preface + Ch 1 + Ch 4 anchors); reference is single-anchor "Julie has watched..." with the angle specific to tribal-knowledge inheritance.
- **A3 (triplet pileup):** Julie's source has clean substance, no triplet construction. Low risk; verify Drafter introduces zero.
- **A1 (antithesis pileup):** Julie's source closer "Source closes that gap before it becomes a sprint failure" is operator-direct declarative — A1 CLEAN. Preserve.
- **A4 (boastful biographical):** Moderate risk. "Every organizational design engagement I have run" credentialing → strip per framework-attribution scrub; the 20-year CHRO credentialing is already established in the Preface and Ch 1 §1.0. Single in-prose attribution; do not re-credentialize.
- **A2 (coined term):** Julie's source uses "Source" as canonical book-vocabulary (already staked in Ch 3 §3.3 and the In Brief). Acceptable. Verify Drafter does NOT pre-empt Knowledge Map naming (defined at L24 in §5.1) — E28 should reference "knowledge" / "what the work requires" / "what people know" rather than "Knowledge Map" (capitalized) before §5.1 defines it.
- **MEANS/ENDS-RISK:** E28 lands chapter-opener-adjacent (between L14 chapter-thesis pivot and L16 §5.0 heading). **MEANS/ENDS-RISK = MED.** Acceptance criterion: close E28 on the operator outcome (the inherited tribal knowledge surfaced before integration failure / the "if this person were not here tomorrow, what would stop working" question that prevented downstream loss) and name Source as the means. Julie's source already does this — preserve the order: inherited tribal knowledge → diagnostic question (the Source question, applied to humans) → operator outcome (alarming answers / gap closed before sprint failure). Verify Drafter does not invert.
- **Forbidden vocab:** Julie's source uses "organizational design engagement" — forbidden per voice charter §3 in mid-market-operator context. **Strip and reframe** as "every M&A integration" / "every post-acquisition redesign" / "every people-systems engagement" / "the knowledge inventory" or plain operator language. Watch for "transformation" / "leverage" / "synergy" / "alignment" (no instances in Julie's source; verify zero introduced by Drafter).
- **E60 anonymization:** "a global food safety company" already conforms; "Fortune 500 parent company" / "Fortune-500 division" already conforms; do not introduce new identifying detail.
- **In-prose attribution (per Q-E21):** Single Julie-anchor sentence at opening of the parallel paragraph; blended-we / third-person for the story body. Frequency: this is the **first Julie-voice paragraph in Ch 5**, and there will be **three more** Julie-voice paragraphs in the chapter (E30, E31, E32). **Calibrate attribution frequency across the chapter** — E28's anchor is named ("Julie has watched..."); subsequent E30 / E31 / E32 anchors should be lighter to avoid attribution fatigue (single Julie name across the chapter; subsequent references can be "she has watched" / "the same diagnostic" / implicit via context).

**Anti-pattern risk (highest):**

- **Cross-chapter n-gram repetition (HIGH)** — four prior a global food safety company anchors already in the manuscript. **Drafter's scanner pipeline n-gram check at threshold 0.85 must run against** Preface L9 + Ch 1 L57 + Ch 2 §2.3 + Ch 4 L18.
- **Framework-attribution (MED)** — "every organizational design engagement I have run" individual credentialing; reframe to joint.
- **Forbidden vocab (MED)** — "organizational design engagement" must be reframed (recurring 3/3 chapter pattern per Preface + Ch 1 + Ch 2 + Ch 4 lessons-learned).
- **A4 (boastful biographical, MED)** — "every... I have run" scope; mitigated by Preface + Ch 1 setup; single in-prose attribution.
- **A2 (coined term, LOW)** — "Source" already staked; "Knowledge Map" pre-empt risk (avoid capitalization before §5.1 defines).
- **A13 (means/ends, MED)** — chapter-opener-adjacent landing; closer must land operator outcome (alarming answers / gap closed) and name Source as the means.

**Framework-attribution rule:** N/A for the framework-introduction side (E28 introduces no framework — Source is already canonically named). Indirect application on the closing-clause credentialing ("every... I have run") — reframe to joint.

**Coherence:**

- E28 must land **first** in the chapter's execution order. It sets the voice E29 / E30 / E31 / E32 write into.
- The Preface E01–E07 + Ch 1 E08–E15 + Ch 2 E16–E19 + Ch 3 E21–E23 + Ch 4 E24–E27 have already established blended-we + in-prose attribution + framework-attribution scrub + forbidden-vocab discipline. E28 inherits; does not invent.
- The Marina story is canonically referenced in Ch 2 L8 and Ch 4 L8. **The $24K coordinator anchor and the Marina-Integrator framing must remain consistent.** Voice-shift must not break the cross-chapter reference.
- The L130 developer-cross-reference is canonical per `ahmed-story-is-chutes-and-ladders` memory — the developer = Ahmed (canonically anonymized) from the Preface chutes-and-ladders story. **Italicize *Chutes and Ladders*** if the proper-noun metaphor is reintroduced; otherwise the L130 cross-reference can stand as "the developer who walked out with everything he knew" (no italics needed if the proper noun is not used in this paragraph). Drafter chooses based on cadence; verify the reference does NOT verbatim-echo Preface L5 phrasing.
- After E28 lands, the L8 → L10 → L12 → L14 → E28-parallel → L16 (§5.0 heading) flow must read: Jesse + Marina coordinator opener (blended-we w/ Jesse anchor) → information-flow framing → Source naming → Julie's parallel tribal-knowledge story (single Julie anchor → tribal knowledge → diagnostic question → operator outcome) → §5.0 deliverable-thesis. Single forward motion.
- Verify NO n-gram repetition with Preface L9 (44-country / Fortune-500 acquisition / "challenge wasn't technology"), Ch 1 L57 ("smaller proportional team than the pre-acquisition domestic function"), Ch 2 §2.3 ("graft-vs-redesign / countries / supplier networks"), or Ch 4 L18 ("matrix-reporting / two reporting lines crossed / leaders operating inside an accountability structure").

---

### E29 (FRAMEWORK-ADD, LAND-WITH-MODIFICATION) — TML Framework as Knowledge Map categorization

**Substance to preserve (from `_julie/julie-redline.md:1535–1551`):**

- The substantive insight: knowledge in any organization divides into three layers:
  - **Task knowledge** = the documented steps, the SOPs, the process maps — the work that can be written down and followed.
  - **Management knowledge** = the decision rights, the escalation paths, the governance rules that determine who approves what.
  - **Leadership knowledge** = the judgment, the relationships, the context, the pattern recognition that only comes from years inside the business.
- The empirical pattern: Task knowledge is easiest to capture and most common in systems; Management knowledge is partially documented but inconsistently followed; Leadership knowledge almost never exists outside the people who hold it.
- **The AI-handling mapping** (this is the load-bearing canonical-definition closing clause that matches manifest E36 canon): **AI can reliably handle Task knowledge; AI can assist with Management knowledge; AI requires human oversight for Leadership knowledge at every step.**
- The operational instruction: the Source Knowledge Map inventory should **explicitly categorize every source against these three layers** — because each layer requires a different capture and transfer approach.

**EC1 CANONICAL-DEFINITION VERIFICATION (MANDATORY per scout.md §5 + Ch 2 lessons-learned EC1 update):**

- **Canonical TML (per manifest E36 + voice charter §3 + Ch 2 L259 forward-reference):** Task → Fully Automatable, Management → AI-Assisted, Leadership → Human Judgment.
- **Julie's E29 source TML (knowledge lens):** Task knowledge (documented/SOPs/process maps) / Management knowledge (decision rights/escalation/governance) / Leadership knowledge (judgment/relationships/context/pattern recognition) — **plus the AI-handling mapping at closing:** AI handles Task / AI assists Management / human oversight for Leadership.
- **EC1 VERDICT: PASS.** Julie's source presents TML through a **knowledge categorization lens** (vs. manifest E36's **work categorization lens** for Ch 6b Work Deconstruction), but: (a) the three-category names (Task / Management / Leadership) match canon; (b) the AI-handling mapping (handle / assist / oversight) matches canon. The lens difference is **complementary, not contradictory** — knowledge categorization in Ch 5 (Source) + work categorization in Ch 6b (Work Deconstruction) are two facets of the same canonical framework.
- **No Drafter modification needed to bring Julie's source paragraph into canon-alignment.** The Drafter task is: (a) preserve the three-category names exactly; (b) preserve the AI-handling mapping at closing; (c) frame as the **knowledge lens** that complements Ch 6b's **work lens**; (d) apply the framework-attribution scrub (joint book IP, not Julie's individual framework).
- **NO author decision required** at this gate. Both lenses match canon. The Drafter executes per acceptance criteria below.

**Modification from Julie's instruction:**

- **Framework-attribution rule — DIRECT APPLICATION:** Julie's source opens "Julie's TML framework gives Source its diagnostic structure." This is **individual attribution of joint book IP** (TML is the canonical framework per voice charter §3 + manifest E36). Per manifest line 57 (global rule) and `framework-attribution-rule` persistent memory, **reject the "Julie's TML framework" framing**. Reframe as joint book IP: "The **TML framework** (Task / Management / Leadership) gives Source its diagnostic structure." OR "Knowledge sorts into three layers — Task, Management, Leadership. The **TML framework** is the lens." **Drafter to prefer the second pattern** (declarative + canonical-vocabulary introduction → three-layer definition) for cleanest A2 first-definition land.
- **A2 first-definition discipline (CRITICAL):** TML is being **first-introduced load-bearing** in Ch 5 (Ch 2 L259 was a forward-reference that says "Chapter 6 introduces the full design instrument" — but Ch 5 lands TML earlier in the manuscript than Ch 6b). The Ch 2 forward-reference points at Ch 6 but TML actually lands in Ch 5 (knowledge lens) and Ch 6b (work lens). **Per A2 (coined term before stakes):** the first-load-bearing introduction in Ch 5 must define the framework precisely enough to support Ch 6b's work-lens application. Acceptance criterion: the Ch 5 introduction must:
  - Define TML as a three-category framework: **Task / Management / Leadership** (names verbatim).
  - Define each category by what it is, what it produces, and how AI handles it (canonical AI-handling mapping).
  - Frame as a lens applied to knowledge in Ch 5; signal that the same framework will be applied to work in Ch 6b.
- **Ch 2 L259 forward-reference reconciliation:** Ch 2 L259 currently says "Chapter 6 introduces the full design instrument — the **TML framework** (Task / Management / Leadership)..." If Ch 5 introduces TML first (E29 lands), then **Ch 2 L259 forward-reference becomes inaccurate** (should point to Ch 5, not Ch 6). **Flagged for the Drafter to fix** — change Ch 2 L259 forward-reference to "Chapter 5 introduces the full design instrument..." or "the **TML framework** (Task / Management / Leadership)... covered in Chapters 5 and 6." **This is a cross-chapter coherence fix; flagged but not blocking.**
- **A3 risk:** Julie's three-layer definition is a **structurally observational three-category framework** (not a constructed parallel triplet). **Acceptable as a three-category enumeration** — it IS the framework. But the **second wave of parallel structure** in Julie's source — "Task knowledge is the easiest to capture... Management knowledge is partially documented... Leadership knowledge almost never exists..." — is a **second triplet on top of the first**. **A3 trap.** Resolution: collapse the second wave into a single sentence or differentiated cadence. Acceptable: "Task knowledge is the easiest to capture and the most common to find in systems; Management knowledge is partially documented and inconsistently followed; Leadership knowledge almost never exists outside the people who hold it." (Single semicolon-bridged sentence keeps the structure but avoids stacked triplet cadence.) **Drafter to prefer single-sentence semicolon-bridge form.**
- **A1 risk:** Julie's source has no antithesis closer; A1 CLEAN.
- **Forbidden vocab:** Julie's source uses "the organizational design foundation of the knowledge mapping work" — **strip per voice charter §3** (organizational design in mid-market-operator context is forbidden). Replace with "the foundation of the knowledge mapping work" or "the design logic of Source" or remove the phrase entirely. Watch for "transformation" / "leverage" / "synergy" / "alignment" — none in Julie's source; verify Drafter introduces zero.
- **A4 (boastful biographical):** Low risk — TML is introduced as joint book IP, not as Julie's individual framework. Framework-attribution scrub addresses.
- **MEANS/ENDS-RISK:** TML introduction reinforces Source diagnostic discipline (means) but closes with operator outcome (each layer requires different capture/transfer; AI can handle some, assists with others, requires oversight on the third) — operator-recognizable. **CLEAN** if framing closes on AI-handling mapping (operator outcome) rather than abstract "diagnostic structure" (system-as-destination).
- **In-prose attribution:** Light. E29 introduces a framework — joint book IP. The framework can be **origin-credited** to Julie's CHRO practice once at the opening if the Drafter chooses ("from her CHRO practice" / "Julie has applied this same three-layer lens in M&A integration work"), but **never as her individual instrument**. Recommended: skip individual attribution at the framework-introduction sentence; let the framework land as joint vocabulary. Single attribution can land in the **example-application sentence** if needed.
- **Landing inside §5.1 or as new H3:** Two acceptable landing patterns:
  - **Pattern A (preferred — paragraph inside §5.1):** Insert after L20 ("Source produces that ground truth..."), before L22 ("This is why Source belongs in Diagnose..."). The TML framework lands as the lens that explains **how** Source produces ground truth — categorizing knowledge into three layers AI handles differently.
  - **Pattern B (new H3 under §5.1):** Add an H3 titled "Three layers of *knowledge*" or "The *TML* lens" between L22 and L24, defining the framework as a sidebar before §5.1's deliverable definition.
  - **Drafter selects based on cadence.** Pattern A keeps §5.1 coherent (TML lands inside the existing diagnosis-not-done framing). Pattern B gives TML its own visual hierarchy. **Recommend Pattern A** for cadence consistency with the chapter's existing one-H2-per-section discipline.

**Anti-pattern risk (highest):**

- **EC1 canonical-definition verification (CRITICAL)** — Task/Management/Leadership names + AI-handling mapping must match canon; **verified PASS per analysis above**; Drafter must preserve.
- **A2 first-definition load-bearing (HIGH)** — TML is being load-bearing-introduced for the first time in the manuscript; must define precisely enough to support Ch 6b's work-lens application.
- **Framework-attribution (HIGH)** — direct application; "Julie's TML framework" → joint book IP framing.
- **A3 stacked triplet (MED)** — three-layer enumeration is the framework (acceptable); the second wave of parallel "Task is easiest... Management is partial... Leadership rarely exists" risks stacked triplet — collapse to single-sentence semicolon-bridge form.
- **Forbidden vocab (MED)** — "organizational design foundation" must be reframed (3/3 chapter recurrence pattern per Preface + Ch 1 + Ch 2 + Ch 4 lessons-learned).
- **Cross-chapter coherence (HIGH)** — Ch 2 L259 forward-reference needs to be updated to point at Ch 5; Ch 6b work-lens application must inherit the canonical TML definition.

**Framework-attribution rule:** **Applies directly.** TML is canonical Compound vocabulary (per voice charter §3 + manifest E36) — joint book IP. Strip "Julie's TML framework" individual framing. Origin-credit to Julie's CHRO practice acceptable as one sentence at the opening but never as her individual instrument.

**Coherence:**

- Lands AFTER L20 (Source produces that ground truth...) and BEFORE L22 (This is why Source belongs in Diagnose...) per Pattern A; alternative landing per Pattern B as new H3 between L22 and L24.
- Must read as **the diagnostic lens that explains how Source categorizes what it finds** — knowledge sorts into three layers, each layer requires a different capture/transfer approach, AI handles each layer differently.
- **Cross-chapter coherence: Ch 2 L259 forward-reference update.** Currently Ch 2 L259 says "Chapter 6 introduces the full design instrument — the **TML framework** (Task / Management / Leadership)..." Drafter to fix in Ch 2 (separate edit pass — flagged but not blocking E29 landing): change to "Chapter 5 introduces the **TML framework** (Task / Management / Leadership) as the lens for organizing what the company knows; Chapter 6 applies the same framework to the work itself."
- **Cross-chapter coherence: Ch 6b work-lens application.** Ch 6b currently uses **four** categories (Human judgment required / Agent-assisted / Fully automatable / Workflow automation only) — NOT yet aligned to TML's three categories. This is E36's job (Ch 6b bead, separate execution). **Flagged but not blocking E29 landing.** E29 must land the canonical three-category framework in Ch 5; E36 will subsequently bring Ch 6b into alignment.
- **Cross-chapter coherence: Glossary E58.** TML is one of the seven glossary additions in E58. E58 (Ch 15 / glossary) will add the canonical definition to the glossary. **Flagged but not blocking E29 landing.**
- E29 must NOT pre-empt §5.4 "People don't have *APIs*" three-categories (Digital / Organic / At-risk sources) — those are **source categories**, not knowledge layers. Both exist in parallel; verify Drafter does NOT conflate.
- E29 must NOT pre-empt §5.2 source classification axes (Structured vs. unstructured, Durable vs. ephemeral, three AI tiers) — those are **classification axes** applied to sources, distinct from TML's knowledge layers. Both exist in parallel; verify Drafter does NOT conflate.

---

### E30 (NEW-SECTION, LAND-WITH-MODIFICATION) — Julie's senior pricing strategist At-Risk Source story

**Substance to preserve (from `_julie/julie-redline.md:1565–1580`):**

- The substantive insight from M&A integration practice: in every acquisition, the most at-risk knowledge is **never the knowledge anyone thought to protect**. The documented processes were protected. The undocumented judgment calls were not.
- The concrete story anchor: at a global food safety company, the single highest-risk knowledge asset in the acquired integration was **a senior pricing strategist who held in his head twenty years of customer-specific pricing exceptions** — decisions that had been made individually over decades and never consolidated into any system.
- The Source-discipline operator outcome: he was not identified as an at-risk knowledge source until Source was run. When he was identified, the team had **four weeks to work with him before he retired. They captured everything.**
- The structural outcome: **the Source discipline prevented a loss that would have taken two years to reconstruct and would have produced pricing errors throughout the transition period.** The "two years to reconstruct" / "pricing errors throughout the transition" beats are operator-load-bearing — preserve verbatim or near-verbatim.
- The closer (substance preserved; cadence reworked): "That is what At-Risk Source does: it names what nobody knew they were about to lose." — substance kept; "That is what... does" cadence cut per A1.

**Modification from Julie's instruction:**

- **Framework-attribution rule — INDIRECT APPLICATION:** Julie's source opens "Julie's M&A integration practice identified a specific pattern in every acquisition..." This is **individual attribution of joint observation** ("the knowledge most at risk is never the knowledge anyone thought to protect" is an observational diagnostic, not a Julie-invented framework). Per framework-attribution rule, reframe to joint observation: "In every acquisition Julie has worked, the most at-risk knowledge has never been the knowledge anyone thought to protect." OR "Julie has watched the same pattern in every M&A integration: the most at-risk knowledge is never the knowledge anyone thought to protect." **Drafter to prefer second pattern** (single Julie anchor sentence → joint observational frame for the diagnostic).
- **A1 risk:** Julie's source has the **AI-tell closer pattern** "That is what At-Risk Source does: it names what nobody knew they were about to lose." Per voice charter §4 A1 and §4 A3-tag-closer-pattern, the "That is what X does" cadence is forbidden. Resolution: preserve substance (At-Risk Source names what nobody knew they were about to lose), cut "That is what" cadence. Acceptable rewrites: "At-Risk Source names what nobody knew they were about to lose." (simple declarative) OR "The pricing strategist case is what At-Risk Source surfaces: knowledge nobody knew they were about to lose." OR combine the operator-math closer with the discipline name: "Source prevented a two-year reconstruction and pricing errors throughout the transition. That is the operator math of At-Risk Source."
- **A3 risk:** Julie's source has clean substance, no triplet construction. Low risk; verify Drafter introduces zero.
- **A4 (boastful biographical):** Moderate risk. "Julie's M&A integration practice identified..." scope; mitigated by Preface + Ch 1 + Ch 4 + E28 attribution setup. Single in-prose attribution per author maximum.
- **A2 (coined term):** Julie's source uses **"At-Risk Source"** — canonical Compound vocabulary defined at L126 in §5.4 ("An at-risk source is institutional knowledge that lives in one person's head and is about to leave — through a planned exit, a retirement, a role change, or a reorg."). E30 lands AFTER L126 (inside §5.4) — definition is established. **Acceptable use.** Verify Drafter does NOT redefine.
- **MEANS/ENDS-RISK:** E30 reinforces §5.4 existing at-risk-source thesis with a concrete Julie-anchored story. **MEANS/ENDS-RISK = LOW.** Closer must land operator outcome (two years to reconstruct / pricing errors avoided / four weeks captured everything) — Julie's source already does this; preserve order.
- **Forbidden vocab:** "M&A integration practice" / "acquisition" / "transition period" — plain operator language; acceptable. Watch for "transformation" / "leverage" / "synergy" / "alignment" — none in Julie's source; verify Drafter introduces zero. "Organizational design" not present in this source.
- **E60 anonymization:** "a global food safety company" already conforms.
- **N-gram coherence:** verify no n-gram repetition with Ch 5 L161 Meridian Sprint beat ("Dave — Organic, at-risk, four years to retirement with an undocumented estimation method"). Both stories share the "retirement" + "undocumented" + "at-risk" + "years of knowledge" thematic ground but should not share verbatim phrasing. E30 should use **"twenty years" / "pricing exceptions" / "four weeks" / "two years to reconstruct"** as the differentiating specifics; L161 uses **"four years to retirement" / "fabrication estimation" / "31 years"** as Dave's specifics.
- **Operator-math closer:** the "four weeks to work with him before he retired. They captured everything" beat is the load-bearing operator outcome. Preserve verbatim or near-verbatim. The "two years to reconstruct... pricing errors throughout the transition period" beat is the cost-of-avoidance math — preserve.
- **In-prose attribution:** Light. E28 has anchored Julie's voice in the chapter; E30 can land with a single passing reference ("Julie has watched..." / "In Julie's M&A work..." / implicit via context "the same gap surfaced at a global food safety company"). **Recommend implicit attribution** — the global food safety company anchor (already established as Julie's CHRO context in Preface + Ch 1 + Ch 2 + Ch 4) carries the attribution without an explicit Julie name.

**Anti-pattern risk (highest):**

- **A1 (AI-tell closer "That is what X does")** — direct hit; cut "That is what" cadence.
- **Framework-attribution (MED)** — "Julie's M&A integration practice identified" → joint observational reframe.
- **N-gram coherence with L161 Dave-Meridian beat (MED)** — verify no verbatim echo on "retirement" / "undocumented" / "years of knowledge."
- **A4 (MED)** — credentialing; mitigated by Preface + Ch 1 + Ch 4 setup.
- **A13 (means/ends, LOW)** — closer lands operator outcome; mostly clean per Julie's source.

**Framework-attribution rule:** **Applies indirectly.** At-Risk Source is canonical Compound vocabulary at L126 — joint book IP. Strip "Julie's M&A integration practice" individual-instrument framing. The story is Julie's; the framework is joint.

**Coherence:**

- Lands AFTER L126 (at-risk-source paragraph closer "For most operating companies this is the single most consequential thing Source does.") and BEFORE L128 (the "When you're building your map, ask explicitly..." paragraph) inside §5.4 "People don't have *APIs*".
- Must read as a **third concrete worked example of at-risk sources** — L126 defines at-risk in the abstract, L128 prescribes the action ("ask explicitly: who on this list is a single point of failure?"), E30 lands between with a Julie-anchored story showing what at-risk-source identification produces (twenty-year pricing strategist captured in four weeks).
- The Meridian Sprint at L161 (Elena + Dave both flagged at-risk) is the chapter's **other** at-risk-source worked example. E30 + Meridian Sprint together bracket the chapter as the discipline working across two contexts: M&A integration (Julie-anchored, multi-decade-knowledge senior strategist) + ongoing operations (Meridian, near-retirement Dave). Cross-chapter coherence required: no verbatim phrasing overlap on "retirement" / "undocumented" / "twenty/thirty years."
- E30 must NOT pre-empt §5.5 "Transcripts: the closest thing a person has to an API" (L132–L149). The "team had four weeks to work with him... they captured everything" beat is **implicitly** a transcripts-as-extraction beat — but the explicit transcripts framing lands at §5.5. Verify Drafter does NOT introduce "transcript" / "structured interview" vocabulary in E30 (those land at §5.5).
- E30 must NOT pre-empt §5.7 "Knowledge management in an *agentic* world" (L165–L185). The "pricing errors throughout the transition period" beat is **implicitly** a knowledge-management beat — but the explicit knowledge-management framing lands at §5.7.

---

### E31 (FRAMEWORK-ADD, LAND-WITH-MODIFICATION) — PIS Framework: Source = Identify phase of Problem/Identify/Solution

**Substance to preserve (from `_julie/julie-redline.md:1590–1604`):**

- The substantive insight: the **Problem/Identify/Solution (PIS) framework** gives the Source conversation its structure.
- The phase mapping: **Problem = Signal (the validated constraint). Identify = Source (everything the organization knows about that problem). Solution = Design + Build (Solution comes later).**
- **The load-bearing canonical-definition statement (matches manifest E31 canon):** **Source is the Identify phase of Problem/Identify/Solution. Source is everything the organization knows about that problem — where the knowledge lives, who holds it, what is at risk if they leave, and what is missing that the Build phase will need.**
- The sequencing-discipline parallel (operator-load-bearing): "Running Source without having completed Signal is the organizational design equivalent of prescribing before diagnosing. The constraint has to be named before the knowledge inventory begins, because the inventory is shaped by the constraint."
- The closer (operator-direct declarative): "A Source run on the wrong constraint is a well-organized inventory of the wrong problem."

**EC1 CANONICAL-DEFINITION VERIFICATION (MANDATORY per scout.md §5 + Ch 2 lessons-learned EC1 update):**

- **Canonical PIS (per manifest E31):** Source = the **I**dentify phase of **P**roblem/**I**dentify/**S**olution.
- **Julie's E31 source PIS:** "The Problem has already been named by Signal — the validated constraint. Source is the Identify phase: everything the organization knows about that problem... Solution comes later, in Design and Build."
- **EC1 VERDICT: PASS.** Julie's source paragraph's PIS naming and phase-mapping matches manifest E31 canon exactly:
  - **P (Problem)** = Signal-validated constraint. ✓
  - **I (Identify)** = Source. ✓
  - **S (Solution)** = Design + Build. ✓
- **No Drafter modification needed to bring Julie's source paragraph into canon-alignment.** The Drafter task is: (a) preserve P/I/S name and three-phase mapping verbatim or near-verbatim; (b) preserve the sequencing discipline ("you do not move to solution until you have identified what you are actually working with"); (c) apply the framework-attribution scrub (joint book IP, not Julie's individual framework).
- **NO author decision required** at this gate. The framework's phase-mapping matches canon. The Drafter executes per acceptance criteria below.

**Modification from Julie's instruction:**

- **Framework-attribution rule — DIRECT APPLICATION:** Julie's source opens "Julie's Problem/Identify/Solution framework gives the Source conversation its structure." This is **individual attribution of joint book IP** (PIS is canonical Compound vocabulary per manifest E31 and pending glossary E58). Per manifest line 57 (global rule) and `framework-attribution-rule` persistent memory, **reject the "Julie's Problem/Identify/Solution framework" framing**. Reframe as joint book IP: "The **Problem/Identify/Solution (PIS) framework** gives the Source conversation its structure." OR "Source maps onto a three-phase diagnostic: Problem / Identify / Solution. **PIS** is the framework name." **Drafter to prefer the second pattern** (declarative + canonical-vocabulary introduction → three-phase definition) for cleanest A2 first-definition land.
- **A2 first-definition discipline (CRITICAL):** PIS is being **first-introduced load-bearing** in Ch 5 (no prior references in Ch 1–4 or appendices). Per A2 (coined term before stakes), the introduction must:
  - Define PIS by the three phases verbatim (Problem / Identify / Solution).
  - Map each phase to its Compound stage(s): Problem = Signal, Identify = Source, Solution = Design + Build.
  - Frame as the diagnostic lens underneath the first three stages of the Sequence.
- **A3 risk:** Julie's three-phase enumeration is **structurally observational three-category framework** (not a constructed parallel triplet). Acceptable. Verify Drafter does NOT add a second wave of parallel structure (e.g., do not add "Problem is the constraint... Identify is the knowledge... Solution is the design..." stacked triplet on top of the framework definition).
- **A1 risk:** Julie's source closer "A Source run on the wrong constraint is a well-organized inventory of the wrong problem." is operator-direct declarative — A1 CLEAN. Preserve.
- **Forbidden vocab:** Julie's source uses "the organizational design equivalent of prescribing before diagnosing" — **strip "organizational design"** per voice charter §3 (mid-market-operator context forbidden). Replace with: "the same discipline as prescribing before diagnosing" / "the structural equivalent of prescribing before diagnosing" / "what doctors call prescribing before diagnosing." **Recommend "the same discipline as"** for cadence consistency.
- **A4 (boastful biographical):** Low risk — PIS is introduced as joint book IP, not as Julie's individual framework. Framework-attribution scrub addresses.
- **MEANS/ENDS-RISK:** PIS introduction reinforces sequencing discipline (Sprint phases ordered correctly = means) but closes with operator outcome (wrong-problem inventory = wasted Sprint). **CLEAN.** Verify Drafter does not invert to system-as-destination cadence.
- **In-prose attribution:** Light. E31 introduces a framework — joint book IP. Acceptable origin-credit to Julie's CHRO practice if framing demands ("Julie has applied this same three-phase lens in M&A diagnostics" / similar), but **never as her individual instrument**. **Recommend: skip individual attribution at framework-introduction sentence**; PIS lands as joint vocabulary.
- **Landing as new H2 or as paragraph in §5.0:** Two acceptable landing patterns:
  - **Pattern A (preferred — new H2):** Insert as new H2 between current §5.0 closer (L22) and §5.1 heading (L24). H2 title: "The *PIS* lens." or "Source is the *Identify* phase." Single-paragraph H2 that lands PIS as framing for the rest of the chapter.
  - **Pattern B (paragraph in §5.0):** Insert as a paragraph between L22 ("This is why Source belongs in Diagnose, not Execute...") and L24 (§5.1 heading "Create a *Knowledge Map*"). PIS lands as final framing before the Knowledge Map deliverable is defined.
  - **Drafter selects.** **Recommend Pattern A** because PIS is a framework, not a paragraph; it deserves its own H2 visual hierarchy. Pattern B is the fallback if cadence demands.

**Anti-pattern risk (highest):**

- **EC1 canonical-definition verification (CRITICAL)** — P/I/S phase mapping must match canon; **verified PASS per analysis above**; Drafter must preserve.
- **A2 first-definition load-bearing (HIGH)** — PIS is being first-introduced; must define precisely enough for cross-chapter coherence and glossary E58.
- **Framework-attribution (HIGH)** — direct application; "Julie's Problem/Identify/Solution framework" → joint book IP framing.
- **Forbidden vocab (MED)** — "organizational design equivalent" must be reframed.
- **A4 (LOW)** — credentialing; framework-attribution scrub addresses.
- **A1 (LOW)** — closer is operator-direct declarative; CLEAN.
- **A13 (LOW)** — closer lands operator outcome; CLEAN.

**Framework-attribution rule:** **Applies directly.** PIS is canonical Compound vocabulary (pending glossary E58) — joint book IP. Strip "Julie's Problem/Identify/Solution framework" individual framing. Origin-credit to Julie's CHRO practice acceptable as one sentence but never as her individual instrument.

**Coherence:**

- Lands as new H2 (Pattern A, recommended) between L22 (§5.0 closer) and L24 (§5.1 heading). H2 title flagged for Drafter: "The *PIS* lens." or "Source is the *Identify* phase." or similar.
- Must read as **the diagnostic-sequencing lens that explains why Source comes second**: Signal names the Problem, Source Identifies what the organization knows about it, Design+Build produce the Solution. PIS is the lens; the Sequence is the operational instantiation.
- **Cross-chapter coherence: Ch 3 §3.3 reference.** Ch 3 currently introduces the six-stage Sequence at §3.3 (L57–L93) including Signal / Source / Design / Build / Deliver / Compound — but does NOT reference PIS. The Ch 3 Sequence definition stands; E31 lands PIS as a complementary lens, not a replacement. Verify Drafter does NOT re-introduce the six-stage Sequence in E31 — reference is one-line ("Signal names the Problem; Source Identifies what is known; Design and Build are the Solution").
- **Cross-chapter coherence: Glossary E58.** PIS is one of the seven glossary additions in E58. E58 (Ch 15 / glossary) will add the canonical definition to the glossary. **Flagged but not blocking E31 landing.**
- E31 must NOT pre-empt §5.1 (Knowledge Map deliverable definition). PIS framing lands BEFORE the Knowledge Map is defined; verify Drafter does NOT introduce Knowledge Map naming before §5.1 picks it up. Reference is "the inventory" / "what the organization knows" / "the Identify phase produces."
- E31 must NOT pre-empt §5.5 "Transcripts" or §5.7 "Knowledge management in an *agentic* world." PIS is the diagnostic-sequencing lens; specific instruments land later.

---

### E32 (NEW-SECTION, LAND-WITH-MODIFICATION) — Julie's "Missing sources column is most important" framing

**Substance to preserve (from `_julie/julie-redline.md:1611–1623`):**

- The substantive insight: in the Knowledge Map's three-section structure (Digital / Organic / Missing), **the Missing sources column is the most important** — because Missing sources are where the highest-risk gaps live.
- The two-category pattern of Missing sources (preserve as observational two-option, NOT triplet): **(a) decisions made by leaders who have since left (Management knowledge loss); (b) customer/market intelligence never systematically captured (Leadership knowledge that existed in individuals who are no longer available).**
- The operator outcome: "The Knowledge Map's missing sources column is where the sprint finds its highest-risk gaps. Every missing source is a potential sprint failure mode."
- The discipline directive: "Name them before Build begins, not after deployment reveals them." — operator-direct declarative closer. Preserve.
- **TML cross-reference at the heart of E32's substance:** Julie's source explicitly invokes TML categories ("Management knowledge loss" + "Leadership knowledge in individuals no longer available"). **Post-E29 landing, TML vocabulary is canonical**; E32 inherits the TML naming and lands as **the chapter's first operational application of the TML framework to a specific Knowledge Map column** (Missing sources).

**Modification from Julie's instruction:**

- **Framework-attribution rule — DIRECT APPLICATION:** Julie's source opens "From an organizational design perspective, the Missing sources column is the most important. Julie's practice in every organizational design engagement is to inventory what the organization does not know it does not know." This is **double individual attribution** of joint observation. Per framework-attribution rule, reframe to joint perspective + single in-prose Julie anchor: "From a people-systems lens, the Missing sources column is the most important. Julie has watched every M&A integration produce the same finding: the highest-risk gaps are what the organization does not know it does not know." **Drafter to prefer single Julie anchor sentence + joint observational frame.**
- **A3 risk:** Julie's source presents a **two-category split** ("Management knowledge loss" + "Leadership knowledge in individuals no longer available"). **Acceptable as observational two-option diagnostic** — preserves the TML structure (Management + Leadership; Task knowledge is well-captured in systems, so not commonly Missing). Verify Drafter does NOT add a third category (e.g., do not introduce "Task knowledge that was never documented" as a third Missing category — that would conflict with TML's empirical pattern that Task knowledge is the easiest to capture).
- **A1 risk:** Julie's source closer "Every missing source is a potential sprint failure mode. Name them before Build begins, not after deployment reveals them." is operator-direct declarative — A1 CLEAN. Preserve.
- **A4 (boastful biographical):** Moderate risk. "Julie's practice in every organizational design engagement..." scope; mitigated by Preface + Ch 1 + Ch 4 + E28 + E30 attribution setup. Single in-prose attribution per author maximum.
- **A2 (coined term):** Julie's source uses "Missing sources" (canonical Knowledge Map vocabulary, defined at L57 — Pass 3 — Missing). Acceptable. "Management knowledge" and "Leadership knowledge" — canonical TML vocabulary post-E29 landing. Acceptable. Verify Drafter does NOT redefine.
- **MEANS/ENDS-RISK:** E32 reinforces §5.1 / Pass 3 Missing column definition. **MEANS/ENDS-RISK = LOW.** Closer lands operator outcome (every missing source = potential sprint failure mode; name them before Build). CLEAN.
- **Forbidden vocab:** Julie's source uses **"organizational design perspective" + "organizational design engagement"** — both forbidden per voice charter §3 in mid-market-operator context. **Strip both.** Acceptable reframes: "people-systems lens" / "knowledge inventory practice" / "every M&A integration" / "every post-acquisition assessment" / plain operator language. Watch for "transformation" / "leverage" / "synergy" / "alignment" — none in Julie's source; verify Drafter introduces zero.
- **TML cross-reference (CRITICAL):** Julie's source uses TML categories without explicit framework name (just "Management knowledge loss" and "Leadership knowledge"). Post-E29 landing, the TML framework is canonical; E32 should **reference TML explicitly** to anchor the cross-section coherence — e.g., "Per the TML framework introduced earlier, Missing sources cluster in two of the three layers: **Management knowledge** (decisions made by leaders who have since left) and **Leadership knowledge** (customer or market intelligence that existed in individuals no longer available). Task knowledge, by contrast, is the layer most commonly captured in systems — its absence is usually a documentation gap, not a knowledge loss." This ties E32 directly to E29's framework introduction and demonstrates the framework's operational application.
- **In-prose attribution:** Light. E28 has anchored Julie's voice; E30 lighter; E31 framework-level (no Julie anchor needed); E32 can land with a single passing reference ("Julie has watched..." / implicit via context "the same finding"). **Recommend implicit attribution** — E32 is the fourth Julie-voice paragraph in the chapter; attribution frequency must compress.

**Anti-pattern risk (highest):**

- **Forbidden vocab (HIGH)** — "organizational design perspective" + "organizational design engagement" both must be reframed (recurring 3/3 chapter pattern per Preface + Ch 1 + Ch 2 + Ch 4 + Ch 5 lessons-learned).
- **Framework-attribution (MED)** — "From an organizational design perspective" + "Julie's practice in every organizational design engagement" double individual attribution → reframe to joint observational with single in-prose anchor.
- **A3 third-option triplet conversion risk (MED)** — preserve Julie's two-category Missing sources frame (Management knowledge loss + Leadership knowledge); do NOT add a third category.
- **A4 (LOW)** — credentialing; mitigated by Preface + Ch 1 + Ch 4 + E28 + E30 attribution setup.
- **A1 (CLEAN)** — closer is operator-direct declarative.
- **TML cross-reference discipline (HIGH)** — E32 must explicitly reference TML framework (per E29 landing); demonstrates the framework's operational application; verifies cross-section coherence.

**Framework-attribution rule:** **Applies directly.** Knowledge Map's Missing-sources column is canonical Compound vocabulary (defined at §5.1 L57) — joint book IP. Strip "Julie's practice in every organizational design engagement" individual framing.

**Coherence:**

- Lands AFTER L57 (the Pass 3 — Missing paragraph "Look at what's absent. What would a designer need to know to solve this constraint that isn't represented anywhere in the first two passes?") AND BEFORE L59 (the §5.1 Action Step "Review your map from Pass 1 and Pass 2...").
- Must read as **the elaboration of why the Missing sources column carries the highest-stakes content** — Pass 3 defines the column, E32 explains why it's the most important and what the two Missing categories typically are (Management knowledge loss / Leadership knowledge in individuals no longer available).
- **TML cross-reference required.** E32 lands AFTER E29 has introduced TML in §5.1 (per recommended bead order). E32 references TML explicitly to demonstrate the framework's operational application: Missing sources cluster in two of TML's three layers.
- E32 must NOT pre-empt §5.4 "People don't have *APIs*" three-source-category framing (Digital / Organic / At-risk). E32 lives inside the Missing sources column; §5.4 lives across all three Knowledge Map sections. Verify Drafter does NOT conflate.
- E32 must NOT pre-empt §5.5 Transcripts framing or §5.7 Knowledge management framing.
- E32 closer reinforces §5.1 Pass 3 Action Step at L61 ("Review your map from Pass 1 and Pass 2. Write down every gap — every question a designer would ask that your current sources can't answer. Add them to the map as Missing sources."). E32 lands BEFORE the Action Step; verify Drafter does NOT duplicate or pre-empt the Action Step content.
- **N-gram coherence:** E32 should NOT verbatim-echo Julie's source closer "Every missing source is a potential sprint failure mode. Name them before Build begins, not after deployment reveals them." — this is the load-bearing operator-math closer; preserve verbatim or near-verbatim; verify no n-gram repetition with other chapter closers (§5.7 closer "Source is not where data infrastructure gets built. Source names the gaps." at L185 is closest semantic ground; check for overlap).

---

## Conflicts and risks

### Conflict 1: E29 — EC1 canonical-definition verification for TML Framework (CRITICAL)

**Source:** Ch 2 lessons-learned EC1 update (2026-05-31) — TML acronym wrongly expanded in Ch 2 first draft (M+L gloss vs. canonical Task/Management/Leadership) triggered the EC1 refinement. + Manifest E36 canon (Task → Fully Automatable, Management → AI-Assisted, Leadership → Human Judgment) + voice charter §3 canonical instruments + Ch 2 L259 forward-reference + Ch 6b work-categorization application (currently four categories, not TML's three).

**Description:** TML Framework is being **first-introduced load-bearing** in Ch 5 via E29. The Ch 5 introduction must:
- Match canonical names (Task / Management / Leadership).
- Match canonical AI-handling mapping (handle / assist / oversight).
- Be precise enough to support Ch 6b's work-lens application (E36 bead, separate execution).
- Reconcile Ch 2 L259 forward-reference (currently points to Ch 6, should point to Ch 5).
- Reconcile Ch 6b current four-category Work Deconstruction taxonomy (E36 will subsequently align).

**EC1 VERDICT after detailed analysis:** **PASS.** Julie's E29 source paragraph's TML naming and AI-handling mapping match canon. The lens difference (knowledge categorization in Ch 5 vs. work categorization in Ch 6b) is complementary — both are valid applications of the same canonical framework.

**Resolution:** No Drafter framework modification needed for canon-alignment. Drafter task: (a) preserve names + AI-handling mapping verbatim; (b) frame as knowledge lens that complements Ch 6b work lens; (c) apply framework-attribution scrub. **NO author decision required.** **Inline scout-note at the E29 landing point must explicitly flag** the canonical-definition verification (Task/Management/Leadership + handle/assist/oversight = manifest E36 canon = Ch 2 L259 forward-reference = pending Ch 6b E36 work-lens application).

**Cross-chapter coherence flagged for separate Drafter pass (not blocking E29):**
- **Ch 2 L259 forward-reference update** — change "Chapter 6 introduces..." to "Chapter 5 introduces the TML framework (Task / Management / Leadership) as the lens for organizing what the company knows; Chapter 6 applies the same framework to the work itself."
- **Ch 6b alignment with TML three categories** — E36 bead (separate execution) will bring Ch 6b's current four-category Work Deconstruction into alignment with TML's three categories. Until E36 lands, the two passages can co-exist; the Ch 5 TML introduction is the canonical source-of-record.
- **Glossary E58** — TML definition lands in glossary; canonical source is Ch 5 E29.

### Conflict 2: E31 — EC1 canonical-definition verification for PIS Framework

**Source:** Manifest E31 canon (Source = the **I**dentify phase of **P**roblem/**I**dentify/**S**olution) + Ch 3 §3.3 six-stage Sequence (Signal / Source / Design / Build / Deliver / Compound) + Glossary E58 (PIS definition pending).

**Description:** PIS Framework is being **first-introduced load-bearing** in Ch 5 via E31. The introduction must:
- Match canonical phase names (Problem / Identify / Solution).
- Match canonical phase-to-stage mapping (Problem = Signal; Identify = Source; Solution = Design + Build).
- Be precise enough to support glossary E58.
- Not conflict with Ch 3 §3.3 six-stage Sequence definition (PIS is a complementary three-phase lens, not a replacement).

**EC1 VERDICT after detailed analysis:** **PASS.** Julie's E31 source paragraph's PIS naming and phase-to-stage mapping match canon. The three-phase lens is complementary to Ch 3's six-stage Sequence — both are valid framings of the same operational discipline.

**Resolution:** No Drafter framework modification needed for canon-alignment. Drafter task: (a) preserve P/I/S phase names + Compound stage mapping verbatim; (b) apply framework-attribution scrub; (c) verify Ch 3 §3.3 Sequence is NOT re-introduced in E31. **NO author decision required.** **Inline scout-note at the E31 landing point must explicitly flag** the canonical-definition verification (P/I/S + Signal/Source/Design+Build = manifest E31 canon).

### Conflict 3: E29 + E31 — Framework-attribution rule applies directly to TWO frameworks introduced in Ch 5

**Source:** Manifest §57 (global rule) + `framework-attribution-rule` persistent memory + voice charter §3 canonical instruments.

**Description:** Ch 5 introduces TWO frameworks (TML at E29 + PIS at E31) — both joint book IP, both currently framed in Julie's source as her individual instruments ("Julie's TML framework" / "Julie's Problem/Identify/Solution framework").

**Resolution:** Strip both individual-attribution framings. Both frameworks land as joint canonical vocabulary. Origin-credit to Julie's CHRO practice acceptable as one sentence per framework if framing demands; never as her individual instrument. **Drafter must verify both reframes land cleanly** — single Julie anchor per framework MAX (or skip individual attribution entirely; let frameworks land as joint vocabulary).

### Conflict 4: E28 — cross-chapter coherence with FOUR PRIOR a global food safety company anchors (HIGH n-gram risk)

**Source:** Preface L9 (a global food safety company 44-country Fortune-500 acquisition / CHRO context) + Ch 1 L57 (a global food safety company headcount-math redesign / smaller proportional team) + Ch 2 §2.3 (a global food safety company graft-vs-redesign story) + Ch 4 L18 (a global food safety company matrix-reporting / no-replacement story) + Ch 5 E28 source (a global food safety company tribal-knowledge inheritance).

**Description:** E28 is the **fifth** a global food safety company anchor in the manuscript. The cumulative risk of cross-chapter n-gram repetition is HIGH — same employer (anonymized "global food safety company"), same Fortune-500 acquisition context, same 2022 timeframe (Preface), same Julie-CHRO scope. Each anchor must differentiate by:
- The specific story angle (tribal-knowledge inheritance for E28).
- The phrasing surrounding the company name (do NOT reuse Preface's "44 countries / challenge wasn't technology" / Ch 1's "smaller proportional team" / Ch 2's "graft-vs-redesign / countries / supplier networks" / Ch 4's "matrix-reporting / two reporting lines crossed").

**Resolution:** E28's differentiating angle is **inherited tribal knowledge / process experts whose expertise was the documentation / "if this person were not here tomorrow, what would stop working?" diagnostic question**. Drafter to verify no phrasing overlap with the four prior anchors. **N-gram check at threshold 0.85 mandatory** per voice-scan pipeline.

### Conflict 5: E29 cross-chapter coherence with Ch 2 L259 forward-reference (cross-chapter coherence fix flagged but NOT blocking)

**Source:** Current Ch 2 L259 ("Chapter 6 introduces the full design instrument — the **TML framework** (Task / Management / Leadership) — which sorts work into three categories rather than two").

**Description:** Ch 2 L259 forward-references TML as introduced in Chapter 6. After E29 lands (TML introduced in Chapter 5 first), this forward-reference is technically inaccurate (off by one chapter).

**Resolution:** Drafter to update Ch 2 L259 in a separate edit pass — change "Chapter 6 introduces..." to "Chapter 5 introduces the **TML framework** (Task / Management / Leadership) as the lens for organizing what the company knows; Chapter 6 applies the same framework to the work itself." **Flagged for cross-chapter coherence; not blocking E29 landing in Ch 5.**

### Conflict 6: E29 cross-chapter coherence with Ch 6b Work Deconstruction taxonomy (NOT blocking E29)

**Source:** Current Ch 6b uses four categories (Human judgment required / Agent-assisted / Fully automatable / Workflow automation only), not TML's three (Task → Fully Automatable / Management → AI-Assisted / Leadership → Human Judgment).

**Description:** Ch 6b's current four-category Work Deconstruction is not yet aligned to TML. Per manifest E36, Ch 6b will be aligned (Task → Fully Automatable, Management → AI-Assisted, Leadership → Human Judgment). E36 is a separate bead (Ch 6b execution, not Ch 5).

**Resolution:** E29 lands the canonical three-category TML framework as the **knowledge lens** in Ch 5. E36 will subsequently align Ch 6b's work-lens to the same three categories. Until E36 lands, the two passages co-exist — E29 is the canonical source-of-record. **Flagged for cross-chapter coherence; NOT blocking E29 landing.**

### Conflict 7: E28 + E29 + E30 + E31 + E32 — Forbidden vocab "organizational design" recurrence (recurring 3/3+ chapter pattern)

**Source:** Julie's source for E28 ("every organizational design engagement I have run") + E29 ("organizational design foundation of the knowledge mapping work") + E31 ("organizational design equivalent of prescribing before diagnosing") + E32 ("From an organizational design perspective" + "every organizational design engagement") + voice charter §3 forbidden vocabulary rule + lessons-learned cross-chapter pattern (Preface + Ch 1 + Ch 2 + Ch 4 all required scrubs).

**Description:** Julie's source paragraphs for ALL FOUR Julie-voice rows (E28, E29, E31, E32) use "organizational design" in some form — forbidden vocabulary in mid-market-operator context per voice charter §3. This is the **most pervasive forbidden-vocab pattern in the chapter** and the recurring 3/3+ chapter pattern per lessons-learned.

**Resolution:** Reframe in ALL four paragraphs to plain operator language. Acceptable alternatives: "people-systems lens" / "M&A integration practice" / "the way the work is set up" / "knowledge inventory engagements" / "every post-acquisition assessment" / plain operator equivalents. **Drafter scanner gate MUST catch zero "organizational design" / "organizational design perspective" / "organizational design engagement" / "organizational design foundation" / "organizational design equivalent" in E28, E29, E30, E31, E32 output.**

### Conflict 8: E29 — A3 stacked triplet risk (three-layer framework + second wave of parallel description)

**Source:** Julie's E29 source has TWO triplet structures stacked: (a) the three-layer framework definition (Task / Management / Leadership — observational, acceptable); (b) the second wave "Task knowledge is the easiest to capture and the most common to find in systems. Management knowledge is partially documented but inconsistently followed. Leadership knowledge almost never exists outside the people who hold it." (constructed parallel triplet — A3 trap).

**Description:** The framework definition is acceptable as a three-category enumeration (it IS the framework). The second wave of parallel description converts the observational three-category framework into a constructed parallel triplet.

**Resolution:** Collapse the second wave into a single sentence with semicolon bridges: "Task knowledge is the easiest to capture and the most common to find in systems; Management knowledge is partially documented and inconsistently followed; Leadership knowledge almost never exists outside the people who hold it." Single sentence preserves the structure while avoiding stacked triplet cadence.

### Conflict 9: E30 — A1 AI-tell closer "That is what At-Risk Source does"

**Source:** Julie's E30 source closer "That is what At-Risk Source does: it names what nobody knew they were about to lose." + voice charter §4 A1 and §4 A3-tag-closer-pattern rejection ("That is the X this [book/chapter/sprint] exists to Y" is forbidden).

**Description:** The "That is what At-Risk Source does" cadence is the AI-tell mission-statement closer pattern flagged in lessons-learned and risk-map.

**Resolution:** Preserve substance (At-Risk Source names what nobody knew they were about to lose), cut "That is what" cadence. Acceptable rewrites in E30 acceptance criteria above.

### Conflict 10: E32 — TML cross-reference dependency on E29 landing first

**Source:** E32's substance explicitly invokes TML categories (Management knowledge loss + Leadership knowledge in individuals no longer available). TML must be introduced (E29) BEFORE E32 lands.

**Description:** E32 lands inside §5.1 (Pass 3 Missing column description). E29 also lands inside §5.1 (per recommended landing). **E29 must execute first in the bead order**; E32 inherits the TML vocabulary.

**Resolution:** Bead execution order: E28 → E29 → E31 → E30 → E32 (per recommended order below). E29 lands TML; E32 references TML explicitly.

### Conflict 11: E28 chutes-and-ladders cross-reference at L130 (proper-noun italicization)

**Source:** L130 currently says "Remember the developer who walked out with everything he knew?... If I had mapped where the knowledge lived before that developer left, the handoff would have been a step instead of a slide." + Preface index.qmd:5 canonical chutes-and-ladders metaphor "his business was a game of *Chutes and Ladders*" with proper-noun italicization + `ahmed-story-is-chutes-and-ladders` persistent memory.

**Description:** The L130 cross-reference does NOT currently use the proper-noun "Chutes and Ladders" italicization; it references the developer-departure story without the proper-noun metaphor. Acceptable but flagged: the Preface canonically uses italicized "*Chutes and Ladders*" as the proper noun. Drafter may choose to (a) preserve current phrasing (developer reference without italics), or (b) reintroduce the proper-noun metaphor with italics ("the chute that opened when our developer walked out, like a square on the *Chutes and Ladders* board").

**Resolution:** Drafter chooses based on cadence. **Recommend preserving current phrasing** (developer reference without proper-noun re-introduction) for two reasons: (1) the Preface establishes the metaphor; chapter cross-references can land plain; (2) re-introducing the metaphor mid-chapter risks decorative redundancy. If Drafter reintroduces, italicize per Preface convention.

### Conflict 12: Marina story cross-chapter coherence (Ch 2 L8 + Ch 5 L8 + Ch 5 L30)

**Source:** Marina is canonically introduced in Ch 2 L8 ("Jesse was in a management meeting with Marina, his Integrator..."). Ch 5 currently uses Marina at L8 and L30 with "I" / "Marina and I" — needs blended-we shift per E28 cascade.

**Description:** The Marina anchor in Ch 5 must inherit the Ch 2 attribution convention. Per Q-E21 and Ch 2 E16 (already landed), Marina is referenced as "Jesse + Marina" or "Marina + Jesse" or via blended-we ("we" with Jesse anchor at the chapter's first Marina reference).

**Resolution:** Drafter applies E28 attribution cascade across L8 + L30 + L130. Verify Marina's role-naming (project coordinator decision-maker, Integrator) does NOT shift between Ch 2 and Ch 5. The Ch 5 references are about the Marina+Jesse coordinator-redesign conversation (same anchor as Ch 2).

### Conflict 13: Meridian Source-stage threading (cross-chapter coherence with Ch 3 Sprint Planning Canvas)

**Source:** Ch 3 §3.4 Sprint Planning Canvas Source row at L165 ("Elena holds the quoting logic. Dave Kowalski (Sr Design Engineer, 31 years) holds the fabrication knowledge... Ty Banfield (Sales Lead) owns HubSpot CRM... 'Customer Notes.xlsx' — 147 rows of pricing exceptions... JobBOSS ERP holds job history but is not connected to CRM.") + Ch 5 §5.6 Sprint · Source at Meridian at L155–L163 + Meridian populated Knowledge Map at L205–L213 + `pm-case-study-thread-through-book` persistent memory.

**Description:** Ch 5 §5.6 (Sprint · Source at Meridian) is the canonical worked-example of Source at Meridian, and matches Ch 3 §3.4 Sprint Planning Canvas Source row (same specifics: Elena's quoting logic, Dave's 31-year fabrication knowledge, Ty's CRM ownership, Customer Notes.xlsx with 147 rows, JobBOSS ERP not connected). The populated Knowledge Map at L205–L213 includes all these elements as table rows.

**Resolution:** **Verify cross-chapter consistency: Meridian Source-stage specifics in Ch 5 (§5.6 + L205–L213) match Ch 3 §3.4 Sprint Planning Canvas Source row.** Cross-reference verified: ✓ (current chapter matches Ch 3). E28 / E29 / E30 / E31 / E32 do NOT touch the Meridian Sprint section — preserve verbatim. **Flagged for awareness; not blocking.**

### MEANS/ENDS-RISK — full §5 sweep (MANDATORY per scout.md §5)

Per scout.md §5, MANDATORY means-vs-ends check on opener, closer, and any paragraph framing the framework/Sequence/Sprint/Source/TML/PIS as destination. Findings:

- **Chapter opener L8–L14 (E28 scope, attribution-only on Marina story side):** Story-based (specific Marina + $24K coordinator decision), not "this chapter is about..." abstract framing. **CLEAN.** Grandfathered chapter prose, not in scope for E28 modification beyond attribution.
- **In Brief (L3–L6):** "Source maps the information environment around the one constraint Signal validated. You're answering a specific question: what does our organization know about *this problem*, and where does that knowledge live? The deliverable is a one-page Knowledge Map — a six-column table (Source, Type, Owner, Status, Pipeline, Notes) that inventories every digital system, person, and gap relevant to the constraint. Skip Source and Design becomes a guessing exercise built on assumptions nobody verified." — Source-as-discipline framed with operator outcome (deliverable = one-page Knowledge Map; skip = Design guessing exercise = cost). **CLEAN.** Out of scope; grandfathered.
- **E28 (Julie's parallel global food safety company tribal-knowledge story, lands between L14 and L16):** Chapter-opener-adjacent. **MEANS/ENDS-RISK = MED.** Acceptance criterion: close on operator outcome (inherited tribal knowledge surfaced before integration failure / "if this person were not here tomorrow, what would stop working" question that prevented downstream loss); name Source as the means. **FLAGGED** in E28 acceptance criteria above.
- **E29 (TML Framework introduction, lands inside §5.1):** **MEANS/ENDS-RISK = LOW.** TML introduction reinforces Source diagnostic discipline (means) but closes with operator outcome (each layer requires different capture/transfer; AI can handle some, assists with others, requires oversight on the third). CLEAN if framing closes on AI-handling mapping (operator outcome). **FLAGGED.**
- **E30 (Julie's senior pricing strategist At-Risk Source story, lands inside §5.4):** Reinforces §5.4 existing at-risk-source thesis. **MEANS/ENDS-RISK = LOW.** Closer lands operator outcome (two years to reconstruct avoided / pricing errors avoided / four weeks captured everything). CLEAN per Julie's source. **FLAGGED.**
- **E31 (PIS Framework introduction, lands as new H2 between L22 and L24):** Chapter-framing-adjacent. **MEANS/ENDS-RISK = MED.** PIS introduction reinforces sequencing discipline (means) but closes with operator outcome (wrong-problem inventory = wasted Sprint). CLEAN per Julie's source; verify Drafter does NOT invert. **FLAGGED.**
- **E32 (Julie's Missing sources column framing, lands inside §5.1 Pass 3):** Reinforces Pass 3 Missing column definition. **MEANS/ENDS-RISK = LOW.** Closer lands operator outcome (every missing source = potential sprint failure mode; name them before Build, not after deployment). CLEAN per Julie's source. **FLAGGED.**
- **§5.0 closer L16–L22:** "Diagnosis is not done until you know what you *have*" → "To become a Co-Intelligent Company capable of Co-Intelligent Co-Operation requires knowing what you're working with..." → "Source produces that ground truth. Skip it and you won't get past the first design conversation..." → "This is why Source belongs in Diagnose, not Execute. The diagnosis includes the information environment. Until you've mapped what you have, the constraint is a named problem without a buildable path forward. Once the map exists, it becomes a design problem — scoped, specific, and grounded in reality." — Source-as-discipline framed with operator outcome (ground truth produced, design conversation enabled, constraint becomes buildable). **CLEAN.** Out of scope; grandfathered.
- **§5.1 Knowledge Map deliverable L24–L66:** Deliverable IS the operator outcome (one-page table, six columns, three-pass build). **CLEAN.** Out of scope; grandfathered.
- **§5.2 Classification L68–L94:** Classification axes + AI tiers — operational instructions; no means-as-destination risk. **CLEAN.** Out of scope; grandfathered.
- **§5.3 How systems talk L96–L116:** API / MCP / Connector definitions in plain operator language. **CLEAN.** Out of scope; grandfathered.
- **§5.4 People don't have APIs L118–L130:** Three-source-category framing (Digital / Organic / At-risk) with the developer chutes-and-ladders cross-reference at L130. **CLEAN.** Out of scope; grandfathered (E28 cascades I→we at L130 but does NOT alter structure).
- **§5.5 Transcripts L132–L149:** Transcripts-as-API-substitute discipline; operator-recognizable. **CLEAN.** Out of scope; grandfathered.
- **§5.6 Sprint · Source at Meridian L151–L163:** Concrete worked example. **CLEAN.** Out of scope; grandfathered.
- **§5.7 Knowledge management L165–L185:** Garbage-in-garbage-out framing with concrete SuperWebPros learning at L177. **CLEAN.** Out of scope; grandfathered.
- **§5.8 Completeness test L187–L201:** Six checks. **CLEAN.** Out of scope; grandfathered.
- **§5.9 Hand off to Design L217–L223:** Closer hands off to Ch 6 with operator outcome framing (constraint + Knowledge Map = Design input). **CLEAN.** Out of scope; grandfathered.
- **Reflection Questions L225–L231:** Engage reader operator on their own constraints — four operator-direct questions. **CLEAN.** Out of scope; grandfathered.

§5 check confirmed: **E28 + E29 + E31 are at active MEANS/ENDS-RISK = MED.** E30 + E32 at LOW. All five flagged with explicit acceptance criteria.

### A2 trap full sweep — Ch 5 canonical vocabulary

Per voice-charter §3 and lessons-learned (A2 coined-term-before-defined: recurring 2/3+ chapters). Ch 5 introduces or load-bears on several canonical terms and instruments:

- **Source** = the stage (canonical, defined in Ch 3 §3.3 + In Brief at L3–L6 + opening framing at L14). Already staked by Ch 5; E28 / E29 / E30 / E31 / E32 may use Source freely.
- **Knowledge Map** = the canonical Source deliverable. Defined at §5.1 L24–L66 (table structure: six columns, three-pass build) + In Brief at L5. **A2 risk:** E28 + E29 + E31 land BEFORE §5.1 defines Knowledge Map; **must use "knowledge" / "what the work requires" / "what people know" / "the inventory" plain operator language, NOT "Knowledge Map" capitalized**, before §5.1 defines. E30 + E32 land AFTER §5.1; "Knowledge Map" capitalized acceptable.
- **TML Framework** = canonical (charter §3 + manifest E36 + Ch 2 L259 forward-reference + Ch 6b work-lens application pending E36). **First load-bearing introduction in Ch 5 via E29.** Per A2: definition must be precise (Task/Management/Leadership names + AI-handling mapping at handle/assist/oversight). Cross-chapter coherence: Ch 2 L259 forward-reference update flagged for separate edit; Ch 6b alignment via E36 separate bead.
- **PIS Framework** = canonical (per manifest E31 + pending glossary E58). **First load-bearing introduction in Ch 5 via E31.** Per A2: definition must be precise (Problem/Identify/Solution names + Compound stage mapping P=Signal, I=Source, S=Design+Build).
- **Source Agent** = canonical Compound Bench / Skills Library instrument (charter §3 — one of the six Compound Bench agents). **NOT load-bearing in E28 / E29 / E30 / E31 / E32.** Per stale-audit + lessons-learned, Bench / Skills Library product references were purged per `48cef93` commit. **Verify Drafter does NOT re-introduce Source Agent vocabulary in any Ch 5 edits** — Source Agent is not in the current chapter and should remain absent unless the Bench framework is reintroduced book-wide (out of scope for Ch 5).
- **Data Pipeline Audit** = canonical (Pipeline column / fifth column of Knowledge Map per §5.1 L41 + §5.3 L96–L116 API/MCP/Connector framing). Already staked in Ch 5; E28 / E29 / E30 / E31 / E32 may reference if needed.
- **Constraint** + **Symptom** = canonical (Ch 4 §4.3 L47–L49 + L51). E29 + E30 + E31 + E32 do not redefine — verify Drafter does NOT redefine.
- **At-Risk Source** = canonical Ch 5 vocabulary (defined at L126 in §5.4). E30 lands AFTER L126; acceptable use. Verify Drafter does NOT redefine.
- **Missing sources** = canonical Knowledge Map vocabulary (defined at L57 in §5.1 Pass 3). E32 lands AFTER L57; acceptable use. Verify Drafter does NOT redefine.
- **Hybrid Accountability Chart (HAC)** = canonical Ch 6 vocabulary. **NOT load-bearing in E28 / E29 / E30 / E31 / E32.** Forward reference is acceptable if Drafter introduces (single instance, no definition); not required.
- **Compound Sprint / Sprint** = canonical (Ch 3 §3.3 + In Brief). Already staked. E28 / E29 / E30 / E31 / E32 may use freely.

**E28 / E29 / E30 / E31 / E32 A2 discipline:**

- E28 (lands before §5.1): plain operator language only. "Knowledge" lowercase plain is fine; "Knowledge Map" capitalized NOT until §5.1 defines. "TML" NOT until E29 defines (E28 executes first; E29 second; ordering preserves discipline). "PIS" NOT until E31 defines.
- E29 (lands inside §5.1): "Knowledge Map" capitalized acceptable (§5.1 has landed conceptually with the H2 heading); the H2 defines the deliverable in the paragraph immediately following E29's landing. Acceptable. **TML is first-defined here.** Do NOT pre-empt PIS (defined at E31).
- E30 (lands inside §5.4): "At-Risk Source" capitalized acceptable (§5.4 L126 defines). "TML" acceptable (E29 defined earlier in chapter). "PIS" acceptable (E31 defined earlier in chapter).
- E31 (lands between L22 and L24, before §5.1): "PIS Framework" first-defined here. Do NOT pre-empt Knowledge Map naming (defined at §5.1 L24 immediately after).
- E32 (lands inside §5.1 Pass 3): "Missing sources" capitalized acceptable (Pass 3 L57 defines). "TML" acceptable (E29 defined). "Management knowledge" + "Leadership knowledge" acceptable (TML categories defined via E29). Do NOT redefine.

### EC1 canonical-definition verification (per Ch 2 lessons-learned, MANDATORY for E29 + E31 in Ch 5)

Per Ch 2 EC1 update (2026-05-31): when a coined term is used in E-rows, the definition must match the canonical definition from voice-charter §3, manifest, glossary, or chapter canon.

- **TML Framework in E29:** Canonical definition is Task / Management / Leadership (three categories) + AI-handling mapping (handle / assist / oversight) per manifest E36 + voice charter §3. Julie's E29 source: Task knowledge (SOPs/process maps) + Management knowledge (decision rights/escalation/governance) + Leadership knowledge (judgment/relationships/context) + AI-handling mapping (handle/assist/oversight). **EC1 VERDICT: PASS.** Names match. AI-handling mapping matches. Lens (knowledge categorization vs. work categorization in Ch 6b) is complementary, not contradictory. Both lenses are valid applications of the same canonical framework.
- **PIS Framework in E31:** Canonical definition is Source = the Identify phase of Problem/Identify/Solution per manifest E31. Julie's E31 source: Problem = Signal-validated constraint; Identify = Source (everything known about the problem); Solution = Design + Build. **EC1 VERDICT: PASS.** Phase names match. Phase-to-Compound-stage mapping matches. Sequencing discipline (you don't move to Solution until Identify is complete) is the load-bearing argument and matches canon.
- **"Source" in E28 + E30:** Canonical definition is "the stage that maps the information environment around the validated constraint" (per Ch 3 §3.3 + Ch 5 In Brief). Julie's sources match (E28: "Source closes that gap before it becomes a sprint failure"; E30: "He was not identified as an at-risk knowledge source until Source was run"). **EC1 VERDICT: PASS.**
- **"At-Risk Source" in E30:** Canonical definition is "institutional knowledge that lives in one person's head and is about to leave" (per Ch 5 L126). Julie's source matches (twenty-year pricing strategist held knowledge in his head, four weeks before retirement). **EC1 VERDICT: PASS.**
- **"Missing sources" in E32:** Canonical definition is one of three Knowledge Map sections (per Ch 5 L57 Pass 3 Missing). Julie's source matches (two categories of Missing sources: Management knowledge loss + Leadership knowledge in individuals no longer available). **EC1 VERDICT: PASS.**

**All EC1 verdicts: PASS. No author decision required for canon-alignment.**

---

## Recommended bead order

Execute in this order. Dependencies in parentheses.

1. **E28** (ATTRIBUTION + NEW-SECTION → LAND-WITH-MODIFICATION, Path A — Drafter solo)
   - Apply blended-we + single in-prose Jesse attribution at L8 opener; cascade I→we at L10, L12, L30, L130
   - Reject Julie's inline `Jesse:` and `Julie:` tags (per Q-E21 convention)
   - **PRESERVE Marina + $24K coordinator story verbatim** (canonical polished replacement per `6c99346`)
   - **PRESERVE L130 chutes-and-ladders developer cross-reference** (per `ahmed-story-is-chutes-and-ladders` and `pm-case-study-thread-through-book` memories); italicize *Chutes and Ladders* only IF proper noun reintroduced
   - Add Julie's parallel global food safety company tribal-knowledge story AFTER L14 (Marina story closer "Mapping that flow was Source...") AND BEFORE L16 (§5.0 heading)
   - **Framework-attribution scrub:** "every organizational design engagement I have run" → joint observational with single in-prose Julie anchor
   - **Cross-chapter n-gram check:** verify no verbatim phrasing overlap with Preface L9 (44-country / Fortune-500 / "challenge wasn't technology") + Ch 1 L57 (smaller proportional team) + Ch 2 §2.3 (graft-vs-redesign / countries / supplier networks) + Ch 4 L18 (matrix-reporting / two reporting lines crossed)
   - **Differentiating angle:** inherited tribal knowledge / process experts whose expertise was the documentation / "if this person were not here tomorrow, what would stop working?" diagnostic question
   - **Forbidden vocab grep:** zero "organizational design" / "transformation" / "leverage" / "synergy" / "alignment" — Drafter scanner gate mandatory (recurring 3/3+ chapter pattern)
   - **E60 anonymization:** "a global food safety company" already conforms; "Fortune 500 parent / division" already conforms
   - **Contractions:** preserve current chapter contractions; do not regress to Julie's no-contractions source
   - *Why first:* Sets the voice E29 / E30 / E31 / E32 write into. Zero dependency on other E-rows. Establishes Julie-voice anchor in the chapter; subsequent rows can use lighter / implicit attribution.

2. **E29** (FRAMEWORK-ADD → LAND-WITH-MODIFICATION, Path A — Drafter solo) **[CANONICAL TML INTRODUCTION — HIGHEST PRIORITY]**
   - Insert as paragraph inside §5.1 AFTER L20 ("Source produces that ground truth..."), BEFORE L22 ("This is why Source belongs in Diagnose..."); Pattern A preferred
   - Alternative landing: new H3 between L22 and L24 (Pattern B fallback)
   - **EC1 CANONICAL-DEFINITION VERIFICATION (CRITICAL):** preserve Task/Management/Leadership names exactly; preserve AI-handling mapping (handle/assist/oversight) verbatim; verify per manifest E36 + Ch 2 L259 forward-reference + Ch 6b E36 work-lens application pending
   - **A2 first-definition load-bearing:** define TML precisely (Task knowledge = SOPs/process maps; Management knowledge = decision rights/escalation/governance; Leadership knowledge = judgment/relationships/context); AI handles Task / assists Management / requires oversight for Leadership
   - **Framework-attribution scrub:** "Julie's TML framework" → "The **TML framework** (Task / Management / Leadership)" joint canonical-vocabulary introduction
   - **A3 stacked triplet collapse:** three-layer framework definition acceptable (it IS the framework); second wave "Task is easiest... Management is partial... Leadership rarely exists..." → single-sentence semicolon-bridge form ("Task knowledge is the easiest to capture and the most common to find in systems; Management knowledge is partially documented and inconsistently followed; Leadership knowledge almost never exists outside the people who hold it.")
   - **Forbidden vocab:** strip "organizational design foundation of the knowledge mapping work" → "the design logic of Source" or remove entirely
   - **In-prose attribution:** light; framework lands as joint vocabulary; acceptable single origin-credit to Julie's CHRO practice if framing demands (but not required)
   - **Frame as knowledge lens:** signal that the same TML framework will be applied to work in Ch 6b (forward reference acceptable single instance)
   - **MEANS/ENDS-RISK:** close on AI-handling mapping (operator outcome) rather than abstract "diagnostic structure" (system-as-destination)
   - **Cross-chapter coherence flagged for separate Drafter pass (not blocking):** Ch 2 L259 forward-reference update + Ch 6b alignment via E36 separate bead + Glossary E58 inherits canonical definition from Ch 5
   - *Dependency:* E28 (Julie-voice anchor established at chapter opener).

3. **E31** (FRAMEWORK-ADD → LAND-WITH-MODIFICATION, Path A — Drafter solo) **[CANONICAL PIS INTRODUCTION — HIGH PRIORITY]**
   - Insert as new H2 between L22 (§5.0 closer "Once the map exists, it becomes a design problem...") and L24 (§5.1 heading "Create a *Knowledge Map*"); Pattern A preferred
   - H2 title flagged for Drafter: "The *PIS* lens." or "Source is the *Identify* phase." or similar
   - Alternative landing: paragraph in §5.0 between L22 and L24 (Pattern B fallback)
   - **EC1 CANONICAL-DEFINITION VERIFICATION (CRITICAL):** preserve P/I/S names + Compound stage mapping (P=Signal, I=Source, S=Design+Build) verbatim; verify per manifest E31
   - **A2 first-definition load-bearing:** define PIS precisely (Problem = Signal-validated constraint; Identify = Source phase; Solution = Design + Build); sequencing discipline (you don't move to Solution until Identify is complete)
   - **Framework-attribution scrub:** "Julie's Problem/Identify/Solution framework" → "The **Problem/Identify/Solution (PIS) framework**" joint canonical-vocabulary introduction
   - **Forbidden vocab:** strip "organizational design equivalent of prescribing before diagnosing" → "the same discipline as prescribing before diagnosing" (preferred) or "the structural equivalent of"
   - **A3 risk:** preserve three-phase framework definition; do NOT add second wave of parallel description
   - **A1 closer:** preserve "A Source run on the wrong constraint is a well-organized inventory of the wrong problem." — operator-direct declarative; CLEAN
   - **MEANS/ENDS-RISK:** PIS introduction reinforces sequencing discipline (means) but closes with operator outcome (wrong-problem inventory = wasted Sprint); verify Drafter does not invert
   - **In-prose attribution:** light; framework lands as joint vocabulary; acceptable single origin-credit if framing demands
   - **Cross-chapter coherence flagged for separate Drafter pass (not blocking):** Glossary E58 inherits canonical definition from Ch 5; Ch 3 §3.3 Sequence not re-introduced in E31
   - *Dependency:* E28 (Julie-voice anchor established at chapter opener); E29 (cumulative framework attribution discipline pattern established).

4. **E30** (NEW-SECTION → LAND-WITH-MODIFICATION, Path A — Drafter solo)
   - Insert as paragraph inside §5.4 "People don't have *APIs*" AFTER L126 (at-risk-source paragraph closer "For most operating companies this is the single most consequential thing Source does.") AND BEFORE L128 (the "When you're building your map, ask explicitly..." paragraph)
   - Julie's senior pricing strategist At-Risk Source story (20 years pricing exceptions captured in 4 weeks before retirement)
   - **Framework-attribution scrub:** "Julie's M&A integration practice identified" → "Julie has watched the same pattern in every M&A integration" joint observational + single in-prose Julie anchor (lighter than E28 anchor)
   - **A1 AI-tell closer fix:** cut "That is what At-Risk Source does:" cadence; preserve substance (At-Risk Source names what nobody knew they were about to lose); use simple declarative or combine with operator-math closer
   - **N-gram coherence check:** verify no verbatim echo with Ch 5 L161 Meridian Sprint beat ("Dave — Organic, at-risk, four years to retirement with an undocumented estimation method"); differentiate by specifics (twenty years / pricing exceptions / four weeks / two years to reconstruct vs. four years to retirement / fabrication estimation / 31 years)
   - **Operator-math closer:** preserve "four weeks to work with him before he retired. They captured everything" beat + "two years to reconstruct... pricing errors throughout the transition period" beat verbatim or near-verbatim
   - **Forbidden vocab grep:** zero "transformation" / "leverage" / "synergy" / "alignment" / "organizational design" — Drafter scanner gate mandatory
   - **E60 anonymization:** "a global food safety company" already conforms
   - **In-prose attribution:** light; implicit via context (global food safety company anchor already established as Julie's CHRO context) acceptable; single Julie anchor maximum
   - *Dependency:* E28 (Julie-voice anchor established), E29 (TML vocabulary established — E30 reinforces At-Risk Source as a Leadership-knowledge case study by implicit reference if needed).

5. **E32** (NEW-SECTION → LAND-WITH-MODIFICATION, Path A — Drafter solo)
   - Insert as paragraph inside §5.1 (Create a *Knowledge Map*) AFTER L57 (Pass 3 — Missing paragraph "Look at what's absent. What would a designer need to know to solve this constraint that isn't represented anywhere in the first two passes?") AND BEFORE L59 (§5.1 Action Step "Review your map from Pass 1 and Pass 2...")
   - Julie's "Missing sources column is most important" framing (two categories: Management knowledge loss + Leadership knowledge in individuals no longer available)
   - **Framework-attribution scrub:** "From an organizational design perspective" + "Julie's practice in every organizational design engagement" double individual attribution → joint observational with single in-prose Julie anchor + reframe vocabulary
   - **Forbidden vocab (HIGH):** strip "organizational design perspective" + "organizational design engagement" — replace with "people-systems lens" / "knowledge inventory practice" / "every M&A integration" / "every post-acquisition assessment" or plain operator language; Drafter scanner gate must catch zero "organizational design" instances
   - **A3 third-option triplet conversion risk:** preserve Julie's two-category Missing sources frame (Management knowledge loss + Leadership knowledge in individuals no longer available); do NOT add a third category (e.g., do not introduce "Task knowledge that was never documented" as a third Missing category — Task knowledge is rarely Missing per TML empirical pattern)
   - **TML cross-reference (CRITICAL):** reference TML framework explicitly (post-E29 landing); demonstrate operational application — Missing sources cluster in two of three TML layers (Management + Leadership; Task is rarely Missing)
   - **A1 closer:** preserve "Every missing source is a potential sprint failure mode. Name them before Build begins, not after deployment reveals them." — operator-direct declarative; CLEAN
   - **In-prose attribution:** light; implicit via context preferred (fourth Julie-voice paragraph in chapter; attribution frequency must compress)
   - **N-gram check:** verify no verbatim echo with §5.7 closer at L185 ("Source is not where data infrastructure gets built. Source names the gaps.") — closest semantic ground; check for overlap on "gap" / "Source names" / "Build begins"
   - **EC1:** "Missing sources" is canonical Knowledge Map vocabulary (L57); E32 elaborates, does NOT redefine
   - *Dependency:* E28 (Julie-voice anchor), E29 (TML vocabulary canonical), E30 (At-Risk Source vocabulary canonical), E31 (PIS vocabulary canonical).

**Path A beads:** All five landing rows (E28, E29, E30, E31, E32). Default to solo Drafter per AGENT-TEAM §1 lessons-learned default + Ch 2 / Ch 3 / Ch 4 outcome (Path A produced clean Ch 2 in 3 iterations).

**Path B candidates if any bead fails voice-gate twice:**

- **E29** — EC1 canonical-definition verification + A2 first-definition load-bearing + framework-attribution scrub + A3 stacked triplet collapse + forbidden-vocab discipline + cross-chapter coherence (Ch 2 L259 + Ch 6b E36 alignment) + MEANS/ENDS-RISK. **Seven intersecting controls — highest anti-pattern density in Ch 5.**
- **E31** — second-highest-risk: A2 first-definition + framework-attribution + forbidden-vocab discipline + MEANS/ENDS-RISK (four controls).
- **E28** lower-priority Path B: cross-chapter n-gram avoidance + framework-attribution scrub + Q-E21 attribution discipline + forbidden-vocab discipline (four controls).
- **E30** + **E32** mid-priority: framework-attribution scrub + A1 closer fix (E30) or A3 third-option risk (E32) + forbidden-vocab discipline + n-gram coherence + TML cross-reference (E32).

**Critical sequencing constraint:** Preface E01–E07, Ch 1 E08–E15, Ch 2 E16–E20, Ch 3 E21–E23, and Ch 4 E24–E27 must have landed first (they cascade the blended-we + no-inline-tag + in-prose attribution + framework-attribution scrub + A1/A2/A3/A13 + forbidden-vocab discipline to Ch 5). Per AGENT-TEAM §6 phase sequence, those are upstream beads; Ch 5 inherits the convention.

---

## Skip / needs-author rationale

### No SKIP-ALREADY-DONE rows

All five in-scope E-rows (E28, E29, E30, E31, E32) introduce new content (attribution shift + Julie-voice paragraphs + two framework introductions + one Missing-sources elaboration). None of the substance is already present in the chapter. All five LAND-WITH-MODIFICATION per acceptance criteria above.

### No NEEDS-AUTHOR rows

All five landing E-rows carry mechanical resolutions per the voice charter, framework-attribution rule, Q-E21 convention, prose-risk-map verdicts, manifest author-approval annotations, and EC1 canonical-definition verification (TML and PIS both PASS canon per detailed analysis).

**Optional author follow-up (post-dispatch, not bead-blocking):**

1. **E28 attribution pattern choice** — Pattern A (Marina + Jesse named opener, blended-we body) vs. Pattern B (Marina + I body with single anchor sentence; same for L130 chutes-and-ladders cross-reference). Drafter picks based on cadence; author can override on diff review.
2. **E29 landing pattern choice** — Pattern A (paragraph inside §5.1 between L20 and L22) vs. Pattern B (new H3 between L22 and L24). Drafter picks; **recommend Pattern A** for cadence consistency.
3. **E31 landing pattern choice** — Pattern A (new H2 between L22 and L24) vs. Pattern B (paragraph in §5.0). Drafter picks; **recommend Pattern A** because PIS is a framework deserving its own H2 visual hierarchy.
4. **E28 + E30 + E32 attribution frequency calibration** — E28 named anchor, E30 lighter, E32 implicit. Author can override if attribution frequency feels off.
5. **L130 chutes-and-ladders italicization** — Drafter preserves current phrasing (no proper-noun re-introduction) OR reintroduces *Chutes and Ladders* italicized. **Recommend preserve current**; author can override.
6. **Cross-chapter coherence flags (separate Drafter pass, not blocking E29/E31 landing in Ch 5):** Ch 2 L259 forward-reference update (point at Ch 5 not Ch 6); Ch 6b alignment via E36 separate bead (TML work-lens); Glossary E58 inherits canonical TML + PIS definitions from Ch 5.

---

## Done test status

- [x] Every in-scope E-row (E28, E29, E30, E31, E32) classified: 1 ATTRIBUTION+NEW-SECTION LAND-WITH-MODIFICATION (E28); 2 FRAMEWORK-ADD LAND-WITH-MODIFICATION (E29, E31); 2 NEW-SECTION LAND-WITH-MODIFICATION (E30, E32); 0 SKIP-ALREADY-DONE; 0 NEEDS-AUTHOR
- [x] Every LAND row has tightened current-chapter line ranges (E28: L8 opener cascade + L30 + L130 Jesse-voice + new Julie-parallel between L14 and L16; E29: paragraph inside §5.1 between L20 and L22 [Pattern A] or new H3 between L22 and L24 [Pattern B]; E30: paragraph inside §5.4 between L126 and L128; E31: new H2 between L22 and L24 [Pattern A] or paragraph in §5.0 between L22 and L24 [Pattern B]; E32: paragraph inside §5.1 between L57 and L59)
- [x] Every LAND row has 2–4+ bullet acceptance criteria covering substance preservation, anti-pattern risk, framework-attribution rule applicability, EC1 canonical-definition verification (for E29 + E31), and coherence
- [x] **MEANS/ENDS-RISK check applied per scout.md §5 on opener / closer / concept-definition paragraphs:** chapter opener (E28 scope, story-based — CLEAN, grandfathered); E28 (chapter-opener-adjacent — MED risk, flagged); E29 (TML framework introduction — LOW risk, flagged); E30 (reinforces §5.4 thesis — LOW risk, flagged); E31 (PIS framework introduction, chapter-framing-adjacent — MED risk, flagged); E32 (reinforces §5.1 Pass 3 — LOW risk, flagged); In Brief, §5.0 closer, §5.1 deliverable, §5.2 classification, §5.3 systems-talk, §5.4 People-don't-have-APIs, §5.5 transcripts, §5.6 Sprint Meridian, §5.7 knowledge management, §5.8 completeness test, §5.9 hand-off-to-Design, reflection questions — ALL clean per §5 sweep; full §5 sweep documented in Conflicts and Risks section
- [x] **EC1 CANONICAL-DEFINITION VERIFICATION applied (MANDATORY for E29 + E31):** TML Framework EC1 verdict = **PASS** (Task/Management/Leadership names match canon; AI-handling mapping handle/assist/oversight matches canon; lens difference knowledge vs. work is complementary per Ch 6b E36); PIS Framework EC1 verdict = **PASS** (Problem/Identify/Solution names match canon; Compound stage mapping P=Signal/I=Source/S=Design+Build matches canon); "Source" + "At-Risk Source" + "Missing sources" usages verified PASS against canonical definitions
- [x] **NO author decision required for canon-alignment of TML or PIS** — both frameworks' Julie source paragraphs match manifest canon; Drafter executes per acceptance criteria
- [x] **A2 traps identified around canonical vocabulary:** Knowledge Map (defined §5.1 L24; E28+E29+E31 lands BEFORE — use plain "knowledge" not capitalized "Knowledge Map"; E30+E32 lands AFTER — capitalized acceptable); TML (first-defined via E29 in Ch 5 §5.1); PIS (first-defined via E31 as new H2 between §5.0 and §5.1); Source Agent (canonical Compound Bench instrument NOT load-bearing in Ch 5 — verify Drafter does NOT re-introduce); Data Pipeline Audit (already staked §5.1 L41); At-Risk Source (defined §5.4 L126; E30 lands AFTER — acceptable); Missing sources (defined §5.1 L57; E32 lands AFTER — acceptable); HAC (Ch 6 vocabulary NOT load-bearing); full A2 sweep documented in Conflicts and Risks section
- [x] **Framework-attribution flags on E29 + E31 (CRITICAL — TWO frameworks introduced in Ch 5):** direct application both rows — E29 reframes "Julie's TML framework" → "The TML framework (Task / Management / Leadership)" joint canonical-vocabulary; E31 reframes "Julie's Problem/Identify/Solution framework" → "The Problem/Identify/Solution (PIS) framework" joint canonical-vocabulary; E28 + E30 + E32 indirect application on credentialing closures ("every... I have run" / "Julie's M&A integration practice identified" / "Julie's practice in every organizational design engagement")
- [x] **Forbidden vocab discipline flagged (recurring 3/3+ chapter pattern):** "organizational design" in E28 ("every organizational design engagement I have run") + E29 ("organizational design foundation of the knowledge mapping work") + E31 ("organizational design equivalent of prescribing before diagnosing") + E32 ("From an organizational design perspective" + "every organizational design engagement") — Drafter scanner gate MUST catch zero across all five E-rows
- [x] **Cross-chapter coherence flagged:**
  - E28 must not verbatim-echo FOUR PRIOR a global food safety company anchors (Preface L9 + Ch 1 L57 + Ch 2 §2.3 + Ch 4 L18)
  - E28 must preserve L130 chutes-and-ladders developer cross-reference (per `ahmed-story-is-chutes-and-ladders` and `pm-case-study-thread-through-book` memories)
  - E28 must preserve Marina story cross-chapter coherence with Ch 2 L8 (Marina canonical reference)
  - E29 Ch 2 L259 forward-reference update flagged (separate Drafter pass, not blocking)
  - E29 Ch 6b E36 alignment flagged (separate bead, not blocking)
  - E29 + E31 Glossary E58 inherits canonical definitions from Ch 5
  - Meridian Source-stage threading verified consistent across Ch 3 §3.4 Sprint Planning Canvas + Ch 5 §5.6 Sprint section + Ch 5 L205–L213 populated Knowledge Map
- [x] **CH-conflict flag check:** Marina opener at L8 is canonical polished replacement per `6c99346`; L130 chutes-and-ladders developer cross-reference is canonical per `ahmed-story-is-chutes-and-ladders` memory; no Bench / Skills Library product references in chapter (`48cef93` purge verified); no Greenline / Ahmed / Donna / Harley / Saint Clair regressions; no MERIDIAN restructuring (preserved verbatim)
- [x] Conflicts flagged with specific source references (manifest §57 global framework-attribution rule, charter §4 A1/A2/A3/A4/A13, charter §3 forbidden vocab + Mid-Market-Operator scoping, Q-E21, manifest E29 + E31 canonical definitions, manifest E36 TML work-lens canon, manifest E58 glossary additions, risk-map E28-E32 verdicts, stale-audit, persistent memories `ahmed-story-is-chutes-and-ladders` and `pm-case-study-thread-through-book` and `framework-attribution-rule`)
- [x] Bead execution order recommended with dependencies cited (E28 → E29 → E31 → E30 → E32)
- [x] Author follow-up items logged separately from bead-blocking decisions (E28 attribution pattern, E29 + E31 landing patterns, attribution frequency calibration, L130 italicization, cross-chapter coherence flags for separate passes)
- [x] Plan file at `_julie/per-chapter/05-source.md`

**Outstanding author asks for Human Orchestrator:**

None blocking. All five E-rows dispatch under their current verdicts. EC1 canonical-definition verification PASS for both TML and PIS — no author decision required.

**Optional author decision points (post-Drafter, before commit):**

1. E28 attribution pattern choice (A vs. B) at L8 opener + L30 + L130 — see optional follow-up #1.
2. E29 landing pattern choice (A paragraph inside §5.1 vs. B new H3) — see optional follow-up #2.
3. E31 landing pattern choice (A new H2 vs. B paragraph in §5.0) + H2 title — see optional follow-up #3.
4. E28 + E30 + E32 attribution frequency calibration — see optional follow-up #4.
5. L130 chutes-and-ladders italicization — see optional follow-up #5.
6. Cross-chapter coherence separate passes (Ch 2 L259 forward-reference update; Ch 6b E36 alignment) — see optional follow-up #6.

---

## Author decisions (logged after dispatch)

*(To be filled in as author reviews each bead diff during execution.)*

- **E28:** _pending_ (attribution-pattern choice at L8 + L30 + L130; cross-chapter n-gram avoidance verification against four prior a global food safety company anchors; framework-attribution scrub on credentialing closure)
- **E29:** _pending_ (EC1 canonical-definition verification for TML; A2 first-definition load-bearing; framework-attribution scrub; A3 stacked triplet collapse to semicolon-bridge form; forbidden-vocab scrub; landing pattern choice A vs. B; Ch 2 L259 + Ch 6b cross-chapter coherence flagged separately)
- **E30:** _pending_ (A1 AI-tell closer fix "That is what At-Risk Source does"; framework-attribution scrub on M&A integration practice individual attribution; n-gram coherence verification with L161 Dave-Meridian beat)
- **E31:** _pending_ (EC1 canonical-definition verification for PIS; A2 first-definition load-bearing; framework-attribution scrub; forbidden-vocab scrub on "organizational design equivalent"; landing pattern choice A vs. B; H2 title selection)
- **E32:** _pending_ (framework-attribution scrub on double individual attribution; forbidden-vocab scrub on "organizational design perspective" + "organizational design engagement"; A3 third-option triplet conversion risk; TML cross-reference explicit invocation post-E29 landing; A1 closer preserve verbatim)

---

## Path verdict summary

- **Verdict:** Default **Path A** (solo Drafter) for all five landing rows (E28, E29, E30, E31, E32).
- **Path B candidates if voice-gate fails twice:** E29 (seven intersecting controls — highest anti-pattern density of any Ch 5 E-row; **HIGHEST risk in entire merge for canonical-definition verification because TML triggered the Ch 2 EC1 lesson**), E31 (four controls — second-highest-risk for first-definition canonical framework introduction), E28 / E30 / E32 lower-priority Path B candidates.
- **Iteration target:** Match Ch 2 / Ch 4 outcome (3 iterations: Scout → Drafter + scanner gate → editorial-coherence + surgical pass → author 2nd/3rd read). Ch 5 inherits the workflow.

---

*End of plan.*
