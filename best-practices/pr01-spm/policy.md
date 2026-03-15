---
process_id: PR01
process_name: "Service Portfolio Management"
category: policy
frameworks:
  - itil-v4
  - fitsm
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: all
sources:
  - "ITIL 4: Portfolio Management"
  - "FitSM-2: §PR1 SPM"
  - "IT4IT: Evaluate Value Stream, Portfolio Function"
last_updated: 2026-03-13
status: draft
---

# Service Portfolio Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Portfolio Management §2, FitSM-2 §PR1 -->

The organization shall maintain a service portfolio that provides a single, authoritative view of all services across their full lifecycle. All decisions to introduce, modify, or retire services shall follow a governed portfolio management process that ensures strategic alignment, sound investment, and continual optimization of the service mix.

## Objectives

1. Ensure the organization invests in the right services to deliver its strategy within available funding and resource constraints
2. Maintain a complete, accurate, and current service portfolio spanning pipeline, catalogue, and retired services
3. Provide transparent governance for service investment decisions through defined approval authorities and review cycles
4. Enable informed decision-making through regular portfolio monitoring, assessment, and value-realization tracking
5. Align the service portfolio with enterprise architecture, financial planning, and customer relationship commitments

## Scope

This policy applies to all services managed by the organization, regardless of lifecycle stage, delivery model, or consumer type. It covers:

- All proposed, planned, in-development, live, and retired services
- All investment decisions related to service creation, modification, and retirement
- All roles involved in portfolio governance, management, and delivery

## Principles
<!-- sources: ITIL 4 Portfolio Management §7, IT4IT §5.1 -->

### P1. Strategic Alignment
Every service in the portfolio shall demonstrably contribute to one or more strategic objectives. Services that no longer align with strategy shall be candidates for retirement or replacement.

### P2. Single Source of Truth
The service portfolio register shall be the authoritative record for all services. No service shall be delivered without a corresponding portfolio entry.

### P3. Evidence-Based Decisions
Portfolio investment decisions shall be based on defined assessment criteria, performance data, and financial analysis — not ad hoc requests or political influence alone.

### P4. Lifecycle Governance
Each service shall have a defined lifecycle stage and a clear owner. Transitions between stages shall require explicit approval according to the governance model.

### P5. Balanced Investment
The organization shall actively manage the balance between discretionary investment (new capabilities) and non-discretionary investment (operational stability), reviewing the allocation at each portfolio review cycle.

### P6. Transparency and Communication
The portfolio management approach, models, and review outcomes shall be communicated to all relevant stakeholders. Portfolio information shall be accessible to authorized parties.

### P7. Continual Optimization
The portfolio shall be subject to regular review and rationalization. Duplicate, underperforming, or misaligned services shall be identified and addressed through the portfolio review process.

## Mandatory Requirements

### Essential (All Tiers)

| ID | Requirement |
|----|------------|
| SPM-R01 | A service portfolio register shall exist and be maintained, covering at minimum all live services |
| SPM-R02 | Every new service proposal shall be evaluated against documented assessment criteria before approval |
| SPM-R03 | Each service shall have a designated owner responsible for its lifecycle |
| SPM-R04 | Service retirements shall follow a managed process that addresses consumer transition and residual obligations |
| SPM-R05 | The portfolio management approach (governance, roles, review frequency) shall be documented and approved |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| SPM-R06 | Portfolio reviews shall be conducted at a defined cadence (at minimum quarterly) with documented outcomes |
| SPM-R07 | Portfolio performance shall be monitored against value-realization criteria and reported to stakeholders |
| SPM-R08 | The portfolio shall span all lifecycle stages: pipeline, catalogue, and retired |
| SPM-R09 | A formal portfolio management approach document shall define models, categories, and decision thresholds |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| SPM-R10 | Portfolio decisions shall be traceable to enterprise architecture roadmap items and strategic objectives |
| SPM-R11 | Formal scope agreements shall link approved portfolio items to delivery commitments, budgets, and timelines |
| SPM-R12 | The portfolio shall be segmented (e.g., market-facing, internal, foundational) to support strategic planning |
| SPM-R13 | End-to-end value realization shall be tracked from proposal through delivery and retirement |

## Compliance and Review

- This policy shall be reviewed at least annually or following significant organizational change
- Compliance with this policy shall be verified during internal service management assessments
- Non-compliance shall be escalated to the Service Portfolio Owner for remediation
- Exceptions to this policy require documented justification and approval from the Service Portfolio Owner

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Service Level Management Policy (PR02) | Portfolio decisions establish target service levels |
| Service Financial Management Policy (PR03) | Financial governance of portfolio investments |
| Change Management Policy (PR15) | Significant portfolio changes follow change governance |
| Continual Improvement Policy (PR24) | Portfolio review findings feed improvement initiatives |
