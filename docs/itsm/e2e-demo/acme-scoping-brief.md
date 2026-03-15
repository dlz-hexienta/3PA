---
title: "Scoping Brief"
organization: "Acme IT Services"
scope: "PR11"
category: scoping-brief
process_id: ~
status: draft
version: "0.1"
date: 2026-03-15
parent: ~
depends_on: []
framework: fitsm
tags: [e2e-demo, t1, greenfield]
---

# Scoping Brief

## 1. Organization Overview

Acme IT Services is a mid-sized managed services provider with approximately 50 IT staff, delivering IT infrastructure and application support services to 5 internal business units and 3 external clients. The organization is headquartered at a single site in Munich, Germany, operating in English. Acme has been delivering IT services informally for 4 years but has no formally documented ITSM processes. The IT director has initiated a process formalization effort, starting with incident management as the highest-priority process.

## 1.5 Engagement Mode

| Attribute | Value |
|-----------|-------|
| **Mode** | Greenfield |
| **Rationale** | No existing ITSM documentation exists. Processes are followed informally based on tribal knowledge. This is a from-scratch documentation effort. |

## 2. Scope Definition

### 2.1 Processes in Scope

| Process ID | Process Name | Phase |
|-----------|-------------|:-----:|
| PR11 | Incident Management | C |

### 2.2 Processes Out of Scope

All other processes (PR01-PR10, PR12-PR24) are out of scope for this engagement. The organization plans to add Service Request Management (PR12) and Problem Management (PR13) in a future engagement after PR11 is established.

### 2.3 Organizational Boundaries

- **In scope:** All IT service teams (Infrastructure, Applications, Service Desk)
- **Out of scope:** Business unit-specific processes, HR, Finance

## 2.5 Organization Profile

### 2.5.1 People

| Dimension | Details |
|-----------|---------|
| **Org Structure** | Flat: IT Director → 3 Team Leads (Infrastructure, Applications, Service Desk) → ~50 staff |
| **IT Teams** | Infrastructure (15), Applications (12), Service Desk (8), IT Management (3), Other (12) |
| **Existing ITSM Roles** | Informal: Service Desk Lead acts as de facto Incident Manager; no formally defined roles |
| **Change Appetite** | Medium — willing to adopt process but want lightweight, practical documentation |
| **Formality Level** | Semi-formal — want documented processes but not bureaucratic overhead |

### 2.5.2 Tools

| Tool | Category | Purpose | Integrations | Constraints |
|------|----------|---------|-------------|-------------|
| Jira Service Management | Ticketing | Incident logging, assignment, tracking | Slack (notifications), Confluence (knowledge base) | Standard cloud plan; no CMDB module |
| Datadog | Monitoring | Infrastructure and application monitoring | Jira SM (alert → ticket creation) | Alerts generate Jira tickets automatically |
| Slack | Collaboration | Team communication, incident coordination | Jira SM, Datadog | Primary communication channel during incidents |
| Confluence | Knowledge Base | Runbooks, known issues, documentation | Jira SM | Limited content; mostly outdated runbooks |

### 2.5.3 Existing Processes

| Process | Documented? | Followed? | Maturity (0-5) | Pain Points | Working Well |
|---------|:-----------:|:---------:|:--------------:|-------------|-------------|
| Incident Management | No | Partially | 1 | No priority matrix; inconsistent escalation; no major incident procedure; tickets often closed without user confirmation | Jira SM ticket creation; Datadog auto-detection; team responsiveness |

## 3. Complexity Assessment

### 3.1 Complexity Signals

| Signal | Value | Tier Indication |
|--------|-------|-----------------|
| Processes in scope | 1 | T1 |
| Organizational roles | 3 (IM, SDA, TS) | T1 |
| Supplier/vendor count | 0 (all internal) | T1 |
| Services in catalogue | ~12 (informal) | T1 |
| Compliance driver | None | T1 |
| Sites / business units | 1 site | T1 |
| Multi-language | No (English only) | T1 |

### 3.2 Assigned Tier

**T1 (Single Process)** — All 7 signals indicate T1. Single process, small role count, no compliance driver, single site, no multi-language requirement. The engagement will produce 4-7 documents with gates G1-G3 + G6.

## 4. Framework Alignment

**FitSM v3** — Selected because:
- Lightweight and practical, matching Acme's "no bureaucracy" requirement
- Designed for organizations of Acme's size and maturity
- PR11 Incident Management maps to FitSM PR9 ISRM (incident scope)
- CC-BY licensed, no cost barrier
- Clear path to ISO 20000 compliance if needed in future

Framework pack loaded: `framework-packs/fitsm.yaml`

**FitSM-specific intake responses:**
- Not part of a federated IT infrastructure
- Not targeting FitSM certification; using as a practical process improvement framework
- No existing processes mapped to FitSM process IDs
- Team has no FitSM training (Foundation training planned after initial documentation)
- No ISO/IEC 20000-1 compliance requirement at this time

## 5. Existing Documentation

No formal ITSM documentation exists. Confluence contains:
- 6 outdated runbooks for common infrastructure issues (last updated 12+ months ago)
- An informal "who to call" list for escalations
- No documented priority matrix, classification scheme, or incident handling procedure

## 6. Stakeholders

| Stakeholder | Role | Concern | Reviews |
|-------------|------|---------|---------|
| Maria Chen | IT Director | Process adoption, measurable improvement | All documents (approval authority) |
| Tom Weber | Service Desk Lead | Practical, usable procedures | Process definition, procedures, RACI |
| Sarah Kok | Infrastructure Lead | Escalation clarity, workload management | Process definition, RACI |

## 7. Intended Use

- Internal operations: standardize how incidents are handled across all teams
- Onboarding: new service desk agents and technical specialists use the procedures as training material
- Measurement: establish KPIs to track incident management performance
- Foundation: serve as the template for future process documentation (PR12, PR13)

## 8. Constraints & Assumptions

- **Timeline:** Documentation to be complete within 2 weeks
- **Resources:** IT Director and Service Desk Lead available for review; limited availability of Infrastructure and Applications leads
- **Assumptions:** Jira Service Management will be the ITSM tool; Datadog integration is already in place; no organizational restructuring planned
- **Language:** All documentation in English
