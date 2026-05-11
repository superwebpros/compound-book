# Compound — Design System

> **Stop transforming. Start compounding.**
>
> The visual + content system for Compound: organizational design for AI, run as a permanent operating layer. Editorial-direct-response. Warm dark, not cold dark. Operators talking to operators.

---

## Index

| File / Folder | What it is |
|---|---|
| `README.md` | This file. Brand context, content fundamentals, visual foundations, iconography. |
| `SKILL.md` | Skill manifest — usable as an Agent Skill in Claude Code. |
| `colors_and_type.css` | Token layer + semantic CSS vars + element defaults. Import this in any artifact. |
| `assets/` | Logos (wordmark + mark), brand SVGs. Copy into your artifact, never link from here cross-project. |
| `fonts/` | Font notes. (Webfonts loaded from Google Fonts CDN — see substitution flag below.) |
| `preview/` | Small HTML cards rendered in the Design System tab. One sub-concept per card. |
| `ui_kits/website/` | Hi-fi recreation of compoundorg.com — JSX components + an interactive index.html. |

### Sources

- **Brand Guide** (canonical, status: refreshed 2026-05-03 against Locked Bones 2026-04-29 + brochure direction 2026-05-02). Pasted in full at the top of this engagement.
- **Logo reference:** `uploads/69f270cc1cc228095.png` — black field, cream wordmark, carbon atom replacing the "O", red nucleus.
- **Superseding context:**
  - Compound HQ → KnowledgeBaseArticle/69f273a3aa2540e88 — Locked Bones (2026-04-29 alignment): black/red/cream + carbon-atom mark; movement-building rejected; direct-response register
  - Operator's Brief brochure draft (2026-05-02) — directional reference for typography, palette warmth, editorial-direct-response register
  - `_bmad-output/campaigns/compound-launch/positioning-brief.md` (lastVerified 2026-04-30)

These source documents are not in this project's filesystem. The summary above + the brand guide pasted in this engagement are the working canon.

---

## Brand at a glance

- **Name:** Compound
- **Domain:** compoundorg.com
- **Tagline:** *Stop transforming. Start compounding.* (in service; under review for paid placements)
- **Mission:** Help companies redesign how their people and teams work alongside AI — so every role, workflow, and result *compounds* instead of accumulating.
- **Archetype:** The Operator (primary) / The Sage (secondary). Not the Magician. Not a movement.
- **Adjectives:** Direct. Confident. No-BS. Wise. Empowering.

### What we are NOT
Elite consultants selling $500K strategy decks. Tech vendors selling a platform. AI trainers teaching prompt engineering. Tech bros hyping the future. Doomsayers. **A movement.** (Movement-building was explicitly rejected in the 2026-04-29 alignment.)

### The Compound Sequence
**Signal → Source → Design → Build → Deliver → Compound** — six stages, always all six, always in order, always with arrows. The six electrons in the carbon-atom mark map 1:1 to the six stages.

---

## Content Fundamentals

### Voice
Direct, Confident, No-BS, Wise, Empowering. **Operator-to-operator** — same vocabulary as a CEO peer, sharper cadence, less hedge, more claim. The earlier "measured peer-philosopher" register has been retired.

### Tone register — old vs new

| Old register | New register |
|---|---|
| "Most companies that have invested in AI have nothing to show for it." | "You bought the tools. You sent someone to a training. Nothing changed." |
| "We help companies redesign how their people work alongside AI." | "We redesign the company around the AI it actually uses." |
| "Consider the organizational design problem." | "It's not a tool problem. It's an operating problem." |

### Pronouns / address
- **You** to the reader. Always. Never "one" or "users."
- **We** for Compound when speaking institutionally. Founders speak in first person on LinkedIn (Jesse / Julie) — the brand account amplifies.
- Never "our customers" / "our clients." They are **operators**, **members**, **the room**.

### Casing
- **Headlines:** sentence case. Period at the end of complete sentences. (`Stop transforming. Start compounding.`) No title case.
- **UI labels / buttons:** sentence case. ("Book the diagnostic call.")
- **Mono meta labels:** UPPERCASE with letter-spacing (`01 / SIGNAL`, `OPERATOR'S BRIEF`, `MAY 2026`).
- **Italics in headlines:** retired. Default emphasis = **red rule underline** (`<em>` renders as ink word with a red rule beneath, ~0.09em thickness). Secondary = **highlighter block** (`.hit-block` — solid red field, ink text, once per page max). Italics are not used in headlines.

### Punctuation
- Periods on headlines. Em-dashes — used freely — are part of the editorial rhythm. Oxford comma. No exclamation marks.
- The Compound Sequence always written with arrows: `Signal → Source → Design → Build → Deliver → Compound`.

### Emoji
**No.** Never. Emoji breaks the editorial-direct-response register and signals the wrong category (LinkedIn-influencer / startup-bro). Use mono-label markers (`01/`) and weight-contrast emphasis instead.

### Numbers, stats, and data
Mono labels. Specific. Anti-slop — never a stat that isn't load-bearing. "If your largest operational constraint costs $150K+ per year, the first sprint pays for the year." > "Save up to 40% on AI costs!"

### CTA library

| Use | Words |
|---|---|
| **Default** | "Book the diagnostic call." |
| Soft (LinkedIn / blog) | "Read the Operator's Brief." / "Read the article." / "Watch the short." |
| Hard (paid / direct response) | "What's your largest operational constraint costing you per year? If $150K+, the first sprint pays for the year." |
| **Forbidden** | ~~"Learn more"~~ ~~"Discover"~~ ~~"Find out how"~~ ~~"Schedule a demo"~~ |

### Forbidden words (full list)
Transformation / Transformative · Leverage · Synergy · Alignment (the meeting kind is fine) · AI-powered · Cutting-edge · Revolutionary · Augmentation · Hybrid (alone — only inside "Hybrid Org Today") · Movement / Join us / Revolution · **"Organizational design" in headlines** (it's the internal category descriptor, not the buyer's pain word).

### Approved signature phrases
- "Stop transforming. Start compounding."
- "Organizational design for AI" (internal only)
- "Signal → Source → Design → Build → Deliver → Compound"
- "The Hybrid Org Today" — the living artifact every member updates
- "Operator's Brief" — internal/insider format signal
- "Headcount math" — Persona 2's pain framing
- "You can see where AI is going. You just don't yet know how to operate inside it." — validated hero line

### Structural moves (the brochure DNA)
1. **Lead with a diagnosis the buyer can nod at.** Then mechanism. Then proof.
2. **Mono labels frame the artifact.** `01 / SIGNAL`, `02 / SOURCE`. Treat the page like an Operator's Brief, not a marketing site.
3. **One sentence, one beat — full sentences, not staccato fragments.** Em-dashes do the work that bullet lists usually do.
4. **Red rule carries the load.** Wrap the emphasized word in `<em>` for a red underline; reach for `.hit-block` once per page when you need a hero moment. Sparingly.
5. **Red is the mechanism, not the brand.** The nucleus, the word, the urgency. Used everywhere, it loses its load.

---

## Visual Foundations

### Palette philosophy — warm dark, not cold dark
The differentiator is the cream-white ink (`#F2EDE4`) on warm near-black (`#0A0A0A`). Pure white on pure black reads cold and SaaS-default; resist it. Red (`#E11D2D`) is the mechanism — the word that does the work, the nucleus, the urgency moment. Used everywhere, red loses its load.

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#0A0A0A` | Default background |
| `--bg-deep` | `#000000` | True black — hero / max-contrast moments |
| `--ink` | `#F2EDE4` | Primary text |
| `--ink-dim` | `#A8A39A` | Secondary text, captions, meta |
| `--rule` | `#1F1E1B` | Borders, dividers |
| `--red` | `#E11D2D` | Primary accent — nucleus, emphasis, CTAs |
| `--red-bright` | `#FF2A3C` | Hover states, urgency moments |

**Dropped:** Deep Blue `#1E3A5F`, Green `#059669`. Anything still carrying these is stale.

### Three-field system — paper · cream · dark

Compound runs **three fields**, not a "dark mode" toggle. Each section commits to one. Alternating fields is how the page gets editorial rhythm — like flipping pages of a magazine. Pick the field by the *job*, not by aesthetic preference.

| Role | **Paper** (canvas) | **Cream** (callout band) | **Dark** (gravitas band) |
|---|---|---|---|
| Background | `--field-bg` `#FAFAF8` | `--field-bg` `#F2EDE4` | `--field-bg` `#0A0A0A` |
| Background-deep | `--field-bg-deep` `#F2EDE4` | `--field-bg-deep` `#E8E1D3` | `--field-bg-deep` `#000000` |
| Ink (primary) | `--field-ink` `#0A0A0A` | `--field-ink` `#0A0A0A` | `--field-ink` `#F2EDE4` |
| Ink (dim) | `--field-ink-dim` `#5A554C` | `--field-ink-dim` `#5A554C` | `--field-ink-dim` `#A8A39A` |
| Rule / border | `--field-rule` `#E8E6E1` | `--field-rule` `#D9D2C2` | `--field-rule` `#1F1E1B` |
| Surface (cards) | `--field-surface` `#F2EDE4` | `--field-surface` `#EBE5D8` | `--field-surface` `#131211` |
| Logo + mark | `logo-compound-dark.svg`, `logo-compound-mark-dark.svg` | `logo-compound-dark.svg`, `logo-compound-mark-dark.svg` | `logo-compound.svg`, `logo-compound-mark.svg` |
| Use for | Articles, sequence detail, body copy, forms, **homepage default** | **One section per page max.** Featured callout, brief preview, testimonial band, sequence summary | Hero, founder quote, footer, section breaks, anywhere the page needs gravitas |

**Red (`--red #E11D2D`) is constant across all three fields.** That's the load-bearing rule — only the field flips around it.

#### Why paper-warm white and not pure white

Same reasoning that picked cream over white originally — applied at the right scale. Pure white (`#FFFFFF`) at 100% luminance on a full-screen canvas is a flashbulb in the afternoon office, especially for the 40+ operator audience. Paper-warm (`#FAFAF8`) cuts the harshness without going so warm it reads "dated paper." It signals *publication* — `Financial Times` web, `The Browser`, `Stripe Press` — rather than SaaS dashboard or Squarespace template.

#### Why cream is no longer the canvas

Cream-as-canvas tested clean at the level it was first evaluated — single-card previews, short prototype pages, 720px-tall mocks. It broke at scale: once a real homepage composed (nav + hero + sequence + brief + articles + footer = 100+ screens of scroll) with cream as the canvas, the warmth became oppressive and signalled "dated paper" rather than "publication." For the 40+ operator audience this read more "Squarespace template" than `Financial Times`. Cream is now correctly scoped to a **callout band** — one per page max — where its warmth is a feature, not a fatigue source.

> **Going-forward test for any new field:** before committing a chosen light field, mock a real page with **5+ screens of scrolling body copy** in that field. The eye accepts warmth in a single 720px card and rejects it at 4096px+ of scroll. A scaled mock catches the failure mode that a preview card hides.

#### When to use which

- **Paper** — default canvas. Anywhere the user sits to read body copy or fill something out: article body, Sequence detail, cohort application form, marketing-page text sections, the homepage as a whole.
- **Cream** — the callout band. **One per page max.** Use for a featured testimonial, a brief callout, a sequence summary band, a "what this is" inset — the slot Kajabi fills with sage-green or soft-gray bands. Warmth without going dark.
- **Dark** — gravitas band. Hero, founder quote, footer, section breaks, anywhere the headline carries the weight. Editorial-direct-response gravitas lives here.

#### Mechanism (CSS)

Apply `data-field="paper"`, `data-field="cream"`, or `data-field="dark"` on a section's root element. The `[data-field="..."]` rules in `colors_and_type.css` flip the `--field-*` token group locally; descendants styled with `var(--field-bg)` / `var(--field-ink)` / etc. recolor automatically. **Never use raw `var(--bg)` or `var(--ink)` on anything inside a section that needs to flip** — always use the `--field-*` family. Logo + mark must be swapped in JSX based on the same field prop (`logo-compound-dark.svg` for paper + cream, `logo-compound.svg` for dark).

#### Don't

- Don't use cream for body copy or any long-scroll section. That's what paper is for.
- Don't put two cream callout bands on the same page.
- Don't invent intermediate fields (no "warm gray" middle ground).
- Don't gradient between fields.
- Don't combine fields within a single section.
- Don't change `--red` between fields.
- Don't use pure white anywhere — paper is the chosen light.

### Typography

| Role | Family | Use |
|---|---|---|
| Display | **Archivo Black (800)** | Headlines, hero, section titles. Heavy geometric grotesque. Emphasis = weight contrast (drop word to 500). |
| Body | **Bricolage Grotesque** | Long-form, body, UI labels. |
| Mono | **JetBrains Mono** | Meta labels (`01/02/03`), numerals, code, technical signals. |

**Pairing logic:** Archivo Black display + Bricolage Grotesque body + JetBrains Mono meta = *editorial direct-response, sans edition*. Heavy display sans survives screen-print, embroidery, favicons, and low-res placements where serifs collapse. **Emphasis is carried by weight contrast, not italics** — drop the load-bearing word from 800 → 500 (or wrap in `<em>` which is restyled as weight-500). Italics are no longer the primary mechanism.

> **Substitution flag:** all three families load from Google Fonts CDN. Self-host into `/fonts` and swap to `@font-face` if licensing requires. **Action for user:** confirm whether to self-host.

> **Why we moved off Instrument Serif:** the Didone-style hairlines didn't survive small sizes, screen-print, or embroidery. Archivo Black holds up across the production-asset surface (t-shirts, pins, low-res favicons) without losing the editorial-direct register.

### Spacing
4px base scale: `--space-1 (4)` → `--space-11 (192)`. Editorial layouts breathe — default vertical rhythm between sections is `--space-9 (96)` or larger. Empty space is content.

### Backgrounds
- **Default:** flat `--bg` (`#0A0A0A`). Texture comes from type, not from background gradients or noise.
- **Hero / lockup moments:** `--bg-deep` (`#000`) for maximum-contrast moments.
- **No gradient meshes. No glassmorphism. No subtle radial glows.** The brochure works because it trusts the reader.
- The only "glow" allowed is `--shadow-glow-red` on a primary CTA when a hover state needs to mark urgency — and even that is optional.

### Imagery
- **Photography:** documentary-direct. Operators in their environment. **No stock**. If it looks like a McKinsey hero, it's wrong.
- **Diagrams:** Excalidraw or hand-rendered, not polished vector. The imperfection of the line is the point.
- **Charts / tables:** dense, mono-labeled, low-chrome.
- **Avoid:** isometric illustrations, gradient meshes, glassmorphism, AI-generated stock-feel imagery, anything that reads "tech startup 2024."
- **Color of imagery:** when used, photography is warm-dark. Black-and-white or desaturated-warm tones preferred. Never cool-blue corporate stock.

### Borders, rules, dividers
Hairline 1px in `--rule`. Borders define editorial structure (operator's-brief grids), they don't decorate. **No double borders. No glow borders.** A border that needs to be noticed is a border doing too much.

### Shadows
Dark UIs read shadow as fog. Use almost never.
- `--shadow-1` — tiny darken-below for raised cards on `--surface-2`.
- `--shadow-2` — modal / floating panel only.
- `--shadow-glow-red` — primary CTA hover, optional. Otherwise, **flat**.

### Corner radii
Restrained. Editorial, not bubbly.
- `--radius-1` (2px) — buttons, tags
- `--radius-2` (4px) — inputs, small cards
- `--radius-3` (8px) — large cards (max)
- `--radius-pill` — only for status pills / mono numeric chips

**No 16px+ rounding.** Compound is not a fintech app.

### Cards
Flat surface (`--surface-1`), 1px hairline border in `--rule`, 24–32px padding, `--radius-2` or `--radius-3`. No shadow by default. Hover = border shifts to `--ink-dim` or `--red`, never elevation.

### Transparency / blur
**Almost never.** No frosted-glass nav. No backdrop-filter overlays. The exception: a fixed top nav over a long page can use a 90% `--bg` background — but no blur. Trust the flat surface.

### Hover states
- **Text links:** underline color shifts from `--rule` to `--red`. No color change on the text itself.
- **Buttons (primary):** `--red` → `--red-bright`. No size change.
- **Buttons (secondary):** border shifts from `--rule` to `--ink`. Background stays.
- **Cards:** border shifts to `--ink-dim`. No translateY. No shadow bloom.

### Press states
- **Buttons:** background darkens by ~8% via filter or via a `:active` token. No scale-down. No shrink.
- Cards do not have a press state — they navigate on click without feedback. The destination is the feedback.

### Animation
- **Duration:** `--dur-fast` (120ms) for hovers, `--dur-base` (200ms) for state transitions, `--dur-slow` (360ms) for page-level reveals only.
- **Easing:** `--ease-out` for enter, `--ease-inout` for symmetric transitions. No bounce. No spring overshoot. Editorial, not playful.
- **No fade-in-on-scroll waterfalls.** They're a tic. If a section needs to land, type lands it.

### Layout rules
- **Max content width** for long-form: `--content-w` (960px) or `--content-w-narrow` (640px) for body copy.
- **Gutter:** `clamp(20px, 4vw, 56px)`.
- **Mono meta labels** sit above headlines as eyebrows, with `letter-spacing: 0.16em`, in `--ink-dim` or `--red`.
- **Section markers** (`01 / SIGNAL`) are part of the layout grid — not decorative — when the page is structured as an operator's brief.

### Fixed elements
- Top nav, when present: 64px tall, `--bg` (NOT `--bg-deep`), 1px bottom border in `--rule`. No blur.
- Footer: editorial, multi-column, mono section labels. Black field with cream type. Not full-bleed images.

---

## Iconography

### Approach
Compound has **almost no decorative icons**. The brand's iconographic load is carried by:

1. **The carbon-atom mark itself** — the only icon that is fully designed and meaningful. (See `assets/logo-compound-mark.svg`.) Use it as favicon, avatar, pin, hat, shirt, app icon. The meaning travels with it.
2. **Mono numeric labels** (`01/`, `02/`, `→`) for sequential structure.
3. **The arrow `→`** — the only "icon" allowed in body copy. It's how the Compound Sequence is written.
4. **Lucide** — for any UI affordance that genuinely needs a glyph (close, external link, chevron, search, menu). Stroke 1.5–1.75px, never filled. Loaded from CDN — see usage below.

### Why Lucide (substitution flag)
Compound's source materials don't ship a custom icon set. Lucide is the closest match to the brand's restraint: thin stroke, geometric, neutral. Documented as an explicit substitution. **Action for user:** if Compound has a sanctioned icon set, drop SVGs into `assets/icons/` and we'll switch.

### Lucide usage
```html
<!-- CDN, no install -->
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<i data-lucide="arrow-right" style="width:16px;height:16px;stroke-width:1.75;color:var(--ink)"></i>
<script>lucide.createIcons();</script>
```

- Stroke width: **1.75** for body-size; **1.5** for large hero icons. Never bolder than 2.
- Color: `currentColor` — inherit from the parent. Never red unless it's *the* red moment.
- Size: 16px (inline), 20px (button), 24px (nav), 40px+ (feature). No filled variants.

### Emoji
**Never.** Not in headlines, not in CTAs, not in mono labels, not in social copy. Emoji is one of the things on the buyer's "you sound like everyone else" allergen list.

### Unicode
The arrow `→` (U+2192) is approved and load-bearing — it carries the Compound Sequence. The em-dash `—` (U+2014) is the editorial spacer. Avoid bullet `•` in marketing pages — use mono numerics (`01/`) or em-dashes instead.

### Logos available

| File | Use |
|---|---|
| `assets/logo-compound.svg` | Full wordmark with embedded atom mark. Default lockup. |
| `assets/logo-compound-mark.svg` | Atom-only mark, cream + red on dark. Avatars, favicons, decorative. |
| `assets/logo-compound-mark-dark.svg` | Atom-only mark, black + red on light. Reverse contexts. |

The wordmark is built as inline SVG with type rendered as paths-via-text — at production scale, swap for an outlined-paths version cut from Adobe Caslon Pro Bold or whatever Compound's brand owner has approved. Documented as a placeholder weight; **action for user:** confirm wordmark font for production export.

---

## Caveats — read these

- **Wordmark typography is approximate.** The reference raster shows a heavy condensed sans-serif wordmark; without access to the source vector or the brand owner's confirmation of the cut, the SVG uses a generic heavy sans (`Inter Tight 900`). Production logo files should replace this.
- **Webfonts are CDN-loaded.** Drop self-hosted files into `/fonts` and swap the `@import` if licensing requires it.
- **Lucide is a substitution.** No sanctioned icon set exists in source.
- **No live codebase, no Figma.** The UI kit (`ui_kits/website/`) is built from the brand guide + brochure direction. It's a faithful interpretation of the system, not a copy of an existing site. If compoundorg.com is live, point me at it and I'll align.
- **Imagery is placeholders.** No documentary photography in source. Real operator photos go in once shoots happen.
