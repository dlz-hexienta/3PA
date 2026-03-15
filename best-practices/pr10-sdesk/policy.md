---
process_id: PR10
process_name: "Service Desk"
category: policy
frameworks:
  - itil-v4
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Service Desk §2.1, §2.2, §2.4"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Desk — Best Practice Policy

## How to Use This Policy Template

This policy establishes the governing principles and mandatory requirements for the service desk practice. It should be customized to reflect the organization's service relationship model, user profile, geographic distribution, and communication culture. Requirements are graduated by maturity — organizations should implement Essential requirements first, then layer on Intermediate and Advanced requirements as the practice matures.

---

## Policy Principles

### 1. Single Point of Contact
<!-- sources: ITIL 4 Service Desk §2.1 -->

The service desk shall be the entry point and single point of contact for the service provider for all users. All user queries — including incidents, service requests, consultations, complaints, and compliments — shall be captured, recorded, and routed through established service desk channels. This ensures consistent quality, complete demand capture, and reliable information flow into the organization's value streams.

### 2. User-Centred Communication
<!-- sources: ITIL 4 Service Desk §2.2.1, §2.2.2 -->

Communication channels shall be designed around user needs — convenient, accessible, and familiar. Communication shall demonstrate service empathy — recognizing and understanding user needs, expressing sympathy where appropriate, and adjusting actions accordingly. Messages shall use terms and styles that users understand. Internal technical language shall be translated for user-facing communications.

### 3. Consistent Quality
<!-- sources: ITIL 4 Service Desk §2.2.3, §3.2.2 -->

Every interaction between the service provider and users shall comply with consistent quality standards, regardless of channel, agent, time, or location. Communication templates and corporate standards shall ensure uniformity. Every moment of truth — each episode where a user contacts the organization — shall reinforce a positive impression of service quality.

### 4. Complete Demand Capture
<!-- sources: ITIL 4 Service Desk §2.4.2, §3.2.1 -->

Every user interaction shall be recorded — uniquely identified in a query log or workflow tool — capturing time, duration, and content at minimum. Even queries requiring no further action shall be recorded. Record keeping is an invaluable source of data on service quality and is essential for demand analysis, improvement, and accountability.

### 5. Effective Triage
<!-- sources: ITIL 4 Service Desk §3.2.1 -->

User queries shall be validated and triaged to the appropriate value stream and practice with accuracy and speed. The service desk practice shall be closely integrated with other practices to understand triage characteristics and their relative importance. Queries resolvable at first contact shall be addressed immediately to improve user experience and reduce demand on specialist teams.

### 6. Channel Integration
<!-- sources: ITIL 4 Service Desk §2.2.1, §2.4.1 -->

Where multiple communication channels are used, they shall be integrated to provide seamless user experience and information flow. The organization shall progress from multichannel toward omnichannel communications — enabling users to switch between channels without losing or corrupting information.

### 7. Continual Improvement
<!-- sources: ITIL 4 Service Desk §3.2.3 -->

The service desk practice shall be subject to continual improvement — reviewing performance, identifying opportunities, initiating improvements, and communicating results. Improvement shall be informed by performance data, satisfaction surveys, technology opportunities, and feedback from all stakeholders.

---

## Mandatory Requirements

### Essential (All tiers)
<!-- sources: ITIL 4 Service Desk §2.1, §2.2, §3.2.1, §3.2.2 -->

| # | Requirement |
|---|-------------|
| 1 | Communication channels shall be established between the service provider and users — appropriate to the service relationship model, user profile, and service portfolio |
| 2 | All user queries shall be acknowledged, recorded, and uniquely identified in a query log or workflow tool — regardless of channel or outcome |
| 3 | User queries shall be validated — verifying identity, service entitlement, and scope of responsibility — before triage and processing |
| 4 | User queries shall be triaged and routed to the appropriate value stream and practice. Triage criteria shall be defined in conjunction with receiving practices |
| 5 | Outgoing communications to users shall follow agreed templates and corporate standards. The service desk shall maintain communication quality across all channels |

### Intermediate (T2+)
<!-- sources: ITIL 4 Service Desk §2.4.1, §3.2.2, §3.2.3 -->

| # | Requirement |
|---|-------------|
| 6 | User feedback shall be collected and processed through service desk channels — on a scheduled basis and triggered by service interactions. Feedback shall be welcomed, not discouraged |
| 7 | Service desk performance shall be reviewed regularly — covering channel effectiveness, query volumes, triage accuracy, and user satisfaction. Improvement opportunities shall be identified and acted upon |
| 8 | Mass communications to users shall be managed through the service desk — with audience verification, channel selection, content review, and feedback processing |
| 9 | Self-service capabilities shall be provided where appropriate — enabling users to submit queries, find information, and track status without human interaction |

### Advanced (T3)
<!-- sources: ITIL 4 Service Desk §2.2.1, §4.2 -->

| # | Requirement |
|---|-------------|
| 10 | Communications shall be omnichannel — integrated across all channels with shared information, seamless transitions, and contextual intelligence |
| 11 | The service desk organizational model shall be formally defined and periodically reviewed — considering local, distributed, virtual, and hybrid options against user needs and cost constraints |
| 12 | Service desk sizing shall be assessed using demand analysis — considering query arrival rates, acceptable waiting times, additional workload from other practices, service level expectations, and staff turnover |

---

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Incident Management Policy (PR11) | Triage routes incidents to incident management. Service desk communicates incident status to users |
| Service Request Management Policy (PR12) | Triage routes service requests to fulfilment. Request catalogue supports self-service |
| Service Level Management Policy (PR02) | SLAs define communication requirements and user entitlements |
| Service Catalogue Management Policy (PR05) | Catalogue and request catalogue are key service desk tools |
| Knowledge Management Policy (PR19) | Knowledge base supports agents in query handling |
| Change Management Policy (PR15) | Change information is communicated to users through service desk channels |
| Information Security Management Policy (PR09) | Security policies govern identity verification and data protection in user communications |
| Relationship Management Policy (PR22) | Service desk is a key interface for user relationship management |
