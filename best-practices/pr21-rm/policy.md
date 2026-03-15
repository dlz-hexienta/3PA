---
process_id: PR21
process_name: "Risk Management"
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
  - "ITIL 4: Risk Management §2.1, §2.2, §2.3, §2.4, §2.5, §5.1, §6"
  - "IT4IT: S2P Value Stream"
last_updated: 2026-03-14
status: draft
---

# Risk Management — Best Practice Policy

## How to Use This Policy Template

This policy establishes the governing principles and mandatory requirements for the risk management practice. It should be customized to reflect the organization's risk profile, regulatory environment, governance structure, and industry context. Requirements are graduated by maturity — organizations should implement Essential requirements first, then layer on Intermediate and Advanced requirements as the practice matures. Risk management has no dedicated FitSM process — this policy draws primarily from ITIL 4 with IT4IT S2P alignment.

---

## Policy Principles

### 1. Risk Management as a Foundation
<!-- sources: ITIL 4 RM §2.1, §4.2 -->

Risk management shall be recognized as a foundational practice that underpins everything the service provider does to enable value co-creation. The practice is everyone's responsibility within their scope of control. All tiers of management shall implement the risk management framework within their scopes. Risk management shall not be treated as an isolated compliance exercise but as an integral part of decision-making at all levels.

### 2. Governance and Accountability
<!-- sources: ITIL 4 RM §2.2.2, §3.2.1 -->

The governing body shall be ultimately accountable for establishing and maintaining an adequate risk management framework. Risk capacity and risk appetite shall be formally documented, communicated, and reviewed. Every identified risk shall have an assigned owner who is accountable for ensuring the risk is understood, analysed, and appropriately treated. The risk management framework shall define analysis methods, scope, treatment principles, and organizational responsibilities.

### 3. Balanced Risk Perspective
<!-- sources: ITIL 4 RM §2.2.1 -->

Risk management shall address both negative risks (threats) and positive risks (opportunities). The practice shall protect the organization from harm while enabling it to capitalize on opportunities for improvement and innovation. Risk decisions shall balance the cost of treatment against the potential impact of the risk, informed by the organization's risk appetite.

### 4. Evidence-Based Analysis
<!-- sources: ITIL 4 RM §2.2.6, §3.2.2 Table 3.4 -->

Risk analysis shall be based on evidence and consistent methods — using qualitative analysis (probability × impact matrices), quantitative analysis (ARO, SLE, ALE), or both as specified in the risk management policy. Analysis methods shall be applied consistently across the organization to enable meaningful comparison and prioritization. Risk evaluation decisions shall be documented and traceable.

### 5. Proportionate Response
<!-- sources: ITIL 4 RM §2.2.4, Table 2.1 -->

Risk treatment shall be proportionate to the significance of the risk and the organization's risk appetite. The four treatment options — accept, avoid, mitigate, and transfer/share — shall be applied based on cost-benefit analysis, availability of effective controls, and organizational context. Accepted risks shall be formally documented and communicated. Residual risk remaining after treatment shall be assessed to confirm it falls within risk appetite.

### 6. Layered Controls
<!-- sources: ITIL 4 RM §2.2.5, Table 2.2 -->

The organization shall maintain a balanced portfolio of controls — preventive, detective, corrective, and directive — appropriate to the risks being managed. Controls shall be designed, implemented, assessed for effectiveness, and reviewed for continuing relevance. No single control type shall be relied upon in isolation for significant risks.

### 7. Continual Monitoring and Improvement
<!-- sources: ITIL 4 RM §3.2.3, §3.2.1 Table 3.2 Activity 5 -->

Risk management shall be subject to continual monitoring and review. Controls shall be assessed for implementation completeness and continuing relevance. Risk audits shall ensure the practice remains appropriate as the environment changes. The governing body shall monitor the organization and trigger framework reviews when significant deviations are detected.

---

## Mandatory Requirements

### Essential (T2+)
<!-- sources: ITIL 4 RM §2.2, §2.3, §3.2.1, §3.2.2 -->

| # | Requirement |
|---|-------------|
| 1 | The organization's risk capacity (maximum bearable risk) and risk appetite (acceptable risk level) shall be formally documented, communicated to all relevant parties, and reviewed at planned intervals |
| 2 | A risk management policy shall be established — defining risk analysis methods, scope, treatment principles, escalation criteria, reporting requirements, and organizational responsibilities |
| 3 | A risk register shall be established and maintained as the primary artefact for recording identified risks — capturing risk description, category, likelihood, impact, risk score, owner, treatment decision, controls, residual risk, and review dates |
| 4 | Every identified risk shall be assigned an owner who is accountable for ensuring the risk is understood, analysed, evaluated, and appropriately treated within agreed timeframes |
| 5 | Risk identification shall be performed systematically — using multiple techniques and sources, at planned intervals and in response to significant events — within defined scopes of control |

### Intermediate (T2+)
<!-- sources: ITIL 4 RM §3.2.2, §3.2.1, §3.2.3 -->

| # | Requirement |
|---|-------------|
| 6 | Risk analysis shall be performed using qualitative and/or quantitative methods as specified in the risk management policy — determining the likelihood and potential impact of each identified risk and evaluating against the organization's risk appetite |
| 7 | Risk treatment decisions shall be documented in the risk register — specifying the treatment option selected, controls to be implemented, implementation timelines, and expected residual risk level. Accepted risks shall be formally documented and communicated to appropriate stakeholders |
| 8 | The governing body shall provide direction to management on risk management implementation — ensuring communication channels are established, managers are engaged, and risk management policies are being realized |
| 9 | Controls shall be assessed and evaluated at planned intervals — verifying that controls are fully and correctly implemented, still fit for purpose, and providing the required level of risk management |

### Advanced (T3)
<!-- sources: ITIL 4 RM §3.2.3, §6 -->

| # | Requirement |
|---|-------------|
| 10 | Risk audits shall be conducted at planned intervals and in response to significant events — ensuring risk management remains appropriate and relevant as the environment changes. Audits may be performed internally or by independent third parties |
| 11 | Risk management frameworks for the organization and its partners and suppliers shall be mutually aligned — with appropriate communication channels established between respective risk owners, risk identification built into service models with suppliers, and regular testing of risk signalling mechanisms |
| 12 | The governing body shall monitor the organization against the risk management framework — reviewing audit reports, assessing compliance with risk management policies, and triggering framework reviews when significant deviations or environmental changes are detected |

---

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Information Security Management Policy (PR09) | Security risk identification, threat and vulnerability assessments, security controls implementation |
| Service Continuity Management Policy (PR07) | Business impact analysis, continuity risks, disaster recovery as risk treatment |
| Availability Management Policy (PR06) | Availability risks, single points of failure, availability design as risk mitigation |
| Change Management Policy (PR15) | Change risk assessment, risk treatment through controlled change implementation |
| Service Portfolio Management Policy (PR01) | Strategic risk assessment for portfolio decisions, investment risk evaluation |
| Supplier Management Policy (PR23) | Supplier risk identification and management, mutual risk framework alignment |
| Service Financial Management Policy (PR03) | Risk management budgeting, financial impact assessment, cost-benefit analysis of controls |
| Continual Improvement Policy (PR24) | Risk management improvement initiatives, risk assessment of improvement proposals |
