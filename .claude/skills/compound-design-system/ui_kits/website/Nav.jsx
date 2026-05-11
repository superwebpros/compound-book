// Top navigation. 64px tall, flat --bg, 1px bottom rule. No blur.
const Nav = ({ active = "Sequence", field, onCTA }) => {
  const links = ["The Sequence", "The Brief", "Cohort", "Writing"];
  const logoSrc = field === "dark"
    ? "../../assets/logo-compound.svg"
    : "../../assets/logo-compound-dark.svg";
  return (
    <header className="cm-nav" data-field={field}>
      <div className="cm-nav-left">
        <a className="cm-logo" href="#">
          <img src={logoSrc} alt="Compound" />
        </a>
        <nav className="cm-links">
          {links.map(l => (
            <a key={l} className={active === l.replace(/^The /, "") ? "active" : ""} href="#">{l}</a>
          ))}
        </nav>
      </div>
      <div className="cm-nav-right">
        <a className="cm-link-mono" href="#">Sign in</a>
        <button className="cm-btn cm-btn-primary" onClick={onCTA}>Book the diagnostic call</button>
      </div>
    </header>
  );
};
window.Nav = Nav;
