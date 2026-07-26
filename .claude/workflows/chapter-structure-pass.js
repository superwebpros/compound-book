export const meta = {
  name: 'chapter-structure-pass',
  description: 'Full structural pass on one chapter: draft → diagrams → gate → judge trio → reconcile → re-gate',
  whenToUse: 'After the chapter-auditor has run and the author has settled conceptual forks (mode: produce), or to resolve a round of author jf-notes (mode: revise). Pairs with the chapter-pass bd formula and .claude/skills/chapter-structure-pass/SKILL.md.',
  phases: [
    { title: 'Draft', detail: 'Opus drafter executes the brief', model: 'opus' },
    { title: 'Diagrams', detail: 'Sonnet agents author TODO excalidraws' },
    { title: 'Gate', detail: 'voice-scan + quarto render' },
    { title: 'Judge', detail: 'voice-scanner / prose-craft / editorial-coherence in parallel', model: 'fable' },
    { title: 'Reconcile', detail: 'Opus implementer applies must/should-fixes under canon guardrails, re-gate', model: 'opus' },
  ],
}

// args:
//   chapter    (required) e.g. 'chapters/07-build.qmd'
//   mode       'produce' (full pass from an audit brief) | 'revise' (resolve jf-notes surgically). default 'produce'
//   auditPath  produce mode: path to the chapter-auditor report (see the section titled "Drafter brief" for the brief itself)
//   rulings    author decisions text (fork answers in produce mode; jf-note rulings in revise mode)
//   skipDiagrams  true to skip the Diagrams phase (e.g. revise rounds that touch no visuals)
// The harness sometimes delivers `args` as a JSON string rather than an object — tolerate both.
const A = typeof args === 'string' ? JSON.parse(args) : (args || {})
const { chapter, mode = 'produce', auditPath = '', rulings = '', skipDiagrams = false } = A
if (!chapter) throw new Error('args.chapter is required, e.g. chapters/07-build.qmd')
const ROOT = '/Users/jesseflores/projects/compound/sites/compound-book'
const stem = chapter.replace(/^.*\//, '').replace(/\.qmd$/, '')
const scanReport = `.claude/output/voice-scan-${stem}.md`

// Locked canon — embedded because implementer agents have no Bash/bd access.
const CANON = `LOCKED CANON (protect; judges/implementers may not "fix" these):
- Constraint Backlog (never "Signal Backlog"); noun spine symptom → candidate constraint → THE constraint; Constraint Statement is a SENTENCE (the 5-field table is its validation record); selection = eligibility → load-bearing → cost tiebreak ("leverage" is charter-forbidden).
- Human Orchestrator = the operator who runs + supervises the shipped workflow's agent team. "supervisor" as a ROLE NOUN is banned book-wide (the verb "supervise" and activity descriptions are fine).
- A17 narrative voice: first-person blended; name the author inline ("Jesse was in our L10…"); NO "Jesse:"/"Julie:" colon-label speaker prefixes. Inline naming in normal prose is correct — never flag it.
- Three shades of decision (Design pair): codified rule (Task) / consistent unsurfaced pattern (Management) / true judgment (Leadership).
- Coordinator episode: Sofia (VP of Operations) proposed letting the coordinator go; the role was deconstructed; the agent team took the admin; she left; NO replacement listing; judgment redistributed to the people who stayed; exceptions landed with Sofia. Rachel left before go-live — no parallel run.
- Sofia is canonical (never Marina). Meridian Manufacturing / Elena Ruiz is the running example — never cut as redundancy.
- Coordination shapes: a pipeline / a coordinating agent (NOT "orchestrator" for the agent shape).
- No "leverage"/"transformation"; em-dashes sparingly, no NEW em-dashes where a colon/comma works; contractions in prose but NOT inside quoted agent-spec text; EOS-agnostic with at most one bridge per concept; no academic citations in prose.`

const LESSONS_REF = `MANDATORY — read _julie/chapter-pass-lessons.md IN FULL before writing a single sentence. It abstracts the author's 22 notes on the Ch7 Build pass, which cleared every gate in this pipeline and was still rated 3/5. Its twelve principles bind you. The ones this pipeline violates most:
- Do NOT invent a rule of thumb to fill the per-step template's heuristic slot. If no real heuristic exists, cut the slot (P3).
- Do NOT state a comparative statistic or a cost claim you cannot source to Meridian, a Compound story, or a citation (P3).
- Do NOT gloss a term already defined in an earlier chapter — grep the corpus first (P2).
- Do NOT define items in a moves-block/roadmap AND again in the teaching below. Roadmap = bare labels; teaching lives once (P5).
- Do NOT editorialize about your own content or state the obvious (P4).
- Hold register and tense across a run of prose; never interrupt a story to teach an instrument (P1).
- Length is a defect. Budget against Signal (~4,500 words) and Source (~6,200) (P12).`

const SCOPE = `SCOPE RULE: edit ONLY ${chapter}. If a fix requires touching any other file (glossary, process-spines, another chapter, appendices), do NOT make it — report it as a PROPAGATION item instead.`

// ---------------------------------------------------------------- Draft
phase('Draft')
const draftPrompt = mode === 'produce'
  ? `You are the drafter for the structural fine-tuning pass on ${chapter} in ${ROOT}.

READ FIRST, in order: (1) .claude/skills/chapter-structure-pass/SKILL.md — the five patterns, the author's verbatim per-step template (a DEFAULT, not a law), and the house rules; (2) _julie/voice-charter.md; (3) the audit report at ${auditPath} in full, including any trailing sections that correct, amend, or add to the sections above them (e.g. "Corrections to the audit above", "Additive findings", "Second-pass priority read") — those later sections are binding and win on conflict with earlier ones. Within it, the section titled "Drafter brief" is your brief and the section whose heading begins "Findings by pattern" is your findings list; (4) ${chapter} in full; (5) the exemplars chapters/04-signal.qmd and chapters/05-source.qmd when in doubt about shape.

AUTHOR RULINGS on the audit's conceptual forks (execute exactly; do not reopen):
${rulings || '(none provided — if the audit has a section whose heading begins "Conceptual forks", STOP and return "FORKS UNSETTLED" plus the fork list instead of drafting)'}

Execute the brief: apply patterns 1–4 (terms, stepwise teaching, redundancy cull, Meridian narrative). For diagrams (pattern 5), leave <!-- TODO excalidraw: <name> — <one-line spec> --> placeholders per the audit's section titled "Diagram list"; do not author JSON yourself. Resolve and DELETE every jf-note marker per the brief.

If the audit report has a section whose heading contains "Propagation" (e.g. "Propagation flags"), those are fixes that are DELIBERATELY OUT OF SCOPE for this chapter pass — they are already tracked as separate corpus-tie-up beads. Do NOT act on any fix listed there and do NOT treat that section as a source for diagram or prose edits.

${CANON}

${LESSONS_REF}

${SCOPE}

VERIFY before finishing (grep): 0 jf-note; 0 colon-label speaker prefixes; 0 leverage/transformation; no supervisor role-nouns introduced.
Return: a change summary — section-by-section what you did, key new prose verbatim for the load-bearing additions, the TODO diagram list, and any PROPAGATION items.`
  : `You are the drafter for a SURGICAL jf-note resolution pass on ${chapter} in ${ROOT}. The chapter already cleared the full workflow; make the smallest edits that fully resolve the author's notes. Do NOT restructure.

READ FIRST: _julie/voice-charter.md, then ${chapter} in full. Every \`jf-note\` marker in the file is an author note to resolve; delete each marker once resolved.

AUTHOR RULINGS for notes that raised conceptual questions (execute exactly; do not reopen):
${rulings || '(none — resolve each note per its own text; if a note asks an open conceptual question you cannot settle from the text, leave that ONE note in place and list it as NEEDS-AUTHOR in your summary)'}

${CANON}

${LESSONS_REF}

${SCOPE}

VERIFY before finishing (grep): jf-note count is 0 (or exactly the NEEDS-AUTHOR ones you list); 0 colon-label prefixes; 0 leverage/transformation; no new em-dashes where a colon/comma works.
Return: per-note resolution summary with key new prose verbatim + any PROPAGATION items + any NEEDS-AUTHOR notes.`

// Prose-writing stages run on Opus at high effort. Fable's 1M context was chosen for retrieval, but
// context was never the binding constraint on a ~7k-word chapter — prose quality is. (Author rated the
// Fable-drafted Ch7 pass 3/5: "poorly written, difficult to skim... tone doesn't match voice.")
const draft = await agent(draftPrompt, { label: `draft:${stem}`, phase: 'Draft', model: 'opus', effort: 'high' })
if (typeof draft === 'string' && draft.includes('FORKS UNSETTLED')) {
  return { status: 'forks-unsettled', draft }
}

// ---------------------------------------------------------------- Diagrams
phase('Diagrams')
let diagramReport = 'skipped'
if (!skipDiagrams) {
  const todos = await agent(
    `In ${ROOT}, run: grep -n "TODO excalidraw" ${chapter} — return ONLY a JSON array of objects {name, spec, line} parsed from the comments (name is the chNN-… identifier, spec is the rest of the comment). Return [] if none.`,
    { label: 'diagram:scan', phase: 'Diagrams', model: 'sonnet', schema: { type: 'object', properties: { todos: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, spec: { type: 'string' }, line: { type: 'number' } }, required: ['name', 'spec'] } } }, required: ['todos'] } }
  )
  const list = (todos && todos.todos) || []
  if (list.length) {
    const results = await parallel(list.map(d => () => agent(
      `Author the excalidraw diagram "${d.name}" for ${chapter} in ${ROOT}. Spec: ${d.spec}

Read the compound-design-system skill README (.claude/skills/compound-design-system/) and 2–3 existing excalidraw/chNN-*.excalidraw files for the exact JSON format. House style: BLACK AND WHITE — strokeColor #000000, transparent fills, roughness 0, fontFamily 1, white canvas. Write the file to excalidraw/${d.name}.excalidraw, validate the JSON parses, render it via the project's kroki/render path the other diagrams use, convert SVG→PNG with rsvg-convert, Read the PNG to eyeball it (no overlapping text, legible labels), and iterate until clean. Then REPLACE the TODO comment in ${chapter} with the shortcode {{< excalidraw ${d.name} "<caption from the spec>" >}}.
Return: file path, one-line description of what it shows, and confirmation the shortcode is wired.`,
      { label: `diagram:${d.name}`, phase: 'Diagrams', model: 'sonnet' }
    )))
    diagramReport = results.filter(Boolean).join('\n---\n') || 'all diagram agents failed'
  } else {
    diagramReport = 'no TODO excalidraw placeholders'
  }
}

// ---------------------------------------------------------------- Gate
phase('Gate')
const gate = await agent(
  `In ${ROOT} run the gate for ${chapter}:
1. /usr/bin/python3 .claude/tools/voice-scan.py ${chapter} — then Read ${scanReport} and summarize alerts (file:line + rule). Note which fall in quoted agent-spec text (contraction false positives) vs real prose.
2. quarto render ${chapter} --to html (MUST exit 0; report the error tail if not).
3. grep -c "jf-note" ${chapter}.
4. LENGTH BUDGET (a clean scan is not a green light — length is the defect our other metrics miss). Count prose words in ${chapter} and in the exemplars chapters/04-signal.qmd and chapters/05-source.qmd, excluding fenced blocks, HTML comments, shortcodes, tables and headings:
   python3 -c "import re,sys;t=open(sys.argv[1]).read();t=re.sub(r'\`\`\`.*?\`\`\`','',t,flags=re.S);t=re.sub(r'<!--.*?-->','',t,flags=re.S);t=re.sub(r'\\{\\{<.*?>\\}\\}','',t,flags=re.S);t=re.sub(r'^\\s*\\|.*$','',t,flags=re.M);t=re.sub(r'^#{1,6} .*$','',t,flags=re.M);print(len(re.findall(r\\"[A-Za-z']+\\",t)))" <file>
   Report all three. Signal is ~4,500 words and Source ~6,200. Flag explicitly if this chapter exceeds Source, and by how much — a chapter materially longer than Source needs a stated reason.
Return: render exit status, jf-note count, alert bullets, and the word-count comparison.`,
  { label: 'gate:scan+render', phase: 'Gate', model: 'sonnet' }
)

// ---------------------------------------------------------------- Judge
phase('Judge')
const FINDINGS = {
  type: 'object',
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          file: { type: 'string' },
          line: { type: 'number' },
          severity: { type: 'string', enum: ['must-fix', 'should-fix', 'note'] },
          issue: { type: 'string' },
          direction: { type: 'string' },
        },
        required: ['file', 'line', 'severity', 'issue', 'direction'],
      },
    },
    verdict: { type: 'string' },
  },
  required: ['findings', 'verdict'],
}

const LESSONS = `MANDATORY CRITERIA — read _julie/chapter-pass-lessons.md in full before judging. It abstracts the author's 22 notes on the Ch7 Build pass, which cleared every gate in this pipeline and was still rated 3/5 ("poorly written, difficult to skim, confusing, tone doesn't match voice"). Our deterministic gates measure violations, not quality: that chapter's Flesch, grade level, words-per-sentence and paragraph lengths were all in band with the exemplars. Judge against these twelve principles explicitly, and cite the principle number in your findings:
P1 register/tense holds across a run of prose; don't interrupt a story to teach an instrument.
P2 gloss a term once per BOOK at first use — grep the corpus before adding any parenthetical; re-glossing a term from an earlier chapter is a defect.
P3 no invented authority: no fabricated comparative statistics, no heuristics invented to fill a template slot, no unsourced assertions. Every number and rule of thumb traces to Meridian, a Compound story, or a citation.
P4 no editorializing about your own content ("that bar is deliberately high"); cut what a competent reader would call obvious.
P5 commit to ONE teaching location — a roadmap is bare scannable labels, teaching lives once, below. Half-defining in both is the per-step template's most repeatable failure.
P6 list-shaped content is a list (3+ parallel items).
P7 every abstract instruction carries a concrete instance.
P8 action steps must be executable by the actual reader, not assume capability the book hasn't built.
P9 no vague evocative modifiers.
P10 provenance for anything inherited — a cross-reference is not provenance; restate the substance in a clause.
P11 attribute failure modes to the right actor; plausible is not true.
P12 length is a defect. Budget against Signal (~4,500 words) and Source (~6,200).`

const judgeCtx = `Judge ${chapter} in ${ROOT} after a ${mode} pass. Drafter change summary:
${draft}

Gate results:
${gate}

${CANON}

${LESSONS}

${mode === 'revise' ? 'Scope: the changed regions per the drafter summary, plus integration with the untouched remainder. The remainder passed a previous judge pass, but that pass predates the twelve principles above — so DO re-examine it against those, while not re-litigating settled matters of taste.' : 'Scope: the full chapter.'}`

const judges = await parallel([
  () => agent(`${judgeCtx}

Judge as the voice-scanner: read _julie/voice-charter.md and the scan report at ${scanReport}. Check anti-patterns A1–A17 — especially A17 speaker labels, A12 invented company beats, A3 triplet pileups, A5 AI smell, A2 coined-term-before-defined. Contraction flags inside quoted agent-spec text are FALSE POSITIVES — protect them.`,
    { label: 'judge:voice', phase: 'Judge', schema: FINDINGS, model: 'fable', agentType: 'voice-scanner' }),
  () => agent(`${judgeCtx}

Judge as prose-craft: your overriding mandate is "is this propelling the reader forward?" Flag the per-step template applied mechanically (identical shape marching section after section), restatement, abstraction pile-ups, monotone rhythm, stranded fragments, filler intensifiers.`,
    { label: 'judge:prose-craft', phase: 'Judge', schema: FINDINGS, model: 'fable', agentType: 'prose-craft' }),
  () => agent(`${judgeCtx}

Judge as editorial-coherence: terminology against the glossary (chapters/appendix-glossary.qmd) and the fine-tuned chapters; moves-block drift against _julie/process-spines.md (flag sync needs, don't edit the registry); cross-chapter story/thread consistency (grep the beats across chapters/); stage-name and artifact-name consistency (Signal/Source/Design/Build/Deliver/Compound; Constraint Backlog; HAC; Knowledge Map). Findings in OTHER files = note severity with file:line (they become propagation beads, not edits).`,
    { label: 'judge:coherence', phase: 'Judge', schema: FINDINGS, model: 'fable', agentType: 'editorial-coherence' }),
])
const [voice, proseCraft, coherence] = judges

// ---------------------------------------------------------------- Reconcile
phase('Reconcile')
const allFindings = judges.filter(Boolean).flatMap(j => j.findings || [])
const inScope = allFindings.filter(f => !f.file || f.file.includes(stem))
const actionable = inScope.filter(f => f.severity === 'must-fix' || f.severity === 'should-fix')
const notes = inScope.filter(f => f.severity === 'note')
const propagation = allFindings.filter(f => f.file && !f.file.includes(stem))

let reconcile = 'no actionable findings'
let finalGate = gate
if (actionable.length) {
  reconcile = await agent(
    `Apply these judge findings to ${chapter} in ${ROOT}. Surgical — touch ONLY what is listed; edit no other file. Read _julie/voice-charter.md first.

${CANON}

If a finding's direction would violate the canon above or the author rulings below, SKIP it and say why in your report.
AUTHOR RULINGS: ${rulings || '(none)'}

FINDINGS (apply each; must-fix are mandatory, should-fix unless canon-conflicting):
${JSON.stringify(actionable, null, 2)}

VERIFY (Grep — you have no Bash): 0 jf-notes (unless the drafter listed NEEDS-AUTHOR ones); 0 colon-label prefixes; 0 leverage/transformation; no new em-dashes introduced by your rewrites.
Return: each fix verbatim old→new, plus any findings you skipped and why.`,
    { label: 'reconcile:implement', phase: 'Reconcile', model: 'opus', effort: 'high', agentType: 'voice-implementer' }
  )
  finalGate = await agent(
    `In ${ROOT}: quarto render ${chapter} --to html (must exit 0) and /usr/bin/python3 .claude/tools/voice-scan.py ${chapter}. Return render status + any NEW alerts vs the previous report.`,
    { label: 'gate:final', phase: 'Reconcile', model: 'sonnet' }
  )
}

return {
  status: 'complete',
  mode,
  chapter,
  draftSummary: draft,
  diagrams: diagramReport,
  gate,
  verdicts: {
    voice: voice && voice.verdict,
    proseCraft: proseCraft && proseCraft.verdict,
    coherence: coherence && coherence.verdict,
  },
  reconcile,
  finalGate,
  notesForOrchestrator: notes,
  propagationItems: propagation,
}
