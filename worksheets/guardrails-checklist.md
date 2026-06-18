Compound · Build / Guardrails

# Answer the seven Guardrails Checklist questions

*Lock the quality, privacy, and oversight decisions in writing — so the human supervisor can actually supervise — before the build goes live.*

The Guardrails Checklist is the second of Build's two instruments. The Build Spec names what the agent *does*; this checklist names what it's *allowed to touch* and what happens when something goes wrong. Answer all seven questions in writing before Build executes. If any question can't be answered, the build isn't ready — that gap is a decision someone will otherwise make under pressure, after something has already gone sideways.

**Before you start, you need the locked Build Spec.** These answers attach to it as a companion document. Do this work before the build runs and it costs almost nothing; discover it after the wrong person pulls the wrong data and it costs a lot more.

Answer the seven questions in order. A blank is not a deferral — it's an undecided guardrail going to production.

---

## Question 1: Lock data access boundaries in writing

Document exactly what data the system may touch and what is off-limits, with an owner for that decision.

1. List every system and dataset the agent is permitted to touch, and mark each one read, write, or both.
2. Write the explicit off-limits list: the systems and data the agent must never reach, named so there's no ambiguity.
3. Name who decided the boundary and where it's documented, so the decision has an owner and a paper trail.

> **Meridian — Data access:** HubSpot CRM deal records (read/write), JobBOSS ERP job costing and rate card (read), cleaned pricing exceptions database (read). Off-limits: financial reporting, employee records, customer payment history, supplier contracts, or any system not listed.

---

## Question 2: Define agent autonomy vs. human sign-off

Draw the exact line between what the agent can do unilaterally and what requires a human approval before action.

1. List what the agent may do without asking anyone — the actions it takes on its own.
2. List what requires human sign-off before it happens — the actions a person must approve first.
3. Check the line for anything irreversible or customer-facing: those almost always belong on the sign-off side.

> **Meridian — Agent autonomy:** Can match RFQs to historical jobs, apply rate card pricing, apply documented exception rules, generate draft PDFs, assign confidence scores, place drafts in review queue. Cannot send anything to a customer, apply undocumented exceptions, override the rate card, or commit a quote.

---

## Question 3: Specify behavior on unrecognized inputs

Prevent the agent from guessing or going silent when it encounters something outside its design envelope.

1. Name the kinds of input the agent was *not* designed for (missing fields, unfamiliar materials, out-of-scope requests).
2. For each, write what the agent does instead of guessing: produce no answer for that item, flag it with a specific label, and stop.
3. Name where each flagged input routes and to whom, so an unrecognized input never just disappears.

> **Meridian — Unrecognized inputs:** If the RFQ references a material not in the pricing exceptions database or ERP materials list — specialty alloys like Inconel — the agent produces no price estimate for that line item, flags it as "manual pricing required," and routes to the senior engineer. If the RFQ lacks sufficient spec detail, the agent flags it as "insufficient for rapid estimate" and routes to Elena.

---

## Question 4: Define quality measurement and baseline

Make "good enough" measurable so the supervisor can calibrate review cadence and know when to trust the system more.

1. Name the specific check that tells you the output is good — compared against what baseline (the human's prior work, an accuracy target).
2. State how often you measure it and over what window.
3. Set the threshold that would let the supervisor reduce review cadence — the number that means "trust this more."

> **Meridian — Quality measurement:** Weekly comparison of agent-drafted prices to Elena's final approved prices. Target: substantive corrections on fewer than 10% of drafts within eight weeks. Historical match accuracy tracked separately, target 95% before Elena reduces review cadence on the Research Agent.

---

## Question 5: Name the escalation path

Route judgment-requiring outputs to a specific person, in a specific form, on a specific timeline — no ambiguity in the moment.

1. List the output types that need human judgment (low confidence, non-standard cases, high-stakes decisions).
2. For each, name exactly who it goes to — a person, not a role in the abstract.
3. State the form it arrives in and the timeline for a response, so the handoff isn't improvised when it happens.

> **Meridian — Escalation path:** Low-confidence quotes to Elena for full manual review. Non-standard materials to Dave Kowalski (senior engineer). Strategic account pricing to Mark Ellison (CEO). Any quote where the calculated price deviates more than 15% from the closest historical match gets flagged for Elena's investigation before approval.

---

## Question 6: Name the accountability owner

Establish who owns a bad output the same way they'd own it if a person produced it — no diffuse responsibility.

1. Name the single person — with their title — who is responsible when the agent produces a bad output.
2. Tie that name to the Hybrid Accountability Chart so the ownership is consistent across the Sprint, not invented here.
3. Confirm it's one named human, not a committee or a tool: accountability without a single name dies.

> **Meridian — Accountability:** Elena Ruiz, VP of Operations, owns every quote the agents produce, the same way she'd own it if she'd built it from scratch. She is the named human supervisor in the Hybrid Accountability Chart.

---

## Question 7: Define the kill switch condition

Pre-decide the specific failures that trigger immediate shutdown, so the decision isn't made under pressure after something goes wrong.

1. Write the specific conditions that would make you shut the workflow down immediately — error rates, a breach of scope, an output reaching a customer unreviewed.
2. State them as concrete, observable thresholds, not vibes (a number, a count, a boundary crossed).
3. Name who holds the switch and can pull it.

> **Meridian — Kill switch:** Pricing errors exceeding 20% on three quotes in any week, any quote reaching a customer without Elena's review, or any data access outside defined scope. Elena holds the switch.

---

## Before you call it done

Run this test before the checklist leaves your hands and the build goes live:

- **All seven questions are answered in writing.** No blanks. An unanswered guardrail is a decision made later, under pressure, after something has already gone wrong.
- **The answers are attached to the Build Spec as a companion document** — the spec names what the agent does, the checklist names what it's allowed to touch; they travel together.
- **Every routing and ownership question lands on a named person**, not a role, a tool, or a committee — escalation (Q5), accountability (Q6), and the kill switch (Q7) each name who.
- **The thresholds are concrete and observable** — quality (Q4) and the kill switch (Q7) are numbers someone could check, not judgment calls made in the moment.

When all four are true, these are the conditions under which the human supervisor can actually supervise. If any question can't be answered, the build is not ready — resolve the gap before going live.
