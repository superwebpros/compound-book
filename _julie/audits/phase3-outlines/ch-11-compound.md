# Phase 3A Outline — Ch 11 (Compound)

**Source file:** `chapters/09-compound.qmd` · **Priority:** 3C #8 · **Drafter model:** Sonnet
**Proposed title:** *"Compound: Turn the Sprint Into Infrastructure"*
**Beads:** `book-o81e` (FLOW#5 trim three-beat outros, artifact dumps, In-Brief/reflection over-caps), `book-bco3` (FLOW#4 Headcount callback only — Diagnosis owns the definition), `book-tb8h` (ARC#1 cross-refs — handled 3B), `book-ultm` (ARC#2 — handled 3B), `book-b8yy` (FLOW#3 Meridian — already strong, no change), HBR citation discipline (no HBR here, OK).
**Status:** Light-to-medium restructure. Chapter content is strong; the work is collapsing three competing outros into one, converting the Headcount Paradox redefinition at L184 into a callback, and surfacing the 90-min time-budget strip to the author. Most prose survives intact. This outline carries the upgraded format ([[chapter-syllogism-and-flow-markers]]) so the Drafter anchors sentence-to-sentence decisions in the chapter's argument structure.

---

## Chapter syllogism

- **Premise 1.** The Sprint shipped — Deliver produced a working, deployed system measured against the constraint named in Source.
- **Premise 2.** Compound is the discipline that turns one Sprint into the foundation of the next: a retrospective on the design (not the people), one committed design change, a re-rank of the Signal Backlog against what the Sprint actually taught you, and three living documents updated before the room empties.
- **Premise 3.** Infrastructure compounds. The next Sprint inherits everything this one built — agents that learned conventions, Source maps already drawn, HAC rows already permanent, Build Spec Writers that know the formats. Sprint 7 doesn't start where Sprint 1 started.
- **Conclusion.** The reader has the discipline to run a Compound session that produces three updated documents (HAC, Signal Backlog, Sprint Outcome Record), one installed design change, and a named next constraint — so the next Sprint inherits the work this one did instead of rebuilding it.

---

## Chapter content outline (proposed)

> **Legend:** [NEW] = added · [CUT] = removed · [MOVE] = relocated · [TRIM] = shortened · [KEEP] = unchanged · *(L#)* = current line in `09-compound.qmd`

### I. In-Brief callout *(L3-6)* [KEEP]

- **Assumes:** reader has finished Ch 10 (Deliver). The Sprint shipped; a working system is in production against the named constraint.
- **Establishes:** Compound is a discrete stage that runs in a single session and produces named outputs (Retrospective + re-rank + one design change + next constraint).
- **Sets up:** the opening story, which shows what compounding produces over multiple Sprints.

- A. Single-paragraph framing: Sprint Retrospective + re-rank + one design change + name the next constraint.
- B. Closing claim: *"The Sprint that skips this stage shipped a project. The Sprint that runs it built infrastructure."*

### II. Opening hook — the 5:30 done story *(L8-30)* [KEEP, light edit only]

- **Assumes:** reader knows what Deliver produced (a working system). They don't yet know what running this on a cadence feels like.
- **Establishes:** the multi-Sprint payoff is structural, not heroic — the reason the laptop closes at 5:30 is infrastructure doing work in parallel, accumulated Sprint over Sprint. Names Compound as the sixth stage of the Sequence and the origin of the company name.
- **Sets up:** the question of how a single Compound session produces that accumulation. (Answer: the three deliverables in §IV.)
- A. **Story / opening claim** *(L8-18)*
    - 1. The compulsive-worker self-portrait; "done" used to mean "out of energy."
    - 2. The 5:30 clock-check. The list is empty. Close the laptop. Family dinner.
    - 3. It happens the next night. And the night after that.
- B. **The eighteen-months-before vs six-months-after delta** *(L22-24)* [KEEP verbatim]
    - 1. Same work, same industry, same speed.
    - 2. What changed: infrastructure doing work in parallel. Each Sprint built on the last.
    - 3. Agents learned conventions in earlier Sprints; tools knew the formats; Source maps from Sprint 1 accelerated Sprint 5.
    - 4. *"I could stop because it ran."*
- C. **Bridge to Compound the stage** *(L26-30)*
    - 1. Every successful business runs on a quarterly rhythm (EOS, Scaling Up, 4DX).
    - 2. Compound is the same beat for the AI operating layer.
    - 3. The retrospective looks at the design, not the people.
    - 4. Compound is the sixth stage of the Sequence. Running the Sequence on a cadence makes the work compound. That is where the company name comes from.

### III. Canvas connection *(L32)* [KEEP]

- **Assumes:** reader has the Sprint Planning Canvas in mind from prior chapters.
- **Establishes:** this chapter fills the Compound row of the Sequence first-pass.
- **Sets up:** the named deliverables that get logged on the Canvas.

- A. One-sentence bridge: this chapter fills in the Compound row of the Sequence first-pass on the Sprint Planning Canvas.

### IV. Concept: What Compound produces — three deliverables *(L34-53)* [KEEP]

  **Heading (proposed, directive):** "Compound Produces Three Deliverables. Don't Skip Any."

- **Assumes:** reader believes Compound is a discrete stage with named outputs (from §I and §II).
- **Establishes:** the three deliverables a Compound session must produce before the team closes the laptop — updated Signal Backlog, updated HAC, Sprint Outcome Record. Names that these are slices of the Hybrid Org Today, so they aren't optional reporting; they're the institutional memory the next Sprint reads.
- **Sets up:** the two instruments that produce those deliverables — the Sprint Retrospective (§V/§VI) and the Constraint Re-rank (§VIII) — and the one rule that gates them (one design change, §VII).

- A. **The three deliverables** *(L36-42)* — produced in a single session before the team closes the laptop.
    - 1. **Updated *Signal Backlog*** — re-ranked against what the Sprint taught you.
    - 2. **Updated *Hybrid Accountability Chart*** — entries made permanent; neighboring rows reviewed for second-order effects.
    - 3. **Sprint Outcome Record** — one sentence capturing the constraint, the before-and-after cost, the specific result. First row of the Compounding Scorecard.
- B. **Artifact:** Excalidraw `ch09-compound-deliverables` *(L44)* [KEEP].
- C. **How the three slot into the Hybrid Org Today** *(L46-48)*
    - 1. Signal Backlog and HAC are slices of the Hybrid Org Today (next chapter).
    - 2. If a Sprint ends without the three updates, the Sprint didn't finish.
- D. **Action Step — schedule the Compound session** *(L50-53)* [TRIM time-budget per ARC#9]
    - 1. Put the Compound session on the calendar before Build.
    - 2. Human Orchestrator + every supervisor who owned a Sprint accountability.
    - 3. If it's not scheduled before the Sprint ships, it won't happen after.
    - 4. // AUTHOR REVIEW: Strip the "90-minute block" per ARC#9 / R2 author preference. The 90-min figure is operationally useful but reads as a procedural time-budget. Recommended replacement wording is in the Drafter notes.

### V. Framework: The Sprint Retrospective *(L55-75)* [KEEP, make checklist explicit]

  **Heading (proposed, directive):** "Run the Sprint Retrospective Honestly"

- **Assumes:** reader knows Compound produces three deliverables (from §IV). They don't yet know how to extract the signal that updates those deliverables.
- **Establishes:** the Retrospective is the first of two instruments in Compound. Three questions, same every time, asked of the design (not the people). The follow-up rule *"what would have to be true for this to not happen again?"* forces structural answers. Meridian's three retrospective items show what honest answers look like.
- **Sets up:** §VI (the compounding measurement questions) which asks what the Sprint produced *beyond* the deliverable, and §VII (the one design change rule) which forces the Retrospective signal to converge into a single installable change.

**Why the Retrospective comes before the Re-rank:** the Retrospective surfaces what the Sprint taught you about the constraint *and* about adjacent constraints. The Constraint Re-rank in §VIII consumes that signal. Without a Retrospective first, the Re-rank is reordering the backlog from memory instead of evidence.

- A. **Framing sentence** *(L58)*: first of two instruments in Compound. Same three questions every time.
- B. **The three questions** [in-body checklist artifact — make explicit]
    - 1. **What worked?** *(L60)* — name the mechanism, not the sentiment. Specific design decisions that paid off.
    - 2. **What didn't work?** *(L62)* — handoffs that broke, dirty inputs, skipped supervisor reviews.
        - a. **Follow-up question (verbatim):** *"What would have to be true for this to not happen again?"*
    - 3. **What one design change would make the next Sprint better?** *(L68)* — given its own section below (§VII).
- C. **Worked example — Meridian Manufacturing retrospective** *(L64-66)* [KEEP]
    - 1. **Item 1: Agent complexity matching.** Historical matching pulled comparable jobs ~85% of the time but missed complexity (12 bends + tight tolerances ≠ 4 bends + standard tolerances). Elena was correcting one in eight quotes. Fix: add fabrication complexity indicators.
    - 2. **Item 2: Ty's old email path.** He forwarded three RFQs the old way in week one out of habit. Fix: kill the old email path on day one, not leave it open as a fallback.
    - 3. **Item 3: Specialty alloys.** Every Inconel or titanium job still routed to Elena because the materials database didn't cover specialty alloys. Fix: add the five most common non-standard materials before Sprint 2.
- D. **Who runs it** *(L70)*: Human Orchestrator + supervisors who owned Sprint accountabilities. Room has to be safe enough for honest answers.
- E. **Pro Tip** *(L72-75)* [KEEP]: If your retrospective produces zero "what didn't work" items, you didn't run it honestly.

### VI. Concept: The compounding measurement — three additional questions *(L77-87)* [KEEP, make checklist explicit]

  **Heading (proposed, directive):** "Measure What Compounded Beyond the Sprint Outcome"

- **Assumes:** reader has run a Retrospective and knows what worked, what didn't, and the candidate design change.
- **Establishes:** the Sprint outcome (delivered in Deliver) is *not* the same as what compounded. Three additional questions measure the compounding effect: what the organization knows now, what capability now exists, and what the next Sprint starts with that this one didn't. If the answers are thin, the Sprint produced output but didn't compound.
- **Sets up:** the one design change rule in §VII — the change is the lever that makes "what the next Sprint starts with" materially different from "what this Sprint started with."

- A. **Framing sentence** *(L79)*: Beyond the Sprint outcome measured in Deliver, Compound asks three more questions. The answers are the compound interest.
- B. **The three questions** [in-body checklist artifact — make explicit]
    - 1. **What does the organization know now that it didn't know before?** *(L81)*
        - a. Meridian example: Elena's 147-row Customer Notes spreadsheet contained only 112 validated rules. Thirty-five were duplicates or outdated. They learned which quote types the agent handles cleanly (~70% standard volume) and which still need Elena's review.
    - 2. **What capability exists now that didn't exist before?** *(L83)*
        - a. Meridian example: working quoting agent team. Standard quote turnaround 3.8 days → 4.2 hours. Elena 15 hrs/wk → 5. Throughput doubled. $47K new revenue in month one.
    - 3. **What is the next Sprint starting with that the first Sprint didn't have?** *(L85)*
        - a. Meridian example: three trained agents, 112 validated pricing rules, three years of indexed ERP job data, a sales team using the new intake workflow.
- C. **Closing claim** *(L87)*: If you can't answer these three, the Sprint delivered output but didn't compound. Projects rebuild each time. Infrastructure accumulates.

### VII. Framework: The one design change rule *(L89-112)* [KEEP]

  **Heading (proposed, directive):** "Install One Design Change. Just One."

- **Assumes:** reader has Retrospective signal + compounding measurement answers in hand. They have more candidate changes than they can install.
- **Establishes:** the rule — one committed structural change, installed before the next Sprint begins, with a 4-field card (What / Who / How you'll know / By date). The failure mode it defeats is the "lessons learned" list that never lands. Meridian's one change (fabrication complexity indicators in the Quote Research Agent) is the worked example, and crucially feeds the §VIII Re-rank as evidence.
- **Sets up:** the Constraint Re-rank in §VIII — once the design change is named, the question becomes whether the next Sprint should attack the same constraint or a different one.

- A. **The rule** *(L91-93)*: One committed design change, installed before the next Sprint begins.
- B. **The failure mode it defeats** *(L95-97)*
    - 1. The temptation: list every observation, call it "lessons learned."
    - 2. The list never lands — too long to install, too vague to enforce.
    - 3. Compound is finished when that one design change is installed.
    - 4. The change has to be structural: chart entry revised, workflow step added, guardrail tightened, Source map updated. An insight that doesn't change the design isn't worth recording.
- C. **How the Human Orchestrator chooses** *(L99)*: look across everything the Sprint surfaced; name the *single* change that will most improve the next Sprint.
- D. **Worked example — Meridian's one design change** *(L101-103)* [KEEP]
    - 1. The change: add fabrication complexity indicators (bend count, tolerance class, weld count, surface finish) as matching criteria in the Quote Research Agent.
    - 2. Who installs: Dave Kowalski provides the classification framework from 31 years of fabrication experience; the agent uses it when selecting historical matches.
    - 3. How you'll know: re-run the eight quotes from the previous month where Elena corrected the agent's match; at least seven of eight produce the correct comparable.
    - 4. By date: installed before Sprint 2 kickoff.
- E. **Artifact:** Excalidraw `ch09-one-design-change` *(L105)* [KEEP].
- F. **Why one is the right number** *(L107)*: One design change per Sprint is small. Eight Sprints of one good design change each is substantial. Skip the discipline and you get the same agent team you always had.
- G. **Action Step — the four-field card** *(L109-112)* [KEEP] — in-body fillable template (artifact)
    - 1. **What** the change is.
    - 2. **Who** installs it.
    - 3. **How you'll know** it's working.
    - 4. **By date** it's installed by.
    - 5. If any field is blank, the change isn't specific enough.

### VIII. Framework: Constraint Re-rank *(L114-133)* [KEEP, make checklist explicit]

  **Heading (proposed, directive):** "Re-Rank the Signal Backlog on What the Sprint Taught You"

- **Assumes:** reader has Retrospective output (§V/§VI) and a named design change (§VII). They have evidence the original Signal Backlog ranking is now out of date.
- **Establishes:** the Re-rank is the second instrument in Compound. Four questions force the backlog to reflect what the Sprint surfaced — new information on other constraints, side-effect resolution, brand-new constraints, and the next pick. Meridian's Sprint 2 setup (HubSpot-to-JobBOSS rises to rank one, scheduling falls, customer pricing standardization enters at rank two) is the worked example.
- **Sets up:** §IX (three living documents updated before the room empties) — the Re-rank produces the new Signal Backlog ordering, which is one of the three documents to update.

**Why the Re-rank comes after the Retrospective:** it consumes Retrospective signal as input. If the Re-rank ran first, it would be reordering on intuition. Running it last means the backlog reflects evidence the team just generated together.

- A. **Framing sentence** *(L116)*: Second instrument in Compound. The Sprint produced new information; reorder the backlog against it.
- B. **The four questions** *(L118-126)* [in-body checklist artifact — make explicit]
    - 1. **Did the Sprint reveal new information about any of the other constraints?** *(L120)*
    - 2. **Did any constraints get partially resolved as a side effect of this Sprint?** *(L122)*
    - 3. **Did any new constraints surface during the Sprint that weren't on the original list?** *(L124)*
    - 4. **Given what you now know, which constraint should the next Sprint solve?** *(L126)*
- C. **Worked example — Meridian Sprint 2 setup** *(L120-126)* [KEEP]
    - 1. Q1: HubSpot-to-JobBOSS data sync exposed — Ty entering the same data twice. Previously ranked third, jumps to first.
    - 2. Q2: Production scheduling partially resolved as side effect; moves from second to fourth.
    - 3. Q3: Customer pricing standardization for the three accounts at 40% of quote volume — wasn't on the backlog, enters at rank two.
    - 4. Q4: Top constraint = HubSpot-to-JobBOSS data sync. Mark assigns Elena as Human Orchestrator. Sprint 2 kicks off at next quarterly planning.
- D. **Pro Tip** *(L128-131)* [KEEP]: If you're picking the same constraint for Sprint 2 that you picked for Sprint 1, the Sprint didn't deliver.
- E. **Closing instruction** *(L133)*: Pull the Signal Backlog. Re-rank using the four questions. Name the top constraint. Assign the next Human Orchestrator. Write both down before leaving the room.

### IX. Concept: Three living documents to update *(L135-150)* [KEEP]

  **Heading (proposed, directive):** "Update the Three Living Documents Before the Room Empties"

- **Assumes:** reader has Retrospective output, a named design change, and a re-ranked backlog. The session has produced everything it needs.
- **Establishes:** the three documents (HAC, Signal Backlog, Sprint Outcome Record) get updated before anyone leaves the room. Fifteen minutes. The Meridian update is the concrete: quoting row becomes permanent at AI-Assisted, Carlos's scheduling row flagged for review, backlog reordered, outcome filed.
- **Sets up:** §X — why these updates matter beyond housekeeping: they are what the next Sprint reads as its starting context.

- A. **Framing sentence** *(L137)*: These three artifacts get updated at the end of every Compound session. They are the institutional memory that makes compounding possible.
- B. **The three updates** *(L139-143)*
    - 1. **Hybrid Accountability Chart** — temporary Sprint entries become permanent (Meridian's quoting row: three agents, Elena confirmed at AI-Assisted level); neighboring rows reviewed (Carlos's scheduling entry flagged because faster quoting was outpacing scheduling).
    - 2. **Signal Backlog** — re-ranked per the Constraint Re-rank (HubSpot-to-JobBOSS at top; customer pricing standardization at two; specialty materials at three).
    - 3. **Sprint Outcome Record** — one-sentence outcome filed (*"Standard quote turnaround reduced from 3.8 days to 4.2 hours. Elena's quoting time from 15 hrs/wk to 5. Throughput doubled. $47K new revenue in month one."*).
- C. **Closing claim** *(L145)*: Fifteen minutes. Without them, you run the same discovery phase from scratch every quarter.
- D. **Action Step** *(L147-150)* [KEEP]: Update all three before anyone leaves the room. Fifteen minutes. No exceptions.

### X. Concept: Infrastructure compounds *(L152-178)* [KEEP]

  **Heading (proposed, directive):** "Infrastructure Compounds. Each Sprint Inherits the Last."

- **Assumes:** reader has the mechanics of a single Compound session (from §IV-§IX). They understand a session produces three updated documents and a named next constraint.
- **Establishes:** the structural payoff — across many Sprints, the artifacts accumulate and the friction per Sprint goes down. Sprint 7 starts where Sprint 1 finished, not from zero. The 45-minute Source session story is the worked example of inherited infrastructure.
- **Sets up:** §XI — if Compound makes each Sprint cheaper than the last, that's what bends the headcount slope Chapter 1 named.

- A. **The structural payoff** *(L154-156)*: This work gets cheaper and better with each Sprint. The artifacts the Sequence produces are permanent, and they accumulate.
- B. **What carries forward across Sprints** *(L158-160)*
    - 1. Sprint 1's Knowledge Map (three weeks of mapping) → Sprint 6 inherits it; Source becomes three days, mostly updating the edges.
    - 2. HAC has one row after Sprint 1, a dozen after Sprint 12 — each Sprint inherits the chart as context.
    - 3. Build Spec Writer learned conventions in Sprint 1, applies them automatically in Sprint 2.
    - 4. Training material from Sprint 3's Deliver becomes onboarding for Sprint 7.
- C. **Artifact:** Excalidraw `ch09-compounding-loop` *(L162)* [KEEP].
- D. **What Sprint 7 feels like vs. Sprint 1** *(L164)*: sharper constraints, afternoon-sized HAC drafts, days-not-weeks Source.
- E. **Story — the 45-minute Source session** *(L166-176)* [KEEP H3 sub-section]
    - 1. Client video call. Map where their information lives.
    - 2. People talk over each other; problems get added mid-session; nobody in the room writes a word.
    - 3. Forty-five minutes later, the document is complete. Attendees, problem inventory, knowledge inventory, current tools, connected data sources, key themes.
    - 4. Client response: *"This is great. I spent zero time creating it."*
    - 5. That document is still inside their company. Next Sprint's Source phase starts from that map, not from zero.
- F. **The coordinator knowledge base callback** *(L178)*: Same mechanism Design described. The numbers in the next chapter (13 people to 8; double-digit growth on billings and profitability) didn't come from a single Sprint. They came from the stack of infrastructure each Sprint left behind.

### XI. Concept: Compound bends the Headcount slope *(L180-186)* [TIGHTEN — FLOW#4 + FLOW#5]

  **Heading (proposed, directive):** "Compound Bends the Headcount Slope" *(was "Compound is not the same as scale")*

- **Assumes:** reader has read Ch 1 (Headcount Paradox is defined and owned there) and knows Compound makes each Sprint cheaper than the last (from §X).
- **Establishes:** scale and Compound are not the same — scale sells quantity of the same thing; Compound makes the next unit cheaper and more strategic. One callback sentence, not a redefinition, connects the slope to the Headcount Paradox.
- **Sets up:** §XII (the unit-of-work close) by handing the reader the structural reason this discipline is worth running.

- A. **The scale-vs-Compound distinction** *(L182)* [KEEP, ~1 line]
    - 1. Every vendor uses "scale" to sell more of the same thing. Quantity claim, no architecture.
- B. **What Compound does that scale doesn't** *(L184)* [TRIM — keep cost/return mechanics, ~2 lines]
    - 1. Friction per Sprint decreases (Source on existing maps; Build on validated conventions; Deliver inheriting training material).
    - 2. Return per Sprint increases as constraints get more strategic.
- C. **Headcount Paradox callback — FLOW#4** *(L184 currently redefines; convert to callback only)* [TIGHTEN]
    - 1. **Proposed wording:** *"Compound is what bends the slope Chapter 1 named — revenue grows while headcount grows slower. The longer the company runs the Rhythm, the wider that gap gets."*
    - 2. [CUT] The current full restatement of the Headcount Math at L184 (Diagnosis owns the definition).
- D. **Artifact:** Excalidraw `ch09-scale-vs-compound` *(L186)* [KEEP].
- E. **Total section target:** ~4-5 lines, single move (slope-bending). No triple duty.

### XII. Closing beat — One Sprint, one Compound *(L196-200)* [KEEP as single closing beat]

  **Heading (proposed, directive):** "One Sprint Equals One Compound Stage"

- **Assumes:** reader has the mechanics and the structural argument. They need a clean unit-of-work close.
- **Establishes:** the unit — one Sprint, one Compound stage, all named outputs produced. That is a complete pass through the system.
- **Sets up:** Ch 12 (Rhythm) — what happens when this pass runs every quarter, and where the Headcount Math from Ch 1 gets answered.

- A. **The unit-of-work claim** *(L198)*
    - 1. One Sprint → one Compound stage. That is the unit.
    - 2. Sprint Retrospective run, compounding measured, Constraint Re-rank done, one design change installed, backlog re-ranked, chart updated, living documents current, next constraint named, next Human Orchestrator assigned.
    - 3. That is a complete pass through the system.
- B. **Closing handoff to Ch 12 Rhythm** *(L200)* [TIGHTEN]
    - 1. **Proposed wording:** *"One Compound stage proves the mechanism on one Sprint. The next chapter is the Rhythm — what happens when this runs every quarter, and where the Headcount Math from the opening of this book gets answered."*

### XIII. [CUT] "The brand and the stage share a name on purpose" *(L188-194)* [CUT — FLOW#5]

- **Assumes / Establishes / Sets up:** N/A — section is cut. Triad omitted by design per FLOW#5.

- A. **Decision:** Cut entirely. Outro padding. Adds nothing structural.
- B. **Rationale:** Three competing outros at L180/L188/L196. Pick one. Keep "One Sprint, one Compound" (XII). Tighten "Compound is not scale" to a slope-bending move (XI). Cut "brand and stage" (XIII).
- C. // AUTHOR REVIEW: If the author wants to preserve the brand/stage point, the surviving move is a one-sentence parenthetical inside §XII.A: *"(The brand and the stage share a name because the company is the stage.)"* Default is full cut.

### XIV. Reflection Questions *(L202-207)* [KEEP all 4]

- **Assumes:** reader has finished the chapter and has a Sprint to apply this to (or is reading anticipatorily).
- **Establishes:** four reflective prompts mapped 1:1 to the chapter's four instruments — Retrospective, Compounding measurement, One design change, Constraint Re-rank.
- **Sets up:** the team session where the leadership group actually runs Compound. Ch 12 (Rhythm) is the next chapter.

- A. **Q1 — Sprint Retrospective.** Walk the three retrospective questions on a recent AI initiative; for each "didn't work" item, the *"what would have to be true"* follow-up. Design fix or knowledge gap?
- B. **Q2 — Compounding measurement.** Answer the three compounding questions. If you can't answer all three, the Sprint produced output but didn't compound.
- C. **Q3 — One design change.** Write it on a card with the four fields. If any field is blank, the change isn't specific enough.
- D. **Q4 — Constraint Re-rank.** Re-rank the Signal Backlog using the four questions.

---

## Heading inventory — current → proposed (full set)

| Current heading *(L#)* | Proposed directive heading |
|---|---|
| `# *Compound*.` *(L1)* | `# Compound: Turn the Sprint Into Infrastructure` |
| `## What *Compound* produces.` *(L34)* | `## Compound Produces Three Deliverables. Don't Skip Any.` |
| `## The Sprint Retrospective.` *(L55)* | `## Run the Sprint Retrospective Honestly` |
| `### Meridian Manufacturing.` *(L64)* | `### Meridian's Retrospective Surfaced Three Items` |
| `## Measuring what compounded.` *(L77)* | `## Measure What Compounded Beyond the Sprint Outcome` |
| `## The one design change *rule*.` *(L89)* | `## Install One Design Change. Just One.` |
| `## Constraint Re-rank.` *(L114)* | `## Re-Rank the Signal Backlog on What the Sprint Taught You` |
| `## Update the living documents.` *(L135)* | `## Update the Three Living Documents Before the Room Empties` |
| `## Infrastructure *compounds*.` *(L152)* | `## Infrastructure Compounds. Each Sprint Inherits the Last.` |
| `### The 45 minutes that saved weeks.` *(L166)* | `### Forty-Five Minutes That Saved Weeks` |
| `## Compound is not the same as *scale*.` *(L180)* | `## Compound Bends the Headcount Slope` *(tightened — see §XI)* |
| `## The brand and the *stage* share a name on purpose.` *(L188)* | *(CUT — FLOW#5)* |
| `## One Sprint, one *Compound*.` *(L196)* | `## One Sprint Equals One Compound Stage` |
| `## Reflection Questions` *(L202)* | `## Reflection Questions` *(keep)* |

---

## Artifacts (placed in context)

| Artifact | Status | Location in chapter |
|---|---|---|
| Three Compound deliverables | Excalidraw `ch09-compound-deliverables` *(L44)* | Keep at §IV.B. |
| One design change rule | Excalidraw `ch09-one-design-change` *(L105)* | Keep at §VII.E. |
| Compounding loop | Excalidraw `ch09-compounding-loop` *(L162)* | Keep at §X.C. |
| Scale vs. Compound | Excalidraw `ch09-scale-vs-compound` *(L186)* | Keep at §XI.D. |
| **Sprint Retrospective 3-question checklist** | Inline prose *(L58-63)* | **Make explicit as in-body checklist artifact at §V.B.** |
| **Compounding measurement 3-question checklist** | Inline prose *(L79-85)* | **Make explicit as in-body checklist artifact at §VI.B.** |
| **One design change card (4 fields)** | Inline prose *(L111)* | **Add in-body fillable template at §VII.G.** |
| **Constraint Re-rank 4-question checklist** | Inline prose *(L118-126)* | **Make explicit as in-body checklist artifact at §VIII.B.** |
| Compounding Scorecard | Cross-reference only | Lives in Ch 12 Rhythm. Referenced from §IV.A.3 (Sprint Outcome Record is the first row). |

---

## Edit decisions (consolidated)

- **FLOW#5 — Trim three competing outros to one.**
    - **CUT:** "The brand and the stage share a name on purpose" *(L188-194)* — outro padding. (§XIII)
    - **TIGHTEN:** "Compound is not the same as scale" *(L180-186)* → "Compound Bends the Headcount Slope," ~4-5 lines, single move. (§XI)
    - **KEEP as closing:** "One Sprint, one Compound" *(L196-200)* → "One Sprint Equals One Compound Stage." (§XII)
- **FLOW#4 — Headcount Paradox callback only.**
    - L184 currently re-defines the Headcount Math as if introducing it. Convert to a one-sentence callback to Ch 1. Diagnosis owns the definition. (§XI.C)
- **ARC#9 — Strip the 90-minute time-budget.**
    - L52 "A 90-minute block" — borderline (operationally useful but reads as a procedural time-budget). Recommend strip; default replacement wording is in §IV.D.4 and Drafter notes. // AUTHOR REVIEW.
- **ARC#1 — Cross-reference fallout.**
    - "Chapter 11" / "Chapter 10" references handled by `book-tb8h` 3B sweep. Drafter does not re-solve.

---

## HBR citation discipline (this chapter)

**Current count:** Zero HBR citations. No work needed.

---

## Meridian thread (per [[meridian-as-side-by-side-thread]])

Meridian appears at FOUR structural landing points in this chapter. The triads above make each appearance inevitable rather than decorative — every section that *Establishes* a mechanism also points at the Meridian beat that demonstrates it.

1. **§V Retrospective — three retrospective items.** §V's triad establishes "honest answers look like Meridian's three items" (agent complexity matching, Ty's old email path, specialty alloys). The triad's *Establishes* explicitly cites the worked example, so Drafter cannot drop Meridian here without breaking the section's logic.
2. **§VII One design change — fabrication complexity indicators.** §VII's triad names Meridian's change (bend count, tolerance class, weld count, surface finish in the Quote Research Agent) as the worked example *and* as the bridge into §VIII (the change becomes evidence the Re-rank consumes). Pulling Meridian here severs the §VII → §VIII handoff.
3. **§VIII Constraint Re-rank — Sprint 2 setup.** §VIII's triad establishes the Re-rank consumes Retrospective signal, and Meridian's Sprint 2 setup (HubSpot-to-JobBOSS rises to one, scheduling falls, customer pricing standardization enters at two) is the demonstration. The four questions get worked answers, not abstract ones.
4. **§IX Living documents — the three updates with Meridian's row-level concretes.** §IX's triad establishes the documents become the next Sprint's starting context; Meridian's HAC update (Elena AI-Assisted, Carlos's scheduling row flagged), Signal Backlog re-ordering, and one-sentence Sprint Outcome Record are what that looks like in practice.

**Status:** Strong (FLOW#3 — `book-b8yy`). No fix needed at the prose level. Triad audit confirms each Meridian appearance is structurally load-bearing — if Drafter trims any of the four, the surrounding triad's *Establishes* claim no longer has a referent.

---

## Cross-chapter dependencies handled in Phase 3B (Drafter does NOT re-solve)

- Canonical agent definition at first use *(book-ultm)* — handled 3B. The parenthetical at L22 ("AI systems that hold a goal…") survives as-is.
- ARC#1 cross-refs *(book-tb8h)* — "Chapter 11" / "Chapter 10" cross-ref fallout from renumbering swept in 3B.
- Compounding Scorecard cross-ref — template lives in Ch 12 Rhythm. This chapter references it at §IV.A.3 and the handoff at §XII.B.
- SPC through-line — chapter fills in the Compound row of the Sprint Planning Canvas (§III).

---

## Drafter notes

- **Drafter model:** Sonnet.
- ~85-90% of existing prose survives. Largest moves: collapse three competing outros into one (§XI/§XII/§XIII); convert L184 from Headcount Paradox redefinition to a one-sentence callback (§XI.C).
- **Anchoring discipline:** Drafter reads the chapter syllogism + each section's Assumes/Establishes/Sets up triad BEFORE writing. Sentence-to-sentence decisions inside a section must respect the section's flow markers. The retrospective-before-re-rank sequencing in §V/§VIII is structural; the design-change-feeding-the-re-rank handoff in §VII → §VIII is structural; the Meridian beats in §V/§VII/§VIII/§IX are structural per the audit above.
- **90-minute block (L52, ARC#9) — surface to author.** Recommended replacement: *"Schedule the Compound session — Human Orchestrator + every supervisor who owned a Sprint accountability. If it's not scheduled before the Sprint ships, it won't happen after."* Drop the 90-minute number. // AUTHOR REVIEW.
- Run `deflourish.py --apply` after drafting (mandatory per memory — [[deflourish-is-non-negotiable]]; do not skip on EC/orchestrator judgment).
- Voice charter applies. Strip italic-fragment headings. No new em-dashes. No triplet pileups.
- Cross-coherence check: Ch 1 (Headcount Paradox ownership — callback only at §XI.C), Ch 12 (Rhythm handoff at §XII.B, Compounding Scorecard template lives in Ch 12 — referenced from §IV.A.3).
- **Re-read pass:** after structural edits land, Drafter reads end-to-end and checks (a) every pronoun has an antecedent within 3 sentences; (b) every Meridian beat retains its concrete numbers; (c) every chart/Excalidraw sits adjacent to the prose that references it; (d) every Action Step still fits its surrounding section.
- **Author followup items already on the table:**
  - (a) 90-min strip at §IV.D.4 — recommended replacement above.
  - (b) Optional one-sentence "brand and stage" parenthetical at §XII.A vs. full cut at §XIII.C — default is full cut.
