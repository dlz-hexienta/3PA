---
process_id: PR21
process_name: "Risk Management"
category: kpis
frameworks:
  - itil-v4
  - it4it
maturity:
  essential: true
  intermediate: true
  advanced: true
tier_minimum: T2
sources:
  - "ITIL 4: Risk Management §2.4, §2.5 Table 2.4"
  - "IT4IT: S2P Value Stream"
last_updated: 2026-03-14
status: draft
---

# Risk Management — Best Practice KPIs

## How to Use This KPI Library

Each KPI is graduated by maturity tier. Organizations should implement Essential KPIs first, then layer on Intermediate and Advanced measures as the practice matures. Target values are indicative — organizations should calibrate to their own context during P2 (Requirements & Decisions). Risk management KPIs are mapped to four practice success factors: (1) establishing effective RM governance, (2) developing risk-aware culture and identifying risks, (3) analysing and evaluating risks systematically, and (4) treating risks and monitoring effectiveness. Risk management has no dedicated FitSM process — KPIs draw primarily from ITIL 4. Many risk management metrics are inherently qualitative — proxy indicators and maturity assessments may be needed alongside quantitative measures.

---

## Essential KPIs (T2+)

### KPI-RM-01: Risk Register Coverage
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of defined organizational scopes (services, projects, business units, practices) that have active, maintained entries in the risk register. Scopes without risk register coverage have unmanaged risks — threats and opportunities are neither identified nor treated, leaving the organization exposed to unknown impacts. Coverage should be measured against the agreed scope defined in the risk management policy, not against theoretical total scopes |
| **Formula** | (Organizational scopes with active risk register entries / Total organizational scopes in agreed RM scope) × 100 |
| **Target** | 100% of in-scope organizational units |
| **Frequency** | Quarterly |
| **Data Source** | Risk register, risk management policy |
| **Owner** | Risk Management Committee |

### KPI-RM-02: Risk Owner Assignment Rate
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF2, §3.2.2 Table 3.4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of identified risks that have an assigned owner who is accountable for ensuring the risk is understood, analysed, and appropriately treated. Risks without owners are orphaned — no one is accountable for ensuring they are managed, and they persist in the register without analysis, evaluation, or treatment. Every risk must have exactly one owner, though one person may own multiple risks |
| **Formula** | (Risks with assigned and active owners / Total identified risks in register) × 100 |
| **Target** | 100% |
| **Frequency** | Quarterly |
| **Data Source** | Risk register |
| **Owner** | Risk Management Committee |

### KPI-RM-03: Risk Identification Frequency
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of defined organizational scopes where risk identification activities have been performed within the scheduled interval. Regular risk identification ensures that new and changing risks are captured — infrequent identification leaves the organization blind to evolving threats and opportunities. Risk identification may be performed on a regular schedule or triggered by events such as security breaches, new services, or new partner relationships |
| **Formula** | (Scopes where risk identification was performed on schedule / Total scopes in scope) × 100 |
| **Target** | ≥ 90% |
| **Frequency** | Semi-annually |
| **Data Source** | Risk register, identification activity records |
| **Owner** | Risk Management Committee |

### KPI-RM-04: Risk Analysis Completion Rate
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of identified risks that have been analysed (likelihood and impact assessed) and evaluated (treatment priority determined) using the methods specified in the risk management policy. Unanalysed risks cannot be meaningfully compared, prioritized, or treated — they consume register space without informing decisions. Analysis should be completed within agreed timeframes after identification |
| **Formula** | (Risks with completed analysis and evaluation / Total identified risks) × 100 |
| **Target** | ≥ 95% |
| **Frequency** | Quarterly |
| **Data Source** | Risk register |
| **Owner** | Risk Management Committee |

---

## Intermediate KPIs (T2+)

### KPI-RM-05: Risk Treatment Implementation Rate
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of risks requiring treatment (not accepted) where the selected treatment has been fully implemented within agreed timeframes. Risks with selected but unimplemented treatments represent known exposures — the organization has identified the risk, decided on a response, but has not yet executed it. Treatment implementation should be tracked with specific milestones and completion dates |
| **Formula** | (Risks with treatment fully implemented on schedule / Total risks requiring treatment) × 100 |
| **Target** | ≥ 85%; trending toward 100% |
| **Frequency** | Quarterly |
| **Data Source** | Risk register, treatment implementation records |
| **Owner** | Risk Management Committee |

### KPI-RM-06: Residual Risk within Appetite
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF3, PSF4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of treated risks where the assessed residual risk (remaining after treatment) falls within the organization's stated risk appetite. Residual risk exceeding appetite indicates either inadequate treatment, underestimated risk severity, or risk appetite set unrealistically low. Each treated risk should have its residual risk assessed and compared to the relevant appetite threshold. Risks that remain outside appetite after treatment require escalation and additional response |
| **Formula** | (Treated risks with residual risk within appetite / Total treated risks) × 100 |
| **Target** | ≥ 95% |
| **Frequency** | Quarterly |
| **Data Source** | Risk register, risk appetite statements |
| **Owner** | Risk Management Committee |

### KPI-RM-07: Control Assessment Completion Rate
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF4, §3.2.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of controls that have been assessed for implementation completeness and evaluated for continuing relevance within their scheduled review interval. Unassessed controls may be ineffective, partially implemented, or obsolete — providing a false sense of security. Assessment frequency should be proportionate to risk significance, with high-risk controls assessed more frequently |
| **Formula** | (Controls assessed on schedule / Total controls requiring assessment) × 100 |
| **Target** | ≥ 90% |
| **Frequency** | Semi-annually |
| **Data Source** | Control assessment records, control inventory |
| **Owner** | Risk Management Committee |

### KPI-RM-08: Stakeholder Risk Awareness
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF2, §4.2 -->

| Attribute | Value |
|-----------|-------|
| **Description** | A composite indicator of the organization's risk management culture — measured through stakeholder awareness of risk management policy, understanding of their risk-related responsibilities, willingness to identify and report risks, and satisfaction with risk management communications. Low risk awareness indicates that the practice exists at a governance level but has not permeated the organization — risks go unreported, controls are bypassed, and the risk register does not reflect reality |
| **Formula** | Composite score from risk awareness survey, reported risks per capita, and risk training completion rates |
| **Target** | Positive trend; awareness increasing across all organizational levels |
| **Frequency** | Annually |
| **Data Source** | Risk awareness surveys, risk register contribution metrics, training records |
| **Owner** | Risk Management Committee |

---

## Advanced KPIs (T3)

### KPI-RM-09: Risk Audit Completion Rate
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF4, §3.2.3 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of scheduled risk audits completed on time — including both internal audits and required external audit engagements. Missed or postponed audits mean parts of the risk management framework remain unverified — control weaknesses, framework gaps, and environmental changes may go undetected. Higher-risk areas should be audited more frequently |
| **Formula** | (Risk audits completed on schedule / Total risk audits scheduled) × 100 |
| **Target** | ≥ 90%; critical audits 100% |
| **Frequency** | Annually |
| **Data Source** | Audit schedule, audit completion records |
| **Owner** | Risk Auditor |

### KPI-RM-10: Audit Finding Resolution Rate
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of risk audit findings and corrective actions that are resolved within agreed timeframes. Unresolved audit findings represent known gaps in the risk management framework — each one continues to expose the organization to risk until addressed. Critical findings should have expedited resolution timelines. All findings should be tracked through to completion with appointed owners |
| **Formula** | (Audit findings resolved within agreed timeframe / Total audit findings) × 100 |
| **Target** | ≥ 90%; critical findings 100% |
| **Frequency** | Semi-annually |
| **Data Source** | Audit reports, finding tracking system |
| **Owner** | Risk Management Committee |

### KPI-RM-11: Partner Risk Framework Alignment
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF1, §6 -->

| Attribute | Value |
|-----------|-------|
| **Description** | The percentage of significant partners and suppliers with mutually aligned risk management frameworks — including established communication channels between respective risk owners, risk identification built into service models, and risk signalling mechanisms tested regularly. Unaligned partner frameworks create risk blind spots — the organization cannot effectively identify or manage risks that originate from or are influenced by partner activities |
| **Formula** | (Partners/suppliers with aligned RM frameworks / Total significant partners/suppliers) × 100 |
| **Target** | 100% of significant partners |
| **Frequency** | Annually |
| **Data Source** | Partner agreements, risk framework assessments, signalling test records |
| **Owner** | Risk Management Committee |

### KPI-RM-12: Risk Management Framework Effectiveness
<!-- sources: ITIL 4 RM §2.5 Table 2.4 PSF1, PSF4 -->

| Attribute | Value |
|-----------|-------|
| **Description** | A composite indicator of the overall effectiveness of the risk management framework — measuring whether risks are being identified before they materialize, whether treatment is preventing or reducing impact, whether controls are effective, and whether the governance framework is enabling consistent risk management across the organization. Effective frameworks demonstrate fewer unexpected risk events, lower realized impact from managed risks, and improving risk management maturity over time |
| **Formula** | Composite of: unexpected risk events (trending down), realized impact vs. expected impact, governance framework compliance rate, risk management maturity assessment score |
| **Target** | Positive trend across all composite indicators |
| **Frequency** | Annually |
| **Data Source** | Risk register, incident records, audit reports, maturity assessments |
| **Owner** | Risk Management Committee |

---

## KPI Summary by Tier

| KPI ID | Name | Tier | Frequency |
|--------|------|------|-----------|
| RM-01 | Risk Register Coverage | T2+ | Quarterly |
| RM-02 | Risk Owner Assignment Rate | T2+ | Quarterly |
| RM-03 | Risk Identification Frequency | T2+ | Semi-annually |
| RM-04 | Risk Analysis Completion Rate | T2+ | Quarterly |
| RM-05 | Risk Treatment Implementation Rate | T2+ | Quarterly |
| RM-06 | Residual Risk within Appetite | T2+ | Quarterly |
| RM-07 | Control Assessment Completion Rate | T2+ | Semi-annually |
| RM-08 | Stakeholder Risk Awareness | T2+ | Annually |
| RM-09 | Risk Audit Completion Rate | T3 | Annually |
| RM-10 | Audit Finding Resolution Rate | T3 | Semi-annually |
| RM-11 | Partner Risk Framework Alignment | T3 | Annually |
| RM-12 | Risk Management Framework Effectiveness | T3 | Annually |
