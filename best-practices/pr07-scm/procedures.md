---
process_id: PR07
process_name: "Service Continuity Management"
category: procedures
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
  - "ITIL 4: Service Continuity Management §3.2.1–§3.2.5"
  - "FitSM-2: §PR4 SACM (continuity scope)"
  - "IT4IT: D2C Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Continuity Management — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier. The five ITIL 4 sub-processes — governance, business impact analysis, plan development, testing, and response and recovery — are consolidated into five procedures. The practice is closely related to availability management — organizations that combine the two practices should integrate the corresponding procedures.

---

## Essential Procedures (T2+)

### PROC-SCM-01: Establish Governance and Perform Business Impact Analysis
<!-- sources: ITIL 4 SCM §3.2.1, §3.2.2 Tables 3.1–3.4 -->

**Trigger:** Initiation of service continuity management programme, new service entering scope, significant change to existing service, or scheduled annual review.

**Scope:** Covers scope definition, policy setting, BIA, and determination of recovery requirements. Maps to definition activities 1–2.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Define scope — determine which services, products, sites, and locations are covered. Define which events constitute disasters using predefined business-impact criteria. Consider staged implementation if costs are high. Use techniques such as cost-benefit analysis, SWOT, and PESTLE to inform scope decisions. Consider existing BIA reports, risk registers, customer requirements, and regulatory requirements | Service Continuity Manager | Previous BIA, risk register, customer requirements, regulatory requirements, risk appetite | Documented scope |
| 2 | Set policy — document scope, assign roles and responsibilities, define organizational structure for response and recovery (strategic, tactical, operational levels), and establish the general approach including available resources and limitations. Communicate policies to all stakeholders as soon as possible | Service Continuity Manager | Scope, organizational context | Service continuity policy; documented roles |
| 3 | Identify vital business functions — use brainstorming, stakeholder interviews, service documentation analysis, and risk assessment data to identify VBFs. Analyse consequences of disruption — both hard impacts (financial loss, SLA fines, regulatory judgments) and soft impacts (reputation, competitive advantage). Assess how impacts change over time. Identify VBF interdependencies using service and configuration models and component failure impact analysis (CFIA) | Service Owner | Service documentation, risk assessments, financial data, service models, CI data | Priority list of VBFs; documented impacts; VBF interdependencies |
| 4 | Determine recovery requirements — based on disruption analysis and interdependencies, define RTO, RPO, and minimum target service levels for each service or VBF within scope. Consider factors including reduction in service delivery capability, SLA fines, regulatory judgments, competitive advantage losses, and reputational damage. Document in BIA report | Service Continuity Manager | VBF analysis, disruption consequences, interdependencies | BIA report with recovery requirements |

**Exit criteria:** Scope and policy documented and communicated. VBFs identified and prioritized. Disruption consequences analysed. RTO, RPO, and minimum service levels determined. BIA report produced.

---

### PROC-SCM-02: Develop Strategies and Plans
<!-- sources: ITIL 4 SCM §3.2.3 Tables 3.5, 3.6 -->

**Trigger:** BIA completed or updated, existing plans require revision due to service or team changes, or exercise/recovery findings require plan updates.

**Scope:** Covers strategy development, plan development, and initial testing. Maps to definition activity 3.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Develop continuity strategies — based on BIA outputs, determine an appropriate and cost-effective set of strategies (diversification, replication, standby, post-incident acquisition, subcontracting, or do nothing). For services with earlier and higher impacts, prioritize preventive measures. For services with lower, slower-developing impacts, emphasize recovery measures. Assess effectiveness (effects versus expected losses) and efficiency (cost versus benefit) of each option | Service Continuity Manager | BIA report, existing controls, available resources | Service continuity strategies |
| 2 | Develop service continuity plans — based on strategies and policy, develop plans at strategic (crisis management decisions, external communications), tactical (coordination, resource allocation, priority management), and operational (team-level recovery procedures) levels. Cover response, recovery, and restoration stages. Include invocation criteria, crisis management contacts, communication procedures, recovery procedures, escalation paths, and restoration instructions. Ensure plans are clear, concise, action-oriented, and time-based | Service Continuity Manager | Strategies, policy, consumer's continuity plans | Service continuity plans |
| 3 | Align with consumer and partner plans — where relevant, ensure service continuity plans interface clearly with the service consumer's business continuity plans and partner continuity arrangements. Validate that recovery timelines and procedures are compatible | Service Continuity Manager | Consumer's continuity plans, supplier agreements | Aligned plans |
| 4 | Perform initial testing — before publishing, test plans using appropriate methods (walkthrough or table-top at minimum). Validate that procedures are correct, team assignments are current, and contact information is accurate. Update plans based on initial testing findings | Recovery Coordinator | Draft plans | Validated and published plans |

**Exit criteria:** Strategies selected and documented. Plans developed at all three levels. Consumer and partner alignment verified. Plans tested and published.

---

## Intermediate Procedures (T2+)

### PROC-SCM-03: Exercise and Audit Plans
<!-- sources: ITIL 4 SCM §3.2.4 Tables 3.7, 3.8, §2.4.3 -->

**Trigger:** Scheduled exercise programme, significant change affecting recovery capability, failed previous exercise, or scheduled audit cycle.

**Scope:** Covers exercise execution, audit, and exercise programme development. Maps to definition activities 5–7.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Develop or update exercise programme — plan exercises to ensure all parts of the practice are tested at least annually, covering all four dimensions (people with right skills, equipment and data available, third parties ready, procedures correct). Scale exercise frequency to impact levels — higher-impact services should be exercised more frequently. Select exercise types appropriate to objectives: walkthrough, table-top, command-post, live, or test | Service Continuity Manager | Continuity plans, risk profile, previous exercise results | Exercise programme |
| 2 | Conduct exercises — execute exercises according to the programme. Observe team performance, plan effectiveness, communication quality, and decision-making. If the exercise involves live components, ensure safety controls are in place. Record observations and measurements (RTO/RPO achievement, minimum service level maintenance) | Recovery Coordinator | Exercise programme, continuity plans | Exercise observations |
| 3 | Produce exercise reports — analyse findings and team performance. Document recommendations including requirements for new or updated controls, plan changes, and training needs. If the exercise failed, schedule re-exercise as soon as possible. Feed findings into plan updates and continual improvement | Service Continuity Manager | Exercise observations | Exercise report with findings and recommendations |
| 4 | Conduct service continuity audits — verify that BIA, strategies, and plans remain appropriate and relevant. Audits may be internal or external, scheduled or triggered by failed exercises or recoveries. Assess compliance with policy and regulatory requirements. Document audit findings and track remediation | Service Continuity Manager | Plans, BIA reports, policies, regulatory requirements | Audit report |

**Exit criteria:** Exercise programme maintained. Exercises conducted on schedule. Findings documented and acted upon. Failed exercises rescheduled. Audits completed with remediation tracked.

---

### PROC-SCM-04: Invoke and Execute Recovery
<!-- sources: ITIL 4 SCM §3.2.5 Tables 3.9, 3.10 -->

**Trigger:** Disruptive event meeting predefined disaster criteria. Invocation decision by crisis management group.

**Scope:** Covers invocation decision, plan execution, and recovery reporting. Maps to definition activity 4.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Assess and decide on invocation — the crisis management group evaluates the potential impact, likely duration, and timing of the disruptive event against invocation criteria. Decide whether to invoke continuity plans. If invoking, select recovery options (if multiple are available) and define the scope of invocation (services, products, sites) | Service Continuity Manager | Incident records, continuity plans, invocation criteria | Invocation decision; scope and recovery option selection |
| 2 | Execute response procedures — perform initial response actions to prevent further damage. Activate communication procedures. Notify all recovery teams, stakeholders, customers, and partners. Establish command and coordination structures at strategic, tactical, and operational levels | Recovery Coordinator | Continuity plans, invocation decision | Response actions completed; communications activated |
| 3 | Execute recovery and restoration — recovery teams perform procedures to resume service delivery according to RTO, RPO, and minimum target service levels. Coordinate across teams and manage resource allocation at the tactical level. Monitor recovery progress. Following recovery, execute restoration procedures to return to normal operations and restore the ability to invoke plans again | Recovery Coordinator | Continuity plans, response status | Service recovered; normal operations restored |
| 4 | Produce recovery report — document the complete recovery timeline, actions taken, actual RTO/RPO achieved, deviations from plans, findings, and recommendations. Identify requirements for new or updated controls. Feed findings into plan updates, strategy review, and continual improvement | Service Continuity Manager | Recovery records, observations | Recovery report with findings and recommendations |

**Exit criteria:** Invocation decision made and documented. Response, recovery, and restoration executed. Service restored to normal operations. Recovery report produced with lessons learned.

---

## Advanced Procedures (T3)

### PROC-SCM-05: Review and Optimize Continuity Arrangements
<!-- sources: ITIL 4 SCM §2.4.2, §3.2.3, §6 -->

**Trigger:** Completed recovery from actual disaster, major exercise findings, annual review cycle, significant environmental change (new consumer, regulatory change, partner change), or uncovered event type.

**Scope:** Covers review of all continuity arrangements, risk mitigation optimization, and partner/supplier integration. Maps to definition activities 8–10.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Review continuity arrangements end-to-end — assess whether scope, policy, BIA, strategies, plans, and exercise programme remain appropriate. Review whether new disaster types should be added to scope. Evaluate whether recovery requirements have changed due to new services, customers, or regulatory requirements | Service Continuity Manager | Recovery reports, exercise reports, audit reports, environmental changes | Arrangement review findings |
| 2 | Optimize risk mitigation measures — review the effectiveness and efficiency of existing measures across all four dimensions. Assess whether new technologies or approaches could improve resilience at lower cost. Compare actual losses from events against expected losses. Propose new or updated controls where justified | Service Continuity Manager | Measure effectiveness data, cost-benefit analysis, technology assessment | Optimized control set; change requests |
| 3 | Integrate with partners and suppliers — negotiate and agree continuity requirements with critical partners and suppliers. Ensure third-party continuity arrangements align with organizational plans. Involve partners in plan development and testing. Assess dependencies on cloud and integrated digital services | Service Continuity Manager | Supplier agreements, partner capabilities, dependency analysis | Updated partner continuity arrangements |
| 4 | Integrate with business continuity management — ensure service continuity plans interface clearly with business continuity plans at all levels. Align BIA cycles, exercise programmes, and communication procedures. Where possible, conduct joint exercises | Service Continuity Manager | Business continuity plans, organizational BCM framework | Integrated continuity framework |
| 5 | Update and communicate — update all affected plans, policies, strategies, and exercise programmes based on review findings. Communicate changes to all stakeholders. Track implementation of optimized measures through change management and continual improvement | Service Continuity Manager | Review findings, optimized arrangements | Updated plans and policies; stakeholder communications |

**Exit criteria:** All continuity arrangements reviewed. Measures optimized. Partner arrangements aligned. Business continuity integration verified. Changes communicated and tracked.
