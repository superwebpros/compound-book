# Action Step Sync Audit

**Generated:** 2026-06-10  ·  **Branch:** merge-julie-feedback  ·  **Agent:** Action Step Sync Auditor

## TL;DR

Chapter prose carries **49 Action Step callouts** across 13 files; the index appendix (`chapters/appendix-action-steps.qmd`) carries **48 entries**. The two sets are NOT in lockstep: one Action Step is missing entirely from the index (the prompt-engineering appendix step), and at least **15 of the 48 mapped entries** have prose drift ranging from light rewording to substantively different titles, framing, or worked-example content. Severity overall: **moderate to high** — counts are nearly aligned but wording and examples diverge widely enough that the appendix can no longer be trusted as a verbatim digest of the chapter callouts.

## Per-chapter audit

### Preface (`/Users/jesseflores/projects/compound/sites/compound-book/index.qmd`)

Action Steps in chapter: **0**
Appendix entries for Preface: **0**

Confirmed N/A. No drift.

---

### Chapter 1 — Diagnosis (`chapters/01-diagnosis.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L85 (prose):**
   ```
   Walk into your next L10 or leadership meeting with this question: "If AI were an employee, what would its scorecard say?" Write down whatever the room produces. If the room can't answer — if there's no scorecard, no number, no owner — that's your answer. There is no scorecard. And that's exactly the problem.
   ```

2. **L135 (prose):**
   ```
   Poll your leadership team individually, not in a group. Ask each person: "What is the ONE operational problem AI should solve for us?" Write down their answers verbatim. If you get five different answers from five people, you've got your diagnosis.
   ```

3. **L161 (prose):**
   ```
   Pick your most critical workflow. Ask the person who owns it: "If you had to hand this off to someone new on Monday, what would you give them?" Whatever they describe is the actual state of your documentation — not whatever lives in SharePoint.
   ```

4. **L179 (prose):**
   ```
   Whiteboard your most constrained workflow in fifteen minutes. Put every handoff on the board. Circle the ones where work stalls, errors appear, or people say "I'll just handle it myself." Those circles are where the real problem lives.
   ```

5. **L197 (prose):**
   ```
   List the five most frequent decisions in your constrained workflow. For each one, write down who currently makes the decision and whether it requires judgment or just follows a rule. The rule-based ones are AI-eligible. The judgment ones need a human-in-the-loop design.
   ```

6. **L215 (prose):**
   ```
   Do the math right now. Hours per week spent on the constraint, multiplied by loaded cost per hour, multiplied by thirteen weeks. That's your quarterly cost floor. If you can't fill in the numbers, write down what data you'd need and where you'd get it. That gap is your first task.
   ```

7. **L281 (prose):**
   ```
   The scorecard is the input every other chapter references. Take an hour with your leadership team, ideally before your next L10, to score each dimension and write the scores down. Every chapter ahead will ask you to come back to them.
   ```

**Appendix entries for Chapter 1 (in order):**

1. **Appendix L12:**
   ```
   Walk into your next L10 or leadership meeting with this question: "If AI were an employee, what would its scorecard say?" Write down whatever the room produces. If the answer is silence, that silence is the diagnosis.
   ```

2. **Appendix L17:**
   ```
   Poll your leadership team individually — not in a group. Ask each person: "What is the ONE operational problem AI should solve for us?" Write down their answers verbatim. If you get five different answers from five people, you have your diagnosis.
   ```

3. **Appendix L22:**
   ```
   Pick your most critical workflow. Ask the person who owns it: "If you had to hand this off to someone new on Monday, what would you give them?" Whatever they describe is the actual state of your documentation — not whatever lives in SharePoint.
   ```

4. **Appendix L27:**
   ```
   Whiteboard your most constrained workflow in fifteen minutes. Put every handoff on the board. Circle the ones where work stalls, errors appear, or people say "I'll just handle it myself." Those circles are where the real problem lives.
   ```

5. **Appendix L32:**
   ```
   List the five most frequent decisions in your constrained workflow. For each one, write down who currently makes the decision and whether it requires judgment or just follows a rule. The rule-based ones are AI-eligible. The judgment ones need a human-in-the-loop design.
   ```

6. **Appendix L37:**
   ```
   Do the math right now. Hours per week spent on the constraint, multiplied by loaded cost per hour, multiplied by thirteen weeks. That's your quarterly cost floor. If you can't fill in the numbers, write down what data you'd need and where you'd get it. That gap is your first task.
   ```

7. **Appendix L42:**
   ```
   Before you turn the page, fill in the scorecard. All five dimensions. Write the scores down — don't just read the descriptions and nod. The scorecard travels with you through the rest of the book, and every chapter will ask you to reference it. Sixty minutes with your leadership team. Do it before your next L10.
   ```

**Drift findings for Chapter 1:**

1. **AS #1 WORDING DIFFERS.** Chapter (L85) ends with "If the room can't answer — if there's no scorecard, no number, no owner — that's your answer. There is no scorecard. And that's exactly the problem." Appendix (L12) compresses this to: "If the answer is silence, that silence is the diagnosis." Substantively similar idea, materially different sentence.
2. **AS #2 minor wording.** Chapter uses "you've got" / "individually, not in a group"; appendix uses "you have" / "individually — not in a group". Effectively cosmetic, but not verbatim.
3. **AS #7 SUBSTANCE DIFFERS.** Chapter (L281) reads "The scorecard is the input every other chapter references. Take an hour with your leadership team, ideally before your next L10, to score each dimension and write the scores down. Every chapter ahead will ask you to come back to them." Appendix (L42) is a completely different sentence: "Before you turn the page, fill in the scorecard. All five dimensions. Write the scores down — don't just read the descriptions and nod. The scorecard travels with you through the rest of the book … Sixty minutes with your leadership team. Do it before your next L10." Different opening, different cadence (60 min vs. an hour), different framing ("travels with you" vs. "input every other chapter references"). This is the largest Ch 1 drift.

---

### Chapter 2 — The Co-Operating Model (`chapters/02-co-operating-model.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L111 — Identify Your Baseline:**
   ```
   Pick one role in your company — yours, or a direct report's. Estimate: what percentage of that person's week is spent on work that belongs in the right column? Write it down. That number is your baseline. You'll use it before the chapter ends.
   ```

2. **L161 — Map One Role Against the Two Columns:**
   ```
   Pick the role you flagged earlier. Think through what that person actually spends their week on — the work as it happens, not the work as the job description writes it. Then sort each task into Column A (Human Intelligence: judgment that changes based on context a machine can't observe) or Column B (Agent Intelligence: processing that follows rules a machine could learn). Some tasks will split — "managing scope change requests" includes reading client politics (Column A) and updating the change log (Column B). Split those and sort each part.

   Consider a typical professional services role — a Project Coordinator at a mid-sized firm. (This is an illustrative composite, not a specific client.) Here is what the sort looks like: [TABLE]
   Column B accounts for roughly 55% of this coordinator's week. At a loaded annual cost of $65,000, that is $36,000 per year of human intelligence allocated to work that follows learnable rules.
   ```

3. **L232 — Calculate Your Design Opportunity:**
   ```
   Take the Column A / Column B sort you did earlier. Count the tasks in each column. Estimate the hours per week for each. Calculate the percentage of the role's week that lives in Column B — that is your design opportunity, the share of the role that could be running on agent intelligence instead of human hours.

   Write it as a single number: "This role is __% Column B."

   Now multiply that percentage by the person's loaded annual cost (salary + benefits + overhead). That number is the annual operating cost of not redesigning this role.

   For the illustrative Project Coordinator: 55% Column B at $65,000 loaded cost = $36,000/year spent on work that follows learnable rules. That is the dollar value of human intelligence being spent on agent-intelligence work.
   ```

4. **L245 — Start Your Hybrid Split:**
   ```
   Now that you've split the role into Column A and Column B, map the hybrid version: who does what when human and agent share the role. The human manages; the agent does the labor that follows rules.

   Here is the illustrative Project Coordinator's hybrid split: [TWO-COLUMN HUMAN MANAGES / AGENT LABORS TABLE]

   This hybrid split is enough to see the shape of the redesigned role. Chapter 5 introduces the full design instrument — the TML framework (Task / Management / Leadership) — which sorts work into three categories rather than two; for now, the two-column version is the right starting point.

   If you have multiple roles touching the same constraint, repeat this process for each one. Compile the results into a single table: Role, Column B %, Loaded Cost, Annual Misallocation Cost. That table is the raw material for the Sprint design work in the chapters ahead.
   ```

**Appendix entries for Chapter 2 (in order):**

1. **Appendix L51 — Identify Your Baseline:** identical to chapter L111. No drift.

2. **Appendix L56 — Map One Role Against the Two Columns:**
   ```
   Take the role you picked earlier. List 10–15 tasks that person actually does in a typical week — not what the job description says, what they do. Pull their calendar. Check their sent folder. Then sort every task into Column A … Some tasks will split — "managing scope change requests" includes reading client politics (Column A) and updating the change log (Column B). Split those and sort each part.

   Here is what this looks like for a Project Coordinator at a professional services firm: [TABLE]
   Column B accounts for roughly 55% of this coordinator's week. At a loaded annual cost of $65,000, that is $36,000 per year of human intelligence allocated to work that follows learnable rules.
   ```

3. **Appendix L75 — Calculate Your Design Opportunity:**
   ```
   Take the Column A / Column B sort you did earlier. … For the Project Coordinator example: 55% Column B at $65,000 loaded cost = $36,000/year spent on work that follows learnable rules. That is the dollar value of human intelligence being spent on agent-intelligence work.
   ```

4. **Appendix L86 — Describe the Hybrid Version:**
   ```
   If Column B tasks were handled by agents, what would this person do with the freed capacity? Write a one-paragraph description of a typical day — not a vision statement.

   Here is the Project Coordinator's hybrid version: Monday morning starts with reviewing agent-generated status reports and flagging anything that needs a human conversation. The rest of the week goes to managing two difficult scope negotiations, sitting in on a client call where the relationship is at risk, and coordinating a cross-functional delivery problem that involves competing priorities between three teams. Meeting summaries write themselves. Overdue items surface automatically. The coordinator's calendar is no longer consumed by administrative motion — it is consumed by judgment calls, relationship management, and the kind of coordination that keeps clients from leaving.

   If you have multiple roles touching the same constraint, repeat this process for each one. Compile the results into a single table: Role, Column B %, Loaded Cost, Annual Misallocation Cost. That table is the raw material for the Sprint design work in the chapters ahead.
   ```

**Drift findings for Chapter 2:**

1. **AS #2 SUBSTANCE DIFFERS.** Different first sentence/opening procedure ("Pick the role you flagged earlier. Think through what that person actually spends their week on" vs. appendix's "Take the role you picked earlier. List 10–15 tasks that person actually does in a typical week … Pull their calendar. Check their sent folder."). The "10–15 tasks / pull calendar / check sent folder" prescription has been REMOVED from the chapter prose but remains in the appendix. The illustrative-composite framing ("a Project Coordinator at a mid-sized firm. (This is an illustrative composite, not a specific client.)") in the chapter is also absent from the appendix's older phrasing.
2. **AS #3 minor.** Chapter uses "For the illustrative Project Coordinator:" — appendix uses "For the Project Coordinator example:". Cosmetic but not verbatim.
3. **AS #4 SUBSTANCE DIFFERS — TITLE AND CONTENT.** Chapter calls this Action Step "**Start Your Hybrid Split**" with a Human-Manages / Agent-Labors table plus a forward-reference to the TML framework in Chapter 5. Appendix calls it "**Describe the Hybrid Version**" with a one-paragraph "typical day" narrative ("Monday morning starts with reviewing agent-generated status reports …"). These are two different exercises that share only the underlying intent. The Hybrid Split table (chapter) is NOT in the appendix at all, and the "typical day" paragraph (appendix) is NOT in the chapter.

---

### Chapter 3 — The Framework (`chapters/03-the-framework.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L53:**
   ```
   Write down the constraint you'd solve first. One sentence. If it takes more than one breath to read aloud, it's too long. (You may not know your constraint yet — that's exactly what Signal in Chapter 4 is for. Write your best guess. Signal will sharpen it.) This is your draft Signal.
   ```

2. **L184:**
   ```
   Fill in a Sprint Planning Canvas for your company. Constraint in one sentence. One first-pass answer per stage. Name the Orchestrator. Book the review. A wrong first guess is better than a blank row — blanks stay blank, guesses get corrected.

   A blank Sprint Planning Canvas template — and the rest of the Compound resources library — will be available at *compound.co/resources* when it launches. Until then, copy the five-part structure into the tool of your choice.
   ```

3. **L205:**
   ```
   Pick your constraint. Fill in the Sprint Planning Canvas. Book the quarterly review. The Sprint is real when the review is on the calendar.
   ```

**Appendix entries for Chapter 3 (in order):**

1. **Appendix L98:**
   ```
   Write down the constraint you'd solve first. One sentence. If it takes more than one breath to read aloud, it's too long. This is your draft Signal — you'll sharpen it in Chapter 4.
   ```

2. **Appendix L103:** identical to chapter L184 wording (BUT without the second-paragraph "blank Sprint Planning Canvas template — and the rest of the Compound resources library" note).

3. **Appendix L108:** identical to chapter L205. No drift.

**Drift findings for Chapter 3:**

1. **AS #1 WORDING DIFFERS.** Chapter (L53) closes with a parenthetical: "(You may not know your constraint yet — that's exactly what Signal in Chapter 4 is for. Write your best guess. Signal will sharpen it.) This is your draft Signal." Appendix (L98) compresses to: "This is your draft Signal — you'll sharpen it in Chapter 4." Same intent, different sentence shape.
2. **AS #2 MISSING IN INDEX.** Chapter (L184) has a second paragraph announcing the resources library at *compound.co/resources*. The appendix entry omits this paragraph. Not just a wording fix — content is dropped.

---

### Chapter 4 — Signal (`chapters/04-signal.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L94:** "Pick your top three candidates. Run Is/Is Not on each. Then run Five Whys on the survivors. Cross off anything that traces to a market condition, a personality, or a problem you can't put a number on."
2. **L141:** "Open a whiteboard or shared doc. Spend twenty minutes listing candidates using the five questions above. No filtering, no debate about whether something belongs. Write everything down."
3. **L182:** "Fill in the one-page Constraint Statement template for your chosen constraint. Read it aloud to the team. If the room can't agree that this is the one constraint worth a Sprint, you're not done. Keep working until you have real agreement — the kind where people nod because the math convinced them, not because the meeting has gone long."
4. **L210:** "Pull your current issues list, your stalled rocks, and any open headcount requests. Pick the one that feels most expensive and run it through the five constraint questions. If you can put a real number on it, you have a constraint worth a Sprint. If you can't, keep walking the list."

**Appendix entries for Chapter 4 (in order):**

1. **Appendix L118:** identical to chapter L94. No drift.
2. **Appendix L123:** identical to chapter L141. No drift.
3. **Appendix L128:** identical to chapter L182. No drift.
4. **Appendix L133:** identical to chapter L210. No drift.

**Drift findings for Chapter 4:**

- **ORDER MISMATCH.** The chapter's natural reading order is: AS #1 (Is/Is Not + Five Whys, L94) → AS #2 (whiteboard candidates, L141) → AS #3 (Constraint Statement, L182) → AS #4 (issues list / stalled rocks, L210). The appendix lists them in the SAME order. **However**, the appendix ordering is arguably illogical: candidate surfacing (chapter L141 / appendix #2) precedes Is/Is Not + Five Whys (chapter L94 / appendix #1) in the actual Signal workflow. The chapter places the diagnostic Action Step (#1) inside the conceptual section on Is/Is Not, before the "How to run Signal yourself" section that introduces the surfacing exercise (#2). Both sources agree — but the order itself appears to be a manuscript ordering bug. Worth flagging but not a chapter↔appendix drift.

Otherwise: no wording drift. **Chapter 4 is the cleanest chapter in the audit.**

---

### Chapter 5 — Source (`chapters/05-source.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L64:** "Open the Constraint Statement from Signal. List every digital system that touches the constraint workflow. For each one, fill in all six columns — Source, Type, Owner, Status, Pipeline, Notes. Don't filter. If it touches the constraint, it goes on the map."
2. **L73:** "Name every person whose judgment the constraint workflow depends on. For each one, write specifically what they know that no system holds. Flag anyone who's a single point of failure."
3. **L85:** "Review your map from Pass 1 and Pass 2. Write down every gap — every question a designer would ask that your current sources can't answer. Add them to the map as Missing sources."
4. **L123:** "Review each source on your map. Mark whether it's structured or unstructured, durable or ephemeral, and which AI tier it belongs to — standing context, retrieved, or historical."
5. **L193:** "Identify the highest-risk organic source on your Knowledge Map — the person whose knowledge is most at risk of leaving. Schedule a structured interview this week. Ask: what decisions do you make that nobody else makes? Record it. Transcribe it. Add the output to the map."
6. **L247:** "Run the six-item completeness test against your Knowledge Map. Fix any gaps. Then put the Constraint Statement from Signal at the top of the page and the Knowledge Map below it. That one page is what you hand to Design."

**Appendix entries for Chapter 5 (in order):**

1. **Appendix L142:** identical to chapter L64. No drift.
2. **Appendix L147:** "Name every person whose judgment is load-bearing for the constraint. For each one, write specifically what they know that no system holds. Flag anyone who's a single point of failure." — **load-bearing** vs. **the constraint workflow depends on**.
3. **Appendix L152:** identical to chapter L85. No drift.
4. **Appendix L157:** identical to chapter L123. No drift.
5. **Appendix L162:** identical to chapter L193. No drift.
6. **Appendix L167:** identical to chapter L247. No drift.

**Drift findings for Chapter 5:**

1. **AS #2 WORDING DIFFERS.** Chapter (L73): "every person whose judgment the constraint workflow depends on". Appendix (L147): "every person whose judgment is load-bearing for the constraint". Same idea, different phrasing.

---

### Chapter 6 — Designing the System (`chapters/06-designing-the-system.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L86:** "Pick one accountability from your constraint workflow. Write down the information flow: what data comes in, from where, what happens to it, what goes out, to whom. Don't describe the role — describe the information. This is the foundation for everything Design produces."
2. **L145:** "For each accountability in your constraint workflow, place it on the AI-assisted-to-automated spectrum. Write down your rationale — not just the label, but why. 'AI-assisted because the exception rules aren't fully documented yet' is a rationale. 'AI-assisted' by itself is a checkbox."
3. **L200:** "Identify your Human Orchestrator candidate. Ask: does this person have authority over the constraint outcome? Are they willing to shift from executing to designing? Write down the name. If there's a development gap, name it — and plan the first Sprint as the ramp-up, not as a test they need to pass."

**Appendix entries for Chapter 6:** appendix L176, L181, L186 — identical wording to chapter prose in all three cases.

**Drift findings for Chapter 6:** None. **Clean.**

---

### Chapter 6b — Designing the Work (`chapters/06b-designing-the-work.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L30:** "List every task in the constraint workflow. Sort each one into the three TML categories — Task, Management, Leadership. Count the tasks in each bucket. If more than half land in **Leadership (Human Judgment Required)**, challenge each one: is this genuinely judgment, or is it judgment because nobody has written down the rules? The exercise takes sixty to ninety minutes for a real role. Do it on paper or in a shared doc."
2. **L99:** "Pick the workflow you're designing. Draw a swim lane diagram with two lanes — human and agent. Map every step. Count the handoff crossings. If the count is higher than the number of steps, redesign the handoffs before moving to Build."
3. **L151:** "Run the five-item Design Gate checklist against your current Sprint's design. If any item has a gap, that gap is your next working session — not your next Build discovery. Fix it now."

**Appendix entries for Chapter 6b:** appendix L195, L200, L205 — identical wording (note that appendix L195 drops the markdown **bold** around "Leadership (Human Judgment Required)" but otherwise verbatim).

**Drift findings for Chapter 6b:**

1. **AS #1 minor formatting.** Chapter bolds "**Leadership (Human Judgment Required)**"; appendix renders it without bold. Cosmetic only.

---

### Chapter 7 — Build (`chapters/07-build.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L62:** "Before your next Build, ask: does the builder need to be a developer, or does the builder need to be the person who knows the work? If the answer is the second, put them in front of the tool and let them build. Pair them with IT for access and security — not for construction."
2. **L105:** "Pull the designed workflow from Design. Run the three-question decision tree above. Write down which path you're on and why. If you can't answer the questions without guessing, Design isn't done — go back."
3. **L162:** "When a vendor or builder proposes fine-tuning, ask: 'Could we get the same result by giving the model access to our data at query time?' If the answer is yes, you've just saved weeks and thousands of dollars. Start with context windows for small datasets. Move to RAG when the data outgrows the window. Fine-tune only when neither gets you there."
4. **L243:** "Open a document. Write the eight section headers. Fill in Sections 1-3 from your Design artifacts — if you can't fill them without guessing, Design isn't done. Then complete Sections 4-8 using the Hybrid Accountability Chart and Knowledge Map. Every section must have content before the spec goes to a builder."
5. **L266:** "Walk through all seven items with the builder present. Check each one against the completed spec. Any item that can't be checked off is a gap that must be resolved before build begins."
6. **L299:** "Answer all seven questions in writing. Attach the answers to the Build Spec as a companion document. If any question can't be answered, the build is not ready to deploy — resolve the gap before going live."
7. **L336:** "Pull last week's real inputs. Run the full five-question test. Document the results. Fix any failures and retest. The test results are part of the Build handoff to Deliver."

**Appendix entries for Chapter 7 (in order):**

1. **Appendix L214:** identical to chapter L62.
2. **Appendix L219:** identical to chapter L105.
3. **Appendix L224:** "When a vendor or builder proposes fine-tuning, ask: 'Could we get the same result by giving the model access to our data at query time?' If the answer is yes, you've just saved weeks and thousands of dollars. **RAG first. Fine-tune only when RAG can't get you there.**"
4. **Appendix L229–245:** identical to chapter L243, L266, L299, L336 respectively.

**Drift findings for Chapter 7:**

1. **AS #3 SUBSTANCE DIFFERS.** Chapter (L162) prescribes a THREE-stage progression: "Start with context windows for small datasets. Move to RAG when the data outgrows the window. Fine-tune only when neither gets you there." Appendix (L224) collapses to a TWO-stage rule: "RAG first. Fine-tune only when RAG can't get you there." The "context window" tier — which appears in the chapter body's RAG / fine-tune / context-window discussion immediately above — is silently dropped from the appendix. This is the single biggest substantive drift in the audit.

---

### Chapter 8 — Deliver (`chapters/08-deliver.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L59:** "Pull up your Hybrid Accountability Chart from Design. List every person whose daily work changes because of this Sprint. For each one, confirm they've completed hands-on training — not a meeting, not an email. If anyone hasn't, that's your first task before deploy."
2. **L102:** "Pick one role from your Hybrid Accountability Chart whose handoffs changed. Write the three-column entry — input, output, escalation — in one sentence each. Be concrete: 'Reviews output' is not specific enough. 'Opens the quote draft in the shared folder, checks unit costs against the rate card, approves or flags within 4 hours' is."
3. **L144:** "Create the log template — four columns: Date, What happened, Category, What it signals — in whatever tool your team already uses. Name the person who owns it. Do this before you flip the switch, not after."
4. **L200:** "Go back to your Signal instrument. Copy the Constraint Statement and quantified cost exactly as written. Measure the same metric now — same unit, same timeframe, same source. Calculate the delta. Write the outcome in one sentence. No spin."

**Appendix entries for Chapter 8:** appendix L253, L258, L263, L268 — verbatim matches.

**Drift findings for Chapter 8:** None. **Clean.**

---

### Chapter 9 — Compound (`chapters/09-compound.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L49:** "Before the Sprint enters Build, put the Compound session on the calendar. A 90-minute block with the Human Orchestrator and every supervisor who owned a Sprint accountability. If it's not scheduled before the Sprint ships, it won't happen after."
2. **L106:** "After the retrospective, write the one design change on a card with four fields: what the change is, who installs it, how you'll know it's working, and the date it's installed by. If any field is blank, the change isn't specific enough."
3. **L144:** "At the end of the Compound session, update all three living documents before anyone leaves the room. Chart row made permanent, backlog re-ranked, Sprint outcome recorded in one sentence. Fifteen minutes. No exceptions."

**Appendix entries for Chapter 9:** appendix L277, L282, L287 — verbatim matches.

**Drift findings for Chapter 9:** None. **Clean.**

---

### Chapter 10 — The Rhythm (`chapters/10-the-rhythm.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L56:** "Put the quarterly operating session on the calendar for the end of this quarter. Book 90 minutes. Invite the leadership team. Set the agenda using the four steps above."
2. **L152:** "Create the Compounding Scorecard. Fill in the first row with your current Sprint. Tape it to the wall next to your accountability chart."

**Appendix entries for Chapter 10:** appendix L296, L301 — verbatim matches.

**Drift findings for Chapter 10:** None. **Clean.**

---

### Chapter 11 — What to Do Next (`chapters/11-what-to-do-next.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L37:** "If you haven't completed the AI Readiness Scorecard yet, go back to Chapter 1 and do it now. It takes ten minutes and tells you exactly where to start."
2. **L128:** "Decide which path you're taking. Write it down. If Path A, schedule the Signal session with your team this week. If Path B, book the Clarity Call. The decision that doesn't work is the one you defer."

**Appendix entries for Chapter 11:** appendix L310, L315 — verbatim matches.

**Drift findings for Chapter 11:** None. **Clean.**

---

### Appendix — Prompt Engineering (`chapters/appendix-prompt-engineering.qmd`)

**Chapter-prose Action Steps (in order):**

1. **L127:**
   ```
   Take your most recent agent interaction that produced disappointing output. Run the four-step diagnostic. Was the problem in the prompt, or in the context? If you don't have a Knowledge Map for the constraint the agent was working on, that's your answer — the context was never designed.
   ```

**Appendix entries for "Appendix — Prompt Engineering":** **NONE.**

**Drift findings for the Prompt Engineering appendix:**

1. **MISSING IN INDEX.** The Action Step Index does not include an "Appendix — Prompt Engineering" section. The single callout in `appendix-prompt-engineering.qmd` (L127) has no entry in `appendix-action-steps.qmd`. This accounts for the 49 vs. 48 count gap.

---

## Summary table

| Chapter | In-chapter count | In-index count | Drift findings |
|---|---|---|---|
| Preface | 0 | 0 | — |
| Ch 1 Diagnosis | 7 | 7 | 3 (1 substance, 1 wording, 1 minor wording) |
| Ch 2 Co-Operating Model | 4 | 4 | 3 (1 substance + title change, 1 substance, 1 minor) |
| Ch 3 The Framework | 3 | 3 | 2 (1 wording, 1 missing paragraph) |
| Ch 4 Signal | 4 | 4 | 0 (order is debatable but both agree) |
| Ch 5 Source | 6 | 6 | 1 (wording) |
| Ch 6 Designing the System | 3 | 3 | 0 |
| Ch 6b Designing the Work | 3 | 3 | 1 (cosmetic formatting only) |
| Ch 7 Build | 7 | 7 | 1 (substance — context window tier missing) |
| Ch 8 Deliver | 4 | 4 | 0 |
| Ch 9 Compound | 3 | 3 | 0 |
| Ch 10 The Rhythm | 2 | 2 | 0 |
| Ch 11 What to Do Next | 2 | 2 | 0 |
| Appendix — Prompt Engineering | 1 | **0** | 1 (missing entire entry) |
| **Total** | **49** | **48** | **12 findings** (1 MISSING, 0 EXTRA, 9 WORDING, 2 SUBSTANCE drift items above cosmetic threshold) |

### Drift category breakdown

- **MISSING IN INDEX:** 1 (Appendix — Prompt Engineering Action Step)
- **EXTRA / ORPHAN IN INDEX:** 0
- **SUBSTANCE DIFFERS** (different exercise, different worked example, different prescription): 3 — Ch 1 AS #7 (scorecard wrap-up), Ch 2 AS #2 (10-15 tasks / calendar instruction), Ch 2 AS #4 (Hybrid Split table vs. Hybrid Version paragraph), Ch 7 AS #3 (two-tier vs. three-tier data-access rule)
- **WORDING DIFFERS** (same exercise, sentence rewritten): 5 — Ch 1 AS #1, Ch 1 AS #2 (minor), Ch 2 AS #3 (minor), Ch 3 AS #1, Ch 5 AS #2
- **MISSING PARAGRAPH** inside an otherwise-matching entry: 1 — Ch 3 AS #2 (compound.co/resources note)
- **COSMETIC** (bold markup only): 1 — Ch 6b AS #1
- **ORDER MISMATCH:** 0 (the order question in Ch 4 is a chapter-internal issue, not chapter↔appendix drift)

## Recommended sync strategy

**Source of truth: chapter prose.** The chapter callouts are the canonical, edited text that Julie and the editorial team have already passed through. The appendix is an index — its purpose is to faithfully reproduce the in-chapter Action Steps in one scannable list. Where the appendix and chapter disagree, the appendix should be updated to match the chapter, NOT vice versa. The two notable substance drifts (Ch 2 AS #4 title + content, Ch 7 AS #3 context-window tier) both look like the chapter was revised after the appendix was authored — so the appendix is stale, not the chapter.

**Recommended fix list, ordered by impact:**

1. **ADD missing appendix entry (1 fix):** Add a new section to `appendix-action-steps.qmd` after "Chapter 11: What to Do Next" titled "Appendix: Prompt Engineering" and include the L127 Action Step verbatim. This restores the 49 = 49 count.
2. **UPDATE Ch 7 AS #3 in appendix (1 fix, highest substance impact):** Replace appendix L224's "RAG first. Fine-tune only when RAG can't get you there." with the chapter's "Start with context windows for small datasets. Move to RAG when the data outgrows the window. Fine-tune only when neither gets you there." This realigns the appendix with the three-tier (context window / RAG / fine-tune) framework the chapter actually teaches.
3. **REPLACE Ch 2 AS #4 in appendix (1 fix, second-highest substance impact):** Change the appendix title from "Describe the Hybrid Version" to "Start Your Hybrid Split" and replace the paragraph-narrative body with the chapter's Human-Manages / Agent-Labors two-column table prescription. Preserve the closing "If you have multiple roles touching the same constraint…" paragraph (it appears in both).
4. **UPDATE Ch 2 AS #2 in appendix (1 fix):** Replace appendix L57 opening ("Take the role you picked earlier. List 10–15 tasks that person actually does in a typical week — not what the job description says, what they do. Pull their calendar. Check their sent folder.") with the chapter L161 opening ("Pick the role you flagged earlier. Think through what that person actually spends their week on — the work as it happens, not the work as the job description writes it."). Also update "Project Coordinator at a professional services firm" to "Project Coordinator at a mid-sized firm. (This is an illustrative composite, not a specific client.)" to match chapter framing.
5. **UPDATE Ch 1 AS #7 in appendix (1 fix):** Replace appendix L42 (the "Before you turn the page" version) with the chapter L281 wording ("The scorecard is the input every other chapter references. Take an hour with your leadership team, ideally before your next L10, to score each dimension and write the scores down. Every chapter ahead will ask you to come back to them.").
6. **UPDATE Ch 1 AS #1 in appendix (1 fix):** Replace appendix L12's "If the answer is silence, that silence is the diagnosis." with the chapter's longer ending "If the room can't answer — if there's no scorecard, no number, no owner — that's your answer. There is no scorecard. And that's exactly the problem."
7. **UPDATE Ch 3 AS #1 in appendix (1 fix):** Replace appendix L98's "This is your draft Signal — you'll sharpen it in Chapter 4." with the chapter's "(You may not know your constraint yet — that's exactly what Signal in Chapter 4 is for. Write your best guess. Signal will sharpen it.) This is your draft Signal."
8. **ADD missing paragraph to Ch 3 AS #2 in appendix (1 fix):** Add the second paragraph from chapter L184 ("A blank Sprint Planning Canvas template — and the rest of the Compound resources library — will be available at *compound.co/resources* when it launches. Until then, copy the five-part structure into the tool of your choice.") to the appendix L103 entry.
9. **UPDATE Ch 5 AS #2 in appendix (1 fix):** Replace appendix L147's "every person whose judgment is load-bearing for the constraint" with chapter L73's "every person whose judgment the constraint workflow depends on".
10. **Minor copy fixes (2 fixes):** Ch 1 AS #2 "you've got" / "individually, not in a group" vs. appendix "you have" / "individually — not in a group"; Ch 2 AS #3 "For the illustrative Project Coordinator:" vs. appendix "For the Project Coordinator example:". Optional — fix while doing the larger sync.
11. **Cosmetic (1 fix, optional):** Restore the bold markup around "**Leadership (Human Judgment Required)**" in Ch 6b AS #1 in the appendix.

No REMOVE actions needed — there are no orphan appendix entries.
No REORDER actions needed — the appendix order matches the chapter order in all twelve chapters.

## Verdict

**12 distinct sync findings** across 7 of the 13 sources (the other 6 chapter/appendix files are clean). The drift is **predominantly minor wording**, but four findings — the missing prompt-engineering Action Step, the Ch 7 context-window tier deletion, the Ch 2 Hybrid Split/Hybrid Version mismatch, and the Ch 1 AS #7 scorecard-wrapup divergence — are substantive enough that an attentive reader who follows the index instead of the chapter will be operating against materially different instructions than the rest of the book teaches.

**Remediation effort estimate:** 30–45 minutes of focused editing. All fixes are localized to `chapters/appendix-action-steps.qmd`; no chapter prose changes required. Recommended pass order is the fix list above (highest impact first). After the edits, re-run a `grep "^## Action Step" chapters/*.qmd` to confirm the appendix count moves from 48 → 49, then do one quick spot-read of the Ch 2 and Ch 7 entries to confirm the substance drifts are gone.
