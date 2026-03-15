---
process_id: PR13
process_name: "Problem Management"
category: procedures
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
  - "ITIL 4: Problem Management §3.2.1–§3.2.4"
  - "FitSM-2: §PR10 PM"
  - "IT4IT: D2C Value Stream"
  - "SIAM: Service Integration (problem coordination)"
last_updated: 2026-03-13
status: draft
---

# Problem Management — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures cover the core operational activities — identifying problems from incident data, investigating root causes, documenting known errors, and resolving and closing problems. Intermediate procedures add proactive problem identification and structured problem reporting. The advanced procedure covers known error monitoring, periodic review, and continual improvement of problem management. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (All tiers)

### PROC-PM-01: Identify and Register Problems
<!-- sources: ITIL 4 Problem Management §3.2.2 Tables 3.4, 3.5, FitSM-2 §PR10 PM (Identify problems) -->

**Trigger:** Incident that cannot be resolved through existing incident models or known errors; recurring incidents of the same type; major incident review identifying an unresolved underlying cause; incident trend analysis revealing a pattern of related incidents

**Inputs:** Incident records and trend data from incident management, major incident review reports, service configuration data from the CMS, service level agreements and achievement data, monitoring data

**Outputs:** Problem records (new), feedback to the problem initiator (incident manager, technical specialist, or service owner)

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Detect the need for problem investigation | Identify that a problem exists based on the trigger. This may arise during an ongoing incident investigation (where the team working on the incident identifies the need for a separate problem investigation) or from analysis of past incident records (where a specialist team detects a pattern — such as a high number of similar incidents, a high percentage of incidents resolved after the target resolution time, a major incident, or availability below the target level) | Incident Manager / Technical Specialist |
| 2 | Register the problem | Log the problem in the ITSM tool with all available information: description, source of identification, associated incident records, associated CIs and CI classes, estimated impact and probability of future incidents, associated and potentially affected services, and impact on the organization and its customers. Link the problem record to the relevant incident records. Where the problem is identified during an ongoing incident, the problem record is linked to the incident for tracking purposes | Problem Manager / Problem Coordinator |
| 3 | Perform initial categorization | Categorize the problem based on the available information — including the affected service or product, the type of issue (software, hardware, procedural, third-party, data, capacity), and the affected CI classes. Initial categorization may change as problem analysis progresses, particularly for problems identified from incident symptom data | Problem Manager |
| 4 | Assign the problem | Based on the initial categorization, assign the problem to the specialist group responsible for the associated CI, service, or product. If the problem was registered after investigation had already begun (during incident handling), the assignment includes the investigation steps already taken, results obtained, and the current status | Problem Manager |

---

### PROC-PM-02: Investigate Problems and Document Known Errors
<!-- sources: ITIL 4 Problem Management §3.2.3 Tables 3.6, 3.7, FitSM-2 §PR10 PM (Handle problems — determine root cause, find workarounds) -->

**Trigger:** Problem record assigned for investigation; problem control initiated after problem identification

**Inputs:** Problem records, service configuration data, technical information about CIs, products, and services, incident records, monitoring data

**Outputs:** Updated problem records (with investigation findings), known error records (in the KEDB), incident solutions (workarounds communicated to incident management)

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Investigate the problem | The assigned specialist team investigates the possible causes of the problem. For reactively identified problems, localization starts with understanding which CIs may have errors causing past or ongoing incidents. For proactively identified problems, CIs or CI classes will typically have been identified during registration. Apply structured analysis techniques appropriate to the problem type — root cause analysis (five whys, fault tree analysis), impact analysis (component failure impact analysis, business impact analysis), and risk analysis. The investigation is not limited to CIs and includes other factors such as user behaviour, human errors, and procedure errors. After the problem is localized to the level of CIs, further diagnostics may be needed to identify specific errors — this work may involve different teams, resulting in reassignment | Technical Specialist |
| 2 | Determine the relevance and status of the problem | If the investigation finds that the reported problem is irrelevant to the organization (for example, a publicly reported vulnerability in software that the organization does not use), close the problem record. If the problem is relevant and the errors have been localized, assign it the known error status for further control and resolution | Problem Manager / Technical Specialist |
| 3 | Document the known error | Record the known error in the KEDB with: the root cause description, the affected CIs and services, the impact assessment, and any available workarounds with clear application instructions. The known error record becomes the primary reference for incident management when handling incidents caused by this problem | Problem Manager |
| 4 | Communicate known error findings | Communicate the results of the investigation to the problem initiator, relevant teams, and incident management. If there are ongoing incidents associated with the problem, communicate the localization results and any recommended incident solutions to the incident investigation teams. Where understanding the error is sufficient to define an incident resolution approach, register the recommended solution in the problem records and communicate it to incident-handling teams and the service desk | Problem Manager / Problem Coordinator |

---

### PROC-PM-03: Resolve and Close Problems
<!-- sources: ITIL 4 Problem Management §3.2.4 Tables 3.8, 3.9, FitSM-2 §PR10 PM (Handle problems — assess resolution options, close problems) -->

**Trigger:** Known error documented and awaiting resolution decision; problem resolution implemented and awaiting verification; problem no longer relevant to the organization

**Inputs:** Problem records, known error records, service configuration data, technical information about CIs, products, and services, incident records, monitoring data, knowledge management data

**Outputs:** Updated problem records, problem models (new or updated), change requests, improvement initiatives, problem solutions, updated KEDB (closed/deactivated known errors), knowledge base updates

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Develop the problem solution | The assigned team determines the appropriate mitigation approach for the known error: (a) full permanent fix — eliminating the root cause through a change; (b) permanent workaround — a durable mitigation that isolates the error and reduces impact; (c) optimized incident management — improving incident detection and handling for incidents caused by the known error. Develop the actual solution within the selected approach. If no viable solution exists, record the supporting information and schedule the error for periodic review | Technical Specialist |
| 2 | Initiate problem resolution | For solutions requiring changes to services, infrastructure, or configurations, submit requests for change through change management. The initiation should include relevant justification — financial, risk, compliance, and technical considerations. For solutions that do not require formal changes, the team initiates the required actions through the appropriate procedures and obtains any necessary approvals | Problem Manager / Technical Specialist |
| 3 | Verify the resolution | Confirm that the resolution has been successfully implemented and that the problem has been eliminated. For reactively identified problems, verification may be based on the change in incident dynamics — related incidents are resolved or prevented. For proactively identified problems, verification may include a period of monitoring to confirm that no incidents are caused by the formerly identified vulnerability. If the resolution is unconfirmed, return to the solution development step | Problem Manager / Technical Specialist |
| 4 | Close the problem | Document the resolution results and formally close the problem record. Update the KEDB to deactivate or close the known error record. Ensure that closed problem records remain available in the knowledge base, especially where there is a chance that similar problems may recur. If the investigation or resolution revealed a pattern that suggests the creation or amendment of a problem model, document and communicate the model as part of the closure activity | Problem Manager |

---

## Intermediate Procedures (T2+)

### PROC-PM-04: Identify Problems Proactively
<!-- sources: ITIL 4 Problem Management §3.2.1 Tables 3.1, 3.2, 3.3 -->

**Trigger:** Information received from vendors or suppliers about vulnerabilities or known defects in their products; errors discovered by developers, designers, or testers working on next versions of components; user and professional community reports of errors in shared systems; monitoring data showing suspicious trends or deviations in service or CI performance; technical audits identifying vulnerabilities

**Inputs:** Error information from vendors and suppliers, information about potential errors submitted by specialist teams, information from external user and professional communities, monitoring data, service configuration data

**Outputs:** Problem records (new), feedback to the problem initiator

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Review the submitted information | Assess the submitted information — whether received from vendors, specialist teams, user communities, or monitoring systems. The review includes checks for duplicates, applicability to the organization's environment, common sense assessment, and identification of any ongoing incidents potentially related to the submitted information. If the information does not warrant a problem record (for example, the vulnerability does not affect the organization's products), provide feedback to the initiator where appropriate | Problem Coordinator / Technical Specialist |
| 2 | Register the problem | If the review confirms the need for problem control, register a problem record with all available information: source, description, associated CIs and CI classes, estimated impact and probability of incidents, associated and potentially affected services, and impact on the organization and customers. This registration can be performed by a dedicated role (problem coordinator) or by a wider group of specialist roles | Problem Coordinator / Problem Manager |
| 3 | Perform initial categorization and assignment | Categorize the problem and assign it to the specialist group responsible for the associated CI, service, or product. Where applicable, notify the problem initiator about the registration. Proactive problem identification should focus on the key systems and components with the highest potential impact, but indications of errors in other systems should not be neglected — seemingly minor errors in non-core systems can contribute to serious incidents in complex environments | Problem Manager |

---

### PROC-PM-05: Produce Problem Reports and Analysis
<!-- sources: ITIL 4 Problem Management §2.5 Table 2.3, FitSM-2 §PR10 PM (regular reporting implied) -->

**Trigger:** Scheduled reporting cycle (monthly, quarterly); ad-hoc request from management or service owners; SLA review preparation; input requested by incident management or continual improvement

**Inputs:** Problem records from the ITSM tool, KEDB data, incident records and trend data, change request status for problem resolutions, improvement initiative status

**Outputs:** Problem reports (regular and ad-hoc), trend analysis data, input to SLA achievement reporting, input to continual improvement

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Extract problem and KEDB data | Extract problem data from the ITSM tool for the reporting period. Include problem volumes by category, priority, status, and assigned team. Include KEDB data — active known errors, new known errors, closed known errors, and workaround usage. Include change request status for problem resolutions in progress | Problem Coordinator |
| 2 | Analyse trends and patterns | Analyse the data for trends — changes in problem volumes, shifts in categorization distribution, services or CIs with high problem counts, resolution rates, time-to-resolution patterns, and the ratio of proactive to reactive problem identification. Compare with previous periods to identify emerging issues or improvements | Problem Manager |
| 3 | Compile the problem report | Produce the problem report covering: total problem volumes and breakdown by category and status, KEDB status (active known errors, new entries, closures), problem resolution rates and times, incidents prevented or more effectively resolved as a result of problem management, workaround effectiveness, proactive identification activity, and key observations or recommendations | Problem Manager |
| 4 | Distribute the report | Distribute the report to management, service owners, and other relevant stakeholders. Provide problem trend data to incident management for input to incident handling approaches. Provide input to SLA achievement reporting for service level management. Provide input to continual improvement for improvement planning | Problem Manager |

---

## Advanced Procedures (T3)

### PROC-PM-06: Monitor Known Errors and Drive Improvement
<!-- sources: ITIL 4 Problem Management §3.2.4 Table 3.9 (known error monitoring and review), §2.4.2 -->

**Trigger:** Scheduled periodic review of active known errors; change in incident dynamics for a known error (increase in frequency or severity); new resolution options becoming available (vendor patch, infrastructure upgrade, budget approval); strategic planning cycle requiring problem management input

**Inputs:** Active known error records from the KEDB, incident data related to known errors, monitoring data, change and release records, supplier updates, resource and budget information, problem model usage data, improvement initiative status from previous reviews

**Outputs:** Updated known error records (revised impact, workaround, or mitigation approach), problem solution development re-initiations, new or updated problem models, improvement initiatives registered in the continual improvement register, technical debt assessments

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Review active known errors | For each active known error under review, assess: the dynamics of associated incidents (frequency, severity, trend), the effectiveness of current incident solutions, the effectiveness of current workarounds, and any changes in the resources needed to solve the problem (budget, vendor updates, new infrastructure, specialist availability). The review may be periodic (scheduled) or triggered by outstanding monitoring results | Problem Manager / Technical Specialist |
| 2 | Reassess the mitigation approach | If the review finds that the current mitigation approach is no longer valid — the workaround is ineffective, incident impact has increased, or new resolution options have become available — re-initiate the problem solution development activity. This may include developing and implementing a problem solution, updating incident solutions for associated incidents, or revising the mitigation approach | Problem Manager |
| 3 | Update or create problem models | If the known error review reveals a pattern that suggests the creation or amendment of a problem model, document the model with the appropriate investigation techniques, steps, roles, and timescales. Communicate updated models to all affected teams | Problem Manager |
| 4 | Assess technical debt | Evaluate the accumulated technical debt from deferred problem resolutions and permanent workarounds. Assess the aggregate risk, the cost of continued mitigation, and the potential impact on service stability. Provide input to service portfolio management and continual improvement on the state of technical debt | Problem Manager |
| 5 | Identify improvement opportunities | Based on the review, identify specific improvement opportunities for problem management — investigation techniques, KEDB quality, problem model coverage, collaboration with incident management and other practices, tool capabilities, or team skills | Problem Manager |
| 6 | Register and track improvement initiatives | Register improvement initiatives in the continual improvement register with owners, target dates, and success criteria. Report on the progress of improvement initiatives from previous reviews. Escalate stalled or blocked improvements through management channels | Problem Manager |
| 7 | Initiate problem closure where appropriate | If a known error no longer exists — the problem has been removed by planned software or hardware updates, or by decommissioning the affected CIs — initiate formal problem closure. Document the closure rationale and ensure the knowledge base is updated | Problem Manager |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-PM-01 | Identify and Register Problems | All | Recurring incidents; unresolvable incident; major incident review; trend analysis |
| PROC-PM-02 | Investigate Problems and Document Known Errors | All | Problem assigned for investigation |
| PROC-PM-03 | Resolve and Close Problems | All | Known error awaiting resolution; resolution implemented; problem no longer relevant |
| PROC-PM-04 | Identify Problems Proactively | T2+ | Vendor advisory; monitoring anomaly; technical audit; user community report |
| PROC-PM-05 | Produce Problem Reports and Analysis | T2+ | Scheduled reporting cycle; ad-hoc request |
| PROC-PM-06 | Monitor Known Errors and Drive Improvement | T3 | Scheduled review; change in incident dynamics; new resolution options; strategic planning |
