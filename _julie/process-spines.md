# Process-Spine Registry

**Source of truth** for every step-driven process in *Co-Intelligent Co-Operation*. This file drives two consumers that must never drift:

1. **Worksheets** (`worksheets/html/*-standalone.html`) — the printable/interactive do-it artifacts.
2. **The book's "the moves" overview sections** — the in-chapter list of steps a reader walks.

**Rule:** there is ONE canonical set of step labels + one-line "why" per process. Both the worksheet and the book overview use these labels and whys **verbatim**. Edit here first; propagate out.

**Spine state legend:**

- **Visible** — the ordered steps are already present and legible in the chapter prose. Needs only label alignment to this registry.
- **Buried** — the process exists in the chapter but the steps are scattered / implicit / not presented as a numbered spine. Needs the spine SURFACED.
- **Absent** — no step sequence in the chapter yet. Needs the spine written into the book.

(No process in the current audit set is Absent. All are Visible or Buried.)

---

## 1. Master table

| # | Process | Chapter | Section anchor | Worksheet slug | Spine state | # steps |
|---|---------|---------|----------------|----------------|-------------|---------|
| 1 | Calculate Revenue per Employee | 01-diagnosis | The Headcount *Paradox* | `revenue-per-employee` | Buried | 6 |
| 2 | Run the AI Readiness Scorecard | 01-diagnosis | Score Your AI *Readiness* | `ai-readiness-scorecard` | Visible | 7 |
| 3 | Take Stock of the Operating-Model Gap | 02-beliefs | — | `take-stock-operating-model-gap` | **REMOVED** | — |
| 4 | Run the Two-Column Role Sort | 02-co-operating-model | Humans own outcomes. Agents own *tasks*. | `two-column-role-sort` | Buried | 5 |
| 5 | Calculate the Design Opportunity | 02-co-operating-model | Two patterns: human-supervised, *agent*-supervised. | `calculate-design-opportunity` | Buried | 5 |
| 6 | Map the Hybrid Split | 02-co-operating-model | Two patterns: human-supervised, *agent*-supervised. | `map-hybrid-split` | Buried | 5 |
| 7 | Fill in the Sprint Planning Canvas | 03-the-framework | The Sprint Planning Canvas asks one *question* per stage | `sprint-planning-canvas` | Visible | 6 |
| 8 | Run the Signal Session | 04-signal | Run the *Signal* session | `run-signal-session` (ships as `signal`) | Buried | 7 |
| 8a | Build the Constraint Backlog | 04-signal | Build the *Constraint Backlog* and select the one | `constraint-backlog` | Buried | 6 |
| 9 | Build the Knowledge Map | 05-source | Build the map in three passes. | `build-knowledge-map` (ships as `knowledge-that-walks`) | Visible | 6 |
| 10 | Classify each source on the map | 05-source | Classify what you found. | `classify-sources` | Buried | 4 |
| 11 | Write the Information Flow Specification | 06-designing-the-system | See the work as information flow first | `information-flow-spec` (ships as `map-the-inputs`) | Buried | 6 |
| 12 | Build the Hybrid Accountability Chart | 06-designing-the-system | The Hybrid Accountability Chart assigns owners to the flow | `hybrid-accountability-chart` | Visible | 6 |
| 13 | Write the Agent Mini-Spec | 06-designing-the-system | Every agent gets a six-field mini-spec | `agent-mini-spec` | Visible | 7 |
| 14 | Work Deconstruction | 06b-designing-the-work | Deconstruct the work task by task. | `work-deconstruction` | Buried | 5 |
| 15 | Write the Design Brief | 06b-designing-the-work | The Design Brief is what Build inherits. | `design-brief` | Visible | 7 |
| 16 | Write the Agent Mini-Spec (DUP of #13) | 06b-designing-the-work | Specify every agent with a six-field mini-spec. | `agent-mini-spec` | Visible | 6 |
| 17 | Write the eight-section Build Spec | 07-build | Write the eight-section Build *Spec*. | `write-build-spec` | Visible | 8 |
| 18 | Audit the spec against seven common failures | 07-build | Audit the spec against seven common *failures*. | `audit-spec-failures` | Visible | 7 |
| 19 | Answer the seven Guardrails Checklist questions | 07-build | Answer the seven *guardrails* questions in writing. | `guardrails-checklist` | Visible | 7 |
| 20 | Run the Deploy Readiness Audit | 08-deliver | The *Deploy Readiness Audit*. | `deploy-readiness-audit` | Visible | 5 |
| 21 | Write the Per-Role Runbook | 08-deliver | The *per-role runbook*. | `per-role-runbook` | Buried | 5 |
| 22 | Build and Maintain the Operational Log | 08-deliver | What gets *logged*. | `operational-log` | Visible | 5 |
| 23 | Measure the Sprint Outcome | 08-deliver | The *measurement* question. | `sprint-outcome-measurement` | Visible | 5 |
| 24 | Run the Sprint Retrospective | 09-compound | Run the Sprint *Retrospective* honestly | `sprint-retrospective` | Buried | 5 |
| 25 | Install One Design Change | 09-compound | Install one *design change*. Just one. | `install-design-change` | Buried | 5 |
| 26 | Re-rank the Constraint Backlog (Constraint Re-rank) | 09-compound | Re-rank the Constraint Backlog on what the *Sprint* taught you | `constraint-re-rank` | Buried | 5 |
| 27 | Run the quarterly operating session | 10-the-rhythm | Run the quarterly operating session in *four steps*. | `quarterly-operating-session` | Visible | 4 |
| 28 | Maintain the Hybrid Org Today | 10-the-rhythm | Maintain one living document: the *Hybrid Org Today*. | `hybrid-org-today` | Buried | 4 |
| 29 | Track compounding on the Compounding Scorecard | 10-the-rhythm | Track compounding on a single *scorecard*. | `compounding-scorecard` | Buried | 4 |
| 30 | Run minimum viable Signal | 11-what-to-do-next | Run *minimum viable Signal* on yourself. | `minimum-viable-signal` | Visible | 3 |
| 31 | Name the Sprint roster | 11-what-to-do-next | Name *three roles*: Orchestrator, Owners, Builder. | `sprint-roster` | Visible | 3 |
| 32 | Fill in the Sprint Planning Canvas (DUP of #7) | 11-what-to-do-next | Fill in the *Sprint Planning Canvas*. | `sprint-planning-canvas` | Buried | 5 |

**32 process entries** across 12 chapters (30 unique processes after deduping #13/#16 and #7/#32 — see §4). *#3 Take-Stock-of-the-Operating-Model-Gap later removed per author; 29 active.*

---

## 2. Canonical spines

Each block below is the verbatim source for both the worksheet and the book overview. Format: ordered step **label** — one-line **why**.

### 1. Calculate Revenue per Employee — `revenue-per-employee`
*01-diagnosis · The Headcount Paradox · Buried*

1. **Pull last-twelve-months revenue** — Establishes the numerator; forces a single agreed-on number before the division.
2. **Count current full-time headcount** — Establishes the denominator; should reflect payroll today, not budgeted seats.
3. **Divide revenue by headcount to get today's baseline** — Produces the per-person productivity proxy that all comparisons anchor to.
4. **Fill in the 'at last major system rollout' row** — Gives a before-AI-investment reference point so the prior tech wave's lift is visible.
5. **Project the '+20% revenue, no new hires' row** — Makes the target slope concrete — shows whether the math is achievable or aspirational.
6. **Read the delta across the three rows** — Surfaces whether prior investment moved the number and whether the AI investment is on track to move it further.

### 2. Run the AI Readiness Scorecard — `ai-readiness-scorecard`
*01-diagnosis · Score Your AI Readiness · Visible*

1. **Assemble the right team** — The Scorecard is designed to surface disagreement; solo scoring misses the organizational signal.
2. **Score all 20 statements 1–5** — Each statement probes one of the five dimensions; honest scoring requires the team to rate the company, not individual performance.
3. **Sum each dimension's four scores into a subtotal out of 20** — Isolates which dimension is weakest so effort can be targeted before the redesign begins.
4. **Add all five subtotals to get the total AI Readiness percentage** — Converts the raw scores into a single number that maps to one of five named readiness buckets.
5. **Read the bucket description for the total score** — Translates the percentage into a starting posture — what to expect from the work ahead.
6. **Identify the lowest dimension subtotal** — Pinpoints where the redesign work will require the most effort and the longest conversations.
7. **Record the three closing-checklist items (overall score, lowest dimension, highest dimension)** — Locks the baseline so progress is measurable and the team has a shared reference as the chapters continue.

### 3. Take Stock of the Operating-Model Gap — `take-stock-operating-model-gap` *(REMOVED)*
*Removed from 02-beliefs per author (edits/fine-tuning, 2026-06): the exercise asked readers to spot "work a system should be doing," a diagnosis they aren't equipped to make in a mindset chapter (if they could, they'd already automate it). Ch 2 now closes with a belief-checklist; real constraint identification happens in the Signal chapter. Worksheet deleted.*

### 4. Run the Two-Column Role Sort — `two-column-role-sort`
*02-co-operating-model · Humans own outcomes. Agents own tasks. · Buried*

1. **Pick a real role** — Grounds the sort in actual work rather than abstract categories; the job description is not the role as it runs.
2. **List the work as it actually happens** — Capturing what the person spends their week on (not the job description) surfaces the tasks that are ripe for redesign.
3. **Sort each task into Column A or Column B** — Column A = judgment that changes based on context a machine cannot observe; Column B = processing that follows rules a machine could learn.
4. **Split compound tasks** — Many tasks contain both a judgment component and a rule-following component; splitting them prevents undercounting Column B.
5. **Read the completed sort** — The distribution of tasks tells you where the design opportunity is and whether a redesign conversation is unavoidable.

### 5. Calculate the Design Opportunity — `calculate-design-opportunity`
*02-co-operating-model · Two patterns: human-supervised, agent-supervised. · Buried*

1. **Count the tasks in each column** — Establishes the ratio of human-intelligence work to agent-intelligence work for this role.
2. **Estimate hours per week for each task** — Converts task count into time, making the misallocation concrete rather than just a fraction.
3. **Calculate the Column B percentage of the role's week** — Produces the headline number — the share of the role that could run on agent intelligence instead of human hours.
4. **Write the single summary sentence** — 'This role is __% Column B' creates a decision-forcing statement the team can react to.
5. **Multiply Column B percentage by the role's loaded annual cost** — Translates the percentage into an annual dollar misallocation — the cost of not redesigning the role.

### 6. Map the Hybrid Split — `map-hybrid-split`
*02-co-operating-model · Two patterns: human-supervised, agent-supervised. · Buried*

1. **Take the completed Column A / Column B sort** — The sort is the raw material; the hybrid split translates it into a redesigned operating picture.
2. **Move Column B tasks into the 'Agent Labors' column** — Names the specific work the agent will own, making the delegation explicit rather than implied.
3. **Move Column A tasks into the 'Human Manages' column** — Names the judgment and direction responsibilities the human retains, clarifying what the redesigned role actually requires.
4. **Add a quality-standard row for the human** — Ensures the human's review responsibility over all agent output is explicit in the design — this is what prevents AI slop shipping under the role's name.
5. **Read the hybrid split as a role description** — The completed table is the shape of the redesigned seat — enough to see whether it is viable and to hand off to Sprint design work.

### 7. Fill in the Sprint Planning Canvas — `sprint-planning-canvas`
*03-the-framework · The Sprint Planning Canvas asks one question per stage · Visible*
**Canonical home for the Sprint Planning Canvas spine. The 11-ch instance (#32) is the abbreviated kickoff version — see §4.**
**REFRAMED (edits/fine-tuning, 2026-06):** the Framework chapter is now an orienting chapter. The Canvas is presented as ONE question per stage (six questions, matching the form diagram), answered across the book — not a fill-it-now nine-step exercise. The in-chapter moves block is a question→teaching-chapter map; the three operating fixtures (sponsor, Orchestrator, review date) and team/review live on the Canvas form (the blank + completed-Meridian excalidraws), not as enumerated steps. Worksheet = the full Canvas form.

1. **Signal — what's the one constraint, and what does it cost?** → Signal chapter. The constraint sentence + its number is the scope boundary the whole Sprint runs against.
2. **Source — what does the org know about it, and where does that knowledge live?** → Source chapter. Surfaces knowledge gaps before Design.
3. **Design — what does the human-and-agent workflow look like, and who owns what?** → Design chapter. Every role, human and agent, gets one named owner.
4. **Build — what gets built, and on what (off-the-shelf, low-code, hand-built)?** → Build chapter. Locks the spec and the path.
5. **Deliver — how do you know it worked, and what number moved?** → Deliver chapter. The per-role landing + the Delivery Test against Signal's number.
6. **Compound — what did you learn, and what changes for the next Sprint?** → Compound chapter. Captures the outcome and re-ranks the queue.

### 8. Run the Signal Session — `run-signal-session` (worksheet ships as `signal`)
*04-signal · Run the Signal session · Buried*

1. **Assemble the room** — The CEO, senior leadership, the relevant function owner, and a facilitator must all be present to validate the constraint.
2. **Surface the symptoms** — Run the surfacing lenses as live questions; write everything down without filtering.
3. **Trace each symptom to root with the Five Whys** — Run the Five Whys out loud until each answer lands on a workflow, handoff, or structural gap — not a person.
4. **Build the Constraint Backlog** — Land each candidate constraint in the standing table; the Backlog is born here and carried forward into every subsequent Sprint.
5. **Select the one** — Filter for eligible candidates, find the load-bearing one, and use cost as the tiebreak only when none clearly governs.
6. **Quantify and write the Constraint Statement** — Write the anchoring sentence and complete the validation record with a cost expressed as a rate or unit per period.
7. **Lock it and check the failure modes** — Run the restate test, read the statement back, and confirm the room agrees before handing off to Source.

### 8a. Build the Constraint Backlog — `constraint-backlog`
*04-signal · Build the Constraint Backlog and select the one · Buried · zooms steps 4–5 of #8*

1. **Enter every candidate constraint in the backlog table** — Land each candidate that survived the Five Whys as a one-line structural statement; the Backlog is born here and carried into every later Sprint.
2. **Fill in owner, closeable, and cost for each row** — A name, a yes/needs-breakdown, and a rate or unit per period — the three fields selection runs on.
3. **Filter for the eligible candidates** — Mark any row with no owner, no cost, or "needs breakdown" as not-ready; it stays in the Backlog but is out of the running.
4. **Find the load-bearing one** — The governing candidate whose removal unblocks or clarifies the others; if one clearly governs, that's the constraint.
5. **Cost tiebreak — only if none clearly governs** — When candidates are independent, commit to the costliest you can close.
6. **Commit the one and record the rest as the standing Backlog** — The selected constraint goes to the Constraint Statement and the Sprint Planning Canvas; the rest persist for the Compound re-rank.

### 9. Build the Knowledge Map — `build-knowledge-map` (worksheet ships as `knowledge-that-walks`)
*05-source · Build the map in three passes · Visible*

1. **Start from the Constraint Statement** — Scopes the entire map to the one validated constraint so no row is extraneous.
2. **Draw the six-column table (Source, Type, Owner, Status, Pipeline, Notes)** — Establishes the shared schema all three passes populate; running both the Knowledge Map and Pipeline Audit together prevents duplicated effort.
3. **Pass 1 — List every digital source that touches the constraint** — Surfaces the named, login-accessible systems first because they are the easiest to enumerate and set the baseline for what is Connected, Manual, or Broken.
4. **Pass 2 — List every person whose judgment the constraint workflow depends on** — Captures organic sources (institutional knowledge held by individuals) and flags single points of failure as AT RISK before the knowledge can walk out the door.
5. **Pass 3 — List every gap: knowledge that should exist but does not appear in Pass 1 or Pass 2** — Naming missing sources before Build begins converts invisible Sprint failure modes into explicit design decisions.
6. **Apply the one-page test** — Forces constraint scope discipline — if the map exceeds one page, rows unrelated to the constraint have crept in and must be cut.

### 10. Classify each source on the map — `classify-sources`
*05-source · Classify what you found · Buried*

1. **Mark each source as structured or unstructured** — Tells Design whether the source is directly queryable or requires an extraction pipeline, which affects cost, speed, and system architecture.
2. **Mark each source as durable or ephemeral** — Filters out knowledge that will not matter in 90 days; only durable knowledge belongs on the map and informs agent design.
3. **Assign each source an AI tier (Tier 1 / Tier 2 / Tier 3 / Not AI-tier)** — Tells Design what is reachable today, what requires extraction work before it is usable, and what must remain human-executed — preventing agents from mixing authoritative and stale sources.
4. **Run the eight-item completeness test** — Acts as a pre-handoff gate ensuring the map covers layers, TML types, pipeline statuses, at-risk flags, gaps, and constraint scope before it goes to Design.

### 11. Write the Information Flow Specification — `information-flow-spec` (worksheet ships as `map-the-inputs`)
*06-designing-the-system · See the work as information flow first · Buried*

1. **Name the accountability** — Pins the spec to one specific outcome so you are describing a workflow, not a job description.
2. **List the data feeds** — Forces you to name every source system and document set that supplies raw material to the work, surfacing hidden dependencies.
3. **Document the processing steps** — Makes the transformation work visible — lookups, comparisons, calculations, formatting — so you can later decide what a rule covers vs. what requires judgment.
4. **Classify each decision: rule-based or judgment-based** — This split is the design hinge: rule-based decisions are AI-automatable; judgment-based ones require a human in the loop.
5. **Define the output and its destination** — Anchors the spec to a measurable deliverable and names who or what receives it, enabling handoff design downstream.
6. **Draw the swim lane diagram** — Puts every actor and every handoff on one page, making fragile multi-handoff flows immediately visible before anything is built.

### 12. Build the Hybrid Accountability Chart — `hybrid-accountability-chart`
*06-designing-the-system · The Hybrid Accountability Chart assigns owners to the flow · Visible*

1. **Name the role/function as an outcome, not a task** — Outcome framing ('produce accurate initial quotes within 2 hours') defines what the row is accountable for; task framing ('look up pricing') describes activity with no clear owner or success criterion.
2. **Name the agent team (or mark None)** — A named team can be pointed to when something goes wrong; 'AI Helper' names nothing useful and dissolves accountability.
3. **Name one human supervisor — no TBD, no shared rows** — Every agent team must have a named human who owns the outcome; blank or shared supervisor cells are a governance failure waiting to surface in production.
4. **Set the autonomy level: AI-Assisted or Automated** — This is a governance decision, not a capability decision; the level determines how much human review sits between the agent output and any consequential action.
5. **Apply the Right Seat Evaluation to the supervisor candidate** — Sees It / Wants It / Suited for It — a supervisor who fails any of the three tests means the chart has a name in the column but ineffective supervision underneath it.
6. **Answer the five governance questions for each row** — Data access, permitted actions, escalation path, quality monitoring method, and kill-switch conditions must be written down before Build begins; unanswered questions become expensive surprises after deployment.

### 13. Write the Agent Mini-Spec — `agent-mini-spec`
*06-designing-the-system · Every agent gets a six-field mini-spec · Visible*
**Canonical home for the Agent Mini-Spec spine. The 06b instance (#16) is the same process — see §4. This 7-step version (system home) is canonical because it adds the tool-category routing step.**

1. **Write the system prompt** — Three-to-five sentences that tell the agent who it is, what it is accountable for, and what it does not decide — the standing operating rules it reads before every task.
2. **List the tools** — Names every API, integration, or system the agent can call; unnamed tools are tools Build has to guess at.
3. **Identify the context sources** — Maps the Knowledge Map rows that feed this agent; if a source is not on the map, it is not a source — this prevents scope creep at the data layer.
4. **Set the memory rules** — Explicitly stating what the agent tracks across runs (or that it tracks nothing) prevents the agent from carrying stale state into new tasks.
5. **Define judgment and escalation rules** — Specifies exactly when the agent escalates, what it refuses, and what triggers a handoff to the human supervisor — the governance answers from the HAC land here, agent by agent.
6. **Rate the oversight load (Low / Medium / High)** — Keeps the supervisor's span of control visible; no supervisor should carry more than three high-oversight agents at once, so this field is the span-of-control check before the spec leaves Design.
7. **Select the tool category (off-the-shelf / low-code / hand-built)** — Locking the category in Design — by running the three routing questions in order — prevents Build from making an architecture decision based on vendor relationships or recency rather than the workflow's actual requirements.

### 14. Work Deconstruction — `work-deconstruction`
*06b-designing-the-work · Deconstruct the work task by task · Buried*

1. **Pull the actual accountability list** — Job descriptions are sanitized; the real weekly task list is what gets classified — you can't sort what you haven't named.
2. **Document source inputs and outputs for each task** — Connecting each task to where its data comes from and where the result goes makes the information flow from Source concrete at task level.
3. **Apply the TML sorting question to each task** — A single binary question — 'would the output need human review every time, or only on exceptions?' — assigns every task to Task, Management, or Leadership without ambiguity.
4. **Tally the three buckets and challenge the Leadership pile** — If more than half land in Leadership, each item must be re-examined — genuine judgment stays, but undocumented rules that look like judgment get reclassified.
5. **Map each classified task to a Hybrid Accountability Chart entry** — Deconstruction is thinking; the chart entry (function, agent team, supervisor, autonomy level) is what makes that thinking durable and actionable for Build.

### 15. Write the Design Brief — `design-brief`
*06b-designing-the-work · The Design Brief is what Build inherits · Visible*

1. **Write the Workflow Summary** — Translates the swim lane or flowchart into written specification — trigger to output, every step, handoff, and decision point named.
2. **Name the Stakeholders** — Identifies the Human Orchestrator, role-change list, downstream consumers, and approvers so accountability is unambiguous before Build begins.
3. **List the Systems** — Every system the workflow touches must be named with the specific data it provides or receives, preventing integration surprises in Build.
4. **Define the Data Requirements** — Specifying what data the agent team needs, where it lives, what format it arrives in, and what happens when it is missing or malformed closes the most common Build failure mode.
5. **State the Success Criteria** — Anchors the brief to the measurable Signal targets so Build knows what it is optimizing for, not just what it is building.
6. **Document Constraints and Guardrails** — Locks the governance decisions from Designing the System — data access, action permissions, escalation paths, quality cadence, kill switch — into the design record before Build inherits it.
7. **Describe the V1 Artifact** — If you cannot describe what the first working version actually produces, the design is not finished — this field forces that decision.

### 16. Write the Agent Mini-Spec (06b instance) — `agent-mini-spec`
*06b-designing-the-work · Specify every agent with a six-field mini-spec · Visible*
**DUPLICATE of #13. Dedupe to the canonical #13 spine. The 06b labels below are kept only as the merge source; do not generate a separate worksheet.**

1. **Write the System Prompt** — Defines what the agent does and, just as explicitly, what it does not do — the operating rules that scope every subsequent decision.
2. **List the Tools** — Every API, integration, or system the agent can call must be named; if a tool is not listed, the agent does not get it.
3. **Cross-reference the Context Sources** — Identifying which Knowledge Map rows feed this agent by row reference makes the spec traceable back to Source and prevents agents being built on undocumented data.
4. **Set the Memory Rules** — Deciding what carries across runs — session state, accumulated decisions, lookback window — determines whether the agent reasons over history or starts fresh each time.
5. **Write the Judgment and Escalation Rules** — The refusal list and escalation triggers are the most important governance element: they define exactly when the agent stops and the human decides.
6. **Assign the Oversight Load and confirm supervisor capability** — Naming Low/Medium/High oversight load (and running the Trace/Challenge/Apply-expertise tests) ensures the supervisor is genuinely in the loop, not rubber-stamping.

### 17. Write the eight-section Build Spec — `write-build-spec`
*07-build · Write the eight-section Build Spec · Visible*

1. **Section 1: Write the workflow summary** — Gives any builder a plain-language end-to-end picture of what they're building before they touch anything.
2. **Section 2: Define the inputs** — Specifies exactly what triggers the workflow and what data enters it, so the builder knows where to reach and how to access it.
3. **Section 3: Define the outputs** — Locks the deliverable form, destination, and recipient so the build can't drift toward something the supervisor can't use.
4. **Section 4: Set agent scope boundaries** — States what the agent handles and what it cannot decide, preventing over-prescription that kills agent effectiveness.
5. **Section 5: Name the human supervisor role** — Identifies who reviews, what they review for, and what the handoff looks like — the accountability anchor for the whole build.
6. **Section 6: List every system and integration** — Documents read/write access, authentication method, and data sensitivity for every system touched so nothing is wired by assumption.
7. **Section 7: Document the failure modes** — Pre-decides what happens on every edge case and outage so the builder wires escalation paths instead of improvising them under pressure.
8. **Section 8: Specify the environment and constraints** — Locks which specific platform within Design's category the build runs on and any data residency, license, or security constraints.

### 18. Audit the spec against seven common failures — `audit-spec-failures`
*07-build · Audit the spec against seven common failures · Visible*

1. **Check 1: Search for existing capabilities before building** — Prevents rebuilding what already exists — the most common implementation failure, which is a research gap, not a technical one.
2. **Check 2: Confirm the environment matches Design's category** — Stops a builder from substituting a 'cleaner' architecture for the one the spec actually calls for.
3. **Check 3: Verify the spec is complete before build starts** — Every empty section becomes an on-the-fly decision that won't match Design's intent.
4. **Check 4: Confirm the output lands where the work already lives** — A workflow that outputs to a tool no one opens produces zero adoption regardless of technical quality.
5. **Check 5: Verify Section 7 (failure modes) is populated** — A build that only handles the happy path breaks on the first edge case.
6. **Check 6: Confirm the build handles real-world edge cases, not just the demo path** — A demo shows the happy path; the build must handle missing data, system outages, and off-script inputs.
7. **Check 7: Require testing against real inputs before declaring done** — Synthetic and cherry-picked examples are not tests; last week's actual data is the only honest gate.

### 19. Answer the seven Guardrails Checklist questions — `guardrails-checklist`
*07-build · Answer the seven guardrails questions in writing · Visible*

1. **Question 1: Lock data access boundaries in writing** — Documents exactly what data the system may touch and what is off-limits, with an owner for that decision.
2. **Question 2: Define agent autonomy vs. human sign-off** — Draws the exact line between what the agent can do unilaterally and what requires a human approval before action.
3. **Question 3: Specify behavior on unrecognized inputs** — Prevents the agent from guessing or going silent when it encounters something outside its design envelope.
4. **Question 4: Define quality measurement and baseline** — Makes 'good enough' measurable so the supervisor can calibrate review cadence and know when to trust the system more.
5. **Question 5: Name the escalation path** — Routes judgment-requiring outputs to a specific person, in a specific form, on a specific timeline — no ambiguity in the moment.
6. **Question 6: Name the accountability owner** — Establishes who owns a bad output the same way they'd own it if a person produced it — no diffuse responsibility.
7. **Question 7: Define the kill switch condition** — Pre-decides the specific failures that trigger immediate shutdown, so the decision isn't made under pressure after something goes wrong.

### 20. Run the Deploy Readiness Audit — `deploy-readiness-audit`
*08-deliver · The Deploy Readiness Audit · Visible*

1. **Gate 1 — Confirm hands-on training** — Every person whose work changes must have practiced on real inputs before go-live; a meeting or email doesn't count.
2. **Gate 2 — Document the escalation path** — Unexpected agent output needs a named human, a channel, and a response window before it hits production.
3. **Gate 3 — Test against real data** — Validating on actual inputs from the last two weeks surfaces gaps that synthetic tests miss.
4. **Gate 4 — Book the Human Orchestrator review cadence** — A recurring, non-negotiable calendar event makes oversight an operating rhythm, not a best intention.
5. **Resolve every Fail before deploying** — Each failed gate becomes a named task; re-running at 4/4 is the deploy condition.

### 21. Write the Per-Role Runbook — `per-role-runbook`
*08-deliver · The per-role runbook · Buried*

1. **Identify affected roles from the Hybrid Accountability Chart** — Scope the runbook to every person whose handoffs changed — no one surprises left out.
2. **For each role, answer the four change questions** — Forces explicit articulation of what the person does differently, what the agent now handles, how they review output, and what triggers escalation.
3. **Write the three-column entry (input / output / escalation)** — One concrete sentence each — vague entries like 'reviews output' are not runbook entries.
4. **Apply the vacation test** — A colleague who missed the entire Sprint should be able to read the document and know exactly what changed about their job.
5. **Publish the runbook in the team's live tool before go-live** — A runbook in a folder no one opens is not a runbook; it must be findable where the team already works.

### 22. Build and Maintain the Operational Log — `operational-log`
*08-deliver · What gets logged · Visible*

1. **Create the four-column log template before deploy** — The log must exist on day one of production — building it post-launch means the first gap goes unrecorded.
2. **Assign a single named owner** — Accountability without a name means the log dies; one person owns it, no committee.
3. **Run daily check-ins for the first two weeks** — The daily cadence surfaces patterns before they compound; week-two review timing aligns with the delivery test window.
4. **Categorize every entry (Unplanned intervention / Data gap / Edge case / User confusion)** — Consistent categories make tallying possible; the category with the most entries identifies the next constraint.
5. **Tally by category at end of week two and surface the top category as the next Sprint signal** — The log is a sensor, not a complaint box — it feeds Design for the next Sprint.

### 23. Measure the Sprint Outcome — `sprint-outcome-measurement`
*08-deliver · The measurement question · Visible*

1. **Pull the Signal statement and quantified cost** — The baseline must come from the original Signal instrument — same metric, same unit — so the comparison is apples-to-apples.
2. **Measure the same metric in production (result after Sprint)** — An imperfect measurement beats a vibe; write the number even when the original Signal quantification was loose.
3. **Compute the delta** — Leadership needs to see what moved, not a narrative — the delta makes the change legible.
4. **Write the outcome in one sentence** — The outcome sentence mirrors the Signal statement and becomes the artifact Compound works against.
5. **Calculate and report adoption rate (week-two window)** — Operational improvement and adoption rate together diagnose whether a low result is a Design problem or a change-management problem.

### 24. Run the Sprint Retrospective — `sprint-retrospective`
*09-compound · Run the Sprint Retrospective honestly · Buried*

1. **Ask: what worked?** — Names the specific design decisions that paid off — mechanism, not sentiment — so they can be intentionally repeated.
2. **Ask: what didn't work?** — Surfaces broken handoffs, dirty inputs, and wrong cadences — the honest friction every Sprint produces.
3. **For each failure, ask: what would have to be true for this not to happen again?** — Reframes blame into design fix — converts observations into actionable constraints on the next Sprint's design.
4. **Ask: what one design change would make the next Sprint better?** — Forces prioritization before the session ends; feeds directly into the Install One Design Change step.
5. **Measure what compounded (three compounding questions)** — Distinguishes output (Sprint delivered something) from compound interest (the Sprint built infrastructure the next Sprint inherits).

### 25. Install One Design Change — `install-design-change`
*09-compound · Install one design change. Just one. · Buried*

1. **Survey everything the Sprint surfaced** — Human Orchestrator scans all retrospective items — Source gaps, wrong cadences, broken handoffs, dirty inputs — before picking.
2. **Name the single change that will most improve the next Sprint** — The discipline of one defeats the 'lessons learned list' failure mode; forces a real priority decision.
3. **Write the four-field change card (What / Who / How you'll know / By date)** — Makes the change specific and testable; any blank field signals the change is too vague to install.
4. **Install the change structurally before the next Sprint begins** — An insight that doesn't change the design isn't worth recording — the change must land in the chart, workflow, or Source map.
5. **Verify the change using the 'how you'll know' criterion** — Closes the loop — confirms the change is working before Sprint two kicks off, not assumed.

### 26. Re-rank the Constraint Backlog (Constraint Re-rank) — `constraint-re-rank`
*09-compound · Re-rank the Constraint Backlog on what the Sprint taught you · Buried*

1. **Ask: did the Sprint reveal new information about any other constraints?** — Solving one constraint exposes the real cost of another — the backlog order the company entered the Sprint with may no longer be correct.
2. **Ask: did any constraints get partially resolved as a side effect?** — Recognizes spillover value and adjusts rankings to reflect what actually changed, not just what was targeted.
3. **Ask: did any new constraints surface during the Sprint that weren't on the original list?** — Prevents new constraints from falling through the cracks by capturing them at the moment of highest clarity.
4. **Ask: given what you now know, which constraint should the next Sprint solve?** — Converts the re-ranked backlog into a decision — the top constraint becomes the input for the next Signal conversation.
5. **Assign a Human Orchestrator for the next Sprint and write it down before leaving the room** — Names ownership before the Compound session ends; without a named Orchestrator the next Sprint has no driver.

### 27. Run the quarterly operating session — `quarterly-operating-session`
*10-the-rhythm · Run the quarterly operating session in four steps · Visible*

1. **Step 1: Review the previous Sprint at the outcome level** — Determines whether the constraint actually moved and whether the workflow is permanent or needs another Sprint — the outcome question, not a status update.
2. **Step 2: Update the Constraint Backlog** — Re-ranks the running inventory of constraints so the next Sprint is chosen from current reality, not last quarter's assumptions.
3. **Step 3: Commit the next Sprint** — Converts backlog priority into a named constraint, a named Human Orchestrator, a budget confirmation, and a start date — the team leaves with a specific commitment.
4. **Step 4: Update the Hybrid Accountability Chart** — Makes permanent any HAC rows from the completed Sprint, removes what didn't work, and resets the Hybrid Org Today baseline so the living document stays current.

### 28. Maintain the Hybrid Org Today — `hybrid-org-today`
*10-the-rhythm · Maintain one living document: the Hybrid Org Today · Buried*

1. **Combine the Hybrid Accountability Chart and Constraint Backlog into one document** — The structural layer (who owns what handoffs) and the constraint inventory (solved / in-flight / queued) together answer the one quarterly question: where does the design layer stand today?
2. **Fit it on one page** — If it spills past one page you are tracking too much — the constraint forces prioritization and prevents the document from becoming an ignored wiki.
3. **Update it during the quarterly session, not between sessions** — Leadership-team ownership in the meeting is the discipline that prevents the document from rotting; Thursday-afternoon curation by a Notion-curator is how every 'living document' dies.
4. **Use it as the standard briefing and the board receipt** — A new executive or a board question gets answered from one current, concrete document — not a slide deck assembled from memory.

### 29. Track compounding on the Compounding Scorecard — `compounding-scorecard`
*10-the-rhythm · Track compounding on a single scorecard · Buried*

1. **Create the scorecard with six columns: Quarter, Constraint Solved, Cost Before, Cost After, Delta, Cumulative Impact** — The fixed structure forces each Sprint to produce a measurable delta and makes the cumulative column — the business case — visible across quarters.
2. **Fill in the first row with the current Sprint** — Anchors the document in real data immediately; an empty scorecard is not a scorecard.
3. **After each Sprint closes, add a row with the measured delta** — The delta tells you whether the design correctly identified the constraint; the retrospective tells you why — both are required to improve the next Sprint.
4. **Read the cumulative column at each quarterly session to confirm compounding** — The cumulative column is the business case for continuing the Rhythm; declining marginal deltas are normal and expected — the compounding is in the stack, not each individual row.

### 30. Run minimum viable Signal — `minimum-viable-signal`
*11-what-to-do-next · Run minimum viable Signal on yourself · Visible*

1. **Name the operational problem** — Forces a specific, observable constraint sentence rather than a vague category — the entry point for every Sprint.
2. **Quantify the annual cost** — Attaches a dollar/hour/headcount number so the constraint can be prioritized and Sprint ROI can later be measured.
3. **State what would have to be true to solve it** — Reveals whether the constraint is Sprint-solvable or whether something upstream must move first, preventing wasted quarters.

### 31. Name the Sprint roster — `sprint-roster`
*11-what-to-do-next · Name three roles: Orchestrator, Owners, Builder · Visible*

1. **Identify the Human Orchestrator** — Assigns workflow ownership and agent-supervision authority to one named person before the Sprint starts.
2. **Name the daily-proximate supervisors** — Identifies the two or three people closest to the problem who contribute to Signal and Source and catch what reports miss.
3. **Confirm the builder resource** — Locks in who will construct the solution — internal developer, external partner, or Compound membership — so the Sprint is fully staffed.

### 32. Fill in the Sprint Planning Canvas (kickoff instance) — `sprint-planning-canvas`
*11-what-to-do-next · Fill in the Sprint Planning Canvas · Buried*
**Same artifact as #7 (canonical home: 03-the-framework). This is the abbreviated kickoff/pre-flight pass. Dedupe to one worksheet — see §4.**

1. **Enter the constraint statement** — Populates the Active Sprint row of the Hybrid Org Today with a single precise sentence — the Sprint's north star.
2. **Enter the annual cost estimate** — Establishes the baseline number the Sprint must beat and makes the business case visible to the team.
3. **Name the three roles on the Canvas** — Connects the roster (Orchestrator, supervisors, builder) to the Sprint artifact so ownership is unambiguous.
4. **Choose and record the path (self-guided or Compound)** — Locks in the operating model so execution doesn't stall on a decision that should already be made.
5. **Run the pre-flight checklist** — Two gate questions (constraint is structural; Orchestrator passes Right Seat Evaluation) catch the gaps that turn into wasted quarters before the Sprint starts.

---

## 3. Work-needed summary

### 3a. Spine state — what the BOOK needs

**SURFACE the spine (Buried — steps exist but are scattered/implicit; needs a numbered "the moves" overview added to the chapter):** 14 processes

| Process | Chapter | Slug |
|---------|---------|------|
| Calculate Revenue per Employee | 01-diagnosis | `revenue-per-employee` |
| Take Stock of the Operating-Model Gap | 02-beliefs | `take-stock-operating-model-gap` — **REMOVED** |
| Run the Two-Column Role Sort | 02-co-operating-model | `two-column-role-sort` |
| Calculate the Design Opportunity | 02-co-operating-model | `calculate-design-opportunity` |
| Map the Hybrid Split | 02-co-operating-model | `map-hybrid-split` |
| Run the Signal Session | 04-signal | `run-signal-session` |
| Build the Constraint Backlog | 04-signal | `constraint-backlog` |
| Classify each source on the map | 05-source | `classify-sources` |
| Write the Information Flow Specification | 06-designing-the-system | `information-flow-spec` |
| Work Deconstruction | 06b-designing-the-work | `work-deconstruction` |
| Write the Per-Role Runbook | 08-deliver | `per-role-runbook` |
| Run the Sprint Retrospective | 09-compound | `sprint-retrospective` |
| Install One Design Change | 09-compound | `install-design-change` |
| Re-rank the Constraint Backlog | 09-compound | `constraint-re-rank` |
| Maintain the Hybrid Org Today | 10-the-rhythm | `hybrid-org-today` |
| Track compounding on the Compounding Scorecard | 10-the-rhythm | `compounding-scorecard` |

*(15 rows; note 06b Agent Mini-Spec and 11-ch Sprint Planning Canvas are deduped, so the unique-Buried count is 14 once #32 collapses into #7.)*

**LABEL-ALIGN only (Visible — steps already legible in prose; just sync labels/whys to this registry):** the remaining processes — #2, 7, 9, 12, 13, 15, 17, 18, 19, 20, 22, 23, 27, 30, 31.

**ABSENT:** none.

### 3b. Worksheets — what to GENERATE

**Already built (3, in `worksheets/html/`):**

| Worksheet file | Registry slug | Process |
|----------------|---------------|---------|
| `signal-standalone.html` | `run-signal-session` | #8 Run the Signal Session |
| `knowledge-that-walks-standalone.html` | `build-knowledge-map` | #9 Build the Knowledge Map |
| `map-the-inputs-standalone.html` | `information-flow-spec` | #11 Write the Information Flow Specification |

**Need a worksheet generated (27 unique processes):**

All other unique processes. Priority tier 1 = the Sprint-spine backbone a reader executes end-to-end:
`ai-readiness-scorecard`, `sprint-planning-canvas`, `classify-sources`, `hybrid-accountability-chart`, `agent-mini-spec`, `design-brief`, `write-build-spec`, `guardrails-checklist`, `deploy-readiness-audit`, `sprint-outcome-measurement`, `sprint-retrospective`, `quarterly-operating-session`.

Tier 2 (calculators / stock-takes / supporting artifacts):
`revenue-per-employee`, `two-column-role-sort`, `calculate-design-opportunity`, `map-hybrid-split`, `work-deconstruction`, `audit-spec-failures`, `per-role-runbook`, `operational-log`, `install-design-change`, `constraint-re-rank`, `hybrid-org-today`, `compounding-scorecard`, `minimum-viable-signal`, `sprint-roster`, `constraint-backlog`.

---

## 4. Duplicate / overlapping processes — DEDUPE

**A. Agent Mini-Spec — #13 (06-designing-the-system) ≡ #16 (06b-designing-the-work).**
Same artifact, same slug `agent-mini-spec`, same six core fields. The 06-system version is the **canonical** spine because it carries a 7th step (tool-category routing) that 06b omits. Action: collapse to ONE worksheet and ONE book overview using the #13 seven-step spine. In 06b, reference the same spine rather than re-listing it with slightly different field-name casing ("System Prompt" vs "system prompt"). The casing/wording drift between the two is exactly the failure mode this registry exists to prevent.

**B. Sprint Planning Canvas — #7 (03-the-framework) ≡ #32 (11-what-to-do-next).**
Same artifact, same slug `sprint-planning-canvas`. #7 is the **canonical full spine** (9 steps, the eight Canvas questions + the three operating fixtures). #32 is an abbreviated 5-step kickoff/pre-flight pass that maps onto a subset of #7 (constraint, cost, roles, path, pre-flight gates). Action: one worksheet (the full Canvas). In Ch 11, present the kickoff pass as a short "fast path through the Canvas you already know" callback, not a second independent process.

**C. Soft overlap to watch (no merge, but keep labels distinct):**
- **Signal family** — `run-signal-session` (#8, full facilitated session) and `minimum-viable-signal` (#30, 3-step solo version). Intentionally different scopes; keep both but cross-link so #30 reads as the stripped-down on-ramp to #8.
- **Backlog re-rank** — `constraint-re-rank` (#26, Compound chapter) and Step 2 of `quarterly-operating-session` (#27, Rhythm chapter) are the same move at two cadences. Keep both; make the Rhythm step explicitly point to the #26 spine so the re-rank logic is authored once.
- **Constraint Backlog lifecycle** — `constraint-backlog` (#8a, Signal: build it + first selection) and `constraint-re-rank` (#26, Compound: re-rank it after each Sprint) are the same standing table at two moments. The build-and-select logic is authored in #8a; #26 re-orders what #8a created. Keep both; the selection rule (eligibility → load-bearing → cost) is shared, authored in #8a.
- **HAC touchpoints** — `hybrid-accountability-chart` (#12, build it), `quarterly-operating-session` Step 4 (#27, update it), `hybrid-org-today` (#28, fold it into the living doc). Not duplicates — lifecycle stages of one artifact. Ensure column names match across all three.

---

## Book-insert convention (slug-anchored "how to" blocks) — LOCKED 2026-06-18

Every process's **book overview** ("the moves" spine) is inserted at its **Section anchor** as a
slug-anchored block so it is both reader-demarcated AND machine-addressable for maintenance:

```
<!-- moves:<slug> -->
### How to <do the process>
1. <Canonical step label 1> — <one-line why>
2. <Canonical step label 2> — <one-line why>
...
<!-- /moves:<slug> -->
```

Rules:
- **Step labels are the canonical labels in this registry, verbatim** (same as the worksheet) — book overview and worksheet read as one spine.
- The block is a **scannable overview, not a re-teach** — the chapter's existing detailed prose stays as the detail beneath/around it.
- **Buried** processes: insert the block at the anchor. **Visible** processes: wrap/align the existing enumerated block with the anchor + canonical labels.
- Heading house style applies (sentence case + one italic where natural; the `### How to …` directive form is the carrier).
- The HTML comments are Quarto-safe (pass through to output as comments) and are the handle the **`sync-process` skill** uses to locate + replace a block by slug.

This is what makes the demarcated how-to sections maintainable: edit worksheet → (if spine changed) update registry labels → `sync-process` finds `<!-- moves:<slug> -->` and replaces the book block. Surgical, no hunting.
