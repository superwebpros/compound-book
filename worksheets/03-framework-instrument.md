# Framework Instrument: Sprint Planning Canvas

**Chapter:** 03 — The Framework
**Artifact produced:** One-page Sprint Planning Canvas
**Who's in the room:** Leadership sponsor + Human Orchestrator + the 2-3 people closest to the constraint

---

## Purpose

The Framework chapter gives you the vocabulary. This worksheet gives you the canvas. Before you dive into Signal, Source, Design, Build, Deliver, and Compound as detailed chapters, you sketch the sprint in one pass — naming the constraint, mapping the stages, identifying the team, and setting the rhythm. The canvas is intentionally incomplete. You will refine every section as you work through the chapters. The point is to start with a compass, not a blank page.

---

## Part 1: Name the Sprint

Every sprint starts with a constraint. If you have already run Signal, write the constraint statement here. If you haven't, write your best guess. You will sharpen it in Chapter 4.

### Questions:

1. **What constraint are you solving?** (One sentence. If you haven't done Signal yet, write your best guess — you'll refine it.)

   ```
   _____________________________________________________________
   ```

2. **Who is the leadership sponsor?** (The person who owns the outcome. Not the person doing the work — the person accountable for the result.)

   ```
   _____________________________________________________________
   ```

3. **What quarter does this sprint land in?**

   ```
   _____________________________________________________________
   ```

> **Pro Tip:** If you can't name the constraint in one sentence, you're not ready for a sprint. Go to Signal (Chapter 4) first. A sprint without a named constraint is a project — and projects drift.

> **Action Step:** Write the constraint, sponsor, and quarter. Read the constraint sentence out loud. If it takes more than one breath, it's too long.

---

## Part 2: Map the Six Stages

Each sprint passes through six stages. You don't need perfect answers now — you need honest first guesses. Fill in as much as you can. Leave blanks where you're uncertain.

| Stage | Key Question | Your Answer |
|---|---|---|
| **Signal** | What is the ONE constraint, and what does it cost? | |
| **Source** | What does the org know about this problem, and where does that knowledge live? | |
| **Design** | What does the human + AI workflow look like? Who owns what? | |
| **Build** | What gets built — off-the-shelf, low-code, or hand-built? | |
| **Deliver** | How do you know it worked? What number moved? | |
| **Compound** | What did you learn? What changes for next sprint? | |

> **Pro Tip:** You don't need to fill this in perfectly now. This is your compass, not your GPS. Each chapter will walk you through the detailed work.

> **Action Step:** Fill in one answer per stage. Write whatever you know. A wrong first guess is better than a blank row — blanks stay blank, guesses get corrected.

---

## Part 3: Identify Your Team

A sprint is not a committee. It is a small team with direct knowledge of the constraint and the ability to build a solution.

### Questions:

1. **Who is the Human Orchestrator?** (The person who will run this sprint day-to-day. Not the sponsor — the operator.)

   ```
   _____________________________________________________________
   ```

2. **Who are the 2-3 people closest to the constraint workflow?** (They'll be in the room for Signal and Source. Pick the people who touch the broken process, not the people who manage it from a distance.)

   ```
   _____________________________________________________________
   _____________________________________________________________
   _____________________________________________________________
   ```

3. **Do you have a technical resource?** (Internal or external — someone who can build what Design specifies.)

   ```
   _____________________________________________________________
   ```

> **Pro Tip:** You don't need an AI team. You need the people who know the workflow plus one person who can build. That's usually 3-5 people.

> **Action Step:** Write the names. If any slot is blank, that's your first task before the sprint starts — fill it.

---

## Part 4: Set the Rhythm

A sprint is not an open-ended initiative. It lands in a quarter. It has a start date, a review date, and a defined audience for the review. This is where the Sprint meets the Rhythm — one sprint per quarter, outcome reviewed before the next sprint begins.

### Questions:

1. **When does this sprint start?**

   ```
   _____________________________________________________________
   ```

2. **What's the quarterly operating session where you'll review the outcome?**

   ```
   _____________________________________________________________
   ```

3. **Who will be in that review?**

   ```
   _____________________________________________________________
   ```

> **Pro Tip:** If the review isn't on the calendar, the sprint has no deadline. And a sprint with no deadline becomes a project that drifts into next quarter. Book the review before you start Signal.

> **Action Step:** Put the review date on the calendar. Name the attendees. Send the invite. The sprint is real when the review is scheduled.

---

## Part 5: Pre-Flight Checklist

Before starting Signal, confirm each of these. If any box is unchecked, resolve it first.

- [ ] Leadership team agrees this constraint is worth a sprint
- [ ] One person is named as Human Orchestrator
- [ ] The team has access to the data and people they'll need for Source
- [ ] There is a realistic expectation that a build can happen this quarter
- [ ] The quarterly review is on the calendar

> **Action Step:** Walk the checklist with your leadership sponsor. Every unchecked box is a blocker. Resolve blockers before moving to Signal — not during.

---

## Populated Example: Marketing Agency Client Onboarding

A 40-person marketing agency running on EOS. The leadership team has identified client onboarding as the constraint slowing growth.

### Part 1: Name the Sprint

**Constraint:** Client onboarding takes 3 weeks and requires 14 manual handoff steps between sales, strategy, and production, costing an estimated $8,200 per client in unbilled time.

**Leadership sponsor:** CEO / Integrator

**Quarter:** Q3 2026

### Part 2: Map the Six Stages

| Stage | Key Question | Answer |
|---|---|---|
| **Signal** | What is the ONE constraint, and what does it cost? | 14 manual handoff steps across 3 departments. $8,200/client in unbilled time. 40 new clients/year = ~$328K annual drag. |
| **Source** | What does the org know about this problem, and where does that knowledge live? | Ops lead has mapped the current workflow on a whiteboard. Sales tracks handoff delays in HubSpot. Strategy team has informal checklists in Google Docs. No single system of record. |
| **Design** | What does the human + AI workflow look like? Who owns what? | AI handles intake form parsing, brief generation, and task creation across PM tool. Humans own strategy decisions and client relationship. Orchestrator reviews AI output before it routes. |
| **Build** | What gets built — off-the-shelf, low-code, or hand-built? | Low-code: HubSpot-to-Asana automation via Make.com, plus a Claude-powered brief generator. One custom integration for the PM handoff. |
| **Deliver** | How do you know it worked? What number moved? | Onboarding time drops from 3 weeks to under 1 week. Handoff steps drop from 14 to 4. Unbilled time per client drops below $2,000. |
| **Compound** | What did you learn? What changes for next sprint? | Review whether the onboarding pattern applies to upsell workflows. Capture the brief-generation prompt as a reusable skill. Feed learnings into Q4 sprint planning. |

### Part 3: Identify Your Team

**Human Orchestrator:** Head of Operations

**People closest to the constraint:** Ops lead (owns current handoff process), senior strategist (receives briefs from sales), production manager (downstream of the bottleneck)

**Technical resource:** External Compound partner (builds the integrations and AI workflows)

### Part 4: Set the Rhythm

**Sprint starts:** July 7, 2026

**Quarterly review:** September 25, 2026 (Q3 Quarterly operating session)

**Review attendees:** CEO, Integrator, Head of Operations, department leads

### Part 5: Pre-Flight Checklist

- [x] Leadership team agrees this constraint is worth a sprint
- [x] One person is named as Human Orchestrator (Head of Operations)
- [x] The team has access to the data and people they'll need for Source
- [x] There is a realistic expectation that a build can happen this quarter
- [x] The quarterly review is on the calendar

---

## Summary of Action Steps

1. **Name the sprint** — Write the constraint in one sentence, name the sponsor, pick the quarter (Part 1)
2. **Map the six stages** — One answer per stage, first guesses, no blanks (Part 2)
3. **Identify the team** — Human Orchestrator, 2-3 workflow people, one technical resource (Part 3)
4. **Set the rhythm** — Start date, review date, review attendees, calendar invite sent (Part 4)
5. **Run the pre-flight checklist** — Five checks, all boxes marked before Signal begins (Part 5)

---

## Pro Tips (collected)

1. If you can't name the constraint in one sentence, you're not ready for a sprint. Go to Signal first. A sprint without a named constraint is a project — and projects drift.
2. You don't need to fill the six-stage table in perfectly. This is your compass, not your GPS. Each chapter walks you through the detailed work.
3. You don't need an AI team. You need the people who know the workflow plus one person who can build. That's usually 3-5 people.
4. If the review isn't on the calendar, the sprint has no deadline. Book the review before you start Signal.

---

## Handoff to Signal

The Sprint Planning Canvas is the artifact you bring to Signal (Chapter 4). Signal will sharpen the constraint — tracing symptoms to root cause, quantifying the cost, and locking the one-page Constraint Statement that the rest of the sprint runs against.

If your canvas has blank rows in the six-stage table, that's fine. Signal, Source, and Design will fill them. If your canvas has no constraint sentence at all, start with Signal before you do anything else.

---

*This worksheet is the manual version of the Sprint Planner instrument in the Compound Skills Library. The method is the same. The tool is a faster, more persistent version of the same conversation.*
