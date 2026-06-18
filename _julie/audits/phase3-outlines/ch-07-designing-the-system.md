# Phase 3A Outline — Ch 7 (Designing the System)

**Source file:** `chapters/06-designing-the-system.qmd` · **Priority:** 3C #4 · **Drafter model:** Sonnet
**Proposed title:** *"Chapter 7: Designing the System: Every Row Has a Name."*
*(Alternative: "Chapter 7: Designing the System: Build the Hybrid Accountability Chart Before You Build Anything Else." Longer; less confrontational. Author preference between the two; "Every Row Has a Name" mirrors the chapter's repeated "no exceptions" gate language and lands the chapter's load-bearing rule in five words.)*
**Beads:** `book-0fq9` (FLOW#1 lead with practice — info-flow before HAC, Human Orchestrator up), `book-lbd7` (ARC#8 HAC-draft Action Step), `book-xqxi` (ARC#3 jargon — handled 3B), `book-g404` (ARC#6 EOS terms scoped — handled 3B), `book-8v6v.32` (ARC#13 Orchestrator/Integrator disambig — handled 3B), HBR citation discipline (memory — Bedard + AWS appear; trim).
**Status:** Medium-to-heavy restructure. Chapter is comprehensive and well-built but front-loads the HAC before the reader sees what information flow means. The Human Orchestrator definition arrives ~80% through despite being the chapter's load-bearing role concept. FLOW#1 reorder (info-flow before HAC; Human Orchestrator promoted up) is the dominant move. HBR trim: keep Bedard, cut AWS. This outline carries the upgraded format ([[chapter-syllogism-and-flow-markers]]) so the Drafter can anchor sentence-to-sentence decisions in the chapter's argument structure — especially the §V→§VII→§VIII reorder, which requires the flow markers to make the new order feel inevitable.

---

## Chapter syllogism

- **Premise 1.** You arrived at Design with a Constraint (from Signal) and a Knowledge Map (from Source). You know *where* the work is broken and *what* knowledge it runs on. You don't yet know how to assign owners to it — human or AI.
- **Premise 2.** Before you assign owners, you have to see the work as information flow. Every accountability in a knowledge business is an information problem; the chart that follows is a chart of who owns which slice of the flow. Information flow comes first; the chart comes second; and every row of the chart — without exception — names a human supervisor.
- **Premise 3.** The chart names *what* is owned and *who* owns it. Three further design decisions name *how* it's owned: the *Human Orchestrator* is the named role that owns the constraint outcome for the Sprint; the *mini-spec* is the per-agent specification Build inherits; the *tool category* is the environment decision Design makes before Build picks a product.
- **Conclusion.** You can leave Design with an HAC entry and a mini-spec for your constraint workflow — every row named, every agent specified, every category chosen — and hand Build something Build can execute against without coming back for interpretation.

---

## Chapter content outline (proposed)

> **Legend:** [NEW] = added · [CUT] = removed · [MOVE] = relocated · [TRIM] = shortened · [KEEP] = unchanged · *(L#)* = current line in `06-designing-the-system.qmd`

### I. In-Brief callout *(L5-8)* [TRIM]

- **Assumes:** reader has finished Signal (constraint named, priced) and Source (Knowledge Map built). They've arrived at Design.
- **Establishes:** the chapter's single load-bearing rule — every accountability has a human supervisor by name — and the four deliverables Design produces.
- **Sets up:** the opening hook, which dramatizes the design move (asking "what does this role actually do?" instead of "who do we hire?").

- A. **Single core claim:** *Every agent team needs a human supervisor by name.* Lead with that, not the four-deliverable enumeration.
- B. The four deliverables (HAC entries, governance framework, agent mini-specs, category choices) follow as the chapter's structure, not as a callout list.
- C. Drop the inline canonical agent definition from the callout (already handled by 3B at first-use elsewhere).

### II. Opening hook — COO/project coordinator scene *(L10-18)* [KEEP verbatim]

- **Assumes:** reader believes Design is a stage they should not skip (from In-Brief). They don't yet know what designing looks like in practice.
- **Establishes:** the design move in story form — pulling a role apart into information sources, outcomes, and a human-judgment-vs-data-flow filter. The instinct to hire is interrupted by the question *"what does this role actually do?"*
- **Sets up:** the conceptual framing — Design exists to ask what the work actually is — which §III then names directly.

- A. COO on a weekly call: *"She's not keeping up with clients. Reports are late. I think we need to let her go."*
- B. The instinct is to solve the personnel problem with a hire; the Sequence interrupts that reflex.
- C. The author stops and asks a different question: *not "who should we hire?" but "what does this role actually do?"*
- D. Role pulled apart into information sources, outcomes, and a filter (human judgment vs. data-flow operations). One job becomes two; one half becomes an agent team.
- E. Outcome: never posted the replacement listing; work absorbed without crisis; judgment stayed with people, administration moved to the agent team.

### III. Why Design exists *(L20-24)* [KEEP, light edit]

- **Assumes:** reader has seen the design move in story form (§II). They understand Design pulls work apart before assigning owners.
- **Establishes:** Design as the first stage of Execute & Compound — the gate that determines whether the Sprint compounds or stalls. Separates "designing the system" (this chapter) from "designing the work" (next chapter).
- **Sets up:** what Design *produces*, which §IV enumerates as four concrete deliverables.

- A. Design exists to ask what the work actually is.
- B. Design is the first stage of *Execute & Compound* — the gate, and the reason every Sprint either compounds or stalls.
- C. This chapter designs the system the work runs through; the next chapter designs the work itself.

### IV. Design has four deliverables *(currently L26-36)* [KEEP, surface as explicit numbered list]

  **Heading (proposed, directive):** "Design Has Four Deliverables"

- **Assumes:** reader believes Design is the gate (from §III). They want to know what Design produces concretely.
- **Establishes:** the four deliverables Design lands together — designed workflow, HAC entries, governance framework, mini-spec + category choice per agent. Names that partial outputs are predictably broken (workflow without owner = process map nobody owns; entry without workflow = org chart row with nothing behind it).
- **Sets up:** the question the four deliverables jointly raise — *but what does this work actually look like before you can assign owners to it?* The answer is information flow (§V), not the chart (§VII). The chapter answers in that order.

- A. **Make the four explicit as a numbered list before the prose develops each one:**
    - 1. A *designed workflow* — inputs, steps, handoffs, outputs, human-decides-vs-agent-executes points.
    - 2. *Hybrid Accountability Chart entries* for every accountability this Sprint touches.
    - 3. A *governance framework* — autonomy levels, guardrails, escalation paths.
    - 4. A *mini-spec* for every agent and a *category choice* before Build begins.
- B. Design has to produce all four; partial outputs are predictably broken (workflow without owner = process map nobody owns; entry without workflow = org chart row with nothing behind it).

### V. See the work as information flow first *(PROMOTED from L76-102 — FLOW#1)*

  **Heading (proposed, directive):** "See the Work as Information Flow First"

  **Critical reorder:** This section moves UP from its current position (after the HAC) to BEFORE the HAC. Reader needs the information-flow lens before seeing the chart that maps it.

- **Assumes:** reader knows Design has four deliverables (from §IV) and is now asking *what* the work looks like before they can assign owners to it. They have a Knowledge Map from Source telling them where knowledge lives, but not how it moves.
- **Establishes:** every accountability in a knowledge business is an information problem. The Information Flow Specification (four fields: data feeds, transformations, decisions, outputs) and the swim lane diagram make the flow visible — including handoffs, which are where workflows fail. Distinguishes the Information Flow Spec (*how* knowledge moves through one workflow) from the Knowledge Map (*what* knowledge exists and *where* it lives). The reader can now describe the flow without yet naming owners.
- **Sets up:** the chart that assigns owners to that flow. The reader has a swim-lane diagram with steps in lanes; the HAC names who owns each lane. §VII opens on that handoff. §VI (five connection patterns) sits between as the menu of *how* AI can plug into each step of the flow before ownership gets assigned.

- A. **The information flow question** *(L78-80)*
    - 1. Before the chart makes sense, you have to answer the question most leadership teams never ask: *how does information actually move through this part of the company?*
    - 2. Every accountability in a knowledge business is an information problem.
    - 3. The design question becomes: *what information does this work need, where does it live, and how should it move?*

- B. **The Information Flow Specification** *(L82-87)* — four fields
    - 1. What data feeds the work (and which systems hold it).
    - 2. What transformations happen (lookups, comparisons, calculations, formatting).
    - 3. What decisions get made (rule-based vs. judgment-based).
    - 4. What the output is and where it goes next.

- C. **Swim lane diagram** *(L89-93)* [KEEP]
    - 1. Parallel lanes — one per actor; each step in its owner's lane; handoffs are line crossings.
    - 2. Makes three things visible: who does what, where information changes hands, how many handoffs the workflow requires.
    - 3. Excalidraw L93 — keep.

- D. **How this differs from the Knowledge Map** *(L95)*
    - 1. Knowledge Map = *what* knowledge exists and *where* it lives.
    - 2. Information flow spec = *how* that knowledge moves through a specific workflow.

- E. **Why start here** *(L97)*
    - 1. Forces start with outcome and work backwards. Roles and tasks fall into position once the flow is mapped.

- F. **Action Step** *(L99-102)* [KEEP]
    - 1. Pick one accountability from your constraint workflow. Write down the information flow. Don't describe the role — describe the information.

### VI. Map AI to information flow using five patterns *(currently L104-138)* [KEEP, folds under §V's frame]

  **Heading (proposed, directive):** "Map AI to Information Flow Using Five Patterns"

- **Assumes:** reader can see the information flow for their constraint workflow (from §V). They're now asking: at each step where AI could plug in, *how* would it actually plug in?
- **Establishes:** five patterns for connecting AI to information (Skills/SOPs, RAG, data pipelines, low-code integration, service layers/APIs). The CEO/operator picks the pattern; Build implements. Most first Sprints use patterns 1 and 2 with some pattern 4 routing. Pattern selection follows from the information problem, never the other way around.
- **Sets up:** the chart that assigns ownership of each accountability — including the pattern decisions just made. The HAC is where pattern choice gets attached to a human supervisor.

- A. **Framing** *(L106, L115)*
    - 1. Once you can see the information flow, you need to know your options for connecting AI to it.
    - 2. You (the CEO/operator) decide which pattern fits. Build handles implementation.

- B. **The five patterns** *(L117-125)* — number explicitly:
    - 1. **Skills reinforcing SOPs.** Knowledge in people's heads, documented as SOPs; AI uses docs as context for brainstorming/drafting. Lowest infrastructure lift.
    - 2. **RAG — retrieval-augmented generation.** Knowledge in documents/records/databases; AI retrieves chunks at runtime. Requires chunking, metadata, freshness decisions.
    - 3. **Data pipelines.** Knowledge in systems that need to talk to each other; AI processes/routes/transforms data between systems. n8n, Make, Zapier handle plumbing.
    - 4. **Low-code integration tools.** Zapier, Make, Power Automate — connectivity without code. Not AI, but part of the design.
    - 5. **Service layers and APIs.** Engineered code running an agent as a backend service. Most engineered pattern; scales agent teams into production workflows.

- C. **Pattern selection note** *(L127)*
    - 1. Most first Sprints use patterns 1 and 2 with some pattern 4 routing.
    - 2. The point is matching pattern to information problem, not the other way around.

- D. **Pattern comparison table** *(L129-135)* [KEEP]
    - 1. Five rows: Pattern / Best For / Infrastructure Level / Example.

- E. **Try This callout** *(L108-113)* [KEEP] — paste Constraint Statement + flow into Claude/ChatGPT; references Prompt Appendix.

- F. **Pro Tip** *(L137-140)* [KEEP] — don't pick the pattern first; map the flow, then ask which pattern fits.

### VII. The Hybrid Accountability Chart assigns owners to the flow *(currently L38-74)*

  **Heading (proposed, directive):** "The Hybrid Accountability Chart Assigns Owners to the Flow"

  **Reframing note:** Now arrives AFTER information flow + five patterns. Drafter reframes opening to position HAC as *how you assign owners to the flow you just mapped*, not as a standalone chart introduction.

- **Assumes:** reader has the information flow drawn (from §V) and a pattern selected for each step where AI plugs in (from §VI). They have lanes and steps; they don't yet have names against the lanes.
- **Establishes:** the HAC as the chart that assigns owners to the flow. The base concept (one accountability, one name, no shared rows). The Hybrid extension (rows for agent teams, accountability stays with the supervisor). The four questions per row (outcome, agent team name, supervisor, AI-assisted vs Automated). The Right Seat Evaluation (Sees It / Wants It / Suited for It) as the discipline that makes supervisor selection a design decision, not a staffing one. The structural rule: every agent team has a human supervisor, no exceptions.
- **Sets up:** the Human Orchestrator (§VIII) — the named role that *owns the constraint outcome for the Sprint* across the rows the chart just created. The chart names *who supervises each row*; §VIII names *who owns the whole Sprint*. The reader needs that role distinction before any of the four downstream decisions (autonomy level, governance, mini-spec, tool category) make sense.

- A. **The Accountability Chart base concept** *(L43)*
    - 1. Maps who owns what; each row = one accountability + one name. No shared rows. No "the team."
    - 2. EOS readers already have one; non-EOS readers think one-page org chart organized around outcomes.

- B. **The Hybrid extension** *(L45)*
    - 1. Adds rows for agent teams. Every row still names one accountability and one human supervisor.
    - 2. Some rows also name the agent team doing execution under that supervisor.
    - 3. Accountability does not move from human to agent; ownership stays with the supervisor.

- C. **The four questions per row** *(L47-52)* — present as numbered list:
    - 1. **What role or function does this team perform?** The outcome, not the task. ("Produce accurate initial quotes within 2 hours" ≠ "Look up pricing.")
    - 2. **What is the name of the agent team, if applicable?** Name it and scope it. Without a name, no owner, no scope, no question to ask when something breaks.
    - 3. **Who is the human supervisor?** Every row, no exceptions. No "TBD." A name.
    - 4. **Is this accountability *AI-assisted* or *Automated*?** AI-assisted = human-in-the-loop, reviews every output. Automated = human-on-the-loop, monitors by exception.

- D. **Right Seat Evaluation** *(L61-67)* — surface the three tests explicitly:
    - 1. ***Sees It*** — understands the work well enough to evaluate output, not rubber-stamp.
    - 2. ***Wants It*** — genuinely accountable for the outcome, not treating the agent team as someone else's problem.
    - 3. ***Suited for It*** — judgment, context, and authority to override the agent and make the calls it can't.
    - 4. If any test fails: choose someone else, or build the development plan that gets the candidate to all three passing before the Sprint runs.

- E. **Structural rule** *(L59, L74)*
    - 1. Every agent team has a human supervisor — no unowned teams.
    - 2. The four questions are a design discipline, not a template you fill in once and forget.

- F. **Pro Tip** *(L69-72)* [KEEP] — EOS readers already have the muscle; HAC sits alongside the Accountability Chart, not as a rewrite.

- G. **Excalidraw L41 + L57** [KEEP — both diagrams]
    - 1. // AUTHOR REVIEW: existing TODO comment at L40 + L56 notes column-A phrasing must use outcome-based descriptions, not task labels. Drafter should preserve the TODO; Excalidraw redo is out of scope here.

### VIII. Name the Human Orchestrator before build begins *(PROMOTED from L259-291 — FLOW#1)*

  **Heading (proposed, directive):** "Name the Human Orchestrator Before Build Begins"

  **Critical reorder:** This section moves UP from L259 (currently ~80% through the chapter) to immediately after the HAC. This is the chapter's load-bearing role concept; placement has been demoting it. Drafter should extract cleanly — the Design Team section (L293+) stays in its current position later in the chapter.

- **Assumes:** reader has an HAC with rows naming an outcome, an agent team, and a human supervisor each (from §VII). Every row has a name in the supervisor column — but the chart says nothing yet about who owns the *constraint outcome* across all those rows for the Sprint as a whole.
- **Establishes:** the Human Orchestrator as the named role that *owns the Sprint's measurable result against the constraint from Signal*. Distinct from row-level supervision: the Orchestrator sets goals for the agent team, designs the workflow, reviews at the goal level (not the task level), and owns the design improvements between Sprints. Disambiguates from EOS Integrator (full-company role) and COO (handled by 3B sweep `book-8v6v.32`). Names the required capabilities (context management, knowing-what-good-looks-like, communication across agents and platforms), the disposition (authority over the workflow, comfort with ambiguity, willingness to shift from executing to designing), the development gap (operations leads excellent at executing now asked to design), and the ramp pattern (Sprint 1 guided, Sprint 2 independent, Sprint 4 improving). Names day-to-day ownership (clean inputs, output review, drift detection).
- **Sets up:** the three Sprint-level design decisions the Orchestrator now owns — autonomy level (§IX), governance (§X), and the per-agent specification work (§XI mini-spec + §XII tool category). The chart and the Orchestrator together define *who*; §IX–§XII define *how*. The reader needs the Orchestrator named before any of those four decisions becomes meaningful.

- A. **What the Human Orchestrator owns** *(L261-267)*
    - 1. Design produces a workflow specification, a HAC entry, AND a role: the Human Orchestrator for this accountability.
    - 2. Sprint-level role: sets goals for the agent team, designs the workflow, owns the constraint outcome for one Sprint.
    - 3. Reviews at the goal level, not the task level. Asks whether the team is moving the constraint, not whether every output line is correct.
    - 4. Owns the design improvements between Sprints — eight Sprints of one good change each compounds into a substantially more capable team.

- B. **Orchestrator vs. EOS Integrator disambiguation** *(L265)* — handled by 3B sweep `book-8v6v.32`; Drafter should NOT alter the disambiguation wording.

- C. **Callback to Chapter 3** *(L269)* [KEEP]
    - 1. Marketing lead running four agent teams in parallel — that shift was designed, not improvised.

- D. **Finding the right person** *(L272-282)*

    **H3 (proposed):** "Pick the Person Who Owns the Outcome"

    - 1. Required capabilities (skills of good management): context management, knowing what good looks like, communicating across agents and platforms, working understanding of tools and information each agent needs.
    - 2. Required disposition: authority over the workflow and constraint outcome; comfort with ambiguity; willingness to shift from executing to designing.
    - 3. Best candidate: usually the person closest to the work who's also frustrated by the parts that don't require their skill.
    - 4. Development gap is real: the operations lead excellent at executing is now being asked to design — different role, deliberate work to develop, not a personality change.
    - 5. Budget for upskilling. It isn't optional.

- E. **Ramp-up pattern** *(L284)* — present as explicit sequence:
    - 1. **Sprint 1:** guided — Orchestrator runs Design with support (Compound coach or step-by-step question sequence). Someone experienced coaches the process, doesn't do the work.
    - 2. **Sprint 2:** independent — Orchestrator runs the process on their own.
    - 3. **Sprint 4:** improving — Orchestrator improves the process.
    - 4. Skill learned by doing, one Sprint at a time, not in training.

- F. **Day-to-day ownership** *(L291)* [KEEP]
    - 1. Orchestrator also owns operation of the agent team: clean inputs, output review at the appropriate frequency, flagging design drift.
    - 2. Drift signals: inputs degrading, outputs trending off, decisions no longer handled cleanly.
    - 3. In a 25-person company that's part of the Orchestrator's role; in a 100-person company they may delegate day-to-day monitoring, but accountability stays with them.

- G. **Action Step** *(L286-289)* [KEEP]
    - 1. Identify your Human Orchestrator candidate. Authority over the outcome? Willing to shift from executing to designing? Name them. If there's a development gap, name it and plan Sprint 1 as the ramp.

### IX. Start AI-assisted. Earn automation. *(currently L142-165)* [KEEP, light touch]

  **Heading (proposed, directive):** "Start AI-Assisted. Earn Automation."

- **Assumes:** reader has an HAC (from §VII) and a named Orchestrator (from §VIII). The fourth question on the HAC — AI-assisted or Automated — is now in front of them as a design decision they own.
- **Establishes:** the rule (always start AI-assisted; no exceptions), the spectrum (not a binary; shifts over time as the team learns which decisions the agent gets right reliably), the worked progression (Quote Generation Team: every-draft review → draft-and-send-with-approval → full automation with contract-level approval), and the move-toward-automated trigger (rubber-stamping more often than not). Autonomy is a governance decision, not a capability decision.
- **Sets up:** governance (§X) — the autonomy spectrum only works if the system underneath it answers what the agent is allowed to do and what it isn't. §IX names the position; §X locks the rails.

- A. **The fourth question is a design decision** *(L144)*
    - 1. Not a technology decision. The one operators get wrong most often.

- B. **The starting position** *(L146)*
    - 1. Always start AI-assisted. Every accountability, every agent team, every Sprint — human in the loop reviewing every output. No exceptions.
    - 2. Progression toward automation isn't about reducing review frequency. It's about moving the human's role toward exceptions and final decisions.

- C. **Worked example: Quote Generation Team** *(L148)* [KEEP]
    - 1. Sprint 1: human reviews every draft and sends to customer.
    - 2. Later: agent drafts and sends; human approves before email goes out.
    - 3. Eventually: agent on website fully automates quotes, subject to human approval before any contract is signed.
    - 4. The human never leaves the workflow. Position changes from line-by-line review to approving final decisions and handling exceptions.

- D. **Spectrum, not binary** *(L150)*
    - 1. Shifts over time. Nothing about the agent changed; the leadership team learned which decisions the agent gets right reliably.

- E. **Excalidraw L152** [KEEP] — AI-assisted-to-Automated spectrum.

- F. **Move toward automated when** *(L154-156)*
    - 1. The human is rubber-stamping more often than not.
    - 2. Autonomy level is a governance decision, not a capability decision.
    - 3. Start with more guardrails than you think you need. Loosening is easy; recovering from an unreviewed bad output is expensive.

- G. **Action Step** *(L161-163)* [KEEP]
    - 1. For each accountability, place it on the spectrum. Write the rationale. "AI-assisted because exception rules aren't fully documented yet" is a rationale; "AI-assisted" alone is a checkbox.

### X. Lock governance before the build begins *(currently L167-188)* [KEEP, surface as 5-question artifact]

  **Heading (proposed, directive):** "Lock Governance Before the Build Begins"

- **Assumes:** reader has placed each accountability on the AI-assisted-to-Automated spectrum (from §IX) and understands autonomy is a governance call.
- **Establishes:** governance as a design decision made in the same session as the workflow — not a separate compliance review, not a post-deployment document. Five questions per agent team: data access, actions without approval, escalation on unrecognized input, quality monitoring, kill switch. Names both failure modes (build-first/permission-later AND review-cycles-that-prevent-building).
- **Sets up:** the mini-spec (§XI), where the governance answers land *agent by agent* in the Judgment and Escalation rules field. §X writes the rules at the team level; §XI attaches them to a specific agent specification Build can execute against.

- A. **The governance question** *(L169-171)*
    - 1. What is this system allowed to do, and what is it not allowed to do?
    - 2. Failure modes: build first / permission later, OR review cycles that ensure nothing gets built.
    - 3. Third way: governance is a design decision, made in the same session as the workflow. Not a separate compliance review. Not a post-deployment document.

- B. **The five questions per agent team** *(L173-183)* — number explicitly:
    - 1. **What data can agents access? What's off-limits?** Name the systems and document sets the agent can read; name what it can't touch (PII, financial records above a threshold, regulated data). Lock access at the source, not at processing time.
    - 2. **What actions can agents take without approval? What requires human sign-off?** Draw the line where output leaves internal review.
    - 3. **What happens when an agent encounters something it wasn't designed for?** Define the escalation path: who gets the flag, how fast, what the agent does while waiting.
    - 4. **How will you monitor output quality?** Full review (AI-assisted), spot checks (transition), or dashboard with exception flags (automated). Pick one. Write it down.
    - 5. **What would cause you to shut down an agent workflow immediately?** Define the kill switch. Not hypothetical — the conditions under which the system stops, and everybody knows it.

- C. **Pro Tip** *(L185-188)* [KEEP] — the "does this workflow need an interface?" question is a governance question in disguise; interface decision follows from autonomy level.

### XI. Every agent gets a six-field mini-spec *(currently L190-216)* [KEEP, HBR trim]

  **Heading (proposed, directive):** "Every Agent Gets a Six-Field Mini-Spec"

- **Assumes:** reader has an HAC with rows for each agent team, an autonomy level per row, and governance answers per team (from §VII, §IX, §X).
- **Establishes:** the mini-spec as the per-agent specification Build inherits. Six fields: system prompt, tools, context sources, memory rules, judgment/escalation rules, oversight load. Every row in the HAC gets a mini-spec. The Bedard ceiling (three high-oversight agents per supervisor; consolidate, raise toward Automated, or split the supervisor role if exceeded) lands here as a design constraint.
- **Sets up:** tool category selection (§XII) — the mini-spec names what the agent *is*; category selection names what kind of environment it *runs on*. The category decision belongs in Design; Build picks the specific product inside the chosen category.

- A. **Framing** *(L192)*
    - 1. The chart names the agent team. The mini-spec names what the agent actually is.
    - 2. Every row in the HAC gets a mini-spec. The mini-spec is what you hand to Build.

- B. **The six fields** *(L194-201)* — number explicitly:
    - 1. **System prompt.** Operating rules. Who the agent is, what it's accountable for, what it does and doesn't decide. Three to five sentences.
    - 2. **Tools.** What the agent can call. APIs, search, file access, named systems. Named by name.
    - 3. **Context sources.** Which Knowledge Map rows feed this agent. If the source isn't on the map, it isn't a source.
    - 4. **Memory rules.** What the agent tracks across runs. Most first-Sprint agents have no memory; saying so is part of the spec.
    - 5. **Judgment and escalation rules.** When the agent escalates, what it refuses, what triggers a hand-off. Governance answers from §X land here, agent by agent.
    - 6. **Oversight load.** Low / Medium / High. How much of the supervisor's attention per run.

- C. **Blank mini-spec template** *(L203-212)* [KEEP] — six-row, two-column fillable table. One per agent on the HAC.

- D. **HBR citation trim** *(L214-216)*:
    - 1. **KEEP:** Bedard 3-agent ceiling *(L214)* — more consequential design constraint; reused downstream in Ch 7b + Ch 8. One paragraph: BCG / March 2026 HBR, productivity inverts after three concurrent AI agents per supervisor; cap at three high-oversight agents under one supervisor. If a supervisor's row count exceeds three, consolidate, raise some toward Automated, or split the supervisor role.
    - 2. **CUT:** AWS/Effectual supervisor-capability check *(L216)* — compress to one sentence without attribution: "The supervisor has to be able to trace decisions, challenge outputs, and apply expertise; if any of the three is missing for an agent on the chart, that agent isn't ready to run."
    - 3. // AUTHOR REVIEW: Drafter sign-off needed on whether the trimmed sentence carries the AWS thought without the attribution, or whether the sentence itself should be cut entirely and the discipline carried by prose around the Bedard ceiling.

### XII. Pick the tool category before you pick the tool *(currently L218-257)* [KEEP, light touch]

  **Heading (proposed, directive):** "Pick the Tool Category Before You Pick the Tool"

- **Assumes:** reader has a mini-spec for every agent on the chart (from §XI). They know what each agent *is*; they don't yet know what kind of environment it runs on.
- **Establishes:** category as a design decision, not a Build decision. Three categories (off-the-shelf, low-code/no-code, hand-built) with three ordered decision questions (mature product? composed of standard primitives? scale/system-of-record/data-sensitivity rules out third-party?). The marketing-lead vs PM-agent-team worked example shows two categories chosen in the same Sprint. The current-tools table is a stable-category, rotating-product reference. If a vendor relationship or market trend is doing the choosing, the design isn't.
- **Sets up:** the Design Team (§XIII) — the function that owns the design work at company scale, especially in companies where Design crosses multiple functions and a single Orchestrator can't see all the dependencies.

- A. **Why category belongs in Design, not Build** *(L220)*
    - 1. Design chooses the category; Build picks the specific environment inside it.
    - 2. A team picking by existing relationship or launch-post recency is making a design decision under cover of Build, and they'll pay for it.

- B. **The three categories** *(L222-228)*:
    - 1. **Off-the-shelf tool.** Existing software that maps to the workflow with light configuration. Use when a mature product already does what the design requires.
    - 2. **Low-code or no-code workflow.** Zapier, Make, Airtable, n8n, Claude project with skills and connectors. The team owns it directly. Use when the workflow is custom but built from standard primitives.
    - 3. **Hand-built integration.** Custom code, API to a system of record, engineer in the loop. Use when the workflow runs at a scale or against a system low-code tools can't reach, or when data sensitivity rules out a third-party platform.

- C. **Excalidraw L230** [KEEP] — three-category decision flowchart.

- D. **Three decision questions in order** *(L232-236)*:
    - 1. Does a mature product already do exactly what this agent requires, with light configuration? If yes, off-the-shelf.
    - 2. Is the workflow custom but composed of standard moves? If yes, low-code.
    - 3. Does the workflow run at a scale, or touch a system of record, low-code can't reach? Or does data sensitivity rule out a third-party platform? If yes, hand-built.

- E. **Worked example: marketing lead vs. PM agent team** *(L238)* [KEEP]
    - 1. Four-agent marketing setup = low-code build (skills wired, projects connected, tools configured).
    - 2. PM agent team that replaced the coordinator = hand-built (server, always-on, real-time across projects/comms).
    - 3. Same Sprint discipline, different category. Design phase named both before Build started either one.

- F. **The current tools table** *(L240-252)* [KEEP] — five-row reference (Conversational AI workspace, Agent platforms with tool use, Low-code automation, Embedded vendor AI, Hand-built integration). Categories stable; products rotate.

- G. **Action Step** *(L254-257)* [KEEP] — for every agent in the HAC, name the category and the one-sentence reason. If you can't write the reason without guessing, the design isn't done.

### XIII. The Design Team is functional, not a committee *(currently L293-308)* [KEEP, light touch]

  **Heading (proposed, directive):** "The Design Team Is Functional, Not a Committee"

- **Assumes:** reader has all four Design deliverables (HAC entries, governance answers, mini-specs, category choices) for their constraint workflow — Sprint-level. They're now asking *who runs this at company scale across many Sprints?*
- **Establishes:** the Design Team as a functional, cross-functional team (not a committee), owned by operating leadership (COO; Integrator in EOS), with a defined charter (research, analyze, benchmark, roadmap, prioritized backlog). The output is the Design Brief — the artifact Build inherits. EOS L10 is distinct from Design Team meetings; keep them separate even if participants and timing overlap.
- **Sets up:** the populated worked example (§XIV) where every concept in the chapter lands in one company's chart for one constraint. The Design Brief preview hands off to Ch 7b.

- A. **Scale** *(L295)*
    - 1. Company of 25: CEO + one direct report at a whiteboard.
    - 2. Company of 100: cross-functional Design Team with a charter.

- B. **Ownership and scope** *(L297)*
    - 1. Functional team, not a committee. Owned by company-level operating leadership (COO; Integrator in EOS companies).
    - 2. Scope: research the constraint, analyze, benchmark, build a roadmap, maintain a prioritized backlog of design work.
    - 3. Members: Human Orchestrator candidate, whoever understands the data/systems, whoever has decision authority on the workflow.

- C. **The charter** *(L299)*
    - 1. Owns design of Human+AI workflows. Meets on cadence (weekly during Sprints, biweekly between). Produces HAC entries and workflow specifications. Does not build.

- D. **Cross-functional dependency catch** *(L301)*
    - 1. Quoting touches sales, ops, engineering. Content touches marketing and client delivery. Cross-functional rep catches dependencies a single-function session misses.

- E. **The Design Brief preview** *(L303)*
    - 1. The artifact that comes out of the Design Team is the *Design Brief* — captures design decisions, stakeholders, systems, and specifications Build inherits.
    - 2. Next chapter introduces the Design Brief in detail. Chapter 8 then shows how the Build Spec is derived from it.

- F. **Pro Tip** *(L305-308)* [KEEP] — EOS L10 overlaps with Design Team but isn't the same; keep them distinct even if they share participants and timing.

### XIV. Meridian's populated Hybrid Accountability Chart *(currently L310-351)* [KEEP]

  **Heading (proposed, directive):** "Meridian's Populated Hybrid Accountability Chart"

- **Assumes:** reader understands every framework concept in §I–§XIII abstractly. They've seen the HAC structure, the four questions, the Right Seat Evaluation, the five governance questions, the mini-spec fields, the three categories. What they haven't seen is *all of it landed in one company at one moment*.
- **Establishes:** Meridian's populated chart — five rows, three agent teams under Elena Ruiz, two human-only rows for Ty Banfield (sales) and Dave Kowalski (engineering), Elena named as Human Orchestrator, all five guardrail questions answered. This is the worked-example proof that the framework lands in real numbers and real names.
- **Sets up:** the closing handoff to Ch 7b (designing the work), which builds the Design Brief on top of this populated HAC.

- A. **Constraint recap from Signal** *(L314)* [KEEP] — Elena Ruiz quoting bottleneck; 3-5 day vs 24-48 hour; $558K annual cost.
- B. **Knowledge Map recap from Source** *(L316)* [KEEP] — HubSpot, JobBOSS, Customer Notes.xlsx (147 → 112), organic and missing sources.
- C. **Blank HAC template** *(L320-327)* [KEEP] — 4-column fillable table (Role/Function, Agent Team, Human Supervisor, Level).
- D. **Populated chart** *(L329-337)* [KEEP] — 5 rows (Quote Research, Quote Pricing, Quote Assembly, Quote delivery, Non-standard consultation).
- E. **Human Roles section** *(L339-341)* [KEEP] — Elena Ruiz as Human Orchestrator; Dave Kowalski as escalation.
- F. **Guardrails — five answered** *(L343-349)* [KEEP] — data access, actions, escalation, monitoring, kill switch.

### XV. Closing handoff *(currently L351)* [REWRITE]

- **Assumes:** reader has seen the framework populated for one company (from §XIV).
- **Establishes:** that Designing the System is complete; the next chapter designs the work itself.
- **Sets up:** Ch 7b (TML deconstruction, Design Brief, gate checklist).

- A. Current: *"The next chapter covers the work itself — Work Deconstruction, populated examples, prototyping, the Design Brief, and the gate checklist that separates Design from Build."*
- B. Proposed (tighter): *"The next chapter designs the work itself: TML deconstruction, populated chart, and the Design Brief that locks the gate."*

### XVI. Reflection Questions *(L353-358)* [KEEP, trim to 3-4]

- **Assumes:** reader has read the chapter end-to-end and seen Meridian's populated example.
- **Establishes:** four reflective prompts that drive the leadership-team Design session.
- **Sets up:** the actual Design session that produces this Sprint's HAC entry and mini-spec.

- A. HAC four-question fill (outcome, agent team name, supervisor, AI-assisted vs. automated) for at least one accountability. Blank = your Design session.
- B. Information flow decision points — rule-based vs. judgment-based — and which of the five connection patterns fits the rule-based portion.
- C. Human Orchestrator identification — authority over outcome + willingness to shift from executing to designing. If there's a development gap, what does the ramp look like?
- D. Five governance questions answered now (data access, actions, unrecognized input, quality monitoring, kill switch). Any unanswered question is a Design gap surfacing in Build at 5× cost.

---

## Heading inventory — current → proposed (full set)

| Current heading *(L#)* | Proposed directive heading |
|---|---|
| `# *Designing the System*.` *(L1)* | `# Designing the System: Every Row Has a Name` *(or with main-idea clause from title)* |
| `## What Design *produces*.` *(L26)* | `## Design Has Four Deliverables` |
| `## The *Hybrid Accountability Chart*.` *(L38)* | *(MOVED — now arrives after info flow + five patterns)* `## The Hybrid Accountability Chart Assigns Owners to the Flow` |
| `## The *information flow* question.` *(L76)* | *(PROMOTED earlier)* `## See the Work as Information Flow First` |
| `## How AI connects to *information*.` *(L104)* | `## Map AI to Information Flow Using Five Patterns` *(folds under info-flow section)* |
| `## AI-assisted or *automated*.` *(L142)* | `## Start AI-Assisted. Earn Automation.` |
| `## Governance and *guardrails*.` *(L167)* | `## Lock Governance Before the Build Begins` |
| `## The *agent mini-spec*.` *(L190)* | `## Every Agent Gets a Six-Field Mini-Spec` |
| `## Tool *category* selection.` *(L218)* | `## Pick the Tool Category Before You Pick the Tool` |
| `### The current tools.` *(L240)* | `### The Current Tools` *(keep as H3 under category selection)* |
| `## The *Human Orchestrator*.` *(L259)* | *(PROMOTED earlier — after HAC)* `## Name the Human Orchestrator Before Build Begins` |
| `### Finding the right *person*.` *(L272)* | `### Pick the Person Who Owns the Outcome` |
| `## The *Design Team*.` *(L293)* | `## The Design Team Is Functional, Not a Committee` |
| `## The populated *example*.` *(L310)* | `## Meridian's Populated Hybrid Accountability Chart` |
| `## Reflection Questions` *(L353)* | `## Reflection Questions` *(conventional; keep)* |

---

## Meridian thread (per [[meridian-as-side-by-side-thread]])

**Status:** Strong. Ch 7 is already on the reference-model list ("Meridian HAC") for chapters with strong side-by-side Meridian presence. The risk after the FLOW#1 reorder is structural — the canonical populated example sits at §XIV (chapter close). After the reorder, §VII (HAC) introduces the chart without showing it landed in a real company until twelve pages later. Meridian needs at least one earlier touch — at the *concept introduction*, not the tail-end illustration — to satisfy the [[meridian-as-side-by-side-thread]] rule.

**Meridian landing points (post-reorder):**

1. **§V Information flow first** — Meridian's quoting workflow is the standing example the reader will see populated at §XIV. Land one sentence at §V.A or §V.B grounding the information-flow concept in the Meridian flow: *"At Meridian, the quoting workflow pulls customer data from HubSpot, matches it against pricing tables in JobBOSS, applies exception rules from a 147-row spreadsheet on Elena's desktop, and assembles the result into a customer-readable format. That's the information flow. The Knowledge Map from Source named where each piece lives; this section is how those pieces move."* Connects the prior chapter's Meridian work (Source/Knowledge Map) directly to the current chapter's first concept.

2. **§VII HAC concept introduction** — [NEW recommended Meridian touch]: at the moment the HAC is introduced (after the §V→§VI setup), surface a one-line forward reference: *"Meridian's chart, populated at the end of this chapter, has five rows — three under Elena Ruiz as the agent supervisor, two human-only rows. Every row has a name."* This satisfies the [[meridian-as-side-by-side-thread]] rule that Meridian appears *at the concept introduction*, not only as the tail-end worked example. Without this touch, the reader meets the HAC abstractly for twelve pages before seeing it land.

3. **§VIII Human Orchestrator** — [NEW recommended Meridian touch]: at the role's introduction (its first major appearance after promotion), land one sentence: *"Meridian's Orchestrator is Elena Ruiz — VP of Operations, the same person the constraint exposed in Signal as the bottleneck. The role names what she now owns differently: not every quote, but the constraint outcome for the Sprint."* Makes the role concrete at the point of introduction; reinforces the through-line from Signal (Elena as bottleneck) to Design (Elena as Orchestrator).

4. **§XIV Populated HAC** — [KEEP] the canonical worked artifact stays where it is. Five rows, three agent teams, named Orchestrator, five guardrail answers. This is the chapter's best in-body Meridian content.

**Why this matters:** the FLOW#1 reorder moves the HAC concept earlier in the chapter, but the populated chart still sits at the end. Without earlier Meridian touches at §VII (HAC intro) and §VIII (Orchestrator intro), the framework introductions become abstract for the bulk of the chapter — a regression against [[meridian-as-side-by-side-thread]]. The two new sentences above bring Meridian's appearance *structurally adjacent* to the concept introductions, preserving the reorder's promotion of practice while keeping the worked example in its strongest natural position at §XIV.

---

## Artifacts (placed in context)

| Artifact | Status | Phase 3B placement |
|---|---|---|
| Hybrid Accountability Chart blank template (4 columns: Role/Function, Agent Team, Human Supervisor, Level) | Phase 3B adds in-body fillable template at ~L309 *(before populated Meridian chart)* | Per consolidated artifact bead. |
| Right Seat Evaluation (3 tests: Sees It / Wants It / Suited for It) | Inline prose L63-67 today | Phase 3B surfaces as explicit in-body checklist artifact. |
| Information Flow Specification template (4 fields: feeds, transformations, decisions, outputs) | Prose only at L82-87 | **NEW recommended:** Phase 3B adds in-body fillable template. |
| Swim lane diagram | Excalidraw L93 | Keep. |
| AI-assisted-to-automated spectrum | Excalidraw L152 | Keep. |
| Five-question governance checklist | Inline prose L173-183 today | Phase 3B surfaces as explicit in-body table — one row per question, one column for the agent team's answer. |
| Agent mini-spec blank template (6 fields) | In-body L205-212 today | Phase 3B adds in-body fillable template at ~L203 *(canonical 6-field reference)*. |
| Tool category decision flowchart | Excalidraw L230 | Keep. |
| Current tools reference table | In-body L244-250 | Keep — solid in-body reference. |
| Meridian populated HAC | In-body L329-337 | Best in-body artifact in the chapter. Keep verbatim. |

---

## HBR citation discipline (this chapter)

**Current count:** 2 distinct HBR citations.
- Bedard "3-agent ceiling" *(L214)* — BCG, March 2026 HBR, "When Using AI Leads to 'Brain Fry.'"
- AWS/Effectual supervisor-capability check *(L216)* — HBR sponsor content, June 2026.

Both citations cluster in the same section, making it read heavy even though raw count is at the cap.

**Trim plan (per memory: cap 1-2; never scaffold a chapter around them):**
- **KEEP:** Bedard 3-agent ceiling. More consequential design constraint; reused downstream in Ch 7b + Ch 8. Keep the paragraph as a structural design rule, not as a quote pile.
- **CUT or COMPRESS:** AWS/Effectual capability check. Either compress to one un-attributed sentence ("trace decisions, challenge outputs, apply expertise") or cut entirely and let the Right Seat Evaluation in §VII carry the load.
- // AUTHOR REVIEW: Drafter sign-off needed on cut-vs-compress for the AWS reference. Recommendation: compress without attribution.

---

## Cross-chapter dependencies handled in Phase 3B (Drafter does NOT re-solve)

- ARC#13 (`book-8v6v.32`) — COO / EOS Integrator / Orchestrator conflation at L265 + L282 + L297. Handled by 3B sweep; Drafter does NOT touch the disambiguation wording.
- ARC#6 (`book-g404`) — EOS terms scoped (Accountability Chart, L10, Integrator, Rocks). Handled by 3B.
- ARC#3 (`book-xqxi`) — Jargon parentheticals (n8n at L121, service layer / API at L125, low-code at L226). Handled by 3B.
- Canonical agent definition at first-use *(book-ultm)* — landed in Ch 2 by 3B; the inline agent gloss in the Ch 7 In-Brief callout can be trimmed accordingly.
- SPC through-line — chapter feeds Sprint Planning Canvas Design row; next chapter (Ch 7b) inherits the Design Brief.

---

## Drafter notes

- **Drafter model:** Sonnet. This is mostly reorder + heading rewrite + light trim; ~85% of existing prose survives. The full QC pipeline ([[qc-pipeline-per-chapter]]) MUST run: Drafter → EC → Deflourisher → Voice Scan → Prose-Craft → Editor → orchestrator gate. No bundling. No skipping.
- **Biggest move:** FLOW#1 reorder. Information flow + five patterns BEFORE the HAC. Human Orchestrator promoted up immediately after the HAC. Drafter should preserve the existing prose; this is mostly cut-and-paste with section transitions tightened.
- **Anchoring discipline:** the Drafter reads the chapter syllogism + each section's Assumes/Establishes/Sets up triad BEFORE writing. Sentence-to-sentence decisions inside a section must respect the section's flow markers. The reorder is fragile precisely because §V's Sets up has to lead into §VII's Assumes (the flow-to-chart handoff) and §VII's Sets up has to lead into §VIII's Assumes (the chart-to-Orchestrator handoff). If a transition sentence at one of those joins violates a marker, the reorder reads as juggling instead of inevitability — and the EC agent will flag it.
- **Re-read pass:** after structural edits land, Drafter reads the chapter end-to-end and checks: (a) every pronoun has an antecedent within 3 sentences; (b) every citation retains its quoted context or is cut; (c) every chart/Excalidraw sits adjacent to the prose that references it (the HAC intro Excalidraw at L41 must move with the §VII section); (d) every Action Step still fits the section restructure that surrounds it (the §V Action Step at L99-102 must travel with §V; the §VIII Action Step at L286-289 must travel with §VIII); (e) the chapter syllogism is intact end-to-end. EC will check these too, but Drafter doing this first reduces the EC delta.
- **Meridian thread:** apply at all four landing points listed in the Meridian thread section above. The two NEW recommended touches (§VII HAC intro forward-reference; §VIII Orchestrator intro Elena sentence) are not optional — without them, the FLOW#1 reorder leaves Meridian's appearance as tail-end illustration only, which violates [[meridian-as-side-by-side-thread]].
- Voice charter applies. Strip italic-fragment heading style. No em-dashes. No triplet pileups.
- **No tools:** Drafter does NOT run deflourish, voice-scan, prose-craft, or any other tool. Those are separate pipeline stages. Drafter does structural edits, then returns summary. (Deflourish runs as its own pipeline stage per [[deflourish-is-non-negotiable]] — non-negotiable; the EC verdict does not gate it.)
- Cross-coherence check against Ch 6 (Source — Knowledge Map handoff feeds info-flow section), Ch 7b (Design Brief preview must still resolve), and Ch 8 (Build Spec derivation must still resolve).
- Verify references to "Chapter 3" / "Chapter 7b" / "Chapter 8" still resolve correctly post-renumbering.

**AUTHOR FOLLOWUP items already on the table:**
- AWS/Effectual citation: cut-vs-compress decision in §XI.D.2 (recommendation: compress without attribution).
- Chapter title choice between *"Every Row Has a Name"* (recommended; mirrors the chapter's "no exceptions" gate language) and the longer *"Build the Hybrid Accountability Chart Before You Build Anything Else"*.
- Confirmation that the Human Orchestrator section can be cleanly extracted from L259-291 without disturbing the Design Team section that follows it at L293+ (the L291 day-to-day-ownership paragraph travels WITH §VIII, not with the Design Team section).
- Two NEW Meridian thread touches at §VII (HAC intro) and §VIII (Orchestrator intro): one-sentence each, per the Meridian thread section above. Confirm voice and content before Drafter dispatches.
- Excalidraw rebuilds (TODO comments at L40, L56) — out of scope for this Drafter pass; preserve the TODO markers verbatim.
