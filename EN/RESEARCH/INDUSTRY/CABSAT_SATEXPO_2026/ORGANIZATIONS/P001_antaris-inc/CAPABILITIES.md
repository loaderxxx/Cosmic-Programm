# Antaris, Inc. | Public technical capability map

Research stage: Company/vendor primary product source (attributed claims). No laboratory qualification or runtime product evaluation was performed by COSMOSYNTH.

## Capability components from source materials

1. **TrueTwin mission digital twin** — published organisation / manufacturer description.
2. **Flight-software-in-the-loop simulation** — published organisation / manufacturer description.
3. **SatOS and Command Center mission operations** — published organisation / manufacturer description.
4. **Scenario testing before flight** — published organisation / manufacturer description.

## System boundaries

- **Virtual spacecraft and scenario modelling**: Orbit state, spacecraft behaviour, ground simulation events. Before integration, obtain model/version, interface/control documentation, supported operating environment and independent tests.
- **Satellite mission command and control**: Operational tasks and mission state; implementation-specific interfaces unknown. Before integration, obtain model/version, interface/control documentation, supported operating environment and independent tests.
- **Mission/ground system engineering**: Requirements, interface control, integration and verification. Before integration, obtain model/version, interface/control documentation, supported operating environment and independent tests.

## Interoperability cannot be inferred from a sector label

- A satellite operator's orbit/capacity service is distinct from satellite modem hardware and mission flight software.
- Products with common labels (VSAT, phased array, Digital IF, GEO/LEO) may have different frequencies, protocols, licences, environments and API profiles.
- No equipment, firmware, API, SLA, orbit availability, funding or flight-qualification claim has been independently tested or procured by COSMOSYNTH.

## Technical unknowns to resolve

Orbit dynamics fidelity, deployment model, SDK/telemetry APIs and commercial access not verified.

## Source

- [Product / corporate primary reference](https://docs.antaris.space/truetwin-technology)
- [Full public source log](SOURCES.md).
