# Design Instrument: Work Deconstruction & Hybrid Accountability Chart

**Chapter:** 06 — Design
**Artifact produced:** Completed Work Deconstruction Sheet + one Hybrid Accountability Chart entry with named roles and guardrails
**Who's in the room:** Constraint owner (Human Orchestrator candidate), the person closest to the daily work (Agent Coordinator candidate), and anyone whose tasks will be deconstructed

---

## Purpose

Design turns the constraint and knowledge map into a workflow with named owners. Signal told you what to solve. Source told you what the work requires. Design decides who does what — human or agent — and writes that decision into a structure the rest of the company can read, build against, and improve.

You leave this session with two artifacts: a Work Deconstruction Sheet that classifies every task in the constraint workflow, and a Hybrid Accountability Chart entry that assigns ownership. If Build has to ask "what did you mean here?" — Design is not done.

---

## Part 1: Work Deconstruction

Pull the real task list for the role most affected by the constraint. Not the job description — job descriptions are always cleaner than reality. The actual list: everything this person touches in a week that relates to the constraint workflow.

### The Four Categories

Every task gets classified into one of four buckets:

| Category | Definition | Review model |
|---|---|---|
| **Human judgment required** | Context-dependent. Requires empathy, taste, negotiation, relationship history, or novel reasoning. An agent cannot reliably do this. | Human owns the work. No agent involved. |
| **Agent-assisted** | AI drafts, compiles, or recommends. A human reviews every output before it goes anywhere. | Human-in-the-loop: reviews every output. |
| **Fully automatable** | Rules-based, repetitive, well-defined inputs and outputs. AI executes. Human audits on a schedule, not per output. | Human-on-the-loop: monitors by exception. |
| **Workflow automation only** | No AI needed. This is a routing or integration problem — better tooling or process handles it. Zapier-level, not agent-level. | Standard automation. No agent team required. |

### The Sorting Question

For every task, ask: "If I gave a well-briefed AI agent this task with the right data, would the output need human review every time, or only when something goes wrong?"

- If every time: **Agent-assisted.**
- If only on exceptions: **Fully automatable.**
- If the agent adds no value and it is just a handoff or routing problem: **Workflow automation only.**
- If the answer depends on who the client is, what happened last week, or a judgment call with no clear rule: **Human judgment required.**

### Questions to Ask for Each Task

1. What is the input? Where does it come from?
2. What does the person actually do with it? (Be specific — not "processes the request" but "compares the spec to three pricing tables and applies the customer-specific exception if one exists.")
3. Is the logic repeatable, or does it change based on context the person carries in their head?
4. What happens when this task goes wrong? What is the cost of an error?
5. How often does this task happen? (Daily, weekly, per-transaction?)

> **Pro Tip:** "Agent-assisted" is where most things start. "Fully automatable" is where things move after the agent has proven itself over multiple sprints. Autonomy is earned, not assigned. The question is not whether the AI *can* operate autonomously — it is whether you have the governance infrastructure to let it. Start restrictive. Widen based on demonstrated performance.

> **Action Step:** List every task in the constraint workflow. Sort each one into the four categories. Count the tasks in each bucket. If more than half land in "Human judgment required," challenge each one: is this genuinely judgment, or is it judgment because nobody has written down the rules?

---

## Part 2: Design the Hybrid Accountability Chart Entry

For each accountability in the constraint workflow, fill in one row:

| Role / Function | Agent Team | Human Supervisor | Level |
|---|---|---|---|
| *(what the work is — the outcome, not the task)* | *(agent team name, or "None")* | *(person's name)* | AI-Assisted / Automated |

### Four Questions Per Row

1. **What is the accountability?** Not the task — the outcome this person or team is responsible for. "Produce accurate initial quotes within 2 hours of request" is an accountability. "Look up pricing" is a task.
2. **Is there an agent team assigned?** If yes, what does the agent team do? Name it. Scope it. A team called "AI Helper" is not designed. A team called "Quote Generation Team" with a defined input (bid request + customer segment data) and output (draft quote with confidence score) is designed.
3. **Who is the named human supervisor?** Every row must have one. No exceptions. No "TBD." No "the team." A name. If you cannot name the supervisor, the accountability is not designed.
4. **Is it AI-Assisted or Automated?** AI-Assisted means human-in-the-loop — reviews every output. Automated means human-on-the-loop — monitors by exception, reviews on schedule.

> **Pro Tip:** The difference between AI-Assisted and Automated is the review cadence. AI-Assisted: every output gets a human eye before it ships. Automated: outputs ship, and a human reviews a sample or responds to flags. If you are not sure which to pick, start AI-Assisted. You can always move toward Automated after the agent proves itself. Moving the other direction — from Automated back to AI-Assisted — means something already went wrong.

> **Action Step:** Build one Hybrid Accountability Chart row for each accountability in the constraint workflow. Every row has all four fields filled. No blanks. No "we'll figure it out in Build."

---

## Part 3: Define the Human Roles

Two roles must be named before Design is locked. They can live in the same person at small scale. They cannot live nowhere.

### Human Orchestrator

The person who owns the constraint outcome. Sets goals for the agent team. Designs the workflow the agents execute against. Reviews at the goal level, not the task level — not checking every output, but asking whether the team is moving the constraint. Makes the design improvements between sprints.

### Agent Coordinator

The technical counterpart. Ensures agents are configured correctly, inputs are clean, outputs are reviewed at the right frequency. Surfaces judgment-call escalations to the Orchestrator. Flags when the design is drifting — inputs degrading, outputs trending off, a class of decisions no longer handled cleanly.

### Questions

1. **Who is the Human Orchestrator for this sprint?** Must be someone with authority over the workflow and the constraint outcome. Not a project manager — an owner.
2. **Who is the Agent Coordinator?** Must be someone who can configure the AI tools, troubleshoot failures, and review output quality day-to-day.
3. **What decisions does the Orchestrator make that agents cannot?** List at least three. These are the judgment calls that stay human — pricing exceptions for strategic accounts, escalation to leadership, workflow redesign between sprints.
4. **What triggers escalation from agent to Orchestrator?** Define at least two conditions. Examples: confidence score below threshold, input data missing or contradictory, output that affects a customer relationship, any decision above a dollar threshold.

> **Pro Tip:** The Human Orchestrator role is more strategic than executing inside the function. The operations lead who got the job because she was excellent at executing operations work is now being asked to design the operations function. Not a smaller role — a different one. Name it explicitly so the person knows what they are signing up for.

> **Action Step:** Name the Human Orchestrator and Agent Coordinator. Write down the Orchestrator's irreducible decisions and the escalation triggers. If you cannot fill these in, the workflow is not ready for agents.

---

## Part 4: Set Guardrails

Before moving to Build, define what the agents are NOT allowed to do. Guardrails are governance infrastructure. Without them, autonomy is a liability.

### Five Guardrail Questions

1. **What data can agents access? What is off-limits?** Name the systems, databases, and document sets the agent can read. Name what it cannot touch — customer PII, financial records above a threshold, strategic plans, anything regulated.

2. **What actions can agents take without approval? What requires human sign-off?** Be specific. "Draft a quote" is different from "send a quote to a customer." "Generate a report" is different from "distribute a report to the leadership team." Draw the line at the point where the output leaves internal review.

3. **What happens when an agent encounters something it was not designed for?** Define the escalation path. Who gets the flag? How fast? What does the agent do while it waits — pause, use a default, or continue with a warning?

4. **How will you monitor agent output quality?** Options: full review of every output (AI-Assisted), spot checks on a sample (transition zone), dashboard with exception flags (Automated). Pick one and write it down.

5. **What would cause you to shut down an agent workflow immediately?** Define the kill switch. Examples: agent produces output that contradicts company policy, sends customer-facing communication without review, processes data it should not have access to, error rate exceeds a defined threshold.

> **Pro Tip:** The autonomy level is a governance decision, not a capability decision. The agent may be capable of running unsupervised. The question is whether your organization has the monitoring, the escalation paths, and the cultural discipline to let it. Start with more guardrails than you think you need. Loosening them is easy. Recovering from a bad output that went unreviewed is not.

> **Action Step:** Answer all five guardrail questions in writing. If any answer is "we haven't decided yet," that is the decision you make now — not in Build, and not after deployment.

---

## Part 5: The Design Gate

Five items must be true before you move to Build. This is the gate. Hold the line.

- [ ] Every task in the constraint workflow is classified (Work Deconstruction complete)
- [ ] Every accountability has a Hybrid Accountability Chart entry with a named supervisor
- [ ] The Human Orchestrator and Agent Coordinator are named
- [ ] AI-Assisted vs. Automated is decided for each agent team, with a rationale
- [ ] Guardrails are defined: data access, action permissions, escalation paths, kill switch

If all five are checked, Build can begin. If any one is missing, Design is not done. Teams that find Build slow or complicated are almost always teams that moved through Design too quickly. Every undecided question discovered in Build is a piece of Design surfacing where it costs five times as much to resolve.

> **Action Step:** Run the five-item gate checklist. Fix any gaps before moving forward.

---

## Populated Example: Manufacturing Quoting Constraint

**Constraint (from Signal):** Design engineers spend 4-6 hours producing initial designs for every bid, including the 50%+ that won't convert, at an estimated cost of $180K/year in misallocated engineering time.

**Knowledge Map (from Source):** CRM with win/loss history (manual pipeline), ERP with materials pricing (not connected to quoting), quoting spreadsheet with 200+ exception rules on one person's desktop, two organic sources (ops manager Maria, senior engineer Dave), two missing sources (historical quote accuracy, segment conversion rates).

### Work Deconstruction: Quoting Workflow

| Task | Category | Rationale |
|---|---|---|
| Receive bid request, log in CRM | Workflow automation only | Routing problem. Trigger on inbound email, auto-create CRM record. No agent needed. |
| Pull customer history and segment data from CRM | Fully automatable | Structured lookup. Agent queries CRM, returns customer profile and win rate for segment. Human audits weekly. |
| Look up materials pricing and availability in ERP | Fully automatable | Structured lookup against known tables. Agent retrieves, flags anything out of stock or above threshold. |
| Apply pricing exceptions for customer-specific terms | Agent-assisted | 200+ exception rules, many undocumented. Agent applies known rules and drafts pricing. Human reviews every output until rules are fully captured and validated. |
| Estimate design feasibility and engineering hours | Human judgment required | Requires Dave's 30 years of experience reading specs and knowing what is buildable at what cost. Cannot be reliably automated until historical accuracy data exists. |
| Generate initial quote document | Agent-assisted | Agent assembles the quote from components above. Human reviews every quote before it reaches the customer. |
| Route quote for internal approval | Workflow automation only | Approval routing based on dollar threshold. Standard automation. |
| Send quote to customer, handle follow-up | Human judgment required | Customer relationship. Requires reading the negotiation, knowing the account history, deciding what to offer on margin. |

**Task count:** Human judgment required: 2. Agent-assisted: 2. Fully automatable: 2. Workflow automation only: 2.

### Hybrid Accountability Chart

| Role / Function | Agent Team | Human Supervisor | Level |
|---|---|---|---|
| Bid intake and CRM logging | None (workflow automation) | Sales Director | N/A — standard automation |
| Customer data retrieval and segment analysis | Quote Research Team | Maria (Ops Manager) | Automated |
| Draft quote generation (pricing + exceptions + assembly) | Quote Generation Team | Maria (Ops Manager) | AI-Assisted |
| Design feasibility estimation | None | Dave (Senior Engineer) | N/A — human judgment |
| Quote delivery and customer negotiation | None | Sales Director | N/A — human judgment |

### Human Roles

**Human Orchestrator:** VP of Operations. Owns the constraint outcome (reduce engineering hours on non-converting bids). Sets the target: cut initial quote turnaround from 4-6 hours to under 1 hour for standard bids. Reviews sprint results against that target. Makes the call on when to move Quote Generation Team from AI-Assisted to Automated.

**Agent Coordinator:** Maria, Ops Manager. Currently does manual reconciliation between CRM and ERP for every quote. Knows the exception rules. Will configure and monitor the Quote Research Team and Quote Generation Team day-to-day. Reviews every draft quote in sprint one. Flags edge cases to the VP of Operations.

**Orchestrator decisions agents cannot make:**
1. Whether to invest full engineering hours on a low-probability bid for a strategic account
2. When to override the agent's pricing recommendation based on competitive intelligence
3. Whether the Quote Generation Team has earned the move from AI-Assisted to Automated

**Escalation triggers:**
1. Agent encounters a customer or spec type not represented in the exception rules
2. Generated quote deviates more than 15% from Dave's feasibility estimate

### Guardrails

1. **Data access:** Agent teams can read CRM deal records, ERP pricing tables, and the exception rules database. Off-limits: customer payment history, contract terms marked confidential, and any data in the HR system.
2. **Actions without approval:** Agents can draft quotes, pull data, and flag exceptions. Agents cannot send any communication to a customer, modify pricing tables, or create CRM records beyond the initial bid log.
3. **Escalation path:** When the agent encounters an input it was not designed for (unknown customer segment, missing ERP data, spec outside historical range), it pauses the quote, flags Maria, and holds until she resolves or routes to the VP of Operations.
4. **Quality monitoring:** AI-Assisted phase — Maria reviews every draft quote. Target: 95% of draft quotes require no substantive correction over 3 consecutive sprints before considering the move to Automated.
5. **Kill switch:** Agent sends or stages a quote for external delivery without human review. Agent accesses data outside its permitted systems. Error rate on pricing exceeds 10% in any sprint.

---

## Summary of Action Steps

1. **List and classify every task** in the constraint workflow using the four categories (Part 1)
2. **Build a Hybrid Accountability Chart row** for each accountability — all four fields, no blanks (Part 2)
3. **Name the Human Orchestrator and Agent Coordinator** — with irreducible decisions and escalation triggers (Part 3)
4. **Answer the five guardrail questions** in writing — data access, action permissions, escalation, monitoring, kill switch (Part 4)
5. **Run the five-item Design Gate checklist** — fix gaps before moving to Build (Part 5)

---

## Pro Tips (collected)

1. "Agent-assisted" is where most things start. "Fully automatable" is where things move after the agent proves itself. Autonomy is earned, not assigned.
2. The difference between AI-Assisted and Automated is the review cadence. If you are not sure, start AI-Assisted. Moving the other direction means something already went wrong.
3. The Human Orchestrator role is more strategic than executing inside the function. Name it explicitly so the person knows what they are signing up for.
4. The autonomy level is a governance decision, not a capability decision. Start with more guardrails than you think you need. Loosening them is easy. Recovering from a bad output that went unreviewed is not.

---

## Handoff to Build

At the end of Design, you have: a Work Deconstruction Sheet (every task classified), a Hybrid Accountability Chart entry (every accountability owned), named Human Orchestrator and Agent Coordinator, and guardrails in writing. That is what Build needs. Build turns this design into a deployable system — specified at the level of detail a developer can execute against, with the oversight decisions Design locked already set. If Build has to make a design decision, Design was not done.

---

*This worksheet is the manual version of the Work Deconstruction and Hybrid Accountability Chart instruments in the Compound Skills Library. The method is the same. The tools run the same logic faster and more persistently.*