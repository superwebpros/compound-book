// Article grid — 3-up. Eyebrow + italic-load title + dim body + read link.
const ARTICLES = [
  { n: "04", k: "DIAGNOSIS",   t: ["It's not a tool problem. It's an ", "operating", " problem."], d: "Why every \"AI rollout\" stalls at the seam between the tool and the team.", r: "8 min read" },
  { n: "05", k: "MECHANISM",   t: ["The Hybrid ", "Org Today", "."],                                d: "The living artifact every member updates each quarter. A working document, not a deck.",     r: "12 min read" },
  { n: "06", k: "PROOF",       t: ["What ", "$150K", " buys."],                                   d: "If your largest operational constraint costs $150K+ a year, the first sprint pays for the year.", r: "6 min read" },
];

const ArticleGrid = ({ field }) => (
  <section className="cm-articles" id="writing" data-field={field}>
    <div className="cm-section-head">
      <div className="cm-eyebrow"><span className="red">04 /</span>&nbsp;WRITING</div>
      <h2 className="cm-h2">Operators talking to <em>operators.</em></h2>
    </div>
    <div className="cm-article-grid">
      {ARTICLES.map(a => (
        <a className="cm-article" key={a.n} href="#">
          <div className="cm-article-meta"><span className="red">{a.n}</span> / {a.k}</div>
          <h3 className="cm-article-title">{a.t[0]}<em>{a.t[1]}</em>{a.t[2]}</h3>
          <p className="cm-article-body">{a.d}</p>
          <div className="cm-article-foot">
            <span className="dim">{a.r}</span>
            <span className="cm-link-arrow">Read article <span className="ar">→</span></span>
          </div>
        </a>
      ))}
    </div>
  </section>
);
window.ArticleGrid = ArticleGrid;
