---
process_id: PR14
process_name: "Monitoring & Event Management"
category: procedures
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Monitoring & Event Management §3.2.1, §3.2.2, §3.2.3"
  - "FitSM-1: §PR4.4, §PR5.4"
  - "IT4IT: D2C Value Stream"
last_updated: 2026-03-14
status: draft
---

# Monitoring & Event Management — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier. The three ITIL 4 sub-processes — monitoring planning, event handling, and monitoring and event management review — are consolidated into five procedures. Event handling should be automated as far as possible — the procedure below describes the logical steps that automation should implement, with human involvement only for oversight and exceptions.

---

## Essential Procedures (T2+)

### PROC-MEM-01: Plan Monitoring for Services and Components
<!-- sources: ITIL 4 MEM §3.2.1 Tables 3.1, 3.2 -->

**Trigger:** New service or service component entering operations, significant change to an existing service, gap identified in monitoring coverage, or scheduled monitoring review.

**Scope:** Covers defining monitoring objectives, assessing capabilities, defining event types and thresholds, and establishing response procedures. Maps to definition activities 1–3.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Define monitoring objectives — working with service design, service level management, and availability/capacity/performance management, identify the key objectives of monitoring for the service or component. Start from warranty requirements, then move to utility requirements. Build a prioritized list of monitoring objectives based on business impact and service dependencies. Assess the monitorability of each component | MEM Coordinator | Service health criteria, SLAs, service design documentation, CI data | Prioritized monitoring objectives |
| 2 | Assess monitoring capabilities and define metrics — map prioritized objectives to available measurements including native monitoring features, existing monitoring tools, and synthetic measurements. Identify gaps where additional instrumentation is needed. Define the metric layers: infrastructure, application, service level, third-party, and process metrics | Monitoring Specialist | Monitoring objectives, available tools and features | Metrics definition; instrumentation gaps |
| 3 | Define event types and thresholds — for each monitored metric, define event types (informational, warning, exception) and the threshold values that trigger each type. Consider that the same metric may need different thresholds depending on the service and SLA it supports. Calibrate thresholds to prevent alert noise while ensuring significant events are captured. Develop monitoring iteratively — start with preventing critical failures, refine later | Monitoring Specialist | Metrics definition, SLAs, capacity/performance targets | Event type definitions; threshold values |
| 4 | Define response procedures and notification routing — for each event type or group, define the action plan to minimize negative impact. Specify which team or function is responsible for response actions and which stakeholders should be notified. Determine which responses can be automated and which require human intervention. Document response procedures as the basis for event handling automation | MEM Coordinator | Event types, organizational structure, automation capabilities | Event response procedures; notification routing matrix |

**Exit criteria:** Monitoring objectives defined and prioritized. Metrics mapped to available measurements. Event types and thresholds defined. Response procedures documented. Notification routing established.

---

### PROC-MEM-02: Handle Events
<!-- sources: ITIL 4 MEM §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Change of state detected by monitoring systems or reported through manual monitoring.

**Scope:** Covers event detection, logging, filtering, correlation, classification, and response execution. Maps to definition activities 4–5. This procedure should be automated as far as possible — the steps describe the logical flow that automation implements.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Detect and log events — monitoring systems detect changes of state through active polling or passive notification. Each detected event is automatically logged in the monitoring system with timestamp, source, metric values, and raw event data. Not all detectable changes of state should be captured — monitoring system bandwidth and processing capacity should be considered | Monitoring Specialist (oversight) | Monitoring system notifications, polling responses | Logged event records |
| 2 | Filter and correlate events — apply rule sets to filter events and identify correlations. Eliminate duplicate events, suppress known transient conditions, and correlate related events across components. This step may be iterative — initial filtering may reveal additional correlations requiring further analysis. Apply AI/ML behavioural analysis where configured | Monitoring Specialist (oversight) | Logged events, correlation rule sets | Filtered and correlated events |
| 3 | Classify events and select response — classify each event into its defined type (informational, warning, exception) based on threshold values and correlation results. Select the appropriate response procedure based on event classification and the response matrix. For exception events, determine whether an incident should be created | Monitoring Specialist (oversight) | Filtered events, event classification rules, response matrix | Classified events; selected response procedures |
| 4 | Execute response and notify — carry out the selected response procedure. Send notifications to responsible teams and stakeholders. For exception events, create incident records in the incident management system. For warning events, notify teams to take preventive action. For informational events, update dashboards and logs. Record response actions and any response errors | Monitoring Specialist (oversight) | Response procedures, notification routing | Response actions executed; incident records created; notifications sent; updated dashboards |

**Exit criteria:** Events detected and logged. Filtering and correlation applied. Events classified. Response procedures executed. Notifications sent. Incidents created for exception events. Response errors recorded.

---

## Intermediate Procedures (T2+)

### PROC-MEM-03: Build Service Health Models and Correlation Rules
<!-- sources: ITIL 4 MEM §3.2.1 Tables 3.1, 3.2 -->

**Trigger:** Critical service entering monitoring, existing health model requires update due to service changes, or event correlation gaps identified during review.

**Scope:** Covers building end-to-end health models, defining correlation rule sets, and mapping events to action plans. Maps to definition activities 6–8.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Build service health models — working with service design teams, construct end-to-end models reflecting the key events in each critical service and the connections between them. Map user journeys through all service components to enable assessment of user experience impact. There may be several models per service representing different capabilities or user groups | Monitoring Specialist | Service design documentation, service dependency maps, user journey maps | Service health models |
| 2 | Define event correlations and rule sets — identify relationships between events across components. Define rule sets specifying how event messages are processed and evaluated — including frequency-based rules (escalate after N occurrences), time-based rules (within M seconds), and combination rules (event A plus event B triggers event C). Consider AI/ML-based behavioural analysis for identifying atypical patterns | Monitoring Specialist | Service health models, event type definitions, historical event data | Correlation rule sets |
| 3 | Map events to action plans and responsible teams — for each event or event group, define a detailed action plan covering the steps to minimize negative impact. Map action plans to the specific teams or functions responsible for execution and notification. Define which plans are automated, semi-automated, or manual | MEM Coordinator | Event correlations, organizational structure, automation capabilities | Event-to-action-plan mapping; updated notification routing |
| 4 | Implement and validate — embed correlation rules in monitoring technology. Configure health model dashboards and reports. Test rule sets against historical event data and known scenarios. Validate that health models accurately reflect service behaviour. Deploy to production monitoring | Monitoring Specialist | Rule sets, health models, monitoring tools | Deployed correlation rules; operational health model dashboards |

**Exit criteria:** Health models built for critical services. Correlation rule sets defined and embedded in technology. Events mapped to action plans. Rules validated and deployed.

---

### PROC-MEM-04: Review and Optimize Event Management
<!-- sources: ITIL 4 MEM §3.2.3 Tables 3.5, 3.6 -->

**Trigger:** Scheduled review cycle, major event or incident revealing monitoring gaps, accumulation of false positives or missed events, or significant change in service portfolio.

**Scope:** Covers post-mortem review, filtering and correlation analysis, threshold tuning, and response procedure improvement. Maps to definition activity 9.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Conduct post-mortem review — for major events and incidents, analyse whether the event was detected in time, whether correlation rules identified the correct significance, and whether the response was appropriate. Decompose major events to component level and explore metrics that could have provided earlier detection. Identify additional risks of affected components | MEM Coordinator | Major event records, major incident records, event statistics | Post-mortem findings; monitoring gap analysis |
| 2 | Review filtering and correlation effectiveness — assess whether monitoring is detecting too many events (noise) or too few (gaps). Identify events that were incorrectly filtered or correlated. Tune thresholds — tightening where events are missed, loosening where noise is excessive. Update rule sets based on operational experience | Monitoring Specialist | Event statistics, false positive/negative data, rule sets | Updated thresholds; improved correlation rules |
| 3 | Review service health models and response procedures — verify that health models accurately reflect current service architecture and dependencies. Identify response procedure failures or inefficiencies. Propose automation for response procedures currently handled manually. Update notification routing for organizational changes | Monitoring Specialist | Health models, response procedure records, organizational changes | Updated health models; improved response procedures |
| 4 | Initiate improvements — register improvement initiatives for processing through continual improvement. Propose changes to monitoring scope, thresholds, tools, or automation. Track implementation and verify outcomes | MEM Coordinator | Review findings, improvement proposals | Registered improvements; change requests |

**Exit criteria:** Major events reviewed and monitoring gaps identified. Filtering and correlation effectiveness assessed. Health models and response procedures updated. Improvements initiated and tracked.

---

## Advanced Procedures (T3)

### PROC-MEM-05: Evaluate Technologies and Optimize Automation
<!-- sources: ITIL 4 MEM §3.2.3 Tables 3.5, 3.6, §5.2 -->

**Trigger:** Scheduled technology review cycle, new monitoring technology available in the market, significant automation gap identified, or budget cycle for monitoring investment.

**Scope:** Covers technology evaluation, automation optimization, and statistical analysis review. Maps to definition activity 10.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Review available monitoring technologies — assess tools available internally and in the market for data analysis, correlation analysis, AI, and ML. Evaluate cloud-based monitoring services, AIOps platforms, and advanced correlation engines. Benchmark against industry practices and peer organizations | Monitoring Specialist | Market research, vendor assessments, current tool inventory | Technology assessment |
| 2 | Assess automation opportunities — identify event handling steps currently requiring human intervention that could be automated. Evaluate the cost-benefit of automating specific response procedures. Assess AI/ML capabilities for event correlation, anomaly detection, and predictive analysis | Monitoring Specialist | Current automation coverage, manual intervention records, AI/ML capabilities | Automation opportunity assessment |
| 3 | Propose and pilot new technologies — within the monitoring budget, propose trials and pilot implementations for promising technologies. Define success criteria and evaluation periods. Implement pilots in a controlled scope before broader deployment | MEM Coordinator | Technology and automation assessments, budget | Pilot proposals; trial implementations |
| 4 | Review statistical information and monitoring trends — analyse the statistical information gathered by monitoring tools to identify patterns, trends, and anomalies not visible in individual event data. Identify services or components where monitoring investment would provide the greatest return. Share trend data with teams involved in the service lifecycle | Monitoring Specialist | Monitoring statistics, trend data | Trend analysis; monitoring investment recommendations |
| 5 | Deploy and measure outcomes — deploy successful technology and automation improvements to production monitoring. Measure impact on event detection accuracy, response timeliness, noise reduction, and operational efficiency. Update monitoring plans and health models to leverage new capabilities | MEM Coordinator | Pilot results, deployment plans | Deployed improvements; outcome measurements |

**Exit criteria:** Technologies reviewed and assessed. Automation opportunities identified. Pilots proposed and executed where justified. Statistical trends analysed and shared. Successful improvements deployed and measured.
