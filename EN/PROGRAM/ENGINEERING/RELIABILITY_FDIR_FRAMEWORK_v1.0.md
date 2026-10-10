# Reliability and FDIR Framework v1.0

## Purpose

FDIR: fault detection, fault isolation and recovery.

## Chain

**Observation → anomaly detection → classification → isolation → transition to a safe state → recovery → confirmation of the result.**

## Failure classes

- sensor;
- actuator;
- power;
- computer;
- memory;
- communications;
- overheating;
- radiation event;
- software error;
- mechanical degradation.

## For every failure

Record:
- symptom;
- data source;
- detection time;
- false-positive conditions;
- allowable response time;
- FDIR action;
- residual functionality;
- recovery method.

## Safe states

Safe mode must explicitly define:
- power consumption;
- attitude;
- communications;
- the minimum active system set;
- exit conditions;
- limits on autonomous actions.

## Verification

Every critical scenario must be reproduced in a model or on a test bench and, where possible, in the integrated system.

Status: FRAMEWORK.
