# Term Usage Audit — Phase 3 Audit 3

**Generated:** 2026-06-05  ·  **Bead:** book-z2ep  ·  **Agent:** Term Usage Consistency Auditor

## TL;DR

Audited 28 canonical Compound terms against the glossary at `/Users/jesseflores/projects/compound/sites/compound-book/chapters/appendix-glossary.qmd`, traced across Ch 1–11 + Ch 6b (no `chapters/index.qmd` exists; that path was checked and is empty). Found roughly **20 distinct drift findings** — three of them book-level structural (Sprint capitalization bimodality, "Co-Intelligent Co-Operation" hyphen-case in the very chapter that defines it, and three glossary terms that have NO matching capitalized form in chapter prose). The remainder are local capitalization/italicization slips. Severity split: **3 blocker-tier** (Co-Operation case error in Ch 2; Sprint capitalization bimodal; glossary terms missing from chapter usage), **9 high-priority** (canonical first-introduction italicization drift, sub-criteria inconsistency), **~8 cosmetic**. The book is broadly coherent at the semantic layer — no term flipped meaning between chapters — but the capitalization-and-italicization layer is the layer that needs surgical cleanup before PR.

## Per-term findings

### Tier 1 (book-level frameworks)

#### Sequence
- **Occurrences:** ~41 across 10 chapters (Ch 3 anchors at 12; Ch 9 at 9; Ch 11 at 8; Ch 10 at 6).
- **First introduction:** Ch 3 line 5 (in-brief) and Ch 3 line 46 (`**Sequence** —` bold definition).
- **Glossary claim:** "First introduced: Chapter 3" ✓ matches.
- **Capitalization drift:** None — "Sequence" is consistently capitalized as a proper noun.
- **Italicization drift:** Yes. Glossary entries italicize `*Sequence*` (5 occurrences in glossary body). In chapter prose, "Sequence" is plain text everywhere except the bold definition in Ch 3 line 46. The voice charter calls for canonical Compound vocabulary italicized on first appearance per chapter — that discipline is **not** applied to "Sequence" anywhere in the chapters. Severity: cosmetic, but it's the term the book is built around.
- **Redefinition downstream:** None.
- **Semantic drift:** None.
- **Verdict:** PASS [1 cosmetic finding — consider italicizing `*Sequence*` on its first appearance in each chapter to match the discipline applied to other canonical terms].

#### Rhythm
- **Occurrences:** ~30+ across Ch 2, Ch 3, Ch 9, Ch 10 (its home), Ch 11.
- **First introduction:** Ch 2 line 5 (in-brief) and Ch 3 line 48 (`**Rhythm** —` bold definition). Pre-introduced in Ch 1 line 82 ("review rhythm" — lowercase, used generically, not yet a canonical term — coherent).
- **Glossary claim:** "First introduced: Chapter 3" ✓ matches Ch 3 definition; Ch 2 references it inside the equation as a forward-pointer (acceptable).
- **Capitalization drift:** Ch 1 line 276 has "meeting rhythms" (lowercase, plural, used as common-noun ordinary English — coherent). All capitalized Compound uses are consistent.
- **Italicization drift:** Ch 10 has `# *Rhythm*.` (title) and `## What *Rhythm* means in this book.` (section header) — italicized. Ch 9 line 196 has `*the Rhythm*`. Otherwise "Rhythm" is plain text. Same discipline gap as Sequence: italicization on first-mention-per-chapter not applied.
- **Redefinition downstream:** Ch 10 lines 26-30 explicitly re-defines Rhythm with `## What *Rhythm* means in this book.` — this is the home-chapter expansion, not redefinition. Coherent.
- **Semantic drift:** None.
- **Verdict:** PASS [1 cosmetic finding — italicization discipline].

#### Compound Sprint
- **Occurrences:** 7 in chapter prose + glossary.
  - Ch 1 line 232: "Compound Sprint framework" (capitalized, plural-singular ambiguous)
  - Ch 2 line 28: "A Compound Sprint" (capitalized)
  - Ch 6b line 132: "The Compound Sprint" (capitalized)
  - Ch 7 line 185: "the Compound Sprint from Chapter 3" (capitalized)
  - Ch 7 line 195: "The Chapter 3 Compound Sprint" (capitalized)
  - Ch 10 line 62 diagram caption: "Compound Sprint Session" (capitalized)
- **First introduction:** Ch 1 line 232 (defined only by name); Ch 2 line 28 (defined inline as "how you do that work"). Glossary line 44-45 — "First introduced: Chapter 3".
- **Glossary claim:** "First introduced: Chapter 3" ✗ — actually pre-introduced Ch 1 / Ch 2. The Ch 3 anchor is where the Sequence is unpacked, but "Compound Sprint" as a phrase appears earlier.
- **Capitalization drift:** **BLOCKER**. Ch 7 line 18 ("a Compound sprint produces"), line 80 ("every Compound sprint"), line 144 ("most Compound sprints"), line 152 ("most builds in a Compound sprint"), line 156 ("Most Compound sprints"); Ch 10 line 36 ("inside a Compound sprint cycle"). Six instances of `Compound sprint` (lowercase 's') where the canonical form is `Compound Sprint`. All in Ch 7 and Ch 10. This is the most-occurring capitalization defect in the book.
- **Italicization drift:** Never italicized. Glossary doesn't italicize it either except in the COE entry referencing it as `*Compound Sprint*`. Consistent if cosmetic.
- **Redefinition downstream:** Ch 7 line 195 mildly redefines: "The Chapter 3 Compound Sprint is the strategic container. Build's sprint discipline is the tactical version." This is a useful disambiguation, not a redefinition.
- **Semantic drift:** None.
- **Verdict:** NEEDS-FIX [7 findings, 6 of them capitalization (Compound sprint → Compound Sprint), 1 cross-reference inaccuracy (glossary first-introduced claim)].

#### Co-Intelligent Co-Operation
- **Occurrences:** 5 in chapter prose + 3 in glossary + 1 in appendix-prompts.qmd subtitle.
  - Ch 1 line 70: `Co-Intelligent Co-Operation` ✓ (capital O)
  - Ch 2 line 20: `Co-Intelligent Co-operation` ✗ (lowercase o)
  - Ch 2 line 30: `Co-Intelligent Co-operation` ✗ (lowercase o)
  - Ch 2 line 32: `Co-Intelligent Co-operation` ✗ (lowercase o)
  - Ch 5 line 22: `Co-Intelligent Co-Operation` ✓ (capital O)
- **First introduction:** Ch 1 line 70 (correctly cased) precedes Ch 2's defining mention. Ch 2 line 30 is the definition entry but uses the wrong case.
- **Glossary claim:** "First introduced: Chapter 2" — defensible, since Ch 2 line 30 defines it. Ch 1 line 70 references the concept without defining. Slight cross-reference inaccuracy.
- **Capitalization drift:** **BLOCKER**. Three of five chapter occurrences use `Co-operation` (lowercase o). The defining chapter (Ch 2) is internally inconsistent and uses the non-canonical form in its definition. Author has clearly chosen `Co-Operation` (capital O) as the canonical form per glossary + Ch 1 + Ch 5 + appendix-prompts subtitle.
- **Italicization drift:** Ch 1 line 70 plain. Ch 2 lines 20, 30, 32: italicized once on line 20 (`*Co-Intelligent Co-operation*`), plain in 30/32. Glossary italicizes `*Co-Intelligent Co-Operation*` in cross-references.
- **Redefinition downstream:** Ch 5 line 22 uses the term in passing without re-defining — coherent.
- **Semantic drift:** None — the meaning is stable across all five uses.
- **Verdict:** NEEDS-FIX [3 findings, all capitalization in Ch 2 lines 20/30/32 — these are the highest-priority surgical fixes in the book because they sit at the book's defining moment for the title concept].

#### Co-Intelligent Company
- **Occurrences:** ~12 across Ch 1, Ch 2, Ch 5, Ch 6, Ch 9, Ch 10, Ch 11.
- **First introduction:** Ch 1 line 274: "We call it the Co-Intelligent Company" (plain, defined inline). Ch 2 line 26: `**Co-Intelligent Company**` (bold definition entry).
- **Glossary claim:** "First introduced: Chapter 1" ✓ matches Ch 1 line 274.
- **Capitalization drift:** None — Title Case consistent.
- **Italicization drift:** Ch 2 line 22 has `## What a *Co-Intelligent Company* is.` (italicized in section header) and Ch 10 line 233 has `## The *Co-Intelligent Company*.` (italicized in section header). Otherwise plain text. Discipline-applied where it counts; coherent.
- **Redefinition downstream:** None — each downstream mention references back.
- **Semantic drift:** None.
- **Verdict:** PASS.

#### Co-Operating Model
- **Occurrences:** ~14 in Ch 1, Ch 2 (heaviest), Ch 9, Ch 10, appendix-prompt-engineering.
- **First introduction:** Ch 1 line 276: "This book gives you the Co-Operating Model to build that company" (referenced without full definition). Ch 2 line 14: "the Co-Operating Model is the answer to it" (referenced). Ch 2 line 18: `**Co-Operating Model**` (bold definition). Ch 2 line 32: `**Co-Operating Model** is the system frame` (definition entry).
- **Glossary claim:** "First introduced: Chapter 2" — defensible (Ch 1 line 276 references but doesn't define). Mild forward-reference, not a blocker.
- **Capitalization drift:** None — Title Case consistent everywhere. Note: hyphen pattern is `Co-Operating` (capital O), matching the parallel discipline applied to `Co-Operation`.
- **Italicization drift:** Ch 2 line 1 title: `# The *Co-Operating* Model.` (only "Co-Operating" italicized — slightly different style from full-term italicization elsewhere). Otherwise plain.
- **Redefinition downstream:** Ch 10 line 166 references back: "The Co-Operating Model from Chapter 2 is no longer a concept." Coherent cross-reference.
- **Semantic drift:** None.
- **Verdict:** PASS.

---

### Tier 2 (canonical instruments / framework components)

#### Hybrid Accountability Chart (HAC)
- **Occurrences:** ~30+ across Ch 3, Ch 5, Ch 6 (its home), Ch 6b, Ch 7, Ch 8, Ch 9, Ch 10, Ch 11.
- **First introduction:** Ch 3 line 73 — referenced ("Design produces the Hybrid Accountability Chart entries"). Ch 6 line 7 / Ch 6 line 26 (italicized `*Hybrid Accountability Chart*`) / Ch 6 line 30 (`## The *Hybrid Accountability Chart*.` section header) / Ch 6 line 32 — full definition.
- **Glossary claim:** "First introduced: Chapter 6" — defensible (Ch 3 mentions, Ch 6 defines). Mild forward-reference, not a blocker.
- **Capitalization drift:** None — Title Case consistent everywhere.
- **Italicization drift:** Ch 6 line 26 and line 30 (section header) italicized; Ch 6b line 34 italicized; Ch 9 line 38, 135 italicized. Otherwise plain. Italicization discipline applied at chapter-entry points — coherent.
- **Redefinition downstream:** Ch 6 line 32 fully defines; subsequent chapters reference. Coherent.
- **Semantic drift:** None.
- **HAC abbreviation:** Used 7+ times. Always uppercase. Glossary defines as "(HAC)" parenthetical. Coherent.
- **Verdict:** PASS.

#### Hybrid Org Today
- **Occurrences:** ~12 across Ch 9 (forward reference), Ch 10 (its home — section header line 80), Ch 11 (back-reference).
- **First introduction:** Ch 9 line 44 — forward reference. Ch 10 line 80 `## The *Hybrid Org Today*.` is the definition section header.
- **Glossary claim:** "First introduced: Chapter 10" ✓ matches (Ch 9's mention is a forward pointer).
- **Capitalization drift:** None.
- **Italicization drift:** Ch 10 line 80 italicized in section header. Subsequent mentions plain. Coherent.
- **Verdict:** PASS.

#### TML Framework (Task / Management / Leadership)
- **Occurrences:** Ch 2, Ch 5 (its claimed home), Ch 6b (where it gets re-applied).
- **First introduction:** Ch 2 line 259: `**TML framework** (Task / Management / Leadership)` (bold, with sub-criteria). Ch 5 line 24 / line 28: full unpacked definition.
- **Glossary claim:** "First introduced: Chapter 5" ✗ — actually first introduced Ch 2 line 259 with sub-criteria parenthetical and the explicit note "Chapter 5 introduces the full design instrument — the **TML framework**". The Ch 2 line is essentially saying "introduced here, expanded in Chapter 5" — but the term and sub-criteria both appear in Ch 2.
- **Capitalization drift:** Ch 2 line 259 / Ch 5 line 24 / Ch 5 line 28 / Ch 6b: "TML framework" (lowercase 'f'). Glossary: "TML Framework" (capital F). Modest inconsistency.
- **Italicization drift:** Ch 6b line 5 uses `***TML framework***` (triple asterisk — strongest emphasis), Ch 6b line 12 uses `*TML*` only. Ch 2 / Ch 5 plain bold. Multiple emphasis levels for the same canonical term in different chapters.
- **Sub-criteria consistency:**
  - Ch 2 line 259: `Task / Management / Leadership` (with slashes)
  - Ch 5 line 24: `Task / Management / Leadership` ✓
  - Ch 5 line 26: full unpacked definitions
  - Ch 6b line 5: `***Task***, ***Management***, ***Leadership***` (triple asterisk, comma-separated)
  - Ch 6b line 14: `***Task***, ***Management***, ***Leadership***` (triple asterisk, comma-separated)
  - Ch 6b line 31: `Task, Management, Leadership` (no italics, comma-separated)
  - Ch 6b line 142: `Task / Management / Leadership` (no italics, slash-separated)
  - Glossary line 117: `*Task*, *Management*, *Leadership*` (single asterisk, comma-separated)
  
  Sub-criteria delimiter is **inconsistent** between slash and comma forms. Emphasis level varies between plain, single-asterisk italic, and triple-asterisk italic — all in the same chapter (Ch 6b).
- **Semantic drift:** None — the meaning is stable across all uses.
- **Verdict:** NEEDS-FIX [3 findings: glossary first-introduction claim, lowercase 'f' in chapter prose vs. capital 'F' in glossary, sub-criteria delimiter / emphasis inconsistency within Ch 6b].

#### PIS Framework (Problem / Identify / Solution)
- **Occurrences:** Only Ch 5 lines 34, 36 + glossary entry.
- **First introduction:** Ch 5 line 34: `**Problem/Identify/Solution (PIS) framework**` (bold, slash delimiter, lowercase 'f').
- **Glossary claim:** "First introduced: Chapter 5" ✓.
- **Capitalization drift:** Ch 5: `(PIS) framework` (lowercase 'f'). Glossary: `PIS Framework` (capital F).
- **Italicization drift:** Ch 5 uses bold only. Glossary uses single-asterisk italics for sub-criteria.
- **Sub-criteria consistency:**
  - Ch 5 line 34: `Problem/Identify/Solution` (no spaces around slashes)
  - Glossary line 90: `*Problem*, *Identify*, *Solution*` (italics, commas)
  - Same delimiter mismatch pattern as TML.
- **Semantic drift:** None.
- **Verdict:** NEEDS-FIX [2 findings: capitalization of 'F', sub-criteria delimiter mismatch with glossary].

#### Right Seat Evaluation (Sees It / Wants It / Suited for It)
- **Occurrences:** Ch 6 lines 47-51 + Ch 11 lines 145-146 + glossary entry.
- **First introduction:** Ch 6 line 47: `***Right Seat Evaluation***` (triple asterisk, strong emphasis) + sub-criteria each `***Sees It***`, `***Wants It***`, `***Suited for It***`.
- **Glossary claim:** "First introduced: Chapter 6" ✓.
- **Capitalization drift:** None.
- **Italicization drift:** Ch 6 uses triple asterisk for first introduction; Ch 11 line 145 / 146 uses single asterisk `*Right Seat Evaluation*`, `*Sees It*`, `*Wants It*`, `*Suited for It*`. This **matches** the voice charter: triple-asterisk for canonical first-introduction, single-asterisk for downstream. Coherent discipline.
- **Sub-criteria consistency:** Ch 6 ↔ Ch 11 ↔ Glossary all match (Sees It / Wants It / Suited for It; commas or slashes vary but the criteria themselves are stable).
- **Semantic drift:** None.
- **Verdict:** PASS — best-disciplined term in the book; should be the model for other canonical first-introductions.

#### Center of Excellence (COE) Operating Model
- **Occurrences:** Ch 10 line 36 only + glossary.
- **First introduction:** Ch 10 line 36: `***Center of Excellence (COE) Operating Model***` (triple asterisk, with attribution to Dave Ulrich).
- **Glossary claim:** "First introduced: Chapter 10" ✓.
- **Capitalization drift:** None.
- **Italicization drift:** Triple-asterisk on first introduction matches discipline. No downstream uses to check.
- **Semantic drift:** None.
- **Verdict:** PASS.

#### Human Orchestrator
- **Occurrences:** ~30+ across Ch 3 (introduced as **Human Orchestrator** bold), Ch 6 (defined with `## The *Human Orchestrator*.` section header line 174 and italicized definition line 176), Ch 6b, Ch 7, Ch 8, Ch 9, Ch 10, Ch 11.
- **First introduction:** Ch 3 line 137 (`**Human Orchestrator**` bold + defined inline). Ch 6 line 174 / 176 (italicized header + body — second-pass canonical definition).
- **Glossary claim:** "First introduced: Chapter 3" ✓ — matches Ch 3 line 137.
- **Capitalization drift:** None — Title Case everywhere.
- **Italicization drift:** Ch 7 line 330 uses `***Human Orchestrator***` (triple asterisk — strong canonical first-introduction marker). But this is the FIFTH chapter to mention the term, well after the Ch 3 / Ch 6 introductions. The triple-asterisk should be reserved for canonical first-introduction; using it in Ch 7 is misleading and breaks the discipline established in Ch 6 (Right Seat Evaluation) and Ch 10 (COE Operating Model).
- **Redefinition downstream:** Ch 6 line 174-180 substantially expands the role (not a redefinition, but a deepening). Subsequent chapters reference. Coherent.
- **Semantic drift:** None — the role is stable (sets goals, reviews at goal level, manages day-to-day, makes design improvements between sprints).
- **Verdict:** NEEDS-FIX [1 finding: triple-asterisk italicization in Ch 7 line 330 should be downgraded to single-asterisk `*Human Orchestrator*` since the term is already canonically introduced].

#### AI Readiness Scorecard
- **Occurrences:** Ch 1 (~5), Ch 11 (~3), Meridian case study, appendix-action-steps, appendix-prompts.
- **First introduction:** Ch 1 line 6 (in-brief) and Ch 1 line 116: "The AI Readiness Scorecard covers five dimensions of operational readiness."
- **Glossary claim:** "First introduced: Chapter 1" ✓.
- **Capitalization drift:** None — Title Case everywhere.
- **Italicization drift:** Never italicized — including its definition chapter. Coherent if cosmetic.
- **Sub-dimensions consistency:** Constraint Clarity / Information Readiness / Workflow Visibility / Decision Rights / Measurement Discipline. Verified at Ch 1 line 122, line 124, line 148, line 166, line 184, line 202, line 226–230 (scorecard table), line 254–258 (Meridian populated example), and glossary line 12. **Fully consistent** across all references — all five sub-dimensions Title Cased identically.
- **Semantic drift:** None.
- **Verdict:** PASS.

#### Compounding Scorecard
- **Occurrences:** Ch 10 (heaviest, its home) + glossary + appendix.
- **First introduction:** Ch 10 line 136: `## The *Compounding Scorecard*.` (italicized section header) + line 138 / 140 body.
- **Glossary claim:** "First introduced: Chapter 10" ✓.
- **Capitalization drift:** None.
- **Italicization drift:** Ch 10 line 136 italicized in section header. Subsequent mentions plain. Coherent.
- **Verdict:** PASS.

#### Knowledge Map
- **Occurrences:** ~25+ across Ch 3 (introduction), Ch 5 (home — `## Create a *Knowledge Map*.`), Ch 6, Ch 7, Ch 11.
- **First introduction:** Ch 3 line 69 (`**Knowledge Map**` bold definition: "Source produces a **Knowledge Map**"). Ch 5 fully unpacks.
- **Glossary claim:** "First introduced: Chapter 5" ✗ — actually first appears in Ch 3 line 69 as the bold-definition entry. Ch 5 is the home chapter where it's developed in depth but the introduction is Ch 3.
- **Capitalization drift:** Mostly Title Case. Ch 5 line 219 `the Knowledge Map` ✓. Some lowercase ordinary-noun uses ("knowledge maps get richer" Ch 3 line 200; "knowledge map comes from Source" Ch 6 line 212) — those are reasonable as plural-noun / generic uses but the line between proper and common noun is fuzzy.
- **Italicization drift:** Ch 5 line 40 italicized in section header (`## Create a *Knowledge Map*.`). Otherwise plain. Coherent.
- **Verdict:** PASS [1 cross-reference inaccuracy: glossary says first-introduced Ch 5, actually Ch 3 line 69].

#### Constraint Statement
- **Occurrences:** Many (Ch 3, 4, 5, 6, 8, 10, appendix-prompts) — but ALL lowercase as "constraint statement" in chapter prose.
- **First introduction:** Ch 3 line 65 references "Signal produces a constraint statement specific enough that…" (lowercase). Ch 3 line 89 same. Ch 4 line 24 "Signal produces a single artifact: a one-page constraint statement" (lowercase). Ch 4 line 43 / 112 / 183 / 222 / 233 — all lowercase.
- **Glossary claim:** "Constraint Statement" Title Case as canonical, "First introduced: Chapter 4" — the FIRST-INTRODUCED claim works (Ch 4 is where it's most fully developed), but the CAPITALIZATION canonical form does **not** match any chapter usage.
- **Capitalization drift:** **BLOCKER**. Glossary canonical: `Constraint Statement` (Title Case). Chapter prose: `constraint statement` (lowercase) in every single occurrence. Zero matches between glossary canonical and chapter usage. Either the glossary should be lowercased to match chapter convention, OR the chapter prose should be Title Cased to match glossary. Pick one — currently they disagree.
- **Italicization drift:** Never italicized in chapter prose.
- **Verdict:** NEEDS-FIX [1 systemic finding: canonical form mismatch across the book — easiest fix is to lowercase the glossary entry to match the established chapter convention, since the chapter convention is unanimous].

#### Design Brief
- **Occurrences:** Ch 6 line 216 (forward reference) + Ch 6b (home — line 103-117) + Ch 7 (back-references) + appendix.
- **First introduction:** Ch 6 line 216: "is a *Design Brief* — a comprehensive document that captures the design decisions" (italicized, defined inline as forward-ref). Ch 6b line 103: `## The *Design Brief*.` (italicized section header). Ch 6b line 105: "*Design Brief* is that document" (italicized).
- **Glossary claim:** "First introduced: Chapter 6b" — defensible. Ch 6 line 216 references; Ch 6b defines.
- **Capitalization drift:** None — Title Case consistent.
- **Italicization drift:** Ch 6 / Ch 6b italicized at introduction; Ch 7 line 185, 206 plain. Coherent — first-mention italicized, downstream plain.
- **Verdict:** PASS.

#### Design Gate
- **Occurrences:** Ch 6b lines 5, 142, 143, 144, 145, 146, 147, 152, 163 + appendix-action-steps + case studies. Five-item checklist appears in Ch 6b lines 142-147.
- **First introduction:** Ch 6b line 5 (in-brief): "Nothing enters Build until the Design Gate is locked — five items, all checked." Ch 6b line 134: `## Design is the *gate*.` (italicized in section header — "gate" only italicized, not "Design Gate"). Ch 6b lines 142-147: the five-item checklist.
- **Glossary claim:** "First introduced: Chapter 6b" ✓.
- **Capitalization drift:** None — Title Case "Design Gate" consistent.
- **Italicization drift:** Ch 6b never italicizes the full term `*Design Gate*` — it italicizes just `*gate*` in the section header. Coherent if subtly different style.
- **Sub-criteria consistency:** Glossary line 60 lists 5 items: `*Work Deconstruction* complete, all *HAC* fields filled with named supervisors, *Human Orchestrator* named, AI-Assisted vs. Automated decided with rationale, and guardrails defined.` 
  Ch 6b lines 142-147 lists the same 5 items but worded differently:
  - "Every task in the constraint workflow is classified — Work Deconstruction complete..."
  - "Every accountability has a Hybrid Accountability Chart entry with all four fields filled and a named supervisor"
  - "The Human Orchestrator is named — with irreducible decisions and escalation triggers documented"
  - (next two items continue with autonomy + guardrails)
  
  The five items semantically match. Coherent.
- **Verdict:** PASS.

#### Information Flow Specification
- **Occurrences:** Ch 6 lines 62-99 (introduces it), appendix-prompts.qmd, glossary.
- **First introduction:** Ch 6 line 68: "That question produces what I call an *information flow specification*" (italicized, **lowercase**). Ch 6 line 75: "tool for making an information flow visible is a *swim lane diagram*" (lowercase). Ch 6 line 81: "The *information flow spec* tells you *how*..." (italicized, lowercase, abbreviated).
- **Glossary claim:** "Information Flow Specification" Title Case, "First introduced: Chapter 6" ✓ (introduction is correct).
- **Capitalization drift:** **BLOCKER** — same pattern as Constraint Statement. Glossary canonical: `Information Flow Specification` Title Case. Chapter prose: `information flow specification` / `information flow spec` (lowercase) in every occurrence. Zero matches between glossary canonical and chapter usage. Furthermore, even the GLOSSARY's own definition body uses lowercase: "the information flow spec is the route the work takes." The glossary entry contradicts itself.
- **Italicization drift:** Ch 6 italicizes at introduction. Coherent.
- **Verdict:** NEEDS-FIX [2 findings: (1) glossary entry contradicts itself between header and body; (2) glossary canonical Title Case doesn't match unanimous chapter convention of lowercase. Same fix as Constraint Statement — pick one form].

#### Sprint Planning Canvas
- **Occurrences:** Ch 3 (its home) + appendix-action-steps + appendix-prompts.
- **First introduction:** Ch 3 line 5 (in-brief) + Ch 3 line 116: `## The *Sprint Planning Canvas*.` (italicized section header) + line 118 definition.
- **Glossary claim:** "First introduced: Chapter 3" ✓.
- **Capitalization drift:** None — Title Case consistent.
- **Italicization drift:** Ch 3 line 116 italicized in section header; subsequent mentions plain. Coherent.
- **Verdict:** PASS.

#### Sprint Retrospective
- **Occurrences:** Ch 9 (home) + Ch 10 + case studies + appendix.
- **First introduction:** Ch 9 line 5 (in-brief): "You run a Sprint Retrospective" (Title Case, plain text). Ch 9 line 53: `## The Sprint Retrospective.` (section header, no italics). Ch 9 line 56: "The Sprint Retrospective is one of two instruments in the Compound stage."
- **Glossary claim:** "First introduced: Chapter 9" ✓.
- **Capitalization drift:** None.
- **Italicization drift:** Section header in Ch 9 line 53 is NOT italicized (`## The Sprint Retrospective.`) — unlike most other Compound vocabulary section headers (`## The *Hybrid Org Today*.`, `## The *Compounding Scorecard*.`, `## The *Sprint Planning Canvas*.`, `## The *Human Orchestrator*.`). Minor discipline gap; would be a one-character edit to italicize.
- **Verdict:** PASS [1 cosmetic — section header italicization would match the rest of the book's pattern].

#### Work Deconstruction
- **Occurrences:** Ch 6 line 253 (forward reference) + Ch 6b (home, ~10 occurrences) + appendix-action-steps + case studies + glossary.
- **First introduction:** Ch 6 line 253 forward reference. Ch 6b line 5 (in-brief): "Work Deconstruction classifies every task..." (Title Case, plain). Ch 6b line 10: `## Work *Deconstruction*.` (only "Deconstruction" italicized). Ch 6b line 14: `*Work Deconstruction*` (italicized).
- **Glossary claim:** "First introduced: Chapter 6b" ✓.
- **Capitalization drift:** None — Title Case consistent.
- **Italicization drift:** Ch 6b line 10 italicizes only "Deconstruction"; Ch 6b line 14 italicizes both words. Both italicization styles exist within the same chapter. Mild inconsistency.
- **Verdict:** PASS [1 cosmetic — section header could italicize the full term].

#### Signal Backlog
- **Occurrences:** Ch 9 (home) + Ch 10 (~6 references) + Ch 11 + appendix + glossary.
- **First introduction:** Ch 9 line 5 (in-brief): "re-rank your Signal Backlog against what the sprint taught you" (Title Case, plain). Ch 9 line 36: `An updated *Signal Backlog* — the running, prioritized list…` (italicized, defined inline).
- **Glossary claim:** "First introduced: Chapter 9" ✓.
- **Capitalization drift:** None.
- **Italicization drift:** Ch 9 line 36 italicized at introduction; Ch 10 subsequent uses plain. Coherent.
- **Verdict:** PASS.

---

### Tier 3 (Stage names)

#### Signal (stage)
- **Occurrences:** Heavy across Ch 3 (introduction), Ch 4 (home), all downstream chapters.
- **First introduction:** Ch 3 line 46 (as part of `Signal → Source → Design → Build → Deliver → Compound`). Ch 3 line 63-67 "Signal — You find the one operational constraint worth solving next." Ch 4 line 1: `# *Signal*.` (italicized chapter title).
- **Glossary claim:** "First introduced: Chapter 3" ✓.
- **Capitalization drift:** None — Title Case everywhere as a proper noun.
- **Italicization drift:** Chapter title italicized; body plain. Coherent.
- **Semantic drift:** None — Signal's role (name/quantify the constraint) is stable.
- **Verdict:** PASS.

#### Source (stage)
- **Occurrences:** Heavy across Ch 3 (introduction), Ch 5 (home), downstream.
- **First introduction:** Ch 3 line 46 (as part of Sequence). Ch 5 line 1: `# *Source*.` (italicized chapter title).
- **Glossary claim:** "First introduced: Chapter 3" ✓.
- **Capitalization drift:** None.
- **Verdict:** PASS.

#### Design (stage)
- **Occurrences:** Heavy. Ch 6 / Ch 6b are home (split).
- **First introduction:** Ch 3 line 46. Ch 6 line 1: `# *Designing the System*.` (chapter title italicized). Ch 6b line 1: `# *Designing the Work*.` (chapter title italicized).
- **Glossary claim:** Design stage is split across Ch 6 / Ch 6b — verified.
- **Capitalization drift:** None.
- **Verdict:** PASS.

#### Build (stage)
- **Occurrences:** Heavy. Ch 7 is home.
- **First introduction:** Ch 3 line 46. Ch 7 line 1: `# *Build*.` (chapter title italicized).
- **Verdict:** PASS.

#### Deliver (stage)
- **Occurrences:** Heavy. Ch 8 is home.
- **First introduction:** Ch 3 line 46. Ch 8 line 1: `# *Deliver*.` (chapter title italicized).
- **Verdict:** PASS.

#### Compound (stage)
- **Occurrences:** Heavy. Ch 9 is home.
- **First introduction:** Ch 3 line 46. Ch 9 — chapter is named after it.
- **Special note:** Ch 9 line 186 acknowledges the load-bearing trinity of "Compound" — company name, the verb, the stage. Explicitly addressed.
- **Verdict:** PASS.

#### Diagnose / Execute & Compound
- **Occurrences:** Ch 3 (introduction), Ch 5 line 30 ("Source belongs in Diagnose, not Execute"), Ch 5 line 271, Ch 6 line 18 ("Design is the first stage of *Execute & Compound*"), Meridian case study Act I / Act II labels.
- **First introduction:** Ch 3 lines 99-101 (`## Diagnose, then *Execute & Compound*.` section header).
- **Glossary claim:** "First introduced: Chapter 3" ✓.
- **Capitalization drift:** None — `Diagnose` and `Execute & Compound` both Title Case consistent. Note Ch 5 / Ch 6 reduce to "Diagnose" and "Execute" without ampersand-Compound — that's contextually clear since both stages are already introduced.
- **Italicization drift:** Ch 6 line 18 has `*Execute & Compound*` italicized. Ch 3 line 97 section header italicized `*Execute & Compound*`. Otherwise plain. Coherent — italicized at first-mention-per-chapter, plain after.
- **Verdict:** PASS.

---

### Audited additionally (Tier 2, glossary terms not in the primary brief but worth tracing)

#### At-Risk Source
- **Occurrences:** Ch 5 line 170 (introduces it lowercase: "An at-risk source is institutional knowledge that lives in one person's head and is about to leave"), Ch 5 line 172 ("That's the operator math of At-Risk Source" — Title Case once at end).
- **Glossary claim:** "At-Risk Source" Title Case, "First introduced: Chapter 5" — Ch 5 introduction is correct; capitalization is split between the introduction (lowercase) and the closing reference (Title Case) in the same chapter.
- **Capitalization drift:** Mild — three lowercase uses + one Title Case use, all in Ch 5.
- **Verdict:** NEEDS-FIX [1 cosmetic — pick lowercase or Title Case consistently within Ch 5; glossary canonical is Title Case].

#### Organizational Memory
- **Occurrences:** Ch 2 line 50 introduces as `**organizational memory**` (bold, **lowercase**).
- **Glossary claim:** "Organizational Memory" Title Case, "First introduced: Chapter 2".
- **Capitalization drift:** **BLOCKER-tier (within Tier 2)** — defining mention is lowercase. Same pattern as Constraint Statement and Information Flow Specification.
- **Verdict:** NEEDS-FIX [1 finding: capitalization mismatch between glossary canonical and only chapter usage].

#### Parallel Workstreams
- **Occurrences:** Ch 2 (heavy) + glossary.
- **First introduction:** Ch 2 line 198: `**parallel workstreams**` (bold, **lowercase**).
- **Glossary claim:** "Parallel Workstreams" Title Case, "First introduced: Chapter 2".
- **Capitalization drift:** Glossary Title Case; Ch 2 lowercase throughout (lines 5, 198, 206, 210, 297).
- **Verdict:** NEEDS-FIX [1 finding: glossary/chapter capitalization mismatch].

#### Co-Intelligence
- **Occurrences:** Ch 2 (heavy), Ch 3 line 28 / 93 / 200, Ch 10 line 28.
- **First introduction:** Ch 2 line 75: "Co-Intelligence is different. The human and the agent are both inside the loop." Ch 2 line 281: `**Co-Intelligence** is the system half` (bold definition).
- **Glossary claim:** "First introduced: Chapter 2" ✓. Title Case (capital I).
- **Capitalization drift:** None — Title Case consistent ("Co-Intelligence", capital I always).
- **Verdict:** PASS.

#### Decision Rights / Sprint (as Compound vocabulary)
- Decision Rights: Title Case consistent (Ch 1 lines 184, 229, 257, 262; Ch 5 line 26). PASS.
- "Sprint" as canonical vocabulary: see Cross-cutting finding below.

---

## Cross-cutting findings

### Italicization convention drift

The voice charter (per task brief) calls for canonical Compound vocabulary italicized on first appearance per chapter — `***Term***` for canonical first-introduction across the book, `*term*` for downstream references where appropriate.

**Adherence by term family:**
- **Right Seat Evaluation / Sees It / Wants It / Suited for It:** Triple-asterisk in Ch 6 (canonical introduction), single-asterisk in Ch 11 (downstream). **Gold standard — model for the rest of the book.**
- **Center of Excellence Operating Model:** Triple-asterisk in Ch 10. Gold standard.
- **TML framework + Task / Management / Leadership sub-criteria:** Mixed — Ch 6b uses triple-asterisk on lines 5 and 14 but downgrades to single-asterisk on line 12 and removes italics entirely on lines 31, 142. **Inconsistent within the same chapter.**
- **Human Orchestrator:** Single-asterisk italicized at first introduction in Ch 6 line 174-176 (acceptable), then triple-asterisk in Ch 7 line 330 (incorrect — triple-asterisk is for canonical first-introduction only; Ch 7 is the fifth chapter to mention the term).
- **Sequence / Rhythm / Sprint / Knowledge Map / Hybrid Accountability Chart / Constraint Statement / Information Flow Specification:** Mostly plain text throughout chapter prose. Voice charter discipline is **not applied** to these terms. The glossary italicizes them in cross-references but chapter prose treats them as plain proper nouns.

**Pattern:** The italicization discipline is applied where the author actively edited (Ch 6 Right Seat, Ch 10 COE, Ch 6b TML — though Ch 6b is internally inconsistent) but is **absent or partial** for the book's oldest / most-load-bearing terms (Sequence, Rhythm, Sprint, Knowledge Map). Likely an artifact of incremental authorship — Julie-merge chapters got the italicization discipline; older chapters did not.

**Recommendation:** Decide whether the discipline applies to ALL canonical vocabulary or only the "newly-introduced-with-Julie" terms. If the former, run a pass on Sequence / Rhythm / Sprint / Knowledge Map / HAC italicizing them on first-mention-per-chapter. If the latter, document the exception in the voice charter so future audits don't flag it.

### Capitalization convention drift

Three patterns observed:

**Pattern A — Glossary Title Case unmatched in chapter prose** (three terms):
1. `Constraint Statement` — glossary Title Case; chapter prose 100% lowercase (`constraint statement`).
2. `Information Flow Specification` — glossary Title Case; chapter prose 100% lowercase (`information flow specification` / `information flow spec`). Even the glossary body contradicts itself.
3. `Organizational Memory` / `Parallel Workstreams` — glossary Title Case; defining mentions in Ch 2 are bold-lowercase (`**organizational memory**`, `**parallel workstreams**`).

**Pattern B — The "Compound Sprint" lowercase bleed** (six occurrences):
- Ch 7 lines 18, 80, 144, 152, 156: "Compound sprint" / "Compound sprints" (lowercase 's').
- Ch 10 line 36: "Compound sprint cycle" (lowercase 's').
- All other occurrences (Ch 1, Ch 2, Ch 6b, Ch 10 diagram caption) use Title Case "Compound Sprint".
- Even more notably: Ch 6 onwards uses "sprint" lowercase as a generic noun ~117 times (Ch 8 alone has 31 lowercase "sprint" instances), while Ch 3 / Ch 4 (when the term is introduced) use Title Case "Sprint" 40+ times. **This is a bimodal book-wide convention drift.** The book uses two different conventions for "Sprint" — Title Case in Ch 3 / Ch 4, lowercase from Ch 6 onward.

**Pattern C — The "Co-Operation" hyphen-case error** (three occurrences in the definition chapter):
- Ch 2 lines 20, 30, 32: `Co-Intelligent Co-operation` (lowercase second 'o').
- Ch 1 line 70 (preceding the definition chapter): `Co-Intelligent Co-Operation` ✓ (capital second 'O').
- Ch 5 line 22 (following): `Co-Intelligent Co-Operation` ✓.
- Glossary line 26: `Co-Intelligent Co-Operation` ✓ (canonical).
- This is the most surgical capitalization fix in the book — three edits in Ch 2 — and it's in the chapter that defines the title concept.

### Sub-criteria consistency

- **AI Readiness Scorecard five dimensions** (Constraint Clarity / Information Readiness / Workflow Visibility / Decision Rights / Measurement Discipline): **Fully consistent** across Ch 1 introduction, Ch 1 scorecard table, Meridian populated example, and glossary. Gold standard.
- **TML categories** (Task / Management / Leadership): Delimiter inconsistent (`/` slashes in Ch 2 / Ch 5, mixed in Ch 6b — slashes on line 142, commas on lines 14, 31). Italicization inconsistent (triple-asterisk on Ch 6b lines 5/14, none on 31/142). Glossary uses single-asterisk and commas. **The same chapter (Ch 6b) uses three different presentation styles for the same three categories.** Needs reconciliation.
- **PIS phases** (Problem / Identify / Solution): Slashes in Ch 5; commas in glossary. Single-asterisk italics in glossary; plain in chapter. Same pattern as TML but only two reference points.
- **Right Seat Evaluation tests** (Sees It / Wants It / Suited for It): Triple-asterisk in Ch 6 (canonical introduction), single-asterisk in Ch 11 (downstream), single-asterisk in glossary. **Consistent — the model for the other sub-criteria sets.**
- **Design Gate five-item checklist**: Glossary lists 5 items in compressed prose; Ch 6b lines 142-147 lists same 5 items as bulleted checklist. Wording differs but semantic content matches. **No drift, just paraphrase.** Coherent.

### Highest-priority surgical fixes

1. **Ch 2 lines 20, 30, 32 — `Co-Intelligent Co-operation` → `Co-Intelligent Co-Operation`** (capital O on second word). Three edits. This is the book's title concept being miscapitalized in its definition chapter. BLOCKER. Author-judgment-zero.
2. **Ch 7 lines 18, 80, 144, 152, 156 — `Compound sprint(s)` → `Compound Sprint(s)`** + **Ch 10 line 36 — `Compound sprint cycle` → `Compound Sprint cycle`**. Six edits. The defined Compound vocabulary term should not be lowercased when used as a proper noun. BLOCKER for canonical-term integrity.
3. **Sprint capitalization bimodality (book-wide).** Decide: Title Case "Sprint" (matches Ch 3 / Ch 4 / glossary canonical "Compound Sprint" form) or lowercase "sprint" (matches Ch 6+ convention used 117+ times)? Whichever way, the book currently uses both. This is the largest cosmetic finding but the lowest blocker (the meaning never drifts). **Author judgment required.** If Title Case is canonical, you'd be changing ~117 instances across Ch 6–11; if lowercase is canonical, you'd lowercase ~40 instances in Ch 3 / Ch 4 plus update the Glossary entry to "compound sprint".
4. **Ch 7 line 330 — `***Human Orchestrator***` → `*Human Orchestrator*`** (downgrade triple-asterisk to single-asterisk). One edit. Triple-asterisk should be reserved for canonical first-introduction across the book; the term is already canonically introduced in Ch 3 / Ch 6.
5. **Glossary entries for `Constraint Statement`, `Information Flow Specification`, `Organizational Memory`, `Parallel Workstreams`** — reconcile against unanimous chapter convention. Three of four have **zero** matching capitalized form in chapter prose. The path of least resistance is to lowercase the glossary entries (`constraint statement`, `information flow specification`, `organizational memory`, `parallel workstreams`) to match. The path of more author-control is to Title Case the chapter prose throughout — but that's 30+ edits across multiple chapters. Author judgment required on direction.

### Low-priority cosmetic items

6. **Italicization discipline for old-guard terms.** Sequence, Rhythm, Sprint, Knowledge Map, Hybrid Accountability Chart — each is plain text in most chapter prose, while the Julie-merge terms (Right Seat Evaluation, COE Operating Model, TML, Work Deconstruction, Design Brief, Design Gate, Compounding Scorecard) get italicization. Decide whether the discipline is universal or scoped.
7. **TML sub-criteria delimiters within Ch 6b.** Three presentation styles for the same three categories. Pick one.
8. **PIS Framework "framework" capitalization.** Lowercase 'f' in chapter prose vs. capital 'F' in glossary. Minor.
9. **Glossary "first introduced" claims for TML, Knowledge Map.** Both terms appear in chapters before their claimed home chapter (TML in Ch 2, Knowledge Map in Ch 3). Minor cross-reference accuracy.
10. **Ch 9 line 53 section header `## The Sprint Retrospective.`** — could italicize as `## The *Sprint Retrospective*.` to match the pattern set by `## The *Hybrid Org Today*.`, `## The *Compounding Scorecard*.`, `## The *Sprint Planning Canvas*.`, etc.
11. **Ch 5 At-Risk Source capitalization.** Lowercase at introduction, Title Case once at the end of the same chapter. Pick one (glossary canonical is Title Case).

---

## Cross-reference cascade flags

Notes for Audit 4 (the cross-reference accuracy audit):

- **Glossary line 117 (TML Framework) claims "First introduced: Chapter 5"** — actually first appears Ch 2 line 259 with full sub-criteria. The Ch 2 line literally says "Chapter 5 introduces the full design instrument — the **TML framework**", which is the author's intent (Ch 5 introduces the *full* instrument), but a strict reader sees TML in Ch 2 and would expect the glossary to credit Ch 2.
- **Glossary line 78 (Knowledge Map) claims "First introduced: Chapter 5"** — actually first appears Ch 3 line 69 as the bold-definition `**Knowledge Map**` entry. Ch 5 is the home chapter where it's developed, but the introduction is Ch 3.
- **Glossary line 45 (Compound Sprint) claims "First introduced: Chapter 3"** — term appears in Ch 1 line 232 ("Compound Sprint framework") and Ch 2 line 28 ("A Compound Sprint... is how you do that work"). Ch 3 is where the Sequence is unpacked, but the phrase "Compound Sprint" appears earlier.
- **Ch 7 line 195 references "The Chapter 3 Compound Sprint"** — Ch 3 does define / introduce it. Accurate.
- **Ch 11 line 116 — `**Design** (Chapter 6) — Architect the solution`** — should likely read "Chapters 6 and 6b" since the Design stage is explicitly split across two chapters (Ch 6 = system, Ch 6b = work). Glossary entry for Design Gate references Ch 6b; for Hybrid Accountability Chart references Ch 6. The split is canonical; Ch 11's reference papers it over.
- **Ch 2 line 259** explicitly forward-references TML to Chapter 5, which is the cleanest forward-reference pattern in the book. Use it as a model.

## Verdict

**Term-usage layer:** Broadly coherent at the semantic level — no canonical term flipped meaning between chapters. The Right Seat Evaluation discipline (triple-asterisk first-introduction, single-asterisk downstream, stable sub-criteria) is the cleanest pattern in the book and should be the model.

**Layer needing surgical cleanup:** Capitalization and italicization. The book has a small number of high-impact defects (Co-Operation lowercase in the defining chapter; Compound Sprint lowercasing in Ch 7 / Ch 10; bimodal Sprint capitalization Ch 3-4 vs. Ch 6-11) and a larger number of cosmetic ones (glossary terms with no matching capitalized form in chapter prose; italicization discipline applied unevenly between old-guard and Julie-merge terms; sub-criteria delimiter inconsistencies).

**Author-judgment-required calls** (3):
- Sprint capitalization direction (Title Case to match Ch 3 / glossary, or lowercase to match Ch 6+ majority).
- Italicization scope (universal canonical-vocab discipline, or scoped to Julie-merge terms).
- Glossary canonical capitalization for Constraint Statement, Information Flow Specification, Organizational Memory, Parallel Workstreams (Title Case the chapter prose, or lowercase the glossary).

**PR readiness:** **Needs surgical fixes before PR.** The three blocker-tier findings (Ch 2 Co-Operation case, Ch 7/10 Compound Sprint case, four glossary-vs-chapter capitalization mismatches) are 12-15 specific edits across five files, all with clear directional resolution. The remaining items are cosmetic and could be deferred or batched into a separate polish pass.

**Total edit estimate (blocker-tier only):** ~15 single-line edits across `chapters/02-co-operating-model.qmd` (3), `chapters/07-build.qmd` (5), `chapters/10-the-rhythm.qmd` (1), `chapters/appendix-glossary.qmd` (4-5 entries), `chapters/05-source.qmd` (1 — At-Risk Source). Estimated execution time: 20-30 minutes once author confirms direction on the three judgment calls.
