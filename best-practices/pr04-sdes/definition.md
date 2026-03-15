---
process_id: PR04
process_name: "Service Design"
category: definition
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T3
sources:
  - "ITIL 4: Service Design §2–§6"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Design — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Service Design §2.1 -->

The purpose of the service design practice is to design products and services that are fit for purpose and fit for use, and that can be delivered by the organization and its ecosystem. This includes planning and organizing people, partners and suppliers, information, communication, technology, and practices for new or changed products and services, and the interaction between the organization and its customers. The practice ensures a holistic, results-driven approach to all aspects of service design, coordinating design efforts across the organization's service value system. Service design applies not only to the creation of new products and services but also to significant changes and planned retirements — unless retirement is carefully planned, it could cause unexpected negative effects on customers or the organization. Not every change requires the same level of design activity — organizations must define what level of design activity is required for each category of change.

## Scope
<!-- sources: ITIL 4 Service Design §2.3 -->

This process covers:

- Ensuring services are fit for purpose and fit for use
- Identifying and documenting risk-aligned service tiers and design packages, incorporating standards, non-functional requirements, and capabilities
- Governing and orchestrating the holistic design approach across all four dimensions of service management
- Integrating teams involved in service design and promoting information exchange between all stakeholders
- Updating service design packages through the lifecycle of the service
- Continually improving the service design practice

This process does not cover: risk identification and management (risk management), demand management (relationship management), definition of architecture patterns and principles (architecture management), definition of security controls and compliance needs (information security management), defining requirements (business analysis), defining service acceptance criteria (service validation and testing), definition of monitoring patterns and event categorization (monitoring and event management), user feedback gathering (service desk), supplier strategy and default contracts (supplier management).

## Key Concepts
<!-- sources: ITIL 4 Service Design §2.2 -->

### 1. Design Thinking
<!-- sources: ITIL 4 Service Design §2.2.1 -->
A practical and human-centred approach that accelerates innovation, used to solve complex problems and find practical, creative solutions that meet the needs of the organization and its customers. Design thinking complements Lean and Agile methodologies by drawing upon logic, imagination, intuition, and systems thinking. It proceeds through five iterative activities: inspiration and empathy (observing how people interact with products and services), ideation (combining divergent and convergent thinking to explore and narrow solutions), prototyping (testing ideas early to gather feedback), implementation (bringing concepts to life in coordination with service management practices), and evaluation (measuring actual performance against acceptance criteria). Design thinking is best applied by multi-disciplinary teams and aligns well with the organization's service value system.

### 2. Customer and User Experience
<!-- sources: ITIL 4 Service Design §2.2.2 -->
Customer experience (CX) is the sum of functional and emotional interactions with a service and service provider as perceived by a customer. User experience (UX) is the sum of functional and emotional interactions as perceived by a user. CX and UX are essential aspects of service design — CX design focuses on managing time, quality, cost, reliability, and effectiveness of the complete customer experience, while UX focuses on ease of use and interaction. Service experience recognizes that value is co-created — consumers are not passive recipients but active participants who also invest effort. Lean UX embraces Lean-Agile methods, implementing functionality in minimum viable increments and measuring results against outcome hypotheses, enabling fast feedback cycles.

### 3. Service Design Package
<!-- sources: ITIL 4 Service Design §2.2.3, §2.2.3.1 -->
A document or set of documents defining all aspects of an IT service and its requirements through each stage of its lifecycle. A service design package (SDP) is produced for each new service, updated periodically or during major changes, and maintained through retirement. The SDP connects demand to value regardless of delivery methodology and must address all four dimensions of service management — organizations and people (operating model, support matrix, training needs), information and technology (tooling, monitoring, data management, vulnerability), partners and suppliers (contracts, service integration, critical success factors), and value streams and processes (critical path analysis, expedited processes) — with customer and user experience at the centre. For each element, the architect provides evidence of compliance; where stakeholders do not approve, issues are addressed through iterative review.

### 4. Service Planning
<!-- sources: ITIL 4 Service Design §2.2.4.1 -->
The strategic phase that designs and develops the target state for end-to-end service provision, ensuring customer and user experience is inherent in service level offerings. Service planning addresses how the design supports business outcomes, how value is created sustainably, what the organization's risk appetite is, how service tiers should be organized, and how service characteristics should vary across those tiers. The answers are driven by the four dimensions of service management and define the organization's ability to respond to demand for value realization. There is a close working relationship with portfolio management for investment decisions and strategy management for risk appetite.

### 5. Service Design Orchestration
<!-- sources: ITIL 4 Service Design §2.2.4.3 -->
Service design orchestration ensures all resources required to achieve the outcome — including suppliers, information, technology, people, processes, and operating models — are considered when designing and transitioning services. It utilizes the principles of service integration and management (SIAM) to manage the level of risk posed to the organization — designing operating models appropriate to the level of risk and designing service components with capabilities matched to the risk level. Where multiple service providers are engaged, the orchestration establishes roles, responsibilities, and how providers work together. It includes managing service design waivers and dispensations where performance does not meet SDP requirements, with agreed milestone dates for remediation.

### 6. Risk Modelling
<!-- sources: ITIL 4 Service Design §2.2.5 -->
Risk modelling determines the appropriate service design package for a service based on its risk profile. It involves several elements: a questionnaire covering data confidentiality, integrity, and availability, financial impacts, regulatory obligations, known risks, reputational damage, and disaster scenarios; an agreed risk impact matrix detailing possible impacts at business operations level; an algorithm for calculating results using agreed service tier distributions; and a result identifying the most appropriate SDP. Risk modelling should be performed at multiple levels — service line, customer journey, and individual IT service — as each may legitimately have different risk profiles. The critical path within a service identifies what would stop a consumer from completing their task.

### 7. Service Design Approaches and Models
<!-- sources: ITIL 4 Service Design §2.4.1 -->
Organizations define and agree approaches and models for designing new and changed services and components. An organization may have several service design approaches depending on different products and services in its portfolio — from linear approaches reusing existing models for familiar designs, to experimental iterative approaches with fast feedback for innovative services. Each approach should have one or several agreed service design models that can be reused for similar products and services. The approaches and models should have flexibility to adapt to changing circumstances, and should be subject to continual improvement.

## Activities
<!-- sources: ITIL 4 Service Design §3.2.1, §3.2.2 -->

### Essential (All tiers)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Analyse service and product environment and requirements | Together with product and service owners, architects, and other teams, analyse and discuss new or changed conditions affecting service design — including preferred approaches, nature of products and services, architecture decisions, customer and user feedback, risk appetite, compliance constraints, market position, financial conditions, and level of control over service components |
| 2 | Review and develop the service design approach | Discuss and agree a new or updated service design approach. Consider organization objectives, customer requirements, ways of communication, ability to innovate, resource constraints, risk appetite, project management methods, and the partner and supplier ecosystem |
| 3 | Review and develop service design models | Based on the approach, define or update service design models — including service design procedures and controls, SDP templates, template plans and schedules, communications plan templates, and knowledge article templates. Assess the extent to which existing models can support specific design instances |
| 4 | Plan service design instances | Plan the methods for requirements tracking, target audience and communications, interactions with partners and suppliers, financial plans and budget control, SDP contents, and resource plans for specific design instances |
| 5 | Communicate service design plans | Prepare communications for new or updated design plans, SDPs, methods, and procedures. Review with stakeholders and feed into service desk and knowledge management |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 6 | Identify applicable design model and plan design activities | Assess service requirements, complexity, interdependencies with existing services, budget, and risks. Choose the appropriate service design model or trigger the planning process for a new model. Plan design activities, identify teams involved, and request resource allocations. Assign responsibilities for SDP maintenance and risk management |
| 7 | Orchestrate and coordinate service design execution | Orchestrate and coordinate teams and resources involved in design execution — managing requirements tracking, communications, information exchange, fast feedback, and data flow. Ensure a holistic view of the design at every stage. Coordinate with all relevant practices and internal and external teams |
| 8 | Review service design outcomes | Run service design review for compliance with standards and conventions and to ensure all agreed SDP requirements have been completed correctly. Update the knowledge base and log lessons learned. Produce a service design review report that may trigger the planning process |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 9 | Model and manage service risk tiers | Develop and maintain risk questionnaires, risk impact matrices, and tier algorithms. Profile services at service line, customer journey, and IT service levels. Assign risk-aligned service tiers and corresponding SDPs. Manage waivers and dispensations where performance does not meet SDP requirements — agree milestone dates for remediation |
| 10 | Optimize the service design practice | Review and improve the service design practice — evaluate adherence to approaches across the portfolio, assess fitness for purpose, measure stakeholder satisfaction with design approaches and the organization's ability to innovate by design. Initiate improvement initiatives to eliminate waste, increase effectiveness, and better deliver stakeholder expectations |

## Inputs
<!-- sources: ITIL 4 Service Design §3.2.1, §3.2.2 -->

| # | Input | Source |
|---|-------|--------|
| 1 | Organization's strategy and service portfolio | Strategy management, portfolio management |
| 2 | Architectural decisions, patterns, and principles | Architecture management |
| 3 | Business analysis reports and requirements | Business analysis |
| 4 | Customer and user feedback | Service desk, relationship management |
| 5 | Service catalogue and service level agreements | Service catalogue management, service level management |
| 6 | IT asset information | IT asset management |
| 7 | Agreements and contracts with suppliers and partners | Supplier management |
| 8 | Policies and plans (information security, continuity, capacity) | Information security management, service continuity management, capacity & performance management |
| 9 | Service design records and review reports (prior cycles) | Service design (prior cycles) |

## Outputs
<!-- sources: ITIL 4 Service Design §3.2.1, §3.2.2 -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Service design approaches and models (updated) | All design teams, management |
| 2 | Service design plans | Project management, product/service owners |
| 3 | Service design packages (SDPs) and SDP templates | Change management, release management, service catalogue, knowledge management |
| 4 | Service design records | Service design (for future reference) |
| 5 | Service design communications | All stakeholders, service desk |
| 6 | Service design review reports | Management, continual improvement |
| 7 | Improvement initiatives and change requests | Continual improvement, change management |
| 8 | Updated knowledge articles and lessons learned | Knowledge management |
| 9 | Service portfolio updates and updated risk register | Portfolio management, risk management |

## Roles
<!-- sources: ITIL 4 Service Design §4.1, §4.1.1, §4.1.2, §4.2 -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Service Design Leader | Accountable for the service design practice. Provides strategic direction and manages maturity. Develops the practice including training, communications, and processes. Governs service design processes and controls. Builds, utilizes, and governs service design packages. Combines good knowledge of the organization's products — architecture, services, and interdependencies — with solid design thinking skills. Competency profile: Leader, Methods expert, Coordinator (LMC) | All |
| Service Design Consultant | Develops and industrializes detailed service design activities. Focuses on detailed procedures, elements of service design packages, provision of consultancy to change initiatives, and orchestrating service provisioning. Coordinates design execution and manages requirements tracking, communications, and information exchange. Competency profile: Methods expert, Coordinator (MC) | All |
| Service/Product Owner | Participates in environment and requirements analysis, approach and model review, design planning, and service design review. Provides the product and service perspective. Ensures design outcomes meet business requirements. May perform the service design leader role in product-based organizations where dedicated design roles are not adopted | All |

## Key Artefacts
<!-- sources: ITIL 4 Service Design §2.2, §3.2 -->

| Artefact | Purpose |
|----------|---------|
| Service Design Approach | Documents the organization's agreed approach to service design — including design philosophy, methods, techniques, stakeholder engagement models, and integration with other practices |
| Service Design Model | A reusable model for a category of service design — including procedures, controls, SDP template, schedule templates, and communications plan templates. Multiple models may exist for different product and service types |
| Service Design Package (SDP) | Documents defining all aspects of an IT service and its requirements through each lifecycle stage — addressing all four dimensions with CX/UX at the centre. Includes functional and non-functional requirements, risk tier, operating model, and compliance evidence |
| Service Design Plan | Plan for a specific service design instance — including requirements tracking methods, communications plan, partner and supplier interactions, financial plan, SDP contents, and resource plan |
| Service Design Review Report | Report from the service design review — assessing compliance with standards and conventions, confirming SDP requirements are met, and logging lessons learned. May trigger the planning process for approach or model updates |

## Process Interfaces
<!-- sources: ITIL 4 Service Design §2.3, §2.4, §3.2 -->

| Interface | Relationship |
|-----------|-------------|
| Service Portfolio Management (PR01) | Portfolio decisions drive service design demand. Design outcomes update the service portfolio |
| Service Level Management (PR02) | SLAs define service requirements. Service design ensures service levels can be met by design |
| Service Financial Management (PR03) | Financial constraints and cost information inform design decisions. Design estimates feed financial planning |
| Availability Management (PR06) | Availability requirements are key design inputs. Design ensures availability targets can be met |
| Service Continuity Management (PR07) | Continuity requirements inform design resilience. Design addresses disaster scenarios |
| Capacity & Performance Management (PR08) | Capacity and performance requirements drive design decisions. Design ensures scalability |
| Information Security Management (PR09) | Security controls and compliance needs are design inputs. Design incorporates security by design |
| Monitoring & Event Management (PR14) | Monitoring patterns and event categorization are design outputs. Design defines what needs monitoring |
| Change Management (PR15) | Design outputs feed change evaluation. Changes trigger design review |
| Release & Deployment Management (PR16) | Design packages support release planning. Release outcomes feed design review |
| Risk Management (PR21) | Risk identification and risk appetite inform design decisions. Design risk modelling produces updated risk registers |
| Relationship Management (PR22) | Customer and user feedback informs design. Demand management drives design requirements |
| Supplier Management (PR23) | Supplier capabilities and contracts constrain and enable design. Design defines supplier requirements and operating models |
| Architecture Management | Architecture patterns, principles, and decisions are foundational design inputs. Design must conform to architectural standards |
