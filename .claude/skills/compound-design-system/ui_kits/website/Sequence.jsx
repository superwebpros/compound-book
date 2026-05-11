// The Compound Sequence — six stages, mono labels + serif descriptors.
const STAGES = [
  { n: "01", k: "SIGNAL",   t: "Find the constraint that costs the most.",     b: "We start where the math is real. The largest operational constraint, named in dollars per year." },
  { n: "02", k: "SOURCE",   t: "Locate the headcount math.",                    b: "Where does the constraint actually live in the org chart? Which roles, which workflows, which decisions." },
  { n: "03", k: "DESIGN",   t: "Redesign the role, not the tool stack.",        b: "Org design first. Tools follow the design. Never the other way." },
  { n: "04", k: "BUILD",    t: "Hybrid Org Today — the living artifact.",       b: "A working document, owned by the operator, updated every quarter. Not a deck." },
  { n: "05", k: "DELIVER",  t: "PowerUps — strategic + tactical, monthly.",     b: "The operating rhythm. The system the buyer runs." },
  { n: "06", k: "COMPOUND", t: "Stack the next sprint on the last one.",        b: "Six months in, the rhythm is the company. The constraint moves. We move with it." },
];

const Sequence = ({ field }) => (
  <section className="cm-sequence" id="sequence" data-field={field}>
    <div className="cm-sequence-head">
      <div className="cm-eyebrow"><span className="red">02 /</span>&nbsp;THE MECHANISM</div>
      <h2 className="cm-h2">Signal <span className="ar">→</span> Source <span className="ar">→</span> Design <span className="ar">→</span> Build <span className="ar">→</span> Deliver <span className="ar">→</span> <em>Compound.</em></h2>
      <p className="cm-lede">Six stages. Always all six. Always in order. Always with arrows.</p>
    </div>
    <ol className="cm-stages">
      {STAGES.map(s => (
        <li className="cm-stage" key={s.n}>
          <div className="cm-stage-meta"><span className="red">{s.n}</span> / {s.k}</div>
          <h3 className="cm-stage-title">{s.t}</h3>
          <p className="cm-stage-body">{s.b}</p>
        </li>
      ))}
    </ol>
  </section>
);
window.Sequence = Sequence;
