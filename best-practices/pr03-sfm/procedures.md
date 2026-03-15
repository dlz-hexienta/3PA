---
process_id: PR03
process_name: "Service Financial Management"
category: procedures
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T3
sources:
  - "ITIL 4: Service Financial Management §3.2.1, §3.2.2, §3.2.3"
  - "IT4IT: S2P Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Financial Management — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier — Essential procedures should be implemented first, with Intermediate and Advanced procedures added as the practice matures. All procedures apply only at T3 complexity (the minimum tier for this process). The three ITIL 4 sub-processes — managing the approach, financial planning, and management accounting — are consolidated into five procedures ordered by implementation priority.

---

## Essential Procedures (All tiers)

### PROC-SFM-01: Define and Maintain the Service Financial Management Approach
<!-- sources: ITIL 4 Service Financial Management §3.2.1 Tables 3.1, 3.2 -->

**Trigger:** New organizational need for service financial management, significant change in organizational structure or strategy, or scheduled review of the approach.

**Scope:** Covers stakeholder analysis, approach definition, communication, and integration with related practices.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Identify stakeholders interested in service financial management information about products and services. Gather and analyse their requirements for financial data — scope, detail, frequency, and format | Service Financial Manager | Organizational architectures, portfolios, service catalogue | Stakeholder requirements analysis |
| 2 | Define and agree the service financial management approach — including cost models, budget models, cost types, cost allocation rules, policies, procedures, data structures, roles, and responsibilities. Discuss and approve with key stakeholders including financial management experts and organizational leaders. Balance practice benefits against practice cost | Service Financial Manager, Executive Leader | Stakeholder requirements, organization's financial policies, IT asset data, service configuration data, contracts and agreements | Documented SFM approach (including cost and budget models) |
| 3 | Communicate the agreed approach to stakeholders across the organization — practitioners participating in SFM activities, technical experts involved in automation, and other affected teams | Service Financial Manager | Approved SFM approach | SFM communications and knowledge materials |
| 4 | Implement the approach in conjunction with IT asset management, service configuration management, supplier management, change management, project management, and other relevant practices. Integrate financial data into operational transactions and value streams | Service Financial Manager | Approved SFM approach, practice integration requirements | Integrated SFM approach in value streams |

**Exit criteria:** Documented approach approved by executive leader. Approach communicated to all stakeholders. Integration points with related practices established.

---

### PROC-SFM-02: Plan and Agree Budgets
<!-- sources: ITIL 4 Service Financial Management §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Start of a new budget period, new initiative requiring financial planning, or budget revision triggered by significant deviation.

**Scope:** Covers analysis of prior performance, cost and income estimation, budget compilation, and budget approval.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Analyse available service financial information — current and previous business plans and performance reports, budgets and budget review reports, financial records, product and service performance reports and capacity forecasts, supplier performance reports, current and planned contracts and agreements, and service performance reports and SLAs | Service Financial Manager | Previous and current plans, budgets, agreements, contracts, performance data, financial records | Performance and cost analysis |
| 2 | Based on the analysis, estimate costs and income for planned initiatives or periods of operation. Income estimates may include charging recommendations where applicable. Involve relevant teams to make, review, or confirm estimates | Service Financial Manager, Finance Business Partner | Performance analysis, SFM approach, capacity forecasts | Cost and income estimates |
| 3 | Aggregate estimates into budgets following the agreed budget model. Where applicable, compile charging guidelines alongside budgets | Service Financial Manager | Cost and income estimates, budget model | Compiled budgets and charging guidelines |
| 4 | Submit budgets to appropriate authorities for approval. If not approved, return to Step 2 with comments and recommendations. Communicate approved budgets to relevant teams for execution. Where applicable, communicate approved charging guidelines | Executive Leader, Service Financial Manager | Compiled budgets | Approved budgets; charging guidelines (if applicable) |

**Exit criteria:** Budgets approved by appropriate authority. Approved budgets communicated to all budget holders. Charging guidelines agreed where applicable.

---

## Intermediate Procedures (T2+)

### PROC-SFM-03: Monitor and Control Budgets
<!-- sources: ITIL 4 Service Financial Management §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Ongoing budget execution, spending request received, significant budget deviation detected, or scheduled budget review.

**Scope:** Covers budget monitoring, spending authorization, budget adjustment within tolerances, escalation, and periodic budget review.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Monitor how budgets are being executed — track actual spending and income against budgeted amounts. Identify variances and trends | Service Financial Manager | Approved budgets, financial transaction records | Budget execution status |
| 2 | Authorize spending requests in accordance with the agreed SFM approach and tolerance levels. Approve off-budget spending or pricing adjustments within agreed tolerances where justified | Service Financial Manager | Spending requests, budget tolerances | Spending decisions — assessments and approvals |
| 3 | Escalate risks and cases of going off-budget outside agreed tolerances to appropriate authorities. Provide analysis of the deviation, its causes, and recommended actions | Service Financial Manager | Budget variance analysis, tolerance thresholds | Escalation reports, risk notifications |
| 4 | Review budgets in case of significant deviations, at the end of budgeted initiatives and periods, and on a regular basis. If revision is required, initiate a new planning cycle (return to PROC-SFM-02). Produce budget review reports | Service Financial Manager | Budget execution data, deviation analysis | Budget review reports; new planning cycle initiation (if required) |

**Exit criteria:** Budget execution monitored continuously. All spending authorized within agreed procedures. Deviations outside tolerance escalated. Periodic reviews completed and reported.

---

### PROC-SFM-04: Perform Management Accounting
<!-- sources: ITIL 4 Service Financial Management §3.2.3 Tables 3.5, 3.6 -->

**Trigger:** Financial transaction recorded, request for service financial information received, or scheduled cost allocation cycle.

**Scope:** Covers cost identification and capture, cost model selection, cost allocation, and exception management.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Identify and capture data about costs following the agreed SFM approach. Automate data capture where possible — manual processing of financial records only where required | Service Financial Manager, Finance Business Partner | SFM approach, financial transaction records, IT asset data, service configuration data | Captured cost data |
| 2 | Select a cost model from those defined by the SFM approach to fit the specific stakeholder requirements for financial information | Service Financial Manager | SFM approach (cost models), stakeholder requirements | Selected cost model |
| 3 | Perform cost categorization and allocation following the selected cost model — categorize costs by type, allocate direct costs to cost objects, allocate indirect costs using agreed cost drivers, and distribute overheads using the agreed formula | Service Financial Manager, Finance Business Partner | Selected cost model, captured cost data | Allocated cost data |
| 4 | Where necessary, manage exceptions — deviate from the approved model within agreed tolerances to better meet stakeholder requirements. Report every exception for continual improvement of the SFM approach | Service Financial Manager | Allocated cost data, exception circumstances | Exception reports; updated cost allocations |

**Exit criteria:** Costs identified, captured, and allocated following the approved model. Exceptions documented and reported. Cost data ready for reporting.

---

## Advanced Procedures (T3)

### PROC-SFM-05: Report and Optimize
<!-- sources: ITIL 4 Service Financial Management §3.2.1 Table 3.2, §3.2.3 Table 3.6, §5.2 -->

**Trigger:** Scheduled reporting cycle, stakeholder request for financial report, scheduled approach review, or event-based review trigger (non-standard request, error, new requirement).

**Scope:** Covers production of financial reports and review and optimization of the SFM approach.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Present required financial information to stakeholders as dashboards, operational reports, or analytical reports in line with the selected cost model. Automate standard report production where possible — produce manual reports for analytical or ad hoc requests | Service Financial Manager | Allocated cost data, report specifications, cost model | Standard and tailored service financial reports |
| 2 | Verify report accuracy and relevance with stakeholders. Ensure reports are tailored to stakeholder needs — no unnecessary data, appropriate level of detail for the decision-maker | Service Financial Manager | Stakeholder feedback, report outputs | Validated reports |
| 3 | Monitor and review the adoption, compliance, and effectiveness of the agreed SFM approach. Perform reviews on both event-based (non-standard requests, identified errors, new requirements) and interval-based schedules | Service Financial Manager, Executive Leader | SFM approach performance data, stakeholder feedback, exception reports | Approach performance assessment |
| 4 | Based on reviews, initiate changes to the approach and its practical implementation. Optimize resource-consuming procedures — especially cost data collection and processing. Automate data collection, processing, and reporting where reasonable | Service Financial Manager | Approach performance assessment, optimization opportunities | Requests for changes and improvement initiatives |
| 5 | Report approach performance to executive leaders and continual improvement. Feed findings into the next cycle of PROC-SFM-01 for approach updates | Service Financial Manager | Assessment results, change requests | SFM approach performance reports; improvement inputs |

**Exit criteria:** Financial reports produced and distributed to stakeholders. Approach reviewed against effectiveness criteria. Optimization opportunities identified and actioned. Performance reported.
