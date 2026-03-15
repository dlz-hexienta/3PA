---
process_id: PR09
process_name: "Information Security Management"
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
  - "ITIL 4: Information Security Management"
  - "FitSM-2: §PR6 ISM"
  - "IT4IT: Cross-cutting (Evaluate Value Stream, security governance)"
last_updated: 2026-03-13
status: draft
---

# Information Security Management — Best Practice Process Definition

## Purpose
<!-- sources: ITIL 4 Information Security Management §2, FitSM-2 §PR6 -->

Information Security Management ensures that the organization protects the information it needs to conduct its business. The process establishes and maintains a coherent approach for understanding and managing risks to the confidentiality, integrity, and availability of information, along with related aspects such as authentication and non-repudiation. It governs the policies, controls, and behaviours needed to prevent, detect, and correct security incidents across all organizational assets — from IT systems and data through to people, processes, and supplier relationships.

## Scope
<!-- sources: ITIL 4 Information Security Management §2.3, FitSM-2 §PR6 -->

The process covers protection of information across all assets relevant to service management and delivery:

- **IT systems and infrastructure:** Servers, networks, storage, cloud platforms, and hosting environments
- **Software and applications:** Business applications, middleware, operating systems, and tools
- **Client devices and endpoints:** Desktops, laptops, tablets, phones, and removable media
- **IoT and operational technology:** Connected devices, sensors, and industrial systems
- **Business processes:** Workflows and procedures that handle sensitive information
- **People:** Employees, contractors, and third parties with access to organizational information
- **Partners and suppliers:** External parties that process, store, or transmit organizational data
- **Data and information:** Structured and unstructured data in all forms (digital, physical, verbal)

The process applies to security requirements derived from service level agreements, legislation and regulation, contractual obligations, and the organization's own risk appetite.

## Key Concepts

### Security Characteristics
<!-- sources: ITIL 4 Information Security Management §2.1 -->

Information security is assessed across five characteristics:

| Characteristic | Description |
|---------------|-------------|
| **Confidentiality** | Information is not made available or disclosed to unauthorized entities |
| **Integrity** | Information is accurate, complete, and protected from unauthorized modification |
| **Availability** | Information and supporting services are accessible and usable when required |
| **Authentication** | The identity of an entity (person, system, or process) can be verified as genuine |
| **Non-repudiation** | Actions or events can be proven to have occurred, preventing denial by the parties involved |

### Threats, Vulnerabilities, and Assets
<!-- sources: ITIL 4 Information Security Management §2.2 -->

Security management revolves around understanding the relationship between assets, threats, and vulnerabilities:

- **Asset:** Any component that has value and requires protection (information, systems, infrastructure, people)
- **Threat:** A potential cause of harm to an asset, originating from a **threat actor** (person, organization, or automated process) that may be external or internal, deliberate or accidental
- **Vulnerability:** A weakness in an asset or control that could be exploited by a threat

Organizations must assess both the likelihood of threats materializing and the potential impact on assets to determine appropriate levels of protection. Two complementary assessments support this:

- **Threat assessment:** Evaluates the likelihood and potential impact of identified threats
- **Vulnerability assessment:** Identifies weaknesses in assets and controls that could be exploited

### Risk Management
<!-- sources: ITIL 4 Information Security Management §2.2, FitSM-2 §PR6 -->

Security risk management uses the following core concepts:

| Term | Description |
|------|-------------|
| **Risk** | The possibility of harm arising from a threat exploiting a vulnerability, characterized by likelihood and impact |
| **Control** | A measure that modifies risk — through prevention, detection, or correction of security events |
| **Risk treatment** | The choice of how to address an identified risk, with four options: **avoidance** (eliminating the risk source), **modification** (applying controls to reduce likelihood or impact), **sharing** (transferring risk to a third party such as an insurer), or **retention** (consciously accepting the residual risk) |
| **Residual risk** | The risk that remains after controls have been applied; must fall within the organization's stated risk appetite |

### Controls Balance
<!-- sources: ITIL 4 Information Security Management §2.4 -->

Security controls serve three complementary functions, and an effective security posture requires a balance across all three:

- **Prevention:** Controls that stop security events from occurring (e.g., access restrictions, encryption, network segmentation)
- **Detection:** Controls that identify security events when they occur (e.g., monitoring, alerting, log analysis, intrusion detection)
- **Correction:** Controls that restore normal operation after a security event (e.g., backup and recovery, incident response procedures, patching)

### Control Dimensions
<!-- sources: ITIL 4 Information Security Management §2.4 -->

Controls are applied across four dimensions of service management:

| Dimension | Examples |
|-----------|---------|
| **Organization and people** | Security awareness training, separation of duties, background checks, security culture programmes |
| **Value streams and processes** | Backup procedures, patch management, code review, change approval for security-sensitive changes |
| **Information and technology** | Firewalls, encryption, anti-virus, intrusion detection systems, access control mechanisms |
| **Partners and suppliers** | Contractual security requirements, supplier audits, third-party certification requirements, network isolation |

### Security Policy Areas
<!-- sources: ITIL 4 Information Security Management §2.4 -->

Information security policies typically address:

- Access control and identity management
- Password and authentication standards
- Communications and social media use
- Malware protection
- Information classification and handling
- Remote and mobile working
- Supplier and third-party access
- Intellectual property protection
- Record management and retention
- Personal data protection and privacy

## Activities

### Essential (All Tiers)

#### 1. Classify and Inventory Information Assets
<!-- sources: FitSM-2 §PR6 Initial Setup, ITIL 4 Information Security Management §2.3 -->

- Define an asset classification scheme appropriate to the organization's context
- Inventory all information assets requiring protection, covering the asset categories in scope
- Identify critical assets by assessing their importance to service delivery and business operations
- Map linkages between technical components (CIs) and the information assets they support

#### 2. Perform Risk Assessment
<!-- sources: FitSM-2 §PR6 Initial Setup, ITIL 4 Information Security Management §2.2 -->

- Define the risk assessment method, including criteria for evaluating likelihood and impact
- Perform an initial risk assessment across all identified critical assets
- Identify threats and vulnerabilities relevant to each asset
- Evaluate risk levels and determine risk treatment options (avoid, modify, share, retain)
- Document risk assessment results and accepted residual risks

#### 3. Define Security Policies
<!-- sources: FitSM-2 §PR6 Initial Setup, ITIL 4 Information Security Management §2.4 PSF1 -->

- Develop an overarching information security policy that defines the organization's security objectives, principles, and risk appetite
- Create subordinate policies addressing specific security domains (access control, classification, remote access, etc.)
- Ensure policies address security requirements derived from SLAs, legislation, and contracts
- Communicate policies to all relevant parties and obtain formal approval

#### 4. Define and Document Security Controls
<!-- sources: FitSM-2 §PR6 Initial Setup, ITIL 4 Information Security Management §2.4 PSF2 -->

- Identify the controls required to mitigate each assessed risk to an acceptable level
- Document controls in a security controls register, linking each control to the risks it addresses
- Ensure controls cover all three functions (prevention, detection, correction) and all four dimensions (people, processes, technology, suppliers)
- Submit change requests to implement new or modified controls through the change management process

#### 5. Manage Access Rights
<!-- sources: FitSM-2 §PR6 Ongoing Execution -->

- Define access rights for users, groups, and roles based on the principle of least privilege
- Implement access provisioning and de-provisioning procedures aligned with HR processes (joiners, movers, leavers)
- Periodically review access rights to verify they remain appropriate
- Document access rights assignments and maintain an up-to-date access rights register

#### 6. Manage Security Incidents
<!-- sources: ITIL 4 Information Security Management §3.2.1 -->

The security incident management process follows five phases:

| Phase | Key Activities |
|-------|---------------|
| **Preparation** | Develop and maintain security incident response plans; define roles and responsibilities; identify critical assets and services; establish communication channels and escalation paths |
| **Detection and escalation** | Monitor for potential security events using available tools and human observation; triage initial reports to determine if a security incident has occurred; escalate confirmed incidents |
| **Triage and analysis** | Assess the severity and scope of the incident; determine affected assets, services, and data; preserve evidence for potential investigation |
| **Containment and recovery** | Contain the incident to prevent further damage; eradicate the root cause; restore affected services and data from known-good sources; verify restoration |
| **Post-incident review** | Conduct a post-incident review to identify root causes, assess the effectiveness of the response, capture lessons learned, and feed improvements into policies and controls |

### Intermediate (T2+)

#### 7. Conduct Security Audits and Reviews
<!-- sources: ITIL 4 Information Security Management §3.2.2 -->

- Identify changes to the business, technology, or threat environment that may affect the security posture
- Assess the effectiveness of existing controls against current threats and applicable security standards
- Identify missing controls through gap analysis against security standards and best practices
- Produce an audit report documenting findings, recommendations, and improvement actions
- Feed audit findings into the continual improvement register

#### 8. Manage Security Awareness and Training
<!-- sources: ITIL 4 Information Security Management §4.1.3 -->

- Deliver regular security awareness training to all staff, covering topics such as phishing, social engineering, password safety, malware, data handling, and incident reporting
- Include security requirements in every job description, with both generic responsibilities and role-specific security activities
- Provide ongoing reinforcement of security information through communications, briefings, and awareness campaigns
- Deliver specialized training to roles with elevated security responsibilities (administrators, developers, service desk staff)

#### 9. Monitor Security Compliance Continuously
<!-- sources: ITIL 4 Information Security Management §2.4 PSF2, FitSM-2 §PR6 Ongoing Execution -->

- Evaluate the security posture on an ongoing basis against policies, controls, and regulatory requirements
- Monitor for policy violations, unauthorized access attempts, and configuration drift
- Produce periodic security reports covering compliance status, incident trends, and risk exposure
- Distribute security reports to relevant stakeholders (management, service owners, auditors)

#### 10. Coordinate Supplier Security Requirements
<!-- sources: ITIL 4 Information Security Management §6 -->

- Negotiate information security requirements with partners and suppliers as part of contract and UA management
- Ensure supplier access to organizational networks and systems is controlled through network isolation, strong authentication, and encryption
- Include audit rights and security certification requirements in supplier contracts
- Coordinate with supplier management to review supplier security performance regularly

### Advanced (T3)

#### 11. Implement End-to-End Security Monitoring
<!-- sources: ITIL 4 Information Security Management §5.2 -->

- Deploy security information and event management (SIEM) capabilities to correlate security events across all infrastructure and application layers
- Implement intrusion detection and intrusion prevention systems (IDS/IPS) at critical network boundaries
- Integrate security monitoring with service monitoring to provide unified visibility into security and service quality
- Establish automated alerting and correlation rules to detect complex attack patterns

#### 12. Exercise and Test Security Plans
<!-- sources: ITIL 4 Information Security Management §2.4 PSF3 -->

- Conduct regular exercises and tests of security incident response plans to validate their effectiveness
- Test business continuity and disaster recovery procedures from a security perspective
- Simulate security incidents (tabletop exercises, red team exercises) to assess organizational readiness
- Update plans and procedures based on exercise outcomes and lessons learned

#### 13. Embed Security Across All Value Streams
<!-- sources: ITIL 4 Information Security Management §2.4 PSF4 -->

- Integrate security requirements into service design, development, and deployment processes (security by design)
- Ensure security is considered in all guiding principles, governance structures, and continual improvement activities
- Embed security review gates into change management and release management workflows
- Promote a security-conscious culture through leadership engagement and organizational incentives

## Process Interfaces

### Inputs From Other Processes

| Source Process | Input | Description |
|---------------|-------|-------------|
| PR02 Service Level Management | Security requirements from SLAs | Security-related service level targets and customer security expectations |
| PR06 Availability Management | Availability requirements | Availability targets that drive redundancy and resilience controls |
| PR08 Capacity & Performance Mgmt | Capacity data | Infrastructure capacity information for security infrastructure sizing |
| PR11 Incident Management | Security incident reports | Incidents flagged as security-related for investigation and response |
| PR14 Monitoring & Event Mgmt | Security event data | Alerts, log data, and event correlations from monitoring systems |
| PR15 Change Management | Change proposals | Changes requiring security impact assessment |
| PR17 Service Configuration Mgmt | Configuration data | CMDB data for identifying critical assets and their relationships |
| PR23 Supplier Management | Supplier security assessments | Supplier compliance data and third-party security audit results |

### Outputs To Other Processes

| Target Process | Output | Description |
|----------------|--------|-------------|
| PR02 Service Level Management | Security targets | Achievable security targets for inclusion in SLAs |
| PR04 Service Design | Security requirements | Security architecture requirements for new or changed service designs |
| PR11 Incident Management | Security incident procedures | Procedures for identifying, escalating, and handling security incidents |
| PR15 Change Management | Security change requests | Requests to implement new or updated security controls |
| PR17 Service Configuration Mgmt | Security classification data | Asset classification and security attributes for CMDB records |
| PR23 Supplier Management | Supplier security requirements | Security clauses and audit requirements for supplier contracts |
| PR24 Continual Improvement | Security improvement initiatives | Findings from audits, incident reviews, and risk assessments driving improvements |

## Roles and Responsibilities
<!-- sources: ITIL 4 Information Security Management §4, FitSM-2 §PR6 -->

### Essential Roles

| Role | Responsibility |
|------|---------------|
| **Chief Information Security Officer (CISO)** | Accountable for the overall security posture; defines security strategy and policy; ensures the scope of security extends beyond IT to encompass the whole organization; reports to senior management on security risk |
| **Information Security Manager** | Manages day-to-day security operations; develops and maintains security policies and plans; coordinates risk assessments and control implementation; oversees security incident management |

### Intermediate Roles (T2+)

| Role | Responsibility |
|------|---------------|
| **Information Security Auditor** | Conducts security audits and reviews; assesses control effectiveness against security standards; identifies missing controls; produces audit reports |
| **Security Analyst** | Performs technical security analysis; supports incident triage and investigation; conducts vulnerability assessments; analyses security monitoring data |

### Advanced Roles (T3)

| Role | Responsibility |
|------|---------------|
| **Security Architect** | Designs security architecture for services and infrastructure; defines security patterns and standards; ensures security by design in all new services |
| **Supplier Security Coordinator** | Manages security requirements in supplier contracts; coordinates supplier security audits; monitors third-party compliance with organizational security standards |

## Key Artefacts
<!-- sources: FitSM-2 §PR6, ITIL 4 Information Security Management §3, §5 -->

| Artefact | Maturity | Description |
|----------|----------|-------------|
| Information Asset Inventory | Essential | Register of all information assets with classification, ownership, and criticality |
| Risk Assessment Report | Essential | Documented assessment of threats, vulnerabilities, and risk levels for critical assets |
| Information Security Policy | Essential | Overarching policy defining security objectives, principles, and risk appetite |
| Security Controls Register | Essential | Inventory of all security controls, mapped to the risks they mitigate |
| Access Rights Register | Essential | Record of access rights granted to users, groups, and roles |
| Security Incident Records | Essential | Documentation of security incidents including detection, response, and resolution |
| Security Audit Report | Intermediate | Findings from security audits including control gaps, effectiveness assessments, and recommendations |
| Security Awareness Training Plan | Intermediate | Schedule and content plan for security awareness activities |
| Security Dashboard | Advanced | Real-time view of security posture, incident status, compliance metrics, and risk exposure |

## Automation and Tooling
<!-- sources: ITIL 4 Information Security Management §5.2 -->

### Security Incident Management Process

| Activity | Tool Category | Automation Impact |
|----------|--------------|-------------------|
| Preparation | Knowledge management tools, document repositories | Medium–High |
| Preparation | Service catalogue and CMDB | Very High |
| Detection and reporting | Monitoring tools | Essential |
| Detection and reporting | SIEM and correlation tools | Medium–Very High |
| Detection and reporting | IDS/IPS | High |
| Triage and analysis | Data forensic tools | Low–Essential |
| Triage and analysis | SIEM or log analysis tools | Very High |
| Containment and recovery | Backup and recovery tools | Essential |
| Containment and recovery | Definitive media library | Very High |
| Post-incident review | Continual improvement register | High |
| Post-incident review | Knowledge management tools | Medium |

### Audit and Review Process

| Activity | Tool Category | Automation Impact |
|----------|--------------|-------------------|
| Identify changes to environment | Process maps, CMDB | High |
| Identify missing controls | Security audit tools, vulnerability scanners | High |
| Assess control effectiveness | Security audit tools, vulnerability scanners | High |
| Create audit report | Knowledge management, CI register | Medium–High |

## Maturity Indicators
<!-- sources: synthesized from ITIL 4 Information Security Management, FitSM-2 §PR6 -->

### Level 1 — Initial
- Security is addressed reactively, primarily in response to incidents
- No formal asset inventory or risk assessment process exists
- Security policies, if any, are informal and inconsistently applied
- Security responsibilities are undefined or scattered across roles

### Level 2 — Managed
- A basic information asset inventory exists for critical assets
- An initial risk assessment has been performed and documented
- Core security policies (access control, password, classification) are defined and communicated
- Security controls are documented but may not be systematically mapped to risks
- Security incidents are handled, though processes may be informal

### Level 3 — Defined
- The complete scope of information assets is inventoried and classified
- Risk assessments are performed regularly using a defined methodology
- Comprehensive security policies are maintained and formally approved
- Security controls are documented in a register with clear risk-to-control traceability
- Security incident management follows a defined multi-phase process
- Roles (CISO, security manager) are formally assigned with clear accountability
- Security audits and reviews are conducted on a scheduled basis

### Level 4 — Measured
- Security compliance is continuously monitored against policies and standards
- Security metrics and KPIs are tracked and reported to management
- Supplier security performance is formally assessed and reviewed
- Security awareness training is systematic with documented completion tracking
- Post-incident reviews consistently produce improvement actions that are tracked to closure

### Level 5 — Optimized
- End-to-end security monitoring (SIEM, IDS/IPS) provides real-time visibility across all layers
- Security is embedded into all value streams (security by design, secure development practices)
- Security incident response plans are regularly exercised and tested
- Predictive security analytics identify emerging threats before they materialize
- Security posture is continuously optimized based on threat intelligence and lessons learned
