# ARC Prospect Read-Through — Synthesis Report

*Source: per-chapter verdicts from readers playing the ideal customer (smart, non-technical entrepreneur). Three bars scored per chapter: **A** = Clarity, **B** = Can-they-get-moving, **C** = Recognizable-artifacts. Scale: Pass / Risk / Fail.*

---

## 1. Overall Read

The book is **not yet prospect-ready, but it is close** — and the gap is editorial, not structural. The four-stage model and the Sprint mechanism are coherent end to end, and the book's signature strength is consistent across every chapter: it produces **real, fillable artifacts** (Scorecard, Constraint Statement, Knowledge Map, Hybrid Accountability Chart, Build Spec, runbooks) with worked Meridian examples a CEO can pattern-match against. Where it shines is forward motion at the section level — most chapters carry concrete Action Steps and sharp reflection questions. Where it **stalls** is at three predictable seams: (1) **undefined technical jargon** dropped into otherwise plain prose (agent, RAG, API, n8n, system prompt, tokens, ontologies) that quietly signals "this isn't for you" to the non-technical reader; (2) **coined book terms referenced before or without definition** (Sprint Planning Canvas, Human Orchestrator, ICs, Hybrid Org Today), often with **broken or circular cross-references** ("defined earlier"/"see Chapter 7"/"introduced in Chapter 11" that point at nothing or at themselves); and (3) **central artifacts that are named but never shown as a blank, fillable template** (Signal Backlog, Hybrid Org Today, Design Brief, Sprint Planning Canvas), so a reader knows the artifact exists but cannot start it. The two case studies are powerful demonstrations that fail to convert to reader action — one has no closing bridge, the other has no reflection questions at all. None of these are deep problems. They are a clean, finite punch list of definitions, cross-reference fixes, and blank-template insertions.

---

## 2. Per-Chapter Scoreboard

| Chapter | A (Clarity) | B (Get-moving) | C (Artifacts) | Overall |
|---|---|---|---|---|
| 01-diagnosis | Risk | Pass | Pass | **Risk** |
| 02-beliefs | Risk | Risk | Risk | **Risk** |
| 02-co-operating-model | Risk | Pass | Risk | **Risk** |
| 03-the-framework | Pass | Pass | Pass | **Pass** |
| 04-signal | Risk | Pass | Risk | **Risk** |
| 05-source | Risk | Pass | Pass | **Risk** |
| 06-designing-the-system | Risk | Pass | Risk | **Risk** |
| 06b-designing-the-work | Risk | Risk | Risk | **Risk** |
| 07-build | Risk | Pass | Pass | **Risk** |
| 08-deliver | Risk | Pass | Pass | **Pass** |
| 09-compound | Pass | Pass | Risk | **Risk** |
| 10-the-rhythm | Risk | Pass | Risk | **Risk** |
| 11-what-to-do-next | Risk | Pass | Risk | **Risk** |
| case-study-meridian | Risk | Risk | Pass | **Risk** |
| case-study-pm-agent-team | Risk | **Fail** | Risk | **Risk** |

**Axis tallies (15 chapters):**

- **A (Clarity):** 2 Pass / 13 Risk / 0 Fail
- **B (Get-moving):** 11 Pass / 3 Risk / 1 Fail
- **C (Artifacts):** 5 Pass / 9 Risk / 0 Fail
- **Overall:** 2 Pass / 13 Risk / 0 Fail

---

## 3. Systemic Patterns

These are cross-chapter failure modes, not isolated chapter issues. Fixing the pattern once (a standard, a glossary, a template convention) resolves many chapters at once.

### 3A. Undefined technical jargon (the #1 systemic clarity failure — drives 13/15 A-Risk scores)

The same handful of terms appear undefined across multiple chapters. A non-technical CEO who hits three undefined terms in a worked example concludes the book is more technical than promised. The repeat offenders:

| Term | Undefined in chapters |
|---|---|
| **agent** (vs. ChatGPT) | 01, 02-beliefs, 09 |
| **RAG / retrieval-augmented generation** | 05, 06, 07 |
| **API** | 02-com, 03, 07 (9×), case-meridian, case-pm |
| **n8n** | 03, 06b, case-meridian, case-pm |
| **system prompt** | 02-com, 06 |
| **tokens** | 05 |
| **ontologies / embeddings / knowledge graphs / taxonomies** | 05 |
| **chunking / metadata / freshness / indexed data store / retrieval layer** | 06, 07 |
| **ERP / EHR** | 04, 09 |
| **Claude Code, webhook, cron, Node.js, HTTPS, API key** | case-pm (six in a row) |

**Root cause:** Build/architecture sections introduce implementation terms that are the *builder's* job, not the CEO's, without ever saying so. **Systemic fix:** a one-time glossary pass + a standing rule — every technical term gets a plain-English parenthetical on first use per chapter, and Build sections explicitly partition "what you decide" vs. "what your Build team handles."

### 3B. Broken or circular cross-references (a trust-killer — concentrated but high-severity)

Multiple chapters point readers at references that don't exist or loop back on themselves:

- **07-build** lines 272/288/292: three "see Chapter 7" references *inside Chapter 7* — sends the reader in a loop.
- **06b-designing-the-work** line 142: "agent-anatomy concept introduced in Ch 3" — actually introduced in 06-designing-the-system; reader who checks finds nothing.
- **11-what-to-do-next** line 30: "Hybrid Org Today, introduced in Chapter 11" — it was Chapter 10; this *is* Chapter 11.
- **01-diagnosis** line 110: "agents — the kind defined earlier" — no prior definition exists in the chapter.
- **02-beliefs** / **04-signal** / **05-source**: "Sprint Planning Canvas" referenced as a known artifact before it's introduced.

**Root cause:** chapter renumbering during edits without updating inline references. **Systemic fix:** a single cross-reference audit pass; ideally replace hard chapter numbers with named-stage references that survive renumbering.

### 3C. Coined terms used before definition (the second clarity pattern)

Book-native terms are deployed as if established: **Sprint Planning Canvas** (02, 04, 05, 10, 11), **Human Orchestrator** (03, 06, 08, 09 — never mapped to the EOS Integrator the reader already knows), **ICs** (02), **Sequence first-pass** (04, 05), **Issue Surfacer** (04), **Hybrid Org Today** (03, 10, 11 — never distinguished from the Hybrid Accountability Chart), **design infrastructure** (10). The **EOS bridge** is the recurring missed opportunity: Hybrid Accountability Chart → Accountability Chart, Human Orchestrator → Integrator, "design the work not do it" → Visionary/Integrator split. These land for free with one sentence and are currently left for the reader to infer (02-beliefs, 03, 06, 09, 10, case-meridian, case-pm).

### 3D. "So what?" / missing-AI-bridge failures

Two chapters never answer the reader's standing question — *what does this have to do with AI?*

- **04-signal**: a whole chapter on constraint-finding with no sentence saying "this is the problem statement your AI Sprint will be built to solve" until the end.
- **case-study-meridian** and **case-study-pm-agent-team**: complete demonstrations of *someone else's* Sprint with no bridge to the reader's own situation.

### 3E. Where a prospect actually stalls (B = Risk/Fail)

Four chapters lack a clean reading-to-doing threshold:

- **case-study-pm-agent-team (B = Fail):** the only Fail in the book. No reflection questions, no handoff, no "your turn" — ends on a retrospective table. A CEO finishes with a great story and zero prompt to act.
- **02-beliefs (Risk):** closes on a tease ("here's what you're actually building") with no assigned action; the gut check produces nothing written.
- **06b-designing-the-work (Risk):** the central artifact (Design Brief) has no Action Step telling the reader to write theirs; only 3 Action Steps for ~5,000 words.
- **case-study-meridian (Risk):** ends as narrative ("The next Sprint starts Monday"), no reader bridge.

### 3F. Artifacts that aren't recognizable as artifacts (C = Risk, 9 chapters)

The recurring pattern: an artifact is *named and described* but never shown as a **blank, fillable template** the reader can start from. The reader knows it exists but can't picture or begin it.

| Artifact | Named but not shown as fillable in |
|---|---|
| **Sprint Planning Canvas** | 04, 05 (referenced; blank only promised at "compound.co/resources when it launches" in 03) |
| **Hybrid Org Today** | 03, 10, 11 (prose only / Excalidraw placeholder; never a row structure) |
| **Signal Backlog** | 09, 11 (re-ranked but never shown — no columns, no example rows) |
| **Design Brief** | 06, 06b (components listed, no blank shell) |
| **Constraint Statement** | 04 (blank lives only in an Excalidraw graphic that may not render in EPUB/PDF) |
| **Hybrid Accountability Chart** | 09, 10 (updated but no row shown in-chapter) |
| **mini-spec** | 06 (six fields named, no populated example) |
| **Source Classification "AI Tier"** | case-meridian, case-pm (Tier/category labels used, never defined) |

Two sub-patterns drive this: (1) **Excalidraw placeholders** that don't render in text/PDF/EPUB, leaving the only copy of a template invisible (04, 08, 09, 10, 11); (2) **forward-deferral** ("the full template is in the next chapter") that introduces a required deliverable then withholds the model (06 mini-spec, 06 Design Brief, 02-com HAC).

---

## 4. Ranked Fix Backlog (Phase-3 Beads)

Ordered by reader impact — highest first. Each item maps to the chapter(s) it affects and the axis it serves.

| # | Fix | Chapters | Axis | Why it ranks here |
|---|---|---|---|---|
| **1** | **Fix all broken/circular cross-references.** Correct the three "see Chapter 7" loops in 07-build (272/288/292); fix 06b "Ch 3" → 06-designing-the-system (142); fix 11 "introduced in Chapter 11" → Chapter 10 (30); fix 01 "defined earlier" for *agent*. | 07, 06b, 11, 01 | A | Pure trust-killers. A reader who follows a reference into a loop or a void concludes the book is broken. Cheap to fix, highest credibility damage if not. |
| **2** | **Define "agent" in plain English at first functional use, and standardize a one-line "agent vs. ChatGPT" definition** reused on first appearance per chapter. | 01, 02-beliefs, 09 | A | The book's central claim ("agents are the real capability") floats without this. The #1 conceptual foundation gap. |
| **3** | **Run a glossary/jargon pass: plain-English parenthetical on first use for RAG, API, n8n, system prompt, tokens, ontologies.** In Build/architecture sections, explicitly split "what you decide" vs. "what your Build team handles." | 05, 06, 07, 02-com, 03, case-meridian, case-pm | A | Drives 13/15 A-Risk scores. Single highest-volume clarity lever; the recurring "not for me" signal for the non-technical buyer. |
| **4** | **Add reflection questions + handoff to case-study-pm-agent-team, and a closing reader bridge to case-study-meridian** ("you have an Elena/Rachel; your next step is to fill in these same artifacts"). | case-pm, case-meridian | B | The only **Fail** in the book plus its companion. Converts two powerful demos from inspiration into activation. |
| **5** | **Embed blank, fillable templates in-body for the artifacts currently named-but-not-shown** — Signal Backlog (cols + 2 example rows), Hybrid Org Today (4-field skeleton), Sprint Planning Canvas (8-question table), Design Brief (labeled shell), Constraint Statement (text table, not only Excalidraw). Stop relying on Excalidraw placeholders and "next chapter" deferral as the only copy. | 09, 11, 10, 03, 04, 05, 06, 06b | C | Resolves the 9-chapter C-Risk pattern. The reader's leave-with-something-buildable moment depends on it. |
| **6** | **Build the EOS bridge once, apply everywhere:** map Hybrid Accountability Chart → Accountability Chart, Human Orchestrator → Integrator, "design the work" → Visionary/Integrator split, on first use per chapter. | 02-beliefs, 03, 06, 09, 10, case-meridian, case-pm | A/C | Near-free buy-in from the core EOS-operator audience; currently left entirely to inference. |
| **7** | **Define coined book terms on first use and add the missing AI bridge to Signal.** Define ICs, Sequence first-pass, Issue Surfacer, design infrastructure, Hybrid Org Today (distinct from HAC); add the "this is the problem your AI Sprint will solve" sentence early in 04-signal. | 02-beliefs, 04, 05, 06b, 10 | A | Removes the second tier of "used before defined" friction and closes the "why is this in an AI book?" gap in Signal. |
| **8** | **Add the missing "do this now" Action Steps** where the central artifact has none: Design Brief (06b), HAC draft (06), gut-check as written artifact (02-beliefs), knowledge-manager role assignment (05). | 06b, 06, 02-beliefs, 05 | B | Closes the reading-to-doing threshold in the 3 B-Risk content chapters. |
| **9** | **Add facilitation/session scaffolding** where the reader knows WHAT but not HOW to convene: who's in the room + time budget for Signal (04); the 90-minute Compound session agenda (09). | 04, 09 | B | Turns "run a session" into a session a CEO can actually schedule and walk into. |
| **10** | **Mechanize the scorecard math and tiebreakers** in 01-diagnosis: fold the dimension-subtotal step into the scoring table (before the bucket descriptions) and add an interim dimension-prioritization tiebreaker so no number is left blank. | 01 | B/C | Prevents the opening chapter from ending with an unfilled scorecard and no fallback rule. |
| **11** | **Define the "AI Tier" / Source Classification categories** (Standing context, Retrieved knowledge, Not-AI-tier) inline wherever the table appears. | case-meridian, case-pm | A/C | A reader filling this artifact for their own business currently can't classify their sources. |
| **12** | **Replace Excalidraw-only templates and the "compound.co/resources when it launches" hedge** with rendered in-body artifacts (or confirm the URL is live before publish). | 03, 04, 08, 09, 10, 11 | C | Production dependency that silently breaks the artifact promise in PDF/EPUB. |

---

*Backlog items 1–4 are the prospect-readiness blockers; 5–7 are the high-leverage clarity/recognition fixes; 8–12 are the completeness sweep.*
