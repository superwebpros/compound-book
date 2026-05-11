// Editorial footer. Mono section labels. Multi-column. Black field, cream type.
const Footer = ({ field }) => {
  const logoSrc = field === "dark"
    ? "../../assets/logo-compound.svg"
    : "../../assets/logo-compound-dark.svg";
  return (
    <footer className="cm-footer" data-field={field}>
    <div className="cm-footer-top">
      <div className="cm-footer-mast">
        <img src={logoSrc} alt="Compound" className="cm-footer-logo" />
        <div className="cm-footer-tag">Stop transforming. Start <em>compounding</em>.</div>
      </div>
      <div className="cm-footer-cols">
        <div>
          <div className="cm-footer-h">SEQUENCE</div>
          <a>Signal</a><a>Source</a><a>Design</a><a>Build</a><a>Deliver</a><a>Compound</a>
        </div>
        <div>
          <div className="cm-footer-h">PROGRAM</div>
          <a>The Brief</a><a>Cohort 01</a><a>PowerUps</a><a>Diagnostic call</a>
        </div>
        <div>
          <div className="cm-footer-h">WRITING</div>
          <a>Articles</a><a>Shorts</a><a>LinkedIn — Jesse</a><a>LinkedIn — Julie</a>
        </div>
        <div>
          <div className="cm-footer-h">CONTACT</div>
          <a>ops@compoundorg.com</a><a>compoundorg.com</a>
        </div>
      </div>
    </div>
    <div className="cm-footer-bottom">
      <span>© 2026 Compound</span>
      <span>Operator's Brief · Vol 01 · May 2026</span>
    </div>
  </footer>
  );
};
window.Footer = Footer;
