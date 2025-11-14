---
name: Intelligence Extractor
description: Extract partnership, funding, and stakeholder intelligence from meeting transcripts, emails, and conversations to populate 360's intelligence databases. Supports automated workflow via Zapier or manual extraction.
version: 1.0.0
author: 360 Social Ventures
created: 2025-03-14
---

# Intelligence Extractor

## Overview

The Intelligence Extractor is a comprehensive system for capturing, structuring, and organizing strategic intelligence about partnerships, funding opportunities, and stakeholders. It transforms unstructured meeting transcripts and communications into actionable intelligence stored in Asana databases.

### What This Skill Does

1. **Analyzes** meeting transcripts, emails, and conversation notes
2. **Extracts** structured intelligence across three categories:
   - Partnership Intelligence (organizations, collaborations, alliances)
   - Funding Opportunity Intelligence (grants, investors, programs)
   - Stakeholder Intelligence (individuals, decision-makers, influencers)
3. **Structures** information according to predefined schemas
4. **Outputs** JSON that can be manually reviewed or automatically imported to Asana
5. **Learns** from feedback to improve extraction quality over time

### Use Cases

**Manual Use:**
- After important meetings, extract intelligence for your records
- Process old meeting notes to populate intelligence database
- Quick intelligence capture from conference conversations

**Automated Use:**
- Zapier workflow processes Fathom transcripts automatically
- Email threads analyzed for funding or partnership intelligence
- Batch process historical transcripts

## Output Format

**CRITICAL:** Always output valid JSON wrapped in ```json blocks.

### Core Output Structure

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

## Intelligence Schemas

### 1. Partnership Intelligence Schema

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

### 2. Funding Intelligence Schema

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

### 3. Stakeholder Intelligence Schema

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

## Extraction Guidelines

### Confidence Scoring

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

### Action Determination

**create_new:**
- This appears to be a new entity not yet in the system
- First mention of organization/funder/person
- No reference to past interactions
- Introductory language ("We met with...")

**update_existing:**
- References to prior interactions ("Follow-up with...", "Continuing our...")
- Relationship history mentioned
- Updates to previous information
- Progress in decision-making or relationship

**flag_for_review:**
- Confidence is low
- Ambiguous or conflicting information
- Sensitive information (conflicts, problems)
- Complex multi-stakeholder dynamics
- Unclear which existing entity this updates
- Need human judgment on interpretation

### Quality Rules

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

### Handling Multiple Entities

When a source contains multiple partnerships, funders, or stakeholders:

1. **Create separate intelligence items** for each distinct entity
2. **Use cross_references** to show connections between them
3. **Maintain consistent confidence** - Same source may yield different confidence for different entities
4. **Avoid duplication** - If same person mentioned in multiple contexts, create one comprehensive stakeholder profile

### Cultural Intelligence Extraction

Pay special attention to cultural context clues:

**Brazilian Context:**
- Relationship-building before business
- Warmth and personal connection
- "Jeitinho" problem-solving
- Flexibility with time and process
- Hierarchy respect with relationship warmth

**US Corporate:**
- Efficiency and directness
- Metrics and outcomes focus
- Punctuality and schedule adherence
- Contract before relationship

**International/Cross-Cultural:**
- Language use and comfort
- Formality and hierarchy
- Decision-making norms
- Time orientation
- Communication directness

### Red Flags to Always Capture

- Values misalignment
- Power dynamics concerns
- Extraction or tokenism
- Unrealistic expectations
- Past harm or broken trust
- Decision authority unclear
- Resource mismatches
- Cultural competency gaps

### Green Flags to Always Capture

- Authentic alignment
- Power-sharing readiness
- Cultural humility
- Clear decision authority
- Adequate resources
- Long-term orientation
- Trust signals
- Mutual benefit clarity

## Processing Instructions

### Step 1: Analyze Source Material

Read the entire source before extracting. Understand:
- Who's involved (organizations and people)
- What's the context (meeting type, stage, history)
- What's the cultural context
- What's the relationship stage
- What decisions or commitments were made

### Step 2: Identify Intelligence Types

Determine which intelligence types are present:
- **Partnership**: Organizational relationships, collaborations
- **Funding**: Grants, investments, funding opportunities
- **Stakeholder**: Individual people with strategic importance

Sources often contain multiple types.

### Step 3: Extract Structured Data

For each intelligence type found:
1. Start with high-confidence, explicit information
2. Fill in interpretations and inferences with appropriate confidence
3. Use `null` for unknown fields
4. Capture behavioral evidence, not just statements
5. Note cultural context throughout

### Step 4: Quality Check

Before outputting:
- Is JSON valid and schema-compliant?
- Are confidence levels justified?
- Are names and organizations exact?
- Are there ambiguities to flag?
- Are cross-references identified?
- Is cultural context captured?

### Step 5: Output JSON

Wrap in ```json blocks with complete, valid JSON.

## Usage Examples

### Example 1: Partnership Exploration Meeting

**Input:**
```
Meeting with Maria Silva, CEO of InovaEduK (Brazilian educational organization)
Date: March 10, 2025

First conversation. They're exploring partnerships for systems-level educational change in São Paulo. Maria mentioned they've tried programmatic interventions before but want to think bigger. She was warm and relationship-oriented, suggested we meet a few more times before discussing specific projects. They work with 50 schools but want to expand. Mentioned they have government relationships but limited funding. Maria will introduce us to her board chair next month.

Decision timeline seems slow - she said "We like to build trust first, then work." Very collaborative communication style.
```

**Extraction Focus:**
- New partnership (Brazilian Educational)
- Relationship-first cultural approach
- Systems change orientation
- Funding needs
- One stakeholder (Maria Silva)

### Example 2: Funder Conversation

**Input:**
```
Call with James Peterson, Program Officer at Foundation for Change
Re: Education Innovation Grant Program

They fund $250K-$1M grants for systems-change work in education. Application deadline is June 1. Decision by September. They're interested in our community-driven approach but want to see more impact data. James suggested setting up a site visit in April. He mentioned the board really cares about sustainability plans. Competitive process - about 15% success rate. They funded similar organizations in Brazil before (mentioned Instituto Natura as example).

James was helpful and encouraging, responded to follow-up email same day.
```

**Extraction Focus:**
- Funding opportunity (Foundation)
- Requirements and timeline
- Success factors
- Stakeholder (James Peterson) with communication style
- Positioning strategy needs

## Integration with Asana

This skill outputs JSON designed to populate three Asana projects:

1. **Partnership Intelligence Hub**
2. **Funding Opportunity Intelligence**
3. **Stakeholder Intelligence Database**

### Manual Workflow

1. Run this skill on meeting transcript/notes
2. Review JSON output
3. Manually create Asana tasks using templates
4. Copy relevant intelligence into task descriptions
5. Set custom fields from extracted data

### Automated Workflow (via Zapier)

1. Transcript saved to Google Drive
2. Zapier triggers on new file
3. Sends to Claude API with this skill
4. Parses JSON response
5. Searches for existing Asana tasks
6. Creates new or updates existing tasks
7. Logs quality metrics

See `ZAPIER-INTEGRATION.md` for detailed setup.

## Quality Feedback Loop

To improve extraction quality over time:

### Provide Feedback

When you review extracted intelligence:

1. **Rate quality** on created Asana tasks:
   - 👍 Excellent
   - 👌 Good
   - 🤷 Fair
   - 👎 Poor

2. **Document issues** in comments:
   - What was missed?
   - What was wrong?
   - What was over/under-interpreted?

3. **Edit and improve** the intelligence:
   - Your edits are tracked
   - Patterns in edits improve future extractions

### Learning Cycle

Every week:
- Quality metrics analyzed
- Common issues identified
- Template improvements suggested
- You approve changes
- System gets better

## Template Selection

The skill includes specialized templates for different meeting types. When using manually, select the appropriate template context:

- **Partnership Exploration** - First/second meetings with potential partners
- **Partnership Check-in** - Follow-ups with existing partners
- **Funder Initial Contact** - First conversations with funding sources
- **Grant Application** - LOI feedback, proposal discussions
- **Board Meeting** - Governance or advisory board meetings
- **Client Sprint** - Working sessions with clients
- **Community Stakeholder** - Grassroots leaders, community organizations
- **International Partner** - Cross-cultural contexts (Brazilian, LatAm, etc.)
- **Conference/Networking** - Brief networking interactions
- **Crisis/Problem-Solving** - Emergency or conflict resolution meetings

See `templates/` directory for full template library.

## Advanced Features

### Cross-Reference Detection

Automatically identifies connections:
- Stakeholder works at Partner organization
- Funder also interested in Partnership
- Multiple stakeholders from same organization
- Overlapping networks or introductions

### Pattern Recognition

Captures recurring patterns:
- "Brazilian partners typically need 3+ relationship meetings"
- "US foundations in Q1 move faster than Q3"
- "Board members who ask financial questions first tend to be slower decision-makers"

### Multi-Language Support

Handles:
- English transcripts
- Portuguese transcripts (Brazilian context)
- Mixed language (code-switching)
- Interpreter-mediated conversations

### Sensitivity Handling

Automatically flags for review:
- Conflicts or tensions
- Past harm or broken trust
- Sensitive political dynamics
- Confidential information
- Legal or compliance concerns

## Error Handling

### Ambiguous Information

When information is unclear:
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

When source lacks detail:
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

When source contains contradictions:
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

## Version History

### v1.0.0 (2025-03-14)
- Initial release
- Three intelligence schemas (Partnership, Funding, Stakeholder)
- 10 specialized extraction templates
- Cross-reference detection
- Quality feedback loop foundation
- Multi-language support (English, Portuguese)
- Cultural intelligence extraction
- Automated and manual workflows

---

## Getting Started

1. **Manual Use**: Paste meeting transcript and specify meeting type
2. **Review Output**: Check JSON for accuracy and completeness
3. **Transfer to Asana**: Create tasks in appropriate intelligence project
4. **Provide Feedback**: Rate quality to improve future extractions

5. **Automated Use**: See ZAPIER-INTEGRATION.md for workflow setup

---

*For questions, improvements, or issues, document in the Intelligence System Improvements project in Asana.*
