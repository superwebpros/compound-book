Compound · Build / Specification

# Write the Eight-Section Build Spec

*Turn the locked Design Brief into a developer-ready specification a builder can start from without asking a single question.*

The Build Spec is one of two instruments Build runs on, and it's the first. It restates the workflow, systems, and data from the Design Brief precisely enough that a builder can begin, then adds three sections Design doesn't own: what each agent handles, what happens when things break, and where the build runs. If the spec is right, the build is mostly execution. If it's wrong, the build is mostly negotiation.

**Before you start, you need a locked Design Brief.** The Design Brief is the single upstream input. If you can't fill Sections 1–3 from your Design artifacts without guessing, Design isn't done — stop and finish it. And one standing rule: if the Build Spec and the Design Brief ever disagree on a workflow step or a system boundary, **the Design Brief wins**, and the gap routes back to Design.

Fill the eight sections in order. An empty section is a decision the builder will make under build pressure, and those decisions almost never match what Design intended.

---

## Section 1: Write the workflow summary

Give any builder a plain-language, end-to-end picture of what they're building before they touch anything.

1. Write one paragraph: what this workflow does, trigger to final output, in plain language. No jargon.
2. Name each step and each agent in sequence, including the human review and approval, so the path is unambiguous.
3. Apply the test: a builder who knows nothing about your business should read it and understand what they're building. If they couldn't, rewrite it.

> **Meridian — Workflow Summary:** When a new RFQ arrives through the standardized intake form, a CRM record is created and the quoting workflow triggers automatically. The Quote Research Agent pulls customer history and matches the RFQ against three years of historical jobs in the ERP. The Quote Pricing Agent applies the rate card, the senior engineer's labor estimate, and the applicable pricing exceptions. The Quote Assembly Agent formats the draft as a PDF and places it in the VP of Operations' review queue. She reviews, edits if needed, and approves. The approved quote routes to the sales lead for customer delivery.

---

## Section 2: Define the inputs

Specify exactly what triggers the workflow and what data enters it, so the builder knows where to reach and how to access it.

1. Name the trigger: what kicks the workflow off, and how it arrives.
2. List every data source that enters the workflow, in what form, and from which system. Include rough volume where it matters (years of history, record counts).
3. For each source, note where the data lives and how the builder accesses it.

> **Meridian — Inputs:** Inbound RFQ (submitted via standardized intake form, parsed into HubSpot CRM as a new deal record), ERP job costing history (three years, roughly 800 completed jobs), current rate card (maintained by finance in JobBOSS ERP), cleaned pricing exceptions database (112 validated customer-specific rules, sourced from the VP's spreadsheet), senior engineer's labor hour estimate (submitted via structured form), and CRM customer history including win/loss records.

---

## Section 3: Define the outputs

Lock the deliverable's form, destination, and recipient so the build can't drift toward something the supervisor can't use.

1. State what the workflow produces and what form it takes.
2. Name where it lands and who receives it.
3. Itemize what the output must contain — the line items, scores, flags, or attachments the recipient needs to act on it.

> **Meridian — Outputs:** A draft PDF quote in Meridian's standard format, landing in the VP of Operations' CRM review queue. It contains a line-item breakdown (materials, labor, overhead, margin), a confidence score (the agent's own estimate of how sure it is about an output) reported as high/medium/low, the closest historical job matches with pricing, and any exception rules applied. Plus a flag for any input the agent could not resolve.

---

## Section 4: Set agent scope boundaries

State what the agent handles and what it cannot decide, preventing over-prescription that kills agent effectiveness.

1. For each agent, name what it handles and what decisions it makes.
2. Write the hard limits: what no agent is permitted to decide or do.
3. Frame all of this as scope boundaries, not step-by-step procedure. Agents over-prescribed at the step level lose the flexibility that makes them effective.

> **Meridian — Agent Scope:** Quote Research matches the RFQ to historical jobs by spec, materials, and complexity, and surfaces customer context and pricing terms. Quote Pricing calculates the draft price using historical matches, rate card, labor estimates, and exception rules. Quote Assembly generates the formatted PDF. No agent sets a final price, overrides the rate card, applies undocumented exceptions, or sends anything to a customer.

---

## Section 5: Name the human supervisor role

Identify who reviews, what they review for, and what the handoff looks like — the accountability anchor for the whole build.

1. Name the person (and their title) who reviews the output.
2. List exactly what they review for, and the expected time per review.
3. Define the handoff: where the output lands, in what form, on what timeline — plus the escalation routes for the outputs they don't approve themselves.

> **Meridian — Human Supervisor Role:** Elena Ruiz, VP of Operations, reviews every draft quote. Reviews for scope interpretation, pricing accuracy, confidence score, and exception rule application. Expected review: fifteen to twenty minutes per quote, down from three hours when she built quotes from scratch. Escalation: low-confidence quotes get her full manual review; non-standard materials route to the senior engineer; strategic account pricing goes to the CEO.

---

## Section 6: List every system and integration

Document read/write access, authentication method, and data sensitivity for every system touched so nothing is wired by assumption.

1. List every system the workflow touches.
2. For each, mark read access, write access, or both, and the authentication method.
3. Assign each system a data sensitivity classification (e.g., low / medium / high).

> **Meridian — Systems and Integrations:** HubSpot CRM (read/write: customer records, RFQ intake, quote pipeline, delivery queue), JobBOSS ERP (read: historical job costing, rate card, materials pricing), Claude Team workspace (single project with three defined workflows), n8n (workflow orchestration and system connectors). Sensitivity: pricing data is medium; everything else is low.

---

## Section 7: Document the failure modes

Pre-decide what happens on every edge case and outage so the builder wires escalation paths instead of improvising them under pressure.

1. List the edge cases and outages the workflow will hit: missing data, unknown inputs, a system being down, low-confidence output, out-of-range results.
2. For each, write what the agent does, who it escalates to, in what form, and on what timeline.
3. Note what the builder must wire to make each escalation path possible.

> **Meridian — Failure Modes:** No similar historical jobs found: agent flags as "insufficient for rapid estimate" and routes to the VP for full manual review. Unknown material (e.g., Inconel): agent produces no price estimate for that line item and flags as "manual pricing required." ERP API down: RFQs queue in the CRM, and the agent processes them when the connection restores. Confidence score below 60%: draft routes to the VP with a warning flag. Pricing deviation greater than 15% from closest historical match: agent flags the deviation, and the VP investigates before approving.

---

## Section 8: Specify the environment and constraints

Lock which specific platform within Design's category the build runs on and any data residency, license, or security constraints.

1. Name the specific environment inside Design's category (off-the-shelf, low-code, hand-built — see the Designing the System chapter), and why.
2. List any builder resourcing the environment requires (existing licenses, a freelance developer, internal team).
3. Write every constraint the builder must observe: data residency (legal or regulatory requirements that your data stay in a specific geography or on servers you control), existing licenses, internal security requirements. Flag any prerequisite that must be true *before* build begins.

> **Meridian — Environment and Constraints:** Low-code category, run via n8n (existing license) and Claude Team. Freelance n8n developer for three days of API wiring to HubSpot and JobBOSS. All data stays in existing systems. The pricing exceptions spreadsheet must be cleaned and validated before build begins. That's a prerequisite, not a build task.

---

## Before you call it done

Run this test before the spec leaves your hands for a builder:

- **All eight sections have content.** No blanks. An empty section is a decision the builder makes under pressure — and it won't match Design.
- **Sections 1–3 came from your Design artifacts, not from guessing.** If you had to invent any of it, Design isn't finished. Go back.
- **Nothing contradicts the Design Brief.** If the spec and the Brief disagree on a workflow step or system boundary, the Brief wins and the gap routes back to Design.
- **A builder who's never met your business could start from this alone** — engineer, vendor, or low-code assembler — with no ambiguity meetings and no mid-build design decisions.

When all four are true, the spec is the artifact. Hand it off. (Next instrument: the seven-question Guardrails Checklist.)
