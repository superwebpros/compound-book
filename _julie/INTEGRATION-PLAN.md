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

## Decisions resolved (set 2026-05-24)

| # | Decision | Resolution |
|---|---|---|
| Q1 | Ch 12–15 structure | **Keep current.** Julie's Ch 12–13 → new case studies in appendix. Ch 14 → existing case-study files. Ch 15 → existing glossary. |
| Q2 | Ch 6 split | **Keep current split.** 06 (human/HAC) + 06b (hybrid/work). Most novel & foundational section of the book — preserve. |
| Q3 | Ch 11 §11.1/§11.2 | **TBD pending Ch 11 re-read.** Work Matters / JMann content likely doesn't fit. Joint "Compound Conversations" podcast is the more likely placement if any. |
| Q4 | E24 CH04-L10 | **Voice-shift only, no destructive change.** |
| Q5 | Case study expansions | **Move to appendix with TODO.** Will likely need Julie's source material to complete. |
| Q6 | Jesse About-the-Authors | **Move all About-the-Authors content to appendix.** Jesse to author his own entry. |
| Q7 | Anonymization convention | **Confirmed.** Julie's biographical refs use "global food safety company," etc. Meridian + PM-Agent stay as-is (fictional composites). |
| Q8 | Framework intros | **Consolidate.** Define once (likely glossary + first appearance), reference thereafter. Subagent in Phase 4 enforces consistency with how current frameworks are introduced. |

## Original decision table (with author notes preserved for reference)

| # | Decision | Recommendation | JF-Notes |
|---|---|---|---|
| Q1 | Ch 12–15 as numbered chapters vs. existing appendix/case-study structure | **Keep current structure.** Map Julie's Ch 12–13 → two new `case-study-*.qmd` files. Julie's Ch 14 → existing case-study files. Julie's Ch 15 → `appendix-glossary.qmd` additions. | Agree; keep current structure. Case studies belong in appendix |
| Q2 | Ch 6 split (Julie = 1 chapter; ours = 06 + 06b) | **Keep current split.** HAC + Right Seat → 06 (E33–35). TML + Pattern Drag at Design Gate → 06b (E36–37). | Keep our split; design as 2 separate chapters makes sense given the volume and distinction b/w the 'human' and 'technical' sides of work |
| Q3 | Ch 11 §11.1/§11.2 collision (Julie wants Work Matters / JMann as §11.1/§11.2, conflicting with current flow) | **Integrate as subsections under Clarity Call**, not as top-level §11.1/§11.2. Preserve existing First-Sprint-Plan-centric flow. | I need to review this; TBD |
| Q4 | E24 touches CH04-L10 polished opening | **Voice-shift only, no destructive change.** Verify with author after voice-implementer pass; do NOT rewrite the L10 story itself. | Agreed |
| Q5 | New case studies (E56/E57) given as single dense paragraphs vs. existing fully-structured case-study format | **Outline → expansion required.** Julie's paragraphs are seed outlines. Expansion likely needs author input to avoid fabrication. Treat as separate workstream — do NOT ship as-is. | Agreed; let's stick in appendix with a todo |
| Q6 | Jesse's About-the-Authors entry referenced but missing | **Confirm with author.** Either it exists somewhere not in repo, or it needs authoring. | About the authos should be in the appendix |
| Q7 | Anonymization convention ("global food safety company", "global automotive supplier", etc.) | **Adopt Julie's convention for her biographical references.** Meridian/PM-Agent are already fictional composites — leave them. | Agreed |
| Q8 | Framework intros (TML, PIS, Pattern Method, Right Seat, COE) repeat across 6+ chapters in Julie's redline | **Consolidate.** Introduce once with full definition (likely in 06 or glossary), reference thereafter. Avoid Julie's repetition pattern. | This is a bit more complex; should definitely be in the glossary. I would introduce once, reference thereafter. _Where_ we reference will have to be delegated to an agent in order to make sure we keep consistent with how we introduce other frameworks. |

## Phased execution plan

> Phase 0 (setup) and Phase 1 (manifest extraction) are **complete**. Branch exists, files staged, manifest written. Phases 2–5 require your approval before starting.

### Phase 1.5 — Codify the current voice (proactive voice protection)

Run `voice-scanner` on representative current chapters (Ch 1, 4, 7, 11) to extract the **live voice profile** — what Jesse's de-AI'd manuscript actually sounds like, ignoring the I/we variable.

Output: `_julie/voice-charter.md` — codified voice profile + forbidden AI patterns (from `julie-final.md` review). Every implementer agent writes **to** this charter, not just gets scanned against it.

This converts voice protection from reactive (catch drift after) to proactive (write to spec).

### Phase 1.6 — De-AI risk map on Julie's proposed prose

Julie's redline gives substantial "proposed prose" verbatim for most NEW-SECTION E-rows. Author review of `_julie/julie-final.md` confirms this prose has AI smell that must be scrubbed before integration.

Run `ai-tell-scan` on `_julie/julie-final.md` and the NEW-SECTION paragraphs in `_julie/julie-redline.md`. Output: `_julie/julie-prose-risk-map.md` — per-paragraph risk verdict (Clean / Light edit / Heavy rewrite / Reject).

Feeds Phase 2 so each NEW-SECTION bead inherits an inline rewrite requirement.

### Phase 1.7 — Stale-reference audit

Subagent runs `git log --grep`, `git log -S`, and repo grep for previously-struck terms (Greenline, "Ahmed", any pre-rename Meridian variants). Cross-checks persistent memory (`ch11-greenline-fabricated`, `meridian-consulting-group-is-meridian-manufacturing`, `ahmed-story-is-chutes-and-ladders`) against current prose.

Output: `_julie/stale-audit.md` — list of stale references + recent decision context that the merge must not regress.

### Phase 1.8 — Author-question research

Single subagent answers 5 research-tractable questions before bead activation (E21, E23, E26, E39, E43). Output: `_julie/author-questions-answered.md`. Remaining BLOCKED rows go to Julie directly.

### Global rule — framework components do not get individual attribution

Both authors share IP on every framework. Reject all "this came from Julie's 20-year practice" framings around HAC, TML, Right Seat Evaluation, Pattern Method, COE. Frameworks themselves can land; the attribution framing cannot.

Applies to: E29, E31, E34 (already rejected), E36, E37, E44, E46, E49, E55. Each of these beads requires framing scrubbed in acceptance criteria.

### Phase 2 — Per-chapter reconciliation (analysis only)

Spawn one subagent per chapter affected. Each reads the current `.qmd`, the relevant E-numbered rows, the voice charter, the prose risk map, and the stale audit — then produces `_julie/per-chapter/NN-chapter.md`:

**On the "syncing" question:** No syncing needed. Current `.qmd` is canonical source of truth. Phase 2 is **non-destructive overlay analysis** — each subagent reads the chapter as-is, overlays the E-rows from the manifest, and tightens landing points. The chapter doesn't move during Phase 2. Edits happen only in Phase 4, governed by beads.

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

1. `voice-implementer` agent picks up VOICE-SHIFT and ATTRIBUTION beads `jf-note: We may want to do a voice scan in advance to make sure that we keep the overall voice (eg code it) so that we have a pro-active approach to voice as opposed to just a reactive one.`
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

- Each chapter is a separable session — no need to load the whole book per task `jf-note: We have a skill for coherance check; we'll need to run that on a per-chapter basis, but also across the book once it executes.`
- Beads carry full inline context so execution sessions don't reload the manifest
- Per-chapter reconciliation files are throwaway scaffolding; once beads are created, they can be archived `jf-note: I'd argue the same is true for "_julie" folder once we've completed the work.`
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
