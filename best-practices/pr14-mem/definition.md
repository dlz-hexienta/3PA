---
process_id: PR14
process_name: "Monitoring & Event Management"
category: definition
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Monitoring & Event Management §2–§6"
  - "FitSM-1: §PR4.4, §PR5.4, §PR6.4 (distributed monitoring)"
  - "IT4IT: D2C Value Stream"
last_updated: 2026-03-14
status: draft
---

# Monitoring & Event Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 MEM §2.1 -->

The purpose of the monitoring and event management practice is to systematically observe services and service components, record and report selected changes of state identified as events, and establish the appropriate response to those events — including responding to conditions that could lead to potential faults or incidents. The practice has two complementary parts: monitoring focuses on services and configuration items to detect conditions of potential significance, track and record state, and provide this information to relevant parties; event management focuses on those monitored changes of state defined by the organization as events, determining their significance, and identifying and initiating the correct response. Information about events is recorded, stored, and provided to relevant parties. The practice provides critical input to incident management, problem management, information security management, availability management, capacity and performance management, change management, and risk management.

## Scope
<!-- sources: ITIL 4 MEM §2.3 -->

This process covers:

- Identifying and optimizing the scope of monitoring — determining which services, systems, configuration items, and other service components to observe
- Implementing and maintaining continuous monitoring — using active and passive monitoring techniques across infrastructure, applications, and services
- Establishing and maintaining event identification, categorization, and processing rules — including thresholds, correlation rules, and response procedures
- Implementing processes and automation to operationalize the defined event management rules
- Ongoing processing of events according to agreed and implemented rules and processes
- Providing information about the current and historical state of monitored services and resources to relevant stakeholders in agreed forms

This process does not cover: management of incidents (incident management), investigation of causes of events and trends (problem management), management of changes in response to events (change management), communications with users (service desk), support for decision-making based on monitoring data (measurement and reporting), setting targets and thresholds for service quality and performance (service level management, availability management, capacity and performance management, information security management, service continuity management), setting thresholds for infrastructure and application components (infrastructure and platform management, software development), setting targets and thresholds for third-party services (supplier management).

## Key Concepts
<!-- sources: ITIL 4 MEM §2.2 -->

### 1. Monitoring
<!-- sources: ITIL 4 MEM §2.2, FitSM-1 §PR4.4, §PR5.4 -->
Repeated observation of a system, practice, process, service, or other entity to detect events and to ensure that the current status is known. Monitoring has two dimensions: active monitoring interrogates service components by polling — requesting information from CIs on a schedule — while passive monitoring collects notifications sent automatically by CIs when certain conditions are met. Passive monitoring detects events immediately but relies on CIs having built-in notification capabilities; active monitoring can identify trends earlier but may delay event detection depending on polling intervals. Monitoring also has a proactive/reactive dimension: reactive monitoring responds to events that have already occurred, while proactive monitoring takes action based on pattern analysis of past events to prevent future adverse events. Although traditionally focused on technology components, monitoring scope can extend to processes, people, and supplier performance. Monitoring is necessary for event management, but not all monitoring results in event detection — thresholds and classification rules determine which changes of state become events.

### 2. Events and Event Types
<!-- sources: ITIL 4 MEM §2.1, §2.2 -->
An event is any change of state that has significance for the management of a service or other configuration item. Not all events have the same significance or require the same response. Events are classified into three types of increasing significance: informational events signify regular operation and do not require action (examples: user login, scheduled operation completed) — they are stored in logs and may be published on status dashboards; warning events signify unusual but not exceptional operation and allow action before negative impact occurs (examples: scheduled backup not running, resource utilization approaching threshold) — they notify appropriate teams to take preventive action; exception events indicate that a critical threshold has been reached and may signify service failure, performance degradation, or loss of functionality (examples: server down, unauthorized software detected, backup failed) — they require immediate action and are the mechanism by which incidents are detected through monitoring. A standard classification scheme enables consistent handling, appropriate notification routing, and efficient resource utilization.

### 3. Thresholds and Alerts
<!-- sources: ITIL 4 MEM §2.2, FitSM-1 §PR5.4 -->
A threshold is the value of a metric that triggers a predefined response — such as creating an alert or notification, creating an incident record, changing the status of a previously recorded alert, or initiating a reactive action. Threshold values should be defined with care to prevent too many responses overwhelming operational resources. Thresholds are typically combined with other rules for processing measurement data — including event correlation rules and engines. An alert is a notification that a threshold has been reached, something has changed, or a failure has occurred. Alerting systems must be highly reliable, flexible enough to notify operators through multiple media, and capable of generating detailed, actionable notification messages. Over-alerting — where more alerts are generated than the organization can process — causes truly significant alerts to become lost in noise. Aggregation, correlation, and filtering of alerts are essential countermeasures.

### 4. Event Correlation and Filtering
<!-- sources: ITIL 4 MEM §2.2, §3.2.1 -->
The process of relating multiple events to each other to determine their combined significance and the appropriate collective response. Correlation rules may use a second event as a check of the first, or to further filter scope. Defined correlations help prevent negative synergistic effects when events occur simultaneously. A rule set consists of several rules defining how event messages for a particular event will be processed and evaluated — for example, a warning event may be generated each time a disk log file reaches capacity, but an exception event is generated only if more than four warnings occur within a defined period. Rules are typically embedded in monitoring and event handling technologies using Boolean algorithms, referred to as correlation engines. AI and ML systems can supplement rule-based correlation by defining typical and atypical behaviours — forming an additional filtering layer that adapts over time.

### 5. Service Health Models
<!-- sources: ITIL 4 MEM §3.2.1 -->
End-to-end models reflecting the key events in a service and the connections between them. Built from input provided by teams involved in service design, health models let the monitoring team assess user experience by tracking the complete path of a service interaction — for example, measuring the time from a user's mobile application request through all backend systems to the completion notification. There may be several models for a single service, each representing a different user journey or service capability. Health models can be implemented as reports or dashboards on service health and performance, used on an ad hoc basis by service owners, operations teams, and other stakeholders. They bridge the gap between low-level infrastructure metrics and the service-level view that business stakeholders require.

### 6. Monitorability
<!-- sources: ITIL 4 MEM §2.2, §6 -->
The degree to which a service component can be observed and measured by monitoring systems. Monitorability depends on native monitoring features built into operating systems, web servers, database servers, and other software, as well as designed-for-purpose monitoring systems that observe web and cloud applications, networks, platforms, and microservices. For in-house applications, custom-built instrumentation (code or interfaces) may be necessary. All services — including those developed by external suppliers — must be designed as monitoring-enabled, meaning they must be able to provide information on their performance and health. Monitorability should be assessed using criteria that are revealing enough to provide a basis for diagnostics and decision-making. Service design and monitoring and event management practices must cooperate to ensure the necessary monitoring capabilities are built into services from the design stage.

## Activities
<!-- sources: ITIL 4 MEM §3.2.1, §3.2.2, §3.2.3 -->

### Essential (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Define monitoring objectives and scope | With information from service design, service level management, and practices involved in availability, capacity, and performance management, define the key objectives of monitoring. Identify and prioritize which services, systems, CIs, and other service components to monitor based on business objectives and service architecture. Requires service dependency mapping — understanding which business capabilities map to which services and underlying infrastructure. Assess the monitorability of each component |
| 2 | Assess monitoring capabilities and define metrics | Map monitoring priority items to available measurements — including native monitoring features, designed-for-purpose monitoring tools, and synthetic measurements derived from available data. Identify gaps where additional measurements are needed. Define the metric layers to be collected: infrastructure metrics, application metrics, service level metrics, third-party performance metrics, and operations and process performance metrics |
| 3 | Define event types, thresholds, and classification rules | Define and classify event types for each monitored object — using the standard classification scheme (informational, warning, exception) or more granular types based on functionality, user groups, or component types. Define threshold values for each event type in conjunction with service and component development teams. Consider that the same metric may require different thresholds depending on which service it supports and the applicable SLAs. Balance event detection against event handling throughput — not every detectable event should be acted upon |
| 4 | Detect, log, and classify events | Detect events through monitoring systems — both active polling and passive notification. Log all detected events automatically. Filter and correlate events according to defined rule sets. Classify events by type and significance. This activity should be automated as far as possible |
| 5 | Execute event response procedures | Select and execute the appropriate response procedure based on event classification. Send notifications to responsible teams. For exception events, log incidents in the incident management system. Execute automated response scripts where defined. Response procedures may be fully automated, semi-automated with human oversight, or manual depending on event type and organizational maturity |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 6 | Define service health models | Based on input from service design teams, build end-to-end health models reflecting key events in each critical service and the connections between them. Models should enable assessment of user experience by tracking the complete path of service interactions. Implement models as reports, dashboards, or real-time monitoring views for use by service owners and operations teams |
| 7 | Define event correlations and rule sets | Define correlation rules that relate multiple events to determine combined significance. Establish rule sets that specify how event messages are processed and evaluated — including rules that escalate or de-escalate based on event frequency, combination, or context. Embed rules in monitoring and event handling technologies. Define AI-based behaviour analysis where appropriate to identify typical and atypical patterns |
| 8 | Map events to action plans and responsible teams | For each event or group of events, define an action plan to minimize negative impact. Based on the action plan, identify the team or function responsible for response actions and those who should be notified. Action plans may be fully automated, semi-automated, or manual. Map event routing to current organizational structure — routing information must be maintained as responsibilities change |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 9 | Conduct post-mortem reviews and optimize event management | Review major events and incidents to identify monitoring gaps — events that were not detected or not acted upon in time. Analyse filtering and correlation effectiveness. Review service health models for accuracy. Examine event response procedures for errors or inefficiencies. Tune thresholds and rules based on operational experience. Propose changes to monitoring to detect similar incidents in future |
| 10 | Evaluate and adopt monitoring technologies | Review tools available internally and in the market for data analysis, correlation analysis, AI, and ML. Assess new techniques, benchmark against industry practices, and propose trials or pilot implementations within the monitoring budget. Evaluate opportunities to increase automation in both event detection and event response. Review statistical information gathered by monitoring tools to propose improvements to monitoring scope and service coverage |

## Inputs
<!-- sources: ITIL 4 MEM §3.2.1, §3.2.2, §3.2.3, §5.1 -->

| # | Input | Source |
|---|-------|--------|
| 1 | Service health criteria and design documentation | Service design |
| 2 | Service level agreements and performance targets | Service level management |
| 3 | Availability, capacity, and performance thresholds | Availability management, capacity and performance management |
| 4 | Service catalogue and CI data | Service catalogue management, service configuration management |
| 5 | Knowledge articles about services and components | Knowledge management |
| 6 | Information about planned and ongoing changes | Change management |
| 7 | Major incident records | Incident management |
| 8 | Improvement proposals | Continual improvement |
| 9 | Policies and regulatory requirements | Information security management, compliance |

## Outputs
<!-- sources: ITIL 4 MEM §3.2.1, §3.2.2, §3.2.3 -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Event records and event statistics | Measurement and reporting, problem management |
| 2 | Incidents logged from exception events | Incident management |
| 3 | Stakeholder notifications and alerts | Operations teams, service owners, service desk |
| 4 | Updated reports, dashboards, and service health models | Service owners, management, operations teams |
| 5 | Knowledge articles updated from event analysis | Knowledge management |
| 6 | Monitoring plans and defined event types with response procedures | Operations teams |
| 7 | Improvement proposals for monitoring and event management | Continual improvement |
| 8 | Event response errors and post-mortem reports | Problem management, continual improvement |

## Roles
<!-- sources: ITIL 4 MEM §4.1 Table 4.1, §4.2 -->

| Role | Responsibility | Tier |
|------|---------------|------|
| MEM Coordinator | Manages the monitoring and event management practice overall. Coordinates monitoring planning with service design and operations teams. Oversees event handling effectiveness and response procedure accuracy. Initiates reviews and improvement activities. Ensures monitoring data is available to relevant stakeholders. Requires methods expertise, understanding of service architecture, and knowledge of monitoring tools and techniques. In many organizations this role is combined with operations management | T2+ |
| Monitoring Specialist | Technical expert responsible for implementing and maintaining monitoring systems. Defines thresholds, correlation rules, and automated response procedures. Builds service health models and dashboards. Configures monitoring tools and integration with ITSM systems. Evaluates new monitoring technologies and automation opportunities. Requires deep technical expertise in monitoring tools, infrastructure, AI/ML, and automation | T2+ |
| Service Owner | Defines monitoring objectives and priorities for their services based on business value and user experience requirements. Provides input to service health models. Participates in post-mortem reviews. Consumes monitoring data for service management decisions. Requires understanding of service value, stakeholder needs, service architecture, and user experience | T2+ |

## Key Artefacts
<!-- sources: ITIL 4 MEM §3.2, §5.1 -->

| Artefact | Purpose |
|----------|---------|
| Monitoring Plan | Documents the monitoring scope, objectives, metrics, polling intervals, and tools for each monitored service or component. Includes prioritization based on business objectives and service dependencies. Updated as services change |
| Event Classification and Response Matrix | Defines event types (informational, warning, exception), threshold values, classification rules, and the corresponding response procedure for each event type. Includes notification routing, escalation paths, and automation triggers |
| Service Health Model | End-to-end model of a service showing key events, their connections, and their combined impact on user experience. May be implemented as dashboards, reports, or real-time monitoring views. Multiple models may exist per service |
| Event Correlation Rule Set | Collection of rules defining how events are filtered, correlated, and evaluated — including Boolean algorithms, frequency rules, and AI/ML behavioural analysis criteria. Embedded in monitoring and event management technology |
| MEM Performance Report | Periodic report on monitoring and event management effectiveness — covering event volumes by type, response timeliness, incident detection rates, false positive rates, health model accuracy, and improvement progress |

## Process Interfaces
<!-- sources: ITIL 4 MEM §2.3, §3.2, §5.1 -->

| Interface | Relationship |
|-----------|-------------|
| Incident Management (PR11) | Exception events trigger incident creation. MEM enables detection of incidents before user impact where possible. Major incident records feed back into monitoring review |
| Problem Management (PR13) | Event trends and patterns provide input to problem identification. Known error information informs event correlation rules. MEM enables error control by monitoring known-error workarounds |
| Change Management (PR15) | Change schedule informs monitoring teams about expected state changes — preventing false alerts during planned changes. Events may trigger change requests |
| Service Level Management (PR02) | SLAs define service performance targets that inform threshold values. MEM provides actual performance data against SLA targets |
| Availability Management (PR06) | Availability targets inform monitoring thresholds. MEM provides availability measurement data |
| Capacity & Performance Management (PR08) | Capacity and performance thresholds inform event classification. MEM provides utilization and performance measurement data |
| Information Security Management (PR09) | Security policies define security event types and thresholds. MEM detects security events and routes them to security management |
| Service Configuration Management (PR17) | CI data and service dependency maps inform monitoring scope and health model design. CI changes trigger monitoring plan updates |
| Service Design (PR04) | Service design outputs define monitoring requirements and health criteria. Monitorability is a design consideration. Monitoring specialist input during design ensures services are monitoring-enabled |
| Service Desk (PR10) | Service desk communicates event-related information to users. Monitoring-detected incidents are routed through service desk for user communication |
| Continual Improvement (PR24) | MEM review outputs feed improvement initiatives. Monitoring data supports improvement identification across all practices |
| Infrastructure & Platform Management | Infrastructure teams implement monitoring agents, configure native monitoring features, and maintain monitoring infrastructure. Threshold recommendations come from infrastructure expertise |
