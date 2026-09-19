# Communications Master v1.0

## Link-budget chain

Each mission should document:

transmit power → antenna gain → path loss → pointing loss → polarization/implementation loss → atmospheric/space losses where applicable → receiver gain/noise → Eb/N0 or equivalent margin → achievable data rate.

## Mission data products

Separate:
- housekeeping telemetry;
- engineering telemetry;
- command traffic;
- payload science data;
- navigation/ranging data;
- contingency communications.

## Ground architecture

Define:
- spacecraft radios;
- antennae;
- ground stations;
- network routing;
- mission control;
- data archive;
- time synchronization;
- command authorization;
- degraded-mode communications.

## Evidence rule

Data-rate numbers are meaningless without frequency band, modulation/coding, range, antenna assumptions and link margin. The public repository therefore records the assumptions with each communications figure.
