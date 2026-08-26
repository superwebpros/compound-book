---
deliverable: amazon-kdp-listing
book: Co-Intelligent Co-Operation
authors: Jesse Flores, Julie Mann
date: 2026-08-26
status: draft — awaiting author sign-off
purpose: Copy-paste-ready KDP metadata for the pre-order listing
sources_of_truth:
  - _quarto.yml (title/subtitle currently shipping)
  - index.qmd (preface — author credibility, core diagnosis)
  - .claude/skills/compound-design-system/uploads/positioning-brief (2).md
  - _julie/voice-charter.md (vocabulary + anti-patterns this copy obeys)
---

# Amazon KDP Listing — *Co-Intelligent Co-Operation*

Everything below is written to paste directly into KDP. Character counts are
measured against the real KDP limits (title + subtitle < 200 combined;
description ≤ 4,000 including HTML tags; 7 keyword slots × 50 characters).

All copy obeys `_julie/voice-charter.md`: contractions throughout, no
forbidden vocabulary (`transformation`, `leverage`, `cutting-edge`,
`organizational design` in operator context, `unlock`/`discover`), no
exclamation marks, no emoji, no rhetorical triplets, em-dashes only where
nothing else works.

---

## 1. Title and subtitle

### Recommended

| Field | Copy |
|---|---|
| **Title** | `Co-Intelligent Co-Operation` |
| **Subtitle** | `How to Build the Human + AI Company: An AI Operating Model That Grows Revenue Without Growing Headcount` |

**Why this and not what's in `_quarto.yml` today.**
The shipping subtitle is *"How to build the Human+AI Company of the
Future...Today"*. It reads well on a cover and does nothing on Amazon. It
carries one searchable term (`AI`), spends its second half on a time
construction nobody types into a search bar, and the ellipsis reads as a
typo in a search-results list. Since the main title is a coined brand term
with effectively zero organic search volume, the subtitle has to carry the
entire keyword load. This one does: `AI`, `AI operating model`, `Human + AI`,
`company`, `revenue`, `headcount`.

It also runs the two-beat reveal the positioning brief locked. Beat one is
the vernacular a CEO already uses (`operating model`, `revenue`,
`headcount`). Beat two is the branded category sitting above it in the title.

### Alternates

**A — Agent-forward.** Trades the revenue promise for the fastest-rising
search term in the category.

> `How to Build the Human + AI Company: An Operating Model for Putting AI Agents to Work Inside Your Business`

**B — Audience-forward.** Targets "AI for business owners" and "AI for small
business" query patterns directly.

> `The AI Operating Model for Business Owners: How to Redesign the Work So Your Team and AI Agents Grow Revenue Together`

### Two things to hold

1. **Whatever you pick has to match the cover.** KDP requires title and
   subtitle to match the cover text. Changing the subtitle here means
   re-cutting `assets/cover.png` and updating `_quarto.yml` in the same pass.
2. **Don't pad it further.** Amazon rejects and de-lists for keyword
   stuffing in the title field. Every alternate above is one clean promise,
   not a keyword list.

---

## 2. Book description

Paste as raw HTML into the KDP description field. KDP does not give you a
visual editor there, and it strips `<img>` and `<a>`.

```html
<h4>Your company bought AI. Your operating model never changed.</h4>

<p>You paid for the subscriptions. Somebody ran a pilot. Maybe you hired a consultant or sent the team to a training. Two years in, three people are using three different tools, nobody coordinates, and revenue per employee sits exactly where it was.</p>

<p>That's not an AI problem. It's an operating problem.</p>

<p>AI arrives inside a company the same way a new employee does. It's looking for a seat, a scope, a set of handoffs, and the information it needs to do the work. In most companies the work was never explicitly designed, so there's no seat for AI to take. That's why the tools are running and the structure hasn't moved.</p>

<p><b>Co-Intelligent Co-Operation</b> is the field manual for designing the work first. It's a framework, not a tool review. Run it and you bend one number: revenue per employee, the cleanest measure of whether your team is producing more without you hiring more.</p>

<h4>What's inside</h4>

<ul>
<li><b>The AI Readiness Scorecard.</b> Twenty questions across five dimensions, scored to one percentage that tells you how ready your operating model actually is and where the work will hurt.</li>
<li><b>The six-stage Sequence.</b> Signal, Source, Design, Build, Deliver, Compound. Every stage gets its own chapter, its own deliverable, and its own gate you have to clear before moving on.</li>
<li><b>The Compound Sprint.</b> The unit of work that takes one real constraint from diagnosis to a shipped system your team uses on Monday morning.</li>
<li><b>The Hybrid Accountability Chart.</b> The artifact that names who owns which decision when half the workflow is a person and half is an agent.</li>
<li><b>Two worked case studies.</b> A 27-person metal fabrication shop that took quote turnaround from 3.8 days to 4.2 hours, and a real five-agent team that absorbed a $24,000-a-year coordinator role at roughly a quarter of the cost.</li>
<li><b>Worksheets, prompts, and per-role runbooks</b> you can run without hiring anybody to run them for you.</li>
</ul>

<p>Jesse Flores builds AI systems inside operating companies and teaches AI-driven systems and organizational design at Michigan State University. His own software company went from thirteen people to eight without losing capacity. Julie Mann was Global CHRO at a global food safety company when it absorbed a Fortune 500 division and expanded across 44 countries overnight. Twenty years of leading people functions taught her the same lesson: the way work actually moves is never what the org chart shows.</p>

<p>This book won't teach you prompting and it won't predict the future of work. It shows you how to find the one constraint worth a sprint, put a dollar figure on it, design the work around it, build the thing that fixes it, and then do it again so each sprint makes the next one faster.</p>

<p>If you run a company somewhere between 25 and 150 people, and the math of adding people to solve problems has stopped working, start here.</p>

<p><b>Stop transforming. Start compounding.</b></p>
```

### Notes on the choices

- **The first two lines are the whole ballgame.** Amazon truncates at
  "Read more" on mobile after roughly two lines. The `<h4>` hook and the
  first sentence are built to survive that cut on their own.
- **No MIT statistic.** The positioning brief leads ads with "95% of AI
  pilots fail." It's a strong line and it's deliberately *not* here: the
  book never cites it, and a description should represent what's between the
  covers. It belongs in ads and A+ content, not the description field.
- **Revenue per employee is the hook** because it's the book's actual spine
  (Chapter 1's Headcount Paradox) and because it's the number this buyer
  already argues about with their CFO.
- **Numbers are load-bearing and real.** 3.8 days to 4.2 hours, $24,000,
  thirteen to eight, 44 countries. All traceable to the manuscript.
- **"Stop transforming. Start compounding."** is the approved tagline, which
  is the one sanctioned use of the otherwise-forbidden `transform` family.
- **Length: 3,079 characters with the HTML, ~487 visible words.** That's
  longer than the 150–250 words usually recommended for nonfiction, and it's
  deliberate: this buyer is Problem Aware at market-sophistication level 3,
  so the mechanism has to be visible before the claim lands. The bullet stack
  carries the skim. If you want it shorter, cut the two paragraphs between
  the author bio and the closing line first. Nothing above the bullets should
  move.

---

## 3. Backend keywords (7 slots, 50 characters each)

Rules applied: spaces not commas (commas waste ~10–15% of capacity), no
quotation marks, no `free`/`bestseller`/`gift`, no competitor book titles,
long-tail phrases a real buyer would type, and no duplication of words the
title or subtitle already index.

One deliberate exception to that last rule: `ai` appears in slot 1. Repeating
a title word normally wastes characters, but `ai agents` is a two-word phrase
with its own query volume, and phrase-level matching is worth three
characters. Every other slot is clean of subtitle vocabulary.

| # | Keyword string | Chars | Targets |
|---|---|---|---|
| 1 | `ai agents for small business owners` | 35 | The highest-volume query the subtitle doesn't already cover |
| 2 | `workflow automation process improvement` | 39 | Ops buyers who don't search "AI" at all |
| 3 | `business systems and processes for founders` | 43 | Systems-and-planning browsers |
| 4 | `change management adoption playbook` | 35 | The HR/ops side of the buying committee |
| 5 | `scaling a business without hiring more staff` | 44 | The pain, phrased the way it gets typed |
| 6 | `future of work automation for mid market ceo` | 44 | Category browsers plus the buyer's own title |
| 7 | `agentic workflows knowledge management guide` | 44 | Rising technical queries the book genuinely serves |

### Optional swaps (higher reward, higher risk)

Use these only if you're comfortable with the trade-off. Both are common
practice and both sit closer to Amazon's line on brand names in metadata.

- **Slot 1 →** `chatgpt claude copilot at work for business` (43). Product
  names of tools the book actually discusses. Big volume. Amazon
  discourages brand names in keyword fields, so this is a judgment call.
- **Slot 4 →** `eos entrepreneurial operating system scaling` (44). This is
  exactly who the book is for and the manuscript speaks EOS fluently
  (Chapter 13 maps Signal onto IDS). "Entrepreneurial Operating System" is
  EOS Worldwide's mark, so it carries some risk. `entrepreneurial operating
  system` in a keyword field is widely used and rarely enforced against,
  but it's your call, not mine.

---

## 4. Categories (pick 3, chosen per format)

KDP no longer takes BISAC codes for Amazon-exclusive titles. You pick from
Amazon's own store tree in the dashboard, and each format gets its own
three. Strategy: one best-fit niche you can realistically badge in, one
complementary angle for a different audience, one broader node for
algorithmic reach.

| Slot | Category | Why |
|---|---|---|
| 1 (niche) | Business & Money → Management & Leadership → Systems & Planning | Closest true fit. Badge-winnable. This is literally what the book is. |
| 2 (complement) | Business & Money → Processes & Infrastructure → Operations Research | Catches the ops buyer who isn't shopping for an AI book |
| 3 (broad) | Computers & Technology → Artificial Intelligence → Business | Where AI browsers actually are; broad reach node |

Node names drift between the Kindle and print trees, so confirm the exact
paths in the dashboard rather than trusting this table verbatim. If Slot 1
turns out to be crowded on the day, `Small Business & Entrepreneurship →
Entrepreneurship` is the next best niche.

---

## 5. About the Author (Amazon Author Central)

Nonfiction conversion leans on credibility, and this field renders on the
product page. ~90 words.

```text
Jesse Flores builds AI systems inside operating companies. He runs Compound, where he installs the Co-Operating Model with mid-market CEOs, and he teaches AI-driven systems and organizational design at Michigan State University. His own software company went from thirteen people to eight without losing capacity.

Julie Mann spent twenty years leading people functions, most recently as Global CHRO at a global food safety company that absorbed a Fortune 500 division and expanded across 44 countries overnight. She's seen the same pattern in nearly every company she's worked in: the way work actually moves is never what the org chart shows.
```

---

## 6. Pre-order mechanics worth knowing before you set this up

- **KDP pre-orders are Kindle-only.** Paperback and hardcover through KDP
  get a release date, not a pre-order button. If a print pre-order matters
  to the launch, that has to come through IngramSpark.
- **You can schedule the Kindle release up to 12 months out.** Release date
  is in GMT.
- **Price only ever moves down for early buyers.** Lower the list price
  during pre-order and Amazon retroactively charges the lower price to
  everyone who already ordered.
- **One free 30-day slip.** You get a single no-penalty delay of the release
  date. Missing the date after that costs you pre-order privileges for a
  year, so set the date you can actually hit.
- **Keep the description evergreen.** No "pre-order now," no dates, no
  launch-week language. It's the same field after release, and time-bound
  promotional copy is what gets descriptions flagged.

---

## 7. What still needs a decision

1. Which subtitle. Everything downstream (cover, `_quarto.yml`, keyword
   slots that avoid subtitle words) depends on it.
2. Whether to take the two optional keyword swaps.
3. Whether print pre-order matters enough to route through IngramSpark.
