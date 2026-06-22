Compound · Source / Knowledge Classification

# Classify each source on the map

*Takes your completed Knowledge Map and tags every source along two axes and one tier system, so Design knows exactly what's reachable today, what needs extraction work, and what stays human.*

This worksheet turns a list of sources into a classified map Design can act on. For each row you already captured, you'll mark structured vs. unstructured, durable vs. ephemeral, and an AI tier — then run a pre-handoff completeness check. The prerequisite is a built Knowledge Map (the "Build the Knowledge Map" worksheet output); this step is fast because the map is already in front of you. No engineer required — you're classifying what exists, not building anything. Run it while the map is still fresh.

---

## 1. Mark each source as structured or unstructured

Tells Design whether the source is directly queryable or requires an extraction pipeline, which affects cost, speed, and system architecture.

1. Go row by row through your Knowledge Map. For each source, mark **Structured** if it lives in defined fields — database tables, CRM records, tagged articles, spreadsheets with real columns. AI can use it directly, cheaply, and fast.
2. Mark **Unstructured** if it's prose or conversation — emails, meeting transcripts, PDFs, Slack threads, "ask Sarah." AI can reason against it, but it costs more in tokens, runs slower, and asks more of the system around it.
3. For any source that's both (a spreadsheet with a free-text notes column, say), classify it by where the *value you need* lives, and note the split.
4. Flag every source that is **unstructured AND valuable.** That flag is a Design decision waiting to be made: how much structure to add, and where. You are not adding it now.

> **Meridian example:** On Elena's map, JobBOSS ERP job-costing history and HubSpot CRM records were structured — queryable as-is. "Customer Notes.xlsx" was structured in form but held 147 free-text pricing rules, so the value was effectively unstructured. Elena's own quoting judgment and Dave's estimation method were fully unstructured and high-value — both flagged for Design.

---

## 2. Mark each source as durable or ephemeral

Filters out knowledge that will not matter in 90 days; only durable knowledge belongs on the map and informs agent design.

1. For each source, ask: will this still matter in 90 days? Mark **Durable** if it's standing knowledge — brand guidelines, pricing rules, process SOPs, regulatory requirements, customer history.
2. Mark **Ephemeral** if it expires — this week's to-do list, meeting notes, brainstorm output, first-pass drafts, in-the-moment status.
3. Cut every ephemeral row from the Knowledge Map. If it won't matter in 90 days, it doesn't belong on the map and shouldn't inform agent design.
4. If a source feels half-and-half, split it: keep the durable part (the standing rule) on the map, drop the ephemeral part (today's instance of it).

> **Meridian example:** Elena's 147 customer-specific pricing rules and Dave's 31 years of fabrication estimation logic were durable — they'd matter long past 90 days, so they stayed on the map. "This week's shop-floor capacity" was ephemeral: real, but it expires by next week, so it stayed off the map and out of agent design.

---

## 3. Assign each source an AI tier (Tier 1 / Tier 2 / Tier 3 / Not AI-tier)

Tells Design what is reachable today, what requires extraction work before it is usable, and what must remain human-executed — preventing agents from mixing authoritative and stale sources.

1. For each durable source, assign one tier using the table below. The tier tells Design how the AI system will access and weight that source.
2. Write the tier directly on the map next to each source. No blanks — every durable row gets a tier.
3. Watch for the trap: a single workflow that mixes Tier 1 truth with a Tier 3 archive will confidently cite deprecated information. The tiers exist to keep authoritative and stale sources from blending.

| Tier | What AI can do | Example |
|---|---|---|
| **Tier 1** | Use it directly. Structured and API-accessible; queried in real time. | CRM records, ERP job costing, rate card |
| **Tier 2** | Process it with an extraction pipeline. Unstructured but capturable. | PDFs, meeting transcripts, documented SOPs |
| **Tier 3** | Nothing yet. Human judgment required; not AI-accessible today. | Creative judgment, undocumented relationship context |
| **Not AI-tier** | Leave it human. Ephemeral or judgment-bound work decided in the moment. | This week's shop-floor capacity, in-the-moment calls |

### The classification table

Fill one row per source carried over from your Knowledge Map:

| Source | Structured / Unstructured | Durable / Ephemeral | AI Tier |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

*Meridian's completed version, for reference:*

| Source | Structured / Unstructured | Durable / Ephemeral | AI Tier |
|---|---|---|---|
| JobBOSS ERP — job costing history (800+ jobs) | Structured | Durable | Tier 1 |
| HubSpot CRM — win/loss records | Structured | Durable | Tier 1 |
| "Customer Notes.xlsx" — 147 pricing rules | Unstructured (free text) | Durable | Tier 2 |
| Elena — quoting judgment, source reconciliation | Unstructured | Durable | Tier 3 |
| Dave — fabrication estimation method | Unstructured | Durable | Tier 3 |
| This week's shop-floor capacity | Unstructured | Ephemeral | Not AI-tier |

> **Meridian example:** Tagging Elena's map this way is what told Design the truth: the ERP and CRM were reachable today (Tier 1), the pricing spreadsheet needed an extraction pipeline before any agent could trust it (Tier 2), and Elena's and Dave's judgment had to stay human or be captured by interview first (Tier 3). Without the tiers, a quoting agent could have cited the 2019 pricing in that spreadsheet as if it were current.

---

## 4. Run the eight-item completeness test

Acts as a pre-handoff gate ensuring the map covers layers, TML types, pipeline statuses, at-risk flags, gaps, and constraint scope before it goes to Design.

1. Work the eight checks below against your now-classified map. Each must pass — a single fail means the map isn't ready for Design.
2. For any check that fails, fix it on the map now (add the missing classification, cut the off-constraint row, name the at-risk person) rather than passing the gap downstream.
3. When all eight pass, the map is the handoff artifact. Design inherits it without coming back to ask you what anything means.

- **Architect test.** Could someone who wasn't in the room read this map and know what they're designing against — what data exists, where it lives, what's missing, what's at risk?
- **Constraint scope test.** Every row connects to the constraint. If a row doesn't, cut it.
- **Layer test.** Every row is classified by information layer: System of Record, System of Knowledge, or System of Semantics. All-Record means you did a data audit, not Source.
- **TML test.** Every row is classified by TML type: Task, Management, or Leadership. This tells Design how to handle capture and transfer.
- **Pipeline test.** Every digital source has a pipeline status — Connected, Manual, or Isolated. No blanks.
- **At-risk test.** You explicitly asked who is a single point of failure, and the answer is on the map.
- **Gap test.** The Missing column isn't empty. Zero missing sources means you didn't look hard enough.
- **One-page test.** The map fits on one page. If it doesn't, you've drifted from the constraint.

> **Meridian example:** Elena's map passed the at-risk test by naming two single points of failure — Elena herself and Dave, four years from retirement — and passed the gap test because the Missing column held two rows (historical quote-to-actual accuracy and segment profitability) that didn't exist yet but were exactly what Design needed to judge whether an agent-assisted quoting workflow was viable.

---

## Before you call it done

You're done when someone who wasn't in the room could take this classified map straight into Design without asking you a single question. Check:

- Every source carries all three tags: structured/unstructured, durable/ephemeral, and an AI tier — no blanks.
- Every ephemeral source has been cut from the map; only durable knowledge remains.
- No row mixes a Tier 1 source and a Tier 3 archive into the same authoritative answer.
- Each unstructured-and-valuable source is flagged as a Design decision, not silently dropped.
- All eight completeness checks pass — including a named at-risk person and a non-empty Missing column.
