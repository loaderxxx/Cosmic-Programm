# Supplier and Interface Matrix v1.0

## Purpose

Determine which elements should be obtained externally and which should remain under architectural control.

## Categories

| Category | Decision type |
|---|---|
| Launch vehicle | predominantly BUY |
| Standard rideshare | BUY |
| Ground communications services | BUY/PARTNER |
| Standard electronic components | BUY |
| Unique payload | BUILD/OWN |
| Mission architecture | BUILD/OWN |
| Autonomous software | BUILD/OWN |
| Data system | BUILD/OWN |
| Specialized interfaces | BUILD/OWN/PARTNER |
| Lunar infrastructure | mixed model |

## For each supplier

Record:
- product;
- interface;
- maturity;
- availability;
- constraints;
- replaceability;
- export and legal restrictions;
- delivery lead time;
- programme dependency;
- replacement plan.

## Rule

An external component must not become a hidden single point of failure in the architecture.

Status: FRAMEWORK.
