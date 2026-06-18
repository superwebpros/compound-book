Compound · Integrate / Designing the System

# Build the Hybrid Accountability Chart

Put a named owner against every lane of the workflow — human and agent — before Build begins.

You traced the work as information flow and drew the swim lanes. Now you assign ownership. The Hybrid Accountability Chart takes those lanes and puts a name against each one: one accountability, one named human supervisor, and (where applicable) one named agent team doing the execution work underneath. The accountability never moves from human to agent — only the execution work does. Work one Sprint at a time, one row per accountability your Sprint touches.

**Before you start:** Have your Information Flow Specification (the swim lanes) and your Knowledge Map in front of you. The chart is the answer to "who owns each lane," so you need the lanes first.

Fill in the four-column chart, one row per accountability:

| Role / Function | Agent Team | Human Supervisor | Level |
|---|---|---|---|
| _(outcome the row owns, not a task)_ | _(named agent team, or None)_ | _(one human, no shared rows)_ | AI-Assisted / Automated / N/A |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Then run the six steps below to make each row real.

---

## Name the role/function as an outcome, not a task

Define what the row is accountable *for* — the outcome, not the activity.

1. For each accountability your Sprint touches, write the outcome the row owns: the measurable result a supervisor would defend in a meeting.
2. Stress-test the phrasing. If it reads like a task a junior could finish in an hour ("look up pricing"), rewrite it as the outcome that work serves.
3. Confirm each row names one outcome, not a bundle of three. Split it if it does.

> **Meridian example.** Elena's quoting Sprint produced five rows. The agent-supervised outcomes were written as outcomes, never tasks: "Customer data retrieval and history matching," "Material and labor pricing assembly," and "Draft quote generation and review" — not "look up the CRM" or "open JobBOSS." The two human-only rows: "Quote delivery and customer negotiation" and "Non-standard material and tolerance consultation."

## Name the agent team (or mark None)

Give the execution work a name you can point to — or mark the row human-only.

1. For each row, decide whether an agent team does the execution work. If yes, name and scope it. If the work is pure human judgment, write **None**.
2. Make the name specific enough to own. "Quote Pricing Agent" names who does what; "AI Helper" names nothing useful and dissolves accountability.
3. Confirm the name carries scope: someone reading it knows what to ask when something goes wrong.

> **Meridian example.** Three named agent teams: Quote Research Agent (customer data retrieval and history matching), Quote Pricing Agent (material and labor pricing assembly), Quote Assembly Agent (draft quote generation and review). The two human-judgment rows — quote delivery/negotiation and non-standard tolerance consultation — are marked **None**.

## Name one human supervisor — no TBD, no shared rows

Every row gets exactly one named human who owns the outcome.

1. Write one person's name in the supervisor cell for every row, agent-supervised and human-only alike.
2. Reject every non-answer: no "TBD," no "the team," no two names sharing a row. If you can't name the supervisor, the design isn't done — that blank is your Design session.
3. Confirm there are no unowned agent teams anywhere in the chart. This is a structural rule, not a soft principle: someone real has to be accountable when the agents drift.

> **Meridian example.** All three agent rows name **Elena Ruiz (VP Ops)** as supervisor. The human-only rows name their owners directly: **Ty Banfield (Sales Lead)** on quote delivery and customer negotiation, **Dave Kowalski (Sr Design Engineer)** on non-standard material and tolerance consultation. Five rows, five names, no blanks.

## Set the autonomy level: AI-Assisted or Automated

Decide how much human review sits between agent output and any consequential action.

1. For each agent-supervised row, set the level: **AI-Assisted** (human-in-the-loop, reviewing every output) or **Automated** (human-on-the-loop, monitoring by exception and reviewing on schedule). Mark human-only rows **N/A — human judgment**.
2. Always start AI-Assisted. Every agent team, every Sprint, begins with a human reviewing every output. You earn automation later, after the agent has proved reliable over several Sprints.
3. Write the *rationale*, not just the label. "AI-Assisted because the exception rules aren't fully documented yet" is a rationale; "AI-Assisted" by itself is a checkbox.
4. Remember this is a governance decision, not a capability decision. The question isn't whether the agent *could* run unsupervised — it's whether you have the monitoring and discipline to let it.

> **Meridian example.** All three agent rows start **AI-Assisted**: Elena reviews every draft quote in Sprint one. The two human rows are **N/A — human judgment**. The move toward Automated is Elena's call, made only after an agent runs clean for several Sprints — not a setting flipped at deploy.

## Apply the Right Seat Evaluation to the supervisor candidate

Confirm the named supervisor can actually supervise — three tests, all must pass.

1. **Sees It** — Does this person understand the work the agent does well enough to evaluate whether the output is correct, or will they rubber-stamp because they can't tell the difference?
2. **Wants It** — Are they genuinely accountable for the outcome, or do they treat the agent team as someone else's problem with their name attached?
3. **Suited for It** — Do they have the judgment, context, and authority to override the agent when it drifts and make the calls the agent can't?
4. If the candidate fails any one of the three, you have a name in the column and ineffective supervision underneath it. Choose someone else, or write the development plan that gets them to all three before the Sprint runs.

> **Meridian example.** Elena Ruiz passes all three for the quoting agents: she ran quoting personally for years (Sees It), she's the Human Orchestrator who owns the constraint outcome (Wants It), and as VP Ops she has the authority and judgment to override a quote and route an exception to Dave or to Mark Ellison on strategic-account pricing (Suited for It).
>
> *EOS note:* this maps closely to the GWC test — Get it / Want it / Capacity — extended from human seats to agent-supervision seats.

## Answer the five governance questions for each row

Write down what the system may do and may not do — before Build, not after a bad output.

For each agent team, answer all five in writing. "We haven't decided yet" is the decision you make now.

1. **What data can agents access? What's off-limits?** Name the systems, databases, and document sets the agent can read; name what it can't touch (PII, regulated records, anything not listed). Lock access at the source, not at processing time.
2. **What actions can agents take without approval? What requires sign-off?** Draw the line where output leaves internal review. "Draft a quote" is not "send a quote."
3. **What happens on an input the agent wasn't designed for?** Define the escalation path: who gets the flag, how fast, and what the agent does while it waits — pause, default, or continue with a warning.
4. **How will you monitor output quality?** Pick one: full review (AI-Assisted), spot checks on a sample (transition), or dashboard with exception flags (Automated).
5. **What would make you shut the workflow down immediately?** Define the kill switch in concrete conditions the whole team knows — customer-facing send without review, data accessed outside permitted systems, error rate over a threshold.

> **Meridian example.**
> 1. *Data access:* read HubSpot CRM deal records, JobBOSS ERP job costing and rate card, and the 112-rule cleaned pricing-exceptions database. Off-limits: financial reporting, employee records, customer payment history, supplier contracts, anything not listed.
> 2. *Actions without approval:* draft quotes, pull data, flag exceptions. Not allowed: send any customer communication, modify pricing tables, apply undocumented pricing exceptions.
> 3. *Escalation:* on unknown material, missing ERP data, RFQ confidence below 60%, or pricing deviation greater than 15% from the closest historical match — flag Elena and hold until she resolves or routes to Dave (materials) or Mark Ellison (strategic-account pricing).
> 4. *Quality monitoring:* AI-Assisted phase — Elena reviews every draft quote. Target: zero substantive corrections for three consecutive weeks before considering human-on-the-loop.
> 5. *Kill switch:* any quote reaching a customer without Elena's review; the agent accesses data outside permitted systems; pricing errors exceed 20% on three quotes in any week.

---

## Before you call it done

Hand the chart to someone who missed the Design session. They should be able to read it and know exactly who owns what — without coming back to ask. Check:

- [ ] Every Role / Function cell names an **outcome**, not a task.
- [ ] Every agent team is **named and scoped** (or the row is honestly marked None).
- [ ] Every row has **one named human supervisor** — no TBD, no "the team," no shared cells, no unowned agent teams.
- [ ] Every agent row has an **autonomy level with a written rationale**, and every agent team starts AI-Assisted.
- [ ] The supervisor on every agent row **passes all three Right Seat tests** (Sees It / Wants It / Suited for It) — or has a named development plan.
- [ ] All **five governance questions are answered in writing** for every agent team, with no "we haven't decided yet."

If any box is blank, that blank is your next Design session — not a Build surprise at five times the cost.
