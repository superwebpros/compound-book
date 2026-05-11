/* global React, ReactDOM, DesignCanvas, DCSection, DCArtboard */
const { useState, useEffect } = React;

/* ---------- shared atoms ---------- */

const MARK_DARK_FIELD = "assets/logo-compound-mark.svg";       // cream + red — for dark bg
const MARK_LIGHT_FIELD = "assets/logo-compound-mark-dark.svg"; // black + red — for light bg
const WORDMARK_DARK_FIELD = "assets/logo-compound.svg";        // cream wordmark — for dark bg
const WORDMARK_LIGHT_FIELD = "assets/logo-compound-dark.svg";  // black wordmark — for light bg

/* Reusable trademark — small, mono, raised. Sits flush with display type. */
function TM({ inkDim }) {
  return (
    <span style={{
      fontFamily: "JetBrains Mono, ui-monospace, monospace",
      fontSize: "0.32em",
      fontWeight: 500,
      letterSpacing: "0.04em",
      verticalAlign: "0.7em",
      marginLeft: "0.06em",
      color: inkDim || "currentColor",
      opacity: 0.78,
    }}>TM</span>
  );
}

/* OG safe-frame wrapper. Every variant is a 1200×630 stage. */
function OG({ field = "dark", deep = false, children, style }) {
  const isDark = field === "dark";
  const bgs = {
    dark:  deep ? "#000000" : "#0A0A0A",
    paper: deep ? "#F2EDE4" : "#FAFAF8",
    cream: deep ? "#E8E1D3" : "#F2EDE4",
  };
  const inks = {
    dark:  "#F2EDE4",
    paper: "#0A0A0A",
    cream: "#0A0A0A",
  };
  const dims = {
    dark:  "#A8A39A",
    paper: "#5A554C",
    cream: "#5A554C",
  };
  const rules = {
    dark:  "#1F1E1B",
    paper: "#E8E6E1",
    cream: "#D9D2C2",
  };
  return (
    <div
      data-field={field}
      style={{
        width: 1200,
        height: 630,
        background: bgs[field],
        color: inks[field],
        fontFamily: "Bricolage Grotesque, system-ui, sans-serif",
        position: "relative",
        overflow: "hidden",
        ["--og-ink"]: inks[field],
        ["--og-dim"]: dims[field],
        ["--og-rule"]: rules[field],
        ["--og-bg"]: bgs[field],
        ["--og-red"]: "#E11D2D",
        ...style,
      }}
    >
      {children}
    </div>
  );
}

const meta = (extra = {}) => ({
  fontFamily: "JetBrains Mono, ui-monospace, monospace",
  fontSize: 16,
  letterSpacing: "0.16em",
  textTransform: "uppercase",
  fontWeight: 500,
  color: "var(--og-dim)",
  ...extra,
});

const display = (size, extra = {}) => ({
  fontFamily: "Archivo, system-ui, sans-serif",
  fontWeight: 800,
  fontSize: size,
  lineHeight: 0.98,
  letterSpacing: "-0.025em",
  color: "var(--og-ink)",
  margin: 0,
  textWrap: "balance",
  ...extra,
});

const redRule = {
  textDecoration: "underline",
  textDecorationColor: "var(--og-red)",
  textDecorationThickness: "0.075em",
  textUnderlineOffset: "0.16em",
  textDecorationSkipInk: "none",
};

const hitBlock = {
  background: "var(--og-red)",
  color: "#F2EDE4",
  padding: "0 0.16em",
  boxDecorationBreak: "clone",
  WebkitBoxDecorationBreak: "clone",
};

/* ============================================================
   Variant 01 — Dark, classic editorial lockup
   Mark + wordmark top-left. Headline center.  Mono URL + sequence
   markers along the bottom.  Red rule under both load-bearing words.
   ============================================================ */
function OG_01_Editorial() {
  return (
    <OG field="dark">
      {/* background mark — far right, bleeding */}
      <img
        src={MARK_DARK_FIELD}
        alt=""
        style={{
          position: "absolute",
          right: -180,
          top: "50%",
          transform: "translateY(-50%)",
          width: 720,
          height: 720,
          opacity: 0.16,
          pointerEvents: "none",
        }}
      />
      {/* gradient gutter so headline stays legible */}
      <div style={{
        position: "absolute", inset: 0,
        background: "linear-gradient(to right, #0A0A0A 0%, rgba(10,10,10,0.85) 55%, rgba(10,10,10,0.0) 88%)",
        pointerEvents: "none",
      }} />

      {/* top bar */}
      <div style={{ position: "absolute", top: 56, left: 64, right: 64, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
          <img src={MARK_DARK_FIELD} alt="" style={{ width: 44, height: 44 }} />
          <span style={{ fontFamily: "Archivo, sans-serif", fontWeight: 800, fontSize: 26, letterSpacing: "-0.02em" }}>Compound</span>
        </div>
      </div>

      {/* headline */}
      <div style={{ position: "absolute", left: 64, right: 64, top: 150 }}>
        <h1 style={display(86)}>
          Create a <span style={redRule}>Co-intelligent</span> Company<TM />.<br />
          <span style={redRule}>Compound</span> your growth.
        </h1>
      </div>

      {/* footer mono row */}
      <div style={{ position: "absolute", left: 64, right: 64, bottom: 56, display: "flex", justifyContent: "space-between", alignItems: "center", borderTop: "1px solid var(--og-rule)", paddingTop: 22 }}>
        <span style={meta()}>compoundorg.com</span>
        <span style={meta()}>Signal&nbsp;→&nbsp;Source&nbsp;→&nbsp;Design&nbsp;→&nbsp;Build&nbsp;→&nbsp;Deliver&nbsp;→&nbsp;<span style={{ color: "var(--og-ink)" }}>Compound</span></span>
      </div>
    </OG>
  );
}

/* ============================================================
   Variant 02 — Dark, hit-block hero
   The brochure's "once per page" highlighter moment, used once.
   Tagline on top sets up the punchline.
   ============================================================ */
function OG_02_HitBlock() {
  return (
    <OG field="dark" deep>
      <div style={{ position: "absolute", top: 56, left: 64, right: 64, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={meta({ color: "var(--og-dim)" })}>Compoundorg.com&nbsp;&nbsp;·&nbsp;&nbsp;Organizational design for AI</span>
        <img src={MARK_DARK_FIELD} alt="" style={{ width: 56, height: 56 }} />
      </div>

      <div style={{ position: "absolute", left: 64, right: 64, top: 200 }}>
        <div style={meta({ color: "var(--og-red)", marginBottom: 28 })}>Stop transforming.</div>
        <h1 style={display(124)}>
          <span style={hitBlock}>Compound</span><br />
          your growth.
        </h1>
      </div>

      <div style={{ position: "absolute", left: 64, right: 64, bottom: 56 }}>
        <div style={{ fontFamily: "Bricolage Grotesque, sans-serif", fontSize: 22, color: "var(--og-dim)", lineHeight: 1.35, maxWidth: 760 }}>
          Create a Co-intelligent Company<TM inkDim="var(--og-dim)" /> — every role, workflow, and result<br />compounds instead of accumulating.
        </div>
      </div>
    </OG>
  );
}

/* ============================================================
   Variant 03 — Paper field, editorial publication feel
   Dark mark, paper canvas, large black display, red rule emphasis.
   ============================================================ */
function OG_03_Paper() {
  return (
    <OG field="paper">
      <div style={{ position: "absolute", top: 56, left: 64, right: 64, display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
          <img src={MARK_LIGHT_FIELD} alt="" style={{ width: 44, height: 44 }} />
          <span style={{ fontFamily: "Archivo, sans-serif", fontWeight: 800, fontSize: 26, letterSpacing: "-0.02em" }}>Compound</span>
        </div>
        <span style={meta()}>May&nbsp;2026&nbsp;&nbsp;·&nbsp;&nbsp;compoundorg.com</span>
      </div>

      <div style={{ position: "absolute", left: 64, right: 64, top: 168 }}>
        <div style={meta({ color: "var(--og-red)", marginBottom: 24 })}>06&nbsp;/&nbsp;COMPOUND</div>
        <h1 style={display(94)}>
          Create a <span style={redRule}>Co-intelligent</span><br />
          Company<TM />. <span style={redRule}>Compound</span> your growth.
        </h1>
      </div>

      <div style={{ position: "absolute", left: 64, right: 64, bottom: 56, borderTop: "1px solid var(--og-rule)", paddingTop: 22, display: "flex", justifyContent: "space-between" }}>
        <span style={meta()}>Stop transforming. Start compounding.</span>
        <span style={meta()}>Book the diagnostic call →</span>
      </div>
    </OG>
  );
}

/* ============================================================
   Variant 04 — Mark-as-hero, dark, mark bleeds right
   Atom dominates right half.  Editorial copy block left.
   ============================================================ */
function OG_04_MarkBleed() {
  return (
    <OG field="dark">
      {/* huge mark, right-bleeding */}
      <img
        src={MARK_DARK_FIELD}
        alt=""
        style={{
          position: "absolute",
          right: -140,
          top: "50%",
          transform: "translateY(-50%)",
          width: 820,
          height: 820,
          opacity: 1,
        }}
      />
      {/* gradient gutter so type stays legible if it overlaps */}
      <div style={{
        position: "absolute", inset: 0,
        background: "linear-gradient(to right, #0A0A0A 0%, #0A0A0A 46%, rgba(10,10,10,0.0) 70%)",
        pointerEvents: "none",
      }} />

      <div style={{ position: "absolute", left: 64, top: 64, right: 64, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={{ fontFamily: "Archivo, sans-serif", fontWeight: 800, fontSize: 26, letterSpacing: "-0.02em" }}>Compound</span>
        <span style={meta({ color: "var(--og-dim)" })}>compoundorg.com</span>
      </div>

      <div style={{ position: "absolute", left: 64, top: 188, right: 540 }}>
        <div style={meta({ color: "var(--og-red)", marginBottom: 22 })}>Organizational design for AI</div>
        <h1 style={display(74)}>
          Create a <span style={redRule}>Co-intelligent</span> Company<TM />.
        </h1>
        <div style={{ marginTop: 22, fontFamily: "Bricolage Grotesque, sans-serif", fontSize: 26, lineHeight: 1.32, color: "var(--og-dim)", maxWidth: 540 }}>
          <span style={{ color: "var(--og-ink)" }}>Compound</span> your growth — every role, workflow, and result.
        </div>
      </div>

      <div style={{ position: "absolute", left: 64, bottom: 56 }}>
        <span style={meta()}>Stop transforming. Start compounding.</span>
      </div>
    </OG>
  );
}

/* ============================================================
   Variant 05 — Sequence brief, dark
   Top: full Compound Sequence line. Centerpiece headline.
   Treats the OG card like the cover of an Operator's Brief.
   ============================================================ */
function OG_05_SequenceBrief() {
  const stages = ["Signal", "Source", "Design", "Build", "Deliver", "Compound"];
  return (
    <OG field="dark">
      {/* top sequence rail */}
      <div style={{ position: "absolute", top: 0, left: 0, right: 0, padding: "44px 64px 28px", borderBottom: "1px solid var(--og-rule)" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
            <img src={MARK_DARK_FIELD} alt="" style={{ width: 32, height: 32 }} />
            <span style={meta({ color: "var(--og-ink)" })}>The Compound Sequence</span>
          </div>
          <span style={meta()}>compoundorg.com</span>
        </div>
        <div style={{ marginTop: 22, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          {stages.map((s, i) => (
            <React.Fragment key={s}>
              <div style={{ display: "flex", alignItems: "baseline", gap: 8 }}>
                <span style={meta({ color: "var(--og-red)" })}>{String(i + 1).padStart(2, "0")}</span>
                <span style={{
                  fontFamily: "Archivo, sans-serif",
                  fontWeight: i === 5 ? 800 : 500,
                  fontSize: 22,
                  color: i === 5 ? "var(--og-ink)" : "var(--og-dim)",
                  letterSpacing: "-0.01em",
                }}>{s}</span>
              </div>
              {i < stages.length - 1 && <span style={{ color: "var(--og-rule)", fontSize: 20 }}>→</span>}
            </React.Fragment>
          ))}
        </div>
      </div>

      <div style={{ position: "absolute", left: 64, right: 64, top: 248 }}>
        <h1 style={display(82)}>
          Create a <span style={redRule}>Co-intelligent</span> Company<TM />.<br />
          <span style={redRule}>Compound</span> your growth.
        </h1>
      </div>

      <div style={{ position: "absolute", left: 64, right: 64, bottom: 52, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={meta()}>Stop transforming. Start compounding.</span>
        <span style={meta({ color: "var(--og-ink)" })}>Book the diagnostic call →</span>
      </div>
    </OG>
  );
}

/* ============================================================
   Variant 06 — Cream callout
   Warm cream (the once-per-page band) used as the OG canvas.
   Mark prominent. Hit-block on "Compound" carries the load.
   ============================================================ */
function OG_06_Cream() {
  return (
    <OG field="cream">
      <div style={{ position: "absolute", top: 56, left: 64, right: 64, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={meta()}>compoundorg.com</span>
        <span style={meta()}>Operator's brief&nbsp;·&nbsp;May 2026</span>
      </div>

      <div style={{ position: "absolute", left: 64, right: 380, top: 156 }}>
        <h1 style={display(96)}>
          Create a Co-intelligent Company<TM />.<br />
          <span style={hitBlock}>Compound</span> your growth.
        </h1>
      </div>

      <img
        src={MARK_LIGHT_FIELD}
        alt=""
        style={{ position: "absolute", right: 56, bottom: 48, width: 280, height: 280 }}
      />

      <div style={{ position: "absolute", left: 64, bottom: 56 }}>
        <span style={{ fontFamily: "Archivo, sans-serif", fontWeight: 800, fontSize: 24, letterSpacing: "-0.02em" }}>Compound</span>
        <div style={meta({ marginTop: 8 })}>Organizational design for AI</div>
      </div>
    </OG>
  );
}

/* ============================================================
   Variant 07 — Wordmark hero, dark
   Big Compound wordmark + a single quiet tagline beneath.
   For when the headline is the brand itself.
   ============================================================ */
function OG_07_Wordmark() {
  return (
    <OG field="dark" deep>
      <div style={{ position: "absolute", inset: 0, display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", padding: 64 }}>
        <img src={WORDMARK_DARK_FIELD} alt="Compound" style={{ width: 920, height: "auto", display: "block" }} />
        <div style={{ marginTop: 18, display: "flex", alignItems: "center", gap: 18 }}>
          <span style={{ width: 40, height: 1, background: "var(--og-rule)" }} />
          <span style={meta({ color: "var(--og-ink)" })}>Stop transforming. Start compounding.</span>
          <span style={{ width: 40, height: 1, background: "var(--og-rule)" }} />
        </div>
        <div style={{ marginTop: 56, fontFamily: "Bricolage Grotesque, sans-serif", fontSize: 24, lineHeight: 1.3, color: "var(--og-dim)", textAlign: "center", maxWidth: 820 }}>
          Create a <span style={{ color: "var(--og-ink)" }}>Co-intelligent Company<TM /></span> — every role, workflow, and result compounds instead of accumulating.
        </div>
      </div>

      <div style={{ position: "absolute", bottom: 40, left: 64, right: 64, display: "flex", justifyContent: "space-between" }}>
        <span style={meta()}>compoundorg.com</span>
        <span style={meta()}>Operator's brief</span>
      </div>
    </OG>
  );
}

/* ---------- mount the canvas ---------- */

function App() {
  return (
    <DesignCanvas
      title="OG share graphic — homepage"
      subtitle="1200×630 · Compound design system · seven directions across paper / cream / dark"
    >
      <DCSection id="dark" title="Dark field — gravitas">
        <DCArtboard id="og-01" label="01 · Editorial lockup" width={1200} height={630}>
          <OG_01_Editorial />
        </DCArtboard>
        <DCArtboard id="og-02" label="02 · Hit-block hero" width={1200} height={630}>
          <OG_02_HitBlock />
        </DCArtboard>
        <DCArtboard id="og-04" label="03 · Mark-bleed" width={1200} height={630}>
          <OG_04_MarkBleed />
        </DCArtboard>
        <DCArtboard id="og-05" label="04 · Sequence brief" width={1200} height={630}>
          <OG_05_SequenceBrief />
        </DCArtboard>
        <DCArtboard id="og-07" label="05 · Wordmark hero" width={1200} height={630}>
          <OG_07_Wordmark />
        </DCArtboard>
      </DCSection>

      <DCSection id="light" title="Light fields — paper + cream">
        <DCArtboard id="og-03" label="06 · Paper, publication" width={1200} height={630}>
          <OG_03_Paper />
        </DCArtboard>
        <DCArtboard id="og-06" label="07 · Cream callout" width={1200} height={630}>
          <OG_06_Cream />
        </DCArtboard>
      </DCSection>
    </DesignCanvas>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
