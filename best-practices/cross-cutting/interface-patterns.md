---
process_id: cross-cutting
process_name: "Cross-Cutting"
category: interfaces
frameworks:
  - itil-v4
  - fitsm
maturity:
  essential: true
  intermediate: true
  advanced: true
sources:
  - "FitSM-2 Process activities and implementation V3.0.2"
  - "ITIL 4 Practice Guides (interface sections)"
last_updated: 2026-03-14
status: draft
---

# Standard Process Interface Patterns

## How to Use These Patterns

This document catalogs the standard interfaces between ITSM processes, organized by the Phase A→B→C→D authoring order. Each interface specifies the source process, the output it produces, the target process that consumes the output, and the trigger for the handoff. During P3 authoring, the `3pa-author` skill uses these patterns to pre-populate interface sections in process definitions and to verify interface consistency across documents (gate G5). Organizations should customize by adding tool-specific integration details and removing interfaces for processes not in scope. Interfaces are synthesized from FitSM-2 process activities (which define explicit inputs and outputs for each process) and ITIL 4 practice guides (which describe interfaces for all 24 practice areas).

---

## Phase A → B Interfaces
<!-- essential -->
<!-- sources: ITIL 4 SPM, ISM, SCFGM, SFM → SLM, SDES, SCATM, RELM, SUPPM -->

Foundation processes (Phase A) produce the strategic and structural artefacts that Agreement processes (Phase B) consume to establish commitments with customers and suppliers.

| Source Process | Output | Target Process | Input | Trigger |
|---------------|--------|---------------|-------|---------|
| PR01 SPM | Service portfolio (approved services, lifecycle status) | PR02 SLM | Services requiring SLAs | New/changed service approved |
| PR01 SPM | Service portfolio (service specifications) | PR05 SCATM | Service descriptions for catalogue | Service enters operation lifecycle stage |
| PR01 SPM | Service models (supplier dependencies) | PR23 SUPPM | Suppliers requiring contracts | New service with external dependencies |
| PR01 SPM | Service portfolio (new service proposals) | PR04 SDES | Services requiring design packages | Service proposal approved for design |
| PR01 SPM | Service portfolio (demand forecasts) | PR03 SFM | Services requiring financial models | Budget cycle or new service approved |
| PR09 ISM | Security policy, classification scheme, security requirements | PR02 SLM | Security clauses for SLAs | New/changed SLA negotiation |
| PR09 ISM | Security policy, compliance requirements | PR23 SUPPM | Security requirements for supplier contracts | New supplier onboarding |
| PR09 ISM | Security risk assessment, control requirements | PR04 SDES | Security design constraints | Service design initiated |
| PR17 SCFGM | CI data, service models, dependency maps | PR02 SLM | Infrastructure underpinning SLA targets | SLA review or new SLA negotiation |
| PR17 SCFGM | CI data, configuration baselines | PR05 SCATM | Technical service component details | Catalogue update triggered |
| PR17 SCFGM | CI ownership, CI relationships | PR04 SDES | Existing configuration for design | Service design initiated |
| PR03 SFM | Cost models, charging policies | PR02 SLM | Financial terms for SLAs | SLA negotiation (T3) |
| PR03 SFM | Budget allocations, investment priorities | PR01 SPM | Financial constraints for portfolio decisions | Budget cycle (T3) |

---

## Phase B → C Interfaces
<!-- essential -->
<!-- sources: ITIL 4 SLM, SDES, SCATM, RELM, SUPPM → SDESK, IM, SRM, PM, MEM, CHM, RDM -->

Agreement processes (Phase B) produce the commitments and designs that Operations processes (Phase C) use to execute day-to-day service delivery and support.

| Source Process | Output | Target Process | Input | Trigger |
|---------------|--------|---------------|-------|---------|
| PR02 SLM | SLAs (service targets, response/resolution times) | PR11 IM | Priority targets, escalation thresholds | Incident registered |
| PR02 SLM | SLAs (service targets) | PR12 SRM | Fulfilment timelines, service entitlements | Service request submitted |
| PR02 SLM | SLAs (availability, performance targets) | PR14 MEM | Monitoring thresholds, event rules | Monitoring configuration updated |
| PR02 SLM | OLAs, UAs (internal/external support targets) | PR11 IM | Escalation targets by support group | Functional escalation triggered |
| PR02 SLM | OLAs, UAs | PR15 CHM | Change assessment criteria, impact scope | Change submitted for assessment |
| PR04 SDES | Service design package (architecture, deployment model) | PR16 RDM | Release and deployment specifications | New/changed service ready for build |
| PR04 SDES | Service design package (operational requirements) | PR10 SDESK | Support model, contact channels, scripts | New service enters operation |
| PR04 SDES | Service design package (monitoring requirements) | PR14 MEM | Monitoring specifications, thresholds | New service enters operation |
| PR05 SCATM | Service catalogue (published services, request types) | PR12 SRM | Request catalogue, fulfilment models | User requests service |
| PR05 SCATM | Service catalogue (service descriptions, user guidance) | PR10 SDESK | Service information for user queries | User contacts service desk |
| PR22 RELM | Customer communication channels, escalation contacts | PR11 IM | Stakeholder communication during incidents | Major incident declared |
| PR22 RELM | Customer satisfaction data, complaint records | PR13 PM | Trend data indicating systemic issues | Problem identification triggered |
| PR22 RELM | Service ordering channels | PR12 SRM | Service request submission routes | User requests service |
| PR23 SUPPM | Supplier contracts, OLAs | PR11 IM | Supplier escalation paths, support obligations | Incident requires supplier involvement |
| PR23 SUPPM | Supplier contracts, performance obligations | PR15 CHM | Supplier change coordination requirements | Change affects supplier-managed CIs |
| PR23 SUPPM | Supplier contracts, delivery schedules | PR16 RDM | Supplier delivery coordination | Release includes supplier components |

---

## Phase C → D Interfaces
<!-- essential -->
<!-- sources: ITIL 4 SDESK, IM, SRM, PM, MEM, CHM, RDM → AM, SCM, CPM, ITAM, KM, MR, RM, CI -->

Operations processes (Phase C) produce the operational data and records that Assurance processes (Phase D) analyse to evaluate performance, manage risk, and drive improvement.

| Source Process | Output | Target Process | Input | Trigger |
|---------------|--------|---------------|-------|---------|
| PR11 IM | Incident records, resolution data, outage durations | PR06 AM | Availability impact data | Reporting period ends |
| PR11 IM | Incident records (recurring incidents, trends) | PR13 PM | Incident trend data for problem identification | Trend threshold exceeded or proactive review |
| PR11 IM | Incident records, known error matches | PR19 KM | Knowledge articles from incident resolutions | Incident resolved with reusable solution |
| PR11 IM | Major incident records, post-incident reviews | PR24 CI | Improvement opportunities from major incidents | Post-incident review completed |
| PR11 IM | Incident records, resolution times, volumes | PR20 MR | Incident management performance data | Reporting period ends |
| PR12 SRM | Request fulfilment records, volumes, timelines | PR20 MR | Service request performance data | Reporting period ends |
| PR12 SRM | Request patterns, demand trends | PR08 CPM | Demand data for capacity forecasting | Capacity review triggered |
| PR13 PM | Known errors, workarounds | PR11 IM | Known error database for incident matching | Known error created or updated |
| PR13 PM | Known errors, workarounds | PR19 KM | Knowledge articles from problem investigations | Known error documented |
| PR13 PM | Problem records, root cause analyses | PR21 RM | Risk identification from systemic issues | Problem analysis reveals systemic risk |
| PR13 PM | Permanent fix proposals | PR15 CHM | RFCs for permanent problem resolution | Permanent fix identified |
| PR14 MEM | Event data, performance metrics | PR08 CPM | Real-time and trend performance data | Threshold breach or capacity review |
| PR14 MEM | Event data, availability metrics | PR06 AM | Availability monitoring data | Reporting period or outage detected |
| PR14 MEM | Security events, anomaly alerts | PR09 ISM | Security event data for investigation | Security event threshold breached |
| PR15 CHM | Change records, post-implementation reviews | PR20 MR | Change management performance data | Reporting period ends |
| PR15 CHM | Change schedule, planned outages | PR06 AM | Planned downtime for availability calculations | Change approved with outage window |
| PR15 CHM | Implemented changes, affected CIs | PR17 SCFGM | CI updates from implemented changes | Change implementation completed |
| PR15 CHM | Change records (failed changes) | PR24 CI | Improvement opportunities from change failures | Failed change review completed |
| PR16 RDM | Deployed releases, updated CIs | PR17 SCFGM | CI baseline updates from deployments | Release deployed to production |
| PR16 RDM | Deployed releases, release records | PR18 ITAM | Asset register updates from deployments | Release includes new/changed assets |
| PR10 SDESK | Contact volumes, channel utilization, FCR data | PR20 MR | Service desk performance data | Reporting period ends |
| PR10 SDESK | User feedback, common queries | PR19 KM | Self-service content requirements | Knowledge gap pattern identified |

---

## Cross-Phase Interfaces
<!-- intermediate -->
<!-- sources: ITIL 4 practice guides (cross-cutting interfaces) -->

Some interfaces cut across the Phase A→D structure, connecting non-adjacent phases or creating feedback loops from assurance back into strategy.

### Feedback Loops (Phase D → A)

| Source Process | Output | Target Process | Input | Trigger |
|---------------|--------|---------------|-------|---------|
| PR20 MR | Management reports, trend analyses | PR01 SPM | Portfolio performance data for strategic decisions | Management review or portfolio review |
| PR20 MR | Service performance reports | PR02 SLM | SLA achievement data for service reviews | Service review scheduled |
| PR24 CI | Improvement register, approved improvements | PR01 SPM | Service improvement proposals | Improvement approved for implementation |
| PR24 CI | Improvement register, approved improvements | PR15 CHM | RFCs for improvement implementation | Improvement requires change |
| PR21 RM | Risk register, risk appetite statements | PR01 SPM | Risk context for portfolio decisions | Portfolio review or new service proposal |
| PR21 RM | Risk assessments, control recommendations | PR09 ISM | Security risk treatment inputs | Risk assessment identifies security risks |
| PR06 AM | Availability analysis, SPOF reports | PR04 SDES | Availability design requirements | Service design initiated |
| PR06 AM | Availability trends, improvement requirements | PR24 CI | Availability improvement proposals | Availability target breach |
| PR08 CPM | Capacity forecasts, demand projections | PR01 SPM | Capacity constraints for portfolio planning | Portfolio review or new service proposal |
| PR08 CPM | Capacity plans, performance baselines | PR04 SDES | Capacity design requirements | Service design initiated |
| PR18 ITAM | Asset lifecycle data, licence compliance | PR03 SFM | Asset cost data for financial models | Budget cycle (T3) |

### Bidirectional Operational Interfaces

| Process A | Process B | Shared Information | Direction |
|-----------|-----------|-------------------|-----------|
| PR11 IM ↔ PR15 CHM | Emergency change requests from major incidents; incident records from failed changes | Both directions — IM raises emergency RFCs; CHM failure triggers incidents |
| PR15 CHM ↔ PR16 RDM | Approved changes bundled into releases; release deployment updates change records | Both directions — CHM feeds changes to releases; RDM updates change status |
| PR17 SCFGM ↔ PR18 ITAM | CI records enriched with asset data; asset records enriched with configuration data | Both directions — continuous synchronization of CI and asset attributes |
| PR09 ISM ↔ PR21 RM | Security risk assessments inform risk register; risk appetite constrains security policy | Both directions — mutual input on risk identification and treatment |
| PR11 IM ↔ PR10 SDESK | Service desk creates incident records; incident updates communicated back through service desk | Both directions — SDESK is the channel; IM is the process |

---

## Interface Pattern Template
<!-- essential -->

Use this template when documenting a new interface between processes:

| Attribute | Value |
|-----------|-------|
| **Source Process** | {Process ID and name} |
| **Output** | {What the source process produces} |
| **Target Process** | {Process ID and name} |
| **Input** | {What the target process consumes} |
| **Trigger** | {Event or condition that initiates the handoff} |
| **Data Elements** | {Specific fields or records exchanged} |
| **Mechanism** | {How the handoff occurs — tool integration, notification, manual handoff} |
| **Frequency** | {Real-time, event-driven, periodic} |
| **Owner** | {Who is responsible for ensuring the interface works} |

---

## Notes

1. **Interface density:** Not all interfaces exist in every engagement. T1 engagements (single process) typically have 5–10 active interfaces. T2 engagements (process groups) typically have 20–40. T3 engagements (full SMS) may have 60–100+ active interfaces.
2. **Tool integration:** In practice, many interfaces are implemented through ITSM tool integrations (workflow rules, data synchronization, automated notifications). The logical interfaces documented here should be mapped to specific tool configurations during implementation.
3. **FitSM mapping:** FitSM-2 defines explicit inputs and outputs for each of its 14 processes (PR1–PR14). The additional 10 processes in the 3PA unified model (PR03, PR04, PR05, PR06/PR07, PR10, PR14, PR18, PR19, PR20, PR21) draw interface definitions from ITIL 4 practice guides.
4. **Consistency verification:** Gate G5 (Interface Consistency) verifies that every output claimed by a source process is acknowledged as an input by the target process, and vice versa. This document provides the reference set for that verification.
5. **Service Desk as channel:** PR10 (Service Desk) functions as a communication channel for multiple processes rather than a standalone operational process. The service desk creates records for PR11 (IM) and PR12 (SRM), communicates updates on behalf of these processes, and serves as the user-facing interface for the entire SMS.
