# Interfaces Master v1.0

Interfaces are treated as first-class engineering objects.

## Launch vehicle ↔ spacecraft
Track:
- payload envelope;
- mass and center-of-gravity constraints;
- mechanical attachment;
- electrical power;
- telemetry/command;
- separation system;
- acoustic/vibration/shock;
- acceleration;
- thermal environment;
- hazardous operations;
- contamination;
- access and integration timeline.

SpaceX's Starship User Guide explicitly provides preliminary volume, mechanical interface and payload-environment information. citeturn0search48

## Spacecraft ↔ payload
Track:
- structural mounting;
- electrical voltage/current;
- data protocol;
- command authority;
- time synchronization;
- thermal coupling;
- electromagnetic compatibility;
- payload safety inhibits;
- software/firmware boundaries.

## Ground ↔ spacecraft
Track:
- command path;
- telemetry;
- ranging/navigation;
- authentication;
- time;
- ground-station coverage;
- mission-control procedures;
- contingency communications.

## Design rule

An interface is not complete until both sides can independently implement and verify it from an Interface Control Document (ICD) or equivalent specification.
