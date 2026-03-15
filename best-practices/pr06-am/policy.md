---
process_id: PR06
process_name: "Availability Management"
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
  - "ITIL 4: Availability Management §2.1–§2.4"
  - "FitSM-2: §PR4 SACM (availability scope)"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-13
status: draft
---

# Availability Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Availability Management §2.1, FitSM-2 §PR4 SACM Objective -->

The organization shall ensure that services deliver the agreed levels of availability to meet the needs of customers and users, cost-effectively. Availability requirements shall be identified, agreed, monitored, and reported for all services within the defined scope. Availability shall be designed into services from the outset and managed throughout the service lifecycle. The organization shall identify and treat availability risks through appropriate controls, selecting countermeasures that balance effectiveness against cost. Availability metrics shall reflect the business impact of service disruptions rather than the technical availability of service components alone. The organization shall continually analyse availability data and optimize availability controls to improve service quality.

## Objectives
<!-- sources: ITIL 4 Availability Management §2.4 PSFs, FitSM-2 §PR4 SACM Key Questions -->

1. Identify service availability requirements — ensuring that availability requirements are understood, reflect how service customers are impacted by outages, and are documented with clear criteria and measurable targets
2. Measure, assess, and report service availability — ensuring that availability is monitored accurately, reported in terms meaningful to stakeholders, and assessed against agreed targets
3. Treat service availability risks — identifying and managing risks that might impact service availability, designing and implementing appropriate controls, and optimizing the portfolio of controls for effectiveness and efficiency

## Scope

This policy applies to all services within the scope of the organization's service management system that have agreed availability targets. It covers:

- Identifying and agreeing service availability requirements with customers
- Defining what constitutes unavailability for each service
- Selecting metrics that reflect business impact
- Designing and configuring availability monitoring
- Monitoring, measuring, and reporting service availability
- Analysing availability data for trends and improvement opportunities
- Identifying and treating availability risks
- Planning and designing availability controls
- Continually optimizing availability controls

This policy does not cover: SLA negotiation (service level management), service design (service design), infrastructure implementation (infrastructure and platform management), event monitoring (monitoring and event management), incident response (incident management), or disaster recovery (service continuity management).

## Principles

### P1. Business-Impact-Oriented Measurement
<!-- sources: ITIL 4 Availability Management §2.2.4, §2.4.2 -->
Availability metrics shall reflect the business impact of service disruptions rather than the technical availability of service components. The ideal metric would measure financial losses due to unavailability; where this is impractical, the organization shall select metrics that approximate how customers lose value during outages. Simple uptime percentages, while useful, do not capture the severity of individual outages, the frequency of disruptions, or the varying impact of outages at different times.

### P2. Proactive Risk Treatment
<!-- sources: ITIL 4 Availability Management §2.3.1, §2.4.3 -->
The organization shall proactively identify and treat availability risks — focusing on reducing the likelihood of service failures through the elimination of single points of failure, improvement of component reliability, and implementation of fault-tolerant designs. Availability management focuses on high-probability risks and prevention, as distinct from service continuity management which focuses on high-impact events and recovery.

### P3. Cost-Effective Optimization
<!-- sources: ITIL 4 Availability Management §2.4.3 -->
The organization shall assess both the effectiveness and efficiency of availability controls. Effectiveness is assessed by comparing the risk reduction achieved against expected losses. Efficiency is assessed by comparing the cost of controls against their benefits. Controls should be implemented only when the expected reduction in losses justifies the investment. The organization shall consider all forms of loss: productivity, response costs, replacement costs, SLA fines, competitive advantage, and reputation.

### P4. Lifecycle Integration
<!-- sources: ITIL 4 Availability Management §2.1, §2.4.3 -->
Availability shall be managed throughout the product and service lifecycle — from ideation and design through to operations. Decisions made during service design significantly affect availability levels and the organization's ability to manage them. It is usually cheaper to design the right level of availability from the start rather than try to add it subsequently. Once a service gains a reputation for unreliability, it becomes very difficult to repair.

### P5. Transparency and Consistency
<!-- sources: ITIL 4 Availability Management §2.1 -->
The organization shall ensure a transparent, consistent, and practical understanding of availability — expected, agreed, designed, and actual — among all relevant parties. Availability criteria, metrics, and targets shall be clearly documented and communicated to customers, service owners, and technical teams.

### P6. Differentiated Approach
<!-- sources: ITIL 4 Availability Management §2.2.1, §2.2.2 -->
Availability design and investment shall be differentiated based on the criticality of the business functions supported by each service. The more vital the business function, the more resilient and available the supporting service needs to be. Different types of services — those enabling business operations, providing resource access, or including fulfilment actions — may require different approaches to defining and measuring availability.

### P7. Continual Improvement
<!-- sources: ITIL 4 Availability Management §3.2.2 -->
The organization shall continually analyse availability data to identify trends, patterns, and improvement opportunities. Availability levels shall be reviewed regularly as business needs and customer demand change. Continually considering opportunities to optimize availability can achieve enhanced levels of availability at lower costs.

## Mandatory Requirements

### Essential (All tiers)

| ID | Requirement |
|----|------------|
| AM-R01 | Availability requirements shall be identified for all services with agreed availability targets, including the vital business functions supported and the impact of service outages on customers |
| AM-R02 | Availability requirements shall be agreed with customers, balancing required availability levels with cost and achievability |
| AM-R03 | An availability monitoring approach shall be defined for all services with agreed availability targets, specifying how service outages will be tracked and recorded |
| AM-R04 | Service availability shall be monitored on an ongoing basis, with availability data collected and aligned to the agreed availability criteria |
| AM-R05 | Service availability shall be reported to customers and management against agreed targets at defined intervals |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| AM-R06 | Formal availability criteria shall be defined for each service, documenting the conditions under which the service is considered unavailable — including underperformance thresholds, user impact scope, and service schedule considerations |
| AM-R07 | Availability metrics shall be selected that reflect the business impact of service disruptions — going beyond simple uptime percentage to include measures such as MTBF, MTRS, number of disruptions, and maximum single outage |
| AM-R08 | Availability data shall be analysed periodically for trends, patterns, and deviations from agreed levels, with corrective action undertaken when faults are found |
| AM-R09 | Availability risks shall be assessed and availability controls shall be planned and designed to meet current and future availability requirements, documented in availability management plans |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| AM-R10 | Availability controls shall be assessed for effectiveness and efficiency using cost-benefit analysis, comparing control costs against expected loss reduction |
| AM-R11 | Service health models shall be developed for critical services to enable accurate service-level availability measurement from infrastructure monitoring data |

## Compliance and Review

- This policy shall be reviewed at least annually or following a significant change to the organization's service portfolio, technology landscape, or regulatory environment
- Compliance with this policy shall be assessed through service availability reports, availability target achievement data, and periodic reviews of availability management plans
- Non-compliance shall be escalated to the availability manager and service management leadership for remediation
- Exceptions to this policy require documented justification and approval from the availability manager or senior leadership

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Service Level Management Policy (PR02) | Availability requirements are derived from SLAs. Availability reporting feeds SLA achievement reporting. The availability management practice provides expertise to SLM during service level negotiation |
| Service Continuity Management Policy (PR07) | Related but distinct concerns — availability focuses on high-probability/proactive risks; continuity focuses on high-impact/reactive events. Both share VBF identification, BIA, and risk assessment |
| Risk Management Policy (PR21) | Risk information supports availability planning. Availability controls are a major category of risk mitigation measures |
| Change Management Policy (PR15) | Change impact analysis includes availability assessment. Availability controls are implemented through authorized changes |
| Incident Management Policy (PR11) | Incident records provide availability data. Availability analysis identifies patterns for incident management |
| Monitoring & Event Management Policy (PR14) | Monitoring tools provide availability data. Availability management defines monitoring requirements |
| Capacity & Performance Management Policy (PR08) | Related service quality concerns affecting the same CIs. The practices share resources and information but require clear separation of responsibilities |
| Information Security Management Policy (PR09) | Related service quality concerns. Security incidents can cause availability incidents. Controls must be coordinated |
