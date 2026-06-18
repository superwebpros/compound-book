Compound · Design / Work Design

# Work Deconstruction

Classify every task in the constraint workflow using the TML framework — Task, Management, Leadership — so each one becomes a row in the Hybrid Accountability Chart with its own supervisor and autonomy level.

Work Deconstruction applies the TML framework from Source to the work itself. Where Source used TML to categorize what the organization knows, here you use it to categorize what the work *requires* — task by task, with its real inputs and outputs named. The output is a classified task table plus the Hybrid Accountability Chart entries that Build inherits. Done honestly, it usually shows that a role assumed to be judgment-heavy is mostly retrieval and assembly.

**Before you start:** Pick the one role (or one workflow) that sits on your constraint from Signal. Have the previous chapter's Source work in front of you — you already know where each task's data lives.

Fill in the classified task table, one row per task:

| Task | Category | Source / Input | Output / Destination | Rationale |
|---|---|---|---|---|
| _(the actual weekly task)_ | _(Task / Management / Leadership)_ | _(system, person, or document the data comes from)_ | _(where the result goes next)_ | _(why it sorts here)_ |
|  |  |  |  |  |
|  |  |  |  |  |

Then run the five steps below to build and pressure-test it.

---

## Pull the actual accountability list

Job descriptions are sanitized; the real weekly task list is what gets classified — you can't sort what you haven't named.

1. List every accountability the role owns from the existing Accountability Chart, not the job description. The job description will be cleaner than reality — ignore it.
2. Add anything the person actually touches every week that the chart doesn't capture. The target is the real list of work, not the tidy version.
3. Break compound items into single tasks ("handle quotes" becomes receive RFQ, pull history, look up pricing, assemble draft, review, deliver). One row per task you could hand off on its own.

> **Jesse:** Before posting a listing for a second project coordinator at $24K, we ran the role through Work Deconstruction. We listed every accountability she owned on the existing Accountability Chart, not her job description. The job description was cleaner than reality. Her actual list was the work she touched every week.

## Document source inputs and outputs for each task

Connecting each task to where its data comes from and where the result goes makes the information flow from Source concrete at the task level.

1. For each task, name the **source input** — the specific system, person, or document the data comes from (e.g., "HubSpot CRM," "Customer Notes.xlsx," "Dave's labor estimate"). If you did the Source work properly, you already know these.
2. Name the **output / destination** — where the result goes next, and to whom (e.g., "draft PDF to Elena's review queue," "approved quote to Ty for delivery").
3. Where a task feeds an agent, note which agent (e.g., "→ Quote Pricing Agent"). The chain of inputs and outputs is the information flow from the previous chapter, written at task level.

> **Meridian example.** For the quoting constraint, "Look up material pricing" drew its input from JobBOSS ERP (materials database, supplier pricing) and sent its output — material costs, lead times, out-of-stock flags — to the Quote Pricing Agent. Every task in the deconstruction names its system in and its destination out.

## Apply the TML sorting question to each task

A single binary question — would the output need human review every time, or only on exceptions? — assigns every task to Task, Management, or Leadership without ambiguity.

1. For each task ask the one sorting question: *"If I gave an agent this task, would the output need human review every time, or only when something goes wrong?"*
2. Sort by the answer. Only on exceptions → **Task** (Fully Automatable), including pure workflow automation where data routes between systems with no agent in the middle. Every output needs review → **Management** (AI-Assisted). The answer depends on who the client is, what happened last week, or a judgment call with no clear rule → **Leadership** (Human Judgment Required).
3. When unsure, start a task at **Management (AI-Assisted)**. Autonomy is earned over multiple Sprints once the agent proves itself, not assigned up front.

> **Meridian example.** "Cross-reference Customer Notes.xlsx for pricing exceptions" sorted to Management (AI-Assisted): 112 customer-specific rules, some simple discounts and others with context the spreadsheet doesn't fully capture, so Elena reviews every output until the exception set is validated. "Review and approve quote" sorted to Leadership — her judgment catches strategic-account and margin calls the rules miss.

## Tally the three buckets and challenge the Leadership pile

If more than half land in Leadership, each item must be re-examined — genuine judgment stays, but undocumented rules that look like judgment get reclassified.

1. Count the tasks in each bucket: Task, Management, Leadership. Write the three numbers down.
2. If **more than half land in Leadership (Human Judgment Required)**, challenge each one: is this genuinely judgment, or is it judgment only because nobody has written down the rules?
3. Reclassify anything that turns out to be a documentable rule down into Management or Task. Genuine judgment — depends on knowing the client, the history, reading a room — stays in Leadership.

> **Meridian example.** The role that felt like "Elena's judgment" tallied 3 Task, 2 Management, 2 Leadership. Roughly 65% of the work was data retrieval and document assembly — it required her *access*, not her judgment. The remaining 35% stayed with her because the deconstruction showed the judgment genuinely couldn't be removed.

## Map each classified task to a Hybrid Accountability Chart entry

Deconstruction is thinking; the chart entry — function, agent team, supervisor, autonomy level — is what makes that thinking durable and actionable for Build.

1. Roll the classified tasks up into functions and create one Hybrid Accountability Chart entry per function: **Role / Function, Agent Team, Human Supervisor, Level**. (If you run EOS, this extends your existing Accountability Chart — agent teams and their supervisors alongside your people.)
2. Give every row a named human supervisor. Task-level workflow automation may have no agent team, but it still has an accountable human. No anonymous rows.
3. Set every agent team's starting Level to AI-Assisted (the human reviews every output and holds final authority). Moving toward Automated is a promotion the agent earns over Sprints, not a default.

> **Meridian example.** The deconstruction produced five chart entries — including "Material and labor pricing assembly → Quote Pricing Agent → Elena Ruiz (VP Ops) + Dave Kowalski → AI-Assisted" and "Quote delivery and customer follow-up → None → Ty Banfield (Sales Lead) → N/A." Every row has a name, every agent team has a supervisor, and all agent outputs start AI-Assisted: Elena reviews every quote.

---

## Before you call it done

Hand the deconstruction to someone who didn't run it — or to the person doing Build. They should be able to see what each task is, where its data comes from, where its result goes, why it sorts where it does, and who supervises it, without coming back to ask. Check:

- [ ] The task list came from the **actual accountability list**, not the job description, broken into single hand-off-able tasks.
- [ ] Every task names a **source input** and an **output / destination** — system, person, or document, in and out.
- [ ] Every task carries a **TML category** answered by the sorting question — no unclassified items.
- [ ] The three buckets are **tallied**, and if Leadership held more than half, each item was challenged and reclassified or kept on purpose.
- [ ] Every classified task rolls up into a **Hybrid Accountability Chart entry** with a named supervisor and a starting Level (agent teams start AI-Assisted).

If any box is blank, the deconstruction isn't ready for Build — finish it here, not in Build.
