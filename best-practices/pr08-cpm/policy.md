---
process_id: PR08
process_name: "Capacity & Performance Management"
category: policy
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Capacity & Performance Management §2.1–§2.4"
  - "FitSM-2: §PR5 CAPM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Capacity & Performance Management — Best Practice Policy

## Policy Principles
<!-- sources: ITIL 4 Capacity & Performance Management §2.1, §2.4.1–§2.4.3, FitSM-2 §PR5 CAPM Objective -->

### 1. Business-Impact-Oriented Measurement
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.2 -->
Capacity and performance metrics shall reflect the business impact of service degradation rather than the technical performance of service components alone. Measurements must be understandable from the user perspective as well as the technical perspective. Technical component metrics support but do not replace business-level performance indicators.

### 2. Proactive Demand Management
<!-- sources: ITIL 4 Capacity & Performance Management §2.1, §2.4.1, FitSM-2 §PR5 CAPM -->
Capacity planning shall anticipate future demand rather than react to capacity shortfalls after they occur. Business activity patterns, transaction volumes, and demand forecasts shall inform both immediate capacity provisioning and longer-term architectural decisions. The practice shall be applied throughout the product and service lifecycle — from ideation and design through to operations.

### 3. Cost-Effective Optimization
<!-- sources: ITIL 4 Capacity & Performance Management §2.1, §2.4.3, §3.2.2 Table 3.4 -->
Capacity and performance controls shall balance service performance levels against cost. Over-provisioning wastes resources; under-provisioning risks service degradation. When demand reaches certain thresholds, architectural changes may be more cost-effective than continued linear scaling. The organization shall evaluate the cost-benefit ratio of different capacity options and choose the approach that achieves required performance at acceptable cost.

### 4. Lifecycle Integration
<!-- sources: ITIL 4 Capacity & Performance Management §2.1, §2.3 -->
Capacity and performance management shall be integrated throughout the product and service lifecycle. Decisions made during design and transition stages affect performance constraints and the organization's ability to monitor and manage capacity. The practice provides a centre of expertise for capacity-related matters and supports other service management practices — including service design, service level management, and change enablement.

### 5. Transparency and Consistency
<!-- sources: ITIL 4 Capacity & Performance Management §2.2 -->
The organization shall ensure a transparent, consistent, and practical understanding of capacity and performance — expected, agreed, designed, and actual — among all relevant parties. Performance criteria shall clearly define the line between acceptable performance variation and reportable degradation. Reporting shall present capacity and performance information consistently across services.

### 6. Differentiated Approach
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.1, §2.4.3 -->
Capacity and performance criteria and controls shall be tailored to each service based on its criticality, the vital business functions it supports, and the scale of user impact. Services supporting critical business functions warrant more stringent performance criteria and more robust capacity controls. The scale factor — whether degradation affects significant numbers of users or individuals — shall be considered when defining performance criteria.

### 7. Continual Improvement
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.3, §3.2.2 Table 3.4, FitSM-2 §PR5 CAPM -->
Capacity and performance controls shall be regularly reviewed and optimized for effectiveness and efficiency. Trend analysis, demand forecasting, and control assessments shall drive improvement initiatives. The practice shall identify opportunities to reduce waste, improve architectural efficiency, and enhance service performance.

---

## Mandatory Requirements
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.1–§2.4.3, §3.2.1, §3.2.2, FitSM-2 §PR5 CAPM -->

### Essential (All tiers)

| # | Requirement |
|---|-------------|
| 1 | Capacity and performance requirements shall be identified and documented for all services with agreed performance targets, including the vital business functions supported, critical service actions, and acceptable performance levels |
| 2 | Performance criteria shall clearly define what constitutes acceptable performance, performance degradation, and unavailability — considering acceptable delays, unacceptable degradation, and the scale of user impact |
| 3 | Capacity and performance shall be monitored using agreed methods and tools appropriate to the service type and scale — from incident-record-based tracking to infrastructure monitoring and real user monitoring |
| 4 | Service capacity and performance shall be reported against agreed targets through regular reports or dashboards, focusing on the consumer experience of service productivity and responsiveness |
| 5 | Capacity and performance data shall be provided to service level management for SLA achievement reporting |

### Intermediate (T2+)

| # | Requirement |
|---|-------------|
| 6 | Capacity and performance metrics shall be selected to reflect the business impact of service degradation, going beyond component-level technical indicators to include service transaction response times, throughput rates, and user-experienced performance |
| 7 | Capacity and performance reports and dashboards shall be designed for different stakeholder groups, presenting data meaningfully with technical indicators supporting the business-level view |
| 8 | Trend analysis shall be performed on capacity utilization and performance data to detect patterns, forecast future demand, and identify components approaching capacity limits |
| 9 | Capacity plans shall be produced covering current capacity and performance levels, anticipated changes in demand, planned resource changes, and recommended actions with timelines and costs |

### Advanced (T3)

| # | Requirement |
|---|-------------|
| 10 | Existing capacity and performance controls shall be assessed for effectiveness — comparing the risk reduction achieved against expected losses — and efficiency — comparing control costs against benefits |
| 11 | Capacity models shall be developed that relate business demand forecasts to resource requirements across service components, informing architectural decisions and IT budget planning |
| 12 | Architectural changes shall be recommended when demand patterns indicate that linear scaling is no longer the most cost-effective approach — evaluating alternative designs that improve performance at lower cost |

---

## Related Policies
<!-- sources: ITIL 4 Capacity & Performance Management §2.3 Table 2.1 -->

| Related Policy | Relationship |
|----------------|-------------|
| Service Level Management Policy (PR02) | Performance criteria and targets are derived from SLAs. Performance reporting feeds SLA achievement reporting. The capacity and performance management practice supports SLM with service component expertise during SLA negotiations |
| Availability Management Policy (PR06) | Capacity/performance and availability address related but distinct quality aspects of the same services. Performance focuses on throughput and speed under varying demand; availability focuses on whether the service is functioning. The practices share resources and information but require clear separation of responsibilities |
| Service Continuity Management Policy (PR07) | Continuity requirements may include minimum capacity levels for recovery scenarios. Capacity constraints affect recovery time and performance objectives |
| Risk Management Policy (PR21) | Risk information supports capacity planning. Capacity and performance controls contribute to risk mitigation. Risk identification and prioritization are key to the practice |
| Change Management Policy (PR15) | Change impact analysis includes capacity and performance assessment. Capacity controls are implemented through authorized changes |
| Monitoring & Event Management Policy (PR14) | Monitoring tools provide capacity utilization and performance data. The capacity practice defines monitoring requirements, thresholds, and alerts |
| Service Design Policy (PR04) | Capacity and performance controls are designed as part of the service model. The practice provides input on performance-optimal architectures |
| Financial Management Policy (PR03) | Capacity plans inform IT budget planning. Cost-benefit analysis of capacity options supports investment decisions |
