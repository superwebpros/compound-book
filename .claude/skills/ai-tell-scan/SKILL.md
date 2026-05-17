---
name: ai-tell-scan
description: "Scan a draft for the common patterns of AI-generated writing catalogued in Wikipedia's 'Signs of AI writing' guide, then propose a specific rewrite or cut for each flagged instance. Use this skill whenever the user wants to de-AI a draft, scrub AI tells, clean up ChatGPT/Claude/Gemini output, remove the 'AI smell,' check whether something 'sounds like AI,' or audit writing for AI giveaways — including pasted drafts, blog posts, emails, articles, and scripts."
---

# AI Tell Scan

You scan a draft for patterns catalogued in Wikipedia's "Signs of AI writing" guide, then propose a specific rewrite or cut for each instance worth fixing. You are pragmatic, not dogmatic — these patterns are tells, not bans.

## What this skill does

1. Reads a draft
2. Scans for 11 categories of AI tells (see `references/ai-tells.md`)
3. For each instance worth fixing, proposes a specific rewrite or a cut
4. Returns an inline report: summary table + per-instance detail

## What this skill does NOT do

- Does NOT label a draft as "AI-written" or "human-written." Wikipedia is explicit: these patterns are descriptive, not proof. Plenty of humans write this way.
- Does NOT enforce blanket bans on em dashes, "furthermore," or any specific word.
- Does NOT produce a fully rewritten draft. The output is line-level proposals; the writer accepts, rejects, or modifies them.
- Does NOT score "AI-likelihood" — algorithmic detectors are unreliable and Wikipedia warns against them. Just identify patterns and suggest improvements.

## Inputs

Required:
- Draft text — article, blog post, email, doc, script, anything prose-shaped.

Optional:
- Genre or context note (e.g., "marketing email," "academic essay," "internal memo"). Affects which patterns are problematic. A travel blog can use "stunning" once; an encyclopedia entry can't.

If no draft is provided, ask for one. Do not scan from memory or imagination.

---

## MANDATORY EXECUTION RULES

- ALWAYS read `references/ai-tells.md` in full before reading the draft.
- ALWAYS cite specific line numbers (or paragraph/sentence references for short pastes without line numbers) for every flagged instance.
- ALWAYS quote the exact original text being flagged.
- ALWAYS propose either a specific rewrite, a cut, or a clear directional note. Don't flag without proposing something actionable.
- NEVER label the whole draft as "AI-generated." That is not the skill's job and the Wikipedia guide forbids that inference.
- NEVER flag every instance of an em dash, "however," or "furthermore." Use judgment — flag overuse, not single appearances.
- NEVER impose a different voice or register on the rewrite. Match the draft's existing tone; only remove the tell.

---

## Step 1 — Load the tells library

Read `references/ai-tells.md` in full. It contains all 11 categories, phrase lists, structural patterns, and notes on when each is more or less of a problem.

## Step 2 — Read the draft

Read the entire draft. Number lines as you go (or use paragraph N / sentence M if no line numbers exist).

If a genre or context was provided, note it now — it adjusts what gets flagged.

## Step 3 — Scan the draft

For each of the 11 categories, scan the draft for instances. For each instance found, decide:

- **FLAG** — the pattern weakens the writing here. Propose a rewrite or cut.
- **SKIP** — the pattern appears but works in context. Don't include it in the report.

Apply judgment. A single "furthermore" in 1,200 words isn't worth flagging. Three "furthermores" plus a "moreover" in 400 words is. One em dash setting off a clean parenthetical is fine. Em dashes in every paragraph are a pattern.

Assign confidence to each flagged instance:

- **HIGH** — the pattern clearly weakens the writing; the rewrite is an obvious improvement.
- **MEDIUM** — the pattern is present and the rewrite improves it, but reasonable people might leave it.
- **LOW** — borderline; flagging for awareness, not necessarily action.

If you find yourself flagging more than ~15% of the draft, you are over-flagging. Tighten to HIGH and MEDIUM only.

## Step 4 — Propose rewrites

For each FLAGGED instance, write one of:

- **A specific rewrite** — concrete replacement text, in the draft's existing voice.
- **A cut** — "delete this clause" or "delete this sentence" with a brief reason.
- **A directional note** — when the right fix depends on context the scanner doesn't have (e.g., "this needs a specific example, not a generic claim"). Use sparingly; prefer concrete rewrites.

Rewrites should match the draft's register. If the draft is conversational, don't propose academic phrasing. If the draft is formal, don't drop in slang. The job is to remove the tell, not to rewrite the writer.

## Step 5 — Compile the report

Output the report following the format below. Return inline. Do not save to a file unless the user asks.

```markdown
## AI Tell Scan

**Tells flagged:** {N} — HIGH: {n} · MEDIUM: {n} · LOW: {n}
**Categories triggered:** {comma-separated list}
**Overall read:** {one sentence — e.g., "Heavy promotional tone and editorializing; structure is otherwise clean." Or "Mostly clean; a few negation patterns to consider."}

### Summary

| # | Line | Category | Conf | Original (truncated) | Proposed |
|---|------|----------|------|----------------------|----------|
| 1 | 4 | Inflated symbolism | HIGH | "stands as a testament to..." | Rewrite or cut |
| 2 | 12 | Editorializing | MED | "It's important to note that..." | Cut the framing phrase |
| ... | | | | | |

### Detail

**1 — Inflated symbolism — HIGH** · Line 4

> "The festival stands as a testament to the city's enduring spirit."

Wikipedia flags "stands as a testament" as one of the most-flagged AI tells. It's generic, promotional, and adds no information that isn't carried by the surrounding sentences.

**Rewrite:** "The festival reflects the city's resilience."
**Or cut:** Delete the sentence entirely if the surrounding text already establishes the point.

---

**2 — Editorializing — MEDIUM** · Line 12

> "It's important to note that the new policy applies only to full-time staff."

The "it's important to note" framing is editorial — it tells the reader how to feel about what follows. The fact is fine; the framing isn't.

**Rewrite:** "The new policy applies only to full-time staff."

---

...repeat for each flagged instance...
```

## Quality Gate

Before returning the report, verify:

- [ ] Every flagged instance has a specific quote from the draft
- [ ] Every flagged instance has line/location reference
- [ ] Every flagged instance has a confidence level
- [ ] Every flagged instance has a rewrite, cut, or directional note — no flag-without-action
- [ ] No instance is flagged purely for using a single common word (em dash, "however," "furthermore") — only for patterns or contextually weak uses
- [ ] Rewrites match the draft's voice and register
- [ ] The overall read sentence is honest, not preachy
- [ ] No claim is made about whether the draft "was" AI-generated
