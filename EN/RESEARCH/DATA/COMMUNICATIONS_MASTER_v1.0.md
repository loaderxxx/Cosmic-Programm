# Communications Master Dataset v1.0

## Link-budget calculation chain

Every mission must document:

transmitter power → antenna gain → propagation losses → pointing losses → polarization/implementation losses → atmospheric/space losses where applicable → receiver gain/noise → Eb/N0 or an equivalent margin → achievable data rate.

## Mission data types

Distinguish:
- housekeeping telemetry;
- engineering telemetry;
- commands;
- payload science data;
- navigation/ranging data;
- emergency communications.

## Ground architecture

Define:
- onboard radios;
- antennas;
- ground stations;
- network routing;
- mission control centre;
- data archive;
- time synchronization;
- command authorization;
- degraded-mode communications.

## Evidence rule

A data-rate figure is meaningless without the frequency band, modulation/coding, range, antenna parameters and link margin. The public database therefore stores these assumptions alongside every communications figure.
