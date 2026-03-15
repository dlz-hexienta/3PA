---
process_id: PR17
process_name: "Service Configuration Management"
category: raci
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
  - "ITIL 4: Service Configuration Management §4.1, §4.2, Table 4.2"
  - "FitSM-2: §PR11 CONFM"
  - "IT4IT: Cross-cutting (CMDB/CMS)"
last_updated: 2026-03-13
status: draft
---

# Service Configuration Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Roles are graduated by maturity tier. Activities marked T2+ or T3 only apply at those tiers. Organizations at lower tiers may combine roles (e.g., the configuration manager may also perform librarian and coordinator functions at T1).

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| CM | Configuration Manager | All |
| CC | Configuration Coordinator | T2+ |
| CL | Configuration Librarian | T2+ |
| RO | Resource Owner | All |
| SO | Service Owner | All |
| SLM | Service Level Manager | All |

## Essential Activities (All Tiers)

### Establishing the SCM Approach
<!-- sources: ITIL 4 Service Configuration Management §3.2.1 Table 4.2 -->

| Activity | CM | CC | CL | RO | SO | SLM |
|----------|:--:|:--:|:--:|:--:|:--:|:---:|
| Analyse stakeholder requirements for configuration information | A/R | C | — | C | C | C |
| Define the scope of configuration management | A/R | — | — | C | C | — |
| Define CI types, attributes, and relationships | A/R | C | — | C | — | — |
| Define naming conventions and identification rules | A/R | C | — | — | — | — |
| Document the SCM approach | A/R | C | — | — | I | I |
| Communicate approach and integrate into value streams | A/R | R | — | I | I | I |

### Registering and Maintaining CIs
<!-- sources: ITIL 4 Service Configuration Management §3.2.2 Table 4.2, FitSM-2 §PR11 CONFM -->

| Activity | CM | CC | CL | RO | SO | SLM |
|----------|:--:|:--:|:--:|:--:|:--:|:---:|
| Identify the applicable CI model for a resource | A | R | R | C | — | — |
| Create or update CI records in the CMDB | A | R | R | C | — | — |
| Record CI lifecycle stage transitions | A | R | R | — | — | — |
| Validate CI records for completeness and accuracy | A | R | R | — | — | — |
| Manage CI model exceptions | A/R | C | C | C | — | — |

### Basic Configuration Verification
<!-- sources: ITIL 4 Service Configuration Management §3.2.3, FitSM-2 §PR11 CONFM -->

| Activity | CM | CC | CL | RO | SO | SLM |
|----------|:--:|:--:|:--:|:--:|:--:|:---:|
| Collect inventory data for verification | I | R | R | C | — | — |
| Compare inventory data with CMDB records | A | R | R | — | — | — |
| Identify and log discrepancies | A | R | R | — | — | — |
| Implement basic corrective actions (update CMDB) | A | R | R | I | — | — |

## Intermediate Activities (T2+)

### CI Model Lifecycle
<!-- sources: ITIL 4 Service Configuration Management §2.2.2, §3.2.2 -->

| Activity | CM | CC | CL | RO | SO | SLM |
|----------|:--:|:--:|:--:|:--:|:--:|:---:|
| Define or revise a CI model | A/R | C | — | C | — | — |
| Define verification and audit procedures for a CI type | A/R | C | — | C | — | — |
| Validate the CI model with stakeholders | A/R | C | — | R | — | — |
| Publish CI model to the models library | A | R | I | I | — | — |
| Conduct periodic CI model reviews | A/R | C | — | C | — | — |

### Scheduled CMDB Verification and Audit
<!-- sources: ITIL 4 Service Configuration Management §3.2.3 Tables 3.5/3.6 -->

| Activity | CM | CC | CL | RO | SO | SLM |
|----------|:--:|:--:|:--:|:--:|:--:|:---:|
| Define verification scope and schedule | A/R | C | — | — | — | — |
| Execute the verification procedure | A | R | R | C | — | — |
| Review the verification output | A/R | C | C | C | — | — |
| Define corrective actions for each discrepancy | A/R | C | — | C | — | — |
| Implement corrective actions | A | R | R | C | — | — |
| Compose and communicate a CMDB verification report | A/R | C | — | — | I | I |

### Configuration Baselines
<!-- sources: ITIL 4 Service Configuration Management §2.2.5 -->

| Activity | CM | CC | CL | RO | SO | SLM |
|----------|:--:|:--:|:--:|:--:|:--:|:---:|
| Identify services or components requiring baselines | A | C | — | C | C | — |
| Capture and record the configuration baseline | A | R | R | C | — | — |
| Review and formally approve the baseline | A/R | — | — | C | C | — |
| Update the baseline after approved major changes | A | R | R | I | I | — |
| Use baselines for comparison during verification | A | R | R | — | — | — |

### Review and Adjust the SCM Approach
<!-- sources: ITIL 4 Service Configuration Management §3.2.1 Table 3.2 -->

| Activity | CM | CC | CL | RO | SO | SLM |
|----------|:--:|:--:|:--:|:--:|:--:|:---:|
| Assess approach effectiveness using metrics and feedback | A/R | C | C | C | C | — |
| Update the SCM approach and procedures | A/R | C | — | I | I | I |
| Communicate the updated approach | A | R | I | I | I | I |

## Advanced Activities (T3)

### Automated Discovery and CMS Integration
<!-- sources: ITIL 4 Service Configuration Management §5.2 Table 5.1 -->

| Activity | CM | CC | CL | RO | SO | SLM |
|----------|:--:|:--:|:--:|:--:|:--:|:---:|
| Design automated discovery and CMDB reconciliation | A/R | R | — | C | — | — |
| Deploy and configure CMS integrations with discovery, monitoring, and service management tools | A | R | — | C | — | — |
| Build and maintain service configuration models for analytical use | A/R | R | — | C | C | — |
| Monitor automated data quality controls | A | R | R | — | — | — |

### Cross-Supplier Configuration Management
<!-- sources: ITIL 4 Service Configuration Management §6 -->

| Activity | CM | CC | CL | RO | SO | SLM |
|----------|:--:|:--:|:--:|:--:|:--:|:---:|
| Define supplier configuration data exchange requirements | A/R | C | — | — | C | — |
| Establish supplier CI model alignment and data format interoperability | A/R | R | — | — | — | — |
| Implement data exchange and integration arrangements | A | R | — | — | — | — |
| Verify supplier-provided configuration data | A | R | R | — | — | — |
| Review and adjust cross-supplier arrangements | A/R | C | — | — | I | — |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The configuration manager is accountable for all configuration management activities — both strategic (approach, CI models) and operational (CI registration, verification).
2. **Role Combining:** At T1, the configuration manager performs all activities directly, including those assigned to configuration coordinator and configuration librarian at higher tiers. The resource owner role exists at all tiers, as resource owners provide domain knowledge about their CIs regardless of organizational maturity.
3. **Configuration Librarian vs Coordinator:** The configuration librarian focuses on day-to-day CMDB operations (data entry, verification, ad-hoc requests). The configuration coordinator is a specialist who supports the configuration manager on CI model design, approach definition, and cross-practice integration. In smaller T2 organizations, these roles may be combined.
4. **Resource Owner Participation:** Resource owners are consulted on activities affecting their resources (CI model definition, CI registration, verification review) because they hold domain knowledge about the actual configuration. They are responsible for validating CI models against real-world resource characteristics.
5. **Service Owner and SLM as Consumers:** Service owners and the service level manager are primarily informed or consulted parties. They participate when configuration decisions affect service delivery or when they need configuration information for their own processes (impact analysis, SLA reporting, availability planning).
6. **Cross-Practice Integration:** Many configuration management activities are triggered by other processes (change management triggers CI updates, incident management consumes CI data). The RACI matrix covers only the configuration management side of these interfaces — the triggering or consuming process has its own RACI for its activities.
