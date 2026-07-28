# Moved

The digital course spec that lived here is now its own repository:

**`superwebpros/compound-course`** — expected at `~/projects/compound/projects/compound-course`

It was migrated on 2026-07-28 from a single ~1,200-line `COURSE-SPEC.md` into an
[OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) knowledge
bundle: 124 concepts, one file per lesson, plain markdown with YAML frontmatter.

## Why it moved

**Lifecycle.** The book is in final revisions and should stop changing. The course is a living
product that gets partially rebuilt as AI tooling decays. Coupling them meant every course edit
noised up the book's history at exactly the wrong time.

**Context.** An agent producing one course asset had to load the entire spec. The bundle exists
so it doesn't — a lesson concept plus its links, and nothing else.

## What this repo still owns

The course bundle **references** these; it never copies them without pinning a commit SHA:

| Artifact | Path | Consumers |
|---|---|---|
| Process-spine registry | `_julie/process-spines.md` | worksheets, book moves-blocks, **the course** |
| Story canon (18 stories) | `.claude/output/story-inventory-dedup-*.md` | the book, **the course** |
| Voice charter | `_julie/voice-charter.md` | the book, **the course** |
| Worksheets (31) | `worksheets/` | the book, **the course** |
| Chapters | `chapters/` | the book, **the course** |

**Bead `book-thdc` ruling:** when `process-spines.md` and the story canon are promoted out of
their scratch directories, they move **within this repo** — not into the course bundle. Two of
three registry consumers live here.

Editing any of the above means checking whether the course bundle's `references/` need updating.
