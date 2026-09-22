# SpaceX — вертикальная интеграция

Дата: **2026-09-22**  
Версия: **v0.1**

## 1. Что подтверждено

В Falcon User’s Guide SpaceX описывает flat corporate structure, lean processes, co-location design/production/quality и низкоинфраструктурный подход.

В 2026 prospectus SpaceX прямо описывает **extreme vertical integration**, включая утверждение, что приблизительно 80% Starship производится in-house, и связывает это с быстрыми итерационными циклами.

Важно: цифра 80% является **заявлением SpaceX**, а не независимо проведённым аудитом Cosmic Programm.

## 2. Что означает вертикальная интеграция

Она может сокращать:
- supplier negotiation latency;
- transfer of design intent;
- interface count;
- procurement dependencies;
- modification lead time.

Но может увеличивать:
- fixed costs;
- internal coordination;
- capex;
- concentration risk;
- failure coupling.

Поэтому вопрос не «вертикальная интеграция хороша или плоха».

Вопрос:

**какие конкретные interfaces настолько критичны, что их выгодно контролировать внутри?**

## 3. Критические interfaces

Кандидаты:
- engine ↔ vehicle;
- vehicle ↔ avionics;
- vehicle ↔ ground systems;
- satellite ↔ network;
- satellite ↔ launch manifest;
- manufacturing ↔ test.

Там, где скорость изменения критична, internal ownership потенциально особенно ценен.

## 4. Не следует копировать 80%

Для Cosmic Programm не надо превращать процент вертикальной интеграции в KPI.

Правильная модель:

**CRITICAL INTERFACE**
→ latency
→ supplier risk
→ change frequency
→ switching cost
→ IP sensitivity
→ internal/external decision.

Для одного компонента Buy может быть оптимальным, для другого — Build.

## 5. Глубокий вывод

Вертикальная интеграция — это прежде всего **управление временем и интерфейсами**, а уже потом управление производством.

Если внешний поставщик способен изменить деталь за 48 часов и обеспечить нужную qualification discipline, внутреннее производство может быть не нужно.

Если изменение занимает месяцы и требует сложной координации, внутренний контроль получает системную ценность.

## 6. Открытые вопросы

- Какова полная cost of ownership внутреннего производства?
- Какие компоненты SpaceX всё же закупает?
- Где проходит граница make/buy?
- Как внутреннее производство влияет на resilience supply chain?
- Какой минимальный вертикальный контур нужен Cosmic Programm?

## Источники

SpaceX Falcon User’s Guide 2025:
https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf

SpaceX 2026 EU Prospectus:
https://content.spacex.com/cms-assets/FINAL_Documents%20and%20Updates/SpaceX%20-%20EU%20Prospectus%20%28Approved%20by%20Bafin%29%20-%20June%205%2C%202026.pdf
