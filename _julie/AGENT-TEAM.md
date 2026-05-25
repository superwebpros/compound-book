# Julie Merge — Agent Team (Hybrid Accountability Chart)

This is the operating model for executing the Julie Mann merge. Modeled on Compound's Co-Operating approach: explicit accountabilities, named inputs, explicit hand-off Done Tests, and gates between roles.

The Human Orchestrator (Jesse) runs the chart. AI agents are supervised by it.

---

## 1. The chart

| Role | Accountability (one sentence) | Implementation | Reports To |
|---|---|---|---|
| **Human Orchestrator** | Decides scope, claims a chapter, approves Scout output, approves diffs, commits, pushes | Jesse | — |
| **Scout** | Translates manifest E-rows for one chapter into a per-chapter execution plan with line-accurate landing points and acceptance criteria | `general-purpose` Agent w/ scout prompt | Human Orchestrator |
| **Drafter** | Takes Julie's substance + voice charter and writes new prose in chapter voice for NEW-SECTION / FRAMEWORK-ADD beads | `voice-implementer` agent | Human Orchestrator |
| **Voice Shifter** | Performs I→We and attribution changes for VOICE-SHIFT / ATTRIBUTION beads without touching substance | `voice-implementer` agent (different prompt scope) | Human Orchestrator |
| **Editor** | Performs STRUCTURE beads — cuts, tightens, reorganizes; does NOT add content | `editor` agent | Human Orchestrator |
| **Anonymizer** | Executes E60 — global anonymization sweep on Julie's biographical references | `general-purpose` Agent w/ anonymizer prompt | Human Orchestrator |
| **Voice Gate** | Validates edited output conforms to voice-charter; produces flag report | `voice-scanner` agent | Human Orchestrator (advisory to all writing roles) |
| **AI-Tell Gate** | Validates no new AI patterns introduced | `ai-tell-scan` skill | Human Orchestrator |
| **Reader Gate** | Validates CEO POV — no new "so what" or undefined-term flags | `ideal-customer-reader` agent | Human Orchestrator |
| **Coherence Gate** | Validates cross-section coherence on the diff | `bmad-mkt-coherence-check` skill | Human Orchestrator |
| **Build Gate** | Validates chapter still renders (HTML at minimum) | `quarto render --to html chapters/NN.qmd` | Human Orchestrator |

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

### Drafter (per bead)
- `chapters/NN-<slug>.qmd` — landing chapter
- `_julie/per-chapter/NN.md` — Scout's plan for this chapter (acceptance criteria)
- `_julie/voice-charter.md` — voice spec (write TO this, not just be scanned against)
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

```
┌─────────────────────────────────────────────────────────────────┐
│  bd ready → Human Orchestrator claims one bead                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Route by bead type:                                            │
│    NEW-SECTION / FRAMEWORK-ADD  → Drafter                       │
│    VOICE-SHIFT / ATTRIBUTION    → Voice Shifter                 │
│    STRUCTURE                    → Editor                        │
│    ANONYMIZATION                → Anonymizer (batched)          │
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

### Drafter's Done Test
1. Julie's substance preserved (intent test — Scout's "must preserve" bullet still holds)
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

| HAC role | Existing agent file | Notes |
|---|---|---|
| Scout | — (new prompt; runs as `general-purpose` Agent) | Sample prompt template lives in this doc |
| Drafter | `.claude/agents/voice-implementer.md` | Brief includes voice-charter reference (update needed per Phase 1.5 closing note) |
| Voice Shifter | `.claude/agents/voice-implementer.md` | Same agent, narrower prompt scope per bead type |
| Editor | `.claude/agents/editor.md` | Existing; respects "no additions" rule |
| Anonymizer | — (new prompt) | Single-pass after most chapters land |
| Voice Gate | `.claude/agents/voice-scanner.md` | Update needed per Phase 1.5 to include new anti-patterns |
| Reader Gate | `.claude/agents/ideal-customer-reader.md` | Existing |
| AI-Tell Gate | `ai-tell-scan` skill | Existing |
| Coherence Gate | `bmad-mkt-coherence-check` skill | Existing |
| Build Gate | `quarto render --to html` | CLI |

**Pre-Phase-2 prerequisite:** Voice-scanner / voice-implementer / book-rewrite-brief.md need updates per voice-charter Section 6. Track as `book-ff63.16` (new task to create).

---

*This document is the operating instruction set for the Julie merge. Update it when the chart, sources, or gates change — don't drift.*
