# Authoring Team Brief — Phase 3 (Consolidated)

**Date:** 2026-06-15
**Purpose:** One place to delegate from. Merges all three phase-2 analyses into a per-chapter punch
list mapped to beads. If you own a chapter, find it below and work its beads.

## The three source analyses (read for depth)
1. `_julie/audits/sprint-canvas-coherence-audit.md` — structural spine (named tool / Sprint Planning Canvas tie-back / closing artifact per chapter). Verdict: spine ~80% built; 4 gaps.
2. `.claude/research/readability-scorecard-compound-vs-traction.md` — length + reading-level targets vs *Traction*. Verdict: matches Traction; 4 technical chapters too dense.
3. `_julie/audits/arc-synthesis.md` — prospect read-through, 3 axes (A clarity / B get-moving / C artifacts). Verdict: editorially close, not structurally broken.
4. `_julie/audits/flow-pacing-synthesis.md` — internal flow vs the canonical template (hook→concept/context→how-to→example), pacing, simplicity, concrete-thread coverage. Verdict: spine sound; how-to arrives too late and concept gets re-argued before the reader can act.

## North-star reminders (from author direction / memory)
- **Canonical chapter flow:** hook/story → concept & context → how-to → example. **Simplify, simplify, simplify** — practical over comprehensive.
- **Meridian/Elena is the deliberate through-line.** Never cut it for "redundancy"; the gap is the front chapters that *lack* it.
- **The mindset chapter is "You're Already a Tech Company"** (not "The Four Beliefs") — it opens by convincing the reader they're already a tech/systems company, then makes the other shifts. It's our "Letting Go of the Vine." Bead `book-zsrx`.
- **Jargon house-rule** (memory `jargon-house-rule`): at first use of a technical term, give a one-sentence plain-English gloss in parentheses **+ a forward pointer to where it's covered in depth** (named-stage ref, not a bare chapter number). One canonical "agent vs. ChatGPT" line reused.
- **EOS positioning** (memory `eos-positioning`): **EOS-agnostic by default** — never require EOS knowledge; frame around "your operating system." Reference EOS **strategically** as an optional familiar-paradigm bridge ("if you run EOS, this is like X") for that target buyer — never load-bearing. Approved mappings (HAC↔Accountability Chart, Human Orchestrator↔Integrator, Signal↔IDS, Right-Seat↔GWC) in the memory.

## All work lives under ONE epic: `book-8v6v` (JF Print Feedback)
20 open children: 12 ARC beads + `.24` (spine visibility) + `.27` (fillable-artifact audit) + 6 flow/pacing/Beliefs beads (below).
*(Separate epic `book-ff63` = Julie-merge, different workstream. ~9 loose beads exist outside both — not part of this brief.)*

---

## Cross-cutting beads — do ONCE, apply everywhere (assign to one owner each)

| Bead | Fix | Priority |
|---|---|---|
| `book-tb8h` ARC#1 | Fix broken/circular cross-references (renumbering fallout) | **P1** |
| `book-ultm` ARC#2 | Define "agent" in plain English + standard "agent vs ChatGPT" line | **P1** |
| `book-xqxi` ARC#3 | Glossary/jargon pass (RAG, API, n8n, tokens…) + "you decide vs Build team handles" | **P1** |
| `book-rhko` ARC#5 | Embed blank fillable templates in-body (stop relying on Excalidraw-only) | P2 |
| `book-g404` ARC#6 | Build the EOS bridge once (HAC→Accountability Chart, Orchestrator→Integrator) | P2 |
| `book-8v6v.24` | Structural-anchor/spine-visibility pass (tool map + standardized In-Brief device) | P2 |
| `book-8v6v.27` | Coaching-ready fillable-artifact audit | P2 |
| `book-b4do` ARC#12 | Replace Excalidraw-only templates + "resources when it launches" hedge | P3 |

These five (ARC#1/2/3/5/6) resolve most of the per-chapter flags below at the source.

---

## Per-chapter punch list (ARC scores + which beads touch the chapter)

Legend: A=Clarity · B=Get-moving · C=Artifacts. ✅Pass ⚠️Risk ❌Fail. Flesch from readability scorecard.

| Chapter | A | B | C | Flesch | Beads touching this chapter |
|---|---|---|---|---|---|
| 01 Diagnosis | ⚠️ | ✅ | ✅ | 66 | ARC#1, ARC#2, ARC#10 (scorecard math) |
| 02 Beliefs | ⚠️ | ⚠️ | ⚠️ | 70 | ARC#2, ARC#6, ARC#7, ARC#8 (no closing action) |
| 03 Co-Operating Model | ⚠️ | ✅ | ⚠️ | 62 | ARC#3, ARC#6 |
| 04 Framework | ✅ | ✅ | ✅ | 69 | ARC#3, ARC#5, ARC#6, ARC#12 — *only full Pass; use as the model* |
| 05 Signal | ⚠️ | ✅ | ⚠️ | 67 | ARC#5, ARC#7 (AI bridge), ARC#9 (session), ARC#12 |
| 06 Source | ⚠️ | ✅ | ✅ | **59** | ARC#3, ARC#5, ARC#7, ARC#8 + **readability: shorten sentences** |
| 07 Designing the System | ⚠️ | ✅ | ⚠️ | **55** | ARC#3, ARC#5, ARC#6, ARC#8 + **readability** |
| 08 Designing the Work | ⚠️ | ⚠️ | ⚠️ | **57** | ARC#1, ARC#5, ARC#7, ARC#8 + **readability** |
| 09 Build | ⚠️ | ✅ | ✅ | **58** | ARC#1, ARC#3, ARC#5 + **readability** |
| 10 Deliver | ⚠️ | ✅ | ✅ | 64 | ARC#12 — *overall Pass; light touch* |
| 11 Compound | ✅ | ✅ | ⚠️ | 65 | ARC#2, ARC#5, ARC#6, ARC#9, ARC#12 |
| 12 Rhythm | ⚠️ | ✅ | ⚠️ | 63 | ARC#5, ARC#6, ARC#7, ARC#12 |
| 13 What to Do Next | ⚠️ | ✅ | ⚠️ | 73 | ARC#1, ARC#5, ARC#12 |
| Case: Meridian | ⚠️ | ⚠️ | ✅ | 55 | ARC#3, ARC#4 (reader bridge), ARC#6, ARC#11 |
| Case: PM Agent Team | ⚠️ | ❌ | ⚠️ | 54 | ARC#3, ARC#4 (**the only Fail** — add reflection+handoff), ARC#6, ARC#11 |

---

## Flow / pacing / simplicity beads (from analysis #4)

| Bead | Fix | Priority |
|---|---|---|
| `book-zsrx` BELIEFS | Retitle "You're Already a Tech Company" + reorganize around the tech-company shift; add closing action; Meridian sentence; Headcount → callbacks | **P1** |
| `book-0fq9` FLOW#1 | Lead with practice — reorder heavy/late chapters so how-to precedes deep concept, pull first action earlier (Build, Co-Op, Framework, Diagnosis, Design-System, 06b, Signal) | **P1** |
| `book-3w1t` FLOW#2 | Source simplicity rescue (cut/merge knowledge-mgmt sections, PIS→1 sentence, resequence vocab) — only main-body Simplicity Fail | **P1** |
| `book-b8yy` FLOW#3 | Weave Meridian into front chapters that lack it (Diagnosis, Co-Op, What-to-Do-Next) | P2 |
| `book-bco3` FLOW#4 | Resolve Headcount-Paradox retread — Diagnosis owns, Beliefs/Compound/Rhythm/WhatNext callback only | P2 |
| `book-o81e` FLOW#5 | Trim three-beat outros, artifact dumps, In-Brief/reflection over-caps (Deliver, Compound, Co-Op, Rhythm, Meridian CS) | P3 |

### Flow/pacing scoreboard (Flow · Pacing · Simplicity · Concrete-thread)

| Chapter | Flow | Pacing | Simplicity | Thread |
|---|---|---|---|---|
| 01 Diagnosis | ⚠️ | ⚠️ | ⚠️ | ❌ |
| 02 Beliefs | ✅ | ⚠️ | ⚠️ | ❌ |
| 03 Co-Op Model | ⚠️ | ⚠️ | ⚠️ | ❌ |
| 04 Framework | ✅ | ⚠️(89% late) | ⚠️ | ✅ |
| 05 Signal | ✅ | ⚠️ | ⚠️ | ✅ |
| 06 Source | ⚠️ | ⚠️ | ❌ | ✅ |
| 07 Design-System | ⚠️ | ⚠️ | ⚠️ | ✅ |
| 08 Design-Work | ⚠️ | ⚠️ | ⚠️ | ✅ |
| 09 Build | ⚠️ | ⚠️ | ⚠️ | ✅ |
| 10 Deliver | ✅ | ⚠️ | ⚠️ | ✅ |
| 11 Compound | ✅ | ⚠️ | ⚠️ | ✅ |
| 12 Rhythm | ✅ | ⚠️ | ⚠️ | ✅ |
| 13 What to Do Next | ⚠️ | ⚠️ | ❌ | ❌ |
| CS Meridian | ✅ | ⚠️ | ⚠️ | ✅ |
| CS PM Team | ⚠️ | ❌ | ❌ | ✅ |

**Systemic:** how-to too late (5 chapters act past midpoint; Framework 89%); concept re-argued before action; only the front three + What-to-Do-Next lack the Meridian thread.

## How to delegate

1. **Assign the 5 cross-cutting beads to single owners first** (ARC#1/2/3/5/6). They each sweep many chapters; doing them once prevents per-chapter owners from solving the same thing 8 ways.
2. **Then assign chapters.** Each chapter owner works only what's left after the cross-cutting sweep — mostly chapter-specific items (scorecard math, Signal AI bridge, case-study activation).
3. **Order:** P1 blockers → P2 high-leverage → P3 completeness. The single highest-value quick win is **ARC#4** (activate the two case studies — fixes the only Fail).
4. **Use Ch 04 Framework as the reference model** — it's the only full Pass on all three axes.

## Open questions for you (Jesse)
- Want an explicit **per-chapter internal-flow / logical-organization** check? Neither ARC nor the coherence audit graded each chapter's internal ordering as its own axis — `.24` covers cross-chapter spine, not within-chapter flow.
- Should the ~9 loose beads (Ch02 instrument, deflourish tooling, case-study diversity, etc.) be folded under `book-8v6v` too, or kept separate?
