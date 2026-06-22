Source · Source / Knowledge Map

# Build the Knowledge Map in three passes

*Inventory everything the one validated constraint touches — every system, every person, every gap — on a single page, so Design works from reality instead of assumptions.*

The Knowledge Map is the deliverable of Source: a six-column table, one row per source, scoped to the one constraint Signal validated. You build it in three passes — digital systems, then people, then gaps — pulling what you can from your standing **Systems Inventory** and adding what only lives in people's heads. **Before you start, you need the Constraint Statement from Signal and access to your Systems Inventory (if you've built one). If you haven't, this is also where you start one.**

The six columns:

| Source | Type | Owner | Status | Pipeline | Notes |
|---|---|---|---|---|---|
|  | Digital / Organic / Missing |  | Clean / Needs Work / Missing | Connected / Manual / Isolated |  |

---

## Start from the Constraint Statement and pull from the Systems Inventory

Scopes the entire map to one constraint so no row is extraneous, and saves you from starting blank.

1. Write the Constraint Statement from Signal at the top of the page. Every row you add has to connect to it.
2. Open your Systems Inventory and pull the systems that sit in the path of this constraint — they're already classified by layer and owner. Leave the rest of the inventory alone; this map is scoped to one constraint, not the whole company.
3. Draw the six-column table. You'll fill it across the three passes below.

> **Meridian:** The constraint was the quoting bottleneck. From the Systems Inventory, Elena's team pulled HubSpot, JobBOSS, and the Customer Notes spreadsheet — the systems in the quoting path — and left HR, marketing, and the accounting close off the map entirely.

---

## Pass 1 — Digital sources

Surfaces the named, login-accessible systems first; they're the easiest to enumerate and they set the pipeline baseline.

1. List every digital source that touches the constraint: CRM records, process logs, shared drives, inboxes, spreadsheets. Mark each **Digital**.
2. For each, name the owner and mark its **Status**: Clean, Needs Work, or Missing.
3. Run the four Pipeline Audit questions and mark each source **Connected**, **Manual**, or **Isolated**: Does it connect to the other systems, or does data move by hand? Can a workflow read it directly? Who owns the handoff? When was the data last verified?

> **Meridian:** HubSpot — Manual. JobBOSS — Manual (Elena queries it from memory, not systematically). Customer Notes.xlsx — Isolated, on Elena's desktop, no backup.

---

## Pass 2 — Organic sources (people)

Captures the institutional knowledge no system holds, and flags single points of failure before the knowledge walks out the door.

1. List every person whose judgment the constraint workflow depends on — if they vanished tomorrow, the work would stop or degrade. Mark each **Organic**.
2. Name specifically what each one knows that isn't documented. Not "she knows quoting" but "she holds the three legacy-customer pricing exceptions that override the rate card."
3. Flag anyone who is a single point of failure with **AT RISK** in the Notes column — especially anyone facing a planned exit, retirement, or role change.

> **Meridian:** Elena — Organic, AT RISK: the only person who can reconcile all the sources. Dave — Organic, AT RISK: 31 years of estimation judgment, undocumented, four years to retirement.

---

## Pass 3 — Missing sources

Converts invisible Sprint failure modes into explicit design decisions by naming what should exist but doesn't.

1. Ask what a designer would need that isn't in Pass 1 or Pass 2: questions your current sources can't answer, decisions made by gut that should be made by data.
2. Add each as a **Missing** row. Note what type it *should* be (digital system, documented process, captured expertise) and what it would take to create.
3. Watch for Management and Leadership knowledge loss — decisions and market intelligence that lived only in someone's head. Task-knowledge gaps are usually just documentation; Management and Leadership gaps are the expensive ones.

> **Meridian:** Historical quote-to-actual accuracy — Missing (the data exists in two places but has never been compared). Customer segment profitability — Missing (would require joining CRM win/loss to ERP job costing).

---

## Apply the one-page test

Forces constraint-scope discipline: if it doesn't fit on a page, rows that don't belong have crept in.

1. Read every row and confirm it connects to the constraint. If it doesn't, cut it.
2. If the map runs longer than one page, you've drifted into a general data audit. Tighten back to the constraint.
3. Put the Constraint Statement at the top and the Knowledge Map below it. That one page is what you hand to Design.

> **Meridian:** Seven rows — three digital, two organic, two missing — on one page. Anyone could read it and see exactly what feeds the quoting constraint and where it's at risk.

---

## Before you call it done

- **Every row connects to the constraint.** No general-audit rows.
- **Every digital source has a pipeline status** — Connected, Manual, or Isolated. No blanks.
- **At-risk people are flagged** — you explicitly asked who's a single point of failure, and the answer is on the map.
- **The Missing column isn't empty.** Zero missing sources means you didn't look hard enough.
- **It fits on one page**, with the Constraint Statement on top.

When all five are true, you've got the second half of the Design input: constraint plus map, one page. (Then classify each source — see the Classify Sources worksheet — before you hand off.)
