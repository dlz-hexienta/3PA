# 3PA Document Taxonomy

> Defines all document types, their authoring layers, tier requirements, and the process interdependency map.

## 1. Document Types (17 Types)

| # | Document Type | Category ID | Layer | T1 | T2 | T3 | Description |
|---|--------------|-------------|:-----:|:---:|:---:|:---:|-------------|
| 1 | Scoping Brief | `scoping-brief` | — | Required | Required | Required | P1 output: scope, tier, stakeholders |
| 2 | Decision Log | `decision-log` | — | Required | Required | Required | P2 output: decisions, glossary |
| 3 | Gap Analysis Report | `gap-analysis-report` | — | — | Revision | Revision | P1.5 output: gap assessment (revision mode only) |
| 4 | SMS Policy | `sms-policy` | 0 | — | Required | Required | Umbrella governance document |
| 5 | Process Policy | `process-policy` | 1 | Required | Required | Required | Per-process strategic intent |
| 6 | Process Definition | `process-definition` | 2 | Required | Required | Required | Operational model for each process |
| 7 | Procedure | `procedure` | 4 | Required | Required | Required | Step-by-step instructions |
| 8 | RACI Matrix | `raci-matrix` | 3 | Required | Required | Required | Role-activity assignment |
| 9 | SLA Template | `sla-template` | 5 | Optional | Required | Required | Service Level Agreement |
| 10 | OLA Template | `ola-template` | 5 | — | Optional | Required | Operational Level Agreement |
| 11 | KPI Definition | `kpi-definition` | 3 | Optional | Required | Required | Metrics and targets |
| 12 | Service Catalogue Entry | `service-catalogue-entry` | 5 | Optional | Required | Required | Service description and terms |
| 13 | Risk Register | `risk-register` | 5 | — | Optional | Required | Risk identification and mitigation |
| 14 | CSI Register | `csi-register` | 5 | — | Optional | Required | Continual Service Improvement log |
| 15 | Completeness Report | `completeness-report` | — | Required | Required | Required | P4 output: gate results |
| 16 | Documentation Pack Manifest | `documentation-pack-manifest` | — | Required | Required | Required | P5 output: pack contents |
| 17 | Document Library | `document-library` | — | Optional | Required | Required | P5 output: organized index |

> **Note:** In revision mode, the Gap Analysis Report (row 3) replaces the need for a standalone current-state assessment. Document counts below reflect greenfield mode; revision mode may include fewer new documents if existing ones are retained.

## 2. Authoring Layers (6 Layers)

Documents must be authored in layer order. A document at Layer N must reach draft status before any Layer N+1 document begins.

```
Layer 0: SMS Policy
         └── Umbrella governance — defines commitment, scope, and policy framework
         └── T2+ only (T1 skips to Layer 1)

Layer 1: Process Policies
         └── Per-process strategic intent — WHY this process exists
         └── One per process in scope

Layer 2: Process Definitions
         └── Operational model — WHAT/WHO/WHEN
         └── Authored in Phase A→B→C→D order (see §3)
         └── One per process in scope

Layer 3: RACI Matrices, KPI Definitions
         └── Cross-cutting assignments that reference Layer 2
         └── One RACI per process (or consolidated)
         └── KPI definitions reference process objectives

Layer 4: Procedures
         └── Step-by-step HOW-TO instructions
         └── One or more per process
         └── Must reference roles from RACI (Layer 3)

Layer 5: Templates & Records
         └── SLA, OLA, Service Catalogue, Risk Register, CSI Register
         └── Evidence artifacts that reference all upper layers
```

## 3. Process Interdependency Map (Layer 2 Ordering)

When multiple process definitions are authored (T2/T3), they must follow the interdependency phases:

### Phase A — Foundation

| Process ID | Process Name | Rationale |
|-----------|-------------|-----------|
| PR1 | Service Portfolio Management (SPM) | Defines the service landscape; all other processes reference it |
| PR11 | Configuration Management (CONFM) | Establishes the CI model; change, incident, problem depend on it |
| PR6 | Information Security Management (ISM) | Security policies constrain all other processes |

### Phase B — Agreements

| Process ID | Process Name | Rationale |
|-----------|-------------|-----------|
| PR2 | Service Level Management (SLM) | Defines SLA/OLA framework; operations processes measure against it |
| PR7 | Customer Relationship Management (CRM) | Customer interface; feeds SLM and complaint handling |
| PR8 | Supplier Management (SUPPM) | Supplier agreements; feeds OLA and underpinning contracts |

### Phase C — Operations

| Process ID | Process Name | Rationale |
|-----------|-------------|-----------|
| PR9 | Incident & Service Request Management (ISRM) | Core operations; depends on CONFM, SLM, ISM |
| PR10 | Problem Management (PM) | Root cause analysis; depends on ISRM, CONFM |
| PR12 | Change Management (CHM) | Controlled changes; depends on CONFM, SLM |
| PR13 | Release & Deployment Management (RDM) | Release lifecycle; depends on CHM, CONFM |

### Phase D — Assurance

| Process ID | Process Name | Rationale |
|-----------|-------------|-----------|
| PR4 | Service Availability & Continuity Management (SACM) | Availability targets; depends on SLM, CONFM |
| PR5 | Capacity Management (CAPM) | Capacity planning; depends on SLM, monitoring |
| PR3 | Service Reporting Management (SRM) | Reporting; depends on KPIs from all processes |
| PR14 | Continual Service Improvement (CSI) | Improvement; depends on reporting, all process outputs |

### Tier Application

- **T1:** Authors one process only — no interdependency ordering needed
- **T2:** Authors the process group in dependency order within Phase A→D
- **T3:** Authors all 14 processes in strict A→B→C→D order

## 4. YAML Frontmatter Standard

All documents use this frontmatter schema:

```yaml
---
title: string                # Document title
organization: string         # Organization name
scope: string                # Process IDs (e.g., "PR1, PR9") or "SMS"
category: enum               # One of the 17 category IDs listed in §1
process_id: string | ~       # PR1–PR14 or ~ for cross-cutting documents
status: draft | review | approved
version: "x.y"
date: YYYY-MM-DD
parent: filename | ~         # Parent document filename or ~
depends_on: []               # List of document filenames this depends on
framework: string | ~        # fitsm | itil-v4 | it4it | siam | ~
tags: []                     # Free-form tags
---
```

### Required Fields by Document Type

| Field | Scoping/Decision | Policy | Process | Procedure | Cross-cutting | Records |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| title | Required | Required | Required | Required | Required | Required |
| organization | Required | Required | Required | Required | Required | Required |
| scope | Required | Required | Required | Required | Required | Required |
| category | Required | Required | Required | Required | Required | Required |
| process_id | ~ | Optional | Required | Required | Optional | Optional |
| status | Required | Required | Required | Required | Required | Required |
| version | Required | Required | Required | Required | Required | Required |
| date | Required | Required | Required | Required | Required | Required |
| parent | ~ | ~ | Policy | Process Def | ~ | ~ |
| depends_on | ~ | ~ | Phase deps | Process Def | Layer 2 docs | Layer 3+ |
| framework | Optional | Optional | Optional | Optional | Optional | Optional |
| tags | Optional | Optional | Optional | Optional | Optional | Optional |

## 5. Document Naming Convention

```
{organization}-{document-type}.md                    # Single instance
{organization}-{process-id}-{document-type}.md       # Per-process instance
```

Examples:
- `acme-sms-policy.md`
- `acme-pr9-process-definition.md`
- `acme-pr9-incident-procedure.md`
- `acme-raci-matrix.md`
- `scoping-brief.md` (shared artifacts use plain names)
- `decision-log.md`

## 6. Document Count by Tier

| Tier | Processes | Policies | Process Defs | RACIs | Procedures | KPIs | Records | Total Range |
|------|:---------:|:--------:|:------------:|:-----:|:----------:|:----:|:-------:|:-----------:|
| T1 | 1 | 1 | 1 | 1 | 1–2 | 0–1 | 0–1 | 4–7 |
| T2 | 2–5 | 2–6 | 2–5 | 2–5 | 2–10 | 1–5 | 1–4 | 15–30 |
| T3 | 6–14 | 7–15 | 6–14 | 6–14 | 6–28 | 6–14 | 5–10 | 50–80+ |

## 7. Cross-References

- Authoring procedures: `3PA-Phase-Guide.md` §P3
- Quality gates: `3PA-Quality-Gates.md`
- Template files: `templates/`
- Framework pack schema: `3PA-Framework-Pack-Specification.md`
