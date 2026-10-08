# Decisions

## D-001 — Capability-compounding architecture

Date: 2026-09-19
Status: ACTIVE

Decision: prioritize reusable capabilities that compound across destinations rather than optimize for one flagship mission.

Rationale: power, logistics, autonomy, ISRU, manufacturing and habitation can support many future missions.

Uncertainty: exact sequencing and economic optimum remain unproven.

## D-002 — Separate baseline from radical concepts

Date: 2026-09-19
Status: ACTIVE

Decision: maintain a radical-concepts portfolio but do not promote speculative technology into the baseline without evidence.

## D-003 — Public repository with protected private core

Date: 2026-09-19
Status: ACTIVE

Decision: Cosmic Programm may be public while proprietary implementation, security-sensitive material and protected IP remain private.

## D-004 — Evidence before escalation

Date: 2026-09-19
Status: ACTIVE

A concept advances through:
HYPOTHESIS → EXPERIMENT → EVIDENCE → ARCHITECTURE CANDIDATE → BASELINE

not through enthusiasm alone.

## D-005 — Trilingual research with English canonical branch

Date: 2026-10-08
Status: OWNER-APPROVED POLICY / repository integration through PR

Decision: from the first research step, maintain substantive English, Russian and Arabic editions in parallel. English is the priority and canonical GitHub `main`; dedicated Git branches `lang/ru` and `lang/ar` hold the localized editions.

Rationale: internationally usable English primary record plus Russian and Arabic research access with one auditable evidence chain, rather than delayed uncontrolled translations.

Evidence: direct owner instruction of 2026-10-08; implementation specification in [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md).

Uncertainty: historical `RU/` and `AR/` directories are not yet fully migrated and many technical documents are not yet available in every language. Branch existence is not full translation.

Next action: review and integrate this language policy, then migrate historical localized links only after a separate non-breaking audit. Review condition: repeated material source divergence or changed owner instruction.
