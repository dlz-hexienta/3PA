---
process_id: PR21
process_name: "Risk Management"
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
  - "ITIL 4: Risk Management §2.1–§2.5, §3.2.1–§3.2.3, §4.1, §5, §6"
  - "IT4IT: S2P Value Stream"
last_updated: 2026-03-14
status: draft
---

# Risk Management — Best Practice Process Definition

## How to Use This Definition

This process definition provides the reference model for risk management at three maturity levels. Organizations should implement Essential elements first, then layer on Intermediate and Advanced capabilities as the practice matures. Risk management has no dedicated FitSM process — this definition draws primarily from ITIL 4 with IT4IT S2P value stream alignment. Risk management is one of the practices that underpins everything the service provider does to enable value co-creation — the practice is everyone's responsibility within their scope of control.

---

## Purpose
<!-- sources: ITIL 4 RM §2.1 -->

To ensure that the organization understands and effectively handles risks — identifying potential threats and opportunities, evaluating their likelihood and impact, and determining appropriate responses that protect the organization's ability to create value while enabling it to capitalize on opportunities.

---

## Key Concepts

### 1. Risk: Threats and Opportunities
<!-- sources: ITIL 4 RM §2.2.1 -->

Risk is a possible event that could cause harm or loss, or make it more difficult to achieve objectives — but risk can also be defined as uncertainty of outcome, encompassing both positive opportunities and negative threats. In service management, risks relate to the organization's ability to deliver and consume services effectively. An effective risk management practice addresses both positive risks (opportunities to be exploited) and negative risks (threats to be mitigated), recognizing that the absence of risk management does not eliminate risk — it merely leaves risks unmanaged.

### 2. Risk Capacity and Risk Appetite
<!-- sources: ITIL 4 RM §2.2.2 -->

Risk capacity is the maximum amount of risk that an organization can bear — the absolute limit beyond which the organization's viability is threatened. Risk appetite is the amount of risk that an organization is willing to accept in pursuit of its objectives — always less than or equal to risk capacity. Risk appetite varies by context — an organization may have higher appetite for innovation risks than for compliance risks. Both risk capacity and risk appetite should be formally documented, communicated, and reviewed as part of risk management governance. They provide the framework within which all risk evaluation and treatment decisions are made.

### 3. Risk Register
<!-- sources: ITIL 4 RM §2.2.3 -->

The risk register is the primary artefact for recording and tracking identified risks throughout their lifecycle. Each entry typically captures: risk description, risk category, likelihood assessment, impact assessment, risk score or rating, risk owner, current status, treatment option selected, controls in place, residual risk level, review dates, and related actions. The risk register is a living document — updated as risks are identified, analysed, treated, and reviewed. Multiple risk registers may exist for different scopes (organizational, project, service, team) but should be consolidated for governance purposes.

### 4. Risk Treatment Options
<!-- sources: ITIL 4 RM §2.2.4, Table 2.1 -->

Four fundamental treatment options are available for each identified risk. Risk acceptance means acknowledging the risk and choosing to take no action — the decision must be documented and communicated to appropriate stakeholders. Risk avoidance means changing plans or activities to eliminate the risk entirely. Risk mitigation (modification) means implementing controls to reduce the likelihood or impact of the risk. Risk transfer (sharing) means shifting the impact of the risk to a third party — through insurance, outsourcing, or contractual arrangements. The choice of treatment depends on the risk's relationship to risk appetite, the cost-benefit analysis of treatment options, and the availability of effective controls.

### 5. Controls
<!-- sources: ITIL 4 RM §2.2.5, Table 2.2 -->

Controls are measures implemented to manage risks — reducing likelihood, limiting impact, or both. Controls are categorized by their function: preventive controls reduce the likelihood of a risk event occurring (access controls, training, procedures), detective controls identify risk events when they occur (monitoring, auditing, alerts), corrective controls limit the impact of risk events that have occurred (disaster recovery, incident response), and directive controls direct behaviour to reduce risk (policies, standards, guidelines). Effective risk management requires a balanced portfolio of control types appropriate to the risks being managed.

### 6. Risk Analysis Methods
<!-- sources: ITIL 4 RM §2.2.6 -->

Risk analysis determines the likelihood and potential impact of each identified risk using methods specified in the risk management policy. Qualitative analysis uses descriptive scales (probability × impact matrices) to categorize risks by severity — suitable for most risk assessment contexts and enabling consistent comparison. Quantitative analysis uses numerical methods to calculate expected loss values — including annualized rate of occurrence (ARO), single loss expectancy (SLE), and annualized loss expectancy (ALE = ARO × SLE). Quantitative methods provide more precise inputs for cost-benefit analysis of treatment options but require more data and expertise. The residual risk remaining after treatment should also be assessed to confirm it falls within risk appetite.

---

## Scope
<!-- sources: ITIL 4 RM §2.3 -->

Risk management is a broad practice that spans all organizational activities — every practice, project, and service involves risk that must be identified and managed. The practice provides the governance framework, analysis methods, treatment approaches, and monitoring mechanisms that enable consistent risk management across the organization. While the actual risk mitigation activities are often performed by other practices (information security management, service continuity management, supplier management), the risk management practice ensures the overarching framework is in place, parties are aligned, and appropriate investment is made in risk identification and analysis.

---

## Practice Success Factors
<!-- sources: ITIL 4 RM §2.4 -->

### PSF1: Establishing and Maintaining Effective Risk Management Governance

The organization establishes and maintains a risk management governance framework that defines risk capacity, risk appetite, risk management policy, analysis methods, scope, and organizational responsibilities. The governing body provides direction and monitors the organization to ensure risk management proceeds according to its intentions.

### PSF2: Developing a Risk-Aware Culture and Identifying Risks Effectively

The organization develops a culture where risk awareness is embedded into everyday activities. Risks are identified systematically using multiple techniques and sources, with each risk assigned an owner who is accountable for ensuring the risk is understood and appropriate action is taken.

### PSF3: Analysing and Evaluating Risks Systematically

The organization applies consistent qualitative and/or quantitative analysis methods to determine the likelihood and impact of identified risks. Based on risk appetite, each risk is evaluated to determine appropriate investment of time and budget for management. Analysis and evaluation decisions are informed and documented.

### PSF4: Treating Risks and Monitoring Effectiveness

The organization selects and implements appropriate treatment options for each risk, implements controls, and continuously monitors and reviews the effectiveness of risk management through control assessments and risk audits. The risk management framework remains appropriate and relevant as the environment changes.

---

## Activities

### Essential (T2+)

<!-- sources: ITIL 4 RM §3.2.1 Tables 3.1–3.2, §3.2.2 Tables 3.3–3.4 -->

| # | Activity | Description |
|---|----------|-------------|
| 1 | Analyse the environment | The governing body (risk management committee on behalf of the board of directors) reviews and analyses the environment in which services are delivered and consumed — identifying factors that influence risk capacity, appetite, and management approach. Considers PESTLE factors (political, economic, social, technological, legal, environmental) and changes in the organizational context |
| 2 | Document risk capacity and risk appetite | Define concise and holistic risk indicators that express the organization's risk capacity (maximum bearable risk) and risk appetite (acceptable risk level). Ensure these are objective, measurable where possible, and clearly communicated so that all risk evaluation and treatment decisions reference a consistent framework |
| 3 | Document risk management policy | Document the risk management policy — specifying risk analysis methods (qualitative, quantitative, or both), scope, treatment principles, escalation criteria, reporting requirements, and organizational responsibilities. Ensure awareness of specific documentation requirements and regulatory obligations |
| 4 | Identify risks | Identify risks within a specific scope of control — project risks, service risks, operational risks, etc. Use multiple techniques: review of previous risk registers, analysis of service portfolio and service models, brainstorming, tabletop exercises, stakeholder interviews, threat and vulnerability assessments, checklists based on standards, risks identified by other parts of the organization, suggestion mechanisms, vendor and partner identified risks, technical tool outputs, and service level reports. Assign an owner to each identified risk who is accountable for ensuring the risk is understood and appropriate action is taken. Document risks and owners in the risk register |
| 5 | Analyse and evaluate risks | Analyse the likelihood and potential impact of each identified risk using qualitative or quantitative methods as specified in the risk management policy. Based on the analysis and the organization's risk appetite, evaluate each risk to decide what level of time and budget should be used to manage it. The risk owner either performs this analysis or delegates it and reviews the findings. Update the risk register with analysis and evaluation output |

### Intermediate (T2+)

<!-- sources: ITIL 4 RM §3.2.2 Table 3.4, §3.2.1 Table 3.2 -->

| # | Activity | Description |
|---|----------|-------------|
| 6 | Treat risks | Select a risk treatment option for each risk (accept, avoid, mitigate, transfer/share). If accepted, document the decision and communicate to appropriate stakeholders. For mitigation, select controls based on the risk management policy, standards, best practices, or situation-specific design. Risk treatment may require design, investment, development, testing, deployment, and other activities — manage these to ensure treatment is fully implemented as agreed by the risk owner. Update the risk register with treatment decisions and implementation dates |
| 7 | Provide direction to management | The governing body provides direction and guidance to management on risk management implementation — enabling communication channels, ensuring ongoing engagement of managers for clarity, and ensuring ongoing realization of risk management policies. Direction covers risk management framework application, resource allocation, and priority setting |
| 8 | Assess and evaluate controls | Assess the extent to which controls have been fully and correctly implemented, that they are still fit for purpose, and that they provide the level of risk management required. Control assessment analyses implementation completeness. Control evaluation analyses continuing relevance — determining whether the risk the control is intended to modify still exists. Often performed for specific control subsets on varying frequencies. May result in register updates, identification of need for new controls, or a need for risk audit |

### Advanced (T3)

<!-- sources: ITIL 4 RM §3.2.3 Tables 3.5–3.6, §3.2.1 Table 3.2 -->

| # | Activity | Description |
|---|----------|-------------|
| 9 | Conduct risk audits and reviews | Ensure that risk management remains appropriate and relevant as the environment changes. Audits are usually performed on a scheduled basis but may be triggered by events such as security incidents, new services, or entering relationships with new partners. May be performed internally or by third parties. Audit output may identify the need to implement new or updated controls, and provides input to the governance process for monitoring the organization |
| 10 | Monitor the organization and review governance | The governing body reviews audit reports and monitors the organization to ensure that risk management is proceeding according to its intentions. If significant deviations are detected, this may trigger a requirement to re-analyse the environment and review risk capacity, appetite, and policy. This activity ensures the risk management framework remains aligned with the organization's evolving context and objectives |

---

## Inputs

<!-- sources: ITIL 4 RM §3.2.1 Table 3.1, §3.2.2 Table 3.3, §3.2.3 Table 3.5 -->

| # | Input | Source |
|---|-------|--------|
| 1 | Organizational strategy and objectives | Governance, Service Portfolio Management |
| 2 | Service portfolio and service models | Service Portfolio Management, Service Design |
| 3 | Existing risk registers | Previous risk management cycles |
| 4 | Standards and frameworks (ISO 31000, COSO, etc.) | External sources |
| 5 | Threat and vulnerability assessment services | Information Security Management, third parties |
| 6 | Risks identified as part of other activities | All practices |
| 7 | Budget for risk management | Service Financial Management |
| 8 | Risk management policy and risk appetite | Governance |
| 9 | Audit reports and compliance records | Internal audit, external audit |

---

## Outputs

<!-- sources: ITIL 4 RM §3.2.1 Table 3.1, §3.2.2 Table 3.3, §3.2.3 Table 3.5 -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Risk management policy | All practices, stakeholders |
| 2 | Risk capacity and risk appetite statements | All practices, governance |
| 3 | Direction and guidance for management | All management levels |
| 4 | Updated risk registers | All practices, governance |
| 5 | New and updated controls | All practices |
| 6 | Audit reports | Governance, all practices |
| 7 | Requirements for new and updated controls | Change Management, Information Security Management |
| 8 | Risk management framework documentation | All practices |
| 9 | Risk assessment reports | Service Portfolio Management, project management |

---

## Roles

<!-- sources: ITIL 4 RM §4.1 Table 4.2, §4.2 -->

| Role | Abbreviation | Tier | Description |
|------|:------------:|:----:|-------------|
| Risk Management Committee Member | RMC | T2+ | Member of the governing body (or committee acting on behalf of the board of directors) responsible for establishing and maintaining the risk management framework. Analyses the environment, documents risk capacity and appetite, develops risk management policy, provides direction to management, and monitors the organization. May be a dedicated committee or integrated into existing governance structures. Competency profiles: MC for environment analysis, MC for capacity/appetite, MCL for policy, LC for direction, CAM for monitoring |
| Risk Owner | RO | T2+ | Any subject matter expert, service owner, or product owner who is assigned ownership of a specific risk and is accountable for ensuring the risk is understood, analysed, evaluated, and appropriately treated. The risk owner either performs analysis and evaluation or delegates it and reviews findings. Responsible for implementing or overseeing risk treatment and ensuring controls are effective. Competency profiles: MTC for identification, TML for analysis, CAM for treatment |
| Risk Auditor | RA | T3 | Member of an audit committee or external auditor (mandated by the board of directors) responsible for conducting risk audits and control assessments to ensure risk management remains appropriate and relevant. Performs or oversees audits internally or through third parties. Provides independent assurance of risk management effectiveness. Competency profile: CAMT |

---

## Artefacts

<!-- sources: ITIL 4 RM §2.2.3, §3.2.1–§3.2.3 -->

| # | Artefact | Purpose |
|---|----------|---------|
| 1 | Risk Register | Records all identified risks with their descriptions, categories, likelihood and impact assessments, risk scores, owners, treatment decisions, controls, residual risk levels, review dates, and related actions |
| 2 | Risk Management Policy | Defines analysis methods, treatment principles, scope, escalation criteria, reporting requirements, and organizational responsibilities for risk management |
| 3 | Risk Capacity and Appetite Statements | Document the organization's maximum bearable risk and acceptable risk levels — providing the framework for all risk evaluation and treatment decisions |
| 4 | Risk Audit Reports | Record audit findings, control assessment results, compliance status, recommendations, and requirements for new or updated controls |
| 5 | Risk Management Framework Documentation | Comprehensive documentation of the risk management framework including methods, scope, objects, role descriptions, and integration with organizational practices |

---

## Interfaces

<!-- sources: ITIL 4 RM §3.2.1–§3.2.3, §5.1, §6 -->

| # | Practice | Interface Description |
|---|----------|----------------------|
| 1 | Information Security Management (PR09) | Security risks are a major category in the risk register; ISM provides threat and vulnerability assessments; security controls implement risk treatment decisions |
| 2 | Service Continuity Management (PR07) | Continuity risks and business impact analysis; continuity plans implement risk treatment for availability and disaster scenarios |
| 3 | Availability Management (PR06) | Availability risks and single points of failure; availability design implements risk mitigation for service availability threats |
| 4 | Change Management (PR15) | Changes carry risks that must be assessed; risk treatment actions may require changes to implement controls |
| 5 | Service Portfolio Management (PR01) | Strategic risks associated with the service portfolio; risk assessment informs portfolio decisions and investment priorities |
| 6 | Supplier Management (PR23) | Supplier risks must be identified, assessed, and managed; partner risk management frameworks must be mutually aligned with appropriate communication channels |
| 7 | Continual Improvement (PR24) | Risk management improvement initiatives; improvement proposals may introduce or modify risks requiring assessment |
| 8 | Service Level Management (PR02) | Service level reports showing trends and potential failures feed into risk identification; risk appetite informs SLA negotiation |
| 9 | Monitoring & Event Management (PR14) | Technical monitoring tools provide operational risk signals; automated detection supports risk identification |
| 10 | Knowledge Management (PR19) | Risk information as knowledge; risk management methods and frameworks stored as knowledge assets |
| 11 | Service Financial Management (PR03) | Budget for risk management activities; financial impact assessment of risks; cost-benefit analysis of treatment options |
| 12 | Measurement & Reporting (PR20) | Risk management metrics and reporting; risk dashboard and governance reporting |
