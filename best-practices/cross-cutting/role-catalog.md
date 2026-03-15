---
process_id: cross-cutting
process_name: "Cross-Cutting"
category: roles
frameworks:
  - itil-v4
  - fitsm
maturity:
  essential: true
  intermediate: true
  advanced: true
sources:
  - "FitSM-3 Role Model V3.0.1 §4–§6"
  - "ITIL 4 Practice Guides (all 24 process areas)"
last_updated: 2026-03-14
status: draft
---

# Standard ITSM Role Catalog

## How to Use This Catalog

This catalog defines the standard roles used across ITSM processes. Roles are organized into four categories: governance roles that oversee the entire SMS, generic role patterns that recur across all processes, process-specific named roles for each of the 24 process areas, and a consolidated matrix mapping roles to processes. Role definitions are synthesized from FitSM-3 (generic patterns and FitSM-specific process roles) and ITIL 4 practice guides (practice-specific roles). During P3 authoring, the `3pa-author` skill uses this catalog to pre-populate RACI matrices and role sections. Organizations should customize role titles, combine roles where appropriate, and map to their own organizational structure.

---

## Governance Roles
<!-- essential -->
<!-- sources: FitSM-3 §4.1, §4.2 -->

### SMS Owner

| Attribute | Value |
|-----------|-------|
| **Tier** | All |
| **Scope** | Entire SMS |
| **Accountability** | Overall SMS effectiveness, alignment with business strategy |
| **Key Tasks** | Ensure top management commitment, approve SMS policy, conduct management reviews, approve SMS scope and plan, ensure resource allocation, represent SMS at executive level |
| **Competencies** | Strategic leadership, business-IT alignment, governance, stakeholder management |
| **FitSM Mapping** | SMS Owner (FitSM-3 §4.1) |
| **ITIL 4 Mapping** | Service management sponsor / executive sponsor |
| **Notes** | Must be a member of top management. Single point of accountability for the SMS. May delegate operational management to the SMS Manager |

### SMS Manager

| Attribute | Value |
|-----------|-------|
| **Tier** | All |
| **Scope** | Entire SMS |
| **Accountability** | Day-to-day SMS operations, process coordination, improvement planning |
| **Key Tasks** | Coordinate SMS implementation, manage process interactions, produce management reports, maintain SMS documentation, drive improvement programme, manage SMS resources, ensure process compliance |
| **Competencies** | ITSM frameworks, process management, project management, people management, reporting |
| **FitSM Mapping** | SMS Manager (FitSM-3 §4.2) |
| **ITIL 4 Mapping** | Practice manager (cross-practice) |
| **Notes** | Operational counterpart to the SMS Owner. Responsible for ensuring all processes work together. May serve as process owner for multiple processes in smaller organizations |

---

## Generic Role Patterns
<!-- essential -->
<!-- sources: FitSM-3 §5.1–§5.4 -->

These four patterns apply to every ITSM process. In smaller organizations, one person may hold multiple pattern roles across processes or combine patterns within a single process (e.g., serving as both process owner and process manager).

### Process Owner

| Attribute | Value |
|-----------|-------|
| **Pattern** | One per process |
| **Accountability** | Process fitness for purpose, strategic direction, continual improvement |
| **Key Tasks** | Define process goals and strategy, ensure process is documented and communicated, allocate resources, approve process changes, review process performance, sponsor process improvement |
| **Competencies** | Strategic thinking, stakeholder management, ITSM domain knowledge |
| **Notes** | Often a senior manager. Owns the process holistically — not individual cases. Must have authority to make decisions about the process |

### Process Manager

| Attribute | Value |
|-----------|-------|
| **Pattern** | One or more per process |
| **Accountability** | Operational process execution, day-to-day management |
| **Key Tasks** | Manage process execution, coordinate staff, monitor KPIs, maintain procedures, handle escalations, produce operational reports, ensure compliance with process design |
| **Competencies** | Operational management, ITSM domain expertise, people management, analytical skills |
| **Notes** | Reports to the Process Owner on process performance. In smaller organizations, may also be the Process Owner |

### Case Owner

| Attribute | Value |
|-----------|-------|
| **Pattern** | One per case/ticket |
| **Accountability** | End-to-end management of a single case through the process |
| **Key Tasks** | Manage the case from registration to closure, coordinate with stakeholders, ensure progress within agreed timelines, update records, communicate with affected parties |
| **Competencies** | Technical knowledge, communication, time management, problem-solving |
| **Notes** | Applicable to ticket-based processes (incidents, service requests, problems, changes, releases). Case ownership may transfer between individuals but accountability remains clear at all times |

### Process Staff Member

| Attribute | Value |
|-----------|-------|
| **Pattern** | Multiple per process |
| **Accountability** | Execution of assigned process activities |
| **Key Tasks** | Perform process activities as directed, follow procedures, create and update records, escalate when needed, contribute domain expertise |
| **Competencies** | Technical skills relevant to the process, attention to detail, procedural compliance |
| **Notes** | The operational workforce of each process. May participate in multiple processes |

---

## Process-Specific Named Roles

### Governance & Strategy (Phase A)
<!-- essential -->
<!-- sources: FitSM-3 §6.1; ITIL 4 SPM, ISM, SCFGM, SFM -->

| Process | Role | Abbr. | Tier | Description |
|---------|------|:-----:|:----:|-------------|
| PR01 SPM | Service Portfolio Manager | SPM | All | Manages the service portfolio lifecycle — maintains portfolio records, evaluates proposals for new/changed services, coordinates service lifecycle transitions, ensures portfolio alignment with strategy |
| PR01 SPM | Service Owner | SO | All | Accountable for the delivery of a specific service — coordinates across processes to ensure the service meets agreed levels, represents the service in governance forums |
| PR01 SPM | Service Portfolio Analyst | SPA | T2+ | Analyses portfolio data, prepares business cases for service proposals, produces portfolio reports, supports demand and investment analysis |
| PR09 ISM | Information Security Manager | ISM | All | Manages the information security management practice — develops security policy, conducts risk assessments, coordinates security controls, manages security incidents |
| PR09 ISM | Information Security Team Member | ISMT | All | Implements security controls, monitors security events, performs vulnerability assessments, maintains security documentation |
| PR09 ISM | Information Security Officer | ISO | T2+ | Provides specialist security expertise — conducts security audits, advises on compliance requirements, reviews security architecture, manages security awareness programme |
| PR17 SCFGM | Configuration Manager | CM | All | Manages the configuration management practice — defines CI scope, maintains CMDB integrity, coordinates verification activities |
| PR17 SCFGM | Configuration Management Team Member | CMT | All | Maintains CI records, performs CMDB updates, supports verification audits, manages CI relationships |
| PR17 SCFGM | CI Owner | CIO | T2+ | Accountable for the accuracy of a specific CI or CI group — ensures CI records are current, authorizes CI changes within scope |
| PR03 SFM | Service Financial Manager | SFM | T3 | Manages financial planning, budgeting, accounting, and charging for IT services — maintains financial models, produces cost reports, advises on investment decisions |
| PR03 SFM | Service Financial Management Team Member | SFMT | T3 | Supports financial modelling, processes cost allocations, maintains financial records, produces financial reports |
| PR03 SFM | Service Budget Approver | SBA | T3 | Authorizes financial commitments — approves budgets, reviews cost-benefit analyses, ensures financial governance compliance |

### Design & Transition (Phase B)
<!-- essential -->
<!-- sources: FitSM-3 §6.2, §6.7–§6.8; ITIL 4 SLM, SDES, SCATM, RELM, SUPPM -->

| Process | Role | Abbr. | Tier | Description |
|---------|------|:-----:|:----:|-------------|
| PR02 SLM | Service Level Manager | SLM | All | Manages service level agreements — negotiates SLAs/OLAs/UAs, conducts service reviews, monitors service performance against targets, manages underpinning agreements |
| PR02 SLM | Service Level Management Team Member | SLMT | All | Supports SLA management activities, collects performance data, prepares service reports, coordinates with service owners |
| PR02 SLM | Service Review Owner | SRO | T2+ | Leads formal service reviews with customers — prepares review materials, facilitates discussions, documents outcomes and actions |
| PR04 SDES | Service Design Manager | SDM | T3 | Coordinates service design activities — ensures design packages are complete, facilitates design reviews, manages transition to operations |
| PR04 SDES | Service Design Team Member | SDT | T3 | Produces design artefacts, participates in design workshops, documents service models, supports utility and warranty analysis |
| PR04 SDES | Service Design Authority | SDA | T3 | Approves service designs against standards and constraints — reviews design packages for completeness, ensures architectural compliance |
| PR05 SCATM | Service Catalogue Manager | SCM | T2+ | Manages the service catalogue — ensures catalogue accuracy, coordinates with service owners, publishes catalogue to stakeholders |
| PR05 SCATM | Service Catalogue Team Member | SCT | T2+ | Maintains catalogue records, updates service descriptions, manages catalogue access, supports catalogue publication |
| PR05 SCATM | Service Catalogue Owner | SCO | T2+ | Accountable for a catalogue entry — ensures service descriptions are accurate and current, approves catalogue updates for their service |
| PR22 RELM | Relationship Manager | RELM | All | Manages stakeholder relationships — maintains satisfaction, handles complaints, conducts relationship reviews, facilitates communication between provider and customer |
| PR22 RELM | Relationship Management Team Member | RELMT | All | Supports relationship activities, manages communication channels, collects satisfaction data, coordinates service ordering |
| PR22 RELM | Customer Relationship Representative | CRR | T2+ | Designated contact for a specific customer or customer group — manages day-to-day relationship, escalates issues, represents customer interests |
| PR23 SUPPM | Supplier Manager | SUPPM | T2+ | Manages supplier relationships — negotiates contracts, evaluates supplier performance, manages disputes, ensures supplier alignment |
| PR23 SUPPM | Supplier Management Team Member | SUPPMT | T2+ | Supports supplier management activities, monitors contract compliance, maintains supplier records, coordinates operational interactions |
| PR23 SUPPM | Supplier Relationship Representative | SRR | T2+ | Designated contact for a specific supplier — manages day-to-day relationship, monitors delivery, escalates supplier issues |

### Operations (Phase C)
<!-- essential -->
<!-- sources: FitSM-3 §6.9–§6.13; ITIL 4 SDESK, IM, SRM, PM, MEM, CHM, RDM -->

| Process | Role | Abbr. | Tier | Description |
|---------|------|:-----:|:----:|-------------|
| PR10 SDESK | Service Desk Manager | SDMGR | All | Manages the service desk function — staffing, workflows, quality, first-contact resolution, user communication channels, omnichannel integration |
| PR10 SDESK | Service Desk Analyst | SDAN | All | Handles user contacts — logs incidents and service requests, provides first-line resolution, routes and escalates, communicates with users |
| PR10 SDESK | Service Desk Supervisor | SDS | T2+ | Oversees daily service desk operations — monitors queue health, manages shift handovers, coaches analysts, handles escalations |
| PR11 IM | Incident Manager | IM | All | Manages the incident management practice — ensures timely resolution, coordinates escalations, oversees major incident process |
| PR11 IM | Incident Management Team Member | IMT | All | Investigates and resolves incidents, applies workarounds, updates incident records, participates in diagnosis and recovery |
| PR11 IM | Major Incident Manager | MIM | T2+ | Leads the response to major incidents — convenes resolution teams, manages stakeholder communication, drives restoration, coordinates post-incident review |
| PR12 SRM | Service Request Manager | SRM | All | Manages the service request fulfilment practice — maintains the request catalogue, ensures fulfilment within agreed timelines |
| PR12 SRM | Service Request Management Team Member | SRMT | All | Fulfils service requests, follows fulfilment procedures, updates request records, communicates with requestors |
| PR12 SRM | Request Fulfilment Coordinator | RFC | T2+ | Coordinates complex or multi-team requests — orchestrates fulfilment activities, tracks dependencies, ensures end-to-end delivery |
| PR13 PM | Problem Manager | PM | All | Manages the problem management practice — coordinates investigation, maintains known error database, drives root cause analysis |
| PR13 PM | Problem Management Team Member | PMT | All | Investigates problems, performs root cause analysis, develops workarounds, documents known errors |
| PR13 PM | Problem Investigation Analyst | PIA | T2+ | Conducts in-depth technical investigation — applies structured analysis techniques, produces investigation reports, recommends permanent solutions |
| PR14 MEM | Event Manager | EM | T2+ | Manages the monitoring and event management practice — defines event rules, manages monitoring tools, ensures events are correctly categorized and routed |
| PR14 MEM | Monitoring & Event Management Team Member | MEMT | T2+ | Configures monitoring tools, responds to events, tunes thresholds, maintains event rules |
| PR14 MEM | Event Monitoring Analyst | EMA | T2+ | Analyses event patterns, identifies trends, recommends threshold adjustments, investigates event correlation |
| PR15 CHM | Change Manager | CHM | All | Manages the change management practice — coordinates change assessment, chairs CAB, manages change schedule, ensures change governance |
| PR15 CHM | Change Authority | CHA | All | Authorized to approve changes at a defined level — standard, normal, or emergency. May be a person, group, or the CAB |
| PR15 CHM | CAB Member | CABM | T2+ | Participates in Change Advisory Board — provides specialist input on change impact, risk, and scheduling |
| PR16 RDM | Release Manager | RM | T2+ | Manages release and deployment activities — plans releases, coordinates build and test, manages deployment schedule |
| PR16 RDM | Release & Deployment Team Member | RDT | T2+ | Builds, tests, and deploys releases, manages deployment infrastructure, performs rollback procedures |
| PR16 RDM | Deployment Engineer | DE | T2+ | Executes deployment activities — manages deployment scripts, monitors deployment health, performs technical rollback |

### Assurance (Phase D)
<!-- essential -->
<!-- sources: FitSM-3 §6.4–§6.6, §6.14; ITIL 4 AM, SCM, CPM, ITAM, KM, MR, RM, CI -->

| Process | Role | Abbr. | Tier | Description |
|---------|------|:-----:|:----:|-------------|
| PR06 AM | Availability Manager | AM | All | Manages service availability — analyses availability data, identifies single points of failure, designs availability improvements, produces availability plans |
| PR06 AM | Availability Management Team Member | AMT | All | Monitors availability, collects availability data, supports availability analysis, maintains availability records |
| PR06 AM | Availability Design Authority | ADA | T2+ | Reviews and approves availability designs — ensures availability requirements are met in service design, validates resilience measures |
| PR07 SCM | Service Continuity Manager | SCMGR | T2+ | Manages service continuity — maintains continuity plans, coordinates testing, manages recovery capabilities |
| PR07 SCM | Service Continuity Team Member | SCMT | T2+ | Supports continuity planning, participates in exercises, maintains recovery procedures, manages continuity documentation |
| PR07 SCM | Service Continuity Exercise Coordinator | SCE | T2+ | Plans and executes continuity exercises — designs test scenarios, facilitates exercises, documents results, coordinates improvement actions |
| PR08 CPM | Capacity & Performance Manager | CPM | All | Manages capacity and performance — analyses trends, forecasts demand, produces capacity plans, manages performance monitoring |
| PR08 CPM | Capacity & Performance Team Member | CPMT | All | Monitors capacity and performance metrics, collects data, supports analysis, maintains monitoring configurations |
| PR08 CPM | Capacity Planning Analyst | CPA | T2+ | Conducts detailed capacity analysis — models future demand, analyses growth trends, recommends capacity adjustments |
| PR18 ITAM | IT Asset Manager | ITAM | T2+ | Manages IT assets through their lifecycle — maintains asset register, coordinates procurement and disposal, ensures licence compliance, optimizes asset utilization |
| PR18 ITAM | IT Asset Management Team Member | ITAMT | T2+ | Maintains asset records, performs asset audits, processes asset requests, tracks licence usage |
| PR18 ITAM | Asset Lifecycle Owner | ALO | T2+ | Accountable for a category of assets through their lifecycle — plans procurement, manages refresh cycles, ensures disposal compliance |
| PR19 KM | Knowledge Manager | KM | T2+ | Manages the knowledge management practice — establishes KM environment, curates knowledge assets, promotes knowledge sharing culture |
| PR19 KM | Knowledge Management Team Member | KMT | T2+ | Maintains knowledge assets, processes information requests, validates knowledge content, supports KM tools |
| PR19 KM | Knowledge Asset Owner | KAO | T2+ | Accountable for the quality and currency of specific knowledge assets — reviews content, approves updates, ensures accessibility |
| PR20 MR | Measurement & Reporting Manager | MRM | All | Manages measurement and reporting — defines metrics framework, produces management reports, ensures data quality |
| PR20 MR | Measurement & Reporting Team Member | MRT | All | Collects data, produces reports, maintains dashboards, supports data analysis |
| PR20 MR | Report Design Authority | RDA | T2+ | Designs report specifications — ensures reports meet stakeholder needs, validates data sources, approves report templates |
| PR21 RM | Risk Management Committee Member | RMC | T2+ | Governs the risk management framework — analyses the environment, documents risk capacity and appetite, establishes risk policy, monitors organizational risk management |
| PR21 RM | Risk Owner | RO | T2+ | Accountable for a specific risk — ensures the risk is identified, analysed, evaluated, and appropriately treated within agreed timeframes |
| PR21 RM | Risk Auditor | RA | T3 | Conducts risk audits — assesses risk management effectiveness, verifies controls, ensures framework compliance, provides independent assurance |
| PR24 CI | CSI Manager | CIM | All | Manages continual improvement — maintains CSI register, evaluates improvement proposals, coordinates improvement implementation |
| PR24 CI | Continual Improvement Team Member | CIMT | All | Supports improvement activities, analyses improvement opportunities, tracks improvement progress |
| PR24 CI | Improvement Owner | IO | All | Accountable for a specific improvement initiative — manages implementation, tracks benefits, reports on outcomes |

---

## Role-to-Process Matrix
<!-- intermediate -->

This matrix shows primary involvement. **P** = Primary role in this process. **S** = Supporting role. **G** = Governance oversight. Organizations should customize based on their structure. Blank cells indicate no standard involvement — though organizations may extend roles as needed.

| Role | PR01 | PR02 | PR03 | PR04 | PR05 | PR06 | PR07 | PR08 | PR09 | PR10 | PR11 | PR12 | PR13 | PR14 | PR15 | PR16 | PR17 | PR18 | PR19 | PR20 | PR21 | PR22 | PR23 | PR24 |
|------|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| SMS Owner | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G |
| SMS Manager | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G | G |
| Service Portfolio Mgr | P | S | S | S | S | | | | | | | | | | | | | | | S | | S | S | S |
| Service Owner | S | P | | S | P | S | S | S | | | S | S | | | S | | S | | | S | | S | | |
| Service Level Mgr | S | P | | | S | S | | | | S | S | S | | | | | | | | S | | S | S | |
| Info Security Mgr | | | | | | | | | P | | S | | | S | S | | S | S | | | S | | | |
| Configuration Mgr | S | | | | S | | | | S | | | | | | S | S | P | S | | | | | | |
| Change Mgr | | | | | | | | | | | | | | | P | S | S | | | | | | | |
| Incident Mgr | | S | | | | S | S | | S | S | P | | S | S | S | | | | S | | | | | |
| Problem Mgr | | | | | | S | | S | S | | S | | P | S | S | | S | | S | | | | | |
| Service Desk Mgr | | S | | | | | | | | P | S | S | | | | | | | S | | | S | | |
| Release Mgr | | | | | | | | | | | | | | | S | P | S | | | | | | | |
| Availability Mgr | S | S | | S | | P | S | S | | | S | | S | S | | | S | | | S | S | | | |
| Capacity Mgr | S | S | S | S | | S | | P | | | | | | S | | | S | | | S | | | | |
| Relationship Mgr | S | S | | | | | | | | S | | S | | | | | | | | | | P | S | |
| Supplier Mgr | S | S | S | | | | | | | | | | | | | S | | | | | | S | P | |
| CSI Mgr | S | S | | | | | | | | | | | | | | | | | | S | | | | P |
| Risk Mgmt Committee | | | | | | | S | | S | | | | | | S | | | | | | P | | | S |
| M&R Mgr | | S | | | | S | | S | | | | | | S | | | | | | P | | | | S |
| Knowledge Mgr | | | | | | | | | | | | | | | | | | | P | | | | | S |
| IT Asset Mgr | | | | | | | | | | | | | | | | | S | P | | | | | S | |

---

## Job Title Mapping
<!-- essential -->

| Standard ITSM Role | Common Job Titles |
|---------------------|-------------------|
| SMS Owner | CIO, VP of IT, IT Director, Head of IT Services |
| SMS Manager | ITSM Manager, IT Operations Manager, Service Delivery Manager |
| Service Portfolio Manager | IT Portfolio Manager, Service Strategy Manager |
| Service Owner | Service Delivery Lead, Product Owner (IT Services) |
| Service Level Manager | SLA Manager, Service Performance Manager |
| Information Security Manager | CISO, IT Security Manager, InfoSec Lead |
| Configuration Manager | CMDB Manager, Asset & Configuration Lead |
| Change Manager | Change Control Manager, CAB Chair |
| Incident Manager | IT Operations Manager, Support Manager |
| Major Incident Manager | Crisis Manager, Major Incident Coordinator |
| Problem Manager | Root Cause Analyst Lead, Problem Coordinator |
| Service Desk Manager | Help Desk Manager, Support Centre Manager |
| Service Desk Analyst | Help Desk Analyst, Support Analyst, Level 1 Support |
| Release Manager | Release Coordinator, Deployment Manager |
| Availability Manager | Reliability Engineer Lead, SRE Manager |
| Capacity Manager | Performance Engineer, Capacity Planner |
| Service Continuity Manager | Disaster Recovery Manager, BCM Manager |
| Supplier Manager | Vendor Manager, Third-Party Relationship Manager |
| Relationship Manager | Customer Success Manager, Client Relationship Manager |
| CSI Manager | Process Improvement Manager, Quality Manager |
| Risk Management Committee Member | Risk Manager, Compliance Officer, GRC Analyst |
| IT Asset Manager | Asset Management Lead, Licence Compliance Manager |
| Knowledge Manager | Knowledge Base Administrator, Content Manager |
| Measurement & Reporting Manager | Analytics Manager, BI Manager, Reporting Lead |

---

## Notes

1. **Role combination:** In smaller organizations (T1), multiple roles are typically combined. A single person may serve as SMS Manager, Change Manager, and CSI Manager simultaneously. The minimum viable role set for T1 is: SMS Owner, SMS Manager (combined with one or more process manager roles), Service Desk Analyst(s), and Process Staff as needed.
2. **Scaling guidance:** T1 organizations typically need 3–5 named role holders. T2 organizations typically need 8–15. T3 organizations typically need 15–30+, with specialist roles and dedicated process managers.
3. **FitSM-3 mapping:** FitSM defines 14 processes (PR1–PR14) with specific role descriptions. The 3PA unified model extends to 24 processes (PR01–PR24) — the additional processes (PR03 SFM, PR04 SDES, PR05 SCATM partial, PR06/PR07 split from SACM, PR10 SDESK, PR14 MEM, PR18 ITAM, PR19 KM, PR20 MR, PR21 RM) draw roles from ITIL 4 practice guides.
4. **Distributed roles:** Some roles (Risk Owner, CI Owner, Knowledge Asset Owner, Improvement Owner, Service Owner) are inherently distributed — they are held by many people across the organization, each accountable within their scope of control.
5. **Authority levels:** Change Authority, Service Design Authority, Availability Design Authority, and Report Design Authority are approval roles that may be held by individuals, committees, or delegated based on risk and impact criteria.
