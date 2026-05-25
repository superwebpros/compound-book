# Stale-Reference Audit — Phase 4 Prep

Generated: 2026-05-24
Purpose: Confirm previously-struck content has not regressed and surface risks the Julie merge must respect.
Method: `grep -rni` across `chapters/*.qmd` and `index.qmd`; `git log --grep` for chronology; cross-ref against `_julie/edit-manifest.md` and persistent memory (`bd memories`).

---

## Section 1 — Stale-reference findings

| Term searched | Hits in current prose | Verdict | Files / lines |
|---|---|---|---|
| **Greenline Home Services** | 3 (intentional, with disclosure) | **STALE — review required** | `chapters/11-what-to-do-next.qmd:164, 167, 192` |
| **Meridian Consulting Group** (old name) | 0 | Clean | — |
| **Meridian Manufacturing** (current name) | many (intentional) | Clean | Ch01, Ch03, Ch06, Ch06b, Ch07, Ch08, Ch09, Ch10, glossary |
| **Ahmed** (developer real name) | 0 | Clean | — |
| **Donna** (real name) | 0 | Clean | — |
| **Harley** (anonymized → "our marketing lead") | 0 | Clean | — |
| **Saint Clair Systems** (anonymized → "a manufacturing company") | 0 | Clean | — |
| **Bench / Skills Library** (deprecated product references) | not checked exhaustively here; commit `48cef93` purged them | Likely clean | — |
| **13-to-8 headcount** | Multiple — framed cumulatively as "over the following year" | Clean (framing OK) | `chapters/01-diagnosis.qmd:49`, `chapters/10-the-rhythm.qmd:8, 22`, `chapters/11-what-to-do-next.qmd:206`, `chapters/09-compound.qmd:167` |
| **Ch02 opening (Marina/coordinator)** | Marina + marketing coordinator story | Clean — current polished version | `chapters/02-co-operating-model.qmd:8-12` |
| **Ch04 L10 opening** | L10 / project coordinator / $24K subcontractor scenario | Clean — current polished version (not the original "nine red weeks") | `chapters/04-signal.qmd:8-16` |
| **Nine red weeks** | 0 | Clean — fabricated framing fully removed | — |
| **Marketing coordinator** (Ch02 opener) | Marina + parallel-workstreams story | Clean | `chapters/02-co-operating-model.qmd:8-14` |

### Greenline detail (the only "Stale" finding)

The Greenline Home Services name was reintroduced in `chapters/11-what-to-do-next.qmd` as an "illustrative example built from patterns across multiple Compound engagements" (line 164). It is NOT prefixed as fictional in the way `case-study-meridian.qmd` opens (italicized disclaimer up front). Persistent memory `ch11-greenline-fabricated` flagged it as needing disclosure or replacement; current state has **partial disclosure** (one inline sentence on line 164), but the cast (Dana / Maria / James, $3M revenue, home services) reads as a fully-specified company.

Decision needed from Jesse: keep with current disclosure, strengthen the disclosure to match Meridian's italicized callout, or replace the named company with a generic "illustrative first sprint plan" — no company name, no people names.

### Disclosure status of named entities

| Entity | Type | Disclosure |
|---|---|---|
| Meridian Manufacturing (Mark Ellison, Elena Ruiz, Dave Kowalski, Ty Banfield, Carlos) | Fictional composite | Disclosed up front in `chapters/case-study-meridian.qmd:3` and in `chapters/01-diagnosis.qmd:229` ("we built a fictional company from the real patterns") |
| Greenline Home Services (Dana, Maria, James) | "Illustrative" example | Inline one-sentence disclosure on `chapters/11-what-to-do-next.qmd:164` only |
| PM Agent Team case study (Sofia Reyes, Rachel, Lucas, Jesse) | Real story from SuperWebPros | Rachel anonymized inline ("we'll call Rachel" on line 5). Sofia Reyes and Lucas are **not** declared anonymized. See §4. |
| SuperWebPros | Jesse's real company | Named directly in `chapters/01-diagnosis.qmd:49` — intentional. |
| Marina (Integrator, Ch02 opener) | Real person, first name only | No explicit anonymization disclosure; first name only. See §4. |

```jf-note:
Greenline isn't real; needs to be scrubbed EVERYWHERE
```

---

## Section 2 — Recent decision context (from git log)

Chronological view of what was struck/replaced and when. Helps Phase 4 understand WHY a section reads the way it does today.

| Commit | Date | Relevance |
|---|---|---|
| `0e5f2e3` | 2026-05 (earlier) | Initial story insertion across 12 chapters (Phase 2 of original revision epic) — many stories later flagged as fabricated |
| `653cff3` | 2026-05-16 | Anonymized Harley (→ "our marketing lead") and Saint Clair Systems (→ "a manufacturing company") cross-chapter |
| `48cef93` / `fbc0892` | 2026-05-17 | Purged Bench and Skills Library product references book-wide and from Ch04 |
| `085108a` | 2026-05-17 | Added Jesse's editorial notes to Ch08–11, baseline for the coherence pass that followed |
| `d687d84` | 2026-05-17 | Added `llm.txt` as cross-chapter coherence source of truth (includes fabrication map) |
| `6c99346` | 2026-05-17 | **Major struck-content commit.** Replaced fabricated Marina/Donna and chutes-and-ladders fabrications with sourced content. Threaded Meridian Manufacturing through Ch01–10 (replaced ghost examples). Threaded PM Agent Team through Ch02/Ch04 openings. Added fictional-composite disclosure to Meridian. |
| `df87abb` | 2026-05-17 | Fixed Meridian case study: coaching model, Design Brief, swim lane, AI-tell cleanup |
| `7709ea8` | 2026-05-18 | Round 2 author review — resolved 33 jf-notes across 8 chapters. **Key: replaced Ch04 opening with PM Agent Team case study; reframed coordinator diagnosis as capacity/capability/redesign.** Also fixed chutes-and-ladders chronology in Ch02. |
| `7bfc51b` | 2026-05-18 | Resolved preface jf-notes; expanded developer-departure story (knowledge predates AI, KM systems built first, AI layer added when tech matured); moved quote-agent-team case study to research/. |
| `124f777` | 2026-05 | Wired Excalidraw shortcodes into chapters |
| `bfc6f9b` → `e60c512` | 2026-05-24 | Phase 0/1 Julie integration: edit manifest, INTEGRATION-PLAN, julie-final |

Key insight: the L10 / $24K subcontractor opening in Ch04 (currently on lines 8–16) is the **polished replacement** that came out of commit `7709ea8`. It is NOT the original fabricated "nine red weeks" opening. Julie's E24 instruction is voice-shift only (add "Jesse:" attribution, convert we↔I) — it does not propose restructuring the story itself.

Similarly, Ch02 opening with Marina + marketing coordinator is the sourced replacement from `6c99346`. The original fabricated CEO-flat-headcount opening is fully gone.

```jf-note:
Marina/Donna and chutes-and-ladders were NOT fictional; they were/are real.
```

---

## Section 3 — Risks the Julie merge must respect

These are places where Julie's redline lands on top of polished, struck-and-replaced, or fragile prose. Cross-ref E-row from `_julie/edit-manifest.md`.

1. **E24 (Ch04 L10 opening) — CH04-L10 conflict flag.** Julie's voice-shift adds "Jesse:" and converts "I asked" → "we asked" in the body. Risk: a careless edit could regress to the older fabricated "nine red weeks" framing if the agent generating the edit relies on Julie's redline as the source-of-record instead of the current `chapters/04-signal.qmd`. Mitigation: explicitly point Phase 4 execution at the current qmd as the substrate; Julie's edit is voice-shift only, not story replacement.

```jf-note:
I think we need to treat Julie's contributes as additive and our current manuscript as the eexising canon. What we may need to do is have an agent review the 'unique' elements of Julie's experience and narrative and then decide an _integrative_ rather than _redactive_ approach. 
```

2. **E01/E02/E04 (Preface) — index.qmd full restructure.** Julie restructures the preface to a dual-author opening ("We came to the same conclusion from opposite directions") and adds her 2022 global food safety company founding story (E03). Risk: the current preface's chutes-and-ladders developer story (lines 3–5) is the canonical version of that anecdote. Julie's restructure must preserve the developer-departure story content; only the framing wrapper changes. Persistent memory flagged `ch02-opening-fabricated-replace-with-marina` and the chutes-and-ladders story as load-bearing and sourced.

```jf-note:
Her preface is fine; it adds much content than mine does not, but it reads like AI. Again, the _content_ is fine (unless otherwise noted) - its the tone that's not.
```

3. **E60 (Anonymization convention) — collision risk with PM Agent Team case study.** Julie's convention introduces anonymized employer descriptors ("global food safety company", "global automotive supplier", "mid-market precision manufacturing company"). These are for **Julie's biographical references** per the manifest note. Risk: if applied book-wide without scoping, it could:
   - Re-anonymize SuperWebPros (intentionally named in Ch01:49)
   - Anonymize Meridian's industry framing in a way that breaks the fictional-composite stylization
   - Conflict with Sofia Reyes / Lucas in the PM Agent Team case study (not currently anonymized)
   Mitigation: edit-manifest §138 explicitly scopes E60 to Julie's bio references only; enforce that boundary in Phase 4.

4. **No E-row touches Greenline Home Services**, but Julie's Ch11 edits (E50, E51-rejected) restructure portions of `chapters/11-what-to-do-next.qmd`. Risk: a structural reshuffle of Ch11 could leave the Greenline illustrative example orphaned, or could amplify its visibility (e.g., move it earlier in the chapter). Phase 4 needs to actively decide whether the Greenline example stays, is reframed with stronger disclosure, or is replaced with a generic placeholder. Persistent memory `ch11-greenline-fabricated` flagged this; the partial disclosure in line 164 is the current state.

5. **E37, E49 (BLOCKED — Pattern Drag, COE Model)** and the global anti-pattern on framework attribution (manifest line 57). Risk: any framework-add row that slips through without the attribution scrub could re-introduce "this came from Julie's 20-year practice" framing — which is rejected globally. This is orthogonal to stale-reference regressions but is the same class of risk: Phase 4 generates prose against Julie's source, and Julie's source contains framing the team has explicitly removed elsewhere.

6. **The 13-to-8 headcount thread** appears in five places (Ch01, Ch09, Ch10 ×2, Ch11) and is framed cumulatively as "over the following year" in every instance. Risk: any edit that re-frames it as a single-moment shift (e.g., "we went from 13 to 8 last quarter") would regress against the persistent memory `13-to-8 headcount shift is a real observation` (cumulative scorecard / Stripe-data-over-time framing). No E-row directly targets this thread, but several E-rows touch Ch10 and Ch11 — keep an eye on framing during merge.

---

## Section 4 — Recommended additional anonymizations

These are named entities currently in the prose that may warrant author decision before Julie merge, since they are not on the E60 anonymization list but follow the same logic as the Harley / Saint Clair anonymizations already executed (`653cff3`).

| Entity | Where | Currently | Recommendation |
|---|---|---|---|
| **Sofia Reyes** | `chapters/case-study-pm-agent-team.qmd` (many), `chapters/07-build.qmd:12` | Full name used directly | Decide: keep (with her permission), first-name-only, or anonymize ("our VP of Operations"). Currently her last name appears 1× in the case study header. |
| **Lucas** (Creative Lead) | `chapters/case-study-pm-agent-team.qmd` (5 mentions) | First name only | First-name-only is already lighter; decide whether to anonymize further ("our creative lead") for consistency with the marketing-lead pattern. |
| **Marina** (Integrator, Ch02 opener) | `chapters/02-co-operating-model.qmd:8, 10`, `chapters/05-source.qmd:8, 30` | First name only | First-name-only is already light; decide whether to anonymize ("my Integrator") for consistency. Note: she is named twice in the Marina+coordinator opener and twice in Ch05. |
| **Rachel** (PM Agent Team subcontractor) | `chapters/case-study-pm-agent-team.qmd` (extensive), `chapters/07-build.qmd:12` | Anonymized inline ("we'll call Rachel") | Already disclosed; no action needed. |
| **Dana / Maria / James** (Greenline cast) | `chapters/11-what-to-do-next.qmd:178–180, 192` | Illustrative, with single-sentence disclosure | See risk #4. If Greenline is reframed, these go away or get strengthened disclosure. |
| **Meridian fictional cast** (Mark Ellison, Elena Ruiz, Dave Kowalski, Ty Banfield, Carlos) | Many chapters | Fully disclosed as fictional composite | No action needed. |

Note: The book also names SuperWebPros (Ch01:49) and Jesse Flores (multiple) directly. These are intentional and should NOT be anonymized.

Additionally, the PM Agent Team case study (`chapters/case-study-pm-agent-team.qmd`) has **no italicized "this is a real story / names changed" disclosure** at the top, unlike `case-study-meridian.qmd` which opens with a clear composite disclaimer. Recommendation: add a one-line disclosure at the top of that case study clarifying which names are pseudonyms (Rachel) and which are real (Sofia, Lucas, Jesse) — consistent with the Meridian convention.

```jf-note:
Sofia is the anonymized name for marina or donna; i don't remember. Same with Lucas. Anything in _my_ appendix should already be treated as canon.
```

---

*End of audit.*
