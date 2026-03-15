---
process_id: PR19
process_name: "Knowledge Management"
category: procedures
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Knowledge Management §3.2.1–§3.2.3, §2.2, §4.1.3"
  - "IT4IT: Cross-cutting Functions"
last_updated: 2026-03-14
status: draft
---

# Knowledge Management — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier. The three ITIL 4 processes — establishing and maintaining the KM environment, on-demand information discovery, and knowledge asset management — are consolidated into five procedures. Knowledge management has no dedicated FitSM process — these procedures draw primarily from ITIL 4. Knowledge management is fundamentally a cultural practice — procedures provide structure, but their effectiveness depends on people's willingness to share, learn, and apply knowledge.

---

## Essential Procedures (T2+)

### PROC-KM-01: Establish and Maintain KM Environment
<!-- sources: ITIL 4 KM §3.2.1 Tables 3.1–3.2 Activities 1–3 -->

**Trigger:** Initiation of knowledge management practice, significant organizational change, scheduled review interval, or stakeholder satisfaction assessment indicating practice gaps.

**Scope:** Covers cultural assessment, requirements review, approach optimization, and environment establishment. Maps to definition activities 1–3.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Assess current culture of knowledge usage and sharing — review organizational information and knowledge flows, progress of KM practice improvement, stakeholder satisfaction, and whether knowledge management is up to date and meets organizational needs. Review results and requests for KM improvement from other practices. Nominate people and assign knowledge management team roles | Knowledge Manager | Stakeholder satisfaction data, improvement results, feedback from practices | Cultural assessment report, team role assignments |
| 2 | Review external and internal requirements and factors of influence — analyse external factors that impact the knowledge system (regulatory requirements such as GDPR, ISO 30401, industry standards), available emerging practices for data, information, and knowledge management, data analysis techniques and methods, and other information supporting the knowledge sharing environment | Knowledge Manager | Regulatory requirements, industry trends, emerging practices | Requirements analysis, factors of influence |
| 3 | Optimize response and identify improvements — based on cultural assessment and requirements review, identify the optimal response of the knowledge management approach to organizational strategy. Define or update the KM approach document including scope, methods, tools, cultural enablers, policies, roles, classification schemes, data and information quality guidelines, and knowledge system design. Not all best practices and new approaches should be implemented immediately — adopt only those that suit the organization's vision | Knowledge Manager | Cultural assessment, requirements analysis, organizational strategy | KM approach document, data and information quality guidelines, templates and guidance for KM lifecycle |

**Exit criteria:** Current knowledge culture assessed. External and internal requirements reviewed. KM approach document defined or updated with scope, methods, and guidelines. Knowledge management team roles assigned.

---

### PROC-KM-02: Process On-Demand Information Requests
<!-- sources: ITIL 4 KM §3.2.2 Tables 3.3–3.4 -->

**Trigger:** Receipt of an unusual or non-routine information request that cannot be fulfilled through existing knowledge systems and patterns — such as non-standard business analysis, emerging technology assessment, assessment of new regulations, or complex rare requests.

**Scope:** Covers request registration, research and data collection, information processing and presentation, acceptance, and initial knowledge integration assessment. Maps to definition activities 4–5 and part of 6.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Register information request — accept the request in agreed format, capturing area of information, purpose of requested information, currently available sources, requested format, timing, and other relevant parameters. Assess whether the request can be fulfilled through existing knowledge systems or requires dedicated research | Knowledge Manager | Information request | Registered and triaged request |
| 2 | Research and collect data — identify roles and people likely to be involved in the research and assign them (or request resource allocation). Agree on time that they devote to the research and expected outputs. Agree on data selection criteria. Obtain and review available data and information from internal and external sources in accordance with agreed procedures and constraints. Interview people and support tacit-to-explicit knowledge transfer where relevant | KM Team Member | Registered request, access to internal and external sources, information security policies, financial guidelines | Collected data and research findings |
| 3 | Process and present information — analyse and structure the collected data and present it in the agreed format. Provide resulting outputs to the agreed group of stakeholders | KM Team Member | Collected data, agreed format requirements | Information in requested format |
| 4 | Obtain acceptance — stakeholders (information requester and/or other intended recipients) review the research output and confirm acceptance, evaluating information quality, output format, and timeliness of presentation. If the information is not accepted, the request can be returned to the research step, or cancelled if no longer relevant or not viably fulfillable | Knowledge Asset Owner | Processed information, acceptance criteria | Accepted or returned information |

**Exit criteria:** Information request registered and triaged. Research conducted from relevant internal and external sources. Information processed and presented in agreed format. Stakeholder acceptance obtained or request appropriately resolved.

---

## Intermediate Procedures (T2+)

### PROC-KM-03: Manage Knowledge Assets
<!-- sources: ITIL 4 KM §3.2.3 Tables 3.5–3.6, §3.2.2 Table 3.4 Activity 5 -->

**Trigger:** Discovery of new or changed information assets, feedback from knowledge users, knowledge asset review findings, stakeholder request, or decision to standardize and integrate on-demand research outputs.

**Scope:** Covers knowledge asset discovery, analysis and classification, guideline development, guideline assignment, acceptance, and integration. Maps to definition activities 6–7 and part of 6.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Discover and identify knowledge assets — analyse the organization's information assets to identify new or changed knowledge assets. This activity is performed regularly or triggered by introduction of new information assets, feedback from knowledge users, knowledge asset review findings, or stakeholder requests. Assess accepted on-demand research outputs for integration opportunities — determining whether information should remain exclusive or be integrated into organizational systems | Knowledge Manager | Information assets, user feedback, review findings, accepted research outputs | New and changed knowledge assets identified |
| 2 | Analyse and classify knowledge assets — evaluate the importance of discovered knowledge assets and identify the appropriate management guidelines and the responsible team or role to assign knowledge asset management responsibilities to. If no applicable guideline has been identified (new asset type or incomplete guideline library), initiate development of a new management guideline | KM Team Member | Discovered knowledge assets, existing guidelines, classification scheme | Classified assets, guideline assignments or new guideline requests |
| 3 | Develop knowledge asset management guidelines — the knowledge manager, assisted by relevant specialists, develops guidelines for the management of newly discovered knowledge asset types. This includes assessment of applicable policies (information security, data quality, regulatory). Guidelines should include recommendations on who should take responsibility for management. Where possible, available guidelines are reused | Knowledge Manager | New guideline request, applicable policies, existing guideline library | Knowledge asset management guidelines |
| 4 | Assign guidelines and manage acceptance — when the applicable guideline is identified, assign it to the appropriate team or person to manage the information assets. The specialist team or person reviews the assignment and accepts or rejects it. Rejections should be explained in enough detail to facilitate reanalysis and reassignment. If accepted, the team or person follows the guideline as part of their usual work within value streams and practices | Knowledge Manager | Guidelines, identified responsible teams | Guideline assignments, acceptance records |

**Exit criteria:** Knowledge assets discovered and identified. Assets classified with appropriate management guidelines. Guidelines developed for new asset types. Assignments made and accepted by responsible teams.

---

### PROC-KM-04: Review and Improve KM Practice
<!-- sources: ITIL 4 KM §3.2.1 Table 3.2 Activity 4, §3.2.3 Table 3.6 Activity 6 -->

**Trigger:** Scheduled review interval, significant stakeholder feedback, completion of improvement initiatives, organizational changes, or knowledge asset review findings.

**Scope:** Covers practice review, improvement identification, initiative management, and knowledge asset effectiveness review. Maps to definition activity 8 and part of 10.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Review practice adoption and effectiveness — assess whether the KM approach, procedures, and guidelines are being followed. Evaluate knowledge usage metrics, stakeholder satisfaction, information request fulfilment rates, knowledge asset health, and practice performance against objectives | Knowledge Manager | KM approach, practice metrics, stakeholder feedback, knowledge asset reports | Practice review findings |
| 2 | Identify improvement initiatives — register all required and identified knowledge management improvement initiatives via the continual improvement register. Prioritize based on organizational impact, feasibility, and alignment with strategy | Knowledge Manager | Practice review findings, stakeholder feedback, audit results | Improvement initiatives registered |
| 3 | Coordinate and monitor improvements — involve relevant members of the organization and the continual improvement practice. Track improvement progress, assess effectiveness of implemented changes, and adjust priorities based on outcomes | Knowledge Manager | Improvement register, implementation progress | Updated improvement status, KM practice improvement plan |
| 4 | Review knowledge asset effectiveness — perform regular reviews of knowledge asset management to assess applicable key metrics of the practice and initiate improvements in the knowledge asset management process and the practice in general. Communicate improvement initiatives to relevant stakeholders | Knowledge Manager | Knowledge asset reports, management metrics | Asset management review findings, targeted improvements |

**Exit criteria:** Practice adoption and effectiveness assessed. Improvement initiatives identified and registered. Improvements coordinated and monitored. Knowledge asset management reviewed and improved.

---

## Advanced Procedures (T3)

### PROC-KM-05: Promote KM Culture and Partner Integration
<!-- sources: ITIL 4 KM §3.2.1 Table 3.2 Activity 5, §5.2, §6 -->

**Trigger:** Scheduled awareness programme, new organizational unit onboarding, partner/supplier onboarding or offboarding, low adoption metrics, or organizational change initiative.

**Scope:** Covers organizational promotion, training, empowerment, partner knowledge sharing, and absorptive capacity development. Maps to definition activity 9 and advanced aspects of practice coordination.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Create guidance and training materials — develop relevant guidance, training materials (text, videos, podcasts), awareness content, and reference documentation for knowledge management activities. Tailor materials to different audiences — technical teams, management, service desk, procurement, partners | Knowledge Manager | KM approach, stakeholder profiles, adoption gaps | Training materials, guidance documents, awareness content |
| 2 | Deliver training and support — share information via relevant channels, conduct training sessions, and actively support organization members in their knowledge management activities. Create feedback loops to measure adoption of promoted patterns and stakeholder satisfaction | KM Team Member | Training materials, delivery channels, target audiences | Training delivery records, adoption metrics, satisfaction data |
| 3 | Integrate KM into partner and supplier relationships — assess knowledge sharing risks when planning cooperation and knowledge sharing interfaces with partner organizations. Include knowledge management actions in onboarding/offboarding procedures to mitigate the risk of losing expertise when activities are outsourced. Agree on knowledge exchange terms that support mutual transparency and organizational absorptive capacity | Knowledge Manager | Partner/supplier agreements, onboarding procedures, risk assessments | Updated partner KM arrangements, onboarding/offboarding procedures |
| 4 | Leverage automation and emerging technologies — evaluate and implement data science technology, AI, machine learning, and other approaches to enhance knowledge management. Deploy knowledge search, visualization, content repository, collaboration, and analytics tools appropriate to the organization's needs and volumes. Assess automation impact and cost-effectiveness | Knowledge Manager | Technology assessments, automation opportunities, cost-benefit analyses | Technology implementation plans, automation deployments |
| 5 | Drive organizational change for knowledge culture — coordinate with organizational change management, workforce and talent management, and relationship management to embed knowledge sharing as a cultural norm. Measure and report on knowledge culture indicators including psychological safety, sharing willingness, and knowledge reuse rates | Knowledge Manager | OCM plans, workforce assessments, culture indicators | Culture change initiatives, knowledge culture reports |

**Exit criteria:** Training materials created and delivered to target audiences. Adoption metrics tracked and improving. Partner KM arrangements established. Automation opportunities evaluated and implemented where effective. Knowledge culture change initiatives underway.
