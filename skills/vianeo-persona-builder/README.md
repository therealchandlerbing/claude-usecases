# Vianeo Persona Builder

**Category:** Research & Validation
**Purpose:** Generate validated stakeholder personas from research data and behavioral patterns
**Framework:** Vianeo Business Validation (Desirability Assessment)

## Description

The Vianeo Persona Builder analyzes research data, interview transcripts, behavioral patterns, and organizational context to create validated stakeholder personas following the Vianeo framework structure. This skill produces evidence-backed personas across four types (partners, innovators, stakeholders, beneficiaries) with dual outputs: a detailed strategic version for internal use and a platform-ready version formatted for Vianeo system entry.

Unlike generic persona tools, this skill enforces the Vianeo four-layer structure, tracks validation evidence, flags quality gaps, and provides scoring guidance aligned with the Vianeo Desirability rubric.

## Use Case

**Primary Use Cases:**
- Building personas for technology validation projects
- Documenting stakeholder needs for partnership development
- Creating evidence-backed user profiles for innovation assessments
- Preparing Desirability dimension documentation for Vianeo submissions
- Validating assumed needs against actual behavioral data

**When to Use:**
- "Build Vianeo personas from this research data"
- "Create stakeholder personas for [project/partnership]"
- "Analyze these interviews and generate validated personas"
- "I need personas in Vianeo format for [context]"

**When NOT to Use:**
- For quick stakeholder summaries (use direct analysis instead)
- When no research data or behavioral context exists (generates low-quality inferred personas)
- For persona types outside the four supported categories

## Prerequisites

### Required Context
At minimum, provide one of these:
- Interview transcripts or survey responses
- Meeting notes or observation documents
- User research reports or case studies
- Uploaded research files via document attachment

### Optional Enhancements
The skill can optionally integrate with:
- **Google Drive** - Research documents, meeting notes, project documentation
- **Gmail** - Communication patterns, engagement analysis, pain point identification
- **Asana** - Project engagement patterns, completion behaviors, collaboration dynamics
- **Google Calendar** - Meeting frequency, stakeholder identification, engagement patterns

All integrations are optional and suggested contextually based on persona type.

## Instructions

### Step 1: Prepare Your Data

**Gather Research Materials:**
- Collect interview transcripts, survey responses, or research reports
- Organize meeting notes or observation documents
- Prepare any behavioral data or project documentation
- Note the persona type(s) needed: partners, innovators, stakeholders, or beneficiaries

**Determine Validation Mode:**
- **Validated Mode**: You have direct stakeholder feedback (interviews, surveys)
- **Inferred Mode**: You have behavioral data or secondary sources only
- **Hybrid Mode**: You have both types of data

### Step 2: Invoke the Skill

**Provide Context:**
Share your data with clear context:
- "Build Vianeo personas from these [X] interviews about [topic]"
- "Create [persona type] personas for [project/partnership]"
- Specify persona type if not obvious from data
- Indicate if tool integration searches would be helpful

**Example Invocations:**
```
"I have 8 partner interview transcripts. Build Vianeo partner personas from this data and show me both the strategic and platform-ready versions."

"Create innovator personas based on these validation reports. Also search our Drive for related support interactions."

"Analyze these stakeholder meeting notes and generate Vianeo personas. Mark which parts are validated vs. inferred."
```

### Step 3: Review Initial Analysis

The skill will:
1. Analyze all provided sources
2. Detect persona type(s) and count
3. Assess validation mode (validated/inferred/hybrid)
4. Identify natural persona segments (recommends 3-5 personas)
5. Suggest optional tool searches if relevant

**You'll receive:**
- Summary of data sources analyzed
- Recommended persona count
- Validation mode determination
- Optional integration suggestions (approve or skip)

### Step 4: Persona Generation

The skill generates both standard outputs:

**Output 1: Full Strategic Version**
- Complete Vianeo four-layer format
- Rich detail (2-3 sentences per field, 4-6 bullets per list)
- Evidence tracking and source attribution
- Validation status markers
- Quality assessment and scoring guidance

**Output 2: Platform-Ready Version**
- Condensed, constraint-compliant format
- Exact Vianeo platform requirements
- 2-3 sentences per text field (strictly enforced)
- 4-6 bullets per list
- Character count verification
- Copy-paste ready structure

### Step 5: Review Quality Assessment

Each output includes:
- **Predicted Vianeo Score** (1-5 scale) with justification
- **Strength Analysis** - What's working well
- **Gap Analysis** - What needs improvement
- **Distinctiveness Check** - Persona overlap warnings
- **Evidence Summary** - Interview counts, quote availability
- **Recommendations** - Specific improvements for higher scores

**Quality Indicators to Check:**
- Interview/source count per persona (5-10 = strong, 3-5 = adequate, <3 = weak)
- Direct quote availability
- Behavioral observation specificity
- Current solution documentation
- Persona distinctiveness (no significant overlap)

### Step 6: Iterate if Needed

**Request Refinements:**
- "Add more specificity to the pain points for Persona 2"
- "Strengthen the evidence for the innovator personas"
- "Make Personas 3 and 4 more distinct from each other"
- "Combine Personas 3 and 4, they're too similar"

**Add New Data:**
- "Here are 3 more interviews, update the personas with this validation data"
- "I found additional research, incorporate these insights"

**Request Additional Outputs:**
- "Create an interactive artifact for these personas" (for presentation/collaboration)
- "Generate a comparison matrix across personas"
- "Map these to our Innovation Compass dimensions"

### Step 7: Deploy Personas

**For Vianeo Submission:**
- Use platform-ready version for data entry
- Keep full strategic version for scoring defense
- Target score 4+ for competitive submissions
- Address flagged gaps before submission

**For Internal Use:**
- Share full strategic version with team
- Review collaboratively to validate accuracy
- Reference personas in decision-making
- Update as understanding improves

**For Stakeholder Presentation:**
- Request interactive artifact if needed
- Use visual comparisons for clarity
- Emphasize evidence-backed insights
- Show validation methodology

## Expected Outputs

### Output 1: Full Strategic Version

**Format:** Detailed prose document (Markdown or Word)
**Purpose:** Internal strategy, team alignment, decision-making

**Sections:**
1. **Executive Summary**
   - Number of personas identified
   - Data sources analyzed
   - Overall validation status
   - Key patterns across personas

2. **Individual Personas** (each includes all four Vianeo layers)
   - Layer 1: Requester (Who They Are)
   - Layer 2: Field of Application (Their World)
   - Layer 3: Activities and Challenges (What They Do and Struggle With)
   - Layer 4: Current Solutions (Their Present Reality)
   - Evidence annotations and source attribution
   - Validation markers

3. **Evidence Appendix**
   - Quote origins and context
   - Interview count per persona
   - Source document references
   - Pattern frequency notes

4. **Quality Assessment**
   - Predicted Vianeo score (1-5 scale)
   - Strength and gap analysis
   - Persona distinctiveness check
   - Recommendations for improvement

### Output 2: Platform-Ready Version

**Format:** Condensed, constraint-compliant document (Word or Markdown)
**Purpose:** Direct entry into Vianeo platform

**Features:**
- All Vianeo format constraints applied
- Character count verification (need statements under 60 chars)
- Clean formatting, copy-paste ready
- Validation badges and evidence counts
- Quick reference with key quotes
- Platform-ready formatting

**Visual Indicators:**
- Character counts on need statements (e.g., "45/60 chars")
- Validation status badges
- Format compliance checks

### Output 3: Interactive Artifact (Optional - Must Be Requested)

**When to Request:**
- After standard outputs reviewed
- For sharing/presenting personas
- For collaborative exploration

**Features:**
- Toggle between personas
- View evidence sources
- Filter by validation status
- Export selected personas
- Compare persona attributes
- View quote context

## Persona Types Supported

### 1. Partner Personas
**Organizations, institutions, universities, or corporations you collaborate with**

**Typical Data Sources:**
- Partnership agreements and project scopes
- Meeting notes and collaboration history
- Email communication patterns
- Project engagement patterns

**Key Insights Generated:**
- Decision-making speed and hierarchy
- Communication preferences and relationship temperature
- Collaboration friction points and success patterns
- Cultural and geographic considerations

### 2. Innovator Personas
**Researchers, inventors, entrepreneurs, or technology creators you're validating**

**Typical Data Sources:**
- Validation reports and technology descriptions
- Support interactions and questions asked
- Engagement with validation processes
- Project timeline and milestone patterns

**Key Insights Generated:**
- Technology maturity and readiness
- Support needs and communication style
- Engagement patterns and completion behaviors
- Resource gaps and capability needs

### 3. Stakeholder Personas
**Funders, tech transfer offices, ecosystem players, or decision-makers**

**Typical Data Sources:**
- Proposal feedback and decision patterns
- Information depth requirements
- Approval processes and timeline patterns
- Meeting participation and engagement signals

**Key Insights Generated:**
- Decision triggers and approval patterns
- Information needs and presentation preferences
- Relationship dynamics and influence networks
- Risk tolerance and investment criteria

### 4. Beneficiary Personas
**End users, impact recipients, or communities served by innovations**

**Typical Data Sources:**
- Impact assessments and user research
- Feedback documents and case studies
- Validation reports with user insights
- Field observations and testimonials

**Key Insights Generated:**
- Actual needs vs. assumed needs
- Current solution gaps and workarounds
- Adoption barriers and success factors
- Impact measurement and value realization

## The Vianeo Four-Layer Structure

Every persona follows this exact structure:

### Layer 1: Requester (Who They Are)
Establishes the human behind the need through context, drivers, and values.

**Components:**
- First name (specific, not generic)
- Age (exact number, not range)
- Life/Motivations (2-3 sentences: daily context, role, why they care)
- Personality/Values (2-3 sentences: character traits, decision-making approach)

### Layer 2: Field of Application (Their World)
Captures mental models, observations, behaviors, and social context.

**Components:**
- Thinks/Feels (2-3 sentences: internal thoughts, worries, hopes)
- Observes (2-3 sentences: what they witness, patterns noticed)
- Does (2-3 sentences: actual behaviors, habits, actions)
- Others Say (2-3 sentences: feedback received, reputation, external perspectives)

### Layer 3: Activities and Challenges (What They Do and Struggle With)
Documents tasks, pain points, and concrete hopes.

**Components:**
- Tasks/Activities (4-6 bullets: specific responsibilities and processes)
- Pains/Lacks (4-6 bullets: frustrations, gaps, inefficiencies)
- Expectations/Hopes (4-6 bullets: desired outcomes and improvements)

### Layer 4: Current Solutions (Their Present Reality)
Shows understanding of current workarounds, why they fail, and gaps.

**Components:**
- Current Solutions (2-3 sentences: what they use now, why inadequate, specific gaps)

## Validation Modes

### Validated Mode
**Triggered By:** Interview transcripts, survey responses, user research reports, direct stakeholder feedback

**Output Characteristics:**
- Personas marked as "Validated"
- Evidence tracking with source attribution
- Quote extraction and citation
- Interview count and confidence levels
- Vianeo scoring prediction (3-5 range achievable)

### Inferred Mode
**Triggered By:** Behavioral data from tools, project documentation, meeting notes, organizational context

**Output Characteristics:**
- Personas marked as "Not Yet Validated" or "Inferred from [source type]"
- Hypothesis generation for research validation
- Research gap identification
- Suggested validation questions
- Use for guiding initial research strategy

### Hybrid Mode
**When both validated and inferred data exist:**
- Marks which elements are validated vs. inferred
- Shows evidence strength per section
- Prioritizes validated insights
- Flags gaps for additional research

## Quality Scoring Alignment

### Score 5: Exceptional Personas
**Criteria:**
- 10+ validated interviews per persona
- Direct quotes with source attribution
- Each persona clearly distinct with non-overlapping needs
- Current solutions specifically named with gap analysis
- Pain points quantified (time, cost, frequency)

**Skill Output:** "Validated - Exceptional Quality" badge

### Score 4: Strong Personas
**Criteria:**
- 5-10 interviews per persona
- Good behavioral detail with validation
- Personas distinct with minor overlap
- Current solutions identified with basic gap analysis
- Most pain points specific and measurable

**Skill Output:** "Validated - Strong Quality" badge

### Score 3: Adequate Personas
**Criteria:**
- 3-5 interviews per persona
- Basic behavioral information
- Personas somewhat distinct
- Current solutions mentioned but not deeply analyzed
- Pain points identified but not all specific

**Skill Output:** "Validated - Adequate Quality" badge

### Score 2: Weak Personas
**Criteria:**
- 1-2 interviews or secondary research
- Limited behavioral detail
- Significant overlap between personas
- Current solutions vaguely mentioned
- Pain points generic or assumed

**Skill Output:** "Inferred - Needs Validation" badge

### Score 1: Critical Gap
**Criteria:**
- No interview validation
- Generic or hypothetical personas
- No clear distinction
- No current solution analysis
- Assumed needs without evidence

**Skill Output:** "Not Validated - Hypothesis Only" badge

## Examples

### Example 1: Partner Persona from Validated Interviews

**Input:**
```
"I have 7 interview transcripts from university research partners.
Build Vianeo partner personas showing both strategic and platform-ready versions."
```

**Expected Process:**
1. Skill analyzes all 7 transcripts
2. Identifies 3 distinct partner segments
3. Extracts quotes and behavioral patterns
4. Maps to Vianeo four-layer structure
5. Generates both output versions
6. Provides quality assessment (likely Score 4-5)

**Expected Output Includes:**
- 3 partner personas with full four-layer structure
- Evidence appendix with quotes from interviews
- Quality score prediction with justification
- Platform-ready version with character counts verified
- Recommendations for any improvements

### Example 2: Innovator Persona from Mixed Data

**Input:**
```
"Create innovator personas based on these 4 validation reports
and our Asana project data. Show which parts are validated."
```

**Expected Process:**
1. Skill analyzes validation reports (validated source)
2. Searches Asana for engagement patterns (inferred source)
3. Creates 2-3 innovator personas
4. Marks validated elements vs. inferred elements
5. Flags gaps needing interview validation
6. Provides hybrid validation markers

**Expected Output Includes:**
- 2-3 innovator personas (hybrid validation)
- Clear markers showing validated vs. inferred sections
- Research gap analysis
- Suggested interview questions for validation
- Quality score (likely 2-3 due to limited validated data)
- Recommendations for improving to Score 4

### Example 3: Beneficiary Persona for Research Planning

**Input:**
```
"We're planning user research for a health tech innovation.
Generate inferred beneficiary personas to guide our interview strategy."
```

**Expected Process:**
1. Skill uses organizational context and project docs
2. Creates hypothesis-based personas
3. Marks as "Not Yet Validated - Hypothesis for Research"
4. Generates research questions to validate each hypothesis
5. Provides interview planning guidance

**Expected Output Includes:**
- 3-4 hypothesis-based beneficiary personas
- Heavy "Not Yet Validated" markers
- Research gap analysis highlighting what needs validation
- Specific interview questions per persona
- Suggested interview count (5-10 per persona)
- Note that these are for research planning, not Vianeo submission

## Notes

### Common Pitfalls and How Skill Prevents Them

1. **Generic Demographics**
   - Skill requires specific age (not ranges)
   - Flags generic language ("professional," "busy")
   - Validates behavioral specificity

2. **Solution-First Thinking**
   - Structures Expectations/Hopes around outcomes, not solutions
   - Focuses on problems, not your product
   - Validates needs exist independently of solution

3. **Overlapping Personas**
   - Automatic distinctiveness testing
   - Flags overlap in needs/pains/tasks
   - Recommends consolidation when appropriate

4. **Ignoring Current Solutions**
   - Requires Current Solutions layer completion
   - Validates specificity (actual products/services named)
   - Checks for gap analysis

5. **Assumed Needs**
   - Validation mode tracking (inferred vs. validated)
   - Evidence requirement for validated claims
   - Quality scoring penalties for assumptions

6. **Vague Pain Points**
   - Seeks quantification in source data
   - Flags vague language
   - Requires specific behaviors and impacts

### Multi-Language Handling

**Language Support:**
- English
- Portuguese (Brazilian)
- Mixed bilingual content

**Approach:**
- Analyze in native language
- Preserve original quotes
- Provide translations in parentheses if needed
- Note cultural patterns when relevant
- No assumption of US-centric norms

### Quality Checks

**Pre-Generation:**
- Data sufficiency assessment
- Coverage across persona layers
- Persona count determination (recommends 3-5)

**Post-Generation:**
- Distinctiveness test (flags overlap)
- Completeness check (all layers populated)
- Specificity audit (generic language detection)
- Format compliance (character limits, sentence counts)
- Evidence strength validation

### Best Practices for Users

**For Research Planning:**
1. Start with inferred personas to guide research design
2. Use suggested validation questions in interviews
3. Collect behavioral data alongside qualitative interviews
4. Track evidence as you conduct research

**For Persona Creation:**
1. Provide all available data upfront
2. Enable relevant tool integrations if helpful
3. Specify persona type if not obvious
4. Request evidence tracking for validation

**For Team Alignment:**
1. Share full strategic version internally
2. Review personas collaboratively
3. Validate against team's stakeholder knowledge
4. Update as collective understanding improves

**For Vianeo Submission:**
1. Target score 4+ for competitive submissions
2. Use platform-ready version for data entry
3. Keep full strategic version for scoring defense
4. Address flagged gaps before submission

**For Ongoing Use:**
1. Update personas as projects progress
2. Reference personas in decision-making
3. Validate with actual stakeholder interactions
4. Track how personas evolve over time

## Related Skills

- Technology validation assessment
- Partnership strategy development
- Market validation research
- Impact measurement planning
- Ecosystem mapping
- 360 Innovation Compass methodology
- Vianeo validation framework implementation

## Version History

- v1.0 - 2025-11-14 - Initial skill creation with dual output structure, validation tracking, and Vianeo framework integration
