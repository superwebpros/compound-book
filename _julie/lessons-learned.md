# Julie Merge — Lessons Learned

Running audit trail of catches per chapter: what surfaced, where, and how it got encoded into source material. Updated after each chapter execution.

The purpose of this doc is to spot **recurring patterns** that signal a missing rule, and to inform future updates to the voice charter, agent definitions, or workflow.

---

## Chapter: Preface (`index.qmd`)

**Executed:** 2026-05-25
**Scout plan:** `_julie/per-chapter/00-preface.md`
**Execution mode:** Solo Path A Drafter (general-purpose Agent, Sonnet)
**Voice scanner pass:** yes
**Iterations:** 4 (initial Drafter → 1st author review → refinement → 2nd author review → final commit)
**Final commit:** `bcf8f11`

### Catches by category

**Category 1 — Author-only catches (philosophical / substantive):**

1. **Means/ends conflation in para 13.** Drafter wrote "This book is about the design work" — treating the system as the destination. Jesse caught it: the book is about a framework that produces operator outcomes (top-line and bottom-line growth without adding headcount). Design is means; growth is end.
   - **Encoded as:** charter anti-pattern A13 (Means/ends conflation); Scout opener/closer special check.

2. **Unqualified AI agency in para 23.** "Neither chooses. AI does." overstated AI autonomy and contradicted the book's own design-work argument.
   - **Encoded as:** charter anti-pattern A15 (Unqualified AI agency).

**Category 2 — Metaphor / precision catches:**

3. **Metaphor literalism violation in para 11.** "No seat for the developer's knowledge, no seat for a coherent operating model" — knowledge and operating models don't have seats. Drafter extended the metaphor past its semantic boundary.
   - **Encoded as:** charter anti-pattern A14 (Metaphor literalism violation).

4. **Book-as-location metaphor in para 15.** "You'll leave with the Sequence..." Books are artifacts with pages, not places.
   - **Encoded as:** charter anti-pattern A16 (Book-as-location metaphor).

5. **Adjective specificity in para 13.** "Design is how you get there" — too broad. "Operating design" ties to the book's specific framing (operating model from Julie's story).
   - **Encoded as:** noted in commit message; not a global rule (too narrow).

**Category 3 — Pattern-mechanical catches (voice scanner found these):**

6. Em-dash density: 16 in first Drafter pass → 7 final. Voice scanner flagged 3 paragraphs with >2 em-dashes.
7. A3 triplet pileups: 3 instances (para 7 "he was ready / architecture / practices"; para 9 "Those aren't the same thing / org chart / operating model"; para 23 "spreadsheet / CRM / Neither chooses / AI does").
8. A4 boastful biography: "before teaching them to anyone else."
9. A5 AI smell: "sitting at the precipice," "future of work itself," "machines that can think," "raw ingredients for something that has since evolved."
10. A11 inflated symbolism: "sitting at the precipice."
11. Hedged constructions: "What you will leave with is..."
12. Forbidden vocab leakage: "leverage" (author-introduced in own edit), "transformations," "org design."
13. Canonical capitalization: "Co-intelligent Co-operation" → "Co-Intelligent Co-Operation."
14. Missing contractions: "That is" → "That's."

### Mechanical-check additions

The voice scanner caught categories 3 reactively. To shift these to proactive (caught by the Drafter before reporting), three mechanical self-checks were added to `voice-implementer.md` pre-completion checklist:

- Em-dash density grep (target ≤8–10 per chapter; ≤1 per paragraph unless deliberately calculated)
- A3 triplet self-count (any sequence of 3+ short parallel sentences)
- Forbidden vocab grep (charter §3 list, case-insensitive)

### Workflow observations

- **Solo Path A Drafter execution was sufficient.** The two E-rows originally tagged Path B (Design Table) — E03 (Julie's founding story) and E06 (closing bio) — landed clean with solo Drafter. The Design Table machinery was not needed. Confirmed: default to Path A, reserve Path B for genuinely contested substance only.
- **Author iteration is unavoidable for Category 1 catches.** Philosophical/substantive judgment calls require human review. The Drafter cannot self-catch "means vs ends" without an explicit rule — which is why A13 now exists.
- **Inline `scout-note:` + `jf-note:` review pattern works.** Reviewing the manuscript with annotations in context (not in a separate plan file) lets the author make decisions in place. Render-safe (HTML comments would have hidden them); fenced code blocks (`​```scout-note:`) made them visible.

### Open questions / pending observations

- Will A13 (means/ends) recur in chapter openers? Likely yes — every chapter opener is at risk of system-as-destination framing. Watch Ch 1, Ch 2, Ch 11 closely.
- Will A14 (metaphor literalism) recur? Probably less often — it was tied to a specific extension; future chapters may use different metaphors.
- Will A15 (unqualified AI agency) recur? Very likely — AI-as-agent is a central frame; multiple places will tempt unqualified statements.
- Will A16 (book-as-location) recur? Unlikely after the first chapter; the metaphor mostly lives in framing language ("leave with," "walk away with") that's bounded to Preface and Ch 11.

---

## Chapter: Ch 1 — The Diagnosis (`chapters/01-diagnosis.qmd`)

**Executed:** 2026-05-25 → 2026-05-26
**Scout plan:** `_julie/per-chapter/01-diagnosis.md`
**Execution mode:** Solo Path A Drafter (general-purpose Agent, Sonnet)
**Voice scanner pass:** yes (LLM-only first; then Vale + Python pipeline introduced mid-execution)
**Iterations:** 5+ (initial Drafter → 1st voice-scanner LLM scan → 3 fixes → author redundancy/triplet review → pipeline build → 2nd scan via pipeline → triage pending)
**Final commit:** TBD (in triage)

### What caught what

| Layer | Catches |
|---|---|
| Author review (Category 1 substance) | Means/ends conflation in E14 opener (Drafter missed despite Scout flag); cross-paragraph redundancy ("three people, three tools, zero coordination" repeated; "The effort was real" repeated); cumulative antithesis pileup; long paragraphs hurting skim; 20-vs-30 years numerical inconsistency |
| LLM-only voice-scanner (whole-chapter pass) | 9 issues total: 1 em-dash overrun in E09, 1 A3 triplet in E09, 3 A5 AI smell patches, 1 "augment" forbidden vocab, 1 E14 means/ends FAIL, 1 negative parallelism cumulative count, 1 E15 author-confirmation flag |
| **Vale + Python pipeline (introduced mid-Ch1)** | **54 deterministic flags**: 24 em-dash density paragraphs, 22 missing contractions, 5 antithesis constructions, 3 long paragraphs (>150 words), plus 4 n-gram phrase repetitions across non-adjacent paragraphs |

### Critical lesson — whole-chapter LLM scanning misses cumulative patterns

The LLM-only scanner caught 9 issues. The Vale + Python pipeline caught 54 (6× more signal). The gap is structural:

- **Counting is hard for LLMs** at 5K-word scale. "Negative parallelism appearing > 3 times" is deterministic; LLM estimates. Em-dash density per paragraph is exact; LLM samples.
- **Cross-paragraph pattern detection is weak** in a single LLM pass. The same phrase appearing in paragraph 17 AND paragraph 39 is a comparison task; LLMs lose paragraph 17 from active attention by the time they read 39.
- **Authors catch the substance; deterministic tools catch the patterns.** The pipeline should split the work: Vale + Python for what's deterministic; LLM for judgment (A1/A2/A4/A5/A12/A13/A14/A15); author for substance/coherence.

### Pipeline architecture introduced (encoded in CLAUDE.md)

Three-layer hybrid:
1. **Vale** (deterministic, per-paragraph + document-level) — 13 rules in `.vale/styles/Compound/*.yml`. Catches A3 antithesis, A6 fear/urgency, A7 book-report citations, A8 conjunctive-adverb pileup, A9 -ing tags, A10 recap rituals, A11 inflated symbolism, A16 book-as-location + em-dash density, paragraph length, forbidden vocab, missing contractions, exclamations.
2. **Python wrapper** (`.claude/tools/voice-scan.py`) — runs Vale subprocess + cross-paragraph n-gram phrase repetition + OpenAI text-embedding-3-small + cosine similarity. Outputs unified Markdown report at `.claude/output/voice-scan-<chapter>.md`.
3. **`voice-scanner` agent (LLM)** — judges only the patterns deterministic can't: A1, A2, A4, A5, A12, A13, A14, A15.

### Semantic similarity threshold calibration

- **0.85**: 0 findings on Ch 1. Genuine paraphrased redundancy is rare at this threshold.
- **0.80**: still 0 findings on Ch 1.
- **0.70**: 4 findings, all in 0.70–0.75 range — these are **topic overlap, not redundancy** (paragraphs in the same section discussing related ideas).

Verdict: **0.85 is the right default.** Lower thresholds surface noise. The n-gram layer catches the genuine exact-phrase repetitions that matter most.

### Grandfathered content nuance

54 Vale flags includes both:
- **Genuine fixes** (new prose with em-dash overruns, paragraphs that became too long during Drafter execution, antithesis cumulative count)
- **Grandfathered content** (em-dashes in Meridian case study narrative, formal phrasing in callout boxes, structured dialogue)

The voice charter §2 says existing manuscript em-dashes are grandfathered; new edits do not add. The pipeline doesn't know which is which — it flags everything. **Triage step required: author marks fix-or-grandfather per cluster.**

### Mechanical Drafter self-checks unreliable

The Drafter claimed in its self-check:
- "Zero triplets in new paragraphs" — wrong, E09 had one
- "Em-dashes were fine" — wrong, E09 had 2 (vs. 1-max rule)
- "A13 means/ends addressed" — wrong, E14 failed it explicitly

**Lesson:** The Drafter's pre-completion checklist (added after Preface) is not a substitute for the scanner. **The voice scanner MUST be a mandatory verification step**, not optional. Update AGENT-TEAM.md workflow accordingly.

### Cross-chapter pattern watch (updated)

| Pattern | Preface | Ch 1 |
|---|---|---|
| Means/ends conflation | ✓ (para 13) | ✓ (E14) |
| Metaphor literalism violation | ✓ | (not yet observed) |
| Unqualified AI agency | ✓ | (not yet observed) |
| Book-as-location metaphor | ✓ | (not yet observed) |
| Em-dash overuse | ✓ (16→7 fixed) | ✓ (24 flags still pending triage) |
| A3 triplet pileup | ✓ | ✓ (5 antithesis + 1 mechanical in E09) |
| Forbidden vocab leakage | ✓ (transformations, leverage, org design) | ✓ (augment, plus 22 missing contractions including some in author-introduced edits) |
| Hedged constructions | ✓ | partial (some) |
| A4 boastful biography | ✓ | ✓ ("every operating-model engagement" in E14) |
| Canonical capitalization | ✓ | (not yet observed) |
| Cross-paragraph phrase repetition | not yet measured | ✓ ("the work before the tool" L17 ↔ L39) |
| Long paragraph skim issue | not yet measured | ✓ (3 paragraphs >150 words) |

**Recurrence signal:** Means/ends conflation (A13) is now confirmed recurring across 2/2 chapters. Em-dash overuse and A3 triplet are recurring. Forbidden vocab leakage is recurring (mostly author-introduced). The new rules (A13–A16) and the Vale pipeline are doing real work.

---

## Cross-chapter pattern watch

Patterns that appear in **multiple chapters** are stronger signals for charter updates than one-off catches. Tracking:

| Pattern | Preface | Ch 1 | Ch 2 | Ch 3 | Ch 4 | Ch 5 | Ch 6 | Ch 6b | Ch 7 | Ch 8 | Ch 9 | Ch 10 | Ch 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Means/ends conflation | ✓ | | | | | | | | | | | | |
| Metaphor literalism violation | ✓ | | | | | | | | | | | | |
| Unqualified AI agency | ✓ | | | | | | | | | | | | |
| Book-as-location metaphor | ✓ | | | | | | | | | | | | |
| Em-dash overuse | ✓ | | | | | | | | | | | | |
| A3 triplet pileup | ✓ | | | | | | | | | | | | |
| Forbidden vocab leakage | ✓ | | | | | | | | | | | | |
| Hedged constructions | ✓ | | | | | | | | | | | | |
| A4 boastful biography | ✓ | | | | | | | | | | | | |
| Canonical capitalization | ✓ | | | | | | | | | | | | |

---

*End of running log. Update after each chapter execution.*
