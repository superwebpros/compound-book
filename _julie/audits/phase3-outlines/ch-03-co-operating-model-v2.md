# Ch 3 (Co-Operating Model) — Outline v2 (re-conception)

**Source file:** `chapters/02-co-operating-model.qmd` · **Branch:** edits/fine-tuning
**Supersedes:** `ch-03-co-operating-model.md` (Phase 3A — a light re-sequence that kept all six jobs; that sprawl is what the author is rejecting).
**Status:** author-approved direction (spectrum + relocation + equation-as-thesis); ready to draft after a final outline read.

---

## The problem we're fixing

The current chapter tries to be six things at once (vocabulary chapter, graft-vs-compound argument, agent-tech primer, role-sort instrument, parallelism argument, closing equation). The actionable heart is buried at ~60%, behind ~40% of abstract setup. Reader gets lost and bored.

## Thesis (now stated EARLY, as the chapter's organizing claim)

> **Co-Intelligence + Co-Operation + Rhythm = Compound.**
> When you combine human and machine intelligence (**Co-Intelligence**), design how they work together (**Co-Operation**), and run that on a standardized cadence of review (**Rhythm**), results **Compound**.

**This chapter owns the first two terms and the spectrum they live on.** Rhythm and Compounding are the rest of the book. The job here is to give the reader the *vision* and the *categories*: what Co-Intelligence and Co-Operation look like in practice, and the spectrum on which they're arranged — so a reader can look at their own shop and say "this operation could be *this* kind, that one could be *that* kind."

## Learning objective (bake into the In Brief)

By the end, the reader can:
1. **Define** a co-operating model.
2. **Contrast** it with a "traditional" operating model.
3. **Place** any operation on a spectrum from assisted → autonomous.

Builds on Ch 1 (operating problem, not tech problem) and Ch 2 (you're already a tech company; the operating-model gap).

---

## NON-NEGOTIABLE: hold the human and the AI sides *alongside* each other

The AI side is the novel part, so it's the easy thing to over-index on. Do not. The "**Co**" is the entire point — Co-Intelligence is *both* human and machine intelligence; Co-Operation is *both* human and agent ownership. Throughout, the human contribution Julie brings (judgment under ambiguity, context, relationships, taste, ethics, knowing what "good" is, the relational read no system holds) gets **equal weight and equal airtime** with the agent contribution. Frame: neither intelligence alone is enough; the combination is what compounds. This connects to Ch 2's "elevate the work for your people" — humans aren't displaced, they're moved up to the judgment. Every table is two columns for a reason; every spectrum mode still has a human owning the outcome.

---

## The spectrum (centerpiece) — grounded in real SWP workflows

Axis = **where the human sits relative to the loop** (generation → review → adjustment). A human owns the outcome at every stop; what moves is the human's position.

| Mode | Where the human sits | Real example (anonymized) |
|---|---|---|
| **Assisted** | *In* the loop, every step. AI is a power tool (a chat client). | Drafting social posts with Claude, then reviewing/approving each one in the publishing tool before it goes out. (KB 1514, Mixpost pattern.) Also: the Ch 1 "three tools, no coordination" world. |
| **Directed** | At the *top* of the loop, every cycle — directs agents, reviews every output. | Compound's marketing lead steering four agent workstreams (design, copy, research, video) toward one output. *(Keep — best Directed exemplar.)* |
| **Supervised** | At the *edge* — exceptions + final review. | The automated quote workflow: agents gather context, research, draft, and QA inside guardrails (a spend cap; a "scope + timeline present?" readiness gate that auto-pauses and asks a human when info is missing); the human reviews every final quote before it's sent. (KB 1521.) |
| **Autonomous** | *Above* the loop — owns design + monitoring, steps in by exception. | The billing/payments operation: runs continuously on triggers and timers, advances payment states, recalculates totals, and posts a weekly financial summary to the team channel; the human owns the design and watches the reports. (KB 1520/1522.) |

**Framing rules for the section:**
- **Map, not a ladder.** The right stop depends on the work, the stakes, and your Source/Design maturity. Some work should stay Assisted forever; not everything should go Autonomous.
- **The invariant:** a human owns the outcome and the split is designed on purpose. The difference is *where the human stands*, never *whether* one is accountable.
- Most companies today sit entirely at **Assisted**, uncoordinated (Ch 1). The co-operating model is the discipline of moving the *right* operations rightward, deliberately.
- The old "two patterns" (human-supervised / agent-supervised) collapse into modes **Directed** and **Supervised** — no longer a separate section.
- New diagram: a single spectrum graphic (absorbs the old `ch02-four-agent-teams`).

**Confidentiality on the KB examples:** describe the *patterns* only. No account IDs, file paths, API keys, workspace UUIDs, tokens, or real employee names. Anonymize pricing. (The subagent flagged real instances of each in the source docs.)

---

## Section outline (proposed)

> Legend: [KEEP] reuse prose · [COMPRESS] keep idea, cut length · [NEW] · [MOVE→] relocate to another chapter · [CUT]

### I. In Brief [REWRITE]
New LO + the thesis equation. Drop "map a role / run the sort" promises (those relocate).

### II. Hook — the coordinator redesign *(current L8–17)* [KEEP, light trim]
Perfect traditional→co-operating contrast, and it already holds both sides (the coordinator keeps the judgment/relationships; agents take the production). Lands: *the problem was the model, not the person.*

### III. The thesis, up front [NEW — promote the equation here]
State **Co-Intelligence + Co-Operation + Rhythm = Compound** as the organizing claim, and decode it in plain language. Tell the reader explicitly: this chapter is about the first two and the spectrum; Rhythm and Compounding come later. This replaces the buried closing equation.

### IV. Co-Intelligence — two kinds of intelligence, held alongside [COMPRESS from current §VI + §VII]
- **Humans bring** (the foundation, full weight): world model, judgment under ambiguity, context/history/relationships, strategy/taste/ethics, standards. Julie's lens: the relational/contextual read no system can hold. Callback to Ch 2 — this is the elevated work.
- **Agents bring** (the novel addition): memory at scale, pattern recognition across your data, tireless synthesis, speed. Crisp chatbot-vs-agent distinction (chatbot answers; agent works a loop you don't restart) — only as much as the spectrum needs. The transmission idea in one or two lines: agents execute on what's transmitted; the human carries the world model.
- The point: **Co-Intelligence is the combination.** Neither alone is enough.
- Keep the compact **"what each brings"** table (two columns, equal weight).
- [MOVE→ Source/Design] six agent parts, LLM deep-dive, Organizational Memory deep-dive, re-told developer-departure story. One-line pointer only.

### V. Co-Operation — how they work together [COMPRESS from current §VIII]
- The ownership split: **humans own outcomes; agents own tasks.** The human always owns the outcome — the invariant. Keep the compact **"what each owns"** table.
- Julie tag: years of watching teams hand judgment to process layers and lose the thing only the person inside the work can supply.
- Hold the balance: this is not "agents do everything"; the human sets the standard and owns the call.

### VI. The spectrum: assisted → directed → supervised → autonomous [NEW — centerpiece]
The table above, in prose: name each mode, where the human sits, the real (anonymized) example. Map-not-ladder + the invariant. New spectrum diagram.

### VII. The vision + what you can do now [NEW]
- The reader can now walk their operations and place each on the spectrum. The rest of the book teaches the skills (Signal finds where to start, Source builds the memory, the Design chapters draw the split, Build/Deliver run it) and the missing equation terms (Rhythm = the cadence; Compound = the payoff).
- Sell the vision, both sides held: humans elevated to judgment, agents carrying the rule-work, every operation placed on the spectrum on purpose, knowledge owned by the business.
- Light bridge to the Framework chapter (where Rhythm gets defined).

### VIII. Handoff → the Framework (six stages, one Sprint at a time).

### IX. Reflection Questions [REWRITE → spectrum placement]
(1) Place three of your operations on the spectrum — where does each sit today? (2) Pick one — where *could* it sit, and what's the gap? (3) Which operation would you never move to Autonomous, and what does that tell you about where human judgment is irreplaceable?

---

## Relocation (author-approved) — design instruments MOVE to the Design chapters

Not deleted — re-homed:
- **MOVE→ Design chapters** (`06-designing-the-system` / `06b-designing-the-work`): **Two-Column Role Sort**, **Calculate the Design Opportunity**, **Map the Hybrid Split** (all three are registered process spines), plus their Action Steps, the Project Coordinator cost example ($36K/yr), and the cost math.
- **MOVE→ Design chapters:** the full **Hybrid Accountability Chart** build (here: one-line preview at most).
- Ch 3 keeps a *preview* only: "the instruments for drawing the split live in the Design chapters."

**Propagation (same pattern as the Ch 2 take-stock removal):**
- `_julie/process-spines.md`: re-home the 3 process rows from `02-co-operating-model` to the target Design chapter(s); update anchors + chapter column.
- The 3 `<!-- moves:slug -->` blocks physically move to the Design chapter(s) at new anchors.
- Worksheets stay valid (processes survive, just relocate).
- Re-point cross-references.
- **OPEN:** which Design chapter takes them — System, Work, or split? (Role sort + cost → likely *Designing the Work*; HAC → *Designing the System*. Confirm when we get there.)

---

## Diagram impact
- **NEW:** spectrum graphic (assisted → directed → supervised → autonomous; human position relative to the loop).
- **UPDATE:** the equation diagram `ch02-the-equation` now reads **Co-Intelligence + Co-Operation + Rhythm = Compound** (three additive terms, was two). File a diagram bead.
- `ch02-three-layer-identity` (identity/activity/structure) likely **retires** with the collapsed vocabulary.

## Notes
- Net effect: materially shorter; front-loads concrete (hook → thesis → Co-Intelligence → Co-Operation → spectrum), cuts the abstract vocabulary and the tech-anatomy primer, relocates the instruments.
- Voice/house rules unchanged; gates run after drafting.
- Citations: 0–1 (the chapter is concretely loaded with real SWP examples; no HBR needed here).
