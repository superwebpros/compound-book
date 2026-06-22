Compound · Compound / Sprint Retrospective

# Run the Sprint Retrospective

Review the Sprint that just shipped — honestly — and turn its friction into design constraints for the next one.

The Sprint Retrospective is the structured review you run after a Sprint delivers. It asks the same questions every time: what worked, what didn't, and — for every failure — what would have to be true for it not to happen again. The output isn't a feelings recap; it's a short list of design constraints the next Sprint inherits. This worksheet captures the answers so they survive past the room.

**Before you start:** Bring the people who owned Sprint accountabilities — your Human Orchestrator and any supervisors who owned lanes. Bring the Sprint outcome number you measured in Deliver (the constraint metric, before and after). The room has to be safe enough for honest answers; if no one will name what broke, the retrospective produces nothing.

Copy this page and fill it in live during the session — one row per worked / didn't-work item, then the four-field change card, then the three compounding answers.

---

## Ask: what worked?

Name the specific design decisions that paid off — mechanism, not sentiment — so they can be intentionally repeated.

1. List each thing that worked as a **mechanism**, not a compliment. "The team did great" is not an answer; "the workflow that cut quoting time" is.
2. For each one, write **why** it worked — the specific design decision (a workflow step, a chosen Human Orchestrator, an agent's data access) that produced the result.
3. Mark which of these you want to **deliberately keep** in the next Sprint's design, so a good decision doesn't quietly get dropped.

> **Meridian example.** What worked: the new intake workflow cut standard quote turnaround from 3.8 days to 4.2 hours. Why: Elena's pricing exceptions were captured as 112 validated rules the agent could apply, and the agent had three years of indexed ERP job data to match against. Keep: the validated-rules layer and the indexed job data carry into Sprint two.

## Ask: what didn't work?

Surface the broken handoffs, dirty inputs, and wrong cadences — the honest friction every Sprint produces.

1. List each thing that broke or underperformed: handoffs that failed, inputs dirtier than Source claimed, supervisor reviews skipped because the cadence was wrong, scope that ran thin.
2. For each item, name **who** raised it and **what specifically** went wrong — concrete enough that someone outside the room understands the failure.
3. Don't stop at the first item. If the "didn't work" column has zero entries, you didn't run it honestly — every Sprint has friction.

> **Meridian example.** Three items surfaced. (1) Dave Kowalski: the agent's historical matching was right ~85% of the time but missed complexity — Elena was correcting about one in eight quotes. (2) Ty admitted he forwarded three RFQs to Elena the old email way in week one out of habit. (3) Carlos: every Inconel or titanium job still routed to Elena manually because the materials database didn't cover specialty alloys.

## For each failure, ask: what would have to be true for this not to happen again?

Reframe blame into a design fix — convert each observation into an actionable constraint on the next Sprint's design.

1. Take each "didn't work" item and answer the single question: *what would have to be true for this not to happen again?* The answer is a **design fix**, not a person to coach.
2. Write the fix as a concrete change to the system — a workflow step, a data field, a killed fallback path, an added Source — and note whether it's a **design fix** or a **knowledge gap**.
3. Keep the failure and its fix paired on the same line, so nothing surfaces without a proposed change attached.

> **Meridian example.** (1) Agent misses complexity → the agent needs fabrication complexity indicators (bend count, tolerance class, surface finish), not just material and dimensions. (2) Old email path still used → kill the old email path on day one, not leave it open as a fallback. (3) Specialty alloys route manually → add the five most common non-standard materials before Sprint two.

## Ask: what one design change would make the next Sprint better?

Force the prioritization before the session ends; this feeds directly into the Install One Design Change step.

1. Look across **everything** the Sprint surfaced — the thin Source phase, the wrong cadence, the broken handoff, the unscoped dirty input. Then name the **single** change that will most improve the next Sprint. One, not a "lessons learned" list.
2. Write it on the four-field change card. **Any blank field means the change is too vague to install:**

   | Field | Fill in |
   |---|---|
   | **What** the change is | |
   | **Who** owns installing it | |
   | **How you'll know** it worked | |
   | **By date** (before next Sprint kickoff) | |

3. Confirm the change is **structural** — a chart entry, a workflow step, a guardrail, a Source map update — not just an insight in a doc. An insight that doesn't change the design isn't worth recording.

> **Meridian example.** One design change: add fabrication complexity indicators (bend count, tolerance class, weld count, surface finish) as matching criteria in the Quote Research Agent. **Who:** Dave Kowalski supplies the classification framework; the agent applies it. **How you'll know:** re-run the eight quotes Elena corrected last month; at least seven of eight now produce the correct comparable. **By date:** installed before Sprint two kickoff.

## Measure what compounded (three compounding questions)

Distinguish output (the Sprint delivered something) from compound interest (the Sprint built infrastructure the next Sprint inherits).

1. Answer: **what does the organization know now that it didn't know before this Sprint?** Name the specific learning, with numbers where you have them.
2. Answer: **what capability exists now that didn't exist before?** Name the working thing that doesn't disappear when the Sprint ends — and its measured effect.
3. Answer: **what is the next Sprint starting with that this one didn't have?** List the concrete assets the baseline now includes. If you can't answer all three, the Sprint produced output but didn't compound.

> **Meridian example.** Knows now: Elena's 147-row Customer Notes spreadsheet held only 112 validated rules (35 were duplicates or outdated), and ~70% of volume is standard-spec the agent handles cleanly. Capability now: a working quoting agent team — standard turnaround 3.8 days → 4.2 hours, Elena's quoting 15 hrs/week → 5, throughput doubled, $47K new revenue in month one. Next Sprint starts with: three trained agents, 112 validated rules, three years of indexed ERP job data, and a sales team six weeks into the new intake workflow.

---

## Before you call it done

Hand this page to someone who wasn't in the room. They should be able to install the next Sprint's improvements from what's written, without coming back to ask. Check:

- [ ] The **what worked** list names **mechanisms**, not sentiment — each with the design decision behind it.
- [ ] The **what didn't work** column has **at least one** honest entry (zero means you didn't run it honestly).
- [ ] Every failure is paired with a **"what would have to be true"** fix, tagged design fix or knowledge gap.
- [ ] Exactly **one** design change is named — not a lessons-learned list.
- [ ] The change card has **no blank fields**: What / Who / How you'll know / By date are all filled.
- [ ] The one change is **structural** (chart, workflow, guardrail, or Source map), inheritable by the next Sprint.
- [ ] All **three compounding questions** are answered. If any is blank, the Sprint delivered output but didn't compound.

Carry the change card and the compounding answers into the Compound session, where the one change gets installed and the Constraint Backlog gets re-ranked.
