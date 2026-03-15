---
process_id: PR15
process_name: "Change Management"
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
  - "ITIL 4: Change Enablement §2–§6"
  - "FitSM-2: §PR12 CHM"
  - "IT4IT: R2D Value Stream"
  - "SIAM: Service Integration (change coordination)"
last_updated: 2026-03-13
status: draft
---

# Change Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Change Enablement §2.1, FitSM-2 §PR12 CHM Objective -->

To maximize the number of successful service and product changes by ensuring that risks have been properly assessed, authorizing changes to proceed, and managing the change schedule. The process ensures that changes — additions, modifications, or removals of anything that could have a direct or indirect effect on services — are controlled, effective, and timely, balancing change throughput with risk management. It encompasses the full change lifecycle from registration through assessment, authorization, planning, realization control, review, and closure, as well as the continual optimization of change models and standard change procedures.

## Key Concepts

### Change
<!-- sources: ITIL 4 Change Enablement §2.2 -->

The addition, modification, or removal of anything that could have a direct or indirect effect on services. Changes may affect any of the four dimensions of service management — information and technology (hardware, software, service architecture), organizations and people (roles, responsibilities, competencies), value streams and processes (workflows, procedures), and partners and suppliers (contractual arrangements, service dependencies). The change enablement practice typically focuses on changes to the information and technology dimension but may extend to other dimensions depending on the organization's scope decisions.

### Standard Change
<!-- sources: ITIL 4 Change Enablement §2.2.1, FitSM-2 §PR12 CHM (identify well-known and recurring changes) -->

A low-risk, pre-authorized change that is well understood and fully documented, and which can be implemented without needing additional authorization for each instance. Standard changes follow a pre-defined procedure that has been fully risk-assessed and authorized when it was created or last modified. Examples include routine software updates, fulfilment of standard service requests, maintenance of infrastructure, and routine testing of contingency measures. Standard changes can also exist in high-uncertainty situations — such as standard incident resolutions or standard disaster responses. Standardization and automation of changes significantly increases throughput while retaining sufficient control.

### Normal Change
<!-- sources: ITIL 4 Change Enablement §2.2.1, FitSM-2 §PR12 CHM (manage change evaluation and approval) -->

A change that requires individual assessment, authorization, and planning because there is no effective standardized approach. Normal changes range from low risk (where the change authority can make rapid decisions, often with automation support) to high risk (where the change authority may be a management board or equivalent). Normal changes are triggered by a request for change (RFC) that may be manual or automated. The level of control, assessment depth, and authorization authority are determined by the applicable change model.

### Emergency Change
<!-- sources: ITIL 4 Change Enablement §2.2.1, FitSM-2 §PR12 CHM (define criteria for identifying emergency changes) -->

A change that must be introduced as soon as possible, typically to resolve a high-impact incident or to address an urgent security vulnerability. Emergency change models may include bypassed or delayed procedures — such as change request registration or updating the change schedule — but "emergency" does not mean "no rules or control." Emergency changes can and should be standardized and automated where possible. Some emergency changes deal with genuinely unpredictable situations where the cost of delay exceeds the risks associated with an unsuccessful change. A mandatory post-implementation review is required for all emergency changes.

### Change Authority
<!-- sources: ITIL 4 Change Enablement §2.2.1, §4.1.2 -->

A person or group responsible for authorizing a change. Change models should define requirements and procedures for authorization, delegating the role of change authority to the appropriate level — development teams, technical experts, service owners, or management — depending on the risk and impact of the change type. Formal committees such as Change Advisory Boards (CABs) that meet regularly to review accumulated changes can become bottlenecks that limit change throughput. Organizations should delegate change authority as close to the work as possible while maintaining appropriate risk control.

### Change Model
<!-- sources: ITIL 4 Change Enablement §2.2.1 Table 2.1, FitSM-2 §PR12 CHM (standard changes and step-by-step workflows) -->

A repeatable approach to the management of a particular type of change. Change models define how changes of a specific type are planned, assessed, authorized, realized, and reviewed. They can be defined based on: the systems or technologies being changed, the scale of the change, the locations or territories affected, the customers impacted, or the regulatory requirements that apply. A change model determines factors across all four dimensions of service management — including the process and level of formalization, the competencies needed, the change authority and delegation rules, information and tooling requirements, and the involvement of third parties.

### Change Schedule
<!-- sources: ITIL 4 Change Enablement §2.3, §3.2.1, FitSM-2 §PR12 CHM (create a schedule of changes) -->

A calendar or timeline showing all planned and ongoing changes, used to coordinate change activities, manage potential conflicts, and communicate change plans to relevant stakeholders. The change schedule provides visibility of what is being changed, when, and by whom — enabling the organization to identify potential clashes between changes, plan deployment windows, and inform affected users and services. In highly automated environments, the change schedule may be maintained automatically through orchestration and workflow tools.

### Request for Change (RFC)
<!-- sources: ITIL 4 Change Enablement §2.2.1, FitSM-2 §PR12 CHM (define standardised way of recording RFCs) -->

A formal request to initiate a change. The RFC captures the information needed for change assessment and authorization — including what is to be changed, why, the expected benefits, the estimated time and cost, the risks, and any regulatory considerations. RFCs may be raised by any role through defined channels and in a defined format. In organizations with CI/CD pipelines, change requests may be accumulated in a product or service backlog and the request process may be highly automated.

### Complexity-Based Approach
<!-- sources: ITIL 4 Change Enablement §2.2.1 -->

The principle that different situations — from routine business-as-usual through to catastrophic events — require different approaches to change planning, authorization, and control. At the predictable end of the spectrum, standard changes with pre-authorized procedures are appropriate. As complexity and uncertainty increase, changes require more expert analysis, possibly including safe-to-fail experiments to test multiple hypotheses before implementing a solution. At the chaotic end, emergency changes may be implemented without sufficient assessment when the cost of delay exceeds the risk of an unsuccessful change. Decreasing the size of individual changes is a key technique for managing complexity — smaller changes are less risky, easier to control, faster to implement, and less costly to reverse.

---

## Activities

### Essential (All tiers)
<!-- sources: ITIL 4 Change Enablement §3.2.1 Tables 3.1, 3.2, FitSM-2 §PR12 CHM (Manage change evaluation and approval, Manage change implementation and review) -->

| # | Activity | Description |
|---|----------|-------------|
| 1 | Register changes | Receive change requests from change initiators through defined channels. Create a change record in the ITSM tool with all required information — what is to be changed, the reason, expected benefits, estimated time and cost, and any regulatory considerations. For standard changes, registration may be automated or simplified. For backlog-managed changes, requests are accumulated in the product or service backlog |
| 2 | Classify changes | Categorize the change by type (standard, normal, or emergency) using defined criteria. Check against major change and emergency change criteria. Determine the applicable change model based on the classification. For standard changes, the pre-authorized procedure is identified and applied directly |
| 3 | Assess change impact and risk | Evaluate the change to understand its potential impact on services, users, infrastructure, and other ongoing or planned changes. Assess the associated risks, required resources, costs, and technical feasibility. Consult subject matter experts, configuration data from the CMS, and recent change and release information as needed. Assessment depth is determined by the change model |
| 4 | Authorize changes | The designated change authority reviews the assessment and provides authorization for the change to proceed. If not authorized, the change is returned for additional assessment or sent for closure. For standard changes, authorization is pre-granted through the approved standard change procedure. For low-risk normal changes, authorization may be delegated and rapid. For high-risk normal changes, a more formal authorization may be required |
| 5 | Plan and schedule changes | Plan the authorized change in detail — defining the implementation steps, resources, timescales, communication requirements, testing approach, and back-out plan. Update the change schedule with the planned implementation dates. Coordinate with other planned changes to avoid conflicts. Planning depth is determined by the change model — for small, automated standard changes, planning may be minimal |
| 6 | Control change realization | Monitor the implementation of the change by internal and external specialist teams. Ensure that deviations from the plan are detected and corrected. For automated standard changes, realization control includes automated validation, testing, configuration control, version control, and backup/restoration capabilities. For manually managed changes, the change manager ensures that implementation proceeds according to plan |
| 7 | Review and close changes | After the change is complete (or if it fails), review the change to assess whether it achieved its intended outcomes, was completed on time, and introduced any unintended consequences. Complete the change record with review findings and close it. For emergency changes, a mandatory post-implementation review is required. For automated standard changes, closure may be automatic after pre-agreed tests confirm success |

### Intermediate (T2+)
<!-- sources: ITIL 4 Change Enablement §2.2.1, §3.2.1, §3.2.2, FitSM-2 §PR12 CHM (initial setup activities) -->

| # | Activity | Description |
|---|----------|-------------|
| 8 | Manage the change schedule | Maintain and publish the change schedule showing all planned and ongoing changes. Ensure the schedule is available to all relevant stakeholders — including service owners, technical specialists, incident management, and users affected by planned changes. Identify and resolve scheduling conflicts between changes. Use the schedule to coordinate deployment windows and manage change freezes |
| 9 | Develop and maintain change models and standard change procedures | Define change models for different change types — specifying the assessment criteria, authorization level, planning requirements, realization controls, and review procedures. Identify recurring low-risk changes suitable for standardization and create standard change procedures with pre-authorized workflows. Review and update models and procedures based on change review findings and operational experience |
| 10 | Manage emergency changes | Operate the emergency change procedure — including expedited assessment and authorization, dedicated high-availability change authority, bypassed or accelerated planning steps where justified, and mandatory post-implementation review. Ensure emergency change criteria are clearly defined and consistently applied. Track emergency change volumes as an indicator of process and infrastructure stability |

### Advanced (T3)
<!-- sources: ITIL 4 Change Enablement §3.2.2 Tables 3.3, 3.4, §2.4 -->

| # | Activity | Description |
|---|----------|-------------|
| 11 | Analyse change reviews and optimize change models | Perform periodic analysis of change review data to identify patterns — unsuccessful changes, recurring issues, bottlenecks, and opportunities for further standardization or automation. Initiate improvements to change models, standard change procedures, and the change enablement practice. Communicate updated models and procedures to all affected teams |
| 12 | Drive continual improvement of change enablement | Review the effectiveness of the change enablement practice against its success factors — change effectiveness and timeliness, minimization of negative impacts, stakeholder satisfaction, and governance compliance. Identify improvement opportunities and register them through the continual improvement process. Measure the impact of improvements on change throughput, success rates, and risk levels |

---

## Inputs
<!-- sources: ITIL 4 Change Enablement §3.2.1 Table 3.1, FitSM-2 §PR12 CHM Inputs -->

| # | Input | Source |
|---|-------|--------|
| 1 | Requests for change (RFCs) | Any process or role (incident management, problem management, service requests, projects, etc.) |
| 2 | Configuration item data and relationships | Service Configuration Management (PR17) |
| 3 | Service level agreements and targets | Service Level Management (PR02) |
| 4 | Risk information and assessments | Risk Management (PR21) |
| 5 | Service catalogue and service architecture information | Service Catalogue Management (PR05), Service Design (PR04) |
| 6 | Financial guidelines and constraints | Service Financial Management (PR03) |

<!-- intermediate -->
| 7 | Change models and standard change procedures | Change Management (internal) |
| 8 | Information on planned releases and deployments | Release & Deployment Management (PR16) |
| 9 | Capacity and performance information | Capacity & Performance Management (PR08) |
| 10 | Information security policies and plans | Information Security Management (PR09) |
| 11 | IT asset information | IT Asset Management (PR18) |

---

## Outputs
<!-- sources: ITIL 4 Change Enablement §3.2.1 Table 3.1, §3.2.2 Table 3.3, FitSM-2 §PR12 CHM Outputs -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Change records (new and updated) | ITSM tool / change register |
| 2 | Authorized and planned changes for deployment | Release & Deployment Management (PR16) |
| 3 | Change schedule (current) | All stakeholders, Incident Management (PR11), Release & Deployment Management (PR16) |
| 4 | Information on implemented changes to CIs | Service Configuration Management (PR17) |
| 5 | Change review reports | Management, service owners |

<!-- intermediate -->
| 6 | Post-implementation review reports | Management, Problem Management (PR13), service owners |
| 7 | Updated change models and standard change procedures | Change Management (internal), all stakeholders |

<!-- advanced -->
| 8 | Change review analysis reports | Management, Continual Improvement (PR24) |
| 9 | Improvement initiatives | Continual Improvement (PR24) |

---

## Roles
<!-- sources: ITIL 4 Change Enablement §4.1.1, §4.1.2, §4.1.3 Table 4.2, FitSM-2 §PR12 CHM -->

| Role | Responsibilities | Tier |
|------|-----------------|------|
| **Change Manager** | Accountable for the change enablement practice. Processes and verifies change requests. Allocates changes to appropriate teams for assessment and authorization according to the change model. Formally communicates decisions of change authorities to affected parties. Monitors and reviews the activities of the teams that build and test changes. Publishes the change schedule and ensures it is available. Conducts regular and ad-hoc change review analyses and initiates improvements to the practice, change models, and standard change procedures. Develops the organization's expertise in change enablement processes and methods | All |
| **Change Coordinator** | Performs change management activities within a defined scope — a specific type of change, territory, or part of the organization. Has similar responsibilities to the change manager but with a more limited scope. Supports the change manager in processing change requests, coordinating assessments, planning changes, and maintaining the change schedule | T2+ |
| **Change Authority** | Responsible for authorizing changes based on assessment of risk, impact, and alignment with organizational objectives. The change authority varies by change model — from automated authorization for standard changes, through delegated authority for low-risk normal changes (service owners, technical leads), to management board or equivalent for high-risk normal changes. The change authority role should be delegated as close to the work as possible while maintaining appropriate risk control | All |
| **Service Owner** | Provides the service-level perspective on changes affecting their services — including impact assessment, risk evaluation, authorization input, and post-implementation review. Participates in change assessment and planning for changes affecting their services. May serve as change authority for changes within their service scope | All |

---

## Artefacts
<!-- sources: ITIL 4 Change Enablement §3.2.1, §5.1, FitSM-2 §PR12 CHM -->

| Artefact | Description | Tier |
|----------|-------------|------|
| **Change Record** | The formal record of a change through its lifecycle, containing: change description, initiator, affected services and CIs, impact and risk assessment, authorization decision, planned implementation details, realization status, review findings, and closure information. The change record tracks the change from registration through assessment, authorization, planning, realization, review, and closure | All |
| **Request for Change (RFC)** | A formal request to initiate a change, capturing: what is to be changed, the reason and expected benefits, estimated time and cost, risks, and any regulatory considerations. RFCs may be submitted through defined channels and in a defined format | All |
| **Change Schedule** | A calendar or timeline of all planned and ongoing changes, used to coordinate activities, manage conflicts, plan deployment windows, and communicate change plans to stakeholders | All |
| **Change Model** | A documented, repeatable approach for managing a specific type of change — defining the assessment criteria, authorization level and authority, planning requirements, realization controls, review procedures, and back-out approach. Change models are defined based on change type, scale, technology, location, or regulatory context | T2+ |
| **Standard Change Procedure** | A pre-authorized, documented procedure for implementing a specific type of low-risk recurring change. Includes the steps to be carried out, the controls applied, and the conditions under which the procedure applies. The procedure is fully risk-assessed when created or modified; individual instances do not require additional authorization | T2+ |
| **Post-Implementation Review Report** | A formal report documenting the review of a completed change — assessing whether it achieved intended outcomes, was completed on time and within budget, and identifying any lessons learned or unintended consequences. Mandatory for emergency changes and major changes | T2+ |
| **Change Review Analysis Report** | A periodic report analysing change data across a review period — patterns of unsuccessful changes, recurring issues, opportunities for standardization or automation, and recommendations for change model improvements | T3 |

---

## Process Interfaces
<!-- sources: ITIL 4 Change Enablement §2.3 Table 2.3, §6, FitSM-2 §PR12 CHM Key Interfaces -->

### Interfaces From Other Processes

| Source Process | Interface Description |
|---------------|----------------------|
| **Incident Management (PR11)** | Requests for change to resolve incidents — including emergency changes for major incidents. Recent change information is also consumed by incident management for incident diagnosis (identifying whether incidents are related to recent changes) |
| **Problem Management (PR13)** | Requests for change to implement permanent problem resolutions — eliminating root causes identified through problem investigation. Problem management is a key source of changes aimed at improving service stability |
| **Release & Deployment Management (PR16)** | Information on planned releases and deployments that informs change scheduling and coordination. Release information on deployed releases feeds post-implementation reviews |
| **Service Configuration Management (PR17)** | Configuration item data and relationships from the CMS that support change impact assessment — identifying which services and CIs are affected by a proposed change and what dependencies exist |
| **Service Level Management (PR02)** | Service level agreements and targets that inform change assessment — ensuring changes do not introduce risk of SLA breach and that change windows respect service availability requirements |
| **Service Request Management (PR12)** | Service requests that require changes to services or infrastructure, processed as standard changes or normal changes depending on their nature |
| **Risk Management (PR21)** | Risk assessments and risk information that support change assessment and authorization decisions |
| **Information Security Management (PR09)** | Security policies and requirements that must be considered during change assessment, and security-related changes (patches, vulnerability remediation) submitted as change requests |

### Interfaces To Other Processes

| Target Process | Interface Description |
|---------------|----------------------|
| **Release & Deployment Management (PR16)** | Authorized and planned changes that are ready for deployment, along with the change schedule with proposed deployment dates. Release and deployment management bundles approved changes into releases and manages their deployment |
| **Service Configuration Management (PR17)** | Information on planned, approved, and implemented changes to CIs, enabling the CMS to be updated to reflect the current and planned state of the infrastructure |
| **Incident Management (PR11)** | The change schedule and information on recent changes, which incident management uses to identify potential causes of incidents and to plan change-free periods for critical services |
| **Service Level Management (PR02)** | Change data that contributes to SLA achievement analysis — demonstrating the impact of changes on service availability and performance |
| **Continual Improvement (PR24)** | Improvement initiatives identified through change review analysis — including proposals for new or updated change models, standard change procedures, and practice improvements |
| **Measurement & Reporting (PR20)** | Change data for management reporting — volumes, success rates, timeliness, emergency change counts, and change-related incident data |
| **Knowledge Management (PR19)** | Lessons learned from change reviews contributed to the knowledge base for organizational learning |
| **Supplier Management (PR23)** | Change-related information for suppliers involved in change realization — coordinating third-party activities and managing supplier dependencies during change implementation |
