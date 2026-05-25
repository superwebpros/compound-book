# Julie Merge — Agent Team (Hybrid Accountability Chart)

This is the operating model for executing the Julie Mann merge. Modeled on Compound's Co-Operating approach: explicit accountabilities, named inputs, explicit hand-off Done Tests, and gates between roles.

The Human Orchestrator (Jesse) runs the chart. AI agents are supervised by it.

**Execution model is hybrid.** Mechanical work runs solo + linear. Substantive content work (NEW-SECTION / FRAMEWORK-ADD with HEAVY-REWRITE verdict) runs through a **Design Table** — persistent specialist teammates iterating on a shared design memo before a Drafter executes the settled plan. This is the closest agent analog to the way Jesse and Julie actually collaborate.

---

## 1. The chart

| Role | Accountability (one sentence) | Implementation | Model | Reports To |
|---|---|---|---|---|
| **Human Orchestrator** | Decides scope, claims a chapter, approves Scout output, resolves Design Table dissent, approves diffs, commits, pushes | Jesse | — | — |
| **Team Lead** | Spawns persistent teammates, dispatches Design Table rounds, detects dissent, runs gates, reports to Human Orchestrator | Main session (Claude) | Opus | Human Orchestrator |
| **Scout** | Translates manifest E-rows for one chapter into a per-chapter execution plan with line-accurate landing points and acceptance criteria | `general-purpose` Agent w/ scout prompt | **Opus** | Team Lead |
| **Substance Lead** *(Design Table)* | Owns "what substance survives" — extracts operator-relevant intent from Julie's source, kills contrived/repetitive material, flags substance-rejects | Persistent teammate (`Agent` w/ `name` + `team_name`) | **Opus** | Team Lead |
| **Voice Lead** *(Design Table)* | Owns "how it sounds" — reads charter + current chapter, identifies cadence/voice constraints and likely anti-pattern traps | Persistent teammate | **Sonnet** | Team Lead |
| **Reader Lead** *(Design Table)* | Owns "does CEO care" — reads chapter arc as ideal customer, validates the substance earns its space, flags "so what" risks | Persistent teammate | **Sonnet** | Team Lead |
| **Drafter** | Executes a settled Design Table plan: writes new prose in chapter voice for NEW-SECTION / FRAMEWORK-ADD beads | `voice-implementer` agent | **Sonnet** | Team Lead |
| **Voice Shifter** | I→We and attribution changes for VOICE-SHIFT / ATTRIBUTION beads; never touches substance | `voice-implementer` agent (narrower prompt) | **Sonnet** | Team Lead |
| **Editor** | STRUCTURE beads — cuts, tightens, reorganizes; does NOT add content | `editor` agent | **Sonnet** | Team Lead |
| **Anonymizer** | E60 global anonymization sweep on Julie's biographical references | `general-purpose` Agent | **Haiku** | Team Lead |
| **Voice Gate** | Validates edited output conforms to voice-charter; flag report | `voice-scanner` agent | **Sonnet** | Team Lead |
| **AI-Tell Gate** | Validates no new AI patterns introduced | `ai-tell-scan` skill | **Sonnet** (skill default) | Team Lead |
| **Reader Gate** | Chapter-level CEO POV check — no new "so what" or undefined-term flags | `ideal-customer-reader` agent | **Sonnet** | Team Lead |
| **Coherence Gate** | Chapter-level cross-section coherence on the diff | `bmad-mkt-coherence-check` skill | **Sonnet** (skill default) | Team Lead |
| **Build Gate** | Chapter still renders (HTML at minimum) | `quarto render --to html chapters/NN.qmd` | n/a | Team Lead |

**Model rationale.** Opus where independent judgment cascades downstream (Scout, Substance Lead, Team Lead). Sonnet for execution against a settled spec (Drafter, Voice Shifter, Editor) and pattern-detection gates. Haiku for mechanical substitution at scale (Anonymizer).

---

## 2. Sources of truth (what each role reads)

Each role only reads what it needs. Inputs are explicit.

### Human Orchestrator
- `_julie/INTEGRATION-PLAN.md` — current phase, decisions
- `_julie/AGENT-TEAM.md` — this doc
- `_julie/edit-manifest.md` — E-row status
- All gate reports
- `bd ready` / `bd show <id>` — work queue

### Scout (per chapter)
- `chapters/NN-<slug>.qmd` — the chapter under review
- `_julie/edit-manifest.md` — filter to E-rows for this chapter
- `_julie/voice-charter.md` — voice constraints
- `_julie/julie-prose-risk-map.md` — per-paragraph rewrite verdict
- `_julie/stale-audit.md` — recent-decision context for this chapter
- `_julie/author-questions-answered.md` — research findings (esp. E21 attribution convention)
- `_julie/julie-redline.md` — original instruction context (read by line range from manifest)
- `_julie/julie-final.md` — substance reference only, when redline ambiguous
- Persistent memories: `framework-attribution-rule`, `julie-prose-ai-patterns`, `julie-prose-is-substance-only`, `julie-merge-rejected-rows`

### Substance Lead (Design Table; persistent across chapter batch)
- Julie's source paragraph(s) from `_julie/julie-redline.md` and (when ambiguous) `_julie/julie-final.md`
- `_julie/julie-prose-risk-map.md` — risk verdict + flagged patterns
- `_julie/edit-manifest.md` — E-row context
- Persistent memories: `julie-prose-is-substance-only`, `julie-prose-ai-patterns`, `julie-merge-rejected-rows`, `framework-attribution-rule`
- The chapter `.qmd` (read for narrative arc only; does not edit)

### Voice Lead (Design Table; persistent across chapter batch)
- `_julie/voice-charter.md` (canonical spec)
- The chapter `.qmd` (read for cadence calibration vs. existing prose)
- Scout's per-chapter plan (`_julie/per-chapter/NN.md`)
- Julie's source paragraph (read to identify anti-pattern traps)

### Reader Lead (Design Table; persistent across chapter batch)
- The chapter `.qmd` — read as the ideal customer (CEO of 25-100 person company running EOS)
- Persistent memory: `compound-does-not-have-on-site-implementers-like` (operator context)
- The chapter's pre-existing narrative arc
- The proposed substance (from Substance Lead's Round 1 take)

### Drafter (per bead, executing settled spec)
- `chapters/NN-<slug>.qmd` — landing chapter
- `_julie/per-bead/EXX-design.md` — **the approved Design Table memo (Path B)** OR `_julie/per-chapter/NN.md` Scout plan (Path A)
- `_julie/voice-charter.md` — voice spec the agent writes against
- `_julie/julie-prose-risk-map.md` — verdict for the specific paragraph (substance preservation level)
- Julie's source paragraph (line range from manifest)
- Persistent memory: `framework-attribution-rule` (scrub attribution language), `julie-prose-is-substance-only` (extract substance, write fresh)

### Voice Shifter (per bead)
- `chapters/NN-<slug>.qmd` — landing chapter
- `_julie/per-chapter/NN.md` — Scout's plan
- `_julie/voice-charter.md` Section 1 + Section 3 — pillars + vocabulary
- `_julie/author-questions-answered.md` Q-E21 — blended "we" + in-prose attribution convention
- E-row from manifest

### Editor (per bead)
- `chapters/NN-<slug>.qmd` — landing chapter
- `_julie/per-chapter/NN.md` — Scout's plan
- `_julie/voice-charter.md` Section 2 — cadence rules

### Anonymizer (single global pass)
- All `chapters/*.qmd` + `index.qmd`
- `_julie/stale-audit.md` Section 4 — additional anonymization decisions
- Bead `book-ff63.14` (Sofia Reyes / Marina / Lucas decisions when resolved)
- Persistent memory: `meridian-consulting-group-is-meridian-manufacturing` (Meridian stays as-is)

### Gates (each reads only the diff or the edited chapter)
- Edited `chapters/NN-<slug>.qmd`
- `_julie/voice-charter.md` (Voice Gate, AI-Tell Gate)
- Pre-edit baseline (for polish-loss diff)

---

## 3. Per-bead workflow (the inner loop)

Beads route to one of two execution paths based on type and risk verdict from the prose risk map.

### Path A — Solo (mechanical work)

Used for: VOICE-SHIFT · ATTRIBUTION · STRUCTURE · ANONYMIZATION · NEW-SECTION/FRAMEWORK-ADD with verdict CLEAN or LIGHT EDIT.

```
┌─────────────────────────────────────────────────────────────────┐
│  bd ready → Human Orchestrator claims one bead                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Route by bead type:                                            │
│    VOICE-SHIFT / ATTRIBUTION    → Voice Shifter                 │
│    STRUCTURE                    → Editor                        │
│    ANONYMIZATION                → Anonymizer (batched)          │
│    NEW-SECTION (CLEAN/LIGHT)    → Drafter (direct)              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Writing role produces edit; outputs diff to working tree       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Gate sequence (per-bead, lightweight):                         │
│    1. Voice Gate           (must pass)                          │
│    2. AI-Tell Gate         (must pass — zero new flags)         │
│    3. Build Gate           (chapter renders)                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Pass → bead closed, change staged                              │
│  Fail → reloop ONCE; second fail → bd human                     │
└─────────────────────────────────────────────────────────────────┘
```

### Path B — Design Table (substantive work)

Used for: NEW-SECTION · FRAMEWORK-ADD with verdict HEAVY REWRITE (or REJECT-for-substance that the Human Orchestrator has decided to salvage). About ~20 of our 42 actionable beads.

```
┌─────────────────────────────────────────────────────────────────┐
│  Team Lead spawns persistent teammates (once per chapter batch) │
│    Substance Lead (Opus) · Voice Lead (Sonnet) · Reader Lead    │
│    (Sonnet) · Drafter (Sonnet, executes after convergence)      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Round 1 — Initial takes (parallel)                             │
│    Each Lead writes their section of the shared design memo:    │
│    _julie/per-bead/EXX-design.md                                │
│      [Substance]  what survives, what to kill, intent           │
│      [Voice]      cadence target, anti-pattern traps, vocab     │
│      [Reader]     CEO take-away test, "so what" risk            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Round 2 — Cross-read and refine (parallel)                     │
│    Each Lead reads the others' Round 1 takes and refines theirs │
│    Any Lead may add a [DISSENT] block flagging unresolvable     │
│    conflict (e.g., Substance wants to keep something Voice says │
│    cannot land cleanly)                                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Team Lead reads memo:                                          │
│    - No [DISSENT] blocks → forward to Human Orchestrator        │
│    - [DISSENT] present  → escalate to Human Orchestrator with   │
│                            framed decision request              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Human Orchestrator approves the memo (or redirects)            │
│  This is THE decision point — substance, framing, fit all       │
│  settled here, not during drafting                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Drafter executes the approved memo                             │
│    Inputs: chapter .qmd · voice-charter · approved memo         │
│    Drafter is executing, not authoring — memo is the spec       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Gate sequence (same as Path A): Voice → AI-Tell → Build        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Pass → bead closed, change staged                              │
│  Fail → REVIEW the memo (the spec may be at fault, not Drafter) │
│         → kick back to Design Table for 1 more round if needed  │
│         → second fail → bd human                                │
└─────────────────────────────────────────────────────────────────┘
```

**Bounded rounds.** Maximum 2 rounds of memo refinement. If consensus not reached by round 2, the bead escalates to Human Orchestrator with the disagreement explicit. This prevents infinite agent-deliberation while preserving real dissent as signal.

**Persistent teammates.** Substance Lead / Voice Lead / Reader Lead / Drafter are spawned once per chapter batch (typically 3–7 beads at a time) and stay alive across beads in that batch. They retain context — Round 2 for bead E11 doesn't reload the chapter from scratch if they already worked E10. Big token savings vs. spawning fresh subagents each bead.

**Cleanup.** When a chapter's beads close, Team Lead dismisses the teammates. Next chapter spawns a fresh team — keeps context windows tight and avoids cross-chapter contamination.

## 4. Per-chapter workflow (the outer loop)

```
┌─────────────────────────────────────────────────────────────────┐
│  Human Orchestrator selects next chapter in sequence:           │
│  Preface → Ch1 → Ch2 → ... → Ch11 → Glossary → About → Cases    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Scout runs on chapter → _julie/per-chapter/NN.md               │
│  (Phase 2)                                                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Human Orchestrator approves Scout output                       │
│  (kicks back if landing points wrong or risks missed)           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 3: per-E-row beads created from Scout's plan             │
│  (parallel via subagent if multiple chapters batched)           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Inner loop: each bead through writer → gates → close           │
│  Order: voice-shift first, then new-section, then structure     │
│  (lets voice land cleanly before substance accretes)            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Chapter-level gate (heavier):                                  │
│    4. Reader Gate          (CEO POV, no new "so what")          │
│    5. Coherence Gate       (cross-section integrity)            │
│    6. Polish-Loss Check    (text-diff vs baseline, <20% drop)   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Human Orchestrator reviews diff, commits, pushes               │
│  Updates epic progress                                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Done Tests (per role)

A handoff is only complete when its Done Test passes. These are the "must-be-true" predicates at each chart boundary.

### Scout's Done Test
1. Every in-scope E-row for the chapter has a verdict: `LAND` / `LAND-WITH-MODIFICATION` / `SKIP-ALREADY-DONE` / `NEEDS-AUTHOR`
2. Every `LAND` E-row has a tightened current-`.qmd` line range (not the manifest's best-guess from Julie's source)
3. Every `LAND` E-row has acceptance criteria written in 2–4 bullets, including:
   - What substance must be preserved
   - Which voice-charter Section 4 anti-patterns are most likely to trip
   - Whether the framework-attribution rule applies
4. Any conflict with recent polish (per `stale-audit.md`) is flagged
5. Output file `_julie/per-chapter/NN.md` exists and is structured per template
6. Suggested bead order is recorded (voice-shift first, then new-section, then structure)

### Substance Lead's Done Test
1. Memo's `[Substance]` block names exactly what intent must be preserved (in operator language, not Julie's)
2. Names exactly what should be cut from Julie's source (with reason — contrived, repetitive, attribution drift, etc.)
3. Cross-references the prose risk map verdict for the paragraph
4. Flags any substance-reject candidate that should NOT be salvaged at all
5. Round 2: has read Voice Lead and Reader Lead's Round 1 takes and either incorporated or flagged dissent

### Voice Lead's Done Test
1. Memo's `[Voice]` block names which charter Section 4 anti-patterns are highest risk for this specific paragraph
2. Specifies cadence target (sentence rhythm, em-dash placement) calibrated to the chapter's existing voice
3. Names any vocabulary collisions (coined terms used before defined, framework attribution drift)
4. Round 2: has read Substance Lead and Reader Lead's Round 1 takes and either incorporated or flagged dissent

### Reader Lead's Done Test
1. Memo's `[Reader]` block states the CEO take-away in one sentence
2. Confirms the proposed substance earns its space (no "so what" flag)
3. Confirms no required term is used before definition
4. Confirms the chapter arc remains coherent with this addition
5. Round 2: has read Substance Lead and Voice Lead's Round 1 takes and either incorporated or flagged dissent

### Drafter's Done Test
1. Julie's substance preserved per the approved memo (or Scout plan for Path A)
2. Voice-charter Section 4 anti-patterns: **zero** in output
3. Cadence matches sampled cadence rules from charter (em-dash usage, sentence length distribution)
4. Reads as smart-friend-over-coffee, not consultant
5. Framework attribution scrubbed (if applies)
6. No new coined vocabulary introduced without definition
7. Output is a unified diff against the current chapter (not a full file rewrite)

### Voice Shifter's Done Test
1. Literal-meaning preserved (semantic equivalence test)
2. Attribution follows Q-E21 convention: **blended "we"** with in-prose attribution; **no inline `Jesse:` / `Julie:` tags**
3. No new substance added
4. No reordering of paragraphs
5. Output is a unified diff against current chapter

### Editor's Done Test
1. Cuts only — no additions
2. Cross-references resolve (no orphaned links, no broken section anchors)
3. Hand-off points preserved (chapters connect at start/end as before)
4. Chapter still renders

### Anonymizer's Done Test
1. Every targeted name replaced with agreed convention
2. Meridian Manufacturing untouched
3. PM Agent Team names untouched
4. No collateral substitution (e.g., didn't replace "Marina" inside an unrelated word)
5. All chapters re-render

### Gate Done Tests
- **Voice Gate**: zero MAJOR flags from voice-scanner; MINOR flags reviewed by Orchestrator
- **AI-Tell Gate**: zero new AI-pattern flags vs. baseline
- **Build Gate**: `quarto render --to html chapters/NN.qmd` exits 0
- **Reader Gate**: zero new "so what" or undefined-term flags from ideal-customer-reader
- **Coherence Gate**: zero new contradiction or undefined-coined-term flags from coherence-check
- **Polish-Loss Check**: text-only diff shows < 20% prose removed for any section (else manual review)

### Human Orchestrator's Done Test (chapter level)
1. All bead-level gates green
2. Chapter-level gates green
3. Diff review confirms no surprise loss of polished passages
4. Git commit message references epic + closed bead IDs
5. `git push` succeeds

---

## 5.5. Design Table protocol (Path B mechanics)

### Memo template

Path B beads use a shared file: `_julie/per-bead/EXX-design.md`. Each Lead owns one block. Round 2 refines the same blocks in place.

```markdown
# Design Memo — EXX [bead title]

**Bead:** book-ff63.NN  ·  **Target file:** chapters/NN-<slug>.qmd  ·  **Lines:** L-L
**Manifest verdict:** HEAVY REWRITE  ·  **Type:** NEW-SECTION

## [Substance] — owned by Substance Lead

**What survives from Julie's source:**
- ...

**What to cut and why:**
- ...

**Operator intent in one sentence:**
> ...

**Rounds:** R1 [timestamp] · R2 [timestamp]
**Dissent:** [none] OR [block referencing the conflict]

## [Voice] — owned by Voice Lead

**Highest-risk anti-patterns for this paragraph:**
- ...

**Cadence target (calibrated to chapter):**
- ...

**Vocabulary watch:**
- ...

**Rounds:** R1 [timestamp] · R2 [timestamp]
**Dissent:** [none] OR [block]

## [Reader] — owned by Reader Lead

**CEO take-away in one sentence:**
> ...

**Earns-its-space test:** PASS / FAIL with reason
**Definition-before-use check:** PASS / FAIL with reason
**Chapter-arc coherence:** PASS / FAIL with reason

**Rounds:** R1 [timestamp] · R2 [timestamp]
**Dissent:** [none] OR [block]

## [Team Lead] — convergence verdict

After R2: CONVERGED / DISSENT-ESCALATED

## [Human Orchestrator] — approval

APPROVED / REDIRECT [with redirection] / KILL [with reason]
```

### Dispatch mechanics

1. **Spawn teammates once per chapter batch.** When Human Orchestrator approves Scout output for a chapter, Team Lead spawns Substance Lead, Voice Lead, Reader Lead, and Drafter as named persistent teammates via `Agent` with `name` + `team_name`. They persist across all Path B beads in that chapter.

2. **Round 1 dispatch.** Team Lead `SendMessage`s each Lead in parallel with the bead context (E-row + Julie source lines + memo path). Each Lead writes their block to the memo, sends back "R1 complete." Team Lead waits on all three.

3. **Round 2 dispatch.** Team Lead notifies each Lead via `SendMessage` that R1 is complete; each re-reads the memo (including the other two Leads' R1 takes) and refines their block. Sends back "R2 complete" or "R2 DISSENT."

4. **Convergence check.** Team Lead reads memo. If no `[DISSENT]` blocks → mark CONVERGED, forward to Human Orchestrator. If any `[DISSENT]` → mark DISSENT-ESCALATED, surface to Human Orchestrator with the conflict framed as a decision request.

5. **Human Orchestrator decision.** APPROVE → Drafter executes. REDIRECT → Team Lead dispatches a single targeted Round 3 with the redirection. KILL → bead closed as won't-do, rationale logged.

6. **Cleanup.** When all beads for the chapter close, Team Lead dismisses the teammates. Next chapter spawns fresh.

### Dissent rules

A `[DISSENT]` block is signal, not failure. It means: "the substance, voice, or reader concerns cannot be reconciled by the Leads alone — the Human Orchestrator must decide."

Acceptable dissent triggers:
- Substance Lead: "the operator intent survives but Voice Lead's cadence target kills the specificity"
- Voice Lead: "Substance Lead's proposed substance forces an anti-pattern I cannot scrub"
- Reader Lead: "the substance survives and the voice lands, but a CEO doesn't care about this paragraph"

Unacceptable dissent triggers (auto-reject by Team Lead, do not surface):
- "I disagree" without a concrete conflict named
- Substance Lead arguing for restoring REJECTED-rule content (framework attribution, etc.)
- Any Lead arguing against the voice charter itself (charter is canon)

### Cost discipline

Path B uses ~4-5x the tokens of Path A per bead. To avoid runaway:

- **Only HEAVY-REWRITE beads use Path B.** Verdicts come from prose risk map (Phase 1.6).
- **Persistent teammates batch beads.** A single Substance Lead handles all HEAVY-REWRITE beads in a chapter before being dismissed. Context loaded once.
- **Bounded rounds.** Maximum 2 rounds before forced escalation.
- **No nested Design Tables.** Drafter executes solo against the approved memo; gates remain solo.

## 6. Sequence (the order in which things run)

### Phase 2 — Scout dispatch (analysis only; no chapter edits)

Run Scout on each chapter, in this order:

1. `index.qmd` (Preface) — establishes dual-author voice frame
2. `chapters/01-diagnosis.qmd`
3. `chapters/02-co-operating-model.qmd`
4. `chapters/03-the-framework.qmd`
5. `chapters/04-signal.qmd` *(touches CH04-L10 — extra care)*
6. `chapters/05-source.qmd`
7. `chapters/06-designing-the-system.qmd`
8. `chapters/06b-designing-the-work.qmd`
9. `chapters/07-build.qmd`
10. `chapters/08-deliver.qmd` *(Julie-led restructure — heaviest)*
11. `chapters/09-compound.qmd`
12. `chapters/10-the-rhythm.qmd`
13. `chapters/11-what-to-do-next.qmd` *(Q3 relocations land here)*
14. `chapters/appendix-glossary.qmd` *(framework definitions land here)*
15. About-the-Authors (new section in appendix — receives relocated E07/E52/E53/E54 content)

Scouts can run in parallel batches of 3–4 once Phase 2 is approved.

### Phase 3 — Bead creation

For each Scout-output that the Human Orchestrator approves:
- Create per-E-row beads with full inline context
- Wire dependencies (Preface beads block downstream attribution beads; framework-add beads block their downstream references)

### Phase 4 — Execution

Process chapters in the same order as Phase 2. Per chapter:
- Inner-loop each bead through writer → gates → close
- Run chapter-level gates after all beads complete
- Human Orchestrator commits + closes chapter

### Phase 5 — Final integration

- Cross-chapter coherence + render
- PR review of `merge-julie-feedback` → `master`

---

## 7. Escalation paths

- **Drafter / Voice Shifter / Editor fails gates twice on same bead** → bead flipped to `bd human`, Human Orchestrator decides (rewrite manually, kick back to Julie, or close as won't-do)
- **Scout finds CONFLICT-flagged content** → bead created as `bd human` from the start, never auto-executes
- **Polish-Loss Check trips on a section** → manual review required before commit; revert is the safe default
- **Substance-reject items (book-ff63.15)** → blocked pending Julie input; never enter the inner loop until resolved

---

## 8. What this maps to in the existing repo

| HAC role | Implementation | Notes |
|---|---|---|
| Team Lead | Main session Claude (Opus) | Spawns teammates via `Agent` with `name`+`team_name`; dispatches via `SendMessage`; reads memos directly |
| Scout | `Agent` w/ scout prompt (Opus) | Sample prompt template lives in this doc §7 below |
| Substance Lead | Persistent teammate `Agent` w/ substance prompt (Opus) | New role; loads context once per chapter batch |
| Voice Lead | Persistent teammate `Agent` w/ voice prompt (Sonnet) | Reads voice-charter as canon |
| Reader Lead | Persistent teammate `Agent` w/ reader prompt (Sonnet) | Inherits `ideal-customer-reader` mindset but participates in Design Table iteration |
| Drafter | `.claude/agents/voice-implementer.md` (Sonnet) | Brief needs voice-charter reference (book-ff63.16) |
| Voice Shifter | `.claude/agents/voice-implementer.md` (Sonnet) | Same agent, narrower prompt scope per bead type |
| Editor | `.claude/agents/editor.md` (Sonnet) | Existing; respects "no additions" rule |
| Anonymizer | `Agent` w/ anonymizer prompt (Haiku) | Single-pass after most chapters land |
| Voice Gate | `.claude/agents/voice-scanner.md` (Sonnet) | Needs anti-pattern updates per book-ff63.16 |
| Reader Gate | `.claude/agents/ideal-customer-reader.md` (Sonnet) | Chapter-level pass after all beads close |
| AI-Tell Gate | `ai-tell-scan` skill | Existing |
| Coherence Gate | `bmad-mkt-coherence-check` skill | Existing |
| Build Gate | `quarto render --to html` | CLI |

**Pre-Phase-2 prerequisites (tracked as `book-ff63.16`):**
1. Update `voice-scanner.md` per voice-charter Section 6
2. Update `voice-implementer.md` to reference voice-charter as spec
3. Update `book-rewrite-brief.md` with forbidden-constructions reference
4. Update `CLAUDE.md` with pointer to charter
5. Author scout / substance-lead / voice-lead / reader-lead / anonymizer prompt templates (lives in `.claude/agents/` or inline in Team Lead's dispatch code)

**Agent Teams primitives used (native):**
- `Agent` with `name` + `team_name` → persistent teammate identity
- `SendMessage` → async mailbox between teammates and Team Lead
- `TaskList` → shared work queue (per-chapter bead set)
- Auto-loading of CLAUDE.md, skills, MCPs per teammate

**Hand-rolled on top:**
- Shared design memo (file-based, not native shared memory)
- Round protocol (bounded to 2, Team Lead dispatches via `SendMessage`)
- Dissent detection (Team Lead reads memo, surfaces `[DISSENT]` blocks)
- Cleanup (Team Lead dismisses teammates at chapter close)

---

*This document is the operating instruction set for the Julie merge. Update it when the chart, sources, or gates change — don't drift.*
