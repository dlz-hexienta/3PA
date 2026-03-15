---
process_id: PR03
process_name: "Service Financial Management"
category: definition
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T3
sources:
  - "ITIL 4: Service Financial Management §2–§6"
  - "IT4IT: S2P Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Financial Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Service Financial Management §2.1 -->

Service financial management supports the organization's strategies and plans for service management by ensuring that its financial resources and investments are being used effectively. The practice provides visibility into the budgeting, costing, and accounting activities related to products and services, enabling reliable financial information to support decision-making at many levels of the organization. It is primarily concerned with the economics of services — understanding and optimizing the financial aspects of service delivery and consumption, understanding and optimizing the costs of products throughout their lifecycle, and providing high-quality financial information about products and services to stakeholders. The practice helps to ensure that the organization's products and services are sufficiently funded by providing cost information, planning and managing budgets, and anticipating and monitoring revenues from service delivery where applicable.

## Scope
<!-- sources: ITIL 4 Service Financial Management §2.3 -->

This process covers:

- Defining and communicating the organization's approach to service financial management
- Identifying cost types, cost objects, and cost allocation methods for products and services
- Planning product- and service-related costs and funding, and communicating and controlling budgets
- Monitoring the actual costs and funding of products and services
- Performing management accounting — capturing, allocating, and reporting costs
- Analysing financial data and providing information for decision-making
- Producing standard and tailored service financial reports
- Reviewing and adjusting the service financial management approach

This process does not cover: making funding decisions or prioritizing investments (portfolio management, strategy management), defining strategies for the economic aspects of products and services (strategy management), tracking valuable IT assets (IT asset management), managing financial risks (risk management), negotiating prices with service consumers (relationship management, service level management), negotiating prices with suppliers (relationship management, supplier management), understanding relationships between resources and services (architecture management, service configuration management), planning capacity of products and resources (capacity and performance management), planning and optimization of staffing (workforce and talent management), or general organizational financial activities not directly related to products and services (investments, credit, loans, financial instruments).

## Key Concepts
<!-- sources: ITIL 4 Service Financial Management §2.2 -->

### 1. Cost Model
<!-- sources: ITIL 4 Service Financial Management §2.2 -->
A structured representation of how the costs of resources are distributed across products and services, and how the costs of products and services are allocated to service consumers, customers, and other cost objects. The cost model maps resources to products to services, enabling the organization to understand the full cost of each product and service. Once costs are understood, it is possible to optimize planning, procurement, and utilization of resources, improve portfolio decisions, plan and control budgets, optimize charging, and align resources to organizational strategy.

### 2. Cost Types
<!-- sources: ITIL 4 Service Financial Management §2.2.1 -->
The highest-level categories to which costs are assigned in budgeting and accounting. Following the four dimensions of service management, cost types include: organizations and people (payroll, travel, training, recruiting), information and technology (hardware, software, networks), partners and suppliers (external services), and value streams and processes (management tools, management activities). Rules for cost categorization should ensure all relevant costs are accounted for logically without omissions or duplications.

### 3. Direct and Indirect Costs
<!-- sources: ITIL 4 Service Financial Management §2.2.2 -->
Direct costs are fully allocated to a single cost object. Indirect costs are shared across multiple cost objects and require allocation using drivers. A cost object is any item to which costs are allocated — products, services, projects, customers, or distribution channels. A significant part of digital and IT costs is indirect, making correct allocation a key enabler of the practice. Cost drivers for indirect cost allocation should be relevant (reflecting architectures and operating models), cost-efficient (not requiring unreasonable resources for data collection), objective (using automated monitoring where possible), and motivating (stimulating responsible resource utilization). Overheads are indirect costs that cannot be reasonably allocated to cost objects and are typically distributed using an agreed formula.

### 4. Activity-Based Costing (ABC)
<!-- sources: ITIL 4 Service Financial Management §2.2.2.1 -->
A method for allocating indirect costs by analysing all activities required to manage a product or deliver a service, documenting the resources required for each activity, measuring the amount of each activity performed for each cost object, and allocating the costs accordingly. ABC is accurate but expensive and complex — it should only be used when people's activity costs constitute a significant part of overhead, better cost understanding may significantly improve decisions, and sufficiently reliable and affordable ways exist to calculate or estimate people's time allocation.

### 5. Capital and Operational Costs
<!-- sources: ITIL 4 Service Financial Management §2.2.3 -->
Capital costs (Capex) are the cost of purchasing or creating resources recognized as financial assets — they depreciate over multiple accounting periods, with only depreciation included in each period's costs. Operational costs (Opex) are incurred through normal business operations — repeating payments such as payroll and supplier services, fully included in each period's costs. In tax and financial accounting, the Capex/Opex classification is determined by enterprise financial policies, legislation, and accounting standards. In management accounting, it may be appropriate to adjust Capex rules if this better reflects the actual lifecycle of resources and provides a more accurate understanding of costs.

### 6. Fixed and Variable Costs
<!-- sources: ITIL 4 Service Financial Management §2.2.4 -->
Fixed costs do not change when service usage varies within a defined variation range. Variable costs reflect variations in service consumption. Most fixed costs are actually semi-variable — they change if service consumption exceeds the capacity of the respective resources. Understanding cost variability is important for capacity planning and budgeting — if business plans include consumption growth, budgets should include respective growth of variable costs. Organizations can manage variable costs through effective procurement decisions.

### 7. Budgeting
<!-- sources: ITIL 4 Service Financial Management §2.2.5 -->
The activity of estimating, target-setting, and controlling the spending and earning of money during a particular period or initiative. Budgeting consists of periodic negotiation of future budgets and the ongoing monitoring and adjusting of current budgets. It is the key mechanism for planning and providing funding for resources necessary to meet organizational objectives. Good budgeting is based on a good cost model — it answers fundamental business questions about resource needs, timing, funding sources, progress milestones, and cost adjustment for consumption changes.

### 8. Charging and Pricing
<!-- sources: ITIL 4 Service Financial Management §2.2.5 -->
If funding includes revenue from service delivery, charging becomes an important subject of financial planning. Charging includes pricing (defining prices and terms for service offerings — including price units, tariffs, plans, and payment options) and billing or invoicing (producing documents to service consumers about money owed). Pricing options include cost-based pricing (prices based on estimated or actual costs), market prices (based on established price levels), and going rates (reflecting previous agreements). Collection and debt management are usually not included in the practice scope.

## Activities
<!-- sources: ITIL 4 Service Financial Management §3.2.1, §3.2.2, §3.2.3 -->

### Essential (All tiers)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Analyse stakeholder requirements | Identify the stakeholders interested in service financial management information about products and services. Gather and analyse their requirements for financial data, cost information, budget visibility, and reporting. Determine the appropriate scope and detail for the service financial management approach |
| 2 | Define and agree the service financial management approach | Discuss and agree a service financial management approach — including cost models, budget models, policies, procedures, data structures, roles, and responsibilities. Discuss and approve the approach with key stakeholders including financial management experts and organizational leaders. Balance the benefits of the practice against its cost — the practice itself is a form of overhead |
| 3 | Communicate and integrate the approach | Communicate the agreed service financial management approach to stakeholders across the organization. Implement the approach in conjunction with IT asset management, service configuration management, supplier management, change management, project management, and other relevant practices |
| 4 | Estimate costs and income | Based on analysis of previous and current plans and performance, estimate costs and income for planned initiatives or periods of operation. Income estimates may include charging recommendations. Involve relevant teams to make, review, or confirm estimates |
| 5 | Compile and agree budgets | Aggregate estimates into budgets following the agreed budget model. Submit budgets to appropriate authorities for approval. If not approved, return to estimation with comments. Communicate approved budgets for execution. Where applicable, discuss and agree charging guidelines |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 6 | Monitor and control costs and income | Monitor how budgets are being executed. Authorize spending requests in accordance with the agreed approach. Adjust budgets within agreed tolerances by approving off-budget spending or pricing. Escalate risks and cases of going off-budget outside agreed tolerances to authorities |
| 7 | Review and report on budgets | Review budgets in case of significant deviations, at the end of budgeted initiatives and periods, and on a regular basis. Initiate new planning cycles where required. Produce budget review reports |
| 8 | Identify and capture costs | Following the agreed approach, identify and capture data about costs. This can be largely automated, but manual processing of financial records may occasionally be required |
| 9 | Perform cost allocation | Select a cost model from those defined by the approach to fit stakeholder requirements. Perform cost categorization and allocation to produce information required for decision-making. Manage exceptions within agreed tolerances, reporting every deviation for continual improvement of the approach |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 10 | Provide standard and tailored financial reports | Present required financial information to stakeholders as dashboards, operational reports, or analytical reports in line with the selected cost model. This can be largely automated, but occasional manual reports may be needed, especially for analytical reports |
| 11 | Review and adjust the approach | Monitor and review the adoption, compliance, and effectiveness of the agreed service financial management approach. Perform reviews on both event-based (non-standard requests, errors, new requirements) and interval-based schedules. Initiate changes to the approach and its practical implementation. Report on approach performance to inform continual improvement |

## Inputs
<!-- sources: ITIL 4 Service Financial Management §3.2.1, §3.2.2, §3.2.3 -->

| # | Input | Source |
|---|-------|--------|
| 1 | Organizational architectures and portfolios | Architecture management, portfolio management |
| 2 | Stakeholder requirements for financial information | Executive leaders, product/service owners |
| 3 | Service catalogue and service configuration data | Service catalogue management, service configuration management |
| 4 | IT asset data | IT asset management |
| 5 | Contracts and agreements with suppliers and service consumers | Supplier management, service level management |
| 6 | Organization's financial management policies, approaches, and data | Corporate finance |
| 7 | Records of financial transactions | Accounting systems |
| 8 | Product and service performance reports and capacity forecasts | Capacity & performance management, measurement & reporting |
| 9 | Previous and current plans, budgets, and budget review reports | Service financial management (prior cycles) |

## Outputs
<!-- sources: ITIL 4 Service Financial Management §3.2.1, §3.2.2, §3.2.3 -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Service financial management approach (including cost and budget models) | All practices, management |
| 2 | Service financial management communications and knowledge materials | All practices |
| 3 | Budgets (compiled and approved) | Executive management, product/service owners |
| 4 | Budget execution reports (ongoing and periodic) | Executive management, product/service owners |
| 5 | Spending decisions — assessments and approvals | Product/service owners, change management |
| 6 | Budget review reports | Executive management |
| 7 | Standard and tailored service financial reports | Stakeholders, management |
| 8 | Exception reports | Service financial management (for continual improvement) |
| 9 | Requests for changes and improvement initiatives | Change management, continual improvement |

## Roles
<!-- sources: ITIL 4 Service Financial Management §4.1 Table 4.2, §4.1.1, §4.2 -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Service Financial Manager | Accountable for the service financial management practice. Defines and maintains the service financial management approach. Performs management accounting — identifying, capturing, and allocating costs. Monitors and controls budgets. Produces financial reports. Reviews and adjusts the approach. Requires analytical skills, knowledge of financial management theory and practice, excellent understanding of the organization's architectures and products, and good understanding of stakeholder needs. This role may be performed by team managers, programme and project managers, product owners, or service owners depending on the approach adopted | All |
| Executive Leader | Decides whether to invest in developing the service financial management approach. Approves the approach and budgets. Provides strategic direction for service financial management. Monitors organizational compliance with the approach. In internal IT providers, this may be the CIO or IT director; in external service providers, the CEO, CFO, or CPO | All |
| Finance Business Partner | Provides specialized financial management expertise to digital product and service teams. Bridges the gap between product/service management expertise and financial management expertise. May be a financial professional embedded in product teams, or a digital/IT business partner within the finance team. Advises on cost models, budgeting, pricing, and financial analysis | All |

## Key Artefacts
<!-- sources: ITIL 4 Service Financial Management §3.2, §5 -->

| Artefact | Purpose |
|----------|---------|
| Service Financial Management Approach | Documents the organization's agreed approach — including cost models, budget models, cost types, cost allocation rules, policies, procedures, data structures, roles, and responsibilities |
| Cost Model | Structured representation mapping resources to products to services, including cost types, cost objects, allocation drivers, and overhead distribution rules |
| Budget | Documented estimate of all spending and earning during a particular period or initiative — compiled following the agreed budget model, approved by appropriate authorities |
| Budget Review Report | Periodic report comparing actual costs and income against budgeted amounts — highlighting deviations, risks, and recommended adjustments |
| Service Financial Report | Standard or tailored report presenting management accounting information — cost allocations, cost breakdowns, trend analyses, and financial recommendations for decision-makers |

## Process Interfaces
<!-- sources: ITIL 4 Service Financial Management §2.3 Table 2.1, §2.4 -->

| Interface | Relationship |
|-----------|-------------|
| Service Portfolio Management (PR01) | Financial information informs portfolio decisions. Portfolio management prioritizes funding for initiatives |
| Service Level Management (PR02) | Financial data supports SLA negotiations. Cost information enables cost-benefit analysis of different service levels |
| Service Configuration Management (PR17) | Service configuration data enables accurate cost allocation — understanding which resources support which products and services |
| IT Asset Management (PR18) | IT asset data provides cost information about assets, depreciation schedules, and asset lifecycle costs |
| Capacity & Performance Management (PR08) | Capacity plans and performance forecasts inform cost estimates. Financial information supports cost-benefit analysis of capacity options |
| Availability Management (PR06) | Availability controls have associated costs. Financial analysis supports cost-benefit assessment of availability options |
| Service Continuity Management (PR07) | Continuity measures have associated costs. Financial information supports justification of continuity investments |
| Supplier Management (PR23) | Supplier contracts and pricing directly affect service costs. Financial analysis supports procurement decisions |
| Change Management (PR15) | Financial assessment is part of change evaluation. Budget-affecting changes require financial approval |
| Risk Management (PR21) | Financial risks are identified and managed. Cost information supports risk treatment decisions |
| Continual Improvement (PR24) | Improvement initiatives require financial justification. Financial analysis identifies cost optimization opportunities |
| Measurement & Reporting (PR20) | Financial reporting uses the measurement and reporting framework. Financial metrics contribute to overall organizational reporting |
| Architecture Management | Understanding resource-to-product-to-service relationships is essential for cost allocation. Architecture decisions have financial implications |
