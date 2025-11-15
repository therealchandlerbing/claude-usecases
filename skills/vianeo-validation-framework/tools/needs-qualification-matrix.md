# Needs Qualification Matrix Tool

**Purpose:** Systematically evaluate the importance and current satisfaction level of each identified need across different requester segments. This tool helps prioritize opportunities by identifying high-importance, low-satisfaction needs.

**Framework Alignment:** Supports Vianeo Desirability dimension assessment

---

## Table of Contents

1. [Overview](#overview)
2. [Matrix Structure](#matrix-structure)
3. [Rating Scales](#rating-scales)
4. [How to Use This Tool](#how-to-use-this-tool)
5. [Output Format](#output-format)
6. [Interpretation Guide](#interpretation-guide)
7. [Examples](#examples)
8. [Integration with Vianeo Framework](#integration-with-vianeo-framework)

---

## Overview

### What is the Needs Qualification Matrix?

The Needs Qualification Matrix is a systematic tool for evaluating each identified need against two dimensions:

1. **Importance:** How critical is this need for the requester segment?
2. **Satisfaction:** How well are current solutions meeting this need?

By plotting needs on these two dimensions across different requester segments, you can:
- Identify priority opportunities (high importance, low satisfaction)
- Discover needs that vary significantly across segments
- Find segments with the most critical unmet needs
- Validate where current solutions are adequate (avoid building what's not needed)

---

### When to Use This Tool

**Use the Needs Qualification Matrix when:**
- Prioritizing which needs to address first
- Deciding which customer segments to target
- Validating assumptions about need importance
- Assessing competitive landscape (satisfaction = how well competitors serve the need)
- Preparing Vianeo Desirability dimension documentation
- Supporting scoring for 29-Question Market Maturity Assessment (especially Q2, Q7, Q28)

**This tool is especially valuable for:**
- Multi-segment markets (different customer types)
- Competitive markets (understanding where current solutions fall short)
- Strategic planning (where to focus development resources)
- Investor presentations (demonstrating market opportunity with data)

---

## Matrix Structure

### Two-Dimensional Assessment

For each **Need × Requester Segment** combination, determine:

| Dimension | Rating Scale | Purpose |
|-----------|-------------|---------|
| **Importance** | Fundamental / Important / Secondary / None / Don't know | How critical is this need? |
| **Satisfaction** | Very well / Pretty much / Rather not / Not at all / Don't know | How well do current solutions meet this need? |

---

### Matrix Layout

The matrix is organized as a table with:
- **Rows:** Individual needs
- **Columns:** Requester segments
- **Cells:** Importance (I) and Satisfaction (S) ratings

**Example Structure:**

|  | **Segment 1** | **Segment 2** | **Segment 3** |
|--|---------------|---------------|---------------|
| **Need 1** | I: [level]<br>S: [level] | I: [level]<br>S: [level] | I: [level]<br>S: [level] |
| **Need 2** | I: [level]<br>S: [level] | I: [level]<br>S: [level] | I: [level]<br>S: [level] |
| **Need 3** | I: [level]<br>S: [level] | I: [level]<br>S: [level] | I: [level]<br>S: [level] |

---

## Rating Scales

### Importance Rating Scale

**Fundamental:**
- Absolutely critical to the requester's core function or goal
- Without addressing this need, the requester cannot function effectively
- Highest priority, urgent need
- Example: "For a senior living activities director, objectively tracking cognitive decline is fundamental to their medical reporting responsibilities"

**Important:**
- Significant need that improves effectiveness or outcomes
- Requester can function without it, but with difficulty or suboptimal results
- High priority, but not mission-critical
- Example: "For caregivers, receiving alerts about cognitive changes is important for early intervention but they can manage without automated alerts"

**Secondary:**
- Nice-to-have need that adds convenience or incremental value
- Requester can function adequately without addressing this need
- Lower priority, enhancement rather than necessity
- Example: "For family members, accessing historical cognitive data is secondary—they primarily care about current status and recent trends"

**None:**
- Not a need for this requester segment
- This segment does not experience or care about this need
- Example: "For medical directors, gamification features are not a need—they care about clinical validity, not engagement mechanics"

**Don't know:**
- Insufficient data to assess importance
- Requires validation research
- Example: "We haven't interviewed this segment yet to understand if this is a fundamental, important, or secondary need for them"

---

### Satisfaction Rating Scale

**Very well:**
- Current solutions address this need comprehensively
- Requester is satisfied with existing options
- Little to no room for improvement
- Low opportunity for new solution
- Example: "Electronic health records very well satisfy the need for long-term data storage—robust, compliant solutions exist"

**Pretty much:**
- Current solutions address the need adequately with minor gaps
- Requester is generally satisfied but sees room for improvement
- Moderate opportunity for better solution
- Example: "Paper-based cognitive games pretty much satisfy the need for brain stimulation, but lack tracking and personalization"

**Rather not:**
- Current solutions partially address the need but have significant limitations
- Requester is dissatisfied with existing options
- Strong opportunity for improved solution
- Example: "Manual observation rather not satisfies the need for objective cognitive tracking—subjective, inconsistent, not longitudinal"

**Not at all:**
- Current solutions do not address this need
- Major gap in the market
- Highest opportunity for new solution
- Example: "No current solution provides automated family alerts about cognitive changes—this need is not at all satisfied"

**Don't know:**
- Insufficient data on current solution satisfaction
- Requires competitive analysis or customer research
- Example: "We haven't asked customers how satisfied they are with current solutions for this specific need"

---

## How to Use This Tool

### Step 1: Identify Needs

List all validated needs you've identified through research.

**Format:** Each need as a clear, concise statement (ideally 60 characters or fewer for Vianeo platform compatibility)

**Example Needs:**
1. Track cognitive decline objectively over time
2. Access clinical-grade tools without facility visits
3. Detect early warning signs before formal diagnosis
4. Monitor daily without specialized training required
5. Share objective data with healthcare providers easily

**Guidance:**
- Use distinct needs (not overlapping)
- Base needs on customer research (validated, not assumed)
- See [Sprint Execution Guide - Needs Statements](../references/sprint-execution-guide.md#needs-statements) for avoiding pitfalls

---

### Step 2: Identify Requester Segments

List all relevant requester (customer) segments.

**Format:** Specific segment names based on personas

**Example Segments:**
1. Senior Living Activities Directors
2. Family Caregivers (Adult Children of Seniors)
3. Medical Directors at Senior Communities
4. Geriatric Neurologists
5. Home Health Agencies

**Guidance:**
- Use specific segments, not generic labels
- Base segments on validated personas
- See [Vianeo Persona Builder](../../vianeo-persona-builder/README.md) for persona development

---

### Step 3: Complete the Matrix

For each **Need × Segment** combination:

1. **Assess Importance:**
   - Ask: "How critical is this need for this segment?"
   - Rate: Fundamental / Important / Secondary / None / Don't know
   - Document evidence: Interview quotes, survey data, behavioral observation

2. **Assess Satisfaction:**
   - Ask: "How well do current solutions meet this need for this segment?"
   - Rate: Very well / Pretty much / Rather not / Not at all / Don't know
   - Document evidence: Customer feedback on current solutions, competitive analysis, pain point data

3. **Record in Matrix:**
   - Cell format: `I: [Importance]` / `S: [Satisfaction]`

---

### Step 4: Analyze Results

**Look for:**

1. **Priority Opportunities:**
   - High Importance + Low Satisfaction = Prime target
   - Example: I: Fundamental, S: Not at all

2. **Segment Differences:**
   - Same need rated very differently across segments
   - Indicates need for segment-specific positioning or features

3. **Low-Hanging Fruit:**
   - Important needs with "Rather not" satisfaction
   - Current solutions exist but are inadequate

4. **Avoid Traps:**
   - Needs with "Very well" satisfaction = crowded market, low opportunity
   - Needs with "None" or "Secondary" importance = not worth pursuing

---

## Output Format

### Standard Matrix Table

|  | **Activities Director** | **Family Caregiver** | **Medical Director** |
|--|-------------------------|----------------------|----------------------|
| **Track cognitive decline objectively** | I: Fundamental<br>S: Not at all | I: Important<br>S: Rather not | I: Fundamental<br>S: Pretty much |
| **Access clinical-grade tools at home** | I: Important<br>S: Rather not | I: Fundamental<br>S: Not at all | I: Secondary<br>S: Very well |
| **Detect early warning signs** | I: Fundamental<br>S: Not at all | I: Fundamental<br>S: Not at all | I: Fundamental<br>S: Pretty much |
| **Monitor daily without training** | I: Important<br>S: Not at all | I: Fundamental<br>S: Not at all | I: None<br>S: N/A |
| **Share data with providers easily** | I: Fundamental<br>S: Rather not | I: Important<br>S: Rather not | I: Important<br>S: Pretty much |

---

### Priority Matrix Visualization

**High Priority Opportunities (Importance: Fundamental or Important, Satisfaction: Not at all or Rather not):**

| Need | Segment | Importance | Satisfaction | Priority Level |
|------|---------|------------|--------------|----------------|
| Track cognitive decline objectively | Activities Director | Fundamental | Not at all | **CRITICAL** |
| Detect early warning signs | Activities Director | Fundamental | Not at all | **CRITICAL** |
| Access clinical-grade tools at home | Family Caregiver | Fundamental | Not at all | **CRITICAL** |
| Monitor daily without training | Family Caregiver | Fundamental | Not at all | **CRITICAL** |
| Detect early warning signs | Family Caregiver | Fundamental | Not at all | **CRITICAL** |

---

**Medium Priority (Importance: Important or Fundamental, Satisfaction: Pretty much or Rather not):**

| Need | Segment | Importance | Satisfaction | Priority Level |
|------|---------|------------|--------------|----------------|
| Track cognitive decline objectively | Medical Director | Fundamental | Pretty much | **MEDIUM** |
| Access clinical-grade tools at home | Activities Director | Important | Rather not | **MEDIUM** |
| Share data with providers easily | Activities Director | Fundamental | Rather not | **MEDIUM** |

---

**Low Priority (Importance: Secondary or None, any Satisfaction):**

| Need | Segment | Importance | Satisfaction | Priority Level |
|------|---------|------------|--------------|----------------|
| Access clinical-grade tools at home | Medical Director | Secondary | Very well | **LOW** |
| Monitor daily without training | Medical Director | None | N/A | **LOW** |

---

## Interpretation Guide

### Priority Levels

#### CRITICAL Priority (Address First)
**Criteria:**
- Importance: Fundamental or Important
- Satisfaction: Not at all or Rather not
- Segment: High-value target segment

**Interpretation:**
- Major unmet need in the market
- Highest opportunity for new solution
- Should be core focus of product/service

**Strategic Action:**
- Build MVP features addressing these needs
- Target segments with multiple CRITICAL needs
- Validate willingness-to-pay for solutions to these needs

---

#### MEDIUM Priority (Address Second)
**Criteria:**
- Importance: Fundamental or Important
- Satisfaction: Pretty much
- OR: Importance: Important, Satisfaction: Rather not (for lower-priority segments)

**Interpretation:**
- Current solutions exist but have room for improvement
- Opportunity for better solution, but competitors present
- May be differentiators rather than core features

**Strategic Action:**
- Identify specific gaps in current solutions
- Develop competitive differentiation strategy
- Consider these for v2 features or premium tiers

---

#### LOW Priority (Deprioritize or Avoid)
**Criteria:**
- Importance: Secondary or None (any satisfaction)
- OR: Satisfaction: Very well (any importance)

**Interpretation:**
- Not a strong market need, or already well-served
- Low opportunity for new solution
- Risk of building features customers don't need

**Strategic Action:**
- Avoid investing development resources here
- If must include, keep lightweight and simple
- Consider dropping from scope entirely

---

### Segment-Level Analysis

#### Segment Prioritization

**Best Target Segments:**
- Multiple needs rated I: Fundamental or Important
- Multiple needs rated S: Not at all or Rather not
- High concentration of CRITICAL priority needs

**Example:**
- **Family Caregivers:** 3 CRITICAL needs, 1 MEDIUM → **Priority Segment #1**
- **Activities Directors:** 3 CRITICAL needs, 1 MEDIUM → **Priority Segment #1**
- **Medical Directors:** 1 CRITICAL need, 2 MEDIUM → **Secondary Segment**

---

#### Need Variation Across Segments

**Look for needs where importance or satisfaction varies significantly across segments:**

**Example:**
- **"Monitor daily without training"**
  - Activities Director: I: Important
  - Family Caregiver: I: Fundamental
  - Medical Director: I: None

**Interpretation:**
- This need is critical for some segments (caregivers) but irrelevant for others (medical directors)
- Feature should be designed for caregiver segment, not medical director

**Strategic Implications:**
- Tailor positioning and messaging by segment
- Design features for specific segment needs
- Avoid one-size-fits-all approach

---

### Portfolio View

**Balanced Portfolio:**
- 3-5 CRITICAL needs across 2-3 priority segments
- 3-5 MEDIUM needs for differentiation
- Minimal or no LOW priority needs

**Risky Portfolio:**
- Many LOW priority needs (building things customers don't need)
- Only MEDIUM needs (entering crowded market with no clear advantage)
- CRITICAL needs concentrated in one segment only (single point of failure)

---

## Examples

### Example 1: Senior Cognitive Monitoring Solution

**Needs Identified:**
1. Track cognitive decline objectively over time
2. Access clinical-grade tools without facility visits
3. Detect early warning signs before formal diagnosis
4. Monitor daily without specialized training required
5. Share objective data with healthcare providers easily

**Requester Segments:**
1. Senior Living Activities Directors
2. Family Caregivers (Adult Children)
3. Medical Directors at Senior Communities

---

**Complete Matrix:**

|  | **Activities Director** | **Family Caregiver** | **Medical Director** |
|--|-------------------------|----------------------|----------------------|
| **Track cognitive decline objectively** | I: Fundamental<br>S: Not at all | I: Important<br>S: Rather not | I: Fundamental<br>S: Pretty much |
| **Access clinical-grade tools at home** | I: Important<br>S: Rather not | I: Fundamental<br>S: Not at all | I: Secondary<br>S: Very well |
| **Detect early warning signs** | I: Fundamental<br>S: Not at all | I: Fundamental<br>S: Not at all | I: Fundamental<br>S: Pretty much |
| **Monitor daily without training** | I: Important<br>S: Not at all | I: Fundamental<br>S: Not at all | I: None<br>S: N/A |
| **Share data with providers easily** | I: Fundamental<br>S: Rather not | I: Important<br>S: Rather not | I: Important<br>S: Pretty much |

---

**Analysis:**

**CRITICAL Priority Needs:**
1. **Track cognitive decline objectively** (Activities Director)
2. **Detect early warning signs** (Activities Director)
3. **Monitor daily without training** (Activities Director)
4. **Access clinical-grade tools at home** (Family Caregiver)
5. **Detect early warning signs** (Family Caregiver)
6. **Monitor daily without training** (Family Caregiver)

**Priority Segments:**
1. **Family Caregivers:** 3 CRITICAL, 2 MEDIUM
2. **Activities Directors:** 3 CRITICAL, 1 MEDIUM
3. **Medical Directors:** 0 CRITICAL, 3 MEDIUM (secondary target)

**Strategic Insights:**
- Focus MVP on **Activities Directors** and **Family Caregivers**
- Core features must address: objective tracking, early detection, ease of use (no training required)
- Medical Directors are secondary segment—existing solutions adequately serve their needs
- "Monitor daily without training" is critical for primary segments but irrelevant for medical directors → design for non-expert users

---

### Example 2: Rural STEM Education Platform

**Needs Identified:**
1. Access hands-on lab experiences remotely
2. Receive real-time expert guidance during experiments
3. Track student progress with limited teacher time
4. Provide personalized learning paths
5. Meet state science standards

**Requester Segments:**
1. Rural Science Teachers
2. School District Administrators
3. Students (ages 14-18)

---

**Complete Matrix:**

|  | **Rural Science Teacher** | **District Administrator** | **Student (age 14-18)** |
|--|---------------------------|----------------------------|-------------------------|
| **Access hands-on lab experiences** | I: Fundamental<br>S: Not at all | I: Important<br>S: Rather not | I: Fundamental<br>S: Not at all |
| **Receive real-time expert guidance** | I: Important<br>S: Not at all | I: Secondary<br>S: Pretty much | I: Fundamental<br>S: Rather not |
| **Track student progress efficiently** | I: Fundamental<br>S: Rather not | I: Fundamental<br>S: Rather not | I: None<br>S: N/A |
| **Provide personalized learning paths** | I: Important<br>S: Rather not | I: Important<br>S: Rather not | I: Important<br>S: Rather not |
| **Meet state science standards** | I: Fundamental<br>S: Pretty much | I: Fundamental<br>S: Pretty much | I: None<br>S: N/A |

---

**Analysis:**

**CRITICAL Priority Needs:**
1. **Access hands-on lab experiences** (Teacher)
2. **Receive real-time expert guidance** (Teacher)
3. **Access hands-on lab experiences** (Student)
4. **Receive real-time expert guidance** (Student) - borderline (I: Fundamental, S: Rather not)

**Priority Segments:**
1. **Students:** 2 CRITICAL needs (hands-on access + expert guidance)
2. **Teachers:** 2 CRITICAL needs (hands-on access + expert guidance)
3. **Administrators:** 0 CRITICAL, 2 MEDIUM (buyer but not primary user)

**Strategic Insights:**
- **Core MVP:** Remote lab access + real-time expert guidance
- **Target Users:** Students and teachers (end users), but administrators are buyers
- **Note:** "Meet state standards" is Fundamental for teacher/admin, but satisfaction is "Pretty much" → current solutions exist, so this is table stakes, not differentiator
- **Positioning:** Sell to administrators (budget holders) based on student/teacher needs, not admin-specific needs

---

## Integration with Vianeo Framework

### Supporting Vianeo Desirability Assessment

The Needs Qualification Matrix directly supports several questions in the **29-Question Market Maturity Assessment**:

**Q2:** "You have identified people with strong needs AND who are looking for solutions to better meet their needs."
- **Evidence:** Matrix cells showing I: Fundamental + S: Not at all or Rather not
- **Strong validation:** Multiple segments with CRITICAL needs identified

**Q7:** "You have checked through direct interviews, with at least 5 people with the same profile, that they express needs."
- **Evidence:** Matrix based on interview data (note interview count per segment)
- **Strong validation:** Matrix reflects 5-10+ interviews per segment

**Q28:** "You are able to prioritise people according to their expectation for a new solutions, those who express strong and very poorly met needs."
- **Evidence:** Priority Matrix showing CRITICAL, MEDIUM, LOW categorization
- **Strong validation:** Clear prioritization with rationale based on importance × satisfaction

---

### Scoring Guidance Using Matrix Results

**For 29-Question Assessment:**

**Score 5 (Absolutely) - Strong matrix evidence:**
- Matrix completed for 3+ segments
- Based on 10+ interviews per segment
- Multiple CRITICAL needs identified with validation
- Clear prioritization with documented rationale

**Score 4 (Rather) - Good matrix evidence:**
- Matrix completed for 2-3 segments
- Based on 5-9 interviews per segment
- Several CRITICAL needs identified
- Prioritization documented

**Score 3 (Rather not) - Preliminary matrix:**
- Matrix completed for 1-2 segments
- Based on 3-4 interviews per segment
- Some needs identified but limited validation
- Basic prioritization

**Score 2 (Not at all) - Weak or assumed matrix:**
- Matrix based on assumptions, not interviews
- 0-2 interviews
- Needs not validated
- No clear prioritization

**Score 1 (Don't know) - No matrix:**
- Needs not identified
- Segments not defined
- No prioritization work done

---

### Usage Workflow

**Step 1: Research**
- Conduct customer interviews (5-10 per segment)
- Ask about needs, current solutions, pain points
- Validate importance and satisfaction directly

**Step 2: Complete Matrix**
- List all validated needs
- Identify requester segments
- Rate importance and satisfaction for each cell
- Document evidence sources

**Step 3: Analyze**
- Identify CRITICAL, MEDIUM, LOW priorities
- Prioritize segments
- Determine strategic focus

**Step 4: Integrate with Vianeo**
- Use matrix as evidence for 29-Question Assessment
- Document findings in platform (within character limits)
- Support Desirability dimension scoring

**Step 5: Product Strategy**
- Build MVP addressing CRITICAL needs
- Target priority segments
- Develop competitive differentiation for MEDIUM needs
- Avoid LOW priority needs

---

## Templates and Tools

### Blank Matrix Template

**Copy and complete:**

|  | **Segment 1: [Name]** | **Segment 2: [Name]** | **Segment 3: [Name]** |
|--|-----------------------|-----------------------|-----------------------|
| **Need 1: [Statement]** | I: <br>S: | I: <br>S: | I: <br>S: |
| **Need 2: [Statement]** | I: <br>S: | I: <br>S: | I: <br>S: |
| **Need 3: [Statement]** | I: <br>S: | I: <br>S: | I: <br>S: |
| **Need 4: [Statement]** | I: <br>S: | I: <br>S: | I: <br>S: |
| **Need 5: [Statement]** | I: <br>S: | I: <br>S: | I: <br>S: |

**Rating Options:**
- **Importance:** Fundamental / Important / Secondary / None / Don't know
- **Satisfaction:** Very well / Pretty much / Rather not / Not at all / Don't know

---

### Interview Questions to Complete Matrix

**To Assess Importance:**
- "On a scale from 'not important at all' to 'absolutely critical,' how important is [need] to you?"
- "What would happen if you couldn't address [need]?"
- "How often does [need] come up in your work/life?"
- "If you had to rank these needs from 1-5, which would be #1?"

**To Assess Satisfaction:**
- "What do you currently use to address [need]?"
- "How satisfied are you with that solution?"
- "What's missing or frustrating about your current approach?"
- "On a scale from 'completely satisfied' to 'not satisfied at all,' how well does [current solution] work?"

---

## Best Practices

### Do's

✅ **Base ratings on customer research**, not assumptions
✅ **Document evidence** for each cell (interview quotes, survey data)
✅ **Use specific segment names** based on validated personas
✅ **Ensure needs are distinct** (not overlapping)
✅ **Validate importance AND satisfaction** separately (both dimensions matter)
✅ **Focus on CRITICAL priorities** for MVP
✅ **Revisit matrix quarterly** as you learn more

### Don'ts

❌ **Don't guess** importance or satisfaction without evidence
❌ **Don't use generic segments** ("consumers," "businesses")
❌ **Don't include overlapping needs** (wastes matrix space)
❌ **Don't ignore LOW priorities** (knowing what NOT to build is valuable)
❌ **Don't treat all CRITICAL needs equally** (prioritize by segment value)
❌ **Don't complete matrix once and forget** (update as you validate)

---

## Related Resources

### Within Vianeo Validation Framework:
- [29-Question Market Maturity Assessment](../references/29-question-market-maturity-assessment.md) - Use matrix to support Desirability scoring
- [Sprint Execution Guide](../references/sprint-execution-guide.md) - Avoid pitfalls in needs statements
- [Platform Character Limits](../references/platform-character-limits.md) - Format needs within 60-character limit

### Related Skills:
- [Vianeo Persona Builder](../../vianeo-persona-builder/README.md) - Generate validated requester personas
- [Vianeo Persona Builder - Interview Questions](../../vianeo-persona-builder/references/interview-question-templates.md) - Ask the right questions to assess importance and satisfaction

---

**Document Version:** 1.0
**Last Updated:** November 2025
**Part of:** Vianeo Business Validation Framework
**Tool Type:** Needs Prioritization and Analysis
