---
process_id: PR19
process_name: "Knowledge Management"
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
  - "ITIL 4: Knowledge Management §2.1–§2.5, §3.2.1–§3.2.3, §4.1, §5, §6"
  - "IT4IT: Cross-cutting Functions"
last_updated: 2026-03-14
status: draft
---

# Knowledge Management — Best Practice Process Definition

## How to Use This Definition

This process definition provides the reference model for knowledge management at three maturity levels. Organizations should implement Essential elements first, then layer on Intermediate and Advanced capabilities as the practice matures. Knowledge management has no dedicated FitSM process — this definition draws primarily from ITIL 4 with IT4IT cross-cutting alignment. Knowledge management is fundamentally a cultural practice — technology and processes support it, but the practice succeeds or fails based on people's willingness to share, learn, and apply knowledge.

---

## Purpose
<!-- sources: ITIL 4 KM §2.1 -->

To maintain and improve the effective, efficient, and convenient use of information and knowledge across the organization — ensuring that stakeholders have access to relevant and reliable information at the right time and in the right format, supporting effective decision-making and reducing the need to rediscover knowledge.

---

## Key Concepts

### 1. Knowledge and the DIKW Model
<!-- sources: ITIL 4 KM §2.2.1 -->

The DIKW model describes the transformation from raw data through information and knowledge to wisdom. Data comprises discrete facts and observations. Information is data placed in context — organized, structured, and interpreted to give it meaning. Knowledge represents the application of information combined with experience, judgment, and values — enabling effective decisions and actions. Wisdom is the ability to make sound judgments and decisions based on knowledge, experience, and understanding. Knowledge management focuses primarily on the knowledge and information layers, ensuring that data is transformed into usable knowledge and that knowledge is accessible when needed. Both data-driven decisions (based on analysis of structured data) and insight-driven decisions (based on tacit knowledge, experience, and judgment) are valuable — the appropriate approach depends on the context.

### 2. Tacit and Explicit Knowledge
<!-- sources: ITIL 4 KM §2.2.2 -->

Knowledge exists in two fundamental forms. Explicit knowledge can be documented, codified, and transferred through formal channels — procedures, records, databases, articles, and documents. Tacit knowledge resides in people's minds — their experience, intuition, skills, and judgment — and is difficult to articulate or transfer through documentation alone. The SECI model describes four modes of knowledge conversion: socialization (tacit to tacit, through shared experience), externalization (tacit to explicit, through articulation and documentation), combination (explicit to explicit, through systematizing and integrating), and internalization (explicit to tacit, through learning by doing). Effective knowledge management addresses both forms and facilitates conversion between them.

### 3. Knowledge Assets
<!-- sources: ITIL 4 KM §2.2.3, §3.2.3 -->

Knowledge assets are the collective and individual, structured and unstructured, tacit and explicit data and information that an organization uses and manages. Examples include incident records, application source code, service level agreements, technical documentation, operational procedures, architectural diagrams, and expertise held by individuals. Knowledge assets have a lifecycle — they are discovered, classified, managed according to guidelines, and reviewed for continued relevance. The scope and level of specification of knowledge assets are defined as part of establishing the knowledge management environment, in conjunction with architecture management, information security management, and service configuration management.

### 4. Absorptive Capacity
<!-- sources: ITIL 4 KM §2.2.4 -->

Absorptive capacity is an organization's ability to recognize the value of new external information, assimilate it, and apply it effectively. Organizations with high absorptive capacity can learn quickly from external sources — industry developments, partner innovations, emerging technologies, and best practices. Absorptive capacity increases both from involving suppliers in knowledge management activities and from recognizing partners as sources of information, even those not directly related to the practice's support function. Building absorptive capacity requires investment in people's capabilities, knowledge sharing channels, and a culture that values learning from external sources.

### 5. Organizational Learning and Knowledge Culture
<!-- sources: ITIL 4 KM §2.2.5, §2.2.6 -->

Knowledge management depends fundamentally on people's willingness and ability to share, use, and create knowledge. An effective knowledge culture is characterized by psychological safety — where people feel safe to learn, unlearn, share mistakes, and ask questions — mutual respect, trust, and accountability. Organizational learning happens when individual knowledge becomes collective capability through sharing, documentation, and integration into processes. The knowledge management practice must address the human and cultural dimensions alongside the technical and procedural ones. Consumers of services also contribute to knowledge through feedback, usage patterns, and service requests — their knowledge should be captured and integrated.

### 6. Knowledge Management Environment
<!-- sources: ITIL 4 KM §2.2.7, §3.2.1 -->

The knowledge management environment encompasses the systems, tools, processes, guidelines, roles, and cultural norms that together support the lifecycle management of knowledge. Establishing and maintaining this environment is the foundational process of knowledge management. The environment includes the knowledge management approach (scope, methods, policies), knowledge systems and repositories, data and information quality guidelines, classification schemes, access controls, and the organizational structures that coordinate knowledge activities. The environment should be designed to make knowledge sharing the path of least resistance — embedding knowledge capture and reuse into everyday value streams rather than creating a parallel bureaucratic function.

---

## Scope
<!-- sources: ITIL 4 KM §2.3 -->

Knowledge management is a broad cross-cutting practice that touches every other practice and value stream. It applies wherever information and knowledge are created, used, shared, or needed for decision-making. The practice covers management of the knowledge environment (approach, culture, capabilities), on-demand discovery and provision of information for non-routine requests, and systematic management of knowledge assets throughout their lifecycle. The scope of knowledge management should be defined explicitly — specifying which knowledge asset types, which parts of the organization, and which activities are governed by the practice — and expanded progressively as the practice matures.

---

## Practice Success Factors
<!-- sources: ITIL 4 KM §2.4 -->

### PSF1: Establishing and Maintaining an Effective Knowledge Management Approach

The organization establishes and maintains a knowledge management approach that defines the scope, methods, tools, and cultural enablers for effective use of information and knowledge. The approach is reviewed and improved based on stakeholder satisfaction, organizational changes, and emerging practices. Knowledge management roles, responsibilities, and capabilities are defined and maintained.

### PSF2: Integrating Knowledge Management into All Value Streams and Practices

Knowledge management activities are embedded into all relevant value streams and practices — not managed as an isolated function. Knowledge is captured as a natural part of work, shared through convenient channels, and applied to improve decision-making and service quality. The organization develops the absorptive capacity to learn from both internal experience and external sources.

---

## Activities

### Essential (T2+)

<!-- sources: ITIL 4 KM §3.2.1 Table 3.1–3.2, §3.2.2 Table 3.3–3.4 -->

| # | Activity | Description |
|---|----------|-------------|
| 1 | Understand current culture of knowledge usage and sharing | Assess organizational information and knowledge flows, review progress of knowledge management practice improvement, evaluate stakeholder satisfaction, and identify whether the organization's knowledge management is up to date and meets needs. Performed regularly (interval-based, once or twice per year) or in response to significant changes (event-based). Nominate people and assign knowledge management team roles |
| 2 | Review external and internal requirements and factors of influence | Continually review external factors that impact the knowledge system — regulatory requirements (GDPR, ISO 30401, ISO 900), industry best practices, emerging data analysis techniques and methods — and internal requirements that shape the knowledge sharing environment |
| 3 | Optimize response and identify improvements | Based on cultural assessment and requirements review, identify the optimal response of the knowledge management approach to organizational strategy. Not all best practices and new approaches should be implemented immediately — the organization should adopt only those that suit its vision and context |
| 4 | Register and triage information requests | Accept and register information requests in agreed format — capturing the area of information, purpose, currently available sources, requested format, timing, and other parameters. Assess whether the request can be fulfilled through existing knowledge systems or requires on-demand discovery |
| 5 | Research, collect, process, and present information | For on-demand requests: identify roles and people likely to be involved, assign research, agree on time and expected outputs, establish data selection criteria. Obtain and review available data from internal and external sources. Interview people to support tacit-to-explicit knowledge transfer. Analyse, structure, and present collected data in the agreed format. Provide resulting outputs to the agreed group of stakeholders |

### Intermediate (T2+)

<!-- sources: ITIL 4 KM §3.2.2 Table 3.4, §3.2.3 Table 3.5–3.6, §3.2.1 Table 3.2 -->

| # | Activity | Description |
|---|----------|-------------|
| 6 | Accept information and integrate knowledge | Stakeholders review research output and confirm acceptance — evaluating information quality, output format, and timeliness of presentation. If not accepted, the request returns to research or is cancelled. Accepted information is assessed for integration into organizational knowledge management systems — it may stay in exclusive possession of intended recipients, or be integrated and published subject to classification and access policies. A decision to standardize the request and make information permanently available may be initiated |
| 7 | Discover, classify, and manage knowledge assets | Analyse the organization's information assets — triggered by new asset introduction, user feedback, review findings, or stakeholder requests. Evaluate the importance of knowledge assets and identify appropriate management guidelines and the responsible team or role. If no applicable guideline exists, initiate development of a new guideline. Develop guidelines with relevant specialists, including assessment of applicable policies and recommendations on responsibility |
| 8 | Review initiatives and initiate improvements | Review the practice and register all required and identified knowledge management improvement initiatives via the continual improvement register. Involve relevant members of the organization and the continual improvement practice. Monitor improvement progress and adjust priorities |

### Advanced (T3)

<!-- sources: ITIL 4 KM §3.2.1 Table 3.2, §3.2.3 Table 3.6 -->

| # | Activity | Description |
|---|----------|-------------|
| 9 | Promote and empower usage of KM practice across the organization | Create relevant guidance, training materials (text, videos, podcasts), and share information via relevant channels. Conduct training and support organization members in their knowledge management activities. Track adoption of promoted patterns and stakeholder satisfaction as input for the practice. Drive organizational change management to embed knowledge sharing as a cultural norm |
| 10 | Review knowledge asset effectiveness and drive continual optimization | Assign knowledge asset management guidelines to appropriate teams. Manage acceptance — specialist teams review and accept or reject assignments with sufficient explanation. Perform regular reviews of knowledge asset management to assess key metrics and initiate improvements. Communicate improvement initiatives to relevant stakeholders through the continual improvement practice |

---

## Inputs

<!-- sources: ITIL 4 KM §3.2.1 Table 3.1, §3.2.2 Table 3.3, §3.2.3 Table 3.5 -->

| # | Input | Source |
|---|-------|--------|
| 1 | KM stakeholder satisfaction assessment | Relationship Management, surveys |
| 2 | Previous improvement results | Continual Improvement |
| 3 | Policies and regulatory requirements | Information Security Management, Governance |
| 4 | Financial guidelines and constraints | Service Financial Management |
| 5 | Improvement proposals from other practices | All practices |
| 6 | Risk information | Risk Management |
| 7 | Information requests | All practices, stakeholders |
| 8 | Information assets used by the organization | Service Configuration Management, all practices |
| 9 | Information about errors in knowledge system | All practices, users |

---

## Outputs

<!-- sources: ITIL 4 KM §3.2.1 Table 3.1, §3.2.2 Table 3.3, §3.2.3 Table 3.5 -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | KM approach document | All practices, stakeholders |
| 2 | Scope of knowledge assets | Service Configuration Management, all practices |
| 3 | KM practice improvement plan | Continual Improvement |
| 4 | Templates, instructions, and guidance for KM lifecycle management | All practices |
| 5 | Data and information quality guidelines | All practices |
| 6 | Knowledge asset management guidelines and assignments | Knowledge asset owners, all practices |
| 7 | Information in requested format | Requesting stakeholders |
| 8 | Updated internal knowledge storages and knowledge assets | All practices |
| 9 | KM reports (usage, asset management, improvement) | Management, all practices |

---

## Roles

<!-- sources: ITIL 4 KM §4.1.1, §4.1.2, §4.1.3 -->

| Role | Abbreviation | Tier | Description |
|------|:------------:|:----:|-------------|
| Knowledge Manager | KM | T2+ | Coordinates the knowledge management culture and capabilities building process. Defines and assigns knowledge team roles. Ensures the knowledge asset management process runs in relevant SVS parts. Empowers, mentors, and leads the knowledge team. Communicates decisions through the practice lifecycle. Monitors and reviews team activities. Conducts regular and ad hoc practice analyses. Creates an environment of psychological safety, mutual respect, and trust. Competency profile: LACMT |
| Knowledge Management Team Member | KMT | T2+ | Works as part of a shared leadership team with different competencies to achieve KM outcomes. Responsible for definition, communication, and execution of KM strategy, plans, and guidelines. Can be assigned to people across the organization depending on experience and competencies. Contributes ingenuity and ideas to effective KM practice. Competency profiles vary by activity: ATC for research, ACT for processing, MTC for integration |
| Knowledge Asset Owner | KAO | T2+ | Any specialist or manager who accepts responsibility for the management of specific knowledge assets within their domain. Reviews and accepts or rejects knowledge asset management assignments — rejections must be explained in enough detail to facilitate reanalysis and reassignment. Follows management guidelines as part of their usual work within value streams. Competency profile: AT |

---

## Artefacts

<!-- sources: ITIL 4 KM §3.2.1–§3.2.3, §5.1 -->

| # | Artefact | Purpose |
|---|----------|---------|
| 1 | KM Approach Document | Defines scope, methods, tools, cultural enablers, policies, roles, and guidelines for the practice |
| 2 | Knowledge Base / Knowledge Management System | Central repository for knowledge assets — articles, procedures, known errors, technical documentation, and other structured and unstructured knowledge |
| 3 | Information Request Register | Tracks on-demand information requests through registration, research, processing, acceptance, and integration |
| 4 | Knowledge Asset Management Guidelines | Type-specific guidelines defining how different categories of knowledge assets should be managed, classified, and maintained |
| 5 | KM Practice Improvement Plan | Records improvement initiatives identified through reviews, audits, and stakeholder feedback — linked to the continual improvement register |

---

## Interfaces

<!-- sources: ITIL 4 KM §3.2.1–§3.2.3, §5.1, §6 -->

| # | Practice | Interface Description |
|---|----------|----------------------|
| 1 | Incident Management (PR11) | Known error articles, resolution knowledge bases, and incident pattern documentation support first-line and specialist resolution |
| 2 | Problem Management (PR13) | Root cause analysis knowledge, workaround documentation, and known error records are managed as knowledge assets |
| 3 | Service Desk (PR10) | Knowledge base articles support service desk agents with self-service content and first-contact resolution scripts |
| 4 | Service Configuration Management (PR17) | Knowledge assets relate to configuration items; CI data informs knowledge scope and classification; CMDB and knowledge systems share data |
| 5 | Information Security Management (PR09) | Security classification policies govern knowledge access controls; information security policies constrain knowledge sharing channels and methods |
| 6 | Continual Improvement (PR24) | KM improvement initiatives feed into the continual improvement register; CI practice supports knowledge management improvements |
| 7 | Service Level Management (PR02) | Knowledge about service agreements, service levels, and performance supports SLM decisions and stakeholder communication |
| 8 | Relationship Management (PR22) | Stakeholder knowledge requirements inform KM scope and priorities; customer and partner knowledge is captured and integrated |
| 9 | Change Management (PR15) | Knowledge about planned and completed changes supports impact assessment; changes may affect knowledge assets requiring updates |
| 10 | Supplier Management (PR23) | Partner knowledge sharing arrangements, onboarding/offboarding knowledge transfer procedures, and supplier-provided information assets |
| 11 | Risk Management (PR21) | Risk information informs KM priorities; knowledge about risks is managed as a knowledge asset; KM supports risk identification and analysis |
| 12 | Measurement & Reporting (PR20) | KM metrics and practice performance data are reported through standard reporting channels |
