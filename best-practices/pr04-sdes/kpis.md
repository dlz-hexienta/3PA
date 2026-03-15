---
process_id: PR04
process_name: "Service Design"
category: kpis
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T3
sources:
  - "ITIL 4: Service Design §2.4, §2.5 Table 2.4"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Design — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the practice matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). This process applies only at T3 complexity. Service design KPIs are mapped to two practice success factors: (1) establishing and maintaining an effective organization-wide approach to service design, and (2) ensuring that services are fit for purpose and fit for use throughout their lifecycle. Design effectiveness should be measured in the context of the value streams to which the practice contributes.

---

## Essential KPIs (All tiers)

### KPI-SDES-01: SDP Completeness
<!-- sources: ITIL 4 Service Design §2.2.3, §2.4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of new or significantly changed services that have a complete service design package (SDP) addressing all four dimensions of service management — organizations and people, information and technology, partners and suppliers, and value streams and processes — with CX/UX considerations documented. Measures whether the foundational design artefact is being produced and maintained to the agreed standard. Incomplete SDPs increase the risk of design gaps being discovered during transition or operation |
| **Formula** | (Services with complete SDPs / Total new or significantly changed services) × 100 |
| **Target** | ≥ 90%; trending toward 100% |
| **Frequency** | Quarterly |
| **Data Source** | Service design records, SDP repository |
| **Owner** | Service Design Leader |

### KPI-SDES-02: Design Approach Coverage
<!-- sources: ITIL 4 Service Design §2.4.1, §2.5 Table 2.4 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of the organization's product and service portfolio that is covered by a defined and agreed service design approach. Measures adherence to the service design approach across the portfolio — a primary metric for PSF1. Gaps indicate areas where design is ad hoc rather than governed, increasing risk of inconsistency and design failure |
| **Formula** | (Products and services with a defined design approach / Total products and services) × 100 |
| **Target** | ≥ 80%; trending toward 100% |
| **Frequency** | Semi-annually |
| **Data Source** | Service design approach documentation, service portfolio |
| **Owner** | Service Design Leader |

### KPI-SDES-03: Fitness for Purpose Rate
<!-- sources: ITIL 4 Service Design §2.5 Table 2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of products and services meeting their agreed requirements for utility — the functional aspects that determine whether the service is fit for purpose. Measured through service design reviews, acceptance testing outcomes, and post-implementation assessments. A low rate indicates systemic design quality issues — requirements are not being properly captured, translated, or verified during the design process |
| **Formula** | (Products and services meeting utility requirements / Total products and services assessed) × 100 |
| **Target** | ≥ 95%; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Service design review reports, acceptance test results, post-implementation reviews |
| **Owner** | Service Design Leader |

### KPI-SDES-04: Fitness for Use Rate
<!-- sources: ITIL 4 Service Design §2.5 Table 2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of products and services meeting their agreed requirements for warranty — the non-functional aspects that determine whether the service is fit for use, including availability, capacity, continuity, and security. Warranty requirements are often more complex to design for than utility requirements as they span multiple practices and require holistic coordination. A low rate indicates that non-functional requirements are being inadequately addressed during design |
| **Formula** | (Products and services meeting warranty requirements / Total products and services assessed) × 100 |
| **Target** | ≥ 90%; trending upward |
| **Frequency** | Quarterly |
| **Data Source** | Service design review reports, operational performance data, SLA achievement |
| **Owner** | Service Design Leader |

---

## Intermediate KPIs (T2+)

### KPI-SDES-05: Stakeholder Satisfaction with Design Capability
<!-- sources: ITIL 4 Service Design §2.5 Table 2.4 PSF1, PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Stakeholder satisfaction with the organization's ability to design products and services — including satisfaction with the chosen design approaches, design models and methods, and the quality of design outcomes. Covers both PSFs — whether the approach is effective and whether the resulting designs are fit for purpose and use. Low satisfaction may indicate misalignment between design approaches and stakeholder expectations, or quality issues in design execution |
| **Formula** | Average satisfaction score from stakeholder survey (scale 1–5 or equivalent) |
| **Target** | ≥ 4.0 / 5.0; trending upward |
| **Frequency** | Semi-annually |
| **Data Source** | Stakeholder satisfaction surveys |
| **Owner** | Service Design Leader |

### KPI-SDES-06: Design Review Completion Rate
<!-- sources: ITIL 4 Service Design §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of completed service design instances that underwent a formal design review — assessing compliance with standards and conventions, verifying SDP completeness, and capturing lessons learned. Measures whether the feedback loop in the design process is operating. Skipped reviews mean design quality issues are not detected and lessons are not captured, leading to repeated failures |
| **Formula** | (Design instances with completed reviews / Total completed design instances) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Service design review reports, design records |
| **Owner** | Service Design Leader |

### KPI-SDES-07: Design-Attributable Defect Rate
<!-- sources: ITIL 4 Service Design §2.1, §2.4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and severity of defects, incidents, or failures in live operation that are attributable to design gaps — including functional gaps, non-functional shortfalls, missing CX/UX considerations, and integration failures. Provides a lagging indicator of design quality. A high rate indicates that the design process is not adequately addressing requirements, risks, or operational needs. Each defect should be traced back to identify the design gap root cause |
| **Formula** | Count of design-attributable defects per period; categorized by severity |
| **Target** | Trending downward; zero critical design defects |
| **Frequency** | Quarterly |
| **Data Source** | Incident records, problem records, post-implementation reviews |
| **Owner** | Service Design Leader |

### KPI-SDES-08: Design Cycle Time
<!-- sources: ITIL 4 Service Design §2.4.2, §3.2.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The average elapsed time from service design initiation to design review completion — measured by design instance category. Provides a leading indicator of design process efficiency. Excessively long cycle times may indicate process bottlenecks, resource constraints, or overly complex models. Excessively short cycle times for complex designs may indicate insufficient design rigour. Should be calibrated by design instance complexity |
| **Formula** | Average (Design review completion date − Design initiation date); by category |
| **Target** | Stable or declining for comparable categories; within agreed timeframes |
| **Frequency** | Quarterly |
| **Data Source** | Service design records |
| **Owner** | Service Design Consultant |

---

## Advanced KPIs (T3)

### KPI-SDES-09: Innovation by Design Score
<!-- sources: ITIL 4 Service Design §2.5 Table 2.4 PSF1 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Stakeholder satisfaction with the organization's ability to innovate by design — including the use of design thinking techniques, the ability to explore creative solutions, and the responsiveness of the design practice to emerging needs and opportunities. Measures whether the design practice is enabling innovation or merely processing requirements. Low scores indicate that the practice may be overly prescriptive or that design thinking is not being effectively applied |
| **Formula** | Average satisfaction score from innovation assessment (scale 1–5 or equivalent) |
| **Target** | ≥ 3.5 / 5.0; trending upward |
| **Frequency** | Annually |
| **Data Source** | Stakeholder surveys, innovation assessments |
| **Owner** | Service Design Leader |

### KPI-SDES-10: Risk Tier Coverage
<!-- sources: ITIL 4 Service Design §2.2.5 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of the organization's services that have been risk-profiled and assigned to a service tier using the agreed risk modelling methodology — including profiling at service line, customer journey, and IT service levels as appropriate. Measures whether risk-aligned design is being applied across the portfolio. Services without risk profiles may be over- or under-designed for their actual risk exposure |
| **Formula** | (Services with completed risk profiles and tier assignments / Total services) × 100 |
| **Target** | ≥ 80%; trending toward 100% |
| **Frequency** | Semi-annually |
| **Data Source** | Risk profiling records, service portfolio |
| **Owner** | Service Design Leader |

### KPI-SDES-11: Design Financial Efficiency
<!-- sources: ITIL 4 Service Design §2.5 Table 2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | Stakeholder satisfaction with the financial efficiency of service design — assessing whether design activities are cost-effective relative to the value they deliver. Measures whether design is perceived as a value-adding investment rather than an overhead. Includes assessment of whether the level of design activity is proportionate to the risk and complexity of each service |
| **Formula** | Average satisfaction score from financial efficiency assessment (scale 1–5 or equivalent); or ratio of design cost to service value |
| **Target** | ≥ 3.5 / 5.0; trending upward |
| **Frequency** | Annually |
| **Data Source** | Stakeholder surveys, design cost records, service financial data |
| **Owner** | Service Design Leader |

### KPI-SDES-12: Waiver and Dispensation Rate
<!-- sources: ITIL 4 Service Design §2.2.4.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The number and status of active service design waivers and dispensations — cases where service performance does not meet the requirements stipulated by the service design package. Measures whether risk exposure from design gaps is being actively managed. A high number of waivers without remediation plans indicates systemic design or delivery capability gaps. Enduring waivers (without milestone dates) represent ongoing unmitigated risk |
| **Formula** | Count of active waivers; percentage with agreed remediation milestone dates; average age of waivers |
| **Target** | Trending downward; 100% with remediation plans; zero enduring waivers without business acceptance |
| **Frequency** | Quarterly |
| **Data Source** | Waiver register, continual improvement register |
| **Owner** | Service Design Leader |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| SDES-01 | SDP Completeness | All | Quarterly |
| SDES-02 | Design Approach Coverage | All | Semi-annually |
| SDES-03 | Fitness for Purpose Rate | All | Quarterly |
| SDES-04 | Fitness for Use Rate | All | Quarterly |
| SDES-05 | Stakeholder Satisfaction with Design Capability | T2+ | Semi-annually |
| SDES-06 | Design Review Completion Rate | T2+ | Quarterly |
| SDES-07 | Design-Attributable Defect Rate | T2+ | Quarterly |
| SDES-08 | Design Cycle Time | T2+ | Quarterly |
| SDES-09 | Innovation by Design Score | T3 | Annually |
| SDES-10 | Risk Tier Coverage | T3 | Semi-annually |
| SDES-11 | Design Financial Efficiency | T3 | Annually |
| SDES-12 | Waiver and Dispensation Rate | T3 | Quarterly |
