# Phase 3A Outline — Ch 8 (Build)

**Source file:** `chapters/07-build.qmd` · **Priority:** 3C #6 · **Drafter model:** Sonnet
**Proposed title:** *"Chapter 8: Build: A Locked Spec Becomes a Deployed System in Three Weeks"* — Traction-style "Chapter N: Descriptive Title: Main Idea Statement" per [[traction-style-chapter-titles]]. Confirm with author at handoff.
**Beads:** `book-0fq9` (FLOW#1 — relocate Technical Literacy + Agile AFTER Build Spec; spec earlier), `book-tb8h` (ARC#1 cross-refs — handled 3B), `book-xqxi` (ARC#3 jargon — handled 3B; chapter is jargon-heavy by necessity), readability (Flesch 58 — sentence-length tightening).
**Status:** Medium restructure. The chapter's how-to (8-section Build Spec) currently arrives at L166 — about 50% in — behind extensive technical-literacy and Agile framing. FLOW#1 reorder: lead with the spec discipline, then provide literacy as supporting reference. Compress Agile heavily.

---

## Chapter syllogism

- **Premise 1.** Design produced a locked Design Brief — workflow specification, guardrail intent, environment category, and the mini-specs Build executes against.
- **Premise 2.** Build is scoped narrowly to the designed workflow. Anything else — feature creep, platform thinking, vendor "improvements" — is a different project that doesn't belong in this Sprint.
- **Premise 3.** Three artifacts carry the chapter: the 8-section Build Spec (turns Design Brief into developer-ready specification), the 7-question Guardrails Checklist (locks quality, privacy, and oversight decisions in writing), and the environment choice (picks the specific tool inside the category Design named).
- **Conclusion.** A working, deployed system handling real work under the named HAC supervisor — not a demo, not a prototype, not a workflow nobody uses.

---

## Chapter content outline (proposed)

> **Legend:** [NEW] = added · [CUT] = removed · [MOVE] = relocated · [TRIM] = shortened · [KEEP] = unchanged · [PROMOTE] = moved earlier · [DEMOTE] = moved later · [COMPRESS] = collapsed · *(L#)* = current line in `07-build.qmd`

### I. In-Brief callout *(L3-6)* [KEEP]

- **Assumes:** reader has finished Ch 7 Design. Design Brief is locked.
- **Establishes:** Build delivers one thing — a deployed working system. Three artifacts gate it: 8-section Build Spec, 7-question Guardrails Checklist, environment choice. Done is real work under real supervision.
- **Sets up:** the opening hook — a worked example of the spec/guardrails/environment discipline already in motion at SuperWebPros.

- A. **Single core claim:** Build is the stage where a locked Design Brief becomes a deployed working system — specified by an 8-section Build Spec, stress-tested by a 7-question Guardrails Checklist, confirmed done only when it handles real work under real supervision.
- B. Closing sentence: if Build feels slow, the problem is upstream.
- C. Already does the work; light readability pass only.

### II. Opening hook — PM agent team build *(L8-14)* [KEEP verbatim]

- **Assumes:** reader believes the In-Brief framing — three artifacts, one deliverable.
- **Establishes:** a worked example of the discipline. Five agents replaced a $24K/year role because the HAC entry, access boundaries, and guardrails were locked in Design before Build executed any of them.
- **Sets up:** the claim that everything Build produces is bounded by what the spec and guardrails locked upstream.

- A. SuperWebPros built five agents that replaced a $24K/year coordinator role.
- B. Hybrid Accountability Chart locked first: Sofia as supervisor, AI-Assisted, sign-off required.
- C. Five agents, five access levels, every boundary decided in Design before Build executed.
- D. Sofia reviewed every output; Rachel shifted to exception handling.
- E. Bridge: the Guardrails Checklist is where you decide what the system is allowed to touch — before Build executes.

### III. Canvas connection *(L16)* [KEEP]

- **Assumes:** reader knows where Build sits in the Sequence (from Ch 4/5).
- **Establishes:** this chapter populates the Build row of the Sprint Planning Canvas.
- **Sets up:** the substance — what Build actually produces.

- A. This chapter fills in the Build row of the Sequence first-pass on the Sprint Planning Canvas.

### IV. Concept: What Build Produces *(L18-28)* [KEEP, light edit]

  **Heading (proposed, directive):** "Build Produces One Thing: A Deployed Working System."

- **Assumes:** reader has just seen the SuperWebPros opener. They know Build executes against a locked spec.
- **Establishes:** the single deliverable definition — *working* (tested against real inputs) and *deployed* (operating inside the business, used by named people). Demos and prototypes don't count.
- **Sets up:** the scope discipline — once you know what Build produces, you also know what it isn't.

- A. **The one deliverable** — a working, deployed solution to the validated constraint.
- B. *Working* — tested against real inputs; outputs the human supervisor can evaluate as they would a person's work.
- C. *Deployed* — operating inside the actual business environment, connected to systems, used by people who need it.
- D. **The high bar:** Build is done when work the team used to do is now being done by the designed system, supervised by the named HAC owner. Demos, prototypes, and workflows nobody uses are not done.

### V. Concept: Build Is Scoped to the Designed Workflow *(L30-51)* [KEEP]

  **Heading (proposed, directive):** "Build Is Scoped to the Designed Workflow. Anything Else Is a Different Project."

- **Assumes:** reader knows the deliverable definition. They might still believe "improving the spec mid-Build" is part of Build.
- **Establishes:** scope drift is the most common Build failure. Two responses to design gaps — stop and fix, or log for next Sprint's Signal. Build is fast because the spec is narrow.
- **Sets up:** who actually executes against that narrow spec — which clears the "hand it to engineering" misconception before the Build Spec lands.

- A. The agents in the previous chapter took on the bulk of the Human Orchestrator's workflow; this is where they got built to the shape Design specified.
- B. **Scope drift** — the engineer/vendor/builder "improves" the spec, adds features, generalizes the workflow into a platform. That isn't Build. That's a different project.
- C. **Build is fast because it's scoped narrowly.** A team built a quoting workflow in three weeks because Design gave them a workflow narrow enough to build in three weeks.
- D. **Design debt** — a decision that belonged in Design but didn't get made, now surfacing in Build. Two responses:
    - 1. If the gap blocks the build, stop, go back to Design, fix, resume.
    - 2. If the gap is real but the build can proceed safely, log it as a Signal item for the next Sprint. Don't absorb it quietly.
- E. **Scope expansion** — eyes get bigger when things work. Log it for the next Signal phase; don't add it to the current build.
- F. **Pro Tip** *(L48-51)* [KEEP] — favor the smallest possible solution that satisfies the spec. Three-skill Claude project in a week beats six-week agentic pipeline if the design called for a skill.

### VI. Concept: Build Lives Outside IT *(L53-70)* [KEEP]

  **Heading (proposed, directive):** "Build Doesn't Require Developers — Just the Person Closest to the Work."

- **Assumes:** reader knows Build is scoped narrowly. They may still default to "hand the narrow spec to engineering."
- **Establishes:** the actual bar is curiosity + systems thinking; tools are designed for non-engineers; IT controls keys, not the workflow build. The person closest to the work executes the spec.
- **Sets up:** the spec itself — now that the reader knows *they* are likely the one filling it in, they're primed to take the 8-section template seriously.

- A. **The bad assumption:** Build means "hand it to engineering." Developer is three projects deep. The Sprint stalls. The constraint keeps costing what it costs.
- B. **The actual bar:** curiosity + systems thinking. The rest is teachable.
- C. **Michigan State students example** [KEEP] — psychology, economics, criminal justice majors building functional data pipelines within a semester. Pulling from APIs, transforming through agents, writing back to systems. The tools are designed for non-engineers.
- D. **Tool examples** — Claude projects for skills, Replit for working apps, n8n for low-code automation. Barrier drops every quarter.
- E. **IT's real role:** controls the keys — permissions, access, security, credentials. IT gates the connection; IT doesn't prototype the workflow. *Person closest to the work builds it. IT makes sure it's safe.*
- F. **Action Step** *(L67-70)* [KEEP] — first Action Step lands at ~30% through, which is appropriate.

### VII. Framework: The Eight-Section Build Spec *(currently L166-219 — PROMOTE per FLOW#1)*

  **Heading (proposed, directive):** "Write the Eight-Section Build Spec."

- **Assumes:** reader knows what Build produces (§IV), that scope stays narrow (§V), and that the person closest to the work fills the spec out (§VI). They are ready for the spec discipline itself — not for more framing.
- **Establishes:** the chapter's central how-to. Eight named sections turn the Design Brief into a developer-ready specification. The spec's job is to remove ambiguity; if it's right, Build is mostly execution. Meridian's populated example lands here as the worked artifact.
- **Sets up:** the audit — once a spec is drafted, the seven Implementation Mistakes are the failure modes to check it against.

- A. **Why this section moves earlier:** The 8-section spec is the chapter's central how-to. Currently arrives at L166 (~50% through) behind 70 lines of technical-literacy and Agile framing. Promote so the spec discipline lands at ~35-40% through, while the reader is still oriented to the Build mindset. The Assumes/Establishes triad above is what justifies that order — §IV-VI clear the conceptual ground (what gets built, how narrow, by whom); the spec then lands on a prepared reader. Technical Literacy and Agile vocabulary do NOT prepare the reader for the spec — they support the environment decision and the time-box discipline that come *after* the spec is written.

- B. **Concept framing** *(L170-178)*
    - 1. Build Spec Writer turns the Design Brief into a developer-ready specification.
    - 2. The Design Brief is the single upstream input. The Build Spec restates workflow, systems, data at developer-execution depth, and adds three sections Design doesn't own: agent scope at the call level, failure-mode behavior, environment and constraints.
    - 3. **The spec's job is to remove ambiguity.** If the spec is right, the build is mostly execution. If the spec is wrong, the build is mostly negotiation.
    - 4. If Build Spec and Design Brief disagree, the Design Brief wins; the gap routes back to Design.

- C. **The eight sections** *(L180-189)* — each as a numbered sub-point [KEEP]
    - 1. **Workflow summary** — one paragraph, plain language, end to end. A builder who knows nothing about the business can read it and understand what they're building.
    - 2. **Inputs** — what triggers the workflow; what data enters, in what form, from which systems; how the builder accesses it.
    - 3. **Outputs** — what the workflow produces; what form; where it goes; who receives it.
    - 4. **Agent scope** — what the agent handles, decides, is not permitted to decide. Scope boundaries, not procedural instructions.
    - 5. **Human supervisor role** — who reviews; what they review for; the handoff form, location, timeline.
    - 6. **Systems and integrations** — every system touched; read/write access; authentication; data sensitivity classification per system.
    - 7. **Failure modes** — what happens when the agent produces output needing escalation. Who, what form, timeline.
    - 8. **Environment and constraints** — specific environment inside Design's category (off-the-shelf, low-code, hand-built — see Ch 7); data residency, license, security constraints the builder must observe.

- D. **ARTIFACT (Phase 3B at ~L193): Blank 8-section Build Spec template** [KEEP — already in chapter as a table]
    - 1. Eight rows, one per section.
    - 2. "Your Sprint" column with prompts for each section.
    - 3. Lead-in line: *Fill in every row before anything ships to a builder. An empty section is a decision the builder will make under build pressure.*

- E. **Worked example: Meridian populated Build Spec** *(in-body L195-211)* [KEEP — best in-body artifact in the chapter]
    - 1. Meridian Manufacturing — 27 employees, custom metal fabrication, quoting bottleneck costing $558K/year.
    - 2. Signal nailed the constraint, Source mapped the data, Design produced the workflow and the Design Brief.
    - 3. Eight populated sections walked through in order — RFQ intake through final delivery.
    - 4. Outcome: *Three and a half weeks, start to finish. No ambiguity meetings. No mid-build design decisions.*
    - 5. **Phase 3B note:** clarify heading structure with section-number labels (e.g., bold the section numbers).

- F. **Action Step** *(L232-235)* [KEEP] — write the eight section headers; fill Sections 1-3 from Design artifacts; complete Sections 4-8 from HAC + Knowledge Map. Every section must have content before the spec goes to a builder.

### VIII. Framework: Implementation Mistakes Checklist *(L237-258)* [KEEP]

  **Heading (proposed, directive):** "Audit the Spec Against Seven Common Failures."

- **Assumes:** reader has drafted (or is drafting) the 8-section Build Spec from §VII.
- **Establishes:** seven failure modes that have killed real builds — reinventing existing capabilities, wrong tool, incomplete spec, ignored handoff, missing failure modes, demo-thinking, declaring done without real inputs. Each as a check against the spec, not against the build.
- **Sets up:** the second locked artifact — guardrails — which gates what the system is allowed to *touch* once the spec is sound.

- A. **Framing line:** Before building starts, audit the spec against these seven failures. Each one has ended a Sprint early or produced a system shut down within weeks.

- B. **The seven mistakes** — each as a numbered sub-point [KEEP]
    - 1. **Reinventing existing capabilities.** Search before you build. 15 minutes of searching saves weeks. Most common implementation failure — not technical, but research.
    - 2. **Using the wrong tool for the job.** Match the environment to Design's category. If spec calls for low-code and someone proposes custom API "because it would be cleaner," the spec wins.
    - 3. **Building before the spec is complete.** Every empty section is a decision the builder will make on the fly. Builders aren't designers.
    - 4. **Ignoring the handoff.** Output must land where work already lives. If it lands in a new tool the team has never opened, adoption is zero.
    - 5. **Skipping failure modes.** Empty Section 7 = build handles the happy path and breaks on the first edge case.
    - 6. **Building for the demo instead of the workflow.** Demo shows the happy path. Build handles edge cases, missing data, outages, weird inputs, the supervisor on vacation.
    - 7. **Declaring done before testing against real inputs.** Pull last week's actual data. Synthetic and cherry-picked aren't tests.

- C. **ARTIFACT: Audit checklist (in-body)** [KEEP — already a numbered list; make explicit as a fillable audit checklist per Phase 3B]
    - 1. Phase 3B should structure as a checklist with check-off marks alongside each item.

- D. **Action Step** *(L255-258)* [KEEP] — walk all seven with the builder present. Check each against the completed spec. Any item that can't be checked off is a gap to resolve before build begins.

### IX. Framework: The Seven-Question Guardrails Checklist *(L260-295)* [KEEP]

  **Heading (proposed, directive):** "Answer the Seven Guardrails Questions in Writing."

- **Assumes:** reader has a complete spec that passes the seven-mistake audit.
- **Establishes:** the second of the chapter's three artifacts. Seven written answers — data access, agent autonomy, unrecognized inputs, quality measurement, escalation, accountability, kill switch — that lock the supervision conditions. Meridian's populated Guardrails table is the worked example.
- **Sets up:** the third artifact — the environment decision — which can only be made cleanly once spec + guardrails are answered, because data-sensitivity and autonomy answers drive the environment choice.

- A. **Framing line:** The set of quality, privacy, and oversight decisions that must be locked before the solution goes live. Answer all seven in writing. If any can't be answered, the build isn't ready.

- B. **The seven questions** — each as a numbered sub-point [KEEP]
    - 1. **Data access.** What data is the system permitted to touch? What is explicitly off-limits? Who decided, and where is it documented?
    - 2. **Agent autonomy.** What can the agent do without human approval? What requires sign-off?
    - 3. **Unrecognized inputs.** When the agent encounters an input it wasn't designed for, what does it do?
    - 4. **Quality measurement.** What specific checks, against what baseline, measured how?
    - 5. **Escalation path.** When output needs human judgment, who does it go to? In what form? On what timeline?
    - 6. **Accountability.** Who is responsible when the agent produces a bad output?
    - 7. **Kill switch.** What would cause you to shut down the agent workflow immediately?

- C. **ARTIFACT (Phase 3B at ~L263): Blank 7-row Guardrails Checklist template** [KEEP — already in chapter as a table]
    - 1. Seven rows, one per question.
    - 2. "Your answer" column blank for completion.

- D. **Worked example: Meridian populated Guardrails table** *(in-body L278-288)* [KEEP — best in-body artifact in chapter]
    - 1. Same seven questions populated with Meridian's answers — data access scope, autonomy boundaries, Inconel/material exceptions, weekly quality comparison, named escalation people (Dave/Mark/Elena), Elena owns accountability, kill-switch triggers (>20% errors on three quotes, any customer-facing without review, scope violation).
    - 2. Closes with: *These are the conditions under which the human supervisor can actually supervise.*

- E. **Action Step** *(L292-295)* [KEEP] — answer all seven in writing; attach as companion document to the Build Spec; if any question can't be answered, build is not ready.

### X. Concept: Pick the Environment Inside Design's Category *(L297-313)* [KEEP, with span-of-control compression]

  **Heading (proposed, directive):** "Pick the Environment Inside Design's Category."

- **Assumes:** spec written, seven-mistake audit passed, seven guardrail questions answered. Reader knows what the agent does and what it's allowed to touch.
- **Establishes:** the third artifact — the specific environment inside Design's category (off-the-shelf / low-code / hand-built). Five environment options with fit criteria. The data-sensitivity answer from Guardrails can force open-source / self-hosted; otherwise default to provider-hosted.
- **Sets up:** the structural check — span of control — that has to verify regardless of which environment was chosen.

- A. **Framing** *(L297-301)*
    - 1. The spec names what the agent does. Guardrails name what it's allowed to touch. Next question: where it actually runs.
    - 2. Design chose the category (off-the-shelf / low-code / hand-built — Ch 7). Build picks the specific environment.
    - 3. Environment options shift faster than workflow design principles. Current products are examples; check the market when you run your Sprint.

- B. **The five environments** — each as a numbered sub-point [KEEP]
    - 1. **Claude Projects** — skill-level work; single agent, defined knowledge base, one person or small team using it co-operatively. Build = configuration: system prompt, uploaded context, scope, guardrails in project settings. A competent person does this in an afternoon. Marketing lead's four-agent setup from Ch 3 started here.
    - 2. **Claude Team** — shared workspace, multiple projects; cross-team skill-level work where multiple people need the same agent context. Knowledge base and guardrails set once; team uses it. Doesn't fit workflows that run on a schedule without a human initiating each run.
    - 3. **Claude Code** — multi-agent, programmatic, tooling-heavy builds. Agents calling other agents, triggers, write-back, monitoring dashboards. SuperWebPros' PM agent team lives here.
    - 4. **n8n, Make, Zapier, and similar workflow orchestration platforms** — data pipeline builds: pull from a system, run through an agent, write back, notify. Meridian's quoting workflow used n8n alongside Claude Team.
    - 5. **Custom server and infrastructure** — workflows where control matters most: data residency rules out third-party, volume no low-code can handle, proprietary system-of-record API. Slower to build, harder to change, requires maintenance. Right call when Guardrails Checklist's data-sensitivity answer forces it — not because it's architecturally elegant.

- C. **ARTIFACT (Phase 3B): Environment summary table** [NEW per existing outline note]
    - 1. Five environments × fit / doesn't fit / example.
    - 2. Phase 3B adds at end of section.

### XI. Framework: Span-of-Control Check *(L315-328)* [COMPRESS — cross-reference only]

  **Heading (proposed, directive):** "Verify Span of Control Before You Pick the Environment."

- **Assumes:** reader has done the environment decision work. They know Bedard's three-agent ceiling from Ch 7.
- **Establishes:** if the designed system puts >3 agents under one supervisor, the environment choice can't fix it — go back to Design. The orchestrator-agent escape hatch (Ch 3) is the architectural workaround when count exceeds three.
- **Sets up:** the supporting reference material (Technical Literacy, then Agile vocabulary) the reader may need to consult — now that the three artifacts are in hand.

- A. **Compress per FLOW#1 / book-tb8h.** The current L286-292 re-explains Bedard's three-agent ceiling. Replace with a single cross-reference to Ch 7.
- B. **The cross-reference:** *Per Bedard's three-agent ceiling (see Chapter 7), productivity inverts after three concurrent agents under one supervisor. If the designed system puts four-plus agents under one supervisor, the environment decision won't fix it — go back to Design.*
- C. **Architectural escape hatch** [KEEP] — coordinator agent pattern (Ch 3 quote-orchestrator): the human reviews what the orchestrator surfaces, not each subagent's output. Design owns this decision; Build inherits it.
- D. **Action Step** *(L325-328)* [KEEP] — map designed agent count against named supervisor. If count > 3, flag as design gap before Build proceeds.

### XII. Concept: Technical Literacy *(currently L72-144 — DEMOTE per FLOW#1)*

  **Heading (proposed, directive):** "Know Enough About Models, Tokens, and Deployment to Hold Your Own."

- **Assumes:** reader has the three artifacts in hand (spec, guardrails, environment) and the span-of-control check has passed. They know what they're building, by what rules, in which environment.
- **Establishes:** the operator-level vocabulary — models and providers, tokens and pricing, open source vs. proprietary, RAG vs. fine-tuning vs. context window, deployment options — needed to make calls without deferring to someone who doesn't understand the constraint. Reference material, not entry ramp.
- **Sets up:** the time-box vocabulary that gives the same operator-level fluency over the *process* — Agile in one paragraph.

- A. **Why this section moves later:** Currently arrives at L72 (~25% through) and runs 70+ lines before the spec discipline lands. Reposition as supporting reference the reader can consult when picking the environment — not as the entry ramp to Build. The Assumes triad above justifies the demotion: a reader who hasn't yet seen the spec doesn't know which of these literacy components they need; a reader who has the spec, guardrails, and environment can consult this section selectively for the decisions in front of them.

- B. **Framing** *(L74-78)* [KEEP]
    - 1. Every company that manages information is already a technology company.
    - 2. You need enough vocabulary, trade-offs, and cost structure to make calls without deferring to someone who doesn't understand your constraint.
    - 3. **Decision split:** CEO/operator decides model, deployment, data-access approach. Builder handles configuration, APIs, wiring.

- C. **The five literacy components** — each as a numbered sub-point [KEEP, readability tightening]
    - 1. **Models and providers** *(L81-87)* — Anthropic (Claude), OpenAI (GPT), Google (Gemini), Meta (Llama — open source), smaller players (Groq, DeepSeek). Trade-offs by provider. Pick the model that fits the task in your spec, not a five-year vendor contract.
    - 2. **Tokens and pricing** *(L89-102)* — token = ~3/4 of a word. Pricing per token, varies by provider/model. Input vs. output priced differently. SuperWebPros four-figure overage example (learned the hard way). **Fix:** capable model where judgment matters; cheaper/faster where it doesn't (classification, summarization, routing). **Pro Tip** *(L99-102)* [KEEP] — estimate monthly token cost before build starts.
    - 3. **Open source vs. proprietary** *(L104-110)* — proprietary (Claude, GPT, Gemini): most capable, provider-managed, your data travels through their systems. Open source (Llama, Mistral): runs on your servers, full data control, gap to top proprietary shifts. For most Sprints, proprietary is right; data-sensitivity exception from Guardrails Checklist drives open-source path.
    - 4. **Making AI work with your data** *(L112-130)* — three sub-approaches:
        - a. **Fine-tuning** — retrain a model on your data. Expensive, slow, hard to update. Rare for most organizations.
        - b. **RAG (retrieval-augmented generation)** — give the model access to your data at the moment it needs it. Cheaper, faster, easy to update. Right approach for most Compound Sprint builds.
        - c. **Large context window** — load documents directly into the conversation. No infrastructure. Works for smaller datasets / ad-hoc work. Performance degrades near limit.
        - d. **Decision rule:** start with context window; move to RAG when data outgrows the window; fine-tune only when the model needs to behave differently at a fundamental level. Knowledge Map from Source tells you what data the model needs.
        - e. **Action Step** *(L128-131)* [KEEP] — when a vendor proposes fine-tuning, ask: could we get the same result with query-time access?
    - 5. **Deployment options (where the build runs)** *(L133-147)* — three options, increasing complexity:
        - a. **Provider-hosted (API)** — default for most builds; simplest, no infrastructure.
        - b. **Your own server** — self-hosted (usually open source). Full data control, higher setup cost, requires maintenance.
        - c. **Serverless / edge** — distributed, auto-scales. High-volume workflows. Overkill for most first Sprints.
        - d. **Decision rule:** start with provider-hosted unless Guardrails Checklist flags data residency.

- D. **Readability target:** mean sentence count per paragraph < 4. Apply paragraph-stats.py after drafting.

### XIII. Concept: Agile Vocabulary, in One Paragraph *(currently L146-164 — COMPRESS HEAVILY per FLOW#1)*

  **Heading (proposed, directive):** "Agile Vocabulary, in One Paragraph."

- **Assumes:** reader has the technical vocabulary from §XII. Some readers come from software backgrounds and want the Compound-to-Agile mapping; others don't.
- **Establishes:** a tight glossary mapping — Sprint = Compound Sprint, Backlog = 8-section Build Spec, QA = five-question Done test, Accountability = HAC supervisor. One paragraph, ~5-7 lines, not a detour.
- **Sets up:** the Meridian Sprint vignette — which shows the whole spec/guardrails/environment/literacy/time-box discipline running end-to-end in three weeks.

- A. **Compress from 19 lines to ~5-7 lines as a single paragraph reference.** Currently a 19-line detour before the spec sections; collapse to a tight glossary-style paragraph.

- B. **Proposed compressed paragraph** [NEW — replaces L149-164]
    - 1. Lead: *If you've run a software team, you know this language. In Compound terms, the vocabulary maps cleanly:*
    - 2. **Sprint** — the time box; here, the Compound Sprint from Ch 4.
    - 3. **Backlog** — the prioritized work list; here, the eight-section Build Spec. New items don't get added mid-build; they log to the next Sprint's Signal.
    - 4. **QA** — testing against real inputs before declaring done; here, the five-question Done test.
    - 5. **Accountability** — every item has an owner, every test a sign-off; here, the human supervisor named in the HAC.

- C. **Pro Tip** *(L165-168)* [KEEP] — if Build is running past the time box, cut scope, not extend deadline. Ship 80%, build the remaining 20% next Sprint.

- D. **// AUTHOR REVIEW:** The original outline (line 50) suggested moving the full Agile detour to a glossary appendix entry. This outline keeps the compressed paragraph in-chapter and does NOT create an appendix entry. If you want the appendix entry, flag it for Phase 3B.

### XIV. Sprint vignette: Meridian three-week quoting workflow *(L330-338)* [KEEP]

  **Heading (proposed, directive):** "The Three-Week Quoting Workflow."

- **Assumes:** reader has seen the three artifacts and the supporting vocabulary. Meridian has already shown up populated inside §VII (Build Spec) and §IX (Guardrails table).
- **Establishes:** the end-to-end Sprint result. Constraint → mapped data → designed workflow → low-code category → Elena assembling it on Claude Team + n8n + three days of contracted help → 3.8 days to 4.2 hours, ten hours/week back to Elena. Spec + Guardrails were ten-minute decisions that made three and a half weeks of build work unambiguous.
- **Sets up:** the Done test — the explicit five-question gate that distinguishes "the system works" from "Build is done."

- A. Signal: quotes at 3.8 days, $558K/year cost.
- B. Source mapped inputs; Design produced the workflow (three agents in a Claude project, Elena reviews every output before Ty delivers).
- C. Low-code category; Elena assembled it herself using Claude Team + n8n; freelance n8n developer for three days.
- D. Cleaning the pricing exceptions spreadsheet took the most work (31/147 rows had conflicts).
- E. Spec + Guardrails Checklist locked before build: ten-minute decisions that made three and a half weeks of build work unambiguous.
- F. Outcome: standard quotes from 3.8 days to 4.2 hours; Elena got ten hours a week back.

### XV. What Done Looks Like *(L340-365)* [KEEP]

  **Heading (proposed, directive):** "What Done Looks Like: The Five-Question Test."

- **Assumes:** reader has built the system the spec described in the environment the Guardrails Checklist allowed.
- **Establishes:** the five-question gate — expected outputs, edge cases handled, escalation works, supervisor can read the output without a walkthrough, team briefed on changed handoffs. Yes-to-all is the only pass condition.
- **Sets up:** the handoff to Deliver — where the deployed system gets put into the operating rhythm.

- A. **The bar:** deployed solution producing outputs against real inputs, reviewed by the named HAC supervisor. The supervisor is using it. The team is using it. Past the demo stage, past the prototype.

- B. **The five-question Done test** [KEEP] — each as a numbered sub-point
    - 1. Did it produce the expected outputs? (Within the quality range the supervisor would accept from a team member.)
    - 2. Did it handle the edge cases? (Every failure mode in Section 7 of the spec.)
    - 3. Did it escalate correctly? (Feed inputs that should trigger escalation; right person, form, timeline.)
    - 4. Could the supervisor understand the output without a walkthrough?
    - 5. Has the team been briefed on what changes? (Human Orchestrator identifies every person whose handoff changes and confirms they're ready day one.)

- C. **Decision rule:** Yes to all five → Build is done; hand to Deliver. No to any → fix, retest, do not advance past Build on partial pass.

- D. **Action Step** *(L362-365)* [KEEP] — pull last week's real inputs, run the test, document results, fix failures, retest. Results are part of the Build → Deliver handoff.

### XVI. Closing handoff to Deliver *(L367-369)* [KEEP, light edit]

  **Heading (proposed, directive):** "Hand Off to Deliver."

- **Assumes:** five-question test passed; system is deployed.
- **Establishes:** Build's job ends at "it works." Deliver's job is putting it in the operating rhythm — training, handoffs, measurement against the dollar cost Signal named.
- **Sets up:** Ch 9 Deliver as the next stage in the Sequence.

- A. Build makes it work. Deliver puts it into the company's operating rhythm — trains people, changes handoffs, measures against the dollar cost Signal named, makes sure the system is owned not orphaned.
- B. **Proposed closing line per existing outline:** *"With the spec locked and the guardrails answered, Build executes. Chapter 9 is where the deployed system gets put in front of real work."*

### XVII. Reflection Questions *(L371-376)* [TRIM from 4 → 3]

- **Assumes:** reader has finished the chapter.
- **Establishes:** three working-session prompts — environment match, hardest guardrail question, where scope creep is already showing up.
- **Sets up:** the leadership-team conversation that turns the chapter's three artifacts into a real Sprint plan.

- A. **Q1 (KEEP):** Match the Design Brief's category to the five environments. Which fits agent count, data sensitivity, supervision model? Does that match where the team assumed you'd end up?
- B. **Q2 (KEEP):** Fill in all seven Guardrails Checklist questions for your workflow. Which is hardest to answer — and is that a Design gap or a genuine open decision?
- C. **Q3 (KEEP):** Where is scope creep already showing up? What does the spec say versus what the builder is proposing — and which one wins?
- D. **Q4 (DROP):** Run the five-question Done test against your build. *(Already covered by the Action Step at §XV.D. Trim.)*

---

## Heading inventory — current → proposed (full set)

| Current heading *(L#)* | Proposed directive heading |
|---|---|
| `# *Build*.` *(L1)* | `# Build: A Locked Spec Becomes a Deployed System` |
| `## What *Build* produces.` *(L18)* | `## Build Produces One Thing: A Deployed Working System` |
| `## Build is scoped to the *designed* workflow.` *(L30)* | `## Build Is Scoped to the Designed Workflow. Anything Else Is a Different Project.` |
| `## Build lives outside IT.` *(L53)* | `## Build Doesn't Require Developers — Just the Person Closest to the Work` |
| `## Technical literacy — what you need to know.` *(L72)* | *(DEMOTED — moves to after Environment Selection)* |
| `## Agile concepts for the rest of us.` *(L149)* | *(DEMOTED + COMPRESSED — moves to after Technical Literacy as one paragraph)* |
| `## The two instruments — *Build Spec Writer* and *Guardrails Checklist*.` *(L170)* | `## Write the Eight-Section Build Spec` *(PROMOTED EARLIER; split from Guardrails)* |
| `## The Implementation Mistakes Checklist.` *(L237)* | `## Audit the Spec Against Seven Common Failures` |
| `## The *Guardrails Checklist*.` *(L260)* | `## Answer the Seven Guardrails Questions in Writing` |
| `## Where the *agent* lives.` *(L297)* | `## Pick the Environment Inside Design's Category` |
| `### The span-of-control constraint.` *(L315)* | `### Verify Span of Control Before You Pick the Environment` *(COMPRESS to cross-ref)* |
| *(landing position after environment)* | `## Know Enough About Models, Tokens, and Deployment to Hold Your Own` *(DEMOTED from L72)* |
| *(landing position after technical literacy)* | `## Agile Vocabulary, in One Paragraph` *(DEMOTED + COMPRESSED)* |
| `## Sprint: the three-week quoting workflow.` *(L330)* | `## The Three-Week Quoting Workflow` |
| `## What *done* looks like.` *(L340)* | `## What Done Looks Like: The Five-Question Test` |
| `## Hand off to *Deliver*.` *(L367)* | `## Hand Off to Deliver` |
| `## Reflection Questions` *(L371)* | `## Reflection Questions` *(KEEP — conventional)* |

H3 set under "Know Enough About Models, Tokens, and Deployment":
- `### Models and Providers`
- `### Tokens and Pricing`
- `### Open Source vs. Proprietary`
- `### Making AI Work with Your Data`
- `### Where the Build Runs` (was "Deployment...")

---

## Artifacts inventory

| Artifact | Status | Location |
|---|---|---|
| Blank 8-section Build Spec template | In-body table at L195-204 [KEEP] | Phase 3B confirms structure; lead-in line about empty sections. |
| Meridian populated 8-section Build Spec | In-body prose L211-226 [KEEP] | Best in-body artifact in chapter. Phase 3B: clarify section-number labels. |
| Blank 7-row Guardrails Checklist template | In-body table at L268-276 [KEEP] | Phase 3B confirms structure. |
| Meridian populated Guardrails table | In-body table L280-288 [KEEP] | Excellent. |
| Implementation Mistakes audit checklist | Numbered list L241-253 [KEEP] | Phase 3B: render as fillable audit checklist with check-off marks. |
| Environment options summary table | [NEW — Phase 3B adds] | Five environments × fit / doesn't fit / example. End of §X. |
| Excalidraw — data access approaches | L126 [KEEP] | Three approaches: context window / RAG / fine-tuning. |
| Excalidraw — Design Brief example | L172 [KEEP] | Lives at §VII opening. |
| Excalidraw — Build Spec sections | L191 [KEEP] | Eight sections with one-line descriptions. |
| Excalidraw — Meridian Design Brief | L208 [KEEP] | Quote Agent Team scope, Elena as supervisor. |
| Excalidraw — Guardrails Checklist | L264 [KEEP] | Seven questions as pre-deploy gate. |
| Excalidraw — Meridian Build Spec | L342 [KEEP] | Final-section visual. |
| Excalidraw — Meridian Guardrails | L344 [KEEP] | Final-section visual. |

---

## Edit decisions

**FLOW#1 reorder** *(book-0fq9)* — the largest move in this chapter:
- **PROMOTE earlier:** The 8-section Build Spec (currently L166-219) moves to ~35-40% through, right after "Build lives outside IT." Reader hits the spec discipline while still oriented to the Build mindset.
- **DEMOTE later:** Technical Literacy (currently L72-144) and Agile Concepts (currently L146-164) move to AFTER the Build Spec, Implementation Mistakes, Guardrails, and Environment sections. They become supporting reference material, not the entry ramp.

**Agile compression** *(book-0fq9)* — collapse 19 lines (L146-164) to one short paragraph as a glossary-style reference. Sprint / Backlog / QA / Accountability each as one-line definitions mapped to Compound terms. // AUTHOR REVIEW: original outline suggested moving the full detour to a glossary appendix; this outline keeps the compressed paragraph in-chapter only.

**Span-of-control compression** *(book-tb8h)* — replace the L286-292 re-explanation of Bedard's three-agent ceiling with a single cross-reference to Ch 7. Drafter must not re-explain.

**Readability** — Flesch 58, dense technical content. Tighten sentence length throughout Technical Literacy. Target: mean sentence count per paragraph < 4. Apply paragraph-stats.py after draft.

**Reflection Questions** — trim 4 → 3; drop Q4 (already an Action Step).

**Closing handoff** — add explicit handoff sentence to Ch 9 Deliver after the §XVI paragraph.

---

## Meridian thread (per [[meridian-as-side-by-side-thread]])

Meridian appears in this chapter at THREE specific landing points, all structurally adjacent to the chapter's framework introductions — which is exactly what the side-by-side thread pattern calls for. The triads above make this adjacency explicit: Meridian shows up *as* the worked example in the section that *introduces* the framework.

1. **§VII Build Spec — populated 8-section example *(in-body L195-211)*.** Meridian's populated Build Spec follows the blank template inside the section that introduces the 8-section framework. The reader sees the framework, the blank template, then Meridian's filled-in version — in one structural unit. Worked example, not a sidebar.
2. **§IX Guardrails Checklist — populated 7-row table *(in-body L278-288)*.** Same structural pattern: the seven questions are introduced, the blank checklist appears, then Meridian's answers — data access, autonomy, escalation people (Dave/Mark/Elena), Elena owns accountability, kill-switch triggers. The section's worked example IS the populated table.
3. **§XIV Sprint vignette — three-week quoting workflow *(L330-338)*.** The end-to-end run: Signal → Source → Design → Build → result (3.8 days to 4.2 hours, ten hours/week back to Elena). This is the integrative landing where every prior Meridian fragment in the book closes out for this Sprint.

**Status:** Meridian thread is already strong in this chapter — populated artifacts at L195-211 and L253-259, plus the Sprint vignette. The triads in §VII and §IX above make explicit that Meridian's populated examples sit structurally adjacent to (not after, not separated from) the framework introductions. Drafter must preserve this adjacency in the restructure. No new Meridian sentences need to be added.

---

## HBR citation discipline (this chapter)

**Current count:** Zero direct HBR citations in body. Bedard's three-agent ceiling appears as a cross-reference at L317 (post-restructure). Keep as cross-reference only; do not re-cite HBR data here. Per [[hbr-citation-discipline]], this chapter is already at the right level — zero direct citations, one cross-reference to the prior chapter's citation. Drafter must not add HBR citations during the restructure.

---

## Cross-chapter dependencies handled in Phase 3B (Drafter does NOT re-solve)

- Canonical agent definition at first use *(book-ultm)* — handled at Ch 2 L35; Ch 8 inherits parenthetical in In-Brief.
- Orchestrator/Integrator disambiguation *(book-8v6v.32)* — Ch 8 uses "Human Orchestrator" cleanly; nothing to do.
- Jargon parentheticals *(book-xqxi)* — chapter is jargon-heavy by necessity (API, RAG, fine-tuning, tokens). Parentheticals already in place at L59, L63, L118. Phase 3B sweep verifies.
- ARC#1 cross-refs *(book-tb8h)* — "see Chapter 7" loops at L189, L301, L317, L321 swept in 3B.
- SPC through-line — Build row of the Sequence (L16) → spec/guardrails as Build artifacts → handoff to Deliver row.

---

## Drafter notes

- This is a medium restructure, not a rewrite. ~80% of existing prose survives.
- Use **Sonnet** (per existing outline). The chapter is procedurally heavy, not voice-heavy.
- The largest move is the FLOW#1 reorder. Drafter must hold the order: In-Brief → Opener → What Build Produces → Scope → Outside IT → **Build Spec (PROMOTED)** → Implementation Mistakes → Guardrails → Environment → Span-of-Control → **Tech Literacy (DEMOTED)** → **Agile (COMPRESSED + DEMOTED)** → Meridian Sprint vignette → Done test → Handoff → Reflection.
- Compress Agile to ~5-7 lines as a single paragraph.
- Replace span-of-control re-explanation with cross-reference to Ch 7. Do not re-explain Bedard.
- Voice charter applies. Strip italic-fragment headings. No em-dashes. Directive headings only.
- Run deflourish.py --apply after drafting (mandatory).
- **Anchoring discipline:** the Drafter reads the chapter syllogism + each section's Assumes/Establishes/Sets up triad BEFORE writing. The triads exist specifically to justify the FLOW#1 reorder — §IV-VI prepare the reader for the spec; §VII (Spec) → §VIII (Audit) → §IX (Guardrails) → §X (Environment) → §XI (Span) sequence the three artifacts cleanly; §XII (Tech Literacy) and §XIII (Agile) land as reference *after* the three artifacts, not as entry ramp.
- **Meridian thread:** preserve the structural adjacency between framework introductions and populated examples in §VII and §IX. Do not separate the blank template from the Meridian populated version — they belong in the same section.
- **Author followup items (handoff sign-off needed):**
  - Chapter title pattern: confirm Traction-style "Chapter 8: Build: A Locked Spec..." vs. current shorter form.
  - Glossary appendix for full Agile content (// AUTHOR REVIEW flagged in §XIII.D) — current outline keeps compressed paragraph in-chapter only; flag if you want the appendix entry.
  - New closing line at §XVI.B.
