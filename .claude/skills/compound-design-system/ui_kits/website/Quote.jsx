// Big pull quote with attribution.
const Quote = ({ field }) => (
  <section className="cm-quote" data-field={field}>
    <div className="cm-quote-inner">
      <div className="cm-eyebrow"><span className="red">05 /</span>&nbsp;FROM THE FOUNDING COHORT</div>
      <blockquote className="cm-pull">
        "We stopped buying tools and started <em>redesigning the role.</em> Six months later the constraint that cost us the year — gone. The math finally worked."
      </blockquote>
      <div className="cm-quote-attr">
        <div className="cm-quote-name">Operator · Founding cohort</div>
        <div className="cm-quote-meta">Anonymized · Q1 2026</div>
      </div>
    </div>
  </section>
);
window.Quote = Quote;
