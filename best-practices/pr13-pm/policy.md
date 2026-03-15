---
process_id: PR13
process_name: "Problem Management"
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
  - "ITIL 4: Problem Management §2.1, §2.2, §2.3, §2.4"
  - "FitSM-2: §PR10 PM"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (problem coordination)"
last_updated: 2026-03-13
status: draft
---

# Problem Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Problem Management §2.1, §2.2, FitSM-2 §PR10 PM Objective -->

The organization shall reduce the likelihood and impact of incidents by identifying actual and potential causes of incidents and managing workarounds and known errors. Problems — causes or potential causes of one or more incidents — shall be identified both reactively (from incident data and trend analysis) and proactively (from monitoring data, supplier information, and vulnerability assessments). Identified problems shall be investigated using structured analysis techniques, and findings shall be documented as known errors in the known error database (KEDB) with associated workarounds. The organization shall adopt a balanced approach to problem mitigation — pursuing permanent resolution where cost-effective, applying permanent workarounds where full fixes are not feasible, and optimizing incident management for low-impact problems. Problems shall be prioritized based on risk, managed through a single prioritized backlog, and resolved through controlled changes. The organization shall periodically review known errors and problem management effectiveness to drive continual improvement.

## Objectives
<!-- sources: ITIL 4 Problem Management §2.4 PSFs, FitSM-2 §PR10 PM Key Questions -->

1. Identify and understand problems and their impact on services — both reactively from incident patterns and proactively from monitoring, supplier information, and vulnerability assessments — to prevent incidents from occurring or recurring
2. Investigate problems using structured root cause analysis techniques to determine the underlying causes of incidents, considering all four dimensions of service management (organizations and people, information and technology, partners and suppliers, value streams and processes)
3. Maintain an accurate and current known error database that provides incident management with documented root causes and workarounds, enabling faster incident diagnosis and resolution
4. Optimize problem resolution and mitigation by applying a balanced approach that considers the costs, risks, and service quality impacts of each mitigation option — permanent fix, permanent workaround, or optimized incident management
5. Initiate problem resolution through controlled changes, ensuring that fixes are implemented safely and do not introduce new problems
6. Continually improve problem management approaches — including investigation techniques, problem models, KEDB quality, and collaboration with incident management and other processes

## Scope

This policy applies to all problem management activities within the scope of the organization's service management system. It covers:

- The identification of problems from incident data and trend analysis (reactive) and from monitoring, supplier, and other proactive sources (proactive)
- The investigation and analysis of problems to determine root causes, including the use of structured analysis techniques
- The documentation and management of known errors and workarounds in the KEDB
- The initiation of problem resolution through changes to fix or reduce the impact of problems
- The monitoring and periodic review of known errors to ensure workarounds remain effective and mitigation approaches remain appropriate
- All roles with responsibility for problem management, from the problem manager through problem coordinators, technical specialists, and service owners

This policy does not cover the resolution of individual incidents (which is managed under Incident Management, PR11) or the control and implementation of changes initiated to resolve problems (which is managed under Change Management, PR15).

## Principles

### P1. Dual-Mode Identification
<!-- sources: ITIL 4 Problem Management §2.2, §2.4.1, §3.2.1, §3.2.2 -->
The organization shall identify problems through both reactive and proactive means. Reactive identification uses incident data — recurring incidents, incidents without known root causes, major incident review findings, and incident trend analysis — to detect problems that have already caused service disruption. Proactive identification uses monitoring data, vendor and supplier information, user community intelligence, technical audits, and planned change assessments to detect problems before they cause incidents. Proactive identification is a form of risk management and should focus on the systems and components with the highest potential impact on the organization and its customers.

### P2. Structured Investigation
<!-- sources: ITIL 4 Problem Management §2.2.2, §3.2.3 Table 3.7 -->
Problems shall be investigated using structured analysis techniques appropriate to the problem type — including root cause analysis methods (such as five whys and fault tree analysis), impact analysis techniques (such as component failure impact analysis), and risk analysis techniques. Investigation shall not be limited to the identification of a single root cause; in complex environments, incidents are often caused by combinations of contributing factors across multiple dimensions. Problem investigation should consider all relevant factors — including configuration items, human behaviour, procedures, and third-party components.

### P3. Risk-Based Prioritization
<!-- sources: ITIL 4 Problem Management §2.2 (problem prioritization) -->
Problems shall be prioritized based on risk — considering the probability and impact of related incidents, the frequency and severity of incidents already caused, the availability and effectiveness of workarounds, and the cost and effort of investigation and resolution. Prioritization is a resource-allocation decision: problems compete for a shared pool of investigation and resolution resources. The organization shall maintain a single prioritized problem backlog and use visualization techniques (such as Kanban boards) to manage problem queues and make prioritization decisions transparent across teams.

### P4. Known Error Management
<!-- sources: ITIL 4 Problem Management §2.2.2, §2.2.3, §3.2.3, FitSM-2 §PR10 PM (Maintain KEDB) -->
When a problem has been analysed and the root cause identified, it shall be documented as a known error in the KEDB with its root cause, impact description, and any available workarounds. Known errors shall be communicated to incident management and the service desk to enable faster incident resolution. Known error records shall have a defined lifecycle — created when analysis is complete, updated as new workarounds or information become available, and deactivated or closed when the underlying problem is permanently resolved or the affected service is retired.

### P5. Balanced Mitigation
<!-- sources: ITIL 4 Problem Management §2.2.3, §2.4.2, Table 2.1 -->
Not all known errors require a full permanent fix. The organization shall assess each known error against three mitigation approaches: (1) full permanent resolution — eliminating the root cause through a controlled change; (2) permanent workaround — a durable mitigation that reduces impact to an acceptable level; (3) optimized incident management — improving the organization's ability to handle incidents caused by the known error when neither a fix nor a permanent workaround is viable. The selected approach shall balance the costs, risks, and service quality impacts. Where the cost of resolution exceeds the cost of living with the known error and managing incidents effectively, the organization may choose to maintain the known error with periodic review.

### P6. Collaboration Across Practices
<!-- sources: ITIL 4 Problem Management §2.3 Table 2.2, §6, FitSM-2 §PR10 PM Key Interfaces -->
Problem management shall operate in close collaboration with incident management, change management, and other related practices. Incident management provides the trend data and incident records that drive reactive problem identification and consumes the known errors and workarounds that problem management produces. Change management controls the implementation of problem resolutions. Suppliers and third parties shall be engaged in problem investigation and resolution where problems relate to third-party components or services. Problem models should define how third parties are involved in problem control and error control for each problem type.

### P7. Continual Improvement
<!-- sources: ITIL 4 Problem Management §2.4.2, §3.2.4, FitSM-2 §PR10 PM (Maintain KEDB) -->
The organization shall periodically review known errors, workarounds, and problem management effectiveness to drive continual improvement. Known error reviews shall assess whether workarounds remain effective, whether new resolution options have become available, whether the impact profile of the known error has changed, and whether the mitigation approach should be revised. Problem management reviews shall assess investigation techniques, problem model usage, KEDB quality, and the contribution of problem management to incident reduction and service stability. Improvement initiatives shall be registered and tracked through the continual improvement process.

## Mandatory Requirements

### Essential (All tiers)

| ID | Requirement |
|----|------------|
| PM-R01 | Problems shall be identified from incident data — including recurring incidents, incidents without known root causes, major incident review findings, and incident trend analysis — and registered in the ITSM tool |
| PM-R02 | Problems shall be categorized using a defined categorization scheme and prioritized based on risk — considering incident impact, probability, workaround availability, and investigation effort |
| PM-R03 | Problems shall be investigated using structured analysis techniques to determine root causes, considering configuration items, processes, human factors, and third-party components |
| PM-R04 | Known errors shall be documented in the KEDB with root cause descriptions and available workarounds, and communicated to incident management to support faster incident resolution |
| PM-R05 | Problem resolution shall be initiated through change management where changes to services or infrastructure are required. The selected mitigation approach shall be documented and justified |
| PM-R06 | Problems shall be closed only when the risk of related incidents has been removed or reduced to an acceptable level, or when the problem no longer affects the organization |
| PM-R07 | A problem manager role shall be assigned with accountability for coordinating problem identification, investigation, and resolution across the organization |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| PM-R08 | Proactive problem identification shall be conducted using monitoring and event data, supplier information, vendor advisories, and analysis of planned changes to detect problems before they cause incidents |
| PM-R09 | Problem models shall be developed and maintained for recurring problem types, specifying the analysis techniques, investigation steps, roles, escalation paths, and expected timescales for each problem category |
| PM-R10 | Regular problem reports shall be produced covering problem volumes, KEDB status, problem resolution rates, workaround effectiveness, and the contribution of problem management to incident reduction |
| PM-R11 | A problem coordinator role shall be assigned to support routine problem management activities — including problem registration, tracking, KEDB maintenance, and report compilation |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| PM-R12 | Known errors shall be periodically reviewed to assess whether workarounds remain effective, whether new resolution options are available, and whether the mitigation approach should be revised |
| PM-R13 | Technical debt accumulated from deferred problem resolutions and permanent workarounds shall be tracked and periodically reassessed for its impact on service stability and risk |
| PM-R14 | Problem management effectiveness shall be reviewed at defined intervals, covering investigation techniques, problem model usage, KEDB quality, and the contribution of problem management to service improvement. Improvement initiatives shall be registered through the continual improvement process |

## Compliance and Review

- This policy shall be reviewed at least annually or following a significant change to the organization's service portfolio, support model, or problem management tooling
- Compliance with this policy shall be assessed through problem reports, KEDB quality audits, problem resolution data, and periodic problem management reviews
- Non-compliance shall be escalated to the problem manager and service management leadership for remediation
- Exceptions to this policy require documented justification and approval from the problem manager or senior leadership

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Incident Management Policy (PR11) | Incident management provides the incident records, trend data, and major incident review findings that drive reactive problem identification. Problem management provides known errors and workarounds to incident management through the KEDB |
| Change Management Policy (PR15) | Changes are required to implement problem resolutions — both permanent fixes and permanent workarounds. Emergency changes may be needed for high-impact problems |
| Service Configuration Management Policy (PR17) | The CMS provides configuration item data, relationships, and configuration baselines that support problem investigation — identifying affected components, dependencies, and recent configuration changes |
| Service Level Management Policy (PR02) | Service level data informs problem prioritization — problems affecting services with poor SLA achievement may warrant higher priority. Problem resolution data contributes to SLA achievement reporting |
| Monitoring & Event Management Policy (PR14) | Monitoring and event data supports proactive problem identification — detecting anomalies and degradation patterns that may indicate underlying problems before they cause incidents |
| Knowledge Management Policy (PR19) | Root cause analysis findings and investigation knowledge are contributed to the knowledge base. Knowledge articles support problem investigation |
| Supplier Management Policy (PR23) | Suppliers provide information on known product defects and patches. Problem models should define how suppliers are involved in problem investigation and resolution for supplier-provided components |
| Continual Improvement Policy (PR24) | Improvement initiatives from problem management reviews feed the continual improvement register. Problem management is a key contributor to the organization's improvement capability |
