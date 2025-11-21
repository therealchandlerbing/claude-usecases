# Context & Impact Analysis

This module guides comprehensive understanding of the AI system's purpose, stakeholders, and potential impacts.

## System Purpose & Scope

Analyze the following dimensions:

**Primary Function and Use Cases**
- What is the core function of this AI system?
- What specific problems does it solve?
- What decisions or recommendations does it make?
- How are its outputs used in practice?

**Decision-Making Authority**
- Is this system advisory (provides recommendations) or determinative (makes final decisions)?
- Who has final authority over decisions?
- Can outputs be overridden? By whom?
- What happens when AI and humans disagree?

**Scale of Deployment**
- How many people are affected?
- What is the geographic scope?
- Is this a pilot or full deployment?
- What is the planned growth trajectory?

**Temporal Scope**
- Are these one-time decisions or ongoing?
- How long do impacts persist?
- Can decisions be revisited or reversed?
- What is the feedback loop timeframe?

**Reversibility of Decisions**
- Can decisions be undone or corrected?
- What is the cost/difficulty of reversal?
- Are there permanent consequences?
- What remediation mechanisms exist?

## Stakeholder Mapping

Identify and analyze all stakeholder groups:

**Direct Users**
- Who interacts directly with the system?
- What is their technical sophistication?
- What control do they have over the system?
- What are their incentives and motivations?

**Affected Parties**
- Who is impacted by system decisions but doesn't use it directly?
- Do they know they're being assessed by AI?
- What recourse do they have?
- How significant is the impact on their lives?

**Vulnerable Populations**
- Which groups face heightened risk of harm?
- Are there populations with historical marginalization relevant here?
- Who has less power to contest or avoid the system?
- Are there groups with special protections needed?

**Decision-Makers**
- Who acts on AI outputs?
- What is their relationship to affected parties?
- Do they understand the AI's limitations?
- Are they incentivized to override when appropriate?

**Oversight Bodies**
- Who reviews and audits the system?
- Do they have necessary independence and authority?
- What enforcement mechanisms exist?
- How often do reviews occur?

## Impact Domains

Assess potential impacts across multiple life domains:

### Economic Impact
- **Employment**: Hiring, firing, promotion, work assignment
- **Financial Access**: Credit, loans, insurance, banking
- **Resources**: Benefits, subsidies, housing, essential services
- **Opportunity**: Career advancement, business opportunities

**Assessment Questions:**
- Does this affect access to economic resources or opportunities?
- Could it create or exacerbate economic inequality?
- What are the financial consequences of errors?
- How does economic impact compound over time?

### Social Impact
- **Relationships**: Social connections, community membership
- **Belonging**: Social acceptance, inclusion/exclusion
- **Reputation**: Social standing, dignity, respect
- **Networks**: Access to social capital and support

**Assessment Questions:**
- Does this affect social relationships or community belonging?
- Could it stigmatize or marginalize certain groups?
- How does it shape social dynamics and interactions?
- What are reputational consequences of system outputs?

### Political Impact
- **Rights**: Civic rights, legal protections
- **Representation**: Political voice, advocacy capacity
- **Participation**: Ability to engage in civic life
- **Power**: Political influence and agency

**Assessment Questions:**
- Does this affect political rights or civic participation?
- Could it influence elections or democratic processes?
- How does it shape power relationships?
- Does it enable or constrain political organizing?

### Health Impact
- **Medical Care**: Diagnosis, treatment, care access
- **Mental Health**: Psychological wellbeing, stress, anxiety
- **Wellbeing**: Overall health and quality of life
- **Safety**: Physical safety and security

**Assessment Questions:**
- Does this affect health or access to healthcare?
- Could it impact mental health or wellbeing?
- What are health consequences of errors?
- Does it affect vulnerable health populations?

### Educational Impact
- **Learning**: Educational opportunities and outcomes
- **Credentials**: Degrees, certifications, qualifications
- **Access**: Admission, financial aid, resources
- **Tracking**: Educational paths and future opportunities

**Assessment Questions:**
- Does this affect educational access or outcomes?
- Could it influence academic tracking or pathways?
- How does it shape future educational opportunities?
- Does it affect students at different developmental stages differently?

### Legal Impact
- **Justice System**: Criminal justice, legal proceedings
- **Rights Enforcement**: Access to justice, legal protections
- **Due Process**: Fair procedures, right to appeal
- **Legal Status**: Immigration, custody, legal standing

**Assessment Questions:**
- Does this affect legal proceedings or outcomes?
- Could it impact constitutional rights?
- What are due process implications?
- Does it affect access to justice?

## Impact Severity Matrix

For each identified impact domain, assess:

| Severity | Description | Examples |
|----------|-------------|----------|
| **Critical** | Irreversible, life-altering consequences | Loss of liberty, denial of critical medical care, permanent status changes |
| **High** | Significant, long-lasting impact | Job loss, loan denial, housing rejection, educational exclusion |
| **Medium** | Meaningful but recoverable impact | Delayed services, additional scrutiny, temporary restrictions |
| **Low** | Minor inconvenience or brief impact | Slightly longer wait times, minimal resource differences |

**Compounding Factors:**
- Vulnerable populations experience higher severity
- Impacts across multiple domains compound
- Irreversible decisions are inherently higher severity
- Scale amplifies severity (more people = greater aggregate harm)

## Analysis Output Template

```
CONTEXT & IMPACT ANALYSIS SUMMARY

SYSTEM OVERVIEW
Purpose: [Core function]
Decision Authority: [Advisory / Determinative / Hybrid]
Scale: [Number of people affected]
Temporal Scope: [One-time / Ongoing / Long-term]

STAKEHOLDER ANALYSIS
Direct Users: [Description, count, characteristics]
Affected Parties: [Who bears consequences]
Vulnerable Populations: [Heightened risk groups]
Decision-Makers: [Who acts on AI outputs]
Oversight: [Review and accountability structures]

IMPACT ASSESSMENT
□ Economic: [Severity level] - [Brief description]
□ Social: [Severity level] - [Brief description]
□ Political: [Severity level] - [Brief description]
□ Health: [Severity level] - [Brief description]
□ Educational: [Severity level] - [Brief description]
□ Legal: [Severity level] - [Brief description]

HIGHEST RISK IMPACTS
1. [Most severe impact area and why]
2. [Second most severe]
3. [Third most severe]

REQUIRED ADDITIONAL ANALYSIS
Based on this context assessment, load these additional modules:
[ ] Bias & Fairness (if affects people differentially)
[ ] Explainability (if consequential decisions)
[ ] Accountability (if significant impacts identified)
[ ] Privacy (if personal data involved)
[ ] Human Oversight (if high severity)
[ ] Community Impact (if affects vulnerable populations)
```
