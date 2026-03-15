---
process_id: PR05
process_name: "Service Catalogue Management"
category: kpis
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Service Catalogue Management §2.5 Table 2.2"
  - "FitSM-2: §PR2 SLM"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Catalogue Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the practice matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). This process applies at T2+ complexity. Service catalogue management KPIs are mapped to two practice success factors: (1) ensuring the service catalogue's structure and scope meet organizational requirements, and (2) ensuring the information in service catalogues meets stakeholders' current and anticipated needs.

---

## Essential KPIs (All tiers)

### KPI-SCATM-01: Catalogue Completeness
<!-- sources: ITIL 4 Service Catalogue Management §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of services managed by the organization that are represented in the service catalogue. Measures the completeness of catalogue coverage — services managed de facto but not included in the catalogue create information gaps for stakeholders. Should cover all in-scope services including internal, external, provided, and consumed services |
| **Formula** | (Services in the catalogue / Total services managed) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Service catalogue, service portfolio |
| **Owner** | Service Catalogue Manager |

### KPI-SCATM-02: Core Data Completeness
<!-- sources: ITIL 4 Service Catalogue Management §5.1, §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of service catalogue entries that have all mandatory core attributes populated — service name, description, status, owner, and target audience. Measures whether the foundational data quality requirement is being met. Missing core attributes make catalogue entries unusable for stakeholders |
| **Formula** | (Catalogue entries with all core attributes populated / Total catalogue entries) × 100 |
| **Target** | 100% |
| **Frequency** | Monthly |
| **Data Source** | Service catalogue data |
| **Owner** | Service Catalogue Manager |

### KPI-SCATM-03: Catalogue Error Rate
<!-- sources: ITIL 4 Service Catalogue Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and impact of catalogue errors — incorrect, missing, or dated information — detected in user- and customer-facing views during the reporting period. Catalogue errors should be treated as incidents. A high error rate indicates systemic data quality issues — insufficient update procedures, broken integrations, or lack of ownership for data accuracy |
| **Formula** | Count of catalogue errors per period; categorized by severity and impact |
| **Target** | Trending downward; zero critical errors |
| **Frequency** | Monthly |
| **Data Source** | Incident records (catalogue-related), error reports |
| **Owner** | Service Catalogue Manager |

### KPI-SCATM-04: Catalogue Requirements Fulfilment
<!-- sources: ITIL 4 Service Catalogue Management §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The degree to which the service catalogue design — structure, scope, views, and data sources — fulfils the agreed organizational requirements. Measured through compliance assessment against documented requirements. Gaps indicate that the catalogue design process has not adequately captured or implemented stakeholder needs |
| **Formula** | (Fulfilled requirements / Total agreed requirements) × 100 |
| **Target** | ≥ 90%; trending toward 100% |
| **Frequency** | Semi-annually |
| **Data Source** | Requirements documentation, compliance assessment |
| **Owner** | Service Catalogue Manager |

---

## Intermediate KPIs (T2+)

### KPI-SCATM-05: Stakeholder Satisfaction with Catalogue Information
<!-- sources: ITIL 4 Service Catalogue Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Stakeholder satisfaction with the information in the service catalogue — measured by stakeholder group (users, customers, internal teams, suppliers). The primary measure of PSF2. Low satisfaction indicates that catalogue content, accuracy, or presentation does not meet stakeholder needs. Should be measured separately for each stakeholder group to identify group-specific issues |
| **Formula** | Average satisfaction score by stakeholder group (scale 1–5 or equivalent) |
| **Target** | ≥ 4.0 / 5.0 across all groups; trending upward |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder satisfaction surveys |
| **Owner** | Service Catalogue Manager |

### KPI-SCATM-06: Stakeholder Satisfaction with Catalogue Interface
<!-- sources: ITIL 4 Service Catalogue Management §2.5 Table 2.2 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Stakeholder satisfaction with the service catalogue interface — usability, navigation, search, view settings, and overall experience. Measured separately from content satisfaction to distinguish between data quality issues and interface issues. For service providers addressing external markets, the catalogue interface is a critical factor in consumer engagement |
| **Formula** | Average satisfaction score by stakeholder group (scale 1–5 or equivalent) |
| **Target** | ≥ 4.0 / 5.0; trending upward |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder satisfaction surveys, usability assessments |
| **Owner** | Service Catalogue Manager |

### KPI-SCATM-07: Data Integration Health
<!-- sources: ITIL 4 Service Catalogue Management §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and impact of missing, ineffective, or manual integrations with information sources required for the catalogue. Measures whether the automated data flow from SLAs, CMDB, financial systems, and other sources is functioning correctly. Broken or manual integrations lead to stale data and increased maintenance effort |
| **Formula** | Count of integration issues per period; or (Functioning automated integrations / Total required integrations) × 100 |
| **Target** | ≥ 95% of integrations functioning; zero critical integration failures |
| **Frequency** | Monthly |
| **Data Source** | Integration monitoring, system health reports |
| **Owner** | Technical Specialist |

### KPI-SCATM-08: Improvement Implementation Progress
<!-- sources: ITIL 4 Service Catalogue Management §2.5 Table 2.2 PSF1, PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The progress of implementation of documented catalogue design and content improvements — both structural improvements (PSF1) and content/interface improvements (PSF2). Measures whether identified improvement opportunities are being actioned. A large backlog of unimplemented improvements indicates resource constraints or insufficient priority |
| **Formula** | (Improvements implemented / Total documented improvements) × 100; by category |
| **Target** | ≥ 80% of approved improvements implemented within agreed timeframes |
| **Frequency** | Quarterly |
| **Data Source** | Improvement register, change records |
| **Owner** | Service Catalogue Manager |

---

## Advanced KPIs (T3)

### KPI-SCATM-09: Catalogue Adoption Rate
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of the target audience that actively uses the service catalogue — measured by stakeholder group. Measures whether the catalogue is being adopted as the primary source of service information. Low adoption may indicate usability issues, awareness gaps, or competing information sources. Should be tracked alongside satisfaction to distinguish between "don't know about it" and "know about it but don't use it" |
| **Formula** | (Active catalogue users / Total target audience) × 100; by stakeholder group |
| **Target** | ≥ 80% across all groups; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Catalogue usage analytics, user records |
| **Owner** | Service Catalogue Manager |

### KPI-SCATM-10: Supplier Integration Coverage
<!-- sources: ITIL 4 Service Catalogue Management §6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of key third-party services that are integrated into the organization's service catalogue with automated data feeds — ensuring that catalogue information about third-party services is as current and actionable as internally provided services. Measures the maturity of supplier catalogue integration |
| **Formula** | (Third-party services with automated catalogue integration / Total key third-party services) × 100 |
| **Target** | ≥ 70%; trending upward |
| **Frequency** | Semi-annually |
| **Data Source** | Integration records, supplier management data |
| **Owner** | Service Catalogue Manager |

### KPI-SCATM-11: Data Freshness
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average age of the most recently verified data in catalogue entries — measuring how current the catalogue information is. Data freshness is critical for stakeholder trust — stale data erodes confidence in the catalogue as a reliable information source. Should be measured across core data and key view-specific attributes |
| **Formula** | Average (Current date − Last verified date) across catalogue entries; or percentage of entries verified within agreed freshness period |
| **Target** | ≥ 95% of entries verified within agreed freshness period |
| **Frequency** | Monthly |
| **Data Source** | Catalogue data audit records |
| **Owner** | Service Catalogue Manager |

### KPI-SCATM-12: Catalogue Automation Rate
<!-- sources: ITIL 4 Service Catalogue Management §5.2 Table 5.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of catalogue management activities that are automated — including data population, data updates, view generation, view delivery, access validation, and feedback collection. Higher automation reduces cost, improves timeliness, and reduces error rates. Measures the maturity of catalogue technology implementation |
| **Formula** | (Automated catalogue activities / Total catalogue activities) × 100 |
| **Target** | ≥ 80%; trending upward |
| **Frequency** | Semi-annually |
| **Data Source** | Automation assessment, system capabilities |
| **Owner** | Service Catalogue Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| SCATM-01 | Catalogue Completeness | All | Quarterly |
| SCATM-02 | Core Data Completeness | All | Monthly |
| SCATM-03 | Catalogue Error Rate | All | Monthly |
| SCATM-04 | Catalogue Requirements Fulfilment | All | Semi-annually |
| SCATM-05 | Stakeholder Satisfaction with Catalogue Information | T2+ | Semi-annually |
| SCATM-06 | Stakeholder Satisfaction with Catalogue Interface | T2+ | Semi-annually |
| SCATM-07 | Data Integration Health | T2+ | Monthly |
| SCATM-08 | Improvement Implementation Progress | T2+ | Quarterly |
| SCATM-09 | Catalogue Adoption Rate | T3 | Quarterly |
| SCATM-10 | Supplier Integration Coverage | T3 | Semi-annually |
| SCATM-11 | Data Freshness | T3 | Monthly |
| SCATM-12 | Catalogue Automation Rate | T3 | Semi-annually |
