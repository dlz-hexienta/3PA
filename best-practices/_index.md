---
title: "3PA Best Practices Library"
description: "Catalog of reusable, anonymized ITSM best practices organized by process area"
version: "0.1"
last_updated: 2026-03-13
---

# 3PA Best Practices Library

## Purpose

This library contains reusable, anonymized best practices for each ITSM process area (PR1–PR14) plus cross-cutting patterns. Best practices are derived from the knowledge library (ITIL v4, FitSM, IT4IT, SIAM) and maintained across engagements.

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
process_id: PR9
process_name: "Incident & Service Request Management"
category: definition
frameworks:
  - itil-v4
  - fitsm
maturity:
  essential: true
  intermediate: true
  advanced: true
sources: []
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

### Per-Process Best Practices

| Directory | Process | Phase | Files |
|-----------|---------|:-----:|:-----:|
| `pr01-spm/` | Service Portfolio Management | A | 5 |
| `pr02-slm/` | Service Level Management | B | 5 |
| `pr03-srm/` | Service Reporting Management | D | 5 |
| `pr04-sacm/` | Service Availability & Continuity Mgmt | D | 5 |
| `pr05-capm/` | Capacity Management | D | 5 |
| `pr06-ism/` | Information Security Management | A | 5 |
| `pr07-crm/` | Customer Relationship Management | B | 5 |
| `pr08-suppm/` | Supplier Management | B | 5 |
| `pr09-isrm/` | Incident & Service Request Mgmt | C | 5 |
| `pr10-pm/` | Problem Management | C | 5 |
| `pr11-confm/` | Configuration Management | A | 5 |
| `pr12-chm/` | Change Management | C | 5 |
| `pr13-rdm/` | Release & Deployment Management | C | 5 |
| `pr14-csi/` | Continual Service Improvement | D | 5 |

### Cross-Cutting Best Practices

| File | Content |
|------|---------|
| `cross-cutting/role-catalog.md` | Standard ITSM role definitions |
| `cross-cutting/interface-patterns.md` | Process interface patterns |
| `cross-cutting/policy-patterns.md` | Reusable policy statements |
| `cross-cutting/escalation-models.md` | Escalation hierarchies |
| `cross-cutting/priority-models.md` | Priority matrix templates |
| `cross-cutting/maturity-model.md` | Maturity assessment criteria |

**Total: 76 content files**

## Knowledge Crawl Status

| Process | Status | Last Crawled |
|---------|:------:|-------------|
| PR1 SPM | stub | — |
| PR2 SLM | stub | — |
| PR3 SRM | stub | — |
| PR4 SACM | stub | — |
| PR5 CAPM | stub | — |
| PR6 ISM | stub | — |
| PR7 CRM | stub | — |
| PR8 SUPPM | stub | — |
| PR9 ISRM | stub | — |
| PR10 PM | stub | — |
| PR11 CONFM | stub | — |
| PR12 CHM | stub | — |
| PR13 RDM | stub | — |
| PR14 CSI | stub | — |
| Cross-cutting | stub | — |
