# SpaceX — Starship and Orbital Logistics

Date: **2026-09-22**  
Version: **v0.1**

## Why Starship is more than a larger rocket

The public Starship architecture describes a reusable two-stage transportation system for Earth orbit and future Moon/Mars missions.

For HLS, NASA documentation adds a more complex logistics chain:
- lander;
- tanker launches;
- propellant aggregation/storage;
- cryogenic transfer;
- rendezvous/docking;
- lunar operations.

## Paradigm shift

Falcon simplification:

**Earth → orbit → payload**

Starship HLS:

**Earth → repeated tanker operations → orbital propellant aggregation → transfer → lander → lunar orbit → surface**

This is an **orbital logistics capability**.

## Hidden dependency

At the top level:

**lunar lander**

At system level:

**launch → tanker cadence → depot/storage → thermal control → rendezvous → transfer → measurement → propulsion → landing**

A small subsystem can become a critical path for the entire architecture.

## Cosmic Programm implication

Do not ask only:

**“Can we land an instrument?”**

Ask:

**“What must exist before, during and after the landing so that the next mission becomes easier?”**

That turns a mission into an infrastructure graph.

## Maturity boundary

Falcon operational reuse and Starship integrated orbital-logistics maturity are separate evidence categories.

## Open questions

- demonstrated propellant transfer;
- depot thermal performance;
- tanker turnaround;
- rendezvous reliability;
- campaign mass and cost;
- HLS reuse.
