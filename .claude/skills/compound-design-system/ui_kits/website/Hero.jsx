// Hero — eyebrow / headline (red-rule emphasis) / lede / dual CTA.
const Hero = ({ field, onCTA }) => (
  <section className="cm-hero" data-field={field}>
    <div className="cm-hero-inner">
      <div className="cm-eyebrow"><span className="red">01 /</span>&nbsp;OPERATOR'S BRIEF · MAY 2026</div>
      <h1 className="cm-h1">
        You can see where AI is going.<br />
        You just don't yet know how to <em>operate</em><br />
        inside it.
      </h1>
      <p className="cm-lede">
        Compound redesigns the company around the AI it actually uses — so every role, workflow, and result compounds instead of accumulating. <em>Not a transformation. An operating layer.</em>
      </p>
      <div className="cm-cta-row">
        <button className="cm-btn cm-btn-primary" onClick={onCTA}>Book the diagnostic call <span className="ar">→</span></button>
        <a className="cm-btn cm-btn-ghost" href="#brief">Read the Operator's Brief <span className="ar">→</span></a>
      </div>
    </div>
  </section>
);
window.Hero = Hero;
