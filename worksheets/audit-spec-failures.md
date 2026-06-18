Compound · Build / Specification

# Audit the Spec Against Seven Common Failures

*Run the completed Build Spec through seven checks that have each ended a Sprint early or gotten a system shut down — before a single thing is built.*

Every failure on this list has happened: it ended a Sprint early or produced a system the team killed within weeks. None of them are caught by looking at the build, because the build doesn't exist yet. You catch them by reading the spec against each failure, with the builder in the room.

**Before you start, you need a completed Build Spec — all eight sections filled.** This audit checks the spec, not the build. Walk through all seven checks with the builder present. Any check you can't clear is a gap that must be resolved *before* build begins, not patched after.

---

## Check 1: Search for existing capabilities before building

Prevents rebuilding what already exists — the most common implementation failure, and it's a research gap, not a technical one.

1. For each section of the spec that describes a capability, ask: does a tool, feature, or integration already do this?
2. Spend fifteen minutes searching — the platform's own features, existing integrations, the connectors your tools already ship with — before agreeing to build it.
3. Write down what you found and what's genuinely missing. Only the genuinely missing parts go into the build.

> **Meridian:** The quoting workflow ran on n8n alongside Claude Team. Rather than hand-build system connections, the team used n8n's standard connectors to reach HubSpot and JobBOSS — the integration already existed. The build was three days of wiring, not weeks of custom development.

---

## Check 2: Confirm the environment matches Design's category

Stops a builder from substituting a "cleaner" architecture for the one the spec actually calls for.

1. Read the category Design chose: off-the-shelf, low-code, or hand-built.
2. Confirm the environment named in the spec sits inside that category — match the environment to the category, not the other way around.
3. If anyone proposes a different approach because "it would be cleaner," the spec wins. Note the disagreement and route it back to Design rather than letting the builder decide.

> **Meridian:** Design chose the low-code category. Build ran it on n8n plus Claude Team — both inside that category — instead of a custom API integration. If a builder had proposed a hand-built integration because it would be "cleaner," the spec's category would have overruled it.

---

## Check 3: Verify the spec is complete before build starts

Every empty section becomes an on-the-fly decision that won't match Design's intent.

1. Walk all eight spec sections. Confirm each one has real content — no blanks, no placeholders.
2. For any thin or empty section, name the specific decision a builder would otherwise make under build pressure.
3. Resolve the gap with Design before build begins. Builders aren't designers; decisions made under build pressure don't match what Design intended.

> **Meridian:** The pricing exceptions database (112 validated customer-specific rules) had to be cleaned and validated *before* build began — it was flagged as a prerequisite, not a build task. An incomplete exceptions section would have forced the builder to guess at pricing rules under pressure.

---

## Check 4: Confirm the output lands where the work already lives

A workflow that outputs to a tool no one opens produces zero adoption regardless of technical quality.

1. Read the spec's output destination. Name the exact tool and place the deliverable lands.
2. Confirm that's where the supervisor and the team already do this work today — not a new tool they'd have to learn or remember to open.
3. If the output lands somewhere new, fix the destination now. Adoption of an output in an unopened tool is zero.

> **Meridian:** Draft quotes land in Elena Ruiz's CRM review queue — the same HubSpot pipeline she already works in every day. The output meets her where the work already lives, so reviewing it is part of her existing flow, not a new habit to build.

---

## Check 5: Verify Section 7 (failure modes) is populated

A build that only handles the happy path breaks on the first edge case.

1. Turn to Section 7 of the spec and confirm it lists the workflow's edge cases and outages — not just the smooth path.
2. For each listed case, confirm there's a defined response: what the agent does, who it escalates to, in what form, on what timeline.
3. If Section 7 is empty or thin, stop. Every workflow has edge cases, and the build will break on the first one Section 7 missed.

> **Meridian:** Section 7 was populated: no similar historical job routes to manual review; an unknown material like Inconel produces no estimate and flags "manual pricing required"; the ERP API going down queues RFQs until the connection restores. The happy path was never the whole spec.

---

## Check 6: Confirm the build handles real-world edge cases, not just the demo path

A demo shows the happy path; the build must handle missing data, system outages, and off-script inputs.

1. Pressure-test the spec against the messy reality: missing data, a system that's down, weird inputs, the supervisor on vacation.
2. For each, confirm the spec says what the build does — not what the demo would do.
3. Where the spec only describes the clean run, send it back to add the edge-case behavior before build proceeds.

> **Meridian:** The guardrails answered the off-script cases directly. A confidence score below the threshold routes the draft to Elena with a warning flag; a price deviating more than 15% from the closest historical match gets flagged for her investigation before approval. The build was specified for the weird inputs, not the demo.

---

## Check 7: Require testing against real inputs before declaring done

Synthetic and cherry-picked examples are not tests; last week's actual data is the only honest gate.

1. Define the test set: pull last week's *actual* records and requests, not synthetic data and not cherry-picked examples.
2. Run them through the build and compare the output to what the human supervisor would have produced.
3. Make passing this test the condition for "done." Don't declare the build finished until it has run against real inputs.

> **Meridian:** The quality measure was a weekly comparison of agent-drafted prices against Elena's final approved prices, with a target of substantive corrections on fewer than 10% of drafts within eight weeks. "Done" was defined against her real, approved quotes — not a demo run.

---

## Before you call it done

Run this test before the build begins:

- **All seven checks were walked with the builder present** — against the completed spec, not the build.
- **Every check cleared, or the gap is written down and routed.** A check that can't clear is a gap that gets resolved before build starts, not after.
- **Where the spec disagreed with Design, Design won** — the gap went back to Design rather than getting decided under build pressure.
- **The "done" condition is real inputs.** Last week's actual data is the gate, named before the build starts so no one is tempted to declare done on a demo.

When all four are true, the spec has survived the audit and Build can proceed.
