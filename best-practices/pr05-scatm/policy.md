---
process_id: PR05
process_name: "Service Catalogue Management"
category: policy
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
  - "ITIL 4: Service Catalogue Management §2.1, §2.4"
  - "FitSM-2: §PR2 SLM (catalogue creation and maintenance)"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Catalogue Management — Best Practice Policy

## How to Use This Policy Template

This policy establishes the governing principles and mandatory requirements for service catalogue management. It should be customized to reflect the organization's service portfolio complexity, stakeholder groups, and automation maturity. Requirements are graduated by maturity — organizations should implement Essential requirements first, then layer on Intermediate and Advanced requirements as the practice matures. This process applies at T2+ complexity.

---

## Policy Principles

### 1. Single Source of Truth
<!-- sources: ITIL 4 Service Catalogue Management §2.1, §2.4.2 -->

The service catalogue shall be maintained as a single source of consistent information about all services and service offerings. Creating separate or isolated service catalogues within different technology systems shall be avoided. A single repository of service data shall be used to generate all agreed tailored views, ensuring consistency across all stakeholder groups and eliminating the risk of contradictory information.

### 2. Stakeholder-Driven Design
<!-- sources: ITIL 4 Service Catalogue Management §2.4.1, FitSM-2 §PR2 SLM -->

The structure, scope, and views of the service catalogue shall be driven by stakeholder requirements. The catalogue shall be designed to answer the questions that stakeholders actually need answered — about service availability, service levels, request procedures, financial terms, and support arrangements. Different stakeholder groups shall receive tailored views appropriate to their role and access entitlements.

### 3. Data Quality and Currency
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2 -->

The service catalogue shall contain correct, complete, and up-to-date information at all times. Catalogue errors on user- and customer-facing views shall be treated as incidents and resolved promptly. Data update procedures shall be defined, and where possible automated, to ensure that changes in services, agreements, and configurations are reflected in the catalogue without delay.

### 4. Automation and Integration
<!-- sources: ITIL 4 Service Catalogue Management §5.2 Table 5.2 -->

Maintaining, updating, and providing the service catalogue shall be automated as much as possible. Catalogue views shall be generated and delivered through self-service portals rather than created manually upon request. The catalogue shall be integrated with other data sources — service level agreements, configuration management database, financial systems, and related records — to ensure comprehensive and current information.

### 5. Usability and Accessibility
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2 -->

The service catalogue shall have an intuitive, familiar, and smooth interface for both internal and external users. Catalogue design shall prioritize usability — new users shall be enabled for effective use, and internal and external users shall be treated equally. User experience shall be monitored and continuously improved.

### 6. Comprehensive Coverage
<!-- sources: ITIL 4 Service Catalogue Management §2.1, FitSM-2 §PR1 SPM -->

The service catalogue shall cover all services managed by the organization — including internal, external, provided, and consumed services. Third-party services that are consumed by the organization and that the organization's services depend on shall also be represented in relevant catalogue views.

### 7. Continual Improvement
<!-- sources: ITIL 4 Service Catalogue Management §2.4.1 -->

The service catalogue design, structure, content, and views shall be subject to continual improvement. Improvement sources include regular reviews, user feedback, changes in requirements, changes in the organization's architecture, and technology opportunities. Stakeholder satisfaction and catalogue usage patterns shall be monitored and used as improvement inputs.

---

## Mandatory Requirements

### Essential (All tiers)
<!-- sources: ITIL 4 Service Catalogue Management §2.4.1, §3.2.1, FitSM-2 §PR2 SLM -->

| # | Requirement |
|---|-------------|
| 1 | The organization shall define and document the service catalogue data structure — including core service data attributes (service name, description, status, owner, target audience), view-specific attributes, data sources, and relationships |
| 2 | Stakeholder groups requiring catalogue access shall be identified and their requirements analysed — covering scope, granularity, data sources, and access controls |
| 3 | Standard service catalogue views shall be defined for key stakeholder groups — at minimum a user view, customer view, and service provider view — and agreed with stakeholders |
| 4 | Service catalogue data shall be collected, entered, and maintained following the agreed structure. Data update procedures shall be defined |
| 5 | The service catalogue shall cover all live services provided to customers that are in scope of the service management system |

### Intermediate (T2+)
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2, §3.2.2 -->

| # | Requirement |
|---|-------------|
| 6 | Service catalogue views shall be made available to stakeholders through automated self-service mechanisms. Access shall be validated against entitlement and access control rules |
| 7 | Catalogue data quality shall be monitored on an ongoing basis. Errors and inconsistencies in user- and customer-facing catalogue information shall be treated as incidents |
| 8 | User feedback shall be collected and processed on a regular basis or triggered by validation failures. Feedback shall inform catalogue design improvements |
| 9 | A request catalogue shall be maintained providing users with details on available service requests for existing and new services |

### Advanced (T3)
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2, §6 -->

| # | Requirement |
|---|-------------|
| 10 | The service catalogue shall be integrated with suppliers' data sources and, where applicable, their service catalogues — ensuring seamless updates without delays that impact information quality |
| 11 | Catalogue usability shall be measured and optimized — including monitoring of use patterns, search requests, and view settings to identify improvement opportunities |
| 12 | Security policies and contract obligations shall not be compromised when providing suppliers with access to catalogue information — access levels shall be defined and controlled |

---

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Service Portfolio Management Policy (PR01) | The service portfolio is the primary source for catalogue content. Portfolio lifecycle decisions trigger catalogue updates |
| Service Level Management Policy (PR02) | SLA information is a key data source for catalogue views |
| Service Financial Management Policy (PR03) | Financial data is included in relevant catalogue views |
| Service Request Management Policy (PR12) | The request catalogue supports service request fulfilment |
| Service Configuration Management Policy (PR17) | Configuration data enriches catalogue views |
| Information Security Management Policy (PR09) | Access controls and data classification apply to catalogue views |
| Relationship Management Policy (PR22) | Customer and user requirements drive catalogue design |
| Supplier Management Policy (PR23) | Supplier services and contracts are reflected in catalogue views |
