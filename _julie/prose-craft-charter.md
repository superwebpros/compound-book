# Prose-Craft Charter

The canonical spec for *clarity, simplicity, and pacing* in *Co-Intelligent Co-Operation*.
Sibling to `voice-charter.md`. **Voice** answers "does it sound like us." **Craft** answers
"is it clear, simple, and well-paced." Different question, different canon, same scan pipeline.

North star (author direction, memory `book-chapter-flow-and-meridian-thread`): **simplify, simplify,
simplify** — the audience is a smart but non-technical entrepreneur; the AI field already bewilders
them. Read this before any prose-craft edit or review.

---

## The canon this charter operationalizes

- **William Zinsser, *On Writing Well*** — clutter, concision, one idea per unit, cut throat-clearing.
- **Joseph Williams, *Style: Lessons in Clarity and Grace*** — characters as subjects, actions as
  verbs, kill nominalizations, old-information-before-new (cohesion).
- **Gary Provost** — sentence-length *variation* is rhythm; monotone length reads as drag.
- **Roy Peter Clark, *Writing Tools*** — long sentences for flow, short for emphasis; ladder of
  abstraction (concrete vs. abstract).

---

## Calibrated targets (from Traction, the reference text)

Measured on the *Traction* audiobook transcript, 2026-06-15 (`/tmp/traction_rhythm.py`). These are
**targets, not gates** — see the metrics-assisted-judgment rule below.

| Metric | Traction (target band) | Tool flag |
|---|---|---|
| Sentence-length CV (per chapter) | 0.43–0.71, mean **0.56** | < 0.45 = monotone/drag |
| Mean sentence length | 15.5w (median 14w) | — |
| Short sentences (≤8w) | ~21% | — |
| Long sentences (≥40w) | ~1.6% | run-on flag |
| Nominalization density | **3.2 / 100 words** | only > 3.6 = genuine outlier |

**Calibration lesson:** Traction itself runs 3.2 nominalizations/100, so raw abstraction density is a
weak signal — the book's gold standard is "heavy" by a naive threshold. What matters is **local
concentration** (a pile-up in one paragraph) and **whether the abstraction earns its place**, which
is a judgment call, not a number.

---

## The rules (highest-leverage first; each with a Ch 1 worked example)

### 1. Advance, don't restate. *(the #1 drag — idea pacing, not sentence pacing)*
A paragraph must move the argument forward, not re-say the thesis in new words. Restatement is the
book's most common drag and no metric catches it cleanly.
- **Ch 1 example:** "operating problem, not technology problem" appears in the title, L17, the L89
  Pro Tip, and L114; "the math moves when the structure changes" recurs at L71/L75/L94. One idea,
  six wordings. **Fix:** state it once at full strength; downstream mentions become one-clause callbacks.

### 2. Concrete over abstract. *(Williams)*
Prefer a person doing a thing over an abstract noun. Watch nominalization **pile-ups**, not average
density.
- **Ch 1 example:** L98 "Co-Operation is the structural work of getting that workforce to operate
  together"; L162 "the operating-model preconditions that determine whether your organization will
  hold the change." **Fix:** name the actor and the action; break the stacked clauses.

### 3. Show, don't tell. Cut throat-clearing.
Delete sentences that *assert* importance or claim an effect the prose hasn't earned.
- **Ch 1 example:** L45 "This pattern is common. It might describe your company."; L114 "None of this
  is mysterious. All of it is operating work, not technology work."; L100 "Culture, training, and tool
  selection are all real factors. The operating model is the bigger problem." **Fix:** cut, or replace
  with one concrete beat.

### 4. Vary the rhythm. *(Provost)*
Keep per-chapter sentence-length CV in Traction's band (~0.56). Watch for monotone runs (5+ same-length
sentences) and run-ons (≥40w). Short sentences are fine — Compound runs ~35% short vs Traction's 21%;
that's punchy, not wrong, unless it becomes choppy.

### 5. One name per concept.
A concept gets exactly one label. Term drift is friction.
- **Ch 1 example:** "Headcount Paradox" (L55/71/89) vs "Headcount Math" (L79). **Fix:** pick one.

### 6. Cut clichés and filler. *(Zinsser)*
- **Ch 1 examples:** "leaving something on the table" (L15), "keeps you up at night" (L160).

### 7. Avoid the antithesis tic. *(also a voice-charter anti-pattern)*
Negative-parallelism ("not X, but Y" / "The failure isn't AI's") is fine once; as a cadence it becomes
a verbal habit. Ch 1 carries several (L67, L69, L114).

---

## The operating principle: metrics-assisted judgment, never a metric gate

The Ch 1 test (2026-06-15) proved it: the deterministic layer came back clean (CV 0.67, proselint
clean) on a chapter that needed work. **Metrics surface candidates; the judgment layer decides.**
- A flat paragraph may be a deliberate staccato list — not drag.
- A 40-word sentence may earn its length — check before cutting.
- Nominalization density near Traction's 3.2 is normal — only pile-ups matter.
Never pass/fail a chapter on a number alone.

---

## Pipeline

1. **Deterministic:** `voice-scan.py` now includes the rhythm/craft section (`prose_rhythm.py`:
   Provost CV, monotone runs, flat paragraphs, run-ons, Williams nominalization, proselint).
2. **Judgment:** the `prose-craft` agent reads the scan + the chapter and applies rules 1–7 above,
   citing the canon and line numbers. It flags; it does not silently rewrite.
