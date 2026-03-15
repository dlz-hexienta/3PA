---
process_id: PR24
process_name: "Continual Improvement"
category: procedures
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
  - "ITIL 4: Continual Improvement §3.2.1, §3.2.2"
  - "FitSM-2: §PR14 CSI"
  - "IT4IT: Cross-cutting"
last_updated: 2026-03-14
status: draft
---

# Continual Improvement — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures cover the core operational activities — managing improvement initiatives from identification through evaluation. Intermediate procedures add structured approaches for establishing the improvement framework, developing business justifications, and embedding continual improvement into organizational culture. Advanced procedures cover practice optimization and supply chain improvement. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (All tiers)

### PROC-CI-01: Manage Continual Improvement Initiatives
<!-- sources: ITIL 4 Continual Improvement §3.2.1 Tables 3.1, 3.2, FitSM-2 §PR14 CSI (manage evaluation of improvements, manage implementation of improvements) -->

**Trigger:** Improvement idea submitted by any stakeholder; post-incident review identifying improvement need; problem outcome generating improvement opportunity; service report highlighting performance gap; audit or assessment finding; customer feedback or complaint; scheduled CIR review cycle

**Inputs:** Suggestions for improvement from all sources, post-incident reviews and problem outcomes, baseline and current performance metrics, customer satisfaction metrics and feedback, service level management practice reviews, assessment and audit reports, service reports, organization's vision and objectives

**Outputs:** Improvement records (logged in CIR), updated CIR (prioritized, status-tracked), improvement plans, requests for change, performance measurements (before and after), lessons learned, improvements to services or the SMS

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify and log the improvement opportunity | Capture the improvement idea and log it in the CIR with a unique identifier. The initial idea does not need to be detailed — it is a starting point for understanding the delta between the current state and the desired future state. Record the requester or source, the configuration item affected (service, product, or practice), and an initial description of the expected value. Capturing ideas is everyone's responsibility | Any staff member / Continual Improvement Manager |
| 2 | Assess and prioritize | Evaluate the improvement opportunity against transparent criteria — considering benefits, cost or effort, urgency, risk, and alignment with organizational objectives. Prioritize against other initiatives in the CIR. When prioritization cannot be clearly assessed, escalate to a governance committee. Low-cost, low-effort initiatives can be prioritized for rapid value realization | Continual Improvement Manager / Improvement Owner |
| 3 | Approve and secure resources | For approved initiatives, secure funding and resources. Develop a business justification appropriate to the initiative's scale — from a simple cost-benefit statement for small improvements to a formal business case for large initiatives. Communicate appropriately with budget holders, referring to return on investment, clearly defined business outcomes, and the organization's vision | Improvement Owner / Senior Manager |
| 4 | Plan the improvement | Plan the approved initiative with appropriate resource allocation, timeline, and methodology. The level of planning should match the initiative's scale. Ensure improvement priorities are consistent with priorities for other types of work in which teams and resources are engaged. Separate the plan into smaller, manageable tasks | Improvement Owner |
| 5 | Facilitate implementation | Facilitate implementation according to the plan and chosen methodology. Track the status and progress of improvement actions through the CIR. Coordinate with the practices responsible for implementing changes. Submit requests for change where changes to services, infrastructure, or processes are required | Improvement Owner / Continual Improvement Manager |
| 6 | Measure and evaluate results | After completion, evaluate whether the improvement achieved its intended outcomes by comparing against agreed success criteria and KPIs. Capture lessons learned — documenting what worked, what did not, and what should be done differently. If expected outcomes were not fully achieved, prioritize gaps for following iterations. Showcase successful improvements to stakeholders to demonstrate value co-creation | Improvement Owner / Continual Improvement Manager |
| 7 | Close and communicate | Close the improvement record in the CIR. Communicate results — both successful outcomes and lessons from initiatives that did not achieve planned results. Relay decisions made as a result of feedback back to the originators. Update metrics and baselines to reflect the new state | Continual Improvement Manager |

---

## Intermediate Procedures (T2+)

### PROC-CI-02: Establish the Continual Improvement Approach
<!-- sources: ITIL 4 Continual Improvement §2.4.1.1, §2.4.1.2, §3.2.2 Tables 3.3, 3.4, FitSM-2 §PR14 CSI (initial process setup) -->

**Trigger:** Initial establishment of the continual improvement practice; organizational strategy change requiring revised improvement approach; periodic review of improvement effectiveness; organizational maturity assessment identifying improvement practice gaps

**Inputs:** Organizational vision and objectives, available frameworks and methods (Lean, Agile, DevOps, Six Sigma, COBIT), organizational change management practices, current organizational culture assessment, available tools and capabilities

**Outputs:** Documented continual improvement approach, CIR structure and tooling, improvement evaluation criteria, cultural change initiatives, adoption of selected methods and principles

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Define the improvement approach | Select and document the organization's continual improvement approach — adapting methods and techniques to the specific environment. Consider the typical timeframes in which challenges manifest. Establish a flexible framework that allows managers to switch between techniques depending on changing circumstances. Align with the continual improvement model (vision → baseline → targets → plan → action → evaluate → sustain) | Continual Improvement Manager / Senior Manager |
| 2 | Establish the CIR and tooling | Set up a tool supporting the recording, prioritization, evaluation, and approval of improvement suggestions. Define the structure and fields for improvement records. Define a standardized way to record suggestions from all identified sources. The CIR may be integrated into the service management system or be a standalone database | Continual Improvement Manager |
| 3 | Define evaluation and prioritization criteria | Establish transparent criteria for evaluating and prioritizing improvement opportunities — covering benefits, cost, effort, urgency, risk, and alignment with objectives. Define the governance escalation path for initiatives that cannot be clearly prioritized. Communicate criteria to all stakeholders | Continual Improvement Manager / Senior Manager |
| 4 | Identify improvement sources | Identify all relevant sources of potential improvement suggestions — including staff, customers, suppliers, incident reviews, problem records, risk registers, process performance records, service reports, and audit findings. Establish feedback channels for each source. Ensure all sources are aware of how to submit improvement ideas | Continual Improvement Manager |
| 5 | Communicate and embed | Communicate the improvement approach across the organization. Train stakeholders on how to identify and submit improvement opportunities. Integrate continual improvement expectations into job descriptions, employee objectives, and performance management. Celebrate early successes to build momentum | Continual Improvement Manager / Senior Manager |

---

### PROC-CI-03: Embed Continual Improvement into Organizational Culture
<!-- sources: ITIL 4 Continual Improvement §3.2.2 Tables 3.3, 3.4, §2.4.1.3, §2.4.1.4 -->

**Trigger:** Initial establishment of the continual improvement practice; cultural assessment revealing low adoption; strategic initiative to strengthen improvement capabilities; post-improvement review revealing cultural barriers

**Inputs:** Organizational change management practices, available frameworks and philosophies, current cultural assessment, lessons learned from improvement initiatives

**Outputs:** Cultural change, adoption of improvement principles, knowledge sharing practices, updated job descriptions and performance expectations

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Assess current culture | Assess the organization's current culture regarding continual improvement — including willingness to suggest improvements, risk tolerance, knowledge sharing norms, and senior management engagement. Identify cultural barriers to effective improvement | Continual Improvement Manager / Senior Manager |
| 2 | Integrate into organizational culture | Ensure senior managers model improvement behaviours — if they do not adopt the practice, others will not adopt it either. Update job descriptions to include service management and improvement responsibilities. Ensure employee goals and objectives consider continual improvement activities. Establish reward and recognition mechanisms for improvement contributions | Senior Manager / Continual Improvement Manager |
| 3 | Identify and adopt relevant principles | Adopt key principles adapted to the organization: focus on incremental changes (large changes are riskier), learn from mistakes, encourage ideas from all levels (many successful initiatives originate from operational staff), and measure improvement (without measurement, success cannot be confirmed) | Continual Improvement Manager |
| 4 | Promote knowledge sharing | Promote knowledge sharing as an organizational capability. In organizations where knowledge sharing is not the norm, successful improvements will be limited. Ensure lessons learned are documented, communicated, and accessible. Create an environment where transparency about outcomes — including failures — is the expectation | Senior Manager / Continual Improvement Manager |
| 5 | Sustain and reinforce | Maintain the safe-to-fail environment through ongoing leadership reinforcement. Celebrate successful improvements visibly. Ensure feedback originators receive responses about decisions made from their input. Monitor adoption of continual improvement behaviours and address declining engagement | Senior Manager / Continual Improvement Manager |

---

## Advanced Procedures (T3)

### PROC-CI-04: Optimize the Continual Improvement Practice
<!-- sources: ITIL 4 Continual Improvement §2.5, §2.4.2 -->

**Trigger:** Periodic assessment of the continual improvement practice (annually or semi-annually); declining improvement initiative success rates; low adoption of improvement culture; strategic planning cycle

**Inputs:** CIR data (volumes, success rates, cycle times), improvement initiative outcomes, stakeholder satisfaction data, adoption metrics, practice performance metrics

**Outputs:** Updated improvement approach and methods, refined evaluation criteria, practice improvement initiatives, updated cultural change strategies

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Assess practice effectiveness | Evaluate the continual improvement practice using the same measurement approach applied to other practices. Assess: volume and quality of improvement suggestions captured, prioritization effectiveness, implementation success rates, value delivered, cycle times, and stakeholder satisfaction. Identify which areas of the organization are delivering initiatives and which are not | Continual Improvement Manager |
| 2 | Assess cultural embedding | Evaluate how deeply continual improvement is embedded in the organizational culture. Assess awareness and adoption of the improvement approach. Identify teams or areas that require additional attention, training, or support from the continual improvement manager | Continual Improvement Manager / Senior Manager |
| 3 | Identify optimization opportunities | Based on the assessments, identify areas where the improvement approach, methods, tools, or cultural strategies need refinement. Consider whether the organization needs different improvement techniques for different types of challenges — structured project-based approaches for large initiatives, rapid iterative methods for urgent operational improvements | Continual Improvement Manager |
| 4 | Implement practice improvements | Implement changes to the continual improvement practice — updated evaluation criteria, improved CIR tooling, refined methods, additional training, or adjusted cultural strategies. Track the impact of these changes on practice performance metrics | Continual Improvement Manager |
| 5 | Report and communicate | Report on the state of the continual improvement practice to senior management. Communicate changes to the improvement approach. Ensure the practice continues to evolve alongside the organization's changing needs and maturity | Continual Improvement Manager |

---

### PROC-CI-05: Manage Supply Chain Improvement
<!-- sources: ITIL 4 Continual Improvement §6, §6.1, §6.2 -->

**Trigger:** Supplier delivering below expected quality; periodic supplier review identifying improvement opportunities; strategic initiative to strengthen supply chain; new supplier relationship established

**Inputs:** Supplier performance data, current supplier agreements, supply chain assessments, CIR entries related to supplier-provided services

**Outputs:** Joint improvement initiatives, updated supplier agreements, supply chain optimizations, requests for change

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify supply chain improvement opportunities | Review supplier performance and identify improvement opportunities across the supply chain. Consider options: accepting current quality, changing suppliers, adding quality control steps to value streams, or collaborating with suppliers to improve quality. Collaboration is generally preferred as it aligns with continual improvement principles | Continual Improvement Manager / Improvement Owner |
| 2 | Engage suppliers in improvement | Encourage suppliers and partners to submit improvement suggestions to the CIR. Establish open communication channels that remove formal bureaucratic barriers. Engage in regular discussions about mutual improvements. Suppliers can contribute at every step of the improvement model — from independently assessing current state to coaching, specialized skills, and independent evaluation of outcomes | Continual Improvement Manager |
| 3 | Plan joint improvements | Collaborate with suppliers to plan joint improvement initiatives — identifying unnecessary requirements, adjusting specifications, reassigning value stream activities, and adjusting delivery cadences and batch sizes. Ensure both parties understand the expected value and success criteria | Improvement Owner |
| 4 | Implement and evaluate | Implement supply chain improvements through agreed channels. Evaluate outcomes collaboratively. Capture lessons learned from both the service provider and supplier perspectives. Update supplier agreements to reflect improved arrangements where appropriate | Improvement Owner / Continual Improvement Manager |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-CI-01 | Manage Continual Improvement Initiatives | All | Improvement idea; incident review; performance gap; audit finding |
| PROC-CI-02 | Establish the Continual Improvement Approach | T2+ | Practice establishment; strategy change; effectiveness review |
| PROC-CI-03 | Embed Continual Improvement into Organizational Culture | T2+ | Practice establishment; cultural barriers; strategic initiative |
| PROC-CI-04 | Optimize the Continual Improvement Practice | T3 | Periodic assessment; declining success rates; strategic planning |
| PROC-CI-05 | Manage Supply Chain Improvement | T3 | Supplier quality issues; supplier review; new supplier relationship |
