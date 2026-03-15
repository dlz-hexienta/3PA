---
process_id: cross-cutting
process_name: "Cross-Cutting"
category: policies
frameworks:
  - itil-v4
  - fitsm
maturity:
  essential: true
  intermediate: true
  advanced: true
sources:
  - "FitSM-1 Requirements V3.0.1 (GR1–GR7)"
  - "FitSM Sample Service Management Policy v1.0"
  - "ITIL 4 Practice Guides (policy sections)"
last_updated: 2026-03-14
status: draft
---

# Reusable Policy Statement Patterns

## How to Use These Patterns

Each section provides reusable policy statement patterns organized by the seven FitSM general requirement areas (GR1–GR7), process-level patterns, and compliance patterns. During P3 authoring, the `3pa-author` skill injects these patterns as starting content for SMS-level and process-level policy documents. Patterns are written as "shall" statements that organizations customize by inserting their specific organizational context, names, frequencies, and scope. Maturity annotations indicate when each pattern becomes relevant. Policy patterns draw from FitSM-1 general requirements (which provide the SMS-level governance framework), the FitSM Sample Service Management Policy (which demonstrates how to structure a concise policy), and ITIL 4 practice guides (which provide process-specific policy guidance).

---

## GR1 — Management Commitment & Accountability Patterns
<!-- essential -->
<!-- sources: FitSM-1 GR1.1–GR1.3; FitSM Sample Policy §Leadership -->

### SMS Ownership

A member of top management of the service provider shall be assigned as the SMS owner with overall accountability for the SMS. The SMS owner shall have authority to make decisions regarding the SMS scope, policy, and resources, and shall ensure that the SMS is aligned with organizational strategy.

### Service Management Policy

A general service management policy shall be defined and approved by the SMS owner. The policy shall include overall service management goals, a commitment to meeting service requirements, a commitment to continual improvement, and an acknowledgement of the service management principles governing service delivery.

### Management Reviews

The SMS owner shall conduct management reviews at planned intervals to evaluate the continuing suitability, adequacy, and effectiveness of the SMS. Management reviews shall consider audit results, service performance, customer feedback, process effectiveness, status of improvement actions, and changes that could affect the SMS. Review outcomes — including decisions and actions — shall be documented.

### Leadership Commitment

Top management shall demonstrate commitment to the service management policy and its implementation by providing the resources required to implement and improve service management and enhance customer satisfaction with IT services.

---

## GR2 — Documentation Management Patterns
<!-- essential -->
<!-- sources: FitSM-1 GR2.1–GR2.4 -->

### SMS Documentation

The key elements of the SMS shall be documented to support effective planning. This documentation shall include the SMS scope statement, the service management policy, the service management plan, process definitions for all processes in scope, and records of process outputs and key activities.

### Process Definitions

Documented definitions shall be created and maintained for all IT service management processes in scope. Each process definition shall include goals, inputs, activities, outputs, roles and responsibilities, and interfaces with other processes.

### Process Records

The key outputs of all IT service management processes shall be documented, and the execution of key activities shall be recorded in a consistent and reliable manner. For all key activities, records shall be created at the time of execution and maintained for the retention period specified in the documentation management policy.

### Document Control

Documented information shall be controlled — addressing creation and approval before distribution, review at planned intervals, versioning, storage at defined locations, and controlled distribution to authorized parties. For each document, responsibilities including ownership shall be defined and documented. All parties involved shall be aware of the mechanisms for accessing, contributing to, and providing feedback on documentation.

---

## GR3 — Scope & Stakeholder Patterns
<!-- essential -->
<!-- sources: FitSM-1 GR3.1–GR3.2 -->

### Stakeholder Identification

The stakeholders of the IT services and the SMS shall be identified and their needs and expectations analysed. Relevant stakeholders include customers, users, service providers, suppliers, regulatory bodies, and internal management. The legal and contractual context governing the organization's service delivery shall be documented.

### SMS Scope Definition

The scope of the SMS shall be defined taking into consideration the results from the stakeholder analysis. The scope statement shall describe the services covered, the organizational units included, physical locations, technical infrastructure, and any exclusions. The scope shall be reviewed when significant changes occur in the stakeholder environment or organizational structure.

---

## GR4 — Planning Patterns
<!-- intermediate -->
<!-- sources: FitSM-1 GR4.1–GR4.2 -->

### Service Management Plan

A service management plan shall be created and maintained. The plan shall include goals and timing of implementing or improving service management processes, resources (including people, technology, information, and financial resources) required, and roles and responsibilities for carrying out the plan.

### Plan Alignment

Any plan created within the scope of the SMS shall be aligned to other plans and the overall service management plan. Process managers shall ensure that process-specific plans are consistent with the overarching service management plan and with each other. Alignment with other plans shall be a required step in the creation of any new plan.

---

## GR5 — Implementation Patterns
<!-- intermediate -->
<!-- sources: FitSM-1 GR5.1–GR5.2 -->

### Plan Implementation

The service management plan shall be implemented according to defined and assigned responsibilities. Activities carried out shall be aligned with the plan, and progress shall be monitored against plan milestones and deliverables.

### Process Compliance

Within the scope of the SMS, the defined service management processes shall be followed in practice, and their application shall be enforced. All staff members shall be aware of and comply with relevant policies, processes, and procedures. The SMS owner shall ensure enforcement at all organizational levels.

---

## GR6 — Monitoring & Review Patterns
<!-- intermediate -->
<!-- sources: FitSM-1 GR6.1–GR6.2 -->

### Process Effectiveness Measurement

The effectiveness of the SMS and its IT service management processes shall be measured and evaluated based on suitable key performance indicators. For all processes, meaningful KPIs shall be defined, measured, reported on at planned intervals, and used as input for management reviews and improvement decisions.

### Assessments and Audits

Assessments and audits of the SMS shall be conducted at planned intervals to evaluate the level of maturity and conformity to the service management policy and plan. A scheduled programme for reviews, audits, and maturity assessments shall be in place. Activities shall be carried out according to the programme, and results shall be documented and used as input for improvement.

---

## GR7 — Continual Improvement Patterns
<!-- essential -->
<!-- sources: FitSM-1 GR7.1–GR7.2; FitSM Sample Policy §Continual improvement -->

### Nonconformity Management

Nonconformities and deviations from goals shall be identified and actions shall be taken to prevent them from recurring. Detection shall be based on scheduled reviews of KPI reports, audit findings, assessments, and service reviews. Corrective actions shall be assigned, tracked, and reviewed for effectiveness.

### Continual Improvement Commitment

The service management policy, service management plan, and all service management processes shall be subject to continual improvement. Feedback from business stakeholders shall be used to improve services and service quality. All proposals for improvements shall be recorded and evaluated. Responsibilities for identifying, evaluating, and implementing improvements shall be clearly defined. Service management shall be improved based on continual monitoring of process performance and effectiveness.

---

## Process-Level Policy Statement Patterns
<!-- essential -->
<!-- sources: synthesized from ITIL 4 practice guides + FitSM-1 PR1–PR14 -->

These patterns provide reusable "shall" statements for individual process policies. Each pattern can be customized for any of the 24 process areas by substituting the placeholders in curly braces.

### Scope and Applicability

{Process name} shall apply to all {scope elements} within the defined SMS scope. All staff involved in {process activity} shall follow the defined policies and procedures.

### Roles and Responsibilities

Roles and responsibilities for {process name} shall be clearly defined, documented, and communicated. A {process manager role} shall be designated with accountability for the operational execution of the process. A {process owner role} shall be designated with accountability for the process's fitness for purpose.

### Process Interfaces

{Process name} shall maintain defined interfaces with {related processes}. Inputs and outputs between processes shall be documented, and handoff procedures shall be established to ensure consistent information flow.

### Process Objectives and KPIs

Measurable objectives shall be defined for {process name}. Key performance indicators shall be established, measured at planned intervals, and reported to the process owner and SMS manager. KPI results shall be used to drive improvement decisions.

### Records and Reporting

All {record types} shall be created, maintained, and retained according to the organization's documentation management policy. {Process name} shall produce reports at planned intervals covering process performance, trends, and exceptions.

### Tools and Automation

{Process name} shall be supported by appropriate tools. Tools shall be configured to enforce process workflows, capture required data fields, and produce required reports. Tool selection and configuration shall be approved by the process owner.

---

## IT-Business Alignment Patterns
<!-- essential -->
<!-- sources: FitSM Sample Policy §IT-Business alignment, §Process approach -->

### Service-Business Alignment

The provision of IT services shall be aligned to customer and user needs. Services shall be delivered to a defined quality sufficient to satisfy requirements identified from business processes.

### Service Portfolio Governance

A clear service portfolio shall be developed and maintained as a basis for all service delivery and service management activities. For all services, appropriate service level agreements — agreed with relevant stakeholders — shall be in place.

### Process Approach

To effectively manage all IT services and underlying components, a process-based approach to service management shall be adopted. All required processes shall be defined, communicated, and improved based on business needs and feedback from people and parties involved. All roles and responsibilities for managing services — including roles as part of service management processes — shall be clearly defined.

---

## Training & Awareness Patterns
<!-- essential -->
<!-- sources: FitSM Sample Policy §Training & awareness; FitSM-1 GR5.2 -->

### Competence and Awareness

Through training and awareness measures, it shall be ensured that staff involved in service management activities can perform effectively according to their assigned roles. Competence requirements shall be identified for each role, and gaps shall be addressed through training, mentoring, or recruitment.

### Process Awareness

All staff operating within the scope of the SMS shall be aware of the service management policy, relevant process definitions, and their specific responsibilities. New staff shall receive orientation to the SMS. Awareness shall be reinforced through regular communication.

---

## Compliance Statement Patterns
<!-- intermediate -->
<!-- sources: synthesized from FitSM-1 GR3.1, GR6.2; ITIL 4 practice guides -->

### Regulatory Alignment

The SMS and its processes shall comply with applicable laws, regulations, and contractual obligations. Regulatory requirements shall be identified, documented, and communicated to relevant parties. Compliance shall be verified through regular assessments and audits.

### Framework Conformity

The SMS shall be designed and operated in conformity with {framework name} requirements. Conformity shall be assessed at planned intervals and nonconformities shall be addressed through corrective actions.

### Audit Readiness

The organization shall maintain sufficient documentation and evidence to support internal and external audits of the SMS. Process records, decision logs, and artefacts shall be retained for the period specified in the documentation management policy.

### Third-Party Assurance
<!-- advanced -->

Where services are delivered in collaboration with suppliers or partners, the organization shall ensure that third-party service management practices meet the requirements of the SMS. Supplier compliance shall be verified through contractual obligations, audits, and performance reviews.
