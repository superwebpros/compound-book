Source · Source / Systems Inventory

# Build and maintain the Systems Inventory

*Catalog every system your company has, what layer it sits in, and who owns it — once — so every Sprint's Knowledge Map starts from what you already know instead of a blank page.*

The Systems Inventory is a standing, company-wide catalog of your information environment. It is not scoped to one constraint and it is not a Source deliverable — it's a durable asset the knowledge manager maintains across every Sprint, the same way the Constraint Backlog is the standing list of constraints the business is working through. Each Sprint's Knowledge Map *pulls from* this inventory. **Before you start, gather whoever knows where data and documentation actually live: operations, finance, sales, and whoever administers your core systems.**

The columns:

| System | Layer | Owner | What it holds | Health | Reachable? |
|---|---|---|---|---|---|
|  | Record / Knowledge / Semantics |  |  | Clean / Needs Work / Stale |  Yes (API/MCP) / Manual / No |

---

## List every system, by layer

Makes the whole information environment visible in one place, sorted by the three layers Source works against.

1. List your **Systems of Record** — where authoritative data lives: CRM, ERP, accounting, project tools. Mark each Layer = Record.
2. List your **Systems of Knowledge** — where institutional know-how lives: SOP libraries, wikis, playbooks, training docs, shared drives. Mark each Layer = Knowledge.
3. List any **Systems of Semantics** — ontologies, knowledge graphs, an embeddings index, or an Open Knowledge Format bundle. Most companies have none yet; if that's you, write "none yet" and treat it as the gap to start closing.

> **Meridian:** Record — JobBOSS ERP, HubSpot CRM, QuickBooks. Knowledge — a thin SOP folder, the Customer Notes spreadsheet, and a lot still in people's heads. Semantics — none yet.

---

## Name an owner and what each system holds

Turns a list of logos into an accountable map: who maintains it and what it's actually good for.

1. For each system, name the single person accountable for it. "IT" or "the team" isn't an owner; a name is.
2. Write one line on what the system actually holds that the business relies on — not the brochure, the real use.
3. Note the obvious gaps: a System of Knowledge that's really just a stale drive, a System of Record nobody trusts.

> **Meridian:** JobBOSS — owner Finance — holds 800+ jobs of costing history, the best pricing source nobody queries. Customer Notes.xlsx — owner Elena — 147 pricing exceptions that exist nowhere else.

---

## Mark health and reachability

Tells every future Sprint, at a glance, what's usable today and what needs work first.

1. Mark each system's **Health**: Clean, Needs Work, or Stale.
2. Mark **Reachable?**: Yes (an API or MCP exists), Manual (a person moves the data), or No (isolated).
3. Flag anything that's a single point of failure or holds knowledge that's about to walk out the door.

> **Meridian:** JobBOSS — Clean, reachable by API. Customer Notes.xlsx — Needs Work, not reachable (isolated on one desktop, single point of failure).

---

## Keep it current — assign the cadence

An inventory that isn't maintained rots into the same mess it was meant to replace.

1. Assign the Systems Inventory to the **knowledge manager** as a standing responsibility, not a one-time project.
2. Set a review cadence — at least once per Sprint — to add systems that surfaced, retire ones that died, and update ownership and health.
3. After each Sprint, fold in what the Knowledge Map learned: new systems, new owners, new gaps.

> **Meridian:** After the quoting Sprint, the inventory gained two new entries (a quote-accuracy dataset and a segment-profitability view) and flagged the Customer Notes spreadsheet for migration off Elena's desktop.

---

## Before you call it done

- **Every system is on the list**, sorted into Record, Knowledge, or Semantics.
- **Every system has a named owner** — a person, not a department.
- **Health and reachability are marked** for each.
- **Single points of failure and at-risk knowledge are flagged.**
- **A knowledge manager owns it** with a review cadence on the calendar.

When all five are true, every future Sprint starts its Knowledge Map from what you already know — and you can see, in one place, where your company's knowledge actually lives and where it doesn't yet.
