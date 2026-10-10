# Cosmic Programm — Candidate First Missions v0.1

Date: 2026-09-19

## Design basis

The candidate missions use a capability-first architecture. NASA's current Moon-to-Mars process starts with future objectives, decomposes them into capabilities/functions/use cases, and then maps those capabilities to systems. NASA also maintains explicit architecture-driven technology and data gaps. citeturn0search2turn0search1

The programme therefore evaluates missions by what durable capability they create, not by the prestige of the hardware.

## Mission A — Orbital Autonomy & Logistics Demonstrator

### Objective
Demonstrate an autonomous orbital logistics node that can receive, monitor, communicate with and operate modular payloads.

### Core capabilities
- autonomous rendezvous/proximity operations
- standardized payload interface
- power/data distribution
- communications
- remote operations
- fault detection and safe mode
- long-duration autonomous operation

### What is bought
Launch service, basic spacecraft bus components, ground communications.

### What is developed
Mission software, payload interface, autonomous operations stack, operations procedures and selected payload.

### Why it matters
Creates reusable operational infrastructure without requiring a lunar mission as the first step.

### Success metric
A complete autonomous logistics cycle is demonstrated repeatedly with defined reliability and recovery criteria.

---

## Mission B — Lunar Resource Scout

### Objective
Deliver an autonomous payload to a lunar polar environment to characterize terrain, thermal conditions, illumination and volatile/resource indicators.

### Core capabilities
- precision landing
- hazard detection
- surface mobility
- communications
- power management
- autonomous navigation
- resource sensing

### Reference scale
ESA's Argonaut provides a useful public benchmark for future lunar logistics: up to 1,500 kg surface cargo, autonomous landing, and a five-year design lifetime for surface operations. This is a benchmark, not our proposed vehicle specification. citeturn0search4

### What is bought
Launch and, initially, lunar landing service.

### What is developed
Scientific/resource payload, data architecture, autonomy layer and mission operations.

### Success metric
Produce a validated resource/terrain dataset that changes the design of a subsequent infrastructure mission.

---

## Mission C — Lunar Infrastructure Pathfinder

### Objective
Deploy the first persistent modular infrastructure node on the Moon.

### Core modules
- power
- communications
- navigation/localization
- thermal survival
- robotic mobility
- standardized cargo/payload interfaces
- resource prospecting
- optional small ISRU experiment

### Architecture
Lander -> power node -> communications node -> rover -> payload interfaces -> resource experiment.

### Why it matters
This is the first mission that creates an extensible lunar system rather than a standalone science mission.

### Success metric
A later mission can arrive and connect to the infrastructure without replacing the original node.

---

## Capability matrix

| Capability | A: Orbital | B: Lunar Scout | C: Lunar Infrastructure |
|---|---:|---:|---:|
| Autonomous operations | High | High | High |
| Communications | High | High | High |
| Navigation | High | High | High |
| Robotics | Medium | High | High |
| Lunar landing | No | High | High |
| Surface power | No | Medium | High |
| ISRU | No | Prospecting | Demonstration |
| Modular interfaces | High | Medium | Very high |
| Cislunar logistics | Foundation | Foundation | Core |
| Mars relevance | Medium | High | Very high |

## Recommended architecture sequence

A -> B -> C is the cleanest capability-building sequence.

The programme should not build a proprietary heavy launcher first. Early missions can purchase launch and landing services while the programme builds the capabilities that are harder to buy as differentiated intellectual property: autonomy, interfaces, operations, data, payloads, resource models and infrastructure architecture.

## Programme metric

The key metric is:

**Capability unlocked per unit of development risk and capital.**

This is an internal planning metric, not a public ranking of existing programmes.

## Next design gate

Before selecting hardware, produce:
1. three mission-level requirements sets;
2. mass budget;
3. power budget;
4. data budget;
5. communications link budget;
6. reliability targets;
7. mission duration;
8. launch/landing service assumptions;
9. technology readiness assessment;
10. test and qualification plan.

## Public boundary

No Cosmic Programm proprietary algorithms, hidden prompts, private decision machinery or confidential partner information are included.
