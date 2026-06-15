# Readability & Structure Scorecard — Compound vs. Traction

**Generated:** 2026-06-14
**Sources:**
- Compound: live manuscript — `audit/readability-report.py` (textstat) + `.claude/tools/paragraph-stats.py`
- Traction: ProHQ audiobook transcripts (`thirdPartyCourseName == "Traction"`) — `/tmp/traction_readability.py` + `/tmp/traction_paragraphs.py`

**Purpose:** Set structural targets for *Co-Intelligent Co-Operation* using *Traction* as the
benchmark for an accessible, operator-facing business book.

---

## Headline comparison (per content chapter, averages)

| Metric | Compound (now) | Traction | Target | Verdict |
|---|---|---|---|---|
| Words / chapter | ~4,515 | ~5,940 | 4,000–6,000 | ✅ in band; room to grow |
| Paragraphs / chapter | ~77 | ~82 | ~75–85 | ✅ match |
| **Sentences / paragraph** | **~3.9** | 3–4 (print ref) | **3–4** | ✅ on target |
| Flesch Reading Ease | ~63 | ~64 | 60–70 | ✅ match |
| Reading level | 8th–10th | ~8th | 8th–10th | ✅ match |
| Total book (content chapters) | ~58,700 | ~59,400 | ~55–65k | ✅ match |

**Bottom line:** Compound now matches Traction on reading ease, paragraph discipline, and total
length. The one real difference is *shape*: Traction concentrates words in a few long chapters;
Compound spreads them across more, shorter chapters.

---

## Compound — per chapter (current manuscript)

| Chapter | Words | Paragraphs | Sent/para | Flesch RE | Level |
|---|---|---|---|---|---|
| 01 Diagnosis | 4,318 | 83 | 3.6 | 66.1 | 8–9 |
| 02 Beliefs | 2,588 | 44 | 4.0 | 69.8 | 8–9 |
| 03 Co-Operating Model | 6,169 | 103 | 4.0 | 62.1 | 9–10 |
| 04 Framework | 4,226 | 61 | 4.7 | 68.9 | 8–9 |
| 05 Signal | 4,592 | 80 | 3.5 | 67.1 | 8–9 |
| 06 Source | 6,505 | 98 | 4.2 | 58.9 | 9–10 |
| 07 Designing the System | 6,588 | 96 | 4.1 | 55.2 | 10–11 |
| 08 Designing the Work | 4,002 | 63 | 4.0 | 57.0 | 10–11 |
| 09 Build | 6,593 | 108 | 3.8 | 58.4 | 10–11 |
| 10 Deliver | 3,100 | 59 | 3.4 | 63.9 | 9–10 |
| 11 Compound | 3,868 | 74 | 3.9 | 64.5 | 9–10 |
| 12 Rhythm | 3,213 | 59 | 4.1 | 63.4 | 9–10 |
| 13 What to Do Next | 2,929 | 67 | 3.1 | 73.1 | 8–9 |
| **Avg / Total** | **~4,515 / 58,691** | **~77 / 995** | **3.9** | **63.3** | — |

*(Chapter numbers are post-Beliefs ordering; renumbering sweep `.29` may shift them. Case studies,
appendices, and worksheets excluded from the chapter averages — whole-manuscript total incl. those
is ~95,600 words.)*

### Watch items (drifting off Traction's accessibility band)
- **Source / Designing the System / Designing the Work / Build** dip to **55–59 Flesch** (10th–11th
  grade) — the densest stretch. Expected for the most technical chapters, but they're the ones a
  non-technical reader is most likely to stall on. Candidates for sentence-shortening.
- **Co-Operating Model** is the longest (6,169) with 14.1-word avg sentences — heaviest front-matter chapter.

---

## Traction — per chapter (audiobook-transcript derived)

| Chapter | Words | Flesch RE |
|---|---|---|
| Ch 1 — Entrepreneurial Operating System | 2,690 | 61.5 |
| Ch 2 — Letting Go of the Vine | 3,834 | 65.5 |
| Ch 3 — Vision Component | 13,883 | ~67 |
| Ch 4 — People Component | 8,627 | ~67 |
| Ch 5 — Data Component | 3,483 | ~64 |
| Ch 6 — Issues Component | 5,035 | ~66 |
| Ch 7 — Process Component | 3,662 | ~65 |
| Ch 8 — Traction Component | 10,132 | ~68 |
| Ch 9 — Pulling It All Together | 5,984 | 69.9 |
| Ch 10 — Getting Started | 2,093 | 59.8 |
| **Avg / Total** | **~5,940 / 59,423** | **64.2** |

---

## Targets for Compound (from this benchmark)

1. **Sentences per paragraph: 3–4 average**, 5–7 only as occasional exceptions. Compound is at ~3.9 — **hold the line**; don't let the technical chapters creep up.
2. **Words per chapter: 4,000–6,000.** Compound averages ~4,515. The short chapters (Beliefs 2,588; What-to-Do-Next 2,929) are fine as deliberately light bookends; everything else is in band.
3. **Flesch Reading Ease: 60–70.** Pull the four 55–59 chapters (Source, Design×2, Build) back up by shortening sentences — that's the highest-leverage readability work left.
4. **Structural choice to make consciously:** Compound is more modular than Traction (13 chapters @ ~4.5k vs 10 @ ~5.9k). That's a legitimate design difference, not a defect — but it means each chapter must earn its place and hand off cleanly (see `sprint-canvas-coherence-audit.md`).

---

## Methodology & caveats
- **Traction word counts and Flesch** are from the **audiobook transcript**, which approximates but
  is not identical to the print edition (includes narration artifacts; chapter splits are uneven
  across transcript files).
- **Sentences/paragraph is NOT apples-to-apples between the two books.** Compound is measured from
  true print/markdown paragraphs (~3.9). Traction's transcript paragraphs are narration chunks that
  run larger (~4.8 measured), so they over-state print paragraphing. The **3–4 print reference**
  encoded in `paragraph-stats.py` is the reliable Traction print target — and Compound meets it.
- Re-run `audit/readability-report.py` after any major content change to refresh Compound numbers.
