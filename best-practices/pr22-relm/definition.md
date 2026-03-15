---
process_id: PR22
process_name: "Relationship Management"
category: definition
frameworks:
  - itil-v4
  - fitsm
  - it4it
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Relationship Management §2–§6"
  - "FitSM-2: §PR7 CRM"
  - "IT4IT: S2P Value Stream"
  - "SIAM: Service Integration (relationship coordination)"
last_updated: 2026-03-13
status: draft
---

# Relationship Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Relationship Management §2.1, FitSM-2 §PR7 CRM -->

The purpose of Relationship Management is to establish and nurture effective links between the organization and its stakeholders at strategic, tactical, and operational levels. This includes the identification, analysis, monitoring, and continual improvement of relationships with and between stakeholders — both internal (teams, departments, management) and external (customers, users, suppliers, partners, regulators, and other interested parties). In the context of IT service management, the process focuses particularly on establishing and maintaining good relationships with customers receiving services — understanding their needs and expectations, managing satisfaction, conducting service reviews, and handling complaints. The practice aims to establish a common organizational approach to relationships that promotes shared goals, open communication, collaboration, and conflict prevention.

## Scope
<!-- sources: ITIL 4 Relationship Management §2.3, FitSM-2 §PR7 CRM -->

The scope of Relationship Management includes:

- Developing and promoting an organization-wide approach to relationships and integrating this approach into the organization's culture
- Identifying and managing stakeholders — mapping their interests, influence, and engagement needs
- Preventing and resolving conflicts between individuals, teams, and organizations
- Monitoring and maintaining effective and healthy relationships within the organization (between teams, departments, and individuals)
- Monitoring and maintaining effective and healthy relationships between the organization and its external stakeholders (customers, users, suppliers, partners, regulators, and others)
- Maintaining a customer database and managing ongoing customer interactions (service reviews, complaints, satisfaction measurement)

### Related Activities in Other Processes
<!-- sources: ITIL 4 Relationship Management §2.3 Table 2.4 -->

Several closely related activities are managed by other processes, though they depend on healthy relationships:

| Activity | Primary Process |
|----------|---------------|
| Establishing and managing service level agreements with customers | Service Level Management (PR02) |
| Establishing and managing service level agreements with suppliers | Supplier Management (PR23) |
| Managing ongoing interactions with users (day-to-day contact) | Service Desk (PR10) |
| Managing ongoing interactions with customers (SLA governance) | Service Level Management (PR02) |
| Managing ongoing interactions with suppliers (contract/performance governance) | Supplier Management (PR23) |

## Key Concepts

### 1. Relationship Types
<!-- sources: ITIL 4 Relationship Management §2.2.1 -->

Relationships within and between organizations can be characterized along a spectrum from exchange-oriented to communal. **Exchange relationships** are transactional and utility-oriented — parties provide benefits with the expectation of comparable return. **Communal relationships** are collaborative — parties provide benefits in response to needs, without expecting immediate reciprocity. Similarly, relationships between teams can exhibit features of **cooperation** (working with others to achieve one's own goals) or **collaboration** (working with others to achieve common shared goals). Organizations operating in complex adaptive systems generally find that collaborative, communal relationships are more effective than formal, exchange-based ones.

### 2. Service Relationship Types
<!-- sources: ITIL 4 Relationship Management §2.2.1.2 Table 2.2 -->

Inter-organizational service relationships fall into three broad types:

| Type | Focus | Org Level | Maturity | Service Type |
|------|-------|-----------|----------|-------------|
| **Basic** | Support and efficiency | Operational | Ad hoc, order taker | Commodity, standardized, off-the-shelf |
| **Cooperative** | Improvement and effectiveness | Operational + tactical | Trusted adviser | Configured, customized services |
| **Partnership** | Innovation and growth | Operational + tactical + strategic | Strategic partner | Custom, bespoke, co-created services |

Understanding which type characterizes each relationship is essential for selecting the right engagement model, agreement type, and communication approach.

### 3. Stakeholder Management
<!-- sources: ITIL 4 Relationship Management §2.2.4 -->

Stakeholders are all parties who contribute to, benefit from, or may be affected by the service relationship — including customers, users, employees, suppliers, regulators, investors, communities, and others. A stakeholder map categorizes stakeholders by their influence (ability to affect the organization) and interest (degree to which they are affected by or care about the organization's activities). This produces four engagement approaches: manage closely (high influence, high interest), keep satisfied (high influence, low interest), keep informed (low influence, high interest), and monitor (low influence, low interest). The stakeholder map should be regularly revisited as influence and interest change over time.

### 4. Relationship Journey
<!-- sources: ITIL 4 Relationship Management §2.2.5, Table 2.3 -->

All relationships follow a journey with broadly similar stages: exploration (understanding markets, needs, and potential partners), engagement (fostering a functioning relationship), offering (shaping demand and service offerings), agreement (aligning expectations and agreeing service scope and quality), onboarding (integrating or separating resources), co-creation (providing, consuming, and acting together to create value), and realization (capturing value and driving improvement). At the service level, these stages map to the customer journey. Each stage requires specific activities, communication patterns, and behaviours that the relationship model defines.

### 5. Relationship Models
<!-- sources: ITIL 4 Relationship Management §3.2.1, §3.2.2 -->

A relationship model defines how the organization manages relationships with a particular stakeholder group. Each model specifies: the level of communality (exchange, cooperation, or partnership), the relationship journey steps appropriate to that stakeholder group, the key activities and responsibilities at each step, the risks and opportunities at each step, and the recommended behaviour patterns. Relationship models are developed for key stakeholder groups and used by relationship agents to guide their interactions consistently.

### 6. Communication Principles
<!-- sources: ITIL 4 Relationship Management §2.2.3 -->

Effective relationships depend on effective communication. Five principles apply: communication is always a two-way process; people are always communicating (including through silence and inaction); timing and frequency matter; there is no single method of communication that works for everyone; and the message is shaped by the medium through which it is delivered. These principles should be embedded in the organization's relationship management approach and reflected in all stakeholder interactions.

### 7. Preventing Toxic Relationships
<!-- sources: ITIL 4 Relationship Management §2.2.2 -->

Toxic work environments lack enthusiasm and mutual support, characterized instead by four destructive behaviours: criticism, defensiveness, contempt, and obstruction. These behaviours undermine trust and make collaboration impossible. The relationship management practice has a specific responsibility to prevent and mitigate toxic behaviour by promoting shared values, establishing conflict resolution mechanisms, and ensuring that the organizational culture supports open communication and psychological safety.

## Activities

### Essential Activities (All Tiers)
<!-- sources: FitSM-2 §PR7 CRM, ITIL 4 Relationship Management §2.2.4, §3.2.2 -->

| # | Activity | Description |
|---|----------|-------------|
| 1 | Identify and map key stakeholders | Identify the internal and external stakeholders relevant to the organization's services. Map them according to their influence and interest to determine the appropriate level of engagement |
| 2 | Maintain a customer and stakeholder database | Establish and maintain a register of service customers with contact information, service agreements, communication preferences, and relationship history. Add new customers, update information, and remove customers as relationships end |
| 3 | Define communication channels for stakeholder engagement | Determine the channels through which stakeholders will engage with the organization — for service reviews, complaints, escalations, and general relationship management |
| 4 | Conduct customer service reviews | Plan, prepare, and conduct periodic service reviews with customers to discuss service performance, satisfaction, emerging needs, and any issues. Document the outcomes and agreed actions |
| 5 | Handle customer complaints | Register, investigate, and resolve customer complaints. Track follow-up actions and review complaints periodically for patterns and improvement opportunities |
| 6 | Measure and manage customer satisfaction | Implement mechanisms to assess customer satisfaction on a regular basis (surveys, feedback forms, interviews). Initiate follow-up actions when satisfaction is insufficient |
| 7 | Identify the applicable relationship model for new stakeholders | When a new relationship opportunity arises (new customer, new team, new supplier relationship), identify the appropriate relationship model or, at T1, the basic engagement approach to follow |
| 8 | Follow the relationship model in ongoing interactions | Ensure that interactions with stakeholders are consistent with the agreed relationship model or engagement approach — applying the defined communication patterns, meeting cadences, and escalation paths |

### Intermediate Activities (T2+)
<!-- sources: ITIL 4 Relationship Management §3.2.1, §3.2.2 -->

| # | Activity | Description |
|---|----------|-------------|
| 9 | Analyse the organization's culture, strategy, and stakeholders | Assess the organization's culture and how it supports (or hinders) effective relationships. Analyse the organization's strategy and its implications for stakeholder relationships. Produce stakeholder maps and culture assessments |
| 10 | Develop and agree key principles of relationships | Define the key principles that will govern the organization's internal and external relationships — values such as openness, collaboration, no-blame, psychological safety. These principles define the desired characteristics of relationships with key stakeholder groups |
| 11 | Develop relationship models for key stakeholder groups | For each key stakeholder group, develop a formal relationship model that defines the communality level, relationship journey stages, key activities and responsibilities at each stage, risks, and recommended behaviour patterns |
| 12 | Embed effective behaviour patterns into daily work interactions | Communicate the agreed principles and models across the organization through training, awareness campaigns, cultural development programmes, and integration with other practices (workforce management, service desk, service level management) |
| 13 | Manage relationship exceptions and conflicts | When conflicts arise or the relationship model does not prove effective, intervene to resolve the issue. Involve managers, HR specialists, and relationship agents as appropriate. Where relevant, propose updates to the relationship model |
| 14 | Review relationships and feed lessons into continual improvement | Periodically (and following significant events) review the health and effectiveness of key relationships. Document lessons learned and improvement initiatives. Communicate findings to relevant parties |

### Advanced Activities (T3)
<!-- sources: ITIL 4 Relationship Management §2.4.3.2, §3.2.1, §6 -->

| # | Activity | Description |
|---|----------|-------------|
| 15 | Review and adjust the organization's relationship approach and models | Monitor the adoption and effectiveness of the agreed relationship principles and models across the organization. Adjust the approach based on relationship incidents, conflicts, stakeholder feedback, and changes to strategy or culture. This activity drives continual improvement of the overall relationship management practice |
| 16 | Manage non-service stakeholder relationships | Actively manage relationships with stakeholder groups beyond the direct service relationship — including governments and regulators, industry associations, media, investors and shareholders, and communities. Identify and analyse these stakeholders, plan engagement approaches, and monitor relationship health |
| 17 | Coordinate relationship management across service integration boundaries | In multi-supplier environments, coordinate the relationship management approach across the service ecosystem. This may involve delegating supplier relationship management to a service integrator or establishing shared relationship principles and models across organizational boundaries. Ensure mutual transparency and visibility of changes that may affect other parties |

## Inputs
<!-- sources: ITIL 4 Relationship Management Tables 3.1, 3.3, FitSM-2 §PR7 CRM -->

| Input | Source |
|-------|--------|
| Organization's strategy and values | Strategic planning, leadership |
| Assessment of the organization's culture and relationship behaviour patterns | HR, organizational development, internal surveys |
| Stakeholder information (customer details, service agreements, contact information) | Customer database, CRM system |
| Current service catalogue | Service Catalogue Management (PR05) |
| Existing SLAs with customers | Service Level Management (PR02) |
| Customer demands and requirements | Customers, service reviews |
| Customer complaints | Customers, service desk |
| Service reports (performance against SLA targets) | Measurement & Reporting (PR20), Service Level Management (PR02) |
| Relationship principles and models | Internal (from Process 1, at T2+) |
| Training and awareness materials | Internal (from relationship awareness activities, at T2+) |

## Outputs
<!-- sources: ITIL 4 Relationship Management Tables 3.1, 3.3, FitSM-2 §PR7 CRM -->

| Output | Consumer |
|--------|----------|
| Stakeholder maps | All service management processes, leadership |
| Culture analysis and strategic requirements | Strategy management, organizational development |
| Principles of relationships | All staff, HR, organizational development |
| Relationship models for key stakeholder groups | Relationship agents, service level managers, supplier managers |
| Planning, training, and awareness materials | HR, workforce management, all staff |
| Relationship review reports and improvement initiatives | Continual Improvement (PR24), leadership |
| Up-to-date customer database | Service Level Management (PR02), all customer-facing processes |
| Service review reports | Service Level Management (PR02), Service Portfolio Management (PR01) |
| Customer complaints records | Continual Improvement (PR24), Change Management (PR15) |
| Customer satisfaction reports | Service Level Management (PR02), leadership, Continual Improvement (PR24) |
| Customer requirements (from service reviews, feedback) | Service Portfolio Management (PR01), Service Level Management (PR02) |

## Roles
<!-- sources: ITIL 4 Relationship Management §4.1.1, §4.2, FitSM-2 §PR7 CRM -->

| Role | Tier | Responsibilities |
|------|------|-----------------|
| **Relationship Manager** | All | Develops and maintains relationship models. Communicates, trains, and supports relationship agents. Reviews relationships and their effectiveness. Coordinates relationship journeys. Manages exceptions in relationship journeys. At T1, may be combined with service level manager or service owner. May be specialized by stakeholder type (customer relationship manager, supplier relationship manager, media/regulatory liaison manager) |
| **Relationship Agent** | T2+ | Maintains healthy day-to-day relationships with assigned stakeholders. Follows the agreed relationship model. Coordinates ongoing interactions between the stakeholder and members of the organization. Participates in the management of exceptions and in relationship reviews. May be performed by account managers, customer relationship managers, sales agents, service desk leads, or other specialist roles depending on the stakeholder type and organizational structure |
| **Service Level Manager** | All | Works alongside relationship management to conduct service reviews, manage SLA expectations, and translate customer requirements into service commitments. Consults on relationship model development for service-consuming stakeholders |
| **Service Owner** | All | Provides input on service performance and customer feedback for their services. Participates in service reviews. Consulted when relationship decisions affect service delivery or service strategy |

## Artefacts
<!-- sources: ITIL 4 Relationship Management §3.2.1–§3.2.2, FitSM-2 §PR7 CRM -->

| Artefact | Description | Tier |
|----------|-------------|------|
| **Customer/Stakeholder Database** | Register of service customers and key stakeholders with contact information, service agreements, communication preferences, and relationship history | All |
| **Stakeholder Map** | Matrix categorizing stakeholders by influence and interest, determining the appropriate engagement approach for each | All |
| **Service Review Reports** | Records of periodic service reviews with customers documenting service performance, satisfaction, agreed actions, and emerging needs | All |
| **Customer Complaints Records** | Log of customer complaints with investigation outcomes, follow-up actions, and resolution status | All |
| **Customer Satisfaction Reports** | Results of satisfaction surveys, feedback analysis, and trend data | All |
| **Relationship Principles** | Documented set of values and principles governing the organization's approach to internal and external relationships | T2+ |
| **Relationship Models** | Formal models for key stakeholder groups defining communality level, journey stages, activities, responsibilities, risks, and behaviour patterns | T2+ |
| **Relationship Review Reports** | Periodic assessment of relationship health, adoption of agreed principles and models, incidents/conflicts, lessons learned, and improvement initiatives | T2+ |
| **Culture Analysis** | Assessment of the organization's culture and its impact on relationships, with recommendations for cultural development | T3 |

## Process Interfaces
<!-- sources: ITIL 4 Relationship Management §2.3 Table 2.4, FitSM-2 §PR7 CRM -->

| Process | Interface Description |
|---------|-----------------------|
| Service Level Management (PR02) | **Bidirectional.** SLAs and service reports provide the foundation for service reviews and customer engagement (input). Customer requirements, satisfaction data, and service review outcomes inform SLA definition and revision (output) |
| Service Portfolio Management (PR01) | **Output.** Customer requirements identified through service reviews and feedback are fed into portfolio decisions about new or changed services |
| Service Desk (PR10) | **Bidirectional.** Service desk staff follow relationship principles in user interactions (consumes principles). User feedback and interaction patterns inform relationship health assessment (provides data) |
| Supplier Management (PR23) | **Parallel.** Supplier relationships follow the same relationship management principles. Supplier performance data informs the overall relationship health picture |
| Measurement & Reporting (PR20) | **Input.** Service performance reports provide the data used in service reviews and satisfaction management |
| Change Management (PR15) | **Output.** Requests for change may be raised to address insufficient customer satisfaction, complaints, or service review findings |
| Continual Improvement (PR24) | **Output.** Relationship review findings, complaint patterns, and improvement initiatives feed the continual improvement register |
| Knowledge Management (PR19) | **Bidirectional.** Relationship models and stakeholder information are knowledge assets (output). Knowledge articles may inform relationship agents about stakeholder history and context (input) |

## Automation Opportunities
<!-- sources: ITIL 4 Relationship Management §5.2, Table 5.1 -->

### Process 1: Managing a Common Approach to Relationships

| Activity | Automation | Impact |
|----------|-----------|--------|
| Analyse the organization's culture, strategy, and stakeholders | Collaboration and communication tools | Low |
| Develop and agree key principles of relationships | Mind mapping, brainstorming tools | Low |
| Develop relationship models for key stakeholder groups | CRM tools, workflow tools, communication and collaboration tools | Medium/High |
| Embed effective behaviour patterns into daily interactions | Communication and collaboration tools, presentation tools, portals | Medium |
| Review and adjust the relationship approach and models | Collaboration and communication tools, reporting tools | Medium |

### Process 2: Managing Service Relationship Journeys

| Activity | Automation | Impact |
|----------|-----------|--------|
| Identify stakeholders and relationship model | Communication and collaboration tools | Medium/High |
| Verify and adjust relationship model to the situation | CRM tools, workflow tools, knowledge management tools | High |
| Follow the relationship model | CRM tools, workflow tools, knowledge management tools, records management, communication management | High |
| Manage exceptions | CRM tools, workflow tools, knowledge management tools, collaboration tools, direct communication | Medium |
| Review the relationship | CRM tools, workflow tools, knowledge management tools, records management, communication management | Medium/High |

## Maturity Levels
<!-- sources: ITIL 4 Relationship Management §2.4, FitSM-2 §PR7 CRM -->

### Level 1 — Initial
Customer relationships are managed informally and reactively. There is no formal customer database or stakeholder register. Service reviews happen ad hoc or not at all. Customer complaints are handled individually without systematic tracking. No defined approach to relationship management exists — relationship quality depends entirely on individual behaviour and goodwill.

### Level 2 — Managed
A customer database is established with contact information for all service customers. Regular service reviews are scheduled and conducted. Customer complaints are logged and tracked to resolution. Basic customer satisfaction measurement is in place (annual surveys or post-interaction feedback). A relationship manager role is assigned (possibly combined with the service level manager). Key stakeholders are identified, though no formal stakeholder map exists.

### Level 3 — Defined
A formal relationship management approach is documented, including stakeholder maps, relationship principles, and relationship models for key stakeholder groups. Relationship agents are assigned for major customer and stakeholder relationships. The organization's culture and its impact on relationships are assessed. Behaviour patterns aligned with the agreed principles are embedded through training and awareness activities. Service reviews, complaint handling, and satisfaction management are systematic with defined procedures and tracked outcomes. Internal relationships are actively managed alongside external ones.

### Level 4 — Quantitatively Managed
Relationship health is measured against defined targets across all key stakeholder groups (satisfaction scores, complaint rates, relationship incident counts, employee relationship climate scores). Trends are analysed and used to drive targeted improvements. Relationship models are periodically reviewed and adjusted based on measured outcomes. The organization actively manages non-service stakeholder relationships (regulators, media, industry groups). Customer satisfaction and relationship health data are integrated into service management decision-making.

### Level 5 — Optimizing
The relationship management approach is a core component of the organization's culture, with all staff understanding and practising the agreed principles. Relationship models are continuously refined based on real-time feedback and organizational learning. The organization coordinates relationship management across service integration boundaries in multi-supplier environments. Relationship analytics predict potential issues (declining satisfaction, emerging conflicts) before they manifest, enabling proactive intervention. The organization is recognized as a trusted partner by its key stakeholders and actively manages its reputation across all stakeholder groups.
