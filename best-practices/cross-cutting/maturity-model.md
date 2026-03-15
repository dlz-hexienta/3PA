---
process_id: cross-cutting
process_name: "Cross-Cutting"
category: maturity
frameworks:
  - itil-v4
  - fitsm
maturity:
  essential: true
  intermediate: true
  advanced: true
sources:
  - "FitSM-6 Assessment and Audit Tool V3.0.3"
  - "FitSM-1 Requirements V3.0.1 (GR1–GR7, PR1–PR14)"
  - "ITIL 4 Practice Guide: Continual Improvement §2.4, §3.2"
last_updated: 2026-03-14
status: draft
---

# Process Maturity Assessment Model

## How to Use This Model

This maturity model provides a structured framework for assessing the capability of each ITSM process and the SMS as a whole. It uses a 5-level scale (0–4) aligned with FitSM-6, with an optional extended level 5 for organizations pursuing optimization beyond managed performance. During P3 authoring, the `3pa-author` skill uses this model to calibrate best-practice content to the organization's current and target maturity levels. During P5 (Publish), the model supports maturity assessment for the continual improvement register. The maturity level descriptions are synthesized from FitSM-6 Assessment and Audit Tool V3.0.3 (which provides requirement-level capability descriptions for levels 0–4) and ITIL 4 Continual Improvement (which provides the improvement framework that enables maturity progression).

---

## Maturity Levels

| Level | Name | Description |
|:-----:|------|-------------|
| 0 | Absent / Unaware | No awareness or a significant lack of understanding of the required activities. Key outputs do not exist. The process is not recognized as needed or is entirely absent |
| 1 | Ad Hoc / Initial | Activities are performed reactively and on an individual basis. Outcomes depend on the people involved rather than on defined processes. Documentation is minimal, inconsistent, or absent. Results vary significantly between instances |
| 2 | Repeatable / Partial | A common understanding of how activities should be performed exists and is generally followed. Some documentation is in place but responsibilities may not be formally defined. Consistency is improving but remains dependent on individual initiative rather than organizational enforcement |
| 3 | Defined / Complete | Activities follow a defined and documented approach with clearly assigned responsibilities. All required elements of the process are in place. Processes are communicated, understood, and consistently followed. Records are produced reliably |
| 4 | Managed / Aligned | Beyond the achievement of level 3, required activities are managed, monitored, and their effectiveness and efficiency evaluated. KPIs are measured and used for process improvement. Process outcomes are predictable and controlled |
| 5 | Optimizing | Beyond the achievement of level 4, the process is subject to systematic continual improvement. Automation is applied where beneficial. The process adapts proactively to changing business needs. Innovation and optimization are embedded in the process culture |

**FitSM-6 alignment:** FitSM-6 defines levels 0–4. Level 5 (Optimizing) extends the model for organizations pursuing maturity beyond the FitSM certification scope. FitSM certification requires level 3 ("Defined / Complete") for all requirements in scope.

---

## General Requirements — Maturity Criteria
<!-- essential -->
<!-- sources: FitSM-6 Assessment Tool — GR1–GR7 -->

### GR1: Top Management Commitment & Accountability

| Level | Criteria |
|:-----:|----------|
| 0 | No awareness of SMS ownership or management commitment requirements |
| 1 | Top management deals reactively with service management issues. No clear allocation of SMS ownership. If a general commitment to service management exists, it is informal and not documented as a policy |
| 2 | Top management exerts some level of control over the SMS. An SMS owner role usually falls to a single individual but may not be formally defined. A general service management policy exists in some form. Management reviews take place but with variable frequency and structure |
| 3 | Top management actively controls the SMS. The SMS owner role — with competencies and tasks — is defined and documented. A comprehensive service management policy covers all necessary elements including clear and verifiable goals. Management reviews are conducted at planned intervals with defined frequency and content |
| 4 | Beyond level 3: SMS governance activities are managed, monitored, and their effectiveness evaluated. Management review outcomes drive measurable improvements |

### GR2: Documentation

| Level | Criteria |
|:-----:|----------|
| 0 | No service management documentation exists |
| 1 | Some initial documentation available. Key documents (scope statement, plan) may be missing. A minority of processes have been defined. Process documentation is very initial and does not address all required elements |
| 2 | Most required documents available including scope statement and policy. Core processes documented, especially those with high volumes. Outputs from most processes documented. Document control understood but not universally formalized |
| 3 | All key SMS elements documented: clear scope statement, comprehensive policy, full service management plan. All processes documented with goals, inputs, activities, outputs, roles, and interfaces. Outputs from all processes documented reliably. Document control responsibilities defined and documented for each document |
| 4 | Beyond level 3: documentation quality and completeness are monitored. Documentation reviews are tracked and their effectiveness evaluated |

### GR3: Scope & Stakeholders

| Level | Criteria |
|:-----:|----------|
| 0 | No awareness of SMS scope or stakeholder analysis requirements |
| 1 | A common understanding of SMS scope exists but is largely undocumented. Some information on stakeholders and legal/contractual context is understood |
| 2 | Documented information on SMS scope available but may be scattered across multiple documents. Stakeholder and legal/contractual context sufficiently understood with some documentation |
| 3 | A comprehensive scope statement exists describing services, locations, organizational units, and exclusions. Stakeholder interests, expectations, and legal/contractual context are documented in a defined and reliable manner |
| 4 | Beyond level 3: scope and stakeholder analysis are actively monitored for currency. Changes trigger systematic review |

### GR4: Planning

| Level | Criteria |
|:-----:|----------|
| 0 | No awareness of IT service management planning requirements |
| 1 | The provider is aware planning is needed but accountability is unclear. Process-specific plans are developed independently with little alignment |
| 2 | Generally good understanding of planning responsibilities. Some awareness of the need to align plans with one another and the overall service management plan |
| 3 | IT service management is planned with clearly defined and documented responsibilities. Process managers are aware of the need to align process-specific plans with the overarching plan. Alignment is a required step in plan creation |
| 4 | Beyond level 3: planning effectiveness is monitored. Plan achievement is tracked and deviations trigger corrective actions |

### GR5: Implementation

| Level | Criteria |
|:-----:|----------|
| 0 | No awareness of the need to implement service management plans |
| 1 | A general understanding exists that processes should be implemented per plan, but not all staff are aware of the necessity to adhere to policies and procedures. Processes are frequently bypassed |
| 2 | The service management plan is largely implemented. People comply with related policies and procedures in most cases. However, adherence is not universally enforced |
| 3 | The service management plan is implemented according to defined and assigned responsibilities. With very few exceptions, policies, processes, and procedures are followed in practice. SMS ownership ensures enforcement at all levels |
| 4 | Beyond level 3: implementation effectiveness is monitored. Process compliance is measured and deviations systematically addressed |

### GR6: Monitoring & Review

| Level | Criteria |
|:-----:|----------|
| 0 | No awareness of the need to measure process effectiveness |
| 1 | The provider is aware that measurements are important. Some basic measurements may exist but are not systematically applied or reported |
| 2 | KPIs are measured and reported for some processes, but not consistently across all processes. Reviews and audits occur but are not scheduled or systematic |
| 3 | For all processes, meaningful KPIs are defined, measured, and reported at planned intervals. A scheduled programme for reviews, audits, and maturity assessments is in place and executed according to schedule |
| 4 | Beyond level 3: monitoring and review activities themselves are evaluated for effectiveness. Insights consistently drive improvement decisions |

### GR7: Continual Improvement

| Level | Criteria |
|:-----:|----------|
| 0 | No awareness of the need for continual improvement |
| 1 | The provider is aware that improvement is important but roles and responsibilities for managing improvements are unclear. Deviations may be identified but corrective actions are not systematically managed |
| 2 | Nonconformities and deviations are usually detected and corrected. Improvements are often handled effectively but documentation is inconsistent |
| 3 | Nonconformities and deviations are detected by scheduled reviews and systematically corrected. Responsibilities for identifying, evaluating, and implementing improvements are clearly defined. Improvement success is reviewed |
| 4 | Beyond level 3: the improvement process itself is monitored for effectiveness. The organization demonstrates a measurable trend of improving service management maturity |

---

## Per-Process Maturity Criteria
<!-- essential -->
<!-- sources: FitSM-6 Assessment Tool — PR1–PR14; ITIL 4 practice guides (PR01–PR24) -->

This section provides maturity criteria for each process area. For FitSM processes (PR1–PR14), criteria are derived directly from FitSM-6 requirement-level capability descriptions. For additional ITIL 4 processes (PR03, PR04, PR05, PR10, PR14, PR18, PR19, PR20, PR21), criteria follow the same 0–4 pattern synthesized from the relevant ITIL 4 practice guide.

### PR01 Service Portfolio Management
<!-- sources: FitSM-6 PR1.1–PR1.4 -->

| Level | Criteria |
|:-----:|----------|
| 0 | No service portfolio exists. The organization cannot describe its service offerings in a structured way |
| 1 | The organization is generally aware of what services it offers and can describe them informally. Proposals for new services are managed ad-hoc. Service lifecycle is not managed — services are developed, deployed, and deactivated without a structured approach |
| 2 | A list of services exists with some structure. Proposals for new/changed services are evaluated using a mostly understood approach. Service lifecycle stages are understood but not always managed smoothly. Supplier relationships per service are understood to some extent |
| 3 | A defined approach for maintaining the service portfolio with documented responsibilities. Proposals evaluated via a defined channel and template. Services controlled throughout their lifecycle with defined phases and transitions. Well-understood supplier relationships per service based on a defined service model |
| 4 | Beyond level 3: portfolio management effectiveness is monitored. Portfolio performance data drives strategic decisions |

### PR02 Service Level Management
<!-- sources: FitSM-6 PR2.1–PR2.5 -->

| Level | Criteria |
|:-----:|----------|
| 0 | No service catalogue, no SLAs, no performance evaluation |
| 1 | The provider can communicate service offerings in some undefined format. No structured SLAs but some understanding of service delivery expectations. Performance monitoring is mostly technical, limited to key components |
| 2 | A list of offerings attempts to divide into logical services. Agreements for key services exist with some service targets. Performance evaluated by service but not systematically. OLAs/UAs exist to some extent for key components |
| 3 | A service catalogue clearly specifies differentiated offerings in value terms. All SLAs follow a defined template with clearly assigned negotiation responsibilities. Service performance evaluated systematically with documented responsibilities. OLAs/UAs follow a defined template and are reviewed at planned intervals |
| 4 | Beyond level 3: SLA management is monitored for effectiveness. Service performance trends drive proactive SLA adjustments |

### PR09 Information Security Management
<!-- sources: FitSM-6 PR6.1–PR6.5 -->

| Level | Criteria |
|:-----:|----------|
| 0 | No awareness of information security management requirements |
| 1 | Some awareness of security risks and basic measures (firewalls, passwords). No formal security policy. Security incidents handled reactively. Access control is basic and inconsistent |
| 2 | An information security policy exists but may not cover all aspects. Security risk assessments conducted for some areas. Security incidents are generally managed with some tracking. Access controls in place for most systems with some defined policies |
| 3 | A comprehensive security policy covering all required aspects with defined review intervals. Security risk assessments conducted systematically with documented responsibilities. All security incidents registered and managed per defined procedures. Access control follows a structured approach including provision, review, and revocation |
| 4 | Beyond level 3: security management effectiveness is monitored. Security metrics drive proactive improvement |

### PR11 Incident Management
<!-- sources: FitSM-6 PR9.1–PR9.6 (ISRM — incident scope) -->

| Level | Criteria |
|:-----:|----------|
| 0 | No incident management process. Incidents handled in entirely unstructured ways |
| 1 | Not all incidents are registered. Records vary significantly. Incidents resolved on a case-by-case basis. Escalation depends on individuals. Communication with users is at the discretion of support staff. Closure is based on individual choice. Major incidents are handled with special care but no defined approach |
| 2 | Most incidents recorded, classified, and prioritized. Incidents handled in a mostly effective way with reference to SLAs. Functional and hierarchical escalation occurs in most cases. Users usually informed of progress. Incidents closed in a generally consistent way. Major incidents understood and mostly handled with special attention |
| 3 | All incidents registered, classified, and prioritized per defined and documented criteria. Interfaces to SLM and PM are defined. Escalation follows documented procedures with defined triggers. Users systematically informed per defined approach. Closure follows documented guidelines. Major incidents managed from occurrence to closure per defined approach |
| 4 | Beyond level 3: incident management effectiveness is monitored. Incident trends drive proactive improvement and problem identification |

### PR13 Problem Management
<!-- sources: FitSM-6 PR10.1–PR10.4 -->

| Level | Criteria |
|:-----:|----------|
| 0 | No problem management process. Root causes not investigated |
| 1 | Problem identification depends on individuals. Investigation is ad-hoc. Known errors and workarounds maintained in varying locations and formats |
| 2 | Common understanding of when problems should be identified. Incident records routinely reviewed. Investigation follows a well-understood sequence. Known errors usually kept up-to-date though not universally perceived as a priority |
| 3 | Defined and documented approach for problem identification including provisions for trend analysis and proactive identification. Formal investigation approach with documented roles and responsibilities. Defined approach for maintaining known error information with documented guidelines and responsibilities |
| 4 | Beyond level 3: problem management effectiveness is monitored. Problem resolution contributes measurably to incident reduction |

### PR15 Change Management
<!-- sources: FitSM-6 PR12.1–PR12.6 -->

| Level | Criteria |
|:-----:|----------|
| 0 | No change management process. Changes implemented without control |
| 1 | Not all changes registered. Records vary. Changes handled differently depending on context. Assessment depends on individuals. Approval authorities unclear. Post-implementation review ad-hoc. No complete change schedule |
| 2 | Most changes registered and classified. Procedures for each change type understood and usually followed. Assessment follows a common approach considering benefits and risks. Approval follows a consensus approach. Post-implementation reviews conducted for most changes. A change schedule exists but may not be comprehensive |
| 3 | All changes registered and classified per documented procedures. Documented procedure for each change type with defined key decisions. Assessment follows a defined approach considering benefits, risks, impact, effort, and feasibility. Approval follows a defined approach with clear authority levels. Post-implementation reviews performed per defined criteria. Complete and accurate change schedule accessible to all interested parties |
| 4 | Beyond level 3: change management effectiveness is monitored. Change success rates and change-related incidents drive improvement |

### PR17 Configuration Management
<!-- sources: FitSM-6 PR11.1–PR11.5 -->

| Level | Criteria |
|:-----:|----------|
| 0 | No configuration management. CIs not tracked |
| 1 | Configuration items intuitively understood but CI types and relationships not formally defined. Configuration information recorded at a very basic level. CMDB concept is known but implemented very basically or not at all. Changes may or may not be tracked. No regular CMDB verification |
| 2 | Scope of configuration management documented in a general manner. Information recorded is generally enough to control each CI. A CMDB is maintained and is rather comprehensive. Changes to CIs usually reflected in CMDB. Verifications conducted at somewhat regular intervals but not planned |
| 3 | CI types and relationship types clearly defined and documented. Defined responsibilities and procedures for recording and updating configuration information. Fully integrated CMDB with complete CI records and relationships. CI information reflects current status with defined responsibilities for updates. CMDB verified at planned intervals with defined scope and quality metrics |
| 4 | Beyond level 3: configuration management effectiveness is monitored. CMDB accuracy and coverage metrics drive improvement |

### PR24 Continual Improvement
<!-- sources: FitSM-6 PR14.1–PR14.3 -->

| Level | Criteria |
|:-----:|----------|
| 0 | No awareness of the need for structured improvement |
| 1 | Opportunities for improvement are recognized by individuals and some are recorded. Evaluation is generally done by a responsible person but without a standard approach. Improvement actions taken where individuals consider them valuable but not consistently tracked |
| 2 | A common approach for seeking and recording improvements exists. Evaluation and approval of opportunities follows a mostly understood approach. Agreed improvement actions are usually implemented and progress tracked |
| 3 | A clearly defined approach to identifying and recording improvement opportunities based on multiple input sources. Evaluation and approval follows a defined approach whenever new opportunities arise. Agreed improvement actions are consistently managed, their status monitored, and effectiveness reviewed |
| 4 | Beyond level 3: the improvement process itself is monitored. Improvement throughput, realization rate, and value delivered are tracked and optimized |

### Additional Process Areas (PR03, PR04, PR05, PR10, PR14, PR18, PR19, PR20, PR21)
<!-- sources: ITIL 4 practice guides — applying standard maturity pattern -->

For processes not covered by FitSM (PR03 SFM, PR04 SDES, PR10 SDESK, PR14 MEM, PR18 ITAM, PR19 KM, PR20 MR, PR21 RM) and those with partial FitSM coverage (PR05 SCATM, PR06 AM, PR07 SCM — split from FitSM PR4 SACM), apply the standard maturity pattern:

| Level | Generic Criteria |
|:-----:|----------|
| 0 | Process does not exist or is not recognized |
| 1 | Activities are performed reactively by individuals. No formal process definition. Key artefacts are absent or inconsistent |
| 2 | A common understanding of activities exists. Key artefacts are maintained but informally. Responsibilities are understood but not formally documented |
| 3 | Process is defined and documented with clear roles, activities, inputs, outputs, and interfaces. Artefacts are produced reliably. The process is consistently followed |
| 4 | Process effectiveness is monitored through defined KPIs. Performance data drives improvement decisions. Process outcomes are predictable |

---

## Assessment Questionnaire Template
<!-- intermediate -->
<!-- sources: FitSM-6 Assessment Tool — assessment columns -->

Use this template to assess each process against the maturity criteria. One row per requirement or capability area.

| # | Process Area | Requirement / Capability | Current Level (0–4) | Target Level | Evidence | Gap Description | Improvement Priority |
|---|-------------|-------------------------|:-------------------:|:------------:|----------|-----------------|:-------------------:|
| 1 | {GR1 / PR01 / etc.} | {Specific requirement} | {0–4} | {0–4} | {Documentation, observations, interviews} | {What is missing to reach target} | {H / M / L} |
| 2 | | | | | | | |

### Assessment Scoring Guidance

| Score | Meaning | Evidence Required |
|:-----:|---------|-------------------|
| 0 | Not present | Absence of any evidence of the requirement |
| 1 | Ad hoc evidence | Some individuals demonstrate awareness; informal artefacts may exist |
| 2 | Partial evidence | Common understanding demonstrated; some documentation and records exist |
| 3 | Full evidence | Documented process, defined roles, consistent records, process followed in practice |
| 4 | Managed evidence | KPIs measured and reported, effectiveness evaluated, improvement actions traceable |

### Assessment Process

1. **Scope:** Identify which requirements are in scope for this assessment (GR1–GR7, selected PR processes)
2. **Evidence collection:** For each requirement, collect evidence from documentation review, interviews, and observation
3. **Scoring:** Assign a maturity level (0–4) based on the evidence against the criteria in this document
4. **Gap analysis:** For each requirement where the current level is below the target, describe the gap
5. **Prioritization:** Prioritize gaps based on business impact, effort required, and dependencies
6. **Reporting:** Produce an assessment report with overall maturity profile, key gaps, and recommended improvement roadmap

---

## Maturity Roadmap Template
<!-- advanced -->
<!-- sources: ITIL 4 CI §3.2; FitSM-6 gap analysis -->

Use this template to plan the journey from current to target maturity levels.

### Roadmap Structure

| Phase | Timeframe | Focus | Target Level | Key Activities |
|-------|-----------|-------|:------------:|----------------|
| **Foundation** | Months 1–3 | Establish governance and core processes | Level 2 for GR1–GR3, level 1–2 for priority processes | Define SMS scope, appoint SMS owner, document service management policy, establish core process definitions |
| **Stabilization** | Months 4–6 | Document and formalize all in-scope processes | Level 3 for GR1–GR7, level 2–3 for all in-scope processes | Complete all process definitions, establish document control, define KPIs, assign roles |
| **Maturation** | Months 7–12 | Implement measurement and systematic management | Level 3–4 for all areas | Implement KPI measurement, conduct first assessments, establish improvement pipeline, align plans |
| **Optimization** | Year 2+ | Achieve managed and optimizing performance | Level 4+ for priority areas | Systematic improvement programme, automation, proactive adaptation to changing needs |

### Improvement Initiative Tracking

| Initiative | Target Process | Current Level | Target Level | Owner | Status | Target Date | Dependencies |
|-----------|---------------|:------------:|:------------:|-------|--------|:-----------:|-------------|
| {e.g., Document all process definitions} | GR2 | 1 | 3 | {SMS Manager} | {Not started / In progress / Complete} | {Date} | {e.g., GR1 level 2 achieved} |

### Maturity Profile Visualization

Track maturity across all assessed areas using a radar/spider chart with the following axes:

- GR1: Management Commitment
- GR2: Documentation
- GR3: Scope & Stakeholders
- GR4: Planning
- GR5: Implementation
- GR6: Monitoring & Review
- GR7: Continual Improvement
- {Each in-scope process: PR01, PR02, ...}

Plot current state, target state, and FitSM certification threshold (level 3) to visualize the maturity gap.

---

## Notes

1. **FitSM certification:** FitSM certification requires level 3 ("Defined / Complete") for all requirements in scope. Organizations seeking certification should use this model to identify gaps against the level 3 criteria.
2. **Level 5 (Optimizing):** Level 5 extends the FitSM-6 model (which covers 0–4) for organizations that wish to track maturity beyond managed performance. It aligns with CMMI level 5 concepts and ITIL 4's emphasis on continual optimization. Not all processes need to reach level 5 — target levels should be set based on business value.
3. **Assessment frequency:** Initial assessments should be conducted during P1 (Intake) to establish baseline maturity. Follow-up assessments should be conducted at least annually, or after significant changes to the SMS.
4. **Maturity vs. capability:** FitSM-6 uses the term "capability level" for individual requirement assessment and "maturity" for overall process/SMS assessment. In this model, both terms refer to the same 0–4 (or 0–5) scale applied at different granularities.
5. **Non-linear progression:** Organizations do not need to achieve the same maturity level across all processes simultaneously. A pragmatic approach targets higher maturity for high-impact processes first, with lower-priority processes following at a sustainable pace.
