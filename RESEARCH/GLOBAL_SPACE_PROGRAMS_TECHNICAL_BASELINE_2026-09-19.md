# Global Space Programs — Technical Baseline 2026-09-19

Status: PUBLIC RESEARCH / TECHNICAL BASELINE
Classification: PUBLIC OUTPUTS ONLY
Private methodology: stored separately in Cosmic-Programm-Private-Core

## Publication boundary

This document intentionally contains technical facts, program structures, technologies, architectures, interfaces, capabilities, constraints and documented lessons.

It does **not** contain:
- private system prompts;
- internal task-processing algorithms;
- private decision procedures;
- protected research methodology;
- confidential partner information;
- unpublished commercial implementation details.

The document is a technical knowledge base about what the major programs are building and how the public systems work, not a description of how Cosmic Programm itself processes information.

---

# 1. Executive technical map

The current global exploration ecosystem can be understood as several partially overlapping stacks:

1. **Earth-to-orbit access** — Falcon 9, Falcon Heavy, Ariane 6, Soyuz/Angara, Long March, H-IIA/H3, PSLV/LVM3 and emerging commercial launchers.
2. **Reusable transportation** — Falcon 9 operational reuse; Starship/Super Heavy pursuing full rapid reuse; ESA Space Rider pursuing reusable uncrewed LEO operations.
3. **Crew transportation** — Orion/SLS, Crew Dragon/Falcon 9, Soyuz, Shenzhou, Gaganyaan, and commercial crew systems.
4. **Orbital infrastructure** — ISS, Gateway, commercial stations, communications/navigation constellations and planned national orbital stations.
5. **Lunar logistics** — NASA CLPS/HLS/Gateway, ESA Argonaut, JAXA lunar logistics, China's Chang'e/ILRS architecture, Korean and Indian lunar programs.
6. **Lunar resource utilization** — polar volatile mapping, regolith handling, oxygen/water extraction demonstrations, power systems and autonomous surface mobility.
7. **Mars science and infrastructure precursors** — orbiters, rovers, sample-return technologies, life-support research and autonomous operations.
8. **Deep-space science** — asteroid sample return, planetary orbiters, telescopes, heliophysics and outer Solar System missions.
9. **Space communications** — traditional RF networks increasingly complemented by optical/laser links and proliferated satellite networks.
10. **Industrialization** — in-space manufacturing, autonomous robotics, reusable logistics, depots, power generation and local-resource utilization.

The major architectural shift is from isolated missions toward **persistent infrastructure and reusable transportation**, with Moon/Mars programs increasingly designed as capability-building chains rather than single expeditions.

---

# 2. NASA — Moon to Mars / Artemis

## Program structure

NASA's current Moon to Mars Architecture has four major segments:

- Human Lunar Return
- Foundational Exploration
- Sustained Lunar Evolution
- Humans to Mars

The architecture is decomposed into major technical sub-architectures including autonomous systems and robotics, communications/PNT, data systems, habitation, human systems, ISRU, infrastructure, logistics, mobility, power, transportation and utilization.

## Core systems

### SLS + Orion
SLS provides heavy-lift launch capability for Orion. Orion is the crew vehicle for lunar missions and is designed to support later deep-space missions.

### Gateway
Gateway is a lunar-orbit infrastructure element intended to support crew transfer, science, logistics and future deep-space operations.

### Human Landing Systems
NASA uses commercial providers for lunar landing. SpaceX is developing Starship HLS; Blue Origin is developing Blue Moon for sustained lunar landing services.

### CLPS
Commercial Lunar Payload Services moves scientific and technological payloads to the lunar surface through commercial landers. This creates a distributed lunar logistics market rather than a single government lander architecture.

### Surface systems
NASA is developing next-generation spacesuits, rovers, surface tools, communications, power and autonomous systems.

## Technical pattern

NASA's architecture separates:
- transportation;
- orbital infrastructure;
- landing;
- surface mobility;
- power;
- communications/navigation;
- habitation;
- resource utilization.

This modularity allows different providers and technologies to satisfy capability gaps.

## Current 2026 context

Artemis II flew astronauts around the Moon in April 2026. NASA currently describes Artemis III as a 2027 low-Earth-orbit demonstration of commercial human landing systems, with Artemis IV targeted as the first lunar surface landing in the current architecture.

Sources:
- https://www.nasa.gov/humans-in-space/artemis/
- https://www.nasa.gov/moontomarsarchitecture-components/
- https://www.nasa.gov/moontomarsarchitecture-architecturedefinitiondocuments/

---

# 3. SpaceX — reusable transportation + Starlink + Starship

SpaceX is a private aerospace company rather than a national space agency, but its systems materially affect the global exploration architecture.

## Falcon 9

Falcon 9 uses:
- nine Merlin engines on the first stage;
- LOX/RP-1 propellants;
- autonomous flight control;
- grid fins for atmospheric re-entry control;
- landing legs and recovery operations;
- a restartable second-stage Merlin Vacuum engine.

SpaceX publishes a payload capacity of approximately 22.8 t to LEO for Falcon 9.

The major architectural contribution is operational first-stage reuse combined with high launch cadence.

## Dragon

Crew Dragon provides crew transportation to LEO and supports NASA commercial crew operations. Cargo Dragon supports ISS logistics.

## Starlink

Starlink is a large LEO satellite network using inter-satellite laser links on many spacecraft. The network is also becoming a communications layer for launch/test operations and future spaceflight missions.

NASA selected SpaceX laser communications hardware derived from Starlink technology for an Artemis III demonstration, illustrating technology transfer between a commercial constellation and government exploration infrastructure.

## Starship / Super Heavy

Super Heavy is the first stage of Starship:
- methane/LOX propulsion;
- 33 Raptor engines;
- designed for return to the launch site and tower catch;
- large propellant capacity;
- intended rapid reuse.

Starship:
- uses three sea-level Raptors and three vacuum Raptors;
- is designed for large payload volume;
- is intended for satellite deployment, lunar cargo, lunar landing and Mars transport;
- requires in-space propellant transfer for the highest-end mission concepts.

SpaceX's public 2026 updates describe Starship V3 propulsion, tank-volume, attitude-control and launch-mount changes aimed at increasing reuse, reducing refurbishment and enabling future in-space propellant transfer.

## Key technical lesson

SpaceX is pursuing a tightly integrated stack:
launch → recovery → reuse → high cadence → large payload → orbital refilling → lunar/Mars logistics.

That is materially different from a mission-by-mission architecture.

Sources:
- https://new.spacex.com/vehicles/falcon-9
- https://new.spacex.com/vehicles/starship
- https://new.spacex.com/updates
- https://www.nasa.gov/blogs/missions/2026/07/16/nasa-taps-spacexs-starlink-to-deliver-artemis-iii-imagery-from-orion/

---

# 4. ESA — Terrae Novae

ESA's Human and Robotic Exploration strategy is organized around:
- low Earth orbit;
- Moon;
- Mars.

Terrae Novae combines human exploration, robotic exploration, science and technology development.

## European Orion contribution

ESA supplies the European Service Module for NASA's Orion spacecraft, providing major spacecraft functions including propulsion, power and consumables support.

## Ariane 6

Ariane 6 has:
- Ariane 62 with two boosters;
- Ariane 64 with four boosters;
- Vulcain 2.1-powered core stage;
- Vinci-powered restartable upper stage;
- solid P120C boosters;
- modular payload configurations.

ESA publishes approximately 21.6 t to LEO for Ariane 64 and approximately 11.5 t to GTO.

The system prioritizes European autonomous access to space and institutional/commercial flexibility.

## Argonaut

Argonaut is ESA's lunar lander program.

Publicly described characteristics:
- autonomous lunar landing;
- cargo delivery;
- up to 1500 kg lunar surface payload for the stated design;
- planned Ariane 6 four-booster launches;
- south-polar mission concept;
- support for robotic and crewed lunar infrastructure.

Argonaut is significant because Europe is developing an independent end-to-end lunar surface logistics capability.

## Space Rider

Space Rider is an uncrewed reusable LEO laboratory:
- approximately two months in orbit;
- up to 600 kg payload;
- controlled environment;
- power, thermal control, telemetry and data services;
- re-entry and recovery of payloads;
- technology demonstration and in-space manufacturing research.

## ExPeRT / exploration preparation

ESA's exploration preparation work connects technology development, mission concepts, human exploration and robotic exploration. This is a pipeline from technology maturation to operational missions.

Sources:
- https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Terrae_Novae
- https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Exploration/Argonaut_Europe_s_lunar_lander_programme
- https://www.esa.int/Enabling_Support/Space_Transportation/Launch_vehicles/Ariane_6_overview
- https://spacetransportation.esa.int/space-rider/programme/

---

# 5. China — Chang'e / ILRS / Tianwen

China's program is increasingly organized around sustained lunar exploration and infrastructure.

## Chang'e

Chang'e missions have progressed from orbital exploration to soft landing, rover operations, sample return and increasingly complex polar missions.

### Chang'e-7

Public objectives include:
- lunar south-pole survey;
- water ice and volatile investigation;
- high-precision landing;
- rover mobility;
- hopping/flying exploration;
- permanently shadowed-region investigation;
- international scientific payloads.

### Chang'e-8

The mission is planned as a technology and science precursor for the International Lunar Research Station and includes lunar-resource-utilization experiments.

## International Lunar Research Station

The ILRS concept includes:
- lunar surface and orbital elements;
- transportation;
- power;
- communications;
- navigation;
- science;
- resource utilization;
- long-duration autonomous operation.

CNSA describes a basic model targeted for the 2030s and an expanded architecture later.

## Tianwen

China's planetary program includes Mars exploration and asteroid/deep-space missions. Tianwen-2 is a major asteroid exploration and sample-return mission.

Sources:
- https://www.cnsa.gov.cn/english/n6465652/n6465653/c10670178/content.html
- https://www.cnsa.gov.cn/english/n6465652/n6465653/c10573094/content.html
- https://www.cnsa.gov.cn/english/n6465652/n6465653/c10670333/content.html

---

# 6. Japan — JAXA

Japan's exploration stack combines:
- H3 launch capability;
- ISS logistics;
- HTV-X;
- lunar exploration;
- Gateway participation;
- science missions;
- human-spaceflight technology.

## HTV-X

HTV-X is the successor logistics spacecraft to Kounotori.

Publicly described improvements include:
- increased cargo capability;
- late cargo loading;
- post-transport orbital experimentation;
- future potential for Gateway logistics.

This makes the spacecraft more than a simple ISS cargo truck: it is designed as a reusable mission architecture element for multiple orbital roles.

## Lunar exploration

JAXA is involved in international lunar exploration and lunar resource/technology programs, including cooperation with NASA and ISRO.

Source:
- https://global.jaxa.jp/projects/iss_human/htv-x/index.html

---

# 7. India — ISRO

## Gaganyaan

Gaganyaan requires:
- human-rated launch vehicle;
- crew escape system;
- habitable orbital module;
- life-support system;
- crew selection/training;
- extensive qualification and ground testing.

ISRO explicitly uses uncrewed missions to demonstrate technologies and verify safety and reliability before crewed flight.

2026 qualification work includes crew-module structural and recovery-system testing. ISRO reports more than 8000 ground tests across the program.

## Lunar and planetary exploration

India is continuing Chandrayaan development, lunar polar resource studies, Venus exploration preparation and cooperation on lunar exploration technologies.

ISRO's 2026 planning documents include Chandrayaan-4, Chandrayaan-5 and Venus Orbiter Mission development.

## Ecosystem

India is also expanding private-sector participation, including launch, satellite and Earth-observation businesses.

Sources:
- https://www.isro.gov.in/FAQ_Gaganyaan.html
- https://www.isro.gov.in/Tests_Crew_Module_systems_of_Gaganyaan_Mission.html
- https://www.isro.gov.in/media_isro/pdf/RTI/DDG_2026_27.pdf

---

# 8. Russia — Roscosmos

Russia's current architecture combines:
- ISS operations;
- Soyuz crew/cargo transportation;
- Angara launch systems;
- Earth-observation and communications constellations;
- Russian Orbital Station planning;
- lunar exploration plans;
- long-term launch and infrastructure modernization.

The Russian Orbital Station is intended as a multipurpose research and technology platform with potential autonomous operation.

Roscosmos has also described the Sfera satellite architecture, including broadband communications and Earth-observation components.

## Engineering lesson

The Luna-25 failure is an important publicly documented systems-engineering case. Roscosmos attributed the 2023 failure to a control-system issue involving accelerometer data and command-array handling, resulting in an incorrect propulsion burn duration and loss of the spacecraft.

This demonstrates the importance of:
- independent sensor validation;
- command-priority handling;
- fault detection;
- timing verification;
- end-to-end closed-loop testing;
- redundancy in navigation/control chains.

Source:
- https://www.roscosmos.ru/39790/

---

# 9. Canada / CSA

Canada's role is concentrated in high-value subsystems and robotics.

Major contribution areas include:
- Canadarm2;
- Canadarm3 / Gateway robotics;
- lunar surface mobility;
- lunar science;
- astronaut participation in Artemis.

The strategic pattern is specialization in robotic manipulation, mobility and infrastructure rather than maintaining an independent heavy-lift stack.

---

# 10. South Korea / KARI

South Korea has developed lunar exploration capability through KPLO/Danuri and is pursuing increasingly ambitious lunar landing and surface exploration systems.

The broader architecture is:
orbiter → communications/navigation/science → lander → rover → increasingly autonomous surface operations.

---

# 11. Commercial lunar ecosystem

Beyond the national agencies, a second architecture is forming around commercial lunar delivery.

Important categories include:
- commercial lunar landers;
- rideshare;
- robotic rovers;
- communications;
- navigation;
- surface power;
- payload hosting;
- lunar data services.

NASA's CLPS program is a major demand-side mechanism for this market.

The technical importance is that exploration infrastructure is becoming service-oriented: governments can purchase transportation or surface delivery as a service instead of developing every vehicle internally.

---

# 12. Technology map

## Launch

Key technologies:
- liquid propulsion;
- staged combustion;
- gas-generator cycles;
- methane/LOX;
- kerosene/LOX;
- cryogenic hydrogen/oxygen;
- solid boosters;
- reusable first stages;
- autonomous flight termination;
- precision landing;
- rapid turnaround.

## Propulsion

Major families:
- chemical;
- electric;
- nuclear-electric research;
- nuclear-thermal research;
- solar-electric;
- advanced/high-Isp concepts.

The central engineering trade is between thrust, specific impulse, power, vehicle mass, transfer time and system complexity.

## Power

Technologies:
- solar arrays;
- batteries;
- radioisotope power;
- fission surface power;
- regenerative energy systems;
- thermal management.

Lunar polar operations create a special requirement for long-duration power through shadowed periods.

## Communications

Technologies:
- S-band/X-band/Ka-band RF;
- relay satellites;
- optical/laser communications;
- inter-satellite links;
- navigation augmentation;
- proliferated LEO constellations.

## Autonomy

Applications:
- landing;
- navigation;
- terrain-relative navigation;
- surface mobility;
- fault detection;
- robotic construction;
- resource prospecting;
- mission planning;
- spacecraft scheduling.

## ISRU

Potential production chains include:
regolith → oxygen;
polar ice → water;
water → hydrogen/oxygen propellant;
local materials → construction feedstock.

The main bottlenecks are energy, excavation throughput, separation efficiency, thermal management, equipment mass, reliability and maintenance.

## Habitation

Key technologies:
- closed-loop life support;
- water recovery;
- atmospheric management;
- radiation protection;
- thermal control;
- fire safety;
- dust mitigation;
- crew health;
- food production.

## Robotics

Important categories:
- manipulators;
- rovers;
- excavation systems;
- construction robots;
- inspection systems;
- autonomous navigation;
- cooperative multi-robot systems.

---

# 13. Cross-program comparison

| Capability | NASA | SpaceX | ESA | China | JAXA | ISRO | Russia |
|---|---|---|---|---|---|---|---|
| Heavy launch | SLS | Falcon Heavy / Starship | Ariane 6 | Long March family | H3 | LVM3 | Angara |
| Operational reusable orbital booster | No | Falcon 9 | Emerging | Developing | Developing | Developing | Limited |
| Full-reuse heavy system | No | Starship target | Research/preparation | Developing | Research | Research | Research |
| Lunar crew architecture | Artemis | Starship HLS partner | Partner/contributor | Developing | Partner | Developing | Developing |
| Lunar logistics | CLPS/HLS/Gateway | Commercial + HLS | Argonaut | Chang'e/ILRS | HTV-X/Gateway | Lunar missions | Luna/Russian plans |
| Orbital infrastructure | ISS/Gateway | Starlink / commercial systems | ISS/Gateway contribution | Tiangong/ILRS | ISS/Gateway | Future station | ISS/Russian station |
| ISRU focus | High | High future focus | High | High | High | Growing | Planned |
| Optical comms | Demonstrated | Starlink operational | Developing | Developing | Developing | Developing | Developing |
| Autonomous robotics | High | High | High | High | High | Growing | High |
| Reusable laboratory | Commercial platforms | Dragon / Starship concepts | Space Rider | Developing | HTV-X orbital roles | Developing | Developing |

This table describes documented program characteristics; it is not a ranking.

---

# 14. Major technical bottlenecks across the ecosystem

1. **Launch cost and cadence** — reusable systems are changing economics, but true rapid full reuse remains difficult.
2. **Orbital refuelling** — essential for high-energy reusable lunar/Mars architectures.
3. **Cryogenic storage and transfer** — long-duration propellant management is a core infrastructure problem.
4. **Surface power** — especially lunar polar/night operations and Mars dust/seasonal effects.
5. **Autonomous landing and navigation** — increasingly important as communication delays and terrain complexity increase.
6. **Dust** — abrasive, electrostatic and operationally disruptive for seals, mechanisms, optics, suits and habitats.
7. **ISRU throughput** — laboratory proof is much easier than continuous industrial production.
8. **Radiation** — crewed Mars missions require substantially stronger protection and operational strategies.
9. **Closed-loop life support** — reliability over months/years is a different problem from short missions.
10. **Maintenance** — long-duration infrastructure needs repairable, modular systems and spare-parts strategies.
11. **Communications** — deep-space bandwidth and latency require autonomous local operations.
12. **Economic utilization** — infrastructure must generate enough recurring value to justify repeated transportation.
13. **System integration** — failures increasingly occur at interfaces between subsystems rather than inside isolated components.

---

# 15. Architectural observations for Cosmic Programm

## Observation A — Infrastructure compounds

Power, communications, mobility, logistics and local resources become more valuable when shared by multiple missions.

## Observation B — Reusability changes the architecture

Reusable transportation is not merely a cheaper rocket. It can change:
- mission frequency;
- vehicle design;
- logistics;
- spare-parts strategy;
- infrastructure utilization;
- economic models.

## Observation C — Lunar south-pole infrastructure is a convergence point

NASA, ESA, China and other programs increasingly investigate:
- water ice;
- permanently shadowed regions;
- power availability;
- communications;
- autonomous navigation;
- resource utilization.

## Observation D — Commercial and government systems are converging

Government agencies increasingly specify outcomes and capabilities while commercial organizations build and operate systems.

## Observation E — Autonomy is becoming infrastructure

Autonomy is no longer limited to rover navigation. It is moving into:
- spacecraft operations;
- communications;
- fault management;
- landing;
- logistics;
- surface construction;
- scientific operations.

## Observation F — The real long-term unit is the capability chain

A sustainable exploration architecture is increasingly:

launch → transport → orbital infrastructure → landing → power → communications → mobility → resource utilization → manufacturing → habitation → science → logistics.

---

# 16. Research backlog

The next technical research packages should quantify:

1. Earth-to-Moon mass flow.
2. Lunar polar power architectures.
3. Cryogenic propellant production and storage.
4. Oxygen extraction from regolith.
5. Water extraction from lunar ice.
6. Autonomous excavation throughput.
7. Lunar construction mass balance.
8. Mars surface power.
9. Mars atmospheric/resource utilization.
10. Radiation shielding mass.
11. Closed-loop life-support closure rates.
12. Deep-space communications architecture.
13. Reusable transportation turnaround requirements.
14. Orbital depot architectures.
15. Lunar cargo cost per delivered kilogram.
16. Mars cargo logistics.
17. Spare-parts and maintenance economics.
18. Multi-robot construction.
19. Space manufacturing.
20. Technology-readiness and dependency graph across the full architecture.

---

# Sources and primary references

NASA:
- https://www.nasa.gov/humans-in-space/artemis/
- https://www.nasa.gov/moontomarsarchitecture-components/
- https://www.nasa.gov/moontomarsarchitecture-architecturedefinitiondocuments/
- https://www.nasa.gov/reference/human-landing-systems/

SpaceX:
- https://new.spacex.com/vehicles/falcon-9
- https://new.spacex.com/vehicles/starship
- https://new.spacex.com/updates

ESA:
- https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Terrae_Novae
- https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Exploration/Argonaut_Europe_s_lunar_lander_programme
- https://www.esa.int/Enabling_Support/Space_Transportation/Launch_vehicles/Ariane_6_overview
- https://spacetransportation.esa.int/space-rider/programme/

CNSA:
- https://www.cnsa.gov.cn/english/n6465652/n6465653/c10670178/content.html
- https://www.cnsa.gov.cn/english/n6465652/n6465653/c10670333/content.html
- https://www.cnsa.gov.cn/english/n6465652/n6465653/c10573094/content.html

JAXA:
- https://global.jaxa.jp/projects/iss_human/htv-x/index.html

ISRO:
- https://www.isro.gov.in/FAQ_Gaganyaan.html
- https://www.isro.gov.in/Tests_Crew_Module_systems_of_Gaganyaan_Mission.html

Roscosmos:
- https://www.roscosmos.ru/
- https://www.roscosmos.ru/39790/
- https://www.roscosmos.ru/41521/

