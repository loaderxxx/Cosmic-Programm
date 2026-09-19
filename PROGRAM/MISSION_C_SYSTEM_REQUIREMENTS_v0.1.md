# Mission C — Lunar Infrastructure Pathfinder — System Requirements v0.1

## Objective
Deploy a persistent modular lunar infrastructure node that can support later robotic missions.

## Core modules
- power generation/storage
- communications
- navigation/localization
- thermal survival
- payload interface
- autonomous controller
- optional rover
- resource-prospecting or small ISRU experiment

## Design benchmark
ESA Argonaut is a useful public reference: its published architecture targets roughly 1,500 kg delivered to the surface and a five-year surface lifetime, with power, communications and ISRU payloads among possible cargo types. citeturn0search7

## Preliminary target
Infrastructure payload: 100–500 kg, depending on final mission architecture.
Continuous power: 0.5–5 kW target range.
Surface lifetime: 1 year minimum target, stretch 3+ years.
Modular expansion: at least two future payload interfaces.

## Required capabilities
1. Survive lunar day/night thermal transitions.
2. Maintain communications.
3. Maintain power through defined environmental conditions.
4. Accept future payloads without redesign of the core node.
5. Support autonomous fault recovery.
6. Provide standardized data and power services.
7. Produce engineering/environmental telemetry.

## ISRU experiment
Only include ISRU if the preceding Scout demonstrates a clear resource target and the experiment can be isolated from the infrastructure's survival-critical functions.

## Gate
Infrastructure becomes an operational programme element only after a full environmental qualification campaign and a demonstrated repeatable interface test with a representative future payload.