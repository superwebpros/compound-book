Compound · Integrate / Designing the System

# Write the Agent Mini-Spec

Turn each row on your Hybrid Accountability Chart into a build-ready spec — what the agent is, what it can touch, and how it's overseen — before Build begins.

The chart names the agent team. The mini-spec names what the agent actually *is*. Every agent-supervised row on your Hybrid Accountability Chart gets one mini-spec, and the mini-spec is what you hand to Build. Seven fields, one to a line. Fill in one of these per agent. The first six describe the agent; the seventh locks the kind of environment it runs on, so Build executes the design instead of re-deciding it.

**Before you start:** Have your Hybrid Accountability Chart (which agent teams exist, who supervises each) and your Knowledge Map (which sources are real) in front of you. The mini-spec draws from both; if a source isn't on the map, it isn't a source.

Fill in the seven-field spec, one per agent:

| Field | This agent |
|---|---|
| **System prompt** | _(operating rules: who the agent is, what it does, what it does not decide. Three to five sentences.)_ |
| **Tools** | _(every API, integration, or system the agent can call. Named.)_ |
| **Context sources** | _(which Knowledge Map rows feed this agent. If it is not on the map, it is not a source.)_ |
| **Memory rules** | _(what carries across runs. Most first-Sprint agents have no memory. Saying so is part of the spec.)_ |
| **Judgment and escalation rules** | _(when the agent escalates, what it refuses, what triggers a hand-off to the human supervisor.)_ |
| **Oversight load** | _(Low / Medium / High. How much of the supervisor's attention per run.)_ |
| **Tool category** | _(Off-the-shelf / Low-code / Hand-built — plus a one-sentence reason.)_ |

Then run the seven steps below to make each field real.

---

## Write the system prompt

Three-to-five sentences that tell the agent who it is, what it is accountable for, and what it does not decide — the standing operating rules it reads before every task.

1. State who the agent is and which workflow it serves, in one sentence. Name the company and the role, the way you'd brief a new hire.
2. State what it produces and who consumes that output. The deliverable, named, and the human or next agent who receives it.
3. State what it does **not** decide. The exclusions matter as much as the job: pricing, exceptions, customer contact — whatever stays human.
4. Keep it to three to five sentences. If it runs longer, you're describing the whole workflow, not this agent's seat.

> **Meridian example — Quote Research Agent.** "You are the Quote Research Agent for Meridian Manufacturing. Your job is to retrieve the customer's purchase history and match their RFQ against the closest historical jobs. You produce a summary for the quoting team to use; you do not set prices, apply exceptions, or contact customers." Three sentences: who it is, what it produces and for whom, and the three things it does not decide.

## List the tools

Name every API, integration, or system the agent can call; unnamed tools are tools Build has to guess at.

1. List every system the agent reads from or writes to, by name. APIs, search, file access, the specific systems the Knowledge Map says it needs.
2. Mark read vs. write for each. "HubSpot read access" and "HubSpot write access" are different grants with different risk.
3. If a tool isn't on this list, the agent doesn't get it. Don't leave a tool implied — Build will either skip it or guess at it.

> **Meridian example — Quote Research Agent.** Tools: HubSpot CRM read access; JobBOSS ERP read access. Both read-only — the research agent retrieves and matches; it never writes back to a system of record.

## Identify the context sources

Map the Knowledge Map rows that feed this agent; if a source is not on the map, it is not a source — this prevents scope creep at the data layer.

1. For each system in the Tools list, name the specific data this agent draws from it. Document store, CRM record, rate-card spreadsheet, the cleaned exception database.
2. Cross-check every source against your Knowledge Map. If it's not a row on the map, either add it to the map first or cut it from the spec.
3. Confirm the agent's sources are scoped to what this seat needs — not every source the company has.

> **Meridian example — Quote Research Agent.** Context sources: HubSpot deal history; JobBOSS job costing records. Both trace to rows on Meridian's Knowledge Map. The 112-rule cleaned pricing-exceptions database feeds the *Pricing* Agent, not this one — so it does not appear here.

## Set the memory rules

Explicitly stating what the agent tracks across runs (or that it tracks nothing) prevents the agent from carrying stale state into new tasks.

1. Decide what, if anything, carries from one run to the next: conversation history, prior outputs, learned customer preferences.
2. If the agent should treat every task fresh, write that down. Most first-Sprint agents have no memory, and saying so is part of the spec — not an omission.
3. If it does carry state, name the window and what triggers a reset, so Build doesn't invent its own.

> **Meridian example — Quote Research Agent.** Memory rules: "No memory across runs. Each RFQ is treated fresh." A first-Sprint agent — the spec states the no-memory rule explicitly rather than leaving Build to assume it.

## Define judgment and escalation rules

Specifies exactly when the agent escalates, what it refuses, and what triggers a hand-off to the human supervisor — the governance answers from the Hybrid Accountability Chart land here, agent by agent.

1. Write the escalation trigger as a concrete condition, not a vibe. A threshold, a confidence floor, a missing input — something a machine can test.
2. Write what the agent does **while it waits**: pause and hold, return a default, or continue with a warning. "Flag and hold" beats "flag and keep going."
3. Pull the governance answers for this row from your Hybrid Accountability Chart (data limits, permitted actions, escalation path) and state them here in the agent's own terms.

> **Meridian example — Quote Research Agent.** Judgment and escalation rules: "If no historical job matches within 20% of the RFQ specs, flag for Elena. Do not estimate; flag and hold." A testable trigger (20% match threshold), a refusal (no estimating), and a wait behavior (hold for the named supervisor).

## Rate the oversight load (Low / Medium / High)

Keeps the supervisor's span of control visible; no supervisor should carry more than three high-oversight agents at once, so this field is the span-of-control check before the spec leaves Design.

1. Rate how much of the supervisor's attention this agent consumes per run: **Low**, **Medium**, or **High**. Write the one-line reason — what the supervisor actually does each run.
2. Count the agents under each supervisor. The hard limit: no more than three high-oversight agents under one human at a time (Bedard and colleagues at BCG, in *Harvard Business Review*, found productivity inverts past three concurrent agents per supervisor).
3. If a supervisor is over the limit, the design isn't done. Consolidate agents, raise some toward Automated, or split the supervisor role — then re-rate.
4. Confirm the supervisor can **trace** the agent's decisions, **challenge** its outputs, and **apply** expertise of their own. If any of the three is missing for this agent, it isn't ready to run.

> **Meridian example — Quote Research Agent.** Oversight load: "Medium — Elena reviews the research summary before the Pricing Agent runs." Elena (VP Ops) supervises three quoting agents; medium load each keeps her inside the span-of-control limit, and she can trace, challenge, and apply expertise to each one.

## Select the tool category (off-the-shelf / low-code / hand-built)

Locking the category in Design — by running the three routing questions in order — prevents Build from making an architecture decision based on vendor relationships or recency rather than the workflow's actual requirements.

1. Run the three questions in order and stop at the first **yes**:
   - Does a mature product already do exactly what this agent requires, with light configuration? → **Off-the-shelf.** Don't build what you can configure.
   - Is the agent's workflow custom but composed of standard moves (pull from a system, run through an agent, write back, notify someone)? → **Low-code.** Your team can own and change it directly.
   - Does the workflow run at a scale, or touch a system of record, that low-code tools can't reach — or does data sensitivity rule out a third-party platform? → **Hand-built.**
2. Write the category in one line and the reason in one sentence. If you can't write the reason without guessing, the design isn't done.
3. Leave the *specific* product to Build. Design names the category; Build picks the environment inside it. (No in-house engineer and the answer is hand-built? That's the row where you bring in a builder or contractor.)

> **Meridian example.** The Quote Research Agent pulls from two systems, runs the matching logic, and hands a summary to the next agent — standard moves the team can own. Category: **Low-code**, because the workflow is custom but built from standard primitives and Elena's team can change it without engineering. By contrast, Compound's own project-management agent team lives on a server, runs continuously, and exchanges information in real time across projects and channels — that one is **Hand-built**. Same Sprint discipline, different category; Design named both before Build started either.

---

## Before you call it done

Hand the mini-spec to someone who missed the Design session — or to the builder. They should be able to build this agent from what's written, without coming back to ask. Check, for every agent on the chart:

- [ ] The **system prompt** is three to five sentences and names what the agent does *not* decide, not just what it does.
- [ ] Every **tool** is named with read vs. write marked; nothing is left implied.
- [ ] Every **context source** traces to a row on the Knowledge Map — no sources invented at the spec.
- [ ] **Memory rules** are stated explicitly, including "no memory" when that's the answer.
- [ ] **Judgment and escalation rules** give a testable trigger, a refusal list, and a wait behavior — not "reviews output."
- [ ] **Oversight load** is rated, no supervisor carries more than three high-oversight agents, and the supervisor can trace / challenge / apply expertise.
- [ ] The **tool category** is chosen by the three routing questions, with a one-sentence reason — and the specific product is left to Build.

If any box is blank, that blank is your next Design session — not a Build surprise at five times the cost.
