# Ch 5 (Signal) — Outline v2 (re-conception)

**Source file:** `chapters/04-signal.qmd` · **Branch:** edits/fine-tuning
**Problem:** the chapter teaches Signal TWICE (a conceptual pass, then a procedural "Run Signal yourself" pass) with heavy redundancy, plus a redundant second framework. Author: "super poorly written… throwing spaghetti at the wall." Same disease as ch3/ch4, worse.

---

## Root cause (why it reads as spaghetti)

1. **Two passes at the same material.** First half (L1–152): concept + Five Whys + stories + template. Second half "Run Signal yourself" (L153–340): re-teaches the session, candidate-surfacing, Five Whys AGAIN, plus a *separate* "five constraint questions."
2. **Duplicated tools/points:** Five Whys taught at L89 and again L234; "most candidates are symptoms" at L91 and L236; candidate-surfacing as "4 patterns" (L71) and again as "Issue Surfacer questions" (L182); the **"five constraint questions" (L269) are just the Constraint Statement fields** (problem/where/how-long/cost/what-changes) presented as a second tool.
3. **Example whiplash:** SuperWebPros → Julie food-safety → Meridian → PT clinic → Meridian → PT-clinic-template → Meridian (surfacer) → Meridian (applied) → Meridian (five questions). No transitions; reader loses the thread.
4. **Voice:** the "weather" analogy (author scrapped it; appears twice), an AI-sounding cost paragraph, three separate EOS bridges, a confusing O'Donnell callout, "hand to Source" (abstraction).

## Thesis / job of this chapter

Teach the reader to run **one Signal session** that produces **one validated Constraint Statement** (one sentence + a dollar number). Follow the book's house pattern and the author's own instruction: **hook → concept → roadmap of the session → step-by-step how-to → ONE worked example carried through.** One pass. Each tool once. Each example once, with a clear job.

---

## The clean spine (one pass, linear)

### I. In Brief [KEEP, light]

### II. Hook — SuperWebPros project coordinator *(L8–16)* [KEEP, de-AI]
The L10 scorecard-blank story. Lands: name the constraint, not the symptom. Fixes: cut the "felt like weather" line; de-AI the "what is this costing us" paragraph (author: "sounds like AI"); keep the capacity-vs-capability-vs-redesign turn.

### III. What Signal is, and what it produces [CONSOLIDATE L18–57]
Merge the "dollar number," "deliverable," and "gate" sections into one concept section:
- Signal produces ONE artifact: the **Constraint Statement** — one anchoring sentence + where it lives + how long + the **dollar number** + validating evidence. Show the anchoring-sentence structure ("[Function] cannot [outcome] because [root cause], which costs [X] per [Y]").
- Why **one** (focus the Sprint — author: it's about focusing the Sprint, not deleting the backlog; the backlog persists).
- Why the **number** (worth-a-Sprint test + Deliver target + names the **opportunity cost** / ensures you solve important problems — author add).
- Signal is a **gate** (don't move to Source until it's locked). State the gate-lock condition ONCE (currently said twice).
- **Julie food-safety** as the brief illustration: trace to root revealed a matrix/authority structure, not bad leaders — and replacing them would have been *more expensive* (retrain, ramp, same bump). [author insight L24]

### IV. The core idea — trace the symptom to the structural constraint [CONSOLIDATE L59–129]
- Symptoms are visible; constraints are structural. (Cut the second "weather" line.)
- **Where constraints hide** — ONE consolidated lens-set (merge the "4 patterns" L71 + the "Issue Surfacer questions" L182): recurring unresolved conversations, workarounds, sausage-making, turnover, new-hire confusion, the headcount reach. Frame as "the first places to look," not exhaustive (author note).
- **PT clinic** as the vivid worked illustration of symptom-vs-constraint (the "almost opened a 6th location / nobody knew the efficiency number / the real constraint was scheduling" story). Used ONCE, here. (Its Constraint Statement can be the populated template example later, or here — see decision C.)

### V. The how-to — run the Signal session [RE-ORDER: roadmap then steps]
Per the author's instruction (roadmap then details, like Framework/Co-Op Model):
- **Roadmap first:** the `run-signal-session` moves block (the registered spine) — the session's steps in order, up top.
- Then **each step walked once, in order:**
  1. **Assemble the room** (who's in it; facilitator; no time budget).
  2. **Surface the candidates** (the lenses from §IV applied live; the Issue Surfacer worksheet table). Sub-note: *If you run EOS / Scaling Up*, the candidates are already on the board (Issues list, stalled rocks, the headcount conversation) — the one EOS bridge, consolidated.
  3. **Trace each to root — the Five Whys** (NAME the tool; walk it concretely; the stop rule: land on workflow/handoff/gap, not a person; push past the person to the structure). ONE Five Whys treatment. O'Donnell callout reworded: "Issue and constraint identification is hard work; Mark O'Donnell's *Issues!* is an excellent field guide."
  4. **Pick among the survivors** (the tiebreaker rubric: foundation-first, highest pain, smallest gap, owner-in-room, two-quarter horizon).
  5. **Quantify and write the Constraint Statement** — the **template IS the five questions** (collapse them; do not teach "five constraint questions" as a separate framework). Include the four cost-estimation formulas (hours/deals/margin/speed). One template appearance.
  6. **Lock it** (lever test + restate test; read it back; the room agrees).
  7. **Check the failure modes** (the 7-item checklist, once — fold the dominant-personality failure here).
- **Meridian carried through** these steps as THE worked example: the surfacer table → Five Whys result → tiebreaker → the completed Constraint Statement. In ONE place, in order (merge the scattered Meridian fragments L81/L201/L252/L296).

### VI. Activity is not Signal *(L342–346)* [KEEP, tight]
Skipping Signal looks like activity (demos, Slack prompting), not failure. One tight section.

### VII. Hand off to Source [FIX abstraction L348–356]
"Hand to Source" → concrete: the locked Constraint Statement goes onto the **Sprint Planning Canvas** (the Constraint row + the first Sequence row), and the **Sprint Lead** carries it into Source, which opens with the dollar number already written. (Author: "source has no hands; say it plainly; show it on the canvas.")

### VIII. Reflection Questions [REWRITE]
Re-pitch to the new structure (the author stopped reading these; redo).

---

## Key consolidations (the redundancy cull)
- **One Five Whys** (merge L89 + L234).
- **Collapse the "five constraint questions" into the Constraint Statement** — same fields; one tool.
- **One candidate-surfacing lens-set** (merge 4 patterns + Issue Surfacer questions).
- **One Constraint Statement template** appearance.
- **One EOS bridge** for Signal (currently IDS at L53 + "EOS calls this Identify" at L109 + the EOS/Scaling-Up section at L219 → consolidate to the EOS/Scaling-Up surfacing note + a single Signal≈deeper-IDS line).
- **Meridian once**, carried through the how-to.
- Cut the whole "two passes" structure → one linear pass.

## Voice / specific note fixes
- Kill "weather" (L12, L67). De-AI the L10 cost paragraph.
- "insisting on one" → "insisting on one *constraint*" (L40); reframe "refuse the list" → focus the Sprint (backlog persists).
- The number also names **opportunity cost** (L44).
- "the seat is rarely the root… how do we know?" (L109) → support/soften the claim.
- O'Donnell callout rewrite (L109).
- "Four patterns… not exhaustive" → "first places to look" (L71).
- "hand to Source" → Canvas + Sprint Lead (L350/356).
- Replacement-costs-more insight (L24).

## Examples — proposed placement (DECISION C)
- **SuperWebPros** (Jesse) — hook.
- **Julie food-safety** — one-paragraph "structure, not the person" illustration in §III.
- **PT clinic** — the single vivid symptom→constraint story in §IV (+ its populated Constraint Statement as the worked template, once).
- **Meridian** — the carried-through worked example in §V (the session steps).
Each appears once, with a distinct job, no bouncing. (Alternative: drop PT clinic to lighten; but it's a strong story and earns one slot.)

## Diagrams
Keep the existing ch04 excalidraws (constraint-statement-template, symptom-to-constraint, five-whys-chain, efficiency-gap, constraint-path, five-signal-questions) — but several map to consolidated sections; verify which survive. The `five-signal-questions` diagram likely retires (questions collapse into the Constraint Statement). Confirm during draft; file a diagram bead for any that need redraw.

## Process registry
`run-signal-session` (worksheet ships as `signal`) stays the canonical spine; the moves block becomes the roadmap at the top of §V. Verify the registry step labels still match after the re-order.

## Open decisions for the author
- **A.** Merge the two passes into one linear spine (concept → roadmap → step-by-step). *(Recommended.)*
- **B.** Collapse the "five constraint questions" into the Constraint Statement (one tool, not two). *(Recommended.)*
- **C.** Example placement (SWP hook / Julie structure-not-person / PT clinic the symptom-story / Meridian carried-through) — keep all four, each once? Or drop PT clinic?
- **D.** EOS bridges down to one consolidated touch. *(Recommended.)*

## Notes
- Net effect: materially shorter, one pass, linear. The chapter has good raw material; the work is sequencing + de-duping, not new content.
- Full pipeline after drafting: voice-scan + deflourish + render, then voice-scanner / prose-craft / editorial-coherence.
