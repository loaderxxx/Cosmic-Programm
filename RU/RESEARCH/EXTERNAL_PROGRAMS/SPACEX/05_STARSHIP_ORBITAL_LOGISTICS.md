# SpaceX — Starship и орбитальная логистика

Дата: **2026-09-22**  
Версия: **v0.1**

## 1. Почему Starship — это не просто «более большая ракета»

В пользовательском руководстве Starship система представлена как two-stage reusable transportation system для Earth orbit, Moon и Mars missions.

Для HLS NASA документирует отдельную сложную архитектуру с:
- Starship lander;
- tanker launches;
- storage depot;
- propellant transfer;
- rendezvous/docking;
- lunar orbit operations.

## 2. Изменение системной парадигмы

Falcon model:

**Earth → orbit → payload.**

Starship HLS model:

**Earth → many tanker operations → orbital propellant aggregation → lander → lunar orbit → surface.**

Таким образом, ключевой продукт становится:

**orbital logistics capability.**

## 3. Самая важная проблема

NASA OIG отмечает, что vehicle-to-vehicle cryogenic transfer для HLS является одной из наиболее значимых технических задач и что такая операция ранее vehicle-to-vehicle не демонстрировалась.

Это означает:

**Starship architecture зависит от новой infrastructure capability, а не только от новой vehicle capability.**

## 4. Hidden dependency

На первый взгляд:
**lander capability**

На системном уровне:
**propellant production/launch → tanker cadence → depot → transfer → thermal control → navigation → rendezvous → verification → mission.**

Это классический пример dependency graph.

## 5. Почему это важно для Cosmic Programm

Для лунной инфраструктуры нельзя спрашивать только:

**«можем ли мы посадить аппарат?»**

Нужно спрашивать:

**«что должно существовать до посадки, во время эксплуатации и для следующего аппарата?»**

Так capability превращается в infrastructure graph.

## 6. Архитектурное следствие

Первый лунный node может иметь смысл не потому, что он выполняет одну миссию, а потому что он создаёт:
- communications;
- navigation;
- power;
- landing knowledge;
- surface operations;
- logistics interfaces.

Это напрямую согласуется с нашей infrastructure model.

## 7. Предварительная оценка зрелости

Необходимо разделять:

**Falcon operational reuse**

и

**Starship full integrated reuse + orbital propellant logistics.**

Второе существенно менее зрелое и не должно наследовать confidence первого.

## Открытые вопросы

- фактическая flight rate Starship;
- demonstrated propellant transfer;
- depot thermal management;
- tanker turnaround;
- orbital rendezvous reliability;
- cumulative mass and cost of tanker campaign;
- landing/reuse of HLS hardware.

## Источники

SpaceX Starship User’s Guide:
https://www.spacex.com/media/starship_users_guide_v1.pdf

NASA OIG HLS Audit:
https://oig.nasa.gov/audits/nasas-management-of-the-human-landing-system-contracts/
