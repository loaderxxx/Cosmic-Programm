# COSMOSYNTH — Language-first research and Git branch policy

**Decision owner:** Human project owner · **Effective date:** 2026-10-08 · **Status:** owner-directed policy, integration via reviewed GitHub PR.

## 0. Mandatory first operation — start in three languages

**Every new COSMOSYNTH research effort begins simultaneously in English (EN), Russian (RU), and Arabic (AR). English has priority and is the canonical reference; RU and AR are complete localized research editions, not optional late summaries.**

Before collecting or analysing sources, the coordinator must:
1. Identify the research decision/question, assign one stable research ID, and open three linked work records `en`, `ru`, `ar` within the same work cycle.
2. Note the canonical English source location, intended RU/AR branches, the common evidence/source register, scope, author/reviewer responsibilities if verified, and initial `IN_PROGRESS` language status.
3. Search the strongest primary sources in **any relevant source language**, including English, Russian and Arabic where material exists; preserve each original source language, publication date, URL, author/organization, technical units and limitations.
4. Build the English master synthesis first for authoritative claim IDs, engineering terminology, version and decisions. Develop Russian and Arabic analyses in parallel from the same evidence, with local context/terminology and explicit source traceability.
5. Do not call a study complete until the EN, RU and AR editions have passed semantic/source consistency checks or have clearly recorded unfinished translation/review blockers.

## 1. Git branch model — public research

| Git branch | Language | Authority |
|---|---|---|
| `main` | English (EN) | Canonical research, source registers, requirements, engineering decisions, status and version history |
| `lang/ru` | Russian (RU) | Complete corresponding Russian research, referencing the authoritative EN ID and commit |
| `lang/ar` | Arabic (AR) | Complete corresponding Arabic research, referencing the authoritative EN ID and commit |

- `main` remains GitHub's default branch. Do **not** rename the repository or replace English `main` with a localized edition.
- Branches `agent/cursor`, `agent/chatgpt`, and `work/<agent>/<task-id>-<slug>` remain engineering/coordination lanes; language branches are not substitutes for feature branches or PR review.
- English claims, source IDs, dates, figures, unit systems, qualification/verification state and status are authoritative. Russian and Arabic may add local terminology/context or additional local sources, but material evidence changes must be re-registered in English and re-synchronised before being described as shared conclusions.
- New EN content is integrated via PR to `main`; new RU and AR content via their own language-lane PRs to `lang/ru` and `lang/ar`, preserving `main` as source-of-truth. Link all three changes by research ID. Never blindly merge a localized branch back into English `main`.
- Historical `RU/` and `AR/` directories currently on `main` are **legacy compatibility material**. Do not delete, rewrite or proclaim fully migrated until references, existing reviews and translations are audited and a safe redirect/migration PR is reviewed. For **new** research, use language branches, not a new localized copy in `main`.

## 2. One research record / three language editions

Each of EN, RU and AR must include:
- common `research_id`, study title, scope, question, English canonical path and **exact source commit SHA** (or `PENDING` until published);
- language, edition version, translation/synthesis status and last independently verified date;
- numbered claims with preserved labels: `FACT`, `SOURCE CLAIM`, `ESTIMATE`, `HYPOTHESIS`, `INTERPRETATION`, `UNKNOWN`;
- the **same authoritative evidence ID and primary-source URL** for shared claims, and a clearly mapped ID for any additional local source;
- core technical analysis, quantitative values, units, confidence/limits, dependencies, conclusions and action recommendations (do not reduce RU/AR to a short abstract);
- any changes versus the English master, unresolved semantic disagreements, missing references and independent reviewer status if applicable.

**Locale statuses:** `IN_PROGRESS`, `SOURCE_REVIEW`, `TRANSLATION_REVIEW`, `VERIFIED`, `BLOCKED`. A source document discovered or an AI draft translated does not by itself establish a `VERIFIED` edition. Preserve directionality and readability for Arabic RTL text, mathematical expressions, identifiers, spacecraft/organization names, citations, URLs and units.

## 3. Integrated research-to-knowledge algorithm

`QUESTION → TRI-LANGUAGE INITIALIZATION (EN/RU/AR) → COLLECT → REGISTER SOURCES → EXTRACT → NORMALIZE → VERIFY → COMPARE → ENGLISH MASTER SYNTHESIS → RU/AR ANALYSIS AND SEMANTIC QA → REQUIREMENTS / PILOT / TASKS → THREE-BRANCH STATUS SYNC → REPORT`

Language-lane creation is **step zero**, not a polishing step at the end. Processing phases can run concurrently, but reference claims must remain comparable. For urgent intermediate results, mark the missing edition **PENDING** and do not present it as completed or equivalent. No invented facts are permitted to fill gaps in any language.

## 4. Publication, governance and confidentiality

- Protect the Public/Private boundary before *any* translation or branch push. Private contacts, negotiations, internal operating methods, proprietary results and sensitive evidence never enter the public `main` or its language branches.
- Keep non-public research and corresponding translations in authorized PRIVATE Core locations only. Never use a language change to bypass classification, intellectual-property review or human publication approval.
- Approved outward-facing materials may be delivered in EN first when the owner explicitly approves an exception, but work-tracking for RU and AR begins at the same time and missing editions remain transparently pending. An exception for release timing is not an exception to tri-language research.
- A branch existing is not proof that its translation is complete. A PR opened is not proof the change is integrated. An approved policy is not proof historical research has been migrated.
- No commits directly to `main` under normal agent workflow; use the existing review protocol.

## 5. Acceptance checks for every study

- [ ] One stable ID links EN, RU and AR artifacts, with correct URLs and exact English revision.
- [ ] English canonical analysis is evidence-labelled and sources are attributable.
- [ ] Russian edition preserves the full decision-useful content, caveats, numbers, source IDs and uncertainties.
- [ ] Arabic edition preserves the same and has reviewed RTL layout / technical terminology.
- [ ] New regional evidence from any language is reconciled in the English source record.
- [ ] Branch/PR/source SHA, locale statuses and open blockers are recorded.
- [ ] PRIVATE CORE and publication gates have not been bypassed.

**Historic migration:** The repository currently retains `EN/`, `RU/` and `AR/` directories in `main` from the previous layout; these remain legible evidence while migration is reviewed. The forward-looking operating model uses English `main`, Russian `lang/ru` and Arabic `lang/ar`.
