# Capability map

[Atlas](../README.md) · [English](https://github.com/loaderxxx/Cosmic-Programm/blob/main/ATLAS/CAPABILITIES/README.md) · [Русский](https://github.com/loaderxxx/Cosmic-Programm/blob/lang/ru/ATLAS/CAPABILITIES/README.md) · [العربية](https://github.com/loaderxxx/Cosmic-Programm/blob/lang/ar/ATLAS/CAPABILITIES/README.md)

**Start with the required function, not a preferred vendor.** This browsing taxonomy organizes the capabilities discussed in the public industry research. It is not a qualification matrix or proof that every listed company can supply a complete system.

| ID | Capability family | What an engineering review must establish |
|---|---|---|
| MISSION_SIM | Mission simulation | Model scope, assumptions, fidelity and reproducibility. |
| MISSION_C2 | Mission command and control | Command authority, state ownership, telemetry and recovery boundaries. |
| LINK_BUDGET | Link-budget analysis | Frequencies, units, losses, margins and scenario assumptions. |
| NETWORK_ORCHESTRATION | Network and contact scheduling | Resource ownership, priorities, conflicts and replanning. |
| GROUND_STATION | Ground-station systems | Antenna, RF, tracking, monitoring and interface responsibilities. |
| GROUND_CLOUD | Managed ground services | Access, scheduling API, data paths and service limits. |
| VSAT_BASEBAND | Modems and baseband networks | Waveform, hub family, terminal support and version compatibility. |
| TERMINAL_ANTENNA | Antennas and terminals | Tracking, pointing, bands, environment and applicable approvals. |
| RF_HARDWARE | Radio-frequency hardware | Power, noise, bandwidth, connectors and operating conditions. |
| DIGITAL_IF | Digital intermediate-frequency processing | Packet profile, timing, context, sample encoding and transport. |
| SATELLITE_OPERATOR | Satellite capacity and services | Coverage, orbit, capacity, service availability and commercial scope. |
| EARTH_OBSERVATION | Earth observation and data | Resolution, revisit, tasking, licensing, quality and user need. |
| SYSTEMS_ENGINEERING | Systems engineering | Requirements, interfaces, budgets, verification and configuration control. |
| NETWORK_INTEGRATION | Network integration | Responsibility boundaries, monitoring, failover and support. |
| INDUSTRY_ASSOCIATION | Industry knowledge and standards | Scope of guidance, membership or certification; no implied accreditation. |
| CYBER_MONITORING | Security and monitoring | Assets, threat model, access control, logging and response ownership. |

## Use the map

For a mission-software question, inspect the Antaris and INTEGRASYS source records. For ground-system options, inspect Calian, SatService, Celestia TTI and AWS. For terminals and RF, inspect AvL, ETL and the component records. For services and data, inspect the operator and Earth-observation records. These are reading routes through the [organization directory](../ORGANIZATIONS/README.md), not preferred-supplier selections.

One organization may cover several functions; two organizations may overlap only partly. Absence of a tag means the capability has not been established in this research, not that the organization lacks it. Do not convert a sparse research map into a ranking of supplier strength.

**Next step:** choose a [system option](../SYSTEM_OPTIONS/README.md), define the interface, inspect primary specifications and write the smallest discriminating test. The [original technical knowledge map](../../RESEARCH/PUBLIC_TECHNICAL_KNOWLEDGE_MAP.md) and [programme capability matrix](../../PROGRAM/ARCHITECTURE/CAPABILITY_MATRIX_v1.0.md) are separate, original-language documents about programme architecture, not this industry qualification dataset.
