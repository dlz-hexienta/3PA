---
process_id: PR04
process_name: "Service Design"
category: policy
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T3
sources:
  - "ITIL 4: Service Design §2.1, §2.2, §2.4"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Design — Best Practice Policy

## How to Use This Policy Template

This policy establishes the governing principles and mandatory requirements for service design. It should be customized to reflect the organization's product and service portfolio, risk appetite, design maturity, and delivery methodology (waterfall, Agile, hybrid). Requirements are graduated by maturity — organizations should implement Essential requirements first, then layer on Intermediate and Advanced requirements as the practice matures. This process applies only at T3 (full SMS) complexity.

---

## Policy Principles

### 1. Holistic Design
<!-- sources: ITIL 4 Service Design §2.1 -->

Service design shall adopt a holistic, results-driven approach to all aspects of design. Products and services shall not be designed in isolation — every design must consider the impact on other products and services, all relevant parties including customers, users, and suppliers, the existing architectures, the required technology, the service management practices, and the necessary measurements and metrics. Management and operational requirements shall be regarded as a fundamental part of the design, not added as an afterthought.

### 2. Customer and User Centricity
<!-- sources: ITIL 4 Service Design §2.2.2 -->

Customer experience (CX) and user experience (UX) shall be at the centre of all service design activities. Service design shall ensure that products and services deliver the desired value by managing every aspect of the complete customer experience — including time, quality, cost, reliability, and effectiveness — and by ensuring ease of use for all users. Service design shall recognize that value is co-created with consumers and shall dynamically respond to consumer behaviour.

### 3. Risk-Aligned Design
<!-- sources: ITIL 4 Service Design §2.2.4.3, §2.2.5 -->

The level of design activity shall be proportionate to the level of risk. Service design shall ensure that products and services are designed to capabilities matched to their risk profile. Operating models — including the supplier ecosystem — shall be appropriate to the level of risk posed to the organization. Where multiple service providers are engaged, roles, responsibilities, and collaboration models shall be established and documented.

### 4. Iterative and Incremental Approach
<!-- sources: ITIL 4 Service Design §2.1, §2.2.1 -->

Service design shall consider iterative and incremental approaches that enable products and services to continually adapt in alignment with evolving needs. Design thinking — combining inspiration, ideation, prototyping, implementation, and evaluation — shall be promoted where appropriate. Lean UX principles, including minimum viable increments and outcome hypothesis testing, shall be available as design techniques.

### 5. Orchestration and Integration
<!-- sources: ITIL 4 Service Design §2.2.4.3, §2.4.2 -->

Service design shall orchestrate all resources required to achieve outcomes across all four dimensions of service management. Effective coordination with related practices — particularly project management, change management, availability management, continuity management, capacity and performance management, service level management, supplier management, and release management — is essential. Integration and coordination shall not be sacrificed under pressure.

### 6. Fitness for Purpose and Use
<!-- sources: ITIL 4 Service Design §2.1, §2.4.2 -->

Products and services created through the design process shall be business- and customer-oriented, cost-effective, flexible and adaptable yet fit for purpose at the point of delivery, able to absorb increasing demand in volume and speed of change, capable of meeting requirements for continuous operation, managed and operated to an acceptable level of risk, and compliant with information and physical security requirements.

### 7. Continual Improvement of Design
<!-- sources: ITIL 4 Service Design §2.4.1 -->

The service design approach, models, and the practice in general shall be subject to continual improvement — constantly seeking ways to deliver stakeholder expectations, increase customer and user satisfaction, eliminate waste, and increase effectiveness and efficiency. Service design approaches shall have flexibility to adapt to changing circumstances, stakeholders, and environment.

---

## Mandatory Requirements

### Essential (All tiers)
<!-- sources: ITIL 4 Service Design §2.1, §2.2, §2.4, §3.2.1 -->

| # | Requirement |
|---|-------------|
| 1 | The organization shall define, document, and agree one or more service design approaches — considering strategic goals, customer requirements, risk appetite, delivery methodology, partner and supplier ecosystem, and resource constraints |
| 2 | Service design models shall be developed for reuse — including procedures, controls, service design package templates, schedule templates, and communications plan templates |
| 3 | Service design packages (SDPs) shall address all four dimensions of service management — organizations and people, information and technology, partners and suppliers, and value streams and processes — with CX/UX at the centre |
| 4 | The level of service design activity required for each category of change shall be defined and communicated, ensuring all stakeholders understand the criteria |
| 5 | Service design plans shall be communicated to all relevant stakeholders and integrated with service desk and knowledge management |

### Intermediate (T2+)
<!-- sources: ITIL 4 Service Design §2.2.4.3, §3.2.2 -->

| # | Requirement |
|---|-------------|
| 6 | Service design execution shall be orchestrated and coordinated across all teams and practices involved — managing requirements tracking, communications, information exchange, and ensuring a holistic view at every stage |
| 7 | Service design reviews shall be conducted for compliance with standards and conventions, confirming all agreed SDP requirements have been completed. Lessons learned shall be logged |
| 8 | When multiple service providers are engaged, an operating model shall be documented defining roles, responsibilities, escalations, and collaboration methods — including provisions for hybrid models |
| 9 | Service design activities shall be coordinated with change management, project management, release management, and all other relevant practices to prevent design isolation |

### Advanced (T3)
<!-- sources: ITIL 4 Service Design §2.2.5, §2.4.1, §2.4.2 -->

| # | Requirement |
|---|-------------|
| 10 | Risk modelling shall be performed using agreed questionnaires, risk impact matrices, and tier algorithms — at service line, customer journey, and IT service levels as appropriate |
| 11 | Service design waivers and dispensations shall be managed with documented mitigations and agreed milestone dates for remediation. Enduring waivers shall be exceptional and require business acceptance of risk exposure |
| 12 | The service design practice shall be periodically reviewed for adherence to approaches, fitness for purpose, stakeholder satisfaction, and ability to innovate by design — with improvement initiatives raised as outcomes |

---

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Service Portfolio Management Policy (PR01) | Portfolio decisions drive service design demand. Design outcomes update the portfolio |
| Service Level Management Policy (PR02) | SLAs define service requirements that design must satisfy |
| Service Financial Management Policy (PR03) | Financial constraints inform design decisions. Design estimates feed financial planning |
| Information Security Management Policy (PR09) | Security controls and compliance needs are design inputs |
| Change Management Policy (PR15) | Design outputs feed change evaluation. Changes trigger design review |
| Risk Management Policy (PR21) | Risk identification and risk appetite inform design decisions |
| Supplier Management Policy (PR23) | Supplier capabilities and contracts constrain and enable design |
| Continual Improvement Policy (PR24) | Design practice improvements are managed through continual improvement |
