# Interfaces Master Dataset v1.0

Interfaces are treated as engineering objects in their own right.

## Launch vehicle ↔ spacecraft

Track:
- payload envelope;
- mass and centre-of-gravity limits;
- mechanical attachment;
- electrical power;
- telemetry/commands;
- separation system;
- acoustics/vibration/shock;
- acceleration;
- thermal environment;
- hazardous operations;
- contamination;
- access and integration schedule.

The Starship User's Guide contains preliminary information on payload volume, mechanical interfaces and environments.

## Spacecraft ↔ payload

Track:
- structural attachment;
- electrical voltage/current;
- data protocol;
- command authority;
- time synchronization;
- thermal coupling;
- electromagnetic compatibility;
- payload safety interlocks;
- software/firmware boundaries.

## Ground ↔ spacecraft

Track:
- command channel;
- telemetry;
- ranging/navigation;
- authentication;
- time;
- ground-station coverage;
- mission-control procedures;
- backup communications.

## Design rule

An interface is not complete until both sides can independently implement and verify it from an Interface Control Document (ICD) or an equivalent specification.
