Compound · Deliver / Per-role runbook

# Write the Per-Role Runbook

*Document, role by role, exactly what changed about each person's job — so the workflow is delivered, not just deployed.*

A deployed workflow isn't a delivered one until every affected person knows what they now do differently, what the agent took over, how they check its work, and when they escalate. This worksheet turns that into one short page per role. The test it has to pass: a colleague who was on vacation for the entire Sprint could read it and know exactly what changed about their job.

**Before you start, you need the Hybrid Accountability Chart from Design** — the map of who owns what, with the agent roles added alongside the human ones. The runbook is scoped from that chart.

---

## Identify affected roles from the Hybrid Accountability Chart

Scope the runbook to every person whose handoffs changed — no one surprises left out.

1. Pull up the Hybrid Accountability Chart from Design. Read down it and circle every role whose daily work changes because of this Sprint.
2. List those roles here — name and seat — one row each. A role only belongs on the list if a handoff (what they send the agent, or what they get back) actually changed.
3. For each role, confirm hands-on training is done — not a meeting, not an email. If anyone hasn't trained, that's the first task before deploy, and their runbook entry isn't trustworthy until they have.

| Role (name + seat) | Handoff that changed | Training done? |
|--------------------|----------------------|----------------|
| | | |
| | | |
| | | |

> **Meridian:** Three roles changed and made the list — Dave Kowalski (Sr. Design Engineer), Elena Ruiz (VP Ops), and Ty Banfield (Sales). Everyone else in the shop kept their handoffs, so they stayed off the runbook.

---

## For each role, answer the four change questions

Forces explicit articulation of what the person does differently, what the agent now handles, how they review output, and what triggers escalation.

For each role on your list, answer all four — in plain sentences, not "handled by agent":

1. What does this person now do **differently** than before the Sprint?
2. What does the **agent** handle that this person used to handle?
3. How does this person **review** the agent's output?
4. What **triggers an escalation** — and to whom?

| Role | 1. Now does differently | 2. Agent now handles | 3. Reviews output by | 4. Escalation trigger → to whom |
|------|------------------------|----------------------|----------------------|--------------------------------|
| | | | | |

> **Meridian — Elena Ruiz (VP Ops):** (1) Used to build every quote from scratch, ~15 hrs/week; now reviews agent-drafted quotes in 15–20 min each and spends the recovered hours on production planning and supplier negotiations. (2) The agent assembles the draft quote, attaches a confidence score, and surfaces historical matches. (3) Reviews every assembled quote in her CRM queue, watching the confidence-score distribution. (4) Updates pricing rules when a new exception appears; flags low-confidence drafts for closer work.

---

## Write the three-column entry (input / output / escalation)

One concrete sentence each — vague entries like 'reviews output' are not runbook entries.

1. Collapse each role's four answers into the three-column form: **Input** (what they send the agent — the trigger), **Output** (what comes back and in what format), **Escalation** (what they do when something lands outside the expected range).
2. Write one concrete sentence per cell. Name the tool, the place, the threshold, the timeline. "Reviews output" fails; "Opens the quote draft in the shared folder, checks unit costs against the rate card, approves or flags within 4 hours" passes.
3. One page per role. Keep it short enough that someone reads the whole thing in under a minute.

| Role | Input (what they receive) | Output (what they produce) | Escalation (when and how) |
|------|---------------------------|----------------------------|---------------------------|
| | | | |

> **Meridian — three-column runbook:**
> - **Dave Kowalski (Sr. Design Engineer):** *Input* — specs flagged by the Quote Research Agent for non-standard materials or tight tolerances. *Output* — manual pricing for flagged line items; confirmation or correction of the agent's historical job match. *Escalation* — consulted on any quote involving Inconel, titanium, or exotic alloys; gets Claude Team notifications when the agent flags a match it can't confirm.
> - **Elena Ruiz (VP Ops):** *Input* — agent-assembled draft quote in her CRM review queue, with confidence score and historical matches. *Output* — approved quote (or edited and approved), updated Customer Notes.xlsx when new exceptions arise. *Escalation* — reviews every assembled quote, monitors confidence-score distribution, updates pricing rules for new exceptions; works from Claude Team and JobBOSS.
> - **Ty Banfield (Sales):** *Input* — approved quote delivered via HubSpot notification. *Output* — customer-facing proposal sent same-day for standard work. *Escalation* — reports customer feedback to Elena, flags any quote that doesn't match what the customer requested, submits all RFQs through the standardized intake form (no email forwards).

---

## Apply the vacation test

A colleague who missed the entire Sprint should be able to read the document and know exactly what changed about their job.

1. Hand each role's page to someone who wasn't in the Sprint — or read it as if you were that person on their first day back.
2. Ask: from this page alone, do I know what I now do differently, what the agent does, how I check it, and when I escalate? Any "I'd have to go ask someone" is a gap.
3. Fix every gap before go-live. The runbook isn't done until it passes this test without a single follow-up question.

> **Meridian:** The test the runbook had to clear — could someone who was on vacation during the entire Sprint sit down with this document and know exactly what changed about their job? Each role's page (Dave, Elena, Ty) was written to answer that with no follow-up call.

---

## Publish the runbook in the team's live tool before go-live

A runbook in a folder no one opens is not a runbook; it must be findable where the team already works.

1. Pick the tool the team already lives in — the project management system, the shared doc, or the Slack channel. Not a new folder, not a new app.
2. Put the runbook there and link it where the affected roles will trip over it in normal work.
3. Do this **before** the workflow goes live, so day one of production is day one of the runbook — not a document people discover weeks later.

> **Meridian:** The runbook went into the tools the team already used so each role found it in the flow of work — published before the workflow went live, not filed in a folder no one opens.

---

## Before you call it done

The runbook is finished when all of these are true:

- **Every affected role from the Hybrid Accountability Chart has a page** — and only the roles whose handoffs actually changed.
- **Each page answers the four change questions** and collapses into a three-column entry with one concrete sentence per cell — tool, place, threshold, timeline named.
- **It passes the vacation test** — a colleague who missed the entire Sprint could read it and know exactly what changed about their job, with zero follow-up questions.
- **It's published in the team's live tool before go-live** — findable where the team already works, not in a folder no one opens.

When all four are true, the workflow is delivered to the people, not just deployed to production.
