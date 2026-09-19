# Engineering Parameters Master v1.0

Updated: 2026-09-19

Normalized public engineering-data layer. Values are separated into flight/operational, design target, study value, estimate, or unknown. Unknown is preferred to invented precision.

## Launch systems

| System | Configuration | Public parameters | Propulsion | Reuse |
|---|---|---|---|---|
| NASA SLS | Block 1 | 322 ft / 98.1 m; >27 t to deep space; 8.8 million lbf max thrust | 4 RS-25 + 2 five-segment SRBs; ICPS | Expendable |
| NASA SLS | Block 1B | 38 t to deep space incl. Orion/crew | Core + RS-25 + boosters + EUS | Expendable |
| SpaceX Falcon 9 | operational | 70 m; 3.7 m; 549,054 kg; 22,800 kg LEO published value | 9 Merlin; LOX/RP-1 | First-stage reuse |
| SpaceX Starship | published architecture | 124 m; 9 m; 100+ t payload target; Starship 1,600 t propellant; Super Heavy 3,650 t | Methane/LOX; Raptor | Fully reusable architecture |
| Blue Origin New Glenn | published architecture | >98 m; 7 m fairing; 45 t LEO / >13 t GTO | 7 BE-4 + 2 BE-3U | Reusable first stage |
| ESA Ariane 6 | Ariane 62/64 | ~10.3 / 21.6 t LEO; ~4.5 / 11.5 t GTO | Vulcain 2.1 + P120C | Expendable |

## Crew / deep-space spacecraft

| System | Role | Public baseline |
|---|---|---|
| Orion | Crew transport / return | 4 crew; up to 21 days; ~78,000 lb gross liftoff mass; crew module + European service module + launch abort system |
| Gateway | Cislunar infrastructure | Modular lunar-orbit architecture for habitation, logistics, science, communications and staging; configuration evolves |
| HLS | Lunar surface transport | Commercial lander architecture integrated with Orion/Artemis; provider-specific design |

## Qualification and verification

Recurring programme activities include component qualification, subsystem tests, structural tests, propulsion hot-fire, avionics/software HIL, thermal-vacuum, acoustic/vibration, aerodynamic testing where applicable, integrated vehicle tests, wet-dress/countdown rehearsal, flight testing and post-flight data review.

## Data schema for future entries

system; subsystem; parameter; value; unit; status; source organization; document; page/section; date; confidence; mission relevance.

The public database deliberately distinguishes measured/operational values from targets and studies.
