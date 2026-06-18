Compound · Deliver / Readiness

# Run the Deploy Readiness Audit

*Four binary gates that prove the organizational side is ready — so you don't discover the gap in production, where fixing it is expensive.*

Before your team flips the switch, you run a pre-flight check. Four gates, each Pass or Fail. The Audit is a check on prior work, not new authoring: every gate points to something that should already exist — a trained person, a documented path, a tested input, a scheduled review. If it doesn't exist, the gate fails and the deploy is blocked.

**Before you start, you need your Hybrid Accountability Chart from Design** — the map of who owns what, extended to include agent roles — and your Signal statement so you know which workflow you're clearing. Run the four gates in order, record Pass or Fail for each, then resolve every Fail before you deploy.

---

## Gate 1 — Confirm hands-on training

Every person whose work changes must have practiced on real inputs before go-live; a meeting or email doesn't count.

1. From the Hybrid Accountability Chart, list every person whose daily work changes because of this Sprint. Leave no affected person off the list.
2. For each person, record whether they completed hands-on practice on actual inputs — not attended a demo, not read an email. Mark Yes or No.
3. If anyone is marked No, write the specific task that closes it (e.g., "Schedule a 60-minute working session with real inputs") and assign it. Gate 1 passes only when every name is Yes.

> **Meridian — Gate 1:** Elena and Dave completed hands-on training with the three-agent quoting pipeline before go-live. Elena ran real quotes through the system; Dave reviewed the agent's historical job matching against specs he knew by heart. Pass.

---

## Gate 2 — Document the escalation path

Unexpected agent output needs a named human, a channel, and a response window before it hits production.

1. Write down what counts as "unexpected output" for this workflow — low-confidence results, non-standard cases, anything outside the expected range.
2. For each, name the specific person it routes to (a name, not a role in the abstract), the channel it travels through, and the response window.
3. Confirm the path is documented where the team will find it, not held in someone's head. Gate 2 passes only when the path is written, named, and findable.

> **Meridian — Gate 2:** The escalation path was documented in the Claude Team workspace. Any quote flagged as low confidence routed to Dave for non-standard materials; Elena reviewed every assembled quote before it went to the customer. Pass.

---

## Gate 3 — Test against real data

Validating on actual inputs from the last two weeks surfaces gaps that synthetic tests miss.

1. Pull a set of real inputs from your operation from the last two weeks — actual customer requests, tickets, or records, not invented test cases.
2. Run them through the live workflow and record what the system produced for each.
3. Note any gap, wrong output, or case the workflow couldn't handle. If gaps appear, write the fix task and assign it. Gate 3 passes only when the workflow handles real two-week inputs cleanly.

> **Meridian — Gate 3:** The workflow was tested against real RFQs pulled from HubSpot — actual customer requests from the prior two weeks. Systems verified: HubSpot connected, JobBOSS connected, Customer Notes.xlsx with 112 validated pricing rules loaded into the agent's context. Pass.

---

## Gate 4 — Book the Human Orchestrator review cadence

A recurring, non-negotiable calendar event makes oversight an operating rhythm, not a best intention.

1. Name the Human Orchestrator — the operational owner accountable for reviewing, course-correcting, and closing the loop on what the agent team produces. (If you run EOS, think of the Integrator role extended to the agent team: same accountability pattern, Sprint-level scope.)
2. Define the review cadence — which days, what time — and put it on the calendar as a recurring event. Recurring. Non-negotiable.
3. Confirm the event actually exists on the calendar, not just as an intention. Gate 4 passes only when the cadence is named and booked.

> **Meridian — Gate 4:** Elena was named as the operational owner. Her review cadence was booked on the calendar: Monday and Thursday mornings, recurring. Pass.

---

## Resolve every Fail before deploying

Each failed gate becomes a named task; re-running at 4/4 is the deploy condition.

1. List every gate marked Fail. For each, write the specific task that closes it and the single person who owns it.
2. Complete the tasks. Don't deploy around a Fail — an open gate is the gap that shows up in production.
3. Re-run the full four-gate audit. Only a clean 4/4 result clears the workflow to deploy.

> **Meridian — Result:** Four gates passed. Clear to deploy.

---

## Before you call it done

Run this test before the workflow goes live:

- **Every gate has a recorded result** — Pass or Fail, all four, no blanks. A skipped gate is a question nobody asked, and failed deploys trace back to exactly that.
- **Every Yes/Pass points to something that already exists** — a trained person (Gate 1), a written path (Gate 2), a tested real input (Gate 3), a calendar event (Gate 4). If a Pass can't point to the artifact, it isn't a Pass.
- **Every routing and ownership answer lands on a named person**, not a role or a tool — the escalation path (Gate 2) and the Human Orchestrator (Gate 4) each name who.
- **The result is 4/4.** If it isn't, you're not ready to deploy — every Fail is an assigned task, and you re-run the audit before flipping the switch.

When all four are true, the organizational side is ready, not just the technology. If any gate can't reach Pass, resolve the gap before go-live.
