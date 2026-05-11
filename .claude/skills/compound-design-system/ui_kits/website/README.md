# UI Kit — compoundorg.com (marketing site)

A hi-fi recreation of the Compound marketing site, built from the brand guide + brochure direction. No live codebase or Figma was provided — this is a faithful interpretation of the system, not a copy of an existing site.

## Files

- `index.html` — interactive demo. Top nav, hero, the Compound Sequence, an Operator's Brief callout, article grid, founder quote block, footer, and a working CTA dialog.
- `Nav.jsx` — top nav (logo + links + primary CTA).
- `Hero.jsx` — full-bleed hero with mono eyebrow + serif headline + italic-load + red word + dual CTA.
- `Sequence.jsx` — the six-stage Compound Sequence (mono labels + serif descriptors).
- `BriefCallout.jsx` — Operator's Brief lockup (mono masthead, dense type, red mark).
- `ArticleGrid.jsx` — 3-up writing grid with eyebrow + italic-load titles.
- `Quote.jsx` — large pull quote with attribution.
- `Footer.jsx` — multi-column editorial footer.
- `Dialog.jsx` — diagnostic-call dialog (working open/close, esc + backdrop dismiss).

## How to view
Open `index.html` directly. CSS pulls from `../../colors_and_type.css`; logo SVGs come from `../../assets/`.

## Three-field system

Compound runs three fields, not a "dark mode." Each section commits to one:

- **Paper** (canvas) — `#FAFAF8` paper-warm. Articles, sequences, body copy, forms, the homepage default. Anywhere users sit to read 800+ words or fill something out. The default canvas — paper-warm rather than pure white because 100% luminance is a flashbulb in the afternoon office (40+ operator audience), and warmth signals *publication*, not SaaS dashboard.
- **Cream** (callout band) — `#F2EDE4`. **One section per page max.** Fills the slot Kajabi uses for sage-green / soft-gray banded sections — a featured testimonial, a brief callout, a sequence summary band. Warmth without going dark. Not a long-form reading surface — at full-page scroll the warmth becomes oppressive.
- **Dark** (gravitas band) — `#0A0A0A`. Hero, founder quote, footer, section breaks, anywhere the headline carries the gravitas. Cream type on near-black, red as the load-bearing accent.

Red is constant across all three. Alternating fields creates a magazine-spread rhythm that signals "publication, not SaaS dashboard." Pick the field by the *job*, not by aesthetic preference.

**Mechanism:** every component takes a `field` prop (`"paper"`, `"cream"`, or `"dark"`) that becomes a `data-field` attribute on its root section. Token overrides in `colors_and_type.css` (`[data-field="..."]`) flip the `--field-*` vars locally, so any descendant using field tokens recolors automatically. Logo + brand mark have light + dark variants and components pick the right one based on `field` (paper + cream both want the dark-ink logo).

**Tweaks panel** in the demo lets you flip each section independently or pick a preset:
- **Editorial (default)** — paper canvas, dark hero, cream brief callout, dark quote + footer. The committed direction.
- **All paper** — pressure-test the canvas at full page scroll.
- **All dark** — original direction, kept for reference.

Toggle "Tweaks" in the toolbar.

## Caveats
- **No live source.** If compoundorg.com goes live, point me at it and I'll align — components are deliberately cosmetic so they're cheap to retune.
- **Imagery is placeholder.** Documentary photography goes in once shoots happen.
- **Wordmark font** in the logo SVG is a generic heavy sans (Inter Tight 900). Production should swap in the brand-owner's approved cut.
