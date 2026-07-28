---
name: chapter-structure-pass
description: "The canonical standard and orchestration recipe for the structural fine-tuning pass on a Co-Intelligent Co-Operation chapter. Use when fine-tuning/re-conceiving any chapter from Co-Operating Model onward, or to pre-process upcoming chapters before the author reads. Encodes the five recurring structural patterns + the proven chapter shape + the audit→draft→diagram→judge recipe. Pairs with the chapter-auditor agent."
---

# Chapter structure pass

Every chapter from the Co-Operating Model onward has arrived with the **same recurring structural problems** (five patterns, plus a sixth added after Ch7 Build cost three passes). This skill is the standard that fixes them, plus the orchestration recipe for applying it. Run it to pre-process a chapter before the author reads, so they read a structurally-sound draft instead of catching the obvious things by hand.

The proven exemplars — chapters that cleared the author's bar — are **Signal (`chapters/04-signal.qmd`)** and **Source (`chapters/05-source.qmd`)**. When in doubt about the shape, match those.

## The patterns (the audit checklist)

### 1. Disambiguate terms
One canonical term per concept. No conflated roles or artifacts. Check every coined/role/artifact term against the glossary (`chapters/appendix-glossary.qmd`) and the chapters already fine-tuned — the same concept must use the same word everywhere.
- **Smell:** two words for one thing (e.g. "human supervisor" vs. "Human Orchestrator"), or one word for two things; a coined term used before it's defined; a role introduced as if new when it already exists.
- **Fix:** pick the canonical term, use it consistently, define it once at first use. If the fix changes a term used in other chapters, that's a **propagation** — flag it (it may need a separate sweep before deploy, like the Signal Backlog→Constraint Backlog and human-supervisor→Human Orchestrator renames).

### 2. Stepwise teaching pattern

> **This template is the DEFAULT, not a law.** It's here because it usually serves the reader — not because every teachable process must wear it. Apply it where it propels the reader forward; depart from it where the material calls for something else (compress over-templated steps, drop a heuristic/table that adds friction, vary the shape). The **prose-craft judge** is the arbiter of whether the structure is serving the reader or being applied mechanically. When in doubt, follow the template; when the judge flags drag, trust the judge.

Every teachable process follows **FRAME → ROADMAP → per-step TEACHING → worked EXAMPLE**:
- **Frame** — what the artifact/process *is* and how it connects to what came just before, *before* the how-to (not buried below it).
- **Roadmap** — the `<!-- moves:slug -->` block: the steps as an at-a-glance scannable list.
- **Per-step teaching (THE canonical template — follow exactly):** after the roadmap, EACH step gets **its own `###` subsection** structured as:
  1. **Intro — what it means and why.** A short framing of the step (1–3 sentences).
  2. **Varied bulleted examples.** Multiple, *generic/varied* examples (different roles/functions) so the reader sees the shape — **NOT** a single Meridian instance woven in. Meridian is the *worked example later*, not threaded through every step.
  3. **For a decision-step (a step with options)** — define EACH option (what it means, when to use it), each with its own bulleted examples. (e.g. for "Set the autonomy level": define AI-Assisted — what it means, when to use it, examples; then Automated — same.)
  4. **A rule-of-thumb heuristic.** Because the reader is making a *new* kind of decision, give them a heuristic for making the call.
  5. **Optional table** if it helps the decision.
  The litmus test: **the reader can DO this step, step by step, from the page + the workbook.** If they can't act on it, it isn't taught.
- **Worked example** — AFTER the per-step teaching, the central artifact filled in for Meridian, as the culmination (one place, narrative).
- **The shape the author specified (verbatim model):**
  ```
  ### Name the role/function as an outcome, not a task
  Intro / what it means / why
  - example
  - example
  - example
  ### Set the autonomy level
  Intro / what it means / why
  - autonomy option: what it means, when to use it.
      - example
      - example
  - autonomy option: what it means, when to use it.
      - example
      - example
  Rule of thumb for making the decision (new information → people need a heuristic)
  {table}
  ```
- **Smell:** a moves block of one-liners with no per-step subsections; the artifact defined *after* its how-to; a Meridian instance jammed into every step instead of generic varied examples + one worked example; a decision-step with no per-option definitions and no heuristic; "names four things" vs. "six steps" count mismatches left unreconciled or belabored on the page.
- **Fix:** add the frame up top; keep the moves block as the at-a-glance roadmap; give each step its own `###` subsection per the template above (intro → varied bullet examples → per-option definitions + heuristic + table for decision-steps); land ONE Meridian worked example after.

### 3. Remove redundancy
Each idea stated once. Cut restatement, throat-clearing, recap rituals, and prose that narrates what a diagram already shows.
- **Smell:** the same claim made 3–6× (e.g. an ownership rule restated in the In-Brief, the section, the moves block, and a callout); "The diagram makes three things visible: …"; a chapter-ending "That's one X, one Y, and a Z" recap; re-listing the In-Brief's contents in the body.
- **Fix:** state it once at full strength; everything else becomes a one-clause callback or is cut. Note: per-step *teaching* (pattern 2) is NOT redundancy — distinct concrete how-to per step is new content, not restatement.

### 4. Meridian narrative
The running example (Meridian Manufacturing / Elena Ruiz) appears as **narrative interstitials with headings**, woven through the steps — not as dropped-in tables with no lead-in.
- **Smell:** "Here's how Meridian populated the worksheet:" followed by a bare table; the example bouncing between companies with no transitions.
- **Fix:** give each Meridian beat a short narrative lead-in and a clear sub-heading; carry one example through the steps; each other example (SWP, Julie's M&A work, etc.) used once with a distinct job.

### 5. Progressive Canvas/artifact excalidraws
The chapter's central artifact rolls up to a **Sprint Planning Canvas row**, and is shown as a **progressively-filled black-and-white excalidraw** built stepwise as you move through the steps/functions (the Signal Constraint-Backlog funnel and the Source Knowledge-Map Pass 1→2→3 series are the models).
- **Smell:** a static end-of-chapter table only; no visual of the artifact building; no statement of how the artifact rolls up to the Canvas.
- **Fix:** author progressive-fill excalidraws (B/W house style — see the `compound-design-system` skill and any existing `excalidraw/chNN-*.excalidraw` for the JSON format: `strokeColor #000000`, transparent fills, `roughness 0`, `fontFamily 1`, white canvas); state once that the artifact is the work behind its Canvas row and gets packaged forward.

### 6. Declared architecture matches actual architecture
The chapter's framing sentences must describe the structure the chapter actually has, and the relationship between its instruments/lists must be stated, not left implicit.
- **Smell:** a frame sentence claiming a count the H2s contradict ("Build runs on two instruments" followed by four co-equal numbered instruments); several numbered sets presented as peers with nothing saying how they relate or in what order the reader uses them; a forward pointer that apologises for the structure ("the environment pick is taught later in this chapter"); one question taught two or three times as if it were two or three different decisions.
- **Fix:** find the organizing idea the chapter is already using silently and say it. Ch7's four instruments were really **one document and three gates on it**, each gate testing a different subject at a different moment — the spec audit tests the *document* (six of its seven checks re-ask "did you fill in Section N"), the guardrails test the *permissions*, the Done Test tests the *built system*. Then make it visible: gate-carrying H2 headings, one subject/when/asks table, a numbered sequence, and a diagram that shows the shape rather than a flat pipeline of peers.
- **Why this pattern is here:** Ch7 took THREE passes and two 3/5 author ratings. Passes 1 and 2 improved sentences inside a broken architecture and the author's complaint did not move. This is the single highest-cost defect class in the project so far. **Check it first.**

### Craft metrics — measure, never guess
Run `/usr/bin/python3 .claude/tools/prose_rhythm.py <chapter>` and compare against the exemplars, at audit time and again before the author reads:

| Metric | Target | Why |
|---|---|---|
| Nominalization (Williams) | **≤ 2.8 /100 words** | Both exemplars sit at 2.8. `≥ 3.6` prints "heavy". This is the measurable form of "complex, boring, not enough active verbs" — abstract `-tion/-ment/-ness` nouns that bury the actor. Ch7 sat at 3.7–3.9 through two passes while the tool printed "heavy" into a report nobody read. |
| Flesch reading ease | **≥ 58** | Source 58.4, Signal 65.8. |
| Prose words | **≤ 6,200** | Source 6,166; Signal 4,514. |
| Enumerated items taught | **≤ ~15** | Ch7 had 27 across four instruments and the reader could not file them. |

A clean Vale/voice scan is evidence that no banned string is present. It is **not** evidence the prose is good.

## Standing house rules (always apply)
- **Jargon** — plain-English gloss inline at first use (RAG, API, MCP, tokens, embeddings, agent…). See the `jargon-house-rule` memory.
- **Bullets** — dense comma-lists and question sets become bullets.
- **In-Brief** — summarizes; never overstates ("that single rule is all Design does" → it's one of N).
- **Close** — 2–4 reflection questions that apply the chapter to the reader's business, then a one-line handoff. No recap summary.
- **Narrative voice** — first-person blended; name the author inline in prose ("Jesse was in our L10…", "I sat in on a meeting…"); NO "Jesse:"/"Julie:" colon-label speaker prefixes (A17 — auto-reject). "We" when both authors. See `_julie/voice-charter.md` A17 and Vale rule `SpeakerLabel.yml`.
- **Voice** — `_julie/voice-charter.md` (declarative operator voice, contractions, em-dashes sparingly, forbidden vocab incl. "leverage"/"transformation"); craft per `_julie/prose-craft-charter.md`.
- **EOS** — agnostic by default; one optional familiar-paradigm bridge per concept.
- **Meridian/Elena** is the deliberate through-line — never cut as "redundancy."
- **Moves blocks** are registered in `_julie/process-spines.md`; keep labels in sync (skill `sync-process`).

## The orchestration recipe

**Model routing:** Heavy passes — the drafter, the judge trio (voice-scanner / prose-craft / editorial-coherence), and the reconcile-implementer — run on **Fable** (`claude-fable-5`): 1M context holds the whole chapter + skill + charter + prior chapters, and stronger judgment catches mechanical or over-templated application. Cheap mechanical work — diagram authoring, greps/renders/renames, worksheet renders — runs on **Sonnet** for cost. The orchestration seat may also run on Fable.

1. **Audit** — dispatch the `chapter-auditor` agent (read-only). It produces a findings + fix-plan report at `.claude/output/structure-audit-<stem>.md`: per-pattern findings with line refs, a drafter brief, a diagram list (new/redrawn progressive excalidraws), a term-disambiguation list (with propagation flags), redundancy cuts, and Meridian-narrative gaps. Fan it out across several upcoming chapters in parallel to get ahead of the author's read.
2. **Settle concept forks** — if the audit surfaces genuine conceptual decisions (term consolidation, what an artifact *is*, structure), raise them with the author via AskUserQuestion *before* drafting. (This is what the Signal noun-spine and ch6 role-consolidation discussions were.)
2b. **Propose the structure, and get the OUTLINE approved before any prose** — if the audit found a structural defect, dispatch an agent that loads `bmad-editorial-review-structure` to write `.claude/output/<stem>-restructure-proposal.md` (proposal only, no chapter edits): diagnosis, proposed section order with word budgets, **the organizing idea that relates the instruments**, scaffolding plan, nominalization plan with worked rewrites, cut list, open questions. Take the organizing idea + section order + open questions to the author via AskUserQuestion. **Do not draft until the outline is approved.** Flag in CAPS any author ruling that overrides the proposal's own recommendation, so the drafter can't quietly revert it. This gate exists because Ch7 burned two full passes polishing prose inside an architecture nobody had agreed to.
3. **Draft** — dispatch the `drafter` agent with the audit's brief (or the `draft-chapter` skill). Apply patterns 1–4; leave `<!-- TODO excalidraw: … -->` comments for diagrams. Remove `jf-note:` markers.
4. **Diagrams** — author the progressive excalidraws (parallel general-purpose agents, B/W house style), validate JSON, then wire shortcodes into the chapter.
5. **Gate** — `/usr/bin/python3 .claude/tools/voice-scan.py <chapter>` + `quarto render <chapter> --to html` (exit 0). Eyeball diagrams (rsvg-convert SVG→PNG, Read the PNG).
6. **Judge** — run the QUARTET in parallel: `voice-scanner`, `prose-craft`, `editorial-coherence`, and **`simplicity`** (Opus/high effort, loads `bmad-editorial-review-prose` and `bmad-editorial-review-structure`, owns nominalization, long sentences, weak verbs, missing scaffolding, unexplained connections, and passages that are simply boring). The simplicity seat was added after the author asked "I thought I had guardrails around a lot of this (eg skills to organize, simplify, etc)" — those skills existed and this pipeline had never invoked them. **The gate (step 5) + judge trio are NON-SKIPPABLE.** The model lacks the author's context and will apply these patterns blindly; this workflow is what catches those blindspots — especially the prose-craft judge catching Pattern 2 applied mechanically. Reconcile their findings yourself (protect canon + the consolidations); apply surgical fixes via an implementer.
7. **Author read** — present the finished chapter + the diagrams + any judgment calls. Nothing commits until the author reads. On their go: commit → merge to master → `bash bin/deploy.sh` (export the nvm PATH so `npx wrangler` resolves).
8. **Propagate** — if a term consolidation flagged in step 1 touches other files, run the focused rename sweep before merge/deploy (precedents: Constraint Backlog, Human Orchestrator).

## When to invoke
Fine-tuning or re-conceiving any chapter Co-Operating Model → end (Designing the Work, Build, Deliver, Compound, Rhythm, What-to-Do-Next, the case studies). The `ideal-customer-reader` agent is **complementary** — run it *after* the structural fixes to catch CEO-confusion/"so what" issues this pass doesn't cover.

## Persistence layers (survive compaction + sessions)
- **Executable pipeline:** `.claude/workflows/chapter-structure-pass.js` — invoke via `Workflow({name: "chapter-structure-pass", args: {chapter, mode: "produce"|"revise", auditPath, rulings, skipDiagrams}})`. It runs draft → diagrams → gate → judge trio → reconcile → re-gate with the model routing and canon guardrails baked in. Never re-author this pipeline inline; invoke the named workflow.
- **Cross-session state:** the `chapter-pass` bd formula (`.beads/formulas/chapter-pass.formula.toml`). One molecule per chapter: audit → **AUTHOR GATE forks** → produce → **AUTHOR GATE read** → jf-note rounds → **AUTHOR GATE approve** → handoff. Human gates block via bd; the author clears them with `bd gate resolve <gate-id>` (or you resolve on their explicit say-so in-session).

## Running a chapter molecule (tmux session bootstrap)
You are one of several parallel sessions, each owning ONE chapter molecule in a SHARED working tree on branch `edits/fine-tuning`.
1. `bd show <molecule-root>` → claim the first open step (`bd update <id> --claim`).
2. Follow each step's description verbatim. The step descriptions are the protocol; this skill is the standard.
3. **Scope rule:** edit only your chapter's `.qmd` (and its own `excalidraw/chNN-*` files). Anything cross-file → `bd create` with label `corpus-tie-up`. This is what makes parallel sessions safe.
4. Commit only your chapter's files; `git pull --rebase` before each commit (other sessions are committing too). If a per-chapter `quarto render` fails on a cache/lock oddity, retry once before debugging.
5. At author gates: park. Update the bead notes with exactly what the author needs to do, then wait for their input in your session.
6. Do NOT merge to master or deploy. The orchestrator ships the corpus after all molecules land and corpus-tie-up beads are swept.
