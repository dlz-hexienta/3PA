---
process_id: PR05
process_name: "Service Catalogue Management"
category: procedures
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Service Catalogue Management §3.2.1, §3.2.2"
  - "FitSM-2: §PR2 SLM (catalogue creation and maintenance)"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Catalogue Management — Best Practice Procedures

## How to Use These Procedures

Each procedure maps to one or more activities from the process definition and specifies step-by-step workflows. Procedures are graduated by maturity tier — Essential procedures should be implemented first, with Intermediate and Advanced procedures added as the practice matures. The two ITIL 4 sub-processes — defining and maintaining catalogue data/views, and providing catalogue views to stakeholders — are consolidated into five procedures. The second process is normally fully or largely automated; manual procedures are provided for exceptions.

---

## Essential Procedures (All tiers)

### PROC-SCATM-01: Design and Structure the Service Catalogue
<!-- sources: ITIL 4 Service Catalogue Management §3.2.1 Tables 3.1, 3.2, FitSM-2 §PR2 SLM -->

**Trigger:** New service management system establishment, significant change in organizational architecture or portfolio, scheduled review of catalogue structure, or stakeholder feedback indicating structural gaps.

**Scope:** Covers stakeholder analysis, data structure definition, and standard view design. Maps to definition activities 1–3.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Identify key stakeholder groups — users, customers, internal teams (technical, support, management), suppliers. Discover and analyse their requirements for catalogue information including scope, granularity, data sources, access controls, and update frequency. Use relationship managers, business analysts, and direct observation. For external service providers, also consider marketing research, benchmarking, industry standards, and regulations | Service Catalogue Manager | Organization's strategy and architecture, service portfolio, customer and user requirements | Stakeholder groups list; agreed requirements |
| 2 | Define the service catalogue data structure — core service data (name, description, status, owner, target audience) common to all services, plus view-specific attributes sourced from SLAs, financial systems, CMDB, and related records. Define the technical approach for data collection, maintenance, and presentation | Service Catalogue Manager, Technical Specialist | Stakeholder requirements, external data sources | Service catalogue data structure; automation and integration requirements |
| 3 | Define standard views for key stakeholder groups — user view (service descriptions, prerequisites, request procedures, SLAs, support info), customer view (service levels, financial data, performance, contracts), and service provider view (technical, security, risk, process info). Document user manuals for view settings where applicable | Service Catalogue Manager | Data structure, stakeholder requirements | Standard catalogue views; user manuals; automation requirements |
| 4 | Submit automation and integration requirements for implementation. The service catalogue manager acts as customer for automation solutions, participating in all related activities. Ensure requirements cover data population, integration, view generation, and access controls | Service Catalogue Manager | Automation requirements | Requirements submitted for implementation |

**Exit criteria:** Stakeholder requirements documented and agreed. Data structure defined. Standard views agreed with stakeholders. Automation requirements submitted.

---

### PROC-SCATM-02: Populate and Maintain Catalogue Data
<!-- sources: ITIL 4 Service Catalogue Management §3.2.1 Tables 3.1, 3.2, FitSM-2 §PR2 SLM -->

**Trigger:** Automation solutions implemented, new service added to portfolio, service changed or retired, external data source updated, or data quality issue detected.

**Scope:** Covers data collection, population, ongoing maintenance, and data quality assurance. Maps to definition activity 4.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | After automation solutions are implemented, collect and enter agreed service data following the defined structure. Populate core service data for all services in scope. Establish initial data integrations with external sources (SLAs, CMDB, financial systems) | Service Catalogue Manager, Technical Specialist | Data structure, service portfolio, external data sources | Initial catalogue data populated |
| 2 | Agree and implement data update procedures — define who updates which data, update triggers, update frequency, and quality checks. Where applicable, agree data sharing protocols or application interfaces with partners and suppliers | Service Catalogue Manager | Data update requirements, supplier agreements | Data update procedures; data sharing protocols |
| 3 | Maintain catalogue data on an ongoing basis — process new service additions, service changes, and service retirements. Update catalogue entries when portfolio lifecycle events occur. Work with service owners and external data owners to ensure timely updates | Service Catalogue Manager, Service Owner | Portfolio lifecycle events, service change notifications | Updated catalogue data |
| 4 | Verify catalogue data completeness and accuracy. Ensure all live services are represented. Cross-check catalogue data against external sources. Flag and correct discrepancies | Service Catalogue Manager | Catalogue data, external source data | Verified catalogue data; correction requests |

**Exit criteria:** All services in scope represented in the catalogue. Data integrations operational. Update procedures documented and followed. Data verified for completeness and accuracy.

---

## Intermediate Procedures (T2+)

### PROC-SCATM-03: Deliver Catalogue Views and Manage Access
<!-- sources: ITIL 4 Service Catalogue Management §3.2.2 Tables 3.3, 3.4 -->

**Trigger:** Stakeholder request for a catalogue view (typically automated through self-service portal), or manual request for a non-standard view.

**Scope:** Covers view request processing, validation, delivery, and feedback collection. Maps to definition activities 5–7. This process is fully or largely automated in most situations.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Process the catalogue view request — in automated scenarios, the user selects a catalogue view through the application interface. In manual scenarios, the service catalogue manager identifies data and data sources needed to fulfil the request | Service Catalogue Manager (if manual) | Catalogue view request, access rules | Data query initiated |
| 2 | Validate the request — check the requestor's entitlement to the requested data and verify data availability, including external integrations. If validation fails, provide a relevant message to the user | Service Catalogue Manager (if manual) | Access rules, data availability | Validated request; or rejection message |
| 3 | Form and present the requested view in the agreed format — typically on-screen through a portal. For manual requests, collect relevant data and assemble the view | Service Catalogue Manager (if manual) | Validated request, catalogue data | Service catalogue view delivered |
| 4 | Collect user feedback — according to agreed schedules or triggered by validation failures. Monitor catalogue errors — treat errors in user- and customer-facing views as incidents. Analyse feedback for improvement opportunities | Service Catalogue Manager | User feedback, error reports | Feedback data; incident records; improvement inputs |

**Exit criteria:** Catalogue views delivered to entitled stakeholders. Access validated against rules. Errors identified and treated as incidents. Feedback collected and analysed.

---

### PROC-SCATM-04: Monitor Data Quality and Improve
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2, §3.2.1 -->

**Trigger:** Scheduled data quality review, catalogue error reported, user feedback received, or change in stakeholder requirements.

**Scope:** Covers data quality monitoring, error management, and catalogue improvement. Maps to definition activities 6–7.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Monitor catalogue data quality on an ongoing basis — check for incorrect, missing, or dated information. Verify that automation tools and data integrations are working as agreed | Service Catalogue Manager | Catalogue data, integration status | Data quality assessment |
| 2 | Treat catalogue errors on user- and customer-facing views as incidents — raise incident records, analyse root causes, and implement corrections. Track error trends to identify systematic issues | Service Catalogue Manager | Error reports, incident data | Corrected data; incident records |
| 3 | Analyse user feedback and usage patterns — survey results, use patterns, favourite view settings, search requests. Identify gaps between stakeholder needs and current catalogue capabilities | Service Catalogue Manager | Feedback data, usage analytics | Improvement opportunities |
| 4 | Initiate improvements to catalogue structure, views, data sources, or automation. Submit change requests through agreed channels. Track implementation of documented improvements | Service Catalogue Manager | Improvement opportunities | Change requests; improvement initiatives |

**Exit criteria:** Data quality monitored continuously. Errors treated as incidents and resolved. Feedback analysed. Improvement initiatives raised and tracked.

---

## Advanced Procedures (T3)

### PROC-SCATM-05: Integrate Supplier Catalogues and Optimize Usability
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2, §6 -->

**Trigger:** New supplier onboarded, service network participation established, usability review scheduled, or user satisfaction below target.

**Scope:** Covers supplier catalogue integration, access control for suppliers, and user experience optimization. Maps to definition activities 8–9.

| Step | Action | Responsible | Input | Output |
|------|--------|-------------|-------|--------|
| 1 | Establish integration with suppliers' data sources and service catalogues — define data sharing protocols, APIs, update frequencies, and data quality requirements. Ensure integration is seamless and updates flow without delays | Technical Specialist, Service Catalogue Manager | Supplier agreements, integration requirements | Integrated supplier data; data sharing protocols |
| 2 | Define and control supplier access to the organization's catalogue — provide views similar to internal technical teams but with restricted access levels. Ensure security policies and contract obligations are not compromised | Service Catalogue Manager | Security policies, contract obligations | Supplier access rules; controlled access implemented |
| 3 | Agree on catalogue utility and warranty — define and monitor service levels for the catalogue itself, including availability, response times, data freshness, and completeness. Treat the catalogue as a service | Service Catalogue Manager | Catalogue SLA requirements | Catalogue utility and warranty agreement |
| 4 | Optimize catalogue usability — design for intuitive use, enable new users for effective catalogue use, monitor user satisfaction, and address feedback. Ensure the interface is smooth for both internal and external users | Service Catalogue Manager | Usability data, user feedback | Usability improvements; updated interface |
| 5 | Monitor and report on catalogue performance — adoption rates, satisfaction scores, error rates, data freshness, and integration health. Feed findings into the continual improvement of the catalogue and the practice | Service Catalogue Manager | Performance data, satisfaction surveys | Catalogue performance report; improvement inputs |

**Exit criteria:** Supplier integrations operational and monitored. Supplier access controlled. Catalogue treated as a service with defined utility and warranty. Usability optimized based on feedback. Performance reported.
