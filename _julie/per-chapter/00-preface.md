# Scout Plan — `index.qmd` (Preface)

**Generated:** 2026-05-25  ·  **Bead:** book-ff63.9.1  ·  **Scout:** Sage

## Chapter context (one paragraph)

The Preface is currently a tight 17-line opener entirely in Jesse's first-person voice. It does five things in order: (1) the developer-departure / chutes-and-ladders origin story (L3); (2) the knowledge-as-asset realization that produced KM systems, EOS discipline, and AI-readiness (L5); (3) a single-sentence pivot — *"That moment is why this book exists."* (L7); (4) the design-before-deploy framing + six-step Sequence handoff (L9–13); (5) the authorship paragraph that closes on *co-intelligent co-operation* (L17). The most recent commit touching this file is `7bfc51b` (2026-05-18, "Resolve preface jf-notes, housekeeping") — that commit expanded the developer-departure story to include the KM-systems-built-first → AI-arrived-ready arc. **That two-paragraph arc (L3 + L5) is the canonical, sourced version of the chutes-and-ladders story** and is load-bearing — `stale-audit.md` §3.2 explicitly flags it as protected. Julie's restructure does not propose deleting it; she wraps it with a dual-author frame and adds Julie's parallel founding story. There is no rejected-row collision in this chapter — every E-row in scope (E01–E06) is APPROVED in the manifest. E07 is RELOCATED to About-the-Authors per Q3 (out of scope here).

**One pre-existing voice problem in the current chapter:** L11 contains the A1 anti-pattern verbatim — *"The Sequence is not a concept to absorb. It is a process to execute."* This is the exact sentence Jesse flagged at `_julie/julie-final.md:102` as the canonical abstract-noun-equals-abstract-noun trap. It is already in our manuscript. Flagged below as an opportunistic cleanup during E05 (the paragraph it lives in is being touched anyway).

## E-row classifications

| E-row | Type | Verdict | Current-chapter target | Notes |
|---|---|---|---|---|
| E01 | STRUCTURE | LAND-WITH-MODIFICATION | New line inserted before L3 | Lands as blended-we opening line per Q-E21; **no `Jesse:` inline tag** |
| E02 | ATTRIBUTION | LAND-WITH-MODIFICATION | L3 (developer-departure paragraph) | Attribution lands via in-prose phrasing ("Jesse was…") inside E01's setup, NOT as inline `Jesse:` tag per Q-E21 |
| E03 | NEW-SECTION | LAND-WITH-MODIFICATION | New paragraph(s) inserted after L5, before L7 | **Path B / Design Table candidate** — risk map: HEAVY REWRITE; Julie's source has multiple AI patterns |
| E04 | VOICE-SHIFT | NEEDS-AUTHOR + LAND-WITH-MODIFICATION | Replace L7 single line | Substance issue: Julie's replacement frames "AI breaks the design" — JF flagged this framing as causally wrong (see Conflicts §1). Substance reframe required before prose work. |
| E05 | VOICE-SHIFT | LAND | L9 ("you've" → "you have"); minor I→we audit across L9, L13, L15 | LOW-risk word-level. **Opportunistic A1 cleanup of L11 in same pass** (see notes). |
| E06 | NEW-SECTION | LAND-WITH-MODIFICATION | Rewrite L17 (final paragraph) | **Path B / Design Table candidate** — risk map: HEAVY REWRITE; Julie's bio source has triplet pileup + AI-tell closer; co-intelligence introduced un-staked here |

**Counts:** 4 LAND-WITH-MODIFICATION · 1 LAND · 1 NEEDS-AUTHOR (E04, hybrid — see below) · 0 SKIP-ALREADY-DONE · 0 hard CONFLICT (E04 is a substance conflict, not a polish-collision conflict).

---

## Per-E-row acceptance criteria

### E01 (STRUCTURE, LAND-WITH-MODIFICATION) — dual-author opening line

**Substance to preserve:**
- The "two practitioners arrived at the same insight from opposite directions" frame
- That what follows is a partnership, not a Jesse-solo book

**Modification from Julie's instruction:**
- Julie proposes the opening line *"We came to the same conclusion from opposite directions."* That line is rare-CLEAN per the risk map and can land as-is.
- **Do NOT** introduce an inline `Jesse:` tag for the developer-departure paragraph (Julie's redline at line 87 inserts the tag explicitly; per Q-E21 the convention is blended "we" with in-prose attribution, not transcript-style author tags).
- Instead, the developer-departure paragraph is introduced in prose: e.g., *"Jesse was in his office when a developer who had been with him for years put in his notice…"* — the attribution lands without the tag.

**Anti-pattern risk:**
- A3 (triplet pileup) — Julie's source has *"the technical architecture and the human capital discipline"* style phrasing; the opening line itself is clean but the supporting setup must not slip into A3.
- A2 (coined term before stakes) — do NOT use "co-intelligence" or "Co-Operating Model" in the opening setup. Reserve coined vocabulary for after stakes are established.

**Framework-attribution rule:** N/A for this row (no framework introduced here).

**Coherence:**
- E01 + E02 together rewrite the first 1–3 lines of the preface. The developer-departure paragraph body (L3 from "I'm sitting there realizing I've just lost something…" forward) **must remain verbatim or near-verbatim** — that prose is sourced and the chutes-and-ladders metaphor is the canonical version (per stale-audit.md §3.2). E01 changes the framing, not the story body.
- This is the row that establishes the dual-author convention for the entire downstream book. The "blended we, in-prose attribution" choice cascades to every chapter Scout from here forward.

---

### E02 (ATTRIBUTION, LAND-WITH-MODIFICATION) — Jesse's developer-departure story

**Substance to preserve:**
- The entire chutes-and-ladders developer-departure story (L3 in current chapter) is sourced canonical content per `7bfc51b` and stale-audit §3.2. Preserve in full.
- The knowledge-as-asset paragraph (L5) that follows is also sourced and protected. Preserve in full.

**Modification from Julie's instruction:**
- Julie's redline (line 87) adds `Jesse:` as an inline tag before the paragraph. **Reject the tag form.** Per Q-E21 convention, attribution is in-prose ("Jesse was…", "In his own company, Jesse…", or whatever lands in the chapter voice). The Voice Shifter handles this when E01 lands — they're the same edit operation in practice.

**Anti-pattern risk:**
- A4 (contrived/boastful biographical examples) — low risk; the developer-departure beat is concrete and operator-weighted as it stands.

**Framework-attribution rule:** N/A.

**Coherence:**
- E01 and E02 should be executed as a **single Voice Shifter bead**, not two. They're a single coherent edit operation: insert a dual-author opening line, then attribute the existing first paragraph in prose. Splitting them creates orphaned attribution.

---

### E03 (NEW-SECTION, LAND-WITH-MODIFICATION) — Julie's 2022 founding story

**Substance to preserve (from `_julie/julie-redline.md:110–130`):**
- 2022, Julie was Global CHRO at an anonymized "global food safety company"
- Acquisition of a Fortune 500 division
- Overnight expansion to 44 countries
- The structural insight: the work — *"who owned what, how decisions moved, what knowledge lived where"* — was never explicitly designed in either company. It lived in heads, informal relationships, tribal processes.
- The "org chart names the boxes; operating model names how work moves" distinction. **This is the operator-load-bearing claim of the paragraph.**

**Modification from Julie's instruction:**
- Julie's source paragraph (redline:110–130) is HEAVY REWRITE per risk map. The substance survives; the prose does not. Direction: lead with the concrete acquisition beat, cut the abstract-noun triplet ("the accountability structure, the knowledge architecture, and the operating model"), drop the closer ("And it is the same gap that is making AI investments disappear without a trace in most companies today") — that closer is generic AI smell.
- **Framework-attribution scrub:** Julie's source doesn't introduce a named framework here (HAC, TML, etc.) so the rule doesn't bite directly — but the *implicit* "Julie's 20 years in CHRO practice" framing should land as biographical fact, not as IP-claim language. The org-chart-vs-operating-model insight is *joint IP* of the book, not Julie's-individual contribution.
- **E60 anonymization:** "a global food safety company" (already in Julie's source per the convention). No further substitution needed.

**Anti-pattern risk (highest):**
- A3 — triplet pileup: Julie's source has *"the accountability structure, the knowledge architecture, and the operating model"* and *"in people's heads, in informal relationships, in tribal processes"*. Both must collapse to one specific instance each.
- A5 — generic AI smell: the closer *"making AI investments disappear without a trace"* is the canonical mission-statement-AI cadence (charter pattern A5 + pattern 4 from risk map §3).
- A1 — possible abstract-noun-equals-abstract-noun if "operating model" gets defined here in the absence of stakes. The reader hasn't earned that term yet. Leave it as a phrase the reader can absorb naturally; don't formally define it in the preface.

**Framework-attribution rule:** Soft-applies. No framework named, but the framing should not read as "Julie's CHRO practice produced this insight." Frame it as a *shared* diagnosis — the discovery in Julie's career that matches what Jesse found in his.

**Coherence:**
- Lands AFTER L5 (the knowledge-as-asset paragraph) and BEFORE L7 (the "That moment is why this book exists" single line, which E04 reworks). The structural arc: Jesse's story → Jesse's realization → Julie's story → shared conclusion.
- Must not introduce coined vocabulary (*co-intelligence*, *Co-Operating Model*, *HAC*) ahead of the stakes paragraph at L9. A2 is the trap.
- Must preserve continuity with the "container for information" framing at L15 — don't contradict the post-acquisition story arrival with later framing.

**Path B candidacy:** Strong. This is a NEW-SECTION + HEAVY REWRITE row with substance preservation requirements that are non-trivial — Substance Lead extracts intent; Voice Lead identifies the A3/A5 traps; Reader Lead validates the CEO take-away is "this isn't just a tech-bro book." Recommend Path B for this bead.

---

### E04 (VOICE-SHIFT, NEEDS-AUTHOR + LAND-WITH-MODIFICATION) — replace "That moment is why this book exists"

**Substance issue (NEEDS-AUTHOR):**
- Julie's proposed replacement (`_julie/julie-redline.md:132–141`) reframes the single-line pivot as a dual-origin closer: *"Both of those moments — Jesse's developer departure and Julie's acquisition integration — pointed to the same root cause. Organizations are not designed for the work they are actually doing. They are designed around the people who happen to be doing it. When the people change, the design breaks. When AI arrives as a new kind of worker, the design breaks in exactly the same way, for exactly the same reason. That is why this book exists."*
- **Per JF's note at `_julie/julie-final.md:53`** (and risk map §4.1): the framing *"When AI arrives, the design breaks"* is causally wrong. AI doesn't break the design; **the work isn't designed in the first place**, so there's no seat for AI to slot into. This is a substance-level reframe Jesse must approve before any prose work begins.
- This is also the row where the A1 anti-pattern lurks: *"Organizations are not designed for the work they are actually doing. They are designed around the people who happen to be doing it."* — the second sentence is the smoothing-AI antithesis closer (pattern 4 in risk map §3).

**Author decision required (one-question prompt):**
> Does the dual-origin closer for the preface land as *"both stories reveal the same root cause: the work was never explicitly designed, so there's no seat for AI to occupy"* — or do we keep the single line *"That moment is why this book exists"* and let E03's founding story do the bridging work without an explicit closer?

**If Jesse approves the reframe (LAND-WITH-MODIFICATION):**
- Substance preserved: both founding stories point to the same diagnosis — work not designed = no seat for AI
- Modification: strip the "AI breaks the design" framing; replace with "the work was never designed, so AI has nowhere to slot in"
- Cut Julie's two-sentence parallel construction ("When the people change…When AI arrives…") — A3 triplet
- Land as ≤4 sentences. The current single-line *"That moment is why this book exists."* is its own paragraph for hammer-blow effect; the replacement should preserve that hammer-blow rhythm.

**If Jesse rejects the reframe (SKIP):**
- Keep current L7 verbatim. E03 lands on its own merits as a parallel story; the single-line pivot continues to read as Jesse-voiced (which conflicts with E01's dual-author opener — flag separately).

**Anti-pattern risk:**
- A1 — abstract-noun-equals-abstract-noun (the second sentence in Julie's draft)
- A3 — the two-sentence parallel pivot
- A5 — overall AI smell on the closer

**Framework-attribution rule:** N/A.

**Coherence:**
- Whatever lands here is the bridge between the founding stories and the design-before-deploy framing at L9. The bridge must NOT introduce coined vocabulary (no "co-intelligence," no "Co-Operating Model").

---

### E05 (VOICE-SHIFT, LAND) — word-level contractions + I→we

**Substance to preserve:**
- Entire content of L9, L13, L15 unchanged

**Edits:**
- L9: `you've` → `you have` (per Julie's redline)

Wait — that violates the voice charter. **Per voice-charter Section 2:** *"Contractions: always. don't, can't, won't, it's, you're, they're, we've, you've. Absence of contractions is an AI tell."*

**Re-classification of E05:** This row needs a modification. Julie wants `you've` → `you have`. The voice charter explicitly says contractions are mandatory and their absence is an AI tell. **Reject the contraction expansion.** Keep `you've` as-is.

The other half of E05 ("minor I→we throughout opening paragraphs") still applies:
- L9 is already in "you" address (no I/we to convert)
- L13 ("When the design is right, 5:30 arrives…") — no I/we present
- L15 ("Your company is not just a business…We are sitting at the precipice…") — already uses "we"; verify no stranded "I"

**Net effect of E05:** Nearly a no-op on the literal Julie instruction. The real value of this bead is the **opportunistic A1 cleanup at L11**: *"The Sequence is not a concept to absorb. It is a process to execute."* This is the exact sentence Jesse flagged at `julie-final.md:102` as the canonical A1 anti-pattern and it sits in our current preface. The Voice Shifter handling E05 should be authorized to cut this sentence or replace it with one operator-weighted line about what running the Sequence costs/produces (per risk map direction at line 48 of risk map).

**Anti-pattern risk:**
- A1 already present at L11 — fix during this pass
- A8 (conjunctive-adverb pileup) — none in target lines
- A11 (inflated symbolism) — L15 "*We are sitting at the precipice of one of the biggest transformations most of us will live through*" leans toward A11 and the forbidden vocabulary list (*transformations* is on the auto-reject list per voice charter §3). **Flag for opportunistic cleanup if scope allows; otherwise file as a separate bead.**

**Framework-attribution rule:** N/A.

**Coherence:**
- The L11 cleanup must preserve the six-stage list (Signal → Source → Design → Build → Deliver → Compound) verbatim — that's canonical Sequence syntax (charter §2: arrow is `→`, always six in order).
- The L15 "transformation" word is forbidden vocabulary. Replace with plain language ("shift," "change in how work happens") — does NOT require dual-author scope; it's a single-word vocab fix.

**Recommendation:** Treat E05 as a small bead with two parts:
1. Audit L9–L17 for stranded "I" (likely no-op)
2. Cut/replace L11 second sentence (A1 anti-pattern fix)
3. Replace "transformations" at L15 (forbidden vocab)

These are mechanical Path A edits. Voice Shifter executes solo.

---

### E06 (NEW-SECTION, LAND-WITH-MODIFICATION) — equal-weight authorship/bio paragraph

**Substance to preserve (from `_julie/julie-redline.md:174–201`):**
- Jesse: technical + operations, enterprise software → startup builds, "developing AI systems inside real companies before teaching them to anyone else"
- Julie: 20 years as practitioner + executive in org design and human capital; Global CHRO at an anonymized global food safety company; multi-billion-dollar acquisition spanning 44 countries; prior VP / HR leadership at three anonymized employers (large furniture and workplace design company, global automotive supplier, mid-market precision manufacturing company)
- Joint claim: "AI is not a technology problem. It is an organizational design problem."
- Joint claim: companies solve AI by "designing the work before deploying the technology" — this aligns with the book's *Design Before Deploy* canonical phrasing (charter §3).

**Modification from Julie's instruction:**
- Julie's source has classic A3 triplet pileup (`large furniture and workplace design company, a global automotive supplier, and a mid-market precision manufacturing company`). All three are anonymized employer names per E60 convention — they should land, but the rhythm needs work. Lead with the strongest credential (Global CHRO at the food-safety company with 44-country integration), then enumerate the prior roles in a single sentence without parallel cadence.
- Julie's source closes with the AI-tell mission-statement cadence — *"And the companies that solve it will solve it by designing the work before deploying the technology."* Replace with one operator-direct sentence. The "Design Before Deploy" phrase is canonical book vocabulary; using it once here is fine.
- **A2 trap:** Julie's source introduces *"AI is not a technology problem. It is an organizational design problem."* This is the central thesis claim of the book. Its placement here — as the closing line of the preface — works IF stakes have been established by E03 (founding story) and E04 (dual-origin closer). If E04 is rejected and the dual-origin closer doesn't land, then the A2 risk increases because the bio paragraph would be carrying both the credentials AND the central thesis without enough setup.
- **Co-intelligent co-operation introduction:** The current L17 closes with *"Hence: co-intelligent co-operation."* — this is the book's title and the coined vocabulary that the rest of the book operates inside. Per charter §3 (Canonical), *Co-Intelligent Co-Operation* is the relational frame and the book title. **Keep that line.** Julie's bio rewrite shouldn't drop it.

**Anti-pattern risk:**
- A3 — triplet of prior employers (high risk, Julie's source has it explicitly)
- A4 — boastful biographical examples (44 countries / multi-billion-dollar acquisition could read as credentialism; mitigated by E03 already establishing operator stakes around the 44-country acquisition)
- A5 — AI smell on the closer ("the companies that solve it will solve it by…")
- A11 — inflated symbolism if "joint expertise" framing leans abstract

**Framework-attribution rule:** Applies in spirit. The bio shouldn't read as "Julie brings HR; Jesse brings tech" → "together we built X framework." The book's frameworks (HAC, TML, etc.) are joint IP. Phrase Julie's credentials as practitioner experience that *informs* the joint work, not as the origin point of any specific framework.

**Coherence:**
- This is the closing paragraph of the preface. It must carry the dual-author weight set up by E01 + E03.
- The *"co-intelligent co-operation"* title-drop at the end of the current L17 is load-bearing. Preserve as-is or relocate to a similar closing position.
- E60 anonymizations land here: "global food safety company," "large furniture and workplace design company," "global automotive supplier," "mid-market precision manufacturing company."

**Path B candidacy:** Strong. NEW-SECTION + HEAVY REWRITE + substance preservation across multiple beats + tight A2/A3/A11 traps. Recommend Path B for this bead.

---

## Conflicts and risks

### Conflict 1: E04 substance — "AI breaks the design" vs. "work isn't designed"
**Source:** `_julie/julie-final.md:53` (JF inline note) cross-ref `julie-prose-risk-map.md` §4.1
**Description:** Julie's E04 replacement frames AI as breaking the design. Jesse's editorial position is that AI doesn't break the design — the work was never designed in the first place, so AI has no seat to occupy. These are causally distinct claims.
**Escalation:** NEEDS-AUTHOR. Cannot bead-execute until Jesse confirms reframe direction. Frame as a one-question prompt to the Human Orchestrator.

### Conflict 2: E05 internal contradiction with voice charter — contractions
**Source:** `_julie/voice-charter.md` §2 ("Contractions: always") vs. Julie's redline asking `you've → you have`
**Description:** Voice charter explicitly mandates contractions and names their absence as an AI tell. Julie's instruction to expand `you've` to `you have` violates the charter. The charter wins (per AGENT-TEAM §5: voice charter is canon).
**Escalation:** No author decision needed. **Reject the contraction expansion in the Scout plan**; the Voice Shifter will preserve `you've` as-is.

### Conflict 3: Q-E21 attribution convention overrides Julie's inline `Jesse:` / `Julie:` tags
**Source:** `_julie/author-questions-answered.md` Q-E21 (researched + JF-approved)
**Description:** Julie's redline at lines 87 and 107 inserts inline author tags before paragraphs. Q-E21 research found this convention is rare in modern dual-author business books; the dominant convention is blended "we" with in-prose attribution. Q-E21 is JF-approved.
**Escalation:** No author decision needed. **Reject the inline tags globally** for E01–E06 (and downstream). This row is the cascade origin — every subsequent chapter Scout will inherit this convention.

### Conflict 4: A1 anti-pattern already present in current preface at L11
**Source:** `index.qmd:11` (existing prose) cross-ref voice charter §4 A1
**Description:** The line *"The Sequence is not a concept to absorb. It is a process to execute."* is the exact sentence Jesse flagged at `_julie/julie-final.md:102` as the canonical A1 example — and it sits in our current manuscript. The voice charter Section 4 lists this as auto-reject.
**Escalation:** Opportunistic fix during E05 execution. No author decision needed. Voice Shifter has authority to cut/replace per charter §5 (anti-pattern fixes are mandatory).

### Conflict 5: Forbidden vocabulary "*transformations*" at L15
**Source:** `index.qmd:15` (existing prose) cross-ref voice charter §3 (Forbidden)
**Description:** The line *"We are sitting at the precipice of one of the biggest transformations most of us will live through"* contains the forbidden word *transformations*. Charter says auto-reject.
**Escalation:** Opportunistic fix during E05 execution. Voice Shifter has authority to replace per charter §5.

### No git-log polish collisions
- The last preface-touching commit (`7bfc51b`, 2026-05-18) expanded the developer-departure story and resolved earlier JF notes. The chutes-and-ladders prose is the canonical sourced version. **No E-row in this chapter regresses against `7bfc51b`** — E01/E02 wrap the prose with a dual-author frame; E03 inserts new content after L5; E04 reworks L7; E06 rewrites L17. The developer-departure body (L3) and the knowledge-as-asset paragraph (L5) are preserved verbatim under all six edits.

---

## Recommended bead order

Execute in this order. Dependencies in parentheses.

1. **E05** (LAND, Path A — Voice Shifter solo)
   - Audit L9–L17 for stranded I/we (likely no-op)
   - Fix A1 anti-pattern at L11
   - Replace forbidden vocab at L15
   - Reject Julie's contraction expansion
   - *Why first:* Cleans up pre-existing voice debt before substance accretes. Zero dependency on other beads.

2. **E01 + E02** (LAND-WITH-MODIFICATION, Path A — Voice Shifter solo, **single bead**)
   - Insert blended-we opening line before L3
   - Attribute developer-departure paragraph in prose (no inline `Jesse:` tag)
   - *Why second:* Establishes the dual-author convention used by E03, E04, E06.
   - *Dependency:* None.

3. **E03** (LAND-WITH-MODIFICATION, **Path B — Design Table**)
   - New paragraph(s) after L5
   - Substance Lead extracts the org-chart-vs-operating-model insight
   - Voice Lead defends against A3/A5 traps
   - Reader Lead validates the CEO takeaway is "this isn't just a tech book"
   - *Dependency:* E01+E02 must land first so the dual-author voice is established before Julie's parallel story arrives.

4. **E04** (NEEDS-AUTHOR; if approved → LAND-WITH-MODIFICATION, Path A — Voice Shifter solo)
   - Replace single-line L7 with dual-origin bridge **iff JF approves the substance reframe** (work isn't designed, not "AI breaks the design")
   - *Dependency:* JF decision; then must follow E03 in execution so the founding-story content E04 references is already in the chapter.

5. **E06** (LAND-WITH-MODIFICATION, **Path B — Design Table**)
   - Rewrite L17 (final paragraph)
   - Substance Lead structures the credentials without triplet
   - Voice Lead defends against A3/A4/A11 + A2 (co-intelligent co-operation introduction)
   - Reader Lead validates the closer paragraph carries the dual-author weight + preserves "co-intelligent co-operation" title-drop
   - *Dependency:* E03 must land first (founding-story credentialing context); E04 should land first (whatever happens to L7 affects whether L17 carries the central thesis alone).

**Path A beads:** E05, E01+E02, E04 — three solo Voice Shifter passes.
**Path B beads:** E03, E06 — two Design Table convergences.

**Critical sequencing constraint:** E01+E02 cascades the dual-author convention to every downstream chapter. Phase 3 must not bead Chapter 1 attribution work until the Preface E01+E02 bead has landed and the convention is concretely modeled in `index.qmd`. The Chapter 1 Scout dispatch should be paused on that gate.

---

## Skip / needs-author rationale (for rows not landing)

### E04 — NEEDS-AUTHOR (substance reframe required before prose work)

**Decision Jesse must make (one-question prompt):**
> The dual-origin closer for the preface — does it land as *"both stories reveal the same root cause: the work was never explicitly designed, so there's no seat for AI to slot in"* (your editorial correction at `julie-final.md:53`), or do we drop the bridge entirely and keep the current single line *"That moment is why this book exists"* (which contradicts E01's dual-author opener)?

A third option: kill E04 entirely (no bridge) and let E03's founding story bleed directly into L9's design-before-deploy paragraph. This avoids the substance reframe but leaves an attribution mismatch with E01.

**Recommended default:** Approve the reframe per `julie-final.md:53` — the substance is right and the prose can be cut to ≤3 sentences. Voice Shifter handles after Path B beads converge.

---

### E07 — RELOCATED (out of scope here)

Per Q3 resolution in the manifest: the 15-year content thread (JMann Radio + Work Matters + Compound) is RELOCATED from the Preface to About-the-Authors / Julie's bio. Tracked under `book-ff63.17`. The Preface Scout does not verdict E07. **The risk-map verdict (REJECT for both style and substance-pending) stands** — Scout for the About-the-Authors section will handle the substance-preservation decision when that bead becomes active.

---

## Done test status

- [x] Every in-scope E-row classified (E01–E06): 4 LAND-WITH-MODIFICATION, 1 LAND, 1 NEEDS-AUTHOR (E04)
- [x] Every LAND / LAND-WITH-MODIFICATION row has tightened current-chapter line ranges (L3, L5, L7, L9, L11, L15, L17)
- [x] Every LAND row has 2–4 bullet acceptance criteria covering substance, anti-patterns, attribution rule applicability, coherence
- [x] Conflicts flagged with specific source references (`julie-final.md:53`, `julie-redline.md:87`+`:107`, `voice-charter.md §2`+`§4`)
- [x] Bead execution order recommended with dependencies cited
- [x] E07 RELOCATED status acknowledged (out of scope per Q3)
- [x] Plan file at `_julie/per-chapter/00-preface.md`

**Outstanding author asks for Human Orchestrator:**

1. **E04 substance reframe** — approve the "work isn't designed" framing per `julie-final.md:53`, OR kill E04 entirely.

That is the only blocking decision for this chapter. E01, E02, E03, E05, E06 can all dispatch under their current verdicts.

---

*End of plan.*
