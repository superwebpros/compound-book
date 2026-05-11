---
name: compound-design
description: Use this skill to generate well-branded interfaces and assets for Compound, either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines, colors, type, fonts, assets, and UI kit components for prototyping.
user-invocable: true
---

Read the README.md file within this skill, and explore the other available files.

If creating visual artifacts (slides, mocks, throwaway prototypes, etc), copy assets out and create static HTML files for the user to view. If working on production code, you can copy assets and read the rules here to become an expert in designing with this brand.

If the user invokes this skill without any other guidance, ask them what they want to build or design, ask some questions, and act as an expert designer who outputs HTML artifacts _or_ production code, depending on the need.

## Quick orientation

- **Tagline:** *Stop transforming. Start compounding.*
- **Voice:** Direct, Confident, No-BS, Wise, Empowering. Operator-to-operator.
- **Palette:** warm dark — `--bg #0A0A0A`, `--ink #F2EDE4`, `--red #E11D2D`. Never pure white on pure black.
- **Three fields, not dark mode** — every section commits to **paper** (canvas — articles, body, forms, homepage default), **cream** (callout band — one section per page max, fills the slot Kajabi uses for sage-green / soft-gray bands), or **dark** (gravitas — hero, founder quote, footer). Red is constant across all three. Magazine-spread rhythm, not page-level toggle. See *Three-field system* below.
- **Type:** Archivo Black 800 (display) · Bricolage Grotesque (body) · JetBrains Mono (meta).
- **Red rule carries the load** (default). Highlighter block secondary, once per page. Mono labels frame the artifact. Red is the mechanism, not the brand.
- **Forbidden:** transformation, leverage, AI-powered, synergy, movement, emoji.
- **Default CTA:** "Book the diagnostic call."

## Three-field system

Compound runs three fields. Pick one per section; never per-page. Pick by *job*, not aesthetic preference.

|  | **Paper** (canvas) | **Cream** (callout band) | **Dark** (gravitas) |
|---|---|---|---|
| `--field-bg` | `#FAFAF8` (paper-warm) | `#F2EDE4` (warm cream) | `#0A0A0A` (warm near-black) |
| `--field-bg-deep` | `#F2EDE4` | `#E8E1D3` | `#000000` |
| `--field-ink` | `#0A0A0A` | `#0A0A0A` | `#F2EDE4` |
| `--field-ink-dim` | `#5A554C` | `#5A554C` | `#A8A39A` |
| `--field-rule` | `#E8E6E1` | `#D9D2C2` | `#1F1E1B` |
| `--field-surface` | `#F2EDE4` | `#EBE5D8` | `#131211` |
| Logo + mark | `logo-compound-dark.svg`, `logo-compound-mark-dark.svg` | `logo-compound-dark.svg`, `logo-compound-mark-dark.svg` | `logo-compound.svg`, `logo-compound-mark.svg` |
| Use for | Articles, body copy, forms, homepage default | **One per page max.** Featured callout / testimonial / brief preview band | Hero, founder quote, footer, section breaks |

**Red stays the same in all three fields.** That's the load-bearing rule — `--red #E11D2D` is the constant; the field flips around it. Pure white is never used; paper-warm is the chosen light because (a) 100% luminance is a flashbulb in the afternoon office for the 40+ operator audience, (b) warmth signals *publication* rather than SaaS dashboard, (c) it gives red room to breathe on light fields. Cream is the *callout band*, not a long-form reading surface — at 4096px+ of scroll its warmth becomes oppressive.

**Mechanism (in code):** every component takes a `field` prop that becomes `data-field="paper"`, `data-field="cream"`, or `data-field="dark"` on its root. The CSS rules `[data-field="..."] { ... }` (in `colors_and_type.css`) flip the `--field-*` tokens locally. Style with `var(--field-bg)`, `var(--field-ink)`, etc. — never `var(--bg)` directly inside a section that needs to flip. See `ui_kits/website/index.html` for the working pattern + presets.

**Don't:** do not use cream for body copy or any long-scroll section (that's paper's job), do not put two cream callout bands on the same page, do not invent intermediate fields, do not gradient between them, do not change red between fields, do not use pure white.

**Test for new fields:** before committing a chosen light field, mock 5+ screens of scrolling body copy in that field. The eye accepts warmth at one card and rejects it at full-page scroll.

## File map

| | |
|---|---|
| `README.md` | Brand canon — content fundamentals, visual foundations, iconography. **Start here.** |
| `colors_and_type.css` | Token layer + element defaults. `@import` from any artifact. |
| `assets/logo-compound.svg` | Full wordmark + atom. |
| `assets/logo-compound-mark.svg` | Atom-only mark (cream + red on dark). |
| `assets/logo-compound-mark-dark.svg` | Atom-only mark (black + red on light). |
| `fonts/README.md` | Webfont substitution notes. |
| `preview/*.html` | Small spec cards — Type, Colors, Spacing, Components, Brand. |
| `ui_kits/website/` | Marketing-site recreation. JSX components + interactive `index.html`. |
