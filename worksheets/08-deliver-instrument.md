# Launch Checklist & Sprint Outcome Template

**Book:** Co-Intelligent Co-Operation
**Chapter:** 08 — Deliver
**Instrument:** Launch Checklist & Sprint Outcome Template

---

## Purpose

Deployed is not delivered. Deployed means the workflow is turned on. Delivered means people's work actually changed — and you can prove it with a number.

This instrument gives you the five parts that separate a real delivery from a premature launch: a readiness audit, per-role runbooks, an operational log, a sprint outcome measurement, and a delivery test. Complete all five. Skip none. The order matters.

---

## Part 1: Deploy Readiness Audit

Four binary pass/fail gates. Answer each one honestly. If any answer is "no," stop. Fix it. Then come back.

| # | Gate | Pass / Fail |
|---|------|-------------|
| 1 | Has every person whose work changes been trained on what is different? Not "informed" — trained, with hands-on practice. | [ ] Pass / [ ] Fail |
| 2 | Is there a documented escalation path for when the workflow produces unexpected output? | [ ] Pass / [ ] Fail |
| 3 | Has the workflow been tested against real data from the last 2 weeks? Not demo data — actual inputs from your operation. | [ ] Pass / [ ] Fail |
| 4 | Is the Human Supervisor's review cadence defined and on the calendar? | [ ] Pass / [ ] Fail |

**Result:** ______ / 4 Pass

If the result is not 4/4, you are not ready to deploy. Every "Fail" is a task. Assign it, complete it, re-run the audit.

### Action Steps

1. List every person whose daily work changes because of this sprint.
2. For each person, confirm they have completed hands-on training — not a slide deck, not a walkthrough email. Hands on keys.
3. Write the escalation path. Name the person, the channel, and the expected response window.
4. Pull real inputs from the last two weeks. Run them through the workflow. Document every failure.
5. Open the Human Supervisor's calendar. Book the review cadence. Recurring. Non-negotiable.

> **Pro Tip:** The audit is not a formality. It is a pre-flight check. Pilots do not skip items on the checklist because they have flown before. Neither do you.

---

## Part 2: Write the Per-Role Runbook

For every role affected by the sprint, document three things: what they receive, what they produce, and when they escalate.

| Role | Input (what they receive) | Output (what they produce) | Escalation (when and how to flag an issue) |
|------|---------------------------|----------------------------|--------------------------------------------|
| | | | |
| | | | |
| | | | |
| | | | |

For each role, answer these four questions:

1. What does this person now do differently than before the sprint?
2. What does the agent handle that this person used to handle?
3. How does this person review agent output?
4. What triggers an escalation?

### Action Steps

1. List every role the sprint touches. Not job titles — roles in the workflow.
2. Fill in one row per role. Be specific. "Reviews output" is not specific. "Opens the quote draft in the shared folder, checks unit costs against the rate card, approves or flags within 4 hours" is specific.
3. For each role, write one sentence that answers: "What changed about this person's job?"
4. For each role, define the escalation trigger. Not "when something seems wrong." A concrete condition: a threshold, a category, a pattern.

> **Pro Tip:** The runbook test: could someone who was on vacation during the entire sprint sit down with this document and know exactly what changed about their job? If not, the runbook is not done.

---

## Part 3: Build the Operational Log

Track what happens in the first 2-4 weeks after deploy. Every entry is a signal.

| Date | What happened | Category | What it signals |
|------|---------------|----------|-----------------|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

**Categories** (use exactly these):

- **Unplanned intervention** — a human had to step in where the agent was supposed to handle it
- **Data gap** — the workflow needed information that does not exist or was not connected
- **Edge case** — an input the design did not account for
- **User confusion** — a person whose work changed did not know what to do

### Action Steps

1. Create the log on day one of deployment. Not day three. Day one.
2. Assign a person to own the log. One person. Named. Accountable.
3. Set a daily check-in for the first two weeks: review the log, categorize new entries, note patterns.
4. At the end of week two, tally entries by category. The category with the most entries is the first thing to fix.

> **Pro Tip:** The operational log is not a complaint box. It is a sensor. Every entry tells Design something about the next sprint. If the same category keeps appearing, that is the next constraint.

---

## Part 4: Measure the Sprint Outcome

Pull the constraint statement from Signal. Write the production result beside it. No narratives. Numbers.

```
SIGNAL STATEMENT:   [the one-sentence constraint from Signal]
COST AT START:      [the quantified cost from Signal — dollars, hours, or margin]
RESULT AFTER SPRINT: [what actually happened — measured against the same metric]
DELTA:              [the change — quantified]
OUTCOME IN ONE SENTENCE: [what this sprint produced, stated plainly]
```

### Action Steps

1. Go back to the Signal instrument. Copy the constraint statement and the quantified cost exactly as written.
2. Measure the same metric now. Same unit, same timeframe, same source.
3. Calculate the delta. If the delta is zero or negative, the sprint did not deliver against the constraint.
4. Write the outcome in one sentence. No spin. What happened.

> **Pro Tip:** If you cannot fill in the "Result After Sprint" line with a number, go back to the operational log and figure out what you need to measure. The sprint has not delivered until a number moved.

---

## Part 5: The Delivery Test

Three questions that separate "deployed" from "delivered." Check each one.

- [ ] Can the people whose work changed describe, concretely, what they now do differently?
- [ ] Has the workflow produced results on real inputs for at least two weeks without reverting to the old process?
- [ ] Can you show the leadership team a number that moved — tied directly to the constraint Signal identified?

**Result:** ______ / 3 Yes

If all three are yes, the sprint delivered. If not, you deployed. There is a difference.

---

## Populated Example: Manufacturing Quoting Sprint

### Deploy Readiness Audit

| # | Gate | Pass / Fail |
|---|------|-------------|
| 1 | Design engineers completed a 90-minute hands-on session building quotes with the new rapid-estimate workflow. Each engineer produced a practice quote and received feedback. | [x] Pass |
| 2 | Escalation path documented: any quote flagged by the agent as "low confidence" routes to the senior design engineer via Slack with a 2-hour response SLA. | [x] Pass |
| 3 | Workflow tested against 47 real RFQs received in the prior two weeks. 44 produced accurate estimates. 3 edge cases identified and added to the escalation criteria. | [x] Pass |
| 4 | Ops manager reviews agent-generated quotes every Monday and Thursday at 9 AM. Calendar hold in place. Review checklist documented. | [x] Pass |

**Result:** 4/4 Pass. Clear to deploy.

### Per-Role Runbook

| Role | Input (what they receive) | Output (what they produce) | Escalation (when and how to flag an issue) |
|------|---------------------------|----------------------------|--------------------------------------------|
| Design Engineer | Agent-generated rapid estimate with material specs, unit costs, and confidence score | Reviewed and approved quote, or flagged revision with specific line-item corrections | Flag any quote where confidence score is below 85% or where material spec does not match the RFQ bill of materials. Route to senior design engineer in Slack #quoting-escalations. |
| Ops Manager | Dashboard of all quotes generated in the review period, with status (approved / flagged / pending) | Bi-weekly review summary: volume, approval rate, average turnaround, escalation count | Flag if approval rate drops below 90% for any rolling 5-day window. Escalate to sprint lead for design review. |
| Sales Rep | Approved quote PDF in shared drive, notification in CRM | Customer-facing proposal incorporating the approved quote, sent within 24 hours of quote approval | Flag if quote does not match customer's stated requirements or if turnaround exceeds 48 hours from RFQ receipt. Notify ops manager. |

**What changed per role:**

- **Design Engineer:** Previously built quotes from scratch (4-6 hours each). Now reviews agent-generated rapid estimates (20 minutes each). Engineering judgment shifts from creation to validation.
- **Ops Manager:** Previously tracked quoting by asking engineers for status updates. Now reviews a dashboard with real-time volume, turnaround, and escalation data.
- **Sales Rep:** Previously waited 3-5 days for engineering to produce a quote. Now receives approved quotes within 24 hours of RFQ submission.

### Operational Log (First Two Weeks)

| Date | What happened | Category | What it signals |
|------|---------------|----------|-----------------|
| Day 2 | Agent generated a quote for a custom alloy not in the material database. Defaulted to standard steel pricing. Engineer caught it in review. | Edge case | Material database needs custom alloy entries. Add to Source backlog. |
| Day 4 | New sales rep (started last month) submitted an RFQ without attaching the customer's drawing. Agent produced an estimate based on incomplete specs. | User confusion | Onboarding materials need to include the new RFQ submission process. Runbook gap for new hires. |
| Day 7 | Agent produced a quote with a confidence score of 92%, but the unit cost was 15% above the rate card because the quantity tier was misread from the RFQ. | Unplanned intervention | Quantity-tier parsing needs refinement. Design task for next sprint. |
| Day 9 | Ops manager's Thursday review surfaced that 3 quotes were stuck in "pending" because the approval notification did not fire. | Data gap | Notification trigger depends on a CRM field that is not consistently populated. Integration fix needed. |
| Day 12 | Design engineer approved a quote without checking the confidence score because "they all look fine now." Skipped the review checklist. | User confusion | Review discipline is slipping. Ops manager to reinforce the checklist in the next bi-weekly review. |

### Sprint Outcome Measurement

```
SIGNAL STATEMENT:    Design engineers spend 4-6 hours per quote, creating a bottleneck
                     that delays proposals and deprioritizes high-probability bids.
COST AT START:       ~30 engineering hours/week on quoting; average quote turnaround
                     of 4.2 days; win rate on quoted deals: 22%.
RESULT AFTER SPRINT: ~5 engineering hours/week on quote review; average quote turnaround
                     of 0.8 days; win rate on quoted deals after 3 months: 32%.
DELTA:               25 engineering hours/week recovered; turnaround reduced by 81%;
                     win rate increased 10 percentage points.
OUTCOME IN ONE SENTENCE: Rapid-estimate workflow freed design engineers from quote
                     creation, cut turnaround from 4 days to under 1, and produced a
                     10-point win rate increase by letting the team focus engineering
                     time on high-probability bids.
```

### Delivery Test

- [x] Can the people whose work changed describe, concretely, what they now do differently? — Yes. Engineers review instead of build. Sales reps receive quotes in hours instead of days. Ops manager reads a dashboard instead of chasing status updates.
- [x] Has the workflow produced results on real inputs for at least two weeks without reverting to the old process? — Yes. 47 quotes processed in weeks one and two. No reversion to manual quoting.
- [x] Can you show the leadership team a number that moved? — Yes. 25 hours/week recovered. Quote turnaround down 81%. Win rate up 10 points in 3 months.

**Result:** 3/3 Yes. The sprint delivered.

---

## Summary

Delivery is five things, in order:

1. **Deploy Readiness Audit** — Four gates. All must pass before you turn anything on.
2. **Per-Role Runbook** — Every affected role knows what changed, what they receive, what they produce, and when to escalate.
3. **Operational Log** — A running sensor for the first 2-4 weeks. Every entry is data for the next sprint.
4. **Sprint Outcome Measurement** — The constraint from Signal, the cost at start, the result after, the delta. Numbers, not narratives.
5. **Delivery Test** — Three questions. All yes means delivered. Anything less means deployed.

Deployed is not delivered. This instrument is the difference.

---

## Handoff

When this instrument is complete, you hold three things:

1. **A proven runbook** that any team member can follow — including someone who missed the entire sprint.
2. **An operational log** that tells you exactly what the next sprint needs to address.
3. **A measured outcome** tied to the constraint Signal identified — the number that proves the sprint produced value.

The operational log feeds directly back into Signal for the next sprint. The categories with the most entries point to the next constraint. The cycle continues.

Take the completed Sprint Outcome Measurement to leadership. Take the operational log to your next sprint's Signal phase. Take the runbook to every person whose work changed.

The sprint is not over when the workflow is live. The sprint is over when the work is different and you can prove it.
