# Source Instrument: Knowledge Map & Pipeline Audit

**Chapter:** 05 — Source
**Artifact produced:** One-page Knowledge Map (with pipeline status)
**Who's in the room:** Constraint owner from Signal + whoever touches the workflows, data, or decisions related to the constraint

---

## Purpose

Source maps the information environment around the one constraint Signal validated. The question is not "what data does our company have?" — that produces a library nobody uses. The question is "what does our organization know about *this specific problem*, and where does that knowledge live?" You leave with a single-page map that a designer can work from.

---

## Part 1: Set Up the Map

Start with a blank page and the constraint statement Signal produced. Draw a table with six columns:

| Source | Type | Owner | Status | Pipeline | Notes |
|---|---|---|---|---|---|
| *(name)* | Digital / Organic / Missing | *(person)* | Clean / Needs Work / Missing | Connected / Manual / Broken | *(one line)* |

The first four columns are the Knowledge Map. The fifth column (Pipeline) is the Data Pipeline Audit — run them together, not as separate exercises.

> **Pro Tip:** If your Source output doesn't fit on one page, it's not scoped to the constraint. You've drifted into a general data audit. Cut it back down.

---

## Part 2: Three Passes

Work the map in three passes. Each pass surfaces a different category of knowledge.

### Pass 1: Digital Sources

List every system, database, file, or tool that holds information relevant to the constraint.

**Questions to ask:**

1. Which systems does this workflow touch? (CRM, ERP, project management, shared drives, spreadsheets, email)
2. What data does each system hold that's relevant to the constraint?
3. Who maintains it?
4. When was the data last verified as accurate?

For each digital source, also answer the four Pipeline Audit questions:

1. Does this source connect to the other systems that touch the constraint, or does data move by manual export?
2. Is the data in a format a designed workflow could consume directly, or does it require translation?
3. Who owns the handoff — a person, a scheduled job, or nobody?
4. When was the connection last verified as working?

Mark each digital source's pipeline status:
- **Connected** — data flows automatically between systems
- **Manual** — data moves, but a person carries it (export, copy-paste, email)
- **Broken** — data doesn't move at all, or the connection is unreliable

> **Action Step:** Open the constraint statement from Signal. List every digital system that touches the constraint workflow. For each one, fill in all six columns. Don't filter — if it touches the constraint, it goes on the map.

### Pass 2: Organic Sources

List every person whose judgment, memory, or expertise is load-bearing for this constraint.

**Questions to ask:**

1. Who makes decisions about this workflow that aren't documented anywhere?
2. Who handles the exceptions? (The three things that happen every week that aren't in the manual.)
3. Who has the longest tenure touching this workflow? What do they know that a new hire wouldn't?
4. Who do people go to when the system doesn't have the answer?

For each person, describe what they know that isn't in any digital source. Be specific — not "she knows the quoting process" but "she knows the three pricing exceptions for legacy customers that override the rate card."

**The at-risk question:** For each organic source, ask: is this person a single point of failure? Could they leave in the next 12 months (retirement, role change, burnout, opportunity)? Mark at-risk sources explicitly.

> **Pro Tip:** The most valuable source of knowledge in most organizations is a person. And a person doesn't have an API. The Knowledge Map treats people as sources in the formal sense — named, located, described — because operationally they are. Data audits that skip organic sources produce libraries nobody uses.

> **Action Step:** Name every person whose judgment is load-bearing for the constraint. For each one, write specifically what they know that no system holds. Flag anyone who's a single point of failure.

### Pass 3: Missing Sources

Look at the map so far and ask: what would a designer need to know about this constraint that isn't represented in Pass 1 or Pass 2?

**Questions to ask:**

1. What question would someone ask about this workflow that we can't currently answer from our data?
2. What decision in this workflow is currently made by gut feel that should be made by data?
3. What does the customer experience that we have no visibility into?
4. What historical data would be useful but was never captured?

Mark each missing source with what type it *should* be (digital system, documented process, captured expertise) and what it would take to create it.

> **Action Step:** Review your map from Pass 1 and 2. Write down every gap — every question a designer would ask that your current sources can't answer. Add them to the map as Missing sources.

---

## Part 3: Classify Your Information

Not all knowledge is the same. Understanding the categories helps you (and eventually your AI systems) know how to use each source.

### Structured vs. Unstructured

| Structured | Unstructured |
|---|---|
| Database fields, tagged articles, CRM records, spreadsheets with defined columns | Emails, meeting transcripts, PDFs, Slack threads, "ask Sarah" |
| AI can use this immediately | AI needs processing before it's useful |

**The rule:** The more structured your information is, the more useful it is to an AI workflow. If a source is unstructured but valuable, flag it — that's a Design decision about whether to structure it.

### Durable vs. Ephemeral

| Durable | Ephemeral |
|---|---|
| Brand guidelines, pricing rules, process SOPs, regulatory requirements | This week's to-do list, meeting notes, brainstorm output, first-pass drafts |
| Earns a place in the organizational brain | Useful now, not worth indexing |

**The rule:** Only durable knowledge belongs on the Knowledge Map. If it won't matter in 90 days, it doesn't belong.

### How AI Will Use It

Think of three tiers of knowledge, each consumed differently by AI:

| Tier | What it is | AI behavior |
|---|---|---|
| **Standing context** | Core facts that are always true (brand rules, product definitions, org structure) | Loaded automatically — AI always has it |
| **Retrieved knowledge** | Documents, articles, detailed procedures | Retrieved on demand when relevant to a query |
| **Historical record** | Transcripts, meeting notes, archived decisions | Lowest priority — flagged as historical, never treated as current truth |

For each source on your map, consider which tier it falls into. This classification will directly inform Design — it determines how the AI system will access and weight each source.

> **Pro Tip:** An AI workflow that treats everything as equally current will confidently cite your deprecated pricing from 2019. The tiers exist to prevent this.

> **Action Step:** Review each source on your map. Mark whether it's structured or unstructured, and which AI tier it belongs to (standing context, retrieved, or historical). This takes five minutes and saves Design hours of rework.

---

## Part 4: The Completeness Test

Before you call Source done, run this test:

- [ ] **Designer test.** Could someone who wasn't in the room look at this map and know what they're designing against — what data exists, where it lives, what's missing, and what's at risk?
- [ ] **Constraint scope test.** Every row on the map connects to the constraint. If a row doesn't, cut it.
- [ ] **Pipeline test.** Every digital source has a pipeline status (Connected / Manual / Broken). No blanks.
- [ ] **At-risk test.** You explicitly asked: who on this list is a single point of failure? The answer is on the map.
- [ ] **Gap test.** The Missing column isn't empty. If you have zero missing sources, you haven't looked hard enough.
- [ ] **One-page test.** The map fits on one page. If it doesn't, you've drifted from the constraint.

> **Action Step:** Run the six-item completeness test. Fix any gaps. Then put the constraint statement from Signal at the top of the page and the Knowledge Map below it. That one page is what you hand to Design.

---

## Populated Example: Manufacturing Quoting Constraint

**Constraint (from Signal):** Design engineers spend 4-6 hours producing initial designs for every bid, including the 50%+ that won't convert, at an estimated cost of $180K/year in misallocated engineering time.

| Source | Type | Owner | Status | Pipeline | Notes |
|---|---|---|---|---|---|
| CRM (deal records, win/loss history) | Digital | Sales ops | Clean | Manual — CSV export to ops team weekly | Has win rates by segment but not linked to quoting system |
| ERP (materials pricing, job costing) | Digital | Finance | Needs Work | Connected to invoicing, not to quoting | Pricing data exists but requires manual lookup for quotes |
| Quoting spreadsheet (pricing exceptions) | Digital | Ops manager | Needs Work | Broken — lives on one person's desktop, no sync | 200+ exception rules, undocumented logic |
| Ops manager (exception handling, customer-specific terms) | Organic | Maria (ops) | — | — | Knows which exceptions apply to which customers. Only person who reconciles CRM + ERP for quotes. **AT RISK: single point of failure** |
| Senior engineer (design judgment for quick estimates) | Organic | Dave (engineering) | — | — | 30 years experience. Can estimate feasibility in minutes vs. hours. Knowledge undocumented. **AT RISK: 3 years to retirement** |
| Historical quote accuracy (which quick estimates matched final designs) | Missing | Nobody | Missing | — | Would validate whether a fast-estimate workflow produces acceptable accuracy. Data exists in CRM + ERP but has never been compared |
| Customer segment conversion rates by quote complexity | Missing | Nobody | Missing | — | Would allow routing: high-probability bids get full engineering, low-probability get rapid estimate. Requires joining CRM win/loss to engineering hours |

---

## Summary of Action Steps

1. **Set up the map** — blank table with six columns, constraint statement at top (Part 1)
2. **Pass 1: Digital sources** — every system that touches the constraint, with pipeline status (Part 2)
3. **Pass 2: Organic sources** — every person whose judgment is load-bearing, with at-risk flags (Part 2)
4. **Pass 3: Missing sources** — every gap a designer would need filled (Part 2)
5. **Classify your information** — structured/unstructured, durable/ephemeral, AI tier (Part 3)
6. **Run the completeness test** — six checks before you hand off to Design (Part 4)

---

## Pro Tips (collected)

1. If your Source output doesn't fit on one page, it's not scoped to the constraint. Cut it back down.
2. The most valuable source of knowledge in most organizations is a person — and a person doesn't have an API. The Knowledge Map treats people as sources because operationally they are.
3. An AI workflow that treats everything as equally current will confidently cite your deprecated pricing from 2019. Classify your knowledge by tier to prevent this.

---

## Handoff to Design

At the end of Source, you have one page: constraint statement at the top (from Signal), Knowledge Map below (from Source). That is the input Design needs. If someone can't look at that page and know what they're designing against, Source isn't done.

---

*This worksheet is the manual version of the Knowledge Map Builder and Data Pipeline Audit instruments in the Compound Skills Library. The method is the same. The tools run the same logic faster and more persistently.*
