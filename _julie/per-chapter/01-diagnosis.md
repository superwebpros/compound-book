# Scout Plan — `chapters/01-diagnosis.qmd` (Ch 1: The Diagnosis)

**Generated:** 2026-05-25  ·  **Bead:** book-ff63.9.2  ·  **Scout:** Sage

## Chapter context (one paragraph)

Ch 1 is the diagnostic. It opens with the three-tools discovery-call story (a real call with a manufacturing company — confirmed canon per persistent memory `ch01-three-tools-story-real`), pivots to the headcount paradox math, resolves it with Jesse's SuperWebPros 13→8 redesign result, then turns to the operating-model frame (EOS shape + AI-as-staff diagnosis), the wrong-question / right-question trap, the five-dimension AI Readiness Scorecard, and a worked Meridian Manufacturing scorecard before closing on a brief "what this book is for" Co-Intelligent Company definition. The chapter is currently entirely in Jesse's first-person voice. The most recent substantive commits are `7709ea8` (2026-05-18, "Author review round 2") — which softened the culture/training dismissal, threaded Meridian's intro, and converted ASCII to tables in Ch01 — and `d7ac7bb` (2026-05-17, "Ch01: implement Jesse's editorial feedback, 14 fixes") which is the established polish baseline. The L9 first line *"I asked them one question. The answer told me everything."* is load-bearing in its current form and is the precise sentence E08 targets. The Meridian scorecard at L227–245 is sourced and protected; E15 does not touch it (E15 lands on the scorecard *intro* at L107, before the dimensions). One pre-existing voice debt — the A3 triplet pileup at L81 *"The pattern is mechanical. The diagnosis is mechanical. The fix is mechanical."* — was explicitly flagged in the voice charter Section 1, Pillar 4 as "reads as AI cadence…should not be imitated." It sits in our current manuscript and is in-scope for opportunistic cleanup during E12 (which lands in the same §1.2 it occupies). Author overall Ch 1 note: *"Approved; we want to make sure we aren't too EOS focused — it's not our IP."* This applies broadly — the EOS-shape paragraph at L69 and the L10/Scaling-Up cross-references throughout must be operator-language plain, not EOS-branded.

## E-row classifications

| E-row | Type | Verdict | Current-chapter target | Notes |
|---|---|---|---|---|
| E08 | VOICE-SHIFT | LAND-WITH-MODIFICATION | L9–L17 (discovery-call section) | I→we mechanical; preserve three-tools story (real per memory); reject inline `Jesse:` tag per Q-E21 — blended-we + in-prose attribution where attribution clarifies |
| E09 | NEW-SECTION | LAND-WITH-MODIFICATION | After L17, before L19 | Julie's "pattern predates AI by 20 yrs" paragraph; HEAVY REWRITE per risk map; strip individual-attribution framing per global rule; substance survives as a *we've-watched* observation |
| E10 | ATTRIBUTION | LAND-WITH-MODIFICATION | L49 (SuperWebPros 13→8 paragraph) | Headcount-paradox result attributes to Jesse's company specifically; lands via in-prose attribution (not inline `Jesse:` tag); preserves canonical 13-to-8 cumulative framing per stale-audit Risk #6 |
| E11 | NEW-SECTION | LAND-WITH-MODIFICATION | After L49 (paired with E10) | Julie's parallel: global food safety company global HR redesign across 44 countries; HEAVY REWRITE per risk map; **MEANS/ENDS-RISK** soft flag — must land "headcount math working" outcome, not "redesign" as destination |
| E12 | NEW-SECTION | LAND-WITH-MODIFICATION | After L65, before L67 (inside §1.2 Operating Problem) | Julie's "thirty years of failed transformations" framing; **forbidden vocab**: "transformations" is auto-reject (charter §3); reframe as "thirty years of operating-model failures"; HEAVY REWRITE per risk map; opportunistic A3 cleanup at L81 in same pass; respect Ch 1 EOS-lean caution |
| E13 | ATTRIBUTION | LAND-WITH-MODIFICATION | L71 (three-questions accountability-chart check) | Re-attribute "three questions" check to Julie via in-prose phrasing per Q-E21; **reject** Julie's redline phrasing *"Julie asks of every leadership team she advises"* (over-attribution; framework-attribution rule soft-applies); land as "the three questions we've asked of every leadership team we've advised…" with Julie's CHRO frame supplied through prior E11 setup |
| E14 | NEW-SECTION | LAND-WITH-MODIFICATION | After L87, before L89 (inside §1.3 Wrong Question, between task-orientation critique and goal-orientation reveal) | Julie's "outcome first, design second, tool third" framing; HEAVY REWRITE per risk map; **MEANS/ENDS-RISK** check — the closer paragraph of §1.3 (L89) lands as "goal-orientation produces results because the design was built to produce them" which is system-as-end-adjacent; verify E14's insertion does not amplify that; lead with outcome the discipline produces |
| E15 | NEW-SECTION | LAND-WITH-MODIFICATION | After L107, before L109 (scorecard intro paragraph before Dimension 1) | Rewrite scorecard intro attributing 5 dimensions split by discipline; **author flag: "Requires review"** — `NEEDS-AUTHOR` lite; framework-attribution rule applies — the scorecard itself is joint IP; can land the *origin* description (which discipline informed which dimension) but cannot land as "Jesse owns these / Julie owns those" IP claim; **MEANS/ENDS-RISK** check — scorecard is means (diagnoses readiness), not end (the goal is headcount math working); avoid framing the scorecard as the destination |

**Counts:** 8 LAND-WITH-MODIFICATION · 0 LAND-clean · 0 SKIP-ALREADY-DONE · 0 NEEDS-AUTHOR (E15 has a soft author-review flag carried from manifest, not a substance NEEDS-AUTHOR) · 0 hard CONFLICT.

**Path verdict:** Default Path A (solo Drafter) per AGENT-TEAM §1 lessons-learned default. E11 and E15 are the strongest Path B candidates if any bead in this chapter gets escalated — E11 because the "headcount math working" outcome must land cleanly without "transformation" / "graft" / "redesign" treated as ends, and E15 because the framework-attribution + IP-split framing has author-flagged review risk. Recommend single solo Drafter pass for all eight rows in the recommended bead order below; escalate to Path B only on second voice-gate fail.

---

## Per-E-row acceptance criteria

### E08 (VOICE-SHIFT, LAND-WITH-MODIFICATION) — discovery-call section I→we

**Substance to preserve:**
- The three-tools / three-people discovery-call beat — REAL story per persistent memory `ch01-three-tools-story-real`. Do NOT flag as fabricated; do NOT rewrite.
- The opening line *"I asked them one question. The answer told me everything."* (L9) — its cadence is the hammer-blow opener the chapter trades on.
- The "ChatGPT / Claude / Poe" enumeration at L11 — three real tools mentioned by three real people; not a contrived triplet for cadence (per memory).
- The "three people, one company, three different tools" beat at L13 and the design-problem pivot at L17.
- The single-sentence hammer line *"That company is not unusual. It might be yours."* at L19.

**Modification from Julie's instruction:**
- Julie's redline (lines 224–262) proposes: replace L9 with *"The answer to one question told us everything we needed to know."* and convert `I asked` → `we asked` at L11, L15. Plus convert *"the most common version of the AI problem I see"* → *"we see"* at L17.
- **Land the we-conversion**, but **modify the opening line**. The risk map verdict for julie-final.md:124 is LIGHT EDIT with the AI-tell direct-address closer *"told us everything we needed to know"* flagged. Direction (risk map line 56): tighten to *"One question told us everything."* That preserves the hammer-blow rhythm and drops the AI-tell.
- **Reject inline `Jesse:` tag** anywhere in this section. Per Q-E21 and the Preface execution pattern, attribution is in-prose. The opening line and the body both land in blended-we voice — the chapter is a *shared* diagnostic, not a transcript of Jesse's call.
- **Optional in-prose attribution** for the discovery call: if the Drafter wants to mark this as a Jesse-led engagement, do it in-prose ("We were on a discovery call — one Jesse was leading…") — but only if it lands cleanly without disrupting the cadence. Default is blended-we throughout.

**Anti-pattern risk:**
- A3 (triplet pileup): low risk for the section as it stands (the ChatGPT/Claude/Poe triplet is the genuine call content, not constructed cadence). Do NOT introduce new triplets in we-conversion.
- A5 (general AI smell): high risk on the opening line — *"told us everything we needed to know"* is the AI-tell direct-address closer. Tighten to *"One question told us everything."*
- A15 (unqualified AI agency): not triggered here; AI is a tool the operators are using, not an agent making decisions.

**Framework-attribution rule:** N/A (no framework introduced in this section).

**Coherence:**
- This section establishes the chapter's blended-we voice. Every downstream E-row (E09–E15) lands inside the voice this row sets. Execute E08 first.
- The "this is the most common version of the AI problem we see" → must remain in chapter-voice operator weight. Don't soften.

---

### E09 (NEW-SECTION, LAND-WITH-MODIFICATION) — pattern predates AI by 20 years

**Substance to preserve (from `_julie/julie-redline.md:272–283`):**
- The pattern of organizational gap-after-new-capability has existed for 20+ years — pre-AI.
- The three classes of prior examples: acquisitions, restructurings, operating model redesigns. (These are the substance; the *triplet construction* is the AI tell — see below.)
- The structural insight: a new capability arrives (merged company / new function / new technology) and the organization tries to absorb it *without changing the structure designed to receive it*. The accountability is never reassigned. The workflows are never redesigned. The new capability sits next to the existing structure and produces nothing structural.
- The hammer claim: *AI is not creating a new organizational problem. It is exposing an old one.* (substance preserved; cadence reworkable)

**Modification from Julie's instruction:**
- Julie's source paragraph (redline:272–283) reads: *"Julie has been watching a version of this pattern for twenty years…In every major organizational transformation she has led — acquisitions, restructurings, operating model redesigns — the failure mode was always the same."*
- **Framework-attribution scrub (global rule applies in spirit, not literally — no framework named here):** Do NOT land as "Julie has been watching." The 20-year-pattern observation is shared diagnosis credibility, not Julie's individual IP. Land as blended-we with in-prose attribution that draws on Julie's CHRO background.
- **A3 triplet:** Julie's source has *"acquisitions, restructurings, operating model redesigns"* — that's a literal triplet but the substance is real (these are three distinct prior contexts that bear the same pattern). Land it as a list collapsed to a single beat or as a single concrete example. Direction: pick ONE acquisition or restructuring with a specific operating consequence — not three abstractions in a row.
- **A5 AI smell:** Julie's source has *"the failure mode was always the same"* — this is generic-AI smoothing. Risk map line 61 direction: *"Lead with the concrete: name one specific transformation, the structural failure, and the cost. Drop 'the failure mode has been identical' — that's smoothing-AI."* Apply that here.
- **Forbidden vocab:** Julie's source uses *"transformation"* — auto-reject per charter §3. Reframe as "operating-model change" / "restructuring" / "integration" / "acquisition" (concrete operator language). The Ch 1 note from author also says *"not too EOS focused — it's not our IP"* — same plain-operator-language principle.
- **A2 risk:** Do NOT introduce coined book vocabulary (Co-Intelligent Company, Co-Operating Model, HAC) in this paragraph — chapter still hasn't earned them. The "operating model" phrase as plain prose is fine; the capitalized terms are not.

**Anti-pattern risk (highest):**
- A3 (triplet) — Julie's *"acquisitions, restructurings, operating model redesigns"* explicitly. Collapse.
- A5 (AI smell) — the smoothing closer *"the failure mode was always the same"* and *"AI is not creating a new organizational problem. It is exposing an old one"* (the latter is the substance hammer; preserve substance, but a cleaner cadence than the "not X. It is Y" closer per charter A3 / risk map Pattern 4).
- A4 (boastful biographical examples) — low risk; the 20-year span is operator-credentialing, not the "121 episodes" beat. Land as a clipped credential, not a tour.
- A11 (inflated symbolism) — guard against "every major transformation" / "every leadership team" generalizations. Specific instance, named context.

**Framework-attribution rule:** Soft applies. No framework named here. Frame as joint observation drawing on Julie's CHRO experience, not as "Julie's 20 years produced this insight."

**Coherence:**
- Lands AFTER L17 (the design-problem pivot) and BEFORE L19 (*"That company is not unusual. It might be yours."*).
- This is where Julie's voice first enters Ch 1. The blended-we from E08 already lands; E09's job is to credibly extend the diagnosis backward in time.
- The "it's not just AI" claim here sets up §1.2's operating-model frame at L61–L71. Do not contradict L65 (*"Culture matters…Training matters…Tool selection matters…all real, none sufficient. The deeper problem is the operating model"*) — E09's pattern observation should foreshadow that frame, not pre-empt it.

---

### E10 (ATTRIBUTION, LAND-WITH-MODIFICATION) — SuperWebPros 13→8 attribution

**Substance to preserve:**
- The entire L49 paragraph is sourced canonical content. **Preserve verbatim or near-verbatim** — only the attribution wrapper changes.
- "13 to 8" framing must remain **cumulative ("over the following year" / no single-moment-shift framing)** per stale-audit Risk #6 and persistent memory `13-to-8 headcount shift is a real observation`.
- "Not through layoffs — through redesign" beat. The mapped-every-function / agent-teams / billings-up / profitability-up arc. The "five roles redesigned out of existence" closer.

**Modification from Julie's instruction:**
- Julie's redline (lines 303–317) proposes converting *"Here is how it resolved for us"* → *"Here is how it resolved for Jesse"* and *"My software development company"* → *"His software development company."* This shifts from first-person to third-person.
- **Reject the third-person shift.** Per Q-E21, attribution is in-prose blended-we, not third-person rewrite. The Ch 1 voice is established as blended-we. Shifting to "Jesse / he / his" mid-chapter creates a transcript-style break that Q-E21 explicitly rejects.
- **Land the attribution differently:** Open the paragraph with an in-prose attribution phrase that establishes this is Jesse's company specifically without breaking the we-voice. E.g., *"Here's how it resolved at Jesse's company. SuperWebPros, his software development firm, went from thirteen people to eight."* — naming SuperWebPros once and "his" once is enough; the rest of the paragraph stays in blended-we.
- **SuperWebPros remains named** per stale-audit Section 1 (intentionally named at Ch01:49). Do not anonymize.
- Preserve the closing sentence *"The rest of this book shows you how we did it and gives you the tools to replicate it."* — that's the chapter's cross-chapter callout; cumulative-we is correct there.

**Anti-pattern risk:**
- A4 (boastful biographical) — moderate risk. The 13→8 result is concrete and operator-relevant, not contrived. Keep operator-direct.
- A3 (triplet) — *"mapped every function, identified what required human judgment and what didn't, built agent teams for the work that followed rules"* — this is a borderline triplet but it's load-bearing concrete process language, not parallel cadence for rhythm. Preserve.
- A5 — none in current paragraph.

**Framework-attribution rule:** N/A.

**Coherence:**
- E10 + E11 execute as a **single paired bead**. E11's Julie parallel lands immediately after E10's Jesse story. The pairing is the rhetorical move — two operators arrived at the same headcount math from different scales. Splitting them strands the rhetoric.
- L51 callout-tip (Pro Tip) follows. Verify the callout still reads correctly after E10+E11 reframe — it likely does, since it's general framing not tied to Jesse-specific or Julie-specific story.

---

### E11 (NEW-SECTION, LAND-WITH-MODIFICATION) — Julie's parallel global HR redesign

**Substance to preserve (from `_julie/julie-redline.md:319–332`):**
- Julie's parallel context: a global food safety company completed a Fortune-500-division acquisition (per Preface E03).
- The integration-instinct was to add headcount (HR business partners, regional managers, coordination roles).
- The alternative path taken was redesign: explicit decisions about which functions required local human judgment, which could be standardized across regions, which could be systematized entirely.
- **The headcount outcome:** the redesigned global HR function served 44 countries with a *smaller proportional team* than the pre-acquisition domestic function. **Not because headcount was cut — because the work was designed before it was staffed.**
- This last claim is the load-bearing operator beat. It's the parallel to Jesse's 13→8 — the same math working at a different scale and in a different industry.

**Modification from Julie's instruction:**
- Julie's source has the **canonical doubled-article LLM artifact** at line 320: *"the the acquired division acquisition"* — Pattern 1 from the risk map (line 187). This is direct evidence the paragraph was LLM-drafted. Replace wholesale.
- **A3 triplet:** *"more HR business partners, more regional managers, more coordination roles"* is a constructed-symmetry triplet. Collapse to one specific role + the headcount math (e.g., "more HR business partners by region" — single instance).
- **A3 triplet (second):** *"explicit decisions about which functions required local human judgment, which could be standardized across regions, and which could be systematized entirely"* — three parallel clauses; collapse to a single concrete example of one decision that turned on judgment-vs-system.
- **MEANS/ENDS-RISK (per scout.md §5):** This paragraph frames "redesign" as the move and "smaller proportional team" as the outcome. That's *correct* means→ends order — substance survives. But the Drafter must NOT slide into *"the redesign produced leverage"* / *"design produced compounding"* abstract-noun closers that frame design as the destination. **Acceptance criterion:** the operator outcome (headcount math, ratio, dollar-equivalent freed capacity) leads; redesign is named as the means to that outcome. Do not close on "design" as the destination.
- **Framework-attribution rule:** Soft applies. The redesign here is biographical fact (Julie was the CHRO; she ran the redesign) — that's fair to credit in-prose. But the paragraph cannot read as "this is the org-design framework Julie brings to the book." The framework lives in joint-IP chapters downstream; here, this is one operator's parallel story to Jesse's 13→8.
- **E60 anonymization:** "a global food safety company" already conforms; preserve.
- **Forbidden vocab:** Watch for *"transformation"* — auto-reject; use "redesign" / "restructure" / "integration" instead.

**Anti-pattern risk (highest):**
- A3 (triplet pileup) — Julie's source has TWO triplets stacked. Both must collapse. This is the highest-risk row in the chapter for A3.
- A5 (AI smell) — Julie's source closer *"Because the work was designed before it was staffed"* is operator-direct and lands; preserve. But *"the redesign produced a global HR function that served 44 countries"* needs to lead with the operator outcome (smaller proportional team, the math), not with the abstract noun "redesign."
- A13 (means/ends) — Per §5 special check above. Lead with outcome; name redesign as the means.
- A4 (boastful biographical) — moderate. 44-countries / Fortune-500-division is credentialing. Mitigated because (a) the Preface E03 already established Julie's credentials and (b) the headcount-math claim earns the credentialing. Don't dwell on the scale; cash it out as the operator beat.

**Framework-attribution rule:** Soft applies. Biographical attribution is fair; framework attribution is not.

**Coherence:**
- Lands as part of the paired E10+E11 bead. Immediately after L49 (Jesse's 13→8 paragraph).
- The pairing should land as: *Here's how it resolved at Jesse's company [E10]. And here's the same math at a different scale, in a different industry [E11].* The transition is the rhetorical work.
- L51 callout-tip ("The headcount paradox doesn't break by adding AI…") follows. Verify it still reads after E10+E11 reframe.
- Excalidraw diagram at L57 (`ch01-headcount-before-after`) is the visual of the headcount paradox; both stories are operating examples of that diagram. No change needed to the diagram itself.

---

### E12 (NEW-SECTION, LAND-WITH-MODIFICATION) — thirty years of operating-model failures

**Substance to preserve (from `_julie/julie-redline.md:352–361`):**
- Operating-model failures predate AI by decades.
- The structural error has the same shape across multiple prior tech/process introductions.
- The capability arrived; the structure never changed to receive it; the new thing sat next to the old structure; produced nothing structural.
- AI is the latest version of this failure pattern. The technology is different; the organizational design error is identical.

**Modification from Julie's instruction:**
- **Forbidden vocab — auto-reject:** Julie's source uses *"transformation initiative"* twice (charter §3 auto-reject). Reframe:
  - *"Every major transformation initiative of the last thirty years"* → *"Every major operating-model change of the last thirty years"* or *"Thirty years of failed operating-model changes"*.
- Author note on Ch 1: *"we want to make sure we aren't too EOS focused — it's not our IP."* This is about EOS, not transformations, but the same principle (plain operator language). Apply broadly.
- **A3 triplet:** Julie's source *"ERP implementations, lean manufacturing rollouts, post-merger integrations"* is a constructed triplet. The substance is real (three concrete prior tech/process examples). Risk-map direction (line 73): *"Pick ONE failure with a number, not three with rhythm."* Apply: name one — e.g., ERP rollouts with a concrete cost — and reference the others briefly without parallel cadence. The author note on Ch 1 (*"not too EOS focused"*) means: be careful here too. Three named systems read as a tour; one named system + one operator number lands.
- **Risk-map line 73 also flags:** Julie's source closer *"The technology is different. The structural error is identical."* This is the smoothing-AI antithesis closer (charter §4 Pattern 4 / A3-adjacent). Preserve the substance — the structural-error-is-identical claim is load-bearing — but rework the cadence away from "X is different. Y is identical." Land as one declarative.
- **Opportunistic A3 cleanup at L81:** The current L81 reads *"The pattern is mechanical. The diagnosis is mechanical. The fix is mechanical."* This is the **exact triplet pileup** the voice charter §1 Pillar 4 flags as auto-reject AI cadence. It sits in our current manuscript. Voice Shifter / Drafter handling E12 (which lands in §1.2) has authority per charter §5 to fix this in the same pass. **Direction:** preserve the principle (the pattern is mechanical, not philosophical) but cut the triplet — single declarative or two-clause sentence.
- **A2 (coined term before stakes):** Do not introduce capitalized framework vocabulary here (Co-Intelligent Co-Operation appears at L63 already — that's the section's coined term and it's load-bearing, leave it; do not stack more on top). The current L63 line *"Specifically, a Co-Intelligent Co-Operation problem"* is the chapter's first naming of the title-phrase. Preserve.

**Anti-pattern risk (highest):**
- A3 (triplet) — Julie's *"ERP / lean / post-merger"* triplet plus existing L81 triplet. Both in scope for this bead.
- A5 (AI smell) — closer cadence.
- Forbidden vocab — "transformation" *must* be replaced.
- A1 (abstract-noun-equals-abstract-noun) — guard against "operating model is X. Organizational design is Y" definitional cadence.
- **Author Ch 1 note compliance:** Do not lean too EOS. The current chapter already has the EOS shape at L69 (paragraph beginning *"Operators who run on EOS…"*); E12 should not amplify the EOS framing further. Keep "any disciplined system" language plain.

**Framework-attribution rule:** N/A (no framework component named).

**Coherence:**
- Lands AFTER L65 (the "Culture matters / Training matters / Tool selection matters" paragraph) and BEFORE L67 (the chatbot-vs-agent mental-model paragraph). E12's job is to give §1.2's operating-model claim historical depth — the same pattern across 30 years of prior tech introductions.
- Must connect smoothly to the L69 EOS shape paragraph (which says *"You know exactly what happens to a company that adds work without naming who owns it"*). E12 + L69 should read as *the same pattern across history AND inside disciplined operating systems* — different evidence for the same diagnosis.
- L81 triplet fix in the same pass.

---

### E13 (ATTRIBUTION, LAND-WITH-MODIFICATION) — three-questions accountability check

**Substance to preserve (from `_julie/julie-redline.md:381–392`):**
- The three questions framework: what is this function accountable for, what is its scorecard, who reviews the output on what cadence.
- The diagnosis hammer: clean answers for the humans, blank stares for the AI. AI has no seat on the chart, no number it's hitting, no review rhythm.
- The closer: *"You are running it that way because you have not yet decided that AI is staff."*

**Modification from Julie's instruction:**
- Julie's redline replaces *"the same three questions you would ask of a human team"* with *"the same three questions Julie asks of every leadership team she advises."*
- **Reject the third-person re-attribution.** Per Q-E21, the convention is blended-we + in-prose attribution. *"Julie asks of every leadership team she advises"* is third-person; it breaks the we-voice. It also reads as over-attribution: framing-of-functions-via-three-questions is generic org-design diagnostic practice, not a Julie-coined framework. Per the framework-attribution rule (manifest §line 57): *"Framework components do not get individual author attribution."* The three-questions check is exactly that class of framework component.
- **Land the attribution differently.** Two options for the Drafter:
  - **Option A (preferred):** Keep the existing phrasing *"the same three questions you would ask of a human team"* — the attribution is unnecessary because E08 + E09 + E11 have already established blended-we, and the three questions are generic org-design discipline that doesn't need a single-author credit. **Verdict: SKIP-ALREADY-DONE on the literal attribution change; the chapter already lands the three questions cleanly.**
  - **Option B:** If author wants Julie's CHRO voice signaled here specifically (per the author's overall approval of E13), add a single in-prose phrase upstream — e.g., a sentence at the start of §1.2 (after E12) that names this as the kind of question Julie has run with leadership teams. Then the three questions later in the section inherit that frame without inline attribution.
- **Hybrid recommendation:** Treat E13 as **LAND-WITH-MODIFICATION → effectively SKIP** at the literal target line (L71). The attribution work happens upstream via E09 + E11 + E12 establishing Julie's CHRO frame; L71 stays in blended-we.

**Anti-pattern risk:**
- A4 (boastful biographical) — would be triggered by *"every leadership team she advises"* (generalizing scope). Avoided by keeping the existing phrasing.
- A3 (triplet) — the three questions ARE a literal triplet but they're the load-bearing content (the framework's three checks). This is the rare exception to A3 — operative enumeration, not constructed cadence. Preserve.

**Framework-attribution rule:** **Applies directly.** The three-questions accountability check is a generic org-design diagnostic. It is joint IP. Reject any individual-author attribution.

**Coherence:**
- L71 is the existing diagnosis-in-one-move paragraph. Preserving it lets the chapter close §1.2 cleanly with the "AI is staff" hammer at the end of the same paragraph and the callout at L73–L77.
- The callout at L73–L77 (Action Step: walk into your next L10 with the question) is preserved. EOS-vocabulary mention ("L10 or leadership meeting") — the *"or leadership meeting"* alternative is already there, satisfying the Ch 1 author note about not over-leaning EOS. Preserve.

---

### E14 (NEW-SECTION, LAND-WITH-MODIFICATION) — outcome-first design discipline

**Substance to preserve (from `_julie/julie-redline.md:418–427`):**
- The discipline of org-design: start with the outcome the organization is accountable for, then design the work backward from that outcome.
- The four checks within that discipline: who owns what; what requires judgment; what can be systematized; where the handoffs live.
- The order: outcome first, design second, tool or role third.
- The hammer: AI didn't invent this discipline. It made the cost of skipping it catastrophically visible.

**Modification from Julie's instruction:**
- Julie's source opens *"Julie has asked a version of this question in every organizational design engagement for twenty years."* Reject the over-attribution phrasing per Q-E21 and framework-attribution rule. The "outcome first, design second, tool third" discipline is joint IP. Reframe in blended-we.
- **A3 triplet:** Julie's source has *"Who owns what. What requires judgment. What can be systematized. Where the handoffs live."* — four parallel one-clause sentences. Risk-map direction (line 76 + 77): *"Cut the five-clause triplet to one concrete example."* Apply: collapse the four to either a single specific example OR a single sentence that lists them without staccato cadence.
- **MEANS/ENDS-RISK check (per §5 special check):** §1.3's closing paragraph at L89 reads *"Goal-orientation produces results because the design was built to produce them."* This is on the edge of framing design-as-destination. E14 should land between L87 (task-orientation critique) and L89 (existing close) and **must reinforce the outcome-leads-design ordering, not flip it.** The closer at L89 will be the existing one; E14's job is to make explicit *what* the outcome-first discipline is. Acceptance criterion: lead with the operator outcome the discipline produces (e.g., the result Elena got, the math working, the cost-of-skipping made visible) — then name the discipline as the means.
- **Forbidden vocab:** Watch for *"transformation"* — Julie's source doesn't appear to use it here, but verify. Use plain operator language.
- **A5 closer:** Julie's source closes *"The AI era did not invent this discipline. It made the cost of skipping it catastrophically visible."* The substance is load-bearing — preserve. The cadence ("X did not invent Y. It made Z…") is mildly AI-tell antithesis. Acceptable single instance; charter §4 allows one per chapter. Verify no other "Not X. Y." cadence is in the same section.
- **Framework-attribution rule:** Applies. The outcome-first/design-second/tool-third discipline is joint IP. No "Julie's twenty years" framing.

**Anti-pattern risk:**
- A3 (triplet) — the four-clause enumeration. Collapse.
- A5 (AI smell) — closer cadence as noted; one instance allowed.
- A13 (means/ends) — moderate. Per §5 special check.
- A4 (boastful biographical) — would be triggered by "twenty years of engagements"; avoided by reframing in blended-we.
- A2 (coined vocab before stakes) — guard against introducing "Co-Operating Model" or "design discipline" capitalized here. Plain language.

**Framework-attribution rule:** Applies directly.

**Coherence:**
- Lands between L87 (task-orientation paragraph closing on *"the gains stay small, the wins stay scattered, and nothing changes structurally"*) and L89 (the existing goal-orientation paragraph). E14 is the bridge: name the discipline that *enables* the goal-orientation reveal.
- L89's existing close at *"Goal-orientation produces results because the design was built to produce them"* — verify it still reads correctly after E14 lands directly above. The bridge should set up the L89 close, not duplicate it.
- L91–L95 callout-tip ("If your AI initiative starts with 'what tasks can AI do?'…") is the section's CTA. Preserve.
- The Excalidraw at L97 (`ch01-wrong-vs-right-question`) is the visual. No change.

---

### E15 (NEW-SECTION, LAND-WITH-MODIFICATION) — scorecard intro with discipline-split attribution

**Substance to preserve (from `_julie/julie-redline.md:445–456`):**
- The five dimensions were developed from both directions: technical systems experience + organizational design experience.
- Jesse-aligned dimensions: Information Readiness, Workflow Visibility (technical preconditions for whether an AI agent can do the work).
- Julie-aligned dimensions: Constraint Clarity, Decision Rights, Measurement Discipline (org-design preconditions for whether the organization will accept and hold the change).
- The dual-readiness claim: a company can be technically ready and organizationally unready; it can be organizationally aligned and technically unprepared; both halves must be green for a sprint to succeed.

**Modification from Julie's instruction:**
- **Author flag: "Requires review."** This row carries explicit author-review flag from the manifest. Per scout.md §5 done-test, this row gets **NEEDS-AUTHOR escalation in the recommended bead order** — execute last, after E08–E14 have landed and the chapter voice has accreted. The author then makes the final call on whether the IP-split framing lands.
- **Framework-attribution rule — DIRECT APPLICATION:** The scorecard itself is joint IP. The five dimensions are joint IP. Attributing dimensions to *which discipline informed them* is fine as **origin-credit prose**, but framing as *"Jesse owns these / Julie owns those"* is over-attribution. Direction: describe the *informed-by* relationship without IP-claim language. The scorecard belongs to the book, not to either author individually.
- **MEANS/ENDS-RISK check (per §5 special check):** This is the **opener of the scorecard section** (currently L99–L107). The scorecard is means (diagnostic instrument), not end (the goal is headcount math working / no AI returns / operator outcomes). Acceptance criterion: lead with the operator outcome the scorecard helps reveal (where you actually stand → ability to start where the leverage is), not with the scorecard-as-thing. The current L101 already does this *"Before you move forward, you need to know where you actually stand."* — preserve that operator-direct opener. E15 lands AFTER L107 (the "a 'constraint' just means the one operational bottleneck" paragraph) and BEFORE L109 (Dimension 1 heading).
- **A3 triplet:** Julie's source enumerates three org-design dimensions in a row (*"Constraint Clarity, Decision Rights, and Measurement Discipline"*) and two technical dimensions (*"Information Readiness and Workflow Visibility"*). These are the actual dimension names — they're operative enumeration, not constructed cadence. Preserve, but don't add additional parallel clauses around them.
- **A1 risk:** Guard against *"Constraint Clarity is the org-design dimension that…"* abstract-noun-equals-abstract-noun definitional cadence. The five dimensions get their own definitions later in §1.4 (each as a `### Dimension N` heading); E15 should *not* re-define them here. E15 only frames the origin / which discipline informed which.
- **A2 (coined term before stakes):** Don't introduce "Co-Operating Model" or other framework vocabulary in E15. The scorecard is the operative artifact; coined book vocabulary lives downstream.
- **A5 closer:** Julie's source closes *"Both halves of the scorecard have to be green for a sprint to succeed."* This is fine substance; sprint is canonical book vocab. But "have to be green for a sprint to succeed" is mildly AI-tell-adjacent. Verify cadence on land.

**Anti-pattern risk (highest):**
- A1 (abstract-noun-equals-abstract-noun) — dimension definitions are the trap.
- A13 (means/ends) — per §5 special check.
- A3 (parallel cadence around the dimension enumeration).
- A4 (boastful biographical) — guard against "Jesse's technical systems experience" and "Julie's organizational design experience" reading as credentialing. The Preface already established credentials.
- Framework-attribution over-application — biggest risk.

**Framework-attribution rule:** **Applies directly.** Most acute application in Ch 1. The five-dimension scorecard is joint IP. Origin credit is fine; ownership claim is not.

**Coherence:**
- Lands AFTER L107 (the "a 'constraint' just means…" paragraph) and BEFORE L109 (`### Dimension 1: Constraint Clarity`).
- The five `### Dimension N` subsections (L109–L203) are sourced and protected. E15 does not touch them.
- The Meridian scorecard at L227–245 is sourced and protected. E15 does not touch it.
- L223–L225 paragraph *"All Green: You don't need the rest of this chapter. Skip to Chapter 4 and run the Sprint."* — verify still reads after E15 lands above. Likely fine.

---

## Conflicts and risks

### Conflict 1: E13 framework-attribution rule vs. Julie's redline

**Source:** `_julie/julie-redline.md:381–392` (Julie's redline phrasing) vs. `_julie/edit-manifest.md:57` (framework-attribution rule global)

**Description:** Julie's redline at L381–392 inserts *"Julie asks of every leadership team she advises"* into the three-questions accountability-chart check. The three-questions framework is a generic org-design diagnostic, joint IP, framework component. Per the manifest's global rule (line 57), framework components do not get individual author attribution.

**Resolution:** Reject the literal attribution rewrite. Lands as effectively-SKIP at L71 (keep existing phrasing). Julie's CHRO voice is established upstream via E09 + E11 + E12. No author decision needed; rule is canon.

### Conflict 2: E15 author-flag "Requires review"

**Source:** `_julie/edit-manifest.md` Ch 1 JF-Note column for E15

**Description:** E15 carries explicit "Requires review" from the author. The scorecard dimension-split framing is the most likely place a framework-attribution scrub could either land cleanly or trip over the joint-IP rule. Author wants to see the prose before the bead executes.

**Resolution:** Execute E15 last in the recommended bead order. Drafter produces the prose under the acceptance criteria above (origin-credit framing, not IP-claim framing). Then author reviews the diff. If author rejects the framing, bead is escalated to Path B (Design Table) for a second pass; if author approves, ship.

### Conflict 3: Forbidden vocab "transformations" in E12

**Source:** `_julie/voice-charter.md` §3 (Forbidden: *transformation, transformative, transform — audience-exhausted*); Julie's source at lines 352–361 uses the word.

**Description:** Julie's E12 source explicitly uses "transformation initiative" twice. Auto-reject per charter.

**Resolution:** Reframe as "operating-model change" / "restructuring" / "integration." No author decision needed; charter is canon.

### Conflict 4: Pre-existing A3 anti-pattern at L81

**Source:** `chapters/01-diagnosis.qmd:81` *"The pattern is mechanical. The diagnosis is mechanical. The fix is mechanical."* — flagged in voice-charter §1 Pillar 4 as auto-reject AI cadence.

**Description:** The triplet sits in our current manuscript. Opportunistic cleanup during E12 (which lands in §1.2, same section as L81). Drafter has authority per charter §5.

**Resolution:** Preserve principle (pattern is mechanical, not philosophical); cut triplet to single declarative or two-clause sentence. No author decision needed.

### Conflict 5: MEANS/ENDS-RISK on three rows

**Source:** scout.md §5 special check; voice-charter A13 (added after Preface trial)

**Description:** Three rows in this chapter touch paragraphs that frame the system/framework/discipline as the destination:
- **E11**: must lead with operator outcome (headcount math working at scale, smaller proportional team) and name redesign as means.
- **E14**: must lead with operator outcome (cost of skipping the discipline made visible; the math working) and name outcome-first design as means.
- **E15**: must lead with operator outcome (knowing where you stand → leverage point for sprint) and name scorecard as means.

Each row's per-row acceptance criteria above include the explicit MEANS/ENDS-RISK check. Drafter must satisfy.

**Resolution:** Encode as acceptance criteria. No author decision needed unless Drafter fails the check twice; then escalate to Path B.

### Conflict 6: Ch 1 EOS-lean caution (author overall note)

**Source:** Author manifest note for Ch 1: *"we want to make sure we aren't too EOS focused — it's not our IP."*

**Description:** Current chapter has the EOS shape at L27 (discovery-call client runs EOS), L69 (operators who run on EOS, Scaling Up, or any disciplined system), L235 (Meridian Manufacturing runs EOS). These are existing references; E12 must not amplify EOS framing further, and E09's "20-year pattern" examples must not lean on EOS specifically. Plain operator language preferred.

**Resolution:** Encode as Drafter constraint in E09 and E12 acceptance criteria above. The existing EOS references in the chapter (L27, L69, L235) are preserved as-is — they're context, not framework promotion.

### No git-log polish collisions

- `7709ea8` (2026-05-18, "Author review round 2") softened Ch 1 culture/training dismissal, threaded Meridian intro, and converted ASCII to tables. E08–E15 do not touch any of those passages directly.
- `d7ac7bb` (2026-05-17, "Ch01: 14 fixes") is the polish baseline. Its substantive edits land outside E08–E15's targets.
- The Meridian scorecard at L227–245 is sourced and protected. E15 does NOT touch it.
- The L9 opening line and L227–245 Meridian scorecard are the chapter's load-bearing sourced passages. E08 modifies L9 (per acceptance criteria above) by tightening — not by replacing. E15 does not enter the Meridian scorecard section.

---

## Recommended bead order

Execute in this order. Dependencies in parentheses.

1. **E08** (LAND-WITH-MODIFICATION, Path A — Voice Shifter solo)
   - I→we across L9–L17
   - Tighten L9 opening line per risk-map direction
   - Establish blended-we voice for chapter
   - *Why first:* Sets the voice all downstream rows write into. Zero dependency.

2. **E09** (LAND-WITH-MODIFICATION, Path A — Drafter solo)
   - New paragraph after L17, before L19
   - Julie's 20-year-pattern observation in blended-we
   - Collapse triplet; cut "transformation"; respect EOS-lean caution
   - *Dependency:* E08 must land first (blended-we voice established).

3. **E10 + E11** (LAND-WITH-MODIFICATION, Path A — Drafter solo, **single bead**)
   - L49 attribution wrapper in-prose for Jesse's 13→8
   - New paragraph after L49 for Julie's parallel global HR redesign
   - MEANS/ENDS-RISK check on E11 closer
   - *Why paired:* The rhetorical move is the pairing. Splitting strands the parallel.
   - *Dependency:* E08, E09.

4. **E12** (LAND-WITH-MODIFICATION, Path A — Drafter solo)
   - New paragraph after L65, before L67
   - Thirty years of operating-model failures (substance) — without "transformation," without EOS-lean, without triplet
   - **Opportunistic A3 cleanup at L81** in same pass
   - *Dependency:* E08, E09. (Lands inside §1.2; coherence with E09 matters — both extend the diagnosis backward in time.)

5. **E13** (LAND-WITH-MODIFICATION → effectively SKIP at L71, Path A — Voice Shifter solo)
   - Verify L71 reads cleanly in blended-we after E09, E11, E12 land
   - Reject Julie's literal attribution change; preserve existing phrasing
   - *Dependency:* E09, E11, E12 (Julie's CHRO frame established upstream).

6. **E14** (LAND-WITH-MODIFICATION, Path A — Drafter solo)
   - New paragraph between L87 and L89
   - Outcome-first / design-second / tool-third discipline in blended-we
   - MEANS/ENDS-RISK check on the bridge
   - *Dependency:* E08, E09 (chapter voice + Julie's CHRO frame established).

7. **E15** (LAND-WITH-MODIFICATION, Path A — Drafter solo; **author-review flag**)
   - New paragraph between L107 and L109
   - Scorecard origin-credit framing (which discipline informed which dimensions); not IP-claim framing
   - MEANS/ENDS-RISK check on scorecard-as-means
   - **Author reviews diff before ship.** If author rejects framing, escalate to Path B.
   - *Dependency:* All prior beads (sets the full voice + dual-author rhythm before the scorecard origin paragraph lands).

**Path A beads:** All seven beads (E08, E09, E10+E11, E12, E13, E14, E15). Default to solo Drafter per AGENT-TEAM §1 lessons-learned default.

**Path B candidates if any bead fails voice-gate twice:** E11 (MEANS/ENDS-RISK + dual-triplet), E15 (framework-attribution + author flag). All other rows are mechanical enough that solo Drafter should land them.

**Critical sequencing constraint:** The Preface E01+E02 bead must have landed first (it cascades the blended-we + no-inline-tag convention to Ch 1). Per the Preface plan, that is already executed (commit `bcf8f11`). Ch 1 inherits the convention.

---

## Skip / needs-author rationale

### E13 — effectively SKIP at literal target

The literal attribution change Julie proposes at L71 (*"Julie asks of every leadership team she advises"*) violates the framework-attribution rule. The three-questions accountability check is generic org-design diagnostic discipline, joint IP.

**Resolution:** Keep existing L71 phrasing. The attribution work happens upstream via E09 + E11 + E12 establishing Julie's CHRO voice. No literal edit at L71.

**This is not a NEEDS-AUTHOR row** — the framework-attribution rule is canon (manifest §line 57); rejection is mechanical.

### E15 — soft NEEDS-AUTHOR review flag (carried from manifest)

Author manifest flag *"Requires review"* on E15. Execute last; author reviews the resulting diff.

**One-question prompt for author after E15 lands:**

> The scorecard intro now lands the five dimensions as "developed from both directions — Information Readiness and Workflow Visibility from the technical preconditions Jesse's work surfaces, Constraint Clarity, Decision Rights, and Measurement Discipline from the org-design preconditions Julie's work surfaces" (or similar non-IP-claim phrasing). Does that origin-credit framing land, or does any dimension attribution feel like an ownership claim?

If author rejects, escalate to Path B (Design Table) for a single Substance/Voice/Reader convergence pass on E15.

---

## Done test status

- [x] Every in-scope E-row (E08–E15) classified: 8 LAND-WITH-MODIFICATION (one effectively SKIP at literal target — E13; one with soft author-review flag — E15)
- [x] Every LAND/LAND-WITH-MODIFICATION row has tightened current-chapter line ranges (L9–L17, L17, L49, L49, L65, L71, L87, L107)
- [x] Every LAND row has 2–4 bullet acceptance criteria covering substance, anti-patterns, framework-attribution rule applicability, coherence
- [x] **MEANS/ENDS-RISK check applied per scout.md §5 on opener/closer/system-framing paragraphs:** E11 closer, E14 bridge, E15 scorecard opener — all three checked with explicit acceptance criteria
- [x] Conflicts flagged with specific source references (manifest §57, charter §3, charter §4 A13, charter §1 Pillar 4 at L81, scout.md §5)
- [x] Bead execution order recommended with dependencies cited
- [x] Pre-existing voice debt (L81 A3 triplet) flagged for opportunistic cleanup
- [x] EOS-lean caution from author note encoded as Drafter constraint
- [x] Plan file at `_julie/per-chapter/01-diagnosis.md`

**Outstanding author asks for Human Orchestrator:**

1. **E15 review after draft.** Origin-credit vs. IP-claim framing on the scorecard dimension split. Execute, then review diff. (Soft flag; not blocking the bead from running.)

No blocking decisions. E08–E14 dispatch under their current verdicts. E15 dispatches with author-review-on-diff.

---

## Author decisions (logged after dispatch)

*(To be filled in as author reviews each bead diff during execution.)*

- **E08:** _pending_
- **E09:** _pending_
- **E10+E11:** _pending_
- **E12:** _pending_
- **E13:** _pending_ (recommendation: confirm SKIP at L71)
- **E14:** _pending_
- **E15:** _pending_ (author-review flag carried from manifest)

---

*End of plan.*
