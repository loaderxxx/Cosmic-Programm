# Flight Software Framework v1.0

## Purpose

Flight software is treated as a critical part of the system, connecting control, data, autonomy and safe modes.

## Architectural layers

1. hardware drivers;
2. middleware;
3. subsystem control;
4. state estimation;
5. planning;
6. autonomy rules;
7. data processing;
8. communications management;
9. diagnostics;
10. fault management;
11. safe mode.

## Requirements

Every critical software component must have:
- a defined input;
- a defined output;
- timing constraints;
- invalid-data handling;
- failure behaviour;
- logging;
- a version;
- test coverage.

## Autonomy

Autonomous functions must be constrained by explicitly defined states and transitions.

For each action, record:
**condition → decision → action → expected result → result monitoring → fallback.**

## Safety

Critical commands must pass admissibility checks. The nominal and emergency control paths must be separated.

## Verification

Minimum path:
unit test → integration test → software-in-the-loop → hardware-in-the-loop → system test → operational data.

Status: FRAMEWORK.
