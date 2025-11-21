# Assessment Output Templates

Standard formats for delivering ethics assessment results.

## Executive Summary Template

```
AI ETHICS ASSESSMENT EXECUTIVE SUMMARY

SYSTEM: [Name and brief description]
ASSESSMENT DATE: [Date]
ASSESSOR: [Name/Team]
RISK LEVEL: [Low / Medium / High / Critical]

==============================================================================
KEY FINDINGS
==============================================================================

1. [Most critical ethical issue identified - brief summary]
2. [Second most critical issue - brief summary]
3. [Third most critical issue - brief summary]

==============================================================================
BIAS ANALYSIS
==============================================================================

Fairness Testing Summary:
- Protected attributes tested: [List: race, gender, age, etc.]
- Fairness metrics evaluated: [Statistical parity, equalized odds, etc.]

Key Findings:
[Summary of bias testing results across demographic groups]

Most Concerning Disparity:
[Describe the most significant fairness issue, or state "No significant
disparities identified"]

Intersectional Analysis:
[Note any compound marginalization effects for intersectional identities]

==============================================================================
COMMUNITY IMPACT
==============================================================================

Affected Population:
The system affects [number/description of people] with particular impact on
[vulnerable populations].

Power Dynamics:
[Brief assessment of who gains/loses power and agency]

Accessibility:
[Assessment of whether system works across communities]

Community Engagement:
[Summary of whether/how affected communities were consulted]

==============================================================================
REGULATORY STATUS
==============================================================================

Compliance Assessment: [Compliant / Gaps Identified / Non-Compliant]

Applicable Regulations:
- [Regulation 1]: [Status]
- [Regulation 2]: [Status]
- [Regulation 3]: [Status]

Critical Compliance Gaps:
[List any significant regulatory issues, or state "None identified"]

==============================================================================
DEPLOYMENT RECOMMENDATION
==============================================================================

[ ] APPROVED - Deploy with monitoring plan
[ ] CONDITIONAL - Deploy after addressing specific issues (listed below)
[ ] NOT READY - Substantial work needed before deployment
[ ] DO NOT DEPLOY - Fundamental ethical issues make deployment inadvisable

==============================================================================
REQUIRED ACTIONS BEFORE DEPLOYMENT
==============================================================================

1. [Most critical action required]
   Priority: [Critical / High / Medium]
   Timeline: [Timeframe]
   Owner: [Responsible party]

2. [Second priority action]
   Priority: [Critical / High / Medium]
   Timeline: [Timeframe]
   Owner: [Responsible party]

3. [Third priority action]
   Priority: [Critical / High / Medium]
   Timeline: [Timeframe]
   Owner: [Responsible party]

==============================================================================
ONGOING MONITORING REQUIREMENTS
==============================================================================

Metrics to Monitor:
- [Key metric 1 with threshold]
- [Key metric 2 with threshold]
- [Key metric 3 with threshold]

Review Cadence:
- Real-time: [Automated alerts for threshold violations]
- Daily: [Operations team review]
- Weekly: [Ethics board briefing]
- Monthly: [Comprehensive audit]
- Quarterly: [External review]

Escalation Criteria:
- [Condition that triggers immediate escalation]
- [Condition requiring urgent review]

Responsible Parties:
- Day-to-day monitoring: [Team/person]
- Incident response: [Team/person]
- Regular reviews: [Team/person]

==============================================================================
NEXT STEPS
==============================================================================

Immediate (within 1 week):
- [Action]
- [Action]

Short-term (within 1 month):
- [Action]
- [Action]

Ongoing:
- [Action]
- [Action]

NEXT REVIEW: [Date for next comprehensive assessment]

==============================================================================
ASSESSMENT TEAM
==============================================================================

Lead Assessor: [Name]
Technical Review: [Name]
Domain Expert: [Name]
Community Representative: [Name]
Legal Review: [Name]

Contact: [Email/phone for questions]

==============================================================================
```

## Technical Assessment Report Template

```
TECHNICAL AI ETHICS ASSESSMENT

SYSTEM OVERVIEW
Name: [System name]
Version: [Version number]
Type: [ML model type]
Purpose: [Primary function]
Deployment: [Scale and context]

==============================================================================
FAIRNESS & BIAS ANALYSIS
==============================================================================

TESTING METHODOLOGY
- Dataset: [Training data description, size, time period]
- Protected Attributes: [List all attributes tested]
- Fairness Metrics: [Metrics applied]
- Test Set: [Description of test data]

QUANTITATIVE RESULTS

[For each protected attribute, include detailed metric table]

Protected Attribute: Race/Ethnicity

| Group Comparison | Metric | Value | Threshold | Status |
|-----------------|--------|-------|-----------|--------|
| Group A vs B | Statistical Parity Diff | +0.08 | ±0.10 | ✓ PASS |
| Group A vs B | Equalized Odds Diff | +0.12 | ±0.10 | ✗ FAIL |
| Group A vs B | Disparate Impact Ratio | 0.85 | >0.80 | ✓ PASS |
| Group A vs C | Statistical Parity Diff | +0.15 | ±0.10 | ✗ FAIL |
| Group A vs C | Equalized Odds Diff | +0.18 | ±0.10 | ✗ FAIL |
| Group A vs C | Disparate Impact Ratio | 0.78 | >0.80 | ✗ FAIL |

[Repeat for gender, age, and other protected attributes]

PERFORMANCE BY DEMOGRAPHIC GROUP

| Demographic | Accuracy | Precision | Recall | FPR | FNR | N |
|------------|----------|-----------|---------|-----|-----|---|
| Overall | 87.3% | 83.2% | 79.5% | 4.3% | 8.2% | 10000 |
| Race A | 88.1% | 84.5% | 80.3% | 4.1% | 7.9% | 4000 |
| Race B | 87.5% | 83.8% | 79.8% | 4.2% | 8.1% | 3500 |
| Race C | 85.9% | 80.9% | 77.1% | 5.1% | 9.4% | 2500 |

INTERSECTIONAL ANALYSIS

Most Disadvantaged Groups:
1. [Group combination]: [Metrics]
2. [Group combination]: [Metrics]
3. [Group combination]: [Metrics]

DATA QUALITY ASSESSMENT
- Representation gaps: [Description]
- Historical bias in data: [Issues identified]
- Labeling bias: [Concerns]
- Data quality disparities: [Findings]

MITIGATION RECOMMENDATIONS
1. [Technical mitigation strategy]
2. [Process improvement]
3. [Monitoring enhancement]

==============================================================================
EXPLAINABILITY ASSESSMENT
==============================================================================

INTERPRETABILITY METHODS APPLIED
- Global: [SHAP global values, feature importance]
- Local: [SHAP/LIME for individual predictions]
- Counterfactual: [Available? Implementation?]

EXPLANATION QUALITY
- Fidelity: [How well explanations match model]
- Consistency: [Explanation stability]
- Comprehensibility: [User testing results]
- Actionability: [Can users act on explanations?]

USER-FACING EXPLANATIONS
- Format: [How explanations presented]
- Accessibility: [Literacy level, languages]
- Accuracy: [Validation results]

TRANSPARENCY DOCUMENTATION
- Model card: [Complete? Y/N]
- Algorithmic impact assessment: [Complete? Y/N]
- User documentation: [Adequate? Y/N]

==============================================================================
PRIVACY & SECURITY
==============================================================================

DATA PROTECTION MEASURES
- Encryption: [At rest? In transit?]
- Access controls: [Description]
- Retention policy: [Period and justification]
- Deletion capability: [Implemented? Y/N]

PRIVACY-PRESERVING TECHNIQUES
- Differential privacy: [Applied? Parameters?]
- Federated learning: [Used? Y/N]
- Data minimization: [Implemented? Y/N]
- Anonymization: [Method and effectiveness]

RE-IDENTIFICATION RISK
- Risk level: [Low / Medium / High]
- Vulnerable populations: [Special concerns]
- Mitigation: [Strategies applied]

CONSENT & CONTROL
- Informed consent: [Obtained? How?]
- User rights: [Access, correction, deletion supported?]
- Privacy preferences: [Respected? Y/N]

==============================================================================
ACCOUNTABILITY & GOVERNANCE
==============================================================================

RESPONSIBILITY MAPPING
- Development: [Team/person]
- Deployment: [Team/person]
- Operations: [Team/person]
- Monitoring: [Team/person]
- Remediation: [Team/person]

OVERSIGHT STRUCTURES
- Ethics review board: [Established? Composition?]
- Independent audit: [Capability? Frequency?]
- Stakeholder representation: [Adequate? Y/N]

INCIDENT RESPONSE
- Detection mechanisms: [Description]
- Response protocols: [Documented? Y/N]
- Team and roles: [Defined? Y/N]

==============================================================================
HUMAN OVERSIGHT
==============================================================================

HUMAN-AI COLLABORATION
- AI role: [Advisory / Determinative / Hybrid]
- Human control: [Meaningful? Assessment]
- Override capability: [Implemented? Easy to use?]
- Time for review: [Adequate? Assessment]

AUTOMATION BIAS MITIGATION
- Training provided: [Y/N, description]
- Uncertainty communication: [How?]
- Culture of questioning: [Assessment]

AGENCY PRESERVATION
- Deskilling risk: [Low / Medium / High]
- Mitigation: [Strategies]

==============================================================================
RECOMMENDATIONS
==============================================================================

CRITICAL (Address before deployment)
1. [Recommendation with technical details]
2. [Recommendation with technical details]

HIGH PRIORITY (Address within 30 days of deployment)
1. [Recommendation]
2. [Recommendation]

MEDIUM PRIORITY (Address within 90 days)
1. [Recommendation]
2. [Recommendation]

BEST PRACTICES (Continuous improvement)
1. [Recommendation]
2. [Recommendation]

==============================================================================
```

## Stakeholder Communication Template

For communicating ethics assessment results to affected communities.

```
AI SYSTEM ETHICS ASSESSMENT SUMMARY
[System Name]

What We Assessed:
We conducted an independent ethics assessment of [system name], which
[brief description of what the system does and who it affects].

Who Was Involved:
This assessment was conducted by [team], with input from [community
representatives, external experts, etc.].

What We Found:

The Good News:
- [Positive finding 1]
- [Positive finding 2]
- [Positive finding 3]

Areas of Concern:
- [Concern 1 in plain language]
- [Concern 2 in plain language]
- [Concern 3 in plain language]

What This Means for You:
[Plain language explanation of how findings affect community members]

What We're Doing About It:
1. [Action being taken]
2. [Action being taken]
3. [Action being taken]

Your Rights:
- You have the right to know when AI is involved in decisions about you
- You have the right to an explanation of decisions
- You have the right to appeal or contest decisions
- You have the right to human review

How to Get Help:
- Questions: [Contact information]
- Complaints: [Process and contact]
- Appeals: [Process and contact]
- More information: [Website/resources]

We Want to Hear From You:
Your feedback helps us improve this system. Please share your experience:
[Feedback mechanism]

Next Steps:
[Timeline for improvements and next review]

Available in: [Languages]
Accessible formats: [Large print, audio, etc.]

==============================================================================
```

These templates ensure consistent, comprehensive, and accessible reporting of AI ethics assessments across different audiences.
