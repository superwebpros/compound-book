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

## Chapter: TBD (Ch 1)

*(To be added after Ch 1 execution.)*

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
