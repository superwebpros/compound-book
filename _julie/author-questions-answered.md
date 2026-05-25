# Author Questions — Research Answers

Five research-tractable questions raised against the Julie Mann redline. Each section: restated question, finding, recommendation (APPROVE / APPROVE-WITH-MODIFICATIONS / REJECT / NEEDS-JULIE-INPUT).

---

## Q-E21 — "Lead with name" attribution paradigm

**Question:** Is it a best practice for co-authored business books to mark which author's voice is speaking? What convention should *Co-Intelligent Co-Operation* use?

**Finding (5 examples surveyed):**

1. **Collins & Porras, *Built to Last*** — single blended "we" voice throughout the prose. Authors only alternate in the audio recording, not the text. No inline "Jim:" / "Jerry:" tags.
2. **Collins & Lazier, *BE 2.0***  — blended "we" with occasional first-person asides attributed in-line ("Bill used to say…"; "I remember when…") rather than as section openers.
3. **Schmidt, Rosenberg & Eagle, *Trillion Dollar Coach*** — three-author "we" voice; the opening prologue uses "we" for the trio. No per-section attribution.
4. **Patrick Lencioni's fables** — single narrative voice (third-person fiction frame), even when conceptually co-developed.
5. **Haslam, Driver & Haslam, *Co-Piloting*** — alternating chapters explicitly labeled by author, not inline tags within chapters.

The dominant convention in modern co-authored business books is **blended "we" voice with occasional in-line first-person attribution** ("Julie ran this engagement…" / "Jesse hit this in his own company…"). The "Jim:" / "Julie:" inline label is rare in trade business books and reads more like a transcript or interview format than authoritative prose. The book that does use full author labels (*Co-Piloting*) alternates whole chapters, not paragraphs.

**Recommendation: APPROVE-WITH-MODIFICATIONS.** Do NOT use inline `Jesse:` / `Julie:` tags as section openers. Instead, use the *BE 2.0* / *Trillion Dollar Coach* hybrid:

- Default to "we" / "us" / "our" for framework arguments.
- For story-grounded passages, name the actor in prose: "Jesse was on a discovery call when…" or "In one of Julie's CHRO engagements…"
- This preserves Julie's stated intent (reader knows whose story it is) without adopting a transcript-style convention foreign to the genre.

Sources: [BE 2.0 — Amazon](https://www.amazon.com/BE-2-0-Beyond-Entrepreneurship-Business/dp/0399564233); [Trillion Dollar Coach — Audible](https://www.audible.com/pd/Trillion-Dollar-Coach-Audiobook/0062839276); [Co-Piloting — S&S](https://www.simonandschuster.com/books/Co-Piloting/Jim-Haslam/9781948677585); [Built to Last — Wikipedia](https://en.wikipedia.org/wiki/Built_to_Last:_Successful_Habits_of_Visionary_Companies); [PublishDrive guide on co-authoring](https://publishdrive.com/how-to-co-author-a-book.html).

---

## Q-E23 — "Order is the Argument"

**Question:** What is "Order is the Argument"? Did Julie coin it or import it?

**Finding:** "The order is the *argument*" is an **existing section** in our book — `chapters/03-the-framework.qmd:18`. It is a Jesse-coined turn of phrase already established and the second H2 of Chapter 3. The argument it makes (verbatim from current prose):

> "Most AI initiatives skip the diagnosis and start at Build. A tool gets chosen, a budget gets spent, a workflow gets launched — and around month nine the CEO is sitting in a meeting trying to explain why the AI line item produced no operational result. The cause is not the tool. The cause is the order." (line 20)

> "Building before diagnosing is the same mistake as framing a house before pouring the foundation… Construction has rules about the order of operations because the order is load-bearing. So does this." (line 22)

The section argues that the Signal → Source → Design → Build → Deliver → Compound *sequence* is itself the load-bearing claim of the framework — i.e., the order in which you do the six stages **is** the entire reason the work compounds, not a stylistic preference. The phrase "the argument" is being used in the rhetorical sense ("the thesis of the book"), not as a debate.

Julie's redline (line 660) preserves the heading verbatim and inserts a supporting paragraph framing this as a 30-year-old organizational design principle ("diagnose before prescribe"). She is *building on* the existing section, not introducing the phrase.

**Recommendation: APPROVE.** Julie's redline correctly anchors to the existing section. Jesse's confusion was about the *phrase* — but it is his own, and the existing prose at `chapters/03-the-framework.qmd:18-28` explains it adequately. No change to the heading needed. Julie's added paragraph (lines 668-677 of redline) is a strong reinforcement.

Source: `/Users/jesseflores/compound/sites/compound-book/chapters/03-the-framework.qmd:18-28`.

---

## Q-E26 — Constraint Statement non-manufacturing example

**Question:** Does §4.1 need at least one non-manufacturing example for the Constraint Statement, or is the abstraction enough?

**Finding:**

(a) **Current example count:** Chapter 4 contains **two** worked constraint-statement examples: Meridian Manufacturing (custom metal fab, $558K quoting bottleneck — `04-signal.qmd:51`) and a PT clinic operator (healthcare/services, $420K unfilled-slot constraint — `04-signal.qmd:92-115`, including the full one-page constraint statement table at lines 108-114).

(b) **Industries spanned:** Manufacturing (Meridian) and healthcare/multi-location services (PT clinic). The Chapter 3 opening discovery-call story also implies a services/agency context. The book is NOT manufacturing-only.

(c) **Readability of abstraction:** The template itself (`04-signal.qmd:24` excalidraw + table fields at 108-114: Constraint / Where it lives / Duration / Quantified cost / Validating evidence) is industry-neutral. The five Issue Surfacer questions at lines 126-130 are also industry-agnostic.

Julie's editorial note (redline:762-768) states the template "should include at least one from Julie's professional services or organizational design experience, not only manufacturing and software examples." That premise is **factually incorrect** — the PT clinic example is already a non-manufacturing services example with a fully worked constraint statement.

**Position:** $5M-$50M CEOs do not need additional worked examples. Two examples in different industries (manufacturing + multi-location healthcare services) plus an industry-neutral template is sufficient. Adding a third example risks making §4.1 feel like a tour rather than a method. The PT clinic example explicitly satisfies the "non-manufacturing services" criterion Julie names.

**Recommendation: APPROVE-WITH-MODIFICATIONS.** Reject the "needs another example" framing — the PT clinic case study already serves that role. However, the underlying concern (the template might *feel* manufacturing-coded) could be addressed by one Julie sentence somewhere in §4.1 noting that constraints can be human-capital / org-design constraints (e.g., role design, accountability gaps, knowledge silos), not just process bottlenecks. That's a 1-2 sentence patch, not a new example. Flag to Julie that her note appears to have missed the existing PT clinic example.

Source: `/Users/jesseflores/compound/sites/compound-book/chapters/04-signal.qmd:92-115`.

---

## Q-E39 — Build Spec accountability column

**Question:** Does the current Build Spec already include an accountability/supervisor column?

**Finding:** The current Build Spec in §7.1 (`chapters/07-build.qmd:208-218`) is structured as **eight numbered sections, not a table with columns**. Accountability is already represented as **Section 5: Human Supervisor Role**:

> "5. **Human supervisor role.** Who reviews the output. What they are reviewing for. What the handoff looks like — where the output lands, in what form, on what timeline." (line 214)

The worked Meridian example fully populates this section: "Elena Ruiz, VP of Operations, reviews every draft quote… Expected review: fifteen to twenty minutes per quote… Escalation: low-confidence quotes get her full manual review; non-standard materials route to the senior engineer; strategic account pricing goes to the CEO." (line 231)

Accountability also appears in two reinforcing places:

- The "Agile concepts" section (line 193): "**Accountability.** Every work item has an owner… This maps directly to the Hybrid Accountability Chart — the human supervisor named there is the person accountable for Build's output."
- The Guardrails Checklist (line 282-294) includes **Accountability** as one of its seven questions, with the worked example naming Elena Ruiz as accountable for every quote.

So Jesse's instinct ("I thought we had that already?") is **correct**. What Julie is proposing in redline:1825-1843 is reframing the existing supervisor-role section as a strict per-row accountability requirement and adding a Build-review step that verifies HAC consistency. The supervisor concept is already pervasive; the *verification gate* is partially new.

**Recommendation: APPROVE-WITH-MODIFICATIONS.** Do NOT add an accountability column (the spec is sections, not a table — the structure doesn't fit). The supervisor-role section and the HAC linkage already exist. The genuinely new contribution in Julie's paragraph is the **HAC-consistency verification step** during Build review: "for every step in the specification, that a named supervisor exists in the HAC who is accountable for that step's output." Fold that one sentence into §7.1 as a discipline-level note, or into the Guardrails Checklist as a check before the seven questions. Reject Julie's full insertion as written; tell Julie the structure conflict and the existing coverage.

Source: `/Users/jesseflores/compound/sites/compound-book/chapters/07-build.qmd:208-218, 231, 282-294`.

---

## Q-E43 — Adoption-rate measurement

**Question:** How is AI tool adoption rate measured in practice? Does Julie's framing reflect accepted practice?

**Finding (synthesis):** The change-management / org-design field has converged on a multi-layer adoption metric stack because **single-number adoption is unreliable**. Practitioners distinguish:

- **License activation** (seats provisioned) — vanity metric. Worklytics cites real cases where 1,000 paid seats yielded only 287 monthly active users — true cost per active user 3.5x the budgeted figure.
- **Active usage rate** (% of licensed users who actually use the tool in a defined window — typically MAU/licensed-user, or WAU for high-frequency tools). 2025 benchmarks land at 60-80% target for healthy 12-month adoption.
- **Workflow-specific adoption** (% of affected roles using the *designed workflow*, not just the tool generically) — this is the metric Julie names. It is the operationally useful one for the Compound framework because it ties to the sprint's specific change, not to the tool company's dashboard.
- **Depth/quality** (prompts per user, time-to-proficiency 7-14 days, productivity delta 15-30%) — used to distinguish habitual use from tourism.

Common pitfalls: equating logins with adoption; trusting vendor dashboards (Copilot, ChatGPT Enterprise) that report engagement but not workflow change; failing to define the denominator (all employees vs. role-affected employees); ignoring "shadow workflow" where the new system runs but the old habit also continues. The Larridin and Worklytics analyses are explicit that **workflow-tied adoption — not platform-tied — is what predicts business value**.

**Assessment of Julie's framing (redline:1935-1950):** Strong. Her formulation is operationally cleaner than most published frameworks because she anchors the denominator to "affected roles" (not all employees) and frames the numerator as "using the new workflow as designed, not the old workflow out of habit." She also makes the two-number reporting (operational delta + adoption %) a hard rule, which is consistent with the Worklytics/Larridin "license vs. usage" critique. Her diagnostic interpretation — high adoption + modest result = Design problem; low adoption + good result = Pattern Drag — is genuinely useful and not standard in the literature.

The measurability concern (Jesse's note) is real but tractable for $5M-$50M companies: the denominator is the named role list from the HAC; the numerator is observable in the operational log Ch 8 already prescribes (`08-deliver.qmd:102` "What gets *logged*"). For a 27-person Meridian-scale company, adoption is countable by name. The framework doesn't need Copilot Analytics — it needs the operational log to record who is using the new workflow and who is still routing around it.

**Recommendation: APPROVE-WITH-MODIFICATIONS.** Julie's substantive content is sound and adds real measurement discipline. Two modifications:

1. Add a sentence specifying how adoption is **measured at HAC-roster scale** — i.e., per named role from the Hybrid Accountability Chart, observable in the operational log. Without this, readers will hear "adoption rate" and think enterprise analytics platforms.
2. Define the **window** — "as of week N after launch," not in perpetuity — so the metric is a sprint-level number, not a dashboard.

These two clarifications convert Julie's paragraph from a principle into a measurable instrument. Otherwise APPROVE the insertion.

Sources: [Worklytics — Measuring AI Adoption](https://www.worklytics.co/resources/measuring-ai-adoption-facilitation-index-manager-kpi-copilot-era); [Larridin — Logins vs. Impact](https://larridin.com/blog/ai-adoption-vs-impact-metric); [Worklytics — 10 AI Adoption KPIs 2025](https://www.worklytics.co/resources/top-10-kpis-ai-adoption-dashboard-2025-dax-formulas); [Microsoft — Measuring AI Adoption whitepaper](https://adoption.microsoft.com/files/copilot/Unlocking-AIs-Impact-whitepaper.pdf).

---
