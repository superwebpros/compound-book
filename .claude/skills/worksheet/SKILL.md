---
name: worksheet
description: "Draft a per-process worksheet (.md source of truth) from a process-spine registry entry + its book section. Use when generating or revising a Compound worksheet, or as the drafting stage of the worksheet pipeline. Produces a consistently-structured worksheet whose step labels match the book by construction."
---

# Draft a Worksheet

A worksheet is the **detailed, fill-in-the-blanks** companion to a book process. Division of labor:
the **book** gives context + overview (the scannable "the moves" spine); the **worksheet** gives the
details (cells to fill, the exact questions, the done test). They must never drift — so the worksheet
uses the **canonical step labels from the registry verbatim**.

## Inputs (handed to you — do not go hunting)
- The process's registry entry from `_julie/process-spines.md`: name, chapter, **section anchor**, and
  the **ordered canonical step labels + the one-line "why" each**. Use those labels exactly.
- The book section the process is taught in (read ONLY that section — stay scoped).

## Output
`worksheets/<slug>.md` — the `.md` is the source of truth; `.html`/`.pdf` render from it for download.

## Canonical structure (match the three exemplars in worksheets/html/)
1. **Header line:** `Compound · <Stage> / <Process category>`
2. **Title** + a one-line subtitle (what this worksheet produces).
3. **Intro** — 1–2 sentences: what you'll capture and why it matters. Name the prerequisite (e.g.,
   "Get one constraint from Signal first").
4. **The steps** — one per canonical registry step, in order. Each step:
   - a **directive heading** = the registry step label (verbatim),
   - a one-line statement of the move (the registry "why"),
   - **numbered sub-actions** (1, 2, 3) — the concrete fill-in instructions,
   - **a real example** in a callout — reuse Meridian/Elena or the Julie cases already in the book;
     never invent new companies or numbers.
5. **"Before you call it captured/done"** — the verify test: someone else (or an agent) could do the
   work from what's written, without going back to ask.

## Rules
- **Labels are law:** step headings = the registry's canonical labels, character-for-character, so the
  book overview and the worksheet read as the same spine.
- **Details live here, not in the book:** the fill-in cells, the exact interview questions, the
  scoring tables belong in the worksheet. The book only summarizes the moves.
- **Plain English.** Audience: smart non-technical entrepreneur, often no engineer / no ERP.
- **Reuse existing examples** (Meridian/Elena, Julie's food-safety cases). No invented facts.
- Markdown source; keep it clean and render-safe. One worksheet = one process.

## Not your job
Inserting the spine into the book is a separate, downstream step (it appends a scannable "the moves"
overview at the registry's section anchor). Do not edit chapter files here.
