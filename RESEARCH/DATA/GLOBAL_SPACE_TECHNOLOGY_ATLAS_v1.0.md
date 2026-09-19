# Global Space Technology Atlas — Quantitative Baseline v1.0

Last verified: 2026-09-19

## Purpose

This file is the quantitative spine of the public Cosmic Programm space-technology database. It records public technical parameters and engineering relationships. It does not publish Cosmic Programm's private reasoning algorithms.

## 1. Earth-to-orbit transportation

| System | Architecture | Key public parameters | Technical significance |
|---|---|---|---|
| Falcon 9 | 2-stage LOX/RP-1 | 70 m; 3.7 m diameter; published LEO payload up to 22,800 kg | Reusable first-stage commercial launch architecture |
| Starship/Super Heavy | 2-stage reusable target | 124 m integrated; 9 m diameter; 100+ t published fully-reusable payload target | Very large reusable transportation + tanker architecture |
| Ariane 62 | 2 solid boosters + cryogenic core/upper stage | ~10.3 t LEO; ~4.5 t GTO | Modular European launcher |
| Ariane 64 | 4 solid boosters + cryogenic core/upper stage | ~21.6 t LEO; ~11.5 t GTO | Higher-capacity Ariane configuration |

SpaceX's published Starship specification lists 1,600 t propellant capacity for Starship, 3,650 t for Super Heavy, 8,240 tf Super Heavy thrust and 33 Raptor engines. ESA lists 21.6 t to LEO for Ariane 64. citeturn0search2turn0search4

## 2. Propulsion

| Engine/system | Propellant | Public parameter | Role |
|---|---|---|---|
| Raptor | CH4/LOX | 250 tf published thrust per engine | Starship |
| Vulcain 2.1 | LH2/LOX | 1,371 kN thrust; 468 s operation; 327+ kg/s consumption | Ariane 6 core |
| Vinci | LH2/LOX | Restartable upper-stage engine | Ariane 6 upper stage |
| Merlin family | RP-1/LOX | Reusable commercial launch engine family | Falcon |

ESA reports Vulcain 2.1 consumes over 327 kg/s and operates for 468 s; the hydrogen turbopump reaches 33,000 rpm and 15 MW. citeturn0search5

## 3. Lunar architecture

NASA currently defines four Moon-to-Mars segments:
- Human Lunar Return
- Foundational Exploration
- Sustained Lunar Evolution
- Humans to Mars

It also defines 12 sub-architectures covering autonomy/robotics, communications/PNT, data, habitation, human systems, ISRU, infrastructure, logistics, mobility, power, transportation and utilization. citeturn0search0

### Architecture chain

Earth launch -> crew/cargo transport -> cislunar infrastructure -> lunar orbit -> landing system -> surface power/communications -> mobility -> science/utilization -> logistics -> ISRU -> sustained operations -> Mars precursor.

NASA's 2026 architecture material explicitly provides technology-gap and data-gap spreadsheets, making these suitable targets for future machine-readable extraction. citeturn0search1

## 4. Starship as an integrated architecture

Published SpaceX data:
- integrated height: 124 m
- diameter: 9 m
- fully reusable payload target: 100+ t
- Super Heavy propellant: 3,650 t
- Starship propellant: 1,600 t
- Super Heavy engines: 33 Raptor
- Starship engines: 3 Raptor + 3 Raptor Vacuum
- published Super Heavy thrust: 8,240 tf
- published Starship thrust: 1,614 tf

The architecture also includes tanker-based on-orbit refilling. SpaceX states that refilling in LEO is intended to enable high-energy missions to Mars. citeturn0search2

## 5. European launch architecture

Ariane 6 is explicitly modular:
- Ariane 62: two boosters
- Ariane 64: four boosters
- core: Vulcain 2.1
- upper stage: restartable Vinci
- P120C/P160C solid booster family
- payload fairings: 5.4 m diameter, 20 m or 14 m variants

ESA reported a June 2026 Ariane 64 flight carrying 36 Amazon Leo satellites, using four upgraded boosters with 14 tonnes more propellant each. citeturn0search4turn0search6

## 6. Communications and navigation

The Atlas treats communications/PNT as an architecture-level dependency:
- Earth ground network
- orbital relay
- cislunar relay
- direct deep-space links
- optical communications
- autonomous relative navigation
- surface communication networks

NASA explicitly places communications and PNT among the 12 Moon-to-Mars sub-architectures. citeturn0search0

Future quantitative fields:
data rate, link distance, frequency/optical band, antenna aperture, terminal mass, terminal power, pointing accuracy, latency, availability, redundancy, navigation error.

## 7. Power

Future system records must distinguish:
- generated power
- continuous power
- peak power
- storage capacity
- eclipse survival
- thermal rejection
- distribution
- lifetime
- degradation

Power is a formal NASA Moon-to-Mars sub-architecture. citeturn0search0

## 8. ISRU

The public Atlas tracks:
resource -> extraction process -> energy input -> throughput -> product purity -> equipment mass -> autonomy -> demonstrated scale -> downstream use.

NASA defines ISRU as extracting resources in space or on the Moon/Mars to generate useful products. citeturn0search0

## 9. Mars transportation

NASA's public technical material currently considers multiple broad Mars transportation architectures, including nuclear thermal, hybrid nuclear-electric/chemical, hybrid solar-electric/chemical, and all-chemical approaches. These are technology-study categories, not a statement that one has been selected as the operational Mars vehicle. citeturn0search8

## 10. China status tracking

The Atlas must timestamp Chinese programme status rather than treating old schedules as current. CNSA reported on 23 August 2026 that Chang'e-7 did not meet launch conditions for its planned 2026 window. Earlier August material had described the integrated vehicle being moved to the launch area. This is a useful example of why mission status requires dated verification. citeturn0search9

## 11. Engineering dependency graph

### Transportation
Launch vehicle -> orbit -> transfer -> landing -> surface mobility.

### Energy
Generation -> storage -> conversion -> distribution -> thermal rejection.

### Information
Sensors -> compute -> navigation -> communications -> command/data handling.

### Autonomy
Perception -> localization -> planning -> control -> fault detection -> recovery.

### Resources
Imported consumables -> recycling -> local extraction -> processing -> manufacturing feedstock.

### Industrialization
Launch cadence -> manufacturing scale -> reuse -> orbital/cislunar logistics -> surface infrastructure -> resource utilization.

## 12. Data quality rules

1. Every numerical value must carry a source.
2. Configuration must be specified.
3. Orbit and mission profile must be specified for payload numbers.
4. Planned capability must be distinguished from demonstrated capability.
5. Company claims must be labelled as company-published claims.
6. Current status must be date-stamped.
7. Derived calculations must be clearly marked as derived.
8. Conflicting values must be retained with provenance rather than silently averaged.
9. TRL must not be invented when no authoritative assessment exists.
10. Public technical data must never be mixed with Cosmic Programm private algorithms.

## 13. Next expansion

The next database layer should add:
- Blue Origin / New Glenn / Blue Moon
- Firefly
- Intuitive Machines
- Rocket Lab
- Axiom Space
- Northrop Grumman
- KARI
- CSA
- UAE
- Australian Space Agency
- commercial Earth-orbit stations
- lunar relay/navigation systems
- nuclear surface power
- Mars EDL
- spacesuits/EVA
- cryogenic storage
- orbital propellant transfer
- sample return
- space manufacturing

The resulting Atlas should become a source-linked engineering knowledge graph rather than a static article.
