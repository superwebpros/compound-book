# Instrument 09: Sprint Retrospective Guide + Constraint Re-rank

**Chapter:** 09 — Compound
**Phase:** Compound (the learning and compounding phase)
**Use when:** A sprint has completed Deliver and you are preparing the ground for the next sprint.

---

## Purpose

The sprint is not the value. The compounding across sprints is the value.

Sprint 1 produces a result. Sprint 2 starts from a higher baseline because of what Sprint 1 built. That delta — the knowledge gained, the capability installed, the friction removed — is the compound interest. This instrument captures it, ranks your next move, and installs the one design change that makes the next sprint better than the last.

---

## Part 1: Sprint Retrospective

Three questions. Ask them in order. The room must be safe enough for honest answers.

### Question 1: What worked?

What in this sprint produced the result? Be specific — name the workflow, the tool, the decision, the person. Not "the team did great." What specifically worked?

| What Worked | Why It Worked (the mechanism) |
|---|---|
| | |
| | |
| | |

### Question 2: What did not work?

Where did the sprint struggle? Where did the design break? Where did the build miss? Where did the rollout stall? Name systems and processes, not people.

For each item, the facilitator asks: **"What would have to be true for this to not happen again?"** This reframes blame into design.

| What Did Not Work | What Would Have to Be True to Prevent It |
|---|---|
| | |
| | |
| | |

### Question 3: What one design change would make the next sprint better?

One change — the one that, applied before the next sprint begins, would have the highest impact on sprint quality.

**The one design change:**

> _____________________________________________________________

This is a commitment, not a suggestion. It gets implemented before the next sprint starts.

**Rules for the retrospective:**

- Focus on systems and processes, not individuals.
- Every observation must be specific (name the workflow, the tool, the handoff).
- The facilitator asks "what would have to be true for this to not happen again?" to reframe blame into design.
- The "one design change" is a commitment. It gets installed before the next sprint starts. See Part 4.

**Pro Tip:** If your retrospective produces zero "what didn't work" items, you didn't run it honestly. Every sprint has friction. The question is whether your team feels safe enough to name it.

**Action Step:** Schedule the retrospective before the sprint ends — not after. Put it on the calendar the day you start Build. If it's not scheduled, it won't happen.

---

## Part 2: Measure What Compounded

Beyond the sprint outcome (measured in Deliver), ask these three questions. The answers ARE the compound interest.

| Question | Answer |
|---|---|
| What does the organization know now that it didn't know before this sprint? | |
| What capability exists now that didn't exist before? (A workflow, a documented process, an agent, a captured expertise) | |
| What is the next sprint starting with that the first sprint didn't have? (Better data, clearer roles, proven tools, documented exceptions) | |

Sprint 1 produces a result. Sprint 2 starts from a higher baseline because of what Sprint 1 built. That delta is the compounding. If you cannot answer these three questions, the sprint delivered output but did not compound.

---

## Part 3: Constraint Re-rank

Pull the Signal Backlog — the list of constraint candidates from Signal that didn't get picked for this sprint.

Re-rank the backlog using these four questions:

| Re-rank Question | What You Learned |
|---|---|
| 1. Did the sprint reveal new information about any of the other constraints? (Often solving one constraint exposes the real cost of another) | |
| 2. Did any constraints get partially resolved as a side effect of this sprint? | |
| 3. Did any new constraints surface during the sprint that weren't on the original list? | |
| 4. Given what you now know, which constraint should the next sprint solve? | |

### Re-ranked Signal Backlog

| Rank | Constraint | Rationale for Rank (what changed since last sprint) |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

The constraint at rank 1 becomes the input for the next Signal conversation.

**Pro Tip:** The constraint you pick for Sprint 2 should be informed by Sprint 1's outcome. If you're picking the same constraint again, the sprint didn't deliver — go back to the operational log and figure out what's still broken.

**Action Step:** Pull the Signal Backlog. Re-rank it using the four questions. Name the top constraint. Assign a Human Orchestrator for the next sprint.

- **Top constraint for next sprint:** ___________________________
- **Human Orchestrator for next sprint:** ___________________________

---

## Part 4: Install the One Design Change

The one design change from the retrospective (Part 1, Question 3) must be installed before the next sprint starts. Not "considered." Installed.

| Question | Answer |
|---|---|
| What is the change? (Specific — a new process step, a new guardrail, a reconfigured tool, a reassigned role) | |
| Who installs it? (Named person) | |
| How will you know it's working? (Observable evidence, not a feeling) | |
| When is it installed by? (Date, before next sprint kicks off) | |

---

## Part 5: Update the Living Documents

Three artifacts get updated at the end of every sprint. Do not skip this. The documents are the institutional memory that makes compounding possible.

- [ ] **Hybrid Accountability Chart** — any row that was temporary (for the sprint) becomes permanent if the workflow is staying. Any row that didn't work gets revised.
- [ ] **Signal Backlog** — re-ranked per Part 3.
- [ ] **Sprint Outcome Record** — the one-sentence outcome from Deliver, filed for future reference.

---

## Populated Example

**Context:** A manufacturing company ran a Compound Sprint to solve the constraint "quoting takes too long and loses deals."

### Part 1: Sprint Retrospective

**What worked:**

| What Worked | Why It Worked |
|---|---|
| Rapid estimate workflow using an AI agent built on historical quote data | Cut quote generation from hours to 20 minutes. The agent had access to 3 years of pricing data and could match specs to past jobs. |
| Ops manager as Human Orchestrator | She knew every pricing exception and could validate agent output in real time during the first week. |

**What did not work:**

| What Did Not Work | What Would Have to Be True to Prevent It |
|---|---|
| 3 edge cases in the first two weeks where the estimate was off by >15% — all involved legacy pricing exceptions the agent didn't have | The agent's knowledge base would need to include the ops manager's pricing exception spreadsheet, not just standard pricing tables. |
| Sales reps bypassed the new workflow for "urgent" quotes twice in week one | The workflow would need to be faster than the old method for every case, or the escalation path would need to be clearer. |

**The one design change:**

> Add the ops manager's pricing exception spreadsheet to the agent's knowledge base before Sprint 2.

### Part 2: Measure What Compounded

| Question | Answer |
|---|---|
| What does the organization know now? | Which quote types the agent handles cleanly (standard specs) and which need human review (legacy pricing exceptions). This was unknown before — they assumed all quotes were equally complex. |
| What capability exists now? | A working rapid-estimate agent that handles 85% of incoming quote requests without human intervention. |
| What is Sprint 2 starting with? | A trained agent, a documented exception list, and sales reps who have used the new workflow for two weeks. |

### Part 3: Constraint Re-rank

| Rank | Constraint | Rationale |
|---|---|---|
| 1 | CRM-to-ERP data sync forces manual reconciliation | The quoting sprint exposed this — every quote the agent generated still had to be manually entered into the ERP. This is now the highest-friction handoff in the sales process. |
| 2 | Customer onboarding takes 3 weeks | Unchanged, but less urgent now that quoting is faster. |
| 3 | Field service scheduling is manual | No new information from this sprint. |

- **Top constraint for next sprint:** CRM-to-ERP data sync
- **Human Orchestrator for next sprint:** IT Director (she owns both systems)

### Part 4: Install the One Design Change

| Question | Answer |
|---|---|
| What is the change? | Add the ops manager's pricing exception spreadsheet (47 exception rules) to the agent's knowledge base. |
| Who installs it? | Ops manager formats the spreadsheet; IT lead uploads it to the agent's vector store. |
| How will you know it's working? | Run the 3 failed edge cases through the updated agent. All three should produce estimates within 5% of the manually corrected price. |
| When is it installed by? | Before Sprint 2 kickoff on Monday. |

### Part 5: Update the Living Documents

- [x] **Hybrid Accountability Chart** — added permanent row: AI Agent owns rapid estimate generation; ops manager owns exception review.
- [x] **Signal Backlog** — re-ranked. CRM-to-ERP sync moved to #1.
- [x] **Sprint Outcome Record** — "Quote turnaround reduced from 4 hours to 20 minutes for standard specs (85% of volume). Edge cases identified and documented."

---

## Summary

The retrospective captures what the sprint taught you. The compounding measurement names the delta between where you started and where you are now. The constraint re-rank turns that learning into the next sprint's direction. The one design change installs the improvement before the next sprint begins. The living documents hold the institutional memory.

Every sprint that runs this instrument starts from a higher baseline than the last. That is compounding.

---

## Handoff

This instrument produces three outputs:

1. **The next constraint** — the top-ranked item from the re-ranked Signal Backlog. This becomes the input to the next sprint's Signal conversation (Instrument 04).
2. **The one design change** — installed before the next sprint begins.
3. **Updated living documents** — the Hybrid Accountability Chart, Signal Backlog, and Sprint Outcome Record, all current.

Hand the next constraint and the named Human Orchestrator to whoever facilitates Signal. The cycle begins again — from a higher baseline.
