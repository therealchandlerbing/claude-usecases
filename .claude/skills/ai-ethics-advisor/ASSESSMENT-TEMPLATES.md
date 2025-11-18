# AI Ethics Assessment Templates

**Copy and fill out these templates for your AI system evaluation**

---

## Template 1: Rapid Ethics Screen (Tier 1)

**Use for: Low-risk systems, early exploration, quick sanity check**

```markdown
# AI ETHICS RAPID SCREEN

**Date:** [YYYY-MM-DD]
**System Name:** [Name of AI system]
**Assessor:** [Your name]
**Stakeholders Present:** [Names/roles]

## SYSTEM OVERVIEW

**What does this AI do?**
[Brief description in 1-2 sentences]

**Who uses it?**
[Direct users]

**Who is affected by it?**
[People impacted by its decisions/outputs]

**What decisions does it make?**
[ ] Advisory only (humans decide)
[ ] Automated with human review
[ ] Fully automated
[Describe specific decisions]

**What happens if it gets it wrong?**
[ ] Minor inconvenience
[ ] Moderate impact (time/money/opportunity)
[ ] Significant harm (rights/safety/wellbeing)
[ ] Severe harm (immediate danger/irreversible loss)
[Describe specific consequences]

## RED FLAGS CHECK

Mark any that apply:

**CRITICAL CONCERNS**
- [ ] Makes decisions about children
- [ ] Involves vulnerable populations (elderly, disabled, low-income, immigrants, etc.)
- [ ] Uses biometric data (face, voice, fingerprints, etc.)
- [ ] Criminal justice or law enforcement context
- [ ] Healthcare diagnosis or treatment decisions
- [ ] Housing or employment decisions
- [ ] No human oversight possible
- [ ] Can't explain how decisions are made

**HIGH-PRIORITY CONCERNS**
- [ ] Uses demographic data (race, gender, age, etc.) as input
- [ ] Training data includes historical bias
- [ ] Affects >10,000 people
- [ ] Decisions are hard to reverse or appeal
- [ ] Team lacks diversity
- [ ] Affected communities not consulted
- [ ] No monitoring plan exists
- [ ] Privacy safeguards unclear

**Count of flags:**
- Critical: [X]
- High-Priority: [X]

## RISK ASSESSMENT

Based on the above:

**Overall Risk Level:**
[ ] Low (0 critical, 0-2 high-priority flags)
[ ] Medium (0 critical, 3+ high-priority flags)
[ ] High (1+ critical flags)
[ ] Critical (2+ critical flags OR severe harm possible)

## IMMEDIATE ACTIONS REQUIRED

**If LOW risk:**
- [ ] Document this screen
- [ ] Proceed with basic best practices
- [ ] Review again in 6 months or before scaling

**If MEDIUM risk:**
- [ ] Proceed to Tier 2 Comprehensive Assessment
- [ ] Form ethics review team
- [ ] Engage affected communities
- [ ] Delay deployment until assessment complete

**If HIGH/CRITICAL risk:**
- [ ] STOP development/deployment
- [ ] Escalate to ethics board immediately
- [ ] Require full impact assessment
- [ ] Engage legal counsel
- [ ] Mandatory external audit
- [ ] Do not proceed without approval

## NOTES AND CONCERNS

[Any additional observations, questions, or concerns]

## NEXT STEPS

1. [Specific action]
2. [Specific action]
3. [Specific action]

**Next Review Date:** [YYYY-MM-DD]

---

**Assessor Signature:** _________________ **Date:** _________

**Reviewed by:** _________________ **Date:** _________
```

---

## Template 2: Comprehensive Ethics Assessment (Tier 2)

**Use for: Moderate-risk systems requiring detailed evaluation**

```markdown
# COMPREHENSIVE AI ETHICS ASSESSMENT

**Assessment Date:** [YYYY-MM-DD]
**System Name:** [Full name of AI system]
**Version:** [Version number or release identifier]
**Assessment Lead:** [Name and title]
**Assessment Team:** [Names and roles of team members]
**Stakeholders Consulted:** [Names/organizations]

---

## SECTION 1: CONTEXT & IMPACT

### 1.1 System Description

**Primary Purpose:**
[What problem does this solve? What need does it address?]

**Key Functions:**
- [Function 1]
- [Function 2]
- [Function 3]

**Technical Approach:**
[High-level description of how it works]

**Decision Authority:**
[ ] Advisory (human makes final decision)
[ ] Augmented (AI and human collaborate)
[ ] Automated with human review (human can override)
[ ] Fully automated (human cannot intervene)

**Deployment Scale:**
- Current users: [Number]
- Projected users in 1 year: [Number]
- Geographic scope: [Region/countries]
- Frequency of decisions: [Per day/week/month]

### 1.2 Stakeholder Analysis

| Stakeholder Type | Specific Groups | Number Affected | Impact Level |
|------------------|----------------|-----------------|--------------|
| Direct Users | [Who interacts with system] | [N] | [Low/Med/High] |
| Decision Subjects | [Who decisions are about] | [N] | [Low/Med/High] |
| Affected Non-Users | [Indirect impacts] | [N] | [Low/Med/High] |
| Vulnerable Populations | [Specific groups] | [N] | [Low/Med/High] |
| Operators/Reviewers | [Who manages system] | [N] | [Low/Med/High] |

**Vulnerable Populations Identified:**
- [ ] Children (<18)
- [ ] Elderly (>65)
- [ ] People with disabilities
- [ ] Low-income communities
- [ ] Racial/ethnic minorities
- [ ] LGBTQ+ individuals
- [ ] Immigrants/refugees
- [ ] People with criminal records
- [ ] Other: [Specify]

**Engagement with Affected Communities:**
[ ] Not yet conducted (REQUIRED before deployment)
[ ] In progress
[ ] Completed

[Describe engagement: methods used, participants, key insights, how feedback influenced design]

### 1.3 Impact Domains

Mark all that apply and describe:

**Economic Impact:**
- [ ] Employment decisions (hiring, firing, promotion, scheduling)
- [ ] Credit/lending (approval, terms, rates)
- [ ] Insurance (coverage, pricing, claims)
- [ ] Resource allocation
- [ ] Other: [Specify]

[Description of economic impact:]

**Social Impact:**
- [ ] Affects relationships or social connections
- [ ] Influences community cohesion
- [ ] Shapes social norms or expectations
- [ ] Other: [Specify]

[Description of social impact:]

**Health Impact:**
- [ ] Medical diagnosis or treatment
- [ ] Mental health assessment
- [ ] Health resource allocation
- [ ] Other: [Specify]

[Description of health impact:]

**Educational Impact:**
- [ ] Admissions decisions
- [ ] Grade/assessment prediction
- [ ] Resource allocation
- [ ] Student tracking/routing
- [ ] Other: [Specify]

[Description of educational impact:]

**Legal/Justice Impact:**
- [ ] Risk assessment (bail, sentencing, parole)
- [ ] Predictive policing
- [ ] Fraud detection
- [ ] Other: [Specify]

[Description of legal impact:]

---

## SECTION 2: BIAS & FAIRNESS ASSESSMENT

### 2.1 Data Audit

**Training Data Source:**
[Where did the data come from? Timeframe?]

**Data Demographics:**

| Demographic Attribute | Representation in Training Data | Representation in Target Population |
|-----------------------|--------------------------------|-------------------------------------|
| [e.g., Gender] | [e.g., 60% F, 40% M] | [e.g., 51% F, 49% M] |
| [e.g., Race/Ethnicity] | [Breakdown] | [Breakdown] |
| [e.g., Age] | [Breakdown] | [Breakdown] |
| [e.g., Geography] | [Breakdown] | [Breakdown] |

**Representation Gaps Identified:**
[Any underrepresented groups? Missing groups? Imbalances?]

**Historical Bias in Data:**
- [ ] Data reflects past discrimination
- [ ] Labels encode subjective judgments
- [ ] Data quality varies by group
- [ ] Missing data patterns correlate with demographics

[Describe specific historical biases found:]

**Proxy Variables:**
- [ ] Features that correlate with protected attributes identified
- [ ] Examples: [e.g., "Zip code correlates with race"]

### 2.2 Fairness Testing Results

**Protected Attributes Tested:**
- [ ] Race/Ethnicity
- [ ] Gender/Gender Identity
- [ ] Age
- [ ] Disability Status
- [ ] Socioeconomic Status
- [ ] Geographic Location
- [ ] Other: [Specify]

**Testing Methodology:**
[Describe how you tested, sample sizes per group, statistical approach]

**Fairness Metrics Calculated:**

#### Statistical Parity Difference

| Group Comparison | SPD Value | Threshold | Pass/Fail |
|------------------|-----------|-----------|-----------|
| [Group A vs Group B] | [0.XX] | +/-0.10 | [Pass/Fail] |
| [Group A vs Group C] | [0.XX] | +/-0.10 | [Pass/Fail] |

#### Disparate Impact Ratio (80% Rule)

| Group Comparison | DI Ratio | Threshold | Pass/Fail |
|------------------|----------|-----------|-----------|
| [Group A vs Group B] | [0.XX] | >=0.80 | [Pass/Fail] |
| [Group A vs Group C] | [0.XX] | >=0.80 | [Pass/Fail] |

#### Equalized Odds Difference

| Group Comparison | EOD Value | Threshold | Pass/Fail |
|------------------|-----------|-----------|-----------|
| [Group A vs Group B] | [0.XX] | +/-0.10 | [Pass/Fail] |
| [Group A vs Group C] | [0.XX] | +/-0.10 | [Pass/Fail] |

**Performance by Demographic Group:**

| Group | Accuracy | Precision | Recall | FPR | FNR |
|-------|----------|-----------|--------|-----|-----|
| [Group A] | [%] | [%] | [%] | [%] | [%] |
| [Group B] | [%] | [%] | [%] | [%] | [%] |
| [Group C] | [%] | [%] | [%] | [%] | [%] |

**Quality of Service Disparities:**
- [ ] Significant performance differences identified (>10%)
- [ ] All groups receive comparable quality

[Describe any disparities:]

**Intersectional Analysis:**
[Results for combinations of protected attributes]

### 2.3 Fairness Assessment Summary

**Violations Identified:**
- [List any metric violations with groups and severity]

**Root Cause Analysis:**
[Why do these disparities exist? Data? Model? Features?]

**Mitigation Actions:**
1. [Specific action to address each violation]
2. [Action]
3. [Action]

---

## SECTION 3: EXPLAINABILITY & TRANSPARENCY

### 3.1 Model Interpretability

**Model Type:**
[ ] Inherently interpretable (linear model, decision tree, rules-based)
[ ] Interpretable with techniques (feature importance, SHAP, LIME)
[ ] Black box (deep learning, complex ensemble)

**Explanation Methods Implemented:**
- [ ] Global feature importance
- [ ] Local explanations (SHAP/LIME)
- [ ] Counterfactual explanations
- [ ] Natural language explanations
- [ ] Other: [Specify]

**Sample Explanation Quality:**
[Paste an example explanation the system provides]

**Is this explanation:**
- [ ] Technically accurate
- [ ] Understandable to non-experts
- [ ] Actionable (explains what could change outcome)
- [ ] Complete (covers main factors)

### 3.2 Transparency Documentation

**Completed:**
- [ ] Model card published
- [ ] Data sheet for dataset
- [ ] Algorithmic impact statement
- [ ] User-facing documentation
- [ ] API documentation includes ethical considerations
- [ ] Limitations clearly stated

---

## SECTION 4: ACCOUNTABILITY & GOVERNANCE

### 4.1 Responsibility Mapping

| Role | Name/Team | Responsibilities |
|------|-----------|------------------|
| System Owner | [Name] | [Overall accountability] |
| Development Lead | [Name] | [Design and implementation] |
| Data Owner | [Name] | [Data quality and governance] |
| Operations Lead | [Name] | [Day-to-day operation and monitoring] |
| Ethics Review | [Name/Board] | [Ethical oversight and approval] |
| Incident Response | [Name/Team] | [Responding to bias incidents] |
| User Support | [Name/Team] | [User questions and appeals] |

### 4.2 Governance Structure

**Ethics Review Board:**
[ ] Established
[ ] Not yet established (REQUIRED)

**Composition:**
- [Name, Role/Expertise]
- [Name, Role/Expertise]
- [Name, Role/Expertise]

**Diversity of Board:**
- [ ] Technical expertise represented
- [ ] Domain expertise represented
- [ ] Ethics/social science expertise represented
- [ ] Legal expertise represented
- [ ] Affected community representation
- [ ] Demographic diversity present

### 4.3 Incident Response Plan

**Bias Incident Detection:**
- [ ] Automated alerts configured
- [ ] User reporting mechanism established
- [ ] Regular audit schedule defined

**Response Protocol:**

**CRITICAL incidents (respond within 1 hour):**
1. [Action]
2. [Action]
3. [Action]

**Contact:** [Name, Phone, Email]

---

## SECTION 5: PRIVACY & DATA PROTECTION

### 5.1 Privacy Risk Assessment

**Personal Data Collected:**
- [Type of data 1]: [Purpose, Retention period]
- [Type of data 2]: [Purpose, Retention period]
- [Type of data 3]: [Purpose, Retention period]

**Sensitive Data:**
- [ ] Health information
- [ ] Financial information
- [ ] Biometric data
- [ ] Location data
- [ ] Protected class information
- [ ] Other: [Specify]

**Data Minimization:**
- [ ] Only necessary data collected
- [ ] Retention periods defined and justified
- [ ] Deletion process established

### 5.2 Privacy-Preserving Techniques

**Implemented:**
- [ ] Differential privacy
- [ ] Federated learning
- [ ] Data anonymization
- [ ] Pseudonymization
- [ ] Encryption (at rest, in transit)
- [ ] Other: [Specify]

### 5.3 Consent & User Control

**User Rights:**
- [ ] Access their data
- [ ] Correct inaccuracies
- [ ] Delete their data (right to be forgotten)
- [ ] Object to processing
- [ ] Data portability
- [ ] Withdraw consent

---

## SECTION 6: HUMAN OVERSIGHT & CONTROL

### 6.1 Human-in-the-Loop Design

**Human Role:**
[ ] Reviews all AI decisions before implementation
[ ] Reviews flagged cases (criteria: [specify])
[ ] Spot checks (frequency: [specify])
[ ] Only intervenes on user appeal
[ ] No human review (fully automated)

**Meaningful Control Assessment:**
- [ ] Humans can understand AI recommendations
- [ ] Humans have sufficient time to review
- [ ] Humans can override AI decisions without penalty
- [ ] Override patterns are monitored

**Override Capability:**
- Override mechanism: [Describe]
- Override rate: [Target % and actual %]
- Override tracking: [Yes/No]

### 6.2 Escalation Paths

**Cases Escalated to Human Review:**
- [ ] High-uncertainty predictions
- [ ] Predictions affecting vulnerable populations
- [ ] User-requested review
- [ ] Conflicting information present
- [ ] Other: [Specify]

---

## SECTION 7: REGULATORY COMPLIANCE

### 7.1 Risk Classification

**EU AI Act Classification:**
[ ] Unacceptable Risk (PROHIBITED)
[ ] High Risk (strict requirements)
[ ] Limited Risk (transparency obligations)
[ ] Minimal Risk (no specific requirements)

**US Regulatory Context:**

**Applicable Laws/Regulations:**
- [ ] Equal Credit Opportunity Act (ECOA)
- [ ] Fair Housing Act
- [ ] Title VII (employment)
- [ ] Americans with Disabilities Act (ADA)
- [ ] FTC Act Section 5 (unfair/deceptive practices)
- [ ] HIPAA (if healthcare)
- [ ] State AI laws: [List states]
- [ ] Other: [Specify]

### 7.2 Compliance Requirements

**Requirements Met:**
- [ ] Risk management system
- [ ] Data governance procedures
- [ ] Technical documentation
- [ ] Logging and record-keeping
- [ ] Transparency obligations
- [ ] Human oversight measures
- [ ] Accuracy/robustness testing
- [ ] Post-market monitoring plan

**Compliance Gaps:**
- [Gap 1]: [Remediation plan and timeline]
- [Gap 2]: [Remediation plan and timeline]

**Legal Review:**
- [ ] Legal counsel consulted
- [ ] Approval obtained: [Date]

---

## SECTION 8: MONITORING & SAFEGUARDS

### 8.1 Technical Safeguards

**Bias Monitoring:**
- [ ] Automated fairness metric tracking
- [ ] Real-time alerts for violations
- [ ] Dashboard for operations team
- [ ] Regular reporting to leadership

**Alert Thresholds:**
| Metric | Threshold | Alert Type | Response Owner |
|--------|-----------|------------|----------------|
| [Metric 1] | [Value] | [Email/Slack/Page] | [Name/Role] |
| [Metric 2] | [Value] | [Alert type] | [Name/Role] |

### 8.2 Audit Schedule

**Internal Audits:**
- Frequency: [Monthly/Quarterly]
- Scope: [What's reviewed]
- Owner: [Name/team]

**External Audits:**
- Frequency: [Annual/Bi-annual]
- Auditor: [Firm/organization]
- Last audit: [Date]
- Next audit: [Planned date]

---

## SECTION 9: COMMUNITY IMPACT

### 9.1 Stakeholder Engagement Summary

**Engagement Methods Used:**
- [ ] Focus groups ([N] sessions, [N] participants)
- [ ] Surveys ([N] responses)
- [ ] Community advisory board
- [ ] Public comment period
- [ ] User testing
- [ ] Other: [Specify]

**Key Insights from Communities:**
1. [Insight]
2. [Insight]
3. [Insight]

**Design Changes Based on Feedback:**
1. [Change made in response to feedback]
2. [Change]
3. [Change]

### 9.2 Power Dynamics

**Who gains power/authority:**
- [Group/role]: [Type of power gained]

**Who loses power/autonomy:**
- [Group/role]: [Type of power lost]

**Marginalized Groups:**
- [ ] System amplifies existing inequities
- [ ] System reduces inequities
- [ ] System maintains status quo

[Explanation:]

### 9.3 Accessibility & Inclusion

**Accessibility Standards:**
- [ ] WCAG 2.1 Level AA compliant
- [ ] Screen reader compatible
- [ ] Keyboard navigation
- [ ] Multiple modalities (text, audio, visual)

**Language Support:**
- Languages available: [List]
- Translation quality verified: [Yes/No]

---

## SECTION 10: DEPLOYMENT DECISION

### 10.1 Readiness Assessment

**Technical Readiness:**
- [ ] Performance meets requirements
- [ ] Bias testing complete and acceptable
- [ ] Monitoring systems configured
- [ ] Incident response tested

**Governance Readiness:**
- [ ] Ethics board approval
- [ ] Legal approval
- [ ] Accountability structure in place
- [ ] Documentation complete

**Stakeholder Readiness:**
- [ ] User communication prepared
- [ ] Feedback mechanisms established
- [ ] Support team trained
- [ ] Appeal process operational

### 10.2 Pre-Deployment Requirements

**Must complete before deployment:**
1. [Specific requirement]
2. [Requirement]
3. [Requirement]

### 10.3 Deployment Approach

**Rollout Strategy:**
[ ] Full deployment
[ ] Phased rollout (timeline: [specify])
[ ] Limited pilot (scope: [specify])

**Success Criteria:**
- [Metric]: [Target]
- [Metric]: [Target]
- [Metric]: [Target]

**Rollback Plan:**
- Trigger conditions: [When to pause/reverse deployment]
- Rollback procedure: [Steps]

### 10.4 Post-Deployment Plan

**Review Schedule:**
- Next ethics assessment: [Date]
- Next external audit: [Date]
- System sunset review: [Date]

---

## SECTION 11: FINAL RECOMMENDATION

### Overall Assessment

**Risk Level:**
[ ] Low Risk
[ ] Medium Risk
[ ] High Risk
[ ] Critical Risk

**Fairness Status:**
[ ] Meets all fairness thresholds
[ ] Minor violations with mitigation plan
[ ] Significant violations requiring remediation
[ ] Not ready (fundamental fairness issues)

**Compliance Status:**
[ ] Fully compliant
[ ] Substantially compliant (minor gaps)
[ ] Material gaps requiring remediation
[ ] Non-compliant (cannot deploy)

### Deployment Decision

[ ] **APPROVED FOR DEPLOYMENT**
   All requirements met. Proceed with deployment plan.

[ ] **CONDITIONAL APPROVAL**
   May deploy after completing the following:
   1. [Condition]
   2. [Condition]
   3. [Condition]

[ ] **NOT READY FOR DEPLOYMENT**
   Significant issues must be addressed:
   1. [Issue and required remediation]
   2. [Issue and remediation]
   3. [Issue and remediation]

   Next assessment date: [Date]

[ ] **DO NOT DEPLOY**
   Fundamental ethical issues identified:
   [Explanation]

### Key Strengths
1. [Something the system does well ethically]
2. [Strength]
3. [Strength]

### Key Concerns
1. [Most significant remaining concern]
2. [Concern]
3. [Concern]

### Top Recommendations
1. [Most important recommendation]
2. [Recommendation]
3. [Recommendation]

---

## SECTION 12: SIGN-OFF

**Assessment Lead:**
Name: _________________________________
Title: _________________________________
Signature: ____________________________ Date: ___________

**Ethics Review Board Approval:**
Chair Name: _________________________________
Signature: ____________________________ Date: ___________

**Legal Approval:**
Counsel Name: _________________________________
Signature: ____________________________ Date: ___________

**System Owner Acknowledgment:**
Name: _________________________________
Title: _________________________________
Signature: ____________________________ Date: ___________

---

## APPENDICES

**Attach:**
- [ ] Detailed fairness testing results (full tables)
- [ ] Stakeholder consultation notes
- [ ] Legal analysis memo
- [ ] Model card
- [ ] Data sheets
- [ ] Monitoring dashboard screenshots/specs
- [ ] Incident response runbooks
- [ ] Training materials
- [ ] Communication templates
```

---

## Template 3: Bias Incident Report

**Use when: A bias or fairness issue is detected in production**

```markdown
# BIAS INCIDENT REPORT

**Incident ID:** [Unique identifier]
**Date Detected:** [YYYY-MM-DD HH:MM]
**Detected By:** [Name/Role or Monitoring System]
**System:** [AI system name]
**Severity:** [Critical / High / Medium / Low]

---

## INCIDENT SUMMARY

**What happened:**
[Brief description of the bias incident - 2-3 sentences]

**Who was affected:**
[Demographic group(s), number of people, timeframe]

**Impact:**
[ ] Allocative harm (unfair distribution of resources/opportunities)
[ ] Representational harm (stereotyping, demeaning)
[ ] Quality-of-service disparity
[ ] Privacy violation
[ ] Other: [Specify]

[Describe specific harm:]

---

## DETECTION

**How was this detected:**
[ ] Automated monitoring alert
[ ] User complaint
[ ] Internal audit
[ ] External audit
[ ] Media/public report
[ ] Other: [Specify]

**Specific trigger:**
[What metric, complaint, or observation triggered identification]

**Evidence:**
[Data, screenshots, logs, or other evidence]

---

## ANALYSIS

**Root Cause:**
[Why did this happen? What went wrong?]

**Was this:**
- [ ] Training data issue
- [ ] Model design issue
- [ ] Feature selection issue
- [ ] Deployment/operations issue
- [ ] Monitoring gap
- [ ] Human oversight failure
- [ ] Other: [Specify]

**Contributing Factors:**
1. [Factor]
2. [Factor]
3. [Factor]

**Fairness Metrics:**

| Metric | Affected Group | Reference Group | Difference | Threshold | Violation |
|--------|----------------|-----------------|------------|-----------|-----------|
| [Metric] | [Value] | [Value] | [Value] | [Value] | [Y/N] |

---

## IMMEDIATE RESPONSE (within 1 hour for Critical)

**Actions Taken:**
- [ ] Automated decision-making halted
- [ ] Switched to human review for affected cases
- [ ] Ethics board notified
- [ ] Leadership notified
- [ ] Legal counsel notified
- [ ] Logs preserved
- [ ] Public communication (if applicable)

**Time to Response:**
- Detection: [HH:MM]
- Initial response: [HH:MM]
- System paused (if applicable): [HH:MM]
- Elapsed time: [minutes]

---

## AFFECTED INDIVIDUALS

**Number of people affected:** [N]

**Time period:** [Start date] to [End date]

**Demographic breakdown:**
- [Group A]: [N] people
- [Group B]: [N] people

**Specific harms experienced:**
- [Type of harm]: [N] people
- [Type of harm]: [N] people

**Notification:**
- [ ] Affected individuals identified
- [ ] Notification plan developed
- [ ] Notifications sent: [Date]
- [ ] Method: [Email/Letter/Phone/Other]

**Remediation for Individuals:**
- [ ] Cases under review
- [ ] Decisions reversed: [N]
- [ ] Compensation provided: [Details]
- [ ] Other remediation: [Specify]

---

## REMEDIATION PLAN

### Immediate Actions (Within 24 hours)

1. [Action]
   - Owner: [Name]
   - Status: [Complete / In Progress]
   - Completion: [Date/Time]

### Short-Term Fixes (Within 1 week)

1. [Action]
   - Owner: [Name]
   - Deadline: [Date]
   - Status: [Status]

### Long-Term Improvements (Ongoing)

1. [Systemic improvement]
   - Owner: [Name]
   - Timeline: [Timeframe]
   - Success criteria: [How we'll know it worked]

---

## TESTING & VALIDATION

**Remediation tested:**
- [ ] Fix validated in test environment
- [ ] Fairness metrics recalculated
- [ ] Edge cases tested
- [ ] External review completed

**New fairness metrics:**

| Metric | Before Fix | After Fix | Threshold | Status |
|--------|------------|-----------|-----------|--------|
| [Metric] | [Value] | [Value] | [Value] | [Pass/Fail] |

**Approval to restore:**
- [ ] Technical validation
- [ ] Ethics board approval
- [ ] Legal approval
- [ ] System owner approval

**System restored:** [Date/Time]

---

## LESSONS LEARNED

**What went well:**
1. [Something that worked well in detection or response]
2. [Positive]

**What could be improved:**
1. [Area for improvement]
2. [Area for improvement]

**Systemic issues identified:**
1. [Broader issue this incident revealed]
2. [Issue]

**Process improvements:**
1. [How to prevent similar incidents]
   - Action: [Specific change]
   - Owner: [Name]
   - Deadline: [Date]

**Monitoring enhancements:**
1. [How to detect similar issues faster]
2. [Enhancement]

---

## FOLLOW-UP

**Effectiveness check:**
- 1 week: [Review fairness metrics, user feedback]
  - Owner: [Name]
  - Date: [Date]

- 1 month: [Comprehensive review]
  - Owner: [Name]
  - Date: [Date]

- 3 months: [Long-term impact assessment]
  - Owner: [Name]
  - Date: [Date]

---

## CLOSURE

**Incident closed:** [Date]

**Final status:**
- Technical fix: [Validated]
- Affected individuals: [Remediated]
- Process improvements: [Implemented]
- Monitoring enhanced: [Complete]
- Documentation: [Complete]

**Sign-off:**

Incident Lead: _________________ Date: _________

Ethics Board Chair: _________________ Date: _________

System Owner: _________________ Date: _________

---

**Attachments:**
- Evidence (logs, screenshots, data)
- Fairness metric calculations
- Communication templates used
- Remediation test results
- Updated monitoring procedures
```

---

## How to Use These Templates

1. **Choose the right template:**
   - Rapid Screen: Quick assessment, low-risk systems
   - Comprehensive: Detailed evaluation, moderate-high risk
   - Incident Report: When issues are detected

2. **Customize for your context:**
   - Add your organization's specific requirements
   - Adjust thresholds based on your risk tolerance
   - Add domain-specific sections (e.g., healthcare, finance)

3. **Don't skip sections:**
   - Every section exists for a reason
   - "Not applicable" is better than blank
   - Document why something doesn't apply

4. **Make it a living document:**
   - Update as system evolves
   - Version control your assessments
   - Regular reviews (at least annually)

5. **Get diverse input:**
   - Don't fill out alone
   - Involve affected communities
   - Include multiple disciplines (tech, ethics, legal, domain experts)

---

**Remember:** These templates are starting points. Adapt them to your specific context, regulatory requirements, and organizational needs. The goal is thorough ethical evaluation, not checkbox compliance.
