# Cosmic Programm ICD Framework v1.0

## Purpose

The Interface Control Document (ICD) defines subsystem boundaries and prevents hidden interface assumptions.

## Interface categories

### Mechanical
- fasteners;
- dimensions;
- mass;
- centre of mass;
- loads;
- vibration;
- deployment.

### Electrical
- voltage;
- current;
- inrush currents;
- peaks;
- grounding;
- protection;
- EMC/EMI.

### Data
- physical interface;
- protocol;
- data rate;
- latency;
- format;
- integrity checking;
- time reference.

### Thermal
- conductive interfaces;
- heat flows;
- allowable temperatures;
- radiators;
- insulation.

### Radio frequency
- frequency range;
- power;
- bandwidth;
- modulation;
- antenna;
- compatibility constraints.

## Interface rule

Every interface must have an owner on each side and a verifiable compatibility statement.

Record format:

**ID → requirement source → side A → side B → parameter → allowable range → verification method → status.**

Status: FRAMEWORK.
