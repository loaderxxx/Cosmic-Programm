# SpaceX — Vertical Integration

Date: **2026-09-22**  
Version: **v0.1**

> Complete translation of `RU/RESEARCH/EXTERNAL_PROGRAMS/SPACEX/02_VERTICAL_INTEGRATION.md`, source blob `ef8780edd3237bd8bb0f2fa4b3cfe96731551b9a`, snapshot `16073db5465c9bf0827f952a229bcded44dbd983`. Translated on 2026-10-08. Source-date claims are preserved, not independently revalidated by translation. Independent human language review is pending.

## 1. What is supported

In the Falcon User's Guide, SpaceX describes a flat corporate structure, lean processes, co-location of design, production and quality, and a low-infrastructure approach.

In its 2026 prospectus, SpaceX explicitly describes **extreme vertical integration**, including the statement that approximately 80% of Starship is produced in-house, and associates this with rapid iteration cycles.

Importantly, the 80% figure is a **SpaceX statement**, not an independent Cosmic Programm audit.

## 2. What vertical integration means

It can reduce:
- supplier negotiation latency;
- the time needed to communicate design intent;
- the number of interfaces;
- procurement dependencies;
- modification lead time.

But it can increase:
- fixed costs;
- internal coordination;
- capital expenditure;
- concentration risk;
- coupling between failures.

The question is therefore not whether vertical integration is good or bad.

It is:

**Which specific interfaces are sufficiently critical to make internal control worthwhile?**

## 3. Critical interfaces

Candidates:
- engine ↔ vehicle;
- vehicle ↔ avionics;
- vehicle ↔ ground systems;
- satellite ↔ network;
- satellite ↔ launch manifest;
- manufacturing ↔ test.

Where the speed of change is critical, internal ownership may be especially valuable.

## 4. Do not copy the 80% figure

Cosmic Programm should not turn the percentage of vertical integration into a KPI.

The appropriate model is:

**CRITICAL INTERFACE**
→ latency
→ supplier risk
→ change frequency
→ switching cost
→ IP sensitivity
→ internal/external decision.

Buying may be optimal for one component, while building may be optimal for another.

## 5. Deeper conclusion

Vertical integration is primarily **management of time and interfaces**, and only then management of production.

If an external supplier can modify a part within 48 hours and provide the required qualification discipline, internal manufacturing may be unnecessary.

If a change takes months and requires complex coordination, internal control acquires system-level value.

## 6. Open questions

- What is the full cost of ownership of internal manufacturing?
- Which components does SpaceX still buy?
- Where does the make/buy boundary lie?
- How does internal manufacturing affect supply-chain resilience?
- What minimum vertically integrated scope does Cosmic Programm need?

## Sources

SpaceX Falcon User's Guide 2025:
https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf

SpaceX 2026 EU Prospectus:
https://content.spacex.com/cms-assets/FINAL_Documents%20and%20Updates/SpaceX%20-%20EU%20Prospectus%20%28Approved%20by%20Bafin%29%20-%20June%205%2C%202026.pdf

[Russian source](../../../../RU/RESEARCH/EXTERNAL_PROGRAMS/SPACEX/02_VERTICAL_INTEGRATION.md) · [Arabic translation](../../../../AR/RESEARCH/EXTERNAL_PROGRAMS/SPACEX/02_VERTICAL_INTEGRATION.md)
