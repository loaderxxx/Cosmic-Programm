# SpaceX AI — Audio Block 03

Дата: 2026-09-23
Версия: v0.1
Статус: PUBLIC RESEARCH / AUDIO / 10-MINUTE BLOCK

## Короткое восстановление

Мы пришли к модели, в которой AI у SpaceX следует рассматривать не как один продукт.

Есть данные, модели, RAG, инструменты, agents, inference, software development и feedback.

Ключевая цепочка:

**DATA → MODEL → AGENT → TOOL → ACTION → MEASUREMENT → FEEDBACK**

А теперь мы идём глубже — к compute, собственным моделям и к вопросу, зачем SpaceX вообще строить весь этот стек.

---

# Новый блок — примерно 10 минут

## 1. Почему inference становится отдельной инженерной задачей

Мы привыкли думать про AI как про модель.

Но представь, что в компании одна модель.

И десять пользователей.

Всё относительно просто.

Теперь представь тысячи инженеров, множество внутренних приложений, десятки или сотни AI workflows и агентов, которые одновременно что-то делают.

Тогда модель — это уже только один компонент.

Нужно решить:

где она работает,

как распределяется нагрузка,

как использовать GPU,

как уменьшать задержку,

как переживать всплески запросов,

как обслуживать разные модели,

как обновлять endpoints,

как не терять reliability.

И вот здесь появляется inference infrastructure.

Публичная вакансия SpaceX Software Engineer, Inference описывает именно такой класс задач: high-throughput inference для mission-critical applications, distributed model serving, load balancing, auto-scaling, batch scheduling, global KV cache и continuous batching.

Это чрезвычайно показательно.

Компания ищет не просто людей, которые умеют пользоваться моделью.

Она строит **систему доставки intelligence как внутреннего сервиса**. citeturn123078search6

---

## 2. Почему это похоже на инфраструктуру электросети

Есть очень простая аналогия.

Потребителю электричества не важно, какой именно генератор произвёл каждый киловатт.

Ему важно, что энергия доступна тогда, когда нужна.

С inference похожая история.

Инженеру не обязательно знать, на каком именно GPU физически запущен его запрос.

Ему важно:

AI доступен,

быстрый,

стабильный,

предсказуемый,

и может работать в нужном масштабе.

Поэтому AI infrastructure постепенно превращается в коммунальный слой.

Условно:

**models are applications**

а

**inference is infrastructure.**

Это очень важное архитектурное разделение.

---

## 3. И вот здесь возвращается старый SpaceX-принцип — bottleneck

Мы уже видели этот принцип в launch business.

Если bottleneck — launch vehicle, улучшается launch vehicle.

Если bottleneck — pad, строится инфраструктура pad.

Если bottleneck — production, масштабируется production.

А в AI:

если bottleneck — compute,

то compute начинает становиться объектом вертикальной интеграции.

Если bottleneck — inference,

строится собственный inference stack.

Если bottleneck — training,

строится training infrastructure.

Если bottleneck — model capability,

появляется собственная model research.

Получается почти универсальная логика:

**Bottleneck → Control → Throughput → Scale.**

И вот это, пожалуй, один из наиболее интересных общих принципов всей SpaceX-истории.

---

## 4. Compute — это уже не просто GPU

Когда AI становится критически важным, GPU — только начало.

Нужны:

электричество,

охлаждение,

сеть,

storage,

data centers,

scheduling,

software,

monitoring.

То есть:

**AI compute = hardware + power + cooling + networking + software + operations.**

И здесь снова появляется очень SpaceX-подобная архитектура.

Речь идёт уже не об отдельном компоненте.

Речь идёт о контроле полного bottleneck chain.

Для launch system:

**engine → vehicle → pad → range → operations.**

Для AI:

**chip → server → data center → power → network → inference.**

В обоих случаях выигрывает не обязательно самый лучший отдельный component.

Выгоднее может оказаться тот, кто лучше контролирует **всю критическую цепочку**.

---

## 5. Теперь возникает проблема внешней зависимости

Представим, что SpaceX использует только внешний AI provider.

Тогда часть intelligence stack находится снаружи.

Провайдер может изменить:

цену,

модель,

API,

лимиты,

политику,

latency,

availability.

Для обычного приложения это может быть нормально.

Но если AI начинает участвовать в mission-critical engineering processes, зависимость становится архитектурным вопросом.

И здесь появляется следующий логичный шаг:

**build your own models and infrastructure.**

Не обязательно всё делать внутри.

Но critical intelligence dependencies начинают иметь смысл контролировать.

---

## 6. xAI меняет положение SpaceX

2 февраля 2026 года xAI объявила, что SpaceX приобрела xAI. citeturn123078search2

Это событие важно рассматривать не как обычную corporate transaction.

Системно это соединяет:

**SpaceX physical infrastructure**

и

**xAI model infrastructure.**

До этого условная цепочка могла выглядеть так:

SpaceX → external AI model.

После появления собственного model stack получается:

SpaceX → own compute → own models → own applications.

И это значительно больше похоже на вертикальную интеграцию.

---

## 7. Но самое интересное — recursive improvement

Представь:

есть модель.

Она используется инженерами.

Инженеры получают результаты.

Система получает feedback.

Этот feedback идёт в evaluation.

Потом в post-training.

Потом появляется новая модель.

Новая модель снова работает.

И опять приходит feedback.

Получается:

**model → use → feedback → training → better model.**

Это один цикл.

Но есть второй.

**model → engineer → design/test → physical result → data → model.**

Теперь два цикла начинают пересекаться.

Первый улучшает AI.

Второй улучшает инженерную систему.

И это уже очень интересная рекурсивная архитектура.

---

## 8. Reinforcement learning особенно интересен именно здесь

Публичные SpaceXAI/xAI роли показывают работу с reinforcement learning и post-training.

Почему это важно?

Потому что supervised training может учить модель воспроизводить известные примеры.

А reinforcement learning позволяет оптимизировать поведение по некоторому signal.

Для engineering agent это потенциально интересно.

Допустим, агент должен решать сложную задачу.

Есть разные варианты действий.

Можно оценивать:

правильность,

стоимость,

время,

количество tool calls,

качество evidence,

соответствие требованиям.

И потом обучать систему предпочитать более полезные trajectories.

Это пока не значит, что SpaceX именно так обучает конкретных engineering agents.

Но это естественное направление, которое видно на пересечении публичных AI hiring signals и инженерной архитектуры.

Поэтому здесь важно говорить:

**potential capability**, а не установленный internal implementation.

---

## 9. Cursor — это не просто редактор кода

Теперь возвращаемся к Cursor.

Cursor официально сообщил 14 августа 2026 года, что был приобретён SpaceX. Сам Cursor описывает переход от code completion к AI teammates, которым можно поручать реальную работу. Там же компания пишет о доступе к очень крупному GPU fleet SpaceX и связывает интеграцию с возможностью строить более сильные и более экономичные модели. citeturn123078search1

Почему для нас это интересно?

Потому что software development — ещё один feedback loop.

Очень простой:

**idea → code → test → result → change.**

Если AI участвует внутри этого цикла, он ускоряет цифровую часть engineering.

А современная космическая система очень сильно зависит от software.

Avionics.

Ground systems.

Telemetry.

Data processing.

AI infrastructure.

Simulation.

Operations.

Поэтому AI-native development становится частью общей инженерной скорости.

---

## 10. Теперь соберём всё вместе

У нас уже есть:

**Engineering AI**

для анализа и design.

**Manufacturing AI**

для inspection и production.

**Reliability AI**

для anomaly detection.

**Starlink ML**

для network optimization.

**RAG**

для engineering knowledge.

**MCP**

для tool access.

**Agents**

для multi-step work.

**Inference infrastructure**

для масштабирования.

**Training**

для создания моделей.

**Post-training / RL**

для улучшения поведения.

**Cursor**

для software engineering.

**Starlink**

для огромного operational data loop.

**Physical SpaceX**

для производства и полётов.

Теперь мы можем нарисовать уже почти целую архитектуру.

---

## 11. Physical stack

Внизу:

**FACTORY**

↓

**VEHICLE**

↓

**LAUNCH**

↓

**SATELLITE**

↓

**NETWORK**

↓

**SERVICE**

Это физическая и эксплуатационная система.

---

## 12. Cognitive stack

Сверху:

**DATA**

↓

**RETRIEVAL**

↓

**MODEL**

↓

**INFERENCE**

↓

**AGENT**

↓

**TOOL**

↓

**ACTION**

↓

**EVALUATION**

↓

**FEEDBACK**

Это когнитивная и вычислительная система.

---

## 13. А теперь самое интересное — пересечение

Physical stack производит данные.

Cognitive stack анализирует данные.

Cognitive stack предлагает действие.

Physical stack выполняет действие.

Physical stack снова производит данные.

Получается:

**PHYSICAL WORLD → DATA → INTELLIGENCE → ACTION → PHYSICAL WORLD.**

Вот здесь и возникает настоящая cognitive engineering loop.

И именно здесь SpaceX становится очень интересным benchmark для нас.

---

## 14. Но где находится человек?

И это принципиальный вопрос.

Потому что мы можем представить красивую полностью автономную систему.

Но engineering reality устроена иначе.

Человек остаётся ответственным за intent, constraints, judgment и high-consequence decisions.

Поэтому реальная система должна иметь:

**agent autonomy**

и одновременно

**human authority.**

А между ними:

**permissions, audit, provenance and verification.**

И тогда AI не заменяет инженера.

Он меняет распределение работы.

AI может выполнять огромное количество промежуточных действий.

Человек задаёт цель, контролирует границы и принимает критические решения.

---

## 15. И здесь начинается наша самая интересная точка

Посмотри, до чего мы дошли.

Мы начинали с вопроса:

**«Какими AI-инструментами пользуется SpaceX?»**

А через несколько уровней пришли к совсем другому:

**«Как SpaceX строит cognitive infrastructure вокруг своей physical infrastructure?»**

Это совершенно другой вопрос.

И именно его я бы исследовал дальше.

Потому что тогда нам уже недостаточно знать названия моделей.

Нужно понять:

какие данные существуют,

как они индексируются,

как устроено retrieval,

какие модели используются,

где находится inference,

какие агенты существуют,

какие tools доступны,

где стоят permissions,

где human gate,

как измеряется качество,

как feedback возвращается в систему.

Это уже reverse-engineering **publicly observable architecture**.

Не секретов.

Не private internals.

А реконструкция по публичным следам.

---

## Пауза

На этом десятиминутном блоке остановимся.

Следующий блок я бы посвятил самому интересному вопросу:

**как восстановить публичную архитектуру SpaceX Engineering AI Stack end-to-end.**

То есть пройти последовательно:

**DATA SOURCES**

→ **DATA INFRASTRUCTURE**

→ **RAG / RETRIEVAL**

→ **MODELS**

→ **INFERENCE**

→ **AGENTS**

→ **MCP / TOOLS**

→ **PERMISSIONS**

→ **HUMAN GATE**

→ **PRODUCTION**

→ **TELEMETRY**

→ **EVALUATION**

→ **FEEDBACK**

И на каждом уровне отделить:

**confirmed**

от

**probable**

и от

**unknown**.

После этого уже будет интересно сравнить получившуюся карту с нашей собственной cognitive architecture.

