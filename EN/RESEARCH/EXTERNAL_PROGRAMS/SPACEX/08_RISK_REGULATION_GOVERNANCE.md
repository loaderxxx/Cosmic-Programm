# SpaceX — Risk, Regulation and Governance

Date: **2026-09-22**  
Version: **v0.1**

> Complete translation of `RU/RESEARCH/EXTERNAL_PROGRAMS/SPACEX/08_RISK_REGULATION_GOVERNANCE.md`; source blob `716ce9b5c39c8ce084aa719e173ff5dd1bffcaa7`; snapshot `16073db5465c9bf0827f952a229bcded44dbd983`. Translation date: 2026-10-08. This preserves a dated research text, not current legal advice or a new regulatory audit. Independent human language review is pending.

## 1. Why regulation is part of the architecture

A rocket system cannot be considered an operational capability without:
- launch licensing;
- environmental review;
- range and airspace coordination;
- safety processes;
- government-customer requirements;
- mission authorization.

The FAA explicitly states that new Starship/Super Heavy operations require the appropriate permit or licence and environmental review.

Consequently:

**REGULATION → SYSTEM ARCHITECTURE**

rather than simply legal support.

## 2. NASA insight and oversight

In 2026, NASA OIG describes the HLS model as a tailored approach that gives providers substantial freedom in project management while retaining agency insight and oversight.

This is an interesting governance architecture:

**provider autonomy + external assurance.**

## 3. Where this model works

It is useful when:
- the provider owns the design;
- the provider can iterate rapidly;
- the customer defines mission requirements;
- an external body maintains safety and contract oversight.

It resembles the separation:

**HOW TO BUILD → provider**

**WHAT MUST BE SAFE / ACHIEVED → customer/regulator**

## 4. Why autonomy has a cost

NASA OIG also shows that high-risk technology can remain immature despite programmatic progress.

For example:
- cryogenic transfer;
- pad turnaround;
- integrated HLS maturity;
- crew safety and verification.

Therefore:

**Autonomy must be paired with evidence visibility.**

## 5. Cosmic Programm

Our programme can use:

**ENGINEERING AUTONOMY**
+
**STRICT EVIDENCE / V&V**
+
**PUBLICATION GATE**
+
**HUMAN APPROVAL FOR HIGH-CONSEQUENCE DECISIONS**

This is already part of our bootstrap architecture.

## 6. Risk taxonomy

For a SpaceX-style system analysis:

- technical;
- integration;
- operations;
- cadence;
- manufacturing;
- regulatory;
- safety;
- supply chain;
- economics;
- programme dependency.

## 7. A particular risk: dependency stacking

Starship HLS illustrates the chain:

vehicle
+ tanker
+ depot
+ transfer
+ pad cadence
+ flight test
+ crew integration.

Every new capability creates new dependencies.

Consequently:

**Architecture complexity grows faster than component count.**

## Open questions

- How much does regulatory latency affect launch cadence?
- Which requirements are most critical to the schedule?
- How are hazards closed before crewed operations?
- Which dependencies truly lie on the critical path?

## Sources

FAA:
https://www.faa.gov/space/stakeholder_engagement/spacex_starship

NASA OIG HLS Audit:
https://oig.nasa.gov/audits/nasas-management-of-the-human-landing-system-contracts/

[Russian source](../../../../RU/RESEARCH/EXTERNAL_PROGRAMS/SPACEX/08_RISK_REGULATION_GOVERNANCE.md) · [Arabic translation](../../../../AR/RESEARCH/EXTERNAL_PROGRAMS/SPACEX/08_RISK_REGULATION_GOVERNANCE.md)
