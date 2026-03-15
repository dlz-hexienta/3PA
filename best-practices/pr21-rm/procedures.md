---
process_id: PR21
process_name: "Risk Management"
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
  - "ITIL 4: Risk Management §3.2.1–§3.2.3, §2.2, §4.1"
  - "IT4IT: S2P Value Stream"
last_updated: 2026-03-14
status: draft
---

# Risk Management — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier. The three ITIL 4 processes — governance of risk management, risk identification/analysis/treatment, and risk monitoring and review — are consolidated into five procedures. Risk management has no dedicated FitSM process — these procedures draw primarily from ITIL 4. Risk identification, analysis, and treatment may be performed by many people in the organization with varying levels of formality — the procedures provide structure while allowing adaptation to different scopes and contexts.

---

## Essential Procedures (T2+)

### PROC-RM-01: Establish Risk Management Governance
<!-- sources: ITIL 4 RM §3.2.1 Tables 3.1–3.2 Activities 1–3 -->

**Trigger:** Initiation of risk management practice, significant environmental change, regulatory change, organizational restructuring, or scheduled governance review.

**Scope:** Covers environment analysis, risk capacity and appetite definition, and risk management policy documentation. Maps to definition activities 1–3.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Analyse the environment — review and analyse the environment in which services are delivered and consumed. Identify factors that influence risk capacity, risk appetite, and the risk management approach. Consider PESTLE factors (political, economic, social, technological, legal, environmental), organizational strategy, regulatory requirements, industry trends, and changes in the service portfolio or supplier landscape | Risk Management Committee | Organizational strategy, service portfolio, service models, regulatory requirements, PESTLE analysis | Environment analysis, risk factors |
| 2 | Document risk capacity and risk appetite — define concise, holistic, and objective risk indicators that express the organization's risk capacity (maximum bearable risk) and risk appetite (acceptable risk level for different risk categories). Ensure indicators are measurable where possible and clearly communicated to all levels of management. Risk appetite may vary by domain — for example, lower appetite for compliance risks than for innovation risks | Risk Management Committee | Environment analysis, organizational strategy, financial constraints | Risk capacity and risk appetite statements |
| 3 | Document risk management policy — specify risk analysis methods (qualitative, quantitative, or both), scope of the risk management practice, treatment principles, escalation criteria, reporting requirements, review intervals, and organizational responsibilities. Ensure awareness of specific documentation requirements and regulatory obligations. Define the risk register structure and data requirements | Risk Management Committee | Environment analysis, risk capacity/appetite, regulatory requirements, organizational structure | Risk management policy |

**Exit criteria:** Environment analysed and risk factors identified. Risk capacity and risk appetite formally documented and communicated. Risk management policy established with analysis methods, scope, and responsibilities defined.

---

### PROC-RM-02: Identify, Analyse, and Treat Risks
<!-- sources: ITIL 4 RM §3.2.2 Tables 3.3–3.4 -->

**Trigger:** Scheduled risk identification interval, new project or service, security breach or incident, new partner relationship, organizational change, risks identified by other activities, or significant environmental change.

**Scope:** Covers risk identification, analysis and evaluation, and treatment selection. Maps to definition activities 4–6.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Identify risks — within the defined scope of control (project, service, business unit, etc.), identify risks using multiple techniques: review of previous risk registers, analysis of service portfolio and service models, brainstorming, tabletop exercises, stakeholder interviews (customers, users, technical staff), threat and vulnerability assessments (internal or third-party), checklists based on standards and best practices, risks identified by other parts of the organization, suggestion box or anonymous reporting, risks identified by vendors, partners, or other organizations, output of technical tools (firewall logs, intrusion detection systems), and service level reports showing trends and potential failures. Assign an owner to each identified risk who is accountable for ensuring the risk is understood and appropriate action is taken. Document risks and owners in the risk register | Risk Owner | Risk management policy, risk appetite, existing risk registers, service portfolio, service models, threat/vulnerability assessments, standards/frameworks | Updated risk register with newly identified risks |
| 2 | Analyse and evaluate risks — determine the likelihood and potential impact of each identified risk using qualitative or quantitative methods as specified in the risk management policy. For qualitative analysis, use the organization's probability × impact matrix to categorize risks by severity. For quantitative analysis, calculate annualized rate of occurrence (ARO), single loss expectancy (SLE), and annualized loss expectancy (ALE = ARO × SLE) where data permits. Based on the analysis and the organization's risk appetite, evaluate each risk to decide what level of time and budget should be used to manage it. The risk owner either performs this analysis or delegates it and reviews the findings. Update the risk register with analysis output | Risk Owner | Identified risks, risk management policy, risk appetite, analysis tools and data | Risk register updated with analysis results and risk scores |
| 3 | Select and implement treatment — choose a risk treatment option for each risk: accept (document and communicate decision), avoid (change plans to eliminate the risk), mitigate (implement controls to reduce likelihood or impact), or transfer/share (shift impact to a third party). For mitigation, select controls based on the risk management policy, standards, best practices, or situation-specific design. Risk treatment may require design, investment, development, testing, deployment, and other managed activities. Ensure treatment is fully implemented as agreed by the risk owner. Update the risk register with treatment decisions and implementation dates | Risk Owner | Risk analysis results, risk management policy, risk appetite, available controls and treatment options, budget | Risk register updated with treatment decisions, new and updated controls |

**Exit criteria:** Risks identified using multiple techniques with owners assigned. Each risk analysed using agreed methods and evaluated against risk appetite. Treatment option selected and implemented for each risk. Risk register updated throughout.

---

## Intermediate Procedures (T2+)

### PROC-RM-03: Assess and Evaluate Controls
<!-- sources: ITIL 4 RM §3.2.3 Tables 3.5–3.6 Activity 1 -->

**Trigger:** Scheduled control review interval, security incident, new or changed service, entering a relationship with a new partner, detection of control weakness, or event indicating control may no longer be fit for purpose.

**Scope:** Covers control assessment (implementation completeness), control evaluation (continuing relevance), and identification of control gaps. Maps to definition activity 8.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Plan control assessment — determine which controls to assess, assessment methods, and required evidence. Control assessment is often performed for a specific subset of controls — some controls may need to be reviewed weekly or daily in high-risk environments, while others require less frequent review. Prioritize based on risk significance and time since last assessment | Risk Owner | Risk register, control inventory, previous assessment results | Assessment plan |
| 2 | Assess control implementation — verify that controls have been fully and correctly implemented. For example: audit computers to establish they have the correct version of anti-virus software, inspect offices to verify clear desk policy adherence, review access control logs to confirm permission models are enforced. Document findings including any gaps or partial implementations | Risk Owner | Assessment plan, control specifications, evidence collection | Implementation assessment findings |
| 3 | Evaluate control relevance — analyse the continuing relevance of each assessed control to determine whether it is still fit for purpose. Assess whether the risk the control is intended to modify still exists, whether the threat landscape has changed, and whether the control remains effective in the current context. A control that was appropriate when designed may become obsolete or insufficient as the environment evolves | Risk Owner | Assessment findings, risk register, threat intelligence, environmental changes | Evaluation findings, control status updates |
| 4 | Update registers and identify gaps — update risk registers based on assessment and evaluation findings. Identify requirements for new or updated controls where gaps are found. Where assessment reveals significant issues, determine whether a full risk audit is needed. Document all findings and actions | Risk Owner | Assessment and evaluation findings | Updated risk registers, requirements for new/updated controls, audit triggers |

**Exit criteria:** Controls assessed for implementation completeness. Controls evaluated for continuing relevance. Risk registers updated with findings. Gaps identified and escalated for treatment.

---

### PROC-RM-04: Provide Direction and Monitor Risk Management
<!-- sources: ITIL 4 RM §3.2.1 Table 3.2 Activities 4–5 -->

**Trigger:** Scheduled governance review, significant audit findings, material changes in organizational risk profile, new regulatory requirements, or significant deviations from risk management policy detected.

**Scope:** Covers governance direction, communication, monitoring, and framework adjustment triggers. Maps to definition activities 7 and 10.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Provide direction to management — communicate the risk management framework, policy, and current risk appetite to all levels of management. Enable communication channels for risk reporting. Ensure ongoing engagement of managers to maintain clarity on risk management expectations. Ensure ongoing realization of risk management policies across the organization | Risk Management Committee | Risk management policy, risk appetite, organizational structure | Direction and guidance communicated |
| 2 | Monitor risk management compliance — review reports from risk owners, control assessments, and audit findings to assess whether risk management is proceeding according to the governing body's intentions. Monitor organizational performance metrics for indicators of emerging risks or risk management failures | Risk Management Committee | Risk owner reports, control assessment results, audit reports, performance metrics | Monitoring findings |
| 3 | Review and adjust governance framework — if significant deviations from intended risk management are detected, or if the environment has materially changed, trigger a re-analysis of the environment and review of risk capacity, appetite, and policy. Determine whether the risk management framework needs adjustment and initiate updates through PROC-RM-01 | Risk Management Committee | Monitoring findings, environmental change indicators, audit recommendations | Framework review trigger, updated governance decisions |

**Exit criteria:** Direction communicated to management. Compliance monitored and deviations identified. Framework adjustments triggered where significant changes are detected.

---

## Advanced Procedures (T3)

### PROC-RM-05: Conduct Risk Audits and Partner Integration
<!-- sources: ITIL 4 RM §3.2.3 Tables 3.5–3.6 Activity 2, §6 -->

**Trigger:** Scheduled audit interval, significant security incident, new service or major change, entering or exiting a relationship with a partner or supplier, or control assessment indicating broader review needed.

**Scope:** Covers risk audits, partner risk alignment, and framework effectiveness assurance. Maps to definition activity 9 and advanced aspects of partner risk management.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Plan and scope risk audit — determine audit scope, method, timeline, and resources. Audits ensure that risk management remains appropriate and relevant as the environment changes. Plan for both internal audits and engagements with external auditors as required by governance or regulation. Define audit criteria, evidence requirements, and reporting format | Risk Auditor | Risk management policy, risk registers, previous audit findings, governance requirements | Audit plan |
| 2 | Execute risk audit — conduct the audit according to the plan. Assess whether the risk management framework is being applied consistently, risks are being identified and treated appropriately, controls are effective, and the practice is delivering value. May include interviews, evidence review, process observation, and testing. Document findings including strengths, weaknesses, and recommendations | Risk Auditor | Audit plan, risk registers, control evidence, framework documentation | Audit findings |
| 3 | Produce audit report and assign actions — document audit findings, recommendations, and requirements for new or updated controls. Distribute through agreed governance channels. Assign owners for post-audit corrective actions with sufficient authority, time, and resources. Audit reports provide input to the governance process for monitoring the organization | Risk Auditor | Audit findings | Audit report, corrective action assignments |
| 4 | Align partner and supplier risk frameworks — ensure that risk management frameworks for the organization and its partners and suppliers are mutually aligned. Establish appropriate communication channels between respective risk owners. Build risk identification and proper signalling into service models with suppliers and regularly test these mechanisms. Ensure the appropriate amount of effort is invested in risk identification and analysis across the service relationship | Risk Management Committee | Supplier agreements, partner contracts, service models | Partner risk alignment arrangements, risk signalling mechanisms |
| 5 | Coordinate cross-organizational risk management — where organizations aim for fast and effective risk management, agree with partners and suppliers to close cooperation — removing formal bureaucratic barriers in communication, collaboration, and decision-making. All parties should aim for mutual transparency and visibility of changes that may affect the other parties. Ensure risk mitigation activities covered by other practices are coordinated with the overarching risk management framework | Risk Management Committee | Partner cooperation agreements, risk management frameworks | Cross-organizational risk management procedures |

**Exit criteria:** Risk audit completed with findings documented and actions assigned. Partner and supplier risk frameworks aligned with communication channels established. Cross-organizational risk management coordinated for effective and transparent cooperation.
