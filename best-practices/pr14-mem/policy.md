---
process_id: PR14
process_name: "Monitoring & Event Management"
category: policy
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Monitoring & Event Management §2.1, §2.2, §2.4"
  - "FitSM-1: §PR4.4, §PR5.4, §PR6.4"
  - "IT4IT: D2C Value Stream"
last_updated: 2026-03-14
status: draft
---

# Monitoring & Event Management — Best Practice Policy

## How to Use This Policy Template

This policy establishes the governing principles and mandatory requirements for the monitoring and event management practice. It should be customized to reflect the organization's service architecture, monitoring maturity, automation capabilities, and operational risk profile. Requirements are graduated by maturity — organizations should implement Essential requirements first, then layer on Intermediate and Advanced requirements as the practice matures. FitSM has no dedicated monitoring and event management process — monitoring activities are distributed across capacity management (PR5.4), availability management (PR4.4), and information security management (PR6.4). This policy consolidates all monitoring and event management requirements into a single governance structure.

---

## Policy Principles

### 1. Business-Aligned Monitoring
<!-- sources: ITIL 4 MEM §2.4.1, §2.5 -->

Monitoring scope shall be driven by business objectives and service value — not by technical capability alone. Deciding which services, systems, and configuration items to monitor requires thorough understanding of the organization's service design architecture and service dependency mapping. Practitioners must understand which business capabilities map to which services and which underlying infrastructure, so that monitoring priorities reflect business impact.

### 2. Proactive Detection
<!-- sources: ITIL 4 MEM §2.2 -->

Monitoring shall enable proactive identification of conditions that could lead to incidents — not merely reactive detection of failures that have already occurred. Warning events shall be used to take preventive action before service impact. Pattern analysis of past events shall inform proactive actions to prevent future adverse events. The practice shall progress from reactive event detection toward proactive trend identification and predictive capability.

### 3. Appropriate Granularity
<!-- sources: ITIL 4 MEM §2.4.1 -->

Monitoring scope, frequency, and metric count shall be balanced against the cost of data collection, storage, and analysis. The main challenge is not lack of data but volume of data — the focus shall be on finding meaningful information to support service operations, improvement, and decision-making. More data does not necessarily produce better outcomes if the organization cannot filter, classify, and act upon it effectively.

### 4. Standard Event Classification
<!-- sources: ITIL 4 MEM §2.2 -->

Events shall be classified using a standard scheme — informational, warning, and exception — enabling consistent handling, appropriate notification routing, and efficient resource utilization. A common set of control actions shall be established for each class: when automated response is appropriate, when human intervention is required, when incident or change processes should be initiated, and when special handling is needed. A one-size-fits-all approach to event handling is inappropriate.

### 5. Automation First
<!-- sources: ITIL 4 MEM §3.2.2, §4.1 -->

Event handling — from detection through response — shall be automated as far as possible. All efforts should be made to minimize human intervention in routine event processing. Automated detection, logging, filtering, correlation, classification, and response reduce processing time, improve consistency, and free operational staff for higher-value activities. Human involvement should focus on monitoring planning, review, and optimization — not routine event processing.

### 6. Design for Monitorability
<!-- sources: ITIL 4 MEM §2.2, §6 -->

All services and service components — including those developed by external suppliers — shall be designed as monitoring-enabled. Monitorability shall be a design requirement, assessed during service design and transition. Services must be able to provide information on their performance and health through native monitoring features, instrumentation, or designed-for-purpose monitoring interfaces. Monitoring requirements shall be defined during service design, not retrofitted after deployment.

### 7. Continual Improvement
<!-- sources: ITIL 4 MEM §3.2.3 -->

Monitoring and event management shall be subject to continual improvement — regardless of current maturity level. Major events and incidents shall trigger post-mortem reviews to identify monitoring gaps. Filtering, correlation, and threshold effectiveness shall be reviewed periodically. Technology opportunities — including AI, ML, and advanced correlation — shall be evaluated and adopted where justified.

---

## Mandatory Requirements

### Essential (T2+)
<!-- sources: ITIL 4 MEM §2.3, §2.4, §3.2.1, §3.2.2 -->

| # | Requirement |
|---|-------------|
| 1 | Monitoring scope shall be defined based on business objectives and service design architecture — identifying and prioritizing services, systems, and configuration items to be observed |
| 2 | Events shall be classified using a standard scheme — at minimum informational, warning, and exception — with consistent handling procedures for each class |
| 3 | Thresholds shall be defined for each monitored metric — specifying the values that trigger event detection and the corresponding response actions. Threshold values shall be calibrated to prevent alert noise while ensuring significant events are detected |
| 4 | All detected events shall be logged automatically with sufficient detail for subsequent analysis, correlation, and reporting |
| 5 | Event response procedures shall be defined for each event type or group — specifying the actions to be taken, teams to be notified, and escalation paths to be followed. Exception events shall trigger incident creation |

### Intermediate (T2+)
<!-- sources: ITIL 4 MEM §2.4.1, §3.2.1, §3.2.2 -->

| # | Requirement |
|---|-------------|
| 6 | Service health models shall be maintained for critical services — showing end-to-end event relationships, enabling assessment of user experience impact, and providing service-level visibility to stakeholders |
| 7 | Event correlation and filtering rules shall be defined and maintained — using rule sets, correlation engines, and where appropriate AI/ML-based behavioural analysis — to reduce event noise and enable efficient response |
| 8 | Events shall be mapped to action plans with identified responsible teams and notification targets. Event routing information shall be maintained as organizational responsibilities change |
| 9 | Monitoring data — including real-time status, historical trends, and service health information — shall be made available to relevant stakeholders in agreed formats through reports, dashboards, or self-service portals |

### Advanced (T3)
<!-- sources: ITIL 4 MEM §2.4, §3.2.3, §6 -->

| # | Requirement |
|---|-------------|
| 10 | Monitoring and event management shall be reviewed regularly — including post-mortem analysis of major events and incidents, review of filtering and correlation effectiveness, and threshold optimization based on operational experience |
| 11 | AI, ML, and advanced correlation technologies shall be evaluated and adopted where they demonstrably improve event detection accuracy, reduce noise, or enable predictive capability. Technology reviews shall include market benchmarking and pilot implementations |
| 12 | All services developed or procured from external suppliers shall be contracted with explicit monitoring requirements — ensuring they are monitoring-enabled and can provide performance and health information through agreed interfaces |

---

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Incident Management Policy (PR11) | Exception events trigger incident creation. Major incident records feed back into monitoring review |
| Problem Management Policy (PR13) | Event trends and patterns feed problem identification. Known error information informs correlation rules |
| Change Management Policy (PR15) | Change schedule prevents false alerts during planned changes. Events may trigger change requests |
| Service Level Management Policy (PR02) | SLAs define performance targets that inform threshold values. MEM provides actual performance data |
| Capacity & Performance Management Policy (PR08) | Capacity and performance thresholds inform event classification. MEM provides utilization data |
| Information Security Management Policy (PR09) | Security policies define security event types. MEM detects and routes security events |
| Service Design Policy (PR04) | Monitorability is a service design requirement. Design outputs define monitoring criteria |
| Continual Improvement Policy (PR24) | MEM review outputs feed improvement initiatives |
