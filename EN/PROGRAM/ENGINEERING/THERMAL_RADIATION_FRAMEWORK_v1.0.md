# Thermal and Radiation Analysis Framework v1.0

## Thermal model

Every spacecraft must be analysed in at least the following scenarios:
- worst-case hot;
- worst-case cold;
- maximum heat generation;
- minimum heat generation;
- transients;
- launch/deployment;
- safe mode;
- loss of part of the power system.

For each node, record the allowable temperature range, operating range and storage limits.

## Heat sources

Account for:
- electronics;
- computers;
- transmitters;
- drives;
- batteries;
- power electronics;
- payload;
- external radiation;
- albedo;
- planetary infrared radiation;
- internal thermal couplings.

## Thermal budget

Distinguish:
**incident input → absorption → generation → conduction → radiation → storage.**

Average temperature is not a sufficient characterization: local hot/cold spots and transients are critical.

## Radiation

Consider separately:
- total absorbed dose;
- single-event effects;
- charged particles;
- solar events;
- trapped radiation;
- electronics susceptibility.

For every critical component, define the required protection level and allowable degradation.

## Verification

Required:
- thermal calculations;
- thermal-balance testing;
- thermal-vacuum testing;
- hot/cold functional tests;
- radiation qualification or an equivalence justification;
- worst-case analysis.

Status: FRAMEWORK.
