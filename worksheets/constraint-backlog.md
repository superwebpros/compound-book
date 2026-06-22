Signal · Signal / Constraint Backlog

# Build the Constraint Backlog and select the one

*Land every candidate constraint that survived the trace in one standing table, then commit the Sprint to the one that's load-bearing.*

The Five Whys turns your symptoms into candidate constraints — the structural roots a Sprint can actually fix. This worksheet captures those candidates in the Constraint Backlog (the standing table you carry into every Sprint that follows) and walks the selection: filter for the ones you can act on, find the one whose removal unblocks the rest, and commit the Sprint to it. **Before you start, you need the candidate constraints from your Five Whys trace — the symptoms that bottomed out at a workflow, a handoff, or a missing system, not at a person or a market condition.**

---

## Enter every candidate constraint in the backlog table

The Backlog is the standing inventory of everything worth a Sprint. It's born here, in this session, and every later Sprint draws from it — so write the candidates down even though you'll only commit to one.

1. Make a table with five columns: candidate constraint, owner, closeable in one Sprint?, cost / measure, load-bearing?
2. Add one row for each candidate constraint that survived the Five Whys. Write each as a single structural sentence — the workflow, handoff, or missing system, not the symptom you started from.
3. Don't rank them yet. This pass is just an honest inventory of what a Sprint could fix.

| Candidate constraint | Owner | Closeable in one Sprint? | Cost / measure | Load-bearing? |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

> **Meridian:** Three symptoms survived the trace — the quoting bottleneck, manual job costing, and PM task visibility. Each went into the Backlog as a one-line structural statement: "Quoting workflow depends on one person's undocumented context," "Job costing is manual; margin not visible until after close," "PM task updates are driven by the VP of Ops, not the system."

---

## Fill in owner, closeable, and cost for each row

These three fields are the eligibility test. A candidate without them isn't a real contender yet, no matter how much it hurts.

1. **Owner** — name one person who would move this if it became the Sprint. A name, not "the team." No owner means no one drives it.
2. **Closeable in one Sprint?** — yes, or "needs breakdown." If the candidate is too big to close in a single Sprint, it has to be broken into a tighter constraint first.
3. **Cost / measure** — a rate or a unit per period: dollars per quarter, hours per week, deals lost per period, days of cycle time. "Significant" is not a number. If the data isn't clean, estimate it and note the estimate.

> **Meridian:** Quoting — owner Ops, closeable yes, ~$558K/year in lost revenue and floor capacity. Job costing — owner Finance, closeable yes, cost still to be estimated. PM visibility — owner VP of Ops, closeable yes, ~4 hours/week of VP time.

---

## Filter for the eligible candidates

You commit only to a candidate you can actually own, measure, and close. The rest aren't dropped — they wait in the Backlog until they're ready.

1. Mark any row with no owner, no cost estimate, or a "needs breakdown" as **not-ready**. It stays in the Backlog; it's just not in the running this Sprint.
2. Confirm the remaining rows each have a name, a number, and a yes. Those are your eligible candidates.
3. If nothing is eligible, you're not done with the trace or the quantification — go back before you go forward.

> **Meridian:** All three candidates had an owner and were closeable in a Sprint, so all three stayed in the running. The only soft spot was the job-costing cost, still an estimate — flagged, but good enough to keep it eligible.

---

## Find the load-bearing one

A Sprint improves the system only by removing the constraint that currently governs it. The load-bearing candidate is the one whose removal unblocks or clarifies the others.

1. For each eligible candidate, ask the test: if you solved this one, would it make two or more of the others easier to evaluate, easier to solve, or unnecessary?
2. The candidate that unblocks the others is the load-bearing one. Mark it. That's where the Sprint starts.
3. If exactly one candidate clearly governs the rest, you're done selecting — skip the cost tiebreak below.

> **Meridian:** The quoting bottleneck was load-bearing. Until Elena's undocumented pricing context was distributed, Finance couldn't build reliable margin forecasts and the PM gap kept getting papered over with VP hours. Solving quoting made the other two easier to evaluate — so quoting was the constraint.

---

## Cost tiebreak — only if none clearly governs

When the eligible candidates are genuinely independent and none unblocks the others, the dollar number breaks the tie.

1. Confirm no single candidate governs the rest — they're separate problems, not a chain.
2. Pick the costliest eligible candidate you can close in a Sprint. The biggest provable payback wins.
3. If the costs are close, take the one whose number is hardest to dispute — the estimate the room will hold each other to.

> **Meridian:** Not needed. Quoting governed the other two, so the load-bearing test settled it before cost ever had to arbitrate.

---

## Commit the one and record the rest as the standing Backlog

Focus is the whole point: one constraint, one target, one number to earn back. The others don't disappear — they become the queue for the Sprints that follow.

1. Mark the selected candidate as **the constraint**. It goes on to the Constraint Statement and the top of the Sprint Planning Canvas as the Sprint's single target.
2. Keep every other candidate in the Backlog, with its owner and cost. This is the standing inventory you'll re-rank in Compound after the Sprint closes.
3. Note that ordering the rest of the Backlog is a separate exercise — you're committing to one now, not ranking the queue.

> **Meridian:** Quoting was committed as the Sprint's constraint and written into the Constraint Statement. Job costing and PM visibility stayed in the Backlog, owners and estimates attached, ready for the Compound re-rank.

---

## Before you call it done

Run this test before you leave the Backlog and move to the Constraint Statement:

- **Every surviving candidate is in the table** — one structural sentence each, with an owner and a cost or a flag that it still needs one.
- **Ineligible candidates are marked not-ready** — no owner, no number, or too big — and left in the Backlog, not deleted.
- **The load-bearing one is identified** — or, if none governs, the cost tiebreak has picked the costliest you can close.
- **One constraint is committed** as the Sprint's target, and the rest are recorded as the standing Backlog for future Sprints.

When all four are true, you have a Backlog you can return to every quarter and a single constraint the Sprint can earn its keep against.
