// Diagnostic-call dialog. Open/close, ESC + backdrop dismiss, fake submit.
const Dialog = ({ open, onClose }) => {
  const [submitted, setSubmitted] = React.useState(false);
  React.useEffect(() => {
    if (!open) { setSubmitted(false); return; }
    const onKey = (e) => { if (e.key === "Escape") onClose(); };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [open, onClose]);
  if (!open) return null;
  return (
    <div className="cm-dialog-backdrop" onClick={onClose}>
      <div className="cm-dialog" onClick={(e) => e.stopPropagation()}>
        <div className="cm-dialog-head">
          <div className="cm-eyebrow"><span className="red">·</span>&nbsp;DIAGNOSTIC CALL · 45 MIN</div>
          <button className="cm-dialog-x" onClick={onClose} aria-label="Close">×</button>
        </div>
        {!submitted ? (
          <>
            <h2 className="cm-h3">What's your largest operational constraint costing you per year?</h2>
            <p className="cm-dialog-sub">If $150K+, the first sprint pays for the year.</p>
            <form className="cm-form" onSubmit={(e) => { e.preventDefault(); setSubmitted(true); }}>
              <label>Name<input required defaultValue="" placeholder="Your name" /></label>
              <label>Work email<input type="email" required placeholder="you@company.com" /></label>
              <label>Annual constraint cost<input required placeholder="$0" /></label>
              <label>What is the constraint?<textarea rows="3" placeholder="Name it in one sentence."></textarea></label>
              <button type="submit" className="cm-btn cm-btn-primary cm-btn-block">Send <span className="ar">→</span></button>
            </form>
          </>
        ) : (
          <div className="cm-dialog-done">
            <h2 className="cm-h3">Sent.</h2>
            <p>One of us will reply within one business day. <em>That's the whole pitch.</em></p>
            <button className="cm-btn cm-btn-secondary" onClick={onClose}>Close</button>
          </div>
        )}
      </div>
    </div>
  );
};
window.Dialog = Dialog;
