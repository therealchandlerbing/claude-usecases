---
name: Intelligence Extractor
description: Extract partnership, funding, and stakeholder intelligence from meeting transcripts, emails, and conversations with real-time quality monitoring and template-based optimization
version: 1.1.0
author: 360 Social Impact Studios
created: 2025-03-14
updated: 2025-11-22
category: data-intelligence
complexity: medium
dependencies:
  - Supabase (optional, for quality monitoring)
  - Asana (optional, for intelligence storage)
  - Zapier (optional, for automation)
outputs:
  - JSON (structured intelligence data)
  - Asana tasks (if integrated)
  - Quality metrics (if dashboard enabled)
---

# Intelligence Extractor - Skill Instructions

## Purpose

This skill extracts structured intelligence from unstructured conversations (meeting transcripts, emails, notes) and outputs JSON data according to three specialized schemas: **Partnership Intelligence**, **Funding Intelligence**, and **Stakeholder Intelligence**.

## Core Capabilities

1. **Template-Based Extraction** - 10 specialized prompt templates for different meeting types
2. **Multi-Type Intelligence** - Extracts partnerships, funding opportunities, and stakeholder profiles
3. **Quality Monitoring** - Built-in confidence scoring and quality tracking
4. **Cultural Intelligence** - Captures cross-cultural communication patterns
5. **Cross-Referencing** - Identifies connections between entities
6. **Real-Time Dashboard** - Optional quality monitoring via Supabase + Next.js dashboard

## When to Use This Skill

Invoke this skill when the user requests:
- "Extract intelligence from this meeting transcript"
- "Analyze this conversation for partnership/funding/stakeholder intelligence"
- "Process meeting notes and structure the intelligence"
- "Use intelligence-extractor skill on..."

## Step-by-Step Execution

### Step 1: Template Selection

First, determine the meeting type and select the appropriate template from `templates/`:

| Meeting Type | Template File | Complexity |
|--------------|---------------|------------|
| New partnership exploration | `01-partnership-new.md` | Medium |
| Existing partnership check-in | `02-partnership-existing.md` | Low |
| Funder initial contact | `03-funder-initial.md` | High |
| Grant application discussion | `04-funder-application.md` | Medium |
| Board/governance meeting | `05-board-governance.md` | High |
| Client sprint/planning | `06-client-sprint.md` | High |
| Community stakeholder | `07-community-stakeholder.md` | High |
| International/cross-cultural | `08-international-partner.md` | High |
| Conference/networking | `09-conference-networking.md` | Low |
| Crisis/problem-solving | `10-crisis-problem-solving.md` | Medium |

**Selection Logic:**
- If meeting involves new organization → Template 1 or 3
- If meeting is follow-up/existing relationship → Template 2
- If cross-cultural context mentioned → Template 8
- If multiple stakeholders/board → Template 5
- If brief/informal → Template 9
- If conflict/problem → Template 10

**Action:** Read the appropriate template file to understand extraction priorities.

### Step 2: Analyze Source Material

Before extracting, analyze the entire source:

**Identify:**
- **Participants:** Who's involved (organizations and people)
- **Context:** Meeting type, stage in relationship, history
- **Cultural Context:** Geographic, organizational culture, communication norms
- **Relationship Stage:** First contact? Ongoing? Established?
- **Decisions/Commitments:** What was decided or committed to

**Cultural Context Clues:**
- **Brazilian Context:** Relationship-first, warmth, "jeitinho" problem-solving, flexible with time
- **US Corporate:** Efficiency, metrics-focused, punctual, contract-before-relationship
- **International:** Language use, formality, hierarchy, decision-making norms

### Step 3: Identify Intelligence Types

Determine which intelligence type(s) are present:

**Partnership Intelligence:**
- Discussion about organizational relationships
- Collaboration opportunities
- Strategic alliances
- Decision-making processes
- Cultural communication patterns

**Funding Intelligence:**
- Specific grants, investments, or funding programs
- Application requirements and timelines
- Decision processes
- Program officer relationships
- Success factors and red flags

**Stakeholder Intelligence:**
- Individual people (not organizations)
- Communication styles and preferences
- Decision-making patterns
- Power dynamics and influence
- Strategic value

**Note:** Sources often contain multiple types (e.g., partnership + stakeholder profiles of key contacts).

### Step 4: Extract Structured Data

For each intelligence type found, extract according to the schema:

#### Partnership Intelligence Schema

```json
{
  "type": "partnership",
  "confidence": "high|medium|low",
  "action": "create_new|update_existing|flag_for_review",

  // Core identification
  "organization_name": "string",
  "partnership_type": "Brazilian Educational|Brazilian Corporate|US Corporate/VC|US Foundation|Asian Partner|European Impact|Government/Policy|Other",
  "primary_contact": "string (name)",
  "secondary_contacts": ["array of names"],

  // Relationship metadata
  "relationship_temperature": "Cold|Warming|Hot|Active Partner|Stalled",
  "cultural_approach": "Relationship-First|Transaction-First|Hybrid|Hierarchical|Collaborative",
  "decision_timeline": "Fast (<3 months)|Deliberate (3-6 months)|Glacial (>6 months)|Unclear",
  "relationship_stage": "Initial Contact|Exploration|Negotiation|Active Partnership|Closed-Won|Closed-Lost",

  // Strategic intelligence
  "opening_opportunities": [
    "Pain points or gaps they're trying to solve",
    "Strategic priorities creating urgency"
  ],

  "strategic_qualification_questions": [
    "Questions that reveal decision-making authority",
    "Questions that surface budget reality",
    "Questions that test cultural fit"
  ],

  "common_hesitations": [
    {
      "hesitation": "Their concern or objection",
      "response_framework": "How to address it",
      "proof_points": "Examples or data to reference (optional)"
    }
  ],

  "strategic_framing": {
    "value_alignment_language": "How to frame 360's work in their terms",
    "cultural_communication_adjustments": "Communication style needs",
    "key_phrases": {
      "alignment_signals": ["Phrases that indicate good fit"],
      "misalignment_signals": ["Phrases that indicate problems"]
    }
  },

  "walk_away_signals": [
    "Red flags or deal-breakers observed or mentioned"
  ],

  // This interaction
  "interaction_notes": "Summary of this specific conversation",
  "next_actions": ["Specific follow-up items"],
  "relationship_owner": "Chandler|Eduardo|Felipe|Team|null"
}
```

#### Funding Intelligence Schema

```json
{
  "type": "funding",
  "confidence": "high|medium|low",
  "action": "create_new|update_existing|flag_for_review",

  // Core identification
  "funder_name": "string",
  "program_name": "string or null",
  "program_officer": "string or null",
  "funder_type": "Foundation|Impact Investor|Government Program|Corporate Partnership|Philanthropic Family Office|Multi-lateral Org|Other",

  // Opportunity details
  "funding_amount_range": "<$50K|$50K-$250K|$250K-$1M|$1M-$5M|>$5M|Unclear",
  "application_deadline": "YYYY-MM-DD or null",
  "decision_expected": "YYYY-MM-DD or null",
  "decision_timeline": "Fast (<2 months)|Standard (2-4 months)|Slow (4-6 months)|Very Slow (>6 months)|Unclear",

  // Strategic intelligence
  "decision_intelligence": {
    "process": "Application stages, review process",
    "decision_makers": "Who decides, how",
    "success_rate_signals": "Competitive? High bar? Open to new grantees?",
    "past_patterns": "Past funded projects, preferences"
  },

  "positioning_strategy": {
    "how_to_frame": "How to position 360's work for this funder",
    "evidence_needed": "Data? Stories? Research? Case studies?",
    "differentiation": "What makes 360 stand out for this opportunity"
  },

  "requirements_mentioned": [
    "Narrative components",
    "Financial documents",
    "Supporting materials"
  ],

  "red_flags": [
    "Deal-breakers or walk-away signals"
  ],

  "success_factors": [
    "What increases likelihood of funding",
    "Unofficial guidance or hints",
    "Relationships or connections that help"
  ],

  "fit_assessment": {
    "mission_alignment": "Excellent|Good|Moderate|Stretch|Poor",
    "geographic_fit": "string describing fit",
    "capacity_match": "Can we deliver what they fund?",
    "values_alignment": "Any concerns or strong alignment notes"
  },

  // This interaction
  "interaction_notes": "Summary of this specific conversation",
  "next_actions": ["Follow-up items"],
  "application_owner": "Chandler|Eduardo|Felipe|Team|null"
}
```

#### Stakeholder Intelligence Schema

```json
{
  "type": "stakeholder",
  "confidence": "high|medium|low",
  "action": "create_new|update_existing|flag_for_review",

  // Core identification
  "full_name": "string",
  "organization": "string",
  "title_role": "string",
  "stakeholder_type": "Board Member|Client Exec|Partner Leader|Community Champion|Policy Maker|Funder Contact|Academic/Researcher|Advisor|Other",

  // Communication intelligence
  "communication_style": "Direct & Efficient|Relational & Warm|Formal & Hierarchical|Collaborative & Inclusive|Data-Driven & Analytical|Visionary & Big-Picture|Mixed",

  "communication_preferences": {
    "meeting_format": "In-Person Priority|Video Comfortable|Phone Preferred|Email Primary|Flexible",
    "response_time": "Very Fast (<24hrs)|Fast (1-3 days)|Moderate (3-7 days)|Slow (>1 week)|Inconsistent",
    "language_preference": "English|Portuguese|Spanish|Multilingual|Other",
    "preparation_needs": "How they like to prep for meetings"
  },

  // Cultural context
  "cultural_context": "US Corporate|US Nonprofit|Brazilian|Latin American (other)|European|Asian|African|Multi-Cultural",

  "cultural_communication_notes": {
    "relationship_building_pace": "Fast trust|Slow cultivation|Relationship before business",
    "formality_level": "Formal|Informal|Context-dependent",
    "time_orientation": "Punctual|Flexible|Varies",
    "decision_making_culture": "Individual|Consensus|Consultative|Hierarchical"
  },

  // Decision-making intelligence
  "decision_authority": "Final Decision-Maker|Strong Influence|Advisory Voice|Limited Influence|Unknown",

  "decision_making_intelligence": {
    "decision_style": "Fast gut check|Deliberate analysis|Consensus-seeking|Consultative|Data-driven",
    "information_needs": "What evidence persuades them",
    "risk_tolerance": "High|Moderate|Low|Unknown",
    "timeline_patterns": "Fast|Deliberate|Varies by situation"
  },

  // Strategic intelligence
  "what_they_care_about": [
    "Core values",
    "Success metrics",
    "Pressure points",
    "Legacy questions"
  ],

  "power_dynamics_awareness": "High (very conscious of equity/power)|Moderate (aware but inconsistent)|Low (not central to their thinking)|Unknown",

  "systems_change_orientation": "Deep Systems Thinker|Open to systems thinking|Programmatic Focus|Transactional Orientation|Unknown",

  // Working relationship intelligence
  "relationship_stage": "New Contact|Building Trust|Established Relationship|Close Collaborator|Champion/Advocate",

  "strategic_value": {
    "level": "high|medium|low",
    "reasoning": "Why they matter strategically"
  },

  "do_list": [
    "Specific practices that work well with this person"
  ],

  "dont_list": [
    "Things to avoid, communication pitfalls"
  ],

  // This interaction
  "interaction_notes": "Summary of this specific interaction",
  "next_actions": ["Follow-up items"],
  "relationship_owner": "Chandler|Eduardo|Felipe|Team|null"
}
```

### Step 5: Confidence Scoring

Assign confidence levels based on information quality:

**High Confidence (70-100%):**
- Multiple clear indicators present
- Enough detail to populate most schema fields
- Consistent information throughout source
- Direct statements vs. interpretation
- Names, organizations, and facts clearly stated

**Medium Confidence (40-69%):**
- Some clear indicators, some interpretation needed
- Partial information across schema fields
- Some ambiguity or conflicting signals
- Mix of explicit and inferred information
- Missing some key details

**Low Confidence (0-39%):**
- Minimal explicit information
- Mostly interpretation and inference
- Significant gaps in schema fields
- Ambiguous or contradictory information
- Should be flagged for human review

### Step 6: Action Determination

**create_new:**
- First mention of organization/funder/person
- Introductory language ("We met with...")
- No reference to past interactions

**update_existing:**
- References to prior interactions ("Follow-up with...", "Continuing our...")
- Relationship history mentioned
- Progress in decision-making or relationship

**flag_for_review:**
- Confidence is low
- Ambiguous or conflicting information
- Sensitive information (conflicts, problems)
- Complex multi-stakeholder dynamics
- Unclear which existing entity this updates

### Step 7: Quality Rules

**CRITICAL - Always Follow:**
1. **Never fabricate information** - If it's not in the source, use `null`
2. **Be conservative with confidence** - When in doubt, score lower
3. **Use exact names and titles** - Don't paraphrase
4. **Preserve cultural context clues** - Language, formality, relationship pace
5. **Flag ambiguities** - Don't resolve them yourself
6. **Extract behavioral evidence** - "She responded within hours" vs. "She seems responsive"
7. **Note what's NOT said** - Silences and avoidances matter
8. **Respect sensitivity** - Flag conflicts, problems, or delicate situations
9. **Cross-reference intelligently** - Note connections between entities
10. **Maintain context** - Include enough detail for future usefulness

### Step 8: Cross-Reference Detection

Identify and document connections between entities:

```json
"cross_references": [
  {
    "type": "partnership_to_funder|stakeholder_to_partnership|etc",
    "from": "Entity 1",
    "to": "Entity 2",
    "relationship": "Description of connection"
  }
]
```

**Common cross-references:**
- Stakeholder works at Partner organization
- Funder also interested in Partnership
- Multiple stakeholders from same organization
- Overlapping networks or introductions

### Step 9: Output Format

**CRITICAL:** Always output valid JSON wrapped in ```json blocks.

```json
{
  "extraction_summary": "Brief overview of what intelligence was found",
  "intelligence_items": [
    {
      "type": "partnership|funding|stakeholder",
      "confidence": "high|medium|low",
      "action": "create_new|update_existing|flag_for_review",
      // ... type-specific fields
    }
  ],
  "flagged_for_review": [
    {
      "reason": "Why human review is needed",
      "context": "Relevant excerpt from source",
      "entity": "Name of partnership/funder/stakeholder"
    }
  ],
  "extraction_metadata": {
    "source_type": "meeting_transcript|email_thread|notes|other",
    "source_date": "YYYY-MM-DD if determinable",
    "participants": ["List of people involved"],
    "meeting_type": "Classification if determinable",
    "language": "english|portuguese|spanish|mixed",
    "cultural_context": "Detected cultural context if relevant"
  },
  "cross_references": [
    {
      "type": "partnership_to_funder|stakeholder_to_partnership|etc",
      "from": "Entity 1",
      "to": "Entity 2",
      "relationship": "Description of connection"
    }
  ]
}
```

### Step 10: Quality Assurance (Optional)

If Supabase quality monitoring is enabled, the JSON output will be logged to the database for real-time quality tracking via the dashboard at `/intelligence-dashboard/`.

**Quality Metrics Tracked:**
- Confidence distribution (% high/medium/low)
- Completeness score (% of schema fields populated)
- Template performance (which templates yield best results)
- Flagged items requiring review
- Extraction trends over time

## Advanced Features

### Multiple Entities Handling

When a source contains multiple partnerships, funders, or stakeholders:
1. Create separate intelligence items for each distinct entity
2. Use cross_references to show connections
3. Maintain consistent confidence (same source may yield different confidence for different entities)
4. Avoid duplication (if same person mentioned in multiple contexts, create one comprehensive stakeholder profile)

### Multi-Language Support

Handles:
- English transcripts
- Portuguese transcripts (Brazilian context)
- Mixed language (code-switching)
- Interpreter-mediated conversations

### Sensitivity Handling

Automatically flag for review:
- Conflicts or tensions
- Past harm or broken trust
- Sensitive political dynamics
- Confidential information
- Legal or compliance concerns

### Pattern Recognition

Capture recurring patterns when observed:
- "Brazilian partners typically need 3+ relationship meetings"
- "US foundations in Q1 move faster than Q3"
- "Board members who ask financial questions first tend to be slower decision-makers"

## Error Handling

### Ambiguous Information

```json
{
  "action": "flag_for_review",
  "confidence": "low",
  "flagged_for_review": [{
    "reason": "Ambiguous decision authority - unclear if Maria can commit or needs board approval",
    "context": "She said 'we need to discuss' but didn't specify who"
  }]
}
```

### Insufficient Information

```json
{
  "organization_name": "InovaEduK",
  "primary_contact": "Maria Silva",
  "opening_opportunities": null,
  "strategic_qualification_questions": null,
  "confidence": "low",
  "action": "flag_for_review",
  "flagged_for_review": [{
    "reason": "Insufficient detail in source - only organization name mentioned",
    "context": "Brief mention in passing, no substantive discussion"
  }]
}
```

### Conflicting Information

```json
{
  "flagged_for_review": [{
    "reason": "Conflicting timeline information",
    "context": "Maria said 'we need to move fast' but also 'we like to take time building trust' - unclear actual timeline expectations"
  }]
}
```

## Limitations

This skill:
- **Cannot** access external data (websites, databases, past Asana tasks)
- **Cannot** validate names or facts against other sources
- **Should not** be used for legal or compliance decisions without human review
- **May miss** subtle cultural nuances without proper context
- **Requires** human judgment for sensitive situations

Always review before acting on extracted intelligence, especially for:
- High-stakes decisions
- Cross-cultural contexts
- Sensitive relationships
- Legal or financial commitments

## Integration Options

### Manual Workflow
1. User provides transcript/notes
2. Run extraction
3. Review JSON output
4. Manually create Asana tasks or store intelligence
5. Provide quality feedback

### Automated Workflow (Zapier)
1. Transcript saved to Google Drive
2. Zapier triggers on new file
3. Sends to Claude API with this skill
4. Parses JSON response
5. Creates/updates Asana tasks automatically
6. Logs to Supabase for quality monitoring
7. User reviews on dashboard

See `.claude/skills/intelligence-extractor/ZAPIER-INTEGRATION.md` for detailed automation setup.

## Supporting Files

**Templates:**
- `templates/00-template-selection-guide.md` - Quick reference
- `templates/01-partnership-new.md` through `templates/10-crisis-problem-solving.md` - Specialized extraction templates

**References:**
- `references/intelligence-schemas.md` - Complete JSON schema documentation
- `references/cross-linking-architecture.md` - Three-system integration guide
- `references/quality-framework.md` - Quality assessment framework
- `references/cultural-intelligence.md` - Cross-cultural communication guide

**Examples:**
- `examples/partnership-extraction-example.md`
- `examples/funder-extraction-example.md`
- `examples/stakeholder-extraction-example.md`

## Version History

### v1.1.0 (2025-11-22)
- Enhanced SKILL.md with complete extraction logic
- Integrated quality monitoring guidance
- Added template selection decision tree
- Comprehensive error handling patterns
- Cross-reference detection system

### v1.0.0 (2025-03-14)
- Initial release
- Three intelligence schemas
- 10 specialized extraction templates
- Cross-reference detection
- Multi-language support
- Cultural intelligence extraction

---

## Quick Execution Checklist

- [ ] Determine meeting type and select template
- [ ] Read entire source before extracting
- [ ] Identify cultural context clues
- [ ] Determine intelligence types present (partnership/funding/stakeholder)
- [ ] Extract structured data per schema
- [ ] Assign confidence levels conservatively
- [ ] Determine action (create_new/update_existing/flag_for_review)
- [ ] Identify cross-references between entities
- [ ] Flag ambiguities and sensitivities for human review
- [ ] Output valid JSON in ```json blocks
- [ ] Never fabricate information - use null when unknown
