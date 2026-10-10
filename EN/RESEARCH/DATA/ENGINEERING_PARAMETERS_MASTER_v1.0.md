# Engineering Parameters Master Dataset v1.0

Updated: 2026-09-19

A normalized public engineering layer. Values are classified as flight/operational, target, research, estimated or unknown. An unknown is preferable to invented precision.

## Launch systems

| System | Configuration | Public parameters | Engines | Reusability |
|---|---|---|---|---|
| NASA SLS | Block 1 | 322 ft / 98.1 m; >27 t on a deep-space trajectory; 8.8 million lbf maximum thrust | 4 RS-25 + 2 five-segment solid boosters; ICPS | Expendable |
| NASA SLS | Block 1B | 38 t to deep space with Orion/crew | Core stage + RS-25 + boosters + EUS | Expendable |
| SpaceX Falcon 9 | operational | 70 m; 3.7 m; 549,054 kg; published 22,800 kg to LEO | 9 Merlin; LOX/RP-1 | First-stage recovery |
| SpaceX Starship | published architecture | 124 m; 9 m; 100+ t payload target; Starship 1,600 t propellant; Super Heavy 3,650 t | Methane/oxygen; Raptor | Fully reusable architecture |
| Blue Origin New Glenn | published architecture | >98 m; 7 m fairing; 45 t to LEO / >13 t to GTO | 7 BE-4 + 2 BE-3U | Reusable first stage |
| ESA Ariane 6 | Ariane 62/64 | ~10.3 / 21.6 t to LEO; ~4.5 / 11.5 t to GTO | Vulcain 2.1 + P120C | Expendable |

## Crewed and deep-space vehicles

| System | Role | Public baseline |
|---|---|---|
| Orion | Crew transportation / return | 4 people; up to 21 days; ~78,000 lb launch mass; crew module + European Service Module + launch abort system |
| Gateway | Cislunar infrastructure | Modular architecture for habitation, logistics, science, communications and staging; evolving configuration |
| HLS | Lunar landing transport | Commercial lander architecture integrated with Orion/Artemis; provider-dependent design |

## Qualification and verification

A typical chain includes component qualification, subsystem tests, structural tests, engine hot-fire tests, avionics/software HIL tests, thermal-vacuum, vibration/acoustic testing, aerodynamic testing where required, integrated tests, fuelling/countdown rehearsals, flight tests and post-flight data analysis.

## Future data schema

system; subsystem; parameter; value; unit; status; source organization; document; page/section; date; confidence; mission applicability.

The public dataset deliberately separates measured/operational values from targets and research values.
