# SpaceX — многоразовость и cadence

Дата: **2026-09-22**  
Версия: **v0.1**

## 1. Единица анализа

Не:

**«многоразовая ракета»**

а:

**«многоразовая транспортная система с повторяемой операцией».**

Value появляется, когда hardware может:
1. летать повторно;
2. возвращаться;
3. инспектироваться;
4. при необходимости ремонтироваться;
5. снова интегрироваться;
6. выполнять следующую миссию с приемлемыми затратами и риском.

## 2. Почему cadence важнее рекорда reuse

Один booster, который летает много раз, ещё не создаёт industrial system.

Нужны:
- fleet size;
- flight rate;
- processing capacity;
- launch infrastructure;
- maintenance;
- spare inventory;
- personnel;
- range availability;
- mission demand.

Поэтому KPI будущего анализа:

**usable missions / unit / time**

и

**useful payload / total lifecycle cost.**

## 3. Falcon как evidence base

Falcon User’s Guide описывает launch operations, mission integration, verification и facilities как standard service architecture.

Это указывает на индустриализацию launch service.

## 4. Starship — отдельный уровень зрелости

NASA OIG отмечает, что Starship HLS сталкивается с задержками и ещё не продемонстрированными integrated technologies, включая cryogenic propellant transfer.

Следовательно, нельзя переносить эксплуатационную зрелость Falcon 9 напрямую на Starship.

## 5. Turnaround как системный bottleneck

Для HLS NASA OIG указывает требование 12–24 дней turnover для launch pad и отмечает риск, что он ещё не продемонстрирован.

Это очень важная мысль для Cosmic Programm:

**cadence — property infrastructure + hardware + process, а не только vehicle.**

## 6. Инженерный loop

Высокая cadence создаёт не только revenue.

Она создаёт:
- more flight data;
- more anomaly data;
- more maintenance data;
- more process data;
- more statistical confidence.

Но повышенная cadence без правильного instrumentation может просто ускорить производство ошибок.

Поэтому:

**CADENCE × MEASUREMENT QUALITY = LEARNING THROUGHPUT**

Это наша аналитическая формула, не публичная формула SpaceX.

## 7. Перенос в Космическую программу

Вместо попытки сразу построить большую лунную систему нужно искать capabilities, которые можно повторять.

Например:
- repeatable autonomous ground experiment;
- repeatable robotics task;
- repeatable communications test;
- repeatable power cycle;
- repeatable orbital service experiment.

Цель:

**получить серию итераций, а не один «героический» прототип.**

## Открытые вопросы

- Реальные turnaround times по booster fleet.
- Средняя refurbishment burden.
- Cost per flight by reuse class.
- Failure/recovery economics.
- Степень зависимости cadence от Starlink.
