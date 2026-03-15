---
process_id: PR02
process_name: "Service Level Management"
category: policy
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
  - "ITIL 4: Service Level Management"
  - "FitSM-2: §PR2 SLM"
  - "IT4IT: R2F Service Level Component"
last_updated: 2026-03-13
status: draft
---

# Service Level Management — Best Practice Policy

## Policy Statement
<!-- sources: ITIL 4 Service Level Management §2, FitSM-2 §PR2 -->

The organization shall maintain service catalogues that accurately represent available services to customers, and shall establish, negotiate, and manage formal service level agreements that set clear, measurable, business-relevant targets for service quality. All agreements shall be underpinned by corresponding operational commitments from internal teams and external suppliers. Achieved service quality shall be continuously monitored, regularly reviewed with stakeholders, and used to drive continual improvement.

## Objectives

1. Maintain accurate, up-to-date service catalogues that present available services in terms meaningful to customers
2. Ensure every critical service has a formal service level agreement that reflects agreed quality targets across relevant service quality aspects
3. Underpin all customer-facing SLA commitments with corresponding operational level agreements and underpinning agreements
4. Continuously monitor and evaluate actual service quality against agreed targets, using both technical metrics and stakeholder feedback
5. Conduct regular service reviews that provide transparency into service performance and identify improvement opportunities
6. Close the gap between measured service levels and perceived service quality by systematically collecting and acting on user and customer feedback

## Scope

This policy applies to all services delivered by the organization to its customers, regardless of whether service levels are formally documented in individual SLAs or covered by a default agreement. It covers:

- All service catalogues maintained by the organization
- All service level agreements, operational level agreements, and underpinning agreements
- All activities related to defining, negotiating, monitoring, reviewing, and improving service levels
- All roles involved in service level governance, management, and reporting

## Principles
<!-- sources: ITIL 4 Service Level Management §2, §7 -->

### P1. Business-Relevant Targets
Service level targets shall reflect business outcomes and customer experience, not only technical metrics. Targets shall cover the service quality aspects that matter most to consumers — including functionality, availability, performance, timeliness, user support, accuracy, and user experience.

### P2. Agreement Before Delivery
No new or significantly changed service shall be delivered to a customer without an applicable service level agreement (individual or default) that documents agreed quality targets, measurement methods, and reporting arrangements.

### P3. Underpinning Commitments
Every customer-facing service level commitment shall be supported by corresponding internal (OLA) and supplier (UA) commitments. The organization shall not agree to SLA targets that are not backed by achievable operational targets.

### P4. Three-Perspective Monitoring
Service quality shall be assessed from three perspectives: achieved service levels (technical data), user satisfaction (end-user feedback), and customer satisfaction (business sponsor assessment). Reliance on technical metrics alone is insufficient.

### P5. Transparency and Communication
Service performance data, SLA compliance status, and improvement actions shall be communicated to customers and relevant internal stakeholders on a regular, agreed basis. Customers shall have visibility into the quality of services they consume.

### P6. Viability Before Commitment
Before committing to service level targets, the organization shall assess the viability of achieving those targets given available resources, supplier capabilities, and known constraints. SLA commitments shall be realistic and achievable.

### P7. Continual Review and Improvement
Service level agreements and the service level management process itself shall be subject to regular review. Gaps between agreed and achieved service levels shall be treated as improvement opportunities and tracked through to resolution.

## Mandatory Requirements

### Essential (All Tiers)

| ID | Requirement |
|----|------------|
| SLM-R01 | A service catalogue shall exist and be maintained, covering at minimum all services actively delivered to customers |
| SLM-R02 | A default SLA shall be in place, establishing baseline service level commitments for all services where no individual SLA has been negotiated |
| SLM-R03 | SLA, OLA, and UA templates shall be defined and used for all new agreements |
| SLM-R04 | SLA fulfilment shall be evaluated at defined intervals and customers shall be notified of significant violations |
| SLM-R05 | Each service shall have an identified service owner who is accountable for its quality |
| SLM-R06 | A defined method shall exist for notifying customers of SLA violations |

### Intermediate (T2+)

| ID | Requirement |
|----|------------|
| SLM-R07 | Service reviews shall be conducted at a defined cadence (at minimum semi-annually) with documented outcomes |
| SLM-R08 | Customer and user satisfaction shall be systematically collected and analysed alongside technical service level data |
| SLM-R09 | OLA and UA fulfilment shall be evaluated with the same rigour and frequency as SLA fulfilment |
| SLM-R10 | Service quality reports shall be produced and distributed to agreed stakeholders at defined intervals |
| SLM-R11 | Service level requirements shall be documented before SLA negotiation begins, capturing both functional and non-functional expectations |

### Advanced (T3)

| ID | Requirement |
|----|------------|
| SLM-R12 | End-to-end service level monitoring shall be established, spanning infrastructure, application, and business process layers |
| SLM-R13 | SLA lifecycle management shall be automated for standardized services, including drafting, renewal, and expiry notification |
| SLM-R14 | Multi-supplier service levels shall be coordinated through formal integration agreements that define contribution measurement and governance |
| SLM-R15 | Service contracts shall be digitally represented and linked to automated monitoring and reporting systems |

## Compliance and Review

- This policy shall be reviewed at least annually or following significant changes to the service portfolio, customer base, or supplier landscape
- Compliance with this policy shall be verified during internal service management assessments
- Non-compliance shall be escalated to the Service Level Manager and relevant Service Owners for remediation
- Exceptions to this policy require documented justification and approval from the Service Level Manager

## Related Policies

| Policy | Relationship |
|--------|-------------|
| Service Portfolio Management Policy (PR01) | Portfolio decisions establish which services require SLAs |
| Availability Management Policy (PR06) | Availability targets in SLAs drive availability planning |
| Capacity & Performance Management Policy (PR08) | Performance targets in SLAs drive capacity planning |
| Information Security Management Policy (PR09) | Security targets in SLAs feed into security requirements |
| Incident Management Policy (PR11) | Incident resolution targets are derived from SLA commitments |
| Monitoring & Event Management Policy (PR14) | Monitoring provides the technical data for SLA evaluation |
| Measurement & Reporting Policy (PR20) | SLA targets and evaluation data feed service reports |
| Relationship Management Policy (PR22) | Customer communication and reviews are jointly governed |
| Supplier Management Policy (PR23) | UA management is coordinated with supplier governance |
| Continual Improvement Policy (PR24) | Service level gaps drive improvement initiatives |
