# Fonts

Compound uses three webfonts loaded from Google Fonts CDN via `colors_and_type.css`:

- **Instrument Serif** — display
- **Bricolage Grotesque** — body
- **JetBrains Mono** — meta labels, numerics, code

## Substitution flag

These are loaded from `https://fonts.googleapis.com` rather than self-hosted. If Compound has license to self-host or wants offline-capable artifacts, drop the `.woff2` files into this folder and replace the `@import` block at the top of `colors_and_type.css` with:

```css
@font-face {
  font-family: "Instrument Serif";
  src: url("./fonts/InstrumentSerif-Regular.woff2") format("woff2");
  font-weight: 400; font-style: normal; font-display: swap;
}
/* ...etc for italic + Bricolage + JetBrains Mono */
```

**Action for user:** confirm self-hosting requirement and provide files if so.
