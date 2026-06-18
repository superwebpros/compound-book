Compound · Design / Specification

# Write the Design Brief

*Capture every decision the design has made into one document — the single artifact Build inherits, with no other channel.*

The Design Brief is Design's output and Build's input. It names who decides, which systems are involved, what data is required, and how the workflow is governed, so a builder can start without guessing and without a meeting. Fill the seven sections in order. Every blank is a Design decision that hasn't been made yet — and a gap here becomes a question in Build.

**Before you start, you need the upstream Design artifacts in hand:** the swim lane or flowchart, the Hybrid Accountability Chart, the governance decisions from Designing the System, and the measurable targets from Signal. If you can't fill a section from those without inventing the answer, the design isn't finished — close that gap first.

---

## Write the Workflow Summary

Translate the swim lane or flowchart into written specification — trigger to output, every step, handoff, and decision point named.

1. State the trigger: what kicks the workflow off, and how it arrives.
2. List every step in sequence, naming each agent and the human review/approval, through to the final output.
3. Count the handoffs (each crossing between agents or between agent and human) so the path is unambiguous.

> **Meridian — Workflow Summary:** Trigger: inbound RFQ email. Steps: auto-log to HubSpot → Quote Research Agent pulls customer history → Quote Pricing Agent assembles material and labor costs → Quote Assembly Agent produces draft PDF → Elena reviews and approves → Ty delivers to customer. Seven steps, four handoff crossings.

---

## Name the Stakeholders

Identify the Human Orchestrator, the role-change list, downstream consumers, and approvers so accountability is unambiguous before Build begins.

1. Name the Human Orchestrator — the person who owns the workflow's outcome.
2. List the team members whose roles change, and state what each moves *from* and *to*.
3. Name the downstream consumers of the agent team's output and anyone with approval authority.

> **Meridian — Stakeholders:** Human Orchestrator: Elena Ruiz (VP Ops). Role changes: Elena moves from building quotes to reviewing drafts. Downstream consumer: Ty Banfield (Sales Lead). Approver: Elena on every quote.

---

## List the Systems

Every system the workflow touches must be named with the specific data it provides or receives, preventing integration surprises in Build.

1. List every system the workflow touches: CRM, ERP, project management tool, communication platforms, spreadsheets.
2. For each, name the specific data it provides or receives — not just the system name.
3. Note any file-based source (a spreadsheet, a document) the same way you note a system; if data flows through it, it belongs here.

> **Meridian — Systems:** HubSpot CRM (customer records, RFQ intake, quote delivery queue). JobBOSS ERP (material pricing, lead times). Customer Notes.xlsx (112 pricing exception rules). Google Workspace (standard quote template).

---

## Define the Data Requirements

Specifying what data the agent team needs, where it lives, what format it arrives in, and what happens when it is missing or malformed closes the most common Build failure mode.

1. For each data requirement, name what data is needed and where it lives.
2. State the format it arrives in and how complete/current it is (structured records, nightly update, validated file).
3. Write the failure rule: what happens when that data is missing, stale, or malformed.

> **Meridian — Data Requirements:** Customer history: HubSpot, structured records, complete for all active accounts. Material pricing: JobBOSS, updated nightly. Pricing exceptions: validated Excel file, 112 rows, loaded as standing context. If exceptions file is missing or stale: escalate to Elena before running.

---

## State the Success Criteria

Anchors the brief to the measurable Signal targets so Build knows what it is optimizing for, not just what it is building.

1. Pull the measurable outcomes from Signal that this design is intended to move.
2. State each as a specific target — from a baseline to a goal — not as vague improvement.
3. Include the business outcome the targets roll up to (revenue, hours recovered, turnaround) so the optimization target is clear.

> **Meridian — Success Criteria:** Quote turnaround from 3 days to same-day. Elena's quoting hours from 15/week to under 3. Revenue recovered from delayed quotes: target $558K annualized.

---

## Document Constraints and Guardrails

Locks the governance decisions from Designing the System — data access, action permissions, escalation paths, quality cadence, kill switch — into the design record before Build inherits it.

1. State data access boundaries (what the agents may read, what they may write) and action permissions (what they may and may not do).
2. Write the escalation paths: the conditions that route a decision to a human, and to whom.
3. Name the kill switch (who can halt the workflow, from where) and the quality monitoring cadence.

> **Meridian — Constraints and Guardrails:** Agents read HubSpot and JobBOSS; no write access except draft quote record. No external communications. Escalate if pricing confidence below 60% or if any exception rule is ambiguous. Kill switch: Ty or Elena can halt the workflow from HubSpot with a single flag. Quality review: Elena audits weekly aggregate accuracy.

---

## Describe the V1 Artifact

If you cannot describe what the first working version actually produces, the design is not finished — this field forces that decision.

1. Name what the first working version produces: an interface, a formatted document, an automated pipeline, a dashboard.
2. State where it lands and within what timeframe of the trigger.
3. State who acts on it next — what the human does with the artifact before the work leaves the building.

> **Meridian — V1 Artifact:** A draft PDF quote in Meridian's standard format, placed in Elena's HubSpot review queue within 2 hours of RFQ receipt. Elena approves or marks for revision before the quote leaves the building.

---

## Before you call it done

Run this test before the Brief leaves your hands for Build:

- **All seven sections have content.** No blanks. An empty section is a decision a builder will make under build pressure, and it won't match what Design intended.
- **Every section came from your Design artifacts, not from guessing** — the swim lane, the Hybrid Accountability Chart, the governance decisions, the Signal targets. If you had to invent any of it, Design isn't finished. Go back.
- **The V1 artifact is describable.** If you can't say what the first working version actually produces, the design isn't done.
- **A builder who's never met your business could start from this alone** — with no ambiguity meetings and no mid-build design decisions.

When all four are true, the Brief is the artifact. Build inherits this document as is. (Next: a six-field mini-spec for every agent on your Hybrid Accountability Chart.)
