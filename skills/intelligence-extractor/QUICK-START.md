# Intelligence Extractor - Quick Start

## One-Line Summary
Extract structured partnership, funding, and stakeholder intelligence from meeting transcripts and conversations.

---

## When to Use
- After meeting with potential partners, funders, or key stakeholders
- To process email threads or conversation notes
- To build institutional intelligence database
- When you need to remember important relationship details

---

## 3-Step Quick Use

### 1. Pick Your Template

| Meeting Type | Template Number |
|--------------|----------------|
| 🤝 New partnership meeting | Template 1 |
| 📞 Follow-up with existing partner | Template 2 |
| 💰 First call with funder | Template 3 |
| 📝 Grant application discussion | Template 4 |
| 🏛️ Board/governance meeting | Template 5 |
| 👥 Client working session | Template 6 |
| 🌍 Cross-cultural/international | Template 8 |
| ☕ Quick networking chat | Template 9 |

👉 **See `templates/00-template-selection-guide.md` for full list**

### 2. Extract Intelligence

**Option A: Manual (Claude Code)**
```
Use the intelligence-extractor skill with Template [X] to extract
intelligence from this [meeting type] transcript:

[paste transcript here]
```

**Option B: Automated (Zapier)**
- Transcript auto-saved to Google Drive → Zapier → Claude API → Asana
- See `ZAPIER-INTEGRATION.md` for setup

### 3. Review Output

You'll get JSON with:
- **Partnership Intelligence** - Organizational relationships, decision patterns
- **Funding Intelligence** - Grant opportunities, application strategies
- **Stakeholder Intelligence** - Individual profiles, communication styles

---

## Quick Decision Tree

```
Is this a NEW entity (never met before)?
├─ Yes → action: "create_new"
└─ No → Is this an UPDATE to existing relationship?
    ├─ Yes → action: "update_existing"
    └─ Not sure → action: "flag_for_review"

Is the information CLEAR and DETAILED?
├─ Yes, lots of specific details → confidence: "high"
├─ Some details, some interpretation → confidence: "medium"
└─ Mostly vague or inferred → confidence: "low" + flag for review
```

---

## Three Intelligence Types

### 🤝 Partnership Intelligence
**What:** Organizations you might collaborate with
**Captures:** Decision-making patterns, cultural approach, strategic opportunities
**Example:** Brazilian educational org, relationship-first culture, 3-6 month timeline

### 💰 Funding Intelligence
**What:** Grants, investors, funding programs
**Captures:** Application requirements, decision process, success factors
**Example:** $250K education grant, June deadline, prefers systems-change approach

### 👤 Stakeholder Intelligence
**What:** Individual people who matter strategically
**Captures:** Communication style, decision authority, what they care about
**Example:** Program officer, responsive (replies < 24hrs), data-driven decision-maker

---

## Quality Rules (The 5 Never's)

1. **Never fabricate** - If it's not in the source, use `null`
2. **Never guess confidence** - When uncertain, score low and flag for review
3. **Never paraphrase names** - Use exact names and titles
4. **Never ignore culture** - Capture relationship-building pace, formality, communication norms
5. **Never skip red flags** - Flag conflicts, misalignments, walk-away signals

---

## Cultural Intelligence Quick Reference

**Brazilian Context:**
- Relationship-building before business ✅
- Warmth and personal connection ✅
- Flexibility with time and process ✅
- Hierarchy + relationship warmth ✅

**US Corporate:**
- Efficiency and directness ✅
- Metrics and outcomes focus ✅
- Punctuality and schedule adherence ✅
- Contract before relationship ✅

**Capture these differences!** They drive relationship success.

---

## Output Format (Always)

```json
{
  "extraction_summary": "What you found",
  "intelligence_items": [
    {
      "type": "partnership|funding|stakeholder",
      "confidence": "high|medium|low",
      "action": "create_new|update_existing|flag_for_review",
      // ... schema fields
    }
  ],
  "flagged_for_review": [
    {
      "reason": "Why needs human review",
      "context": "Relevant excerpt",
      "entity": "Name"
    }
  ],
  "extraction_metadata": {
    "source_type": "meeting_transcript|email_thread|notes",
    "source_date": "YYYY-MM-DD",
    "participants": ["Names"],
    "cultural_context": "Detected context"
  },
  "cross_references": [
    {
      "type": "relationship_type",
      "from": "Entity 1",
      "to": "Entity 2",
      "relationship": "Connection description"
    }
  ]
}
```

---

## Common Mistakes to Avoid

❌ **Creating duplicates** - Search first, update if entity exists
❌ **Over-interpreting sparse info** - Low confidence + flag for review instead
❌ **Ignoring ambiguity** - Flag conflicting or unclear information
❌ **Missing cultural context** - Always note relationship-building pace, formality
❌ **Fabricating details** - Better to have `null` than wrong information

---

## What to Flag for Review

- **Low confidence** (< 40%) extractions
- **Ambiguous** information (conflicting signals)
- **Sensitive** situations (conflicts, past harm, broken trust)
- **Complex dynamics** (multi-stakeholder, unclear authority)
- **Legal/compliance** concerns
- **High-stakes** decisions

---

## Integration Paths

### Path 1: Manual (Start Here)
1. Extract intelligence → JSON output
2. Review and validate
3. Copy key insights to notes/Asana
4. **Time:** 10 mins per meeting

### Path 2: Semi-Automated
1. Extract intelligence → JSON output
2. Review and validate
3. Use Asana task templates to create entries
4. **Time:** 5 mins per meeting

### Path 3: Fully Automated (Advanced)
1. Meeting happens → Auto-transcript
2. Zapier → Claude API → JSON
3. Zapier → Creates Asana tasks automatically
4. You review on dashboard
5. **Time:** 2 mins review only

---

## Quality Monitoring (Optional)

If you've deployed the **intelligence-dashboard**:

- 📊 Real-time quality metrics
- 📈 Template performance tracking
- 🎯 Completeness scoring
- 🚨 Flagged items dashboard
- 📉 Trend analysis over time

**Deploy:** See `../../intelligence-dashboard/DEPLOYMENT_GUIDE.md`

---

## Supporting Files

**Essential:**
- `SKILL.md` - Complete extraction logic (read this for deep understanding)
- `README.md` - System overview and implementation guide
- `templates/00-template-selection-guide.md` - Template selection help

**Advanced:**
- `references/intelligence-schemas.md` - Complete JSON schema docs
- `references/cross-linking-architecture.md` - Multi-system integration
- `references/quality-framework.md` - Quality metrics explained
- `.claude/skills/intelligence-extractor/ZAPIER-INTEGRATION.md` - Automation setup

**Examples:**
- `examples/partnership-extraction-example.md`
- `examples/funder-extraction-example.md`
- `examples/stakeholder-extraction-example.md`

---

## Example Use (30 Seconds)

**Input:**
```
Extract intelligence from this new partnership meeting:

Meeting with Dr. Sofia Martinez, Director of InovaEdu Brazil
Date: Nov 20, 2025

First conversation. They work with 40 schools in São Paulo on
systems-level education change. Sofia was warm and relationship-
focused - suggested 2-3 more meetings before discussing projects.
They have government connections but limited funding. She'll intro
us to her board chair next month.

Timeline feels slow - she said "We build trust first, then work."
```

**Output:**
```json
{
  "extraction_summary": "New Brazilian educational partnership, relationship-first approach, early exploration stage",
  "intelligence_items": [
    {
      "type": "partnership",
      "confidence": "high",
      "action": "create_new",
      "organization_name": "InovaEdu Brazil",
      "partnership_type": "Brazilian Educational",
      "primary_contact": "Dr. Sofia Martinez",
      "relationship_temperature": "Warming",
      "cultural_approach": "Relationship-First",
      "decision_timeline": "Deliberate (3-6 months)",
      "relationship_stage": "Exploration",
      ...
    },
    {
      "type": "stakeholder",
      "confidence": "medium",
      "action": "create_new",
      "full_name": "Dr. Sofia Martinez",
      "organization": "InovaEdu Brazil",
      "title_role": "Director",
      "communication_style": "Relational & Warm",
      "cultural_context": "Brazilian",
      ...
    }
  ],
  ...
}
```

---

## Troubleshooting

**Problem:** Extraction is too generic
**Fix:** Use more specific template, add more context

**Problem:** Creating duplicate entities
**Fix:** Use action: "update_existing" for follow-up meetings

**Problem:** Confidence scores seem wrong
**Fix:** Be conservative - when in doubt, score low and flag for review

**Problem:** Missing cultural nuances
**Fix:** Explicitly mention cultural context in prompt, use Template 8 for international

---

## Next Steps

1. ✅ **Try it once** - Pick a recent meeting, extract intelligence
2. ✅ **Review output** - See what's useful, what needs work
3. ✅ **Build habit** - Extract after every important meeting
4. ⏩ **Automate** - Set up Zapier workflow (optional, saves 10+ hrs/month)
5. ⏩ **Deploy dashboard** - Real-time quality monitoring (optional)

---

## Need Help?

- **Template selection:** See `templates/00-template-selection-guide.md`
- **Complete schemas:** See `references/intelligence-schemas.md`
- **Automation setup:** See `.claude/skills/intelligence-extractor/ZAPIER-INTEGRATION.md`
- **Dashboard deployment:** See `../../intelligence-dashboard/DEPLOYMENT_GUIDE.md`
- **Full documentation:** Read `SKILL.md` (comprehensive)

---

**Ready? Pick a recent meeting transcript and extract intelligence now. 🚀**

Version 1.1.0 | Updated: 2025-11-22 | 360 Social Impact Studios
