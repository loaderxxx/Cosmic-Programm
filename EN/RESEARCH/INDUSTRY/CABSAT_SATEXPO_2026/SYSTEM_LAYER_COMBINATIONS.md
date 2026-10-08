# Space Industry Atlas — illustrative capability combinations

*Open research · 8 October 2026. These are conceptual arrangements of published industry capabilities, not products jointly validated or sold by these suppliers and not COSMOSYNTH partnerships.*

## Why this map exists

It separates a market **service operator** from a **modem vendor**, **antenna maker**, **ground-station integrator**, **digital IF processor** and **mission software vendor**, avoiding the mistake of treating every satellite company as a substitute.

## Illustrative configurations
### Virtual spacecraft + ground contact lifecycle

**Category:** Independent architectural illustration

- **Antaris, Inc.:** spacecraft mission virtualisation / onboard software model.
- **Calian:** network/pass orchestration and resource conflicts.
- **Amazon Web Services (AWS):** managed ground contact scheduling (Digital Twin feature after onboarding).

**Possible alternative roles, not required additional suppliers:** Kratos (virtual TT&C and monitoring products; event status unconfirmed); INTEGRASYS (link-budget/network planning, overlaps with Calian in parts).

**Critical qualification:** Mission command authority and ephemeris ownership must be separated from ground resource ownership. AWS Digital Twin is not a packet/telemetry dataflow test.

Source context: https://docs.aws.amazon.com/ground-station/latest/ug/digital-twin.html

### Turnkey ground station: owned vs managed alternatives

**Category:** Independent architectural illustration

- **Calian:** ground systems engineering and integration.
- **SatService GmbH:** antenna M&C and sat-nms system, within Calian corporate group.
- **AvL Technologies:** portable antenna/positioner candidate.
- **ETL Systems:** RF distribution / Digital IF candidate.

**Possible alternative roles, not required additional suppliers:** Celestia TTI (turnkey ground station and RF antenna provider); Amazon Web Services (AWS) (managed cloud ground station rather than equipment ownership); Kratos (virtualised TT&C functions, 2026 exhibiting unconfirmed).

**Critical qualification:** Calian and SatService are in one corporate group; avoid treating them as independent competitors for procurement. AWS cloud ground and owned antenna use different commercial/regulatory models.

Source context: https://satservicegmbh.de/about/calian.html

### DIFI/RF-over-IP digital ground subsystem

**Category:** Independent architectural illustration

- **ETL Systems:** ETL DIGITAL 1000 RF-over-IP digitisation and Amphinicy Blink software modem (2026 vendor demonstration).
- **INTEGRASYS:** INTEGRASYS Digital IF signal analysis (supplier claims compatibility with Calian/ETL/Kratos).

**Possible alternative roles, not required additional suppliers:** Calian (Calian DIFI digitizer/provider profile); Kratos (Kratos quantum wideband software processing, event role unconfirmed).

**Critical qualification:** DIFI is a constrained VITA49.2 profile; independently match packet type, stream and context IDs, timing, IQ format, security/transport, samplerates.

Source context: https://www.etlsystems.com/news/etl-systems-and-amphinicy-technologies-demonstrate-interoperable-digital-ground-segment-solution-at-satshow-2026/

### Commercial VSAT network / backhaul infrastructure

**Category:** Independent architectural illustration

- **SES:** operator satellite network/capacity (choose region/orbit).
- **ST Engineering iDirect:** one example VSAT hub/baseband/NMS family.
- **AvL Technologies:** terminal/antenna tracking option.
- **INTEGRASYS:** installation/commissioning/spectrum tools; documented historical iDirect Velocity integration.

**Possible alternative roles, not required additional suppliers:** Eutelsat (multi-orbit service alternative); AsiaSat (GEO/teleport service alternative); Comtech Telecommunications (alternative modem family); ND SatCom (alternative VSAT hub family); SpaceBridge Inc. (alternative VSAT hub family); Hughes (alternative JUPITER VSAT family); SATEC (SATEC antenna terminal alternative); StarWin (StarWin flat panel antenna alternative); Coxsat Technology Co., Ltd (Coxsat Ka phased array option); Guangdong Mikwave Communication Tech Ltd (Mikwave phased array alternative).

**Critical qualification:** Do NOT require five hubs to build one network. Select one modem family and validate operator coverage, antenna approvals, waveform compatibility, licences and service subscription.

Source context: https://www.stengg.com/en/newsroom/news-releases/st-engineering-idirect-streamlines-site-installation-process-for-intelsat-flexenterprise-customers/

### Small spacecraft + EO data supply chain

**Category:** Independent architectural illustration

- **Geoscan:** Geoscan 16U CubeSat platform and EO payload options.
- **Antaris, Inc.:** independent mission simulation option.
- **Calian:** ground coordination and pass scheduling option.
- **Neo Space Group:** Neo Space Group UP42 geospatial data marketplace/analytics.

**Possible alternative roles, not required additional suppliers:** Azercosmos (Azercosmos satellite imagery/space services (2026 event presence unconfirmed)); Amazon Web Services (AWS) (cloud ground-station contact workflow (not direct imaging payload access)); Kratos (Kratos smallsat TT&C virtual processing; event status unconfirmed).

**Critical qualification:** A supplier's satellite platform and another provider's EO data marketplace are not automatically connected or licensed to share spacecraft tasking/imagery.

Source context: https://www.geoscan.ru/en/products/cubesat-16U

### High-latitude connectivity and mobile resilient services

**Category:** Independent architectural illustration

- **Space Norway:** Space Norway Arctic HEO broadband infrastructure.
- **AvL Technologies:** AvL multi-orbit tracked terminal option.
- **IEC Telecom LLC:** IEC Telecom hybrid SATCOM/GSM field service concept.

**Possible alternative roles, not required additional suppliers:** Eutelsat (Eutelsat OneWeb LEO coverage where commercial service is available); Telesat (Telesat Lightspeed under deployment; full service availability requires verification).

**Critical qualification:** ASBM commercial payload services and military-hosted payload use cases are distinct. Access to government payloads is not assumed.

Source context: https://spacenorway.com/satellite-connectivity-solutions/vsat-data-services/arctic-satellite-broadband-mission/

### Gulf regional GEO, IoT and media services

**Category:** Published industry connection plus analytical system layers

- **Es'hailSat:** Es'hailSat GEO satellite service/orbital capacity.
- **GulfSat:** GulfSat announced Ku-band IoT service carried by Es'hail-1 in 2025.

**Possible alternative roles, not required additional suppliers:** Türksat (Türksat 2025 broadcast/IoT MoU with GulfSat, 2026 show attendance unconfirmed); Nilesat (Nilesat regional Ku/Ka operator alternative; 2026 show role unconfirmed); Space Communication Technologies (OmanSat) (OmanSat national satellite development (not necessarily operational fleet)).

**Critical qualification:** Public 2025 GulfSat/Türksat MoU is not a 2026 CABSAT agreement and not a COSMOSYNTH relationship. Satellite bandwidth may be resold, not a separate spacecraft integration.

Source context: https://www.gulfsat.com/news.html

### UAE capability development and industrial interface

**Category:** Independent architectural illustration

- **Calian:** ground segment engineering and resource orchestration.
- **Antaris, Inc.:** virtual mission test environment.
- **World Teleport Association:** World Teleport Association technical standards/certification benchmark.

**Possible alternative roles, not required additional suppliers:** ETL Systems (digital ground infrastructure cluster including Amphinicy); Amazon Web Services (AWS) (AWS software-only digital contact scheduler after onboarding).

**Critical qualification:** UAE Space Agency, Space42, Orbitworks are distinct institutions and companies **outside this original 55-event roster**; public summit/agency sources do not prove attendee meetings or authority.

Source context: https://space.gov.ae/en/projects-and-initiatives/space-economy/space-economic-zones

## Decision hygiene
- Public evidence is not a completed technical integration.
- Acquisitions and signed company agreements have specific dates and separate sources.
- Satellite coverage, waveform compatibility, RF qualification, legal approvals and API access are scenario-specific.
- COSMOSYNTH has not contacted or contracted these providers through this publication.

References: [Corporate & market relations](INDUSTRY_RELATIONSHIPS.md), [research methodology](METHODOLOGY.md).
