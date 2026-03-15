---
process_id: PR07
process_name: "Service Continuity Management"
category: policy
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
  - "ITIL 4: Service Continuity Management §2.1, §2.2, §2.3, §2.4"
  - "FitSM-1: §PR4.1–§PR4.3"
  - "IT4IT: D2C Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Continuity Management — Best Practice Policy

## How to Use This Policy Template

This policy establishes the governing principles and mandatory requirements for the service continuity management practice. It should be customized to reflect the organization's risk profile, regulatory environment, service portfolio criticality, and relationship to the broader business continuity management function. Requirements are graduated by maturity — organizations should implement Essential requirements first, then layer on Intermediate and Advanced requirements as the practice matures. In FitSM, service continuity is managed together with availability in PR4 SACM — this policy covers the continuity scope only.

---

## Policy Principles

### 1. Organizational Resilience
<!-- sources: ITIL 4 SCM §2.1 -->

Service continuity management shall provide a framework for building organizational resilience — the capability to produce an effective response that safeguards the interests of key stakeholders, the organization's reputation, brand, and value-creating activities. The practice shall ensure readiness to respond to high-impact incidents that disrupt the organization's core activities or credibility.

### 2. Risk-Based Approach
<!-- sources: ITIL 4 SCM §2.3.3, FitSM-1 §PR4.2 -->

Service continuity management shall focus on high-impact, low-probability risks which cannot be totally prevented — disasters, emergencies, and crises. The practice shall mitigate these risks by minimizing expected losses so that, when disasters occur, they do not cause damage beyond predefined acceptable levels. Risk information shall be obtained through the risk management practice and continuity risks shall be assessed at planned intervals.

### 3. BIA-Driven Requirements
<!-- sources: ITIL 4 SCM §2.2.5, §2.4.1 -->

Service continuity requirements — including recovery time objectives, recovery point objectives, and minimum target service levels — shall be derived from business impact analysis. BIA shall identify vital business functions, analyse disruption consequences, identify interdependencies, and determine recovery requirements. Requirements shall drive strategy selection, plan development, and resource allocation.

### 4. Plans Must Be Tested
<!-- sources: ITIL 4 SCM §2.4.3 -->

Recovery plans that have not been tested often do not work as intended. Testing and exercising shall be a critical part of the practice — the only way of ensuring that selected strategies, implemented measures, and plans are actually working. All parts of the practice — site, team member, service, or configuration item — shall be tested at least once a year.

### 5. Cost-Effective Measures
<!-- sources: ITIL 4 SCM §2.4.2 -->

Service continuity measures shall be assessed for both effectiveness and efficiency. The effects of a measure shall be compared against expected losses from the disruptive event. The cost of implementation shall be compared against the benefit — calculated by estimating risk reduction multiplied by expected impact. The organization shall invest proportionately — more preventive measures for higher-impact, faster-developing disruptions; more recovery measures where impact is lower and develops slowly.

### 6. Integration with Business Continuity
<!-- sources: ITIL 4 SCM §2.1, §2.2 -->

Service continuity management shall be integrated with the broader business continuity management function where one exists. Service continuity plans shall provide a clear interface to business continuity plans. In a digitally-enabled service economy, the boundaries between IT continuity and business continuity are increasingly blurred — integration is both possible and beneficial.

### 7. Continual Improvement
<!-- sources: ITIL 4 SCM §3.2.3, §3.2.4, FitSM-1 §PR4.3 -->

Service continuity arrangements shall be subject to continual improvement — informed by exercise findings, actual recovery experience, audit results, environmental changes, and technology opportunities. Plans, strategies, and controls shall be updated to reflect lessons learned. Failed exercises and failed recoveries shall trigger immediate review and plan revision.

---

## Mandatory Requirements

### Essential (T2+)
<!-- sources: ITIL 4 SCM §2.3, §2.4, §3.2.1, §3.2.2, FitSM-1 §PR4.1, §PR4.2 -->

| # | Requirement |
|---|-------------|
| 1 | The scope of service continuity management shall be defined — specifying which services, products, sites, and locations are covered, and which events constitute disasters requiring invocation of continuity plans |
| 2 | Business impact analysis shall be performed for all services within scope — identifying vital business functions, analysing disruption consequences, and determining RTO, RPO, and minimum target service levels |
| 3 | Service continuity strategies shall be selected based on BIA outputs — balancing preventive and recovery measures against impact profiles and cost constraints |
| 4 | Service continuity plans shall be developed and maintained at strategic, tactical, and operational levels — covering response, recovery, and restoration stages with clear, action-oriented procedures |
| 5 | Roles and responsibilities for service continuity management — including crisis management, recovery coordination, and plan execution — shall be documented and communicated to all relevant parties |

### Intermediate (T2+)
<!-- sources: ITIL 4 SCM §2.4.2, §2.4.3, §3.2.4, FitSM-1 §PR4.3 -->

| # | Requirement |
|---|-------------|
| 6 | An exercise programme shall be maintained ensuring all parts of the practice are tested at least annually — using exercise types appropriate to the risk level and covering all four dimensions of service management |
| 7 | Exercise and recovery reports shall document findings and recommendations. Failed exercises shall be rescheduled. All findings shall be fed into plan updates and improvement initiatives |
| 8 | Service continuity audits shall be conducted to ensure BIA, strategies, and plans remain appropriate and relevant. Audits may be scheduled or triggered by failed exercises, failed recoveries, or significant environmental changes |
| 9 | Risk mitigation measures shall be assessed for effectiveness (against expected losses) and efficiency (cost versus benefit). Appropriate measures shall be implemented across all four dimensions of service management |

### Advanced (T3)
<!-- sources: ITIL 4 SCM §2.3.1, §6 -->

| # | Requirement |
|---|-------------|
| 10 | Service continuity requirements shall be negotiated and agreed with partners and suppliers — ensuring third-party continuity arrangements align with organizational plans. Partners shall be involved in plan development, testing, and execution |
| 11 | Service continuity management shall be integrated with the broader business continuity management function — with clear interfaces between service continuity plans and business continuity plans at all levels |
| 12 | BIA, strategies, and plans shall be reviewed at least annually and when significant changes occur — new services, new customers, new partnerships, uncovered events, or regulatory changes. Scope and policies shall be formally revised |

---

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Availability Management Policy (PR06) | Closely related — both address service resilience. Availability focuses on high-probability prevention; continuity on high-impact response. May be merged |
| Risk Management Policy (PR21) | Risk assessments inform BIA and continuity planning. Continuity measures contribute to organizational risk mitigation |
| Incident Management Policy (PR11) | Major incidents may escalate to disasters. Clear invocation criteria distinguish the two practices |
| Service Level Management Policy (PR02) | SLAs define continuity requirements and RTO/RPO targets |
| Information Security Management Policy (PR09) | Cyber attacks are a key disaster scenario. Security controls support continuity measures |
| Service Design Policy (PR04) | Continuity solutions are designed as part of the service model |
| Change Management Policy (PR15) | Infrastructure resilience measures are implemented through change management |
| Supplier Management Policy (PR23) | Third-party continuity arrangements must align with organizational plans |
