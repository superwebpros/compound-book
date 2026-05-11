// Operator's Brief callout — masthead-style block, mono eyebrows, dense type.
const BriefCallout = ({ field }) => (
  <section className="cm-brief" id="brief" data-field={field}>
    <div className="cm-brief-grid">
      <aside className="cm-brief-side">
        <div className="cm-brief-mast">
          <div className="cm-brief-mast-row"><span>OPERATOR'S BRIEF</span><span className="red">·</span><span>VOL 01</span></div>
          <div className="cm-brief-mast-row dim"><span>COMPOUNDORG.COM</span><span>·</span><span>MAY 2026</span></div>
        </div>
        <img src={field === "dark" ? "../../assets/logo-compound-mark.svg" : "../../assets/logo-compound-mark-dark.svg"} alt="" className="cm-brief-mark" />
      </aside>
      <div className="cm-brief-body">
        <div className="cm-eyebrow"><span className="red">03 /</span>&nbsp;FOR LEADERS, NOT LEARNERS</div>
        <h2 className="cm-h3">A working document for the operationally mature mid-market — read by the CEO, run by the operator, updated <em>every quarter.</em></h2>
        <p>The Brief names the constraint, sources the headcount math, and prescribes the redesign. It's not a deck. It's not a strategy memo. It's the artifact the company runs.</p>
        <ul className="cm-brief-list">
          <li><span className="num">01</span><span>Diagnose the largest operational constraint in dollars per year.</span></li>
          <li><span className="num">02</span><span>Locate it in the org chart — role, workflow, decision.</span></li>
          <li><span className="num">03</span><span>Redesign the role with AI as a permanent operating layer.</span></li>
          <li><span className="num">04</span><span>Stack the next sprint. Compound the result.</span></li>
        </ul>
        <a className="cm-link-arrow" href="#">Read the full brief <span className="ar">→</span></a>
      </div>
    </div>
  </section>
);
window.BriefCallout = BriefCallout;
