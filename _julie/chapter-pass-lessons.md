# Chapter-pass lessons — the Ch7 Build round (2026-07-26)

Author verdict on the Ch7 produce pass: **3/5**. "Poorly written, difficult to skim, confusing in a lot of places, tone doesn't match voice." 22 jf-notes.

This file abstracts those notes into principles. Read it before drafting or reconciling any chapter. It is the answer to *why did every gate pass and the prose still fail?*

---

## The headline: our gates measure violations, not quality

Ch7 passed everything and was still judged slop. Measured after the fact:

| Metric | Ch7 | Signal (exemplar) | Source (exemplar) | Verdict |
|---|---|---|---|---|
| Flesch reading ease | 56.4 | 65.8 | 58.4 | in band |
| Grade level | 9.2 | 7.6 | 9.1 | in band |
| Words/sentence | 15.3 | 14.2 | 16.2 | in band |
| Paragraphs >120 words | 1 | 0 | 3 | **better than Source** |
| Vale alerts | 5 | — | — | improved 8→5 |
| n-gram repeats | 16 | — | — | improved 19→16 |
| **Total words** | **7,211** | 4,514 | 6,166 | **longest chapter in the book** |

*Remediation round (same day): 7,211 → 6,122 words, now just under Source. Flesch moved 56.4 → 55.5 and grade 9.2 → 9.5 — slightly denser per sentence, because cutting bulk removes connective prose. That trade is correct: the author's complaint was skimmability and bulk, not sentence difficulty. It is also a reminder that Flesch is not the target and optimizing for it would be the same mistake in a new direction.*

Every readability metric is fine. The one number that is *not* fine is length: Ch7 is 60% longer than Signal and 17% longer than the next-longest chapter.

**Lesson: sentence-level metrics cannot detect the failures that actually make a chapter unreadable.** Those failures are register, organization, invented authority, and bulk. Stop treating a clean Vale/voice-scan run as evidence the prose is good. It is only evidence that no banned string is present.

---

## P1 — Register and tense must hold within a run of prose

**Failure (Ch7 L8–32):** the opening moves story (past) → instrument lecture (present imperative) → Canvas rollup → chapter roadmap → diagram. Four register switches in 25 lines. Author: *"Why are we switching tenses? … I'm not really sure about the organizational scheme here."*

**Test:** read any three consecutive paragraphs aloud. If the speaker changes — storyteller, instructor, narrator of the book's own structure — either transition explicitly or move one block.

**Corollary:** don't interrupt a story to teach an instrument. Finish the beat, then turn.

## P2 — Gloss a term once per BOOK, at first use, not once per chapter

**Failure:** Ch7 re-glossed the Hybrid Accountability Chart (L8) and Human Orchestrator (L48) — both used since Ch3, both with worksheet exercises behind them. Author: *"why are we redefining terms? if we already specified it before we dont need to parenthetical it"* and *"If you've made it this far, you should've already done the hybrid accountability chart exercise."*

**Test:** before adding a parenthetical gloss, grep the corpus. If the term is defined in an earlier chapter, cite forward at most (`see the X chapter`) or say nothing. Glosses are for genuinely new terms.

**Note:** this is a correction to how the jargon house rule was being applied. First use means **first use in the book**.

## P3 — No invented authority

Three distinct forms, all present in Ch7:

- **Fabricated comparative stats.** "The assumption that Build means 'hand it to engineering' kills more Sprints than bad specs do." Author: *"what?! thats a complete unfounded claim."*
- **Contrived heuristics.** "Fifteen minutes against three hours is a build worth making. Two hours against three is a design gap wearing a spec." Author: *"what? why? this feels so contrived."* A rule of thumb has to be derived from something, not invented to fill the template's heuristic slot.
- **Unsourced assertions.** "hiring a freelancer for a day or two is normal — and still far cheaper than a standing engineering team." Author: *"where does this come from?"*

**Test:** every number, comparison, and rule of thumb traces to Meridian, a Compound story, or a cited source. If it exists to satisfy a structural slot, cut the slot.

## P4 — Don't editorialize about your own content

**Failure:** "That bar is deliberately high." Author: *"thats not a high bar, its just done. what are we trying to communicate here? is this an attempt at prose?"* And "a prototype sitting in a sandbox" → *"obviously."*

**Test:** delete any sentence that characterizes the significance of what you just said instead of saying something. State the bar; don't announce that it's high. Cut anything a competent reader would call obvious.

## P5 — Commit to one teaching location

**Failure (L245–256):** the moves block gave each of the seven checks a one-line definition, and the teaching below defined them again. Author: *"we should treat the above like a bullet list and not like a definition list. If we're gonna do the definitions down here, then commit to definitions down here and use the above purely as a checklist. I think it's confusing like this."*

**Test:** a roadmap is a bare scannable list of labels. Teaching lives in one place, below. Half-defining in both is worse than either alone. This is the single most repeatable structural error the per-step template produces.

## P6 — List-shaped content is a list

**Failure:** "Every workflow's failure list draws from the same five families: missing data, an unrecognized input, a system that's down, low-confidence output, and an out-of-range result." Author: *"why isnt this bullets?"*

**Test:** three or more parallel items in a sentence become bullets. Already a house rule; it was under-applied because prose passed the paragraph-length check.

## P7 — Abstract instruction needs a concrete instance

**Failure:** "Check 1: Search for existing capabilities before building" → *"like what?"*. "Check 2: Confirm the environment matches Design's category" → *"what does this mean?"*

**Test:** every checklist item and every step carries one concrete instance. If you can't produce one, the item may not be real.

## P8 — Action steps must be executable by the actual reader

**Failure:** "put them in front of the tool and let them build." Author: *"what if they dont know how? most people wont."*

**Test:** does the action step assume a capability the book has not built? If yes, either build it or name the gap honestly.

## P9 — No vague evocative modifiers

**Failure:** "Don't try to absorb it quietly" → *"quietly? what does that mean?"* And "the architecture you wish you had" → *"is a nonsense statement."*

**Test:** if a word sounds meaningful but you cannot say what it specifies, cut it.

## P10 — Show provenance for anything inherited

**Failure:** the seven guardrails questions → *"Where are these questions first articulated? where do they come from? I don't recall them from the previous chapters."* Bedard's three-agent ceiling → *"is this true? i dont recall it. source?"*

**Test:** a chapter pointer is not provenance. If the reader is expected to recall something, restate the substance in one clause, not just the cross-reference.

## P11 — Attribute failure modes to the right actor

**Failure:** scope drift blamed on "the engineer or vendor or low-code builder." Author: *"usually its not the vendor or engineer who wants to add scope, its the process owner who 'wants more' than what they scoped."*

**Test:** check claims about who does what against the authors' actual operating experience. Plausible ≠ true.

## P12 — Length is a defect

7,211 words. Nothing individually flagged; cumulatively unreadable. The per-step teaching template, applied across four numbered instruments (8 spec sections + 7 audit checks + 7 guardrails questions + 5 Done questions = 27 enumerated items), inflates without anyone noticing because each addition looks locally justified.

**Test:** budget against Signal (4,514) and Source (6,166). A chapter materially longer than Source needs a reason. When the template and the word budget conflict, the budget wins — the template is a default, not a law.

---

## What this means for the pipeline

1. **Add a length budget to the gate.** Word count vs. the exemplars, reported, before the judges run.
2. **The judges need these principles as explicit criteria.** Prose-craft caught mechanical cadence and the 184-word paragraph; it did not catch invented heuristics, re-glossing, or register drift, because nothing told it to look.
3. **The per-step template is the leading cause of P3, P5, and P12.** Its heuristic slot invites invented rules; its roadmap+teaching pairing invites double-definition; its per-item expansion drives length. Apply it where it earns its place.
4. **A clean gate is not a green light.** Ch7 shipped to the author with every check passing.
