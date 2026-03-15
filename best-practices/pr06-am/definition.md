---
process_id: PR06
process_name: "Availability Management"
category: definition
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
  - "ITIL 4: Availability Management §2–§6"
  - "FitSM-2: §PR4 SACM (availability scope)"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-13
status: draft
---

# Availability Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Availability Management §2.1, FitSM-2 §PR4 SACM Objective -->

Availability management ensures that services deliver the agreed levels of availability to meet the needs of customers and users. The practice ensures that requirements for service availability are understood, that availability is designed into services from the outset, that it is monitored and measured in a way that reflects business impact, and that availability risks are identified and treated through appropriate controls. The practice is applied throughout the product and service lifecycle — from ideation and design through to operations — and provides a centre of expertise for availability matters to support other service management practices.

## Scope
<!-- sources: ITIL 4 Availability Management §2.3, FitSM-2 §PR4 SACM -->

This process covers:

- Identifying and agreeing service availability requirements with customers
- Defining availability criteria — what constitutes unavailability for each service
- Selecting availability metrics that reflect the business impact of service disruptions
- Designing and configuring availability monitoring
- Monitoring, measuring, and reporting service availability against agreed targets
- Analysing availability data to identify trends, patterns, and improvement opportunities
- Identifying and treating availability risks — including single points of failure and unreliable components
- Planning and designing availability controls across all four dimensions of service management
- Continually optimizing availability controls for effectiveness and efficiency

This process does not cover: negotiating and agreeing SLAs (service level management), designing service models (service design), implementing infrastructure changes (infrastructure and platform management), monitoring infrastructure events (monitoring and event management), managing availability incidents (incident management), or managing the impacts of major disruptive events such as disasters (service continuity management). Almost every service management practice contributes to service availability directly or indirectly; this process provides the coordination, analysis, and expertise that ensures availability is managed as a coherent concern.

**Relationship to service continuity management (PR07):** Availability management and service continuity management address related but distinct concerns. Availability management focuses on high-probability risks, proactive prevention, reducing the likelihood of service failures, and optimizing availability within normal operations. Service continuity management focuses on high-impact risks (emergencies, disasters), reactive measures, reducing the impacts of major disruptive events, and creating redundancy for force-majeure situations. Availability management works with statistics and analyses trends; continuity management is concerned with how to respond to disruptive events.

## Key Concepts
<!-- sources: ITIL 4 Availability Management §2.2 -->

### 1. Availability
<!-- sources: ITIL 4 Availability Management §2.1 -->
The ability of an IT service or other configuration item to perform its agreed function when required. Availability depends on how frequently a service fails (measured by MTBF) and how quickly it recovers after a failure (measured by MTRS). In practice, availability is a complex characteristic that depends on service architecture, the importance of specific service components or actions, the criteria for what constitutes unavailability, service hours, and other parameters. Availability from a user perspective can differ from availability measured at the provider or customer level.

### 2. Vital Business Function
<!-- sources: ITIL 4 Availability Management §2.2.1 -->
A vital business function (VBF) is the part of a service that is critical to the organization's success. A service may also support business functions that are not vital. The distinction is important because it influences availability design and the associated costs — the more vital the business function, the more resilient and available it needs to be. Identifying VBFs is essential for focusing availability investment where it matters most.

### 3. Mean Time Between Failures (MTBF)
<!-- sources: ITIL 4 Availability Management §2.1, §2.2.4 -->
A measure of how frequently a service fails. A higher MTBF indicates greater reliability. MTBF is one of the key availability metrics that reflects the frequency of service disruptions rather than just the total uptime percentage.

### 4. Mean Time to Restore Service (MTRS)
<!-- sources: ITIL 4 Availability Management §2.1, §2.2.4 -->
A measure of how quickly a service is restored after a failure. A lower MTRS indicates faster recovery. Together with MTBF, MTRS determines the overall availability of a service. Services designed for high availability balance high MTBF with short MTRS.

### 5. Availability Criteria
<!-- sources: ITIL 4 Availability Management §2.2.3, §2.4.1.2 -->
The agreed conditions under which a service is considered unavailable. Defining availability criteria is often complicated because a service may have multiple functions and customers with different requirements. Factors to consider include: the criticality of business functions enabled by the service, thresholds for underperformance versus unavailability, the number and type of users impacted, whether vital users or sites are affected, and the service delivery schedule and peak hours. These criteria should be documented in the SLA.

### 6. Availability Metrics
<!-- sources: ITIL 4 Availability Management §2.2.4, §2.4.2 -->
The measures used to quantify and report service availability. The most common metric is the availability percentage: (agreed service time − downtime) / agreed service time. However, this formula does not reflect the business impact of complicated service disruption scenarios. Additional metrics include MTBF, minimum time between failures, number of service disruptions, total downtime, maximum single outage, and MTRS. Whatever metrics are selected, they should reflect the business impact of service disruptions rather than the technical availability of service components.

### 7. Availability Measurement Methods
<!-- sources: ITIL 4 Availability Management §2.2.5, Table 2.1 -->
Three principal methods for measuring availability: (1) **Incident records** — tracking outage duration from incident timestamps, reliable for small-scale providers but limited by detection and recording delays; (2) **IT infrastructure monitoring** — tools measure component availability which can be translated to service availability through service models, but component outages do not always cause service outages; (3) **Business transaction monitoring and real user monitoring** — measures availability from the business operations perspective, including synthetic monitoring (simulated transactions) and real user monitoring (capturing actual end-user experience). The choice of method depends on the type of service, the scale of the user base, and the availability of monitoring tools.

### 8. Single Point of Failure
<!-- sources: ITIL 4 Availability Management §2.3.2, §2.4.3 -->
A component or element whose failure would cause a service failure because there is no redundancy or alternative. Availability management focuses on identifying and eliminating single points of failure where it is cost-justifiable. Countermeasures include fault-tolerant technology, duplexing (alternative infrastructure components), improved component reliability, and resilient network design.

### 9. Service Health Model
<!-- sources: ITIL 4 Availability Management §2.2.5, Table 2.1 -->
A model that determines how the underperformance or outage of a service component impacts other components and the service as a whole. Service health models enable more accurate measurement of service-level availability from infrastructure monitoring data. Developing such models is resource-intensive and must be maintained as infrastructure changes — they are most valuable for critical, complex services.

## Activities
<!-- sources: ITIL 4 Availability Management §3.2.1, §3.2.2, FitSM-2 §PR4 SACM -->

### Essential (All tiers)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Identify service availability requirements | Derive availability requirements from SLAs, customer needs, and business impact analysis. Identify the vital business functions supported by each service. Work with the service level management and business analysis practices to clarify what availability means for each service and its consumers. Document the requirements in a form that enables monitoring and reporting |
| 2 | Agree service availability requirements | Analyse whether the identified availability requirements are achievable and affordable given available resources, technology, and supplier capabilities. Negotiate with customers to balance availability levels with cost. The main output is an agreement on availability targets with estimated costs and timelines for fulfilment |
| 3 | Determine availability monitoring approach | Define how service outages will be tracked and recorded on an ongoing basis. Configure monitoring to collect availability data aligned with the agreed metrics and criteria. The monitoring approach may range from incident-record-based tracking to automated infrastructure monitoring to real user monitoring, depending on the service type and organizational capability |
| 4 | Monitor service availability | Collect availability data from the configured monitoring sources. Track downtime periods, service disruptions, and restoration times. Ensure that monitoring data is aligned with the agreed availability criteria — not all incidents are availability incidents, and not all component outages cause service unavailability |
| 5 | Report service availability | Produce reports or dashboards showing service availability achievements against agreed targets. Communicate results through agreed channels. Service availability reporting is usually part of overall service quality reporting through the service level management practice |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 6 | Define availability criteria and select metrics | Establish formal criteria for what constitutes service unavailability — considering business function criticality, underperformance thresholds, user impact scope, vital user groups, and service schedules. Select availability metrics that reflect the business impact of service disruptions, going beyond simple uptime percentage to include MTBF, MTRS, number of disruptions, maximum single outage, and total downtime |
| 7 | Design availability reports and dashboards | Design report templates and dashboards that present availability data meaningfully to different stakeholders — from technical teams to service owners to customers. Ensure reports reflect business impact rather than just technical component status |
| 8 | Analyse service availability | Perform trend analysis on availability data to detect patterns and flaws that have not yet caused incidents. Investigate all deviations from agreed availability levels and undertake corrective action. Analysis may be performed at the service component level (by technical specialists) and at the service level (by the availability manager and service owner). Log problems or risks identified through analysis. Consider inputs from service continuity BIAs and risk assessments |
| 9 | Plan and design availability controls | Assess availability risks, identify single points of failure and unreliable components, and design countermeasures across all four dimensions of service management. Produce availability management plans covering current availability levels, key service components, anticipated requirement changes, and recommended controls. Ensure that new or changed services meet customer availability requirements. More preventive measures should be adopted for services with earlier and higher business impacts |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 10 | Assess effectiveness and efficiency of availability controls | Evaluate existing availability controls using cost-benefit analysis. Assess effectiveness by comparing the risk reduction achieved against the expected losses due to incidents. Assess efficiency by comparing the cost of controls against their benefits. Consider all forms of loss: productivity, response costs, replacement costs, SLA fines, competitive advantage, and reputation. Optimize the portfolio of availability controls to achieve maximum availability with available resources |
| 11 | Develop and maintain service health models | Create models that determine how component underperformance or outage impacts other components and the overall service. Service health models enable more accurate service-level availability measurement from infrastructure monitoring data and support proactive availability planning. Maintain models as infrastructure and services change |

## Inputs
<!-- sources: ITIL 4 Availability Management §3.2.1, §3.2.2, FitSM-2 §PR4 SACM -->

| # | Input | Source |
|---|-------|--------|
| 1 | Customer requirements and business needs | Customers, business analysis |
| 2 | Service level requirements and SLAs | Service level management |
| 3 | Service models and configuration information (CMDB) | Service configuration management |
| 4 | Monitoring data (infrastructure, application, real user) | Monitoring & event management |
| 5 | Incident records | Incident management |
| 6 | Risk register and risk assessment data | Risk management |
| 7 | Information about available resources and technology | Infrastructure & platform management |
| 8 | Service specifications and architecture information | Service design, architecture management |
| 9 | Regulatory requirements regarding service availability | Governance, compliance |

## Outputs
<!-- sources: ITIL 4 Availability Management §3.2.1, §3.2.2, FitSM-2 §PR4 SACM -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Agreed service availability requirements | Service level management (for SLA inclusion) |
| 2 | Availability monitoring requirements and configuration | Monitoring & event management |
| 3 | Service availability reports and dashboards | Service level management, customers, management |
| 4 | Availability management plans | Service design, change management |
| 5 | New and updated availability controls | Change management (for implementation) |
| 6 | Problem records (from availability analysis) | Problem management |
| 7 | Availability report templates | Service level management, measurement & reporting |
| 8 | Improvement initiatives | Continual improvement |
| 9 | Requests for change | Change management |

## Roles
<!-- sources: ITIL 4 Availability Management §4.1, §4.2, Table 4.2, Table 4.3 -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Availability Manager | Accountable for ensuring cost-efficient availability management across services. Analyses availability data, designs metrics and reports, plans and designs availability controls, and drives practice improvement. This role may be combined with the service continuity administrator or IT risk manager role. In smaller organizations, availability management responsibilities may be performed by the service owner | All |
| Service Owner | Provides the service-level perspective on availability requirements and achievements. Participates in identifying and agreeing availability requirements, reporting availability to customers, and reviewing availability performance. May perform availability management activities as part of service-level reporting in smaller organizations | All |
| Technical Specialist | Provides technical expertise on monitoring tools, infrastructure, and availability controls. Performs availability analysis at the service component and infrastructure level. Configures monitoring, implements availability controls, and advises on fault-tolerant technologies and resilience measures. Includes system administrators, infrastructure engineers, and monitoring tool administrators | All |

## Key Artefacts
<!-- sources: ITIL 4 Availability Management §3.2, §5, FitSM-2 §PR4 SACM -->

| Artefact | Purpose |
|----------|---------|
| Availability Requirements Document | Documents the agreed availability requirements for each service — VBFs, availability criteria, metrics, targets, and monitoring approach. May be incorporated into the SLA |
| Service Availability Report | Periodic report showing availability achievements against agreed targets — including availability percentage, MTBF, MTRS, number of disruptions, total downtime, and maximum single outage |
| Availability Management Plan | Documents current availability levels, key service components, anticipated requirement changes, availability risks, and recommended controls with implementation timelines |
| Availability Report Template | Standardized template or dashboard design for presenting availability data to different stakeholder groups |
| Service Health Model | Model mapping how component availability impacts service availability — enabling accurate service-level measurement from infrastructure monitoring data (T3) |

## Process Interfaces
<!-- sources: ITIL 4 Availability Management §2.3 Table 2.2, §3, §4.2 Table 4.3, FitSM-2 §PR4 SACM Key Interfaces -->

| Interface | Relationship |
|-----------|-------------|
| Service Level Management (PR02) | Availability requirements are derived from SLAs. Availability reporting feeds SLA achievement reporting. The availability management practice provides input and expertise to SLM during service level negotiation |
| Service Continuity Management (PR07) | Related but distinct concerns — availability focuses on high-probability/proactive/optimization; continuity focuses on high-impact/reactive/redundancy. Both practices share VBF identification, BIA, and risk assessment. Inputs from continuity BIAs and risk assessments inform availability planning |
| Risk Management (PR21) | Risk information supports availability planning. Availability controls are a major category of risk mitigation measures. The availability management practice contributes significantly to risk management |
| Change Management (PR15) | Change impact analysis includes availability impact assessment. Availability controls are implemented through authorized changes. The change schedule is consulted when planning availability improvements |
| Incident Management (PR11) | Incident records provide availability data. Availability analysis may identify patterns that feed incident management. The practice reacts to events that threaten availability targets |
| Monitoring & Event Management (PR14) | Monitoring tools provide infrastructure and application availability data. Availability management defines monitoring requirements and helps translate monitoring data into meaningful service availability information |
| Capacity & Performance Management (PR08) | Related service quality concerns — availability, capacity, and performance affect the same CIs and services. The practices benefit from sharing resources and information but require clear separation of responsibilities |
| Information Security Management (PR09) | Related service quality concerns. Security incidents can cause availability incidents. Security controls and availability controls must be coordinated |
| Service Design (PR04) | Availability controls are designed as part of the service model. It is usually cheaper to design the right level of availability from the start than to add it later |
| Service Configuration Management (PR17) | Service models and CI data from the CMDB support availability analysis and the development of service health models |
| Problem Management (PR13) | Availability trend analysis may identify problems. Problem resolutions may require availability control improvements |
| Continual Improvement (PR24) | Improvement initiatives from availability analysis feed the continual improvement register. Availability optimization is tracked as improvement work |
| Supplier Management (PR23) | Availability requirements must be negotiated and agreed with suppliers. Suppliers may provide resilience technologies and services (fault tolerance, clustering, backup systems) |
| Measurement & Reporting (PR20) | Availability reporting contributes to overall service quality reporting. The measurement and reporting practice may provide tools and templates for availability dashboards |
| Service Catalogue Management (PR05) | Service availability information is published in the service catalogue to inform customer expectations and support service selection |
| Architecture Management | Availability controls are aligned with the organization's architecture. Architecture decisions affect availability levels and constraints |
