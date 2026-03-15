---
process_id: PR12
process_name: "Service Request Management"
category: policy
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Service Request Management §2.1, §2.2, §2.4"
  - "FitSM-1: §PR9.1–§PR9.5"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Request Management — Best Practice Policy

## How to Use This Policy Template

This policy establishes the governing principles and mandatory requirements for the service request management practice. It should be customized to reflect the organization's service portfolio, request catalogue maturity, automation capabilities, and user base characteristics. Requirements are graduated by maturity — organizations should implement Essential requirements first, then layer on Intermediate and Advanced requirements as the practice matures.

---

## Policy Principles

### 1. Predefined and Pre-Agreed
<!-- sources: ITIL 4 SRM §2.1, §2.2 -->

Service requests represent actions that have been agreed as a normal part of service delivery. Every service request type shall have a tested, pre-approved outcome — meaning the fulfilment workflow was designed, the approval flow was agreed, staff were trained, and service components were configured to support fulfilment. Service requests are business as usual — not exceptions requiring ad hoc decision-making.

### 2. User-Friendly Fulfilment
<!-- sources: ITIL 4 SRM §2.1, §2.4.2, FitSM-1 §PR9.4 -->

Service request fulfilment shall be designed for user convenience and satisfaction. Users shall have clear visibility of available requests, submission requirements, approval status, and expected fulfilment times. Communication shall be proactive — keeping users informed of progress without requiring them to chase status. Fulfilment experiences directly influence user satisfaction and perception of overall service quality.

### 3. Model-Based Fulfilment
<!-- sources: ITIL 4 SRM §2.2, §2.4.1, FitSM-2 §PR9 -->

Every type of service request shall be supported by a documented request model that defines the fulfilment procedure, responsibilities, automation, and third-party involvement. Models shall be produced during service design, tested before deployment, and maintained as services evolve. Fulfilment without a model is an exception — not a normal operating mode.

### 4. Appropriate Authorization
<!-- sources: ITIL 4 SRM §2.1 -->

Authorization and approval workflows shall be proportionate to the risk and cost of each request type. Policies shall define which requests can be fulfilled with limited or no additional approvals, enabling streamlined processing for low-risk, routine requests. Authorization shall not create unnecessary bureaucracy but shall ensure appropriate oversight where the request involves cost commitments, security implications, or changes to the production environment.

### 5. Catalogue-Driven Transparency
<!-- sources: ITIL 4 SRM §2.2, §2.4.1 -->

Service requests shall be described in a request catalogue that is available to all eligible users. The catalogue shall provide accurate, SLA-specific information — including prerequisites, required input, approval workflows, and target fulfilment times. The more relevant the catalogue information, the more efficient the fulfilment and the higher the user satisfaction.

### 6. Standardization and Automation
<!-- sources: ITIL 4 SRM §2.1, §2.4.1, FitSM-2 §PR9 -->

Service requests and their fulfilment shall be standardized and automated as far as possible. Automation shall be prioritized for the most popular and routine requests with limited variations in fulfilment workflows. Tailored, complex, and rare requests shall be automated only after careful consideration to ensure costs and risks of automation are justified by volume and value.

### 7. Continual Improvement
<!-- sources: ITIL 4 SRM §2.4.1, §3.2.2 -->

Service request fulfilment procedures shall be subject to continual improvement — informed by performance monitoring, user satisfaction data, exception analysis, and technology opportunities. Improvement shall focus on reducing fulfilment times, increasing automation, eliminating unnecessary steps, and ensuring request models remain aligned with evolving service offerings and user needs.

---

## Mandatory Requirements

### Essential (All tiers)
<!-- sources: ITIL 4 SRM §2.1, §2.2, §3.2.1, FitSM-1 §PR9.1, §PR9.2, §PR9.5 -->

| # | Requirement |
|---|-------------|
| 1 | All service requests shall be registered, classified, and prioritised in a consistent manner — taking into account service targets from SLAs and the organization's classification and prioritisation scheme |
| 2 | Every type of service request shall be supported by a documented request model that defines the fulfilment procedure, responsibilities, approvals, and target fulfilment time |
| 3 | Service requests shall be fulfilled according to their agreed model and within the timeframes defined in applicable SLAs |
| 4 | The request catalogue shall accurately describe available requests — including prerequisites, required information, approval workflows, and fulfilment targets — tailored to the SLA applicable to each user group |
| 5 | Closure of service requests shall include verification that the desired result has been produced and user communication confirming completion |

### Intermediate (T2+)
<!-- sources: ITIL 4 SRM §2.4, §3.2.1, §3.2.2, FitSM-1 §PR9.3, §PR9.4 -->

| # | Requirement |
|---|-------------|
| 6 | Ad hoc fulfilment — where standard models do not produce the desired result — shall be tracked as exceptions. All exception details shall be recorded and fed into the model improvement process |
| 7 | Service request fulfilment performance shall be reviewed regularly — covering fulfilment times, exception rates, procedural adherence, and user satisfaction. Improvement opportunities shall be identified and acted upon |
| 8 | Functional and hierarchical escalation paths shall be defined for service requests — enabling consistent escalation when fulfilment is at risk of exceeding agreed timeframes or when ad hoc decisions are required |
| 9 | Self-service capabilities shall be provided for routine, high-volume requests — enabling users to submit, track, and where possible receive fulfilment through automated channels |

### Advanced (T3)
<!-- sources: ITIL 4 SRM §2.4.1, §3.2.2, §6 -->

| # | Requirement |
|---|-------------|
| 10 | Service request fulfilment shall be optimized through automation — from fully automated self-service to orchestrated workflows across multiple systems and teams. Automation decisions shall be justified by volume, cost, and risk analysis |
| 11 | Third-party contributions to request fulfilment shall be formally defined in request models — with standard interfaces specifying data exchange, tools, and processes for collaboration in multi-vendor environments |
| 12 | Service request model updates shall be communicated to all relevant stakeholders — including fulfilment teams, service desk agents, service owners, and users — ensuring consistent adoption across all channels |

---

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Service Desk Policy (PR10) | Service desk triages user queries and routes service requests to fulfilment. Status updates are communicated through service desk channels |
| Incident Management Policy (PR11) | Requests incorrectly submitted as service requests are redirected to incident management. Incorrect fulfilment may cause incidents |
| Change Management Policy (PR15) | Service request fulfilment may trigger standard or normal changes. Change typology defines the correlation |
| Service Catalogue Management Policy (PR05) | Service catalogue management maintains the request catalogue. Catalogue accuracy directly affects fulfilment efficiency |
| Service Level Management Policy (PR02) | SLAs define fulfilment targets, user entitlements, and conditions for each request type |
| Service Design Policy (PR04) | Request models are created during service design and tested before deployment to operations |
| Information Security Management Policy (PR09) | Security policies govern identity verification and access provisioning in request fulfilment |
| Continual Improvement Policy (PR24) | Improvement initiatives from performance review are processed through continual improvement |
