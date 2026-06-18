# Phase 3A Outline — Ch 6 (Source)

**Source file:** `chapters/05-source.qmd` · **Priority:** 3C #2 · **Drafter model:** Opus
**Proposed title:** *"Source: Map What the Organization Knows About the Constraint"*
**Beads:** `book-3w1t` (FLOW#2 simplicity rescue — only Simplicity Fail in main body), `book-n628` (ARC#11 AI Tier inline definition reconciliation), `book-xqxi` (ARC#3 jargon — 3B sweep), `book-b8yy` (FLOW#3 Meridian — placement, not absence), HBR citation discipline (memory), AI Tier terminology (memory — adopt case-study Tier 1 / Tier 2 / Tier 3 / Not AI-tier).
**Status:** Heaviest restructure in Phase 3C. Promote Jesse PM coordinator as opener; strip HBR scaffolding (Argenti + Sadun + AWS); compress PIS framework to one sentence; compress TML to one paragraph; move Meridian vignette earlier (was at ~70% through); merge "people don't have APIs" Digital/Organic/At-risk into the three-pass section; collapse two near-duplicate KM sections into one; revise AI tier vocabulary to match case studies (Tier 1 / Tier 2 / Tier 3 / Not AI-tier); convert italic-fragment headings to directive language. **Outline carries the upgraded format ([[chapter-syllogism-and-flow-markers]]) so the Drafter can anchor the heavy restructure in chapter-level logic — sentence-level decisions inside reorganized sections must respect their flow markers.**

---

## Chapter syllogism

- **Premise 1.** The reader arrives at Source with a validated constraint from Signal — a named problem with a dollar number on it, but no buildable path. Without Source, Design starts on assumptions nobody verified.
- **Premise 2.** The information any constraint depends on lives in three layers — Systems of Record (authoritative data), Systems of Knowledge (documented know-how), Systems of Semantics (relationships and meaning AI needs to reason). What "knowing what you have" means is naming, for the constraint, which layer each piece of knowledge currently lives in.
- **Premise 3.** Source produces one artifact — a one-page Knowledge Map — built in three passes (Digital, Organic, Missing) and classified along two axes (Structured/Unstructured, Durable/Ephemeral) plus the AI Tier system (Tier 1 / Tier 2 / Tier 3 / Not AI-tier). The classification tells the Drafter what's reachable today, what's reachable with extraction work, and what stays human.
- **Conclusion.** Source ends when the reader can hand Design a one-page Knowledge Map plus the Constraint Statement from Signal. Constraint plus map is the input Design needs to start building — the assets, the flow, the gaps, the at-risk dependencies, and the tier of each, on one sheet of paper.

---

## Chapter content outline (proposed)

> **Legend:** [NEW] = added · [CUT] = removed · [MOVE] = relocated · [TRIM] = shortened · [COMPRESS] = collapsed to one paragraph or sentence · [COLLAPSE] = two sections merged into one · [MERGE] = folded into another section · [REVISE] = vocabulary or framing reconciled · [KEEP] = unchanged · *(L#)* = current line in `05-source.qmd`

### I. In-Brief callout *(L3-6)* [TRIM]

- **Assumes:** reader has just finished Signal. They have a validated constraint with a dollar cost attached. They believe Source is the next step but don't yet know what Source produces.
- **Establishes:** Source maps what the organization knows about that constraint. Deliverable = one-page Knowledge Map. Gate = skipping Source means Design starts on assumptions.
- **Sets up:** the chapter's opening hook, where Source is shown in action before the frameworks behind it get named.

- A. **Single core claim:** Source maps what the organization knows about the constraint Signal validated. Deliverable = one-page Knowledge Map.
- B. Closing sentence: skip Source and Design becomes guessing on assumptions nobody verified.
- C. Drop the three-layer enumeration in the callout; let the chapter make the claim. *(currently 4 lines of dense framework name-checking → target 3 lines, single artifact + single gate.)*

### II. Opening hook — Jesse PM coordinator anecdote *(currently L26-30 — [MOVE] up to chapter opener)*

  **Heading (proposed, directive):** "Before You Decide What to Do, Map What She Actually Does."

- **Assumes:** reader knows from the In-Brief that Source produces a one-page Knowledge Map. No prior framework context.
- **Establishes:** Source is what happens when leadership stops trying to decide *what to do* about a constraint and starts asking *what does this person/system actually do* — the mapping discipline that keeps a team from acting on assumptions. The Jesse/Sofia coordinator call is the worked example of that move; the chapter is the discipline of doing it deliberately.
- **Sets up:** the three-layer frame (§III), which is the structural answer to "what does she actually do" — namely, every task consumes information that lives in one of three layers.

- A. **The scene:** Jesse and Sofia on a call deciding what to do about the project coordinator. ~$24k/year role. Work falling behind. Billing impacted. Signal validated the constraint.
- B. **The turn:** before deciding *what to do*, they stopped. "We need to understand what she actually does. Not the job description. What she touches, what systems she's in, what decisions she makes that nobody else makes, what's in her head that isn't written down."
- C. **The reframe:** the question stopped being whether to replace the coordinator and started being how information moved through her role. Every task consumed information from somewhere and produced information that went somewhere else. **Mapping that flow was Source.**
- D. **Bridge sentence:** they didn't call it Source at the time. But it was the step that kept them from acting on assumptions instead of reality. The rest of this chapter is the discipline of doing that work deliberately.
- E. [CUT] Any HBR opener material from the current L8-22 frame. The chapter does NOT open on abstract framework framing.

### III. The three layers of organizational information *(currently L8-22 — [MOVE] AFTER the Jesse opener; [TRIM] HBR scaffolding)*

  **Heading (proposed, directive):** "Every Organization's Information Lives in Three Layers."

- **Assumes:** reader has just watched Jesse and Sofia stop and map what the coordinator actually does. They believe Source is real work but don't yet have a frame for *what kinds of information* they're mapping.
- **Establishes:** the three-layer frame — Systems of Record (authoritative data), Systems of Knowledge (documented know-how), Systems of Semantics (relationships and meaning AI needs to reason). Names that Source doesn't *build* Systems of Semantics; it names what layer each piece of knowledge currently lives in so Design knows what's there and what has to be built. The canonical agent definition lands here at first use (`book-ultm`).
- **Sets up:** §IV (Julie M&A) as the non-AI parallel — same three-layer gap in M&A integration — and §V's claim that diagnosis isn't done until you know what you *have* across these three layers.

- A. **The frame** *(L12)* — three layers cover where knowledge lives in every operating company.
- B. **Systems of Record** *(L14)* [KEEP]
    - 1. Authoritative data: CRM, ERP, JobBOSS, QuickBooks.
    - 2. If it's wrong here, it's wrong everywhere.
    - 3. The layer operators know best and trust most.
- C. **Systems of Knowledge** *(L16)* [KEEP]
    - 1. Institutional know-how: SOPs, playbooks, training docs, captured expertise.
    - 2. Not the raw log — the interpretation of it.
    - 3. Mid-market companies have partial Systems of Knowledge at best.
- D. **Systems of Semantics** *(L18)* [KEEP, with canonical agent definition preserved]
    - 1. Relationships and meaning. Ontologies, embeddings, knowledge graphs.
    - 2. The structures that let an AI model know "client A" in CRM = "Account 0042" in ERP, both covered by a pricing exception on Elena's desktop.
    - 3. The layer most companies don't yet have.
    - 4. Without it, an agent can retrieve data but can't reason across it.
    - 5. [KEEP] Canonical agent definition at first use (`book-ultm`) — already landed at L18 per Phase 3B.
- E. **The HBR scaffolding** *(L20-22)* [CUT — heaviest cut in chapter]
    - 1. [CUT] Argenti "ground truth" block-quote *(L20)*.
    - 2. [CUT] Sadun "well-integrated with specific use case" *(L20)*.
    - 3. [CUT] AWS "lack the contextual awareness..." *(L22)*.
    - 4. **HBR count check:** target = 0-1 citations in Ch 6. If author wants the data-is-ground-truth framing kept, the cleanest move is one Argenti sentence with parenthetical attribution (not block-quote). // AUTHOR REVIEW: zero HBR citations is also clean — Ch 2 keeps the Argenti banker scene, so this chapter can carry its own claim.
- F. **Source's job** *(L24)* [KEEP]
    - 1. Source doesn't *build* Systems of Semantics. That's Design and Build.
    - 2. Source names what layer each piece of knowledge currently lives in.
    - 3. Tells Design exactly what exists and what has to be built.

### IV. Julie M&A example *(L34)* [KEEP]

- **Assumes:** reader knows the three layers, knows Source's job is to name what layer each piece of knowledge lives in.
- **Establishes:** the same three-layer gap is visible outside AI — Julie's post-acquisition integration work surfaced 20 years of process-expert institutional memory that existed nowhere in any system. The principle is the same: name what would stop working if this person were not here tomorrow.
- **Sets up:** the urgency of §V — diagnosis isn't done until the mapping is complete; the M&A parallel shows what acting before mapping costs.

- A. Same gap surfaces in M&A integration work, outside any AI context.
- B. Acquired division at global food safety company. Inherited assets included process experts with 20 years of institutional memory existing nowhere in any system.
- C. Julie's standing question: *if this person were not here tomorrow, what would stop working?*
- D. **Function:** the non-AI parallel. Source closes that gap before it becomes a Sprint failure.

### V. Diagnosis isn't done until you know what you have + TML *(currently L38-50 — [COMPRESS] from two sections into one tight paragraph)*

  **Heading (proposed, directive):** "You Aren't Done with Diagnosis Until You Know What You Have."

- **Assumes:** reader has the three-layer frame (where knowledge lives) and has seen the M&A parallel. The temptation now is to act — to move from constraint to solution without inventorying first.
- **Establishes:** the second lens — TML (Task / Management / Leadership) — runs orthogonal to the three-layer frame. Three-layer = WHERE knowledge lives. TML = WHAT the knowledge lets someone do. AI handles Task; assists with Management; requires human oversight on Leadership. Together the two lenses are why Source belongs in Diagnose, not Execute. Until you've mapped what you have along both axes, the constraint is a named problem without a buildable path. Closes with the one inline PIS sentence (Source = Identify between Problem and Solution).
- **Sets up:** the Knowledge Map (§VII), which is the artifact that captures the inventory the two lenses describe. Also sets up Ch 7b's role-by-role TML application — same framework, different scope.

- A. **The temptation to act** *(L40)* [KEEP, tightened]
    - 1. End of Signal, the constraint is named and the team wants to move: hire, buy, build.
    - 2. Acting before you know what you have wastes the spend.

- B. **TML framework — [COMPRESS] from 3 paragraphs (L44-48) to one paragraph**
    - 1. Three-layer = WHERE knowledge lives. TML = WHAT it lets you do.
    - 2. **Task knowledge:** documented steps, SOPs. Easiest to capture. AI handles directly.
    - 3. **Management knowledge:** decision rights, escalation paths. Partially documented. AI assists.
    - 4. **Leadership knowledge:** judgment, relationships, pattern recognition. Almost never documented. Requires human oversight at every step.
    - 5. **Forward link:** same framework returns in Chapter 7b for role-by-role work decomposition.
    - 6. [TRIM] Cut the "each layer requires a different capture and transfer approach" sentence as redundant with Task/Management/Leadership capture-friction implied above.

- C. **Why Source belongs in Diagnose** *(L50)* [KEEP one sentence]
    - 1. Until you've mapped what you have, the constraint is a named problem without a buildable path.

### VI. PIS framework *(currently L52-58, full section)* [COMPRESS to one sentence]

- **Assumes:** reader has accepted that diagnosis isn't done until you know what you have (from §V) and is wondering what discipline enforces "don't move to solution yet."
- **Establishes:** Source = Identify between Problem (Signal) and Solution (Design and Build). The discipline is the Compound Sequence itself; PIS is not a third taxonomy on top of three-layer + TML — it's the same sequencing rule named once and folded in.
- **Sets up:** the Knowledge Map (§VII) as the artifact that proves Identify is complete; the section heading goes away, the one sentence lands inline.

**Placement decision (forces resolution of an old ambiguity):** the one PIS sentence folds into the closing of §V — *"Source is the Identify phase between Signal's Problem and Design's Solution; don't move to solution until identification is complete."* — rather than the opening of §VII. Rationale: §V is the diagnosis-completion section; PIS is the sequencing rule that defines completion. §VII opens cleanly on the Knowledge Map artifact without re-stating the sequencing rule.

- A. **[CUT] section heading.** PIS is not a third taxonomy — it's a sequencing principle.
- B. **Replacement (one sentence, inline):** *"Source is the Identify phase between Signal's Problem and Design's Solution; don't move to solution until identification is complete."*
- C. **Placement:** fold the one sentence into the closing of Section V (Diagnosis paragraph) or the opening of Section VII (Knowledge Map).
- D. [CUT] L54-58 supporting prose ("PIS sequencing discipline enforces..." through "inventory for a problem you don't have"). The Compound Sequence already enforces this; PIS as a named framework adds a third taxonomy on top of three-layer + TML and is the single biggest contributor to FLOW#2 Simplicity Fail.

### VII. Create the Knowledge Map *(currently L60-78)* [KEEP, with artifact placement made explicit]

  **Heading (proposed, directive):** "Build the One-Page Knowledge Map."

- **Assumes:** reader knows Source is the Identify phase between Problem and Solution (folded in at the end of §V). They believe the inventory has to happen and they're ready to see what the artifact looks like.
- **Establishes:** the deliverable — a six-column table (Source · Type · Owner · Status · Pipeline · Notes), one row per source, one page total. Digital systems, people, and gaps all appear as rows in the same table because a workflow consumes all of them the same way. Scoping discipline: one Sprint, one constraint, one map. The test: could someone who wasn't in the room use this to architect against the constraint? Blank template lives in-body at ~L301.
- **Sets up:** the three-pass build (§VIII) — Digital, Organic, Missing — which is the method for populating the six columns row by row.

- A. **The deliverable** *(L62)* [KEEP]
    - 1. Structured inventory of every information source relevant to the validated constraint.
    - 2. Six columns: **Source, Type, Owner, Status, Pipeline, Notes.**
    - 3. One row per source. Fits on one page.
    - 4. Digital systems, people, and gaps all appear as rows in the same table.

- B. **Scoping discipline** *(L66)* [KEEP]
    - 1. One Sprint, one constraint, one map.
    - 2. Quoting cycle = pricing rules, historical quotes, exception handling, customer-specific terms. NOT HR records, NOT marketing analytics.
    - 3. Over multiple Sprints, the maps accumulate into a broader picture.

- C. **The test** *(L68)* [KEEP]
    - 1. Could someone who wasn't in the room use this map to architect a workflow against the constraint?
    - 2. PM coordinator example: the map cataloged what she touched, what she decided, what would break if she disappeared.

- D. **ARTIFACT — blank Knowledge Map template** [NEW in-body, per consolidated artifact bead]
    - 1. **Where:** added at ~L301 by Phase 3B.
    - 2. **Format:** 6-column fillable table (Source · Type · Owner · Status · Pipeline · Notes) with empty rows and a one-line legend explaining the column controlled vocabularies (Type: Digital / Organic / Missing; Status: Clean / Needs Work / Missing; Pipeline: Connected / Manual / Broken).
    - 3. **Drafter action:** call out the in-body template in the prose; the table itself is Phase 3B's job to insert.

- E. **Pro Tip** *(L72-74)* [KEEP]
    - 1. "If your Source output doesn't fit on one page, it's not scoped to the constraint. You've drifted into a general data audit. Cut it back down."

- F. **The setup paragraph** *(L79)* [KEEP]
    - 1. Start with the Constraint Statement.
    - 2. Six columns. First four = Knowledge Map. Fifth (Pipeline) = Data Pipeline Audit. Run them together.
    - 3. Three passes follow.

### VIII. Three-pass build *(currently L81-113)* [KEEP, with people-don't-have-APIs content [MERGED] in]

  **Heading (proposed, directive):** "Build the Map in Three Passes."

- **Assumes:** reader has the deliverable in their head (six columns, one row per source, one page) and the scoping discipline (one constraint). They're ready for the method.
- **Establishes:** the method has three passes, each adding a kind of row to the same map — Digital, Organic, Missing. The three passes together populate the table. The "People don't have APIs" Digital / Organic / At-risk taxonomy folds in as part of Pass 1 / Pass 2 / Pass 2-subcategory; the old §IX standalone section disappears.
- **Sets up:** §IX Meridian — the worked example showing the three passes running live in one company. Reader sees the method, then sees the method applied to Elena, Mark, Ty, and Dave.

**Per-pass triads (the Drafter's coherence work hinges on these — see [[chapter-syllogism-and-flow-markers]] on context drift across reorganized sub-sections):**

- A. **Pass 1 — Digital Sources** *(L81-88)* [KEEP]

    - **Assumes:** reader has six columns drawn on a blank page and the Constraint Statement from Signal at the top.
    - **Establishes:** the first pass populates the rows with named digital sources — CRM, process logs, shared drives, inboxes, spreadsheets. Each row carries Type=Digital, Owner, Status (Clean / Needs Work / Missing), and Pipeline status (Connected / Manual / Broken) answered against the four Pipeline Audit questions. The "digital sources are the smallest part of the actual information environment" framing folds in here (one sentence) as the bridge to Pass 2. *(// AUTHOR REVIEW: drafter discretion whether to include this framing or let Pass 2/3 carry the implicit contrast.)*
    - **Sets up:** Pass 2 — most of what makes the work run isn't in any of the digital sources just enumerated. The people who run the work are the next set of rows.

    - 1. **What:** every digital source touching the constraint — CRM, process logs, shared drives, inboxes, spreadsheets.
    - 2. **Method:** name each source · mark Digital · name owner · status (Clean / Needs Work / Missing).
    - 3. **Pipeline Audit (4 questions):**
        - a. Does this source connect to other systems that touch the constraint, or does data move by manual export?
        - b. Can a workflow read from it directly, or does someone export and re-enter?
        - c. Who owns the handoff: person, scheduled job, nobody?
        - d. When was the data last verified?
    - 4. **Pipeline status:** Connected · Manual · Broken.
    - 5. [KEEP] Action Step at L86-88.
    - 6. [MERGE from current L182-184] The "Digital sources are the smallest part of the actual information environment" framing — fold the one useful sentence into the closing of Pass 1, then cut the standalone section. // AUTHOR REVIEW: drafter discretion whether to include the framing or just let Pass 2/3 carry the implicit contrast.

- B. **Pass 2 — Organic Sources (People)** *(L90-97)* [KEEP, [MERGE] At-risk subcategory in]

    - **Assumes:** reader has the digital rows on the map and has just been told most of what makes the work run isn't in any of them.
    - **Establishes:** people are sources in the formal sense — named, located, described, on the same table as the digital rows. Each carries Type=Organic, names what they know that isn't documented anywhere, and is assessed for at-risk status (planned exit, retirement, role change, reorg). The pricing-strategist example from the global food safety company folds in here as the worked at-risk case — 20 years of customer-specific pricing exceptions captured in four weeks before retirement, prevented a two-year reconstruction.
    - **Sets up:** Pass 3 — the rows on the map so far describe what exists. The highest-leverage column is what's *missing.*

    - 1. **What:** every person whose judgment the constraint workflow depends on.
    - 2. **Method:** name them · name what they know that isn't documented · assess at-risk status · be specific.
    - 3. **Example:** not "she knows the quoting process" but "she knows the three pricing exceptions for legacy customers that override the rate card."
    - 4. [MERGE from current L190-196] **At-risk subcategory** — institutional knowledge in one person's head about to leave through planned exit, retirement, role change, or reorg. Cost is invisible until it's gone.
    - 5. [MERGE from current L194] **The pricing strategist example** — global food safety company. 20 years of customer-specific pricing exceptions, never consolidated. Identified through Source, four weeks to capture before retirement. Prevented a 2-year reconstruction.
    - 6. [KEEP] Action Step at L94-96.
    - 7. [CUT] L198 dangling "developer left" sentence — references a story (the Preface developer) not present in this chapter. Drafter cuts the orphan reference.

- C. **Pass 3 — Missing Sources** *(L99-109)* [KEEP]

    - **Assumes:** reader has Digital and Organic rows on the map. They can see what exists. The next question is what *should* exist that doesn't.
    - **Establishes:** Missing is the highest-leverage column — questions a designer would ask that current sources can't answer, decisions made by gut that should be made by data. Every Missing row carries what type it should be (digital, documented process, captured expertise) and what creation requires. TML overlay: Missing rows cluster in Management (decisions by departed leaders) and Leadership (uncaptured market intelligence); Task gaps are usually documentation gaps, not knowledge loss.
    - **Sets up:** the close of §VIII (one page, one constraint, everything relevant) which directly hands into §IX — Meridian, where all three passes ran live in one company.

    - 1. **What:** what's absent. Questions a designer would ask that current sources can't answer. Decisions made by gut that should be made by data.
    - 2. **Method:** add Missing rows · note what type they should be (digital, documented process, captured expertise) · note what creation requires.
    - 3. **Why Missing is the highest-leverage column:** highest-risk gaps live here.
    - 4. **TML overlay** *(L103)* — Missing cluster in Management (decisions by departed leaders) and Leadership (uncaptured market intelligence) knowledge categories. Task gaps are usually documentation gaps; Management/Leadership gaps are knowledge loss.
    - 5. [KEEP] Action Step at L106-108.

- D. **Closing of three passes** *(L111)* [KEEP]
    - 1. One page, one constraint, everything relevant.
    - 2. If a row doesn't connect, it doesn't belong.

- E. **[CUT entire section: L178-198 "People don't have APIs"]**
    - 1. Reason: the Digital / Organic / At-risk taxonomy already appeared as Pass 1 / Pass 2 / (Pass 2 sub-category) above.
    - 2. The only new content was the at-risk subcategory (merged into Pass 2 above) and the broken developer callback (cut).
    - 3. Drafter deletes the H2 and its three H3s.

### IX. Source at Meridian *(currently L219-231 — [MOVE] up; was at ~70% through chapter, now lands right after Pass 3)*

  **Heading (proposed, directive):** "Source at Meridian." *(Promote from H3 to H2.)*

- **Assumes:** reader has just finished the three-pass method (§VIII). They know what Digital, Organic, and Missing rows are, they have the six-column structure in their head, and they're now asking: *what does this look like when a real team runs the three passes against a real constraint?* Meridian's earlier appearance is structurally required by what §VIII just established — the three-pass method without a worked example is procedure without proof.
- **Establishes:** Elena's Thursday afternoon session — one question (*when an RFQ hits my inbox, what do I actually do?*), 45-minute answer, three people in the room (Mark, Ty, Dave), and the Knowledge Map that emerged. HubSpot CRM (Connected, win/loss not linked to quotes); JobBOSS ERP (Connected, never queried for quoting); Customer Notes.xlsx (Broken, on Elena's desktop); Elena (Organic, at-risk, only person who reconciles); Dave (Organic, at-risk, four years to retirement). The session produced the map Design needed. Without it, the team would have built against assumptions.
- **Sets up:** §X (Classify what you found) — once the map is built, each source has to be classified along Structured/Unstructured, Durable/Ephemeral, and AI Tier. Meridian's map is the worked input to that classification work.

- A. **The session** *(L223)* [KEEP]
    - 1. Elena clears Thursday afternoon. Sits down with Mark, Ty, Dave.
    - 2. One question: *when an RFQ hits my inbox, what do I actually do?*

- B. **Elena's 45-minute answer** *(L225)* [KEEP]
    - 1. Cross-references customer history, material requirements, labor estimates simultaneously.
    - 2. Pulls "Customer Notes.xlsx" off her desktop. 147 rows of pricing exceptions. Never shared, backed up, or version-controlled.

- C. **Dave's piece** *(L227)* [KEEP]
    - 1. 31 years of fabrication experience compressed into gut-feel hour estimates, accurate within 10% on standard work.
    - 2. Can't estimate materials cost. No customer-specific pricing. No access to ERP job costing.

- D. **Ty's piece** *(L227)* [KEEP]
    - 1. Forwards RFQs to Elena and waits. Zero visibility into where a quote stands.

- E. **The Knowledge Map that emerged** *(L229)* [KEEP]
    - 1. HubSpot CRM: Connected, but win/loss records not linked to quotes.
    - 2. JobBOSS ERP: Connected to invoicing, but nobody queried it for quoting.
    - 3. Customer Notes.xlsx: Broken, Elena's desktop, no sync.
    - 4. Elena: Organic, at-risk, only person who can reconcile all sources.
    - 5. Dave: Organic, at-risk, four years to retirement with undocumented estimation.

- F. **The point** *(L231)* [KEEP]
    - 1. That single session produced the map Design needed.
    - 2. Without it, the team would have built agents against assumptions about what Elena did.
    - 3. **Source gives you the second starting point.**

- G. **ARTIFACT — Elena's Knowledge Map (Excalidraw L221)** [KEEP at top of section]

### X. Classify what you found *(currently L115-147)* [KEEP, with AI Tier section [REVISED]]

  **Heading (proposed, directive):** "Classify What You Found."

- **Assumes:** reader has a populated Knowledge Map in their head — they've seen Elena's six-column table at Meridian. They know what rows look like. What they don't yet know is how each row gets handed to Design.
- **Establishes:** each source on the map gets classified along two axes — Structured vs. Unstructured (does AI use it directly or reason against it) and Durable vs. Ephemeral (only durable belongs on the map; 90-day test) — and one tier system. The tier system uses case-study vocabulary: **Tier 1** (AI can use directly, structured/API-accessible), **Tier 2** (AI can process with an extraction pipeline, unstructured but capturable), **Tier 3** (human judgment required, not AI-accessible today), **Not AI-tier** (stays human, queried in real time, ephemeral or judgment-bound). The classification tells Design what's reachable now, what's reachable with extraction work, and what stays human.
- **Sets up:** §XI (How systems talk to each other) — the AI Tier and Pipeline classifications make sense only if the reader knows what APIs, MCPs, and connectors are. The next section defines them.

- A. **Setup** *(L117)* [KEEP]
    - 1. Once the map is built, classify each source along two axes and one tier system.

- B. **Structured vs. Unstructured** *(L119-121)* [KEEP]
    - 1. Structured: database fields, tagged articles, CRM records, defined columns. AI uses directly, cheaply, fast.
    - 2. Unstructured: emails, transcripts, PDFs, Slack threads. AI can reason against it — slower, more tokens.
    - 3. **The point:** not to structure everything. Be deliberate about what gets structured, what stays prose, what gets light structure layered on.
    - 4. [KEEP] Token definition at L121 (parenthetical: "the units of text AI is priced and limited by, roughly three-quarters of a word each").

- C. **Durable vs. Ephemeral** *(L123-125)* [KEEP]
    - 1. Durable: brand guidelines, pricing rules, SOPs, regulatory.
    - 2. Ephemeral: this week's to-do, meeting notes, first-pass drafts.
    - 3. Only durable belongs on the Knowledge Map. 90-day test.

- D. **AI Tiers** *(L127-147)* [REVISE — adopt case-study vocabulary]
    - 1. **[CUT current 3-tier scheme]:** standing context / retrieved / historical.
    - 2. **[NEW] 4-tier scheme matching `case-study-meridian.qmd` L141-150 and `case-study-pm-agent-team.qmd` L76-86:**
        - a. **Tier 1:** AI can use directly (structured, API-accessible). Any structured source the AI can query in real time.
        - b. **Tier 2:** AI can process with an extraction pipeline (unstructured but capturable — PDFs, transcripts, documents).
        - c. **Tier 3:** Human judgment required (not AI-accessible at all today).
        - d. **Not AI-tier:** Stays human. Queried in real time. Ephemeral or judgment-bound work.
    - 3. **For each source on the map, mark which tier it falls into.** This classification directly informs Design.
    - 4. **ARTIFACT — AI Tier classification table [NEW]** — flagged for Drafter to add a small reference table inline: *Tier · What AI Can Do · Example.* Placement: directly under the four-tier definitions. // AUTHOR REVIEW: confirm the four-tier vocabulary matches the case studies *after* Drafter completes; cross-coherence pass against both case-study files mandatory.
    - 5. **Update Pro Tip** *(L138-140)* [REVISE] — current "treats everything as equally current" framing still works; refresh language to reference Tier 1/2/3 directly. *"An AI workflow that mixes Tier 1 truth with Tier 3 archive will confidently cite your 2019 pricing. The tiers prevent it."*
    - 6. [KEEP] Action Step at L144-146, rewritten to point at the four-tier vocabulary.

### XI. How systems talk to each other *(currently L149-176)* [KEEP — serves `book-xqxi` cross-cutting goal]

  **Heading (proposed, directive):** "How Systems Talk to Each Other."

- **Assumes:** reader has classified every source by tier (§X) and is staring at Pipeline column values — Connected, Manual, Broken — without yet knowing what makes a pipeline Connected.
- **Establishes:** plain-language definitions of three terms — **APIs** (how systems talk to systems), **MCPs** (how AI talks to systems), **Connectors** (pre-built integrations; the most common thing companies buy before doing Source work). The Pipeline column becomes operational: Connected = an API/MCP/connector carries the data; Manual = a person carries it; Broken = it doesn't move at all.
- **Sets up:** §XII (Transcripts) — once the reader has the systems-talking-to-systems vocabulary, the natural next question is how a *person* gets close to that vocabulary. The answer is the transcript.

- A. **Setup** *(L151)* [KEEP]
    - 1. If you're mapping where knowledge lives, you need to understand how it moves.
    - 2. Three terms come up constantly. Define in plain language.

- B. **APIs** *(L153-155)* [KEEP] — application programming interfaces. How systems talk to systems.

- C. **MCPs** *(L157-159)* [KEEP] — model context protocols. How AI talks to your systems. Without MCP, an AI model only knows what you paste into the prompt.

- D. **Connectors** *(L161-163)* [KEEP] — pre-built integrations. Zapier, Make, n8n. Most common thing companies buy before doing Source work.

- E. **Terminology note callout** *(L166-169)* [KEEP] — different platforms, same idea (MCP / tools / integrations / actions).

- F. **The Pipeline column made operational** *(L171)* [KEEP] — Connected / Manual / Broken defined against APIs / MCPs / Connectors.

- G. **Pro Tip** *(L173-176)* [KEEP] — "you don't need to understand the engineering; you need to know whether a person is carrying data."

- H. **Cross-cutting bead note:** `book-xqxi` 3B sweep handles parenthetical first-use jargon definitions across the rest of the book. Drafter does not expand this section.

### XII. Transcripts as the closest thing to an API *(currently L200-217)* [KEEP]

  **Heading (proposed, directive):** "A Transcript Is the Closest Thing a Person Has to an API."

- **Assumes:** reader has the API / MCP / connector vocabulary in their head (§XI) and is sitting with the at-risk organic rows on their own map, asking what extraction looks like for a person.
- **Establishes:** people don't have APIs but you can make them transcripts. Typing compresses; speech-to-text doesn't. A well-structured transcript becomes raw material AI can reference, retrieve, and reason against. The practical move: when the map flags an organic source as at-risk, the first action is a structured interview with three questions — *What decisions do you make that nobody else makes? Which exceptions have you handled that aren't written down? What rule of thumb do you use that you've never had to explain?*
- **Sets up:** §XIII (Knowledge management as infrastructure) — once the reader knows extraction can run, the next question is who keeps the captured knowledge clean and current after Source ends.

- A. **The claim** *(L202)* [KEEP]
    - 1. People don't have APIs. You can make them transcripts.

- B. **Why typing loses information** *(L204)* [KEEP]
    - 1. Forms compress. People edit as they go. Data entry is lossy.
    - 2. Sit them down, ask the right questions, record what they say → judgment and qualifiers survive.

- C. **Why speech-to-text changes the math** *(L206)* [KEEP]
    - 1. Humans evolved voice over 100Ks of years.
    - 2. As speech-to-text drops to zero, talking is cheaper than typing in both time and information quality.

- D. **What a well-structured transcript becomes** *(L208)* [KEEP]
    - 1. Raw material AI can reference, retrieve, reason against.
    - 2. Examples: ops lead's exception handling, salesperson's terms logic, engineer's estimation logic.
    - 3. The transcript makes the judgment available when the person isn't in the room.

- E. **The practical move** *(L210)* [KEEP]
    - 1. When the Knowledge Map flags an organic source as at-risk → first action is a structured interview.
    - 2. **The three questions:** What decisions do you make that nobody else makes? Which exceptions have you handled that aren't written down? What rule of thumb do you use that you've never had to explain?

- F. **Action Step** *(L214-217)* [KEEP] — identify highest-risk organic source, schedule structured interview this week, record, transcribe, add to map.

### XIII. Knowledge management as infrastructure *(currently L233-256, two near-duplicate sections)* [COLLAPSE into one]

  **Heading (proposed, directive):** "Treat Knowledge Management as Infrastructure."

- **Assumes:** reader has the Knowledge Map, the classification, the API/MCP vocabulary, and the transcript move. They know Source produces a clean artifact for one constraint. The unasked question: what happens after this Sprint ends?
- **Establishes:** knowledge management is the foundation under every Sprint. Default state (shared drive organized once a year, wiki that rots, tribal knowledge that walks out) was tolerable when humans were the only consumers. Agents don't compensate for messy knowledge bases — they treat every accessible piece as equally valid unless told otherwise. Context engineering is downstream of knowledge management. Treat it as a budget line, a named owner, a regular review cadence — infrastructure, not a project.
- **Sets up:** §XIV (the knowledge manager role) — the named owner the infrastructure framing just demanded.

- A. **[CUT entire section L233-242 "Knowledge management in an agentic world"]**
    - 1. Reason: near-duplicate of L244-256. Both sections argue that knowledge management was tolerable when humans were the consumers and isn't anymore.
    - 2. Salvage: one sentence on agents treating every accessible piece of information as equally valid unless told otherwise — fold into the consolidated section's opening.

- B. **[KEEP, expanded] Section based on L244-256** "Knowledge management is the foundation"
    - 1. **The default state** *(L246)* — shared drive organized once a year. Wiki that rots. Tribal knowledge that walks out with one person.
    - 2. **Why it doesn't work anymore** *(L248-252)* — every claim in this book about what AI can do depends on the knowledge it can reach. Clean → operates like a well-briefed employee. Dirty → confidently, plausibly, wrong.
    - 3. **The compounding effect** *(L252)* — human handed bad info slows down. Agent handed bad info executes at scale, in parallel, every time you ask.
    - 4. **Context engineering as downstream** *(L254)* [KEEP] — context engineering is downstream of knowledge management. Can't engineer context out of a knowledge base that hasn't been curated.
    - 5. **The infrastructure framing** *(L256)* — budget line, named owner, regular review cadence. Sprints get cheaper after the first one if the Knowledge Map already exists for the next constraint's neighborhood.

- C. **[NEW one-sentence salvage from cut section]:** insert at top of consolidated section — *"Humans compensate for messy knowledge bases. Agents don't — they treat every accessible piece of information as equally valid unless told otherwise."*

### XIV. The knowledge manager role *(currently L258-266)* [KEEP as H3 under the consolidated KM section]

  **Heading (proposed, directive):** "Name a Knowledge Manager."

- **Assumes:** reader believes knowledge management is infrastructure (from §XIII) and is asking who owns it.
- **Establishes:** the working term — *knowledge manager* — and the job: curate institutional knowledge across Sprints; decide what gets captured, retired, restructured, connected to which agent. Relationship to the Human Orchestrator (Ch 7): Orchestrator runs goals inside a Sprint; knowledge manager works underneath every Sprint, keeping inputs clean.
- **Sets up:** §XV (Garbage in, garbage out) — the lived consequences of *not* naming this role, told as the Compound story and the client mirror.

- A. **The gap** *(L260)* [KEEP]
    - 1. Most companies don't have anyone whose job this is.
    - 2. Shared drive owned by whoever set it up. Wiki owned by whoever last cared. What's current vs. archived owned by nobody.

- B. **The role** *(L262)* [KEEP]
    - 1. Working term: *knowledge manager.*
    - 2. Curates institutional knowledge: what gets captured, retired, restructured, connected to which agent.
    - 3. Accountable for whether the knowledge base reflects how the business actually operates today.

- C. **Relationship to Human Orchestrator** *(L264)* [KEEP]
    - 1. Human Orchestrator (Ch 7) sets goals for an agent team inside a single Sprint.
    - 2. Knowledge manager works underneath every Sprint, keeping inputs clean, current, reachable.
    - 3. Orchestrator outcomes are only as good as the knowledge a knowledge manager made clear.

- D. **Closing** *(L266)* [KEEP] — companies that introduce this role early run Sprints against knowledge they can trust.

### XV. Garbage in, garbage out *(currently L268-279)* [KEEP]

  **Heading (proposed, directive):** "Garbage In, Garbage Out."

- **Assumes:** reader believes a knowledge manager owns the infrastructure. The next question: what does the *absence* of that role actually cost?
- **Establishes:** the Compound first-person story (agents kept surfacing wrong info because current and expired were indexed together) and the client mirror (same pattern, same root cause). The AI was doing what it was designed to do; nobody had done Source first. Names Source's boundary — Source identifies the gaps, Design decides how to fill them. Confusing the two phases is how Source bloats into a year-long data project.
- **Sets up:** §XVI (the completeness test) — the discipline that prevents Source bloat by giving the reader an 8-item gate before handoff.

- A. **The principle** *(L268-269)* [KEEP] — foundational principle of Source work. Company data is a massive asset *if* you can get it into a format AI can actually use.

- B. **The Compound story** *(L271-273)* [KEEP]
    - 1. Early on, weren't clear about taxonomies, knowledge hygiene, or vectorization.
    - 2. Agents kept surfacing wrong info. Old pricing, deprecated processes, policies superseded two revisions back.
    - 3. Took more iterations than they want to admit before asking the right question: *why does it keep showing old information?*
    - 4. Answer: everything indexed together. Current and expired side by side, no distinction.
    - 5. [KEEP] Inline parenthetical definitions for taxonomies / knowledge hygiene / vectorization (`book-xqxi` 3B sweep handles refinement).

- C. **The client mirror** *(L275)* [KEEP] — same pattern at a client site. Application against internal knowledge base kept surfacing expired info. Same root cause.

- D. **The verdict** *(L277)* [KEEP] — AI was doing exactly what it was designed to do. Nobody had done Source work first.

- E. **Source's boundary** *(L279)* [KEEP]
    - 1. Source isn't where data infrastructure gets built.
    - 2. Source names the gaps. Filling them is a Design decision.
    - 3. Confusing the two is how Source bloats into a year-long data project that never ships a workflow.

### XVI. The completeness test *(currently L281-297)* [KEEP — strong in-body fillable checklist]

  **Heading (proposed, directive):** "Run the Completeness Test Before You Hand Off."

- **Assumes:** reader has a populated map, classified rows, vocabulary for systems and people, and the discipline to keep Source from bloating. They need to know when Source is *done.*
- **Establishes:** eight checks — Architect, Constraint scope, Layer, TML, Pipeline, At-risk, Gap, One-page. Each check maps to one of the lenses already introduced (three-layer at the Layer test; TML at the TML test; the three-pass build at Pipeline / At-risk / Gap; the Knowledge Map artifact at One-page).
- **Sets up:** §XVII (the artifacts — blank template + Meridian's completed map) and §XVIII (the handoff to Design). The completeness test is the gate; the artifacts are what gets handed across the gate.

- A. **Setup** *(L283)* [KEEP] — before you call Source done, run eight checks.

- B. **The 8-item checklist** [KEEP all 8, with item 3 and 4 wording refreshed to match upstream framework presentations]
    - 1. **Architect test** — Could someone who wasn't in the room use this map to know what they're designing against: data, location, gaps, risks?
    - 2. **Constraint scope test** — Every row connects to the constraint. If a row doesn't, cut it.
    - 3. **Layer test** — Every row classified by information layer: System of Record / Knowledge / Semantics. If all rows are Record and none are Knowledge or Semantics, you did a data audit, not Source.
    - 4. **TML test** — Every row classified by TML type: Task / Management / Leadership. Informs how Design handles capture and transfer.
    - 5. **Pipeline test** — Every digital source has a Pipeline status: Connected / Manual / Broken. No blanks.
    - 6. **At-risk test** — You explicitly asked: who is a single point of failure? Answer on the map.
    - 7. **Gap test** — Missing column isn't empty. Zero missing means you didn't look hard.
    - 8. **One-page test** — Map fits on one page. If it doesn't, you drifted from the constraint.

- C. **Action Step** *(L294-296)* [KEEP] — run the eight checks, fix gaps, place Constraint Statement above and Knowledge Map below on one page. That page is what you hand to Design.

### XVII. ARTIFACTS — Knowledge Map blank template + Meridian completed Knowledge Map *(currently L301-322)*

- **Assumes:** reader has the eight-item completeness test fresh in their head and is ready to see what a passing artifact looks like — both blank (for their own work) and worked (Meridian, the canonical example).
- **Establishes:** two artifacts on the page — (1) the blank six-column template for the reader to copy; (2) Meridian's seven-row completed Knowledge Map populated against the quoting constraint. The Meridian table reads back to itself in prose: two at-risk organic sources, one broken spreadsheet on Elena's desktop, two pieces of Missing information that are exactly the inputs Design will need.
- **Sets up:** §XVIII (Hand off to Design) — the artifacts are what gets handed; the next section is the language of the handoff.

- A. **Blank Knowledge Map template** *(L301-309)* [KEEP] — added by Phase 3B at ~L301. Six columns. Sample legend row. // AUTHOR REVIEW: Phase 3B inserts the table; Drafter's job is to ensure the prose introduces and follows up on it.

- B. **Closing instruction** *(L310)* [KEEP] — one row per source, flag at-risk organic sources with **AT RISK** in Notes, if it runs longer than one page you drifted.

- C. **Meridian's completed Knowledge Map** *(L312-322)* [KEEP — the chapter's best in-body artifact]
    - 1. Seven-row in-body table populated against the Meridian quoting constraint.
    - 2. HubSpot CRM, JobBOSS ERP, Customer Notes.xlsx, Elena, Dave, Historical quote-to-actual accuracy (Missing), Customer segment profitability (Missing).
    - 3. [KEEP] The L324 closing paragraph that reads the map back to the reader — "two organic sources flagged at risk... two pieces of information that don't exist yet are the exact inputs the team would need to decide whether an agent-assisted quoting workflow is viable."

### XVIII. Hand off to Design *(currently L326-332)* [KEEP, tighten]

  **Heading (proposed, directive):** "Hand Constraint Plus Map to Design."

- **Assumes:** reader has a passing artifact in hand (or has the blank template and the Meridian worked example to follow).
- **Establishes:** the handoff — two things on one sheet of paper: the Constraint Statement from Signal + the Knowledge Map. Assets, flow, gaps, at-risk dependencies, and tier of each — all visible together. Source is the bridge between Diagnose and Execute.
- **Sets up:** Chapter 7 — ownership decisions, the Hybrid Accountability Chart entry for this Sprint, and the crossing into Execute.

- A. **The handoff** *(L328)* [KEEP] — two things on one sheet: the constraint Signal validated + the Knowledge Map. Assets, flow, and gaps together.

- B. **The transition** *(L332)* [KEEP, tighten] — Source is the bridge. Last thing you do before you start to design.

- C. **Closing sentence (proposed tighten):** *"Constraint plus map is the input Design needs. Bring both to Chapter 7."*

### XIX. Reflection Questions *(L334-339)* [TRIM from 4 → 3]

- **Assumes:** reader has finished the chapter, knows Constraint plus Map is the input for Design.
- **Establishes:** three (or four — see Q3 decision) reflective prompts for the leadership team's working session. Each prompt maps to a specific section's frame — Q1 → §VIII three-pass build; Q2 → §VIII Pass 2 + §XII transcripts; Q4 → §X classification axes.
- **Sets up:** the team conversation that gets the leadership group aligned before they sit down to actually build the Knowledge Map.

- A. **Q1 (Knowledge Map build)** [KEEP] — first-pass Knowledge Map for top constraint. Connected vs. Manual vs. Broken ratio. What does it tell you about design work ahead?
- B. **Q2 (Organic single point of failure)** [KEEP] — who on your map is an organic source? Single point of failure? If they left tomorrow, what breaks first?
- C. **Q3 (developer chute callback)** *(L338)* [CUT or REVISE] — references "the developer who walked out with everything he knew." That story is in the Preface, not in this chapter (the L198 reference was already cut). // AUTHOR REVIEW: either (a) restore a one-sentence callback to the Preface developer story in §XII Transcripts, then keep this question, or (b) cut Q3 entirely and let Q1/Q2/Q4 carry the reflection.
- D. **Q4 (structured vs. unstructured)** [KEEP] — share of structured vs. unstructured? Most valuable unstructured knowledge in the constraint workflow — what would it take to make it AI-usable?

### XX. Closing handoff line *(currently L332)* [REWRITE — see XVIII.C above]

- **Assumes:** reader has finished the chapter and the Reflection Questions.
- **Establishes:** the one-sentence forward link to Design — *"Constraint plus map is the input Design needs. Bring both to Chapter 7."*
- **Sets up:** Chapter 7 (Designing the System / Hybrid Accountability Chart) as the next phase. The artifact pair (Constraint + Map) is what Design starts with.

---

## Heading inventory — current → proposed (full set)

The current chapter heavily uses italic-fragment headings (`## Every organization runs on three *layers*.`). Italic-fragment style is a Compound voice tic — neither directive nor labels. Convert to directive language matching the rest of the book's Phase 3 standard.

| Current heading *(L#)* | Proposed directive heading |
|---|---|
| `# *Source*.` *(L1)* | `# Source: Map What the Organization Knows About the Constraint` |
| *(NEW opener H2 around current L26)* | `## Before You Decide What to Do, Map What She Actually Does.` |
| `## Every organization runs on three *layers*.` *(L8)* | `## Every Organization's Information Lives in Three Layers.` |
| `## Diagnosis is not done until you know what you *have*.` *(L38)* | `## You Aren't Done with Diagnosis Until You Know What You Have.` |
| `## Source is the *Identify* phase.` *(L52)* | *(SECTION CUT — PIS compressed to one inline sentence)* |
| `## Create a *Knowledge Map*.` *(L60)* | `## Build the One-Page Knowledge Map.` |
| `### Pass 1: *Digital*.` *(L81)* | `### Pass 1 — Digital Sources` |
| `### Pass 2: *Organic*.` *(L90)* | `### Pass 2 — Organic Sources (People)` |
| `### Pass 3: *Missing*.` *(L99)* | `### Pass 3 — Missing Sources` |
| *(NEW H2 after Pass 3 — Meridian promoted)* | `## Source at Meridian` *(was H3 at L219; promote)* |
| `## Classify what you *find*.` *(L115)* | `## Classify What You Found.` |
| `### Structured vs. *unstructured*.` *(L119)* | `### Structured vs. Unstructured` |
| `### Durable vs. *ephemeral*.` *(L123)* | `### Durable vs. Ephemeral` |
| `### AI *tiers*.` *(L127)* | `### Sort by AI Tier (1, 2, 3, or Not AI-Tier)` |
| `## How systems *talk to each other*.` *(L149)* | `## How Systems Talk to Each Other.` |
| `### *APIs*.` *(L153)* | `### APIs — How Systems Talk to Systems` |
| `### *MCPs*.` *(L157)* | `### MCPs — How AI Talks to Systems` |
| `### *Connectors*.` *(L161)* | `### Connectors — Pre-Built Integrations` |
| `## People don't have *APIs*.` *(L178)* | *(SECTION CUT — merged into Pass 1/2/3)* |
| `### *Digital* sources.` *(L182)* | *(merged into Pass 1)* |
| `### *Organic* sources.` *(L186)* | *(merged into Pass 2)* |
| `### *At-risk* sources.` *(L190)* | *(merged into Pass 2)* |
| `## Transcripts: the *closest thing* a person has to an API.` *(L200)* | `## A Transcript Is the Closest Thing a Person Has to an API.` |
| `### Sprint · Source at Meridian.` *(L219)* | *(MOVED — see "Source at Meridian" H2 above, right after Pass 3)* |
| `## Knowledge management in an *agentic* world.` *(L233)* | *(SECTION CUT — collapsed into next section; one sentence salvaged)* |
| `## Knowledge management is the *foundation*.` *(L244)* | `## Treat Knowledge Management as Infrastructure.` |
| `### The *knowledge manager*.` *(L258)* | `### Name a Knowledge Manager` |
| `## Garbage in, Garbage Out.` *(L268)* | `## Garbage In, Garbage Out.` |
| `## The *completeness test*.` *(L281)* | `## Run the Completeness Test Before You Hand Off.` |
| `## Hand off to *Design*.` *(L313)* | `## Hand Constraint Plus Map to Design.` |
| `## Reflection Questions` *(L321)* | `## Reflection Questions` *(conventional; keep)* |

---

## HBR citation discipline (this chapter)

**Current count:** 3 HBR citations in the opener alone (Argenti, Sadun, AWS at L20-22). Ch 6 Source is the second-worst HBR-scaffold offender in the main body after Ch 2.

**Trim plan (target: 0-1 citations):**
- **CUT:** Sadun "effective only to the extent" at L20. Already overused across chapters; same author cited in Ch 2 and Ch 1.
- **CUT:** AWS "lack the contextual awareness..." at L22. Author already flagged this for Ch 1 as advertorial; remove from Ch 6 too.
- **AUTHOR DECISION (open question #1):** Argenti "data is ground truth" at L20.
    - Option A: KEEP one sentence with parenthetical attribution (not block-quote).
    - Option B: CUT entirely. Ch 2 already keeps the Argenti banker scene; Ch 6 carries its own claim without citation.
    - **Recommend Option B** (cleaner) but flagging for explicit author sign-off. // AUTHOR REVIEW: confirm before Drafter dispatches.

---

## AI Tier terminology reconciliation (memory rule)

Currently L127-134 names three tiers: standing context / retrieved / historical. The case studies (`case-study-meridian.qmd` L141-150 and `case-study-pm-agent-team.qmd` L76-86) use **Tier 1 / Tier 2 / Tier 3 / Not AI-tier.**

**Rewrite L127-147 to adopt case-study vocabulary** (Tier 1 = structured/API-accessible; Tier 2 = unstructured but extractable; Tier 3 = human judgment required; Not AI-tier = ephemeral/queried in real time).

**ARTIFACT — small reference table [NEW]** inline at the AI Tier definitions (per §X.D.4 above): *Tier · What AI Can Do · Example.* So the reader sees classification as classification, not prose.

**Cross-coherence pass mandatory after Drafter:** verify final language against both case studies. If language drifts, case studies get updated to match the chapter, not the other way around (chapter is canonical).

---

## Meridian weave (FLOW#3 — `book-b8yy`) · audit per [[meridian-as-side-by-side-thread]]

**Audit verdict: Ch 6 Source is in the "strong Meridian presence" tier.** The Elena Knowledge Map at L301-309 is the canonical worked example for Source. The chapter already carries Meridian at three landing points (L77-81 PT clinic Excalidraw ref, Elena vignette L219-231, completed table L299-311). The original issue was **placement, not absence.**

**The move (preserved from the prior outline):** Elena vignette goes from L219 (~70% through the chapter) to **right after Pass 3 (current ~L113)** as §IX of the new structure. Reader sees the worked example BEFORE the classification, jargon-pass, transcripts, and knowledge-management sections.

**Structural inevitability check (new — per the upgraded triads above):** the §IX Meridian triad makes the earlier appearance feel structurally required, not editorially preferred. §VIII's *Sets up* explicitly hands to §IX ("the worked example showing the three passes running live in one company"); §IX's *Assumes* is the three-pass method the reader just finished; §IX's *Sets up* is the classification work that follows. The reader can't skip Meridian without breaking the chain — they need the worked map to classify in §X. **Meridian appears where the syllogism requires it to appear; the editorial decision to promote it earlier is the structural decision.**

**Meridian landing points after restructure (4 total):**

1. §III three-layer frame — passing reference to Elena's desktop spreadsheet as the "covered by a pricing exception" example *(L18, existing — KEEP)*.
2. §IX **Source at Meridian** *(NEW H2, promoted from H3)* — the full session vignette + the emergent Knowledge Map.
3. §XVII the completed seven-row Knowledge Map table *(L312-322, existing — KEEP)*.
4. §XVII closing read-back paragraph *(L324, existing — KEEP)* — reads the populated map back to the reader (two at-risk organic, broken spreadsheet, two Missing rows).

---

## Cross-chapter dependencies handled in Phase 3B (Drafter does NOT re-solve)

- Canonical agent definition at first use *(book-ultm)* — already landed at `05-source.qmd` L18 by Phase 3B. KEEP.
- Plain-English parentheticals on first-use jargon — RAG, embeddings, vectorization, ontologies, taxonomies, knowledge hygiene *(book-xqxi)* — 3B sweep handles. Drafter leaves jargon in place where present.
- Knowledge Map blank template insertion at ~L301 — Phase 3B's job. Drafter's job is to introduce and reference it in prose.
- SPC through-line: chapter ends pointing at Design (Ch 7). Knowledge Map + Constraint Statement = the artifact pair Design inherits.

---

## Drafter notes

- **Drafter model:** Opus. This is the heaviest restructure in Phase 3C (Simplicity Fail rescue).
- Estimated **70-75% of existing prose survives** the restructure. The move is cut + compress + reorder, not rewrite.
- **Anchoring discipline (NEW — per [[chapter-syllogism-and-flow-markers]]):** read the chapter syllogism and every section's Assumes / Establishes / Sets up triad BEFORE writing. Sentence-to-sentence decisions inside a reorganized section must respect the section's flow markers. This chapter is the heaviest restructure in 3C — sections move, sub-sections merge, frameworks compress. The triads tell the Drafter what each REORGANIZED section establishes after the move. If a sentence violates an Assumes/Establishes/Sets up dependency (orphaned antecedent, severed cross-section reference, restated prior claim), it's a coherence break the Drafter fixes before moving on.
- **Per-pass triad discipline:** Pass 1 / Pass 2 / Pass 3 each carry their own Assumes/Establishes/Sets up. The transitions between passes are where coherence has historically drifted (the "People don't have APIs" section existed because Pass 1's Sets up to Pass 2 was implicit). With the merge into Pass 1/2/3, each pass's Sets up makes the next pass structurally required — Pass 1's smallest-part-of-information-environment bridge into Pass 2; Pass 2's at-risk pivot into Pass 3 Missing. Drafter respects those bridges.
- **The six highest-leverage moves, in order:**
    1. Strip HBR scaffolding from opener (Argenti + Sadun + AWS at L20-22).
    2. Promote Jesse PM coordinator (L26-30) as the chapter opener.
    3. Compress PIS framework to one inline sentence; cut the section heading.
    4. Move Meridian vignette earlier (right after Pass 3, not at ~70%).
    5. Collapse two near-duplicate KM sections (L233-242 + L244-256) into one; salvage one sentence from the cut section.
    6. Merge "people don't have APIs" Digital / Organic / At-risk into Pass 1/2/3; cut the L198 dangling developer reference.
- Convert italic-fragment headings to directive language per inventory above.
- Adopt case-study AI Tier vocabulary (Tier 1 / Tier 2 / Tier 3 / Not AI-tier) at L127-147.
- **No tools (NEW — per [[qc-pipeline-per-chapter]]):** Drafter does NOT run deflourish, voice-scan, prose-craft, or any other tool. Those are separate pipeline stages. Drafter does structural edits + sentence-level coherence work per the triads, then returns a summary of edits and flagged decisions. Full QC pipeline runs after: Drafter → EC → Deflourisher → Voice Scan → Prose-Craft → Editor → orchestrator gate. No bundling. No skipping.
- **Re-read pass:** after structural edits land, Drafter reads the chapter end-to-end and checks: (a) every pronoun has an antecedent within 3 sentences; (b) every citation retains its quoted context or is cut; (c) every chart/Excalidraw sits adjacent to the prose that references it; (d) every Action Step still fits the section restructure that surrounds it (Pass 1 / Pass 2 / Pass 3 each carry their own Action Step — the restructure must not orphan any of them); (e) every cross-section reference (forward and backward) still resolves after the moves. EC will check these too, but Drafter doing this first reduces the EC delta.
- Voice charter applies. No new em-dashes. No triplet pileups around the three layers / three passes / TML.
- **Author sign-off needed BEFORE Drafter dispatches on:**
    - (a) HBR citation choice in §III.E — Option A (one Argenti sentence) or Option B (zero citations).
    - (b) Reflection Q3 in §XIX.C — restore a Preface developer callback in §XII or cut Q3 entirely.
    - (c) The "Digital sources are the smallest part..." salvage in §VIII.A.6 — keep or drop. *(Pass 1 triad currently treats this as the bridge into Pass 2; if dropped, the bridge falls to Pass 2's opening instead.)*
- After Drafter completes, cross-coherence-check against `case-study-meridian.qmd` L141-150 and `case-study-pm-agent-team.qmd` L76-86 — both Tier tables should use the same vocabulary the chapter now defines.

---

## AUTHOR FOLLOWUP items (consolidated)

Surfaced by this outline upgrade — the syllogism + triads exposed three structural decisions the prior outline left ambiguous:

1. **PIS placement (RESOLVED in this upgrade).** Prior outline said "fold into closing of §V OR opening of §VII." Syllogism forces the call: PIS folds into §V (the diagnosis-completion section), not §VII (the artifact-introduction section). §VII opens cleanly on the Knowledge Map.
2. **HBR citation choice (still open — author sign-off).** §III.E Argenti — Option A keep one sentence with parenthetical attribution, or Option B cut entirely. Recommend Option B.
3. **Reflection Q3 (still open — author sign-off).** Either restore the Preface developer callback in §XII Transcripts and keep Q3, or cut Q3.
4. **Pass 1 → Pass 2 bridge (still open — author sign-off).** The "Digital sources are the smallest part of the actual information environment" sentence — keep as the Pass 1 closing bridge, or drop and let Pass 2's opening carry the contrast implicitly.
5. **Section IX heading promotion confirmation.** Promoting "Source at Meridian" from H3 to H2 changes the chapter's H2 count by one. Author should confirm this is the desired shape (Meridian gets H2-level prominence in this chapter, matching the strong-Meridian-presence chapters in the audit).
