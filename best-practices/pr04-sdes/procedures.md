---
process_id: PR04
process_name: "Service Design"
category: procedures
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T3
sources:
  - "ITIL 4: Service Design §3.2.1, §3.2.2"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Design — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier — Essential procedures should be implemented first, with Intermediate and Advanced procedures added as the practice matures. All procedures apply only at T3 complexity. The two ITIL 4 sub-processes — service design planning and service design coordination — are consolidated into five procedures. Regular reviews of the planning process should take place every two to three months or more frequently, depending on the effectiveness of existing models and procedures.

---

## Essential Procedures (All tiers)

### PROC-SDES-01: Define and Maintain the Service Design Approach
<!-- sources: ITIL 4 Service Design §3.2.1 Tables 3.1, 3.2 -->

**Trigger:** New organizational strategy or portfolio change, significant change affecting service design (architecture, risk appetite, market position, compliance), scheduled periodic review (recommended every 2–3 months), or event-based trigger (design failures, new requirements, feedback).

**Scope:** Covers environment analysis, approach definition, and approach agreement. Maps to service design planning process activities 1–2.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Analyse the service and product environment — assess preferred approaches, nature of products and services, architecture decisions, customer and user feedback, risk appetite, compliance and regulatory constraints, market position, financial conditions, and level of control over service components | Service Design Leader | Organization's strategy and portfolio, architectural decisions, customer/user feedback, policies and regulatory requirements, service catalogue, SLAs | Service design environment analysis |
| 2 | Assess the factors that determine the design approach — strategic goals, current and potential customers, communication channels, ability to innovate, resource constraints, risk appetite, project management methods, and the partner and supplier ecosystem | Service Design Leader | Environment analysis, current design approaches | Assessment of design approach requirements |
| 3 | Discuss and agree a new or updated service design approach with relevant stakeholders. The approach may differ across the product and service portfolio. Ensure flexibility to adapt to changing circumstances | Service Design Leader | Assessment, stakeholder input | Documented service design approach |
| 4 | Review and approve the approach with executive stakeholders. Where multiple approaches exist for different product and service types, document the criteria for selecting each approach | Service Design Leader | Draft approach | Approved service design approach; improvement initiatives |

**Exit criteria:** Service design approach documented, agreed, and approved. Criteria for selecting approaches defined for different product and service types.

---

### PROC-SDES-02: Develop Design Models and Plan Instances
<!-- sources: ITIL 4 Service Design §3.2.1 Tables 3.1, 3.2 -->

**Trigger:** New or updated service design approach, new service design instance requiring a model, or scheduled model review.

**Scope:** Covers model development, instance planning, and plan communication. Maps to service design planning process activities 3–5.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Based on the approach, define or update service design models — including procedures, controls, SDP templates, plan and schedule templates, communications plan templates, and knowledge article templates. Assess whether existing models can support the design instance in question | Service Design Consultant | Approved approach, current models, service requirements | Updated service design models; SDP templates |
| 2 | For specific design instances, assess requirements considering innovation level, previous knowledge, architecture, product environment, SLA and user relationships, policies, and financial constraints. Select an existing model or trigger PROC-SDES-01 for a new approach | Service Design Consultant | Service requirements, existing models | Selected model or new approach trigger |
| 3 | Plan the design instance — define methods for requirements tracking, target audience and communications, interactions with partners and suppliers, financial plan and budget control methods, SDP contents, and resource plans | Service Design Consultant, Service/Product Owner | Selected model, instance requirements | Service design plan; SDP outline |
| 4 | Prepare communications for new or updated design plans, SDPs, methods, and procedures. Review with stakeholders and feed into service desk and knowledge management | Service Design Leader | Design plan, SDP template | Service design communications; updated knowledge articles |

**Exit criteria:** Design models documented and reusable. Instance plan complete with resource allocations. Communications prepared and distributed.

---

## Intermediate Procedures (T2+)

### PROC-SDES-03: Coordinate Service Design Execution
<!-- sources: ITIL 4 Service Design §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Service design instance initiated — new or significantly changed product or service requiring design coordination.

**Scope:** Covers model identification, resource planning, and design execution orchestration. Maps to service design coordination process activities 1–3.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Assess service requirements, complexity, interdependencies with existing services, budget, and risks. Choose the appropriate service design model. If no suitable model exists, trigger PROC-SDES-02 for model development | Service Design Consultant | Service requirements, existing models, budget | Selected model; service design records |
| 2 | Plan design activities based on the selected model. Identify teams involved, plan and request resource allocations. Identify additional capabilities that may need to be purchased, outsourced, or gained. Assign responsibilities for maintaining the SDP and managing risks | Service Design Consultant | Selected model, resource requirements | Detailed activity plan; resource allocations; responsibility assignments |
| 3 | Orchestrate and coordinate teams and resources involved in design execution — manage requirements tracking, communications, information exchange, fast feedback, and data flow. Ensure a holistic view of the design at every stage. Coordinate with project management, change management, software development, infrastructure management, business analysis, service validation and testing, and supplier management | Service Design Consultant | Activity plan, SDP, design models | Updated SDP; service design records; design communications; updated risk register |
| 4 | Monitor design execution progress against the plan. Manage issues and risks. Escalate where resource allocations or capabilities are insufficient. Gather feedback from users, customers, and involved team members throughout the process | Service Design Consultant | Execution status, feedback | Progress reports; feedback records; escalations |

**Exit criteria:** Design execution coordinated across all teams. SDP updated throughout execution. Feedback gathered and processed. Issues escalated and managed.

---

### PROC-SDES-04: Review Service Design Outcomes
<!-- sources: ITIL 4 Service Design §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Service design execution completed or reached a review milestone.

**Scope:** Covers design review, compliance assessment, lessons learned, and feedback to the planning process. Maps to service design coordination process activity 4.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Review the service design for compliance with standards, conventions, and the agreed SDP requirements. Verify that all elements of the SDP have been completed correctly — including all four dimensions and CX/UX considerations | Service Design Leader | Completed SDP, standards, design records | Compliance assessment |
| 2 | Assess whether the service is fit for purpose and fit for use — evaluating utility and warranty requirements. Engage stakeholders including product owners, customers, and testing specialists | Service Design Leader, Service/Product Owner | Compliance assessment, stakeholder feedback | Fitness assessment |
| 3 | Document lessons learned, update the knowledge base, and log improvement initiatives. Identify opportunities to improve design approaches, models, or procedures | Service Design Consultant | Assessment results, execution experience | Lessons learned; updated knowledge articles; improvement initiatives |
| 4 | Produce the service design review report. If findings indicate the need for approach or model changes, trigger PROC-SDES-01 or PROC-SDES-02. Update the service portfolio and risk register as appropriate | Service Design Leader | Assessments, lessons learned | Service design review report; portfolio updates; updated risk register |

**Exit criteria:** Design reviewed for compliance and fitness. Lessons learned captured. Review report produced. Portfolio and risk register updated.

---

## Advanced Procedures (T3)

### PROC-SDES-05: Model Risk Tiers and Optimize the Practice
<!-- sources: ITIL 4 Service Design §2.2.5, §2.4.1, §2.5 -->

**Trigger:** New service requiring risk profiling, scheduled risk model review, practice optimization review, or significant design failure or stakeholder dissatisfaction.

**Scope:** Covers risk modelling, tier assignment, waiver management, and practice optimization. Maps to definition activities 9–10.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Develop and maintain risk questionnaires covering data (confidentiality, integrity, availability), financial impacts, regulatory obligations, known risks and constraints, reputational damage, and disaster scenarios. Define an agreed risk impact matrix detailing possible impacts at business operations level | Service Design Leader | Risk management approach, business impact data | Risk questionnaire; risk impact matrix |
| 2 | Develop and calibrate the tier algorithm — agree the number of service tiers, score distribution for questions, maximum score thresholds, and target percentage of services at each tier. Calibrate using representative services | Service Design Leader | Risk impact matrix, service portfolio | Calibrated tier algorithm |
| 3 | Profile services at service line, customer journey, and IT service levels. Identify the critical path within each service — what would stop the consumer from completing their task. Assign risk-aligned tiers and corresponding SDPs | Service Design Consultant | Tier algorithm, service inventory | Risk-profiled services; tier assignments; SDP requirements |
| 4 | Manage service design waivers and dispensations where performance does not meet SDP requirements. Document mitigations and agree milestone dates for remediation. Track waivers in the continual improvement register. Enduring waivers require explicit business acceptance of risk exposure | Service Design Leader | Compliance gaps, waiver requests | Documented waivers with remediation plans |
| 5 | Review and optimize the service design practice — evaluate adherence to approaches across the portfolio, assess fitness for purpose of designed services, measure stakeholder satisfaction with design approaches and the organization's ability to innovate by design. Raise improvement initiatives to eliminate waste and increase effectiveness | Service Design Leader | Practice performance data, stakeholder satisfaction, design outcomes | Practice optimization report; improvement initiatives |

**Exit criteria:** Risk models calibrated and applied across the portfolio. Waivers managed with remediation plans. Practice reviewed and optimization initiatives raised.
