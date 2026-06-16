# Phase 3A Outline — Ch 4 (The Framework)

**Source file:** `chapters/03-the-framework.qmd` · **Priority:** OPTIONAL / do LAST in Phase 3C · **Drafter model:** Sonnet (lightest touch)
**Proposed title:** *"Chapter 4: The Framework: Six Stages, One Sprint at a Time"*
*(Alternative considered: "The Framework: Diagnose Before You Build, Then Compound." Both work; first one is the recommendation.)*
**Beads:** `book-0fq9` (FLOW#1 — pull first Action Step earlier; consider trimming "One Sprint, then another" tail), no other chapter-specific beads. SPC blank template already landed at L138-157 via Phase 3B consolidated artifact bead.
**Status:** **Reference model.** The only chapter with a full ✅ Pass on all three ARC axes. Minimal touch: retitle, strip italic-fragment headings, optional early Action Step. ~95%+ of existing prose survives. This is the chapter the other Drafters should learn from, not the chapter to rewrite. This outline carries the upgraded format ([[chapter-syllogism-and-flow-markers]]) so the Drafter can anchor sentence-to-sentence decisions in the chapter's argument structure.

---

## Chapter syllogism

- **Premise 1.** Chapters 1-3 established the problem (Diagnosis), the mindset shifts that make the work hold (Beliefs), and the way humans and agents operate together (Co-Op Model). The reader now knows there IS structural work to do; what they don't have is a procedure for doing it.
- **Premise 2.** The Framework is that procedure: a six-stage **Sequence** (Signal → Source → Design → Build → Deliver → Compound) run inside a single bounded **Sprint**. Each stage produces a named artifact the next stage depends on.
- **Premise 3.** One Sprint produces a structural change. The **Rhythm** is what makes those changes compound; the second Sprint is cheaper than the first, the third cheaper than the second.
- **Conclusion.** The reader leaves the chapter able to fill in a Sprint Planning Canvas — eight first-pass answers, one constraint named, the three operating fixtures locked — for their own first Sprint. The remaining chapters teach how to sharpen each answer.

---

## Chapter content outline (proposed)

> **Legend:** [NEW] = added · [CUT] = removed · [MOVE] = relocated · [TRIM] = shortened · [KEEP] = unchanged · *(L#)* = current line in `03-the-framework.qmd`

### I. In-Brief callout *(L3-6)* [KEEP]

- **Assumes:** reader has finished Ch 1-3 and accepts the problem is structural, not technological.
- **Establishes:** what this chapter delivers — the Sequence walked in order, the Canvas to plan one Sprint, Meridian's worked Canvas.
- **Sets up:** the opening story's "just build it" framing as the failure mode the chapter exists to prevent.

- A. Already clean — names the Sequence, the Canvas, the Meridian walk.
- B. No edits needed.

### II. Opening story — the "just build the workflow" CEO scene *(L8-18)* [KEEP verbatim]

- **Assumes:** reader has read the In-Brief and knows a procedure is coming.
- **Establishes:** the failure mode the chapter prevents — starting at Build. Names the diagnose-first move and the two-decade pattern behind it (Julie's ERP and integration history).
- **Sets up:** the section that says WHY order matters and what each stage owes the next.

- A. CEO on the call: *"Can we just build the workflow? I just need this thing built."* *(L8)*
- B. The pattern that follows when you start at Build: shifting requirements, scope expansion, edge cases, tool abandoned. *(L12)*
- C. The diagnosis-first move: a focused Signal Sprint instead of the build she asked for. *(L14)*
- D. Julie's two-decades pattern: ERP rollouts nobody used, post-merger integrations that broke the company. Root cause is always the same — solution built before problem understood. *(L16)*
- E. Closing transition: *"That's the conversation this chapter is meant to prevent."* *(L18)*
- F. **Exemplary narrative anchor — do not touch.**

### III. Concept — why the order matters *(L20-28)* [KEEP, retitle only]

  **Heading (current):** `## Why the *order* matters.`
  **Heading (proposed, directive, strip italics):** `## Diagnose Before You Build, or Build Pays the Cost`

- **Assumes:** reader saw the opening scene and recognizes the "just build it" instinct in themselves.
- **Establishes:** the principle behind the Sequence — wrong order is the failure, not wrong tool — and the dependency chain that gives each stage its job.
- **Sets up:** the four-words sidebar that locks the jargon (Framework / Sequence / Sprint / Rhythm) before the six stages walk in.

- A. The most common AI failure mode is wrong order, not wrong tool. *(L22)*
- B. The 30-year diagnose-before-prescribe principle from org-design; Julie's and Jesse's direct exposure. *(L24)*
- C. **The dependency chain — each stage produces what the next requires.** *(L26)*
    - 1. Signal → Constraint Statement
    - 2. Source → Knowledge Map (against the constraint)
    - 3. Design → accountability split (against both)
    - 4. Build → executes against Design
    - 5. Deliver → installs Build into operating rhythm
    - 6. Compound → captures learning, feeds next Sprint's Signal
- D. *"Skip the first two stages and you're buying a tool. Run all six in order and you're changing how the work is owned."* *(L28)* [KEEP]

### IV. Four-words sidebar *(L30-40)* [KEEP]

- **Assumes:** reader has accepted the order-matters principle and is about to hear repeated, slippery terms.
- **Establishes:** clean definitions for Framework, Sequence, Sprint, Rhythm — so the next section's six-stage walk doesn't have to relitigate vocabulary.
- **Sets up:** the six-stage walk, which uses all four terms as load-bearing words.

- A. Framework / Sequence / Sprint / Rhythm — directly addresses ARC#3 jargon needs.
- B. Lands well; no change.

### V. Framework — the six stages of the Sequence *(L42-106)*

  **Heading (current):** `## The six *stages*.`
  **Heading (proposed, directive, strip italics):** `## The Six Stages, in Order`

- **Assumes:** reader has the four-word vocabulary locked and accepts order is load-bearing.
- **Establishes:** what each of the six stages IS, what it produces, what changes after, and how the artifact it produces is consumed by the next stage. Each stage subsection follows the same shape (why it matters → what it produces → what changes after); the Meridian thread runs across all six.
- **Sets up:** the Diagnose / Execute & Compound split (the macro-structure of the Sequence), then the Canvas that holds first-pass answers for all six in one page.

- A. Intro sentence + Sequence Excalidraw *(L44-46)* [KEEP].
- B. **Each stage follows the same shape: why it matters → what it produces → what changes after. This is the template other restructured chapters should mirror.**

#### V.A. Signal — name the constraint, price it *(L48-56)* [KEEP]

  **Heading (current):** `### *Signal*. The constraint, named and priced.`
  **Heading (proposed):** `### Signal — Name the Constraint, Price It`

- **Assumes:** reader knows the Sequence runs Signal first.
- **Establishes:** what Signal IS as a stage — the diagnosis move that produces a one-page Constraint Statement with a dollar number against it. Meridian already lives in this stage at L52.
- **Sets up:** Source, which can only map knowledge against a named constraint.

- 1. **Why it matters:** most teams build for the visible problem or loudest complaint — neither is automatically the constraint. Symptom vs. structural cause. *(L50)*
- 2. **What it produces:** a one-page **Constraint Statement** with the function failing, outcome blocked, structural cause, and quantified cost. Meridian: *"Elena Ruiz is the sole quoting bottleneck… \$558K/year in delayed and lost revenue."* *(L52)*
- 3. **Quantified cost is non-negotiable.** Tells you if the constraint is worth a Sprint; gives Deliver a target. *(L54)*
- 4. **What changes after Signal:** team stops arguing about symptoms; sponsor knows the number the Sprint will move; cost is on paper for Deliver to measure against. *(L56)*
- 5. **[OPTIONAL] Pacing intervention point (FLOW#1):** could place a 30-second "name your constraint candidate" Action Step here. **AUTHOR REVIEW:** add it here, or after the Diagnose/Execute split (§VII), or skip? Recommend skip if it bloats; the chapter is intentionally concept-heavy.

#### V.B. Source — map what the organization knows *(L58-66)* [KEEP]

  **Heading (current):** `### *Source*. What the org actually knows.`
  **Heading (proposed):** `### Source — Map What the Organization Knows`

- **Assumes:** Signal produced a named constraint with a price on it.
- **Establishes:** what Source IS — the inventory of structured / semi-structured / tacit knowledge against that constraint, producing a Knowledge Map. Meridian already lives in this stage at L62 (147-row spreadsheet, Dave's 31 years, JobBOSS-CRM disconnect).
- **Sets up:** Design, which uses the Knowledge Map to make the human / agent split functional rather than ideological.

- 1. **Why it matters:** workflows built without Source have no reliable ground for an agent to reason against — hallucinations, gaps, edge-case failures. *(L60)*
- 2. **What it produces:** a **Knowledge Map** across three categories — structured (CRM, ERP, SOP), semi-structured (desktop spreadsheets, transcripts), tacit (in people's heads). Meridian: 147-row Customer Notes.xlsx, Dave Kowalski's 31 years of fabrication knowledge, JobBOSS-CRM disconnect. *(L62)*
- 3. **Three categories drive three Build moves:** connect (structured), organize (semi-structured), capture (tacit). *(L64)*
- 4. **What changes after Source:** Sprint stops running on collective memory and starts running on a map; you know which knowledge an agent can reason against and which a human still has to supply. *(L66)*

#### V.C. Design — make the shape of the work explicit *(L68-76)* [KEEP]

  **Heading (current):** `### *Design*. The shape of the work, made explicit.`
  **Heading (proposed):** `### Design — Make the Shape of the Work Explicit`

- **Assumes:** Source produced a Knowledge Map; the constraint is named, priced, and grounded in real artifacts.
- **Establishes:** what Design IS — the stage where the Co-Operating Model from Ch 3 becomes an actual chart (Hybrid Accountability Chart + Design Brief). Names handoff triggers, supervisors, exception routing.
- **Sets up:** Build, which executes against Design's shape. If a stalled Sprint blames Build, the diagnostic rule (§VI) says check Design first.

- 1. **Why it matters:** a workflow without a designed shape is a habit; adding an agent to that produces an agent nobody knows how to supervise. Design is where the Co-Operating Model from Ch 3 becomes an actual chart. *(L70)*
- 2. **What it produces:** two artifacts — the **Hybrid Accountability Chart** (functions, handoffs, supervisors, exception routing) and the **Design Brief** (information flow, governance, guardrails). *(L72)*
- 3. **Human/agent split is functional, not ideological.** Two questions: judgment a model can't supply → human; rules an agent can apply consistently → agent under supervisor. *(L74)*
- 4. **What changes after Design:** every accountability has a named owner; every handoff has a defined trigger; every agent has a human supervisor; Build has something to execute against. *(L76)*
- 5. **[NEW — Meridian thread, per [[meridian-as-side-by-side-thread]]]** Add ONE Meridian sentence inside the "what it produces" block (L72) so the stage isn't abstract: *"For Meridian, Design produced a Hybrid Accountability Chart where Elena moved from quote producer to quote reviewer, Ty took quote initiation, and the quoting agent landed under Elena's supervisor seat."* One sentence. Light touch. See Meridian audit below.

#### V.D. Build — ship the system that works *(L78-86)* [KEEP]

  **Heading (current):** `### *Build*. The system, working.`
  **Heading (proposed):** `### Build — Ship the System That Works`

- **Assumes:** Design produced a locked HAC and Design Brief; the human / agent split is settled before code gets written.
- **Establishes:** what Build IS — fast execution against Design, producing a Build Spec, a Guardrails Checklist, and the working machine. Names the path choice (off-the-shelf / low-code / hand-built).
- **Sets up:** Deliver, which lands the working machine into how work actually gets done (not the same thing as shipping it).

- 1. **Why it matters:** Build is fast when Design is locked. Slowness teams blame on building is usually Design work bleeding into Build. *(L80)*
- 2. **What it produces:** a **Build Spec** end to end + a **Guardrails Checklist** (what the agent can/can't do, when humans pull in, what gets logged) + the working machine (prompts, integrations, knowledge layer, observability). *(L82)*
- 3. **Build also chooses a path:** off-the-shelf · low-code · hand-built. Pick one. *(L84)*
- 4. **What changes after Build:** a working system handles real work end to end against Signal's constraint, Design's shape, and Source's data. *(L86)*
- 5. **[NEW — Meridian thread]** Add ONE Meridian sentence inside the "what it produces" block (L82): *"Meridian's Build Spec connected HubSpot → JobBOSS → Claude through an n8n workflow, with the Guardrails Checklist locking 'no quote ships without Elena's approval until the workflow has been calibrated for sixty days.'"* One sentence. See Meridian audit below.

#### V.E. Deliver — land the system in how work actually gets done *(L88-96)* [KEEP]

  **Heading (current):** `### *Deliver*. The handoff into how work actually gets done.`
  **Heading (proposed):** `### Deliver — Land the System in How Work Actually Gets Done`

- **Assumes:** Build produced a working machine that passes its own tests.
- **Establishes:** what Deliver IS — the stage that closes the deployed-vs-delivered gap, producing a Deploy Readiness Audit, per-role runbooks, and a Delivery Test measured against Signal's cost number.
- **Sets up:** Compound, which can only run if Deliver actually moved the work (otherwise there's nothing to learn from).

- 1. **Why it matters:** deploying isn't delivering. A tool in an unopened tab is deployed, not delivered. Most AI projects die in the gap. *(L90)*
- 2. **What it produces:** three things — **Deploy Readiness Audit** (integrations, data flows, guardrails under load), **per-role runbook** (what each person does now, what's different, what to escalate), **Delivery Test** (workflow measured against Signal's cost). *(L92)*
- 3. **Runbook matters more than audit.** Audit confirms the machine; runbook confirms the humans whose work changes know what to do Monday morning. *(L94)*
- 4. **What changes after Deliver:** the work itself has changed — not the slide deck about the work, the work itself. The Constraint Statement's numbers have moved against target. *(L96)*
- 5. **[NEW — Meridian thread]** Add ONE Meridian sentence inside the "what it produces" block (L92): *"Meridian's Delivery Test was thirty quotes through the new workflow in thirty days, with the runbook telling Ty exactly what to initiate, what to validate, and when to pull Elena in."* One sentence. See Meridian audit below.

#### V.F. Compound — turn the Sprint into infrastructure *(L98-106)* [KEEP]

  **Heading (current):** `### *Compound*. What the next Sprint inherits.`
  **Heading (proposed):** `### Compound — Turn the Sprint Into Infrastructure`

- **Assumes:** Deliver actually moved the Constraint Statement's numbers against target; one structural change is in the operating model.
- **Establishes:** what Compound IS — the stage that captures what shipped, updates the Hybrid Org Today, re-ranks the constraint queue, and seeds the Compound Bench for the next Sprint.
- **Sets up:** the Diagnose / Execute & Compound split (§VI), which generalizes what each half of the Sequence is for, and the Canvas, which is the planning artifact for the NEXT Sprint.

- 1. **Why it matters:** Sprints stop being one-offs when the company starts to compound; otherwise every next Sprint restarts from scratch. *(L100)*
- 2. **What it produces:** **Sprint Outcome Record** (shipped, changed, cost, return) + updated **Hybrid Org Today** + re-ranked constraint queue + handoff to **Compound Bench**. *(L102)*
- 3. **What carries forward isn't just documents.** Reusable knowledge base, practiced design discipline, roster of Sprint operators — second Sprint costs less than first. *(L104)*
- 4. **What changes after Compound:** the company learns; the Knowledge Map gets richer; the Sprint stops being a project and becomes part of how the company runs. *(L106)*
- 5. **[NEW — Meridian thread]** Add ONE Meridian sentence inside the "what it produces" block (L102): *"Meridian's Sprint Outcome Record carried the quoting workflow into Q4 with scheduling — the next Elena-dependent function — re-ranked to the top of the queue."* One sentence. See Meridian audit below.

### VI. Concept — Diagnose vs. Execute & Compound *(L108-119)* [KEEP, retitle only]

  **Heading (current):** `## *Diagnose* and *Execute & Compound*.`
  **Heading (proposed, directive):** `## Diagnose Before You Execute & Compound`

- **Assumes:** reader has walked all six stages and seen each stage's artifact feed the next.
- **Establishes:** the macro-shape of the Sequence — Diagnose (Signal + Source) vs. Execute & Compound (Design / Build / Deliver / Compound) — and the diagnostic rule: a stalled Build is almost never a Build problem.
- **Sets up:** the Canvas, which is the artifact that holds first-pass answers across BOTH halves on one page.

- A. The Sequence splits into two groups *(L110)*
    - 1. **Diagnose:** Signal, Source — the work most companies skip (inputs abstract, output is paper).
    - 2. **Execute & Compound:** Design, Build, Deliver, Compound — the work most companies start at (building feels like progress).
- B. **The diagnostic rule:** a Sprint that stalls in Build almost never has a Build problem. Go back to Signal. *(L110)*
- C. Physical vs. information processes: in information work, taxonomy errors stay invisible until the damage is done. Diagnose is where you find them first. *(L112)*
- D. Excalidraw — Diagnose/Execute split *(L114)* [KEEP].
- E. **Pro Tip callout** *(L116-119)*: *"When a Sprint stalls in Build, don't troubleshoot the build. Go back to Signal, Source, and Design."* [KEEP]
- F. **[OPTIONAL] Pacing intervention point (FLOW#1):** alternative location for an earlier interactive moment — "which half did your last initiative fail in?" prompt. **AUTHOR REVIEW:** add here, after V.A. Signal, or skip?

### VII. Framework — the Sprint Planning Canvas, eight questions *(L121-194)*

  **Heading (current):** `## The *Sprint Planning Canvas*.`
  **Heading (proposed, directive):** `## The Sprint Planning Canvas Holds Eight Questions in One Page`

- **Assumes:** reader has the Sequence in head and knows what each stage produces.
- **Establishes:** the Canvas as the one-page artifact that holds first-pass answers for all eight questions — one per stage plus Rhythm. Names the three operating fixtures (sponsor, Orchestrator, review date) that turn a plan into a Sprint. Includes the blank template, the populated Meridian Canvas, and the Action Step that points the reader at their own first pass.
- **Sets up:** the closing — Run one Sprint, then another — which generalizes from "first Sprint" to "Rhythm."

- A. **Why a Canvas before a Sprint.** Stop staring at a blank page; start with something the Sequence can sharpen. Intentionally incomplete. *(L123)*

- B. **The eight questions** *(L125-134)* [KEEP] — each previews a stage and points at a teaching chapter:
    - 1. **What's the validated constraint, and what does it cost?** → Signal
    - 2. **What does the org know about it, and where does that knowledge live?** → Source
    - 3. **How does information flow through the workflow?** → Source / Design
    - 4. **Who's accountable across humans and agents?** → Design (Hybrid Accountability Chart)
    - 5. **What's the system specification?** → Build (Spec + Guardrails Checklist)
    - 6. **How does the deployment land in real work?** → Deliver (runbook + Delivery Test)
    - 7. **What changed structurally?** → Compound (Hybrid Org Today)
    - 8. **What's the cadence, and what's next?** → Rhythm (next Sprint)

- C. **Canvas Excalidraw** *(L136)* [KEEP].

- D. **[Phase 3B] Blank Sprint Planning Canvas template** *(L138-157)* [VERIFY — added by consolidated artifact bead, do not redo]
    - 1. Constraint sentence at top.
    - 2. Three operating fixtures line: Leadership sponsor · Human Orchestrator · Quarter / review date.
    - 3. Eight-row table: # · Question · Your first-pass answer · Teaching chapter.
    - 4. Team + Review-date closers.
    - 5. **Drafter task:** confirm the heading + intro sentence at L138 connect cleanly into the table; no other change.

- E. **Bridge prose** *(L159)*: "The eight questions are the spine. Each subsequent chapter takes one or two and walks you through how to answer it." [KEEP]

- F. **Sprint scope discipline** *(L161)*: bounded by scope, not calendar. Days, weeks, or across a quarter; scope is what doesn't stretch. **Time-budget language (ARC#9) — KEEP**, it's operational, not procedural.

- G. **Three operating fixtures** *(L163)* [KEEP]: Leadership sponsor · Human Orchestrator · Review date. *"The Sprint is real when the review is on the calendar."*

#### VII.H. A populated Canvas — Meridian *(L165-194)* [KEEP]

  **Heading (current):** `### What a populated Canvas looks like.`
  **Heading (proposed):** `### A Populated Canvas Looks Like This`

- **Assumes:** reader has read the blank Canvas template and the eight questions. Has seen Meridian appear in each of the six stage subsections (per Meridian audit below).
- **Establishes:** what a complete first-pass Canvas LOOKS like — a real company's eight answers, the three operating fixtures filled in, the review on the calendar. The central illustration of the chapter.
- **Sets up:** the "Fill In Your Own" Action Step (the reader's first deliverable from this chapter).

- 1. Meridian recap: \$7.2M, 27 employees, Mark + Elena, 3-5 day quotes vs. competitors' 24-48 hours. *(L167)*
- 2. Setup sentence *(L169)*.
- 3. **Constraint:** Elena, \$558K/year. *(L171)*
- 4. **Operating fixtures line:** Mark (sponsor), Elena (Orchestrator), Q3. *(L173)*
- 5. **Eight-row populated table** *(L175-184)* — all eight Meridian first-pass answers [KEEP verbatim].
- 6. **Team + Review** closers *(L186-188)*.
- 7. **Populated Canvas Excalidraw** *(L190)* [KEEP].
- 8. **The thirty-minute observation** *(L192)*: *"That Canvas took thirty minutes to fill. It's wrong in at least two places."* — **KEEP**, anchors the "first pass, not final" discipline. Time-budget strip flag (ARC#9): operational, not procedural.
- 9. **Format-doesn't-matter close** *(L194)* [KEEP].

#### VII.I. Fill in your own — Action Step *(L196-205)* [KEEP, retitle]

  **Heading (current):** `### Fill in your own.`
  **Heading (proposed, strip italic):** `### Fill In Your Own`

- **Assumes:** reader has seen Meridian's populated Canvas and accepts "wrong first guess beats blank row."
- **Establishes:** the chapter's deliverable — the reader's own first-pass Canvas. Names the question-to-teaching-chapter map so the reader knows where each weak row gets sharpened.
- **Sets up:** the "Run one Sprint, then another" close, which generalizes from one Canvas to the Rhythm.

- 1. **Action Step callout** *(L198-203)* [KEEP]
    - a. One sentence for the constraint.
    - b. One first-pass answer per question.
    - c. Name the sponsor, Orchestrator, review date.
    - d. *"A wrong first guess is better than a blank row."*
    - e. Pointer to the blank template above (Phase 3B).
- 2. **Teaching-chapter mapping** *(L205)* [KEEP] — explicitly maps the eight questions to the chapters that teach them:
    - Q1 → Signal
    - Q2, most of Q3 → Source
    - Rest of Q3 + Q4 → Design
    - Q5 → Build
    - Q6 → Deliver
    - Q7, Q8 → Compound
    - Rhythm chapter → what happens after one Sprint is done.
- 3. Closing line *(L207)*: *"The eight-question Canvas is the artifact the rest of the book is organized around. Carry it forward."* [KEEP]

### VIII. Closing — Run one Sprint, then another *(L209-213)* [KEEP, retitle; optional tighten]

  **Heading (current):** `## One Sprint, then *another*.`
  **Heading (proposed, directive):** `## Run One Sprint. Then Another.`

- **Assumes:** reader has a first-pass Canvas in hand (or is about to draft one).
- **Establishes:** the conclusion of the chapter's syllogism — one Sprint produces structure, but the Rhythm is what compounds; each Sprint is cheaper and faster than the last.
- **Sets up:** the handoff to Ch 5 (Signal), the first stage of the first Sprint.

- A. The Framework is learned by running it; the stages' dependencies only become real when you hit them. *(L211)*
- B. The Rhythm turns one Sprint into a compounding business; each Sprint cheaper and faster than the last. *(L213)*
- C. **[OPTIONAL] Tail trim (reading-team flag):** current closing is 5 sentences across two paragraphs. Consider tightening to 3-4 sentences. **AUTHOR REVIEW:** trim or keep? Recommend keep; the rhythm payoff matters for the next chapter handoff.

### IX. Handoff — Begin at Signal *(L215-217)* [KEEP, strip italic]

  **Heading (current):** `## Begin at *Signal*.`
  **Heading (proposed):** `## Begin at Signal`

- **Assumes:** reader accepts the Rhythm payoff and is willing to start.
- **Establishes:** the handoff sentence pointing at Ch 5 — Every Sprint begins at Signal, with one constraint named, quantified, and validated.
- **Sets up:** Ch 5, which teaches Signal as a full stage.

- A. *"The Sequence is the workflow. The next chapter is the first stage. Every Sprint begins at Signal, with one constraint named, quantified, and validated before anything else moves."* [KEEP — already crisp]

### X. Reflection Questions *(L219-225)* [KEEP all 4]

- **Assumes:** reader has finished the chapter and possibly drafted a Canvas.
- **Establishes:** four prompts that translate the chapter's claims into a leadership-team conversation (have you jumped to Build · Canvas confidence map · Diagnose vs. Execute & Compound stall · Human Orchestrator named).
- **Sets up:** the team conversation that turns a first-pass Canvas into a Sprint actually on the calendar.

- A. Q1 — Have you jumped to Build before Signal/Source? What did it cost?
- B. Q2 — Fill in the Canvas; which rows are confident and which are blank? Blanks are the diagnostic.
- C. Q3 — Diagnose vs. Execute & Compound: which half did your last stall happen in?
- D. Q4 — Human Orchestrator: name written down, or seat vacant?

---

## Heading inventory — current → proposed (full set)

| Current heading *(L#)* | Proposed directive heading |
|---|---|
| `# The *Framework*.` *(L1)* | `# Chapter 4: The Framework: Six Stages, One Sprint at a Time` |
| `## Why the *order* matters.` *(L20)* | `## Diagnose Before You Build, or Build Pays the Cost` |
| `## The six *stages*.` *(L42)* | `## The Six Stages, in Order` |
| `### *Signal*. The constraint, named and priced.` *(L48)* | `### Signal — Name the Constraint, Price It` |
| `### *Source*. What the org actually knows.` *(L58)* | `### Source — Map What the Organization Knows` |
| `### *Design*. The shape of the work, made explicit.` *(L68)* | `### Design — Make the Shape of the Work Explicit` |
| `### *Build*. The system, working.` *(L78)* | `### Build — Ship the System That Works` |
| `### *Deliver*. The handoff into how work actually gets done.` *(L88)* | `### Deliver — Land the System in How Work Actually Gets Done` |
| `### *Compound*. What the next Sprint inherits.` *(L98)* | `### Compound — Turn the Sprint Into Infrastructure` |
| `## *Diagnose* and *Execute & Compound*.` *(L108)* | `## Diagnose Before You Execute & Compound` |
| `## The *Sprint Planning Canvas*.` *(L121)* | `## The Sprint Planning Canvas Holds Eight Questions in One Page` |
| `### What a populated Canvas looks like.` *(L165)* | `### A Populated Canvas Looks Like This` |
| `### Fill in your own.` *(L196)* | `### Fill In Your Own` |
| `## One Sprint, then *another*.` *(L209)* | `## Run One Sprint. Then Another.` |
| `## Begin at *Signal*.` *(L215)* | `## Begin at Signal` |
| `## Reflection Questions` *(L219)* | `## Reflection Questions` *(keep)* |

---

## Artifacts inventory

| Artifact | Status |
|---|---|
| Sprint Planning Canvas — blank, 8-question template *(L138-157)* | ✅ Already added by Phase 3B consolidated artifact bead. Verify placement, do not redo. |
| Populated Meridian Canvas — 8-row table with first-pass answers *(L175-184)* | ✅ Already in body. Keep verbatim. |
| Eight-question list *(L125-134)* | ✅ Already in body. Keep verbatim. |
| Sequence Excalidraw *(L46)* | ✅ Keep. |
| Diagnose/Execute split Excalidraw *(L114)* | ✅ Keep. |
| Sprint Planning Canvas blank Excalidraw *(L136)* | ✅ Keep. |
| Sprint Planning Canvas populated/Meridian Excalidraw *(L190)* | ✅ Keep. |
| Action Step — Fill in your own Canvas *(L198-203)* | ✅ Keep. |
| Four-words sidebar — Framework/Sequence/Sprint/Rhythm *(L30-40)* | ✅ Keep — addresses ARC#3 jargon clarity. |
| Pro Tip — when stalled, go back to Signal *(L116-119)* | ✅ Keep. |

---

## Meridian thread audit (per [[meridian-as-side-by-side-thread]])

Ch 4 already has Meridian as the chapter's central illustration — the populated Sprint Planning Canvas at L171-188 is the payoff. Per the new rule, Meridian should ALSO appear at the introduction of each of the six stages so the reader meets the parallel at the concept landing, not only at the end. Light touch: ONE sentence per stage, inside the existing "what it produces" block.

**Current Meridian presence in `chapters/03-the-framework.qmd`:**

| Location | Meridian present? | Notes |
|---|---|---|
| L5 (In-Brief) | ✅ Named — "you'll have walked Meridian Manufacturing's populated Canvas" | Keep |
| §V.A Signal (L52) | ✅ Strong — Constraint Statement with Elena + \$558K | Keep |
| §V.B Source (L62) | ✅ Strong — 147-row spreadsheet, Dave's 31 years, JobBOSS-CRM disconnect | Keep |
| §V.C Design (L72) | ❌ Missing | **ADD ONE SENTENCE** per V.C.5 above |
| §V.D Build (L82) | ❌ Missing | **ADD ONE SENTENCE** per V.D.5 above |
| §V.E Deliver (L92) | ❌ Missing | **ADD ONE SENTENCE** per V.E.5 above |
| §V.F Compound (L102) | Partial — mentions "Hybrid Org Today" but not Meridian's specifically | **ADD ONE SENTENCE** per V.F.5 above |
| §VII Canvas intro (L123-134) | Indirect — eight questions land abstract | No change; Meridian arrives at L165 |
| §VII.H Populated Canvas (L165-194) | ✅ Central — full populated Canvas | Keep verbatim; this is the chapter's payoff |
| §VIII Closing (L209-213) | ❌ No Meridian | No change; closing generalizes from one Sprint to Rhythm |

**Recommendation:** add four single sentences (V.C, V.D, V.E, V.F). The cumulative add is ~80 words. The chapter's minimal-touch scope is preserved; the Meridian thread now lands at every stage introduction. The populated SPC at L171-188 remains the chapter's central illustration.

**Why these specific landings work:** each one slots inside the existing "what it produces" block (not a new bullet, not a new paragraph). The reader sees the abstract artifact named, then sees what it looked like at Meridian, then continues to "what changes after." The structure of the stage doesn't change; one parallel sentence rides inside it.

---

## Edit decisions (minimal touch)

1. **Retitle** to `# Chapter 4: The Framework: Six Stages, One Sprint at a Time` (Traction-style; descriptive + main-idea clause).
2. **Strip italic-fragment headings** across all 15 headings (see inventory table above). This is the largest single move and it is mechanical.
3. **[OPTIONAL] Add ONE early Action Step / interactive moment** — current chapter places its only Action Step at L199, which is 89% through (reading-team FLOW#1 flag). Two candidate slots: after V.A. Signal (L56) or after VI. Diagnose/Execute split (L119). **AUTHOR REVIEW:** add one, or skip if it bloats? Recommend skip unless it can stay to ~3 lines; the chapter's 90% concept / 10% action shape is appropriate for a Framework overview.
4. **[OPTIONAL] Tail tighten** — "Run one Sprint, then another" at L209-213 reads slightly soft per reading team. Consider 3-4 sentences instead of 5. **AUTHOR REVIEW:** trim, or keep? Recommend keep; the rhythm payoff sets up the next chapter.
5. **[VERIFY only]** Phase 3B's SPC blank template at L138-157 — confirm heading + intro sentence connect cleanly into the table; no other change.
6. **[NEW — Meridian thread per [[meridian-as-side-by-side-thread]]]** Add ONE Meridian sentence inside the "what it produces" block of each of the four stages that currently lack Meridian: Design (L72), Build (L82), Deliver (L92), Compound (L102). Exact suggested sentences are in §V.C.5, V.D.5, V.E.5, V.F.5 above. Total add: ~80 words. The chapter's central illustration (populated Canvas at L171-188) is unchanged. // AUTHOR FOLLOWUP: confirm the four suggested sentences land cleanly; the Drafter may tighten wording but the four landings are non-negotiable per the Meridian rule.

---

## HBR citation discipline (this chapter)

**Current count:** Zero HBR citations.
**Action:** None. Keep zero.

---

## Cross-chapter dependencies handled in Phase 3B (Drafter does NOT re-solve)

- Canonical agent definition at first use *(book-ultm)* — handled in Ch 2 at L35. No conflict here.
- Orchestrator/Integrator disambiguation *(book-8v6v.32)* — the chapter uses both terms cleanly (Elena Ruiz is named "integrator" in EOS context at L167 and "Human Orchestrator" in Sprint context at L173). No fix needed; **VERIFY** post-Phase-3B that the global convention lands well here.
- Jargon parentheticals *(book-xqxi)* — the four-words sidebar at L30-40 already handles the chapter's core jargon. None to add.
- SPC through-line *(consolidated artifact bead)* — blank template already added at L138-157.
- Chapter-N refs post-renumbering *(book-tb8h)* — already verified. No additional work.
- Meridian weave *(FLOW#3)* — Meridian's populated Canvas is the chapter's central illustration. Strong. Per [[meridian-as-side-by-side-thread]], the rule now requires Meridian at each stage introduction (not only the central illustration); four single-sentence adds in §V.C-F are listed in the Meridian audit above. Drafter handles, not Phase 3B.

---

## Drafter notes

- **Drafter model:** Sonnet (lightest touch).
- **Do this chapter LAST in Phase 3C.** Ch 4 is the reference model. Doing it last lets the other Drafters converge on directive-heading style and Traction title conventions so Ch 4's update is mechanical and inherits any patterns that emerge.
- ~95%+ of existing prose survives. This is retitle + heading sweep + four Meridian single-sentence adds + (optional) one Action Step + (optional) tail tighten. Not a restructure.
- **Anchoring discipline:** Drafter reads the chapter syllogism + each section's Assumes/Establishes/Sets up triad BEFORE writing. Sentence-to-sentence decisions inside a section must respect the section's flow markers. The four new Meridian sentences must satisfy the stage's Sets up line (i.e., they support the next stage's Assumes, not just illustrate the current one).
- **Full QC pipeline runs per [[qc-pipeline-per-chapter]]:** Drafter → EC → Deflourisher → Voice Scan → Prose-Craft → Editor → orchestrator gate. No bundling, no skipping. EC verifies the chapter against the syllogism; Deflourish is non-negotiable per memory.
- **No tools:** Drafter does NOT run deflourish, voice-scan, prose-craft, or any other tool. Those are separate pipeline stages.
- Voice charter applies. The chapter is already low on em-dashes; **the four new Meridian sentences must contain ZERO em-dashes** (voice charter on new layers).
- Verify the Phase 3B SPC blank template at L138-157 renders cleanly and connects to the intro sentence; no other change.
- // AUTHOR FOLLOWUP: sign-off needed BEFORE Drafter dispatches on: (a) whether to add an earlier Action Step and where; (b) whether to trim the "One Sprint, then another" tail; (c) the four suggested Meridian sentences in §V.C.5 / V.D.5 / V.E.5 / V.F.5 (Drafter may tighten wording, but the four landings are required).
