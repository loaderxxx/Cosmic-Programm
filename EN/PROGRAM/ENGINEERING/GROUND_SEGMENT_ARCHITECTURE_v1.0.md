# Ground Segment Architecture v1.0

## Purpose

The ground segment is treated as part of the space system, not as an auxiliary service.

## Layers

1. ground stations;
2. radio-frequency chain;
3. contact scheduling;
4. command path;
5. telemetry;
6. data processing;
7. storage;
8. health monitoring;
9. event analysis;
10. archive and data provenance;
11. simulator;
12. verification tools.

## Command path

A command must have:
- a unique identifier;
- a version;
- creation time;
- execution time;
- a source;
- an admissibility check;
- acknowledgement of receipt;
- an execution result.

## Telemetry

Distinguish:
- heartbeat;
- subsystem status;
- warnings;
- emergency events;
- experiment parameters;
- diagnostic data.

## Autonomy

The ground segment must support operation under:
- communications delay;
- temporary station unavailability;
- loss of some telemetry;
- a need for the spacecraft to enter safe mode.

## Data

Every significant dataset must preserve provenance:

**spacecraft → subsystem → measurement → time → configuration → processing → result.**

## Verification

The ground segment is verified together with flight software through end-to-end tests.

Status: FRAMEWORK.
