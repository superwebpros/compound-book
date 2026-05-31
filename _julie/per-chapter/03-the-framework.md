# Scout Plan — `chapters/03-the-framework.qmd` (Ch 3: The Framework)

**Generated:** 2026-05-31  ·  **Bead:** book-ff63.9.4  ·  **Scout:** Sage

## Chapter context (one paragraph)

Ch 3 is the **framework chapter** — Ch 1 diagnosed (operating-model failure), Ch 2 framed the structural answer (Co-Operating Model), and Ch 3 introduces the *operational mechanism* the rest of the book teaches: the Compound Framework, its six-stage Sequence (Signal → Source → Design → Build → Deliver → Compound), the Sprint as the unit of execution, the Rhythm as the cadence, the Diagnose / Execute & Compound split, and the Sprint Planning Canvas as the one-page starting artifact (Meridian Manufacturing populates the worked example at L122–L147). The chapter is the canonical source for four coined terms — **Framework, Sequence, Sprint, Rhythm** — defined together in §3.2 at L41–L44, plus introduces the **Diagnose / Execute & Compound** grouping in §3.3 at L68–L80. The opener (L8–L16) is a discovery-call story currently in first-person-singular voice ("She's on the screen and I can tell..." / "I know exactly what she means..." / "I've also watched what happens..."), closed by the load-bearing pivot line at L16: "That is the conversation this chapter exists to prevent you from having with yourself." Section §3.1 "The order is the *argument*" begins at L18, with the existing argument running L20–L28 — the "cause is not the tool, the cause is the order" → construction metaphor (foundation/walls/roof) → "Framework exists because there is a correct sequence" → chutes-and-ladders callback to the Preface developer-departure story. **Per Q-E23 (resolved):** "Order is the Argument" is Jesse's own coined section heading (already at L18); Julie's E23 is extending, not importing. Author jf-note on Q-E23 reads: *"If I made a phrase and don't remember it, its not a good phrase. NEeds to be revised."* — this is a soft author-revisit signal but does not block E23 from landing as an extension. The most recent commits touching this chapter are `124f777` (excalidraw shortcodes wired in), `7709ea8` (author review round 2 — resolve all 33 jf-notes across 8 chapters), `e63aa07` (Ch03-specific implementation of Jesse's editorial feedback, 9 fixes), `6c99346` (cross-book coherence, Meridian threading, fabrication replacement), and `e36b426` (glossary + action steps + reflection questions). The chapter is **polished**. The In Brief callout (L3–L6) does the load-bearing terms preview; the Reflection Questions at L184–L189 close in the established pattern. Per stale-audit: no Greenline / Ahmed / Donna / Harley / Saint Clair / Marina-fabrication / nine-red-weeks regressions in Ch 3; Meridian Manufacturing threading at L122–L147 is canonical and matches the Ch 1 introduction. Per `compound-does-not-have-on-site-implementers-like` memory: the discovery-call frame at L8–L14 is fine (Compound runs discovery calls / Clarity Calls — that's not on-site implementation). Per author manifest annotation: overall *Approved* ("Can we just build it" opening + order-is-the-argument); E21 *Approved* with Q-E21 convention; E22 *Approved*; E23 *Approved* (Q-E23 resolved).

## E-row classifications

| E-row | Type | Verdict | Current-chapter target | Notes |
|---|---|---|---|---|
| E21 | ATTRIBUTION | LAND-WITH-MODIFICATION | L8 opener with cascading shifts at L10, L12, L14, L26 | Apply Q-E21 convention: blended-we + single in-prose attribution naming Jesse once; reject inline `Jesse:` tag; preserve discovery-call story and "Can we just build it" beat verbatim |
| E22 | NEW-SECTION | LAND-WITH-MODIFICATION | After L14 (end of discovery-call story), before L16 (the "conversation this chapter exists to prevent" pivot line) | Julie's "20 years of ERP/restructuring/acquisition failures" response paragraph; HEAVY REWRITE per risk map; **framework-attribution rule applies** — strip "I have had a version" individual framing → joint "we have watched"; **A3 triplet acute** (ERP / restructurings / acquisitions enumeration); **MEANS/ENDS-RISK** — lead with operator outcome (twelve months in, built the wrong thing at great expense), name diagnosis as the means; **single in-prose attribution** signaling Julie's CHRO/org-design experience |
| E23 | NEW-SECTION | LAND-WITH-MODIFICATION | After L20 (the "cause is the order" hammer line), before L22 (the construction metaphor paragraph) inside §3.1 "The order is the *argument*" | Julie's "thirty-year-old org-design principle / diagnose before prescribe" extension; HEAVY REWRITE per risk map; **A3 triplet acute** ("Diagnose before you prescribe. Understand the system before you change it. Map the work before you redesign it." — three-clause triplet, risk-map explicit cut); **framework-attribution rule applies** — strip "Julie has applied... Jesse discovered..." paired personal-attribution; reframe as joint book IP extending the existing §3.1 argument; **Q-E23 author-revisit signal**: heading phrase itself may be revised post-merge (jf-note line 54) — flagged as optional author follow-up, does NOT block landing E23 substance |

**Counts:** 2 NEW-SECTION LAND-WITH-MODIFICATION (E22, E23) · 1 ATTRIBUTION LAND-WITH-MODIFICATION (E21) · 0 LAND-clean · 0 SKIP-ALREADY-DONE · 0 NEEDS-AUTHOR (the Q-E23 heading-revisit is a *soft* author follow-up logged below, not a blocker)

**Path verdict:** Default **Path A** (solo Drafter) per AGENT-TEAM §1 lessons-learned default and Ch 2 outcome (Path A produced clean Ch 2 in 3 iterations). E22 and E23 are the strongest Path B candidates if any bead in this chapter fails voice-gate twice:

- **E22** because it lands the chapter's first Julie-voice paragraph against the load-bearing L16 pivot ("the conversation this chapter exists to prevent"). Framework-attribution scrub + A3 triplet collapse + MEANS/ENDS-RISK + single-in-prose attribution stack four anti-pattern controls in one paragraph.
- **E23** because A3 triplet is acute (three-clause "diagnose / understand / map" is the entire substance), framework-attribution is explicit in Julie's source ("Julie has applied this principle... Jesse discovered it...") — three intersecting anti-patterns in a paragraph that lands inside Jesse's existing argument at §3.1.

Recommend single solo Drafter pass for all three rows in the recommended bead order below; escalate to Path B only on second voice-gate fail.

---

## Per-E-row acceptance criteria

### E21 (ATTRIBUTION, LAND-WITH-MODIFICATION) — opener blended-we + in-prose attribution

**Substance to preserve (current chapter L8–L16):**

- The full discovery-call story: a prospective client on a video call, twenty-minute conversation about her company / bottlenecks / what she hopes AI can fix, then leans forward and says "Can we just build it? I just need this thing built." Preserve verbatim — this is the chapter's load-bearing opening hook (per manifest E21 row and author overall *Approved* note: "*'Can we just build it' opening*").
- The "she's seen demos, she's read the case studies" beat at L10 — preserve.
- The "When you know what you want, you build it" closer at L10 — preserve.
- The "But I've also watched what happens" paragraph at L12 — preserve substance verbatim; this paragraph captures the build-first failure mode and is what E22 then deepens.
- The "I didn't tell her that on the call. I said: let's start at Signal" beat at L14 — preserve verbatim. This is the Sequence's first appearance in the chapter, hooks forward to Ch 4.
- The L14 closer: "If we'd built what she came in asking for, we'd have solved the wrong problem and charged a lot to do it." — preserve.
- The L16 pivot line: "That is the conversation this chapter exists to prevent you from having with yourself." — preserve verbatim. This is the chapter-thesis hammer that E22 lands directly before.
- The L26 chutes-and-ladders callback to the Preface developer-departure story — preserve substance; voice shift only (see Modification below).

**Modification from Julie's instruction:**

- Julie's redline (line 631) inserts a literal `Jesse:` underline tag at the top of the section. **Reject per Q-E21:** inline author tags are not the book's convention (per author-questions-answered finding on co-authored business books); blended-we + in-prose attribution is the convention; the Preface + Ch 1 + Ch 2 have all modeled this and Ch 3 inherits.
- **Land the attribution differently:** the current opener is in first-person-singular throughout L8–L14 and at L26 ("the chutes-and-ladders problem I described at the start of this book"). Two acceptable patterns:
  - **Pattern A (preferred, parallels Ch 2 E16):** Insert a single in-prose attribution at L8 — e.g., open with "Jesse was on a discovery call. She's on the screen and he can tell from the way she's sitting that she's already made up her mind. We've been talking for maybe twenty minutes..." Then sustain blended-we / third-person across L10, L12, L14. The single Jesse-named opener satisfies the dual-author signaling; the body inherits the chapter's blended-we voice. At L26, the chutes-and-ladders callback shifts to "the chutes-and-ladders problem we described at the start of this book" — joint framing because the Preface establishes both authors' arc.
  - **Pattern B (alternative):** Keep singular-I at L8–L14 (the discovery-call story is Jesse-specific) but add one in-prose attribution sentence — e.g., before the story opens: "Jesse was on a discovery call..." then the existing prose follows as-is. This is closer to the existing Ch 1 §1.0 voice ("We were on a discovery call...") and may preserve more cadence. L26 still shifts to blended-we (callback to Preface, joint).
- **Drafter picks based on which preserves the discovery-call cadence best.** Author can override on diff review. The Ch 2 E16 execution used Pattern A; recommend Drafter try Pattern A first for cross-chapter consistency, fall back to Pattern B if cadence breaks.
- **L26 specifically (chutes-and-ladders callback):** the "I described at the start of this book" sentence is currently first-person-singular and refers to the Preface (where Jesse's developer-departure story lives). **Shift to "we described at the start of this book"** — the Preface itself uses blended-we to narrate the chutes-and-ladders story (index.qmd L5: "Jesse was in his office when a developer who had been with him for years put in his notice. Sitting there, he realized..."). The Preface attributes the story to Jesse via in-prose attribution and then narrates in third-person/blended-we; Ch 3 inherits the same convention. The L26 closer ("the only reason what came next worked is because I solved the problem in a specific order") shifts to "the only reason what came next worked is because the problem got solved in a specific order" or "...because Jesse solved the problem in a specific order" — second is preferred (cleaner narrative, light in-prose attribution).
- **Contractions:** the existing prose uses contractions throughout ("She's", "we've", "she's", "I've", "didn't", "we'd"). Julie's source (L619–L638) does NOT use contractions ("She is", "We have been", "she has", "I have", "did not", "we would"). The current chapter is already correct per voice charter §2 "Contractions: always." **Preserve current chapter contractions; do not regress to Julie's source phrasing.**

**Anti-pattern risk:**

- **A4 (boastful biographical):** Low risk. The discovery-call story is a concrete operating example, not credentialing.
- **A3 (triplet pileup):** Low-to-moderate risk in the existing prose. L10 has "She's seen demos. She's read the case studies. She has a clear picture..." — three short parallel sentences. This is a hammered cadence that earns its space (it cashes out the operator instinct the story is naming). **Grandfathered** — do NOT modify during E21 attribution-shift; the cadence is load-bearing for the story's hook. Drafter must not introduce *new* parallel constructions during the I→we conversion.
- **A5 (general AI smell):** Low risk; the opener already lands operator-direct. Watch the in-prose attribution sentence — keep terse, no padding ("on a discovery call" not "during what would turn out to be a pivotal discovery call").
- **A13 (means/ends):** Indirect risk. L16 "the conversation this chapter exists to prevent you from having with yourself" is *what the chapter prevents the reader from doing wrong*, framed as the chapter's purpose. This is structural framing (chapter-as-conversation-substitute), not system-as-destination. **Grandfathered chapter prose**, not in scope for E21 modification. Flag for awareness; do NOT modify.
- **A14 (metaphor literalism):** L22 "framing a house before pouring the foundation. The walls go up. The roof goes on." is the construction metaphor that E23 lands directly after. Construction metaphor literally applies (the building has structural order; so does the framework). No violation. **Grandfathered.**
- **A16 (book-as-location):** L24 "Run all six in order and you are changing how the work is owned" is fine — no "leave with" / "walk away from" language. Clean.

**Framework-attribution rule:** N/A for E21 (attribution-only voice shift; no framework is being introduced or credited individually here).

**Coherence:**

- E21 must land **first** in the chapter's execution order. It sets the voice E22 and E23 write into.
- The Preface E01/E02 + Ch 1 E08–E11 + Ch 2 E16 have already established blended-we + in-prose attribution as the convention. E21 inherits; does not invent.
- The L26 chutes-and-ladders callback must remain a recognizable reference back to the Preface. Voice shift must not break the recognition — "the chutes-and-ladders problem" phrase preserved verbatim (it's the canonical name per persistent memory `ahmed-story-is-chutes-and-ladders`).
- After E21 + E22 + E23 land, the L8 → L14 → L16 → §3.1 → L20 → L22 → L24 → L26 flow must read: discovery-call story (blended-we w/ Jesse attribution) → "let's start at Signal" pivot → "this chapter exists to prevent that conversation" → E22 (joint Julie-lens response framing the build-first failure pattern as 20-year-old org-design diagnosis) → §3.1 heading → "cause is the order" hammer → E23 (joint extension naming diagnose-before-prescribe as the principle) → construction metaphor → "Framework exists because there is a correct sequence" → "this book was born from the chutes-and-ladders problem we described in the Preface." Single forward motion.

---

### E22 (NEW-SECTION, LAND-WITH-MODIFICATION) — Julie's "20 years of failed initiatives" response paragraph

**Substance to preserve (from `_julie/julie-redline.md:640–658`):**

- The substantive insight: the instinct to move to solution before diagnosis is not unique to AI. It is the most common and most expensive mistake in organizational change.
- The 20-year pattern: every major implementation failure that gets called in for salvage had the same root cause — solution built before problem was understood.
- The diagnosis-as-invisible-work observation: the diagnosis gets skipped because it feels slow, abstract, and like something that doesn't produce visible output. So everyone moves to what feels like progress — which is building.
- The operator math: twelve months later, they discovered they'd built the wrong thing at great expense. **This is the load-bearing operator beat** — preserve as the closing operator-math line.
- The hook to Signal: "Signal exists to prevent that. It is the discipline of refusing to build until the problem has been precisely named and its cost has been quantified." The "precisely named and its cost has been quantified" phrase is the canonical articulation of Signal's deliverable per Ch 4 §4.1 and lands here as a forward reference.

**Modification from Julie's instruction:**

- **Framework-attribution rule — DIRECT APPLICATION:** Julie's source opens "I have had a version of this conversation in every major organizational initiative I have ever led." This is **individual attribution of joint book IP** (the diagnosis-before-build principle is the central argument of the entire chapter and the entire framework — not Julie's individual practice). Per manifest line 57 (global rule) and `framework-attribution-rule` persistent memory, reject the individual-Julie framing. **Reframe as joint blended-we:** "We've watched a version of this conversation in every major organizational initiative either of us has led." The "either of us" is the cleanest joint construction; alternatives: "We've watched this pattern across two decades..." (echoes Ch 1 L21 "We've watched this same pattern for two decades..." — verify no redundancy with that exact line).
- **A3 triplet acute:** Julie's source lists "ERP systems nobody used, restructurings that broke the company they were supposed to fix, acquisitions that destroyed more value than they created" — three-clause enumeration. Per voice charter §4 A3 and risk-map line 110 ("Cut the failure-pattern hedge-list. Lead with one specific company."). **Resolution:** Collapse to ONE specific example, plus a brief generalization. Acceptable patterns:
  - **Pattern A:** Lead with the ERP example (operator-recognizable, most concrete): "An ERP rollout that nobody used. A restructuring that broke the company it was supposed to fix. An acquisition that destroyed more value than it created. Different industries, same root cause." This **preserves the triplet but reframes as observational pattern** rather than constructed parallel — the three are operator-recognizable failure modes, not rhetorical decoration. Marginally acceptable IF the closer ("Different industries, same root cause") earns the cadence. **High-risk; verify with Drafter.**
  - **Pattern B (safer, per risk-map):** Pick ONE concrete failure-mode and generalize. "An ERP rollout that nobody used. The pattern repeated across restructurings, acquisitions, integrations — same root cause." This collapses the three-clause cadence into a single concrete example + a generalizing list (which is a different rhetorical move and avoids the A3 triplet trap).
  - **Pattern C (safest):** Strip the enumeration entirely. "Every major implementation failure I've been called in to salvage had the same root cause." Reframe loses the operator-recognizable specificity but is cleanest. **Recommend Drafter try Pattern B first; fall back to Pattern C if voice-gate flags A3.**
- **A5 (closer):** Julie's source closes "Signal exists to prevent that. It is the discipline of refusing to build until the problem has been precisely named and its cost has been quantified." The cadence is operator-direct; "precisely named and its cost has been quantified" is the canonical Signal deliverable phrase. **Preserve verbatim.** This earns the closer position.
- **MEANS/ENDS-RISK (direct application per scout.md §5):** This paragraph lands directly before L16 (the chapter-thesis pivot). The risk is closing on "Signal as the discipline" (means) rather than the operator outcome (the wrong thing built at great expense — what Signal prevents). **Acceptance criterion:** the paragraph must lead with the operator outcome (twelve months later, built the wrong thing at great expense) and name Signal as the means to avoid it. The current Julie-source structure already does this — preserve the order: 20-year pattern observation → why diagnosis gets skipped → operator math (12 months, wrong thing, great expense) → Signal as the discipline that prevents it. Verify the Drafter does not invert.
- **A2 (coined term before stakes):** "Signal" is defined later in the chapter (§3.3 at L57) and gets a full chapter at Ch 4. Mentioning it here as a forward reference is fine — it's the chapter introducing the Sequence; the term is mid-staking. Pattern at L14 already does this ("I said: let's start at Signal"). E22 forward-reference is consistent.
- **A4 (boastful biographical):** Moderate risk. Julie's source frames this as "every major organizational initiative I have ever led" and "every major implementation failure I have been called in to salvage." The 20-year credentialing is **already established in the Preface** (index.qmd L9: "In 2022, Julie was Global CHRO at a global food safety company..." + L21 "Over twenty years of leading people functions, she's seen this same pattern in nearly every company she's worked in"). Ch 3 inherits the credentialing. **Reframe the personal phrasing as joint observational:** "We've watched the same pattern across two decades of organizational work — Julie inside enterprise transformations [redacted — see below], Jesse inside operating companies" is one option, but **risks redundancy with Ch 1 L21**. Safer: a single in-prose attribution phrase ("This is the pattern Julie has watched across two decades of org-design work — same root cause every time...") then sustain blended-we for the rest of the paragraph. **Drafter picks the cadence-cleanest landing.**
- **Forbidden vocab:** Julie's source uses "organizational change" (acceptable, plain operator language). **Watch for "transformation" / "transformative" / "transform" — per lessons-learned, recurring 3/3 chapters from Julie's source.** Also "leverage" (forbidden corporate filler). Verify zero before Drafter completes. Use "implementation" / "restructure" / "redesign" / "integration" — all plain operator language. Charter §3 allowed.
- **In-prose attribution (per Q-E21):** This paragraph is the **first place in Ch 3 where Julie's voice meaningfully enters**. Land it in blended-we with one in-prose attribution sentence that signals Julie's CHRO/org-design experience as the diagnostic lens. Single attribution; no inline `Julie:` tag from Julie's redline (line 640).

**Anti-pattern risk (highest):**

- **A3 (triplet/enumeration)** — three-clause ERP/restructuring/acquisition list. **Auto-reject as constructed parallel.** Pattern B or Pattern C above; verify Drafter resolution.
- **A4 (boastful biographical)** — "every major organizational initiative" credentialing. Mitigated by Preface setup; single in-prose attribution; do not dwell on scope.
- **A5 (general AI smell)** — Julie's source has some hedging cadence ("it felt slow, abstract, and like something that did not produce visible output. So everyone moved to what felt like progress, which was building"). The "felt slow / felt like progress" antithesis is **acceptable single instance** per charter §4 if it lands the diagnostic-as-invisible-work observation. Drafter to verify cadence is operator-weighted, not philosophical-hedged.
- **A13 (means/ends)** — direct application per §5 special check; closer must land operator outcome (wrong thing built at expense) and name Signal as the means.
- **Framework-attribution** — direct application; "I have had a version" individual framing **must be reframed** as joint blended-we. Diagnosis-before-build is joint book IP, not Julie's individual instrument.
- **Forbidden vocab leakage** — "transformation" family (3/3 chapter pattern per lessons-learned). Drafter scanner gate must verify zero.

**Framework-attribution rule:** **Applies directly.** Diagnosis-before-build is joint book IP — the entire central argument of Ch 3 (and the book). Strip "I have had" individual framing. The paragraph lands as joint observation extended by Julie's lens, not as Julie's individual diagnostic discovery.

**Coherence:**

- Lands AFTER L14 (end of discovery-call story / "let's start at Signal" pivot) and BEFORE L16 (the chapter-thesis pivot line "That is the conversation this chapter exists to prevent you from having with yourself").
- Must read as a **deepening of the discovery-call story** — the story names a single instance ("Can we just build it"); E22 universalizes the pattern across 20 years and multiple failure modes; L16 then closes both at the chapter-thesis level.
- The L16 pivot line is **load-bearing as the chapter-thesis hammer**. E22 must NOT replace or duplicate L16's framing. Specifically: do not close E22 on "this chapter exists to prevent that" — that's L16's job. Close E22 on "Signal exists to prevent that" — the *stage* level, leaving the *chapter* level for L16.
- E22 must NOT introduce any of the four canonical terms (Framework, Sequence, Sprint, Rhythm) — they are defined in §3.2 at L41–L44. Forward reference to "Signal" is fine (it appears at L14 already).
- E22 must NOT introduce "Diagnose / Execute & Compound" grouping — that is §3.4 at L68. Forward reference to "diagnosis" as a general concept is fine and is the substance of the paragraph.
- Verify no n-gram repetition with Ch 1 L21 ("We've watched this same pattern for two decades..."). E22's "20 years" + "watched" + "pattern" risks cross-chapter phrase repetition (per Ch 2 lessons-learned: cross-paragraph n-gram repetition is a recurring pattern). **Suggested wording differentiation:** Ch 1 says "We've watched this same pattern for two decades, long before AI entered the conversation." Ch 3 should NOT echo that exact construction. Acceptable alternative phrasings: "Every major implementation failure we've been called in to salvage..." or "The pattern shows up across two decades of organizational work..." The phrasing must not duplicate Ch 1 L21.

---

### E23 (NEW-SECTION, LAND-WITH-MODIFICATION) — Julie's "diagnose before prescribe" thirty-year-old principle extension

**Substance to preserve (from `_julie/julie-redline.md:668–678`):**

- The substantive claim: the diagnose-before-build principle is not new and is not a technology insight. It's an organizational design principle that's at least thirty years old.
- The three articulations of the principle: "Diagnose before you prescribe. Understand the system before you change it. Map the work before you redesign it." (**TRIPLET — must collapse; see modification below.**)
- The joint framing: this principle has been applied across both authors' work in different contexts. Julie in org-design engagements; Jesse in his own company's first sprint discovering the constraint he thought he was solving was a symptom of a different constraint two steps upstream.
- The hammer claim: the order is not a preference. The order is the reason it works.
- **Critical:** this paragraph **extends Jesse's existing §3.1 argument** (L20–L28: "cause is the order" → construction metaphor → "Framework exists because there is a correct sequence" → chutes-and-ladders Preface callback → "That is the argument. Now the vocabulary."). Julie's paragraph anchors the argument as a thirty-year-old organizational-design principle, not a Compound invention.

**Modification from Julie's instruction:**

- **Per Q-E23 (resolved):** "Order is the Argument" is Jesse's **existing coined section heading** at L18 (and "That is the argument" closer at L28). Julie is **extending the argument** (anchoring it to org-design tradition), not introducing the phrase. Verify the L18 heading stays as-is; verify the §3.1 argument at L20–L28 stays intact. E23 lands as a paragraph **inside** §3.1, between the "cause is the order" hammer (L20) and the construction metaphor (L22) — making the section explicitly *say* "this principle is thirty years old in org design" before the construction metaphor cashes it out.
- **Author jf-note on Q-E23 (soft signal, logged as follow-up):** *"If I made a phrase and don't remember it, its not a good phrase. NEeds to be revised."* This is the author's optional signal to revisit the **section heading phrase** itself. Per scout role definition, this is a substance/framing decision for the author, NOT a scout decision. **Resolution for this scout pass:** treat the heading as STABLE per Q-E23 approval; E23 lands the extension paragraph as-is. **Log the heading-revisit as an optional author follow-up** in the conflicts section below. Do NOT make the heading revision a blocker on E23 landing.
- **A3 triplet — ACUTE, AUTO-REJECT:** Julie's source contains the canonical three-clause triplet: "**Diagnose before you prescribe. Understand the system before you change it. Map the work before you redesign it.**" Per risk-map line 111 ("'Diagnose before prescribe / Understand the system before you change it / Map the work before you redesign it' — three-clause triplet... cut the triplet") and voice charter §4 A3. **Resolution:** Collapse to ONE articulation. The strongest single articulation is **"Diagnose before you prescribe"** — it is the canonical org-design principle name, semantically loaded, and the cleanest operator translation. The other two ("Understand the system before you change it" and "Map the work before you redesign it") are **paraphrases** of the same idea; cutting them tightens the cadence and avoids the triplet. **Drafter to keep "Diagnose before you prescribe" only; cut the two paraphrases.**
- **Framework-attribution rule — DIRECT APPLICATION:** Julie's source has explicit paired personal-attribution: "**Julie has applied this principle in every organizational design engagement she has led. Jesse discovered it when he ran his own company's first sprint and found that the constraint he thought he was solving was a symptom of a different constraint two steps upstream.**" Per manifest line 57 (global rule) and `framework-attribution-rule` persistent memory. **The paired Julie/Jesse attribution is itself a constructed parallel** (Julie did X / Jesse did Y) — both an A3 risk AND a framework-attribution risk. **Resolution:** Reframe as joint book IP with a single in-prose attribution. Acceptable patterns:
  - **Pattern A:** Strip the paired attribution entirely. "It's an organizational design principle that's at least thirty years old: diagnose before you prescribe. We have applied it across both our work — Julie inside organizational redesigns, Jesse inside operating companies." This collapses to single sentence + single attribution + joint framing.
  - **Pattern B (preferred):** Use a single biographical anchor (Julie's org-design context, since that's where the thirty-year principle lives) + a single Jesse-anchor that ties to the chutes-and-ladders callback already at L26. "It's an organizational design principle Julie has watched anchor every major engagement she's led: diagnose before you prescribe. Jesse hit the same principle inside his own company's first sprint — the constraint he thought he was solving was a symptom of a different constraint two steps upstream." This is closer to Julie's substance but reframes "applied" → "watched anchor" (avoids framework-IP language) and ties Jesse's discovery to a single concrete instance (his first sprint) rather than abstracting "the principle." **Drafter to prefer Pattern B if cadence allows; fall back to Pattern A if voice-gate flags A3 on the paired attribution.**
  - **Pattern C (safest, framework-attribution-clean):** Strip both personal attributions. "It's an organizational design principle that's at least thirty years old: diagnose before you prescribe. Same instinct in software ("don't refactor until you've traced the bug to its actual cause"). Same instinct in medicine. Same instinct in this book." This is the cleanest joint framing but **loses the operator-recognizable cross-context anchor** (Julie's org-design / Jesse's first sprint). **Not recommended unless Pattern A and B both fail.**
- **A1 risk (abstract-noun-equals-abstract-noun):** Julie's source has the closer "The order is not a preference. The order is the reason it works." This is **A1-adjacent** ("X is not A. X is B" — antithesis) — acceptable single instance per charter §4 IF no other antithesis closer in §3.1. Verify: §3.1 currently has "That is the argument. Now the vocabulary." (L28) as the section closer — declarative, not antithesis. E23's "The order is not a preference. The order is the reason it works." would land **before** the construction metaphor (L22). The construction metaphor closes with "Construction has rules about the order of operations because the order is load-bearing. So does this." — declarative, not antithesis. E23's antithesis closer is the only antithesis in §3.1. **Acceptable.** Preserve.
- **MEANS/ENDS-RISK (direct application per scout.md §5):** This paragraph lands inside §3.1 (the chapter's framework-section that argues *the order is load-bearing*). The risk is closing on "the order" as the destination (means-as-end) rather than the operator outcome. **Acceptance criterion:** E23 must lead with the principle's operator value (preventing the wrong-thing-built-at-expense pattern E22 just named) and name the order as the means. The current Julie-source closer ("The order is the reason it works") is **system-as-destination cadence** — system *works* is not the operator outcome. **Reframe the closer.** Acceptable resolutions:
  - "The order is not a preference. The order is the reason the work compounds." (ties to the canonical Equation *Co-Intelligence + Rhythm = Compound* — compounding is the operator outcome).
  - "The order is not a preference. The order is the reason the result is operational and not theatrical." (operator-direct).
  - "The order is not a preference. The order is the reason what gets built actually ships, gets used, and produces a number." (most concrete; ties to Ch 4–8 deliverables).
  - **Drafter to prefer the first option** ("the reason the work compounds") for vocabulary-consistency with the canonical Equation closer at L171.
- **A2 (coined term before stakes):** Do NOT name Framework / Sequence / Sprint / Rhythm / Compound Bench / Skills Library / HAC / TML / Compound Sprint in E23. The four core terms are defined in §3.2 at L41–L44; Compound Sprint is the unit defined at L43; HAC is downstream Ch 6; TML is downstream Ch 6b. "the order" / "the principle" / "the work" — plain operator language for E23.
- **A4 (boastful biographical):** Low-moderate risk. The "thirty-year-old principle" framing is **non-credentialing** (it's the field's principle, not Julie's discovery). The paired Julie/Jesse attribution in Julie's source IS credentialing-adjacent ("Julie has applied... Jesse discovered..."). The framework-attribution scrub above mitigates by reframing to joint application/observation. Single in-prose attribution per author maximum.
- **Forbidden vocab:** Watch for "transformation" / "transformative" / "leverage" / "alignment" / "synergy." Julie's source paragraph does not appear to use any of these directly. Use plain operator language: "redesign" / "implementation" / "organizational design" (allowed in narrow technical context per charter §3 — but **NEVER in headings**; E23's body can use the term sparingly to reference the field).
- **In-prose attribution:** Single attribution per author maximum. The L26 chutes-and-ladders callback (in E21 scope) is the second Jesse-anchor in the chapter; E23 should not repeat the Jesse-anchor heavily. The Julie-anchor in E22 is the first Julie-voice paragraph; E23's Julie-anchor should be **lighter** to avoid over-attribution (per Ch 1 + Ch 2 pattern, one attribution per coined-term-introducing section is the calibrated frequency).

**Anti-pattern risk (highest):**

- **A3 (triplet)** — three-clause "diagnose / understand / map" enumeration AND paired Julie/Jesse attribution parallel. **Auto-reject both.** Collapse the principle to single articulation; reframe the paired attribution to joint with single in-prose anchor per author.
- **Framework-attribution** — direct application; "Julie has applied... Jesse discovered..." paired personal-attribution must be reframed as joint book IP.
- **A13 (means/ends)** — closer "the order is the reason it works" is system-as-destination cadence. Reframe to operator outcome.
- **A1 (abstract-noun-equals-abstract-noun)** — antithesis closer "X is not A. X is B" is acceptable single instance in §3.1; verify no second instance.
- **A2 (coined vocab discipline)** — no Framework / Sequence / Sprint / Rhythm / HAC / TML / Compound Sprint capitalized as load-bearing carriers; "the order" / "the principle" plain.
- **A4 (boastful biographical)** — credentialing-adjacent paired attribution. Mitigated by framework-attribution scrub.

**Framework-attribution rule:** **Applies directly.** The diagnose-before-prescribe principle is org-design canon (thirty years old per Julie's source) — neither Julie nor Jesse invented it. Strip the paired "Julie has applied... Jesse discovered..." attribution. Reframe as joint book IP extending the field's principle. Single in-prose attribution per author maximum.

**Coherence:**

- Lands AFTER L20 (the "cause is the order" hammer) and BEFORE L22 (the construction metaphor "framing a house before pouring the foundation").
- Must read as a **substance anchor** for the §3.1 argument — the cause is the order *because* this is a thirty-year-old org-design principle, *and* the construction metaphor (L22) is one way to see it, *and* the chutes-and-ladders callback (L26) is another.
- E23 must NOT pre-empt or duplicate the construction metaphor at L22. Specifically: do NOT use a "build before X" / "construct before Y" cadence in E23 — that's L22's territory. Use the org-design verbs (diagnose, prescribe).
- E23 must NOT pre-empt the chutes-and-ladders callback at L26 ("the framework you are about to learn was born from the chutes-and-ladders problem we described at the start of this book"). Julie's source paragraph references "Jesse discovered it when he ran his own company's first sprint and found that the constraint he thought he was solving was a symptom of a different constraint two steps upstream." That phrasing is **a different Jesse anchor** (first sprint, not chutes-and-ladders / developer-departure). The two anchors do not duplicate; preserve E23's first-sprint anchor if Pattern B is used.
- After E23 lands, the L20 → E23 → L22 → L24 → L26 → L28 flow must read: "cause is the order" hammer → "this is a thirty-year-old org-design principle, applied across both our work" (E23) → construction metaphor → "Framework exists because there is a correct sequence" → chutes-and-ladders Preface callback → "That is the argument. Now the vocabulary." Single forward motion; E23 anchors the argument substantively, then the construction metaphor cashes it out as image, then the chutes-and-ladders story cashes it out as concrete operator history.
- **E23 must NOT introduce the four canonical terms (Framework / Sequence / Sprint / Rhythm).** They are defined at L41–L44 in §3.2. Pre-empting in §3.1 would A2-trap. Use plain phrasing: "the order" / "the principle" / "the work compounds" (the last echoes the canonical Equation closer but does not name "Rhythm" or "Compound" as terms).

---

## Conflicts and risks

### Conflict 1: E21 inline-tag Q-E21 rejection (mechanical)

**Source:** `_julie/julie-redline.md:631` (Julie's literal `Jesse:` inline tag) vs. `_julie/author-questions-answered.md` Q-E21 finding + author APPROVED jf-note.

**Description:** Julie's redline applies the inline-tag convention; Q-E21 research established the book uses blended-we with in-prose attribution per the *BE 2.0* / *Trillion Dollar Coach* model. Preface E01/E02, Ch 1 E08–E11, and Ch 2 E16 have all modeled this convention.

**Resolution:** Reject inline tag. Apply in-prose attribution per E21 acceptance criteria above (Pattern A preferred, Pattern B fallback). No author decision needed; convention is canon.

### Conflict 2: E22 framework-attribution rule applies directly to "I have had a version" individual framing

**Source:** `_julie/edit-manifest.md:57` (global rule) + `framework-attribution-rule` persistent memory + manifest E22 row.

**Description:** Julie's source opens "I have had a version of this conversation in every major organizational initiative I have ever led" — attributing the diagnosis-before-build pattern observation to Julie's individual practice. The pattern is joint book IP and the central argument of the chapter.

**Resolution:** Reframe to joint blended-we with single in-prose attribution. No author decision needed; framework-attribution is canon.

### Conflict 3: E22 A3 triplet — ERP / restructurings / acquisitions enumeration

**Source:** `_julie/julie-redline.md:646–650` + `_julie/julie-prose-risk-map.md:110` ("Cut the failure-pattern hedge-list. Lead with one specific company.") + voice charter §4 A3.

**Description:** Julie's source lists three failure modes (ERP / restructurings / acquisitions) as a parallel-clause enumeration. Risk map flags as auto-cut.

**Resolution:** Collapse per E22 acceptance criteria above. Pattern B preferred (one example + generalizing list); Pattern C fallback (strip enumeration entirely).

### Conflict 4: E22 cross-chapter n-gram repetition risk with Ch 1 L21

**Source:** `chapters/01-diagnosis.qmd:21` ("We've watched this same pattern for two decades, long before AI entered the conversation.") vs. E22's "20 years of organizational work" framing.

**Description:** Both paragraphs make the same temporal-pattern observation ("we've watched / for two decades"). Cross-paragraph phrase repetition is a recurring pattern per Ch 1 + Ch 2 lessons-learned. Verbatim or near-verbatim echo would trigger n-gram flag.

**Resolution:** Drafter to use differentiated phrasing for E22. Acceptable: "Every major implementation failure we've been called in to salvage..." or "The pattern shows up across two decades of organizational work..." — explicitly avoid "we've watched this same pattern for two decades" verbatim from Ch 1.

### Conflict 5: E23 A3 triplet — three-clause "diagnose / understand / map" enumeration AND paired Julie/Jesse attribution

**Source:** `_julie/julie-redline.md:669–671` (three-clause triplet) + `_julie/julie-redline.md:671–675` (paired Julie/Jesse attribution as constructed parallel) + `_julie/julie-prose-risk-map.md:111` ("cut the triplet") + voice charter §4 A3.

**Description:** Julie's source has TWO A3 constructions in one paragraph: the three-clause principle enumeration AND the paired authorial attribution parallel. Combined with the framework-attribution scrub on the paired Julie/Jesse line, this paragraph has the highest anti-pattern density of any E-row in Ch 3.

**Resolution:** Collapse principle to "Diagnose before you prescribe" only (cut the two paraphrases). Reframe paired attribution to joint with single in-prose anchor per author (Pattern B preferred per E23 acceptance criteria). No author decision needed; both fixes are canon.

### Conflict 6: E23 MEANS/ENDS-RISK on closer cadence

**Source:** Voice charter §4 A13 + scout.md §5 special check + chapter structure (§3.1 is the framework-argument section).

**Description:** Julie's source closes "The order is the reason it works" — system-as-destination cadence (the order *works*, framing the system as the destination). §3.1 is the chapter's framework-argument section; this is the §5 special check's textbook trigger.

**Resolution:** Reframe closer per E23 acceptance criteria — prefer "The order is the reason the work compounds" (vocabulary-consistent with the canonical Equation *Co-Intelligence + Rhythm = Compound* at L171). Drafter to verify no other system-as-destination cadence in E23.

### Conflict 7: E23 author jf-note signal on section heading "Order is the Argument" (Q-E23)

**Source:** `_julie/author-questions-answered.md:54` jf-note: *"If I made a phrase and don't remember it, its not a good phrase. NEeds to be revised."*

**Description:** Q-E23 was researched and APPROVED — "Order is the Argument" is Jesse's own existing coined section heading at L18 of the current chapter (and "That is the argument" closer at L28). The author's jf-note on Q-E23 is a *soft signal* that the **section heading phrase itself** may want revision — not a blocker on E23 substance landing, but an explicit author follow-up.

**Resolution:** **Treat heading as STABLE for this scout pass.** E23 lands the extension paragraph between L20 and L22 as currently planned. The heading revision is a separate decision that can be made post-E23-landing without re-running the merge. **Log as optional author follow-up** in the asks list below. No bead is created for the heading revision; it is author-driven.

### Conflict 8: E23 framework-attribution + paired Julie/Jesse personal-discovery framing

**Source:** `_julie/edit-manifest.md:57` (global rule) + `framework-attribution-rule` persistent memory + manifest E23 row.

**Description:** Julie's source attributes the diagnose-before-prescribe principle to both authors individually ("Julie has applied this principle in every organizational design engagement she has led. Jesse discovered it when he ran his own company's first sprint..."). The principle is org-design canon (thirty years old), not either author's individual discovery. The paired attribution itself is also an A3 constructed parallel.

**Resolution:** Strip "applied... in every engagement" and "discovered it when..." individual-discovery framing. Reframe to joint application/observation of a field-canon principle. Single in-prose attribution per author maximum. Per E23 acceptance criteria Pattern B (preferred).

### Conflict 9: A2 coined-term discipline across E22 + E23

**Source:** Voice charter §4 A2 + chapter structure (Framework / Sequence / Sprint / Rhythm defined in §3.2 at L41–L44).

**Description:** E22 and E23 both land in §3.0–§3.1 (before §3.2 defines the four core terms). Any premature use of Framework / Sequence / Sprint / Rhythm as **load-bearing carriers** in E22 or E23 would A2-trap. The chapter's order of operations is: opening story → 20-year pattern (E22) → §3.1 order argument → E23 extension → construction metaphor → "Framework exists because there is a correct sequence" (L24, first capitalized "Framework" appearance) → chutes-and-ladders callback → "That is the argument. Now the vocabulary." (L28) → §3.2 four-term definitions.

**Resolution:** E22 may forward-reference "Signal" (already named at L14) as a stage; do not introduce "Sequence" or "Framework" as terms. E23 must use plain language ("the order" / "the principle" / "the work") — no capitalized "Sequence" / "Framework" / "Sprint" / "Rhythm." The first capitalized "Framework" in the chapter is at L24 (`The Framework exists because...`); E23 lands at L20–L22, BEFORE L24. Verify Drafter does not pre-empt.

### Conflict 10: Cross-chapter coherence with Preface chutes-and-ladders callback at L26

**Source:** Current chapter L26 ("The framework you are about to learn was born from the chutes-and-ladders problem I described at the start of this book.") + `index.qmd:5` (Preface developer-departure story) + persistent memory `ahmed-story-is-chutes-and-ladders`.

**Description:** L26 is the canonical chutes-and-ladders Preface callback. E21 must shift "I described" → "we described" (joint Preface authorship). E23 must NOT pre-empt the callback — Julie's source references "Jesse discovered it when he ran his own company's first sprint and found that the constraint he thought he was solving was a symptom of a different constraint two steps upstream." This is a **different Jesse anchor** (the first sprint at his company, distinct from the chutes-and-ladders/developer-departure story which is the Preface). Both anchors are operator-recognizable; they do not duplicate.

**Resolution:** Preserve both anchors. E23's "first sprint at his own company" anchor is canonically Jesse's (per Preface establishment); the chutes-and-ladders callback at L26 is also Jesse's. The two stories are different — the first sprint at his company was the work that *solved* the chutes-and-ladders problem in a specific order. E23's anchor is the *discovery* moment ("the constraint I thought I was solving was a symptom upstream"); L26 is the *origin* moment (the Preface developer departure). Verify Drafter does not blend the two.

### Pre-existing voice debt — opportunistic awareness only

The chapter contains some inherited cadence patterns that are **grandfathered** and out of scope for E21/E22/E23 modification:

- **L10 triplet cadence** — "She's seen demos. She's read the case studies. She has a clear picture in her head..." — A3-adjacent but hammered cadence earns the operator hook. Grandfathered.
- **L12 long paragraph** — "But I've also watched what happens when you start there." — 152 words, A5-adjacent ("the requirements shift two weeks in because nobody mapped... so the spec changes, the scope expands... edge cases surface that nobody anticipated"). Risk-map line 110 flags as HEAVY REWRITE candidate, but it is **NOT in E22's scope** (E22 lands a NEW paragraph after L14, not a rewrite of L12). Grandfathered.
- **L22 construction metaphor** — "framing a house before pouring the foundation. The walls go up. The roof goes on." — A14 metaphor literalism check: construction has structural order; framework has sequence order; metaphor literally applies. Clean. Grandfathered.
- **L24 "Skip the first two steps and you are buying a tool. Run all six in order and you are changing how the work is owned."** — antithesis closer, A1-adjacent. Acceptable single instance in §3.1. Grandfathered.
- **L41–L44 four-term definition block** — risk map line 113 flags as REJECT style ("four abstract-noun definitions in sequence"). This is **chapter-canonical**: the four terms must be defined together because they are canonical vocabulary (charter §3). The risk-map verdict is a Julie-source rejection, not a current-chapter rejection — the chapter's L41–L44 block is already operator-direct (each term defined by what it produces / who runs it / what it replaces). Grandfathered.

None of these are in scope for E21/E22/E23; flagged only so the Drafter does not introduce *new* parallel constructions or *new* metaphor extensions that compound with these inherited ones.

### No CONFLICT-flagged content per stale-audit

- Discovery-call frame at L8–L14 is canonical (Compound runs discovery calls; per `compound-does-not-have-on-site-implementers-like` memory, discovery/Clarity Calls are the model — this is not on-site implementation).
- Chutes-and-ladders callback at L26 is sourced (Preface canonical, per `ahmed-story-is-chutes-and-ladders` memory).
- Meridian Manufacturing threading at L122–L147 is canonical and matches Ch 1 + cross-book commits.
- No Greenline / Marina-fabrication / nine-red-weeks / Ahmed / Donna / Harley / Saint Clair regressions.
- No CH04-L10 / PM-Agent-Team collisions in Ch 3.

### MEANS/ENDS-RISK — full §5 sweep

Per scout.md §5, MANDATORY means-vs-ends check on opener, closer, and any paragraph framing the framework/Sequence/Sprint as destination. Findings:

- **E22 (chapter-opener-adjacent):** Lands between the discovery-call story and the chapter-thesis pivot. MEANS/ENDS-RISK = HIGH. Acceptance criterion: close on operator outcome (twelve months later, built the wrong thing at expense — what Signal prevents), name Signal as the means. Flagged.
- **E23 (§3.1 framework-argument section):** Lands inside the chapter's framework-argument section. MEANS/ENDS-RISK = HIGH. Acceptance criterion: close on operator outcome (the work compounds / actually ships / produces a number), name the order as the means. Flagged.
- **Chapter opener L8–L16 (E21 scope, attribution-only):** Currently "That is the conversation this chapter exists to prevent you from having with yourself." — this is *what the chapter prevents the reader from doing wrong*, not system-as-destination. **CLEAN.** Grandfathered.
- **Chapter closer L180–L182 ("Begin at *Signal*")** + reflection questions L184–L189: closer focuses on the operator outcome of refusing to move forward until the constraint is named, with the operator math at L182 ("Most companies will not do it. The ones that do are the ones that compound"). Compounding = operator outcome (per canonical Equation). **CLEAN.** Out of scope; grandfathered.
- **§3.6 "You learn this on a *Sprint*" (L163–L173):** Closer at L171 echoes the canonical Equation "*Co-Intelligence + Rhythm = Compound.*" and L173 lands "The first Sprint is where the Framework stops being something you read about and starts being something your organization can do." — operator outcome framing (organization-can-do). **CLEAN.** Out of scope; grandfathered.
- **L165 "the Framework is not a model of how AI implementation could go — it is the structure of how the work moves when it moves correctly":** A1-adjacent (Framework = structure of how work moves) — but "the work moves correctly" is operator outcome. Borderline but reads operator-direct. **CLEAN.** Out of scope; grandfathered.

§5 check confirmed: only E22 and E23 are at active MEANS/ENDS-RISK. Both flagged with explicit acceptance criteria.

### A2 trap full sweep — Ch 3 canonical vocabulary

Per voice-charter §3 and Ch 2 lessons-learned (A2 coined-term-before-defined: 2/2 chapters where new concepts introduced). Ch 3 introduces four canonical terms in §3.2:

- **Framework** = the whole six-step shape (charter §3).
- **Sequence** = the ordered steps Signal → Source → Design → Build → Deliver → Compound. The order is the argument.
- **Sprint** = one pass through the Sequence on one validated constraint.
- **Rhythm** = the cadence — running the framework over and over. Quarterly.

Also forward-referenced at higher level in Ch 3 (and required to NOT be load-bearing in E21–E23):

- **Compound Sprint** (the unit) — currently named in the chapter at L43 inside the Sprint definition; Compound Bench (the six AI coaching agents) and Skills Library (the twelve instruments) are NOT introduced in Ch 3 in current form (per grep — both appear only in glossary). This is a discrepancy with the bead prompt's note that they are "introduced in Ch 3 at high level." **Flagged for awareness; out of scope for E21–E23.**
- **Diagnose / Execute & Compound** grouping — introduced in §3.4 at L68.
- **Hybrid Accountability Chart (HAC)** — referenced at L171 ("The Hybrid Accountability Chart gains new entries") but defined in Ch 6 per charter §3 + manifest mapping. Out of scope for E21–E23; flagged.
- **Equation: *Co-Intelligence + Rhythm = Compound*** — referenced at L171, defined cleanly in context.

**E22 and E23 A2 discipline:**

- Neither E22 nor E23 may introduce Framework / Sequence / Sprint / Rhythm as load-bearing carriers (defined at L41–L44).
- E22 may forward-reference "Signal" (already named at L14, defined at L57).
- E23 must use plain operator language ("the order" / "the principle" / "the work") in lieu of canonical terms.
- The first capitalized "Framework" in the chapter is at L24 (after E23's landing point). Drafter must not pre-empt.

### EC1 canonical-definition verification (per Ch 2 lessons-learned)

Per Ch 2 EC1 update (2026-05-31): when a coined term is used in E22 or E23, the definition must match the canonical definition from voice-charter §3, manifest, or glossary. Verification points for Ch 3:

- **"Signal"** in E22 forward reference: must match charter §3 / chapter §3.3 L57: "you find the one operational constraint worth solving next (or first), and quantify what it costs." E22's "Signal exists to prevent that. It is the discipline of refusing to build until the problem has been precisely named and its cost has been quantified" — verify alignment. **PASS** (the "precisely named and its cost has been quantified" phrase is canonical Signal language).
- **"diagnose before prescribe" in E23**: this is not a Compound coined term; it's an org-design field principle. No canonical definition in book vocabulary. Verify Drafter uses the phrase as-is from Julie's source (it is the recognizable org-design canonical formulation). No EC1 trap.

---

## Recommended bead order

Execute in this order. Dependencies in parentheses.

1. **E21** (ATTRIBUTION → LAND-WITH-MODIFICATION, Path A — Voice Shifter solo)
   - Apply blended-we + single in-prose attribution at L8 opener (Pattern A preferred per cross-chapter consistency with Ch 2 E16; Pattern B fallback)
   - Reject Julie's inline `Jesse:` tag
   - Preserve "Can we just build it" beat verbatim (canonical opening hook per author-Approved manifest note)
   - Preserve L10 triplet cadence ("She's seen demos. She's read the case studies. She has a clear picture...") — grandfathered, do not modify
   - Preserve L14 "let's start at Signal" pivot verbatim
   - L26 chutes-and-ladders callback: shift "I described" → "we described" (joint Preface authorship); "I solved the problem" → "Jesse solved the problem" or "the problem got solved" (lighter)
   - **Contractions: preserve current chapter contractions; do not regress to Julie's no-contractions source**
   - *Why first:* Sets the voice E22 and E23 write into. Zero dependency.

2. **E22** (NEW-SECTION → LAND-WITH-MODIFICATION, Path A — Drafter solo)
   - New paragraph after L14, before L16
   - **Framework-attribution scrub:** reframe "I have had a version" → joint blended-we ("We've watched..." or "Every major implementation failure we've been called in to salvage..."); single in-prose attribution sentence anchoring Julie's CHRO/org-design lens
   - **A3 triplet collapse:** ERP / restructurings / acquisitions enumeration → Pattern B preferred (one example + generalizing list) or Pattern C fallback (strip enumeration); explicit risk-map directive: "Cut the failure-pattern hedge-list. Lead with one specific company."
   - **MEANS/ENDS-RISK:** close on operator outcome (twelve months in, built the wrong thing at great expense) and name Signal as the means; preserve Julie's source closer phrase "precisely named and its cost has been quantified" (canonical Signal deliverable language)
   - **Cross-chapter n-gram check:** explicitly avoid Ch 1 L21 "We've watched this same pattern for two decades" verbatim phrasing
   - **A2 discipline:** forward-reference "Signal" is fine (already named at L14); no Framework / Sequence / Sprint / Rhythm capitalized as load-bearing
   - **Forbidden vocab grep:** zero "transformation" / "leverage" / "synergy" / "alignment" / "augment" — Drafter scanner gate mandatory
   - **Coherence:** must not duplicate L16 chapter-thesis pivot ("the conversation this chapter exists to prevent"); close at the *stage* level (Signal as discipline), let L16 land the *chapter* level
   - *Dependency:* E21 (blended-we voice established at opener).

3. **E23** (NEW-SECTION → LAND-WITH-MODIFICATION, Path A — Drafter solo)
   - New paragraph after L20 (the "cause is the order" hammer), before L22 (the construction metaphor)
   - **A3 triplet collapse:** "Diagnose before you prescribe. Understand the system before you change it. Map the work before you redesign it." → "Diagnose before you prescribe." only (cut the two paraphrases)
   - **Framework-attribution + paired-attribution scrub:** "Julie has applied... Jesse discovered..." → joint reframe (Pattern B preferred per E23 acceptance criteria: single in-prose anchor per author, no individual-discovery framing of field-canon principle)
   - **MEANS/ENDS-RISK:** closer "The order is the reason it works" (system-as-destination) → "The order is the reason the work compounds" (operator outcome, vocabulary-consistent with canonical Equation at L171)
   - **A2 discipline:** no Framework / Sequence / Sprint / Rhythm / HAC / TML / Compound Sprint capitalized as load-bearing carriers; plain language ("the order" / "the principle" / "the work")
   - **A1 antithesis discipline:** "The order is not a preference. The order is the reason..." closer is acceptable single instance in §3.1; verify no second antithesis in E23 body
   - **Forbidden vocab grep:** zero "transformation" / "leverage" / "synergy" / "alignment"; "organizational design" allowed sparingly in body (NEVER in heading); Drafter scanner gate mandatory
   - **Coherence:** must NOT pre-empt construction metaphor at L22 (no "build before X" cadence in E23); must NOT pre-empt chutes-and-ladders callback at L26 (E23's Jesse-anchor is *the first sprint at his company*, not the developer-departure)
   - **Author follow-up logged:** Q-E23 jf-note on section heading "Order is the Argument" is a separate, post-E23-landing author decision; does not block E23 substance
   - *Dependency:* E21 (chapter voice established), E22 (Julie's voice established in the chapter; E23 inherits the calibrated attribution frequency).

**Path A beads:** All three rows (E21, E22, E23). Default to solo Drafter per AGENT-TEAM §1 lessons-learned default + Ch 2 outcome (Path A produced clean Ch 2 in 3 iterations).

**Path B candidates if any bead fails voice-gate twice:**

- **E22** — framework-attribution scrub + A3 triplet collapse + MEANS/ENDS-RISK + cross-chapter n-gram avoidance + forbidden-vocab discipline. Five intersecting controls; if Drafter trips on any, the Substance/Voice/Reader convergence may be necessary.
- **E23** — highest anti-pattern density of any E-row in Ch 3 (dual A3 triplet — principle enumeration + paired attribution parallel — plus framework-attribution scrub plus MEANS/ENDS-RISK plus A1 antithesis discipline plus A2 coined-term discipline). If Drafter fails to scrub all, Path B is appropriate.

**Critical sequencing constraint:** Preface E01/E02, Ch 1 E08–E15, and Ch 2 E16–E19 must have landed first (they cascade the blended-we + no-inline-tag + in-prose attribution convention + framework-attribution scrub + A3/A13 discipline to Ch 3). Per AGENT-TEAM §6 phase sequence, those are upstream beads; Ch 3 inherits the convention from `bcf8f11` (Preface), the Ch 1 commit (per lessons-learned), and `b53ca0d` (Ch 2 final commit).

---

## Skip / needs-author rationale

**No SKIP-ALREADY-DONE rows.** Verified: the current chapter does NOT contain the substance of E22 (the 20-year ERP/restructuring/acquisition pattern observation) or E23 (the thirty-year-old org-design principle anchor). Both are net-new content. E21 lands a voice-shift on the existing opener (which already contains the discovery-call story Julie's source mirrors).

**No NEEDS-AUTHOR rows.** All three in-scope E-rows (E21, E22, E23) carry mechanical resolutions per the voice charter, framework-attribution rule, Q-E21 + Q-E23 convention, prose-risk-map verdicts, and manifest author-approval annotations. No new author decisions required beyond the manifest-level approvals already on the books.

**Optional author follow-up (post-merge, not bead-blocking):**

1. **Q-E23 section heading revisit** — per author jf-note ("If I made a phrase and don't remember it, its not a good phrase. NEeds to be revised."). The heading "The order is the *argument*" at L18 is Jesse's existing coined phrase. The author may want to revise the heading independently of the E23 substance landing. **Logged here; not a bead, not a blocker.**
2. **E21 attribution pattern choice** — Pattern A (named opener, full-third-person body) vs. Pattern B (single attribution sentence + sustained singular-I body). Drafter picks based on cadence; author can override on diff review.
3. **E22 attribution phrasing** — confirm the single in-prose attribution phrase for Julie's CHRO/org-design lens does not over-credentialize relative to the Preface establishment.
4. **E23 attribution phrasing** — confirm Pattern B (Julie-anchor: "Julie has watched anchor every major engagement she's led" + Jesse-anchor: "Jesse hit the same principle inside his own company's first sprint") does not over-attribute; Pattern A or C fallback if cadence breaks.

---

## Done test status

- [x] Every in-scope E-row (E21, E22, E23) classified: 3 LAND-WITH-MODIFICATION (1 ATTRIBUTION + 2 NEW-SECTION); 0 SKIP, 0 NEEDS-AUTHOR
- [x] Every LAND row has tightened current-chapter line ranges (E21: L8 opener with cascading shifts at L10, L12, L14, L26; E22: between L14 and L16; E23: between L20 and L22 inside §3.1)
- [x] Every LAND row has 2–4+ bullet acceptance criteria covering substance preservation, anti-pattern risk, framework-attribution rule applicability, and coherence
- [x] **MEANS/ENDS-RISK check applied per scout.md §5 on opener/closer/concept-definition paragraphs:** E22 (chapter-opener-adjacent, lands before chapter-thesis pivot), E23 (§3.1 framework-argument section), both flagged with explicit acceptance criteria; full §5 sweep confirms no other §5-trigger paragraphs at risk
- [x] **A2 traps identified around Framework / Sequence / Sprint / Rhythm / Compound Bench / Skills Library:** A2 discipline acute in E22 + E23 (both land BEFORE §3.2 four-term definitions); plain operator language required; HAC / TML / Compound Sprint also discipline-applied
- [x] **Framework-attribution flags on E22 + E23:** direct application both rows — E22 reframes "I have had a version" → joint blended-we; E23 reframes paired Julie/Jesse personal-discovery → joint book IP extending field-canon principle
- [x] **Cross-chapter n-gram repetition flagged:** E22 must not duplicate Ch 1 L21 "We've watched this same pattern for two decades" verbatim
- [x] **EC1 canonical-definition verification applied:** "Signal" forward reference in E22 verified against charter §3 + chapter §3.3 (PASS); "diagnose before prescribe" in E23 is non-Compound field-canon phrase (no EC1 trap)
- [x] Conflicts flagged with specific source references (manifest §57, charter §4 A2/A3/A13, Q-E21, Q-E23, risk-map lines 109–112, stale-audit, persistent memories)
- [x] Bead execution order recommended with dependencies cited (E21 → E22 → E23)
- [x] Pre-existing voice debt at L10, L12, L22, L24, L41–L44 flagged for awareness (not in scope for modification)
- [x] Author follow-up items logged separately from bead-blocking decisions (Q-E23 heading revisit, E21/E22/E23 attribution phrasing)
- [x] Plan file at `_julie/per-chapter/03-the-framework.md`

**Outstanding author asks for Human Orchestrator:**

None blocking. All three beads dispatch under their current verdicts.

**Optional author decision points (post-Drafter, before commit):**

1. E21 attribution pattern choice (A vs. B) — see optional follow-up #2.
2. E22 attribution phrasing — see optional follow-up #3.
3. E23 attribution phrasing — see optional follow-up #4.
4. Q-E23 section heading "Order is the Argument" — see optional follow-up #1 (logged separately, post-merge).

---

## Author decisions (logged after dispatch)

*(To be filled in as author reviews each bead diff during execution.)*

- **E21:** _pending_ (attribution-pattern choice; L26 callback shift)
- **E22:** _pending_ (framework-attribution scrub + A3 collapse + MEANS/ENDS-RISK on closer + cross-chapter n-gram avoidance)
- **E23:** _pending_ (dual A3 collapse: principle triplet + paired-attribution parallel; framework-attribution scrub; MEANS/ENDS-RISK on closer; A2 coined-term discipline)

---

## Path verdict summary

- **Verdict:** Default **Path A** (solo Drafter) for all three rows.
- **Path B candidates if voice-gate fails twice:** E22 (five intersecting controls), E23 (highest anti-pattern density of any Ch 3 E-row).
- **Iteration target:** Match Ch 2 outcome (3 iterations: Scout → Drafter + scanner gate → editorial-coherence + surgical pass → author 2nd/3rd read).

---

*End of plan.*
