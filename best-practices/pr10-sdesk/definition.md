---
process_id: PR10
process_name: "Service Desk"
category: definition
frameworks:
  - itil-v4
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Service Desk §2–§6"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Desk — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Service Desk §2.1 -->

The purpose of the service desk practice is to capture demand for incident resolution and service requests, and to be the entry point and single point of contact for the service provider for all users. More broadly, the practice establishes an effective communication interface between the service provider and its users, with incidents and service requests being two of several communication subjects. The service desk practice addresses all four dimensions of service management — dedicated teams (organizations and people), dedicated information systems (information and technology), workflows and procedures for user communications (value streams and processes), and involved third parties (partners and suppliers). The term "service desk" can refer to a team, an information system, or a set of processes. The service desk practice is involved in all value streams where the service provider communicates with users, aiming to ensure these communications are effective and convenient for all parties.

## Scope
<!-- sources: ITIL 4 Service Desk §2.3 -->

This process covers:

- Establishing and maintaining communication channels and interfaces between the service provider and users
- Enabling, logging, and tracking communications between the service provider and users

This process does not cover: incident resolution and management (incident management), management and fulfilment of service requests (service request management), defining content, timing, and format of communications (respective practices — incident, problem, change, release, etc.), monitoring of technology and service performance (monitoring and event management), management of improvement initiatives (continual improvement), communications between the service provider and stakeholders other than users (relationship management), maintenance and improvement of information and knowledge (knowledge management).

## Key Concepts
<!-- sources: ITIL 4 Service Desk §2.2 -->

### 1. Communication Channels
<!-- sources: ITIL 4 Service Desk §2.2.1 -->
Effective and convenient communication channels between users and the service provider. Good communication channels allow information exchange that is convenient for all parties and ensures information quality. Convenience includes eight characteristics: accessibility (language, format, features for impaired users), assurance (genuine, secure, compliant channels), availability (where and when needed — from business hours to continuous), contextual intelligence (pre-populated data, communication history, user profiles), emotional alignment (ability to communicate emotions and feeling), familiarity (adaptation of familiar channels — social media, forums, email, chat), integration (channels integrated to prevent duplication and information loss), and usability (clear, intuitive, helpful, functional interfaces).

### 2. Omnichannel Communications
<!-- sources: ITIL 4 Service Desk §2.2.1 -->
Unified communications across multiple channels based on sharing information across channels and providing a seamless communication experience. In multichannel communications, the user would start a new journey in every channel. In omnichannel communications, the journey continues, switching between channels as convenient — enabling seamless user experience and information flow without corruption or loss of data.

### 3. Service Empathy
<!-- sources: ITIL 4 Service Desk §2.2.2 -->
The ability to recognize, understand, predict, and project the interests, needs, intentions, and experiences of another party in order to establish, maintain, and improve the service relationship. A service desk agent should recognize and understand a user's frustration, express sympathy, and adjust their actions accordingly. Although automated systems can be enhanced with emotional analysis capabilities, service empathy is usually fulfilled by human interactions via channels such as chat, video, voice calls, and face-to-face meetings. Service empathy is an important factor of user satisfaction and should apply to all service interactions, not just user support.

### 4. User Satisfaction and Moments of Truth
<!-- sources: ITIL 4 Service Desk §2.2.3 -->
The service desk practice significantly influences user satisfaction, customer satisfaction, and service relationship success. A moment of truth is any episode in which the customer or user contacts the organization and gets an impression of service quality — the basis for setting and fulfilling expectations and achieving satisfaction. Many moments of truth occur during user–provider communications. The service desk is also used for collecting user satisfaction data — surveys and research tools generally use the communication channels established by this practice. These channels must be perceived as trusted, effective, and convenient for reliable feedback.

### 5. User Query Triage
<!-- sources: ITIL 4 Service Desk §3.2.1 -->
The process of sorting incoming user queries based on their characteristics, urgency, and the likely benefit of processing them. Triage categorizes queries and uses predefined activity sequences for known query types. Some queries may be resolved at first contact as the dialogue progresses. Triage typically results in initiating a specific value stream — the service desk must be closely integrated with other practices to understand the triage characteristics and their relative importance. Even queries requiring no further action must be recorded with sufficient information.

### 6. Service Desk Organization Models
<!-- sources: ITIL 4 Service Desk §4.2.1 -->
Four organizational models for structuring the service desk team: local (physically co-located with users — quick communications, easy human contact, but dependency risks), distributed (multiple locations linked by common standards — user proximity with coordination challenges), virtual (no physical co-location with users — lower costs, technology barriers reduce pressure, but requires investment in channels and tools), and hybrid (combining elements — including concierge services on customer premises, field services for remote locations, and offshore or shared desk teams for cost optimization). The optimal model is defined by the organization's service relationship model, user profile, geographic distribution, and cost constraints.

## Activities
<!-- sources: ITIL 4 Service Desk §3.2.1, §3.2.2, §3.2.3 -->

### Essential (All tiers)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Acknowledge and record user queries | Receive user queries through all established channels. Acknowledge the query politely to an agreed standard. Record every interaction — uniquely identify it in a query log or workflow tool. Capture time, duration, and content at minimum. Self-service tools may handle preliminary stages before human response |
| 2 | Validate user queries | Verify the user's identity, their entitlement to consume the specified service, whether the query pertains to the service provider's area of responsibility, and whether additional identity checks are needed for protected information. Automated validation can be integrated into the user journey |
| 3 | Triage user queries and initiate appropriate activities | Categorize queries and route them to the appropriate value stream and practice — incident management, service request management, or other relevant practices. Resolve elementary queries at first contact where possible. Ensure sufficient information is captured even for queries requiring no further action |
| 4 | Identify target audience and communication channels for outgoing communications | For both individual and mass communications, identify and confirm the target audience and select appropriate communication channels. Comply with consistent communication standards. Mass communications require audience verification by the service desk |
| 5 | Package and send information to users | Format communications using agreed templates and corporate standards. Ensure messages are clear and use terms and styles that users understand. Manage approval processes for outgoing communications where required. Issue communications through the agreed channels |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 6 | Gather and process receipt confirmations and feedback | Welcome feedback from users through all channels. Collect and process both solicited and unsolicited feedback. Ensure incoming queries relating to specific mass communications are identified and acted upon. Manage follow-up for communications requiring user response, controlling thresholds to avoid user irritation |
| 7 | Review service desk performance | The service desk manager, with relevant stakeholders, reviews performance reports, satisfaction survey results, technology opportunities, and incident and service request reports. Identify opportunities for practice improvement |
| 8 | Initiate and communicate service desk improvements | Register improvement initiatives for processing through the continual improvement practice or initiate change requests. Communicate successful improvements to relevant stakeholders through the communication process |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 9 | Implement and maintain omnichannel integration | Develop multichannel communications toward omnichannel — ensuring seamless user journeys with the ability to switch between channels without losing or corrupting information. Integrate contextual data, communication history, and user profiles across all channels |
| 10 | Optimize service desk organization and sizing | Evaluate and optimize the service desk organizational model — local, distributed, virtual, or hybrid. Assess sizing using queueing theory variables, additional workload from other practices, user expectations, and staff turnover. Balance vertical vs horizontal structures and specialization approaches |

## Inputs
<!-- sources: ITIL 4 Service Desk §3.2.1, §3.2.2, §3.2.3, §5.1 -->

| # | Input | Source |
|---|-------|--------|
| 1 | User queries (via all channels) | Users |
| 2 | Service management records (incidents, changes, problems) | Incident management, change management, problem management |
| 3 | Service configuration and IT asset information | Service configuration management, IT asset management |
| 4 | Service catalogue and request catalogue | Service catalogue management |
| 5 | Knowledge base articles and known error records | Knowledge management, problem management |
| 6 | Change schedule and planned change impacts | Change management |
| 7 | Service desk performance reports and satisfaction surveys | Measurement and reporting |
| 8 | Policies and regulations governing service provision | Information security management, compliance |

## Outputs
<!-- sources: ITIL 4 Service Desk §3.2.1, §3.2.2, §3.2.3 -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Recorded and classified user queries | Incident management, service request management, other value streams |
| 2 | Initiated processing of classified queries | Relevant practice processes |
| 3 | Communicated messages to users | Users |
| 4 | Communication reports | Management, measurement and reporting |
| 5 | User feedback data | Continual improvement, relationship management |
| 6 | Service desk improvement initiatives | Continual improvement, change management |
| 7 | Service desk improvement communications | All stakeholders |

## Roles
<!-- sources: ITIL 4 Service Desk §4.1 Table 4.2, §4.2 -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Service Desk Agent | Front-line role handling user interactions. Acknowledges, records, validates, and triages user queries. Identifies target audiences and communication channels. Packages information for outgoing communications. Gathers and processes feedback. Requires communication skills, writing skills, business and service awareness, some technical skills, understanding of user validation methods, and ability to demonstrate service empathy. May resolve elementary queries at first contact | All |
| Service Desk Manager | Manages the service desk practice overall. Approves and sends outgoing communications. Reviews service desk performance. Initiates improvement initiatives. Communicates improvements to stakeholders. Requires decision-making and leadership skills, methods and techniques expertise, technical skills for communication tools, and knowledge of improvement processes. Responsible for service desk team sizing, structure, and staffing | All |

## Key Artefacts
<!-- sources: ITIL 4 Service Desk §3.2, §4.2, §5.1 -->

| Artefact | Purpose |
|----------|---------|
| User Query Record | Uniquely identified record of every user interaction — capturing time, duration, content, classification, validation results, and triage outcome. Foundation for demand analysis and improvement |
| Communication Standards and Templates | Agreed standards for outgoing communications — corporate templates for notifications, status updates, mass communications, and user surveys. Ensures consistent quality across all agents and channels |
| Service Desk Organization Model | Documents the chosen organizational model (local, distributed, virtual, hybrid), team structure (vertical vs horizontal), sizing rationale, escalation paths, and specialization approach |
| Communication Channel Catalogue | Documents all established communication channels, their characteristics (accessibility, availability, integration status), access requirements, and user guidance |
| Service Desk Performance Report | Periodic report on service desk performance — channel usage, query volumes, triage accuracy, satisfaction scores, improvement progress, and staffing metrics |

## Process Interfaces
<!-- sources: ITIL 4 Service Desk §2.3, §3.2, §5.1 -->

| Interface | Relationship |
|-----------|-------------|
| Incident Management (PR11) | Triage initiates incident management for incidents. Incident status updates are communicated to users through service desk channels |
| Service Request Management (PR12) | Triage initiates service request fulfilment. Request catalogue supports user self-service |
| Problem Management (PR13) | Known error information supports agent work. Problem management provides information about known issues for user communications |
| Service Catalogue Management (PR05) | Service catalogue and request catalogue are key tools for the service desk. Catalogue errors on user-facing views should be reported |
| Service Level Management (PR02) | SLAs define communication requirements and user entitlements. Service desk collects satisfaction data for SLA reviews |
| Change Management (PR15) | Change information is communicated to users through service desk channels. Change schedule informs agents about planned impacts |
| Release & Deployment Management (PR16) | Release information is communicated to users through service desk channels |
| Service Configuration Management (PR17) | Configuration information supports query validation and triage |
| IT Asset Management (PR18) | Asset information supports query handling |
| Knowledge Management (PR19) | Knowledge base supports agents in query resolution. Service desk feeds back knowledge gaps |
| Relationship Management (PR22) | User satisfaction data flows to relationship management. Service desk is a key user-facing interface |
| Continual Improvement (PR24) | Improvement initiatives are processed through continual improvement |
