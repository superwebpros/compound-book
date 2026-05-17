# AI Tells — Reference Library

Source: Wikipedia's "Signs of AI writing" guide (Project AI Cleanup, 2025), plus widely-discussed expansions from third-party summaries.

This is descriptive, not prescriptive. These patterns are tells — they often appear in AI-generated prose, but they also appear in human writing. Flag patterns that weaken the draft. Don't flag single-instance use of common words.

## How to use this file

When scanning, walk each category in order. For each category:

1. Look for the listed phrases or structural patterns.
2. Count occurrences.
3. Decide FLAG vs SKIP based on whether the pattern is weakening this specific draft.

When in doubt, lean toward SKIP. Over-flagging trains the writer to ignore the report.

---

## 1. Inflated symbolism and meaning

AI exaggerates a topic's importance by tying it to broad themes, legacy, history, or spirit. Often promotional in flavor.

**Phrases to watch:**

- stands as a testament to
- serves as a testament to
- is a testament to
- plays a vital role / plays a significant role
- plays a pivotal role
- underscores its importance
- continues to captivate
- leaves a lasting impact / lasting impression
- watershed moment
- key turning point
- deeply rooted in
- profound heritage
- steadfast dedication
- solidifies its place
- cements its status
- enduring legacy
- has captured the imagination

**Why it's a tell:** these phrases substitute generic gravitas for specific information.

**Rewrite direction:** replace with a concrete claim or cut. If the surrounding text already makes the point, delete the inflated sentence. If the point is important, replace with the specific reason it matters.

---

## 2. Promotional / tourism-brochure language

AI writes about places, cultures, products, and people in admiring, advertising-adjacent prose. Often slips through even with neutral prompts.

**Phrases to watch:**

- rich cultural heritage
- rich history
- rich tapestry
- rich cultural tapestry
- breathtaking
- must-visit / must-see / must-try
- stunning natural beauty
- enduring legacy / lasting legacy
- vibrant (community, scene, culture)
- bustling (city, market, hub)
- nestled (in / between / among)
- a true gem
- hidden gem
- world-class
- unparalleled
- a feast for the senses

**Why it's a tell:** reads like travel copy or marketing — not analysis.

**Rewrite direction:** replace with specifics. "Bustling market" → "the market handles ~3,000 vendors daily." "Rich cultural heritage" → name the specific traditions, events, or artifacts. Or cut.

---

## 3. Editorializing / signposting opinion

AI adds interpretation or commentary even when neutral tone is requested. The most common form is framing phrases that tell the reader how to feel about what follows.

**Phrases to watch:**

- it's important to note (that)
- it's worth noting (that)
- it is worth mentioning
- it should be noted
- it's worth considering
- it bears mentioning
- no discussion would be complete without
- it would be remiss not to mention
- in this article
- as we have seen / as we will see
- one cannot overstate
- it goes without saying

**Why it's a tell:** these phrases add no information and frame the next fact as somehow noteworthy by author fiat.

**Rewrite direction:** almost always cut the framing phrase. If "It's important to note that X" is the sentence, just say X.

---

## 4. Section-ending summaries / wrap-ups

AI loves to close sections with a recap, even when the section was short enough that no recap is needed.

**Phrases to watch:**

- In summary,
- In conclusion,
- Overall,
- To sum up,
- All things considered,
- Taken together,
- In short,
- Ultimately, (when used to signal a concluding take rather than a logical "ultimately")

**Why it's a tell:** they signal "essay structure" rather than thought structure. Tight prose doesn't need them.

**Rewrite direction:** usually cut the transition word and start the next sentence with the substance. If the wrap-up sentence itself is redundant, cut the whole sentence.

---

## 5. Overuse of conjunctive adverbs

Transitions help writing flow, but AI relies on a narrow set and uses them densely. Multiple instances of the same handful of connectors per page is the tell.

**Phrases to watch:**

- however
- moreover
- furthermore
- in addition
- additionally
- on the other hand
- in contrast
- notably
- importantly
- consequently
- therefore (when used as filler)

**Why it's a tell:** these aren't bad words — they're just over-used. AI scaffolds paragraphs with them; humans usually don't need most of them.

**Rewrite direction:** count occurrences in the draft. If more than one per ~200 words on average, flag the densest cluster. Most can be deleted with no loss — sentences usually flow without the connector. Replace some with conjunctions ("but," "and," "so") or simple sentence breaks.

---

## 6. Negative parallelism ("not X, but Y")

The single most-flagged structural tell. AI loves the "It's not just X — it's Y" rhythm.

**Patterns to watch:**

- "It's not [X], it's [Y]."
- "It's not just [X], it's [Y]."
- "This isn't [X] — it's [Y]."
- "More than [X], it's [Y]."
- "Not only [X], but also [Y]."
- Two-sentence form: "X. However/But, Y." (when set up to deliver a contrast punch)

**Examples:**

> "It's not just about the beat — it's about the atmosphere."
> "He came from a theatrical family. However, his path intertwined personal ambition and family complexity."

**Why it's a tell:** the structure manufactures a pseudo-insight by setting up a contrast. Often the X and Y aren't actually opposites — the structure just makes them sound profound.

**Rewrite direction:** rewrite as a direct claim. "It's not just about the beat; it's about the atmosphere" → "The atmosphere matters more than the beat." Or, if the contrast is fake, cut the X half and just state Y.

---

## 7. Superficial analyses with "-ing" tags

AI tacks on a participial phrase at the end of a sentence that pretends to analyze the preceding clause.

**Tag words to watch (often at clause-end):**

- ensuring...
- highlighting...
- emphasizing...
- reflecting...
- showcasing...
- underscoring...
- demonstrating...
- making it (a / one of the)...
- solidifying...
- cementing...

**Example:**

> "Consumers can use their preferred wallet at participating merchants, improving convenience."

The "improving convenience" tag adds nothing — the main clause already implies it.

**Why it's a tell:** the tag offers commentary disguised as analysis. Frequently it just restates the implication of the main clause.

**Rewrite direction:** cut the participial tag in most cases. If the tag carries real information, promote it to a full clause with a specific claim.

---

## 8. Vague attribution / weasel wording

AI frequently attributes claims to unnamed authorities. Sometimes called "weasel words." Can also slip in when the writer has fed AI a stack of sources and the AI is hedging.

**Phrases to watch:**

- industry reports (suggest / indicate)
- observers have cited / observers note
- some critics argue
- experts say / experts believe
- it has been suggested
- many believe / many argue
- studies show (without a specific study)
- research has shown (without a citation)
- analysts say
- it is widely accepted that

**Why it's a tell:** the prose sounds informed and authoritative but cites no one in particular. Often the "experts" are one source, or none.

**Rewrite direction:** either name the source (preferred) or drop the attribution and state the claim as a direct observation. If neither is possible, the claim might not belong in the draft.

---

## 9. Excessive boldface

AI bolds for emphasis far more than human writers, often bolding section headers within paragraphs, product names, or "key terms" in every paragraph.

**Patterns to watch:**

- Bold every product or proper noun
- Bold the first phrase of most paragraphs
- Bold "key terms" sprinkled through prose
- Bold inside bullet lists where bolding adds no hierarchy

**Why it's a tell:** human prose uses bold sparingly. Heavy bolding looks like AI structure-imitating-headings.

**Rewrite direction:** keep bolding for genuine hierarchy (true headings, key labels). Strip the rest. If the draft would read fine without the bold, remove the bold.

---

## 10. Em dashes where commas or parentheses would do

Em dashes aren't an AI invention — humans use them often. The tell is the density and the substitution pattern.

**Patterns to watch:**

- Em dash where a comma would work cleanly
- Em dash where parentheses would work cleanly
- Multiple em dashes per paragraph
- Em dashes setting off short asides that don't need them

**Example:**

> "The product — released in March — sold quickly."

Could just as easily be: "The product, released in March, sold quickly." Or with parens.

**Why it's a tell:** AI defaults to em dashes for any aside. Mixed usage (some commas, some parens, some em dashes) reads more human.

**Rewrite direction:** swap some em dashes for commas or parentheses. Keep em dashes for genuine dramatic interruption or where the aside is long enough to need the strong visual break. Don't replace all of them — that overcorrects.

---

## 11. Bullet points with bolded titles that restate themselves

AI loves bullet lists where each bullet starts with a bolded label, then a sentence that just rephrases the label.

**Pattern:**

> - **Scalability:** The system is designed to scale across different use cases.
> - **Efficiency:** Improves efficiency by streamlining workflows.
> - **Flexibility:** Built with flexibility in mind.

The label and the sentence carry the same information.

**Why it's a tell:** real bullet lists either (a) have labels with sentences that add specifics, or (b) skip the labels and just state the points. The AI version does neither.

**Rewrite direction:** either drop the bold labels and let the sentences stand, or keep the labels and rewrite the sentences to add specifics. If neither works, the bullet list itself may be padding.

---

## Other patterns worth noting

These show up in third-party expansions of the Wikipedia guide but aren't always called out as named categories. Flag them when they appear:

- **Rule of three everywhere** — every list has exactly three items, every sentence has three parallel clauses. AI defaults to triplets; humans vary.
- **Uniform sentence length** — every sentence the same length, every paragraph the same size. Indicates structural autopilot.
- **Lack of specifics** — no names, dates, numbers, or examples. Generic claims throughout. Wikipedia's editors note that this often pairs with the promotional tone.
- **"In today's world" / "In an era of" intros** — generic scene-setting that adds nothing.

These are softer signals — flag when they compound with other tells, not in isolation.

---

## Severity guidance

When deciding HIGH / MEDIUM / LOW confidence:

- **HIGH** — the phrase or pattern is on the core list above, appears in a context where it's clearly weakening the writing, and a specific rewrite obviously improves it. Examples: "stands as a testament," "it's important to note," "not just X, it's Y" used twice in a row.
- **MEDIUM** — the pattern is present and the rewrite improves it, but a reasonable writer might leave it. Single "moreover" in an otherwise tight paragraph; one em-dash that could be a comma.
- **LOW** — borderline; only worth flagging because it compounds with other tells, or because the writer specifically asked for a thorough scan.

If the whole draft is dense with HIGH-confidence tells, lead with those in the report and group the rest. Don't bury HIGH issues under a wall of LOW noise.
