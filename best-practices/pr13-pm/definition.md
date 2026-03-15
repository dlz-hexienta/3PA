---
process_id: PR13
process_name: "Problem Management"
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
  - "ITIL 4: Problem Management §2–§6"
  - "FitSM-2: §PR10 PM"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (problem coordination)"
last_updated: 2026-03-13
status: draft
---

# Problem Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Problem Management §2.1, FitSM-2 §PR10 PM Objective -->

To reduce the likelihood and impact of incidents by identifying actual and potential causes of incidents and managing workarounds and known errors. Problem management investigates the underlying causes of incidents — both reactively (after incidents have occurred) and proactively (before incidents occur) — to prevent recurrence, reduce severity, and improve the overall stability of services. The process maintains the known error database (KEDB) to provide incident management with documented root causes and workarounds that accelerate incident resolution.

## Key Concepts

### Problem
<!-- sources: ITIL 4 Problem Management §2.2, FitSM-1 -->

A cause, or potential cause, of one or more incidents. A problem is distinct from an incident: an incident is an unplanned service interruption or quality reduction that requires immediate restoration of service, whereas a problem is the underlying cause that may give rise to incidents. Problems exist independently of incidents — a problem may be identified before any incident occurs (proactive identification) or after one or more incidents have already been reported (reactive identification). Not all incidents have an associated problem record, and a single problem may be the cause of many incidents.

### Known Error
<!-- sources: ITIL 4 Problem Management §2.2, FitSM-2 §PR10 PM (KEDB) -->

A problem that has been analysed and has not been resolved. A known error has a documented root cause (or sufficient understanding of its nature) and, where available, a documented workaround. Known errors are recorded in the known error database (KEDB) and remain active until the underlying problem is permanently resolved or the affected service is retired. The existence of a known error does not necessarily mean that a permanent resolution is being developed — the organization may choose to manage the risk through workarounds or by optimizing incident handling if the cost of a permanent fix is not justified.

### Workaround
<!-- sources: ITIL 4 Problem Management §2.2 -->

A solution that reduces or eliminates the impact of an incident or problem for which a full resolution is not yet available. Workarounds are documented as part of known error records in the KEDB and are consumed by incident management to accelerate incident diagnosis and restore service more quickly. Some workarounds are temporary (applied while a permanent fix is developed), while others may become permanent if the organization decides against pursuing a full resolution. Workarounds should be tested and documented with clear application instructions before being published.

### Known Error Database (KEDB)
<!-- sources: ITIL 4 Problem Management §2.2, §3.2 Process 3, FitSM-2 §PR10 PM (Maintain KEDB) -->

A database or structured register of known errors, their root causes, and their associated workarounds. The KEDB is maintained by problem management and is a primary input to incident management — it enables service desk agents and technical specialists to match incidents to known errors and apply documented workarounds without re-investigating the root cause. Known error records in the KEDB have a defined lifecycle: they are created when a problem is sufficiently analysed, updated as new information or workarounds become available, and deactivated or closed when the underlying problem is permanently resolved.

### Problem Model
<!-- sources: ITIL 4 Problem Management §2.2, §3.2 Process 3 -->

A repeatable, pre-defined approach to investigating and resolving a particular type of problem. Problem models describe the investigation techniques, analysis steps, roles, escalation paths, and expected timescales appropriate for a given problem category — for example, software defects, hardware failures, procedural gaps, third-party service issues, or capacity-related problems. Problem models provide a consistent starting point for investigation and help ensure that appropriate analysis techniques are applied systematically.

### Three Phases of Problem Management
<!-- sources: ITIL 4 Problem Management §2.2 -->

Problem management operates through three distinct phases:

1. **Problem identification** — Detecting and logging problems. This occurs either reactively (triggered by incident data, recurring incidents, or incident trend analysis) or proactively (triggered by monitoring data, event pattern analysis, supplier information, or analysis of service changes before they cause incidents).

2. **Problem control** — Analysing identified problems to understand their root cause and document them as known errors. Problem control uses structured analysis techniques to investigate problems, determine their root cause, and communicate findings. When a root cause is identified but the problem is not yet resolved, it becomes a known error and is recorded in the KEDB with any available workarounds.

3. **Error control** — Managing known errors through their lifecycle. Error control involves developing solutions, initiating problem resolution through change management, monitoring known errors for changes in impact or new mitigation options, and closing problems once they are permanently resolved. Error control also assesses whether each known error warrants a permanent fix, a permanent workaround, or optimization of incident handling as the most appropriate mitigation approach.

### Reactive and Proactive Problem Identification
<!-- sources: ITIL 4 Problem Management §2.2, §3.2 Processes 1–2, FitSM-2 §PR10 PM (Identify problems) -->

Reactive problem identification investigates the causes of incidents that have already occurred — triggered by individual incidents that cannot be resolved through incident models or known errors, by recurring incidents of the same type, or by analysis of incident records and trend data. Proactive problem identification seeks to identify problems before they cause incidents — triggered by monitoring and event data, analysis of configuration or capacity trends, information from suppliers about known defects, or review of planned changes and their potential failure modes. Both modes produce problem records that enter the same problem control phase.

### Problem Prioritization
<!-- sources: ITIL 4 Problem Management §2.2 -->

Problems are prioritized based on the risk they pose — considering the probability and impact of related incidents, the frequency and severity of incidents already caused, the availability and effectiveness of workarounds, and the cost and effort of resolution. Unlike incident prioritization (which is driven by SLA response targets), problem prioritization is a resource-allocation decision. Problems compete for a shared pool of investigation and resolution resources, and the organization should maintain a single prioritized problem backlog. Visualization techniques such as Kanban boards help manage the problem queue and make prioritization decisions transparent.

### Error Control Mitigation Approaches
<!-- sources: ITIL 4 Problem Management §2.2 Table 2.1 -->

Not all known errors require a full permanent fix. Error control assesses each known error against three mitigation approaches:

1. **Full permanent resolution** — The ideal outcome: the root cause is eliminated through a change to the service, infrastructure, or configuration, and the problem is closed.
2. **Permanent workaround** — A durable workaround that sufficiently reduces the impact, applied when a full fix is too costly, too risky, or not technically feasible. The problem remains open as a known error but its impact is managed.
3. **Optimize incident management** — When neither a fix nor a permanent workaround is viable, the organization improves its ability to handle the resulting incidents — for example, by creating or improving incident models, training service desk agents, or automating incident detection and initial response for incidents caused by the known error.

### Technical Debt
<!-- sources: ITIL 4 Problem Management §2.2 -->

The total rework backlog accumulated by choosing workarounds, quick fixes, or deferred resolution instead of permanent solutions. Technical debt is a natural consequence of error control decisions — when the organization chooses a permanent workaround or optimized incident management over a full fix, it accepts a degree of technical debt. Problem management should track and periodically reassess technical debt to ensure that accumulated debt does not erode service stability or create compounding risks.

---

## Activities

### Essential (All tiers)
<!-- sources: ITIL 4 Problem Management §3.2 Processes 2–4, FitSM-2 §PR10 PM (Identify problems, Handle problems, Maintain KEDB) -->

| # | Activity | Description |
|---|----------|-------------|
| 1 | Identify problems from incident data | Detect problems reactively from incident management inputs — incidents that cannot be resolved through existing incident models or known errors, recurring incidents of the same type, and patterns identified through incident trend analysis. Register problems in the ITSM tool and assign for investigation |
| 2 | Categorize and prioritize problems | Classify the problem using the defined categorization scheme. Assess the risk posed by the problem — considering the probability and impact of related incidents, the frequency and severity of incidents already caused, and the availability of workarounds. Assign priority based on risk and available resources |
| 3 | Investigate and diagnose problems | Analyse the problem to determine its root cause using structured techniques appropriate to the problem type — such as timeline analysis, fault isolation, five whys analysis, or fault tree analysis. Review configuration data, change and release history, and incident records. Engage technical specialists with the relevant domain expertise |
| 4 | Document known errors and workarounds | When the root cause of a problem has been identified but a permanent resolution is not yet available, record it as a known error in the KEDB. Document the root cause analysis findings, the known error's impact, and any available workarounds with clear application instructions. Communicate known errors to incident management |
| 5 | Develop and initiate problem resolution | Determine the appropriate mitigation approach for each known error — full permanent fix, permanent workaround, or optimization of incident management. For resolutions requiring changes to services or infrastructure, submit requests for change through change management. Coordinate with the responsible teams to implement the resolution |
| 6 | Close problems | Close the problem record when the underlying cause has been permanently resolved, the associated known error has been verified as eliminated, and no further incidents are occurring. Update the KEDB to deactivate the known error record. Where the problem is closed without a full fix (permanent workaround or managed through incident handling), document the rationale and ensure the known error record reflects the ongoing mitigation approach |

### Intermediate (T2+)
<!-- sources: ITIL 4 Problem Management §3.2 Process 1, §2.4 PSF1, FitSM-2 §PR10 PM (Identify problems — trend analysis) -->

| # | Activity | Description |
|---|----------|-------------|
| 7 | Identify problems proactively | Detect problems before they cause incidents by analysing monitoring and event data, reviewing configuration and capacity trends, assessing information from suppliers about known defects, and evaluating planned changes for potential failure modes. Register proactively identified problems and prioritize them alongside reactively identified problems in the shared problem backlog |
| 8 | Develop and maintain problem models | Create and maintain pre-defined investigation approaches for recurring problem types — specifying the analysis techniques, investigation steps, roles, escalation paths, and expected timescales appropriate for each problem category (software defects, hardware failures, procedural gaps, third-party issues, capacity-related problems). Review models periodically and update based on investigation outcomes |
| 9 | Produce problem reports and analysis | Generate regular problem management reports covering: problem volumes and status, known error counts and KEDB status, problem resolution times and rates, workaround effectiveness, input to service level reporting, and trend data. Provide problem analysis data to management, service owners, and incident management |

### Advanced (T3)
<!-- sources: ITIL 4 Problem Management §3.2 Process 4, §2.4 PSF2, §2.2 (technical debt) -->

| # | Activity | Description |
|---|----------|-------------|
| 10 | Monitor and review known errors | Periodically review active known errors in the KEDB to assess whether workarounds remain effective, whether new resolution options have become available, whether the impact profile has changed, and whether the known error should be reprioritized for permanent resolution. Update known error records and workaround documentation based on review findings |
| 11 | Assess and manage technical debt | Track the accumulated technical debt from deferred problem resolutions and permanent workarounds. Periodically reassess the risk and cost of outstanding technical debt. Provide input to service portfolio management and continual improvement on the state of technical debt and its impact on service stability |
| 12 | Drive continual improvement of problem management | Review the effectiveness of problem management approaches — investigation techniques, problem models, KEDB quality, collaboration with incident management and other processes. Identify improvement opportunities and register them through the continual improvement process. Measure the impact of problem management on incident reduction and service stability |

---

## Inputs
<!-- sources: ITIL 4 Problem Management §3.2 Tables 3.1, 3.4, 3.6, 3.8, FitSM-2 §PR10 PM Inputs -->

| # | Input | Source |
|---|-------|--------|
| 1 | Incident records, trend data, and recurring incident patterns | Incident Management (PR11) |
| 2 | Configuration item data and relationships | Service Configuration Management (PR17) |
| 3 | Change and release records | Change Management (PR15), Release & Deployment Management (PR16) |
| 4 | Service level targets and achievement data | Service Level Management (PR02) |
| 5 | Knowledge articles and resolution history | Knowledge Management (PR19) |

<!-- intermediate -->
| 6 | Events, monitoring data, and event correlation patterns | Monitoring & Event Management (PR14) |
| 7 | Supplier information on known defects and product issues | Supplier Management (PR23) |
| 8 | Service and product roadmap information | Service Portfolio Management (PR01) |

<!-- advanced -->
| 9 | Improvement initiative status from previous reviews | Continual Improvement (PR24) |

---

## Outputs
<!-- sources: ITIL 4 Problem Management §3.2 Tables 3.1, 3.4, 3.6, 3.8, FitSM-2 §PR10 PM Outputs -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Problem records (new and updated) | ITSM tool / problem register |
| 2 | Known errors and workarounds (KEDB updates) | Incident Management (PR11), Service Desk (PR10) |
| 3 | Requests for change (for problem resolution) | Change Management (PR15) |
| 4 | Root cause analysis findings | Knowledge Management (PR19), Incident Management (PR11) |

<!-- intermediate -->
| 5 | Problem reports and trend analysis | Management, service owners, Measurement & Reporting (PR20) |
| 6 | Updated problem models | Problem Management (internal) |
| 7 | Problem data for SLA reporting | Service Level Management (PR02) |

<!-- advanced -->
| 8 | Improvement initiatives | Continual Improvement (PR24) |
| 9 | Technical debt assessments | Service Portfolio Management (PR01) |

---

## Roles
<!-- sources: ITIL 4 Problem Management §4.1.1, §4.1.2 Table 4.2, FitSM-2 §PR10 PM -->

| Role | Responsibilities | Tier |
|------|-----------------|------|
| **Problem Manager** | Accountable for the problem management process. Coordinates problem identification, investigation, and resolution across the organization. Manages the problem backlog and prioritization decisions. Ensures the KEDB is maintained and provides value to incident management. Monitors the effectiveness of problem management — including the ratio of proactive to reactive identification, investigation completion rates, and the impact of problem resolution on incident volumes. Develops the organization's expertise in root cause analysis and problem management techniques. Reports on problem management performance to management and service owners | All |
| **Technical Specialist** | Provides domain-specific expertise for problem investigation and root cause analysis. Applies structured analysis techniques to diagnose problems within their area of technical knowledge. Participates in investigation teams — which may be temporary, formed for the duration of a specific problem investigation, and disbanded after resolution. Contributes findings to the KEDB and knowledge base | All |
| **Problem Coordinator** | Performs routine problem management activities under the direction of the problem manager — including problem registration, categorization, tracking, KEDB maintenance, and report compilation. Coordinates communication between investigation teams and stakeholders. In organizations with a small problem management scope, the problem coordinator role may be combined with the problem manager role | T2+ |
| **Service Owner** | Provides the service-level perspective on problems affecting their services — including business impact assessment, resolution priority input, and acceptance of risk when problems are managed through workarounds rather than permanent fixes. Participates in problem reviews and prioritization decisions for problems affecting their services | All |

---

## Artefacts
<!-- sources: ITIL 4 Problem Management §5.1 Table 5.1, §3.2, FitSM-2 §PR10 PM -->

| Artefact | Description | Tier |
|----------|-------------|------|
| **Problem Record** | The formal record of a problem through its lifecycle, containing: problem description, categorization, affected service(s) and CI(s), related incident records, investigation findings, root cause analysis, known error reference (if applicable), resolution actions, current status, and priority. The problem record tracks the problem from identification through investigation, known error documentation, resolution, and closure | All |
| **Known Error Database (KEDB)** | A structured database or register of known errors with their root causes, impact descriptions, and documented workarounds. The KEDB is the primary interface between problem management and incident management — it enables incident handlers to match incidents to known causes and apply pre-documented workarounds. Each record has a defined lifecycle: created, updated, and deactivated/closed | All |
| **Root Cause Analysis Record** | Documentation of the investigation process and findings for a specific problem — including the analysis technique(s) used, the evidence gathered, the root cause determination, and any contributing factors identified. Attached to the problem record and contributed to the knowledge base | All |
| **Workaround Record** | A documented workaround associated with a known error, containing: the conditions under which the workaround applies, step-by-step application instructions, any limitations or side effects, and the expected outcome. Published through the KEDB for consumption by incident management | All |
| **Problem Model** | A documented, repeatable approach for investigating a specific category of problem — specifying the analysis techniques, investigation steps, roles, escalation paths, and expected timescales. Problem models provide consistency across investigations and ensure appropriate techniques are applied | T2+ |
| **Problem Report** | A periodic report summarizing problem management activity — including problem volumes by category and status, KEDB status (active known errors, new entries, closed entries), problem resolution rates, workaround usage, and the impact of problem resolution on incident volumes | T2+ |

---

## Process Interfaces
<!-- sources: ITIL 4 Problem Management §2.3 Table 2.2, §6, FitSM-2 §PR10 PM Key Interfaces -->

### Interfaces From Other Processes

| Source Process | Interface Description |
|---------------|----------------------|
| **Incident Management (PR11)** | Incident records, trend data, and recurring incident patterns that trigger reactive problem identification. Incidents that cannot be resolved through existing incident models or known errors indicate potential new problems. Major incident review reports provide input to problem investigation |
| **Service Configuration Management (PR17)** | Configuration item data, relationships, and configuration baselines from the CMS that support problem investigation — identifying affected components, dependency chains, and recent configuration changes that may have introduced the problem |
| **Change Management (PR15)** | Change records and post-implementation review data that support problem investigation — identifying whether recent changes have introduced problems or whether change-related issues are contributing to incidents |
| **Release & Deployment Management (PR16)** | Release and deployment records that provide context for problem investigation — identifying whether problems correlate with recent releases or deployment activities |
| **Service Level Management (PR02)** | Service level targets and achievement data that inform problem prioritization — problems affecting services with poor SLA achievement may warrant higher priority |
| **Monitoring & Event Management (PR14)** | Events, monitoring data, and event correlation patterns that support proactive problem identification — detecting anomalies, trends, or degradation patterns before they cause incidents |
| **Supplier Management (PR23)** | Supplier information on known product defects, patches, and service issues that support proactive problem identification and problem investigation for supplier-provided components |
| **Knowledge Management (PR19)** | Knowledge articles and historical resolution data that support problem investigation and root cause analysis |

### Interfaces To Other Processes

| Target Process | Interface Description |
|---------------|----------------------|
| **Incident Management (PR11)** | Known errors and workarounds from the KEDB that enable faster incident diagnosis and resolution. Root cause information that improves incident classification accuracy and supports the development of incident models for incidents caused by known problems |
| **Change Management (PR15)** | Requests for change to implement permanent problem resolutions — including fixes to services, infrastructure, configurations, or procedures. Emergency changes may be required for high-impact problems |
| **Knowledge Management (PR19)** | Root cause analysis findings, investigation techniques used, and resolution approaches that are contributed to the knowledge base for organizational learning |
| **Continual Improvement (PR24)** | Improvement initiatives identified through problem reviews — including improvements to problem management methods, investigation techniques, KEDB quality, and cross-process collaboration |
| **Measurement & Reporting (PR20)** | Problem management data for management reporting — problem volumes, resolution rates, KEDB status, and the impact of problem resolution on incident trends and service stability |
| **Service Level Management (PR02)** | Problem resolution data that contributes to SLA achievement analysis — demonstrating the contribution of problem management to reduced incident volumes and improved service stability |
| **Service Desk (PR10)** | Known error and workaround information published through the KEDB for use by service desk agents during incident handling |
| **Supplier Management (PR23)** | Problem data related to supplier-provided components or services — feeding supplier performance assessment and supporting discussions with suppliers about product defects or service issues |
