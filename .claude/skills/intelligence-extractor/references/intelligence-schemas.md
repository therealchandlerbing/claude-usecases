# Intelligence Schemas

**Purpose:** Defines the JSON structure for all three intelligence types extracted from meetings and conversations.

**Last Updated:** November 2025

---

## Table of Contents

1. [Overview](#overview)
2. [Partnership Intelligence Schema](#partnership-intelligence-schema)
3. [Funding Intelligence Schema](#funding-intelligence-schema)
4. [Stakeholder Intelligence Schema](#stakeholder-intelligence-schema)
5. [Shared Fields Across All Types](#shared-fields-across-all-types)
6. [Cross-Linking Fields](#cross-linking-fields)
7. [Confidence and Quality Indicators](#confidence-and-quality-indicators)
8. [Usage Examples](#usage-examples)

---

## Overview

The Intelligence Extractor produces three types of structured intelligence, each with a specific JSON schema optimized for storage in Asana tasks or Supabase database.

### Key Principles

1. **Required vs. Optional:** Fields marked `[REQUIRED]` must be present. Optional fields can be null or omitted.
2. **Cross-Linking:** All schemas include fields for linking to other intelligence types
3. **Confidence Tracking:** Every extraction includes confidence and completeness metadata
4. **Temporal Tracking:** All schemas track when intelligence was captured and last updated
5. **Cultural Context:** International and cross-cultural contexts are captured where relevant

---

## Partnership Intelligence Schema

### Purpose
Captures information about organizational partnerships, collaborations, and strategic relationships.

### JSON Structure

```json
{
  "intelligence_type": "partnership",
  "extraction_metadata": {
    "meeting_date": "YYYY-MM-DD",
    "meeting_type": "partnership_new | partnership_existing | ...",
    "template_version": "1.0",
    "extraction_date": "YYYY-MM-DD",
    "confidence_level": "high | medium | low",
    "completeness_score": 0.85,
    "flags": []
  },

  "organization": {
    "name": "[REQUIRED] Organization name",
    "type": "JV Partner | Brazil Tech Transfer | US Corporate/VC | Foundation | ...",
    "geographic_region": "[REQUIRED] Brazil - São Paulo | US - San Francisco | ...",
    "language": "Portuguese | English | Spanish | ...",
    "website": "https://...",
    "size": "startup | small | medium | large | enterprise"
  },

  "relationship_status": {
    "stage": "[REQUIRED] exploration | negotiation | active | paused | dead",
    "temperature": "[REQUIRED] hot | warm | cool | cold",
    "health": "[REQUIRED] healthy | at_risk | deteriorating",
    "first_contact_date": "YYYY-MM-DD",
    "last_interaction_date": "[REQUIRED] YYYY-MM-DD",
    "partnership_timeline": "Expected timeline in months",
    "success_likelihood": "very_high | high | medium | low | very_low"
  },

  "strategic_intelligence": {
    "problems_they_face": "[REQUIRED] Array of specific problems",
    "urgency_level": "high | medium | low",
    "past_attempts": "What they've tried before",
    "why_past_failed": "Why previous solutions didn't work",
    "strategic_fit": "[REQUIRED] How this partnership aligns with our strategy",
    "opening_opportunities": "Specific opportunities this creates",
    "value_alignment": {
      "score": 0-5,
      "details": "Areas of strong/weak alignment"
    }
  },

  "decision_intelligence": {
    "decision_makers": "[REQUIRED] Array of names (link to Stakeholder Intelligence)",
    "decision_process": "How decisions are made",
    "decision_timeline": "When decision will be made",
    "approval_levels_needed": "Board | Executive | Manager | ...",
    "budget_authority": "Who controls budget decisions",
    "political_dynamics": "Internal politics affecting decision"
  },

  "cultural_intelligence": {
    "cultural_approach": "[REQUIRED] relationship_first | transactional | collaborative | hierarchical",
    "communication_style": "direct | indirect | formal | informal",
    "decision_pace": "fast | deliberate | slow",
    "trust_building_needs": "What's needed to build trust",
    "formality_level": "high | medium | low",
    "power_distance": "How hierarchical the organization is"
  },

  "operational_intelligence": {
    "what_working_well": "What's going well (for existing partnerships)",
    "what_not_working": "What's not working (for existing partnerships)",
    "resource_capacity": "Their capacity for partnership",
    "technical_capacity": "Their technical capabilities",
    "partnership_history": "Track record with other partners",
    "common_hesitations": "Recurring concerns they raise"
  },

  "next_steps": {
    "immediate_actions": "[REQUIRED] Array of specific next steps",
    "owner_360": "Who owns this on our side",
    "owner_partner": "Who owns this on their side",
    "next_meeting_date": "YYYY-MM-DD",
    "deliverables_needed": "What we need to provide",
    "open_questions": "What we still need to learn"
  },

  "cross_linking": {
    "key_stakeholders": "[REQUIRED] Array of stakeholder names (links)",
    "potential_funders": "Array of funder names (links)",
    "related_partnerships": "Array of related partnership names",
    "supporting_funding_opportunities": "Array of funding opportunity names"
  },

  "quality_indicators": {
    "red_flags": "Array of concerning signals",
    "green_flags": "Array of positive signals",
    "walk_away_signals": "Signals to end pursuit",
    "deal_breakers_identified": "Non-negotiable issues"
  }
}
```

### Required Fields for Minimum Viable Intelligence

**Minimum for 75% completeness:**
- `organization.name`
- `organization.geographic_region`
- `relationship_status.stage`
- `relationship_status.temperature`
- `relationship_status.health`
- `relationship_status.last_interaction_date`
- `strategic_intelligence.problems_they_face`
- `strategic_intelligence.strategic_fit`
- `decision_intelligence.decision_makers`
- `cultural_intelligence.cultural_approach`
- `next_steps.immediate_actions`
- `cross_linking.key_stakeholders`

---

## Funding Intelligence Schema

### Purpose
Captures information about funding opportunities, grants, investments, and program officer relationships.

### JSON Structure

```json
{
  "intelligence_type": "funding",
  "extraction_metadata": {
    "meeting_date": "YYYY-MM-DD",
    "meeting_type": "funder_initial | funder_application | ...",
    "template_version": "1.0",
    "extraction_date": "YYYY-MM-DD",
    "confidence_level": "high | medium | low",
    "completeness_score": 0.82,
    "flags": []
  },

  "funder": {
    "name": "[REQUIRED] Foundation/Fund/Investor name",
    "type": "foundation | corporate | government | impact_investor | vc | ...",
    "program_name": "Specific program or fund name",
    "geographic_focus": "[REQUIRED] Where they fund",
    "website": "https://...",
    "total_funding_capacity": "Annual budget or fund size"
  },

  "opportunity": {
    "opportunity_type": "[REQUIRED] grant | investment | prize | contract | ...",
    "funding_amount_range": "Min-max or target amount",
    "timeline": "[REQUIRED] Application deadlines and decision dates",
    "stage": "[REQUIRED] research | LOI | full_proposal | finalist | awarded | declined",
    "success_likelihood": "very_high | high | medium | low | very_low",
    "competition_level": "How competitive is this opportunity"
  },

  "program_fit": {
    "alignment_score": "[REQUIRED] 0-5 rating",
    "what_they_really_care_about": "[REQUIRED] Their true priorities",
    "stated_priorities": "What they say they care about",
    "unstated_priorities": "What they care about but don't say",
    "our_fit_strengths": "Where we're a strong match",
    "our_fit_gaps": "Where we don't match well",
    "competitive_advantage": "What makes us stand out"
  },

  "decision_intelligence": {
    "decision_makers": "[REQUIRED] Program officers, board members (links to Stakeholder)",
    "decision_process": "[REQUIRED] How decisions are made",
    "decision_timeline": "When decisions happen",
    "evaluation_criteria": "What they evaluate on",
    "past_grantees_pattern": "Types of orgs they've funded before",
    "funding_cycle": "Annual, rolling, one-time",
    "board_dynamics": "How board influences decisions"
  },

  "application_intelligence": {
    "application_requirements": "What's required to apply",
    "success_factors": "What makes applications successful",
    "red_flags_to_avoid": "What makes applications fail",
    "budget_considerations": "Budget requirements and flexibility",
    "reporting_requirements": "What reporting is expected",
    "partnership_requirements": "Do they require collaboration",
    "geographic_requirements": "Where work must happen",
    "timeline_flexibility": "Can deadlines or timelines flex"
  },

  "relationship_intelligence": {
    "relationship_status": "new | existing | warm_intro | cold",
    "relationship_temperature": "hot | warm | cool | cold",
    "trust_level": "high | medium | low",
    "last_interaction_date": "[REQUIRED] YYYY-MM-DD",
    "interaction_history": "Summary of past interactions",
    "political_considerations": "Who we know, who knows us",
    "warm_intro_paths": "Who could introduce us"
  },

  "strategic_positioning": {
    "our_positioning": "How we should position ourselves",
    "narrative_frame": "The story we should tell",
    "proof_points_needed": "What evidence we need",
    "differentiation_strategy": "How to stand out from others",
    "risk_mitigation": "How to address perceived risks",
    "coalition_strategy": "Should we apply with partners"
  },

  "next_steps": {
    "immediate_actions": "[REQUIRED] Array of specific next steps",
    "owner_360": "Who owns this on our side",
    "deadlines": "Key dates we must hit",
    "deliverables_needed": "What we need to prepare",
    "research_needed": "What we still need to learn",
    "relationship_building_actions": "How to strengthen relationship"
  },

  "cross_linking": {
    "decision_makers_stakeholders": "[REQUIRED] Array of stakeholder names (links)",
    "supporting_partnerships": "Partnerships that strengthen application",
    "related_funding": "Other funding from this funder",
    "coalition_partners": "Partners for joint application"
  },

  "quality_indicators": {
    "green_flags": "Array of positive signals",
    "red_flags": "Array of concerning signals",
    "likelihood_score": 0-100,
    "confidence_rationale": "Why we're confident/not confident"
  }
}
```

### Required Fields for Minimum Viable Intelligence

**Minimum for 75% completeness:**
- `funder.name`
- `funder.type`
- `funder.geographic_focus`
- `opportunity.opportunity_type`
- `opportunity.timeline`
- `opportunity.stage`
- `program_fit.alignment_score`
- `program_fit.what_they_really_care_about`
- `decision_intelligence.decision_makers`
- `decision_intelligence.decision_process`
- `relationship_intelligence.last_interaction_date`
- `next_steps.immediate_actions`
- `cross_linking.decision_makers_stakeholders`

---

## Stakeholder Intelligence Schema

### Purpose
Captures information about individual people: their communication styles, decision-making approaches, influence, and relationships.

### JSON Structure

```json
{
  "intelligence_type": "stakeholder",
  "extraction_metadata": {
    "meeting_date": "YYYY-MM-DD",
    "meeting_type": "partnership_new | board_governance | ...",
    "template_version": "1.0",
    "extraction_date": "YYYY-MM-DD",
    "confidence_level": "high | medium | low",
    "completeness_score": 0.88,
    "flags": []
  },

  "person": {
    "name": "[REQUIRED] FirstName LastName",
    "current_role": "[REQUIRED] Title, Organization",
    "organization": "[REQUIRED] Organization name",
    "previous_roles": "Relevant previous positions",
    "geographic_location": "City, Country",
    "language": "Primary language(s)",
    "linkedin": "LinkedIn URL",
    "email": "Email if available",
    "phone": "Phone if available"
  },

  "influence_intelligence": {
    "power_level": "[REQUIRED] high | medium | low",
    "influence_scope": "What they have influence over",
    "decision_authority": "[REQUIRED] final | advisory | influencer | executor",
    "network_influence": "Who they know and influence",
    "reputation": "How they're perceived in their field",
    "areas_of_expertise": "What they're known for"
  },

  "communication_intelligence": {
    "communication_style": "[REQUIRED] direct | indirect | analytical | relational | ...",
    "preferred_channels": "Email | Phone | In-person | ...",
    "response_patterns": "How quickly they respond, when they respond",
    "communication_pace": "fast | moderate | slow",
    "formality_preference": "formal | semiformal | informal",
    "language_preference": "Which language(s) they prefer",
    "best_times_to_reach": "When they're most responsive"
  },

  "decision_making_intelligence": {
    "decision_style": "[REQUIRED] analytical | intuitive | consultative | directive | ...",
    "what_they_care_about": "[REQUIRED] Their priorities and values",
    "what_motivates_them": "What drives their decisions",
    "what_concerns_them": "What they worry about",
    "evidence_they_need": "Data | Stories | References | ...",
    "risk_tolerance": "high | medium | low",
    "decision_pace": "fast | deliberate | slow"
  },

  "cultural_intelligence": {
    "cultural_background": "Relevant cultural context",
    "cultural_approach": "[REQUIRED] relationship_first | transactional | collaborative | hierarchical",
    "relationship_building_pace": "fast | moderate | slow",
    "trust_building_needs": "What they need to trust you",
    "formality_norms": "How formal they expect interactions",
    "power_distance": "How they relate to hierarchy",
    "communication_directness": "How direct they are"
  },

  "relationship_intelligence": {
    "relationship_status": "[REQUIRED] new | developing | established | strong | at_risk | dormant",
    "relationship_temperature": "[REQUIRED] hot | warm | cool | cold",
    "trust_level": "high | medium | low",
    "first_contact_date": "YYYY-MM-DD",
    "last_interaction_date": "[REQUIRED] YYYY-MM-DD",
    "interaction_frequency": "How often you interact",
    "relationship_trajectory": "improving | stable | declining",
    "relationship_history": "Summary of relationship evolution"
  },

  "strategic_intelligence": {
    "their_priorities": "[REQUIRED] What matters to them right now",
    "their_constraints": "What limits them",
    "their_opportunities": "What opportunities they see",
    "their_challenges": "What challenges they face",
    "how_we_can_help": "Value we can provide to them",
    "what_they_can_help_with": "Value they can provide to us",
    "strategic_value_to_us": "high | medium | low"
  },

  "working_style": {
    "collaboration_style": "How they work with others",
    "meeting_preferences": "How they like meetings run",
    "detail_orientation": "high | medium | low",
    "follow_through": "Reliable | Variable | Unreliable",
    "conflict_approach": "Direct | Avoidant | Collaborative | ...",
    "stress_patterns": "How they behave under pressure"
  },

  "next_steps": {
    "immediate_actions": "[REQUIRED] Array of specific next steps",
    "owner_360": "Who owns this relationship on our side",
    "next_interaction_date": "YYYY-MM-DD",
    "relationship_building_actions": "How to deepen relationship",
    "open_questions": "What we still need to learn"
  },

  "cross_linking": {
    "associated_partnerships": "[REQUIRED] Array of partnership names (links)",
    "funding_influence": "Array of funding opportunities (links)",
    "other_stakeholders": "Related stakeholders in their network",
    "organizations": "All organizations they're connected to"
  },

  "quality_indicators": {
    "red_flags": "Array of concerning patterns",
    "green_flags": "Array of positive patterns",
    "reliability_signals": "How reliable they've been",
    "alignment_signals": "How aligned they are with us"
  }
}
```

### Required Fields for Minimum Viable Intelligence

**Minimum for 75% completeness:**
- `person.name`
- `person.current_role`
- `person.organization`
- `influence_intelligence.power_level`
- `influence_intelligence.decision_authority`
- `communication_intelligence.communication_style`
- `decision_making_intelligence.decision_style`
- `decision_making_intelligence.what_they_care_about`
- `cultural_intelligence.cultural_approach`
- `relationship_intelligence.relationship_status`
- `relationship_intelligence.relationship_temperature`
- `relationship_intelligence.last_interaction_date`
- `strategic_intelligence.their_priorities`
- `next_steps.immediate_actions`
- `cross_linking.associated_partnerships`

---

## Shared Fields Across All Types

### Universal Metadata

Every intelligence extraction includes:

```json
{
  "extraction_metadata": {
    "meeting_date": "YYYY-MM-DD",
    "meeting_type": "Template type used",
    "template_version": "Version number",
    "extraction_date": "When extraction was performed",
    "confidence_level": "high | medium | low",
    "completeness_score": 0.0-1.0,
    "flags": ["flag1", "flag2"]
  }
}
```

### Universal Cross-Linking Fields

Fields that appear in all types (with variations):

- **Partnership:** `key_stakeholders`, `potential_funders`
- **Funding:** `decision_makers_stakeholders`, `supporting_partnerships`
- **Stakeholder:** `associated_partnerships`, `funding_influence`

### Universal Quality Indicators

All types include:

```json
{
  "quality_indicators": {
    "red_flags": "Array of concerning signals",
    "green_flags": "Array of positive signals"
  }
}
```

---

## Cross-Linking Fields

### Purpose
Enable the three intelligence systems to work together as an interconnected ecosystem.

### Partnership → Stakeholder Links

```json
{
  "cross_linking": {
    "key_stakeholders": [
      "Maria Silva (CEO, InovaEduK)",
      "Roberto Santos (CTO, InovaEduK)"
    ]
  }
}
```

### Partnership → Funding Links

```json
{
  "cross_linking": {
    "potential_funders": [
      "Omidyar Network - Brazil Education Systems Grant",
      "Gates Foundation - Systems Change RFP"
    ]
  }
}
```

### Funding → Stakeholder Links

```json
{
  "cross_linking": {
    "decision_makers_stakeholders": [
      "Jennifer Chen (Program Officer, Gates Foundation)",
      "Carlos Alvarez (Board Member, Gates Foundation)"
    ]
  }
}
```

### Funding → Partnership Links

```json
{
  "cross_linking": {
    "supporting_partnerships": [
      "Coalition for Educational Equity",
      "MinEduc Brazil Collaboration"
    ]
  }
}
```

### Stakeholder → Partnership Links

```json
{
  "cross_linking": {
    "associated_partnerships": [
      "InovaEduK - Educational Systems Partnership",
      "MinEduc Brazil Collaboration"
    ]
  }
}
```

### Stakeholder → Funding Links

```json
{
  "cross_linking": {
    "funding_influence": [
      "BNDES Social Impact Fund",
      "Omidyar Network - Brazil Education"
    ]
  }
}
```

---

## Confidence and Quality Indicators

### Confidence Levels

**High Confidence (>85% completeness):**
- All required fields present
- Most optional fields populated
- Clear signals in transcript
- Minimal ambiguity
- Strong evidence for all claims

**Medium Confidence (60-85% completeness):**
- All required fields present
- Some optional fields missing
- Some ambiguity in transcript
- Reasonable inferences made
- Some evidence gaps

**Low Confidence (<60% completeness):**
- Some required fields missing
- Many optional fields missing
- Significant ambiguity
- Many inferences, few facts
- Evidence gaps throughout

### Automated Flags

System automatically flags extractions when:

- **`confidence_completeness_mismatch`:** High confidence but low completeness, or vice versa
- **`critical_fields_missing`:** Required fields are null or empty
- **`parsing_errors`:** Transcript was difficult to parse
- **`multiple_warnings`:** Several quality issues detected
- **`cultural_context_unclear`:** Cross-cultural meeting but cultural intelligence incomplete
- **`decision_intelligence_weak`:** Decision-making information is vague

---

## Usage Examples

### Example 1: Partnership Intelligence (High Confidence)

```json
{
  "intelligence_type": "partnership",
  "extraction_metadata": {
    "meeting_date": "2025-11-10",
    "meeting_type": "partnership_new",
    "template_version": "1.0",
    "extraction_date": "2025-11-10",
    "confidence_level": "high",
    "completeness_score": 0.87,
    "flags": []
  },
  "organization": {
    "name": "InovaEduK",
    "type": "Brazil Tech Transfer",
    "geographic_region": "Brazil - São Paulo",
    "language": "Portuguese",
    "website": "https://inovaeduk.com.br",
    "size": "medium"
  },
  "relationship_status": {
    "stage": "exploration",
    "temperature": "warm",
    "health": "healthy",
    "first_contact_date": "2025-11-10",
    "last_interaction_date": "2025-11-10",
    "partnership_timeline": "6-8 months",
    "success_likelihood": "high"
  },
  "strategic_intelligence": {
    "problems_they_face": [
      "Schools lack capacity to implement technology effectively",
      "Teacher training programs don't scale beyond pilot cities",
      "Government procurement process is slow and bureaucratic"
    ],
    "urgency_level": "high",
    "past_attempts": "Worked with 3 other consulting firms, all focused on technology deployment without capacity building",
    "why_past_failed": "Technology-first approach didn't address teacher mindset and school leadership gaps",
    "strategic_fit": "Our capacity-building approach addresses their core problem. We've solved similar challenges in 15+ Brazilian municipalities.",
    "opening_opportunities": "Introduction to Ministry of Education (Maria sits on advisory board), access to 200+ schools in their network",
    "value_alignment": {
      "score": 5,
      "details": "Strong alignment on equity, teacher capacity, and sustainable change approach"
    }
  },
  "decision_intelligence": {
    "decision_makers": ["Maria Silva (CEO, InovaEduK)", "Roberto Santos (CTO, InovaEduK)"],
    "decision_process": "Maria and Roberto make decision together, then present to board for approval (formality, not real gate)",
    "decision_timeline": "Want to decide by end of Q1 2026",
    "approval_levels_needed": "Executive (real) + Board (formality)",
    "budget_authority": "Maria has authority up to R$500K without board",
    "political_dynamics": "Board includes 2 former Ministry officials - very supportive of partnerships"
  },
  "cultural_intelligence": {
    "cultural_approach": "relationship_first",
    "communication_style": "semiformal",
    "decision_pace": "deliberate",
    "trust_building_needs": "Need multiple conversations, want to meet our team, references from shared connections matter",
    "formality_level": "medium",
    "power_distance": "low (flat organization, collaborative)"
  },
  "next_steps": {
    "immediate_actions": [
      "Send proposal outline by Nov 20",
      "Schedule follow-up meeting with full teams (their tech team + our program team)",
      "Connect Maria with our Municipal Education contact for reference"
    ],
    "owner_360": "Jessica Chen",
    "owner_partner": "Maria Silva",
    "next_meeting_date": "2025-11-25",
    "deliverables_needed": "Proposal outline, 2 case studies from similar work, budget range",
    "open_questions": ["What's their exact budget range?", "Timeline for Ministry introduction?"]
  },
  "cross_linking": {
    "key_stakeholders": ["Maria Silva (CEO, InovaEduK)", "Roberto Santos (CTO, InovaEduK)"],
    "potential_funders": ["Omidyar Network - Brazil Education Systems Grant"],
    "related_partnerships": [],
    "supporting_funding_opportunities": []
  },
  "quality_indicators": {
    "red_flags": [],
    "green_flags": [
      "Clear problem definition",
      "Past attempts failed for addressable reasons",
      "Decision timeline is specific",
      "Budget authority is clear",
      "Strong value alignment"
    ],
    "walk_away_signals": [],
    "deal_breakers_identified": []
  }
}
```

### Example 2: Funding Intelligence (Medium Confidence)

```json
{
  "intelligence_type": "funding",
  "extraction_metadata": {
    "meeting_date": "2025-11-12",
    "meeting_type": "funder_initial",
    "template_version": "1.0",
    "extraction_date": "2025-11-12",
    "confidence_level": "medium",
    "completeness_score": 0.72,
    "flags": ["decision_intelligence_weak"]
  },
  "funder": {
    "name": "Imaginable Futures",
    "type": "foundation",
    "program_name": "Education Innovation Fund",
    "geographic_focus": "Global, with focus on Brazil and India",
    "website": "https://imaginablefutures.com",
    "total_funding_capacity": "$100M annually"
  },
  "opportunity": {
    "opportunity_type": "grant",
    "funding_amount_range": "$250K - $1M",
    "timeline": "LOI due Jan 15, 2026; Full proposal March 1, 2026; Decisions June 2026",
    "stage": "research",
    "success_likelihood": "medium",
    "competition_level": "High - global competition, ~5% acceptance rate"
  },
  "program_fit": {
    "alignment_score": 4,
    "what_they_really_care_about": "Evidence of systems-level change (not just pilot projects). They want to see government adoption and sustainability plan from day one.",
    "stated_priorities": "Innovation, equity, scale, sustainability",
    "unstated_priorities": "Strong partnership with government or large institutions. Previous grantees all had government partnerships.",
    "our_fit_strengths": "Strong municipal government partnerships, track record of government adoption, sustainability focus",
    "our_fit_gaps": "Haven't worked at national scale yet (all municipal), limited evidence of replication across contexts",
    "competitive_advantage": "Deep Brazil experience, government relationships, capacity-building approach"
  },
  "decision_intelligence": {
    "decision_makers": ["Sarah Kim (Program Officer, Imaginable Futures)"],
    "decision_process": "Program officer reviews LOIs, selects for full proposals. Investment committee makes final decision. Board approval is formality.",
    "decision_timeline": "LOI decisions by Feb 15, final decisions by June 30",
    "evaluation_criteria": "Systems impact, sustainability, partnership quality, evidence base, team capacity",
    "past_grantees_pattern": "Majority are research institutions or NGOs with 10+ years track record and government partnerships",
    "funding_cycle": "Annual",
    "board_dynamics": "Not discussed - unclear"
  },
  "relationship_intelligence": {
    "relationship_status": "new",
    "relationship_temperature": "cool",
    "trust_level": "low",
    "last_interaction_date": "2025-11-12",
    "interaction_history": "First conversation - 30 min intro call",
    "political_considerations": "We don't have warm connections. Sarah seemed interested but reserved.",
    "warm_intro_paths": "Could ask Roberto Santos (InovaEduK) - he knows someone on their advisory board"
  },
  "strategic_positioning": {
    "our_positioning": "Position as 'government-partnership specialists' not 'consultants.' Emphasize sustainability through capacity building.",
    "narrative_frame": "Frame around 'systemic capacity building that governments adopt' not 'innovative interventions'",
    "proof_points_needed": "3-5 examples of government adoption, sustainability data from past projects, replication evidence",
    "differentiation_strategy": "Unique combination of: (1) deep government relationships, (2) teacher capacity focus, (3) Brazil expertise",
    "risk_mitigation": "Address scale concern by showing replication framework, not just single-city success",
    "coalition_strategy": "Consider partnering with university research partner to strengthen evidence base"
  },
  "next_steps": {
    "immediate_actions": [
      "Review past grantee list and analyze patterns",
      "Reach out to Roberto for warm intro to advisory board member",
      "Draft LOI outline for internal review",
      "Gather sustainability and government adoption evidence"
    ],
    "owner_360": "Michael Rodriguez",
    "deadlines": "LOI due Jan 15, 2026",
    "deliverables_needed": "LOI (3 pages), budget narrative, theory of change",
    "research_needed": "What makes LOIs successful? What evidence do they value most?",
    "relationship_building_actions": "Get warm intro, share our municipal government case studies"
  },
  "cross_linking": {
    "decision_makers_stakeholders": ["Sarah Kim (Program Officer, Imaginable Futures)"],
    "supporting_partnerships": [
      "InovaEduK - Educational Systems Partnership",
      "MinEduc Collaboration"
    ],
    "related_funding": [],
    "coalition_partners": []
  },
  "quality_indicators": {
    "green_flags": [
      "Strong program fit on sustainability",
      "Government partnerships are valued",
      "Our Brazil experience is relevant"
    ],
    "red_flags": [
      "Highly competitive (5% acceptance)",
      "No warm intro yet",
      "Scale gap (municipal vs national)",
      "Short track record compared to past grantees"
    ],
    "likelihood_score": 40,
    "confidence_rationale": "Medium confidence because decision process details were limited and we don't have full picture of evaluation criteria"
  }
}
```

### Example 3: Stakeholder Intelligence (High Confidence)

```json
{
  "intelligence_type": "stakeholder",
  "extraction_metadata": {
    "meeting_date": "2025-11-10",
    "meeting_type": "partnership_new",
    "template_version": "1.0",
    "extraction_date": "2025-11-10",
    "confidence_level": "high",
    "completeness_score": 0.91,
    "flags": []
  },
  "person": {
    "name": "Maria Silva",
    "current_role": "CEO, InovaEduK",
    "organization": "InovaEduK",
    "previous_roles": "Director of Innovation at State Education Secretariat (São Paulo), Teacher for 10 years",
    "geographic_location": "São Paulo, Brazil",
    "language": "Portuguese (native), English (fluent)",
    "linkedin": "https://linkedin.com/in/mariasilva-inovaeduk",
    "email": "maria@inovaeduk.com.br",
    "phone": null
  },
  "influence_intelligence": {
    "power_level": "high",
    "influence_scope": "InovaEduK decision-making, Ministry of Education advisory board, São Paulo education tech community",
    "decision_authority": "final",
    "network_influence": "Strong relationships with Ministry officials, 200+ school principals, education tech community in Brazil",
    "reputation": "Respected voice on teacher capacity and education technology implementation",
    "areas_of_expertise": "Teacher professional development, education technology implementation, government partnerships"
  },
  "communication_intelligence": {
    "communication_style": "relational",
    "preferred_channels": "Email for formal communication, WhatsApp for quick questions",
    "response_patterns": "Responds within 24-48 hours, more responsive in mornings (Brazil time)",
    "communication_pace": "moderate",
    "formality_preference": "semiformal",
    "language_preference": "Portuguese for substantive discussions, English OK for brief updates",
    "best_times_to_reach": "Tuesday-Thursday mornings Brazil time"
  },
  "decision_making_intelligence": {
    "decision_style": "consultative",
    "what_they_care_about": "Teacher empowerment, sustainable change (not flash-in-pan pilots), equity for underserved schools, building school leadership capacity",
    "what_motivates_them": "Seeing teachers succeed, creating lasting change in schools, building strong collaborative relationships",
    "what_concerns_them": "Solutions that don't stick after consultants leave, technology without pedagogy, initiatives that burden teachers",
    "evidence_they_need": "Stories from teachers, data on sustainability, examples from similar contexts (Brazilian municipalities preferred)",
    "risk_tolerance": "medium",
    "decision_pace": "deliberate"
  },
  "cultural_intelligence": {
    "cultural_background": "Brazilian, grew up in São Paulo, worked in public education for 15 years",
    "cultural_approach": "relationship_first",
    "relationship_building_pace": "moderate",
    "trust_building_needs": "Multiple conversations, meeting our team, seeing our work firsthand, references from people she trusts",
    "formality_norms": "Semiformal - use first names but maintain professional respect",
    "power_distance": "Low - values collaborative decision-making, flat organizational culture",
    "communication_directness": "Moderately direct - will raise concerns but in considerate way"
  },
  "relationship_intelligence": {
    "relationship_status": "developing",
    "relationship_temperature": "warm",
    "trust_level": "medium",
    "first_contact_date": "2025-11-10",
    "last_interaction_date": "2025-11-10",
    "interaction_frequency": "New relationship - weekly interactions expected during exploration",
    "relationship_trajectory": "improving",
    "relationship_history": "First meeting went very well - strong rapport, shared values, mutual excitement"
  },
  "strategic_intelligence": {
    "their_priorities": "Scaling teacher capacity building to 200+ schools in network, securing sustainable funding model, strengthening Ministry relationships",
    "their_constraints": "Limited budget for external partnerships, small internal team (need external capacity), pressure to show results to board",
    "their_opportunities": "Ministry advisory board position, growing network of schools, reputation in education tech community",
    "their_challenges": "Past partnerships failed to deliver sustainable change, skepticism from teachers about 'another initiative'",
    "how_we_can_help": "Proven capacity-building approach, track record of sustainability, teacher-centered methodology, municipal government experience",
    "what_they_can_help_with": "Introduction to Ministry officials, access to 200+ schools, credibility in Brazil ed tech community",
    "strategic_value_to_us": "high"
  },
  "working_style": {
    "collaboration_style": "Collaborative - values input from team, builds consensus",
    "meeting_preferences": "Likes structured agendas but with time for relationship-building",
    "detail_orientation": "high",
    "follow_through": "Reliable - does what she says she'll do",
    "conflict_approach": "Collaborative - addresses issues directly but tactfully",
    "stress_patterns": "Remains calm under pressure, but communication slows when overwhelmed"
  },
  "next_steps": {
    "immediate_actions": [
      "Send proposal outline by Nov 20",
      "Schedule follow-up meeting with full teams for Nov 25",
      "Connect Maria with Municipal Education contact for reference",
      "Share 2 case studies from similar work"
    ],
    "owner_360": "Jessica Chen",
    "next_interaction_date": "2025-11-25",
    "relationship_building_actions": "Share teacher success stories, introduce her to our program team, visit one of her schools if possible",
    "open_questions": ["What's her exact timeline for Ministry introduction?", "How often does she want updates during exploration phase?"]
  },
  "cross_linking": {
    "associated_partnerships": ["InovaEduK - Educational Systems Partnership"],
    "funding_influence": [],
    "other_stakeholders": ["Roberto Santos (CTO, InovaEduK)"],
    "organizations": ["InovaEduK", "Ministry of Education (advisory board)"]
  },
  "quality_indicators": {
    "red_flags": [],
    "green_flags": [
      "Strong values alignment",
      "Clear communication style",
      "Reliable follow-through",
      "Influential network",
      "Transparent about challenges"
    ],
    "reliability_signals": "Did exactly what she said she'd do (sent follow-up email within 24 hours, shared documents promised)",
    "alignment_signals": "Strong alignment on teacher empowerment, sustainability, equity"
  }
}
```

---

## Related Documentation

- [Cross-Linking Architecture](cross-linking-architecture.md) - How the three intelligence types interconnect
- [Intelligence Extractor README](../README.md) - Overview of the intelligence extraction system
- [Template Selection Guide](../templates/00-template-selection-guide.md) - Choosing the right extraction template
- [Quality Framework](quality-framework.md) - How quality is measured and tracked

---

**Document Version:** 1.0
**Last Updated:** November 2025
**Maintained by:** 360 Intelligence Systems Team
