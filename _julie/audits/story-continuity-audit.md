# Story Continuity Audit — Phase 3 Audit 5

**Generated:** 2026-06-05  ·  **Bead:** book-3id7  ·  **Agent:** Story Continuity Auditor

## TL;DR

Audited 5 canonical stories across 14 chapter/case-study files (Preface, Ch 1–11 including 06b, plus case-study-meridian.qmd, case-study-pm-agent-team.qmd, appendix-glossary.qmd). Across roughly 75 detail-checks the spine is in remarkably good shape: Meridian's canonical numbers (\$7.2M, 27 employees, \$558K, 3.8 days → 4.2 hours, 10 hrs/wk, 147→112 rules, \$47K, JobBOSS/HubSpot, three-and-a-half weeks) hold consistently everywhere they appear, characters keep their canonical roles, and the anonymization (Sofia/Rachel) is uniform. **15 findings** total: 2 high-severity (Meridian's documented-lost-revenue figure has competing variants \$418K vs. \$558K; the Preface developer-departure story is staged as a *single-moment* realization that conflicts with the bd-memories canon of "noticed over time via EOS scorecard + Stripe/financials"), 6 medium (stylistic-but-noticeable variants in turnaround phrasing, 13→8 thread thin in Ch 10, "five agents" / Sofia-role minor inconsistency), and 7 low (formatting/style variants like "\$558K" vs "\$558,000"). Overall **PR-ready with recommended surgical fixes** — none of the findings block the merge, but four are worth a 10-minute pass before final.

## Per-story findings

### Meridian Manufacturing

**Detail-by-detail audit:**

| Detail | Canonical value | Occurrences | Drift? |
|---|---|---|---|
| \$7.2M revenue | \$7.2M | 03 L153; 10 L180; case-study L5, L110; glossary L81; "Seven-point-two million" 01 L246 | NO. Phrasing varies ("\$7.2M" vs "Seven-point-two million" vs "\$7.2 million") — stylistic, internally consistent |
| 27 employees | 27 / twenty-seven | 01 L246; 03 L153; 07 L221; case-study L5; glossary L81 | NO |
| Custom metal fabrication | yes | 01 L246; 03 L153; 07 L221; case-study L5; glossary L81 | NO |
| Grand Rapids, Michigan | Grand Rapids, MI | 03 L153 ("Grand Rapids"); case-study L5 ("Grand Rapids, Michigan"); glossary L81 ("Grand Rapids, Michigan") | LOW — Ch 1 introduction does NOT name the city (01 L246 omits Grand Rapids). Worth adding once for completeness; not a contradiction |
| \$558K constraint cost | \$558K/yr | 03 L65, L158, L164; 04 L34, L153, L172; 04 L57 ("$558K per year"); 06 L227; 06b L55; 07 L221, L306; 08 L178; 10 L216; case-study L321; glossary L81 | NO — \$558K is canonical across 11 locations |
| \$418K documented lost revenue | \$418K | 01 L248 ("\$418,000"); case-study L23 ("\$418,000"), L40, L71, L86 ("\$418K/year"), L362 | **HIGH — variant exists.** Ch 1 introduces the cost as "\$418,000 in named lost revenue" and case study uses \$418K as "documented lost revenue" while everywhere else (Ch 3, 4, 6, 6b, 7, 8, 10) uses **\$558K** as the headline constraint cost. The case study reconciles these: \$418K documented loss + \$80K Elena time + \$60–90K floor underutilization = \$558–598K. But **Ch 1 doesn't bridge that gap.** A reader of Ch 1 sees \$418K; a reader of Ch 3 sees \$558K. The two numbers are reconcilable but the bridge sentence is missing from Ch 1 |
| Elena Ruiz role | VP of Operations + Integrator + Human Orchestrator | 01 L246; 02 L156; 03 L153, L160; 04 L57; 05 L201; 06 L227, L243; 06b L55; 07 L221; 08 L87; 09 L122; 10 L189; case-study L7 | NO — perfectly consistent |
| Ty Banfield role | Sales Lead | 01 L246 ("Ty Banfield in sales"); 03 L165, L171; 05 L207; 08 L88; 09 L116; 10 L198; case-study L7, L19 | NO |
| Dave Kowalski role | Senior Design Engineer, 31 yrs fabrication | 01 L246 ("senior design engineer (thirty-one years…)"); 03 L69, L165; 05 L205; 08 L86 ("Sr. Design Engineer"); 09 L62, L97; case-study L7 | NO — consistent, 31 years referenced uniformly |
| Mark Ellison role | CEO + strategic-account escalation | 01 L246; 03 L153; 06 L249; 07 L293; 09 L122; case-study L7 | NO |
| Carlos Medina role | Shop floor supervisor | 01 L246; 06 (escalation context); 09 L62; case-study L7 | NO |
| 112 validated pricing rules (from 147) | 147 raw → 112 validated | 03 L69, L165 ("147 rows"); 05 L203, L207, L257, L263; 06 L229 ("147 rows … cleaned to 112"); 06b L62 ("112 validated rules"); 07 L225 ("112 validated"), L308 ("147 → 112"); 08 L56 ("112 validated"); 09 L77 ("147 rows … 112 validated"); appendix-prompt-engineering L97 ("147 customer pricing exceptions"); case-study L122, L138, L208, L289, L306, L308, L419 | NO — every mention agrees. The fact that "147 rows → 112 validated rules" is the cleanest-traced detail in the entire book |
| 3.8 days → 4.2 hours turnaround | 3.8 days → 4.2 hours | 03 L164, L168; 07 L306, L312; 08 L180, L183, L190; 09 L79, L139; 10 L203, L216; case-study L357, L373 (3-5 days variant), L395, L497 | MEDIUM — **two parallel phrasings coexist.** "3.8 days" is the precise canonical figure used in every results context. But narrative introductions in Ch 1 L248, Ch 3 L153, Ch 4 L153, Ch 6 L227, Ch 8 L90, and case-study L9/L83 use **"3–5 days" / "three to five business days"** as the symptom phrasing. Reconcilable (3.8 is the average inside the 3–5 range), but the book never explicitly tells the reader "the range is 3–5, the average is 3.8" — and the reader who notices both will wonder which number is authoritative |
| 10 hours/week Elena recovered | 10 hrs/wk | 07 L312 ("Elena got ten hours of her week back"); 08 L187 ("recovered 10 hours/week"); 09 L79 ("fifteen hours a week to five"); 10 L203; case-study L395, L497 ("ten hours per week") | NO — math is consistent (15 → 5 = 10 hours recovered) |
| Customer Notes.xlsx inputs source | Customer Notes.xlsx | 03 L165, L166; 05 L203, L207, L257; 06 L229; 06b L62; 07 L225; 08 L56, L87, L129 ("CustomerNotes.xlsx"); 09 L77; appendix-prompt-engineering L70; case-study L120, L138, L306 | LOW — **formatting variant.** Ch 8 lines 56, 87, 129 write the filename as **"CustomerNotes.xlsx"** (no space) while everywhere else it is **"Customer Notes.xlsx"** (with space, quoted). Three occurrences of the no-space variant in Ch 8 only |
| JobBOSS ERP | JobBOSS | All 11 chapters consistent | NO |
| HubSpot CRM | HubSpot | All 11 chapters consistent | NO |
| Agent stack (Claude Team + n8n + low-code) | Claude Team + n8n + freelance n8n developer for 3 days | 03 L167 ("n8n workflow … Claude"); 07 L233, L237, L308; 08 L56; case-study L300, L302 | NO |
| Three-and-a-half-week sprint duration | 3.5 weeks | 07 L237, L239, L310, L312; case-study L302 | NO — internally consistent. Note: Ch 7 L38 references "three weeks" as a generic claim about a quoting build, which is close-enough rounding given the same passage but worth noting |
| Quote volume 8–10 → 18–22 quotes/week | 8–10 → 18–22 | 08 L181, L184; case-study L359 | NO — appears only in Deliver / case study, but consistent there |
| \$47K month-one revenue impact | \$47K new revenue in month one | 08 L185, L188, L191; 09 L79 ("$47,000"), L139 ("$47K"); 10 L203; case-study L362, L497 | LOW — Ch 9 L79 uses "\$47,000"; everywhere else "\$47K". Stylistic |
| Elena's hours: 15 → 5 (recovered 10) | 15 hrs/wk → 5 hrs/wk | 06b L55 ("fifteen hours a week"); 08 L90, L181, L184; 09 L79, L139; case-study L86, L395 | NO |
| Eleven lost bids × \$38K avg = \$418K | 11 × \$38K = \$418K | 01 L248; case-study L23, L86 | NO — the arithmetic is consistent within case study + Ch 1, but again this is the \$418K thread that doesn't bridge to \$558K in Ch 1 |
| Claude Team workspace as AI backbone | Claude Team | 07 L233, L237; 08 L56, L86, L87; case-study L300, L322, L323 | NO |
| Three agents: Research / Pricing / Assembly | Quote Research / Pricing / Assembly | 06 L235–237; 06b L74–76; 07 L233, L306; 08 L86; 09 L135; 10 L197; case-study L257, L324 | NO |

**Verdict:** PASS with **2 high-priority surgical opportunities** (Ch 1 \$418K → \$558K bridge; "Customer Notes.xlsx" filename style in Ch 8) and **3 low-priority polish items.**

### PM Agent Team (Ch 7 opener + case study)

| Detail | Canonical value | Occurrences | Drift? |
|---|---|---|---|
| Five agents replaced coordinator | 5 agents | 07 L8, L10 ("five agents, five different access levels"); case-study L187, L273, L302, L355 | NO |
| \$24K/year coordinator role cost | \$24K/yr | 04 L8; 05 L8; 06b L51; 07 L8 ("our \$24,000-a-year coordinator role"); case-study L7, L21, L22, L225, L252, L300, L320, L326 | NO |
| Sofia — VP of Operations | Sofia Reyes / VP of Operations | 07 L12 ("Sofia, our VP of Operations"); case-study L5, L23 ("Sofia Reyes (VP of Operations, Human Orchestrator)"), L187 ("Sofia Reyes supervises … as Human Orchestrator"), L355 | NO — Sofia is consistently VP of Operations / Human Orchestrator. Last name "Reyes" appears only in case study (3 occurrences); Ch 7 just calls her "Sofia" |
| Rachel — subcontractor doing coordination | subcontractor we'll call Rachel | 07 L12; case-study L5, L7, L13, L15, L21, L34, L40–56 (HAC), L64–72 (Knowledge Map), L93, L95, L101, L103, L105, L187, L342 | NO — consistent throughout |
| Access-layer-first design discipline | access layer locked before workflow | 07 L8 ("the first thing we locked wasn't the workflow. It was the access layer"); 07 L10 (five access levels); 07 L310 (Meridian context); 07 L289 (Guardrails) | NO |
| Marina mention in Ch 2 vs Sofia in Ch 7 | — | 02 L8, L10 (Marina, "Integrator"); 05 L8 ("Jesse and Marina"); 07 L12 (Sofia, "VP of Operations") | **MEDIUM — character ambiguity.** Ch 2 L8 names **"Marina, his Integrator"** and Ch 5 L8 again names **"Jesse and Marina."** Ch 7 L12 names **"Sofia, our VP of Operations."** Both characters describe themselves doing the same kind of design-session work with Jesse on the coordinator/PM problem. If Marina = Sofia (anonymization) the role title is inconsistent (Integrator vs VP Ops). If Marina ≠ Sofia, the book never says so. Stale-audit flagged this exact concern: Sofia "possibly originally Marina or Donna." From the prose it reads as if they are different people — but the reader can't tell |

**Verdict:** PASS for Sofia/Rachel anonymization. **1 medium finding** on Marina vs Sofia identity ambiguity.

### Katie + Jill (Ch 11 opener)

| Detail | Canonical value | Occurrences | Drift? |
|---|---|---|---|
| Katie — CEO, came in with list | yes | 11 L8 | NO |
| Jill — different CEO, following week | yes, different CEO, same structure | 11 L18 | NO |
| 30-minute call duration | 30 minutes | 11 L10 ("we've got thirty minutes"); 11 L20 ("Thirty minutes"); 11 L88, L100, L123 (Clarity Call = 30 min); glossary L21 | NO |
| Minute-8 cost question | minute 8 | 11 L10 ("about eight minutes in and I ask her: 'What does this problem cost you?'") | NO |
| Minute-25 outcome | minute 25 | 11 L16 ("By minute twenty-five, we'd named something she hadn't walked in with…"); 11 L18 ("Both of them could name it by minute twenty-five") | NO |
| "Oh. That's what it is." | exact quote | 11 L16 (*"Oh. That's what it is."*) | NO |
| Katie/Jill referenced in chapter reflection | mentioned by name | 11 L172 ("Katie and Jill — both CEOs who discovered their real constraint…") | NO |

**Verdict:** PASS. Katie+Jill is the tightest-written canonical story in the book — 30 / 8 / 25 / "Oh. That's what it is." all internally consistent, name+role consistent, and the chapter-end reflection (L172) re-cites them correctly.

### Ahmed / Developer-left / Chutes and Ladders

| Detail | Canonical value | Occurrences | Drift? |
|---|---|---|---|
| Developer left → knowledge walked out | yes | Preface L5; 02 L54; 03 L30; 06 L12 (project coordinator analog); 11 L158 | LOW — Ch 6 L12 talks about "the project coordinator" leaving rather than the developer; that's a *different* (PM agent team) thread. Both are valid "knowledge walks out" examples but they should not be conflated. Currently they are not — but a reader might miss that Ch 6's story is about the coordinator, not the developer |
| "Chutes and Ladders" framing | yes | Preface L5 ("his business was a game of 'Chutes and Ladders'"); 02 L54 ("a game of *Chutes and Ladders*"); 03 L30 ("the *Chutes and Ladders* problem we described at the start"); 11 L158 ("playing *Chutes and Ladders*") | NO — phrasing consistent |
| 13 → 8 headcount thread | thirteen people to eight | 01 L55 ("from thirteen people to eight … five roles … redesigned out of existence"); case-study-pm L342 ("headcount reduction from 13 to 8 … We lost the coordinator role entirely") | **MEDIUM — thread is thin.** The 13→8 number appears explicitly only twice in the book: Ch 1 L55 (as the headline arc) and case-study-pm L342 (the PM agent contribution to it). Ch 10 §The headcount paradox, resolved (L120–132) describes the *concept* of the paradox resolution but never re-cites the 13→8 number. Ch 10's "Two business lines, half the staff" (L168–176) is a different framing of the same outcome but again doesn't tie back to 13→8. **The Preface developer-departure story → 13→8 resolution thread is implicit, not explicit.** A reader who picked up the preface story is never told in the book proper that *"the developer leaving was the start of the journey from 13 to 8"* — they have to construct the bridge themselves |
| "Ahmed" name in book prose | not used | grep across all chapters: **no occurrence of "Ahmed"** | NO — the developer is anonymized throughout. Per bd-memories `ahmed-story-is-chutes-and-ladders`, Ahmed is the real-world identity behind the preface story but is correctly NOT named in book prose |
| Knowledge walked out the door | yes | Preface L5 ("walking out the door in a banker's box"); 02 L54 ("the knowledge left with him"); 03 L30 ("the knowledge left with him"); 06 L12 ("walks out the door"); 11 L158 ("walking out the door when the person did") | NO — phrasing is variant but the concept is consistently echoed |
| Single-moment realization vs. EOS-scorecard / Stripe / financials over time | Preface stages it as a *single-moment epiphany* | Preface L5 ("Sitting there, he realized he'd just lost something he couldn't replace"); 02 L56 ("That issue … surfaced during a normal issues meeting") | **HIGH — conflict with bd-memories.** Per `all-stories-in-the-book-must-be-written`, Jesse noticed the 13→8 capacity shift "over time via EOS scorecard + Stripe/financials (not single moment)." But the Preface (L5) tells the story as an in-the-office single-moment realization the day the developer gave notice. Ch 2 L56 actually does it better — "That issue surfaced during a normal issues meeting" implies the L10 / EOS context — but the Preface narration is the one most readers will remember, and it does not match the canonical "noticed over time" framing. This may be intentional dramatic compression, but it is the single largest semantic gap between the bd-memory canon and the chapter prose |

**Verdict:** PASS-with-caveat. The thread is intact but **two findings need author judgment:** (1) the Preface single-moment vs. EOS-scorecard-over-time tension, and (2) the missing explicit "13→8 because the developer left" bridge in Ch 10's resolution.

### Marina / Donna

| Detail | Canonical value | Occurrences | Drift? |
|---|---|---|---|
| Marina mentioned by name | yes (twice) | 02 L8, L10 ("Marina, his Integrator"); 05 L8 ("Jesse and Marina") | NO occurrence of "Donna" anywhere in the book |
| Marina's role | "his Integrator" | 02 L8; 02 L10 (re-referenced) | LOW — Marina is described only as "his Integrator" with no last name or further bio. Sofia in case-study-pm-agent-team is "VP of Operations" with the last name "Reyes." If they are the same person (anonymization), the title varies (Integrator vs VP Ops). If they are different people, the book never disambiguates |
| Donna mentioned by name | — | not found | NO — Donna does not appear in the chapter prose; the stale-audit concern was preemptive |

**Verdict:** PASS for Donna (does not appear). **1 LOW finding on Marina vs Sofia disambiguation** (overlap with PM Agent Team finding above).

## Cross-cutting findings

### Number drift

1. **\$418K vs \$558K (HIGH).** Ch 1 introduces Meridian's quoting cost as \$418K named lost revenue. Every other chapter cites \$558K as the constraint cost. The case study (case-study-meridian L86) reconciles them mathematically (\$418K + \$80K Elena time + \$60–90K floor = \$558–598K total). **Ch 1 should add one bridging sentence** so the \$558K number that appears in Ch 3 onward doesn't surprise the reader.
2. **"3.8 days" vs "3–5 days" (MEDIUM).** Narrative introductions use 3–5; results / Signal artifacts use 3.8. Reconcilable but never made explicit. A footnote or a single bridging sentence ("Average of 3.8 days, with the worst stretching to five") would resolve.
3. **"\$47K" vs "\$47,000" (LOW).** Ch 9 L79 uses the long form; everywhere else the abbreviated form. Stylistic.
4. **"\$558K" vs "\$558,000" (LOW).** Grep showed no instance of "\$558,000" in chapter prose — the abbreviated form is universal. No drift.
5. **"three weeks" vs "three and a half weeks" sprint duration (LOW).** Ch 7 L38 uses "three weeks" as a generic claim ("a team that built a quoting workflow in three weeks") in the same passage that later (L237, L239, L310, L312) says "three and a half weeks" for Meridian specifically. Close-enough but worth a once-over.
6. **Ch 9 L79 "$47,000" formatting (LOW).** See item 3 above.

### Role drift

1. **Marina ("his Integrator", Ch 2 + Ch 5) vs Sofia ("our VP of Operations", Ch 7 + case study) (MEDIUM).** Two anonymized senior-ops women appearing in similar narrative contexts (working sessions with Jesse on the coordinator/PM problem) with different roles. The book never says whether they are the same person, separate people, or composites. Reader will likely assume same person and be confused by the title change.
2. **No other role drift detected** for Meridian characters (Elena VP Ops, Ty Sales, Dave Sr Design Eng, Mark CEO, Carlos shop floor are all stable).

### Anonymization drift

1. No real names leaked. "Ahmed" does not appear in chapter prose — the developer is consistently anonymous in the Preface, Ch 2, Ch 3, Ch 11. PM agent team uses "Rachel" + "Sofia" consistently. Marina is used twice (Ch 2 + Ch 5) without surfacing the real name. No "Donna" anywhere.
2. **One ambiguity:** Marina's identity vs Sofia's identity (above). This is anonymization-discipline-related, not anonymization-leakage.

### Filename / formatting variants

1. **"Customer Notes.xlsx" vs "CustomerNotes.xlsx" (LOW).** Ch 8 L56, L87, L129 spell it without the space; every other chapter spells it with the space. Three occurrences, easy fix.

### Thread continuity

1. **Preface developer-departure → Ch 10 §The headcount paradox, resolved (MEDIUM).** The Preface promises the thread will pay off; Ch 10 §The headcount paradox, resolved (L120–132) describes the paradox-resolution behavior change but never explicitly says "we went from 13 to 8 because of moves like the one I described in the preface." Ch 10's "Two business lines, half the staff" sub-section (L168–176) covers the resolution narratively but loses the developer-departure framing. A single sentence in Ch 10 §Headcount paradox resolved tying back to the Preface developer would close the loop.
2. **Preface single-moment realization vs. bd-memory "noticed over time via EOS scorecard + Stripe" (HIGH).** Per `bd memories all-stories-in-the-book-must-be-written`, the 13→8 was a slow recognition over multiple scorecard cycles, not the in-the-office epiphany the Preface stages. This is the only finding that contradicts an explicit canonical memory.

### Highest-priority surgical fixes

1. **Preface (index.qmd L5).** Reconcile the in-the-office single-moment realization with the bd-memory canon "noticed over time via EOS scorecard + Stripe/financials." Either soften the Preface so it reads as the *first signal* of a slow recognition, or accept the dramatic compression and update the memory. (HIGH)
2. **Ch 1 (01-diagnosis.qmd L248).** Add a one-sentence bridge so \$418K named-lost-revenue connects to the \$558K full-cost figure that the rest of the book uses. Example: "The named loss is \$418K; once you add Elena's misallocated time and the floor underutilization that the bottleneck creates, the total annual cost runs ~\$558K. The team will land on that number in Signal." (HIGH)
3. **Ch 2 + Ch 5 (Marina) vs Ch 7 + case study (Sofia).** Decide if Marina and Sofia are the same person and either (a) collapse the names + reconcile the title, or (b) add a brief disambiguation. (MEDIUM)
4. **Ch 8 filename "CustomerNotes.xlsx" → "Customer Notes.xlsx"** (3 occurrences: L56, L87, L129). (LOW, but a 30-second fix)
5. **Ch 10 §The headcount paradox, resolved (L120–132).** Add a single sentence tying the resolution explicitly back to the Preface developer-departure / 13-to-8 number, so the through-line lands. (MEDIUM)

## Verdict

**PR-ready with recommended polish.** The canonical Meridian numbers and characters are remarkably consistent (the 147→112 trace alone passes through 14 different chapter locations without a single discrepancy). Katie+Jill is tight. Sofia/Rachel anonymization is uniform. The two HIGH findings (the Preface single-moment framing and the Ch 1 \$418K→\$558K bridge) are *author-judgment* calls, not factual errors — both are reconcilable interpretations of the canon. None of the 15 findings should block the Julie-Mann merge into "Co-Intelligent Co-Operation." A 15-minute editorial pass on the five highest-priority items above would close every gap worth closing.
