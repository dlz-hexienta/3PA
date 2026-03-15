---
process_id: PR21
process_name: "Risk Management"
category: raci
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Risk Management §4.1 Tables 4.1–4.2, §4.2"
  - "IT4IT: S2P Value Stream"
last_updated: 2026-03-14
status: draft
---

# Risk Management — Best Practice RACI Matrix

## How to Read This Matrix

- **R** — Responsible: performs the work
- **A** — Accountable: owns the outcome (exactly one per activity)
- **C** — Consulted: provides input before the activity
- **I** — Informed: notified after the activity

Risk management is everyone's responsibility within their scope of control. The governing body (board of directors or their delegates) is ultimately accountable for the risk management framework. The ongoing development is usually delegated to one or more risk management committees. The three roles below consolidate the practice-specific responsibilities described in ITIL 4 Table 4.2. In practice, risk owners are distributed across the organization — any manager or subject matter expert may be assigned risk ownership.

## Roles Key

| Abbreviation | Role | Tier |
|-------------|------|------|
| RMC | Risk Management Committee Member | T2+ |
| RO | Risk Owner | T2+ |
| RA | Risk Auditor | T3 |

## Essential Activities (T2+)

### Governance and Risk Identification
<!-- sources: ITIL 4 RM §4.1 Table 4.2, §3.2.1, §3.2.2 -->

| Activity | RMC | RO | RA |
|----------|:---:|:--:|:--:|
| Analyse the environment | A/R | I | I |
| Document risk capacity and risk appetite | A/R | I | I |
| Document risk management policy | A/R | C | I |
| Identify risks | C | A/R | I |
| Analyse and evaluate risks | I | A/R | I |

## Intermediate Activities (T2+)

### Treatment, Direction, and Control Assessment
<!-- sources: ITIL 4 RM §4.1 Table 4.2, §3.2.2, §3.2.1, §3.2.3 -->

| Activity | RMC | RO | RA |
|----------|:---:|:--:|:--:|
| Treat risks | I | A/R | I |
| Provide direction to management | A/R | I | I |
| Assess and evaluate controls | C | A/R | C |

## Advanced Activities (T3)

### Audits and Organizational Monitoring
<!-- sources: ITIL 4 RM §4.1 Table 4.2, §3.2.3, §3.2.1 -->

| Activity | RMC | RO | RA |
|----------|:---:|:--:|:--:|
| Conduct risk audits and reviews | I | C | A/R |
| Monitor the organization and review governance | A/R | I | C |

## Notes

1. **Risk Management Committee Member:** Represents the governing body (board of directors or committee acting on its behalf) responsible for establishing and maintaining the risk management framework. Analyses the environment across PESTLE factors, documents risk capacity and risk appetite using concise and objective risk indicators, develops the risk management policy with awareness of organizational documentation requirements, provides direction to management through communication channels ensuring engagement and clarity, and monitors the organization by reviewing audit reports and performance metrics. The committee defines the risk analysis method, scope, and objects, and ensures that role descriptions can be contained within the framework even for operational line staff. Competency profiles: MC for environment analysis, MC for capacity/appetite documentation, MCL for policy documentation, LC for providing direction, CAM for monitoring.
2. **Risk Owner:** Any subject matter expert, service or product owner, or manager who is assigned ownership of a specific risk and is accountable for ensuring the risk is understood and appropriate action is taken. Risk identification is performed by subject matter experts with professional competencies and visibility over PESTLE factors within their scope of assessment (MTC competency). Risk analysis and evaluation is performed by the risk owner (or delegated to and reviewed by them) with ability to systematically apply qualitative and quantitative risk analysis tools (TML competency). Risk treatment is implemented by the risk owner in coordination with cyber security project managers and other implementers, applying project management practices (CAM competency). Control assessments are performed by risk owners and risk management committee delegates with awareness of existing controls and maintenance requirements (MTCA competency). Multiple risk owners exist across the organization — each responsible for risks within their domain.
3. **Risk Auditor:** Member of an audit committee or external auditor, mandated by the board of directors, responsible for conducting risk audits and reviews that ensure risk management remains appropriate and relevant as the environment changes. Audits may be internal or third-party. Output may identify the need for new or updated controls and provides input to the governance process. Required skills: audit management techniques, command of common audit practices, assured auditor integrity, objectivity, and independence (CAMT competency). Auditors must have access to the risk management framework including the risk register, although risk management culture within the organization must be observed via non-automated interactions.
4. **Distributed Responsibility:** Risk management is one of the practices that underpins everything the service provider does to enable value co-creation. Thus the practice is everyone's responsibility, within their scope of control. The key goal of the governing body is to ensure that all tiers of management in the service provider organization implement the risk management framework within their scopes of control. Role descriptions for risk identification, monitoring, and other activities can be contained within the framework even for operational line staff.
5. **Partner and Supplier Roles:** Partners and suppliers to the service provider can generate new risks and mitigate existing ones. Risk management frameworks for all parties must be mutually aligned with appropriate communication channels established between respective risk owners. Risk identification and proper signalling must be built into the service model with suppliers and regularly tested. While actual risk mitigation activities are likely covered by other practices, the risk management practice ensures framework alignment and appropriate investment in risk identification and analysis.
