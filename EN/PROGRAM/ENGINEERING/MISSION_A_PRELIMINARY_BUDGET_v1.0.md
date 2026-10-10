# Mission A — Preliminary Engineering Budget v1.0

## Purpose
This document converts the “Orbital Autonomy and Logistics Demonstrator” concept into a measurable engineering object. All numerical values, except those explicitly identified as assumptions, must be supported by calculation, testing or a primary source.

## System boundaries
Mission A should demonstrate in orbit:
- autonomous mode management;
- power supply and distribution;
- communications and transmission of telemetry/payload data;
- attitude control;
- execution of commands under delays and communications loss;
- safe recovery from deliberately simulated faults;
- a modular interface for future payloads.

## Budgets
| Budget | What to include | Rule |
|---|---|---|
| Mass | platform, power system, communications, computer, ADCS, payload, cables, fasteners, margin | nominal + margin |
| Power | generation, storage, distribution, computing, communications, actuators, thermal control | average and peak power |
| Data | telemetry, commands, technical data, service protocols | include overhead and retransmission |
| Communications | link budget, windows, data rate, coding, margin | do not assume a guaranteed link |
| Reliability | single failures, degradation, safe mode, recovery | critical failures must have a response |

## Mass breakdown
1. structure;
2. electrical power;
3. ADCS;
4. communications;
5. onboard computer;
6. software and memory;
7. thermal control;
8. payload;
9. cable harness;
10. adapters and interfaces;
11. margins.

Numerical limits are set after selecting the orbit, launch vehicle and available adapter. Do not force the architecture to fit an arbitrary mass.

## Power breakdown
For each mode, define baseline, average and peak loads, peak duration, available generation, storage capacity, energy margin and behaviour following loss of generation.

Minimum modes: launch/deployment, nominal, high-data-rate transmission, autonomous operation, safe mode and recovery.

## Readiness criterion
Every significant budget row must include: value → unit → source/calculation method → uncertainty → margin → verification status.

Status: CONCEPTUAL / requires calculation.
