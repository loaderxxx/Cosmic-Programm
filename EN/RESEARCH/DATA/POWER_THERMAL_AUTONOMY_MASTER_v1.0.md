# Power, Thermal Conditions and Autonomy Master Dataset v1.0

## Power

Every mission must have:
- a generation budget;
- a battery/storage budget;
- peak and average loads;
- eclipse survival;
- distribution losses;
- non-essential load shedding;
- safe-mode power consumption;
- a margin for end-of-life degradation.

## Thermal conditions

Every mission must document:
- hot/cold cases;
- internal heat generation;
- external heat fluxes;
- radiating surfaces;
- conductive paths;
- heaters;
- survival configuration;
- thermal-vacuum verification.

## Autonomy

The public architecture treats autonomy as a layered capability:

1. state monitoring;
2. fault detection;
3. fault isolation;
4. transition to a safe state;
5. recovery;
6. navigation and state estimation;
7. autonomous sequence execution;
8. mission-level decision support.

Autonomy requires explicit failure scenarios and test evidence. Merely saying “the system is autonomous” is not engineering evidence.

## First-generation Cosmic focus

The orbital demonstrator must obtain actual telemetry and fault-injection data across these three areas before progressing to lunar missions.
