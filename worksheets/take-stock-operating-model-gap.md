Compound · Diagnosis / Operating-Model Stock-Take

# Take Stock of the Operating-Model Gap

*Produces a short, system-by-system list of where people are still doing work the software should be doing — the raw candidate-constraints your first Sprint runs against.*

This worksheet turns "we should use AI somewhere" into a concrete, scoped list. You'll open your four core systems, name one gap in each, and record it where Sprint 1 can pick it up. The discipline is restraint: one item per system, observation only, no solving. No analyst or engineer required — you need login access to your own stack and twenty honest minutes. Do this *before* you start Sprint 1; the list is the input the Signal chapter prices.

---

## 1. Open your four core systems side by side

Forces the reader to look at the actual stack rather than describe it from memory, surfacing real friction points.

1. Pull up your four core systems on one screen, logged in and live — not from memory, not from a vendor slide: your CRM, your accounting or ERP system, your project tool, and your communications stack.
2. If a system has a "recent activity," "tasks," or "audit log" view, open it. You're looking at how the work actually moves, not how the tool was sold to you.
3. Add a row for any other system that real work runs through — a document store, a scheduling tool, a spreadsheet everyone secretly depends on.

> **Meridian example:** Elena's team opened HubSpot (CRM), NetSuite (accounting/ERP), and Asana (project tool) on the same screen. Looking at the live systems — not describing them — is what surfaced that the shop-floor handoff never touched a system at all.

---

## 2. For each system, name one place a person is doing work the system should be doing

Constrains the exercise to one item per system so the list stays actionable rather than becoming a complaint session.

1. For each system, write the single clearest spot where a person is hand-doing work the software could carry — re-keying data, manually drafting the same document, approving something only one person can approve, relaying information by phone or email that should move automatically.
2. Hold yourself to **one item per system.** If three things jump out, pick the one that costs the most hours or money. This is a stock-take, not a gripe list.
3. Write each entry as a concrete sentence naming who does the work and what it costs you, even roughly. "Elena drafts every custom quote by hand" beats "quoting is slow."

> **Meridian example:** Under CRM — "Elena manually drafts every custom quote; the bottleneck costs ~$558K/year in delayed closes." Under accounting — "Pricing exceptions sit on Elena's desktop; no one else can approve them." Under project tool — "Shop-floor handoff still happens by phone; no task is created when a job is won." One item each, named with a person and a cost.

---

## The table

| System | Where a person does work the system should be doing |
|---|---|
| CRM |  |
| Accounting / ERP |  |
| Project tool |  |
| Communications |  |
| Document store |  |
| Other |  |

*Meridian's completed version, for reference:*

| System | Where a person does work the system should be doing |
|---|---|
| CRM (HubSpot) | Elena manually drafts every custom quote; the bottleneck costs ~$558K/year in delayed closes |
| Accounting / ERP (NetSuite) | Pricing exceptions sit on Elena's desktop — no one else can approve them |
| Project tool (Asana) | Shop-floor handoff still happens by phone call; no automatic task is created when a job is won |
| Communications | — |
| Document store | — |
| Other | — |

---

## 3. Record the list in the Sprint Planning Canvas table

Externalizes the gap so it can be handed to Sprint 1 as a concrete candidate-constraint input, not a vague feeling.

1. Copy your entries into the candidate-constraints area of the Sprint Planning Canvas — the master worksheet you'll build up across the book and carry into your first Design Brief. If you don't have the Canvas started yet, keep this table; it *is* the first input.
2. Keep every entry, even the ones that feel small. You're not ranking yet; you're capturing.
3. Save it somewhere your team will actually find it again — the same place you keep the rest of your Sprint planning, not a one-off note.

> **Meridian example:** Elena's short list — the quoting bottleneck, the trapped pricing exceptions, the missing shop-floor handoff — became Sprint 1's candidate constraints and the first entries on Meridian's Sprint Planning Canvas.

---

## 4. Carry the list forward — do not solve yet

The chapter explicitly defers prioritization to the Signal chapter; the move here is observation, not intervention.

1. Resist the urge to fix, automate, or scope anything on the list right now. The job here was to *see* the gap, not close it.
2. Leave the list as-is until the Signal chapter, which is where you price your top item and pick the one constraint Sprint 1 will actually solve.
3. Note the date you took stock. When you return in a chapter or two, you'll want to confirm the picture hasn't already shifted.

> **Meridian example:** Meridian did not touch the quoting bottleneck the day they spotted it. The list sat as raw material; the Signal chapter is where the $558K/year quoting constraint got priced and chosen as Sprint 1's target.

---

## Before you call it captured

You're done when someone who wasn't in the room could pick up this sheet and hand it straight to Sprint 1 without asking you a single question. Check:

- Every core-system row has either one named gap or an honest dash — no blanks left ambiguous.
- Each entry names *who* does the work and, where you can, *what it costs* — not just "this is slow."
- You held to one item per system; the table reads as a stock-take, not a complaint log.
- The list is recorded where your Sprint planning lives, not stranded in a private note.
- You solved nothing. Pricing and picking happen later, in Signal — the list is observation only.
