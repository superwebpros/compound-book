# Signal Instrument: Constraint Identification Worksheet

**Chapter:** 04 — Signal
**Artifact produced:** One-page Constraint Statement
**Who's in the room:** Leadership team + whoever owns the metrics that are off track

---

## Purpose

Signal turns "something feels broken" into "this specific constraint costs us $X per quarter, lives in this workflow, and has existed since Y." The worksheet below is the structured path from one to the other. You leave with a one-page document the rest of the Sprint runs against.

---

## Part 1: Surface the Candidates

Before you can pick one constraint, you need an honest inventory of what's broken or slow. This is the Issue Surfacer conversation.

### Questions to ask the room:

1. What are we working around? (What manual process exists because something upstream failed?)
2. What does a new person always find confusing in their first 90 days?
3. What process would we never let a customer watch?
4. Where do we keep losing the same person or role? (Turnover clusters around constraints.)
5. What conversation keeps coming up in meetings but never gets resolved?

### If you run EOS or Scaling Up:

Pull these existing artifacts — the candidates are already in them:

- **Issues list:** Walk it and ask for each: is this the thing, or is this how the thing shows up?
- **Stalled rocks:** A rock carried 3 quarters without progress is sitting on an unnamed constraint. Ask: what would have to be true for this rock to move on its own?
- **Headcount conversations:** Every time the org reaches for a hire, a constraint is hiding underneath. Ask: what is the workflow that's generating the demand for this role?

### Output: Candidate list

Write every candidate on the board. No filtering yet. Aim for 5-10. If you have fewer than 3, you haven't been honest enough. If you have more than 15, you're listing symptoms — group them.

> **Action Step:** Open a whiteboard or shared doc. Spend 20 minutes listing candidates using the five questions above. Write everything down without filtering.

---

## Part 2: Trace Symptoms to Constraints

Most of your candidates are symptoms. A symptom is what you feel. A constraint is the thing that, if removed, would change the math.

### The Is/Is Not Test

For each candidate that feels important, run this diagnostic:

| | IS | IS NOT |
|---|---|---|
| **Where** does it occur? | (specific team, workflow, handoff) | (teams/workflows where it doesn't appear) |
| **When** does it happen? | (triggers, timing, conditions) | (conditions where it doesn't happen) |
| **Who** is affected? | (specific roles, customers) | (roles/customers who don't experience it) |
| **What** is the problem? | (precise description) | (what it is NOT — related problems that are different) |

The pattern that emerges from the IS NOT column is often more diagnostic than the IS column. If the problem occurs in quoting but not in invoicing, the constraint lives in the quoting workflow specifically — not in "operations" broadly.

### The Five Whys

For each candidate that survives the Is/Is Not test, trace it to root cause:

1. Why is this happening? → (first answer — usually a symptom)
2. Why is that the case? → (gets closer)
3. Why does that occur? → (starts touching the constraint)
4. What's beneath that? → (structural cause)
5. What's the root cause? → (the constraint itself)

**Stop rule:** You've reached the constraint when the answer points to a workflow, a handoff, a missing system, or a structural gap — not a person's behavior or a market condition.

> **Pro Tip:** If your fifth "why" points to a person ("because Sarah is the only one who knows"), reframe: the constraint is undistributed knowledge — critical information trapped in one person's head with no system to share it.

> **Action Step:** Pick your top 3 candidates. Run Is/Is Not on each. Then run Five Whys on the survivors. Cross off anything that traces to a market condition, a personality, or a problem you can't put a number on.

---

## Part 3: The Five Constraint Questions

Walk each surviving candidate through these five questions, in order. Do not skip ahead.

### Question 1: What is the problem in one sentence?

Force precision. "Our quoting process is slow" is not a sentence — it's a complaint. "Design engineers spend 4-6 hours producing initial designs for every bid, including the 50%+ that won't convert" is a sentence.

**Test:** Could someone outside your company read this sentence and understand the problem without asking a follow-up question?

### Question 2: Where does it live in the organization?

Name the team, the workflow, and the handoff. If it crosses departments, name the boundary where the breakdown occurs.

**Test:** Could you walk to the place in your building where this problem lives?

### Question 3: How long has it existed?

Months? Years? Since a system change? Since a hire? Since a departure?

Duration tells you two things: (a) how deeply embedded the workarounds are, and (b) whether the team has normalized the problem. Anything over 12 months has almost certainly been normalized.

### Question 4: What does it cost?

In hours per week, dollars per quarter, margin lost, or deals not closed. This must be a number.

**This is the gate.** Most leadership teams stop at Question 3. They name the problem, locate it, and jump to solutions. The quantified cost is what turns a complaint into a constraint you can act on.

If you cannot put a number on it, you are not at Signal yet. Keep working until you can — or move to the next candidate.

**How to estimate cost when the data isn't clean:**
- Hours: "How many hours per week does [person/team] spend on this?" × hourly loaded cost × 52 weeks
- Deals: "How many quotes/proposals/opportunities did we lose or not pursue because of this?" × average deal value
- Margin: "What would our margin be on this line if this constraint didn't exist?" minus current margin
- Speed: "How many days does this add to our cycle?" × cost of delay per day

### Question 5: If this constraint were removed, what would actually change?

Be specific. Not "things would be better" — what would be different in the next 90 days? Who would feel it? What number would move?

**Test:** If someone handed you a magic wand that removed this constraint overnight, could you describe specifically what Monday morning would look like differently?

> **Pro Tip:** Question 4 is where Signal lives or dies. "It's expensive" is not Signal. "$180,000 in overtime and rework over the last twelve months, concentrated in the operations group" is Signal. The number does two things: tells you whether the constraint is worth a Sprint, and gives the Deliver phase a target to measure against.

> **Action Step:** Walk your top candidates through all five questions. For each one, write the answers in the template below. The candidate with the strongest answers — clearest location, longest history, largest cost — is your constraint.

---

## Part 4: Lock the Constraint

Pick one. Write it up using this template.

### One-Page Constraint Statement

```
CONSTRAINT (one sentence):
_____________________________________________________________

WHERE IT LIVES (team / workflow / handoff):
_____________________________________________________________

DURATION (how long it has existed):
_____________________________________________________________

QUANTIFIED COST (dollars, hours, or margin — with math):
_____________________________________________________________

VALIDATING EVIDENCE (data checked, people consulted, numbers confirmed):
_____________________________________________________________
```

### Populated Example: PT Clinic Scheduling

```
CONSTRAINT: Patient cancellation slots are filled manually by front desk
staff, leaving 37-42% of cancellation slots unfilled despite a backlog
of patients waiting for appointments.

WHERE IT LIVES: Front desk → scheduling workflow → the manual process
of matching cancellations to the waitlist. Crosses all 5 clinic locations.

DURATION: Since the practice opened its third location (~2 years).
Workaround normalized — staff treats manual slot-filling as their job,
not as a broken process.

QUANTIFIED COST: Clinical efficiency running at 58-63% vs. 83% industry
threshold for expansion. Gap represents approximately $420K/year in
unrealized revenue across 5 locations (est. 22 unfilled slots/week ×
$75 avg visit × 5 locations × 50 weeks). Also blocking a planned 6th
location — estimated $200K+ in delayed expansion revenue.

VALIDATING EVIDENCE: Efficiency calculated live in leadership meeting.
Front desk confirmed manual process. Waitlist exists in EHR but is not
connected to cancellation notifications. No staff member disputed the
gap once calculated.
```

> **Action Step:** Fill in the template for your chosen constraint. Read it back to the room. Ask: "Is this the thing?" If anyone hesitates, you're not locked. Keep refining until the room agrees — not politely, but actually.

---

## Part 5: Failure Mode Checklist

Before you call Signal complete, check for these common failure modes:

- [ ] **Too abstract.** "We need better processes" is not a constraint. Can you point to a specific workflow?
- [ ] **Too many.** You wrote down three constraints. Pick one. A Sprint that solves three problems solves none.
- [ ] **No number.** The cost field is empty or says "significant." Go back to Q4.
- [ ] **Loudest voice won.** The constraint was named by the most senior person in the room and nobody pushed back. Ask: "Did we pick this because the data points here, or because [name] said it first?"
- [ ] **Solved the symptom.** Your constraint sentence describes what you feel, not what causes it. Run Five Whys one more time.
- [ ] **Can't be solved by a Sprint.** The constraint is "our market is shrinking" or "our founder won't delegate." These are real, but they're upstream of this book. Signal is for operational constraints a Sprint can address.

> **Pro Tip:** The inability to agree on one constraint is itself diagnostic. It almost always means the leadership team is unclear about priorities. That's a leadership problem, not a technology problem — and no AI tool resolves it.

---

## Summary of Action Steps

1. **Surface candidates** — 20 minutes, whiteboard, five questions, no filtering (Part 1)
2. **Trace to constraints** — Is/Is Not test + Five Whys on top 3 candidates (Part 2)
3. **Run the five constraint questions** — in order, no skipping Q4 (Part 3)
4. **Fill in the one-page template** — read it back to the room, get real agreement (Part 4)
5. **Run the failure mode checklist** — six checks before you call Signal locked (Part 5)

---

## Handoff to Source

The one-page constraint statement is the artifact you bring to Source (Chapter 5). Source maps the knowledge and data that surround the constraint — what the organization knows about the problem, where that knowledge lives, who holds it, and what's missing.

If you cannot hand someone this one page and have them understand what the Sprint is solving without asking a follow-up question, you are not done with Signal.

---

## Pro Tips (collected)

1. If your fifth "why" points to a person, reframe: the constraint is undistributed knowledge — critical information trapped in one head with no system to share it.
2. Question 4 is where Signal lives or dies. The number tells you whether the constraint is worth a Sprint, and gives Deliver a target to measure against.
3. The inability to agree on one constraint is itself diagnostic — it means the leadership team is unclear about priorities.

---

*This worksheet is the manual version of the Constraint Finder and Issue Surfacer instruments in the Compound Skills Library. The method is the same. The tools are a faster, more persistent version of the same conversation.*
