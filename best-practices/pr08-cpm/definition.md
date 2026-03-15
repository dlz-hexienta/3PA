---
process_id: PR08
process_name: "Capacity & Performance Management"
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
  - "ITIL 4: Capacity & Performance Management §2–§6"
  - "FitSM-2: §PR5 CAPM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Capacity & Performance Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Capacity & Performance Management §2.1, FitSM-2 §PR5 CAPM Objective -->

Capacity and performance management ensures that services achieve the agreed and expected levels of performance and satisfy current and future demand in a cost-effective way. The practice covers the performance of services and the performance of the resources that support them — infrastructure, applications, and third-party services. It ensures that capacity and performance requirements are understood, that services are designed and provisioned to meet those requirements, that performance is monitored and measured in terms meaningful to the business, and that capacity risks are identified and treated through appropriate controls and planning. The practice is applied throughout the product and service lifecycle — from ideation and design through to operations — and provides a centre of expertise for capacity and performance matters to support other service management practices.

## Scope
<!-- sources: ITIL 4 Capacity & Performance Management §2.3, FitSM-2 §PR5 CAPM -->

This process covers:

- Identifying and agreeing service capacity and performance requirements with customers
- Defining performance criteria — what constitutes acceptable performance, degradation, and unavailability
- Selecting capacity and performance metrics that reflect business impact
- Designing and configuring capacity and performance monitoring
- Monitoring, measuring, and reporting service capacity and performance against agreed targets
- Analysing capacity and performance data to identify trends, constraints, and improvement opportunities
- Identifying and treating capacity and performance risks
- Planning capacity to meet current and future demand — producing and maintaining capacity plans
- Continually optimizing capacity and performance controls for effectiveness and efficiency

This process does not cover: negotiating and agreeing SLAs (service level management), designing service models (service design), aligning with business architecture (architecture management), monitoring infrastructure events (monitoring and event management), managing performance-related incidents (incident management), or implementing infrastructure changes (infrastructure and platform management). Many practices contribute directly or indirectly to service performance; this process provides the coordination, analysis, and expertise that ensures capacity and performance are managed as a coherent concern.

**Relationship to availability management (PR06):** Capacity and performance management and availability management address related but distinct quality aspects of the same services and components. Performance focuses on the rate and speed of service transactions under varying demand; availability focuses on whether the service is functioning at all. A service that is available but performing poorly may breach performance targets while meeting availability targets. The practices benefit from sharing resources and information but require clear separation of responsibilities, particularly in regulated areas.

## Key Concepts
<!-- sources: ITIL 4 Capacity & Performance Management §2.2, FitSM-2 §PR5 CAPM -->

### 1. Performance
<!-- sources: ITIL 4 Capacity & Performance Management §2.2 -->
A measure of what is achieved or delivered by a system, person, team, practice, or service. Service performance is usually associated with the rate of service transactions and the time needed to fulfil them at a given level of demand. Performance depends on service capacity and varies with demand. Specific metrics depend on the technology and business nature of the service — they may include response times, transaction throughput, processing speed, and queue lengths.

### 2. Service Capacity
<!-- sources: ITIL 4 Capacity & Performance Management §2.2 -->
The maximum throughput that a configuration item or service can deliver. Service performance depends on service capacity — when demand approaches or exceeds capacity, performance degrades. Capacity may relate to computing power, storage, network bandwidth, staff numbers, or any other resource that constrains throughput. Understanding the relationship between capacity and performance is essential for effective service design and planning.

### 3. Capacity and Performance Criteria
<!-- sources: ITIL 4 Capacity & Performance Management §2.4.1 -->
The agreed conditions that define acceptable performance, degradation, and unavailability for a service. Factors to consider include: the vital business functions and critical service actions, acceptable versus unacceptable delays in executing service transactions, and the scale factor — whether degradation is experienced by significant numbers of users or by individuals. The line between acceptable performance variation and reportable degradation should be clearly defined. Performance criteria should be documented in SLAs.

### 4. Component versus Service Performance
<!-- sources: ITIL 4 Capacity & Performance Management §2.2, §2.4.2 -->
A critical distinction exists between the technical performance of individual service components and the end-to-end performance experienced by users. Infrastructure monitoring provides component-level metrics (CPU utilization, memory usage, network throughput) but it is difficult to accurately measure service transaction performance from infrastructure data alone. Tools such as real user monitoring and business transaction monitoring provide a more accurate picture of the user experience. Capacity and performance metrics should reflect the business impact of service degradation, not just the technical performance of components.

### 5. Business Activity Patterns and Demand Forecasting
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.1 Table 3.2 -->
Business activity patterns describe how demand for services varies over time — including seasonal variations, growth trends, campaign-driven spikes, and cyclical workload patterns. Understanding these patterns is essential for capacity planning. Transaction volumes and forecasts inform both the immediate capacity provisioning and the longer-term architectural decisions. Short-term demand spikes (such as marketing campaign traffic) may be handled through automated scaling, while sustained growth requires architectural planning.

### 6. Capacity Plan
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.2, FitSM-2 §PR5 CAPM -->
A document covering current capacity and performance levels, anticipated changes in demand, planned upgrades or downgrades of resources, and recommended actions to ensure services continue to meet their performance targets. Capacity plans translate business demand forecasts into resource requirements and investment decisions. They may cover individual services, service groups, or the entire infrastructure, and typically include short-term, medium-term, and long-term perspectives.

### 7. Automated Scaling and Load Balancing
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.1 Table 3.2 (cloud scenario), §3.2.2 Table 3.4 -->
In cloud and modern infrastructure environments, capacity can be adjusted dynamically in response to demand through automated scaling and load balancing tools. These capabilities allow the organization to respond to short-term demand variations without manual intervention. However, automated linear scaling is not always the most cost-effective approach — at certain demand thresholds, it may be more prudent to alter the underlying architecture than to continue scaling linearly. Capacity practitioners should evaluate when architectural changes are more efficient than incremental scaling.

### 8. Service Integration for Performance
<!-- sources: ITIL 4 Capacity & Performance Management §6 -->
In multi-vendor environments where multiple external service providers are responsible for different service components, end-to-end service performance can be overlooked. A service integration function should maintain the end-user focus of all performance management efforts by coordinating across providers. Service providers should be incentivized to communicate performance issues to a centralized entity to support rapid coordination. Capacity practitioners should understand modern IT infrastructure architectures and suggest alternative designs when multi-vendor arrangements create performance bottlenecks.

## Activities
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.1, §3.2.2, FitSM-2 §PR5 CAPM -->

### Essential (All tiers)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Identify service capacity and performance requirements | Derive performance and capacity requirements from customer needs, SLAs, and business activity patterns. Identify the critical service actions and vital business functions that define performance priorities. Determine the transaction volumes, throughput requirements, and growth forecasts that drive capacity needs. Document requirements in a form that enables monitoring and reporting |
| 2 | Agree service capacity and performance requirements | Analyse whether the identified requirements are achievable and affordable given available resources, technology, and supplier capabilities. Determine estimated costs for different capacity and performance options. The capacity and performance management practice supports SLM with service component expertise during SLA negotiations, helping to balance the cost-benefit ratio of different performance levels |
| 3 | Determine capacity and performance monitoring approach | Define how service performance and capacity utilization will be monitored and recorded. Select appropriate monitoring methods based on the service type and available tools. Define thresholds and alerts for performance degradation and capacity exhaustion. In cloud environments, design automated capacity adjustment triggers |
| 4 | Monitor service capacity and performance | Collect capacity and performance data from monitoring tools, including infrastructure metrics, application performance data, and where available, real user monitoring. Track performance against agreed targets and capacity utilization against thresholds. Respond when capacity thresholds are exceeded |
| 5 | Report service capacity and performance | Produce reports or dashboards showing capacity and performance achievements against agreed targets. Focus reporting on the customer's business processes and user experience rather than technical component metrics alone. Communicate results through agreed channels as part of overall service quality reporting |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 6 | Define capacity and performance criteria and metrics | Establish formal criteria for what constitutes acceptable performance, degradation, and unavailability — considering critical service actions, acceptable delays, and the scale of user impact. Select metrics that reflect the business impact of service degradation, going beyond component-level technical indicators to include service transaction response times, throughput rates, and user-experienced performance |
| 7 | Design capacity and performance reports and dashboards | Design report templates and dashboards that present capacity and performance data meaningfully to different stakeholders. Ensure reports focus on the consumer experience of service productivity, responsiveness, and capacity, with technical indicators supporting rather than replacing the business-level view |
| 8 | Analyse service capacity and performance | Perform trend analysis on capacity utilization and performance data. Analyse business activity patterns to forecast future demand. Identify constraints, bottlenecks, and components approaching capacity limits. Investigate performance deviations and identify root causes. Consider whether current service architecture remains appropriate for the evolving demand profile |
| 9 | Plan and design capacity and performance controls | Produce capacity plans covering current levels, anticipated demand changes, and recommended resource actions. Assess the impacts of components' capacity and performance on end-to-end service performance. Design controls and countermeasures to prevent, detect, and mitigate capacity and performance risks. Recommend architectural changes where linear scaling is no longer cost-effective |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 10 | Optimize capacity and performance controls | Evaluate existing capacity and performance controls for effectiveness and efficiency. Compare the cost of controls (including over-provisioning) against the expected losses from performance degradation. Identify opportunities to reduce waste while maintaining required performance levels. Suggest alternative architectural arrangements that improve performance at lower cost |
| 11 | Model and forecast capacity demand | Develop capacity models that relate business demand forecasts to resource requirements across all service components. Model the performance impact of different architectural options and scaling strategies. Produce long-term capacity forecasts that inform IT budget planning and strategic investment decisions |

## Inputs
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.1, §3.2.2, FitSM-2 §PR5 CAPM -->

| # | Input | Source |
|---|-------|--------|
| 1 | Customer requirements and business needs | Customers, business analysis |
| 2 | Service level requirements and SLAs | Service level management |
| 3 | Business activity patterns, transaction volumes, and demand forecasts | Business analysis, customers |
| 4 | Service component specifications and manufacturer requirements | Suppliers, infrastructure management |
| 5 | Service models and configuration information (CMDB) | Service configuration management |
| 6 | Monitoring data (infrastructure, application, real user) | Monitoring & event management |
| 7 | Incident and problem records related to performance | Incident management, problem management |
| 8 | Change schedule | Change management |
| 9 | Information about available resources and constraints | Infrastructure & platform management, financial management |

## Outputs
<!-- sources: ITIL 4 Capacity & Performance Management §3.2.1, §3.2.2, FitSM-2 §PR5 CAPM -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Agreed capacity and performance requirements | Service level management (for SLA inclusion) |
| 2 | Capacity and performance monitoring requirements and configuration | Monitoring & event management |
| 3 | Service capacity and performance reports and dashboards | Service level management, customers, management |
| 4 | Capacity plans | Service design, change management, financial management |
| 5 | New and updated capacity and performance controls | Change management (for implementation) |
| 6 | Improvement initiatives | Continual improvement |
| 7 | Requests for change | Change management |
| 8 | Service design and architecture recommendations | Service design, architecture management |
| 9 | IT budget planning updates | Financial management |

## Roles
<!-- sources: ITIL 4 Capacity & Performance Management §4.1 Table 4.2, §4.2 -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Capacity & Performance Manager | Accountable for ensuring cost-efficient service capacity and sufficient performance levels across services. Analyses capacity and performance data, designs metrics and reports, produces capacity plans, and drives practice improvement. This role requires strong business and technical knowledge, combined with communication and advocacy skills. In smaller organizations, responsibilities may be performed by the service owner or combined with the availability manager role | All |
| Service Owner | Provides the service-level perspective on capacity and performance requirements and achievements. Participates in identifying and agreeing requirements, reporting performance to customers, and reviewing capacity plans. May perform capacity management activities as part of service-level reporting in smaller organizations | All |
| Technical Specialist | Provides technical expertise on infrastructure, applications, monitoring tools, and capacity technologies. Performs component-level capacity and performance analysis, configures monitoring, implements capacity controls, and advises on scaling and architectural options. Includes system administrators, infrastructure engineers, cloud architects, and monitoring tool administrators | All |

## Key Artefacts
<!-- sources: ITIL 4 Capacity & Performance Management §3.2, §5, FitSM-2 §PR5 CAPM -->

| Artefact | Purpose |
|----------|---------|
| Capacity and Performance Requirements Document | Documents the agreed capacity and performance requirements for each service — critical service actions, performance criteria, metrics, targets, and monitoring approach. May be incorporated into the SLA |
| Service Capacity and Performance Report | Periodic report showing capacity utilization and performance achievements against agreed targets — including response times, throughput rates, capacity headroom, and trend data |
| Capacity Plan | Documents current capacity levels, demand forecasts, planned resource changes (upgrades, downgrades, reallocations), and recommended actions with timelines and costs |
| Capacity and Performance Report Template | Standardized template or dashboard design for presenting capacity and performance data to different stakeholder groups |
| Performance Baselines | Documented baseline measurements of service and component performance under defined conditions, used as reference points for trend analysis and capacity planning |

## Process Interfaces
<!-- sources: ITIL 4 Capacity & Performance Management §2.3 Table 2.1, §3, §4.2, FitSM-2 §PR5 CAPM Key Interfaces -->

| Interface | Relationship |
|-----------|-------------|
| Service Level Management (PR02) | Capacity and performance requirements are derived from SLAs. Performance reporting feeds SLA achievement reporting. The capacity and performance management practice provides expertise to SLM during service level negotiation |
| Availability Management (PR06) | Related but distinct service quality concerns — capacity/performance focuses on throughput and speed; availability focuses on whether the service functions at all. The practices share resources, monitoring data, and information but require clear separation of responsibilities |
| Service Continuity Management (PR07) | Continuity requirements may include minimum capacity levels for recovery scenarios. Capacity constraints affect recovery time objectives |
| Risk Management (PR21) | Risk information supports capacity planning. Capacity and performance controls contribute to risk mitigation |
| Change Management (PR15) | Change impact analysis includes capacity and performance assessment. Capacity controls are implemented through authorized changes. The change schedule informs capacity planning |
| Incident Management (PR11) | Performance-related incidents provide data for capacity analysis. Capacity constraints may contribute to incidents |
| Monitoring & Event Management (PR14) | Monitoring tools provide capacity utilization and performance data. Capacity management defines monitoring requirements, thresholds, and alerts |
| Service Design (PR04) | Capacity and performance controls are designed as part of the service model. The practice provides input on performance-optimal architectures and resource requirements |
| Service Configuration Management (PR17) | Service models and CI data from the CMDB support capacity analysis and the assessment of component impact on end-to-end performance |
| Problem Management (PR13) | Capacity analysis may identify underlying problems causing performance degradation. Problem resolutions may require capacity improvements |
| Continual Improvement (PR24) | Improvement initiatives from capacity analysis feed the continual improvement register. Capacity optimization is tracked as improvement work |
| Supplier Management (PR23) | Capacity requirements must be agreed with suppliers for third-party components and services. In multi-vendor environments, service integration for performance coordination is essential |
| Architecture Management | Capacity practitioners recommend architectural changes when demand patterns require alternatives to linear scaling. Architecture decisions affect capacity and performance levels |
| Financial Management (PR03) | Capacity plans inform IT budget planning. Cost-benefit analysis of capacity options supports investment decisions |
| Service Catalogue Management (PR05) | Service performance information is published in the service catalogue to inform customer expectations |
| Measurement & Reporting (PR20) | Capacity and performance reporting contributes to overall service quality reporting. The measurement and reporting practice may provide tools and templates |
