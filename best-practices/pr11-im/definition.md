---
process_id: PR11
process_name: "Incident Management"
category: definition
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
  - "ITIL 4: Incident Management §2–§6"
  - "FitSM-2: §PR9 ISRM (incident scope)"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (incident coordination)"
last_updated: 2026-03-13
status: draft
---

# Incident Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Incident Management §2.1, FitSM-2 §PR9 ISRM Objective -->

To minimize the negative impact of incidents on the business by restoring normal service operation as quickly as possible. The process ensures that incidents — unplanned interruptions to a service or reductions in the quality of a service — are detected, registered, classified, prioritized, investigated, resolved, and closed using a consistent, repeatable approach. It encompasses both the operational handling of individual incidents and the periodic review of incident data to drive improvement.

## Key Concepts

### Incident
<!-- sources: ITIL 4 Incident Management §2.2, FitSM-1 -->

An unplanned interruption to a service or a reduction in the quality of a service. An incident represents a deviation from agreed or expected service performance as defined in service level agreements. Incidents may be reported by users, detected by technical staff, or identified automatically through monitoring and event management systems.

### Incident Model
<!-- sources: ITIL 4 Incident Management §2.2, §2.4.2, FitSM-2 §PR9 ISRM (identify well-known and recurring incidents) -->

A repeatable, pre-defined approach to managing a particular type of incident. Incident models describe the steps, roles, timescales, and escalation paths required for efficient handling of known or recurring incident types. They enable consistent, rapid resolution by encoding proven resolution paths so that agents do not need to investigate each occurrence from scratch. Incident models should be regularly reviewed and updated based on experience and periodic incident analysis.

### Major Incident
<!-- sources: ITIL 4 Incident Management §2.2, §2.4.2, FitSM-2 §PR9 ISRM (manage major incidents) -->

An incident with significant business impact requiring an immediate coordinated resolution effort. Major incidents are distinguished from standard incidents by defined criteria (typically based on the severity of business impact, the number of affected users or services, or the potential for reputational or financial harm). They trigger a dedicated handling procedure with a designated coordinator, elevated priority, accelerated communication to stakeholders, and a mandatory post-incident review.

### Priority (Impact and Urgency)
<!-- sources: ITIL 4 Incident Management §2.4.2, FitSM-2 §PR9 ISRM (define prioritisation scheme) -->

The mechanism for determining the order in which incidents are addressed, based on a combination of impact (the effect on the business, measured by factors such as the number of affected users, the criticality of the affected service, and the financial or operational consequences) and urgency (the speed at which the business requires resolution, often linked to SLA targets). The priority matrix translates impact and urgency into a priority level that drives response and resolution targets, resource allocation, and escalation timing. Where resource conflicts arise, organizations should use techniques such as Kanban or Lean to visualize and manage incident queues.

### Swarming
<!-- sources: ITIL 4 Incident Management §2.2, §2.4.2, §4.2.1 -->

A collaborative approach to incident resolution in which multiple specialists from different domains work together on a complex incident from the outset, rather than following a rigid tiered escalation path (L1 to L2 to L3). Swarming replaces sequential handoffs with parallel collaboration, enabling faster resolution of complex incidents by bringing the right expertise to bear immediately. The approach requires collective responsibility, a no-blame culture, and continual learning.

### Workaround
<!-- sources: ITIL 4 Incident Management §2.2 -->

A solution that reduces or eliminates the impact of an incident or problem for which a full resolution is not yet available. Workarounds provide immediate relief to affected users while the underlying cause is being investigated or a permanent fix is being developed. They are documented and made available through the known error database to support future incident resolution.

### Known Error and KEDB
<!-- sources: ITIL 4 Incident Management §2.4.2, FitSM-2 §PR9 ISRM (known error database), §PR10 PM -->

A known error is a problem that has been analysed and has a documented root cause and, where available, a workaround. The known error database (KEDB) is maintained by Problem Management and provides incident management with pre-identified resolution paths and workarounds that accelerate diagnosis and resolution. Effective use of the KEDB is a key factor in reducing resolution times for recurring incident types.

---

## Activities

### Essential (All tiers)
<!-- sources: ITIL 4 Incident Management §3.2.1 Table 3.2, FitSM-2 §PR9 ISRM (manage incidents, manage major incidents) -->

| # | Activity | Description |
|---|----------|-------------|
| 1 | Detect incidents | Identify incidents through monitoring and event management alerts, user reports via the service desk (phone, email, portal, chat), technical observation, or automated event correlation. The goal is to detect incidents as early as possible — ideally before users are affected |
| 2 | Register incidents | Log each incident in the ITSM tool with a complete set of required fields — incident title, affected user(s), affected service or CI, current and potential impact, time of first symptom, and source of detection. Automated registration from monitoring events should be used where possible |
| 3 | Classify and prioritize incidents | Categorize the incident using the defined classification scheme. Assess impact and urgency to determine priority using the priority matrix. Check against major incident criteria. Match the incident to existing incident models or known errors where applicable |
| 4 | Diagnose incidents | Investigate the incident to determine its cause and identify the appropriate resolution. Use the KEDB, knowledge articles, configuration data from the CMS, and diagnostic tools. For complex incidents, engage additional technical specialists or suppliers as needed |
| 5 | Resolve incidents | Apply the identified fix, workaround, or automated remediation to restore normal service operation. Confirm that the service has been restored and the user can resume normal work. Document the resolution actions taken |
| 6 | Close incidents | Verify with the user that the incident has been resolved satisfactorily. Complete the incident record with resolution details, time stamps, and categorization. Capture user satisfaction data where appropriate. Identify whether a problem record or change request should be raised |
| 7 | Manage major incidents | When an incident meets major incident criteria: assign a major incident coordinator, handle with highest priority, inform stakeholders and escalate as required, coordinate resolution across multiple teams, perform a post-major-incident review, and close the major incident with a formal review report |

### Intermediate (T2+)
<!-- sources: ITIL 4 Incident Management §2.4.2, §3.2.1, FitSM-2 §PR9 ISRM (initial setup activities, manage workflows) -->

| # | Activity | Description |
|---|----------|-------------|
| 8 | Develop and maintain incident models | Create and maintain pre-defined handling procedures for known and recurring incident types. Each model specifies the classification, diagnostic steps, resolution actions, escalation criteria, and target timescales. Review models periodically and update based on incident review findings and knowledge base contributions |
| 9 | Manage incident escalation | Define and operate functional escalation paths (to specialist teams with the required expertise) and hierarchical escalation paths (to management for resource allocation, priority conflicts, or SLA breach risk). Ensure escalation criteria and timescales are documented and consistently applied |
| 10 | Produce incident reports and analysis | Generate regular incident reports showing volumes, classification breakdowns, resolution times, SLA achievement, backlog trends, and major incident summaries. Provide trend data to Problem Management for pattern and root cause analysis |

### Advanced (T3)
<!-- sources: ITIL 4 Incident Management §2.4.3, §3.2.2, §4.2.1 -->

| # | Activity | Description |
|---|----------|-------------|
| 11 | Conduct periodic incident reviews | Perform scheduled reviews of incident records and data to identify trends, recurring issues, systemic weaknesses, and opportunities for improvement. Analyse resolution effectiveness, model usage, and the quality of incident data. Include input from service owners, technical specialists, and suppliers |
| 12 | Initiate incident model improvements | Based on review findings, initiate specific improvements to incident models, handling procedures, classification schemes, escalation paths, or automation. Register improvement initiatives and track them through the continual improvement process. Communicate updated models to all affected teams |
| 13 | Implement collaborative resolution approaches | Adopt swarming and other collaborative techniques that replace rigid tiered escalation with dynamic, cross-team collaboration for complex incidents. Develop flat team structures, promote collective responsibility, establish a no-blame culture, and encourage continual learning across support teams |

---

## Inputs
<!-- sources: ITIL 4 Incident Management §3.2.1 Table 3.1, §3.2.2 Table 3.3, FitSM-2 §PR9 ISRM Process Inputs -->

| # | Input | Source |
|---|-------|--------|
| 1 | Incidents reported by users | Users (via service desk channels) |
| 2 | Events and alerts from monitoring | Monitoring & Event Management (PR14) |
| 3 | Known errors and workarounds (KEDB) | Problem Management (PR13) |
| 4 | Configuration item data and relationships | Service Configuration Management (PR17) |
| 5 | Service level targets and escalation timescales | Service Level Management (PR02) |
| 6 | Existing incident models and workflows | Incident Management (internal) |
| 7 | Release and deployment information | Release & Deployment Management (PR16) |
| 8 | Knowledge articles and resolution guidance | Knowledge Management (PR19) |
| 9 | Criteria for identifying major incidents | Incident Management policy |

<!-- intermediate -->
| 10 | Incident trend data and reports from previous periods | Measurement & Reporting (PR20) |
| 11 | Improvement initiatives from previous reviews | Continual Improvement (PR24) |

---

## Outputs
<!-- sources: ITIL 4 Incident Management §3.2.1 Table 3.1, §3.2.2 Table 3.3, FitSM-2 §PR9 ISRM Process Outputs -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Incident records (new and updated) | ITSM tool / incident register |
| 2 | Major incident review reports | Management, service owners, Problem Management |
| 3 | Requests for change | Change Management (PR15) |
| 4 | Problem records (for recurring or unresolved incidents) | Problem Management (PR13) |
| 5 | Workaround records | KEDB (via Problem Management) |
| 6 | User satisfaction data | Service Level Management (PR02), Measurement & Reporting (PR20) |
| 7 | Regular incident reports | Management, service owners, Measurement & Reporting (PR20) |

<!-- intermediate -->
| 8 | Updated incident models and workflows | Incident Management (internal), Service Desk (PR10) |
| 9 | Incident trend data for pattern analysis | Problem Management (PR13) |

<!-- advanced -->
| 10 | Improvement initiatives from periodic reviews | Continual Improvement (PR24) |
| 11 | Updated classification schemes and escalation paths | Incident Management (internal), Service Desk (PR10) |

---

## Roles
<!-- sources: ITIL 4 Incident Management §4.1.1, §4.1.2 Table 4.2, FitSM-2 §PR9 ISRM -->

| Role | Responsibilities | Tier |
|------|-----------------|------|
| **Incident Manager** | Coordinates incident handling across the organization or within a defined scope (territory, product, service). Coordinates manual work with incidents, especially those involving multiple teams. Monitors and reviews the work of teams that handle and resolve incidents. Ensures awareness of incidents and their status across the organization. Conducts regular and as-needed incident reviews. Develops the organization's expertise in incident management processes and methods. At T2+, may also serve as major incident manager or delegate that role | All |
| **Service Desk Agent** | First point of contact for user-reported incidents. Registers incidents, performs initial classification and prioritization, attempts first-contact resolution using incident models and the KEDB, escalates incidents that cannot be resolved at first contact, and manages incident closure including user confirmation | All |
| **Technical Specialist** | Provides technical expertise for incident diagnosis and resolution within a specific domain (application, infrastructure, network, security, etc.). Participates in swarming for complex incidents. Contributes to incident model development and knowledge base content. May be internal staff or third-party supplier personnel | All |
| **Major Incident Manager** | Coordinates the response to major incidents. Serves as the single point of contact and coordination during major incidents. Has wider authority than the incident manager for major incident situations, including the ability to mobilize dedicated resources and invoke emergency change procedures. Conducts the post-major-incident review | T2+ |

---

## Artefacts
<!-- sources: ITIL 4 Incident Management §5.1 Table 5.1, §3.2.1, FitSM-2 §PR9 ISRM -->

| Artefact | Description | Tier |
|----------|-------------|------|
| **Incident Record** | The formal record of an incident through its lifecycle, containing: incident title/description, affected user(s), current and future impact, time of first symptom, time of last known good function, affected CI details, comparable unaffected items, investigation details, actions taken, resolution details, assigned owner, and timestamps for all state transitions | All |
| **Priority Matrix** | A matrix mapping combinations of impact and urgency to priority levels, with associated response and resolution targets. Shared with SLA definitions and used across incident and other operational processes | All |
| **Incident Classification Scheme** | A defined taxonomy for categorizing incidents by type, affected service, affected technology, or other dimensions relevant to routing, reporting, and trend analysis | All |
| **Escalation Paths** | Documented functional escalation paths (to specialist resolver groups) and hierarchical escalation paths (to management), with criteria and timescales for each escalation level | All |
| **Incident Model** | A documented, repeatable approach for handling a specific type of known or recurring incident, including classification, diagnostic steps, resolution actions, escalation criteria, and target timescales | T2+ |
| **Major Incident Review Report** | A formal report produced after resolution of a major incident, documenting the timeline, actions taken, root cause (if identified), lessons learned, and follow-up actions | T2+ |
| **Incident Report** | A periodic report summarizing incident volumes, classification breakdowns, resolution times, SLA achievement, backlog trends, and major incident summaries | T2+ |
| **Known Error Database (KEDB)** | A database of known errors with documented root causes and workarounds, maintained by Problem Management and consumed by Incident Management to accelerate diagnosis and resolution. Shared artefact with Problem Management (PR13) | T2+ |

---

## Process Interfaces
<!-- sources: ITIL 4 Incident Management §2.3 Table 2.1, §6, FitSM-2 §PR9 ISRM Key Interfaces -->

### Interfaces From Other Processes

| Source Process | Interface Description |
|---------------|----------------------|
| **Service Desk (PR10)** | User-reported incidents received through the service desk contact channels. The service desk provides the primary user-facing interface for incident registration and status communication |
| **Monitoring & Event Management (PR14)** | Events and alerts that trigger automatic or manual incident detection. Event correlation identifies patterns that indicate service degradation or failure before users report them |
| **Service Level Management (PR02)** | SLAs containing agreed service targets that drive incident prioritization, escalation timescales, and resolution targets. Service level data informs the priority matrix |
| **Problem Management (PR13)** | Known errors and workarounds from the KEDB that support faster incident diagnosis and resolution. Problem Management also provides root cause information for recurring incident types |
| **Service Configuration Management (PR17)** | Configuration item data and relationship information from the CMS that supports incident classification, impact analysis, diagnosis, and resolution routing |
| **Release & Deployment Management (PR16)** | Information on planned or recently deployed releases that supports incident diagnosis — identifying whether incidents are related to recent changes or deployments |
| **Knowledge Management (PR19)** | Knowledge articles, resolution guides, and diagnostic procedures that support incident diagnosis and resolution |
| **Change Management (PR15)** | Information on recent and planned changes that may be related to incident causes. Emergency change authorization for incident resolution where needed |

### Interfaces To Other Processes

| Target Process | Interface Description |
|---------------|----------------------|
| **Problem Management (PR13)** | Incident trend data, incident records, and reports that enable pattern and trend analysis for problem identification. Incidents that cannot be permanently resolved are input to problem investigation |
| **Change Management (PR15)** | Requests for change raised to resolve incidents (where a change to the infrastructure or service is required) or to implement permanent fixes for recurring incidents |
| **Service Level Management (PR02)** | Incident resolution data that feeds SLA achievement reporting — including response times, resolution times, and SLA breach information |
| **Knowledge Management (PR19)** | New resolution knowledge, updated workarounds, and diagnostic techniques discovered during incident handling, contributed to the knowledge base for future use |
| **Continual Improvement (PR24)** | Improvement initiatives identified during periodic incident reviews, including proposed changes to incident models, handling procedures, classification schemes, or team structures |
| **Measurement & Reporting (PR20)** | Incident data for management reporting — volumes, trends, SLA achievement, customer satisfaction, and major incident summaries |
| **Service Desk (PR10)** | Updated incident models, classification schemes, and escalation paths that the service desk uses for first-contact handling. Incident status updates for user communication |
| **Supplier Management (PR23)** | Escalation of incidents to third-party suppliers for diagnosis or resolution, and supplier performance data from supplier-involved incidents |
