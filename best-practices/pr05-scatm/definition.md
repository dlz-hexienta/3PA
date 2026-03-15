---
process_id: PR05
process_name: "Service Catalogue Management"
category: definition
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
  - "ITIL 4: Service Catalogue Management §2–§6"
  - "FitSM-2: §PR1 SPM (service portfolio basis), §PR2 SLM (catalogue creation and maintenance)"
  - "IT4IT: R2F Value Stream"
last_updated: 2026-03-14
status: draft
---

# Service Catalogue Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Service Catalogue Management §2.1, FitSM-2 §PR2 SLM -->

The purpose of the service catalogue management practice is to provide a single source of consistent information on all services and service offerings, and to ensure that it is available to the relevant audience. The practice ensures that all stakeholders refer to a single, consistent source of information about services and service offerings, and provides relevant views matching their needs and level of access. The service catalogue covers all services managed by the organization — including internal, external, provided, and consumed — and serves as a key interface between the service provider and service consumers. In FitSM, service catalogue management is the bridge between the service portfolio (PR1 SPM) and service level agreements (PR2 SLM) — the catalogue is the customer-facing representation of the portfolio and the basis for defining and negotiating service levels.

## Scope
<!-- sources: ITIL 4 Service Catalogue Management §2.3, FitSM-2 §PR2 SLM -->

This process covers:

- Defining the appropriate service description structure — including mandatory attributes and relationships — for the catalogue to be well-structured and meet stakeholder needs
- Capturing service information and keeping it up to date, ensuring the quality of data in the service catalogue
- Defining tailored views of the service catalogue for relevant stakeholder groups and implementing changes to the catalogue structure
- Publishing the service catalogue and managing different views for different stakeholders

This process does not cover: defining and managing the service portfolio (portfolio management), defining services and service offerings including utility and warranty details (business analysis, service design), establishing service level agreements with customers and suppliers (service level management, supplier management), managing service requests (service request management), managing information about relationships between services and other configuration items (service configuration management), managing information about IT service assets (IT asset management, service financial management).

## Key Concepts
<!-- sources: ITIL 4 Service Catalogue Management §2.2 -->

### 1. Service Catalogue
<!-- sources: ITIL 4 Service Catalogue Management §2.2 -->
Structured information about all the services and service offerings of a service provider, relevant for a specific target audience. The term usually refers to a tailored view on services and service offerings, but in the context of the practice it also refers to the collection of service data used as the single source for all catalogue views. This may be managed as a centralized database or as multiple databases managed by different teams — the practice ensures effective integration and quality of service-related information. Creating separate or isolated service catalogues within different technology systems should be avoided as this increases segregation and complexity. Instead, a single repository of service data should generate all agreed tailored views.

### 2. Service Offering
<!-- sources: ITIL 4 Service Catalogue Management §2.2 -->
A formal description of one or more services, designed to address the needs of a target consumer group. A service offering may include goods, access to resources, and service actions. The visible part of a product is described in one or more service offerings addressing the needs of potential consumers. Service offerings are presented in the service catalogue for potential customers, while existing customers see services being consumed and associated agreements.

### 3. Request Catalogue
<!-- sources: ITIL 4 Service Catalogue Management §2.2 -->
A view of the service catalogue providing details on service requests for existing and new services, made available for users. Request catalogues are addressed to users and can also be used by the service provider's teams when interacting with users. As part of the service catalogue practice, request catalogues are maintained in a correct and up-to-date condition.

### 4. Service Catalogue Views
<!-- sources: ITIL 4 Service Catalogue Management §2.4.2 -->
Tailored presentations of service catalogue information for specific stakeholder groups, drawn from a single data repository. Three primary view types are: the user view (service descriptions, prerequisites, request procedures, SLAs, support information — filtered by user status and entitlement), the customer view (agreed service levels, financial data, performance measurement, contractual requirements — filtered by customer and customer group), and the service provider view (technical, security, risk, and process-related information for service delivery — with multiple sub-views for different internal teams). Views should be generated from the central repository, not maintained as separate catalogues.

### 5. Core Service Data
<!-- sources: ITIL 4 Service Catalogue Management §5.1 -->
The mandatory attributes that are included in every service catalogue entry: service name, service description, service status, service owner, and service target audience. These core attributes are supplemented by view-specific data obtained from other sources — service level agreements, financial models, configuration management data, and related records.

### 6. Catalogue Data Integration
<!-- sources: ITIL 4 Service Catalogue Management §5.1 Table 5.1 -->
Service catalogue information is enriched from multiple external sources: service level agreements with customers (service levels, prices, agreements, contacts, available service requests, metrics), service level agreements with suppliers (supporting services, contracts, constraints), service financial models (costs, prices, financial data), configuration management database (related services, configuration items, support teams), and respective records (incidents, problems, changes). Effective integration with these sources — automated where possible — is essential for catalogue accuracy and timeliness.

## Activities
<!-- sources: ITIL 4 Service Catalogue Management §3.2.1, §3.2.2, FitSM-2 §PR2 SLM -->

### Essential (All tiers)

| # | Activity | Description |
|---|----------|-------------|
| 1 | Analyse stakeholder requirements for the service catalogue | Identify key stakeholder groups — users, customers, internal teams, suppliers. Discover and analyse their requirements for catalogue information — scope, granularity, structure, data sources, access controls, and update frequency. Use relationship managers, business analysts, and direct observation where possible |
| 2 | Define the service catalogue data structure | Based on requirements, define the structure including core service data common to all services and view-specific data obtained from other sources. Define the technical approach to collect and maintain data, the approach to presenting standard views, and requirements for automation and integration |
| 3 | Define and agree standard catalogue views | Based on agreed requirements and data structure, define standard views for key stakeholder groups — user view, customer view, and service provider view at minimum. Document user manuals for view settings where necessary. Submit automation requirements |
| 4 | Collect and maintain service catalogue data | After automation solutions are implemented, collect and enter data following the agreed structure. Agree and implement data update procedures and tools. Work with external data owners to ensure timely updates. Establish data sharing protocols with partners and suppliers where applicable |

### Intermediate (T2+)

| # | Activity | Description |
|---|----------|-------------|
| 5 | Provide catalogue views to stakeholders | Fulfil requests for service catalogue views — typically automated through self-service portals. Validate the requestor's entitlement to the requested data and data availability. Form and present the requested view in the agreed format. Handle exceptions for unusual or manual requests |
| 6 | Monitor and maintain catalogue data quality | Ensure catalogue data is correct, complete, and up to date. Ensure automation tools work as agreed. Monitor data integrations with external sources. Treat catalogue errors on user- and customer-facing views as incidents — report, analyse, and correct them |
| 7 | Gather and process user feedback | Collect feedback from catalogue users on a scheduled basis or triggered by validation failures. Monitor user experience directly where technology permits — use patterns, favourite view settings, search requests. Use feedback as input to catalogue design improvements |

### Advanced (T3)

| # | Activity | Description |
|---|----------|-------------|
| 8 | Integrate with external data sources and supplier catalogues | Ensure the organization's service catalogue is integrated with suppliers' data sources and their service catalogues — integration should be seamless, ensuring updates without delays. When participating in complex service networks as integrator or integrated supplier, the catalogue becomes a key integration point between parties |
| 9 | Optimize catalogue usability and user experience | Design for usability — ensure the catalogue has an intuitive, familiar, and smooth interface for both internal and external users. Agree on catalogue utility and warranty and monitor compliance. Enable new users for effective catalogue use. Treat internal and external users equally. Monitor and improve user satisfaction continuously |

## Inputs
<!-- sources: ITIL 4 Service Catalogue Management §3.2.1, §3.2.2, §5.1, FitSM-2 §PR2 SLM -->

| # | Input | Source |
|---|-------|--------|
| 1 | Organization's strategy and architecture | Strategy management, architecture management |
| 2 | Service portfolio | Service portfolio management |
| 3 | Customer and user requirements | Relationship management, business analysis |
| 4 | Contracts and agreements with customers and suppliers | Service level management, supplier management |
| 5 | Service configuration data and service models | Service configuration management |
| 6 | Financial data (costs, prices, budgets) | Service financial management |
| 7 | Service catalogue feedback and continual improvement register | Catalogue users, continual improvement |
| 8 | Policies, regulations, and access control requirements | Information security management, compliance |

## Outputs
<!-- sources: ITIL 4 Service Catalogue Management §3.2.1, §3.2.2, FitSM-2 §PR2 SLM -->

| # | Output | Destination |
|---|--------|-------------|
| 1 | Service catalogue data structure | Catalogue management tools, technical teams |
| 2 | Standard service catalogue views and user manuals | All stakeholder groups |
| 3 | Published service catalogue data | Users, customers, internal teams, suppliers |
| 4 | Service catalogue views (delivered on request) | Requesting stakeholders |
| 5 | Data integration requirements | Technical teams, suppliers |
| 6 | Requirements for catalogue management tools | IT, procurement |
| 7 | Catalogue user feedback data | Continual improvement |
| 8 | Requests for changes to catalogue structure or content | Change management, continual improvement |

## Roles
<!-- sources: ITIL 4 Service Catalogue Management §4.1, §4.1.1, §4.2 -->

| Role | Responsibility | Tier |
|------|---------------|------|
| Service Catalogue Manager | Accountable for the service catalogue practice. Defines, designs, and maintains the catalogue. Understands and manages stakeholder relationships. Continually improves catalogue structure, automation, and views. Integrates the catalogue into value streams. Coordinates with other teams and roles. Acts as customer for catalogue automation solutions. Requires understanding of stakeholders' work and needs, analytical skills, knowledge of data architecture, and communication skills | All |
| Service Owner | Provides service-specific input to the catalogue — service descriptions, status updates, target audience information. Participates in stakeholder requirements analysis, standard view definition, and catalogue review. Ensures the accuracy of catalogue data for their services | All |
| Technical Specialist | Supports data integration, automation, and tooling for the catalogue. Maintains data structures, implements views, manages external data integrations, and resolves technical issues with catalogue systems. Requires knowledge of data architecture and technical skills | All |

## Key Artefacts
<!-- sources: ITIL 4 Service Catalogue Management §2.2, §3.2, §5.1, FitSM-2 §PR2 SLM -->

| Artefact | Purpose |
|----------|---------|
| Service Catalogue Data Structure | Documents the agreed structure of the catalogue — core service data attributes, view-specific attributes, data sources, relationships, and integration requirements |
| Service Catalogue Views | Tailored presentations for stakeholder groups — user view, customer view, service provider view, and request catalogue — generated from the central data repository |
| Service Catalogue User Manual | Documentation for catalogue users on how to access, navigate, and configure catalogue views — including view settings and self-service features |
| Core Service Data Template | Template defining mandatory attributes for each service entry — service name, description, status, owner, and target audience — plus required supplementary attributes |
| Service Catalogue Data | The actual data repository containing all service information — the single source of truth from which all views are generated |

## Process Interfaces
<!-- sources: ITIL 4 Service Catalogue Management §2.3 Table 2.1, §2.4, §5.1, FitSM-2 §PR1 SPM, §PR2 SLM -->

| Interface | Relationship |
|-----------|-------------|
| Service Portfolio Management (PR01) | The service portfolio is the primary source for catalogue content. Portfolio lifecycle decisions (propose, plan, produce, retire) trigger catalogue updates |
| Service Level Management (PR02) | SLA information is a key data source for catalogue views. The catalogue provides the basis for defining and negotiating service levels |
| Service Financial Management (PR03) | Financial data — costs, prices, other financial information — is included in relevant catalogue views |
| Service Design (PR04) | Service design defines services and service offerings that populate the catalogue. SDPs include catalogue requirements |
| Service Desk (PR10) | The service catalogue is a primary tool for the service desk. Catalogue errors on user-facing views should be treated as incidents |
| Incident Management (PR11) | Catalogue errors on user- and customer-facing views are treated as incidents — reported, analysed, and corrected through incident management |
| Service Request Management (PR12) | The request catalogue is a key input to service request fulfilment. Catalogue views enable users to identify and submit service requests |
| Service Configuration Management (PR17) | Configuration data — service models, related CIs, support teams — enriches catalogue views. The catalogue and CMDB should be integrated |
| IT Asset Management (PR18) | Asset information may be referenced in service provider catalogue views |
| Relationship Management (PR22) | Customer and user requirements drive catalogue design. The catalogue is a key interface for relationship management |
| Supplier Management (PR23) | Supplier contracts and services are reflected in catalogue views. Supplier catalogues may be integrated with the organization's catalogue |
