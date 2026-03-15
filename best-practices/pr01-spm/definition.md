---
process_id: PR01
process_name: "Service Portfolio Management"
category: definition
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

# Service Portfolio Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Portfolio Management §2, FitSM-2 §PR1 -->

Service Portfolio Management ensures that an organization maintains the right mix of services, products, and programmes to execute its strategy within available funding and resource constraints. It governs the service portfolio throughout the full service lifecycle — from initial demand through retirement — so that investment decisions are sound, resources are allocated to the highest-value work, and the portfolio is continually optimized to meet evolving business needs.

## Scope
<!-- sources: ITIL 4 Portfolio Management §2, IT4IT §5.1 Evaluate Value Stream -->

The process covers:

- Defining and maintaining the service portfolio as a structured inventory of all services (proposed, in development, live, and retired)
- Establishing the portfolio management approach, models, and governance structures
- Collecting, evaluating, and prioritizing service initiatives and investment proposals
- Monitoring portfolio performance and value realization against strategic objectives
- Conducting periodic portfolio reviews to approve, reprioritize, or retire portfolio items
- Managing service lifecycle transitions (propose, plan, build, operate, retire)
- Coordinating with enterprise architecture, financial management, and strategy management to ensure portfolio alignment

## Key Concepts

### Service Portfolio Structure
<!-- sources: FitSM-2 §PR1, IT4IT §6.2.3 Product Portfolio -->

The service portfolio is the complete set of services managed by the organization across all lifecycle stages. It typically contains three segments:

- **Service Pipeline:** Services under consideration or in development (proposed, planned)
- **Service Catalogue:** Live services currently available to customers (production)
- **Retired Services:** Services that have been withdrawn but may still require data retention or contractual obligations

At advanced maturity, portfolios may be further segmented into tiers:

- **Market-facing:** Services delivered to external customers
- **Internal-facing:** Services consumed by employees and internal operations
- **Foundational:** Shared infrastructure, platforms, and building blocks underpinning other services

### Portfolio Types
<!-- sources: ITIL 4 Portfolio Management §2 -->

Organizations may maintain multiple interconnected portfolios:

- **Product/Service Portfolio:** The primary inventory of services and products
- **Programme/Project Portfolio:** Initiatives that create, modify, or retire services
- **Customer Portfolio:** Relationships, agreements, and value commitments to customers

### Service Lifecycle Phases
<!-- sources: FitSM-2 §PR1, IT4IT §4.10 -->

Each service progresses through defined lifecycle stages:

1. **Proposed** — Initial concept or demand signal captured
2. **Evaluated** — Business case assessed, feasibility determined
3. **Planned** — Approved for development, resources allocated
4. **In Development** — Being built or significantly modified
5. **Production** — Live and available to consumers
6. **Retiring** — Transition period, consumers migrating away
7. **Retired** — Withdrawn from the catalogue, residual obligations managed

### Investment Categories
<!-- sources: IT4IT §5.1 Evaluate Value Stream -->

Portfolio funding typically falls into two categories:

- **Grow the Business (GtB):** Discretionary investment in new capabilities, innovation, and strategic initiatives
- **Run the Business (RtB):** Non-discretionary investment in maintaining current operations and service levels

Portfolio reviews balance allocation between these categories to ensure both operational stability and strategic advancement.

### Portfolio Optimization Decisions
<!-- sources: ITIL 4 Portfolio Management §3.1 -->

During portfolio reviews, each service or initiative is evaluated using a decision framework:

- **Retain/Hold:** Continue with current investment level
- **Promote/Invest:** Increase investment to grow the service
- **Replace/Renew:** Modernize or substitute with a better alternative
- **Retire/Divest:** Withdraw the service and reallocate resources

## Activities

### Essential (All Tiers)

#### 1. Define the Portfolio Management Approach
<!-- sources: ITIL 4 Portfolio Management §3.1, FitSM-2 §PR1 Initial Setup -->

- Establish how the service portfolio will be documented and maintained
- Define the service specification template covering lifecycle phases, ownership, and key attributes
- Set assessment criteria for evaluating new or changed service proposals
- Document the governance model for portfolio decisions (who approves what, at which thresholds)

#### 2. Establish the Initial Service Portfolio
<!-- sources: FitSM-2 §PR1 Initial Setup -->

- Inventory all existing live services with their key attributes (name, description, owner, status, consumers)
- Document known services in the pipeline and any recently retired services
- Map the parties involved in delivering each service (internal teams, partners, suppliers)
- Identify a single point of contact for each delivery party

#### 3. Manage Demand and Service Proposals
<!-- sources: FitSM-2 §PR1 Ongoing Execution, ITIL 4 Portfolio Management §3.2.2 -->

- Identify demand for new or changed services from customer requirements, market signals, and internal strategy
- Create service proposals using a standardized template that captures the business case, estimated effort, and expected value
- Evaluate proposals against defined assessment criteria before they enter the portfolio pipeline
- Review submissions for completeness and alignment with strategic direction before formal acceptance

#### 4. Maintain the Service Portfolio
<!-- sources: FitSM-2 §PR1 Ongoing Execution -->

- Add approved services to the portfolio with full specification
- Update service records as services transition between lifecycle phases
- Manage changes to existing service specifications (scope, ownership, target levels)
- Retire services that are no longer needed, ensuring all contractual and data-retention obligations are met

### Intermediate (T2+)

#### 5. Monitor Portfolio Performance
<!-- sources: ITIL 4 Portfolio Management §3.2.2, IT4IT §5.1 -->

- Track value realization for each portfolio item against its original business case
- Measure performance against planned value-realization criteria (ROI, adoption, satisfaction)
- Report portfolio health to the portfolio owner and stakeholders, including exceptions and trends
- Aggregate data from monitoring, event management, service level management, and financial management to build a holistic portfolio view

#### 6. Conduct Periodic Portfolio Assessments
<!-- sources: ITIL 4 Portfolio Management §3.2.2 -->

- Merge portfolio monitoring data with broader business performance indicators
- Assess portfolio balance across investment categories (GtB vs. RtB)
- Formulate recommendations for portfolio optimization (invest, divest, reprioritize)
- Produce portfolio reports that feed into formal portfolio reviews

#### 7. Conduct Portfolio Reviews
<!-- sources: ITIL 4 Portfolio Management §3.2.2 -->

- Hold regular governance meetings where new initiatives are approved and existing items reprioritized
- Make formal decisions: approve new investments, divest underperforming services, reprioritize the backlog
- Evaluate changes to the portfolio management approach and models based on lessons learned
- Document decisions in portfolio review reports that feed back into the approach management cycle

### Advanced (T3)

#### 8. Align Portfolio to Enterprise Architecture
<!-- sources: IT4IT §6.1.3 Enterprise Architecture -->

- Ensure each service in the portfolio maps to an enterprise architecture blueprint and value stream
- Validate that approved portfolio items align with architecture roadmap items and strategic objectives
- Track the relationship between portfolio backlog items, scope agreements, and architecture roadmap delivery
- Use architecture governance to ensure new services comply with technology standards, security policies, and platform strategies

#### 9. Manage Proposals and Scope Agreements
<!-- sources: IT4IT §6.2.2 Proposal -->

- Create formal scope agreements for approved portfolio backlog items, capturing budget projections, acceptance criteria, and delivery timelines
- Evaluate proposals using both expedited (urgent/agile) and structured (annual planning) approval paths
- Model labour and asset consumption, validate against available resource pools, and define tangible/intangible benefits
- Track scope agreement status through its lifecycle (proposed → approved → active → deferred → rejected)
- Compare planned benefits against actual delivery outcomes to close the value-realization loop

#### 10. Optimize Portfolio Segmentation and Rationalization
<!-- sources: IT4IT §6.2.3 Product Portfolio -->

- Segment the portfolio into market-facing, internal-facing, and foundational tiers to facilitate strategic planning
- Compare similar services across the portfolio to identify rationalization opportunities (consolidation, deduplication)
- Track total cost of ownership, business criticality, security risk, and investment status for each service
- Support strategic funding and de-funding decisions at the portfolio level across all contained services

## Process Interfaces

### Inputs From Other Processes

| Source Process | Input | Description |
|---------------|-------|-------------|
| PR02 Service Level Management | Service performance data | Actual service levels to compare against portfolio targets |
| PR03 Service Financial Management | Financial data, budgets | Cost information, ROI actuals, and funding constraints |
| PR04 Service Design | Service designs | New or updated service specifications ready for portfolio evaluation |
| PR07 Service Catalogue Management | Catalogue data | Current live service inventory and consumer information |
| PR08 Capacity & Performance Management | Capacity data | Resource availability and constraints for portfolio planning |
| PR15 Change Management | Change proposals | Significant changes that affect portfolio composition |
| PR22 Relationship Management | Customer demand | Business requirements and demand signals from customers |
| PR24 Continual Improvement | Improvement initiatives | Optimization proposals from CSI that may affect the portfolio |

### Outputs To Other Processes

| Target Process | Output | Description |
|----------------|--------|-------------|
| PR02 Service Level Management | Portfolio decisions | Approved services and their target service levels |
| PR03 Service Financial Management | Investment decisions | Approved budgets, funding allocations, and scope agreements |
| PR04 Service Design | Design mandates | Approved service proposals requiring design work |
| PR07 Service Catalogue Management | Catalogue updates | Services transitioning to production or retirement |
| PR15 Change Management | Portfolio-driven changes | Strategic changes arising from portfolio review decisions |
| PR22 Relationship Management | Portfolio roadmap | Planned service changes communicated to customers |
| PR24 Continual Improvement | Portfolio review findings | Lessons learned and improvement opportunities from reviews |

## Roles and Responsibilities
<!-- sources: ITIL 4 Portfolio Management §4, FitSM-2 §PR1 -->

### Essential Roles

| Role | Responsibility |
|------|---------------|
| **Service Portfolio Owner** | Defines the portfolio strategy, monitors portfolio achievements (e.g., return on investment), obtains approvals for the portfolio strategy and implementation plan, secures funding |
| **Service Portfolio Manager** | Approves new initiatives and manages prioritization, ensures the portfolio is reviewed and optimized, leads improvements to the portfolio management practice, communicates the approach and models across the organization |

### Intermediate Roles (T2+)

| Role | Responsibility |
|------|---------------|
| **Portfolio Coordinator** | Facilitates portfolio reviews, maintains portfolio records, coordinates communication between stakeholders |
| **Business Analyst** | Analyses demand signals, evaluates service proposals, supports business case development |
| **Finance Manager** | Provides financial analysis, validates cost models, tracks budget allocation and spend |

### Advanced Roles (T3)

| Role | Responsibility |
|------|---------------|
| **Investment Manager** | Manages investment appraisals, evaluates funding proposals, tracks scope agreement delivery |
| **Enterprise Architect** | Ensures portfolio alignment with architecture blueprints, roadmaps, and technology standards |
| **PMO Representative** | Coordinates programme/project portfolio alignment, tracks delivery of portfolio initiatives |

## Key Artefacts
<!-- sources: FitSM-2 §PR1, ITIL 4 Portfolio Management §3, IT4IT §6.2 -->

| Artefact | Maturity | Description |
|----------|----------|-------------|
| Service Portfolio Register | Essential | Master inventory of all services across lifecycle stages |
| Service Specification Template | Essential | Standardized template for documenting a service (attributes, lifecycle phase, ownership, consumers) |
| Service Proposal Template | Essential | Template for submitting new or changed service requests with business justification |
| Portfolio Management Approach | Intermediate | Documented approach including models, categories, governance rules, and review cadence |
| Portfolio Review Report | Intermediate | Formal record of review decisions (approvals, reprioritizations, retirements) |
| Portfolio Health Dashboard | Advanced | Real-time view of portfolio performance, value realization, and investment balance |
| Scope Agreement | Advanced | Formal agreement linking approved portfolio backlog items to delivery commitments and budgets |

## Automation and Tooling
<!-- sources: ITIL 4 Portfolio Management §5.2 -->

| Activity | Tool Category | Automation Impact |
|----------|--------------|-------------------|
| Define portfolio approach | Collaboration and communication tools | Low |
| Develop portfolio models | CRM, workflow, financial analysis tools | Medium |
| Collect portfolio initiatives | Workflow automation, ERP, reporting tools | Medium–High |
| Monitor portfolio performance | Monitoring, financial assessment, modelling tools | Medium–High |
| Assess portfolio periodically | Workflow automation, collaboration, reporting tools | Medium |
| Conduct portfolio reviews | Collaboration, reporting, dashboard, visualization tools | Medium |

## Maturity Indicators
<!-- sources: synthesized from ITIL 4 Portfolio Management, FitSM-2 §PR1, IT4IT §6.2 -->

### Level 1 — Initial
- Services exist but are not formally inventoried
- No structured process for evaluating new service requests
- Portfolio decisions are ad hoc and reactive

### Level 2 — Managed
- A basic service portfolio register exists covering live services
- Service proposals follow a simple template and approval path
- Portfolio is reviewed periodically but without formal performance data

### Level 3 — Defined
- Complete portfolio spanning pipeline, catalogue, and retired services
- Formal portfolio management approach with documented governance
- Regular portfolio reviews using monitoring data and financial analysis
- Roles (portfolio owner, portfolio manager) are formally assigned

### Level 4 — Measured
- Portfolio performance is tracked against planned value realization criteria
- Investment balance (GtB vs. RtB) is actively managed
- Portfolio health dashboards provide real-time visibility
- Scope agreements link portfolio decisions to delivery commitments

### Level 5 — Optimized
- Portfolio management is tightly integrated with enterprise architecture and strategy management
- Continuous rationalization identifies consolidation and innovation opportunities
- Automated portfolio analytics support proactive decision-making
- End-to-end value realization tracking from proposal through retirement
