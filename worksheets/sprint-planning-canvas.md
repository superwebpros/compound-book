Compound · The Framework / Sprint Planning

# Fill in the Sprint Planning Canvas

Sketch one Sprint on a single page — eight questions, three operating fixtures, before you run anything.

The Sprint Planning Canvas is the one-page artifact the rest of the book is organized around. It names the validated constraint, captures a first-pass answer to each stage of the Sequence, identifies the team, and locks the review date. It is intentionally incomplete: the point is to stop staring at a blank page and start with something the Sequence can work against. A wrong first guess beats a blank row — guesses get corrected, blanks stay blank.

**Before you start:** You need a constraint candidate to anchor the page. If you've run a Signal Session, bring the Constraint Statement. If you haven't, write your best one-sentence guess at the bottleneck and let the stage chapters correct it. The format doesn't matter — a doc, a spreadsheet, or a whiteboard all work — as long as all eight answers, the constraint, and the three fixtures sit in one place.

Copy this table; you'll fill one row per question and the three fixtures at the top.

**Constraint:** _One sentence. The validated bottleneck, where it lives, what it costs._

**Leadership sponsor:** _____________ **Human Orchestrator:** _____________ **Quarter (review date):** _____________

| # | Question | Your first-pass answer |
|---|---|---|
| 1 | What's the validated constraint, and what does it cost? |  |
| 2 | What does the org know about it, and where does that knowledge live? |  |
| 3 | How does information flow through the workflow? |  |
| 4 | Who's accountable across humans and agents? |  |
| 5 | What's the system specification? |  |
| 6 | How does the deployment land in real work? |  |
| 7 | What changed structurally? |  |
| 8 | What's the cadence, and what's next? |  |

Then run the nine steps below to make each cell real.

---

## Name the constraint and price it

The constraint sentence is the scope boundary the entire Sprint runs against; without a number the Sprint has no target to measure.

1. Write the constraint as one sentence at the top of the Canvas: the validated bottleneck, *where* it lives, and *what it costs* per year. This is Canvas Question 1.
2. Put a real number on the cost — delayed revenue, lost bids, hours burned. If you can only estimate, estimate; mark it as a guess Signal will validate.
3. Confirm the sentence names a workflow or handoff, not a person to blame. The constraint is the structure the work is stuck in, not someone's fault.

> **Meridian example.** "Elena Ruiz is the sole quoting bottleneck. Every quote flows through her, costing an estimated \$558K/year in delayed and lost revenue." Quoting takes 3.8 days average; competitors close in 24–48 hours. The number is a first-pass estimate the Signal stage will pressure-test.

## Inventory what the org knows and where it lives

Surfaces knowledge gaps before Design so the build is not assembled from memory.

1. In Canvas Question 2, list what the organization knows about the constraint and *where that knowledge physically lives* — a person's head, a spreadsheet, an ERP, a CRM.
2. Name the people who hold critical knowledge by name and role, and flag any single point of failure (one person, one file).
3. Note which systems are connected and which are not — disconnected systems are future Design work.

> **Meridian example.** "Elena holds quoting logic. Dave Kowalski (Sr Design Engineer, 31 years) holds fabrication knowledge. Ty Banfield (Sales Lead) owns HubSpot CRM and sees RFQs first. Critical artifact: 'Customer Notes.xlsx', 147 rows of pricing exceptions Elena maintains by hand. JobBOSS ERP holds job history but isn't connected to CRM."

## Trace how information flows through the workflow

Exposes the handoffs and disconnected systems that are invisible on an org chart.

1. In Canvas Question 3, walk the workflow start to finish: where the work enters, every hand-off between people and systems, and where it exits to the customer or next step.
2. Count the handoffs and call out the disconnected systems — these are where the work slows and breaks.
3. Keep it to the path the constraint actually travels; don't diagram the whole company.

> **Meridian example.** "RFQ lands in HubSpot via Ty. Ty pastes the inquiry into an email to Elena. Elena opens Customer Notes.xlsx, cross-references JobBOSS history, asks Dave about fabrication feasibility, drafts a quote in Word, sends it back to Ty, Ty sends it to the customer. Five handoffs, two systems disconnected."

## Assign accountability across humans and agents

Every role — human and agent — needs one named owner before any code is written.

1. In Canvas Question 4, sketch who (or what) owns each part of the workflow once AI is in the loop: what the agent drafts or pulls, and who reviews and approves.
2. Name a human who owns judgment on the hard cases, and name who validates output before it reaches the customer.
3. Don't leave any lane unowned. This is a first pass at the Hybrid Accountability Chart you'll build in Design — one named owner per lane.

> **Meridian example.** "AI drafts quotes by pulling customer history from HubSpot, job data from JobBOSS, and exception rules from Customer Notes.xlsx. Elena reviews and approves, owns judgment on non-standard jobs. Ty routes inbound RFQs and validates final quotes before they go to the customer. Dave is consulted for fabrication-heavy exceptions only."

## Draft the system specification

Locks what the build must produce and what guardrails it must honor, preventing scope drift in Build.

1. In Canvas Question 5, name what gets built: the knowledge capture, the workflow connections between systems, and the agent or assistant that does the work.
2. Write at least one guardrail — the thing the system may *not* do without a human. This becomes your Guardrails Checklist in Build.
3. Keep it a first-pass spec, not a contract. Build will sharpen it; the Canvas just locks the intent.

> **Meridian example.** "Knowledge capture sessions with Elena and Dave, structured into a quoting knowledge base. n8n workflow connecting HubSpot → JobBOSS → Claude for quote generation. Claude-powered quoting assistant that applies documented pricing logic and flags exceptions for Elena's review. Guardrails: no quote ships without Elena's approval until the workflow has been calibrated for sixty days."

## Define how the deployment lands in real work

Forces a per-role answer before launch, which is the gap where most AI projects fail.

1. In Canvas Question 6, state the target outcome in a measurable number (turnaround, volume, error rate) and how each role's day changes once the system is live.
2. Write a per-role runbook line: what each named person does differently the morning after launch.
3. Define a Delivery Test — a concrete count of real work through the new workflow inside a fixed window — so you'll know if it actually landed.

> **Meridian example.** "Quote turnaround target: under eight hours. Ty initiates a draft quote without Elena in the room. Exception flags catch non-standard jobs before they go out. Per-role runbook for Elena (review queue, override patterns), Ty (initiation, validation), and Dave (exception-only consults). Delivery Test: thirty quotes through the new workflow inside thirty days."

## Describe what changes structurally after the Sprint

Commits the team to a specific operating-model change rather than a tool no one uses.

1. In Canvas Question 7, name how roles shift: who stops doing what, who picks up what, and what knowledge moves out of one head into a shared place.
2. Name the new agent the org now operates and who supervises it — this is the first entry in your Hybrid Org Today.
3. Frame it as a structural change, not a tool purchase. The test: would an org chart drawn after the Sprint look different from before?

> **Meridian example.** "Elena's role shifts from quote producer to quote reviewer. Ty's role expands from RFQ routing to quote initiation. The Customer Notes.xlsx artifact migrates from Elena's desktop into a structured knowledge base every agent and human can read. The Hybrid Org Today picks up its first explicit agent: the quoting assistant, supervised by Elena."

## Set the cadence and identify the next Sprint

Books the review date and names the next constraint, turning one Sprint into a compounding system.

1. In Canvas Question 8, set the review date (the quarterly operating session where this Sprint's outcome gets measured) and name what happens if the Delivery Test passes vs. fails.
2. Name the next Sprint candidate — the next constraint you'd tackle once this one closes — so the work compounds instead of stopping.
3. Note what artifact carries forward (the Sprint Outcome Record) so the next quarter starts from this quarter's result, not a blank page.

> **Meridian example.** "Quarterly review at end of Q3. If the Delivery Test passes, the next Sprint candidate is scheduling, the next Elena-dependent workflow. If it doesn't pass, the Sprint regroups in Signal and revalidates the constraint. The Sprint Outcome Record carries forward to Q4."

## Name the three operating fixtures: sponsor, Orchestrator, review date

A Sprint without a named sponsor, orchestrator, and calendar date has no accountability and no deadline.

1. **Leadership sponsor** — name the person accountable for the *outcome*, not the person doing the work. One name, no "leadership team."
2. **Human Orchestrator** — name the person who runs the Sprint day-to-day, owns the cadence, and holds the handoffs together. (If you run EOS, think Integrator extended to run the agent team — Sprint-level scope, same accountability.)
3. **Review date** — book the quarterly operating session on the calendar *before* Signal begins, and list its attendees. A Sprint with no review date has no deadline; the Sprint is real when the review is on the calendar.

> **Meridian example.** Leadership sponsor: Mark Ellison (CEO). Human Orchestrator: Elena Ruiz (VP of Operations). Quarter: Q3. Review: quarterly operating session, end of Q3; attendees Mark Ellison, Elena Ruiz, Ty Banfield, Dave Kowalski; calendar invite sent before Signal begins.

---

## Before you call it done

Hand the Canvas to someone who wasn't in the room. They should be able to read it and know the constraint, the plan, and who's on the hook — without coming back to ask. Check:

- [ ] The **constraint** is one sentence with a **dollar (or hours) cost** at the top of the page.
- [ ] All **eight questions** have a first-pass answer — a guess where you don't know yet, never a blank row.
- [ ] Every lane in Question 4 has a **named owner**; no unowned work, no "TBD."
- [ ] Question 5 names at least one **guardrail** the system may not cross without a human.
- [ ] Question 6 names a **measurable target** and a **Delivery Test** with a count and a window.
- [ ] The three **operating fixtures** are named with real people: sponsor, Human Orchestrator, review date.
- [ ] The **review date is on the calendar** before Signal begins, with attendees listed.
- [ ] Question 8 names the **next Sprint candidate**, so this Sprint compounds into the next.

A blank row isn't a failure — it's a diagnostic. The blanks are exactly what the stage chapters teach you to fill in. Carry the Canvas forward.
