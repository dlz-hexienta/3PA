---
process_id: PR22
process_name: "Relationship Management"
category: procedures
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
  - "ITIL 4: Relationship Management §3.2.1, §3.2.2"
  - "FitSM-2: §PR7 CRM"
  - "IT4IT: S2P Value Stream"
  - "SIAM: Service Integration (relationship coordination)"
last_updated: 2026-03-13
status: draft
---

# Relationship Management — Best Practice Procedures

## How to Use This Procedure Library

Each procedure is graduated by maturity tier. Essential procedures are required at all tiers and cover the operational foundation of relationship management — maintaining stakeholder data, conducting service reviews, handling complaints, and measuring satisfaction. Intermediate procedures add a strategic layer — developing a formal relationship approach, building relationship models, and conducting relationship health reviews. The advanced procedure extends relationship management across multi-supplier integration boundaries. Organizations should implement Essential procedures first, then layer on higher-tier procedures as the practice matures.

---

## Essential Procedures (All Tiers)

### PROC-RELM-01: Maintain Customer and Stakeholder Database
<!-- sources: FitSM-2 §PR7 CRM (Initial Setup: identify customers, set up database; Ongoing: maintain customer database), ITIL 4 Relationship Management §2.2.4 -->

**Trigger:** New customer or stakeholder identified; change to existing stakeholder information; periodic scheduled review of database currency

**Inputs:** Information on customers and stakeholders, service catalogue, existing service level agreements, stakeholder communication from service reviews and service desk interactions

**Outputs:** Up-to-date customer/stakeholder database with contact information, service agreements, communication preferences, and engagement approach

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Identify customers and stakeholders | Identify the internal and external stakeholders who receive, contribute to, or are affected by the organization's services. Use service agreements, organizational charts, and input from service owners to build the initial list | Relationship Manager |
| 2 | Collect stakeholder information | For each identified stakeholder, gather contact details, the services they receive or are associated with, communication preferences, and any existing agreements or relationship history | Relationship Manager |
| 3 | Register stakeholder in the database | Create a record in the customer/stakeholder database with all required attributes. Link the stakeholder to the relevant services and agreements | Relationship Manager |
| 4 | Map stakeholder influence and interest | Assess each stakeholder's influence (ability to affect the organization) and interest (degree to which they are affected by or care about the organization's activities). Record the quadrant classification (manage closely, keep satisfied, keep informed, monitor) and the corresponding engagement approach | Relationship Manager |
| 5 | Review and update records periodically | At defined intervals (at least annually), review all stakeholder records for accuracy and completeness. Update contact information, service associations, and engagement approaches. Add new stakeholders and archive records for relationships that have ended | Relationship Manager |
| 6 | Communicate database changes to dependent processes | Notify Service Level Management, Service Desk, and other consuming processes when significant stakeholder changes occur (new customers, changed contact points, ended relationships) | Relationship Manager |

---

### PROC-RELM-02: Conduct Customer Service Review
<!-- sources: FitSM-2 §PR7 CRM (Ongoing: perform service reviews), ITIL 4 Relationship Management §3.2.2 Table 3.4 (co-creation and realization stages) -->

**Trigger:** Scheduled service review date reached; significant service event requiring ad-hoc review

**Inputs:** Service performance reports (from Measurement & Reporting), SLA achievement data (from Service Level Management), open incident and problem records, customer complaints log, previous service review actions, customer satisfaction data

**Outputs:** Service review report documenting discussed topics, agreed actions, customer requirements, and follow-up responsibilities

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Schedule the service review | Plan the service review according to the agreed cadence (defined in the SLA or relationship agreement). Confirm the date with the customer representative | Relationship Manager |
| 2 | Prepare the review pack | Compile service performance data, SLA achievement reports, open issues, complaints received since the last review, satisfaction survey results, and the status of actions from the previous review | Relationship Manager |
| 3 | Invite participants | Invite the customer representatives and internal participants — relationship manager or agent, service level manager, and relevant service owners | Relationship Manager |
| 4 | Conduct the service review | Discuss service performance against agreed targets, customer satisfaction, any complaints or issues, emerging customer requirements, and opportunities for service improvement. Review the status of previously agreed actions | Relationship Manager |
| 5 | Document outcomes and agreed actions | Record the key discussion points, decisions, agreed actions with owners and target dates, and any new customer requirements or change requests identified during the review | Relationship Manager |
| 6 | Distribute the service review report | Send the service review report to the customer representative, internal participants, and relevant process owners (Service Level Management, Service Portfolio Management, Continual Improvement) | Relationship Manager |
| 7 | Track agreed actions to completion | Monitor the completion of agreed actions. Escalate overdue actions. Report action status at the next service review | Relationship Manager |

---

### PROC-RELM-03: Handle Customer Complaint
<!-- sources: FitSM-2 §PR7 CRM (Ongoing: handle complaints), ITIL 4 Relationship Management §3.2.2 Table 3.4 (managing exceptions) -->

**Trigger:** Customer submits a formal complaint through any defined channel

**Inputs:** Customer complaint (via email, service desk, service review, direct communication), customer/stakeholder database, service level agreements, relevant service records

**Outputs:** Complaint record with investigation findings, resolution, corrective actions, and customer communication; updated complaints log

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Receive and register the complaint | Log the complaint in the complaints register with the date received, customer details, complaint description, and the service or topic involved | Relationship Manager |
| 2 | Acknowledge receipt to the customer | Confirm receipt of the complaint to the customer within the agreed timeframe. Communicate the expected investigation timeline and the contact person for follow-up | Relationship Manager |
| 3 | Assign the complaint for investigation | Determine who should investigate the complaint based on the service area and nature of the issue. Assign ownership and set investigation deadlines | Relationship Manager |
| 4 | Investigate the complaint | Gather relevant facts — review service records, incident logs, SLA data, and prior communications. Consult with the affected service owner and technical teams as needed. Identify root causes and contributing factors | Assigned Investigator |
| 5 | Determine resolution and corrective actions | Based on the investigation, determine the appropriate resolution for the customer and any corrective actions to prevent recurrence. Where the complaint reveals a systemic issue, raise a change request or continual improvement initiative | Relationship Manager |
| 6 | Communicate resolution to the customer | Inform the customer of the investigation findings, the resolution, and any corrective actions being taken. Confirm whether the customer considers the complaint resolved | Relationship Manager |
| 7 | Close the complaint and record lessons learned | Close the complaint record with the final status and resolution details. Review the complaint for patterns — if similar complaints recur, escalate to Continual Improvement. Include complaint data in the next service review | Relationship Manager |

---

### PROC-RELM-04: Measure Customer Satisfaction
<!-- sources: FitSM-2 §PR7 CRM (Ongoing: manage satisfaction), ITIL 4 Relationship Management §2.5 Table 2.5 PSF3 -->

**Trigger:** Scheduled satisfaction measurement cycle; post-interaction feedback opportunity; management request for satisfaction assessment

**Inputs:** Customer/stakeholder database, service catalogue, previous satisfaction results, complaint history, service review outcomes

**Outputs:** Customer satisfaction reports with scores, trends, and follow-up actions; input to service reviews and continual improvement

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Define the satisfaction measurement approach | Determine the measurement method (periodic surveys, post-interaction surveys, structured interviews, or a combination), the frequency, the target audience, and the scoring scale. At T1, a simple annual or semi-annual survey may suffice | Relationship Manager |
| 2 | Design or update the survey instrument | Create or revise the satisfaction survey. Include questions covering overall satisfaction, service quality, communication effectiveness, complaint handling, and willingness to recommend. Keep the survey concise to encourage completion | Relationship Manager |
| 3 | Distribute the survey | Send the survey to the defined audience at the scheduled interval. Use the communication channel most likely to reach the audience effectively (email, portal, in-person at service review) | Relationship Manager |
| 4 | Collect and compile responses | Gather completed surveys. Calculate response rates. Compile raw data for analysis | Relationship Manager |
| 5 | Analyse results | Calculate satisfaction scores by service, customer group, and overall. Compare with previous periods to identify trends. Highlight areas of strength and areas requiring attention. Cross-reference with complaint data and service performance | Relationship Manager |
| 6 | Report satisfaction results | Produce a satisfaction report for the relationship manager, service level manager, service owners, and leadership. Include scores, trends, key findings, and recommended actions | Relationship Manager |
| 7 | Initiate follow-up actions | Where satisfaction is below target or declining, define specific follow-up actions with owners and target dates. Feed findings into service reviews, SLA discussions, and the continual improvement register | Relationship Manager |

---

## Intermediate Procedures (T2+)

### PROC-RELM-05: Develop Relationship Approach and Models
<!-- sources: ITIL 4 Relationship Management §3.2.1 Tables 3.1, 3.2, §2.4.1 -->

**Trigger:** Initial establishment of the relationship management practice; significant change to organizational strategy, culture, or stakeholder landscape; periodic scheduled review of the relationship approach

**Inputs:** Organization's strategy and values, assessment of organizational culture, stakeholder maps, current relationship patterns and issues, feedback from relationship reviews and satisfaction data

**Outputs:** Documented relationship principles, relationship models for key stakeholder groups, training and awareness materials, communication plan for embedding the approach

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Analyse the organization's culture and strategy | Assess how the organization's current culture supports or hinders effective relationships. Review the organizational strategy and its implications for stakeholder relationships — which relationships are strategically important, what type of engagement is needed | Relationship Manager |
| 2 | Review and update stakeholder maps | Ensure the stakeholder map is current and comprehensive. Identify stakeholder groups that require formal relationship models. Prioritize groups based on strategic importance, relationship complexity, and current relationship health | Relationship Manager |
| 3 | Define relationship principles | Develop the key principles that will govern the organization's approach to relationships — values such as openness, collaboration, no-blame culture, psychological safety, and proactive communication. These principles define the desired characteristics of all organizational relationships | Relationship Manager |
| 4 | Develop relationship models | For each priority stakeholder group, create a relationship model that defines: the appropriate communality level (basic, cooperative, or partnership), the relationship journey stages, the key activities and responsibilities at each stage, the risks and opportunities, and the recommended behaviour patterns | Relationship Manager |
| 5 | Validate with stakeholders and leadership | Present the proposed principles and models to key stakeholders and organizational leadership for review and agreement. Incorporate feedback and secure endorsement | Relationship Manager |
| 6 | Embed through training and awareness | Communicate the agreed principles and models across the organization. Develop training and awareness materials. Integrate the approach with other practices — workforce management, service desk, service level management. Ensure relationship agents understand and can apply the models | Relationship Manager |
| 7 | Publish models for operational use | Make the approved relationship models available to relationship agents and other staff who manage stakeholder interactions. Establish a review cycle to keep the models current | Relationship Manager |

---

### PROC-RELM-06: Conduct Relationship Review
<!-- sources: ITIL 4 Relationship Management §3.2.1 Table 3.2 (review and adjust), §3.2.2 Table 3.4 (review the relationship), §2.4.2 -->

**Trigger:** Scheduled relationship review date; significant relationship event (major complaint, conflict, stakeholder change, strategy change); request from leadership

**Inputs:** Stakeholder satisfaction data, complaint records and trends, relationship incident/conflict reports, service review outcomes, employee engagement and internal collaboration data, current relationship models and principles

**Outputs:** Relationship review report with health assessment, lessons learned, and improvement initiatives; input to continual improvement register

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Define the review scope | Determine which relationships or relationship areas will be reviewed — a specific key customer, internal team relationships, a stakeholder group, or the overall relationship approach. Confirm the review participants | Relationship Manager |
| 2 | Gather relationship health data | Collect relevant data: satisfaction scores, complaint volumes and trends, conflict or relationship incident reports, service review outcomes, employee feedback on internal collaboration, and any informal feedback from relationship agents | Relationship Manager |
| 3 | Assess relationship health | Evaluate the health and effectiveness of the relationships in scope against the agreed models and principles. Identify strengths (healthy relationships, effective models) and areas of concern (declining satisfaction, recurring conflicts, poor adoption of principles) | Relationship Manager |
| 4 | Assess internal relationship health | Review the health of internal relationships — between teams, departments, and individuals. Use employee feedback, climate assessments, and observations from relationship agents. Identify toxic behaviour patterns (criticism, defensiveness, contempt, obstruction) if present | Relationship Manager |
| 5 | Identify improvement opportunities | Based on the assessment, identify specific improvement initiatives — updates to relationship models, additional training, targeted interventions for troubled relationships, process changes to address systemic complaints | Relationship Manager |
| 6 | Document and communicate findings | Produce a relationship review report with findings, lessons learned, and recommended improvement actions with owners and target dates. Communicate findings to relevant parties — leadership, relationship agents, and affected stakeholders | Relationship Manager |
| 7 | Register improvements | Submit improvement initiatives to the continual improvement register. Track implementation of agreed actions. Feed outcomes back into the next review cycle | Relationship Manager |

---

## Advanced Procedures (T3)

### PROC-RELM-07: Coordinate Cross-Boundary Relationship Management
<!-- sources: ITIL 4 Relationship Management §6, SIAM Service Integration (relationship coordination) -->

**Trigger:** New multi-supplier arrangement established; significant change to the service integration model; periodic review of cross-boundary relationship effectiveness

**Inputs:** Service integration model and supplier landscape, supplier relationship data (from Supplier Management), cross-boundary complaints and relationship incidents, relationship models and principles of all parties

**Outputs:** Coordinated cross-boundary relationship approach, aligned relationship models, mutual transparency arrangements, cross-boundary relationship health reports

| Step | Activity | Description | Role |
|:----:|----------|-------------|------|
| 1 | Map cross-boundary relationships | Identify all relationship touchpoints that cross organizational boundaries — between the organization, its service integrator (if any), and individual service providers. Map which parties interact with which stakeholders and how | Relationship Manager |
| 2 | Assess current cross-boundary relationship health | Evaluate the effectiveness of existing cross-boundary relationships. Identify friction points, communication gaps, conflicting relationship approaches, and customer impact | Relationship Manager |
| 3 | Align relationship principles across boundaries | Work with counterparts at partner organizations and the service integrator to agree on shared relationship principles that apply across the service ecosystem. Address differences in relationship culture and communication styles | Relationship Manager |
| 4 | Establish coordination mechanisms | Define how relationship management activities will be coordinated — shared stakeholder registers, joint service reviews, unified complaint handling, mutual escalation paths, and information sharing arrangements | Relationship Manager |
| 5 | Define mutual transparency requirements | Agree on what relationship information will be shared between parties — customer feedback, complaint data, satisfaction scores, planned relationship changes that could affect other parties | Relationship Manager |
| 6 | Implement and operate the coordinated approach | Execute the agreed coordination mechanisms. Conduct joint service reviews where appropriate. Share relationship data as agreed. Coordinate stakeholder communications to present a coherent service experience | Relationship Manager |
| 7 | Review and adjust cross-boundary arrangements | Periodically assess whether the cross-boundary relationship approach is effective. Adjust coordination mechanisms, information sharing, and aligned principles based on outcomes and stakeholder feedback | Relationship Manager |

---

## Procedure Summary by Tier

| Procedure ID | Name | Tier | Trigger |
|-------------|------|------|---------|
| PROC-RELM-01 | Maintain Customer and Stakeholder Database | All | New stakeholder; information change; periodic review |
| PROC-RELM-02 | Conduct Customer Service Review | All | Scheduled review date; significant service event |
| PROC-RELM-03 | Handle Customer Complaint | All | Customer complaint received |
| PROC-RELM-04 | Measure Customer Satisfaction | All | Scheduled measurement cycle |
| PROC-RELM-05 | Develop Relationship Approach and Models | T2+ | Practice establishment; strategy/culture change; periodic review |
| PROC-RELM-06 | Conduct Relationship Review | T2+ | Scheduled review; significant relationship event |
| PROC-RELM-07 | Coordinate Cross-Boundary Relationship Management | T3 | New multi-supplier arrangement; integration model change |
