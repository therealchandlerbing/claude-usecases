# Intelligence Extractor - Quick Start

## One-Line Summary
Extract structured partnership, funding, and stakeholder intelligence from unstructured conversations and store in Asana.

---

## When to Use
- After meetings with partners, funders, or stakeholders
- To process email threads or meeting notes
- To build searchable intelligence database in Asana
- When you need to remember strategic relationship details

---

## 5-Minute Quick Use

### Step 1: Identify Meeting Type

| Meeting Type | Focus |
|--------------|-------|
| 🤝 New partnership exploration | Organizations, collaboration opportunities |
| 💰 Funder conversation | Grants, funding programs, application strategy |
| 👤 Stakeholder interaction | Individual profiles, decision-making patterns |
| 🏛️ Board/governance meeting | Multiple stakeholders, group dynamics |
| 🌍 Cross-cultural meeting | International partners, cultural intelligence |

### Step 2: Provide Context + Transcript

```
Use the intelligence-extractor skill to extract intelligence from this
[meeting type] with [organization/person]:

[Paste your transcript, email thread, or notes here]
```

### Step 3: Review JSON Output

You'll get structured JSON with three possible intelligence types:

- **Partnership Intelligence** → Create task in "Partnership Intelligence Hub" (Asana)
- **Funding Intelligence** → Create task in "Funding Opportunity Intelligence" (Asana)
- **Stakeholder Intelligence** → Create task in "Stakeholder Intelligence Database" (Asana)

---

## Three Intelligence Types

### 🤝 Partnership Intelligence (Organizations)
**Captures:**
- Decision-making patterns and timelines
- Cultural communication approach
- Strategic opportunities and hesitations
- Relationship temperature and stage

**Example:** Brazilian educational nonprofit, relationship-first culture, 3-6 month decision timeline, systems-change focus

---

### 💰 Funding Intelligence (Opportunities)
**Captures:**
- Funding amount, deadlines, decision process
- Application requirements and success factors
- Program officer relationships
- Positioning strategy and fit assessment

**Example:** $250K education systems grant, June deadline, site visit offered, board values sustainability

---

### 👤 Stakeholder Intelligence (People)
**Captures:**
- Communication style and preferences
- Decision authority and influence
- What they care about strategically
- Do's and don'ts for working relationship

**Example:** Program officer, responds < 24 hrs, data-driven, moderate influence, needs impact metrics

---

## Quick Decision Rules

### Confidence Scoring
- **High (70-100%):** Lots of specific details, names, dates, clear statements
- **Medium (40-69%):** Some details, some interpretation, partial info
- **Low (0-39%):** Minimal details, mostly inference → FLAG FOR REVIEW

### Action Determination
- **create_new:** First mention of entity, introductory meeting
- **update_existing:** Follow-up meeting, references past interactions
- **flag_for_review:** Ambiguous, conflicting info, or sensitive

---

## The 5 Never's (Quality Rules)

1. **Never fabricate** - If not in source, use `null`
2. **Never paraphrase names** - Use exact names and titles
3. **Never skip cultural context** - Capture relationship pace, formality, communication style
4. **Never ignore red flags** - Flag misalignments, conflicts, walk-away signals
5. **Never guess when uncertain** - Low confidence + flag for review

---

## Cultural Intelligence Quick Ref

**Brazilian Context:**
- ✅ Relationship-building before business discussions
- ✅ Warmth, personal connection, "jeitinho" problem-solving
- ✅ Flexible with time, deliberate decision-making
- ✅ Hierarchy + relationship warmth

**US Corporate:**
- ✅ Efficiency, directness, metrics-focused
- ✅ Punctuality, schedule adherence
- ✅ Contract before relationship, fast decisions

**Capture these differences!** They determine relationship success.

---

## Output Format

Always output valid JSON:

```json
{
  "extraction_summary": "Brief overview",
  "intelligence_items": [
    {
      "type": "partnership|funding|stakeholder",
      "confidence": "high|medium|low",
      "action": "create_new|update_existing|flag_for_review",
      // Type-specific schema fields...
    }
  ],
  "flagged_for_review": [
    {
      "reason": "Why human review needed",
      "context": "Relevant excerpt",
      "entity": "Entity name"
    }
  ],
  "extraction_metadata": {
    "source_type": "meeting_transcript|email_thread|notes",
    "source_date": "YYYY-MM-DD",
    "participants": ["Names"],
    "cultural_context": "Context"
  },
  "cross_references": [
    {
      "type": "Relationship type",
      "from": "Entity 1",
      "to": "Entity 2",
      "relationship": "Connection"
    }
  ]
}
```

---

## Flag for Review When...

- 🚨 Confidence < 40%
- 🚨 Ambiguous or conflicting information
- 🚨 Sensitive situations (conflicts, past harm, broken trust)
- 🚨 Complex multi-stakeholder dynamics
- 🚨 Legal or compliance concerns
- 🚨 Unclear which existing entity to update

---

## Integration Workflows

### Manual Workflow (10 mins)
1. Run intelligence-extractor skill
2. Review JSON output
3. Create Asana tasks in appropriate project
4. Populate custom fields from JSON
5. Add to correct section

### Automated Workflow (0 mins - Zapier)
1. Meeting transcript → Google Drive
2. Zapier detects new file
3. Sends to Claude API with skill
4. Parses JSON response
5. Creates/updates Asana tasks automatically

👉 **See ZAPIER-INTEGRATION.md for automation setup**

---

## Asana Integration

### Three Asana Projects

1. **Partnership Intelligence Hub**
   - Sections: Initial Contact, Exploration, Negotiation, Active Partnership
   - Custom fields: Relationship Temperature, Decision Timeline, Cultural Approach

2. **Funding Opportunity Intelligence**
   - Sections: Watching, Considering, Applying, Submitted, Decided
   - Custom fields: Funding Amount, Deadline, Decision Timeline, Fit Assessment

3. **Stakeholder Intelligence Database**
   - Sections: By Stakeholder Type, By Relationship Stage
   - Custom fields: Communication Style, Decision Authority, Strategic Value

👉 **See ASANA-SETUP.md for complete configuration**

---

## Example Extraction (1 Minute)

**Input:**
```
Meeting with Maria Silva, CEO of InovaEduK (Brazilian educational org)
Date: March 10, 2025

First conversation. They're exploring systems-level educational change
in São Paulo. Maria was warm, relationship-oriented, suggested meeting
2-3 more times before discussing specific projects. They work with 50
schools but want to expand. Limited funding. Maria will intro us to
board chair next month.

Decision timeline seems slow - she said "We like to build trust first."
```

**Output Includes:**
- Partnership Intelligence for InovaEduK (high confidence)
  - Relationship-first cultural approach
  - Deliberate (3-6 month) decision timeline
  - Systems-change orientation
  - Funding needs
- Stakeholder Intelligence for Maria Silva (medium confidence)
  - Relational & warm communication style
  - Brazilian cultural context
  - Decision-maker with board influence

---

## Common Mistakes

❌ Creating duplicate tasks (search Asana first!)
❌ Over-interpreting sparse information (use low confidence instead)
❌ Ignoring cultural context (it drives relationship success!)
❌ Fabricating details not in source (use `null` instead)
❌ Missing cross-references (note connections between entities)

---

## Schemas Quick Reference

**Partnership Schema Highlights:**
- organization_name, partnership_type
- relationship_temperature, cultural_approach, decision_timeline
- opening_opportunities, strategic_qualification_questions
- common_hesitations, strategic_framing
- walk_away_signals

**Funding Schema Highlights:**
- funder_name, program_name, funder_type
- funding_amount_range, deadlines
- decision_intelligence, positioning_strategy
- requirements_mentioned, success_factors
- fit_assessment, red_flags

**Stakeholder Schema Highlights:**
- full_name, organization, title_role, stakeholder_type
- communication_style, communication_preferences
- cultural_context, cultural_communication_notes
- decision_authority, decision_making_intelligence
- what_they_care_about, strategic_value
- do_list, dont_list

👉 **See SKILL.md for complete schemas**

---

## Troubleshooting

**"Extraction too generic"**
→ Add more context about meeting type, participants, history

**"Creating duplicates"**
→ Use action: "update_existing" for follow-ups
→ Search Asana before creating new tasks

**"Missing cultural nuances"**
→ Explicitly mention cultural context in prompt
→ Note relationship-building pace, formality, communication style

**"Confidence seems wrong"**
→ Be conservative - when in doubt, score low and flag for review

---

## Next Steps

1. ✅ **Try once** - Extract from recent meeting
2. ✅ **Review** - Check JSON quality and completeness
3. ✅ **Create Asana tasks** - Manual or template-based
4. ⏩ **Set up Asana projects** - See ASANA-SETUP.md
5. ⏩ **Automate** - Zapier workflow saves 15 mins/meeting

---

## Supporting Files

**Setup & Implementation:**
- `README.md` - Full system overview and implementation plan
- `ASANA-SETUP.md` - Step-by-step Asana project configuration
- `ZAPIER-INTEGRATION.md` - Automation workflow setup
- `SKILL.md` - Complete extraction logic and schemas

**Templates:** (in `templates/` directory)
- Partnership exploration templates
- Funder conversation templates
- Stakeholder meeting templates
- Board meeting templates
- International partner templates
- And more...

---

**Ready to start? Pick a recent conversation and extract intelligence now. 🚀**

Version 1.0.0 | Updated: 2025-11-22 | 360 Social Ventures
