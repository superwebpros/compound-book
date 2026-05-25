# Voice Charter — *Co-Intelligent Co-Operation*

The canonical voice profile for this book. Extracted from the de-AI'd chapter source after multiple polishing rounds. Authoring agents must read this before drafting or rewriting any prose.

**Out of scope:** I-vs-we / Jesse:/Julie: callout convention. That is handled separately as the dual-author pass. This charter governs cadence, vocabulary, sentence structure, anti-patterns, and anti-AI signals only.

---

## Section 1 — Voice pillars (what to preserve)

**1. Operator-to-operator, declarative, unhedged.**
Same register as a CEO talking to a CEO. No qualifiers that soften the diagnosis. Claims arrive without throat-clearing. Example (01-diagnosis.qmd:9): *"I asked them one question. The answer told me everything."* Not "In this section we will explore how a single question can sometimes reveal..."

**2. Diagnostic, not motivational.**
The book diagnoses. It does not exhort. No "your competitors are already doing this," no "the future is here." When stakes appear, they appear as math — dollar figures, hours, headcount ratios — not as urgency. Example (04-signal.qmd:30): *"The quoting bottleneck is costing us $558K per year..."*

**3. Specific over general. Always.**
Numbers are load-bearing. Names of artifacts, tools, people (anonymized or composite) are concrete. When a generic claim appears, a specific instance follows. Example (07-build.qmd:8): *"the five agents that replaced our $24,000-a-year coordinator role."*

**4. Mechanical / structural framing.**
The work is plumbing, not philosophy. Words like *workflow, handoff, accountability, structural, designed, gate, deliverable* carry the weight. Example (01-diagnosis.qmd:81): *"The pattern is mechanical. The diagnosis is mechanical. The fix is mechanical."*

```jf-note:
The principle is correct, but that example reads like AI
```

**5. Embedded story, never decorative anecdote.**
Stories arrive at the moment they make a point and end the moment the point is made. They are first-person, specific, and quantified where possible. They do not begin with "Imagine if..." or "Picture a company..." Example (04-signal.qmd:92): the PT clinic story opens *"I sat in on a meeting with a PT clinic operator that was forty-five minutes into a conversation about opening their sixth location."*

```jf-note:
Correct, but with "we" language or "Jesse/Julie" distinction when appropraite
```

**6. Refuses summary rituals.**
No "In this chapter we covered...", no "To recap...", no "Taken together...". Chapters end on a handoff to what comes next — usually one paragraph, sometimes a one-line transition. Example (07-build.qmd:342): *"Build makes it work. Deliver puts it into the company's actual operating rhythm..."*

```jf-note:
All chapters should be ending with reflection questions to keep the reader engaged
 and thinking about their busienss.
 ```

**7. Education through redefinition.**
When introducing a new term (agent, RAG, token, sprint), the book defines it in plain language *before* using it operationally, and the definition is an analogy a non-technical operator can hold. Example (07-build.qmd:125): *"Tokens are to AI what minutes are to a phone plan."*

**8. Peer authority, not consultant authority.**
Evidence is grounded in lived operating experience — "We learned...", "I've watched...", "In my company..." — not citations, not "studies show," not appeals to authority. Example (01-diagnosis.qmd:49): *"My software development company, SuperWebPros, went from thirteen people to eight."*

```jf-note:
Both/and. When there is research to substantiate our perspectives, we want to use it.
```

---

## Section 2 — Cadence and structural rules

**Sentence-length mix.** Short punchy (3–8 words) interleaved with medium (15–25 words). Long sentences (30+) appear sparingly and use em-dashes to carry the breath. *Example:* 01-diagnosis.qmd:29 — *"One person working harder inside a system that was never designed for AI is not adoption."* (Single load-bearing sentence as its own paragraph.)

```jf-note:
No em-dashes.
```

**Em-dashes are the editorial rhythm.** Used freely. They replace bullet lists for parenthetical/expansive content. *Example:* 04-signal.qmd:8 — *"...a subcontractor we were paying $24,000 a year — and the work was still falling behind."*

```jf-note:
See above; em-dashes are generally an AI-tell. We should use them sparingly. See the 'voice' skill
```

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

- **Co-Intelligent Company** — what the reader's company becomes.
- **Co-intelligence** — humans + AI as one system, not two parallel tracks.
- **Co-Intelligent Co-Operation** — the relational frame (and the book title).
- **Co-Operating Model** — the structural frame.
- **Framework / Sequence / Rhythm / Sprint** — four distinct words. Not interchangeable.
- **Stages:** Signal → Source → Design → Build → Deliver → Compound.
- **Grouping:** Diagnose (Signal + Source) ⟂ Execute & Compound (Design + Build + Deliver + Compound).
- **The twelve instruments:** Constraint Finder, Issue Surfacer, Knowledge Map, Data Pipeline Audit, Work Deconstruction, Hybrid Accountability Chart, Build Spec Writer, Guardrails Checklist, Deploy Readiness Audit, Training Set Generator, Sprint Retrospective, Constraint Re-rank.
- **Six Compound Bench agents:** Signal Agent, Source Agent, Design Agent, Build Agent, Deliver Agent, Compound Agent.
- **Roles:** Human Orchestrator, Agent Coordinator.
- **Artifacts:** Hybrid Accountability Chart, Hybrid Org Today.
- **Pain framing:** Headcount Paradox, headcount math, Design Before Deploy.
- **Equation:** *Co-Intelligence + Rhythm = Compound.*
- **Tagline:** *Stop transforming. Start compounding.*
- **CTA:** Clarity Call. compoundorg.com/clarity-call.

### Forbidden (auto-reject)

- *transformation, transformative, transform* (audience-exhausted)
- *leverage, synergy, alignment* (corporate filler — "the meeting kind" of alignment is fine)
- *AI-powered, AI-enabled, cutting-edge, revolutionary, game-changer, paradigm shift*
- *augmentation* (use *co-intelligence*) `jf-note: AI-powered and AI-enabled are fine.`
- *hybrid* alone — only inside locked phrases *Hybrid Accountability Chart*, *Hybrid Org Today*
- *organizational design* in headings/mastheads `jf-note: Rarely; most entrepreneurs don't think about org design; Julie's experience in HR is heavily enterprise-coded, but smaller/mid-market companies don't think or talk like that. We need to use plain words. Org design should be sparing and only when necessary.`
- *movement, join us, revolution* `jf-note: Movement is fine. Community is better.`
- "Learn more," "Discover," "Find out how," "Schedule a demo," "Dive in," "Navigate," "Unlock"
- "It's important to note," "rapidly evolving landscape"
- "studies show" (without specifics), "(Author, Year)", "In [Book] by [Author]..."
- Emoji. Anywhere.

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

```jf-note:
We have a skill to help detect AI-voice. Needs to be run on a per-chapter basis in order to make sure anti-patterns aren't missed in a context window.
```

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

Also: scanner's Pillar 6 ("First Person & Anonymized") will need revision once the I-vs-we dual-author convention is finalized. Out of scope for this charter.

### `voice-implementer.md` — needs additions
Voice Quick Reference (lines 31–35) is thin. **Suggested addition:** a "before you rewrite, run this checklist" block pointing to this charter's Section 4. Currently the implementer has no anti-pattern reference at all — it just trusts the scanner's flags.

### `book-rewrite-brief.md` — needs additions
Voice section (lines 14–25) is solid on positive instruction but does not name anti-patterns explicitly. **Suggested addition:** a "Forbidden constructions" subsection mirroring Section 4 of this charter, OR a one-line reference: *"See `_julie/voice-charter.md` Section 4 for forbidden constructions. Auto-reject filters apply."*

### `CLAUDE.md` (Editorial notes section)
Already concise and accurate. **Suggested addition:** one line pointing new agents to this charter — *"Voice canon: see `_julie/voice-charter.md`. Read it before any prose edit."*

---

*End of charter.*
