---
process_id: PR16
process_name: "Release & Deployment Management"
category: raci
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
  - "ITIL 4: Release Management §4.1.1, §4.2 Table 4.2"
  - "ITIL 4: Deployment Management §4.1.1, §4.1.2, §4.1.3"
  - "FitSM-2: §PR13 RDM"
  - "IT4IT: R2D Value Stream"
last_updated: 2026-03-13
status: draft
---

# Release & Deployment Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

All activities in this process are T2+ (process tier minimum is T2). The release manager is accountable for the release lifecycle, release models, and the release schedule. The deployment manager is accountable for deployment execution and deployment models. In smaller organizations, the release manager and deployment manager roles may be combined into a single role. Activities marked T3 only apply at that tier.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| RM | Release Manager | T2+ |
| DM | Deployment Manager | T2+ |
| TS | Technical Specialist | T2+ |
| SO | Service Owner | T2+ |

## Essential Activities (T2+)

### Release and Deployment Lifecycle
<!-- sources: ITIL 4 Release Management §3.2.2, §4.2 Table 4.2, ITIL 4 Deployment Management §3.2.1, §4.1.3, FitSM-2 §PR13 RDM -->

| Activity | RM | DM | TS | SO |
|----------|:--:|:--:|:--:|:--:|
| Identify applicable model and plan the release | A/R | C | C | C |
| Build and test the release | A | C | R | C |
| Verify release procedures and deployment readiness | C | A | R | C |
| Execute the deployment | I | A | R | I |
| Execute the release | A/R | I | C | C |
| Verify the release and deployment | A | C | R | C |
| Review and close the release | A/R | C | C | C |

### Emergency Release Handling
<!-- sources: ITIL 4 Release Management §2.2.2, ITIL 4 Deployment Management §3.2.1, FitSM-2 §PR13 RDM -->

| Activity | RM | DM | TS | SO |
|----------|:--:|:--:|:--:|:--:|
| Confirm emergency classification and plan | A/R | C | C | C |
| Build and perform expedited testing | A | C | R | I |
| Execute the emergency deployment | I | A | R | I |
| Execute the emergency release | A/R | I | C | I |
| Verify the emergency release | A | C | R | C |
| Complete records | A/R | C | C | I |
| Conduct the mandatory post-release review | A/R | C | C | C |

## Intermediate Activities (T2+)

### Release and Deployment Model Management
<!-- sources: ITIL 4 Release Management §3.2.1, §4.2 Table 4.2, ITIL 4 Deployment Management §3.2.2, §4.1.3 -->

| Activity | RM | DM | TS | SO |
|----------|:--:|:--:|:--:|:--:|
| Analyse product architecture and service relationships | A/R | C | C | R |
| Define or update the release model | A/R | C | C | C |
| Define or update the deployment model | C | A/R | C | C |
| Validate and test the model | C | C | R | R |
| Publish and communicate the model | A/R | R | I | I |
| Review models periodically | A/R | R | C | C |

### Release Schedule Management
<!-- sources: ITIL 4 Release Management §3.2.1 (release plan communication) -->

| Activity | RM | DM | TS | SO |
|----------|:--:|:--:|:--:|:--:|
| Maintain and publish the release schedule | A/R | C | I | I |
| Coordinate release schedule with change schedule | A/R | C | — | C |

### Release and Deployment Reporting
<!-- sources: ITIL 4 Release Management §2.5, ITIL 4 Deployment Management §2.5 -->

| Activity | RM | DM | TS | SO |
|----------|:--:|:--:|:--:|:--:|
| Extract release and deployment data | A | C | R | — |
| Analyse trends and patterns | A/R | C | — | C |
| Compile the report | A/R | C | — | — |
| Distribute reports to stakeholders | A/R | I | I | I |

## Advanced Activities (T3)

### Release and Deployment Review Analysis and Optimization
<!-- sources: ITIL 4 Release Management §3.2.1 (regular review), ITIL 4 Deployment Management §3.2.2 (deployment review and analysis) -->

| Activity | RM | DM | TS | SO |
|----------|:--:|:--:|:--:|:--:|
| Select releases and deployments for review | A/R | C | — | C |
| Analyse failure patterns and bottlenecks | A/R | R | C | C |
| Assess model effectiveness | A/R | R | C | C |
| Identify and initiate improvements | A/R | C | I | I |
| Communicate findings and updated models | A/R | R | I | I |

## Notes

1. **Single Accountable:** Every activity has exactly one "A". The release manager is accountable for all release-related activities — from release planning through review and closure, as well as release model development and practice optimization. The deployment manager is accountable for deployment execution and deployment model development. Where release and deployment responsibilities overlap, accountability follows the dominant concern of the activity.
2. **Role Combining:** In smaller organizations, the release manager and deployment manager roles may be combined into a single role. The key requirement is that accountability for both release and deployment management is explicitly assigned. When combined, the single role-holder is accountable for the full release and deployment lifecycle.
3. **Release Manager:** Plans, coordinates, and manages releases and the release schedule. Maintains release models and approaches. Promotes adoption of agreed release approaches across the organization. Reviews release effectiveness and drives practice improvement. In organizations with significant release volumes, this is a dedicated role; in others, responsibilities may be taken by product or service owners.
4. **Deployment Manager:** Plans, coordinates, and manages deployments to target environments. Maintains deployment models and procedures. Ensures component integrity throughout the deployment process. Manages deployment resources and monitors performance. Requires strong knowledge of the organization's technology, platforms, and infrastructure. In some organizations, part of the deployment manager's responsibilities may be delegated to deployment coordinators or team leaders.
5. **Technical Specialist:** Executes deployments, performs technical verification of components and environments, and provides expertise on deployment feasibility and risks. May include deployment practitioners, systems administrators, development team members, infrastructure team members, or third-party supplier personnel. In CI/CD environments, many technical specialist activities are automated through the pipeline.
6. **Service Owner:** Provides the service-level perspective on releases and deployments. Participates in release planning, acceptance decisions, architecture analysis, and post-release reviews. May serve as release authority for releases within their service scope. Contributes to model validation by confirming that models meet service-level requirements.
7. **Third-Party Suppliers:** External suppliers are not listed as a separate RACI role but participate in deployment execution as technical specialists under their contractual arrangements. Suppliers may also be involved in deployment model development and review, particularly for components they develop, supply, or support. Release and deployment models should define how third parties are involved and how deployment responsibilities cross organizational boundaries.
