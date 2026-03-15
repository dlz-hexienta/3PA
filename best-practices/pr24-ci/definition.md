---
process_id: PR24
process_name: "Continual Improvement"
category: definition
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
  - "ITIL 4: Continual Improvement §2–§6"
  - "FitSM-2: §PR14 CSI"
  - "IT4IT: Cross-cutting"
last_updated: 2026-03-14
status: draft
---

# Continual Improvement — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Continual Improvement §2.1, FitSM-2 §PR14 CSI Objective -->

Continual improvement aligns the organization's practices and services with changing business needs through the ongoing improvement of products, services, practices, and any element involved in the management of products and services. The practice enables the service provider to adapt to changing circumstances and to improve its overall capabilities to deliver and manage services efficiently. Failure to adapt and improve leads to a reduction in the value of services. The practice plans, implements, and reviews improvements to services and processes — ensuring that improvement opportunities are identified, evaluated, prioritized, and tracked through to completion. Continual improvement is a core component of the service value system and must be embedded in all other service management practices.

## Scope
<!-- sources: ITIL 4 Continual Improvement §2.3, FitSM-2 §PR14 CSI -->

This process covers:

- Establishing and nurturing a continual improvement culture across the organization
- Planning and maintaining improvement approaches and methods throughout the organization
- Identifying, logging, and managing improvement opportunities from all sources
- Assessing, prioritizing, and approving improvement initiatives using transparent criteria
- Developing business justifications for improvement investments
- Planning improvement initiatives with appropriate resource and timeline planning
- Facilitating the implementation of improvement initiatives throughout their lifecycles
- Measuring and evaluating the results of improvement initiatives — including outputs, outcomes, efficiency, risks, and costs
- Generating and incorporating feedback on improvements' implementation and results
- Maintaining the continual improvement register (CIR)
- Capturing and sharing lessons learned from improvement initiatives

This process does not cover: implementing improvements through projects, software development, infrastructure changes, or deployments (project management, change enablement, deployment management, release management); definition of vision and strategic objectives (strategy management); analysis of flaws in a value stream (business analysis); change authorization (change enablement); providing measurement tools (measurement and reporting); decision-making on funding of large improvement initiatives (portfolio management); assessing risks against desired outcomes (risk management); negotiating joint improvement initiatives with partners and suppliers (supplier management, relationship management); informing and agreeing on improvements with service consumers (service level management); providing interfaces for user feedback and improvement ideas (service desk); or managing the human aspects of large-scale improvement initiatives (organizational change management).

## Key Concepts
<!-- sources: ITIL 4 Continual Improvement §2.2, FitSM-2 §PR14 CSI -->

### 1. Improvement
<!-- sources: ITIL 4 Continual Improvement §2.2 -->
A deliberately introduced change that results in increased value for one or more stakeholders. Almost every action taken in an organization can be seen as an improvement activity. Improvement means change — there cannot be a change to outcomes without changing the current state. All improvement initiatives should cascade from the organizational vision; if an improvement is not contributing to achieving the vision, it is probably not necessary or useful.

### 2. Continual Improvement Register (CIR)
<!-- sources: ITIL 4 Continual Improvement §5.1.2, §5.1.3, FitSM-2 §PR14 CSI -->
A database or structured document used to record and manage improvement initiatives throughout their lifecycles. In Agile methodologies, the CIR serves as the product backlog. People throughout the organization should be encouraged to record ideas in the CIR. Each improvement record includes fields such as: unique identifier, name, requester or source, configuration item affected, improvement owner, urgency, status, indicative cost, value or benefits statement, and improvement plan. The CIR may be an integrated part of the service management system or a standalone database.

### 3. Continual Improvement Model
<!-- sources: ITIL 4 Continual Improvement §2.4.1.1 -->
A high-level model providing guidance for improvement initiatives through seven iterative steps: (1) What is the vision? — understand the business vision, mission, goals, and objectives; (2) Where are we now? — perform baseline assessments; (3) Where do we want to be? — define measurable targets; (4) How do we get there? — define the improvement plan; (5) Take action — execute improvement actions; (6) Did we get there? — evaluate metrics and KPIs; (7) How do we keep the momentum going? — embed lessons and sustain gains. The steps need not be followed linearly — it may be necessary to return to previous steps at various points.

### 4. Feedback Loops
<!-- sources: ITIL 4 Continual Improvement §2.2 -->
Part of the output of an activity that is used for new input. Well-constructed feedback mechanisms provide understanding of end user and customer perception of value, the efficiency and effectiveness of value chain activities, the effectiveness of governance and management controls, the interfaces between the organization and its partner and supplier network, and the demand for products and services. Feedback can be analysed to identify and validate improvement opportunities, risks, or issues. Multiple feedback channels — formal and informal — should be established.

### 5. Business Justification
<!-- sources: ITIL 4 Continual Improvement §2.4.2.5 -->
A documented articulation of the reason for undertaking an improvement initiative. Business justifications should include data and evidence relating to costs and expected benefits. The focus should not be limited to return on investment but should also address the business value (value on investment) that the improvement would bring. Success criteria and their measurements, including timescales, must be clearly defined. For small-scale initiatives, a Lean Canvas approach can create a single-page business model covering: problem statement, suggested initiative, key metrics, value proposition, unfair advantage, customer segments, channels, cost structure, and benefits forecast.

### 6. Improvement Culture
<!-- sources: ITIL 4 Continual Improvement §2.4.1.3, §2.4.1.4 -->
A culture of continual improvement encourages stakeholders to suggest and support improvements, encourages stakeholders to express their needs and take risks, recognizes that perfectionism is typically self-defeating, considers continual improvement to be a business-as-usual activity, celebrates successful improvements, encourages fast feedback loops, and promotes learning from failures rather than a blame culture. Senior management commitment is critical to establishing this culture. A safe-to-fail environment promotes psychological safety, relying on respect and trust between team members and managers. Knowledge sharing is a critical success factor — in organizations where knowledge is seen as a personal asset rather than an organizational capability, it will be difficult to benefit from continual improvement.

### 7. Improvement Prioritization
<!-- sources: ITIL 4 Continual Improvement §2.4.2.2, FitSM-2 §PR14 CSI -->
Prioritization criteria must be transparent and applied impartially to all initiatives. Some outcomes will be more critical than others, and there may be a required order for changes. Low-cost, low-effort initiatives can be prioritized for rapid value realization. Evaluation criteria include benefits and cost/effort. When prioritization cannot be clearly assessed, the initiative should be escalated to a governance committee. In organizations with a product owner role, improvement suggestions may be filtered and adjusted by the product owner before addition to the CIR.

### 8. Improvement Ownership
<!-- sources: ITIL 4 Continual Improvement §2.4.2.3 -->
The owners of specific service, product, or practice value streams are accountable for managing relevant continual improvement initiatives within their scope. These owners should lead by example, demonstrating the value of improvement activities. The continual improvement practice owner is accountable for managing the practice itself — ensuring the organization has the knowledge, skills, and tools needed to identify, assess, fund, perform, and evaluate improvement initiatives. Responsibility for an improvement initiative should not be shared across teams — each initiative has a single improvement owner.

## Activities
<!-- sources: ITIL 4 Continual Improvement §3.2.1, §3.2.2, FitSM-2 §PR14 CSI -->

### Essential (All tiers)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Identify and log improvement opportunities | Capture ideas for improvement from all sources — staff at all levels, customers, suppliers, partners, incident reviews, problem outcomes, service reports, audit reports, and assessment results. Log each improvement idea in the CIR with a unique identifier. Capturing ideas is everyone's responsibility and is critical to developing a continual improvement culture |
| 2 | Assess, prioritize, and approve improvement initiatives | Evaluate each improvement opportunity against transparent criteria — considering benefits, cost, effort, urgency, risk, and alignment with the organizational vision. Prioritize initiatives and secure funding and resources for the most important ones. Develop business justifications appropriate to the scale of the initiative. Escalate to governance committees when prioritization cannot be clearly assessed |
| 3 | Plan improvement initiatives | Plan approved initiatives with appropriate resource allocation, timeline, and methodology. The level of planning should match the initiative's scale — from simple task assignments for small improvements to formal project management for large initiatives. Ensure improvement priorities are consistent with priorities for other types of work |
| 4 | Facilitate improvement implementation | Separate the approved initiative plan into smaller tasks. Facilitate implementation according to the plan and chosen methodology. Track the status and progress of improvement actions. Coordinate with the practices responsible for implementing the changes |
| 5 | Measure and evaluate improvement results | After completion, evaluate whether the improvement achieved its intended outcomes. Compare outcomes against agreed success factors and KPIs. Capture lessons learned. If expected outcomes were not fully achieved, prioritize gaps for following iterations. Showcase successful improvements to stakeholders to demonstrate and validate value co-creation |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 6 | Establish and maintain the improvement approach | Define and maintain the organization's continual improvement approach — selecting appropriate methods and techniques adapted to the organization's environment. Consider the typical timeframes in which challenges manifest. Establish a flexible framework that allows managers to switch between techniques depending on changing circumstances. Ensure the approach is documented and communicated |
| 7 | Integrate continual improvement into organizational culture | Ensure senior management models improvement behaviours. Update job descriptions and employee objectives to include service management and improvement responsibilities. Reward compliance with improvement practices. Establish a safe-to-fail environment where teams can experiment with limited risk. Promote knowledge sharing as an organizational capability |
| 8 | Promote continuous learning | Capture lessons learned at every improvement iteration — both from successful initiatives and from those that did not achieve planned outcomes. Maintain a lessons learned log throughout initiative implementation. Produce lessons learned reports and ensure they are used for similar future initiatives. Create a blameless environment where the primary focus is learning, not assigning blame |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 9 | Optimize the continual improvement practice | Assess the continual improvement practice itself using the same measurement and evaluation approach applied to other practices. Evaluate whether the organization's improvement methods are yielding expected results. Identify areas where the improvement approach needs refinement — including capture methods, prioritization criteria, implementation effectiveness, and measurement of results. Apply improvement techniques such as Toyota Kata or OODA loops for environments requiring different improvement cadences |
| 10 | Manage supply chain improvement | Include suppliers and partners in continual improvement initiatives. Encourage suppliers to submit suggestions to the CIR. Collaborate with suppliers to identify improvement opportunities across the supply chain — including removing unnecessary requirements, adjusting product specifications, reassigning value stream activities, and adjusting delivery cadences. Engage suppliers in regular discussions and planning of mutual improvements |

## Inputs
<!-- sources: ITIL 4 Continual Improvement §3.2.1 Table 3.1, FitSM-2 §PR14 CSI -->

| # | Input | Source |
|---|-------|--------|
| 1 | Organization's vision, mission, and objectives | Senior management, strategy management |
| 2 | Suggestions for improvement from all sources | All staff, customers, suppliers, partners |
| 3 | Post-incident reviews and problem outcomes | Incident management, problem management |
| 4 | Baseline and current performance metrics | Measurement & reporting, all practices |
| 5 | Customer satisfaction metrics and feedback | Relationship management, service desk |
| 6 | Service level management practice reviews | Service level management |
| 7 | Assessment and audit reports | Internal audit, risk management |
| 8 | Service reports | Measurement & reporting |
| 9 | Results from measurements, assessments, and audits of the SMS | All practices |

## Outputs
<!-- sources: ITIL 4 Continual Improvement §3.2.1 Table 3.1, FitSM-2 §PR14 CSI -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Improvement records (logged in CIR) | Continual improvement register |
| 2 | Updated CIR (prioritized, status-tracked) | All practices, management |
| 3 | Business justifications (draft and approved) | Portfolio management, financial management |
| 4 | Improvement plans | Relevant practices, project management |
| 5 | Requests for change | Change management |
| 6 | Performance measurements (before and after) | Measurement & reporting |
| 7 | Lessons learned | Knowledge management, all practices |
| 8 | Improvements to services or the SMS | All practices |

## Roles
<!-- sources: ITIL 4 Continual Improvement §4.1 Table 4.2, §4.2, FitSM-2 §PR14 CSI -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Continual Improvement Manager / CIR Administrator | Accountable for managing the continual improvement practice. Ensures the organization has the knowledge, skills, and tools needed to identify, assess, fund, perform, and evaluate improvement initiatives. Maintains the CIR. Coordinates prioritization. Facilitates the embedding of continual improvement into the organizational culture. In smaller organizations, this may be a part-time role or combined with a coaching role; as organizational proficiency increases, the role may become part-time | All |
| Improvement Owner | Accountable for implementing a specific improvement initiative. Plans, facilitates, and tracks the initiative through to completion. Develops business justifications and measures results. Each improvement has a single owner — responsibility should not be shared across teams. May be a team leader, project manager, or practice manager depending on the initiative's scope | All |
| Senior Manager | Provides strategic direction, approves significant improvement investments, and models improvement behaviours. Ensures continual improvement is embedded in the organizational culture through role-modelling, reward structures, and updated job expectations. Evaluates improvement results for strategic and tactical decisions | All |

## Key Artefacts
<!-- sources: ITIL 4 Continual Improvement §3.2, §5, FitSM-2 §PR14 CSI -->

| Artefact | Purpose |
|----------|---------|
| Continual Improvement Register (CIR) | Complete list of improvement records used to track and manage all improvement initiatives throughout their lifecycles. Each record includes identifier, name, source, affected CI, owner, urgency, status, cost, value statement, and plan |
| Improvement Record | Individual record for an improvement initiative — capturing the problem, proposed solution, priority, owner, status, and outcomes. Logged in the CIR with a unique identifier |
| Business Justification | Documents the reason, costs, expected benefits, success criteria, and measurements for an improvement initiative. May use Lean Canvas format for small-scale initiatives |
| Improvement Plan | Documents the approach, resources, timeline, methodology, and tasks for implementing an approved improvement initiative |
| Lessons Learned Report | Captures what was learned from an improvement initiative — what worked, what did not, what should be done differently. Produced at initiative completion and used for future initiatives |

## Process Interfaces
<!-- sources: ITIL 4 Continual Improvement §2.3 Table 2.1, §3, FitSM-2 §PR14 CSI Key Interfaces -->

| Interface | Relationship |
|-----------|-------------|
| All Practices | Every practice generates improvement opportunities and contributes suggestions to the CIR. The continual improvement practice supports improvement of all other practices, products, and services |
| Change Management (PR15) | Improvement initiatives that require changes to services, infrastructure, or processes are implemented through the change management process. Requests for change are a key output |
| Measurement & Reporting (PR20) | Provides tools, metrics, and baseline data for assessing the current state and measuring improvement results. Service reports are a key source of improvement opportunities |
| Service Level Management (PR02) | SLM practice reviews identify service quality issues that become improvement opportunities. Improvements affecting service consumers are agreed through SLM |
| Risk Management (PR21) | Risk assessments may identify improvement needs. Risks associated with improvement initiatives are assessed through the risk management practice |
| Incident Management (PR11) | Post-incident reviews generate improvement opportunities. Incident trends may reveal underlying issues requiring improvement |
| Problem Management (PR13) | Problem outcomes and known error workarounds generate improvement opportunities. Root cause analysis identifies improvement needs |
| Portfolio Management (PR01) | Major improvement initiatives require portfolio-level funding decisions and business case approval |
| Relationship Management (PR22) | Joint improvement initiatives with customers are negotiated through relationship management. Customer feedback is a key source of improvement ideas |
| Supplier Management (PR23) | Joint improvement initiatives with suppliers are negotiated through supplier management. Supply chain improvements require supplier collaboration |
| Knowledge Management (PR19) | Lessons learned from improvement initiatives feed into the knowledge management system. Knowledge sharing is critical to the success of continual improvement |
| Service Desk (PR10) | Provides interfaces between the service provider and users for feedback and improvement ideas |
| Project Management | Large improvement initiatives may be managed as projects. Project management provides planning, execution, and tracking capabilities |
