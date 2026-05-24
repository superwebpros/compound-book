# Julie Feedback Integration Plan

**Branch:** `merge-julie-feedback`
**Manifest:** [`_julie/edit-manifest.md`](./edit-manifest.md) (60 edits, 8 open decisions)
**Source:** Julie's redline (`_julie/julie-redline.md`) — canonical edit list
**Reference:** Julie's "final" (`_julie/julie-final.md`) — only when redline is ambiguous

---

## Goal

Merge Julie Mann's feedback into the current book **without losing the weeks of polish** already in the canonical prose (jf-notes resolved, voice-scan passes, Meridian threading, fabrication replacement, excalidraw work). The current book is the source of truth for voice and structure; Julie's docs are the requirements input.

## Risk frame (why this isn't a clean merge)

Julie's redline doesn't know about recent edits. Three categories of risk:

1. **Voice drift.** Mechanically applying Julie's prose introduces AI-smell, hedging, and qualifier patterns the current voice has been scrubbed of. Every chapter touch must run the voice gate.
2. **Lost polish.** Wholesale-replacing a section nukes recent work (e.g., ch04 L10 opening, Meridian threading, PM Agent case study). Edits must be surgical — minimal diff, additive where possible.
3. **Structural divergence.** Julie numbers Ch 12–15 differently than us. Naively renumbering breaks the entire `_quarto.yml` and cross-references.

## Scope at a glance

- **60 actionable edits** (E01–E60) extracted from 27 editorial-note blocks
- **Risk:** 26 HIGH (new sections, framework adds, Ch 8 restructure) · 25 MED (voice/attribution, scoped new paras) · 5 LOW · 4 unclassified
- **New content:** 2 case studies, 7 glossary terms, About the Authors, 15-year content thread
- **Conflict flags:** 1 touches polished work (E24 → CH04-L10, voice-shift only, low-impact). 0 touch Meridian / PM-Agent / Greenline.

## Open decisions to resolve before execution

| # | Decision | Recommendation |
|---|---|---|
| Q1 | Ch 12–15 as numbered chapters vs. existing appendix/case-study structure | **Keep current structure.** Map Julie's Ch 12–13 → two new `case-study-*.qmd` files. Julie's Ch 14 → existing case-study files. Julie's Ch 15 → `appendix-glossary.qmd` additions. |
| Q2 | Ch 6 split (Julie = 1 chapter; ours = 06 + 06b) | **Keep current split.** HAC + Right Seat → 06 (E33–35). TML + Pattern Drag at Design Gate → 06b (E36–37). |
| Q3 | Ch 11 §11.1/§11.2 collision (Julie wants Work Matters / JMann as §11.1/§11.2, conflicting with current flow) | **Integrate as subsections under Clarity Call**, not as top-level §11.1/§11.2. Preserve existing First-Sprint-Plan-centric flow. |
| Q4 | E24 touches CH04-L10 polished opening | **Voice-shift only, no destructive change.** Verify with author after voice-implementer pass; do NOT rewrite the L10 story itself. |
| Q5 | New case studies (E56/E57) given as single dense paragraphs vs. existing fully-structured case-study format | **Outline → expansion required.** Julie's paragraphs are seed outlines. Expansion likely needs author input to avoid fabrication. Treat as separate workstream — do NOT ship as-is. |
| Q6 | Jesse's About-the-Authors entry referenced but missing | **Confirm with author.** Either it exists somewhere not in repo, or it needs authoring. |
| Q7 | Anonymization convention ("global food safety company", "global automotive supplier", etc.) | **Adopt Julie's convention for her biographical references.** Meridian/PM-Agent are already fictional composites — leave them. |
| Q8 | Framework intros (TML, PIS, Pattern Method, Right Seat, COE) repeat across 6+ chapters in Julie's redline | **Consolidate.** Introduce once with full definition (likely in 06 or glossary), reference thereafter. Avoid Julie's repetition pattern. |

## Phased execution plan

> Phase 0 (setup) and Phase 1 (manifest extraction) are **complete**. Branch exists, files staged, manifest written. Phases 2–5 require your approval before starting.

### Phase 2 — Per-chapter reconciliation (analysis only)

Spawn one subagent per chapter affected. Each reads the current `.qmd`, the relevant E-numbered rows, and produces `_julie/per-chapter/NN-chapter.md`:

- Confirms or revises the target line ranges (manifest gave best-guess; chapter-aware pass tightens)
- Classifies each E-row per chapter: ALREADY-DONE / SAFE-ACCEPT / VOICE-IMPLEMENTABLE / STRUCTURAL-NEEDS-AUTHOR / CONFLICT
- Drafts acceptance criteria specific to that chapter's polished state
- Flags any voice/coherence risk specific to that chapter

**Output:** 11 per-chapter files + 1 cross-cutting (E60 anonymization). No edits to chapter files.
**Effort:** ~30 min wall-clock (parallel subagents).
**Stop point:** Author reviews per-chapter findings before bead creation.

### Phase 3 — Bead creation

After per-chapter review approves the actionable set, create one bead per edit with:

- Full inline context (E-row, target file + lines, Julie's prose verbatim, acceptance criteria, conflict notes)
- Type label (`voice-shift`, `attribution`, `new-section`, `framework-add`, `anonymization`, `structure`)
- Priority by risk (HIGH = P1, MED = P2, LOW = P3)
- Dependencies wired (Preface E01–E07 block all chapter attributions; Q8-consolidated framework intros block per-chapter framework adds)
- `bd human` flag on anything STRUCTURAL-NEEDS-AUTHOR or CONFLICT

**Effort:** ~10 min (parallel subagents creating beads in batches).
**Stop point:** Author reviews bead list (or pulls `bd ready`) before execution.

### Phase 4 — Execution (per-chapter, sequential)

Process chapters in this order to manage dependencies and let voice land cleanly:

1. **Preface (E01–E07)** — establishes dual-author voice frame. All downstream attribution depends on this.
2. **Ch 1 (E08–E15)** — first chapter; sets voice precedent for chapters 2–11.
3. **Ch 2 (E16–E20)** through **Ch 11 (E51–E55)** — sequential, one chapter per work session ideally.
4. **Glossary additions (E58)** — after framework chapters land.
5. **About the Authors (E59 + Q6)** — needs author confirmation on Jesse's entry first.
6. **New case studies (E56–E57)** — separate workstream; requires author expansion.
7. **Anonymization sweep (E60)** — last; runs across all chapters at once.

Per-chapter loop:

1. `voice-implementer` agent picks up VOICE-SHIFT and ATTRIBUTION beads
2. `editor` agent picks up NEW-SECTION and FRAMEWORK-ADD beads
3. Quality gates run (see below)
4. If gates pass, commit chapter changes; close beads
5. If gates fail, re-loop or escalate to `bd human`

### Phase 5 — Final integration

- Cross-chapter coherence check (terminology, framework consistency, references resolve)
- Full `quarto render` (HTML + PDF + EPUB) and diff against baseline render captured pre-merge
- Update `_quarto.yml` if new files added
- Squash-merge or PR review of `merge-julie-feedback` → `master`

## Quality gates (per-chapter, after edits land)

Run in order; any failure halts merge for that chapter:

1. **`bmad-mkt-voice-scan`** (skill) — Jesse/Compound voice compliance. No new violations vs. baseline.
2. **`ai-tell-scan`** (skill) — no AI smells in new prose. Flag and fix before commit.
3. **`voice-scanner`** (agent) — flag report on Jesse Voice DNA. Zero MAJOR flags allowed; MINOR flags reviewed.
4. **`ideal-customer-reader`** (agent) — CEO-perspective pass. No new "so what?" or undefined-term flags.
5. **Render check:** `quarto render chapters/NN-chapter.qmd --to html` builds without error.
6. **Coherence check:** `bmad-mkt-coherence-check` (skill) on the diff — no cross-section contradictions introduced.
7. **Baseline diff:** text-only diff of rendered HTML against pre-merge baseline. Reviewer scans for "polish I lost" — lines removed vs. added ratio reasonable.

## Baseline snapshot (do once, before Phase 4 execution)

```bash
quarto render --to html
cp -R _book _baseline_book/   # captures pre-merge rendered text for diff comparison
```

Add `_baseline_book/` to `.gitignore` (not versioned; throwaway reference).

## Bead naming convention

When created in Phase 3:

- Title: `[E##] <type>: <≤8 word summary>` — e.g. `[E03] new-section: Julie founding story in Preface`
- Type field: `task` for voice/attribution; `feature` for new sections; `bug` for clarity/correction
- Priority: 1 (HIGH risk), 2 (MED), 3 (LOW)
- Each bead has Julie's prose, target lines, acceptance criteria inline — readable cold

## Escape hatches (when to stop and flag)

- **CONFLICT classification** in Phase 2 → bead created with `bd human` from the start
- **Quality gate fails twice** on same bead → escalate to `bd human`, do NOT keep rewriting
- **Voice-scanner reports MAJOR flag** post-merge → revert that edit, escalate
- **Polish-loss diff** showing > 20% prose removed for a section → manual review required before commit
- **Author input required** (case-study expansion, About-the-Authors Jesse entry, anonymization ambiguity) → bead held in `blocked` state until human resolves

## Context-window efficiency notes

- Each chapter is a separable session — no need to load the whole book per task
- Beads carry full inline context so execution sessions don't reload the manifest
- Per-chapter reconciliation files are throwaway scaffolding; once beads are created, they can be archived
- Subagent delegation pattern: scanner / implementer / reader are scoped tools — main session orchestrates, agents do the work

## What's done so far

- [x] Branch `merge-julie-feedback` created off `master`
- [x] `.gitignore` updated for `.DS_Store` and `full_book.md`
- [x] Julie's docs converted: `_julie/julie-redline.md`, `_julie/julie-final.md`
- [x] Edit manifest extracted: `_julie/edit-manifest.md` (60 rows + 8 decisions)
- [x] Integration plan: this file

## What's next (awaiting approval)

- [ ] Resolve Q1–Q8 (open decisions above)
- [ ] Phase 2: per-chapter reconciliation (parallel subagents)
- [ ] Phase 3: bead creation
- [ ] Baseline snapshot
- [ ] Phase 4: chapter-by-chapter execution

---

*Generated 2026-05-24. Update this doc as decisions resolve and phases complete.*
