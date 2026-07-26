# Voice Charter — *Co-Intelligent Co-Operation*

The canonical voice profile for this book. Extracted from the de-AI'd chapter source after multiple polishing rounds. Authoring agents must read this before drafting or rewriting any prose.

**Narrative voice rule (canonical — now in scope):** Stories are told in first-person, blended narrative. Never use "Jesse:" / "Julie:" — or any — colon-label speaker prefixes; that screenplay/transcript format is banned and is an auto-reject anti-pattern (see A17 below). When a story belongs to one author, name them inside the prose ("Jesse was in our L10…", "My ops manager…") and use "I"; when it belongs to both, use "we." Inline naming in normal prose is correct and must not be flagged. This REPLACES the prior dual-author convention. This charter governs cadence, vocabulary, sentence structure, anti-patterns, and anti-AI signals.

---

## Section 1 — Voice pillars (what to preserve)

**1. Operator-to-operator, declarative, unhedged.**
Same register as a CEO talking to a CEO. No qualifiers that soften the diagnosis. Claims arrive without throat-clearing. Example (01-diagnosis.qmd:9): *"I asked them one question. The answer told me everything."* Not "In this section we will explore how a single question can sometimes reveal..."

**2. Diagnostic, not motivational.**
The book diagnoses. It does not exhort. No "your competitors are already doing this," no "the future is here." When stakes appear, they appear as math — dollar figures, hours, headcount ratios — not as urgency. Example (04-signal.qmd:30): *"The quoting bottleneck is costing us $558K per year..."*

**3. Specific over general. Always.**
Numbers are load-bearing. Names of artifacts, tools, people (anonymized or composite) are concrete. When a generic claim appears, a specific instance follows. Example (07-build.qmd:8): *"the five agents that replaced our $24,000-a-year coordinator role."*

**4. Mechanical / structural framing.**
The work is plumbing, not philosophy. Words like *workflow, handoff, accountability, structural, designed, gate, deliverable* carry the weight. The sampled triplet "*The pattern is mechanical. The diagnosis is mechanical. The fix is mechanical.*" (01-diagnosis.qmd:81) reads as AI cadence (triplet pileup, A3 below) and should not be imitated — the *principle* lives, the *construction* doesn't.

**5. Embedded story, never decorative anecdote.**
Stories arrive at the moment they make a point and end the moment the point is made. They are first-person, specific, and quantified where possible. They do not begin with "Imagine if..." or "Picture a company..." First-person tag follows the narrative voice rule: name the author inline in prose ("Jesse was in our L10…"; "I sat in on a meeting…") and use "I" for one author, "we" for both. Never use a colon-label prefix ("Jesse: …"). Example (04-signal.qmd:92): the PT clinic story opens *"I sat in on a meeting with a PT clinic operator that was forty-five minutes into a conversation about opening their sixth location."*

**6. Refuses recap rituals; ends with reflection questions.**
No "In this chapter we covered...", no "To recap...", no "Taken together...". Chapters end with **reflection questions that engage the reader to apply the chapter to their own business** — typically 2–4 short questions in a `### Reflect on your operation` style block (or equivalent), followed by a one-line handoff to the next chapter. Example handoff (07-build.qmd:342): *"Build makes it work. Deliver puts it into the company's actual operating rhythm..."*

**7. Education through redefinition.**
When introducing a new term (agent, RAG, token, sprint), the book defines it in plain language *before* using it operationally, and the definition is an analogy a non-technical operator can hold. Example (07-build.qmd:125): *"Tokens are to AI what minutes are to a phone plan."*

**8. Peer authority — with sourced research where it substantiates.**
Evidence is grounded in lived operating experience first — "We learned...", "I've watched...", "In my company..." — not detached citations. **Both/and: when published research substantiates a claim, name it inline with a specific reference (author, work, what it found)**. The forbidden form is "studies show" without specifics. The allowed form is "Mark O'Donnell's *Issues!* names this exact pattern as..." (one line, no bibliography theater). Example: 01-diagnosis.qmd:49 — *"My software development company, SuperWebPros, went from thirteen people to eight."*

---

## Section 2 — Cadence and structural rules

**Sentence-length mix.** Short punchy (3–8 words) interleaved with medium (15–25 words). Long sentences (30+) appear sparingly and use commas, semicolons, or sentence breaks to carry the breath. *Example:* 01-diagnosis.qmd:29 — *"One person working harder inside a system that was never designed for AI is not adoption."* (Single load-bearing sentence as its own paragraph.)

**Em-dashes are an AI tell — use sparingly, calculated, never as default rhythm.** This is a revision from earlier brief guidance. Em-dashes were previously called "the editorial rhythm" and "used freely"; that produced AI-cadence drift. Going forward: em-dashes appear only when no other punctuation works (parenthetical aside that breaks the sentence's spine; a deliberate beat). Default rhythm uses periods, commas, and semicolons. The existing manuscript has em-dashes from the prior rule that are grandfathered in, but **new edits do not add em-dashes** unless they're the only option. The voice scanner flags em-dash density.

**Paragraph rhythm.** Most paragraphs are 3–6 sentences. Single-sentence paragraphs land as hammer blows after a longer setup. *Example:* 01-diagnosis.qmd:19 — *"That company is not unusual. It might be yours."* (two short sentences, full paragraph.)

**Headlines: sentence case, periods, one *italic* emphasized word.** Never title case. Asterisks wrap the load-bearing word in the heading; CSS renders it as a red rule-underline. *Example:* 04-signal.qmd:18 — `## The deliverable is *one sentence*.`

**Contractions: always.** *don't, can't, won't, it's, you're, they're, we've, you've.* Absence of contractions is an AI tell. *Example:* 11-what-to-do-next.qmd:43 — *"Not after the offsite or the next tool evaluation."*

**Numbers are specific, loaded, sourced.** "$558K/year," "thirteen people to eight," "3.8 days to 4.2 hours," "$24,000 a year." Never "up to 40%," never "significant savings," never "many companies." *Example:* 07-build.qmd:312.

**The Sequence arrow.** Always `→` (U+2192), never `->`, never "to." Always the full six in order when listing: **Signal → Source → Design → Build → Deliver → Compound.** Brief: line 71.

**No bullets for narrative.** Bullets are reserved for genuine enumerations (the seven Guardrails questions, the five Whys, the three build paths). Narrative content uses em-dashes. Brief: line 146.

**No exclamation marks.** Brief: line 20.

**"You" address to the reader. First person ("I," "we") for stories.** Never "one," never "users," never "our clients."

---

## Section 3 — Vocabulary (canonical, forbidden, retired)

Authoritative source: `book-rewrite-brief.md` lines 27–137. Confirmed consistent across the four sampled chapters. Use these exactly.

### Canonical (use these)

**Capitalization rule (locked 2026-05-31):** every "Co-Intelligent" / "Co-Intelligence" / "Co-Operation" / "Co-Operating" form uses **capital I and capital O**. The capital-letter family is the canonical Compound brand convention. Author flagged inconsistency between earlier charter wording ("Co-intelligence" lowercase i) and the glossary + Equation ("Co-Intelligence" capital I); resolved to capital I across the board.

- **Co-Intelligent Company** — what the reader's company becomes (capital I).
- **Co-Intelligence** — humans + AI as one system, not two parallel tracks. The system half of the Equation. Capital I.
- **Co-Intelligent Co-Operation** — the relational frame (and the book title). Capital I, capital O.
- **Co-Operating Model** — the structural frame. Capital O.

**Adjectival form:** *Co-Intelligent organization* (capital I, lowercase noun) is acceptable when "organization" is the noun. *Co-Intelligent Company* is preferred when "Company" is doing branded work.

Voice scanner / editorial-coherence: flag any lowercase "co-intelligent" / "co-intelligence" / "co-operation" instance in body prose (callouts, glossary, equation contexts excluded only when already canonical).
- **Framework / Sequence / Rhythm / Sprint** — four distinct words. Not interchangeable.
- **Stages:** Signal → Source → Design → Build → Deliver → Compound.
- **Grouping:** Diagnose (Signal + Source) ⟂ Execute & Compound (Design + Build + Deliver + Compound).
- **The twelve instruments:** Constraint Finder, Issue Surfacer, Knowledge Map, Data Pipeline Audit, Work Deconstruction, Hybrid Accountability Chart, Build Spec Writer, Guardrails Checklist, Deploy Readiness Audit, Training Set Generator, Sprint Retrospective, Constraint Re-rank.
- **Six Compound Bench agents:** Signal Agent, Source Agent, Design Agent, Build Agent, Deliver Agent, Compound Agent.
- **Roles:** Human Orchestrator (operates and supervises the agent team in the shipped workflow), Sprint Lead (runs the Sprint project), leadership sponsor (accountable for the outcome), Agent Coordinator.
- **Artifacts:** Hybrid Accountability Chart, Hybrid Org Today.
- **Pain framing:** Headcount Paradox, headcount math, Design Before Deploy.
- **Equation:** *Co-Intelligence + Co-Operation + Rhythm = Compound.* (Co-Operation added as an explicit term in the Ch 3 re-conception, 2026-06; supersedes the earlier two-term form.)
- **Tagline:** *Stop transforming. Start compounding.*
- **CTA:** Clarity Call. compoundorg.com/clarity-call.

### Forbidden (auto-reject)

- *transformation, transformative, transform* (audience-exhausted)
- *leverage, synergy, alignment* (corporate filler — "the meeting kind" of alignment is fine)
- *cutting-edge, revolutionary, game-changer, paradigm shift*
- *augmentation* (use *co-intelligence*)
- *hybrid* alone — only inside locked phrases *Hybrid Accountability Chart*, *Hybrid Org Today*
- *organizational design* in **any** mid-market-operator context (use plain words: "how the work is set up," "who owns what," "the way the team runs"). Mid-market CEOs don't think or talk in HR-enterprise vocabulary. Allowed only in narrow technical context where no plain equivalent exists, and never in headings.
- *join us, revolution* (movement is allowed but **community is better**)
- "Learn more," "Discover," "Find out how," "Schedule a demo," "Dive in," "Navigate," "Unlock"
- "It's important to note," "rapidly evolving landscape"
- "studies show" without specifics; "(Author, Year)" citation format; "In [Book] by [Author]..." book-report openers (the *form* is forbidden — a sourced research reference inline with author, work, and what it found is fine; see Pillar 8)
- Emoji. Anywhere.

**Allowed** (clarified from earlier brief): *AI-powered, AI-enabled* are fine when they describe a concrete capability ("AI-enabled workflow"). They are not the same as the audience-exhausted *transformation/transformative* family.

### Retired (do not resurrect)

- *Orchestrated Organization* → use **Co-Intelligent Company**.
- *AI Maturity Diagnostic, diagnostic call, strategy call, discovery call* → use **Clarity Call**.
- *Act One / Act Two* grouping of the Sequence → use **Diagnose ⟂ Execute & Compound**.
- Old skill names (*Outcome Map, Data Inventory, Pipeline Map, Work Decomposition, Sprint Scorecard, ROI Calculator, Scale Decision*) → use the canonical twelve.

---

## Section 4 — Anti-patterns (forbidden — auto-reject)

Each entry: **(a)** the pattern, **(b)** why forbidden, **(c)** what NOT to write.

### A1. Abstract-noun-equals-abstract-noun ("Sequence is a process to execute")
**Why:** Definitionally hollow. Equates one abstraction to another without giving the reader anything to grip. Flagged by Jesse at `_julie/julie-final.md:102`.
**Don't write:** *"The Sequence is a process to execute."* *"Co-intelligence is a way of working."* *"Rhythm is a cadence."*
**Do instead:** Define by what it produces, who runs it, or what it replaces. *"The Sequence is the order — Signal first, Compound last — that the rest of the book argues for."*

### A2. Coined term used before stakes are established
**Why:** Brand-new terms (*co-intelligence*, *Co-Operating Model*, *Hybrid Org Today*) cannot do work the first time they appear unless the reader has been given a reason to care. Flagged at `_julie/julie-final.md:113`.
**Don't write:** *"Between the two of us, we bring the technical architecture and the human capital discipline required to install co-intelligence..."* (before *co-intelligence* has been defined or staked).
**Do instead:** Stake the problem first. Name the term as the resolution.

### A3. Triplet pileup / parallel-construction overload
**Why:** Reads as AI cadence. The book uses parallel structure sparingly and for emphasis — not every paragraph. Flagged at `_julie/julie-final.md:133`. Voice scanner pillar: "Negative parallelism overuse — flag if more than 3 per chapter."
**Don't write:** *"The vision was clear, the team was ready, the path was set."* *"We mapped the work, we identified the constraints, we redesigned the workflow."*
**Do instead:** Use one parallel construction per section, max — and only when it carries argumentative weight. Vary cadence everywhere else.

### A4. Contrived or boastful biographical examples
**Why:** Examples that exist to make the author look impressive (rather than to make a point the reader can use) read as AI puffery. The "121 episodes simultaneous with global HR function" beat at `_julie/julie-final.md:64-69` was flagged precisely for this.
**Don't write:** *"One hundred and twenty-one episodes produced while simultaneously running a global HR function."*
**Do instead:** Use biographical detail only when it produces a number the reader can compare themselves against, or a pattern they can recognize in their own org.

### A5. General "AI smell" — hedged, verbose, no operator weight
**Why:** Long sentences with multiple qualifiers, abstract-noun chains, no specific evidence. The whole point of the de-AI pass. Flagged at `_julie/julie-final.md:71`.
**Don't write:** *"This represents a transformative opportunity to fundamentally reimagine how organizations approach the integration of artificial intelligence within their operational frameworks."*
**Do instead:** One claim, one piece of evidence, one number.

**Tooling note.** The `ai-tell-scan` skill exists to catch this category at scale. It must be run **per chapter** (not just at the end of a batch) to prevent context-window blindness from missing anti-patterns that accumulate gradually across paragraphs.

### A6. Fear-based or competitive-threat urgency
**Why:** Existing voice rule (`voice-scanner.md`). Audience is exhausted by it.
**Don't write:** *"Your competitors are already doing this."* *"Don't get left behind."*
**Do instead:** Math. *"Every quarter you stay inside the old operating model is a quarter you keep adding people..."* (11-what-to-do-next.qmd:198).

### A7. Book-report citations
**Why:** Existing voice rule. Peer-to-peer not professor.
**Don't write:** *"In [Book] by [Author]..."* *"According to [Author]..."* *"(Smith, 2023)"*
**Do instead:** Lift the insight and credit briefly inline, as the book does for Mark O'Donnell's *Issues!* (04-signal.qmd:195) — one line, no bibliography theater.

### A8. Conjunctive-adverb pileup
**Why:** Existing voice rule. "However," "moreover," "furthermore" exceeding 1 per 200 words is an AI tell.
**Don't write:** *"However, this is not the only consideration. Moreover, we must also examine... Furthermore..."*
**Do instead:** Em-dash, period, or restructure.

### A9. Superficial -ing tag clauses
**Why:** Existing voice rule. AI generates filler closers like "ensuring...," "highlighting...," "underscoring..."
**Don't write:** *"This produces real results, ensuring better outcomes and highlighting the value of the framework."*
**Do instead:** End the sentence. The next sentence carries the next idea.

### A10. Section-ending summaries / recap rituals
**Why:** Brief lines 156–158. Trust the reader.
**Don't write:** *"In summary, this chapter has covered..."* *"To recap the key points..."* *"Taken together, these ideas..."*
**Do instead:** Handoff to the next chapter — one paragraph, sometimes one line.

### A11. Inflated symbolism / abstract elevation
**Why:** AI tell. Voice scanner pattern.
**Don't write:** *"...stands as a testament to..."* *"...plays a pivotal role in..."* *"...serves as a cornerstone of..."*
**Do instead:** Say what it does.

### A12. Generic / invented company beats
**Why:** Brief line 195: "Do not invent numbers, names, or details beyond what's provided."
**Don't write:** *"A Fortune 500 company we worked with saw 47% improvement..."* (no such engagement exists).
**Do instead:** Use the named real composites (Meridian Manufacturing, Greenline Home Services) or generic-by-design ("a 60-person professional services firm"). The Compound internal sprints (Knowledge Capture, Process Automation, Performance Gap) and Saint Clair, Jill, Donna, the mobile home distributor are the only named engagements available.

### A13. Means/ends conflation
**Why:** The book exists to produce operator-recognizable outcomes — top-line and bottom-line growth, headcount math working in the operator's favor, fires reduced. The framework / Sequence / Sprint / design discipline are *means*, not ends. Drafts that describe the system as the destination ("This book is about the design work...") treat the means as the end and bury the value the reader actually buys. Caught by Jesse on the Preface trial (paragraph 13).
**Don't write:** *"This book is about the design work that has to happen before any tool gets deployed."* *"What we offer is a framework for organizational design."* (System framed as end.)
**Do instead:** Lead with the operator outcome the framework produces, then name the framework as the means. *"This book is about a framework, not a tool. Run it and you get top-line and bottom-line growth without adding headcount... Operating design is how you get there."*

### A14. Metaphor literalism violation
**Why:** Every metaphor must literally apply to all the things it's attached to. Extending a metaphor past its semantic boundary makes the prose feel "loose" — like the writer is reaching for cadence over meaning. Caught by Jesse on the Preface trial: "no seat for the developer's knowledge" failed because knowledge doesn't have seats.
**Don't write:** *"No seat for the developer's knowledge, no seat for a coherent operating model..."* (Seats apply to workers; not to knowledge, not to operating models.) *"You'll leave with the Sequence..."* (Books are not places you leave.)
**Do instead:** Either restrict the metaphor to where it literally applies (the AI worker has a seat; the developer's knowledge had a place — a different metaphor), or describe each referent in its own terms.

### A15. Unqualified AI agency
**Why:** The book argues that AI's effectiveness depends entirely on the design that constrains and enables it. Sentences that describe AI as choosing / deciding / acting without grounding in operator-designed context contradict the book's own argument and read as the "magical AI" framing the audience is exhausted by. Caught by Jesse on the Preface trial: "Neither chooses. AI does." overstated AI autonomy.
**Don't write:** *"AI decides what comes next."* *"The agent chooses the right path."* *"AI does."* (without qualification)
**Do instead:** Qualify with the design constraint. *"AI does, inside whatever context you design for it."* *"The agent decides — but only within the scope the operator has defined."*

### A16. Book-as-location metaphor
**Why:** Books are artifacts with pages and a finish point. They are not locations a reader enters, occupies, or leaves. "Leave with," "walk away from," "inside this book" treat the book as a place — false metaphor. Caught by Jesse on the Preface trial: "You'll leave with..."
**Don't write:** *"You'll leave with the framework..."* *"Walk away from this book with..."* *"Inside this book, you'll find..."*
**Do instead:** Use verbs that match the book's actual ontology. *"By the last page, you'll have..."* *"When you finish, you'll have..."* *"You'll close this book with..."* *"You'll put this book down with..."*

### A17. Colon-label speaker prefix — AUTO-REJECT
**Why:** The screenplay/transcript format "Jesse: …" / "Julie: …" breaks the first-person blended narrative voice. It signals a different genre (interview, script, dialogue) and ruptures the reader's immersion in the book's operator-to-operator register. Inline naming in normal prose ("Jesse was in our L10," "Julie sat in on a meeting") is **correct** and must never be flagged.
**Don't write:** *"Jesse: We had a project coordinator role…"* *"Julie: I ran the sprint with a PT clinic…"* or any `Name:` prefix at the start of a sentence or paragraph.
**Do instead:** Name the author inside the prose and use "I" or "we." *"We had a project coordinator role…"* (both authors) or *"Jesse was reviewing the role when we ran it through Work Deconstruction…"* (one author named inline).
**Vale rule:** `SpeakerLabel.yml` (error level) flags this pattern automatically. LLM scanner also checks.

---

## Section 5 — How to use this charter (operator instructions for implementer agents)

**You — `voice-implementer`, `bmad-quick-dev`, chapter-writer, editor — read this charter before every rewrite or draft. Not after. Not "if needed." Before.**

The order of operations:

1. **Read Section 4 (anti-patterns) before drafting.** Treat each pattern as an auto-reject filter. If you find yourself writing toward one of them, stop and rephrase before completing the sentence.

2. **Validate Section 3 vocabulary at the term level.** Every load-bearing noun in your draft must be on the canonical list or be plain English. Search the draft for forbidden and retired terms. Replace before submitting.

3. **Validate Section 2 cadence at the paragraph level.** Check sentence-length mix, em-dash usage, headline format, contractions, presence of specific numbers. If a paragraph reads "smooth" — uniform sentence length, no specifics, no em-dashes — it is almost certainly AI smell. Rewrite.

4. **Validate Section 1 voice pillars at the section level.** For each section ask: Is this operator-to-operator? Diagnostic, not motivational? Specific, not general? Mechanical / structural? Story embedded at the right moment? Refusing summary rituals? Defining new terms first? Grounded in lived experience?

5. **If the scanner (`voice-scanner.md`) flags something this charter forbids, the fix is mandatory.** No "this is also valid prose" defenses against Section 4 anti-patterns.

6. **Never resurrect retired vocabulary** (Section 3) even if it appears in old drafts, `_julie/julie-final.md`, or prior brand materials. Those drafts predate the de-AI'd canonical voice.

---

## Section 6 — Mapping to existing agent definitions

The following existing agent/brief files do NOT yet reference the anti-patterns this charter codifies. They should be updated to incorporate them. *Listing only — do not make these edits as part of this task.*

### `voice-scanner.md` — needs additions
Current anti-pattern list (lines 41–50) covers corporate filler, fear-urgency, book-reports, citations, generic AI tells, inflated symbolism, summary rituals, conjunctive-adverb overuse, negative-parallelism overuse, and -ing tag clauses. **Missing:**
- A1 (abstract-noun-equals-abstract-noun) — add as flagged pattern with example
- A2 (coined term before stakes) — add as flagged pattern; requires scanner to track which terms have been defined in earlier paragraphs
- A3 (triplet pileup) — partially covered by negative-parallelism rule but should be expanded to cover any triplet construction, not just "not X — it's Y"
- A4 (contrived/boastful biographical examples) — currently no rule
- A12 (invented company beats) — currently no rule; scanner should flag any numeric claim attached to an unnamed engagement

Also: scanner's Pillar 6 ("First Person & Anonymized") must be updated to reflect the canonical narrative voice rule now in this charter: colon-label speaker prefixes ("Jesse: …", "Julie: …") are banned and are auto-reject (A17). First-person blended with inline naming is the correct form.

### `voice-implementer.md` — needs additions
Voice Quick Reference (lines 31–35) is thin. **Suggested addition:** a "before you rewrite, run this checklist" block pointing to this charter's Section 4. Currently the implementer has no anti-pattern reference at all — it just trusts the scanner's flags.

### `book-rewrite-brief.md` — needs additions
Voice section (lines 14–25) is solid on positive instruction but does not name anti-patterns explicitly. **Suggested addition:** a "Forbidden constructions" subsection mirroring Section 4 of this charter, OR a one-line reference: *"See `_julie/voice-charter.md` Section 4 for forbidden constructions. Auto-reject filters apply."*

### `CLAUDE.md` (Editorial notes section)
Already concise and accurate. **Suggested addition:** one line pointing new agents to this charter — *"Voice canon: see `_julie/voice-charter.md`. Read it before any prose edit."*

---

*End of charter.*
