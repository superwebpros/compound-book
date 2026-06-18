Compound · Deliver / Production Sensor

# Build and Maintain the Operational Log

*Stand up a four-column log on day one of deployment, run it for two weeks, and turn the busiest category into the signal for your next Sprint.*

The operational log captures, in real time, the gaps between what you designed and what production actually revealed. It is not a complaint box — it is a sensor. Every entry tells Design something about the next Sprint, and the category that fills up fastest is the next constraint. **Before you start, you need a deployed workflow and the named roles from the Hybrid Accountability Chart whose handoffs changed in this Sprint.**

---

## Create the four-column log template before deploy

The log must exist on day one of production — building it post-launch means the first gap goes unrecorded.

1. Make the table live where the team already works (the same shared doc or tool the workflow runs in), with exactly four columns: **Date**, **What happened**, **Category**, **What it signals**.
2. Lock the four categories at the top of the log so every entry uses the same words: **Unplanned intervention** (a human had to step in where the agent was supposed to handle it), **Data gap** (the workflow needed information that doesn't exist or wasn't connected), **Edge case** (an input the design didn't account for), **User confusion** (a person whose work changed didn't know what to do).
3. Confirm the log is open and reachable before go-live — not a thing someone promises to set up later that day.

> **Meridian:** Elena Ruiz's quoting workflow went live with the four-column log already open. Day 2 it caught the first entry — the agent hitting an Inconel 718 spec that wasn't in Customer Notes.xlsx — because the log existed before the first RFQ ran through the new path.

---

## Assign a single named owner

Accountability without a name means the log dies; one person owns it, no committee.

1. Write one person's name as the log owner — the same person reviews it every day for the first two weeks. Not "the team," not "whoever's around."
2. Make the owner the person closest to the review work, so logging is part of their existing flow rather than a separate chore.
3. State, in writing, what the owner does each day: read new entries, categorize them, and note any pattern forming.

> **Meridian:** Elena owned the log. She works the HubSpot review queue every day, so catching and recording each gap — the 40%-low Inconel estimate, the missing-drawing RFQ — happened inside the review she was already doing, not on top of it.

---

## Run daily check-ins for the first two weeks

The daily cadence surfaces patterns before they compound; week-two review timing aligns with the delivery test window.

1. Book a short daily check-in for fourteen days, on the calendar, non-negotiable — the owner reviews the day's entries and categorizes each one.
2. At each check-in, write the category in column three the same day the event happened, while the detail is still fresh, so column two stays specific.
3. Note any category that is starting to repeat — a forming pattern is the early read on where the next Sprint will aim.

> **Meridian:** Across the first two weeks the daily review captured the Day 2 edge case, the Day 4 user confusion (Ty submitting an RFQ with no drawing), and the Day 7 unplanned intervention (Dave catching the tolerance mismatch on a weldment quote) — each logged the day it happened, not reconstructed later.

---

## Categorize every entry (Unplanned intervention / Data gap / Edge case / User confusion)

Consistent categories make tallying possible; the category with the most entries identifies the next constraint.

1. Assign every entry exactly one of the four categories — no new categories, no blanks.
2. In "What it signals," write the design fix the entry points to (a guardrail, a required field, a new matching criterion), not just a description of what went wrong.
3. Log the positives too: a genuinely good outcome with no category (mark it "— (positive signal)") still tells Design what the new workflow is producing.

> **Meridian:** The Day 2 edge case signaled a guardrail ("no price estimate for unknown materials — flag as 'manual pricing required' and stop," added same day). The Day 10 entry — a customer praising same-day turnaround and submitting a second RFQ that afternoon — was logged as a positive signal: speed is producing repeat inbound, worth tracking.

---

## Tally by category at end of week two and surface the top category as the next Sprint signal

The log is a sensor, not a complaint box — it feeds Design for the next Sprint.

1. At the end of week two, count entries by category and write the totals down.
2. Name the category with the most entries — that category is the first thing to fix and the strongest signal for where the next Sprint should aim.
3. Hand the top category, with its underlying entries, to Design as a candidate constraint for the next Sprint.

> **Meridian:** At the two-week tally, whichever category had stacked up the most entries became the lead candidate for the next Sprint — the tolerance-class matching gap from Day 7, for instance, was already written down as a Design task for the next Sprint at the moment it surfaced.

---

## Before you call it done

Run this test at the end of week two:

- **The log existed on day one** — four columns, four locked categories, live where the team works, in place before the first real input ran through the workflow.
- **One named person owns it** — and reviewed it daily for two weeks, not a committee and not retroactively.
- **Every entry is categorized** with one of the four labels, and each "What it signals" names a design fix, not just a description.
- **The week-two tally is written down** and the top category has been handed to Design as the next Sprint's candidate constraint.

When all four are true, the log has done its job: it turned two weeks of production into a specific signal the next Sprint can run against.
