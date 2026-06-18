---
name: sync-process
description: "Maintain a Compound process across its three linked artifacts (registry + worksheet + book how-to block) when real-world implementation feedback comes in. Use when a worksheet/process needs editing based on real-human use, or when a process changes and the book must stay in sync. Event-driven, one process at a time."
---

# Sync a Process

The living-loop maintenance skill. When you use a process with real humans and learn something, this
keeps the **three linked artifacts** in sync so the book, the worksheet, and the registry never drift.

## The triple (source of truth per process)
1. **Registry entry** — a row in `_julie/process-spines.md` (the canonical step labels — the contract).
2. **Worksheet** — `worksheets/<slug>.md` (the fill-in details; where real-world use lives).
3. **Book "how to" block** — `<!-- moves:<slug> --> … <!-- /moves:<slug> -->` in the chapter, at the
   registry's Section anchor (the scannable overview the reader sees).

The **slug** is the handle that ties all three together.

## Inputs
- The process **slug** (e.g., `write-build-spec`).
- The **change / learning** (what real use revealed).

## The loop
1. **Locate the triple:** registry row (grep the slug in `process-spines.md`), `worksheets/<slug>.md`,
   and the `<!-- moves:<slug> -->` block in the chapter (grep across `chapters/*.qmd`).
2. **Apply the change to the worksheet first** (`worksheets/<slug>.md`) — details live there.
3. **Decide the blast radius:**
   - **Detail-only** (a question reworded, an example improved, a cell added): update the worksheet,
     re-render, done. The registry and book block don't change.
   - **Spine-level** (a step added, removed, reordered, or relabeled): also update the **registry's
     canonical labels** for this process, then update the **book block** to match — find
     `<!-- moves:<slug> -->`, replace its labels with the new canonical ones (verbatim). Labels stay
     identical across registry + worksheet + book by construction.
4. **Re-render** the worksheet: `/usr/bin/python3 .claude/tools/render_worksheet.py worksheets/<slug>.md`
   (review render). The production html/pdf comes from the bundler pipeline separately.
5. **Render-verify** the affected chapter if you touched it: `quarto render chapters/<file>.qmd --to html`.
6. Report what changed in each artifact + whether it was detail-only or spine-level.

## Rules
- **Labels are law and shared:** registry = worksheet headings = book block headings, character-for-character.
- **Book block stays a scannable overview, not a re-teach** — the chapter's detailed prose carries the detail.
- Never change a slug (it's the cross-artifact key). If a process genuinely splits/merges, update the
  registry deliberately and re-anchor.
- Keep everything Quarto-safe and render-verified.

## Why this works
Because the book block is slug-anchored and the registry holds canonical labels, propagating a learning
from real-world use back into the book is **surgical** — find by slug, replace the block. That is the
payoff of the demarcated "how to" sections. (Generation is the `worksheet` skill + the fan-out workflow;
this skill is the ongoing maintenance counterpart — event-driven, per process.)
