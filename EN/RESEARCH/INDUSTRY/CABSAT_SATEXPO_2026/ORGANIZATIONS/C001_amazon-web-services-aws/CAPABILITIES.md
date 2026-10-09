# Amazon Web Services (AWS) | Public technical capability map

Research stage: Company/vendor primary product source (attributed claims). No laboratory qualification or runtime product evaluation was performed by COSMOSYNTH.

## Capability components from source materials

1. **AWS Ground Station API and managed contacts** — published organisation / manufacturer description.
2. **Digital Twin scheduling & error-handling test** — published organisation / manufacturer description.
3. **EventBridge contact events** — published organisation / manufacturer description.
4. **RF dataflow services in production mode** — published organisation / manufacturer description.

## System boundaries

- **Ground-station systems and operations**: Stations, scheduling, antenna interfaces, gateways or operational support. Before integration, obtain model/version, interface/control documentation, supported operating environment and independent tests.
- **Managed cloud ground-station service**: Reservation APIs, ground contact events and cloud integration. Before integration, obtain model/version, interface/control documentation, supported operating environment and independent tests.

## Interoperability cannot be inferred from a sector label

- A satellite operator's orbit/capacity service is distinct from satellite modem hardware and mission flight software.
- Products with common labels (VSAT, phased array, Digital IF, GEO/LEO) may have different frequencies, protocols, licences, environments and API profiles.
- No equipment, firmware, API, SLA, orbit availability, funding or flight-qualification claim has been independently tested or procured by COSMOSYNTH.

## Technical unknowns to resolve

Digital Twin onboarding required; DOES NOT deliver data or telemetry in virtual test.

## Source

- [Product / corporate primary reference](https://docs.aws.amazon.com/ground-station/latest/ug/digital-twin.html)
- [Full public source log](SOURCES.md).
