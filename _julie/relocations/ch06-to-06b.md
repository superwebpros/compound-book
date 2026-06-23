# ch06 → 06b Relocations

Sections cut from `chapters/06-designing-the-system.qmd` during the June 2026 chapter-split pass.
Place these into `chapters/06b-designing-the-work.qmd` in the upcoming 06b structure pass.
Each section is preserved verbatim (minus `jf-note:` markers, which were removed chapter-wide).

---

## 1. "Every agent gets a mini-spec" (full section)

**Note:** the `ch06-agent-mini-spec` excalidraw shortcode relocates with this section.

This section belongs in 06b alongside the Design Brief, where agent mini-specs live as part of the Design Brief's specification work. The brief intro sentence referencing it in ch6's moves block should simply say the mini-spec lives in the next chapter.

---

## Every agent gets a *mini-spec*

The chart names the agent team. The mini-spec names what the agent actually is. Every row in the Hybrid Accountability Chart that has an agent team gets a mini-spec, and the mini-spec is what you hand to Build.

A mini-spec is a one-page spec that answers six questions defining the agent, plus a seventh that locks the tool category before Build inherits it. Think of it as the agent's standing operating rules — what it does, what it reads, what it remembers, and what it escalates.

<!-- moves:agent-mini-spec -->
### How to write the *Agent Mini-Spec*

1. **Write the system prompt** — Three-to-five sentences that tell the agent who it is, what it's accountable for, and what it does not decide — the standing operating rules it reads before every task.
2. **List the tools** — Names every API (application programming interface — how systems talk to each other), integration, or system the agent can call; unnamed tools are tools Build has to guess at.
3. **Identify the context sources** — Maps the Knowledge Map rows that feed this agent; if a source isn't on the map, it isn't a source — this prevents scope creep at the data layer.
4. **Set the memory rules** — Explicitly stating what the agent tracks across runs (or that it tracks nothing) prevents the agent from carrying stale state into new tasks.
5. **Define judgment and escalation rules** — Specifies exactly when the agent escalates, what it refuses, and what triggers a handoff to the Human Orchestrator — the governance answers from the HAC land here, agent by agent.
6. **Rate the oversight load (Low / Medium / High)** — Keeps the Orchestrator's span of control visible; no Orchestrator should carry more than three high-oversight agents at once, so this field is the span-of-control check before the spec leaves Design.
7. **Select the tool category (off-the-shelf / low-code / hand-built)** — Locking the category in Design prevents Build from making an architecture decision based on vendor relationships or recency rather than the workflow's actual requirements.
<!-- /moves:agent-mini-spec -->

Here's what filling in each field actually requires.

**Write the system prompt.** Three to five sentences: who the agent is, what it's accountable for producing, and what it explicitly does not decide. The last sentence is load-bearing — it's the hard boundary. Without it, the agent will drift into decisions it was never designed for. *Meridian:* "You are the Quote Research Agent for Meridian Manufacturing. Your job is to retrieve the customer's purchase history and match their RFQ against the closest historical jobs. You produce a summary for the quoting team to use; you do not set prices, apply exceptions, or contact customers."

**List the tools.** Name every API or system the agent can call — by name, not by category. "CRM access" is not a tool spec; "HubSpot CRM read access" is. Build uses this list to wire the integrations; anything unnamed is a gap Build has to interpret. *Meridian:* HubSpot CRM read access; JobBOSS ERP read access.

**Identify the context sources.** Map the Knowledge Map rows that feed this agent. If a source isn't on the Knowledge Map from Source, it isn't an authorized context source — this is where scope creep gets caught before it reaches Build. *Meridian:* HubSpot deal history; JobBOSS job costing records.

**Set the memory rules.** State explicitly what the agent tracks across runs, and what it doesn't. "No memory across runs" is a complete answer. So is "remembers the last five quotes for this customer." What's not acceptable is leaving it blank — an unspecified memory model means Build makes a default choice you may not want. *Meridian:* No memory across runs. Each RFQ is treated fresh.

**Define judgment and escalation rules.** State exactly when the agent escalates, what it refuses to do, and what triggers a handoff to the Human Orchestrator. This is where the governance answers from the HAC land at the agent level — not company-wide policy, but the specific conditions this agent responds to. *Meridian:* if no historical job matches within 20% of the RFQ specs, flag for Elena; do not estimate — flag and hold.

**Rate the oversight load.** Low, Medium, or High — based on how much review the Orchestrator will need to do per run. This field is the span-of-control check: no Orchestrator should carry more than three high-oversight agents at once. Julie Bedard and colleagues at BCG, writing in *Harvard Business Review*, found that productivity inverts after three concurrent AI agents per supervisor. Manage agent oversight the way operations leaders already manage spans of control for human reports. Count the oversight loads before the specs leave Design. *Meridian:* Medium — Elena reviews the research summary before the Pricing Agent runs.

**Select the tool category.** Lock the category here — off-the-shelf, low-code, or hand-built — so Build inherits a decision, not an open question. The full routing logic for picking the category is in the "Pick the tool category" section below. *Meridian:* low-code (the Quote Research Agent pulls from two read-only APIs and writes to a staging table — standard moves, no custom infrastructure).

### Meridian's Quote Research Agent mini-spec

{{< excalidraw ch06-agent-mini-spec "Meridian's Quote Research Agent mini-spec: system prompt, tools, context sources, memory, escalation rules, and oversight load." >}}

| Field | Quote Research Agent |
|---|---|
| **System prompt** | You are the Quote Research Agent for Meridian Manufacturing. Your job is to retrieve the customer's purchase history and match their RFQ against the closest historical jobs. You produce a summary for the quoting team to use; you do not set prices, apply exceptions, or contact customers. |
| **Tools** | HubSpot CRM read access; JobBOSS ERP read access |
| **Context sources** | HubSpot deal history; JobBOSS job costing records |
| **Memory rules** | No memory across runs. Each RFQ is treated fresh. |
| **Judgment and escalation rules** | If no historical job matches within 20% of the RFQ specs, flag for Elena. Do not estimate; flag and hold. |
| **Oversight load** | Medium — Elena reviews the research summary before the Pricing Agent runs. |

The mini-spec template gets its full walkthrough in the next chapter inside the Design Brief. What matters here is naming the discipline: every agent on the chart has a spec, every spec answers six questions, and no agent goes to Build without one.

---

## 2. "Pick the tool category before you pick the tool" (full section)

**Note:** the `ch06-tool-category-decision` excalidraw shortcode relocates with this section.

This section belongs in 06b alongside the Design Brief and mini-specs. Tool category selection is part of specifying each agent before Build, which is 06b territory.

---

## Pick the *tool category* before you pick the tool

The mini-spec names what each agent is. Tool category selection names the kind of environment each agent runs on.

There are three categories. Most Compound Sprints land in one of them; a few combine two. The categories are stable; the specific products rotate every few quarters, so check current options when you build.

{{< excalidraw ch06-tool-category-decision "Pick the tool category: three routing questions lead to off-the-shelf, low-code, or hand-built." >}}

**Off-the-shelf tool.** Existing software that maps cleanly to the designed workflow with light configuration. The work is selection, configuration, and integration — not building from scratch. Use this category when a mature product already does what the design requires, with no custom behavior needed. (Examples: conversational AI workspaces like Claude Projects or ChatGPT Workspace, or embedded vendor AI features already inside a tool you pay for.)

**Low-code workflow.** A workflow assembled in a visual builder like Zapier, Make, n8n (a visual automation platform that connects apps and moves data between them without writing code), or a similar tool. No external engineering — your team owns it directly, can see how it works, and can change it. Use this category when the workflow is custom but built from standard moves: pull from a system, run through an agent, write back, notify someone. (This is the path for operators with no in-house engineer.)

**Hand-built integration.** Custom code involving an API (application programming interface — how systems talk to each other) to a system of record, with an engineer in the loop. Slower than low-code, higher return, harder to change later. Use this category when the workflow runs at a scale or against a system that low-code tools can't reach, or when the data sensitivity rules out routing through a third-party platform. (No in-house engineer? This is the category where you bring in a builder or contractor for the implementation — the other two your team can usually own directly.)

To pick the category for each agent in your Hybrid Accountability Chart, run these three questions in order:

1. Does a mature product already do exactly what this agent requires, with light configuration? If yes — off-the-shelf. Don't build what you can configure.
2. Is the agent's workflow custom but composed of standard moves (pull from a system, run through an agent, write back, notify someone)? If yes — low-code. Your team can own and change it directly.
3. Does the workflow run at a scale, or touch a system of record, that low-code tools can't reach? Or does the data sensitivity rule out a third-party automation platform? If yes — hand-built.

Our marketing lead's four-agent setup, the one from the Co-Operating Model chapter, didn't require a line of code. Low-code build: skills wired, projects connected, tools configured.

The project management agent team that replaced our coordinator role was different. It lives on a server, runs continuously, and is always on. That one required infrastructure, monitoring, and an always-on deployment. Hand-built.

:::{.callout-note}
## Action Step
For every agent in your Hybrid Accountability Chart, name the category (off-the-shelf, low-code, hand-built). Write the choice in one line per agent and the reason in one sentence. If you can't write the reason without guessing, the design isn't done. (Build will pick the specific environment inside the category.)
:::

---

## 3. Human Orchestrator operational content — "What the Orchestrator's role actually looks like"

**Note:** This is the "day-to-day review, ramp-up arc, drift, marketing-lead four-agent example" content from the "What the Orchestrator's role actually looks like" subsection and the Action Step that follows it. It belongs in 06b, which covers designing the work (the day-to-day operating side). Ch6 retains naming/choosing the Orchestrator (Right Seat Evaluation); 06b covers how the Orchestrator actually runs the team.

---

### What the Orchestrator's role actually looks like

The Orchestrator runs the agent team's work day-to-day once the workflow ships. They review at the goal level, not the task level. They don't check every output line by line; they ask whether the team is moving the constraint in the right direction. And they feed the design improvements between Sprints. After every Compound phase, the Orchestrator looks at what the team produced and asks: what one design change would make the next Sprint better? Eight Sprints of one good design change each produces an agent team substantially more capable than the one that shipped in Sprint one.

The right person has operational authority over the workflow: someone who can direct the agent team and make the calls it can't, not just coordinate around it. They need comfort with ambiguity, because the first few Sprints will surface problems nobody anticipated. And they need willingness to shift from executing the work themselves to directing the team that executes it. The best candidate is usually the person closest to the work who's also frustrated by the parts of it that don't require their skill.

That third trait is the development gap. The operations lead who got the job because she was excellent at executing operations work is now being asked to direct an agent team that does the executing instead of doing it herself. It's a different role, and developing the capability is deliberate work.

What does ramp-up look like? The first Sprint is guided: the Orchestrator works through Design alongside the Sprint Lead, with support from a Compound coach or from the framework's question sequence step by step. Someone experienced sits alongside them to coach the process, not to do the work. By the second Sprint, they're operating the workflow independently. The fourth Sprint is when they start driving design improvements themselves — not because someone handed it to them, but because they've run the loop enough times to see what to fix. The skill is learned by doing the work, one Sprint at a time.

The Orchestrator also owns the day-to-day operation once the workflow ships: keeping inputs clean, reviewing outputs at the appropriate frequency, and flagging when the design is drifting. Drift shows up as inputs degrading, outputs trending off, and a class of decisions no longer being handled cleanly. Companies that deploy agent teams without a named person responsible for this operational layer discover within weeks that the team has drifted — inputs no longer reviewed, outputs no longer trusted, the workflow quietly reverted to "we just do it the old way." The fix is naming the role and giving it the hours. In a 25-person company, that's part of the Orchestrator's existing role. In a 100-person company, the Orchestrator may delegate day-to-day monitoring to someone on their team, but the accountability stays with the Orchestrator.

You met a version of this role in the Co-Operating Model chapter: our marketing lead running four agent teams in parallel, each working a different piece of the same content project. Each one had a named tool, a scoped task, and her reviewing outputs. What I didn't show you there is the Design work that made that shift possible. Someone had to sit down and ask what she was actually accountable for. Which parts of her job required her judgment, and which required execution any well-designed agent could handle? Which teams needed to surface decisions to her, and at what frequency? Those questions got answered in a Design session before a single agent was built. The four-tab setup wasn't improvised. It was designed, and because it was designed, her role changed when the agents came in.

:::{.callout-note}
## Action Step
Identify your Human Orchestrator candidate. Ask: does this person have operational authority over the workflow? Are they willing to shift from executing the work themselves to directing the team that executes it? Write down the name. If there's a development gap to fill before they can run the role, name it, and plan the first Sprint as the ramp-up — not as a test they need to pass.
:::
