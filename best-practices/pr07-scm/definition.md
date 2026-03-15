---
process_id: PR07
process_name: "Service Continuity Management"
category: definition
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
  - "ITIL 4: Service Continuity Management §2–§6"
  - "FitSM-1: §PR4.1–§PR4.3 (continuity scope)"
  - "FitSM-2: §PR4 SACM (continuity scope)"
  - "IT4IT: D2C Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Continuity Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 SCM §2.1, FitSM-0 §6.17 -->

The purpose of the service continuity management practice is to ensure that the availability and performance of a service are maintained at sufficient levels in case of a disaster. The practice provides a framework for building organizational resilience with the capability of producing an effective response that safeguards the interests of key stakeholders and the organization's reputation, brand, and value-creating activities. The practice helps ensure a service provider's readiness to respond to high-impact incidents which disrupt the organization's core activities or credibility. It is closely related to, and may be merged with, the availability management practice — and may be incorporated into the broader business continuity management function. The concept of risk is central: the practice generally focuses on mitigating high-impact, low-probability risks which cannot be totally prevented because some risk factors are outside the organization's control. In FitSM, service continuity is managed together with availability in PR4 (Service Availability and Continuity Management), with continuity defined as the property of a service to maintain all or parts of its functionality even in exceptional circumstances including emergencies, crises, or disasters.

## Scope
<!-- sources: ITIL 4 SCM §2.3, FitSM-1 §PR4.1–§PR4.3 -->

This process covers:

- Performing business impact analysis to quantify the impact of service unavailability to the service provider and service consumers
- Developing service continuity strategies — including risk-mitigation measures and selection of appropriate recovery options
- Developing and managing service continuity plans — and providing a clear interface to business continuity plans where relevant
- Performing exercises and testing service continuity plan invocation in case of disaster
- Invoking and executing service continuity plans during actual disruptive events

This process does not cover: communicating with customers to align business and service continuity strategies (relationship management), negotiating and agreeing customer requirements for service continuity (service level management), designing service continuity solutions as part of the service model (service design), identifying risks associated with service continuity (risk management), establishing and managing contracts with suppliers and partners (supplier management), monitoring the availability of services (monitoring and event management), implementing risk mitigation measures and changing IT infrastructure to ensure resilience (project management, change management), managing and implementing improvements on an ongoing basis (continual improvement).

## Key Concepts
<!-- sources: ITIL 4 SCM §2.2 -->

### 1. Disaster and Service Continuity
<!-- sources: ITIL 4 SCM §2.1, §2.2, §2.2.1, FitSM-0 §6.17 -->
A disaster is a sudden unplanned event that causes great damage or serious loss to an organization — to be classified as a disaster, the event must match predefined business-impact criteria. Typical disasters include cyber attacks, electricity outages, failures of strategic partners, fires, floods, key personnel unavailability, large-scale IT infrastructure failures, and natural disasters. Events that are not disasters include minor failures (assessed based on business impact) and strategic, political, market, or industry events. Service continuity is the capability of the service provider to continue service operation at acceptable predefined levels following a disaster. The practice is distinguished from availability management: availability focuses on high-probability risks and proactive prevention, while continuity focuses on high-impact risks and reactive response. Availability management reduces the likelihood of unwanted events through optimization; continuity management reduces the impact through redundancy and recovery planning.

### 2. Recovery Objectives
<!-- sources: ITIL 4 SCM §2.2.2, §2.2.3, §2.2.4 -->
Three recovery objectives define the requirements for service continuity. The recovery time objective (RTO) is the maximum period following a disruption that can elapse before the lack of business functionality severely impacts the organization — the maximum agreed time within which a service must be resumed. The recovery point objective (RPO) is the point to which information must be restored to enable the service to operate effectively upon resumption — it defines the period of acceptable data loss and drives backup frequency. The minimum target service level is the level of service acceptable during a disruption — usually defined in terms of available service actions, limited user groups, or reduced transaction throughput. RTO should be less than the maximum acceptable outage by an amount reflecting organizational risk appetite. RPO depends on data criticality and production rate. All three are determined during business impact analysis and documented in service continuity plans.

### 3. Business Impact Analysis
<!-- sources: ITIL 4 SCM §2.2.5, §3.2.2, FitSM-2 §PR4 -->
A key activity that identifies vital business functions (VBFs) and their dependencies — including suppliers, people, business processes, and IT services. BIA defines the recovery requirements for IT services: RTOs, RPOs, and minimum target service levels. The process involves identifying VBFs, analysing the consequences of disruption (both hard impacts such as financial loss and soft impacts such as reputational damage), identifying VBF interdependencies using service and configuration models, and determining service continuity requirements. Impacts may change over time — a service provider may function without a particular service briefly, but losses typically grow exponentially. BIA should be performed when context changes (new consumer, new service) and otherwise at least annually, synchronized with risk assessment cycles. FitSM requires that continuity requirements be identified based on SLAs and business impact analysis, and that continuity risks be assessed at planned intervals.

### 4. Service Continuity Plans
<!-- sources: ITIL 4 SCM §2.2.6, §2.4.1, §3.2.3 -->
Clearly defined plans guiding the service provider through response, recovery, and restoration following a disruption. Plans cover three stages: the response plan defines how to react initially to prevent further damage; the recovery plan defines how to recover the service to achieve RTO and RPO; the plan for returning to normal operations defines how to resume full service following recovery. Plans operate at three levels: strategic (how executives make decisions and communicate externally), tactical (how management coordinates recovery and allocates resources), and operational (how teams perform recovery activities). Plans should be clear, concise, and action-oriented — excluding information not directly applicable to recovery teams. Procedures should be time-based and include information about delays and interrelations between plans and teams. Plans are developed based on BIA outputs and service continuity strategies, and must be updated when services or team members change, following exercises, or after actual recovery.

### 5. Service Continuity Strategies
<!-- sources: ITIL 4 SCM §2.4.1, §2.4.2 -->
The set of approaches selected for ensuring service continuity, chosen with respect to continuity requirements identified during BIA. Strategies include diversification, replication, standby, post-incident acquisition, do nothing, and subcontracting. For services with earlier and higher impacts, more preventive measures should be adopted; where impact is lower and develops slowly, greater emphasis on recovery measures is more cost-effective. Risk mitigation measures span all four dimensions of service management: organizations and people (managing people during disasters, alternative facilities), information and technology (physical security, data protection, backups, fault-tolerant applications, monitoring), partners and suppliers (reciprocal agreements, multi-provider outsourcing), and processes and value streams (manual operations, alternative methods, recovery procedures). The effectiveness of each measure should be compared against expected losses, and the cost should be compared against the benefit.

### 6. Exercises and Testing
<!-- sources: ITIL 4 SCM §2.4.3, §3.2.4 -->
The only way of ensuring that strategies, measures, and plans actually work. Five exercise types of increasing rigour: walkthrough exercises (discussion-based, unpressurized, for initial team familiarization), table-top exercises (scenario-based discussion, may include time-jumps, for improving plan knowledge), command-post exercises (simulated real incident, for testing communication and coordination), live exercises (most realistic, from small-scale component rehearsal to full-scale organizational recovery, for testing RTO/RPO/minimum-level achievement), and tests (applied to specific hardware or software with pass/fail criteria). Exercises should be conducted at planned intervals and when significant changes may impact recovery. The higher the possible impact of outage, the higher the exercise frequency. Exercises are also improvement opportunities — findings and recommendations should be documented in exercise reports. Failed exercises should be rescheduled as soon as possible. Plans should be tested across all four dimensions: the right people with the right skills, required equipment and data available, third parties ready, and procedures correct and manageable.

## Activities
<!-- sources: ITIL 4 SCM §3.2.1–§3.2.5, FitSM-2 §PR4 -->

### Essential (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Define scope and policy | Define the practice scope — which services, products, sites, and locations are covered, and which situations constitute disasters. Scope may be staged if implementation costs are high. Set policy documenting scope, roles and responsibilities, organizational structure for response and recovery, general approach, available resources, and limitations. Communicate policies to all stakeholders. Revise scope and policies at least annually or when triggered by uncovered events, new services, or new relationships |
| 2 | Identify vital business functions and perform BIA | Identify VBFs using brainstorming, stakeholder interviews, service documentation analysis, and risk assessment information. Analyse consequences of disruption — both financial and reputational impacts. Identify VBF interdependencies using service and configuration models and component failure impact analysis. Determine RTO, RPO, and minimum target service levels for each service or VBF within scope |
| 3 | Develop service continuity strategies and plans | Based on BIA outputs, determine cost-effective continuity strategies. Develop service continuity plans at strategic, tactical, and operational levels — covering response, recovery, and restoration. Ensure plans are clear, concise, action-oriented, and time-based. Perform initial testing before publication. Update plans when services or teams change |
| 4 | Invoke and execute service continuity plans | When a disruptive event meets disaster criteria, the crisis management group decides on invocation — accounting for potential impact, likely duration, and timing. Execute response, recovery, and restoration procedures. Coordinate recovery teams across tactical and operational levels. Produce recovery reports with findings and recommendations |
| 5 | Develop and maintain awareness and exercise programme | Plan education, awareness training, and exercises to ensure all parts of the practice are tested at least annually — covering all four dimensions of service management. Schedule exercises appropriate to impact levels and organizational change |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 6 | Perform exercises and test plans | Conduct exercises at planned intervals and when significant changes may impact recovery. Analyse findings and team performance. Produce exercise reports with recommendations. If exercises fail, reschedule as soon as possible. Update plans based on findings |
| 7 | Conduct service continuity audits | Ensure BIA, strategies, and plans remain appropriate and relevant as the environment changes. Audits may be scheduled or triggered by failed exercises or failed recoveries. Conducted internally or by third parties. Output may identify needs for new or updated controls or policy adjustments |
| 8 | Assess and manage risk mitigation measures | Define and manage controls across all four dimensions. Assess effectiveness of each measure against expected losses. Assess efficiency by comparing implementation cost against the benefit of risk reduction. Implement agreed measures through service design, infrastructure management, and change management |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 9 | Review and optimize continuity arrangements | Following actual recovery or major exercises, review findings and update strategies, plans, and controls. Analyse whether events not covered by plans should be added to scope. Review cost-effectiveness of existing measures. Propose improvements through continual improvement |
| 10 | Integrate continuity with partners and suppliers | Negotiate and agree service continuity requirements with partners and suppliers. Ensure third-party continuity arrangements align with the organization's plans. Involve partners in plan development, testing, and execution. Assess dependencies on cloud services and integrated digital services for continuity risks |

## Inputs
<!-- sources: ITIL 4 SCM §3.2.1–§3.2.5, §5.1, FitSM-2 §PR4 -->

| # | Input | Source |
|---|-------|--------|
| 1 | Service documentation and service models | Service design, service catalogue management |
| 2 | Risk assessment reports and risk register | Risk management |
| 3 | Financial data on loss of VBFs | Business stakeholders, financial management |
| 4 | Major incident reports | Incident management |
| 5 | Service level agreements with continuity requirements | Service level management |
| 6 | Regulatory requirements regarding continuity | Compliance, information security management |
| 7 | Consumer's continuity plans and business context | Relationship management, customers |
| 8 | CI data, service architecture, and dependency maps | Service configuration management, architecture management |
| 9 | Existing controls and resilience measures | Availability management, information security management |

## Outputs
<!-- sources: ITIL 4 SCM §3.2.1–§3.2.5, FitSM-2 §PR4 -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Service continuity policy, scope, and roles | All stakeholders |
| 2 | Business impact analysis reports | Management, service owners, risk management |
| 3 | Service continuity strategies | Service design, management |
| 4 | Service continuity plans (response, recovery, restore) | Recovery teams, crisis management |
| 5 | Awareness and exercise programme | Recovery teams, all staff |
| 6 | Exercise reports with findings and recommendations | Continual improvement, management |
| 7 | Recovery reports | Management, continual improvement |
| 8 | Requests for change (controls, infrastructure, plans) | Change management |
| 9 | Audit reports | Management, compliance |

## Roles
<!-- sources: ITIL 4 SCM §4.1 Table 4.2, §4.2, FitSM-3 §6.4 -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Service Continuity Manager | Manages the practice overall. Develops and maintains continuity policy, scope, and plans. Coordinates BIA with service owners. Develops continuity strategies and exercise programmes. Maintains plan documentation and version control. Produces exercise reports and coordinates audits. Requires methods and techniques expertise, documentation skills, understanding of recovery processes and technology, and knowledge of service architecture and interdependencies. Corresponds to ITIL continuity administrator and FitSM process manager SACM (continuity scope) | T2+ |
| Service Owner | Participates in BIA — identifies VBFs, analyses disruption consequences, and validates recovery requirements (RTO, RPO, minimum levels) for their services. Provides input to continuity strategies. Participates in exercises and post-recovery reviews. Requires good knowledge of the service consumer's business, service architecture and configuration, and professional competencies across PESTLE factors. Multiple service owners participate depending on scope | T2+ |
| Recovery Coordinator | Leads recovery teams during exercises and actual invocations. Coordinates response, recovery, and restoration activities at the tactical level. Ensures communication across teams and with stakeholders during recovery. Participates in plan development and testing. Requires coordination and communication skills, excellent knowledge of continuity plans, and understanding of the technology used in continuity strategies. Corresponds to FitSM case owner (continuity plan owner) | T2+ |

## Key Artefacts
<!-- sources: ITIL 4 SCM §2.2, §2.4, §3.2, FitSM-2 §PR4 -->

| Artefact | Purpose |
|----------|---------|
| Business Impact Analysis Report | Documents VBFs, disruption consequences (financial and reputational), VBF interdependencies, and recovery requirements (RTO, RPO, minimum target service levels) for each service within scope. Updated at least annually or when context changes |
| Service Continuity Plan | Action-oriented plan covering response, recovery, and restoration — at strategic, tactical, and operational levels. Includes crisis management contacts, invocation criteria, recovery procedures, communication procedures, escalation paths, and restoration instructions. Clear, concise, time-based, and regularly tested |
| Service Continuity Policy | Documents scope (services, sites, disaster definitions), roles and responsibilities, organizational structure for response and recovery, general approach, available resources, and limitations. Communicated to all stakeholders |
| Exercise Programme | Scheduled programme of exercises covering all parts of the practice at least annually. Specifies exercise types (walkthrough, table-top, command-post, live, test), scope, participants, and frequency — scaled to impact levels |
| Exercise and Recovery Report | Documents findings and recommendations from exercises and actual recovery events. Includes observations on team performance, plan effectiveness, identified gaps, and improvement recommendations |

## Process Interfaces
<!-- sources: ITIL 4 SCM §2.3, §3.2, §5.1, FitSM-2 §PR4 -->

| Interface | Relationship |
|-----------|-------------|
| Availability Management (PR06) | Closely related — both involve risk and service resilience. Availability focuses on high-probability, proactive prevention; continuity focuses on high-impact, reactive response. May be merged in some organizations |
| Risk Management (PR21) | Provides risk assessment information and risk register. Continuity management contributes risk-mitigation measures back to risk management |
| Incident Management (PR11) | Major incidents may escalate to disasters triggering invocation. Clear criteria distinguish incident management from continuity management. In small providers, continuity activities may be performed within major incident management |
| Service Level Management (PR02) | SLAs define continuity requirements (RTO, RPO targets). BIA validates whether SLA targets are achievable |
| Service Design (PR04) | Continuity solutions are designed as part of the service model. Continuity requirements inform design decisions |
| Change Management (PR15) | Risk mitigation measures and infrastructure resilience changes are implemented through change management |
| Service Configuration Management (PR17) | CI data and service dependency maps support BIA and VBF interdependency identification |
| Information Security Management (PR09) | Security controls contribute to continuity (physical security, data protection). Cyber attacks are a key disaster scenario |
| Supplier Management (PR23) | Partners and suppliers may provide continuity services and solutions. Third-party continuity arrangements must align with organizational plans |
| Monitoring & Event Management (PR14) | Monitoring provides prompt alerts for disaster detection. Monitoring data informs invocation decisions |
| Continual Improvement (PR24) | Exercise findings and recovery reports feed improvement initiatives |
| Relationship Management (PR22) | Consumer continuity plans must be aligned with service provider plans. Communication with customers during disasters is managed through relationship management |
