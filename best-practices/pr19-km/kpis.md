---
process_id: PR19
process_name: "Knowledge Management"
category: kpis
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Knowledge Management §2.4, §2.5 Tables 2.2–2.3"
  - "IT4IT: Cross-cutting Functions"
last_updated: 2026-03-14
status: draft
---

# Knowledge Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the practice matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Knowledge management KPIs are mapped to two practice success factors: (1) establishing and maintaining an effective KM approach, and (2) integrating KM into all value streams and practices. Knowledge management has no dedicated FitSM process — KPIs draw primarily from ITIL 4. KM metrics are inherently difficult to measure — many rely on qualitative assessment and proxy indicators rather than direct measurement. Initial measurement may reveal baseline gaps in knowledge management maturity rather than performance levels.

---

## Essential KPIs (T2+)

### KPI-KM-01: Knowledge Management Approach Coverage
<!-- sources: ITIL 4 KM §2.5 Table 2.2 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of organizational practices and value streams that have their knowledge management scope, methods, and guidelines defined within the KM approach. Practices without KM coverage are managing knowledge on an ad hoc basis — knowledge capture, sharing, and reuse happen inconsistently or not at all, leading to knowledge loss and repeated discovery costs. Coverage should be measured against the agreed scope, expanding progressively as the practice matures |
| **Formula** | (Practices/value streams with defined KM scope and methods / Total practices/value streams in agreed scope) × 100 |
| **Target** | 100% of in-scope practices |
| **Frequency** | Quarterly |
| **Data Source** | KM approach document, practice inventory |
| **Owner** | Knowledge Manager |

### KPI-KM-02: Knowledge Asset Register Coverage
<!-- sources: ITIL 4 KM §2.5 Table 2.2 PSF1, §3.2.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of identified knowledge asset types that have records in the knowledge management system with defined classification, management guidelines, and assigned owners. Asset types without register coverage cannot be systematically managed, reviewed, or improved — they remain invisible to the practice. Coverage should be measured against all known knowledge asset types within the agreed scope |
| **Formula** | (Knowledge asset types with register records and assigned guidelines / Total identified knowledge asset types in scope) × 100 |
| **Target** | ≥ 90%; trending toward 100% |
| **Frequency** | Quarterly |
| **Data Source** | Knowledge management system, knowledge asset register |
| **Owner** | Knowledge Manager |

### KPI-KM-03: Information Request Fulfilment Rate
<!-- sources: ITIL 4 KM §2.5 Table 2.3 PSF2, §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of on-demand information requests that are fulfilled and accepted by the requesting stakeholders. Unfulfilled requests indicate either gaps in the organization's knowledge base, insufficient research capabilities, or misalignment between request expectations and delivery capabilities. Both completed-and-accepted and completed-but-returned requests should be tracked to distinguish quality issues from scope issues |
| **Formula** | (Information requests fulfilled and accepted / Total information requests received) × 100 |
| **Target** | ≥ 85% |
| **Frequency** | Quarterly |
| **Data Source** | Information request register |
| **Owner** | Knowledge Manager |

### KPI-KM-04: Information Request Turnaround Time
<!-- sources: ITIL 4 KM §2.5 Table 2.3 PSF2, §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average time from registration of an information request to delivery and acceptance of the information. Long turnaround times reduce the value of knowledge — information that arrives too late for the decision it was meant to support is wasted effort. Turnaround time should be measured against agreed service levels and tracked by request complexity category to enable meaningful comparison |
| **Formula** | Sum of (acceptance date − registration date) for all fulfilled requests / Number of fulfilled requests |
| **Target** | Within agreed service levels; trending downward |
| **Frequency** | Quarterly |
| **Data Source** | Information request register |
| **Owner** | Knowledge Manager |

---

## Intermediate KPIs (T2+)

### KPI-KM-05: Knowledge Asset Guideline Coverage
<!-- sources: ITIL 4 KM §2.5 Table 2.2 PSF1, §3.2.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of knowledge asset types that have documented management guidelines — specifying how assets of that type should be discovered, classified, maintained, reviewed, and retired. Asset types without guidelines are managed inconsistently — each team invents its own approach, leading to duplication, quality variance, and maintenance gaps. Guidelines should include responsibility assignments and applicable policy references |
| **Formula** | (Knowledge asset types with documented management guidelines / Total identified knowledge asset types in scope) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Knowledge asset management guidelines, knowledge management system |
| **Owner** | Knowledge Manager |

### KPI-KM-06: Knowledge Reuse Rate
<!-- sources: ITIL 4 KM §2.5 Table 2.3 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of information needs that are satisfied by existing knowledge assets (knowledge base articles, documented procedures, known error records) without requiring on-demand research. High reuse rates indicate that the knowledge base is well-maintained and accessible. Low reuse rates may indicate gaps in the knowledge base, poor search capabilities, or cultural resistance to using documented knowledge. Measured through knowledge base access logs, self-service resolution rates, and first-contact resolution using knowledge articles |
| **Formula** | (Information needs resolved through existing knowledge / Total information needs) × 100 |
| **Target** | ≥ 70%; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Knowledge management system access logs, service desk records |
| **Owner** | Knowledge Manager |

### KPI-KM-07: Stakeholder Satisfaction with Knowledge Services
<!-- sources: ITIL 4 KM §2.5 Table 2.2 PSF1, §3.2.1 Table 3.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Satisfaction of key stakeholders — including service desk agents, technical specialists, service owners, management, and knowledge consumers — with the quality, availability, timeliness, and usefulness of knowledge provided by the practice. Covers satisfaction with the knowledge base, on-demand information services, knowledge sharing channels, and the overall knowledge management culture. Low satisfaction may indicate that knowledge is hard to find, outdated, incomplete, or poorly structured |
| **Formula** | Average satisfaction score from stakeholder survey (scale 1–5 or equivalent) |
| **Target** | ≥ 4.0 / 5.0 |
| **Frequency** | Annually |
| **Data Source** | Stakeholder satisfaction surveys |
| **Owner** | Knowledge Manager |

### KPI-KM-08: Knowledge Asset Quality Score
<!-- sources: ITIL 4 KM §2.5 Table 2.2 PSF1, §3.2.1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | A composite score assessing the quality of knowledge assets against the organization's data and information quality guidelines — measuring accuracy, currency, completeness, comprehensibility, and relevance. Assessed through sampling and review of knowledge assets against quality criteria. Poor quality knowledge is worse than no knowledge — it leads to incorrect decisions, wasted effort, and erosion of trust in the knowledge management system |
| **Formula** | (Knowledge assets meeting quality criteria / Total knowledge assets reviewed) × 100 |
| **Target** | ≥ 90% |
| **Frequency** | Semi-annually |
| **Data Source** | Knowledge asset review records, quality audits |
| **Owner** | Knowledge Manager |

---

## Advanced KPIs (T3)

### KPI-KM-09: Knowledge Contribution Rate
<!-- sources: ITIL 4 KM §2.5 Table 2.3 PSF2, §2.2.5 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of organizational teams and practices that actively contribute to the knowledge base — creating new knowledge assets, updating existing ones, or sharing tacit knowledge through documented channels. Low contribution rates indicate that knowledge management is a consumer-only practice — people use knowledge but do not contribute, leading to a stagnating and increasingly outdated knowledge base. Contribution should be normalized by team size to avoid penalizing smaller teams |
| **Formula** | (Teams/practices with knowledge contributions in period / Total teams/practices in scope) × 100 |
| **Target** | ≥ 80%; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Knowledge management system contribution logs |
| **Owner** | Knowledge Manager |

### KPI-KM-10: KM Practice Adoption Across Value Streams
<!-- sources: ITIL 4 KM §2.5 Table 2.3 PSF2, §3.2.1 Table 3.2 Activity 5 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The extent to which knowledge management activities are embedded into organizational value streams — measured through adoption of knowledge capture at source, use of knowledge during service delivery, integration of knowledge activities into standard procedures, and participation in knowledge sharing channels. Adoption is the ultimate measure of PSF2 — a practice that exists on paper but is not embedded in daily work delivers no value |
| **Formula** | Composite adoption score based on: knowledge capture events per value stream transaction, knowledge article usage in service delivery, participation in knowledge sharing activities |
| **Target** | Positive trend; adoption increasing across all value streams |
| **Frequency** | Semi-annually |
| **Data Source** | Knowledge management system, value stream analytics, participation metrics |
| **Owner** | Knowledge Manager |

### KPI-KM-11: Organizational Absorptive Capacity
<!-- sources: ITIL 4 KM §2.2.4, §6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | A composite indicator of the organization's ability to recognize, assimilate, and apply new external knowledge — measured through the number and impact of external knowledge sources integrated into organizational practices, speed of adoption of external best practices, and effectiveness of partner and supplier knowledge sharing arrangements. Organizations with high absorptive capacity learn faster, adapt to changes more effectively, and derive more value from their partner and supplier relationships |
| **Formula** | Composite of: external knowledge sources monitored, external practices adopted, partner knowledge sharing effectiveness score |
| **Target** | Positive trend; expanding scope of external knowledge integration |
| **Frequency** | Annually |
| **Data Source** | KM approach reviews, partner relationship assessments, practice improvement records |
| **Owner** | Knowledge Manager |

### KPI-KM-12: KM Practice Cost Efficiency
<!-- sources: ITIL 4 KM §2.4 PSF1, §2.5 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The ratio of value generated by knowledge management activities to the total cost of the practice — including people, tools, and processes. Value generated is measured through avoided duplicate research, reduced incident resolution time through knowledge base use, reduced onboarding time for new staff, and prevented knowledge loss during organizational transitions. A mature knowledge management practice should generate substantially more value than it consumes — knowledge is an asset that appreciates with use |
| **Formula** | Value generated by KM (duplicate research avoided + resolution time saved + onboarding time saved + knowledge loss prevented) / Total KM practice costs |
| **Target** | > 1.0; trending upward |
| **Frequency** | Annually |
| **Data Source** | KM cost records, value tracking, impact assessments |
| **Owner** | Knowledge Manager |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| KM-01 | Knowledge Management Approach Coverage | T2+ | Quarterly |
| KM-02 | Knowledge Asset Register Coverage | T2+ | Quarterly |
| KM-03 | Information Request Fulfilment Rate | T2+ | Quarterly |
| KM-04 | Information Request Turnaround Time | T2+ | Quarterly |
| KM-05 | Knowledge Asset Guideline Coverage | T2+ | Quarterly |
| KM-06 | Knowledge Reuse Rate | T2+ | Quarterly |
| KM-07 | Stakeholder Satisfaction with Knowledge Services | T2+ | Annually |
| KM-08 | Knowledge Asset Quality Score | T2+ | Semi-annually |
| KM-09 | Knowledge Contribution Rate | T3 | Quarterly |
| KM-10 | KM Practice Adoption Across Value Streams | T3 | Semi-annually |
| KM-11 | Organizational Absorptive Capacity | T3 | Annually |
| KM-12 | KM Practice Cost Efficiency | T3 | Annually |
