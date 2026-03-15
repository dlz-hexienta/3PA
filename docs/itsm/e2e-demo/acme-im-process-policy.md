---
title: "Incident Management Policy"
organization: "Acme IT Services"
scope: "PR11"
category: process-policy
process_id: PR11
status: draft
version: "0.1"
date: 2026-03-15
parent: ~
depends_on: []
framework: fitsm
tags: [e2e-demo, t1, greenfield]
---

# Incident Management Policy

<!-- Layer 1 document — strategic intent for Incident Management. WHY this process exists. -->

## 1. Purpose

This policy establishes the strategic intent and governing principles for Incident Management (PR11) at Acme IT Services. It ensures that all incidents — unplanned interruptions to a service or reductions in the quality of a service — are detected, registered, classified, prioritized, diagnosed, resolved, and closed using a consistent, repeatable approach.

The policy exists to protect the quality of managed services delivered by Acme IT Services to its clients by minimizing the negative business impact of incidents and restoring normal service operation as quickly as possible.

## 2. Scope

This policy applies to:

- All incidents affecting services managed by Acme IT Services from the Munich site, whether reported by users, detected by technical staff, or identified through Datadog monitoring and alerting
- The full incident lifecycle — from detection and registration through classification, prioritization, diagnosis, resolution, and closure
- Major incidents and the dedicated procedure for their coordinated handling and post-incident review
- All roles with responsibility for incident management: Incident Manager (IM), Service Desk Agents (SDA), and Technical Specialists (TS)
- The priority matrix, classification scheme, escalation paths, and other supporting artefacts that govern how incidents are handled
- All approximately 12 services in the Acme IT Services portfolio

This policy does not cover:

- Service requests, which are tagged separately in Jira Service Management and managed under Service Request Management (PR12) — per decision D-7
- Root cause investigation and known error database maintenance, which are managed under Problem Management (PR13) — noted as a future process

## 3. Policy Statements

### 3.1 Incident Detection and Registration

- PS-01: All incidents shall be registered in Jira Service Management with a complete set of required fields, including affected user(s), affected service or CI, impact, urgency, priority, and time of first symptom (ref: IM-R01).
- PS-02: Incidents shall be detected as early as possible through Datadog monitoring and alerting, user reports via Service Desk channels (phone, email, Jira SM portal, Slack), and technical observation.

### 3.2 Classification and Prioritization

- PS-03: Incidents shall be classified using a two-dimensional scheme (Service x Technology Layer: Infrastructure / Application / End User) to support routing, reporting, and trend analysis (ref: IM-R02, D-5).
- PS-04: Incidents shall be prioritized based on impact and urgency using a 4-level priority matrix (P1-P4) derived from a 3x3 Impact x Urgency grid, with associated response and resolution targets (ref: IM-R03, D-1).

### 3.3 Major Incident Handling

- PS-05: Criteria for identifying major incidents shall be defined and consistently applied: P1 Critical priority OR 2+ services affected OR external client service unavailable OR declared by IT Director/Service Desk Lead (ref: IM-R04, D-2).
- PS-06: A major incident handling procedure shall be established, including coordinator assignment (Incident Manager at T1), elevated priority handling, stakeholder communication via Slack, and a mandatory post-major-incident review documented in Confluence (ref: IM-R05, D-2).

### 3.4 Resolution and Closure

- PS-07: Incidents shall be resolved and closed with user confirmation that service has been restored satisfactorily. Resolution details and timestamps shall be recorded in Jira Service Management (ref: IM-R06).

### 3.5 Escalation

- PS-08: A 3-tier functional escalation model (Service Desk Agent -> Technical Specialist -> Team Lead) and hierarchical escalation (Service Desk Lead -> IT Director) shall be maintained with defined timescales per priority level (ref: D-3).

### 3.6 Accountability

- PS-09: The Incident Manager role shall be assigned with accountability for coordinating incident handling, monitoring resolution team performance, and ensuring awareness of incidents and their status (ref: IM-R07).

## 4. Objectives

| Objective | Metric | Target | Measurement Period |
|-----------|--------|--------|-------------------|
| Restore services within agreed SLA targets | Incident Resolution Within SLA Target Rate | >= 90% | Monthly |
| Minimize mean time to resolve incidents | Mean Incident Resolution Time (MTTR) | Within SLA targets per priority level | Monthly |
| Maximize first-contact resolution | First-Contact Resolution Rate | >= 60% | Monthly |
| Maintain manageable incident backlog | Incident Backlog Size and Trend | Stable or trending downward | Monthly |

## 5. Roles & Authorities

| Role | Authority | Reports To |
|------|-----------|-----------|
| Incident Manager (IM) — Tom Weber, Service Desk Lead | Accountable for all incident management activities. May declare major incidents. Coordinates escalation. Also serves as Process Owner at T1 | IT Director |
| Service Desk Agent (SDA) — Service Desk team (8 staff) | Registers, classifies, prioritizes incidents. Performs first-contact resolution. Manages incident closure with user confirmation | Incident Manager |
| Technical Specialist (TS) — Infrastructure & Applications teams | Provides technical expertise for diagnosis and resolution. Participates in major incident resolution when mobilized by IM | Team Leads (functional), Incident Manager (for incident coordination) |

## 6. Compliance

- Compliance with this policy is verified through monthly incident reports covering SLA achievement, resolution times, and backlog trends generated from Jira Service Management
- Major incident review reports shall be completed for all major incidents within 5 business days of resolution
- Non-compliance shall be escalated to the Incident Manager (Tom Weber) and IT Director for remediation
- This policy shall be reviewed at least annually or following a significant change to Acme IT Services' service portfolio, support model, or incident management tooling

## 7. Exceptions

- Exceptions to this policy require documented justification and approval from the Incident Manager or IT Director
- Exception requests shall be recorded in Confluence with the rationale, duration, risk assessment, and compensating controls
- Standing exceptions (e.g., for specific low-impact internal services) shall be reviewed during the annual policy review

## 8. Related Documents

| Document | Relationship |
|----------|-------------|
| acme-im-process-definition.md | Child — defines WHAT the process does, WHO is involved, and process flow |
| acme-im-raci-matrix.md | Child — role-activity assignments for all incident management activities |
| acme-im-kpi-definitions.md | Child — KPI definitions with SLA-aligned targets and RAG thresholds |
| acme-im-procedures.md | Child — step-by-step procedures for incident handling and major incident handling |
| Service Request Management (PR12) | Related — service requests tagged separately in Jira SM per D-7 |
| Problem Management (PR13) | Related — future process; incident trends feed problem identification |
| Change Management (PR15) | Related — future process; changes may be required to resolve incidents |

## 9. FitSM Alignment Statement

This process policy aligns with the FitSM v3 standard as follows:

- **FitSM PR9 (ISRM):** This policy addresses the incident management scope of FitSM's combined Incident and Service Request Management process. Per decision D-7, Acme IT Services documents incident management (PR11) and service request management (PR12) as separate processes, with service requests tagged separately in Jira Service Management. This policy covers all FitSM PR9 requirements related to incident registration, classification, prioritization, escalation, resolution, closure, and major incident handling.
- **GR1 (Top Management Commitment):** The IT Director serves as the accountable executive for the SMS. The Incident Manager role is formally assigned to Tom Weber (Service Desk Lead), demonstrating management commitment to incident management.
- **GR2 (Documentation Management):** This policy and its child documents (process definition, RACI matrix, KPI definitions, procedures) constitute the documented process definition required by GR2.2, covering goals, inputs, activities, outputs, roles, interfaces, policies, and procedures.
- **GR3 (Resource Management):** Roles and staffing levels (8 Service Desk Agents, Infrastructure & Applications teams) are defined and aligned to incident volumes and SLA targets.
- **GR7 (Continual Improvement):** The policy mandates periodic review of incident data to identify trends, improvement opportunities, and process refinements. Improvement initiatives will be tracked through Continual Improvement (PR24) when that process is established.

## 10. Approval & Review

| Version | Date | Approved By | Next Review |
|---------|------|------------|-------------|
| 0.1 | 2026-03-15 | TBD | 2027-03-15 |
