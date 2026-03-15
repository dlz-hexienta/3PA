---
process_id: PR23
process_name: "Supplier Management"
category: policy
frameworks:
  - itil-v4
  - fitsm
  - it4it
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Supplier Management §2.1, §2.3, §2.4"
  - "FitSM-2: §PR8 SUPPM"
  - "IT4IT: S2P Value Stream"
  - "SIAM: Service Integration (supplier coordination)"
last_updated: 2026-03-13
status: draft
---

# Supplier Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Supplier Management §2.1, §2.4, FitSM-2 §PR8 SUPPM -->

The organization shall ensure that all suppliers and their performances are managed appropriately to support the seamless provision of quality products and services. This shall be achieved through a common approach to sourcing strategy and supplier management that is aligned with the organization's overall strategy, maintains a single point of control over active and planned supplier contracts, and promotes closer, more collaborative relationships with key suppliers. The organization shall evaluate and select suppliers against defined criteria, negotiate and manage contracts through their lifecycle, monitor supplier performance against agreed targets, and conduct periodic supplier reviews. Supplier risk and compliance shall be actively managed throughout the supplier journey. The organization shall categorize its suppliers according to their importance and manage each relationship with effort proportionate to its significance.

## Objectives
<!-- sources: ITIL 4 Supplier Management §2.4 PSFs, FitSM-2 §PR8 SUPPM -->

1. Ensure that the sourcing strategy and guidelines effectively support the organization's strategy — defining which resources are sourced externally, the categorization of suppliers, and the standards for evaluation, contracting, and performance management
2. Ensure that service relationships with all suppliers and partners are managed effectively and in line with internal and external regulations — from evaluation and selection through contracting, service delivery, and review
3. Ensure the effective integration of third-party services into the organization's products and services — understanding dependencies, managing risks, and maintaining service quality through supplier transitions
4. Establish and maintain healthy relationships with internal and external suppliers and monitor their performance against agreed targets
5. Ensure that supplier contracts represent value for money and that costs are optimal relative to the quality and risks of the services consumed
6. Prevent and resolve conflicts with suppliers through established governance mechanisms, collaboration frameworks, and clear contractual terms

## Scope

This policy applies to all supplier relationships that the organization maintains in the course of managing and delivering its services. It covers:

- All external suppliers providing services, products, or resources to the organization
- All internal suppliers (internal teams or departments operating under formal OLAs) where formal supplier management applies
- All stages of the supplier journey — from identification and selection through contracting, onboarding, service delivery, performance management, review, and offboarding
- All roles with responsibility for supplier management, from organizational leaders through to staff who interact with suppliers operationally
- The sourcing strategy, supplier categorization, and governance arrangements that shape how supplier relationships are conducted

## Principles

### P1. Strategy-Aligned Sourcing
<!-- sources: ITIL 4 Supplier Management §2.4.1 -->
The organization's sourcing strategy shall be aligned with and support the overall organizational strategy. The strategy shall define which resources are sourced internally and which externally, and to what extent. It shall include supplier categorization criteria, evaluation and selection standards, contracting principles, and the overall approach to managing third-party relationships. Policies and guidelines defined in the sourcing strategy shall be consistently applied across all sourcing decisions.

### P2. Value for Money
<!-- sources: ITIL 4 Supplier Management §2.4.1 -->
The organization shall ensure that supplier contracts are cost-effective and provide value for money. This shall be measured not only in terms of direct cost but also in terms of year-on-year benefit, potential value from innovation and transformation, risk reduction, and alignment with the organization's strategic objectives. Managing suppliers includes ensuring that contracts deliver proportionate value relative to their cost and risk.

### P3. Risk-Based Supplier Management
<!-- sources: ITIL 4 Supplier Management §3.2.2 Table 3.4, §2.4.1 -->
Supplier risk shall be identified, assessed, and managed throughout the entire supplier journey — from initial due diligence during evaluation and selection, through ongoing risk monitoring during service delivery, to risk assessment during contract renewal or termination decisions. The supplier risk register shall be actively maintained. Governance structures shall focus on managing supplier risks, contractual adherence, compliance, and the conduct of supplier audits.

### P4. Performance-Driven Relationships
<!-- sources: ITIL 4 Supplier Management §2.2.1, §2.4.2 -->
All suppliers shall be evaluated and assessed for their performance and value realization against defined performance targets. Performance measurement parameters shall be clearly articulated in contracts and shall be appropriate to the type of service relationship — warranty-focused for basic relationships, extending to innovation and collaboration for partnership relationships. Supplier performance reports and scorecards shall inform decisions on reward, penalty, contract renewal, or termination.

### P5. Proportionate Engagement
<!-- sources: ITIL 4 Supplier Management §2.4.2, §3.2.2 Table 3.4 -->
The level of management effort, governance, and performance monitoring applied to each supplier shall be proportionate to the supplier's significance to the organization. Suppliers shall be categorized based on their importance, the type of service relationship, and the associated risks and dependencies. Strategic and partnership suppliers shall receive the most intensive engagement; generic and commodity suppliers shall be managed with appropriate but lighter-touch controls.

### P6. Effective Third-Party Integration
<!-- sources: ITIL 4 Supplier Management §2.4.3 -->
The organization shall ensure the effective integration of third-party services into its own products and services. This requires understanding the scope, nature, and terms of external services, understanding their dependencies and risks, and considering these from the early stages of product design and service lifecycle. Supplier onboarding and offboarding shall be managed with defined procedures that maintain service continuity and update the supplier dependency matrix.

### P7. Lifecycle Contract Management
<!-- sources: ITIL 4 Supplier Management §2.2, §3.2.2 Table 3.4 -->
Supplier contracts shall be managed through their full lifecycle — from creation and negotiation through execution, amendment, renewal, and termination. The organization shall maintain an appropriate structure for formulating contracts, evaluating and negotiating contract terms, and reviewing contracts for renewal or termination. The level of contract formality shall reflect the type of service relationship — more formal for lower-trust relationships, more flexible for established partnerships.

## Mandatory Requirements

### Essential (All organizations implementing this process)

| ID | Requirement |
|----|------------|
| SUPPM-R01 | A supplier database shall be maintained with current contact and contract information for all internal and external suppliers |
| SUPPM-R02 | Supplier evaluation and selection criteria shall be defined, documented, and consistently applied to all supplier selection decisions |
| SUPPM-R03 | Supplier contracts shall document roles, responsibilities, service descriptions, service level targets, performance measurement parameters, terms and conditions, and reward or penalty mechanisms |
| SUPPM-R04 | Supplier performance shall be monitored against agreed targets at defined intervals, with performance reports produced |
| SUPPM-R05 | Periodic supplier reviews shall be conducted to discuss performance, compliance, issues, and improvement opportunities |
| SUPPM-R06 | Follow-up actions for insufficient supplier performance shall be agreed with the supplier, documented, and tracked to completion |
| SUPPM-R07 | A supplier manager role shall be assigned with accountability for the overall management of supplier relationships and performance |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| SUPPM-R08 | A sourcing strategy shall be documented, aligned with the organizational strategy, and include supplier categorization, evaluation standards, contracting principles, and performance measurement standards |
| SUPPM-R09 | Suppliers shall be categorized by importance and relationship type (generic/commodity, operational/tactical, strategic/partner), with management effort proportionate to significance |
| SUPPM-R10 | Formal onboarding and offboarding procedures shall be in place, covering service integration, access management, dependency matrix updates, and risk identification |
| SUPPM-R11 | Supplier governance structures shall be established for monitoring compliance, managing risk, and conducting periodic audits |
| SUPPM-R12 | Compliance audits shall be conducted at defined intervals, with the supplier risk register actively maintained |
| SUPPM-R13 | The supplier dependency matrix shall be maintained and used for impact analysis, sourcing decisions, and risk management |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| SUPPM-R14 | The sourcing strategy and supplier management procedures shall be subject to periodic review and adjustment based on measured outcomes, lessons learned, and strategic changes |
| SUPPM-R15 | In multi-supplier environments, cross-supplier integration and collaboration shall be actively managed, with collaboration clauses in contracts and shared governance arrangements |
| SUPPM-R16 | Supplier value realization assessments shall be conducted periodically, evaluating not only operational performance but also strategic contribution, innovation, and year-on-year value |
| SUPPM-R17 | Multi-dimensional supplier scorecards shall be used to provide comprehensive performance and value assessments across all evaluation parameters |

## Compliance and Review

- This policy shall be reviewed at least annually or following a significant change to the organization's strategy, supplier landscape, or sourcing requirements
- Compliance with this policy shall be assessed through supplier reviews, performance reports, compliance audits, and governance meeting outcomes
- Non-compliance shall be escalated to the supplier manager and organizational leadership for remediation
- Exceptions to this policy require documented justification and approval from the supplier manager or senior leadership

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Relationship Management Policy (PR22) | Supplier relationships follow the same relationship principles; relationship management owns stakeholder engagement, supplier management owns contractual and performance aspects |
| Service Level Management Policy (PR02) | SLAs, OLAs, and UAs provide the service level framework for supplier contracts; service level data informs supplier performance evaluation |
| Service Portfolio Management Policy (PR01) | Portfolio decisions drive sourcing needs; supplier capabilities inform portfolio planning |
| Service Configuration Management Policy (PR17) | Supplier services and their dependencies are documented as CIs in the CMS |
| Service Financial Management Policy (PR03) | Budgetary and financial considerations inform sourcing decisions and contract value assessments |
| Risk Management Policy (PR21) | Supplier risk assessments and the supplier risk register feed the organization's overall risk management |
| Information Security Management Policy (PR09) | Security requirements govern supplier access to organizational resources and are embedded in supplier contracts |
| Continual Improvement Policy (PR24) | Supplier assessment results and improvement initiatives feed the continual improvement register |
