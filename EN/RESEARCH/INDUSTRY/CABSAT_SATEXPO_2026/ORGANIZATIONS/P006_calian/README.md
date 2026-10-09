# Calian — independent industry profile

*COSMOSYNTH / Cosmic Programm · Open-source industry research · Reviewed 8 October 2026.*

**Profile ID:** `P006`  
**Sector:** Space engineering / ground stations  
**Research maturity:** Company/vendor primary product source (attributed claims)  
**Show record:** Named in the SATExpo 2026 organizer exhibitor directory; booth and personal contacts not independently verified here.

> Independent analysis. COSMOSYNTH does not represent, endorse or claim an affiliation, contract or meeting with this organisation.

## Published capability snapshot

- Multi-orbit Orchestrator network resource management — attributed to the linked organisation / primary product documentation.
- EarthMesh space-ground link modelling — attributed to the linked organisation / primary product documentation.
- Pass scheduling and gateway visibility — attributed to the linked organisation / primary product documentation.
- Ground station engineering and mission operations — attributed to the linked organisation / primary product documentation.

## Architecture position (independent interpretation)

- **Satellite mission command and control.** Operational tasks and mission state; implementation-specific interfaces unknown. This is a value-chain classification, not a product compatibility test.
- **RF and/or optical link engineering.** Geometry, radio budgets, coverage and link conditions. This is a value-chain classification, not a product compatibility test.
- **Multi-orbit and network resource orchestration.** Resource allocation, carrier/routing decisions, ground contacts. This is a value-chain classification, not a product compatibility test.
- **Ground-station systems and operations.** Stations, scheduling, antenna interfaces, gateways or operational support. This is a value-chain classification, not a product compatibility test.
- **Digital intermediate frequency.** RF-over-IP IQ streams, packet timing, contextual metadata and interoperability. This is a value-chain classification, not a product compatibility test.
- **Mission/ground system engineering.** Requirements, interface control, integration and verification. This is a value-chain classification, not a product compatibility test.

## Publicly documented industry connections and comparisons

- [SatService GmbH](../P019_satservice-gmbh/README.md): **Reported ownership / acquisition**, 2019-04-01. Calian acquired SatService in April 2019; SatService identifies itself as a Calian Group company. *Status:* FACT. [Original source](https://www.calian.com/news-media/calian-group-expands-european-satellite-business-with-acquisition-of-germany-based-satservice/).

**Functional intersections (not necessarily formal relationships):**
- [INTEGRASYS](../P016_integrasys/README.md): **Interoperability claimed by supplier (not independently replicated)** — INTEGRASYS claimed DIFI compatibility with Calian digital IF hardware (2024). *Evidence:* [source A](https://www.integrasys-space.com/post/integrasys-releases-the-first-multi-vendor-difi-signal-analysis-virtualized-system), [source B](https://dificonsortium.org/). **Qualification:** SOURCE CLAIM / NOT INDEPENDENTLY TESTED; proposed interfaces require independent verification.
- [Antaris, Inc.](../P001_antaris-inc/README.md): **Comparable product functions (analytical comparison)** — Antaris mission C2/orchestration intersects with Calian mission scheduling and resource orchestration. *Evidence:* [source A](https://www.antaris.space/platform), [source B](https://www.calian.com/space/space-products-and-services/resource-orchestration/). **Qualification:** INTERPRETATION; proposed interfaces require independent verification.
- [INTEGRASYS](../P016_integrasys/README.md): **Comparable product functions (analytical comparison)** — Calian EarthMesh/Orchestrator and INTEGRASYS BestPath/BeamBudget overlap in multi-orbit network planning. *Evidence:* [source A](https://www.calian.com/space/space-products-and-services/resource-orchestration/), [source B](https://www.integrasys-space.com/bestpath). **Qualification:** INTERPRETATION; proposed interfaces require independent verification.
- [Amazon Web Services (AWS)](../C001_amazon-web-services-aws/README.md): **Comparable product functions (analytical comparison)** — Calian schedules contact/network resources while AWS Ground Station manages antenna contact reservation; scope differs. *Evidence:* [source A](https://www.calian.com/space/space-products-and-services/resource-orchestration/), [source B](https://docs.aws.amazon.com/ground-station/latest/ug/digital-twin.html). **Qualification:** INTERPRETATION; proposed interfaces require independent verification.

## Open questions

No published COSMOSYNTH integration or trials; APIs and commercial model unknown.

## Source and reading trail

- [Product / corporate primary reference](https://www.calian.com/space/space-products-and-services/resource-orchestration/)
- [Evidence and provenance](SOURCES.md)
- [Technical capability breakdown](CAPABILITIES.md)
- [All sourced ecosystem links and comparative overlaps](RELATIONSHIPS.md)

**Disclosure statement:** This is independently authored research based on public sources. It is not a vendor-issued or vendor-approved profile. Showcase or exhibition status and individual product claims have separate evidence standards.
