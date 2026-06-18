# Phase 3A Outline — Ch 1 (Diagnosis)

**Source file:** `chapters/01-diagnosis.qmd` · **Priority:** 3C #7 (SECOND DO-OVER after the first pass produced reader-facing context bleed) · **Drafter agent:** `voice-implementer` (NOT `general-purpose` with brief)
**Proposed title:** *"Chapter 1: Diagnosis: It's an Operating Problem, Not a Technology Problem"*
**Beads:** `book-68zp` (ARC#10 scorecard math), `book-tb8h` (ARC#1 cross-refs — handled 3B), `book-ultm` (ARC#2 agent definition), `book-b8yy` (FLOW#3 Meridian — REVISED: Meridian is the FICTIONAL anchor introduced at §IV.I, NOT conflated with the real discovery-call client).
**Status:** Second do-over. The first pass produced mechanical coherence but failed the reader-in-context test ([[reader-in-context-discipline]]). The pipeline as run was incomplete: the `ideal-customer-reader` agent was skipped, and `general-purpose` was used in place of project-specific agents (`voice-implementer`, `editorial-coherence`, `voice-scanner`, `prose-craft`, `editor`). This outline carries the corrected scope.

---

## Chapter syllogism

- **Premise 1.** Your AI investments aren't paying off.
- **Premise 2.** The reason isn't the tools — it's that your operating model was never designed to absorb a non-human worker.
- **Premise 3.** Revenue per employee is the productivity proxy that tells you whether the operating model is doing real work. Every prior technology wave bent that number; AI bends it more dramatically because it can take over whole categories of human activity, not just speed humans up.
- **Premise 4.** Five dimensions tell you where your operating model needs the most work: Constraint Clarity, Information Readiness, Workflow Visibility, Decision Rights, Measurement Discipline.
- **Conclusion.** Score yourself on the five dimensions. The total tells you how ready you are; the dimensions tell you where in the work ahead you'll need to push hardest.

---

## Chapter content outline (proposed)

> **Legend:** [NEW] = added · [CUT] = removed · [MOVE] = relocated · [TRIM] = shortened · [REVERT] = undo prior change · [KEEP] = unchanged · *(L#)* = current line in `01-diagnosis.qmd`

### I. In-Brief callout *(L3-7)* [TRIM]

- **Assumes:** reader is opening the book. No prior context.
- **Establishes:** chapter is a diagnostic. By the end the reader has a 20-question Scorecard, a single percentage, and a sense of where in the work ahead they'll need to push hardest.
- **Sets up:** the diagnostic frame for the opening story.

Content guidance:

- A. **Strip the orchestrator-conversation context bleed.** Current text carries this cluster: *"The Scorecard measures readiness. It doesn't route you to a starting point. The framework does that, and the starting point is always Signal."* That's residue of an author/orchestrator back-and-forth about how the Scorecard works mechanically. It is meta-commentary, not reader prose. **CUT.**
- B. **Reader gets exactly two things from the In-Brief:** what this chapter does (diagnostic), what they walk away with (a percentage + an honest read of where their first stretch of work will demand the most attention).
- C. **Target length:** 3-4 sentences max.

### II. Opening hook — the discovery call *(L9-15)* [REVERT Meridian misattribution]

- **Assumes:** reader has read the In-Brief. Knows they're being diagnosed.
- **Establishes:** the most common AI failure pattern — three people, three tools, no coordination, no structural change.
- **Sets up:** the claim that this is a design problem, not a technology problem.

Content:

- A. **CRITICAL — REVERT.** The discovery-call company is NOT Meridian. Meridian Manufacturing is a FICTIONAL case study we will introduce later as a worked anchor running through the book. The discovery call in the opener is an anonymized REAL client. The prior pass conflated them; do not repeat. **The opener returns to the original framing:** anonymized mid-market manufacturing client, no name, no Meridian reference.
- B. CEO + two directors on a discovery call. CEO uses ChatGPT, one director uses Claude, the other Poe (the aggregator).
- C. Three people, one company, three tools, no shared accounts, no shared workflow.
- D. They booked the call because they sensed they were leaving something on the table; they couldn't say what. (Keep the existing emotional framing; the cliché is acceptable because it accurately captures the reader's likely state. Voice scanner / prose-craft may flag for tightening.)
- E. **No Meridian here.** Meridian gets introduced at §IV.I where the chapter pivots from diagnosis to "here's how the redesign starts," with explicit framing that Meridian is a fictional anchor.

### III. Is Your Operating Model Any Good? *(currently L17-33)* [HEAVY REWRITE]

**Proposed heading:** `## Is Your Operating Model Any Good?`

- **Assumes:** reader saw the three-tools-one-company story. They've recognized the pattern in their own company.
- **Establishes:** every business has SOME operating model. The diagnostic question is whether it's any good. A good operating model knows things the chapter then lists; a weak one doesn't. The pattern of "buy tools first, design later" predates AI by decades.
- **Sets up:** the next section's question — if it's operating-model design that's at issue, how do you measure whether the design is working?

Content:

- A. **Opening sentence — REWRITE.** Lead with the story above, not with an orphaned "This." Suggested: *"What that team showed us is the most common AI failure pattern we see — three tools, no coordination, no structural change. Nobody designed the work before the tools arrived."* **CUT** the prior pass's follow-on "This is a design problem, and the design that's missing is the operating model." That sentence asserts a conclusion the reader hasn't been led to yet. Let the bullet contrast (below) make the case.

- B. **The contrast list — REFRAME to GOOD vs. WEAK.** Per author note: every business has SOME operating model; the question is quality. **NOT "WITH" vs. "WITHOUT."**

    **A good operating model:**
    - Knows who decides what gets done.
    - Knows who hands what to whom.
    - Knows what each function is accountable for.
    - Can describe end-to-end how work flows from intake to outcome.
    - Can name where the work breaks before it breaks.

    **A weak one:**
    - Has an org chart but no map of how work actually moves through it.
    - Resolves coordination by whoever is loudest in the room.
    - Discovers handoffs failing only when a customer complains.
    - Hires when the work stalls, because no other lever is visible.
    - Adds tools (including AI) on top of undesigned work and expects the tools to do the design.

- C. **Pattern predates AI.** Two decades of mid-market acquisitions absorbed without redesigning how work actually moved. The acquired operation got bolted on; the accountability map was never rebuilt. AI is the latest technology to expose the same gap.

- D. **HBR / Sadun citation: CUT.** Per prior decision. The contrast list carries the claim without authority transfer.

- E. **The CEO line most readers say privately** *(L29 blockquote)* [KEEP verbatim]
    - *"You know AI matters. You just don't know what it can actually do inside your company — or where to start."*

- F. **Bridge to the gap (folded former §IV "you've already tried" content)** — REWRITE per author note. Two specific corrections:
    - 1. **NOT "Most readers have already tried."** That overstates what we know. Rewrite as conditional: *"If you're like most operators, you've already tried."*
    - 2. **NOT "a tool your team barely uses."** False. People ARE using AI — heavily, individually, in silos. That's the design failure. Rewrite: *"...you've already tried — subscriptions, a pilot or two, a consultant, a vendor demo. The result is people using AI in silos, with no coordination across the company. The tools are doing work. Nothing structural has changed."*
    - 3. **Closing line:** *"The missing piece is how to design the work — treating workflows as systems, knowledge as an indexed asset (data organized so an AI can search and retrieve from it on demand; covered in depth in Source), and handoffs as interfaces."*

### IV. The Headcount Paradox *(currently L49-92)* [REWRITE — build the argument carefully]

**Proposed heading:** `## The Headcount Paradox`
**Sub-H3:** `### Redesign the Operating Model Before You Staff It`

- **Assumes:** reader believes AI failures are operating-model failures (from §III).
- **Establishes:** revenue per employee is the productivity proxy that measures whether the operating model is doing real work. Every prior tech wave DID bend RPE (acknowledge this). What's new about AI is that it bends RPE more dramatically — because it takes over whole categories of work, not just speeds humans up. The Headcount Paradox is what happens when AI investment is on the books but RPE hasn't moved.
- **Sets up:** the redesign principle (§IV.I), where Meridian gets introduced as the fictional case study, and the diagnostic dimensions (§V → §VI → §VII).

Content (built in this order, NOT the order of the prior draft):

- A. **Lead with the calc instructions:**

    > *Stop here and do this calculation. Add up your company's revenue for the last twelve months. Divide it by the number of full-time employees on payroll today. That's your revenue per employee — the dollars of revenue each person on staff generates.*

- B. **Define RPE as productivity proxy** — make the connection explicit (per author note: we haven't done a good job connecting RPE to productivity).

    > *Revenue per employee is the cleanest dollar-level proxy for productivity at the company level. Higher revenue per employee means each person on staff is producing more, usually because the company has invested in systems, processes, or technology that lets people produce more without working harder. Flat or declining revenue per employee means revenue grew, but only by adding people at the same rate. The whole reason companies invest in technology is to move this number — to get more output from the same number of people.*

- C. **Table context** — explain the three comparison points, why they matter:

    > *Compare three snapshots: where you were at your last major system rollout (your ERP, CRM, PSA, practice-management system, or whatever you most recently installed company-wide is the cleanest reference point most operators have); where you stand today; and where you'd be next year if you grew 20% without adding people. The first comparison tells you whether your prior tech investment moved the number. The second tells you whether you can plausibly grow without adding bodies.*

- D. **The fillable 3-row table** [KEEP]:

    ```
    | Snapshot                                | Revenue | Employees | Revenue per Employee |
    |---|---|---|---|
    | At your last major system rollout       | $______ | ______    | $______ |
    | Today                                   | $______ | ______    | $______ |
    | Next year, +20% revenue, no new hires   | $______ | ______    | $______ |
    ```

- E. **Acknowledge prior tech worked** — REVISE per author note. Don't pose the rhetorical "every prior wave was supposed to bend this number" — answer it.

    > *Every prior technology wave bent this number. Spreadsheets bent it. CRM bent it. ERP bent it. The reason your company invested in any of them was the same: to move revenue per employee in the right direction. Most of them worked. The companies that ran them well got more output from the same staff.*

- F. **What's special about AI** — answer the question explicitly:

    > *AI can move that number more dramatically. Prior waves made a human faster at a category of work. AI can take the category. Triaging inbound, drafting recurring documents, reconciling records, summarizing what was said — categories of work that previously required a person are now categories an AI can hold. That's the difference. Not faster humans; fewer human-hours required for whole categories of output.*

- G. **The slope and the COO calendar** — connect productivity to headcount slope explicitly:

    > *Revenue and headcount have run on a slope for most of business history: every meaningful jump in revenue pulled a roughly proportional jump in headcount. That slope IS the productivity question. If RPE is rising, the slope bends — revenue grows faster than headcount. For most mid-market operators, the AI line item on the P&L hasn't bent that slope, because the operating model never got redesigned. Meanwhile your COO is on the calendar asking to approve the next two roles, and you sign off knowing the AI investment was supposed to bend that slope by now.*

- H. **Name the paradox cleanly:**

    > *That gap has a name. The Headcount Paradox. Each new dollar of revenue still demands roughly the same headcount it did before, even after you invested in AI to change that math. The investment is on the books. The structure hasn't changed.*

- I. **ARTIFACT — Headcount before/after Excalidraw** — sits here, adjacent to where the paradox is named.

- J. **Sub-H3: Redesign the Operating Model Before You Staff It**

    Content:
    - 1. **Principle:** redesign the operating model before you staff it. Sometimes that redesign uses AI; sometimes it doesn't. The principle is the same.
    - 2. **Jesse / SuperWebPros example (AI-era):** thirteen people to eight. Mapped every function, separated judgment from rule-based work, built agent teams. Billings up. Profitability up.
    - 3. **Julie / 44-country HR integration (pre-AI):** CHRO over a Fortune 500 division acquisition. Resisted the instinct to add HR business partners by region; redesigned the function first. The global team ran on a smaller proportional headcount than the pre-acquisition domestic function — because the work was designed before it was staffed.
    - 4. **Bridge:** AI wasn't part of Julie's redesign. The principle was. AI lets that same kind of redesign reach further, because an agent can hold a workflow a software tool could only assist with.
    - 5. **[NEW — Meridian INTRODUCTION here, NOT at opener]** This is where the fictional case study lands. Suggested wording:

        > *Throughout the rest of this book, we'll follow a fictional case study: Meridian Manufacturing, a twenty-seven-person custom metal fabrication shop with $7.2M in revenue. Meridian is a composite — built from the patterns we've seen across dozens of mid-market operators — but everything we'll show you happens at companies like Meridian every day. Meridian's quoting workflow is bottlenecked on Elena Ruiz, the VP of Operations, who holds fifteen hours a week of pricing and exception decisions nobody else in the company can make. Costing them, by their own first read, around $558K a year in delayed and lost bids. Every chapter ahead shows what redesigning Meridian's work looks like in real time. By the end of the book, you'll have walked their full first Sprint with them.*

- K. **Pro Tip callout** [KEEP] — the Headcount Paradox is an operating problem, not a technology problem.

### V. You Have a Co-Intelligent Co-Operation Problem *(currently §VI, L94-124)* [TRIM and REORDER]

**Proposed heading:** `## You Have a Co-Intelligent Co-Operation Problem`

- **Assumes:** reader believes the operating-model redesign principle (from §III + §IV) and has seen Meridian as the worked example of where a redesign starts.
- **Establishes:** a NAME for this class of problem — *Co-Intelligent Co-Operation*. Names what makes the problem new: there's a non-human worker that the existing operating model wasn't designed to absorb.
- **Sets up:** the diagnostic — once you know it's a Co-Intelligent Co-Operation problem, the question is *where* in your operation it's broken. That's the Scorecard.

Content (per author note: get to the naming sooner, don't restate prior sections):

- A. **Open by naming the problem directly, not by restating §III/§IV.** The prior pass opened with *"Your AI investments aren't producing returns because of an operating-model problem"* — a restatement of what the chapter has already established. Replace with:

    > *That's the class of problem you're solving. It has a name: a Co-Intelligent Co-Operation problem. Co-Intelligent is the actual workforce — humans and AI as one workforce. Co-Operation is how you design the handoffs between your human team and your AI agents: who does what, who reviews, where the work moves between them.*

- B. **What also matters, briefly** [KEEP, tightened]: culture, training, tool selection — real factors. Operating-model design is what they all sit on top of.

- C. **Why the new worker produces nothing** [KEEP]: company was designed to be run by humans alone. You introduced a second kind of worker without changing the structure. No seat, no accountability, no defined handoff → produces nothing the organization can compound on.

- D. **Chatbot vs. agent** [KEEP, brief]: AI is usually treated as a chatbot — one human, one chat window, one task at a time. The real capability is in agents, which run in parallel inside designed workflows. The canonical definition lives in the Co-Op Model chapter; one inline forward reference is sufficient.

- E. **Action Step — REPLACE.** The current L10-themed Action Step is vestigial. Suggested replacement:

    > **Action Step.** Walk through your company and list every function where AI is currently being used. For each, write down: who supervises the AI's output, how often it gets reviewed, and what scorecard the AI is being measured against. The rows that come back blank are where your Co-Intelligent Co-Operation has no structure — and the Scorecard ahead will tell you which of the five dimensions of that missing structure to read most carefully.

- F. **The instinct-to-interrupt blockquote** [KEEP]: *"The instinct to solve a people problem with another person is exactly the instinct this book exists to interrupt."*

### VI. The Five Dimensions That Tell You Where Your Operating Model Is Broken *(currently §VII, L116-148)* [REFRAME — teach, do NOT use Meridian here]

**Proposed heading:** `## The Five Dimensions That Tell You Where Your Operating Model Is Broken`

- **Assumes:** reader knows they have a Co-Intelligent Co-Operation problem. They don't know where in their operation it's broken.
- **Establishes:** what the five dimensions ARE and why each one matters as an independent failure mode. Names the two-precondition grouping (technical vs. operating-model) with a graphic.
- **Sets up:** the Scorecard, where the reader measures each dimension in their own company. **Meridian's results appear AFTER the Scorecard, not here.**

Content:

- A. **Section opening:**

    > *Before you can fix where your operating model needs work, you need to see what "weak" looks like at a level you can measure. There are five dimensions where AI-ready operating models hold and AI-unready ones don't. The Scorecard ahead measures each one. This section names what each dimension is and why it matters.*

- B. **The two preconditions split** [KEEP, lives here NOT inside the Scorecard]:
    - 1. **Technical preconditions** (whether an AI agent can do the work at all): Information Readiness, Workflow Visibility.
    - 2. **Operating-model preconditions** (whether your organization holds the change once it's deployed): Constraint Clarity, Decision Rights, Measurement Discipline.
    - 3. A company can score strongly on one half and weakly on the other. Both halves have to come up before the redesign work compounds.

- C. **[NEW] ARTIFACT — the split graphic** (Excalidraw, 2-column diagram).

- D. **The five dimensions — each with its own H3.** Per author note: **NO "Meridian's first read"** here. Meridian's results land in §VII after the reader has run the Scorecard.

    - 1. **H3: Constraint Clarity**
        - *What it is:* can your leadership team name the ONE operational constraint AI should solve, and quantify what it costs?
        - *Why it matters:* tools without a target produce scattered pilots. Naming the constraint precisely is the single most consequential move ahead of you.

    - 2. **H3: Information Readiness**
        - *What it is:* is the knowledge your team runs on documented and accessible, or trapped in people's heads?
        - *Why it matters:* an agent can only act on knowledge it can reach. Tacit knowledge in a person's head is invisible to AI.

    - 3. **H3: Workflow Visibility**
        - *What it is:* can you draw the workflow where the constraint lives, including who does what and where handoffs break?
        - *Why it matters:* workflows that exist only in habit can't be specified for an agent.

    - 4. **H3: Decision Rights**
        - *What it is:* do you know who decides what AI handles and what stays with humans?
        - *Why it matters:* organizational trust, not AI capability, determines what gets deployed. Without explicit decision rights, every AI output gets second-guessed or rubber-stamped.

    - 5. **H3: Measurement Discipline**
        - *What it is:* can you put a dollar number on what the constraint costs per quarter?
        - *Why it matters:* without a number, you can't prove AI made it better. An AI experiment without a target is curiosity, not investment.

- E. **Closing transition** to the Scorecard:

    > *Now you know what each dimension is and why it matters. The Scorecard is how you measure each one in your company.*

### VII. The AI Readiness Scorecard *(currently §VIII, L148-301)* [CONSOLIDATE — one table, Likert scale, no mid-table interruptions]

**Proposed heading:** `## Score Your AI Readiness`

- **Assumes:** reader knows what each of the five dimensions IS and why it matters (from §VI).
- **Establishes:** where YOUR organization sits on each dimension, as a measured number. Produces dimension subtotals, a total percentage, a bucket reading, and (Meridian's results) one worked example of what a first read looks like.
- **Sets up:** Chapter 2 (the beliefs that have to be in place) and the chapters that follow (where the redesign work actually happens).

Content (REVISED per author note: one consolidated table, Likert scale, no mid-section Action Steps):

- A. **Scorecard intro — TRIMMED.** No re-definition of dimensions (handled in §VI). Just the scoring mechanics:

    > *Twenty questions, four per dimension. For each statement, rank your company on a 1-to-5 scale — 1 means "not at all true" and 5 means "absolutely true." Do this with whoever would be in the room if you were deciding whether to invest in AI. Not just you. The team.*

- B. **One consolidated 20-row table.** All five dimensions, all twenty questions, presented together — no Pro Tips, no Action Steps interrupting mid-table. The reader scores all 20 in one continuous pass, then encounters the math and the bucket.

    Table format (Likert-scale columns):

    ```
    | #  | Dimension                | Statement                                                                       | 1 | 2 | 3 | 4 | 5 |
    |----|--------------------------|---------------------------------------------------------------------------------|---|---|---|---|---|
    | 1  | Constraint Clarity       | We can name one operational constraint that, if removed, would change the P&L. | ☐ | ☐ | ☐ | ☐ | ☐ |
    | 2  | Constraint Clarity       | We've quantified the cost of that constraint in dollars, hours, or margin.     | ☐ | ☐ | ☐ | ☐ | ☐ |
    | 3  | Constraint Clarity       | Our leadership team agrees on what the #1 constraint actually is.              | ☐ | ☐ | ☐ | ☐ | ☐ |
    | 4  | Constraint Clarity       | We've traced the symptoms back to a structural root.                           | ☐ | ☐ | ☐ | ☐ | ☐ |
    | 5  | Information Readiness    | We can answer "where does this information live?" for every critical workflow. | ☐ | ☐ | ☐ | ☐ | ☐ |
    | ...| (all 20 rows)            | ...                                                                              | ☐ | ☐ | ☐ | ☐ | ☐ |
    ```

    Note for production: the ☐ boxes need to render as a clean visual Likert scale in the PDF. Drafter notes the design intent; production handles the actual rendering.

- C. **[H3] Compute Your Dimension Subtotals** — after the table, add the in-body subtotal table:

    ```
    | Dimension                 | Subtotal (out of 20) |
    |---|---|
    | Constraint Clarity        | ___ |
    | Information Readiness     | ___ |
    | Workflow Visibility       | ___ |
    | Decision Rights           | ___ |
    | Measurement Discipline    | ___ |
    ```

- D. **[H3] Compute Your Total and Read the Bucket** — total all 20 (max 100, which IS your AI Readiness percentage), then read the bucket:

    | Score | What it means |
    |---|---|
    | 20-34% | Start here. The operating model isn't designed for AI yet. Most honest answer most mid-market companies give on first read. |
    | 35-49% | Foundations exist; the math hasn't compounded yet. Most readers land here. |
    | 50-64% | You're above average. The framework will sharpen what's already there. |
    | 65-79% | You're operating well. The book formalizes what you already do informally. |
    | 80-100% | You're running a Co-Intelligent Co-Operation in fact, if not in name. The chapters ahead give you the vocabulary and the through-line to scale the discipline. |

- E. **[NEW — Meridian's results land HERE, not in §VI]** Per author note: Meridian's first-pass scores belong AFTER the reader has run their own Scorecard, as a worked illustration.

    > *On their first read, Meridian's leadership team scored 41% — the 35-49% bucket. Foundations present, math not yet compounding. Their dimension subtotals: Constraint Clarity 6, Information Readiness 9, Workflow Visibility 8, Decision Rights 10, Measurement Discipline 8. The bottleneck was felt but never priced; the Customer Notes spreadsheet existed but lived on one desktop; the workflow had five handoffs and two systems that didn't talk. We'll walk Meridian through the rest of the chapters as they work that score.*

- F. **[H3] Read Your Subtotals — where the chapters ahead will demand the most attention** — REFRAME the prior "Map Your Lowest Dimension to the Sequence Stage" section. Per author note: strip the "Signal," "Sequence" forward references that read as undefined terms to a first-time reader; strip the meta-routing-vs-readiness commentary.

    > *Your lowest dimension is the one part of the work ahead that will demand the most attention in your first stretch of redesign. The chapters that follow walk through the redesign in order; nothing in that order changes based on your score. What changes is where you'll need to push hardest, which conversations will be longer, which inputs you'll need to assemble before the first session. If two dimensions tie for the lowest score, the one that maps to earlier work in the redesign is the more consequential gap — because each stage of the work depends on the inputs the prior stage produced.*

- G. **Closing checklist callout** — write down overall score, lowest dimension, highest dimension, and one sentence describing where the reader expects to need the most help.

- H. **Pro Tip callout** [REWRITE] — keep it tight, no meta-routing context bleed:

    > *The Scorecard isn't a test. It's a map of where you stand and where you'll need to push hardest. The framework ahead works the same way regardless of where you started.*

### VIII. Closing handoff to Ch 2 *(L303)* [REWRITE]

- **Assumes:** reader has scored themselves and knows where they'll need to push hardest.
- **Establishes:** the framework starts compounding only if four mindset shifts are in place. The next chapter is where those shifts land.
- **Sets up:** Ch 2 ("You're Already a Tech Company") as the precondition belief that makes the rest of the framework hold.

Content: *"The next chapter makes the case that you're already a tech company. Three other shifts follow from that. Without those shifts in place, the framework reads as extra work for the same outcomes. With them, it's the cheapest path to outcomes you already want."*

### IX. Reflection Questions *(L305-311)* [TRIM 5 → 4]

- **Assumes:** reader has completed the Scorecard.
- **Establishes:** four reflective prompts for the leadership team's working session.
- **Sets up:** the team conversation that gets the leadership group aligned.

Drop Q5. Keep Q1-Q4. Verify Q1's wording doesn't imply "which dimension to start with" — it asks which dimension scored lowest and whether the team agrees.

---

## Heading inventory — current → proposed

| Current heading | Proposed directive heading |
|---|---|
| `# Chapter 1: Diagnosis: It's an Operating Problem, Not a Technology Problem` | KEEP (title-vs-§V antithesis resolved by §V being renamed to name the problem, not restate the antithesis) |
| `## The Diagnosis Is the Operating Model` | `## Is Your Operating Model Any Good?` |
| `## The Headcount Paradox` | `## The Headcount Paradox` *(keep)* |
| `### Redesign the Operating Model Before You Staff It` | KEEP |
| `## Name the Problem: You Have a Co-Intelligent Co-Operation Problem` | `## You Have a Co-Intelligent Co-Operation Problem` *(shorter)* |
| `## Before You Score, Understand the Five Dimensions` | `## The Five Dimensions That Tell You Where Your Operating Model Is Broken` |
| Five H3 dimension intros | Same, with "what it is / why it matters" only — NO Meridian first-read inside §VI |
| `## Score Your AI Readiness` | KEEP |
| Per-dimension H3s inside Scorecard | CUT — one consolidated 20-row table replaces them |
| *(NEW)* | `### Compute Your Dimension Subtotals` |
| *(NEW)* | `### Compute Your Total and Read the Bucket` |
| *(NEW)* | `### Read Your Subtotals — Where the Chapters Ahead Will Demand the Most Attention` |
| `## Reflection Questions` | KEEP |

---

## Meridian thread (per [[meridian-as-side-by-side-thread]], REVISED)

Meridian is a FICTIONAL case study, not a real client. The chapter introduces it at one place and references it at one more:

1. **§IV.I.5 Redesign** — Meridian gets INTRODUCED here as a fictional composite, with the explicit framing that the book will follow them through every chapter. Sized, named, described, given the worked constraint (quoting bottleneck, Elena, $558K/year). This is where the case-study thread starts.
2. **§VII.E Bucket** — Meridian's first-pass Scorecard score (41%, 35-49% bucket) lands here, as the worked example of what a first-pass score looks like.

**Meridian does NOT appear in §II (opener) or §VI (dimensions teaching).** The opener stays a real anonymized client. The dimensions section teaches without leaning on Meridian, because the reader hasn't run their own Scorecard yet — there's nothing to compare against until §VII.

---

## HBR citation discipline (this chapter)

**Recommendation: CUT** all HBR citations. The chapter does not need authority transfer. Sadun was cut in the prior pass; do not restore.

---

## Cross-chapter dependencies handled in Phase 3B (Drafter does NOT re-solve)

- **Agent definition standardization** *(book-ultm, ARC#2)* — canonical "agent" gloss at first standalone use, per [[jargon-house-rule]]. Drafter places it at the §V "chatbot vs. agent" paragraph. EC verifies. If deflourish strips it, EC fails.
- **Cross-references** *(book-tb8h, ARC#1)* — named-stage forward pointers only. No bare "Chapter 2." Use "the next chapter" or "the Co-Op Model chapter."
- **Orchestrator/Integrator disambiguation** *(book-8v6v.32)* — already cleared.

---

## Drafter notes

### Pipeline — full QC stack must run

This chapter's prior pass produced reader-facing context bleed because the QC pipeline ran an incomplete set of stages with `general-purpose` agent dispatches instead of the project-specific agents. Per [[qc-pipeline-per-chapter]], the FULL stack runs, using these specific agents (from `.claude/agents/`):

1. **`voice-implementer`** (Sonnet) — Drafter; applies this outline + author annotations.
2. **`editorial-coherence`** (Opus) — substance-landed, framework-attribution, coined-term-before-defined, callouts-assuming-context, structural balance.
3. **`.claude/tools/deflourish.py --apply`** — paragraph-level voice rewrites.
4. **`.claude/tools/voice-scan.py`** — Vale + n-gram + semantic check.
5. **`voice-scanner`** agent — voice judgment the tool misses; line-numbered direction (does NOT rewrite).
6. **`voice-implementer`** (round 2) — applies voice-scanner direction.
7. **`prose-craft`** agent — craft flags (restatement, abstraction, telling-not-showing, monotone rhythm); line-numbered direction.
8. **`editor`** agent — structural cuts, pacing tightens, flab removal.
9. **`ideal-customer-reader`** (Sonnet) — reads as CEO of 25-100-person company running EOS; flags AND fixes undefined terms, "so what?" gaps, context bleed, unsubstantiated claims. **This stage was skipped in the prior pass; it must run.**
10. **`quarto render`** — verify the chapter still builds.
11. **Orchestrator gate** — diff review, then surface to author.

The orchestrator does NOT surface a chapter to the author until ALL nine agents/tools have completed.

### Anchoring discipline

The Drafter reads the chapter syllogism + each section's Assumes/Establishes/Sets up triad BEFORE writing. A sentence that violates a marker (orphaned antecedent, restated prior claim, severed dependency, forward reference to undefined term, context bleed from author/orchestrator conversation, unsubstantiated categorical claim) is a coherence break the Drafter fixes before moving on. Per [[reader-in-context-discipline]].

### Specific items from the author's review of the prior pass

- §I In-Brief: strip the meta-routing-vs-readiness cluster ("Scorecard measures readiness, framework routes, start at Signal").
- §II Opener: **REVERT** the Meridian misattribution. The discovery-call company is an anonymized REAL client, not Meridian.
- §III: cut the unsubstantiated "design problem / operating model is missing" sentence; reframe contrast as GOOD vs. WEAK.
- §III.F: rewrite to "if you're like most operators" and "people use AI in silos, not coordinated"; **do not claim "team barely uses."**
- §IV: build the RPE / productivity / slope / AI-difference argument carefully in the new order shown above. Answer "what's special about AI?" explicitly.
- §IV.I.5: INTRODUCE Meridian as the fictional case study HERE.
- §V: don't re-restate the operating-model claim; lead with NAMING the Co-Intelligent Co-Operation problem.
- §VI: NO Meridian first-read per dimension.
- §VII: ONE consolidated 20-row table, Likert-scale boxes, no mid-table interruptions. Meridian's results land here, after the reader scores.
- §VII.F: strip the "Signal," "Sequence" forward references and the meta-routing commentary.

### Author followup items still on the table

- Likert-scale rendering: confirm with production whether the ☐ box notation will render cleanly in PDF, or whether a different visual treatment is needed.
- §I In-Brief target length: 3-4 sentences max — confirm exact wording.
- §III.F "people use AI in silos" framing: confirm specific phrasing before drafting (the line carries weight in setting up §IV's design-problem framing).
