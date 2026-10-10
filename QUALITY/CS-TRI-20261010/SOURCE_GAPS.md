# Open source and engineering-interpretation issues

**CS-TRI-20261010 · SOURCE_REVIEW / TRANSLATION_REVIEW**

## Unresolved source-export references

Five original PROGRAM documents retain conversation-native citation markers rather than portable bibliographic references: `CANDIDATE_FIRST_MISSIONS_v0.1.md`, `MISSION_A_SYSTEM_REQUIREMENTS_v0.1.md`, `MISSION_B_SYSTEM_REQUIREMENTS_v0.1.md`, `MISSION_C_SYSTEM_REQUIREMENTS_v0.1.md`, and `SPACE_PROGRAM_CONCEPT_v0.1.md`.

They are preserved for textual provenance, but are not functioning GitHub source links. The associated external parameters must not be treated as independently verified. Next action: recover the precise primary document and revision for each claim, register its URL and page, and refrain from procurement or external commitments based on the figure until that check is complete. Republishing the translation does not close this gap.

## Decision-relevant issues

**G01 — Mission A:** reconcile the phrase “continuous telemetry and command” with ground-contact windows and any relay architecture. Continuous command-handling capability is not continuous RF coverage.

**G02 — Historical launch price:** an early concept's reference price is not a current supplier quotation and does not include the total mission cost.

**G03 — Lunar duration:** mission lifetime and day/night transitions must be checked jointly against power and thermal budgets. They are target requirements, not demonstrated service life.

**G04 — Engineering datasets:** launch performance depends on configuration, orbit and flight profile. Matching translated numbers does not establish their current validity.

**G05 — Cooperation:** MoUs, demonstrated configurations and corporate group membership do not establish universal interoperability, a purchase order or independent suppliers.

## Numeric formatting review

The automated screening can flag thousands-separator differences, including `549 054` versus `549,054`, `22 800` versus `22,800`, `78 000` versus `78,000`, and `33 000` versus `33,000`. These are review candidates, not permission to silently change source values.

## Completion boundary

Structural checks cover file presence, table structure, the link-budget formula, REQ/SYS identifiers, local links and the source graph. Independent language review, primary-source revalidation and engineering validation are not performed by the script and are not implied by a passing run. All unresolved work remains visible rather than being replaced by invented references or precision.
