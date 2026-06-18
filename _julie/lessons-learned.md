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

## Chapter: Ch 2 — The Co-Operating Model (`chapters/02-co-operating-model.qmd`)

**Executed:** 2026-05-25 → 2026-05-31  ·  **Scout plan:** `_julie/per-chapter/02-co-operating-model.md`  ·  **Final commit:** `b53ca0d`
**Iterations:** 3 (Drafter → editorial-coherence + surgical pass → author second/third-read fixes). **Down from Ch 1's 5–6.** New pipeline materially compressed iteration count.

### Canonical workflow (replicable for Ch 3 onward)

Sequence that produced clean Ch 2 in 3 iterations:

1. **Create Scout sub-bead** under `book-ff63.9`. Title: `Scout: Ch N <title> (NN-<slug>.qmd)`. Include in-scope E-rows, RELOCATED/REJECTED rows explicitly noted as out-of-scope, author manifest annotations, persistent-memory context.
2. **Dispatch Scout** (`general-purpose`, Opus). Reads: scout.md role, voice-charter A1–A16, manifest, prose risk map, stale audit, author-questions-answered, AGENT-TEAM, lessons-learned, the chapter, adjacent committed chapters for voice calibration, Julie's source paragraphs by line range, `bd memories`. §5 means-vs-ends check MANDATORY on opener/closer/concept-definition paragraphs. Output: plan file + inline `scout-note:` + empty `jf-note:` blocks. Render-verify. Close bead.
3. **Commit Scout output** (chapter with scout-notes + plan file).
4. **Author reads chapter** in editor, drops `jf-note:` responses inline, pushes back.
5. **Commit author jf-notes** as audit trail.
6. **Dispatch Drafter** (`general-purpose`, Sonnet). Reads voice-implementer.md (mandatory scanner gate), voice-charter, chapter with jf-notes, Scout plan, Julie's source paragraphs, adjacent chapters, lessons-learned, `bd memories`. Per-E-row author decisions explicit in prompt. Critical rules called out: MEANS/ENDS-RISK, A2 traps, framework-attribution, dual-author convention. Scanner BEFORE editing to baseline; AFTER editing to verify no new flags. Strip all scout-notes + jf-notes. Render-verify.
7. **Verify Drafter output** independently (residuals, render, scanner).
8. **Dispatch editorial-coherence** (`general-purpose`, Opus). Reads editorial-coherence.md role, voice-charter, Scout plan, chapter, scanner report. PRIMARY: substance preservation per E-row. SECONDARY: EC1–EC7 + manual I/we sweep. Output: report at `.claude/output/editorial-coherence-<chapter-stem>.md`.
9. **Apply surgical fixes** to top-priority editorial-coherence findings + I/we sweeps + structural fixes.
10. **Run scanner once more** to verify no regression.
11. **Commit cleanup pass.**
12. **Author second read** — typically surfaces 3–6 additional catches (substantive + AI-coded vocab + missed forward-references).
13. **Address author second-read notes** — smaller surgical fixes.
14. **Final commit + push.**
15. **Triage remaining Vale alerts** at cluster level (em-dash fix-all vs grandfather; contractions body-prose-only). Optional — depends on author appetite for chapter cleanup vs moving forward.

### Skills / agents per step

| Step | Tool | Model | What |
|---|---|---|---|
| 1, 5, 11, 13 | beads (`bd create/update/close`) | n/a | scoping + audit trail |
| 2 | Scout (via `general-purpose` + role file) | **Opus** | plan + inline notes |
| 6 | Drafter (via `general-purpose` + voice-implementer.md role) | **Sonnet** | revised chapter |
| 6 (within) | `voice-scan.py` mandatory gate | n/a | flag report |
| 8 | Editorial-coherence (via `general-purpose` + role file) | **Opus** | substance + EC report |
| 9 | Direct editor (main session) | Opus | surgical fixes |
| 10 | `voice-scan.py` verification | n/a | confirm no regression |

**Total spawned-agent runs per chapter: 3** (Scout, Drafter, editorial-coherence). Scanner invoked ≥2× (Drafter mandatory + my verification).

### What caught what on Ch 2

| Catch | Source |
|---|---|
| §5 MEANS/ENDS-RISK flags upfront (E17, E18, E19) | Scout |
| A2 traps (work deconstruction, HAC capitalization, Co-Intelligent Company redefinition risk) | Scout |
| Drafter intro'd 3 em-dashes / 2 long paragraphs / 2 n-gram repetitions → self-fixed | Drafter scanner gate |
| E17 Julie attribution dropped (chapter went 73 lines without her voice) | Editorial-coherence PRIMARY |
| E18 close inversion (means/ends regression) | Editorial-coherence PRIMARY + EC |
| E19 antithesis residue ("graft produced strain / redesign produced...") | Editorial-coherence PRIMARY |
| §2.6 80-line block needs H3 | Editorial-coherence EC5 |
| 7 I/we paragraphs Drafter missed | Editorial-coherence manual sweep |
| EC1 Compound Sprint forward-deployed | Editorial-coherence EC1 |
| EC2 TML Split Action Step redundancy | Editorial-coherence EC2 |
| EC4 mild "expect a reaction" patronizing | Editorial-coherence EC4 |
| L18–L24 "has a name" fragmentation | Author 2nd read |
| "Load-bearing" as AI-coded word | Author 2nd read |
| Missing table-to-prose transition L151 | Author 2nd read |
| L159/L165 redundancy | Author 2nd read |
| Action Step "CIA investigation" patronizing language | Author 2nd read |
| **TML acronym wrongly expanded (M+L gloss vs canonical Task/Management/Leadership)** | **Author 3rd read** — editorial-coherence missed because it verdicted "TML Split CLEAN" without checking definition against canon |

### Key lesson: EC1 canonical-definition verification (encoded 2026-05-31)

Editorial-coherence originally verified that *a* definition exists per coined term. Ch 2's TML proved this is insufficient — a wrong definition can pass the check. **Updated:** EC1 now requires verifying the definition matches the canonical definition from manifest, charter §3, glossary, or framework canon. See `.claude/agents/editorial-coherence.md` EC1 section.

### Iteration count compression confirmed

Ch 1: 5–6 iterations. Most catches surfaced in author review.
Ch 2: 3 iterations. Editorial-coherence + Drafter mandatory scanner gate caught most issues before author review. Author still surfaced ~6 catches on second/third read — some informed agent updates (TML canonical-definition catch led to EC1 refinement).

**This is the canonical workflow for the remaining 9 chapters.**

---

## Cross-chapter pattern watch

Patterns that appear in **multiple chapters** are stronger signals for charter updates than one-off catches. Tracking:

| Pattern | Preface | Ch 1 | Ch 2 | Ch 3 | Ch 4 | Ch 5 | Ch 6 | Ch 6b | Ch 7 | Ch 8 | Ch 9 | Ch 10 | Ch 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A13 Means/ends conflation | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | | | |
| A14 Metaphor literalism violation | ✓ | | | | ✓ | | | | | | | | |
| A15 Unqualified AI agency | ✓ | | | | | | | | | | | | |
| A16 Book-as-location metaphor | ✓ | | | | | | | | | | | | |
| Em-dash overuse | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | | | |
| A3 triplet pileup | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | | | |
| Forbidden vocab leakage | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | | | |
| Hedged constructions | ✓ | | | | | | | | | | | | |
| A4 boastful biography | ✓ | ✓ | | | | ✓ | | | | | | | |
| Canonical capitalization | ✓ | | | ✓ | | | | | | | | | |
| A2 coined-term-before-defined | | ✓ | ✓ | ✓ | | ✓ | | | | | | | |
| Cross-paragraph phrase repetition | n/m | ✓ | ✓ | ✓ | | ✓ | | | | | | | |
| Long paragraph skim issue | n/m | ✓ | ✓ | ✓ | | ✓ | | | | | | | |
| Concept fragmentation across paragraphs | | | ✓ | | | | | | | | | | |
| Table-to-prose transition missing | | | ✓ | | | | | | | | | | |
| AI-coded vocab (load-bearing, etc.) | | | ✓ | ✓ | | | | | | | | | |
| Wrong canonical definition (vs glossary) | | | ✓ | | | | | | | | | | |
| Factual content error (story attribution / facts) | | | | ✓ | ✓ | | | | | | | | |
| Skimmability — H3s needed in taxonomy sections | | | | ✓ | | ✓ | | | | | | | |

**Recurrence headline:** A13 means/ends + em-dash overuse + A3 triplet + forbidden vocab leakage now 6/6 chapters. The voice charter A13–A16 rules + scanner pipeline are doing real work across every chapter.

---

## Chapter: Ch 3 — The Framework (`chapters/03-the-framework.qmd`)

**Executed:** 2026-05-25 → 2026-05-26  ·  **Scout plan:** `_julie/per-chapter/03-the-framework.md`  ·  **Final commit:** `0fad966`
**Iterations:** 3 (Scout → Drafter+EC → author 2nd read with 7 jf-notes → author 3rd read with TML acronym catch). Author surfaced more issues than Ch 4/5 because the chapter was the most thinly written (six-stage section was a sparse 6-bullet list).

### Key catches
- **A13 means/ends on chapter opener and Sequence-introduction** (Scout caught upfront via §5 check)
- **Author second-read flagged 7 substantive issues** that no agent caught: "halves" math error (2/4 ≠ halves of 6), burned-egg over-specific example, "Design sits at the top of the Execute half" inconsistency, Pro Tip missing Design as upstream, Business Model Canvas prescription, "thin chapter" critique (Six Stages section expanded ~450 words), Meridian-in-Ch-2 oversight discovery
- **Author third-read TML catch**: TML acronym wrongly expanded as M+L gloss instead of canonical Task/Management/Leadership. **Triggered EC1 canonical-definition verification refinement** (editorial-coherence agent updated to verify definitions match canon, not just verify a definition exists). This is the most consequential agent update of the merge.
- **Cross-book consistency sweep**: Co-Intelligence capital-I locked across charter + 3 chapters; *Chutes and Ladders* italicized proper-noun across Preface + 3 chapters

### What was added beyond the manifest
- **Six Stages section expansion** (each stage gained H3 with concrete examples, Meridian references, what-it-produces beat)
- **`### How the stages connect.`** section explaining why this is a Framework not a checklist
- **Sprint Planning Canvas PDF + resources library bead** (`book-ff63.20`) — broken link removed, replaced with placeholder
- **Excalidraw diagram bead** (`book-ff63.21`) — for ch03-stage-dependencies

### Architecture lesson
EC1 canonical-definition verification refinement. Editorial-coherence now verifies each coined term's definition matches the canonical source (manifest, charter §3, glossary), not just that a definition exists. Encoded in `.claude/agents/editorial-coherence.md` EC1 section.

---

## Chapter: Ch 4 — Signal (`chapters/04-signal.qmd`)

**Executed:** 2026-05-31  ·  **Scout plan:** `_julie/per-chapter/04-signal.md`  ·  **Final commit:** `ef45c46`
**Iterations:** 2 (Scout + Drafter+EC in single combined pass + author 1 sparse jf-note). **Cleanest workflow execution so far.**

### What caught what
- Scout: E26 SKIP-ALREADY-DONE (PT clinic example already serves Julie's "non-manufacturing example" ask — Q-E26 research findings applied upfront)
- Scout: CH04-L10 conflict protection (L10 / $24K subcontractor story preserved verbatim through E24 voice-shift)
- Drafter mandatory scanner gate caught and self-fixed introductions during execution
- Editorial-coherence: all 4 E-rows PASS substance; 0 NEEDS-REVISION; 3 optional advisory polishes
- **Author single catch on 2nd read**: PT clinic story is JULIE's, not Jesse's (factual correction — Q-E26 research had incorrectly attributed it). Cross-chapter attribution memory not yet codified — author judgment still ground truth for who-did-what.

### Architectural pattern validated
**Drafter does both Scout work AND opening polish in one pass.** Author quote: *"the opening story is riddled with em-dash and ai-sounding repetition. its hard for me to read. just implement scout's feedback and give me a clean pass before i go through and read this version."*

This pattern (Ch 4 onward) compressed iteration count from Ch 1's 5–6 → 1–2 before author read. Now canonical per `canonical-chapter-workflow` memory.

---

## Chapter: Ch 5 — Source (`chapters/05-source.qmd`)

**Executed:** 2026-05-31  ·  **Scout plan:** `_julie/per-chapter/05-source.md`  ·  **Final commits:** `def37b9` (Drafter+EC), `af08f3d` (H3 skimmability)
**Iterations:** 2 (Drafter+EC pass + author second-read with H3 skimmability ask). All EC1 canonical-definition checks PASS.

### What caught what
- **EC1 canonical-definition: 4/4 PASS** on Knowledge Map, TML, PIS, Source. **Ch 2 TML failure mode did NOT recur.** The Ch 3 author catch (TML acronym wrong gloss) led to the EC1 refinement, which paid off immediately on Ch 5's dual-framework introduction.
- Scanner: 35 baseline → 3 final Vale alerts (**91% reduction** — steepest of any chapter)
- Em-dash count: ~48 → ~12 chapter-wide
- Cross-chapter coherence: E28 differentiated from 4 prior global food safety company anchors (Preface L9, Ch 1 L57, Ch 2 §2.3, Ch 4 L18) without verbatim n-gram echo
- **Cross-chapter cascade catch**: Ch 2 L259 forward-reference said "Chapter 6 introduces TML framework" but TML now lands first in Ch 5. Editorial-coherence caught the stale forward-reference; surgical fix applied to Ch 2.

### Architectural pattern validated
**Parallel taxonomy H3 pattern.** Ch 5 has 4 sections that each introduce a 3-item taxonomy (Passes 1/2/3; Structured vs. unstructured + Durable vs. ephemeral + AI tiers; APIs/MCPs/Connectors; Digital/Organic/At-risk sources). Author asked for H3s on the Passes section explicitly; I applied the same pattern across all 4 taxonomy sections (12 new H3s total). Consistent reader skim across the chapter.

### Architecture lesson
Cross-chapter forward-reference cascades. When a framework's first-introduction moves chapter (TML moved from Ch 6 → Ch 5), every downstream chapter that referenced its location must be updated. Editorial-coherence's cross-chapter coherence check catches these. Worth a systematic pre-publication pass at Phase 5.

---

## Parallelization test (Ch 6 + Ch 6b)

**Initiated:** 2026-05-31. Test case: dispatch both Scouts in parallel, then sequential Drafter+EC (Ch 6 first, then Ch 6b).

### Hypothesis
Parallel Scouts cleanly parallelize because (a) no content changes during Scout, (b) Scout reads canonical sources that don't change during the parallel dispatch, (c) chapter files are distinct. Sequential Drafter+EC preserves the cross-chapter coherence catches that have been load-bearing.

### Risks
- Cross-Scout interference if Ch 6b Scout's TML treatment depends on Ch 6's HAC introduction — mitigated by spec'ing Ch 5 as the TML canon source (Ch 6 doesn't introduce TML; Ch 6b extends it to work-lens).
- File collisions: none (Scouts write to distinct files).
- Bead collisions: none (Dolt handles concurrent writes).

### Preliminary results (Phase 1 — Scout parallel)
Both Scouts completed within similar wall-clock windows (~10 min for Ch 6, ~15 min for Ch 6b). Both report cleanly:
- Ch 6 EC1 PASS for Right Seat Evaluation; Path A solo Drafter
- Ch 6b EC1 PASS for TML at work-lens (matches Ch 5 canon); Path A default but Path B fallback more likely than any prior bead (15-point restructure cascade for E36)
- Critical Ch 6b catch: chapter currently has 4 TML categories; E36 collapses to canonical 3 — exact kind of cross-chapter coherence work the test was designed to validate

### Phase 2 results (Drafter+EC sequential — 2026-06-01)

**Both chapters EC PASS with 0 surgical fixes on first pass.** Sequential Drafter+EC preserved every cross-chapter coherence catch the test was designed to validate.

**Ch 6 (E35 Right Seat Evaluation):**
- Pattern A landing (declarative canonical-vocabulary-first introduction) — zero individual attribution
- ***Right Seat Evaluation*** + ***Sees It*** / ***Wants It*** / ***Suited for It*** italicized on first use
- A1 binary closer cut ("is not a supervisor. They are a liability." → Rewrite C operator-outcome bridge to L185-L189 development-gap framing)
- EC1 PASS: three criteria match manifest E35 + E58 glossary canon verbatim
- EC3 PASS: Meridian L215-L245 untouched (Elena's implicit Right Seat pass preserved); Human Orchestrator section untouched (different selection-test layer)
- Scanner: 38→24 alerts (37% reduction); no new flags from E35
- Commit: dc6869b

**Ch 6b (E36 TML 4→3 category restructure — highest-risk bead in merge):**
- 15-location restructure cascade landed clean on first pass
- Cross-chapter bridge sentence opens §Work Deconstruction: "Work Deconstruction applies the TML lens from Source to the work itself. Where Source used TML to categorize what the organization knows, Design uses TML to categorize what the work requires." — closes Ch 5 §5.0 L28 forward-reference word-aligned
- Workflow automation folded into Task as parenthetical sub-category (per Julie's E36 canon)
- TML names match Ch 5 §5.0 canon verbatim (Task / Management / Leadership)
- HAC entries autonomy levels UNCHANGED (orthogonal to TML — Drafter did not conflate)
- L223 Design Gate closer STRENGTHENED per Scout recommendation (A13 fix: "Holding that line is the difference between sprints that produce a designed workflow you can compound on and sprints that produce code nobody uses" — replaces Sequence-as-destination framing)
- Framework-attribution scrub: zero "Julie's TML framework" individual-instrument language
- EC1 PASS verbatim; EC3 PASS on all five cross-chapter checks (Ch 5 forward-ref / Ch 2 L259 Hybrid Split bridge / Ch 6 HAC orthogonality / Ch 6 Right Seat reference-not-redefinition / E58 glossary alignment)
- Scanner: 13→11 alerts; no new flags from E36
- Commit: 83791a5
- Path B not invoked; Path A solo Drafter sufficed on first pass for the most cross-referenced framework in the book

### Validation summary

**Parallel Scouts: VALIDATED.** Both Scouts produced independent plans without coordination issues. Wall-clock parallel (~10 + ~15 min). Cross-Scout coordination handled via explicit Scout-plan annotations naming which canonical instruments live in which chapter (Ch 6 owns HAC + Right Seat; Ch 6b owns TML work-lens application; Ch 6 introduces Right Seat that Ch 6b references but does not redefine).

**Sequential Drafter+EC: VALIDATED.** Both chapters PASS EC on first pass with 0 surgical fixes. Sequential ordering (Ch 6 first to lock HAC + Right Seat canon; Ch 6b second to extend) eliminated cross-chapter ambiguity. Highest-risk bead (E36 restructure cascade across 15 landing points) landed clean — Path B fallback not needed.

**Pattern table update:** All 8 committed chapters (Preface + Ch 1-5 + Ch 6 + Ch 6b) now have A13 means/ends catches in the cross-chapter pattern. A13 recurrence pattern stands at 8/8 chapters — the most persistent anti-pattern in the merge.

### Decision: scale parallel Scouts to remaining chapters

Validation criterion met. Recommend parallel Scout dispatch for the remaining 5 chapters (Ch 7 Build, Ch 8 Deliver, Ch 9 Compound, Ch 10 The Rhythm, Ch 11 What to Do Next). Possible groupings:

- **Group A (3 chapters parallel):** Ch 7 Build + Ch 8 Deliver + Ch 9 Compound (Build/Deliver/Compound triple — each independent; Compound has Pattern Method E46 substance-overlap with E37 BLOCKED, watch for unblock first)
- **Group B (2 chapters parallel):** Ch 10 The Rhythm + Ch 11 What to Do Next

Sequential Drafter+EC remains the convention. Path B fallback ready if any single bead (e.g., Ch 9 E46 Pattern Method three-lens retrospective, if it lands as canonical first-introduction with cross-bead alignment to E37 + E58) requires Design Table triangulation.

---

*End of running log. Update after each chapter execution.*
