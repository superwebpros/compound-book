# Phase 3A Outline — Ch 7b (Designing the Work)

**Source file:** `chapters/06b-designing-the-work.qmd` · **Priority:** 3C #5 · **Drafter model:** Sonnet
**Proposed title:** *"Designing the Work: Deconstruct, Specify, Prototype, Lock the Gate"*
**Beads:** `book-0fq9` (FLOW#1 lead with practice — promote coordinator story, demote 19-line swim-lane Pro Tip), `book-lbd7` (ARC#8 Design Brief closing Action Step), `book-xqxi` (ARC#3 jargon — handled 3B), HBR citation discipline (Bedard 3-agent ceiling + AWS/Effectual — cross-reference Ch 7, do not re-cite).
**Status:** Medium restructure. Chapter is strong but coordinator opener is buried mid-section; the 19-line swim-lane Pro Tip is structurally outsized; Design Brief lacks closing Action Step. This outline carries the upgraded format ([[chapter-syllogism-and-flow-markers]]) so the Drafter anchors sentence-to-sentence decisions in the chapter's argument structure.

---

## Chapter syllogism

- **Premise 1.** Chapter 7 produced the system design — the Hybrid Accountability Chart, the information flows, the per-agent placeholders. You know who's responsible for what, but not yet what each agent or human actually does at the task level.
- **Premise 2.** Work Deconstruction with TML breaks each accountability into its component tasks and classifies each one: Task (Fully Automatable), Management (AI-Assisted), Leadership (Human Judgment Required). The classification tells you which work an agent can hold and which work stays with the human.
- **Premise 3.** The Design Brief is the single artifact that captures every decision — workflow summary, stakeholders, systems, data, success criteria, guardrails, V1 artifact — plus a six-field mini-spec per agent. The Design Gate is the five-item checklist that proves the brief is complete.
- **Conclusion.** When all five gate items are checked, the reader hands a complete Design Brief to Build. Until then, Build cannot begin.

---

## Chapter content outline (proposed)

> **Legend:** [NEW] = added · [CUT] = removed · [MOVE] = relocated · [TRIM] = shortened · [KEEP] = unchanged · [DEMOTE] = compressed to reference · *(L#)* = current line in `06b-designing-the-work.qmd`

### I. In-Brief callout *(L3-6)* [KEEP]

- **Assumes:** reader has just finished Ch 7 (the system design — HAC, info flows, agent placeholders). They know the architecture but not the task-level work.
- **Establishes:** chapter delivers Work Deconstruction (TML), the Design Brief (with mini-specs), the prototype discipline, and the five-item Design Gate.
- **Sets up:** the coordinator opener as proof that the method works on real roles with real hiring decisions on the table.

Content: keep current. Single paragraph naming the four deliverables.

### II. Opening hook — coordinator role deconstruction *(currently L39-53 — PROMOTE as opener)* [MOVE]

  **Heading (proposed, directive):** "What Coordinator Deconstruction Looks Like in Practice"

- **Assumes:** reader trusts the Ch 7 system design but doesn't yet know how to decompose work at the task level. They have a HAC populated with placeholders, not specifications.
- **Establishes:** Work Deconstruction is the method that turns a placeholder ("project coordinator") into a classified task list. Run on a real role, in real time, with a real hiring decision pending — one row in the chart replaced a $24K hire.
- **Sets up:** the formal framework (§IV). The opener shows the outcome; §IV teaches the method that produced it.

*Triad justification for the PROMOTE:* the coordinator story IS the proof-of-method this chapter argues for. Burying it 30% in means readers hit the framework abstract, before they've seen it work. Promoted, the framework reads as "here's how to reproduce what just happened" instead of "here's a method, trust us."

- A. **Story / opening claim** — the coordinator story from Ch 7 *(L40)*
    - 1. The project coordinator example — run in real time, on a real role, with a pending hiring decision on the table.
    - 2. We listed every accountability she owned on the existing Accountability Chart — not her job description, which was cleaner than reality.
- B. **What the deconstruction surfaced** *(L47)*
    - 1. A substantial fraction of her work was routing and documentation.
    - 2. Scheduling client check-ins, updating the project tracker, generating weekly status reports from CRM data.
    - 3. Looked like operations because it lived inside the operations function — was administration, not judgment.
- C. **The redesign outcome** *(L51-53)* [KEEP]
    - 1. That work became a designed agent team — landed in the HAC as an AI-assisted entry, Elena-style supervision.
    - 2. Remaining accountability stayed with her: relationships, judgment calls, history-dependent decisions.
    - 3. The junior coordinator listing was never posted. **One row in the chart replaced a $24K hire.**
- D. **Bridge sentence into the framework** *(NEW)*
    - 1. That outcome was Work Deconstruction with TML. Here is the method.

### III. Context — where this lands on the Sprint Planning Canvas *(L8-10)* [KEEP]

- **Assumes:** reader saw what Work Deconstruction produces (§II) but doesn't know where it sits in the Sprint structure.
- **Establishes:** this chapter is the second half of the Design row on the Sprint Planning Canvas — the half that locks in the Human Orchestrator.
- **Sets up:** the framework introduction. With the canvas position fixed, the reader can attach what comes next to where it belongs.

Content: one short paragraph. Keep current.

### IV. Framework: Work Deconstruction with TML *(L12-37)* [KEEP, light edit]

  **Heading (proposed, directive):** "Deconstruct the Work Task by Task"

- **Assumes:** reader has seen Work Deconstruction's outcome (§II) and knows where this work lives on the canvas (§III). They need the formal method to reproduce the result on their own roles.
- **Establishes:** the method — pull the actual accountability list, classify each task with the one sorting question, sort into TML (Task / Management / Leadership). TML comes from Source; here it's applied to the work the organization does, not the knowledge it holds.
- **Sets up:** Meridian's quoting workflow (§V) as the worked example. Once the method is named, the next section runs it end-to-end on Meridian.

*Meridian thread structural adjacency:* the framework introduction at §IV.A explicitly names that Source uses TML for knowledge and Design uses TML for work. Meridian's worked example (§V) follows immediately. Concept → worked example sit shoulder to shoulder.

- A. **Concept** *(L14)*
    - 1. Work Deconstruction applies Source's TML lens to the work itself.
    - 2. Source uses TML to categorize what the organization knows; Design uses TML to categorize what the work requires.
- B. **The method** *(L16)*
    - 1. Pull the actual accountability list for a role — not the job description.
    - 2. Go task by task and classify each one.
    - 3. For every task, document *source inputs* (which system, person, document) and *outputs* (where the result goes next).
- C. **The one sorting question** *(L20)*
    - 1. "If I gave a well-briefed agent this task with the right data, would the output need review every time, or only on exceptions?"
- D. **The three TML categories** *(L20)*
    - 1. ***Task*** (Fully Automatable) — only exception review needed; includes pure workflow automation with no agent in the middle.
    - 2. ***Management*** (AI-Assisted) — every output requires review.
    - 3. ***Leadership*** (Human Judgment Required) — answer depends on context, relationship, or judgment without a clear rule.
- E. **Pro Tip — autonomy is earned** *(L22-25)* [KEEP]
    - 1. AI-Assisted is where most things start. Fully Automatable is where they move after the agent proves itself.
- F. **Honest decomposition** *(L27-29)* [KEEP]
    - 1. Most accountabilities have a different shape than the leader assumed.
    - 2. TML doesn't tell you which column is right; it forces you to ask what type of intelligence the work requires.
- G. **Action Step — first classification pass** *(L31-34)* [KEEP]
    - 1. List every task in the constraint workflow. Sort into three TML categories. Count.
    - 2. If more than half land in Leadership, challenge each one: genuine judgment, or judgment because nobody wrote the rules down?
- H. **Handoff into the HAC** *(L36)* [KEEP]
    - 1. Each classified task maps to a chart entry — function, agent team, supervisor, autonomy level.
    - 2. Work Deconstruction is the thinking; the HAC entries make the thinking durable for Build.

### V. Worked example: Meridian quoting workflow *(L55-82)* [KEEP — best in-body artifact]

  **Heading (proposed):** "Meridian's Quoting Workflow, Fully Deconstructed"

- **Assumes:** reader has the TML method (§IV) and has already met Meridian in earlier chapters. They know Elena's quoting bottleneck cost $558K/year.
- **Establishes:** what a complete Work Deconstruction looks like when applied end-to-end. Seven tasks, classified, with source inputs and outputs. Then the HAC entries derived directly from the classification. The role that felt like "Elena's judgment" was 65% data retrieval and document assembly.
- **Sets up:** §VI (legibility / visualization) — now that the reader sees what a classified workflow looks like in a table, the next step is making the design legible as a diagram before Build.

*Meridian thread structural adjacency:* this is the chapter's longest Meridian beat. The 7-task table sits at L59-67, the derived HAC at L73-79. Both are immediately adjacent to §IV's method — concept introduction is followed by the worked artifact, not separated by chapters of intervening text.

- A. **Context** *(L57)*
    - 1. Elena Ruiz, VP of Operations, sole bottleneck for every quote.
    - 2. Fifteen hours a week building quotes from scratch — held customer-specific pricing, material lead-time knowledge, historical job context.
    - 3. Annual bottleneck cost: $558K.
- B. **In-body artifact — Meridian Work Deconstruction (7-task table)** *(L59-67)* [KEEP]
    - 1. Task: Receive RFQ, log in CRM — Task (workflow automation).
    - 2. Task: Pull customer history from HubSpot — Task (Fully Automatable).
    - 3. Task: Look up material pricing in JobBOSS — Task (Fully Automatable).
    - 4. Task: Cross-reference Customer Notes.xlsx for pricing exceptions — Management (AI-Assisted).
    - 5. Task: Calculate final price and assemble quote — Management (AI-Assisted).
    - 6. Task: Review and approve quote — Leadership (Human Judgment Required).
    - 7. Task: Deliver quote to customer — Leadership (Human Judgment Required).
- C. **Task-count read** *(L69)*
    - 1. Leadership: 2. Management: 2. Task: 3.
    - 2. Roughly 65% data retrieval and document assembly — required her access, not her judgment.
- D. **In-body artifact — HAC entries derived from the deconstruction** *(L73-79)* [KEEP]
    - 1. Five rows: RFQ intake, customer data retrieval, material/labor pricing, draft quote generation, quote delivery.
    - 2. Every row has a name. Every agent team has a supervisor. All agent outputs start AI-Assisted.
- E. **Pro Tip — AI-Assisted vs. Automated distinction** *(L83-86)* [KEEP]
    - 1. Difference is the human's role, not review frequency.
    - 2. Start AI-Assisted. Moving toward Automated is a promotion the agent earns.

### VI. Concept: Seeing the design *(L88-99)* [KEEP, light touch]

  **Heading (proposed, directive):** "Make the Design Legible Before You Build It"

- **Assumes:** reader has a classified task list (from §IV-V) but a list isn't the same as a design. They need to see the workflow as a diagram before they can spot its gaps.
- **Establishes:** three visualization choices — swim lanes for information flow, flowcharts for decision logic, visual design tools for stakeholder-facing output. Each fits a specific design question.
- **Sets up:** the Design Brief (§VII) — once the workflow is legible as a diagram, the brief is what captures it (plus everything else) as a single artifact Build can inherit.

*Triad justification for the DEMOTE:* the 19-line "How to draw a swim lane" Pro Tip (L101-119) teaches procedure that already lives in `appendix-diagramming-primer.qmd`. Demoting to a 3-line appendix reference keeps the chapter focused on the conceptual claim (legibility is a precondition) and lets the procedural how-to live where readers go when they need it. The current placement makes a tool tutorial structurally equal to the framework — a fragmentation the rest of the chapter doesn't have.

- A. **Why legibility matters** *(L90)*
    - 1. A good workflow design is legible — trace the path from input to output, see where humans decide and agents execute, spot gaps before Build does.
- B. **Visualization choices** *(L94-98)*
    - 1. **Swim lane diagrams** — for mapping information flows between humans and agents. Every handoff is a design decision. More than fifteen crossings on a six-step workflow = fragile.
    - 2. **Flowcharts** — for mapping decision logic. Lucidchart, Miro, whiteboard photo, or Mermaid (text-based, AI-generatable).
    - 3. **Visual design tools** (Figma, Claude artifacts, Excalidraw) — for when the output is something a stakeholder needs to see.
- C. **Swim-lane appendix reference** *(L101-119 → DEMOTE)* [DEMOTE]
    - 1. **Replace 19-line "How to draw a swim lane" Pro Tip with a 3-line reference:** *"For deeper coverage of swim lanes and flowcharts — how to read one, when to use which, and the Mermaid-via-AI shortcut — see the Diagramming Primer in the appendix."*
    - 2. The full how-to-draw procedure already lives at `chapters/appendix-diagramming-primer.qmd`. // AUTHOR REVIEW: confirm appendix coverage parity before cutting.
- D. **Action Step — swim lane the workflow** *(L121-124)* [KEEP]
    - 1. Pick the workflow. Draw human/agent swim lane. Count crossings. If higher than step count, redesign handoffs before Build.

### VII. Framework: The Design Brief *(L126-138)* [KEEP — chapter's central artifact]

  **Heading (proposed, directive):** "The Design Brief Is What Build Inherits"

- **Assumes:** reader has the deconstruction (§IV-V) and the diagrams (§VI). They have decisions; they don't yet have a single document that captures them.
- **Establishes:** the Design Brief — seven sections (workflow summary, stakeholders, systems, data requirements, success criteria, constraints/guardrails, V1 artifact description). The single artifact Design produces. Build's only input from Design.
- **Sets up:** the per-agent mini-spec (§VIII) — the Design Brief's hardest section, the one that specifies each agent at the level of precision Build needs.

- A. **Concept** *(L128)*
    - 1. The single artifact Design produces. Captures the decisions, stakeholders, systems, and governance Build inherits.
    - 2. Design's output. Build's input. No other channel.
- B. **The 7 sections** *(L130-138)*
    - 1. **Workflow summary** — trigger to output, every step, handoff, decision named.
    - 2. **Stakeholders** — Human Orchestrator, role-change list, downstream consumers, approvers.
    - 3. **Systems** — every system touched, with the specific data each provides or receives.
    - 4. **Data requirements** — what data, where it lives, what format, what happens when it's missing or malformed.
    - 5. **Success criteria** — measurable targets from Signal that this design has to move.
    - 6. **Constraints and guardrails** — data access, action permissions, escalation paths, quality cadence, kill switch.
    - 7. **V1 artifact description** — what the first working version produces: interface, document, pipeline, dashboard.
- C. **In-body artifact — blank Design Brief template** *(added in Phase 3B at ~L140)* [KEEP]
    - 1. Seven-row fillable table. One column per Sprint. Build inherits as is.

### VIII. Framework: Per-agent mini-spec *(L152-167)* [KEEP, cross-reference Ch 7]

  **Heading (proposed):** "Specify Every Agent with a Six-Field Mini-Spec"

- **Assumes:** reader has the Design Brief shape (§VII) and the agent-anatomy concept from Ch 3 and Ch 7. They know agents have a structure; here they specify each one.
- **Establishes:** the six fields per agent — system prompt, tools, context sources, memory rules, judgment/escalation rules, oversight load. Each field is a Build-blocking decision if missing.
- **Sets up:** the span-of-control check (§IX) and supervisor capability checklist (§X) — both are constraints on the mini-spec, not separate frameworks.

- A. **Concept** *(L154)*
    - 1. For every agent named in your HAC, the Design Brief includes a mini-spec.
    - 2. **Cross-reference Ch 7** — the six fields come from the agent-anatomy concept introduced there. Do not re-derive.
- B. **The 6 fields** *(L156-166)*
    - 1. **System prompt** — operating rules; what the agent does and explicitly doesn't do.
    - 2. **Tools** — every API, integration, system the agent can call. Named. Unlisted = no access.
    - 3. **Context sources** — which Knowledge Map rows feed this agent. Cross-reference the row directly.
    - 4. **Memory rules** — what carries across runs. Session state, accumulated decisions, lookback window.
    - 5. **Judgment and escalation rules** — when it escalates, what it refuses outright, what triggers a handoff.
    - 6. **Oversight load** — Low / Medium / High. Cognitive-budget decision per supervisor.
- C. **In-body artifact — blank mini-spec template** *(added in Phase 3B at ~L181)* [KEEP]
    - 1. Six-row fillable table. Copy once per agent on the HAC.

### IX. Framework: Span-of-control check *(L168-170)* [KEEP, cross-reference]

  **Heading (proposed):** "Check Span of Control Against the Three-Agent Ceiling"

- **Assumes:** reader has a populated HAC and the mini-spec method (§VIII). They may have assigned more than three concurrent agents to one supervisor without naming the tradeoff.
- **Establishes:** Bedard's three-agent ceiling as a design question to answer explicitly, not a hard limit. Citation lives in Ch 7; this section cross-references.
- **Sets up:** the supervisor capability checklist (§X) — even when the count is safe, the supervisor still has to pass Trace / Challenge / Apply.

- A. **The rule** — when one supervisor has more than three concurrent agents, the load must be justified.
- B. **HBR cross-reference (NOT re-citation):** *"Per Bedard's three-agent ceiling (see Chapter 7)..."* — citation lives once, in Ch 7.
- C. **The design test** — three-agent ceiling is not a hard stop, but a design question you answer explicitly.

### X. Framework: Supervisor capability checklist *(L172-178)* [KEEP, cross-reference]

  **Heading (proposed):** "Confirm Supervisor Capability: Trace, Challenge, Apply"

- **Assumes:** reader has the mini-spec (§VIII) and the span-of-control rule (§IX). They've named a supervisor per agent team but haven't confirmed the supervisor can actually do the work.
- **Establishes:** three tests — Trace (reconstruct the agent's reasoning from inputs), Challenge (target a specific line, get a real revision), Apply expertise (do something the agent can't). Cross-reference AWS/Effectual via Ch 7.
- **Sets up:** the Quote Assembly Agent worked example (§XI) — the mini-spec + Trace/Challenge/Apply check, populated end-to-end on Meridian.

- A. **The 3 tests**
    - 1. **Trace** — can the supervisor reconstruct why the agent produced this output from its inputs? If not, oversight is rubber-stamping.
    - 2. **Challenge** — can the supervisor target a specific line and get a real revision, not just reject the whole document? If not, oversight is theater.
    - 3. **Apply expertise** — where does the supervisor apply expertise the agent can't replicate? If every output ships without supervisor input, the supervisor is a speed bump.
- B. **HBR cross-reference (NOT re-citation):** AWS/Effectual source is already cited in Ch 7. *"(see Chapter 7)"* — cite-by-reference. // AUTHOR REVIEW: if Ch 7 ends up cutting AWS/Effectual, decide whether to expand here or cut here too.

### XI. Worked example: Quote Assembly Agent mini-spec *(L191-208)* [KEEP — excellent]

  **Heading (proposed):** "Worked Example — Quote Assembly Agent"

- **Assumes:** reader has the mini-spec framework (§VIII), span-of-control (§IX), and Trace/Challenge/Apply (§X). They've seen Meridian's deconstruction at the task level (§V).
- **Establishes:** what a fully populated mini-spec looks like for one specific agent (Quote Assembly Agent) — all six fields filled at the precision Build needs. Followed by Elena's Trace/Challenge/Apply check, also populated.
- **Sets up:** §XII (prototype) — the brief is complete on paper; the next discipline tests whether it survives contact with reality.

*Meridian thread structural adjacency:* this is the second longest Meridian beat in the chapter. It sits immediately after the mini-spec framework (§VIII) and supervisor checklist (§X). The concept-to-worked-example adjacency repeats the same pattern §IV → §V uses for the deconstruction itself. Meridian is the chapter's running case study at every major framework introduction, not a one-time mention.

- A. **Context** — Elena's quoting team has three agents; this is the mini-spec for the last one in the chain.
- B. **In-body artifact — populated 6-field mini-spec** *(L196-202)* [KEEP]
    - 1. System prompt, tools (HubSpot/Google Workspace/n8n), context sources, memory rules, escalation rules, oversight load.
- C. **In-body artifact — Trace/Challenge/Apply check for Elena** *(L204-208)* [KEEP]
- D. **Handoff sentence to Build** *(L210)*
    - 1. The Design Brief feeds the Build Spec. Build Spec is derived, not parallel — restates relevant sections at developer depth and adds agent scope at the call level, failure-mode behavior, and the specific environment.

### XII. Concept: Prototype before you build *(L212-225)* [KEEP]

  **Heading (proposed, directive):** "Prototype Before You Build"

- **Assumes:** reader has a populated Design Brief with mini-specs. The design looks right on paper.
- **Establishes:** Design isn't finished when it looks right; it's finished when the people who'll use the output understand what they're getting. Run one real input through the workflow. Two questions. Five customer responses are enough.
- **Sets up:** the Design Gate (§XIII) — prototyping is the final check that surfaces gaps before they become Build problems. The gate is what locks it in.

- A. **The standard** *(L214)*
    - 1. Design isn't finished when the workflow looks right on paper. It's finished when the people who'll use the output understand what they're getting and agree it solves the constraint.
- B. **The two-question prototype** *(L216-218)*
    - 1. Run one real input through the designed workflow.
    - 2. Ask: Does this output look right? Does this workflow match how you'd actually use it?
    - 3. The findings will surprise you. Every one is a design fix that costs minutes now and hours in Build.
- C. **Pro Tip — stakeholder surveys** *(L220-223)* [KEEP]
    - 1. Five customer responses are enough to catch the design gaps internal review misses.
- D. **Constant prototyping discipline** *(L225)* [KEEP]
    - 1. Design, prototype, feedback, adjust — runs naturally if you start early.

### XIII. Framework: The Design Gate *(L227-248)* [KEEP — five-item in-body checklist]

  **Heading (proposed, directive):** "Design Is the Gate. Hold It."

- **Assumes:** reader has done the deconstruction, populated the brief, written mini-specs, run a prototype. They have everything; they need a way to know it's complete.
- **Establishes:** the five-item Design Gate checklist — Work Deconstruction complete, HAC entries with named supervisors, Human Orchestrator named, AI-Assisted vs. Automated decided with rationale, guardrails defined (including kill switch). Plus two Action Steps: run the gate, fill the brief.
- **Sets up:** the handoff to Ch 9 (Build). When the five items check, Build can begin. The Design Brief is what Build inherits.

- A. **Why the gate matters** *(L229-231)*
    - 1. Teams that find Build slow almost always moved through Design too quickly.
    - 2. Every mid-Build "decision nobody made" costs five times as much to resolve.
- B. **The 5-item Design Gate checklist** *(L233-239)* [KEEP — checkbox format]
    - 1. **Work Deconstruction complete** — every task classified into three TML categories; no unclassified items.
    - 2. **HAC entries with named supervisor** — every accountability has a chart entry with all four fields filled.
    - 3. **Human Orchestrator named** — irreducible decisions and escalation triggers documented.
    - 4. **AI-Assisted vs. Automated decided** — per agent team, with rationale, not just a box checked.
    - 5. **Guardrails defined** — data access boundaries, action permissions, escalation paths, quality monitoring cadence, kill switch.
- C. **Emphasis on item 5** *(L241)* [KEEP]
    - 1. Define what the agents *aren't* allowed to do. Governance decisions belong in Design, not discovered in Build.
- D. **Action Step #1 — run the Design Gate checklist** *(L243-246)* [KEEP]
    - 1. Run the five-item checklist against current Sprint's design. Any gap = next working session, not next Build discovery.
- E. **[NEW] Action Step #2 — fill the Design Brief (ARC#8 closer)**
    - 1. Suggested wording: *"Open the Design Brief template. Fill in every section you can answer from the current Sprint. Every blank is a Design decision that hasn't been made — schedule that decision before Build begins."*
    - 2. Why this addresses ARC#8: the Design Brief is the chapter's central artifact and currently has no "do this now" closer.
- F. **Handoff to Build** *(L248-250)* [KEEP, light tighten]
    - 1. When the five are in place, Build can begin. Until then, it can't.
    - 2. Next chapter: Build — designed workflow becomes a deployable system, guardrails and oversight already set.

### XIV. Reflection Questions *(L252-257)* [TRIM from 4 → 3]

- **Assumes:** reader has the full method, the brief, and the gate.
- **Establishes:** three reflective prompts that send a leadership team into its next working session with named work.
- **Sets up:** Chapter 9 (Build) — the next chapter starts only when the gate is locked.

- A. Run Work Deconstruction on one real role — not the job description. What percentage lands in Leadership? Challenge each one.
- B. Run the 5-item Design Gate checklist against the current Sprint. Which item is hardest to check off — and what would clear it in the next session?
- C. Have you shown the designed output to the stakeholder who will live with it daily? What surprised them?
- D. [DROPPED] Swim-lane handoff-crossing question — absorbed into the swim-lane Action Step at VI.D.

---

## Heading inventory — current → proposed (full set)

| Current heading *(L#)* | Proposed directive heading |
|---|---|
| `# *Designing the Work*.` *(L1)* | `# Designing the Work: Lock the Gate or Build Pays the Cost` |
| *(NEW opener — promote coordinator story from L39)* | `## What Coordinator Deconstruction Looks Like in Practice` |
| `## Work *Deconstruction*.` *(L12)* | `## Deconstruct the Work Task by Task` |
| `## The role, *deconstructed*.` *(L39)* | *(absorbed into the opener at the top of the chapter)* |
| `### Populated example: Meridian Manufacturing quoting` *(L55)* | `### Meridian's Quoting Workflow, Fully Deconstructed` |
| `## Seeing the *design*.` *(L88)* | `## Make the Design Legible Before You Build It` |
| *(L101-119 swim-lane Pro Tip)* | *(DEMOTED to 3-line appendix reference)* |
| `## The *Design Brief*.` *(L126)* | `## The Design Brief Is What Build Inherits` |
| `### Per-agent mini-spec.` *(L152)* | `### Specify Every Agent with a Six-Field Mini-Spec` |
| `#### Span-of-control check.` *(L168)* | `#### Check Span of Control Against the Three-Agent Ceiling` |
| `#### The supervisor capability checklist.` *(L172)* | `#### Confirm Supervisor Capability: Trace, Challenge, Apply` |
| `#### Worked example: Quote Assembly Agent (Meridian Manufacturing).` *(L191)* | `#### Worked Example — Quote Assembly Agent` |
| `## Prototype before you *build*.` *(L212)* | `## Prototype Before You Build` |
| `## Design is the *gate*.` *(L227)* | `## Design Is the Gate. Hold It.` |
| `## Reflection Questions` *(L252)* | `## Reflection Questions` *(keep; trim 4 → 3)* |

---

## Artifacts (placed in context)

| Artifact | Status | Location |
|---|---|---|
| Work Deconstruction (TML categories) | Excalidraw L18 + in-body table L55-69 | Keep. Add in-body fillable template for reader's own work. |
| Coordinator before/after | Excalidraw L45 | Keep. Production redo flagged (existing TODO at L44). |
| **Meridian Work Deconstruction** (7-task table) | In-body L55-69 | Best artifact. Keep. |
| **HAC entries derived from deconstruction** | In-body L73-79 | Excellent. Keep. |
| Swim lane diagram | Excalidraw L93 (referenced) | Keep. |
| **Design Brief blank template** (7 sections) | Added by Phase 3B at ~L140 | Chapter's central artifact. |
| **Per-agent mini-spec blank template** (6 fields) | Added by Phase 3B at ~L181 | Mirrors Ch 7 mini-spec. |
| Span-of-control check | Inline L168-170 | Keep. |
| Supervisor capability checklist | Prose L172-178 | Already in-body. |
| Quote Assembly Agent mini-spec (populated) | In-body L196-202 | Excellent. |
| **5-item Design Gate checklist** | In-body L233-239 | Fillable as-is. |

---

## Meridian thread (per [[meridian-as-side-by-side-thread]])

Meridian appears in this chapter at THREE structurally adjacent landing points — each one paired with a framework introduction, not tacked on:

1. **§V — full Work Deconstruction worked example** *(L55-82)* — Elena's 7-task quoting workflow, classified end-to-end, with the derived HAC entries at L73-79. Sits immediately after the TML method (§IV).
2. **§XI — Quote Assembly Agent mini-spec** *(L172-186 / source L191-208)* — populated 6-field mini-spec plus Elena's Trace/Challenge/Apply check. Sits immediately after the mini-spec framework (§VIII) and supervisor checklist (§X).
3. **(Implicit) §II — coordinator opener** is NOT Meridian (it's the SuperWebPros coordinator role from Ch 7's opening). Meridian comes in at §V. This is correct: opener uses a different real role so the chapter doesn't lean on a single case study for every claim.

The Meridian appearances are structurally adjacent to the framework introductions they exemplify (§IV→§V; §VIII/§X→§XI). The reader doesn't have to wait for the case study; it lands the moment the concept is named.

---

## HBR citation discipline (this chapter)

**Current count:** 2 citations.
- Bedard 3-agent ceiling *(L166, L170)*
- AWS/Effectual supervisor capability source *(L174)*

**Trim plan (target: cross-reference, not re-cite):**
- **Bedard:** replace with *"Per Bedard's three-agent ceiling (see Chapter 7)..."* — citation lives once in Ch 7.
- **AWS/Effectual:** if Ch 7 retains AWS/Effectual citation, cross-reference here. If Ch 7 cuts it, decide whether to expand here or cut here too. // AUTHOR REVIEW.

---

## Edit decisions (summary)

- **PROMOTE coordinator story** *(L39-53)* to chapter opener — currently buried ~30% through.
- **DEMOTE 19-line swim-lane Pro Tip** *(L101-119)* to a 3-line reference pointing at `appendix-diagramming-primer.qmd`. // AUTHOR REVIEW: confirm appendix parity.
- **ADD closing Design Brief Action Step** (ARC#8) — central artifact currently has no "do this now."
- **CROSS-REFERENCE Ch 7** for Bedard 3-agent ceiling and AWS/Effectual — do not re-cite.
- **TRIM Reflection Questions** 4 → 3 (absorb swim-lane question into the swim-lane Action Step).

---

## Cross-chapter dependencies handled in Phase 3B (Drafter does NOT re-solve)

- Canonical agent definition first use *(book-ultm)* — landed earlier in the book; this chapter inherits.
- Orchestrator/Integrator disambiguation *(book-8v6v.32)* — no conflation sites in this chapter.
- Jargon parentheticals *(book-xqxi)* — API and Mermaid parentheticals already present at L158, L96.
- Design Brief blank template insertion at ~L140 — Phase 3B artifact placement.
- Per-agent mini-spec blank template insertion at ~L181 — Phase 3B artifact placement.

---

## Drafter notes

- Drafter model: **Sonnet** (~70-80% of existing prose survives; structural moves dominate, not rewriting).
- **Anchoring discipline:** Drafter reads the chapter syllogism + each section's Assumes/Establishes/Sets up triad BEFORE writing. Sentence-to-sentence decisions inside a section must respect the section's flow markers. If a sentence violates a marker (orphaned antecedent, restated prior claim, severed dependency), it's a coherence break the Drafter fixes before moving on.
- **Re-read pass:** after structural edits land, Drafter reads end-to-end and checks: (a) every pronoun has an antecedent within 3 sentences; (b) every cross-reference (Ch 3, Ch 7, Ch 9, appendix) resolves; (c) every artifact (Excalidraw, table, mini-spec template) sits adjacent to the prose that references it; (d) every Action Step still fits the section it lives in.
- Run `deflourish.py --apply` after drafting (mandatory — non-negotiable per memory).
- Voice charter applies. Strip italic-fragment headings. No em-dashes. No triplet pileups around the TML categories or the Trace/Challenge/Apply tests.
- Verify "Chapter 3" / "Chapter 7" / "Chapter 9" cross-references resolve correctly post-renumbering.
- **Author followup items already on the table:**
  - AWS/Effectual disposition pending Ch 7 outcome (see §X / HBR section).
  - Appendix swim-lane coverage parity confirmation before cutting the 19-line Pro Tip from §VI.
  - Coordinator before/after Excalidraw redo (existing TODO at source L44 — triplet pattern needs replacement).
