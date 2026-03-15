---
title: "3PA Best Practices Library"
description: "Catalog of reusable, anonymized ITSM best practices organized by process area"
version: "0.2"
last_updated: 2026-03-13
---

# 3PA Best Practices Library

## Purpose

This library contains reusable, anonymized best practices for each ITSM process area (PR01–PR24) plus cross-cutting patterns. Best practices are derived from the knowledge library (ITIL v4, FitSM, IT4IT, SIAM) and maintained across engagements.

Best practices are the **fourth architectural layer** of 3PA:

| Layer | Name | Contains | Role |
|:-----:|------|----------|------|
| 1 | Methodology | Phase procedures, taxonomy, gates | HOW to run |
| 2 | Engine | Claude Code skills | Automation |
| 3 | Framework Packs | Framework metadata, mappings | Structure & validation |
| 4 | **Best Practices** | **Reusable content** | **Starting content for authoring** |

## How Best Practices Are Used

1. **P1 (Intake):** Best practices inform process scoping suggestions
2. **P3 (Authoring):** `3pa-author` loads best practices for each process in scope and injects them as starting content into templates — the user then customizes for their organization
3. **P5 (Publish):** New patterns discovered during the engagement are harvested back into the library

## Best Practice Document Format

Each best practice file uses this frontmatter:

```yaml
---
process_id: PR11
process_name: "Incident Management"
category: definition
frameworks:
  - itil-v4
  - fitsm
  - siam
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Incident Management"
  - "FitSM-2: §PR9 ISRM (incident scope)"
last_updated: YYYY-MM-DD
status: stub | draft | reviewed
---
```

Content is organized by template section with maturity annotations:

```markdown
## Purpose
<!-- essential -->
{Best practice purpose statement — included at all maturity levels}

## Activities
<!-- essential -->
| # | Activity | Description |
|---|----------|-------------|
| 1 | Basic Activity | Always included |

<!-- intermediate -->
| 2 | Mature Activity | Included at T2+ |

<!-- advanced -->
| 3 | Advanced Activity | Included at T3 |
```

## Catalog

### Governance & Strategy

| Directory | Process | ID | Tier | Files |
|-----------|---------|:--:|:----:|:-----:|
| `pr01-spm/` | Service Portfolio Management | PR01 | All | 5 |
| `pr02-slm/` | Service Level Management | PR02 | All | 5 |
| `pr03-sfm/` | Service Financial Management | PR03 | T3 | 5 |

### Design & Transition

| Directory | Process | ID | Tier | Files |
|-----------|---------|:--:|:----:|:-----:|
| `pr04-sdes/` | Service Design | PR04 | T3 | 5 |
| `pr05-scatm/` | Service Catalogue Management | PR05 | T2+ | 5 |
| `pr06-am/` | Availability Management | PR06 | All | 5 |
| `pr07-scm/` | Service Continuity Management | PR07 | T2+ | 5 |
| `pr08-cpm/` | Capacity & Performance Management | PR08 | All | 5 |
| `pr09-ism/` | Information Security Management | PR09 | All | 5 |

### Operations

| Directory | Process | ID | Tier | Files |
|-----------|---------|:--:|:----:|:-----:|
| `pr10-sdesk/` | Service Desk | PR10 | All | 5 |
| `pr11-im/` | Incident Management | PR11 | All | 5 |
| `pr12-srm/` | Service Request Management | PR12 | All | 5 |
| `pr13-pm/` | Problem Management | PR13 | All | 5 |
| `pr14-mem/` | Monitoring & Event Management | PR14 | T2+ | 5 |

### Change & Release

| Directory | Process | ID | Tier | Files |
|-----------|---------|:--:|:----:|:-----:|
| `pr15-chm/` | Change Management | PR15 | All | 5 |
| `pr16-rdm/` | Release & Deployment Management | PR16 | T2+ | 5 |

### Asset & Configuration

| Directory | Process | ID | Tier | Files |
|-----------|---------|:--:|:----:|:-----:|
| `pr17-scfgm/` | Service Configuration Management | PR17 | All | 5 |
| `pr18-itam/` | IT Asset Management | PR18 | T2+ | 5 |

### Knowledge & Reporting

| Directory | Process | ID | Tier | Files |
|-----------|---------|:--:|:----:|:-----:|
| `pr19-km/` | Knowledge Management | PR19 | T2+ | 5 |
| `pr20-mr/` | Measurement & Reporting | PR20 | All | 5 |

### Assurance

| Directory | Process | ID | Tier | Files |
|-----------|---------|:--:|:----:|:-----:|
| `pr21-rm/` | Risk Management | PR21 | T2+ | 5 |
| `pr22-relm/` | Relationship Management | PR22 | All | 5 |
| `pr23-suppm/` | Supplier Management | PR23 | T2+ | 5 |
| `pr24-ci/` | Continual Improvement | PR24 | All | 5 |

### Cross-Cutting Best Practices

| File | Content |
|------|---------|
| `cross-cutting/role-catalog.md` | Standard ITSM role definitions |
| `cross-cutting/interface-patterns.md` | Process interface patterns |
| `cross-cutting/policy-patterns.md` | Reusable policy statements |
| `cross-cutting/escalation-models.md` | Escalation hierarchies |
| `cross-cutting/priority-models.md` | Priority matrix templates |
| `cross-cutting/maturity-model.md` | Maturity assessment criteria |

**Total: 126 content files** (24 processes × 5 + 6 cross-cutting)

## Cross-Framework Mapping

| ID | Process | FitSM | ITIL v4 | IT4IT | SIAM |
|:--:|---------|:-----:|:-------:|:-----:|:----:|
| PR01 | Service Portfolio Management | PR1 SPM | Portfolio Mgmt | S2P | — |
| PR02 | Service Level Management | PR2 SLM | Service Level Mgmt | R2F | Yes |
| PR03 | Service Financial Management | — | Service Financial Mgmt | S2P | — |
| PR04 | Service Design | — | Service Design | R2D | — |
| PR05 | Service Catalogue Management | PR1 SPM (part) | Service Catalogue Mgmt | R2F | — |
| PR06 | Availability Management | PR4 SACM (part) | Availability Mgmt | R2D | — |
| PR07 | Service Continuity Management | PR4 SACM (part) | Service Continuity Mgmt | D2C | — |
| PR08 | Capacity & Performance Mgmt | PR5 CAPM | Capacity & Performance | R2D | — |
| PR09 | Information Security Mgmt | PR6 ISM | Information Security Mgmt | X-cut | — |
| PR10 | Service Desk | — | Service Desk | R2F | Yes |
| PR11 | Incident Management | PR9 ISRM (part) | Incident Mgmt | D2C | Yes |
| PR12 | Service Request Management | PR9 ISRM (part) | Service Request Mgmt | R2F | — |
| PR13 | Problem Management | PR10 PM | Problem Mgmt | D2C | Yes |
| PR14 | Monitoring & Event Mgmt | — | Monitoring & Event Mgmt | D2C | — |
| PR15 | Change Management | PR12 CHM | Change Enablement | R2D | Yes |
| PR16 | Release & Deployment Mgmt | PR13 RDM | Release + Deployment | R2D | — |
| PR17 | Service Configuration Mgmt | PR11 CONFM | Service Config Mgmt | X-cut | Yes |
| PR18 | IT Asset Management | — | IT Asset Mgmt | X-cut | — |
| PR19 | Knowledge Management | — | Knowledge Mgmt | X-cut | — |
| PR20 | Measurement & Reporting | PR3 SRM | Measurement & Reporting | X-cut | — |
| PR21 | Risk Management | — | Risk Mgmt | S2P | — |
| PR22 | Relationship Management | PR7 CRM | Relationship Mgmt | S2P | Yes |
| PR23 | Supplier Management | PR8 SUPPM | Supplier Mgmt | S2P | Yes |
| PR24 | Continual Improvement | PR14 CSI | Continual Improvement | X-cut | — |

## Knowledge Crawl Status

| ID | Process | Status | Last Crawled |
|:--:|---------|:------:|-------------|
| PR01 | Service Portfolio Management | **draft** | 2026-03-13 |
| PR02 | Service Level Management | **draft** | 2026-03-13 |
| PR03 | Service Financial Management | **draft** | 2026-03-14 |
| PR04 | Service Design | **draft** | 2026-03-14 |
| PR05 | Service Catalogue Management | **draft** | 2026-03-14 |
| PR06 | Availability Management | **draft** | 2026-03-13 |
| PR07 | Service Continuity Management | **draft** | 2026-03-14 |
| PR08 | Capacity & Performance Mgmt | **draft** | 2026-03-14 |
| PR09 | Information Security Mgmt | **draft** | 2026-03-13 |
| PR10 | Service Desk | **draft** | 2026-03-14 |
| PR11 | Incident Management | **draft** | 2026-03-13 |
| PR12 | Service Request Management | **draft** | 2026-03-14 |
| PR13 | Problem Management | **draft** | 2026-03-13 |
| PR14 | Monitoring & Event Mgmt | **draft** | 2026-03-14 |
| PR15 | Change Management | **draft** | 2026-03-13 |
| PR16 | Release & Deployment Mgmt | **draft** | 2026-03-13 |
| PR17 | Service Configuration Mgmt | **draft** | 2026-03-13 |
| PR18 | IT Asset Management | **draft** | 2026-03-14 |
| PR19 | Knowledge Management | **draft** | 2026-03-14 |
| PR20 | Measurement & Reporting | **draft** | 2026-03-14 |
| PR21 | Risk Management | **draft** | 2026-03-14 |
| PR22 | Relationship Management | **draft** | 2026-03-13 |
| PR23 | Supplier Management | **draft** | 2026-03-13 |
| PR24 | Continual Improvement | **draft** | 2026-03-14 |
| — | Cross-cutting | **draft** | 2026-03-14 |
