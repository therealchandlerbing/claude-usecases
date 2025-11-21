# Bias & Fairness Assessment

Comprehensive framework for identifying, measuring, and addressing bias in AI systems.

## Data Bias Audit

### Representation Analysis

**Training Data Demographics vs. Affected Population**
- What is the demographic breakdown of training data?
- What is the demographic breakdown of the affected population?
- Where are the gaps and mismatches?
- Which groups are underrepresented or missing entirely?

**Historical Bias Encoded in Training Data**
- Does historical data reflect past discrimination?
- Are historical inequities treated as ground truth?
- Does the data normalize unjust historical patterns?
- What structural inequities are baked into the data?

**Protected Class Distribution and Intersectionality**
- How are protected attributes distributed in training data?
- Are intersectional identities represented (e.g., Black women, elderly disabled persons)?
- Do subgroups have sufficient representation for meaningful analysis?
- Are there proxy variables that correlate with protected attributes?

**Missing Data Patterns by Demographic Group**
- Do certain groups have more missing or incomplete data?
- Are missingness patterns systematic or random?
- How are missing values imputed? Does this introduce bias?
- What assumptions underlie handling of missing data?

**Data Quality Disparities Across Groups**
- Is data quality consistent across demographic groups?
- Are certain groups' data noisier, older, or less accurate?
- Do measurement errors vary systematically?
- Are there differences in data collection methods by group?

### Labeling Bias Check

**Who Labeled the Training Data?**
- What is the demographic makeup of labelers?
- What is their expertise and training?
- What incentives and constraints did they face?
- Were they from the same communities as affected populations?

**What Assumptions Underlie the Labels?**
- What cultural norms and values are embedded in labels?
- Are subjective judgments framed as objective truth?
- What alternative labeling schemes are possible?
- Who decided what categories to use?

**Subjective Judgments as Objective Truth**
- Are labels truly objective or culturally situated?
- Do labels reflect dominant group perspectives?
- Could reasonable people disagree on labels?
- Are uncertainty and ambiguity acknowledged?

**Cultural Norms in Labels**
- Do labels reflect universal standards or specific cultural contexts?
- Are labels appropriate across all affected populations?
- Do labels disadvantage certain cultural practices or expressions?
- Is there cultural sensitivity in what's labeled positive/negative?

### Temporal Bias Evaluation

**How Old is the Training Data?**
- When was the training data collected?
- How much has the world changed since then?
- Are there secular trends not captured?
- Is there concept drift over time?

**Do Historical Patterns Reflect Current Reality?**
- Have social norms evolved since data collection?
- Have legal frameworks changed?
- Are historical patterns still valid?
- What has changed in the affected population?

**Does the Model Perpetuate Outdated Social Structures?**
- Does the system encode past discrimination into future predictions?
- Does it assume stability in social patterns?
- Could it prevent social progress by reinforcing status quo?
- Does it allow for social change and mobility?

## Model Behavior Testing

### Systematic Fairness Testing

Test AI system behavior across these critical dimensions:

**Race and Ethnicity**
- Major racial/ethnic groups relevant to deployment context
- Multiracial identities
- Ethnic subgroups within broader categories
- Indigenous populations

**Gender and Gender Identity**
- Men, women, non-binary individuals
- Transgender individuals
- Gender expression variations
- Intersections with other identities

**Age Groups**
- Children and adolescents
- Young adults
- Middle-aged adults
- Older adults and elderly
- Age transitions (e.g., aging out of services)

**Socioeconomic Status**
- Income levels
- Wealth and assets
- Educational attainment
- Occupation and employment status
- Housing stability

**Geographic Location**
- Urban vs. rural
- Regional differences
- Neighborhood characteristics
- Access to infrastructure and services
- State/provincial variations

**Language and Accent**
- Primary language
- English proficiency levels
- Dialect and accent variations
- Multilingual speakers
- Literacy levels

**Disability Status**
- Physical disabilities
- Sensory disabilities
- Cognitive and developmental disabilities
- Mental health conditions
- Chronic health conditions

**Immigration Status**
- Citizens vs. non-citizens
- Documented vs. undocumented
- Refugees and asylum seekers
- Length of time in country
- Language barriers

**Prior System Contact**
- Criminal justice system involvement
- Social services history
- Credit history
- Employment history
- Educational records

## Fairness Metrics Application

For each protected attribute, calculate appropriate fairness metrics. **Note: Perfect fairness across all metrics simultaneously is mathematically impossible. Choose metrics based on context and values.**

### Statistical Parity (Demographic Parity)

**Formula:** P(Ŷ=1 | A=a) = P(Ŷ=1 | A=b)

**Meaning:** Equal positive prediction rates across groups

**When to Use:**
- When equal opportunity/access is the primary goal
- In contexts where qualification differences may reflect historical bias
- For exploratory screening processes

**Limitations:**
- May require different accuracy across groups
- Doesn't account for base rate differences
- Can be inappropriate when true qualification rates differ legitimately

### Equalized Odds

**Formula:** P(Ŷ=1 | Y=y, A=a) = P(Ŷ=1 | Y=y, A=b) for y ∈ {0,1}

**Meaning:** Equal true positive AND false positive rates across groups

**When to Use:**
- When both errors (false positives and false negatives) matter equally
- In contexts requiring balanced error rates
- For classification with clear ground truth

**Limitations:**
- Very restrictive constraint
- May not be achievable with certain data distributions
- Doesn't consider which type of error is more harmful

### Equalized Opportunity

**Formula:** P(Ŷ=1 | Y=1, A=a) = P(Ŷ=1 | Y=1, A=b)

**Meaning:** Equal true positive rates (equal benefit when qualified)

**When to Use:**
- When false negatives are more harmful than false positives
- For opportunity allocation (hiring, admissions, loans)
- When you want to ensure qualified individuals have equal chances

**Limitations:**
- Allows different false positive rates
- May disadvantage groups with lower base rates
- Doesn't address disparate impact from false positives

### Predictive Parity (Precision Parity)

**Formula:** P(Y=1 | Ŷ=1, A=a) = P(Y=1 | Ŷ=1, A=b)

**Meaning:** Equal precision across groups (predictions equally accurate)

**When to Use:**
- When those who receive positive predictions should have equal success rates
- For resource allocation where false positives are costly
- When prediction calibration matters

**Limitations:**
- Incompatible with equalized odds when base rates differ
- May result in different selection rates
- Can disadvantage groups with lower base rates

### Calibration

**Formula:** P(Y=1 | Ŷ=p, A=a) = P(Y=1 | Ŷ=p, A=b) = p

**Meaning:** Predicted probabilities match actual outcomes across groups

**When to Use:**
- When probability estimates are used for decision-making
- For risk assessment tools
- When transparency about confidence is important

**Limitations:**
- Can be satisfied while having large fairness violations
- Doesn't ensure equal treatment or outcomes
- Can coexist with significant bias

### Choosing Fairness Metrics

**Decision Framework:**

1. **What type of harm matters most?**
   - False negatives (missed opportunities) → Equalized Opportunity
   - False positives (undeserved burden) → Predictive Parity focus
   - Both equally → Equalized Odds

2. **What is the decision context?**
   - Opportunity allocation → Statistical Parity or Equalized Opportunity
   - Risk assessment → Calibration + chosen error rate metric
   - Screening/filtering → Equalized Opportunity
   - Punitive decisions → Equalized Odds

3. **What are the base rates?**
   - Similar across groups → More metrics achievable
   - Different across groups → Choose most appropriate metric, accept others may not be satisfied

4. **What do affected communities want?**
   - Consult with impacted populations
   - Different groups may prioritize different fairness notions
   - Balance multiple perspectives

## Intersectional Analysis

**Why Intersectionality Matters:**
Bias is not simply additive. Being Black AND female is not just "Black bias" + "female bias" — there are unique biases at intersections.

**How to Test:**
1. Identify relevant intersections in your context
2. Test combinations of protected attributes:
   - Race × Gender
   - Age × Disability
   - Socioeconomic × Race
   - Immigration × Language
   - All relevant combinations

3. Look for:
   - **Compound marginalization**: Multiple identities creating unique disadvantage
   - **Bias amplification**: Intersections experiencing worse outcomes than either identity alone
   - **Erasure**: Intersectional groups absent from training data or analysis

**Example Intersections to Test:**
- Black women vs. Black men vs. white women vs. white men
- Elderly disabled individuals vs. young disabled vs. elderly non-disabled
- Low-income immigrants vs. middle-class immigrants vs. low-income citizens
- LGBTQ+ people of color vs. white LGBTQ+ vs. straight people of color

## Edge Case & Adversarial Testing

**Unusual but Realistic Scenarios**
- Rare but legitimate cases
- Boundary conditions
- Outliers in feature space
- Atypical but valid data patterns

**Adversarial Inputs Designed to Expose Bias**
- Deliberately craft inputs to test bias
- Minimal changes that flip outcomes
- Probing for proxies and correlations
- Testing robustness to identity variations

**Stress Testing with Corner Cases**
- Extreme values
- Missing data
- Incomplete information
- Ambiguous cases

**Worst-Case Impact Scenarios**
- Most vulnerable populations
- Highest stakes decisions
- Cascading failures
- Systemic implications

## Outcome Fairness Evaluation

### Allocative Harm Assessment

**Question:** Does the system distribute opportunities, resources, or benefits inequitably?

**Look for:**
- Different approval/selection rates across groups
- Disparate access to positive outcomes
- Unequal resource distribution
- Opportunity gaps

**Examples:**
- Loan approval rates differ by race
- Job candidates screened out at different rates by gender
- Healthcare resources allocated unequally by age

### Representational Harm Assessment

**Question:** Does the system reinforce stereotypes or demean certain groups?

**Look for:**
- Stereotypical associations
- Demeaning or offensive outputs
- Erasure or invisibility of certain groups
- Misrepresentation or caricature

**Examples:**
- Image search results reinforcing gender stereotypes
- Language models associating certain groups with negative attributes
- Facial recognition failing to recognize certain ethnic groups

### Quality-of-Service Disparity

**Question:** Does system performance vary significantly across demographic groups?

**Look for:**
- Different accuracy rates by group
- Longer response times for certain users
- Lower quality outputs for some populations
- Unequal error rates

**Examples:**
- Voice recognition worse for accented speakers
- Facial recognition less accurate for darker skin tones
- Chatbots providing lower quality responses in certain languages

### Feedback Loop Analysis

**Question:** Could system outputs create self-fulfilling prophecies or compounding disadvantage?

**Look for:**
- Model predictions influencing future reality
- Historical bias amplified over time
- Compounding disadvantage for already marginalized groups
- Barriers to social mobility

**Examples:**
- Predictive policing concentrating enforcement in certain neighborhoods, generating more data from those areas, reinforcing the prediction
- Credit scoring denying opportunities, making it harder to build credit, perpetuating low scores
- Hiring algorithms trained on historical data replicating past discrimination

**Intervention:** Design feedback mechanisms that don't reinforce bias, monitor for self-fulfilling prophecies, implement circuit breakers when loops detected.

## Bias Assessment Output Template

```
BIAS & FAIRNESS ASSESSMENT SUMMARY

DATA BIAS FINDINGS
□ Representation Gaps: [Key findings]
□ Historical Bias: [Issues identified]
□ Labeling Bias: [Concerns]
□ Temporal Bias: [Relevance of historical data]

FAIRNESS METRICS RESULTS
Protected Attribute: [Race / Gender / Age / etc.]
- Statistical Parity Difference: [Value] (Threshold: 0.1)
- Equalized Odds Difference: [Value] (Threshold: 0.1)
- Equal Opportunity Difference: [Value] (Threshold: 0.1)
- Disparate Impact Ratio: [Value] (Threshold: 0.8)

[Repeat for each protected attribute]

INTERSECTIONAL FINDINGS
Most Disadvantaged Groups: [List intersectional identities with worst outcomes]
Compound Marginalization: [Description]

HARM ASSESSMENT
Allocative Harm: [Yes/No] - [Description]
Representational Harm: [Yes/No] - [Description]
Quality-of-Service Disparity: [Yes/No] - [Description]
Feedback Loop Risk: [Yes/No] - [Description]

BIAS SEVERITY: [Low / Medium / High / Critical]

MITIGATION REQUIRED
1. [Most critical bias issue to address]
2. [Second priority]
3. [Third priority]

RECOMMENDED FAIRNESS METRIC FOR DEPLOYMENT
Primary Metric: [Chosen metric based on context]
Rationale: [Why this metric is most appropriate]
Monitoring: [How to track this metric ongoing]
```
