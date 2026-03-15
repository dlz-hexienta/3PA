---
process_id: PR11
process_name: "Incident Management"
category: policy
frameworks:
  - itil-v4
  - fitsm
  - it4it
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Incident Management §2.1, §2.3, §2.4"
  - "FitSM-2: §PR9 ISRM (incident scope)"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (incident coordination)"
last_updated: 2026-03-13
status: draft
---

# Incident Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Incident Management §2.1, §2.3, FitSM-2 §PR9 ISRM Objective -->

The organization shall minimize the negative impact of incidents on the business by restoring normal service operation as quickly as possible. All incidents — unplanned interruptions to a service or reductions in the quality of a service — shall be detected, registered, classified, prioritized, diagnosed, resolved, and closed using a consistent, repeatable approach. The organization shall establish clear criteria for identifying major incidents and operate a dedicated procedure for their coordinated resolution. Incident handling shall be supported by defined incident models, a priority matrix based on impact and urgency, documented escalation paths, and effective use of the known error database. The organization shall periodically review incident data to identify trends, improve incident models, and drive continual improvement of incident management approaches.

## Objectives
<!-- sources: ITIL 4 Incident Management §2.4 PSFs, FitSM-2 §PR9 ISRM Key Questions -->

1. Detect incidents as early as possible — ideally before users are aware of service degradation — through effective monitoring, event correlation, and multiple reporting channels
2. Restore normal service operation quickly and efficiently through a combination of incident models for known types, effective use of the known error database, structured diagnostic approaches, and collaborative resolution techniques
3. Minimize the business impact of incidents through prioritization based on impact and urgency, with resource allocation aligned to business need
4. Ensure that major incidents receive immediate coordinated attention with a dedicated coordinator, accelerated communication, and a mandatory post-incident review
5. Maintain accurate and complete incident records that support resolution, reporting, trend analysis, and compliance
6. Continually improve incident management approaches through periodic review of incident data, analysis of trends and patterns, and improvement of incident models, classification schemes, and handling procedures

## Scope

This policy applies to all incidents affecting services within the scope of the organization's service management system. It covers:

- All unplanned interruptions to services or reductions in the quality of services, whether reported by users, detected by technical staff, or identified through monitoring and event management
- The full incident lifecycle — from detection and registration through classification, prioritization, diagnosis, resolution, and closure
- Major incidents and the dedicated procedure for their coordinated handling and post-incident review
- All roles with responsibility for incident management, from the incident manager through service desk agents, technical specialists, and major incident coordinators
- Incident models, classification schemes, priority matrices, escalation paths, and other supporting artefacts that govern how incidents are handled
- The periodic review of incident data to drive improvement of incident management approaches

This policy does not cover service requests (which are managed under Service Request Management, PR12) or the investigation of root causes and maintenance of the known error database (which are managed under Problem Management, PR13).

## Principles

### P1. Early Detection
<!-- sources: ITIL 4 Incident Management §2.4.1 -->
The organization shall aim to detect incidents as early as possible, ideally before users experience service degradation. This requires effective integration with monitoring and event management, the use of event correlation to identify patterns indicating service failure, and the provision of multiple accessible channels through which users can report incidents. Proactive detection reduces both the duration and the impact of incidents.

### P2. Rapid Service Restoration
<!-- sources: ITIL 4 Incident Management §2.4.2, FitSM-2 §PR9 ISRM Objective -->
The primary objective of incident handling is to restore normal service operation as quickly as possible. This shall be achieved through the use of pre-defined incident models for known incident types, effective use of the known error database and workarounds, structured diagnostic approaches, and the ability to mobilize the right expertise rapidly. Where a permanent resolution is not immediately available, a workaround that reduces impact shall be applied while the underlying cause is investigated.

### P3. Impact-Based Prioritization
<!-- sources: ITIL 4 Incident Management §2.4.2 -->
Incidents shall be prioritized based on a defined combination of impact (the effect on the business) and urgency (the speed at which resolution is required). The priority matrix shall drive response targets, resolution targets, resource allocation, and escalation timing. Where resource conflicts arise between incidents of similar priority, the organization shall use transparent queue management techniques to allocate resources fairly and effectively.

### P4. Consistent Handling
<!-- sources: ITIL 4 Incident Management §2.4.2, FitSM-2 §PR9 ISRM (define standardised procedures) -->
Incidents shall be handled using defined, repeatable procedures. The organization shall establish a standard classification scheme, a standard prioritization procedure, and standard procedures for registration, escalation, and closure. For known and recurring incident types, pre-defined incident models shall describe the specific steps, roles, timescales, and escalation criteria required for efficient resolution.

### P5. Effective Escalation
<!-- sources: ITIL 4 Incident Management §2.4.2, FitSM-2 §PR9 ISRM (define escalation procedure) -->
The organization shall define and operate both functional escalation paths (to specialist resolver groups with the required technical expertise) and hierarchical escalation paths (to management for resource allocation decisions, priority conflicts, or SLA breach risk). Escalation criteria and timescales shall be documented and consistently applied. Escalation shall be treated as a normal part of incident resolution, not as a failure.

### P6. User Communication
<!-- sources: ITIL 4 Incident Management §5.1, FitSM-2 §PR9 ISRM (closing procedure — user communication and confirmation) -->
Users who report or are affected by incidents shall be kept informed of the status and progress of incident resolution. Incident closure shall require user confirmation that the service has been restored satisfactorily. Where possible, users shall have access to real-time incident status information through a service portal. Communication shall be timely, clear, and proportionate to the incident's impact.

### P7. Continual Improvement
<!-- sources: ITIL 4 Incident Management §2.4.3 -->
The organization shall periodically review incident data to identify trends, recurring issues, systemic weaknesses, and opportunities for improvement. Reviews shall lead to specific, actionable improvements — to incident models, classification schemes, escalation paths, handling procedures, team structures, or automation. Improvement initiatives shall be registered and tracked through the continual improvement process. The organization shall foster a culture of collective responsibility, no-blame investigation, and continual learning across all teams involved in incident resolution.

## Mandatory Requirements

### Essential (All tiers)

| ID | Requirement |
|----|------------|
| IM-R01 | All incidents shall be registered in the ITSM tool with a complete set of required fields, including affected user(s), affected service or CI, impact, urgency, priority, and time of first symptom |
| IM-R02 | Incidents shall be classified using a defined classification scheme that supports routing, reporting, and trend analysis |
| IM-R03 | Incidents shall be prioritized based on impact and urgency using a defined priority matrix, with associated response and resolution targets |
| IM-R04 | Criteria for identifying major incidents shall be defined, documented, and consistently applied during incident classification |
| IM-R05 | A major incident handling procedure shall be established, including coordinator assignment, elevated priority handling, stakeholder communication, and a mandatory post-major-incident review |
| IM-R06 | Incidents shall be resolved and closed with user confirmation that service has been restored satisfactorily. Resolution details and timestamps shall be recorded |
| IM-R07 | An incident manager role shall be assigned with accountability for coordinating incident handling, monitoring resolution team performance, and ensuring awareness of incidents and their status |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| IM-R08 | Incident models shall be developed and maintained for known and recurring incident types, specifying classification, diagnostic steps, resolution actions, escalation criteria, and target timescales |
| IM-R09 | Functional and hierarchical escalation paths shall be documented with clear criteria and timescales for each escalation level |
| IM-R10 | Regular incident reports shall be produced, covering volumes, classification breakdowns, resolution times, SLA achievement, backlog trends, and major incident summaries |
| IM-R11 | A major incident manager role shall be assigned with dedicated responsibility for coordinating the response to major incidents, including wider authority to mobilize resources and invoke emergency procedures |
| IM-R12 | Post-major-incident reviews shall be conducted for all major incidents, producing a formal report with timeline, actions taken, root cause (if identified), lessons learned, and follow-up actions |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| IM-R13 | Periodic incident reviews shall be conducted at defined intervals, analysing incident data for trends, recurring issues, systemic weaknesses, and improvement opportunities |
| IM-R14 | Incident models, classification schemes, escalation paths, and handling procedures shall be subject to regular review and improvement based on incident review findings and operational experience |
| IM-R15 | Collaborative resolution approaches — including swarming and cross-team collaboration — shall be adopted for complex incidents, supported by flat team structures, collective responsibility, and a no-blame culture |

## Compliance and Review

- This policy shall be reviewed at least annually or following a significant change to the organization's service portfolio, support model, or incident management tooling
- Compliance with this policy shall be assessed through incident reports, SLA achievement data, major incident review reports, and periodic incident reviews
- Non-compliance shall be escalated to the incident manager and service management leadership for remediation
- Exceptions to this policy require documented justification and approval from the incident manager or senior leadership

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Service Desk Policy (PR10) | The service desk is the primary user-facing channel for incident registration and status communication; service desk agents perform first-contact incident handling |
| Problem Management Policy (PR13) | Problem Management maintains the KEDB that supports incident resolution; incident trend data feeds problem identification and root cause investigation |
| Change Management Policy (PR15) | Changes may be required to resolve incidents; emergency changes follow an expedited authorization path; recent changes may be the cause of incidents |
| Service Level Management Policy (PR02) | SLAs define service targets that drive incident prioritization, escalation timescales, and resolution targets; incident data feeds SLA achievement reporting |
| Monitoring & Event Management Policy (PR14) | Monitoring and event management provides the events and alerts that trigger proactive incident detection and automated incident registration |
| Service Configuration Management Policy (PR17) | The CMS provides configuration item data and relationships that support incident classification, impact analysis, and resolution routing |
| Knowledge Management Policy (PR19) | Knowledge articles and resolution guides support incident diagnosis; new resolution knowledge discovered during incident handling is contributed to the knowledge base |
| Continual Improvement Policy (PR24) | Improvement initiatives from periodic incident reviews feed the continual improvement register |
