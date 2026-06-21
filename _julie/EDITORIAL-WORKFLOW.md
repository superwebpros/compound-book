# Editorial Workflow — Co-Intelligent Co-Operation

**Purpose:** the canonical "how we edit this book" reference. Read this first when picking up
editorial work (especially after compaction). Last updated 2026-06-18.

---

## Current state (2026-06-18)
- **Beta is LIVE:** `https://books.compoundorg.com`, tagged **`v0.9.0-beta`**.
- **`master`** = clean baseline (R3 restructure + worksheets + how-to spines + `.gitattributes`). Pushed.
- **Working branch for edits:** `edits/fine-tuning` (off master). Future work branches off `master`.
- The book: 13 core chapters + 2 case studies + appendices. Filename numbers ≠ book numbers (renumbered); cross-refs use **named** chapter references, not numbers.

## The three-stage model + Sprint
Four-stage model (Explore → Organize → Integrate → Compound) + the Compound Sprint with stages
**Signal → Source → Design → Build → Deliver → Compound**. Keep stage/phase names consistent across chapters.

---

## Source-of-truth artifacts (the system)
| Artifact | What it is |
|---|---|
| `_julie/voice-charter.md` | Voice canon. Read before any prose edit. |
| `_julie/prose-craft-charter.md` | Craft canon (clarity/simplicity/pacing), calibrated to Traction (CV ~0.56, nominalization ~3.2/100). |
| `_julie/process-spines.md` | **Registry** of 30 teachable processes: canonical step labels, chapter, section anchor, slug, spine-state. Drives worksheets + book how-to blocks. Includes the slug-anchored block convention. |
| `worksheets/*.md` | 27 per-process worksheets (source of truth; `.html`/`.pdf` render from these). |
| Book `<!-- moves:<slug> --> … <!-- /moves:<slug> -->` blocks | The scannable "how to" spine in each chapter, at the registry anchor. Reader-demarcated AND machine-addressable. |
| Memory entries | `book-chapter-flow-and-meridian-thread`, `beliefs-chapter-identity`, `jargon-house-rule`, `eos-positioning` — load these. |

## Skills (`.claude/skills/`)
- **`draft-chapter`** — reorganize a chapter from its Phase-3A outline under the house rules.
- **`worksheet`** — generate a per-process worksheet `.md` from a registry entry (labels verbatim).
- **`sync-process`** — maintenance loop: edit worksheet → (if spine changed) update registry labels → replace the `<!-- moves:slug -->` book block → re-render. Event-driven, per process.
- **`prose-craft`** — clarity/simplicity/pacing judgment review (Zinsser/Williams/Provost). Flags, doesn't rewrite.

## Tools (`.claude/tools/`, run with `/usr/bin/python3` — system python; Homebrew python expat is broken)
- `voice-scan.py <chapter>` — Vale + n-gram + OpenAI-semantic + **prose-rhythm** layer → `.claude/output/voice-scan-<stem>.md`.
- `prose_rhythm.py` — Provost sentence-variance + Williams nominalization + proselint (imported by voice-scan; calibrated to Traction).
- `deflourish.py <chapter> --apply` — AI-flourish removal. **Non-negotiable** final pass on any touched chapter.
- `paragraph-stats.py` — sentences/paragraph.
- `render_worksheet.py <ws.md>` — review-grade md→html → `worksheets/review-html/` (NOT production; production html/pdf is a separate bundler pipeline).
- `audit/readability-report.py` — textstat readability per chapter (needs `pip install textstat proselint`).

## Agents (`.claude/agents/`)
`drafter` (restructure, has Bash), `prose-craft` (craft judgment), `voice-scanner` (voice flags), `voice-implementer` (applies fixes — **NO Bash**), `editor` (structural cuts), `editorial-coherence`, `ideal-customer-reader` (prospect lens), `scout`, `substance-lead`/`voice-lead`/`reader-lead` (Design Table).

---

## The editorial pipeline (per chapter)
**Draft/edit → voice-scan (incl. rhythm) → prose-craft gate → fix-loop → deflourish --apply → render-verify → commit.**
- Gates auto-fix clear wins; surface judgment calls for the author (agreed model).
- `prose-craft` reports; `voice-implementer` (or a general agent) applies fixes.
- Always `quarto render <chapter> --to html` (exit 0) before committing.

## Worksheet ↔ book maintenance
Use **`sync-process <slug>`** when real-world feedback changes a process. The slug-anchored
`<!-- moves:slug -->` block makes the book edit surgical. Keep registry = worksheet = book labels.

## Validation
**Reading-team pass** = `ideal-customer-reader` fan-out (prospect lens) + synthesis → bead reconciliation.
Run after a batch of edits to confirm the prospect experience improved.

---

## Orchestration rules (learned this session — important)
- **Parallelize by CHAPTER, not by process**, when agents edit chapter files — multiple agents on the same file collide. (Worksheets are per-file so per-process is fine.)
- **Agents don't `git commit`** in fan-outs; the orchestrator **batch-commits** after (clean control, no races).
- **Worktrees** only when agents mutate the *same* files in parallel; for different-file work, skip them.
- **Pilot before fan-out** — prove the pipeline on 1–3 units, then scale.
- **Resume on failure** — `Workflow({scriptPath, resumeFromRunId})` re-runs only failed/changed stages.
- **Shell-running stages need Bash** — use `general-purpose`, NOT `voice-implementer` (no Bash). This bit us once.
- **Close beads on evidence** (reader-confirmed), not on faith.

## House rules (apply to every edit)
- **Headings:** directive, sentence case, one *italic* word, no numericals.
- **Jargon:** plain-English gloss + forward pointer (named-stage ref) at first use. One canonical "agent vs ChatGPT" line.
- **EOS:** agnostic by default; optional familiar-paradigm bridge (HAC↔Accountability Chart, Orchestrator↔Integrator≠equivalent, Signal↔IDS, Right-Seat↔GWC). Never a dependency.
- **Meridian/Elena** is the deliberate through-line — never cut as "redundancy."
- **Headcount Paradox:** Ch 1 (Diagnosis) owns the full thesis; everyone else callbacks only.
- **HBR/outside citations:** ≤ 1–2 per chapter.
- **No time-budget estimates.** **Don't edit case-study files** for core feedback. **Don't edit `_quarto.yml`** (collect title renames for one approval).
- Audience: smart non-technical entrepreneur, often **no in-house engineer / no ERP** — never assume either.
- North star: **simplify**. Match Traction's accessibility (~8th–9th grade).

## Build / deploy / infra
- **Render:** `quarto render` (HTML+PDF+EPUB → `_book/`). PDF needs xelatex + brand fonts.
- **Deploy (production, manual):** `bin/deploy.sh` → `wrangler pages deploy _book --project-name=compound-books --branch=master` → `books.compoundorg.com`. If the script ever fails on `set: pipefail`, it's CRLF — run the commands directly.
- **Line endings:** `.gitattributes` forces LF; this clone has `core.autocrlf=false`. Keep it that way.
- **Git:** commit/push when the user asks; default branch pushes need explicit user go. End commits with the Co-Authored-By trailer. Beads: `bd`, then `bd dolt push` + `git push` at session end.

## Open work (next)
- **Author read** of the beta — the main gate. Start with Source / Designing-the-System / Build (densest).
- **`book-lsly`** — author 8 missing excalidraw diagrams (their own branch): ch01-dimensions-split, ch06-hybrid-accountability-chart-intro, ch06-platform-decision, ch07-design-brief-example, ch07-design-brief-meridian, ch10-hybrid-org-today-meridian, cs-meridian-swim-lane, appendix-context-stack.
- **~30 open beads** under epic `book-8v6v` — residual polish (esp. the dense technical chapters' reading level).
- This branch **`edits/fine-tuning`** — author's fine-tuned edits as the read surfaces them.
