# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A [Quarto](https://quarto.org) book project that produces *Co-Intelligent Co-Operation* (Jesse Flores & Julie Mann, Compound) in HTML, PDF, and EPUB. There is no application code — the repository is prose source (`.qmd`) plus a single Quarto config.

## Commands

Quarto CLI is required (`/usr/local/bin/quarto`, currently 1.9.37).

- `quarto preview` — Live-reload HTML preview while editing.
- `quarto render` — Build all configured formats (HTML + PDF + EPUB) into `_book/`.
- `quarto render --to html` — Build a single format (substitute `pdf`, `epub`).
- `quarto render chapters/02-stage-1-explore.qmd` — Render one chapter in isolation; useful for fast iteration on a single file.
- `quarto check` — Diagnose missing dependencies (TinyTeX for PDF, Pandoc, etc.).

PDF builds require a LaTeX install. If missing, `quarto install tinytex` provides one.

## Structure

- `_quarto.yml` — Book config: title, authors, chapter order, output formats. **Adding a new chapter requires editing the `chapters:` list here** — Quarto does not auto-discover files.
- `index.qmd` — Preface; first entry in the book.
- `chapters/NN-slug.qmd` — Numbered chapter files. The numeric prefix is for filesystem ordering only; the actual book order is whatever `_quarto.yml` lists.
- `_book/` — Build output. Gitignored. Never edit by hand.
- `.quarto/` — Quarto's cache. Gitignored.
- `assets/` — Cover image, brand logos, and the per-format style files (`brand.scss` for HTML, `epub.css` for EPUB, `preamble.tex` for PDF). The brand system itself is documented in `.claude/skills/compound-design-system/` — `assets/` is just the consumed/wired version.

## Brand wiring

- HTML uses `theme: [cosmo, assets/brand.scss]`. SCSS pulls Compound paper-field tokens (paper-warm canvas `#FAFAF8`, ink `#0A0A0A`, red `#E11D2D`) and Google-Fonts-loaded Archivo / Bricolage Grotesque / JetBrains Mono.
- EPUB ships `assets/epub.css` — same fonts via `@import`, reader-safe subset (many readers ignore custom CSS; fallbacks are system fonts).
- PDF uses `pdf-engine: xelatex` + `assets/preamble.tex` for color defs and Koma overrides. Brand fonts (Archivo, Bricolage Grotesque, JetBrains Mono) are resolved by name from system fonts — on a fresh machine, install with `brew install --cask font-archivo font-bricolage-grotesque font-jetbrains-mono` before rendering PDF, or xelatex errors with "font cannot be found."
- Link colors in PDF go through Quarto YAML (`urlcolor: compoundred`, etc.), not the preamble — Pandoc's template loads `hyperref` after `include-in-header`, so calling `\hypersetup` directly from the preamble errors.

## Editorial notes

- **Voice canon: `_julie/voice-charter.md`.** Read it before any prose edit. The charter codifies pillars, cadence, vocabulary, and 12 auto-reject anti-patterns extracted from the de-AI'd manuscript.
- The book is a four-stage model (Explore → Organize → Integrate → Compound) plus a "Compound Sprint" operational mechanism. Chapters cross-reference these stages and phases; when editing one chapter, check that terminology (stage names, sprint phase names like Signal/Source/Design/Build/Deliver/Compound) stays consistent with the others.
- Author voice is declarative and unhedged (see `chapters/01-introduction.qmd` for the established tone). Avoid softening edits that introduce qualifiers the surrounding prose doesn't use.
- **Em-dashes: use sparingly** (revised rule — see voice charter). They were previously the "editorial rhythm"; now they're a calculated tool, not a default.
- **Chapters end with reflection questions** (2–4 short questions that engage the reader to apply the chapter to their business), followed by a one-line handoff. No recap-style summaries.
- **Dual-author convention:** "Jesse:" / "Julie:" when a story belongs to one of them; "we" when both. Blended authorial voice for analysis.
- Diagrams will (soon) be authored as Excalidraw drawings. Default to **black and white** unless the chapter context explicitly calls for color.

## Voice scanning pipeline

Three-layer hybrid scanner for chapter voice compliance:

1. **Vale** (deterministic, per-paragraph + document-level). Config: `.vale.ini`. Custom rules: `.vale/styles/Compound/*.yml`. Catches em-dash density per paragraph, antithesis patterns, forbidden vocabulary, paragraph length, missing contractions, conjunctive adverb pileup, -ing tag clauses, recap rituals, inflated symbolism, book-as-location, fear/urgency, book-report citations. Install: `brew install vale`. Docs: <https://docs.vale.sh>.
2. **Python wrapper** (`.claude/tools/voice-scan.py`). Runs Vale subprocess, adds cross-paragraph n-gram phrase repetition (≥5-word overlap) and OpenAI embedding-based semantic similarity (cosine ≥ 0.85). Outputs unified Markdown report at `.claude/output/voice-scan-<chapter>.md`. Requires `OPENAI_API_KEY` in `.claude/.env` (gitignored) for the semantic layer; falls back to deterministic-only if missing.
3. **`voice-scanner` agent** (`.claude/agents/voice-scanner.md`). LLM judgment layer. Reads the Markdown report, judges patterns deterministic scanning can't catch: A1 abstract-noun=abstract-noun, A2 coined-term-before-stakes, A4 boastful biographical, A5 AI smell, A12 invented company beats, A13 means/ends conflation, A14 metaphor literalism, A15 unqualified AI agency.

Run: `/usr/bin/python3 .claude/tools/voice-scan.py chapters/01-diagnosis.qmd` (the system Python 3.9 — Homebrew's python@3.13/3.14 have a broken expat as of 2026-05).

Voice charter (canonical voice spec): `_julie/voice-charter.md`. Update the Compound style rules in `.vale/styles/Compound/` when adding new anti-patterns.

## Related skills

`.claude/skills/compound-design-system/` is available via the `compound-design-system` skill for Compound-branded visual assets (covers, diagrams, marketing mocks). Not needed for prose edits.


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
