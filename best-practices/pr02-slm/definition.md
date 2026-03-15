---
process_id: PR02
process_name: "Service Level Management"
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
  - "ITIL 4: Service Level Management"
  - "FitSM-2: §PR2 SLM"
  - "IT4IT: R2F Service Level Component, Deploy & Release Value Streams"
last_updated: 2026-03-13
status: draft
---

# Service Level Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Service Level Management §2, FitSM-2 §PR2 -->

Service Level Management ensures that clear, business-relevant targets for service quality are established, agreed with customers and suppliers, and continually monitored. It maintains the service catalogue as the customer-facing view of available services, governs the full lifecycle of service level agreements (SLAs) and supporting agreements, and provides the feedback loop through which achieved service quality is measured against commitments — driving improvement where gaps are found.

## Scope
<!-- sources: ITIL 4 Service Level Management §2.1, FitSM-2 §PR2 -->

The process covers:

- Maintaining service catalogues that present available services and their attributes to customers
- Defining customer requirements for service quality, including both functional and non-functional aspects
- Negotiating, agreeing, and managing the lifecycle of SLAs between the service provider and customers
- Establishing and managing supporting agreements — Operational Level Agreements (OLAs) with internal teams and Underpinning Agreements (UAs) with external suppliers — that underpin SLA commitments
- Monitoring actual service quality against agreed targets using both technical data and stakeholder feedback
- Conducting periodic service reviews to assess service quality and identify improvement opportunities
- Producing service quality reports and dashboards for customers and internal stakeholders
- Initiating improvement actions when service levels are not met or when customer expectations evolve

## Key Concepts

### Service Quality Aspects
<!-- sources: ITIL 4 Service Level Management §2.3 -->

Service quality is multi-dimensional and should be assessed across several aspects rather than reduced to a single metric. The key quality aspects are:

| Aspect | Description |
|--------|-------------|
| **Functionality** | The extent to which the service provides the features and capabilities consumers need |
| **Availability** | The proportion of agreed service time during which the service is accessible and usable |
| **Performance** | The speed and responsiveness of the service (e.g., transaction response times, throughput) |
| **Timeliness** | The degree to which service actions (provisioning, changes, fixes) are completed within agreed timeframes |
| **User Support** | The quality and accessibility of support channels, including response times and resolution quality |
| **Accuracy** | The correctness and integrity of service outputs and data |
| **User Experience** | The overall ease of use, intuitiveness, and satisfaction experienced by consumers |

### Agreement Hierarchy
<!-- sources: FitSM-2 §PR2, ITIL 4 Service Level Management §2.2 -->

Service level commitments are structured in a tiered hierarchy:

- **Service Level Agreement (SLA):** A formal agreement between the service provider and a customer that documents agreed service targets, responsibilities, and remedies. SLAs may be tailored (negotiated per customer) or standardized (pre-defined service levels selected from a catalogue).
- **Operational Level Agreement (OLA):** An internal agreement between the service provider's teams specifying the operational targets each team must meet to support the SLA commitments.
- **Underpinning Agreement (UA):** A contract or agreement with an external supplier that underpins the service provider's ability to meet SLA commitments by securing specific operational targets from the supplier.

The hierarchy ensures that every customer-facing commitment in an SLA is supported by corresponding internal and supplier commitments.

### Service Catalogue
<!-- sources: FitSM-2 §PR2, IT4IT §8.1 Consume Function -->

The service catalogue is the customer-facing subset of the service portfolio. It presents available services in terms meaningful to consumers, including:

- What the service provides (description, features, service levels)
- How to request or subscribe to the service
- What service level options are available (standard or tailored)
- Who to contact for support

At advanced maturity, the service catalogue may be presented as a self-service portal where consumers can browse, compare, and order services directly.

### Tailored vs. Standardized Services
<!-- sources: ITIL 4 Service Level Management §3.2 -->

The SLM process varies significantly depending on the service delivery model:

- **Standardized (out-of-the-box):** Services with pre-defined service level options. Customers select from the catalogue. Requirements definition and viability analysis are largely automated. SLA negotiation is minimal — the customer accepts standard terms.
- **Tailored:** Services customized to individual customer needs. Requirements are gathered through direct engagement. Viability analysis involves manual assessment of feasibility and cost. SLAs are individually negotiated and may go through multiple iterations.

Most organizations maintain a mix of both models, with standardized services for common needs and tailored services for strategic or complex requirements.

### The Watermelon Effect
<!-- sources: ITIL 4 Service Level Management §2.3 -->

A common risk in service level management is the "watermelon effect" — where technical metrics appear green (targets met) on the outside, but the consumer's actual experience is red (dissatisfied) on the inside. This occurs when:

- SLA metrics are purely technical and do not reflect business-relevant outcomes
- User and customer feedback is not systematically collected alongside technical data
- Service reviews focus on metrics dashboards without engaging consumers

Effective SLM combats this by monitoring service quality from three perspectives: achieved service levels (technical data), user satisfaction (end-user feedback), and customer satisfaction (business sponsor assessment).

### Service Contract in the IT Value Chain
<!-- sources: IT4IT §8 R2F Service Level Component, §5.4 Deploy Value Stream -->

In the IT4IT reference architecture, service level commitments are represented as Service Contract data objects within the Service Level functional component. Service contracts are activated during service deployment (instrumenting metrics collection and KPI targets) and are accessible to consumers through the Consumption Experience portal. This provides end-to-end traceability from service design through deployment to ongoing service level monitoring.

## Activities

### Essential (All Tiers)

#### 1. Define the SLM Approach and Templates
<!-- sources: FitSM-2 §PR2 Initial Setup, ITIL 4 Service Level Management §2.1 -->

- Define the minimum structure, format, and content for service catalogues
- Create SLA, OLA, and UA templates covering all required fields (service description, targets, measurement methods, reporting, escalation, review schedule)
- Establish a basic or default SLA that applies to all services where no individual agreement exists
- Define the standard method for notifying customers of SLA violations

#### 2. Establish the Service Catalogue
<!-- sources: FitSM-2 §PR2 Initial Setup, IT4IT §5.5 Release Value Stream -->

- Create an initial service catalogue based on the information in the service portfolio
- Populate catalogue entries with service descriptions, available service level options, and ordering information
- Identify the most critical supporting service components and their delivery parties (internal teams, suppliers)
- Publish the catalogue to customers through agreed channels

#### 3. Define and Negotiate Service Level Agreements
<!-- sources: ITIL 4 Service Level Management §3.2.1, FitSM-2 §PR2 Ongoing Execution -->

- Gather customer requirements for service quality, including functional and non-functional expectations
- Assess the viability of requested service levels against available capabilities, resources, and supplier commitments
- Draft SLAs based on viability analysis, using existing service specifications and templates as building blocks
- Negotiate SLA terms with customers until mutually acceptable; iterate on the draft as needed
- Formalize agreed SLAs with sign-off from both parties

#### 4. Evaluate Agreement Fulfilment
<!-- sources: FitSM-2 §PR2 Ongoing Execution, ITIL 4 Service Level Management §3.2.2 -->

- Collect service performance data from monitoring systems, incident records, and service request fulfilment metrics
- Compare actual service levels against SLA, OLA, and UA targets for each reporting period
- Identify breaches and near-misses, documenting root causes where known
- Notify customers of SLA violations through the agreed notification method
- Escalate OLA/UA violations to the responsible internal team or supplier

#### 5. Manage Supporting Agreements
<!-- sources: FitSM-2 §PR2 Ongoing Execution -->

- Identify internal teams and external suppliers whose operational targets must underpin SLA commitments
- Define and negotiate OLAs with internal delivery teams
- Define and negotiate UAs with external suppliers, working with supplier management
- Evaluate OLA and UA fulfilment alongside SLA evaluation
- Review, update, or terminate supporting agreements as service requirements change

### Intermediate (T2+)

#### 6. Conduct Service Reviews
<!-- sources: ITIL 4 Service Level Management §3.2.2 -->

- Conduct periodic service reviews (interval-based, e.g., quarterly) covering achieved service levels, customer satisfaction, and improvement opportunities
- Conduct event-based reviews when triggered by significant incidents, customer complaints, policy changes, or organizational restructuring
- Involve relevant stakeholders: service owners, relationship managers, product owners, technical leads, and where appropriate, customers
- Produce internal reports documenting review findings, improvement initiatives, and any required SLA changes
- Feed service review findings into the SLA review and improvement processes

#### 7. Monitor Service Quality Continuously
<!-- sources: ITIL 4 Service Level Management §3.2.2 -->

- Collect ongoing service quality data from infrastructure monitoring, application monitoring, and user behaviour analytics
- Gather impromptu user feedback alongside scheduled satisfaction surveys
- Compare actual service quality against both SLA targets and informal service level expectations
- Publish service quality dashboards accessible to customers and internal stakeholders in agreed formats
- Identify trends — both positive and negative — that warrant proactive attention before formal reviews

#### 8. Manage Customer and User Satisfaction Surveys
<!-- sources: ITIL 4 Service Level Management §3.2.2 -->

- Design and conduct regular satisfaction surveys for both customers (business sponsors) and users (end users)
- Collect feedback on aspects of service quality that may not be captured by technical metrics (ease of use, communication quality, perceived value)
- Analyse survey results alongside technical service level data to identify gaps between measured and perceived quality (watermelon detection)
- Communicate survey findings to service owners and relationship managers for inclusion in service reviews

#### 9. Produce Service Quality Reports
<!-- sources: ITIL 4 Service Level Management §3.2.2, FitSM-2 §PR2 -->

- Produce regular service quality reports demonstrating achieved service levels, satisfaction scores, and improvement progress
- Tailor report content and format to the audience: technical detail for internal teams, business-focused summaries for customers
- Distribute reports through agreed channels and at agreed frequencies
- Ensure reports cover both quantitative metrics and qualitative feedback

### Advanced (T3)

#### 10. Implement End-to-End Service Level Monitoring
<!-- sources: IT4IT §5.4 Deploy Value Stream, ITIL 4 Service Level Management §5.2 -->

- Instrument service contracts at deployment time so that KPI targets are automatically monitored from the moment a service goes live
- Establish end-to-end service level monitoring that spans infrastructure, application, and business process layers
- Integrate service level data with configuration management to enable root-cause correlation across service components
- Implement real-time alerting for service level target breaches with automated escalation paths

#### 11. Automate SLA Lifecycle Management
<!-- sources: ITIL 4 Service Level Management §5.2, IT4IT §8.1 Consume Function -->

- Automate SLA drafting for standardized services using service portal integration and catalogue-driven workflows
- Implement automated viability checking that validates resource availability and supplier capacity against requested service levels
- Automate SLA expiry notifications, renewal workflows, and version control
- Provide self-service access for customers to review their service contracts, current service levels, and historical performance through a consumption experience portal

#### 12. Integrate Multi-Supplier Service Level Coordination
<!-- sources: SIAM concepts, IT4IT §8 R2F Functions -->

- Coordinate service levels across multiple suppliers through an integration layer that aggregates individual supplier performance into end-to-end service quality measures
- Establish service integration agreements that define how supplier contributions are measured, reported, and governed
- Track end-to-end SLA compliance where a single customer SLA depends on multiple underpinning OLAs and UAs from different suppliers
- Support cross-supplier service review meetings where improvement actions span organizational boundaries

## Process Interfaces

### Inputs From Other Processes

| Source Process | Input | Description |
|---------------|-------|-------------|
| PR01 Service Portfolio Management | Service portfolio and specifications | Portfolio entries and service specifications as a basis for creating catalogue entries and SLAs |
| PR06 Availability Management | Availability data and targets | Achieved availability levels and capacity for setting availability targets in SLAs |
| PR08 Capacity & Performance Management | Performance data and targets | Capacity and performance baselines for setting performance targets in SLAs |
| PR09 Information Security Management | Security requirements | Security targets and constraints that must be reflected in SLAs |
| PR10 Service Desk | User feedback and complaints | Real-time user sentiment and recurring issues that affect perceived service quality |
| PR11 Incident Management | Incident records | Incident volumes, resolution times, and impact data for SLA evaluation |
| PR14 Monitoring & Event Management | Monitoring data | Technical service quality measurements from infrastructure and application monitoring |
| PR22 Relationship Management | Customer requirements and feedback | Customer-specific service level requirements and feedback from service reviews |
| PR23 Supplier Management | Supplier capabilities and contracts | Supplier capacity and existing contract terms as a basis for defining OLAs and UAs |

### Outputs To Other Processes

| Target Process | Output | Description |
|----------------|--------|-------------|
| PR01 Service Portfolio Management | Service performance data | Achieved service levels compared against portfolio targets |
| PR06 Availability Management | Availability targets from SLAs | Agreed availability and continuity targets that drive availability planning |
| PR08 Capacity & Performance Management | Performance targets from SLAs | Agreed capacity and performance targets that drive capacity planning |
| PR09 Information Security Management | Security targets from SLAs | Agreed security targets that feed into security requirements |
| PR20 Measurement & Reporting | SLA targets and evaluation data | Agreed service targets and fulfilment data as the basis for service reports |
| PR22 Relationship Management | Service catalogue and SLAs | Catalogue of available services and agreed SLAs to support customer communication |
| PR23 Supplier Management | OLAs/UAs and performance reports | Supporting agreements and operational target reports for supplier evaluation |
| PR24 Continual Improvement | Improvement opportunities | Gaps between agreed and achieved service levels that feed the improvement register |

## Roles and Responsibilities
<!-- sources: ITIL 4 Service Level Management §4, FitSM-2 §PR2 -->

### Essential Roles

| Role | Responsibility |
|------|---------------|
| **Service Owner** | Accountable for end-to-end management of a specific service; ensures ongoing provision meets agreed requirements; translates customer needs into service designs and draft SLAs; conducts service reviews; negotiates SLAs |
| **Service Level Manager** | Manages the SLM process; maintains service catalogues and agreement registers; coordinates SLA negotiation, evaluation, and reporting; identifies improvement opportunities from service level data |

### Intermediate Roles (T2+)

| Role | Responsibility |
|------|---------------|
| **Relationship Manager** | Acts as the primary customer liaison; facilitates requirements gathering; participates in SLA negotiation and service reviews; communicates service performance to customers |
| **Service Designer** | Assesses viability of requested service levels; translates agreed targets into service designs; ensures service architecture supports agreed quality aspects |
| **Product Owner** | Monitors service quality from the product perspective; coordinates with technical teams on monitoring and improvement |

### Advanced Roles (T3)

| Role | Responsibility |
|------|---------------|
| **Service Quality Analyst** | Analyses service quality data across multiple dimensions; produces trend reports; identifies watermelon effects and systemic quality gaps |
| **Supplier Manager** | Negotiates and manages UAs; coordinates cross-supplier service level reviews; escalates supplier performance issues |
| **Account Manager** | Manages SLA lifecycle for key customer accounts; oversees SLA prolongation and renewal; handles commercial aspects of service agreements |

## Key Artefacts
<!-- sources: FitSM-2 §PR2, ITIL 4 Service Level Management §3, IT4IT §8 R2F -->

| Artefact | Maturity | Description |
|----------|----------|-------------|
| Service Catalogue | Essential | Customer-facing inventory of available services with descriptions, service level options, and ordering information |
| SLA Template | Essential | Standardized template for documenting service level agreements |
| Service Level Agreement (SLA) | Essential | Formal agreement with a customer documenting agreed service targets, measurement methods, responsibilities, and review schedule |
| Default SLA | Essential | Baseline agreement applied to all services where no individual SLA has been negotiated |
| OLA / UA | Essential | Supporting agreements with internal teams (OLA) and external suppliers (UA) that underpin SLA commitments |
| Service Level Requirements | Intermediate | Documented customer requirements for service quality, capturing both functional and non-functional expectations |
| Service Review Report | Intermediate | Formal record of service review outcomes including findings, improvement initiatives, and SLA change recommendations |
| Service Quality Dashboard | Advanced | Real-time or near-real-time view of service quality across all monitored services, integrating technical metrics and satisfaction data |
| Service Contract | Advanced | Digital representation of the SLA within the IT toolchain, linking agreed targets to automated monitoring and reporting |

## Automation and Tooling
<!-- sources: ITIL 4 Service Level Management §5.2 -->

| Activity | Tool Category | Automation Impact |
|----------|--------------|-------------------|
| Define customer requirements | Service catalogue and portals | Very high for standardized services |
| Viability analysis | CMDB, availability/capacity monitoring tools, asset management | Very high for standardized services |
| Draft SLA | Contracting tools, service portals | High for standardized services |
| SLA negotiation | Contracting tools, portals | Medium |
| SLA communication and enablement | Change tools, billing, communication tools, knowledge management | High for standardized, digitally delivered services |
| SLA review / prolongation / withdrawal | Document control tools | Low to medium |
| Customer and user satisfaction surveys | Survey tools, communication tools, social media analytics | Very high |
| Ongoing service quality monitoring | Infrastructure/application monitoring, dashboarding, advanced analytics, user portals | High |
| Service review | Reporting tools, contracting tools, portals | Low to medium |
| Service quality reporting | Reporting and dashboarding tools, portals, communication tools | Low to high depending on volume |

## Maturity Indicators
<!-- sources: synthesized from ITIL 4 Service Level Management, FitSM-2 §PR2, IT4IT §8 R2F -->

### Level 1 — Initial
- Services exist but no formal service catalogue is maintained
- SLAs are absent or informal (verbal agreements, emails)
- Service quality is not systematically measured or reported

### Level 2 — Managed
- A basic service catalogue exists covering the most important services
- A default SLA is in place; individual SLAs exist for critical services
- SLA fulfilment is evaluated periodically but primarily using technical metrics
- Customers are notified of major SLA violations

### Level 3 — Defined
- Complete service catalogue spanning all customer-facing services
- Formal SLA, OLA, and UA templates with standardized structures
- Regular service reviews incorporating both technical data and customer feedback
- Service quality reports produced and distributed to stakeholders on a defined schedule
- Roles (service level manager, service owner) are formally assigned

### Level 4 — Measured
- Service quality monitored across all seven quality aspects, not just availability and performance
- Customer and user satisfaction surveys conducted regularly and analysed alongside technical metrics
- Watermelon effects actively detected and addressed
- OLA and UA performance tracked with the same rigour as SLAs
- Service quality dashboards provide near-real-time visibility

### Level 5 — Optimized
- End-to-end service level monitoring integrated from deployment through operation
- SLA lifecycle management is largely automated for standardized services
- Multi-supplier service levels are coordinated through formal integration agreements
- Predictive analytics identify service quality trends before breaches occur
- Continuous improvement driven by integrated analysis of technical, user, and customer data
