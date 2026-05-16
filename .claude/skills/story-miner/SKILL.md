---
name: story-miner
description: "Search Compound transcripts for stories, anecdotes, and case studies, then outline each using Vinh Giang's 3-Ingredients framework (Be Specific, Relive vs Report, Share the Meaning). Outputs structured story outlines with source references to .claude/output/ for human review and content reuse. Use when the user wants to mine transcripts for stories, find anecdotes for content, extract case studies, or build a story library."
---

# Story Miner

You search Compound's transcript library for stories worth retelling, then outline each one using Vinh Giang's 3-Ingredients storytelling framework. The output is a structured file the human reviews to decide which stories to develop for content.

## What this skill does

1. Takes a topic, theme, or content need from the user
2. Searches transcripts using `mcp__claude_ai_Compound_Qdrant__search_transcripts` and/or `mcp__claude_ai_ProHQ_Transcripts__Search_Transcripts_in_Typesense`
3. Identifies story candidates — anecdotes, case studies, examples, personal narratives, client transformations, metaphors-in-action
4. Outlines each story using Vinh Giang's 3-Ingredients framework
5. Recommends a story structure and tactics from the Storytelling Matrix
6. Saves output to `.claude/output/stories-{topic-slug}-{date}.md`

## What this skill does NOT do

- Does NOT write the final story. The outline is a skeleton for the human to develop.
- Does NOT fabricate details. Every claim traces back to a transcript passage.
- Does NOT decide which stories to use. The human picks from the mined set.
- Does NOT replace the storyteller's voice. The outline provides raw material; delivery is human.

## Inputs

Required:
- **Topic or theme** — what the stories should be about (e.g., "leadership under pressure," "first sprint results," "headcount math," "why companies fail at AI")

Optional:
- **Content format** — where the story will be used (e.g., "keynote talk," "LinkedIn post," "book chapter," "podcast episode"). Affects structure recommendations.
- **Number of stories** — how many to find (default: 5, max: 10)
- **Speakers to prioritize** — specific people whose stories matter most

If no topic is provided, ask for one. Do not mine without direction.

---

## MANDATORY EXECUTION RULES

- ALWAYS read `references/vinh-giang-3-ingredients.md` and `references/storytelling-matrix.md` before searching.
- ALWAYS run at least 3 different search queries to cover the topic from multiple angles (synonyms, adjacent concepts, specific vocabulary the speakers use).
- ALWAYS include the source transcript reference (title, speaker, timestamp/passage) for every story found.
- ALWAYS quote the key passage from the transcript that contains the story's core moment.
- NEVER invent details not present in the transcript. If sensory details aren't in the source, mark them as "[needs detail from speaker]" in the outline.
- NEVER skip the Meaning section. If the speaker didn't state the meaning explicitly, propose a candidate meaning and mark it "[inferred — verify with speaker]".
- ALWAYS save the output file to `.claude/output/` relative to the project root.

---

## Step 1 — Load the frameworks

Read both reference files:
- `references/vinh-giang-3-ingredients.md` — the primary outlining framework
- `references/storytelling-matrix.md` — for structure and tactic recommendations

## Step 2 — Design the search strategy

From the user's topic, generate 3-5 search queries. Think about:
- The topic stated directly
- Synonyms and adjacent concepts
- Specific Compound vocabulary (e.g., "Signal," "headcount math," "sprint," "constraint")
- Emotional moments (breakthroughs, failures, surprises, realizations)
- Concrete situations (client names redacted, specific workflows, before/after moments)

Example for topic "why companies fail at AI":
- "companies failed AI implementation"
- "bought tools no results"
- "AI investment wasted money"
- "transformation didn't work"
- "tool adoption failure"

## Step 3 — Search and collect

Run searches using:
- `mcp__claude_ai_Compound_Qdrant__search_transcripts` (semantic search — best for thematic queries)
- `mcp__claude_ai_ProHQ_Transcripts__Search_Transcripts_in_Typesense` (keyword search — best for specific phrases)

For each result, scan for **story signals**:
- A specific person, company, or situation being described
- A before/after or transformation arc
- A moment of realization, failure, or breakthrough
- Dialogue or quoted speech
- Concrete details (numbers, timelines, named tools, specific outcomes)
- Emotional weight — the speaker's voice changes, they slow down, they emphasize

Collect the raw passages. Group overlapping references to the same story.

## Step 4 — Outline each story

For each story candidate, produce this outline:

### Story Title (working title)

**Source:** [Transcript title / Speaker / Date or ID]
**Key Passage:**
> [Direct quote from transcript — the core of the story]

**Context:** [1-2 sentences: when/where this happened, who was involved]

#### Ingredient 1: Be Specific (Sensory Inventory)

For each sense, note what the transcript provides and what's missing:

| Sense | From Transcript | Needs Detail |
|-------|----------------|--------------|
| Sight | [what's described] | [what to ask speaker] |
| Sound | [what's described] | [what to ask speaker] |
| Smell | [if any] | [if relevant] |
| Touch | [if any] | [if relevant] |
| Emotion | [what's described] | [what to explore] |

**Strongest sensory anchor:** [the single most vivid detail available]

#### Ingredient 2: Relive vs. Report

**Current state:** Report / Partial Relive / Full Relive
**Present-tense rewrite of the core moment:** [1-2 sentences converting the key moment to present tense, as a model for the storyteller]
**Body/delivery note:** [any physicality or gesture the speaker used, or suggestion for delivery]

#### Ingredient 3: Share the Meaning

**Explicit meaning (from transcript):** [if the speaker stated the lesson]
**Inferred meaning:** [if not explicit — mark as "[inferred — verify with speaker]"]
**Bridge phrase draft:** "The reason I'm telling you this is because..."
**Audience relevance:** [why this meaning matters to the target audience]

#### Storytelling Matrix Recommendation

**Recommended structure:** [Linear / Listicle / Explainer / Problem-Solution / Comparative] — [why]
**Suggested tactics:** [1-2 tactics from the matrix] — [why]

#### QA Checklist

- [ ] Source transcript identified and passage quoted
- [ ] Story has a specific person/situation (not generic)
- [ ] At least 2 sensory details present or flagged for collection
- [ ] Core moment can be told in present tense (relive-ready)
- [ ] Meaning is stated or inferred and marked for verification
- [ ] No fabricated details — everything traces to source

---

## Step 5 — Compile and save

Compile all story outlines into a single markdown file. Include:

1. **Header** — topic, date, number of stories found, search queries used
2. **Story Index** — numbered list with working titles and one-line summaries
3. **Full Outlines** — one per story, in the format above
4. **Source Log** — all transcript references used, for audit

Save to: `.claude/output/stories-{topic-slug}-{YYYY-MM-DD}.md`

Report the file path and a brief summary to the user.

## Output Format

```markdown
# Story Mine: {Topic}

**Date:** {YYYY-MM-DD}
**Stories found:** {N}
**Search queries used:**
1. {query 1}
2. {query 2}
3. {query 3}
...

---

## Story Index

1. **{Working Title}** — {one-line summary} (Source: {transcript ref})
2. ...

---

## Story 1: {Working Title}

{full outline per Step 4 format}

---

## Story 2: {Working Title}

...

---

## Source Log

| # | Transcript | Speaker | Passage Used | Story # |
|---|-----------|---------|-------------|---------|
| 1 | {title} | {speaker} | {brief desc} | 1, 3 |
| 2 | ... | ... | ... | ... |
```

## Quality Gate

Before saving, verify:

- [ ] At least 3 search queries were run
- [ ] Every story has a quoted transcript passage with source reference
- [ ] Every story has all 3 Vinh Giang ingredients addressed (even if some are "[needs detail]")
- [ ] Every story has a meaning — explicit or inferred-and-marked
- [ ] No fabricated details — everything traces to a transcript
- [ ] QA checklist completed for each story
- [ ] File saved to `.claude/output/`
- [ ] File path reported to user
