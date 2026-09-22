# SpaceX — риск, регулирование и governance

Дата: **2026-09-22**  
Версия: **v0.1**

## 1. Почему регуляторный контур — часть архитектуры

Rocket system не может считаться operational capability без:
- launch licensing;
- environmental review;
- range / airspace coordination;
- safety processes;
- government customer requirements;
- mission authorization.

FAA прямо указывает, что новые Starship/Super Heavy operations требуют соответствующего permit/license и environmental review.

Следовательно:

**REGULATION → SYSTEM ARCHITECTURE**

а не только юридическое сопровождение.

## 2. NASA insight/oversight

NASA OIG в 2026 году описывает HLS model как tailored approach с существенной свободой provider-а в project management при сохранении agency insight/oversight.

Это интересная governance architecture:

**provider autonomy + external assurance.**

## 3. Где работает такая модель

Она полезна, когда:
- provider owns design;
- provider can iterate rapidly;
- customer defines mission requirements;
- external body maintains safety and contract oversight.

Это похоже на separation:

**HOW TO BUILD → provider**

**WHAT MUST BE SAFE / ACHIEVED → customer/regulator**

## 4. Почему autonomy имеет цену

NASA OIG также показывает, что high-risk technology can remain immature despite programmatic progress.

Например:
- cryogenic transfer;
- pad turnaround;
- HLS integrated maturity;
- crew safety and verification.

Therefore:

**autonomy must be paired with evidence visibility.**

## 5. Cosmic Programm

Для нашей программы можно использовать:

**AUTONOMY OF ENGINEERING**
+
**STRICT EVIDENCE / V&V**
+
**PUBLICATION GATE**
+
**HUMAN APPROVAL FOR HIGH-CONSEQUENCE DECISIONS**

Это уже находится в нашем bootstrap architecture.

## 6. Risk taxonomy

Для SpaceX-style system analysis:

- technical;
- integration;
- operations;
- cadence;
- manufacturing;
- regulatory;
- safety;
- supply chain;
- economics;
- program dependency.

## 7. Особый риск — dependency stacking

Starship HLS показывает цепь:

vehicle
+ tanker
+ depot
+ transfer
+ pad cadence
+ flight test
+ crew integration.

Каждый новый capability создаёт новые dependencies.

Следовательно:

**architecture complexity grows faster than component count.**

## Открытые вопросы

- How much regulatory latency affects launch cadence?
- What requirements are most schedule-critical?
- How are hazards closed before crewed operations?
- Which dependencies are true critical path?

## Источники

FAA:
https://www.faa.gov/space/stakeholder_engagement/spacex_starship

NASA OIG HLS Audit:
https://oig.nasa.gov/audits/nasas-management-of-the-human-landing-system-contracts/
