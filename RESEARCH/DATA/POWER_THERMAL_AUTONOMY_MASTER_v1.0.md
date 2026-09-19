# Power, Thermal and Autonomy Master v1.0

## Power

Every mission shall maintain:
- generation budget;
- battery/storage budget;
- peak and average loads;
- eclipse survival;
- distribution losses;
- load shedding;
- safe-mode power;
- end-of-life degradation margin.

## Thermal

Every mission shall document:
- hot/cold cases;
- internal dissipation;
- external heat inputs;
- radiative surfaces;
- conductive paths;
- heaters;
- survival configuration;
- thermal-vacuum verification.

## Autonomy

The public architecture treats autonomy as a layered capability:

1. health monitoring;
2. fault detection;
3. fault isolation;
4. safe-state transition;
5. recovery;
6. navigation and state estimation;
7. autonomous sequencing;
8. mission-level decision support.

Autonomy must have explicit failure cases and test evidence. A claim that a system is 'autonomous' is not sufficient engineering evidence.

## Cosmic first-generation focus

The orbital demonstrator should generate real telemetry and fault-injection data for these three domains before lunar deployment.
