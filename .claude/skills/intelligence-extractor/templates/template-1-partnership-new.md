# Template 1: New Partnership Exploration

**When to Use:** First or second meeting with potential partner organization

**Version:** 1.0
**Template ID:** template-1

---

## Context Requirements

When using this template, provide:
- Organization name
- Partner type (Brazilian Educational/US Corporate/etc.)
- Meeting stage (first meeting/second meeting)
- Date
- Participants from both sides
- Any known cultural context

---

## Extraction Priorities

### 1. Organization Intelligence (HIGH PRIORITY)

Extract:
- What problems are they trying to solve?
- What's creating urgency for them right now?
- What have they tried before that didn't work?
- What gaps exist in their current approach?
- What resources do they have (people, budget, relationships)?
- What resources do they lack?

### 2. Cultural & Communication Patterns (HIGH PRIORITY)

Observe and capture:
- **Meeting pace**: Did they want to jump into business or build relationship first?
- **Formality level**: Titles used? First names? Hierarchical language?
- **Decision-making signals**: Who else needs to be involved? How do they decide?
- **Time orientation**: Specific timelines or flexible/exploratory?
- **Communication style**: Direct? Diplomatic? Collaborative? Formal?
- **Language**: English, Portuguese, mixed? Comfort level?

### 3. Fit Assessment Signals

Look for:
- **Values alignment** indicators: Equity, community voice, systems change mentioned?
- **Red flags**: Extractive language, unrealistic expectations, values misalignment
- **Green flags**: Genuine curiosity, openness to co-design, long-term thinking
- **Approach alignment**: Do they think programmatically or systemically?

### 4. Decision Process Intelligence

Capture:
- Who else needs to be part of conversations?
- What's their internal approval process?
- Timeline expectations (fast/deliberate/glacial)
- Budget authority level of people in this meeting
- Who has final decision authority?

### 5. Next Steps Clarity

Extract:
- What did they commit to?
- What did we commit to?
- What remains ambiguous that needs clarification?
- When is next interaction?
- Who owns what actions?

---

## Stakeholder Extraction

For each person on the call, capture:
- **Name and role**
- **Communication style** observations
- **What they seemed most interested in** or concerned about
- **Decision-making authority** indicators
- **Relationship temperature**: Engaged? Skeptical? Enthusiastic? Guarded?

Create separate stakeholder intelligence entries for key participants (minimum 2-3 people).

---

## Pattern Recognition

### Look for these PARTNERSHIP patterns:

**Decision Authority Signals:**
- "We need to talk to [name/role]" → Decision authority is elsewhere
- "I can commit to..." vs. "We'll need to discuss..." → Authority level
- "Let me check with the board/team" → Consultation requirements

**Opening Opportunities:**
- "We tried X and it didn't work" → Past pain points
- "We're struggling with..." → Current challenges
- "We need..." → Explicit needs
- "Our goal is... but we can't..." → Gaps between aspiration and capacity

**Hesitation Signals:**
- "How do you handle Y?" → Concern area
- "What about...?" → Potential objection
- "We've worked with others who..." → Past experience coloring expectations
- Pauses or uncertainty when discussing timelines/budgets → Unclear

**Relationship Pace:**
- Language about timeline → Decision speed
- Suggestions for multiple meetings before commitment → Relationship-first culture
- Diving into specifics immediately → Transaction-oriented

**Credibility Assessment:**
- Questions about other organizations you work with → Checking credentials
- Questions about approach/methodology → Due diligence
- References to mutual connections → Trust-building through network

### Look for these CULTURAL patterns:

**Brazilian Context Indicators:**
- Relationship-building conversation before business
- Warmth, personal questions, coffee/meal offers
- Flexible with time, okay with longer meetings
- Formal titles (Doutor, Professor) but warm tone
- "Vamos ver" (let's see) - flexibility orientation
- Reference to "jeitinho" or creative problem-solving

**US Corporate Indicators:**
- Jump to business quickly
- Metrics and ROI questions
- Efficiency orientation (shorter meetings)
- Direct communication
- Calendar/timeline focus

**Community Organization Indicators:**
- Emphasis on community voice and participation
- Questions about power-sharing
- Past experiences with NGOs (good or bad)
- Trust-building pace (slower)
- Grassroots vs. top-down language

---

## Output Requirements

Generate:
1. **Partnership Intelligence** object:
   - Confidence: medium or high (first meetings rarely "low" if substantive)
   - Action: create_new
   - All relevant schema fields populated

2. **Stakeholder Intelligence** for each key participant:
   - Minimum 2-3 detailed profiles
   - Include: communication style, decision authority signals, what they care about
   - Relationship stage: New Contact or Building Trust

3. **Flag for review if**:
   - Major red flags detected
   - Unclear fit (conflicting signals)
   - Sensitive information shared (conflicts, past harm)
   - Complex decision-making structure unclear

---

## Cultural Context Notes

### If Brazilian Partner:

Pay attention to:
- Relationship-building pace (typically slower, trust-first)
- Formality of address (titles matter but warmth also matters)
- Timeline expectations (may be more flexible than stated)
- Hierarchical decision-making (who defers to whom)
- Personal connection importance

Capture:
- Language used (Portuguese, English, code-switching)
- Formality markers
- Relationship-building cues
- Decision consultation patterns

### If US Corporate:

Pay attention to:
- Efficiency focus (get to the point)
- Metrics and outcomes orientation
- Timeline and deadline adherence
- Direct communication style
- Individual decision authority

Capture:
- Speed of decision signals
- Data/evidence requests
- ROI framing
- Process and structure preferences

### If Other International Context:

Specify cultural context in notes and capture:
- Relationship-building norms
- Communication directness/indirectness
- Hierarchy and decision-making
- Time orientation
- Formality expectations

---

## Confidence Calibration

**High Confidence (75-100%):**
- Clear articulation of challenges and needs
- Explicit discussion of decision process
- Multiple participants sharing consistent information
- Specific next steps agreed upon
- Names, roles, and organizations clearly stated

**Medium Confidence (50-74%):**
- General discussion of challenges
- Some decision process hints but not complete
- Limited participants or brief conversation
- Vague next steps ("we'll follow up")
- Some key details missing

**Low Confidence (<50%):**
- Very brief or surface-level conversation
- Unclear decision process
- Conflicting information
- Many unknowns
- Should be flagged for human review

---

## Example Extraction

**Source:**
> Meeting with Dr. Maria Silva, CEO of InovaEduK (Brazilian educational org) and Paulo Rodrigues, their Director of Partnerships. First conversation.
>
> They're exploring partnerships for systems-level educational change in São Paulo state. Maria mentioned they've tried programmatic interventions (after-school tutoring, teacher training workshops) but results haven't been sustained. They want to think bigger about changing the system.
>
> She was very warm - we spent 15 minutes on relationship-building (coffee, talking about mutual connections). She suggested we meet 2-3 more times before discussing specific projects. Very collaborative communication style.
>
> They work with 50 schools but want to expand to 200. Mentioned they have good government relationships (State Education Secretary is former board member) but limited funding. Paulo will send us their strategic plan. Maria will introduce us to her board chair (Ana Santos) next month.
>
> When I asked about timeline, Maria said "We like to build trust first, then work together. Maybe we start something in 6 months?" Paulo seemed more eager, mentioned budget cycle closes in August.

**Output:**

```json
{
  "extraction_summary": "First partnership exploration with Brazilian educational organization InovaEduK. Systems-change orientation, relationship-first culture, strong government connections but funding constrained. Two key stakeholders identified.",

  "intelligence_items": [
    {
      "type": "partnership",
      "confidence": "high",
      "action": "create_new",
      "organization_name": "InovaEduK",
      "partnership_type": "Brazilian Educational",
      "primary_contact": "Dr. Maria Silva (CEO)",
      "secondary_contacts": ["Paulo Rodrigues (Director of Partnerships)"],
      "relationship_temperature": "Warming",
      "cultural_approach": "Relationship-First",
      "decision_timeline": "Deliberate (3-6 months)",
      "relationship_stage": "Exploration",
      "opening_opportunities": [
        "Past programmatic interventions (tutoring, teacher training) haven't sustained results - seeking systems-level approach",
        "Want to expand from 50 to 200 schools but lack capacity/approach for scale",
        "Have government relationships but limited funding - need partnership for resources and methodology"
      ],
      "strategic_qualification_questions": [
        "Who else on the board besides Ana Santos needs to be involved in partnership decisions?",
        "What does 'systems-level change' mean specifically to your team vs. programmatic work?",
        "Paulo mentioned August budget cycle - what funding decisions happen then and who decides?",
        "What past partnerships have worked well? Which haven't? Why?",
        "How do you balance State Education Secretary relationship with community voice?"
      ],
      "common_hesitations": [
        {
          "hesitation": "Timeline (Maria said 6 months, Paulo seemed more eager) - unclear urgency and decision pace",
          "response_framework": "Propose phased approach: relationship-building phase now, scope definition in 2-3 months, potential start in 6 months aligning with their comfort",
          "proof_points": "Reference other Brazilian partners where trust-building led to stronger collaboration"
        }
      ],
      "strategic_framing": {
        "value_alignment_language": "Frame as 'sustainable systems change' not quick fixes; emphasize long-term partnership not transaction; highlight government + community approach",
        "cultural_communication_adjustments": "Continue relationship-building pace (2-3 meetings before proposal); use formal titles (Doutora Maria) but warm tone; allow time for trust development; respect hierarchy (Maria leads, Paulo supports)",
        "key_phrases": {
          "alignment_signals": ["systems-level change", "sustained results", "build trust first", "long-term partnership"],
          "misalignment_signals": ["quick implementation", "proven programmatic models", "standard contract", "immediate start"]
        }
      },
      "walk_away_signals": [],
      "interaction_notes": "First meeting, very positive. Relationship-first Brazilian cultural approach evident (15 min relationship-building, multiple meetings before business). Maria is primary decision-maker but collaborative. Paulo more operational, eager. Good systems-change orientation. Next steps: Paulo sends strategic plan, meet again in 3-4 weeks, meet board chair Ana Santos next month.",
      "next_actions": [
        "Receive strategic plan from Paulo (he'll send)",
        "Schedule second meeting in 3-4 weeks",
        "Prepare for meeting with board chair Ana Santos (next month)",
        "Research State Education Secretary connection (past board member mentioned)"
      ],
      "relationship_owner": "Chandler"
    },
    {
      "type": "stakeholder",
      "confidence": "high",
      "action": "create_new",
      "full_name": "Dr. Maria Silva",
      "organization": "InovaEduK",
      "title_role": "CEO",
      "stakeholder_type": "Partner Leader",
      "communication_style": "Relational & Warm",
      "communication_preferences": {
        "meeting_format": "In-Person Priority",
        "response_time": "Moderate (3-7 days)",
        "language_preference": "Portuguese",
        "preparation_needs": "Relationship-building time before business, prefers in-person for important conversations"
      },
      "cultural_context": "Brazilian",
      "cultural_communication_notes": {
        "relationship_building_pace": "Slow cultivation - wants 2-3 meetings before project discussion",
        "formality_level": "Formal (uses title Doutora) but warm and personal",
        "time_orientation": "Flexible - '6 months' is indicative not hard deadline",
        "decision_making_culture": "Consultative - will involve board (especially Ana Santos)"
      },
      "decision_authority": "Final Decision-Maker",
      "decision_making_intelligence": {
        "decision_style": "Consensus-seeking with board, relationship-driven",
        "information_needs": "Trust and relationship first, then strategic alignment, then specifics",
        "risk_tolerance": "Moderate - wants proven but open to innovation if trust exists",
        "timeline_patterns": "Deliberate - won't rush into partnership"
      },
      "what_they_care_about": [
        "Sustained impact (not quick fixes that fade)",
        "Systems-level change in São Paulo education",
        "Building trusted partnerships",
        "Expanding reach (50 to 200 schools)"
      ],
      "power_dynamics_awareness": "Unknown",
      "systems_change_orientation": "Deep Systems Thinker",
      "relationship_stage": "Building Trust",
      "strategic_value": {
        "level": "high",
        "reasoning": "CEO of significant Brazilian educational org, systems-change oriented, strong government relationships, represents partnership opportunity in key geography and sector"
      },
      "do_list": [
        "Invest in relationship-building time (coffee, personal connection)",
        "Use formal title (Doutora) in written communication",
        "Be patient with timeline - don't push for speed",
        "Involve her in design, not just implementation"
      ],
      "dont_list": [
        "Don't rush to proposal before trust is built",
        "Don't skip relationship phases",
        "Don't assume 6 months is firm deadline"
      ],
      "interaction_notes": "First meeting. Very warm and relationship-oriented. Clear leader but collaborative. Patient decision-maker. Values trust highly. Systems thinker frustrated with programmatic band-aids.",
      "next_actions": [
        "Meet again in 3-4 weeks",
        "Prepare to meet board chair Ana Santos (Maria will introduce)"
      ],
      "relationship_owner": "Chandler"
    },
    {
      "type": "stakeholder",
      "confidence": "medium",
      "action": "create_new",
      "full_name": "Paulo Rodrigues",
      "organization": "InovaEduK",
      "title_role": "Director of Partnerships",
      "stakeholder_type": "Partner Leader",
      "communication_style": "Direct & Efficient",
      "communication_preferences": {
        "meeting_format": "Flexible",
        "response_time": "Fast (1-3 days)",
        "language_preference": "Portuguese",
        "preparation_needs": "Unknown"
      },
      "cultural_context": "Brazilian",
      "cultural_communication_notes": {
        "relationship_building_pace": "Faster than Maria - seems eager to move forward",
        "formality_level": "Unknown",
        "time_orientation": "More timeline-focused (mentioned August budget cycle)",
        "decision_making_culture": "Defers to Maria but has operational input"
      },
      "decision_authority": "Advisory Voice",
      "decision_making_intelligence": {
        "decision_style": "Unknown - didn't lead conversation",
        "information_needs": "Unknown",
        "risk_tolerance": "Unknown",
        "timeline_patterns": "Possibly faster than Maria based on August budget comment"
      },
      "what_they_care_about": [
        "Partnership logistics and operations",
        "Budget cycles and timing",
        "Scaling (50 to 200 schools)"
      ],
      "power_dynamics_awareness": "Unknown",
      "systems_change_orientation": "Unknown",
      "relationship_stage": "New Contact",
      "strategic_value": {
        "level": "medium",
        "reasoning": "Operational partner contact, will handle day-to-day partnership logistics, but Maria is decision-maker"
      },
      "do_list": [
        "Keep him in the loop operationally",
        "He's responsive - good for logistics coordination"
      ],
      "dont_list": [
        "Don't go around Maria to Paulo for decisions"
      ],
      "interaction_notes": "Second chair in meeting. More operationally focused than Maria. Mentioned budget cycle August deadline (Maria more flexible). Will send strategic plan. Seems eager to move forward.",
      "next_actions": [
        "Receive strategic plan from Paulo"
      ],
      "relationship_owner": "Chandler"
    }
  ],

  "flagged_for_review": [],

  "extraction_metadata": {
    "source_type": "meeting_transcript",
    "source_date": "2025-03-10",
    "participants": ["Chandler Bing (360)", "Dr. Maria Silva (InovaEduK, CEO)", "Paulo Rodrigues (InovaEduK, Director of Partnerships)"],
    "meeting_type": "Partnership Exploration - First Meeting",
    "language": "english",
    "cultural_context": "Brazilian - Relationship-first culture, formal but warm, deliberate timeline"
  },

  "cross_references": [
    {
      "type": "stakeholder_to_partnership",
      "from": "Dr. Maria Silva",
      "to": "InovaEduK",
      "relationship": "CEO and primary decision-maker"
    },
    {
      "type": "stakeholder_to_partnership",
      "from": "Paulo Rodrigues",
      "to": "InovaEduK",
      "relationship": "Director of Partnerships, operational contact"
    },
    {
      "type": "stakeholder_to_stakeholder",
      "from": "Ana Santos (mentioned)",
      "to": "Dr. Maria Silva",
      "relationship": "Board chair, will be introduced next month - key relationship for Maria"
    }
  ]
}
```

---

This template provides comprehensive guidance for extracting maximum intelligence from first partnership meetings while respecting cultural context and relationship-building norms.
