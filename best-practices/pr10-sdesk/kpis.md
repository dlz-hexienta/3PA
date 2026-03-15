---
process_id: PR10
process_name: "Service Desk"
category: kpis
frameworks:
  - itil-v4
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Service Desk §2.4, §2.5 Table 2.5"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Desk — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the practice matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Service desk KPIs are mapped to two practice success factors: (1) enabling and continually improving effective, efficient, and convenient communications between the service provider and its users, and (2) enabling the effective integration of user communications into value streams. Service desk metrics should be measured in the context of the value streams to which the practice contributes.

---

## Essential KPIs (All tiers)

### KPI-SDESK-01: Query Recording Rate
<!-- sources: ITIL 4 Service Desk §2.4.2, §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of user interactions that are recorded as unique query records in the query log or workflow tool. Every interaction must be recorded — including queries requiring no further action — as record keeping is invaluable for demand analysis and service quality data. A low recording rate indicates that demand is being lost, which undermines all downstream processes and improvement efforts |
| **Formula** | (Recorded user queries / Estimated total user interactions) × 100 |
| **Target** | 100% |
| **Frequency** | Monthly |
| **Data Source** | Query management system, channel usage logs |
| **Owner** | Service Desk Manager |

### KPI-SDESK-02: Triage Accuracy
<!-- sources: ITIL 4 Service Desk §2.5 Table 2.5 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of user queries correctly triaged to the appropriate value stream and practice on the first attempt — without requiring reclassification or rerouting. Incorrect triage delays resolution, increases handling costs, and frustrates users. Measures the quality of the service desk's integration with other practices and the effectiveness of triage criteria |
| **Formula** | (Correctly triaged queries / Total triaged queries) × 100 |
| **Target** | ≥ 90%; trending upward |
| **Frequency** | Monthly |
| **Data Source** | Query management system, reclassification records |
| **Owner** | Service Desk Manager |

### KPI-SDESK-03: First Contact Resolution Rate
<!-- sources: ITIL 4 Service Desk §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of user queries resolved at first contact — during the initial interaction with the service desk, without requiring escalation or transfer to another team. Higher first contact resolution improves user satisfaction and reduces overall support costs. Should be balanced against the risk of agents spending excessive time on complex queries that should be escalated |
| **Formula** | (Queries resolved at first contact / Total queries received) × 100 |
| **Target** | ≥ 40%; trending upward (varies significantly by organization) |
| **Frequency** | Monthly |
| **Data Source** | Query management system |
| **Owner** | Service Desk Manager |

### KPI-SDESK-04: Channel Availability
<!-- sources: ITIL 4 Service Desk §2.2.1, §2.4.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of agreed operating hours during which communication channels are available and functioning correctly. Communication channels should be available where and when they are needed — as defined by the service agreement. Channel unavailability prevents users from contacting the service provider and represents a direct failure of the practice purpose |
| **Formula** | (Actual channel available hours / Agreed channel available hours) × 100 |
| **Target** | ≥ 99% for primary channels |
| **Frequency** | Monthly |
| **Data Source** | Channel monitoring, system availability reports |
| **Owner** | Service Desk Manager |

---

## Intermediate KPIs (T2+)

### KPI-SDESK-05: User Satisfaction with Service Desk
<!-- sources: ITIL 4 Service Desk §2.5 Table 2.5 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Satisfaction of users with the quality of information and the convenience of service desk communication channels — the primary measure of PSF1. Covers both the effectiveness of communication (did the user get what they needed?) and the convenience of the experience (was it easy and pleasant?). Should be measured separately for different channels and user groups to identify channel-specific and audience-specific issues |
| **Formula** | Average satisfaction score from user survey (scale 1–5 or equivalent) |
| **Target** | ≥ 4.0 / 5.0; trending upward |
| **Frequency** | Monthly or quarterly |
| **Data Source** | Post-interaction surveys, periodic satisfaction surveys |
| **Owner** | Service Desk Manager |

### KPI-SDESK-06: Information Quality
<!-- sources: ITIL 4 Service Desk §2.5 Table 2.5 PSF1, PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The quality of information received through and communicated via service desk channels — measured against agreed quality criteria including accuracy, completeness, timeliness, and relevance. Covers both inbound quality (information captured from users for processing by value streams — PSF2) and outbound quality (information communicated to users — PSF1). Poor information quality leads to rework, delays, and user dissatisfaction |
| **Formula** | Composite score from information quality assessment; or percentage of communications meeting quality criteria |
| **Target** | ≥ 90% meeting quality criteria; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Quality assessments, sample audits, stakeholder feedback |
| **Owner** | Service Desk Manager |

### KPI-SDESK-07: Self-Service Adoption Rate
<!-- sources: ITIL 4 Service Desk §3.2.1, §2.4.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of user queries handled through self-service channels (web portals, chatbots, IVR, mobile applications) rather than human interaction channels. Self-service reduces per-query costs, improves availability (often 24/7), and scales efficiently. Should be monitored alongside satisfaction to ensure self-service is not degrading user experience |
| **Formula** | (Queries handled via self-service / Total queries) × 100 |
| **Target** | Trending upward; target calibrated to organization |
| **Frequency** | Monthly |
| **Data Source** | Channel usage analytics |
| **Owner** | Service Desk Manager |

### KPI-SDESK-08: Average Response Time
<!-- sources: ITIL 4 Service Desk §2.4.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average time between a user submitting a query and receiving an initial acknowledgement or response from the service desk — measured by channel. Fast initial response is a key driver of user satisfaction and moments of truth. Long response times indicate capacity constraints, channel design issues, or prioritization problems |
| **Formula** | Average (First response timestamp − Query submission timestamp); by channel |
| **Target** | Within agreed service levels per channel; trending downward |
| **Frequency** | Monthly |
| **Data Source** | Query management system |
| **Owner** | Service Desk Manager |

---

## Advanced KPIs (T3)

### KPI-SDESK-09: Omnichannel Integration Score
<!-- sources: ITIL 4 Service Desk §2.2.1, §2.4.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | A composite assessment of the degree of omnichannel integration across communication channels — measuring whether users can switch between channels without losing context, whether contextual intelligence (history, profiles, pre-populated data) is available across channels, and whether information flows seamlessly. Distinguishes between multichannel (separate journeys per channel) and true omnichannel (continuous journey across channels) |
| **Formula** | Composite score from omnichannel maturity assessment (defined rubric) |
| **Target** | Trending upward; target calibrated to organizational maturity |
| **Frequency** | Semi-annually |
| **Data Source** | Channel integration assessment, user experience testing |
| **Owner** | Service Desk Manager |

### KPI-SDESK-10: Service Desk Cost per Query
<!-- sources: ITIL 4 Service Desk §4.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average cost of handling a user query through the service desk — including staff costs, technology costs, and overhead — measured by channel and query type. Provides a basis for optimizing the channel mix, assessing self-service ROI, and making informed decisions about organizational model (local vs virtual vs offshore). Lower costs per query indicate operational efficiency, but must be balanced against satisfaction and quality |
| **Formula** | Total service desk operating costs / Total queries handled; by channel |
| **Target** | Stable or declining; proportionate to service value |
| **Frequency** | Quarterly |
| **Data Source** | Financial records, query management system |
| **Owner** | Service Desk Manager |

### KPI-SDESK-11: Agent Utilization and Wellbeing
<!-- sources: ITIL 4 Service Desk §4.2.2, §6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The utilization rate of service desk agents (time spent handling queries vs available time) combined with indicators of agent wellbeing — staff turnover, satisfaction, and burnout indicators. High turnover and burnout are significant risks for service desk teams. External providers have developed specialized hiring, training, and performance management techniques specifically to address these risks. Utilization should be balanced — too high leads to burnout and quality issues, too low indicates overstaffing |
| **Formula** | Agent utilization: (Time handling queries / Available time) × 100; plus staff turnover rate and agent satisfaction score |
| **Target** | Utilization 60–80%; turnover below industry benchmark; agent satisfaction ≥ 3.5/5.0 |
| **Frequency** | Quarterly |
| **Data Source** | Workforce management system, HR records, agent surveys |
| **Owner** | Service Desk Manager |

### KPI-SDESK-12: Demand Capture Completeness
<!-- sources: ITIL 4 Service Desk §2.4.2, §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | An assessment of whether all demand for service provider interaction is being captured through service desk channels — including shadow IT queries handled outside official channels, informal support within teams, and unrecorded interactions. Incomplete demand capture means the organization lacks visibility into true support needs and cannot make informed capacity and improvement decisions |
| **Formula** | Qualitative assessment based on shadow channel monitoring, user surveys, and comparison of recorded queries against expected demand patterns |
| **Target** | All significant demand channels identified and integrated; no material shadow channels |
| **Frequency** | Semi-annually |
| **Data Source** | User surveys, shadow channel audits, demand analysis |
| **Owner** | Service Desk Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| SDESK-01 | Query Recording Rate | All | Monthly |
| SDESK-02 | Triage Accuracy | All | Monthly |
| SDESK-03 | First Contact Resolution Rate | All | Monthly |
| SDESK-04 | Channel Availability | All | Monthly |
| SDESK-05 | User Satisfaction with Service Desk | T2+ | Monthly/Quarterly |
| SDESK-06 | Information Quality | T2+ | Quarterly |
| SDESK-07 | Self-Service Adoption Rate | T2+ | Monthly |
| SDESK-08 | Average Response Time | T2+ | Monthly |
| SDESK-09 | Omnichannel Integration Score | T3 | Semi-annually |
| SDESK-10 | Service Desk Cost per Query | T3 | Quarterly |
| SDESK-11 | Agent Utilization and Wellbeing | T3 | Quarterly |
| SDESK-12 | Demand Capture Completeness | T3 | Semi-annually |
