# Programme and Engineering Risk Register v1.0

## Principal classes
| Class | Risk | What to verify |
|---|---|---|
| R1 | Incorrect input parameters | primary source, date, units, range |
| R2 | Insufficient power | average/peak power, storage, eclipse, margin |
| R3 | Inadequate communications link | link budget, windows, pointing, losses |
| R4 | Navigation/attitude error | ADCS, sensors, actuators |
| R5 | Computing-system failure | watchdog, redundancy, safe mode |
| R6 | Thermal incompatibility | worst-case hot/cold, transients |
| R7 | Radiation environment | dose, single-event effects, shielding |
| R8 | Interface incompatibility | mechanics, power, data, EMC/EMI |
| R9 | Insufficient verification | test coverage and correct test level |
| R10 | Supplier dependency | availability, interface, schedule, replacement |
| R11 | Unverified autonomy | HIL, flight-like environment, fault scenarios |
| R12 | Scaling error | transition to a repeatable system without verified data |

## Evidence rule
Every significant risk must have: triggering condition → observable effect → detection → mitigation → verification → residual uncertainty.

## Key principle
A successful launch alone does not demonstrate the architecture. Evidence consists of measured results that allow a verified capability to be transferred into the next mission.

Status: BASELINE / quantitative ranking follows acquisition of mission-specific data.
