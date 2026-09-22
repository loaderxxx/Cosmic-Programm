# SpaceX — глубокий анализ применения AI

Дата: **2026-09-22**  
Версия: **v0.2**  
Статус: **PUBLIC RESEARCH / VERIFIED DEEP ANALYSIS**

## 1. Главный вывод

Публичные данные 2026 года показывают, что AI у SpaceX уже нельзя корректно описывать как один корпоративный «инструмент».

Наблюдаются связанные слои:
- engineering AI;
- simulation automation и surrogate modeling;
- manufacturing AI / computer vision / NDE;
- reliability AI;
- Starlink data / ML;
- internal model training;
- internal high-performance inference;
- RAG, MCP и agentic engineering;
- foundation-model capability после интеграции xAI;
- orbital AI compute через Starmind.

Центральная гипотеза:

> **Наиболее важен не сам факт использования LLM, а включение AI в реальные engineering, manufacturing и operations loops, где есть данные, инструменты, измеримый результат и обратная связь.**

## 2. Доказательная дисциплина

**DOCUMENTED FACT** — прямое заявление в корпоративном раскрытии, официальной вакансии или на официальном сайте.

**STRONG PUBLIC EVIDENCE** — один и тот же технический контур подтверждается несколькими публичными инженерными источниками.

**OPEN / INFERENCE** — аналитическая реконструкция, требующая дальнейшей проверки.

Особенно важно:

**job posting ≠ доказательство массовой production-эксплуатации.**

## 3. Engineering AI

Текущая роль Sr. Software Engineer (Vehicle Engineering) прямо описывает:
- training internal engineering models on SpaceX data;
- training from scratch;
- fine-tuning;
- reinforcement learning для LLM post-training;
- agentic engineering tools;
- engineering RAG;
- engineering MCP servers;
- anomaly detection;
- predictive modeling;
- automated decision-making;
- LLM, vision и multimodal systems;
- применение AI к electronics и propulsion;
- полный lifecycle от data preparation и training infrastructure до deployment, monitoring и continuous improvement.

Источник:
https://job-boards.greenhouse.io/spacex/jobs/8555142002

## 4. Simulation → datasets → surrogate models

SpaceX одновременно ищет инженеров по автоматизации FEA, CFD, thermal и structural simulation и ML-инженеров по surrogate modeling.

Публично заявлены:
- создание больших curated training datasets;
- tens of thousands of high-fidelity simulation results;
- neural operators;
- physics-informed ML;
- uncertainty quantification;
- active learning;
- inverse problems;
- geometry / shape optimization.

Источники:
https://job-boards.greenhouse.io/spacex/jobs/8559054002
https://job-boards.greenhouse.io/spacex/jobs/8559035002

Рабочая цепочка:

**simulation → automated data generation → dataset → surrogate model → fast analysis / optimization**

Это показывает, что simulation может быть не только инструментом расчёта, но и машиной производства training data.

## 5. Manufacturing AI

Роль Sr. Software Engineer, Computer Vision описывает production-scale AI для Starship, Raptor и Starlink.

Публично указаны:
- real-time inspection;
- automated defect recognition;
- NDE;
- materials engineering;
- sensor fusion;
- stream processing;
- cloud/edge inference;
- model versioning;
- A/B testing;
- drift detection;
- retraining;
- Ray / Kubernetes / Kubeflow / MLflow-подобный MLOps.

Источник:
https://job-boards.greenhouse.io/spacex/jobs/8517346002

Архитектура:

**physical process → sensors/images → model → quality estimate → production action**

## 6. Reliability AI

Публичные reliability-роли описывают:
- predictive modeling;
- anomaly detection;
- build metrics;
- flight indicators;
- LLM / generative AI workflows;
- AI agents;
- build-to-flight analysis.

Источники:
https://job-boards.greenhouse.io/spacex/jobs/8463192002
https://job-boards.greenhouse.io/spacex/jobs/8782080002

Рабочая схема:

**build → test → flight → observation → anomaly → diagnosis → improvement**

## 7. Starlink: AI как оптимизатор живой системы

Публичные Starlink роли указывают на:
- telemetry;
- large-scale data processing;
- forecasting;
- clustering;
- anomaly detection;
- predictive models;
- network analytics;
- growth analytics;
- network observability;
- automation.

Источники:
https://job-boards.greenhouse.io/spacex/jobs/8243150002
https://job-boards.greenhouse.io/spacex/jobs/8573711002
https://job-boards.greenhouse.io/spacex/jobs/8577262002

Здесь AI работает как optimization engine:

**measure → detect → model → predict → act → measure again**

## 8. Internal inference layer

Публичная роль Software Engineer, Inference (AI Data Engineering) описывает внутреннюю high-performance AI inference platform.

Указаны:
- distributed inference;
- load balancing;
- autoscaling;
- batch scheduling;
- global KV cache;
- continuous batching;
- low tail latency;
- observability;
- quantization;
- speculative decoding;
- GPU optimization;
- CI/CD;
- support for training workloads.

Источник:
https://job-boards.greenhouse.io/spacex/jobs/8717350002

Это сильный сигнал, что inference рассматривается как отдельная enterprise capability.

## 9. Foundation models и xAI

SEC сообщает, что 2 февраля 2026 года xAI стала wholly-owned subsidiary SpaceX.

В AI-сегменте SpaceX публично описывает frontier model Grok, AI solutions и AI computational infrastructure.

Источник:
https://www.sec.gov/Archives/edgar/data/1181412/000162828026052535/spcx-20260630.htm

Публичные AI-роли дополнительно показывают работу с pre-training, fine-tuning, post-training, reinforcement learning и foundation models.

## 10. Agentic engineering и MCP

SpaceX прямо упоминает:
- agentic engineering tools;
- multi-agent workflows;
- RAG-based engineering tools;
- engineering MCP servers.

Источник:
https://job-boards.greenhouse.io/spacex/jobs/8555142002

Потенциальный цикл:

**engineer → agent → retrieval → tool → simulation / data / code → analysis → recommendation**

При этом публичных доказательств fully autonomous safety-critical engineering decision-making недостаточно.

## 11. AI data layer

Публично просматриваются разные источники данных:

**Engineering**
- requirements;
- design data;
- simulations;
- test results;
- flight data.

**Manufacturing**
- images;
- sensors;
- inspection;
- process data.

**Operations**
- telemetry;
- network health;
- anomalies;
- reliability data.

**Business**
- customer / product / growth data.

Отсюда возникает heterogeneous AI data estate, поверх которого работают разные классы моделей.

## 12. AI methods portfolio

Публично наблюдаются:

**Statistical / classical ML**
- forecasting;
- clustering;
- anomaly detection;
- time-series analysis;
- predictive modeling.

**Deep learning**
- computer vision;
- multimodal models;
- foundation models.

**Physics-informed ML**
- surrogate models;
- neural operators;
- PINNs;
- inverse problems.

**Generative / agentic**
- RAG;
- tool calling;
- MCP;
- multi-agent workflows;
- LLM post-training.

Следовательно правильнее рассматривать SpaceX AI как portfolio of methods selected per bottleneck.

## 13. AI compute

Q2 2026 SEC disclosure показывает:
- AI revenue: **$2.561B**;
- AI capex: **$15.828B**;
- nameplate compute: **1.4 GW**;
- AI Adjusted EBITDA: **$1.146B**;
- AI operating loss: **$1.257B**.

Источник:
https://www.sec.gov/Archives/edgar/data/1181412/000162828026052515/earningsreleaseq22608042.htm

Это финансовые показатели всего AI-сегмента, а не доказательство ROI внутреннего engineering AI.

## 14. Starmind

Официальная страница Starmind описывает:
- orbital AI compute;
- solar energy;
- local compute;
- laser links;
- Starlink connectivity;
- до 250 kW peak / 175 kW average compute payload;
- modular architecture;
- chip-vendor agnostic design.

Источник:
https://new.spacex.com/spacexai/starmind

Уровень доказательности:

**publicly described development architecture**, а не подтверждённая широкомасштабная operational network.

## 15. Cursor

14 августа 2026 года Cursor сообщил, что официально вошёл в SpaceX.

Источник:
https://prod.cursor.com/blog/joining-spacex

Для AI/software engineering это добавляет отдельный контур:

**spec → code → agent → test → review → deploy → feedback**

Количественная оценка вклада Cursor в общую производительность SpaceX по публичным данным пока невозможна.

## 16. Сквозная аналитическая реконструкция

На текущем уровне доказательств полезна схема:

**PHYSICAL SYSTEMS**
→ sensors / telemetry / inspection / simulation

↓

**DATA**
→ ingestion / storage / retrieval

↓

**MODELS**
→ ML / vision / surrogate / LLM / multimodal

↓

**INFERENCE**
→ distributed serving / GPU infrastructure

↓

**AGENTS / TOOLS**
→ RAG / MCP / APIs / simulations / enterprise tools

↓

**ENGINEERING / OPERATIONS**
→ analysis / detection / prediction / proposed action

↓

**MEASUREMENT**
→ test / production / flight / network outcome

↓

**FEEDBACK**
→ new data / new model / new process / new hardware

Это аналитическая реконструкция, а не опубликованная SpaceX схема.

## 17. Что доказано с высокой уверенностью

Публичные источники подтверждают, что SpaceX в 2026 году развивает или использует AI/ML для:
1. engineering models;
2. simulation and surrogate modeling;
3. manufacturing inspection;
4. reliability and anomaly detection;
5. Starlink analytics;
6. internal inference;
7. RAG / MCP / agentic engineering;
8. foundation-model development;
9. AI-native software development;
10. orbital AI compute architecture.

## 18. Что пока неизвестно

Публичные данные не позволяют надёжно установить:
- долю engineering work, выполняемую AI;
- production coverage отдельных моделей;
- точную автономность агентов;
- конкретные safety-critical model architectures;
- exact internal datasets;
- exact engineering ROI;
- долю автоматически принимаемых решений;
- внутреннюю структуру permissions / approval gates.

Эти вопросы остаются OPEN RESEARCH.

## 19. Главная гипотеза исследования

AI наиболее интересен там, где он уменьшает latency полного цикла:

**question → data → computation → decision → physical test → feedback**

а не только ускоряет генерацию текста.

Центральная единица анализа:

## AI-ACCELERATED FEEDBACK LOOP

## 20. Следующий уровень исследования

Следует восстановить по публичным данным:

1. data sources;
2. ingestion;
3. storage;
4. retrieval;
5. simulation;
6. training;
7. model registry;
8. inference;
9. agents;
10. MCP / tools;
11. permissions;
12. human approval;
13. deployment;
14. monitoring;
15. model evaluation;
16. rollback;
17. telemetry feedback.

Особый вопрос:

> Какие элементы этого контура повторяются между разными командами SpaceX, а какие являются локальными решениями отдельных программ?

## Источники

SEC:
https://www.sec.gov/Archives/edgar/data/1181412/000162828026052535/spcx-20260630.htm
https://www.sec.gov/Archives/edgar/data/1181412/000162828026052515/earningsreleaseq22608042.htm

Engineering:
https://job-boards.greenhouse.io/spacex/jobs/8555142002
https://job-boards.greenhouse.io/spacex/jobs/8559054002
https://job-boards.greenhouse.io/spacex/jobs/8559035002
https://job-boards.greenhouse.io/spacex/jobs/8517346002
https://job-boards.greenhouse.io/spacex/jobs/8717350002
https://job-boards.greenhouse.io/spacex/jobs/8658743002
https://job-boards.greenhouse.io/spacex/jobs/8463192002
https://job-boards.greenhouse.io/spacex/jobs/8782080002
https://job-boards.greenhouse.io/spacex/jobs/8243150002
https://job-boards.greenhouse.io/spacex/jobs/8573711002
https://job-boards.greenhouse.io/spacex/jobs/8577262002

Official:
https://new.spacex.com/spacexai/starmind
https://prod.cursor.com/blog/joining-spacex

---

**Статус: PUBLIC / VERIFIED DEEP ANALYSIS**

Эта версия является текущей рабочей точкой AI-исследования; v0.1 сохранён как исторический слой.
