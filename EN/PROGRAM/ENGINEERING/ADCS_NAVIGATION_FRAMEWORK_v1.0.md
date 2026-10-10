# ADCS and Navigation Framework v1.0

## Purpose

A public engineering framework for selecting and verifying the attitude determination, attitude control and navigation system.

## Functional chain

**State determination → state estimation → attitude planning → control → actuators → result measurement → error detection → safe mode.**

## Sensors

Consider:
- Sun sensors;
- gyroscopes;
- accelerometers;
- magnetometers for low-orbit applications;
- star trackers;
- GNSS where available;
- radio navigation;
- optical/lidar methods for specialized modes.

For each sensor, record accuracy, update rate, latency, failure modes, temperature dependence and conditions of applicability.

## Actuators

Consider:
- reaction wheels;
- magnetic actuators;
- microthrusters;
- specialized drives.

For each, record torque range, saturation, consumption, service life, vibration and failure states.

## Modes

At minimum, verify:
1. initialization;
2. stabilization;
3. Earth pointing;
4. Sun pointing;
5. high-precision attitude control;
6. manoeuvre;
7. sensor loss;
8. actuator loss;
9. safe mode;
10. recovery.

## Navigation

For each mission, define:
- absolute state;
- relative state;
- time source;
- coordinate frame;
- transformations between frames;
- allowable position error;
- allowable velocity error;
- allowable attitude error;
- allowable latency.

## Verification

Simulation, software-in-the-loop, hardware-in-the-loop and testing of flight-like hardware are required where necessary.

Status: FRAMEWORK.
