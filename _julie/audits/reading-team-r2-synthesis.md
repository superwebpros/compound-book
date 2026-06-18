# Reading-Team R2 Synthesis — Post-3C Restructure

**Date:** 2026-06-16
**Input:** Fresh reading-team verdicts (12 chapter reads, A/B/C rubric) against the open bead backlog.
**Rubric:** A = Clarity (jargon/definitions), B = Get-Moving (actionability), C = Artifacts (fillable, blank+worked pairing). Overall is the worst of the three.

---

## 1. Overall read

**The book is not prospect-ready yet, but it is materially closer than the pre-3C ARC pass.**

The pre-3C ARC read scored **0 Pass / 13 Risk / 0 Fail**, with clarity flagged Risk on 13 of 15 dimensions. This R2 read scores **0 Pass / 12 Risk / 0 Fail at the chapter (Overall) level** — superficially identical. But the texture underneath has changed in the book's favor, and the "Overall = Risk" verdict is now driven by a *narrower, more mechanical* set of misses rather than structural confusion:

- **Get-Moving improved sharply.** 7 of 12 chapters now Pass on B (Beliefs, Co-Op Model, Framework, Source, Build, Compound). The Action Step + blank-then-worked-Meridian cadence is landing. Pre-3C, actionability was a systemic weakness; now it is a per-chapter polish item.
- **Clarity is the dominant residual.** 11 of 12 chapters are Risk on A. But the *cause* has narrowed: almost every clarity flag is now a **missing inline gloss on a specific named term** (system prompt, embeddings, confidence score, chunking, n8n, RAG sub-terms, Human Orchestrator, Hybrid Org Today, Signal Backlog) or a **missing EOS bridge** — not "the reader is lost." These are find-and-fix edits, not rewrites.
- **Artifacts are the surprise soft spot.** 6 of 12 chapters are Risk on C, almost entirely from **blank-template-without-adjacent-worked-example** (Co-Op HAC, Design System info-flow table, mini-spec, governance table; 06b Design Brief) or **named-but-never-shown artifacts** (Sprint Planning Canvas, Hybrid Org Today, Compounding Scorecard reappearing un-glossed in late chapters). The artifacts exist; they are not yet consistently *embedded where the concept lands and shown filled in.*

**Net:** the manuscript moved from "structurally confusing" to "structurally sound but lexically and referentially leaky." The remaining work is high-volume but low-risk: define terms inline at first use, build the approved EOS bridges, and pair every blank template with a worked Meridian example in-body. No chapter requires re-architecting.

---

## 2. Per-chapter scoreboard

| Chapter | A (Clarity) | B (Get-Moving) | C (Artifacts) | Overall |
|---|---|---|---|---|
| 01-diagnosis | Risk | Risk | Pass | Risk |
| 02-beliefs (You're Already a Tech Company) | Risk | Pass | Risk | Risk |
| 02-co-operating-model | Risk | Pass | Risk | Risk |
| 03-the-framework | Risk | Pass | Pass | Risk |
| 04-signal | Pass | Risk | Risk | Risk |
| 05-source | Risk | Pass | Pass | Risk |
| 06-designing-the-system | Risk | Risk | Risk | Risk |
| 06b-designing-the-work | Risk | Risk | Risk | Risk |
| 07-build | Risk | Pass | Pass | Risk |
| 08-deliver | Risk | Risk | Pass | Risk |
| 09-compound | Risk | Pass | Risk | Risk |
| 10-the-rhythm | Risk | Risk | Risk | Risk |
| 11-what-to-do-next | Risk | Risk | Risk | Risk |

**Tally:** 0 Pass / 13 Risk / 0 Fail at Overall. A: 1 Pass / 12 Risk. B: 7 Pass / 6 Risk. C: 5 Pass / 8 Risk.

(Note: the verdict JSON lists 13 chapter reads; 02-beliefs and 02-co-operating-model are distinct chapters sharing a numeric prefix.)

---

## 3. Bead reconciliation

Verdicts are conservative: **RESOLVED** only when a reader's *improved* note clearly covers the bead's concern; **PARTIAL** when partly addressed but a related miss still appears in *remaining*; **OPEN** when a reader still flags it or there is no evidence either way.

| Bead | Verdict | Evidence |
|---|---|---|
| book-0fq9 (FLOW#1 lead-with-practice reorder) | PARTIAL | Action Steps now land mid-chapter and B passes in 7 chapters, but Ch06/06b/10/11 still flag the artifact/payoff arriving late (HAC at 88%, Canvas buried). Reorder partly achieved, not complete. |
| book-3w1t (FLOW#2 Source simplicity rescue) | PARTIAL | 05-source improved notably (three-pass cadence, pressure-release Pro Tip, side-by-side blank+Meridian); B passes. But A still Risk: embeddings/taxonomies/vectorized work/context engineering glosses missing. Simplicity improved, not clean. |
| book-8v6v.33 (Ch11 Compound headcount-slope as last move) | OPEN | 09-compound (the Compound chapter) reader does not confirm the headcount-slope payoff as the closing move; no improved note covers it. |
| book-8v6v.34 (Ch12 Headcount resolved reorder) | RESOLVED | 10-the-rhythm improved: "Headcount Paradox resolution (lines 92–105): connects back to Ch.1 promise, shows the mechanism... The loop closes here and it lands." Sits before the one-page doc description. |
| book-8v6v.40 (Ch1 2-precondition split vs 5 dimensions) | OPEN | 01-diagnosis still flags it: "'Technical preconditions' framing (lines 109-111)... No counter-framing is offered." Relationship to the 5 dimensions still not clarified. |
| book-8v6v.50 (Ch1 RPE non-ERP anchor) | PARTIAL | 02-beliefs Pro Tip gives revenue÷headcount any CEO can run (RPE landed there). But 01-diagnosis itself still assumes context; no improved note confirms a non-ERP alternate anchor in Ch1 §IV. |
| book-8v6v.60 (Ch1 $558K disambiguation) | OPEN | No reader note references the $558K figure or its dual use under Constraint Clarity vs Measurement Discipline. No evidence either way → conservative OPEN. |
| book-7zzd (no-engineer/no-ERP reader path) | PARTIAL | 03-framework addresses non-engineer path on n8n inline; 05-source Pro Tip grants permission to stop at the Pipeline column. But 02-beliefs still uses "defined interfaces"/"substrate" un-glossed and ERP-centric framing persists. Partial. |
| book-8v6v.24 (structural-anchor pass: central Q + named tool + closing checklist) | PARTIAL | Many chapters now have In-Brief + named artifact + closing checklist (01, 03, 08, 09). But 02-co-operating-model "closing section is thin," 11 "closing has no Action Step." Not uniform. |
| book-8v6v.27 (fillable-artifact audit: ≥1 per chapter) | RESOLVED | Every reviewed chapter names and shows at least one fillable artifact in improved notes (Scorecard, Take-stock table, ownership tables, Canvas, Knowledge Map, Build Spec, runbook, scorecard). The ≥1-per-chapter bar is met; quality issues are tracked separately under book-rhko. |
| book-8v6v.35 (Ch4 compounding payoff at 95% reposition) | OPEN | 03-framework reader does not confirm; no improved note on repositioning a deep-buried compounding payoff. |
| book-8v6v.37 (Ch4 Diagnose/Execute split prefaces six-stage walk) | RESOLVED | 03-framework improved: "Four-words callout (lines 24–34) orients the reader before the six-stage wall. Framework / Sequence / Sprint / Rhythm are distinguished cleanly." Orientation now precedes the walk. |
| book-8v6v.38 (Ch6 Connected/Manual/Broken defined before classify) | OPEN | 05-source remaining flags the inverse: tier system introduced after the build, template has no Tier column. The pipeline/status taxonomy ordering is still flagged, not confirmed resolved. |
| book-8v6v.39 (Ch8 Span-of-Control ordering) | OPEN | 07-build reader does not mention Span-of-Control ordering; no evidence. |
| book-8v6v.41 (Ch11 recovery Action Step after failure verdict) | OPEN | 09-compound reader does not confirm a recovery Action Step; the "zero didn't-work items" Pro Tip is praised but that is a different beat. |
| book-8v6v.42 (Ch5 Activity-Is-Not-Signal redirect) | OPEN | 04-signal reader does not mention an Activity-Is-Not-Signal → run-the-session redirect. No evidence. |
| book-8v6v.43 (Ch7/7b ceiling failure next move) | OPEN | No reader note covers naming a concrete next move (split seat/defer/train) on ceiling+capability failure. |
| book-8v6v.44 (Ch7b prototype 'five responses' mechanism) | OPEN | 06b reader does not confirm the prototype mechanism is named (call/form/mockup). |
| book-8v6v.45 (Signal vs L10/quarterly/IDS relationship) | PARTIAL | 04-signal improved: "EOS connections are solid: Issues list, stalled Rocks, L10s explicitly mapped to Signal's candidate inventory." That covers Ch5 §XII. But the Ch12 §V side (10-the-rhythm) and IDS specifically not confirmed. |
| book-8v6v.46 (HAC vs Accountability Chart per-chapter naming) | PARTIAL | 06-designing-the-system gets it right (improved: "HAC alongside the Accountability Chart, not replacing it"). But Co-Op Model, 03-framework, 06b, 09, 10 all flag the HAC↔Accountability-Chart bridge as MISSING. Resolved in one chapter, open in five. |
| book-8v6v.47 (Ch7 Design Team seat) | RESOLVED | 06-designing-the-system improved: "Design Team vs L10 distinction (lines 300-302)." The seat/meeting relationship is addressed. |
| book-8v6v.48 (Ch6 Knowledge Manager seat) | OPEN | 05-source remaining: "Name a knowledge manager... the EOS bridge is absent." Seat placement on the Accountability Chart still unaddressed. |
| book-8v6v.49 (GWC parallel Sees/Wants/Suited) | OPEN | 11-what-to-do-next remaining: "EOS bridge missing for Right Seat Evaluation (Sees It/Wants It/Suited for It)... approved mapping to GWC. One parenthetical is all it needs." Still missing. |
| book-8v6v.52 (self-build-vs-contract rule Ch7/Ch8) | OPEN | 07-build reader praises "IT's real role" framing but does not confirm a resolved self-build-vs-contract decision rule; 08-deliver no evidence. |
| book-8v6v.55 (Ch5 Signal session ballpark hours) | OPEN | 04-signal remaining implies the session shape is still thin ("whoever runs Source" undefined); no improved note gives ballpark hours. 11 also flags Signal session has "no shape — duration, attendees, output." |
| book-8v6v.61 (Ch6 Tier3 vs Not-AI-tier) | OPEN | No reader note distinguishes Tier 3 from Not-AI-tier; 06-system flags Tier glosses generally but not this merge. |
| book-8v6v.62 (Ch12 design-validation vs dollars) | OPEN | 10-the-rhythm reader does not address the design-validation-not-financial framing vs dollar columns. |
| book-8v6v.63 (Ch12 Sprint compounding cumulative-not-marginal) | PARTIAL | 10-the-rhythm Pro Tip (lines 163–166) preempts the misread: "The first Sprint's delta will almost always be the largest. Don't let the smaller numbers in later quarters fool you." Covers the spirit; does not explicitly state cumulative-not-marginal math. |
| book-b8yy (FLOW#3 Meridian into front chapters) | RESOLVED | Meridian now runs through the front chapters: 01 (worked Scorecard example), 02-beliefs (Take-stock Meridian row), Co-Op Model (Elena 58% Column B), 03-framework (fully populated Meridian Canvas). Front-chapter weave confirmed across multiple improved notes. |
| book-bco3 (FLOW#4 Headcount callback-only) | PARTIAL | 10-the-rhythm closes the loop cleanly (callback works). But 11-what-to-do-next invokes "Headcount Paradox" by name with no explanation/pointer — a callback that doesn't read as a callback. Partial. |
| book-chf3 (ARC#7 coined terms first-use + AI bridge to Signal) | PARTIAL | Coined-term glossing improved in several chapters, but the AI bridge to Signal is explicitly still missing: 04-signal remaining — "no AI connection until the very last reflection question... a single sentence mid-chapter... would remind the reader why." And Co-Op Model still piles up three coined terms. |
| book-jrrh (recovery paths for failing diagnostics) | OPEN | 01-diagnosis remaining flags the unaddressed blank-rows case and "push hardest is abstract"; 09/11 lack recovery Action Steps. Recovery paths still thin. |
| book-rhko (ARC#5 fillable templates in-body) | PARTIAL | Strong where done (01 Scorecard, 03 Canvas, 05 Knowledge Map, 07 Build Spec/Guardrails blank+worked). But Co-Op (HAC), 06-system (info-flow table, mini-spec, governance table), 06b (Design Brief), 08/11 (Sprint Planning Canvas never shown) all flag templates named-but-not-shown or blank-without-worked. In-body embedding incomplete. |
| book-68zp (ARC#10 scorecard math + tiebreakers) | PARTIAL | 01-diagnosis: Scorecard scale + interpretation buckets praised, but a format inconsistency remains (1–5 scale vs five checkboxes). 04-signal: five-criteria tiebreaker praised but mis-ordered (sits before the Five Constraint Questions). Mechanized but with sequencing/format bugs. |
| book-8v6v.53 (Compound coach definition) | OPEN | 06-designing-the-system remaining: "'a Compound coach' without explaining what that is or how to access one... the chapter's only unexplained proprietary reference." Still undefined. |
| book-8v6v.56 (which-role/constraint-first selection criterion) | OPEN | No reader note confirms a selection criterion for which role/constraint to start with in Ch3/Ch7. |
| book-8v6v.57 (Ch12 time allocation across 4 agenda steps) | OPEN | 10-the-rhythm praises the four-step agenda but does not confirm time allocation per step within a 1–2 hour session. |
| book-8v6v.59 (Ch2 worksheet handoff line) | OPEN | 02-beliefs remaining: "Sprint Planning Canvas and Design Brief introduced as promises... neither is defined or previewed... what that something looks like is opaque." The handoff is still unclear, not resolved. |
| book-b4do (ARC#12 Excalidraw-only replacement + 'when it launches' hedge) | OPEN | Excalidraw placeholders still render blank: 04-signal ("renders as a placeholder"), 06b ("missing placeholder, line 32"), 07-build (callouts misplaced), 10 (placeholder line 88). Not replaced. |
| book-i91z (ARC#9 facilitation/session scaffolding) | OPEN | 11-what-to-do-next remaining: "Signal session... given no shape for what that session looks like — duration, attendees, output." Facilitation scaffolding still absent. |
| book-lbd7 (ARC#8 missing Action Steps for central artifacts) | PARTIAL | Many Action Steps now present and praised. But specific gaps remain: 06-system "No Action Step follows the governance five-question table"; 11 "Closing section has no Action Step callout." Partly closed. |
| book-n628 (ARC#11 AI Tier / Source Classification inline definition) | OPEN | 05-source remaining: tier system applied retroactively, template has no Tier column; categories not defined inline at point of use. |
| book-o81e (FLOW#5 trim outros/dumps + In-Brief/reflection caps) | PARTIAL | Reflection questions consistently praised as tight and applied (caps working). But 02-co-operating-model "closing section is thin/deflated" and 09-compound late artifact dumps suggest trim/dump work uneven. |

---

## 4. Beads safe to CLOSE (RESOLVED only)

- **book-8v6v.34** — Ch12 Headcount Paradox resolved reorder (loop closes, lands before the doc description).
- **book-8v6v.27** — Fillable-artifact audit; every chapter now has ≥1 fillable artifact (quality tracked under book-rhko).
- **book-8v6v.37** — Ch4 Diagnose/Execute orientation now prefaces the six-stage walk (Four-words callout).
- **book-8v6v.47** — Ch7 Design Team seat clarified (Design Team vs L10 distinction).
- **book-b8yy** — FLOW#3 Meridian woven through front chapters (confirmed in 01, 02, Co-Op, 03).

Five beads. All other open beads are PARTIAL or OPEN and should stay open.

---

## 5. Residual issues, ranked

### Tier 1 — Real problems blocking prospect-readiness (do these next)

1. **Inline glosses for named technical terms at first use (book-chf3, book-n628, partial book-3w1t).** The single most-repeated reader flag. Concrete offenders: *system prompt* (Co-Op, 06-system, 06b), *embeddings / taxonomies / vectorized work / context engineering* (05-source), *confidence score* (06-system, 06b, 08), *chunking / metadata / retrieval index / retrieval layer* (06-system, 07-build), *n8n* (06b), *RAG sub-terms*, *Claude / Claude Team workspace* (03, 08), *ERP / RFQ* (08, 09), *defined interfaces / substrate* (02-beliefs). Each is a one-clause fix; the volume is the problem, not the difficulty. **Highest leverage on the A-clarity wall.**

2. **EOS bridges where the approved mapping table already exists (book-8v6v.46, book-8v6v.49).** HAC↔Accountability Chart is missing in five chapters (Co-Op, 03, 06b, 09, 10) despite being an approved bridge; Human Orchestrator↔Integrator missing in 03, 05, 10; GWC↔Sees/Wants/Suited missing in 11. These cost one parenthetical each and land with the primary audience.

3. **Blank templates without an adjacent worked Meridian example (book-rhko).** Co-Op HAC (teased, not shown), 06-system info-flow table / mini-spec / governance table (blank only), 06b Design Brief (blank only, the chapter's primary artifact). Pair each blank with one filled row.

4. **Named-but-never-shown artifacts in the back chapters (book-rhko, book-8v6v.59).** Sprint Planning Canvas is referenced as "pull it back out" in 08 and 11 but never reproduced; Hybrid Org Today and Compounding Scorecard appear in 09/10/11 un-glossed and unshown. The reader is told to use documents they cannot see. Reproduce or name the rows at point of use.

5. **The AI bridge to Signal (book-chf3).** 04-signal reads as a pure ops chapter until the last reflection question. One mid-chapter sentence tying constraint quality to AI-tool quality. Important because Signal is where a skeptical CEO decides whether this is an AI book or a repackaged EOS.

### Tier 2 — Sequencing / structural polish

6. **Artifact-after-classification ordering (book-8v6v.38, book-n628).** 05-source asks readers to tier sources after the build, with no Tier column in the template. 04-signal tiebreaker rubric sits before the questions that produce the survivors it ranks.
7. **Late-arriving central artifact (book-0fq9, book-rhko).** 06-system HAC at ~88%; 03/04-signal Canvas buried after the six-stage wall. Preview or move earlier.
8. **Missing Action Steps on consequential artifacts (book-lbd7).** Governance table (06-system) and the closing section (11) have no Action Step callout.
9. **Recovery paths for failing diagnostics (book-jrrh, book-8v6v.41).** 01 blank-rows case ("that is your answer, and it's the most common one"); 09/11 recovery Action Steps after a failure verdict.
10. **Excalidraw placeholders rendering blank (book-b4do).** 04, 06b, 07, 10 all show empty placeholders or misplaced diagram callouts. A visible production bug to a prospect reader.

### Tier 3 — Nice-to-haves / low-risk

11. **Internal contradictions to scrub.** 04-signal Meridian vignette frames Elena *as* the constraint two paragraphs before the Stop Rule says not to; Co-Op calls Claude AI/NotebookLM "agents" against the chapter's own six-part agent definition. Small but credibility-denting for a careful reader.
12. **Facilitation scaffolding (book-i91z, book-8v6v.55, book-8v6v.57).** Session hours, who's in the room, time-per-agenda-step. Useful, not blocking.
13. **Coached-term pile-up (book-chf3, book-o81e).** Co-Op introduces three coined terms in three consecutive paragraphs; needs a one-sentence "the one to remember is the model" anchor.
14. **Compound coach definition (book-8v6v.53), self-build-vs-contract rule (book-8v6v.52), scorecard format consistency (book-68zp: 1–5 scale vs checkboxes).**
15. **Thin outros (book-o81e).** Co-Op equation section reads as a slogan, not a synthesis; trim or strengthen.

**Bottom line for the next pass:** Tier 1 items 1–3 alone would flip most A-clarity and C-artifact Risks toward Pass, because they are the literal content of nearly every *remaining* note. The book's structure is no longer the problem; its glosses, bridges, and worked examples are.
