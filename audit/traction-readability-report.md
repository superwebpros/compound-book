# Traction — Readability & Length Benchmark

Generated 2026-06-14 from ProHQ audiobook transcripts (`thirdPartyCourseName == "Traction"`),
via `/tmp/traction_readability.py`. Word counts aggregated from the per-segment transcript files
(the audiobook splits several chapters across multiple files). Flesch computed per segment.

**Purpose:** length + reading-level benchmark for *Co-Intelligent Co-Operation* (compare against
`audit/readability-report.md`).

## Per-chapter (aggregated)

| Traction chapter | Words | Flesch RE (segment range) |
|---|---|---|
| Ch 1 — The Entrepreneurial Operating System | 2,690 | 61.5 |
| Ch 2 — Letting Go of the Vine | 3,834 | 65.5 |
| Ch 3 — The Vision Component | 13,883 | 65.8–70.1 |
| Ch 4 — The People Component | 8,627 | 62.2–71.6 |
| Ch 5 — The Data Component | 3,483 | 63.1–65.7 |
| Ch 6 — The Issues Component | 5,035 | 62.3–70.0 |
| Ch 7 — The Process Component | 3,662 | 63.5–65.6 |
| Ch 8 — The Traction Component | 10,132 | 64.6–70.5 |
| Ch 9 — Pulling It All Together | 5,984 | 69.9 |
| Ch 10 — Getting Started | 2,093 | 59.8 |
| (front/end credits) | 72 | — |
| **TOTAL** | **~59,495** | **avg 64.2** |

- **Content chapters:** 10. **Total content words:** ~59,423.
- **Average chapter:** ~5,940 words — but extremely uneven (Vision 13.9k and Traction 10.1k are
  outliers; Getting Started 2.1k and the EOS overview 2.7k are the shortest).

## Traction vs. Compound (our book)

| | Traction | Compound (as of 2026-05-17) |
|---|---|---|
| Content chapters | 10 | 12 |
| Total chapter words | ~59,423 | ~45,572 |
| Avg words / chapter | ~5,940 | ~3,800 |
| Whole book | ~59,500 | 68,298 (incl. appendices + worksheets) |
| Avg Flesch RE | 64.2 | 63.5 |
| Reading level | ~8th grade | ~8th–9th grade |

**Read:**
- **Reading ease is a near-exact match** (64.2 vs 63.5) — Compound sits right in Traction's
  accessibility band. Good.
- **Compound chapters run shorter** (~3,800 vs ~5,940 avg) and there are more of them — a more
  modular structure than Traction's few long component chapters.
- Traction concentrates mass in two anchor chapters (Vision, Traction). Compound spreads it more
  evenly; the longest is Build (~6.0k), the shortest What-to-Do-Next (~2.4k).

## Caveats
- Source is the **audiobook** transcript, not the print edition; word counts approximate print but
  include narration artifacts (credits) and may differ slightly from the page.
- Compound figures predate phase-2 (no `02-beliefs`, new appendices, or recent chapter expansion) —
  re-run `audit/readability-report.py` for a current comparison.
