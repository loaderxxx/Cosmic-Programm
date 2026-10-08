# Data, sources and traceability

[Atlas](../README.md) · [English](https://github.com/loaderxxx/Cosmic-Programm/blob/main/ATLAS/DATA/README.md) · [Русский](https://github.com/loaderxxx/Cosmic-Programm/blob/lang/ru/ATLAS/DATA/README.md) · [العربية](https://github.com/loaderxxx/Cosmic-Programm/blob/lang/ar/ATLAS/DATA/README.md)

## Shared source records

[CATALOG_SOURCE.json](CATALOG_SOURCE.json) is the unchanged public industry catalogue from commit `75066d88bbcc96eb63f6242df48cbcf5eac9fc67`. [portal.json](portal.json) records the source base, language branches and reader-facing pages. These files are shared evidence metadata, not independent validation of company claims.

**Path rule:** the `path` fields in the preserved catalogue are relative to its ORIGINAL source root, not this DATA folder. Resolve them against `industry_source_root` in portal.json. For example, record P001 resolves to the original `ORGANIZATIONS/P001_antaris-inc/README.md` under that root. We do not silently rewrite source records or merge the entire old research branch.

## Evidence grades in the 55-record snapshot

| Grade | Count | What it means |
|---|---:|---|
| PRODUCT_PRIMARY_SOURCE | 40 | A primary product/organization reference is linked; performance is not independently certified. |
| EVENT_PROFILE_ONLY | 4 | Event/profile information only; product research remains open. |
| PRELIMINARY_SOURCE | 2 | Preliminary source evidence requiring further review. |
| ORGANIZATION_INFO | 1 | Organization information, not product qualification. |
| IDENTITY_UNKNOWN | 8 | Identity unresolved; not a verified supplier entry. |

These categories describe the source snapshot. Event attendance and COSMOSYNTH relationships are separate fields and must not be inferred from a product-source link.

## Maintain one evidence chain

Use stable organization and research IDs, original source language, source URL, publication/check dates, scope, claim class, uncertainty and exact revisions. Additional RU/AR evidence must be reconciled with the English record. A translation should preserve numbers, units, dates, source IDs, caveats and the distinction between proposals and results.

Current detailed organization dossiers remain English source documents. New entry pages and directory explanations are available in all three languages; [translation coverage](../../RESEARCH_STATUS.md) is explicit. Private contact data, relationship histories and internal prioritization are not part of these public datasets.
