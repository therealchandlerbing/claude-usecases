# 360 Partnership & Opportunity Intelligence System

A comprehensive workflow for capturing, structuring, and organizing strategic intelligence about partnerships, funding opportunities, and stakeholders.

---

## What This System Does

Transforms unstructured conversations into structured, actionable intelligence:

**Input:** Meeting transcripts, emails, conversation notes
**Output:** Organized intelligence in Asana about:
- **Partnerships** - Organizations, collaboration opportunities, strategic alliances
- **Funding** - Grants, investors, application strategies
- **Stakeholders** - Key individuals, communication styles, decision-making patterns

**Value:** Never lose critical intelligence from important conversations. Build institutional knowledge. Make better strategic decisions.

---

## Quick Start (5 Minutes)

### Try It Manually

1. **Find a recent meeting transcript** (any conversation with a partner, funder, or important stakeholder)

2. **Use the intelligence-extractor skill:**
   ```
   Open Claude Code, paste your transcript, and say:
   "Use the intelligence-extractor skill to extract partnership and stakeholder intelligence from this meeting transcript."
   ```

3. **Review the JSON output** - See what intelligence was captured

4. **Copy relevant insights** to your notes or Asana

That's it! You've extracted intelligence.

---

## Full Implementation (4-6 Weeks)

### Phase 1: Manual Intelligence Capture (Week 1-2)

**Goal:** Start using the skill, build the habit

**Steps:**
1. ✅ Read [SKILL.md](SKILL.md) to understand intelligence schemas
2. ✅ After important meetings, use skill to extract intelligence
3. ✅ Review outputs, note what's useful
4. ✅ Start manually adding intelligence to your notes

**Time:** 5-10 minutes per meeting
**Benefit:** Immediate intelligence capture

---

### Phase 2: Set Up Asana Intelligence Databases (Week 2-3)

**Goal:** Create structured home for intelligence

**Steps:**
1. ✅ Read [ASANA-SETUP.md](ASANA-SETUP.md)
2. ✅ Create three Asana projects:
   - Partnership Intelligence Hub
   - Funding Opportunity Intelligence
   - Stakeholder Intelligence Database
3. ✅ Set up custom fields, sections, templates (detailed in guide)
4. ✅ Create 5-10 initial tasks to populate system

**Time:** 3-4 hours initial setup
**Benefit:** Centralized, searchable intelligence repository

---

### Phase 3: Integrate Manual Workflow (Week 3-4)

**Goal:** Connect skill output to Asana databases

**Steps:**
1. ✅ After meetings, use intelligence-extractor skill
2. ✅ Review JSON output
3. ✅ Create/update Asana tasks from extracted intelligence
4. ✅ Populate custom fields
5. ✅ Build the habit

**Time:** 10-15 minutes per meeting
**Benefit:** Consistent, comprehensive intelligence capture

---

### Phase 4: Automate with Zapier (Week 4-6, Optional)

**Goal:** Hands-free intelligence extraction

**Steps:**
1. ✅ Read [ZAPIER-INTEGRATION.md](ZAPIER-INTEGRATION.md)
2. ✅ Set up Zapier workflow:
   - Trigger: New transcript in Google Drive
   - Action: Send to Claude API with intelligence-extractor
   - Action: Parse JSON response
   - Action: Create/update Asana tasks
3. ✅ Test with sample transcripts
4. ✅ Enable for all meetings

**Time:** 4-6 hours initial setup
**Benefit:** Automatic intelligence capture, 10+ hours saved per month

---

## System Components

### 1. Intelligence Extractor Skill

**File:** [SKILL.md](SKILL.md)

**Purpose:** Claude skill that analyzes conversations and extracts structured intelligence

**Includes:**
- Three intelligence schemas (Partnership, Funding, Stakeholder)
- Extraction guidelines and quality rules
- Pattern recognition frameworks
- Cultural intelligence capture
- Confidence scoring system

**Use:** Manually via Claude Code or automated via Zapier

---

### 2. Extraction Templates

**Folder:** `templates/`

**Purpose:** Specialized prompts for different meeting types to maximize extraction quality

**Available Templates:**
- `template-1-partnership-new.md` - First partnership meetings
- `template-2-partnership-existing.md` - Follow-ups with existing partners
- `template-3-funder-initial.md` - Initial funder conversations
- `template-4-funder-application.md` - Grant application discussions
- `template-5-board-meeting.md` - Board/governance meetings
- `template-6-client-sprint.md` - Client working sessions
- `template-7-community-stakeholder.md` - Community leader meetings
- `template-8-international-partner.md` - Cross-cultural contexts
- `template-9-conference-networking.md` - Brief networking interactions
- `template-10-crisis-problemsolving.md` - Emergency or conflict meetings

**Use:** Reference appropriate template when extracting intelligence for better results

---

### 3. Asana Intelligence Databases

**File:** [ASANA-SETUP.md](ASANA-SETUP.md)

**Purpose:** Structured projects in Asana to store, organize, and access intelligence

**Three Projects:**

#### Partnership Intelligence Hub
- Track organization relationships
- Capture decision-making patterns
- Store strategic positioning approaches
- Monitor relationship health

#### Funding Opportunity Intelligence
- Track funding sources and programs
- Capture application requirements
- Store decision process intelligence
- Monitor application pipeline

#### Stakeholder Intelligence Database
- Profile key individuals
- Capture communication styles
- Store decision-making patterns
- Monitor relationship stages

**Features:**
- Custom fields for structured data
- Task templates for consistency
- Automation rules for workflow efficiency
- Multiple views for different purposes

---

### 4. Zapier Automation Workflow

**File:** [ZAPIER-INTEGRATION.md](ZAPIER-INTEGRATION.md)

**Purpose:** Automate the entire intelligence extraction and storage workflow

**Flow:**
```
Meeting happens
  ↓
Fathom creates transcript
  ↓
Saves to Google Drive
  ↓
Zapier detects new file
  ↓
Sends to Claude API (intelligence-extractor skill)
  ↓
Claude extracts structured intelligence
  ↓
Zapier parses JSON response
  ↓
Creates/updates Asana tasks automatically
  ↓
You review and refine
```

**Benefits:**
- Zero manual data entry
- Consistent intelligence capture
- Saves 15-20 minutes per meeting
- Never miss important intelligence

---

## File Structure

```
intelligence-extractor/
├── README.md (this file)
├── SKILL.md (main skill documentation)
├── ASANA-SETUP.md (Asana project setup guide)
├── ZAPIER-INTEGRATION.md (automation workflow guide)
├── templates/
│   ├── template-1-partnership-new.md
│   ├── template-2-partnership-existing.md
│   ├── template-3-funder-initial.md
│   └── ... (10 templates total)
└── examples/
    └── (sample extractions for reference)
```

---

## Key Concepts

### Intelligence Types

**Partnership Intelligence:**
- Organizational relationships, not individual people
- Strategic opportunities and hesitations
- Decision-making processes
- Cultural communication patterns

**Funding Intelligence:**
- Specific funding opportunities or programs
- Application requirements and strategies
- Decision processes and timelines
- Program officer relationships

**Stakeholder Intelligence:**
- Individual people, not organizations
- Communication styles and preferences
- Decision-making patterns
- Power dynamics and influence

### Confidence Levels

**High (75-100%):** Multiple clear indicators, enough detail, consistent information
**Medium (50-74%):** Some indicators, partial information, some ambiguity
**Low (0-39%):** Minimal information, mostly interpretation, should be reviewed by human

### Actions

**create_new:** New entity not yet in system
**update_existing:** Updates to existing entity
**flag_for_review:** Needs human judgment due to ambiguity or sensitivity

---

## Usage Patterns

### For New Partnerships

1. After first meeting → Extract partnership + stakeholder intelligence
2. Create Asana tasks in Partnership Hub + Stakeholder DB
3. Before second meeting → Review intelligence, prepare questions
4. After second meeting → Update existing tasks with new insights
5. Build comprehensive profile over multiple interactions

### For Funding Opportunities

1. Initial conversation → Extract funding + stakeholder (program officer) intelligence
2. Create task in Funding Intelligence project
3. Research phase → Add to intelligence (past grantees, requirements, etc.)
4. Application phase → Reference intelligence for positioning
5. Post-decision → Capture lessons learned (win or lose)

### For Stakeholder Profiling

1. After any meaningful interaction → Extract stakeholder intelligence
2. Build profile over time (multiple interactions = richer profile)
3. Before important meeting → Review profile, prepare approach
4. After interaction → Update with new observations
5. Reference when planning engagement strategies

---

## Best Practices

### Do's ✅

- **Extract immediately after meetings** while details are fresh
- **Review and edit** extracted intelligence (don't trust blindly)
- **Update existing profiles** rather than creating duplicates
- **Capture cultural context** (relationship-building pace, communication norms)
- **Note what's NOT said** (silences, avoidances, hesitations matter)
- **Link related entities** (stakeholder → partnership → funder)
- **Provide feedback** to improve future extractions

### Don'ts ❌

- **Don't fabricate** information that's not in the source
- **Don't over-interpret** low-confidence signals
- **Don't skip cultural context** (it drives relationship success)
- **Don't create duplicate tasks** (search first, update if exists)
- **Don't ignore red flags** (capture walk-away signals honestly)
- **Don't let intelligence go stale** (update Last Interaction dates)

---

## Example Use Cases

### Use Case 1: Brazilian Educational Partnership

**Situation:** First meeting with potential Brazilian educational partner

**Process:**
1. Meeting happens (relationship-building focus, warm but formal)
2. Use intelligence-extractor with "partnership-new" context
3. Extracts:
   - Partnership intelligence (relationship-first culture, deliberate timeline, systems-change orientation)
   - Stakeholder profiles (CEO and Partnerships Director)
4. Create Asana tasks in both projects
5. Before second meeting, review intelligence → prepare appropriate relationship-building approach
6. Result: Culturally appropriate engagement, stronger relationship

### Use Case 2: US Foundation Funding

**Situation:** Program officer call about potential grant

**Process:**
1. Conversation about program, requirements, decision process
2. Use intelligence-extractor with "funder-initial" context
3. Extracts:
   - Funding opportunity intelligence (competitive, site visit offered, board priorities)
   - Program officer profile (responsive, helpful, moderate influence)
4. Create tasks, populate application strategy section
5. Reference intelligence when writing LOI
6. Result: Stronger application, 15% → secured funding

### Use Case 3: Board Meeting Intelligence

**Situation:** Quarterly board meeting with multiple decision-makers

**Process:**
1. Meeting with 8 board members discussing strategy
2. Use intelligence-extractor with "board-meeting" context
3. Extracts:
   - 8 stakeholder profiles (different communication styles, priorities, influence levels)
   - Board dynamics patterns (decision-making culture, power structure)
4. Create/update stakeholder profiles for each board member
5. Before next meeting, review who needs what kind of information
6. Result: More effective board engagement, better decision outcomes

---

## Metrics & ROI

### Time Savings

**Manual Intelligence Capture (before system):**
- 0-5 minutes (usually forgot to do it)
- Inconsistent quality
- Lost intelligence over time

**With Intelligence Extractor:**
- 10 minutes manual (consistent, comprehensive)
- 0 minutes automated (if using Zapier)
- Permanent, searchable, structured

**Monthly Savings (40 meetings):**
- Manual: 40 × 10 min = ~7 hours/month
- Automated: Essentially zero time, infinite ROI

### Quality Improvements

- **Consistency:** Every meeting captured the same way
- **Completeness:** Comprehensive schemas ensure nothing missed
- **Usability:** Structured data = searchable, filterable, actionable
- **Learning:** Patterns emerge across partnerships, funders, stakeholders
- **Institutional knowledge:** Intelligence persists beyond individual memory

### Decision Improvements

- Better partnership positioning (cultural intelligence)
- Higher funding success rates (application strategy intelligence)
- More effective stakeholder engagement (communication style intelligence)
- Faster relationship building (pattern recognition)
- Fewer costly mistakes (red flags captured early)

---

## Troubleshooting

### "Extraction is too generic"

**Problem:** Intelligence lacks specific, actionable details

**Solutions:**
- Use more specific extraction template for meeting type
- Include more context in prompt (meeting type, participants, history)
- Review source transcript - is it detailed enough?
- Manually add specificity after extraction

### "Confidence levels seem wrong"

**Problem:** High confidence for sparse information or low confidence for good information

**Solutions:**
- Provide feedback via quality ratings
- System learns and calibrates over time
- Adjust confidence thresholds in automation
- Review confidence scoring guidelines in SKILL.md

### "Creating duplicate tasks"

**Problem:** New task created when should have updated existing

**Solutions:**
- Search Asana before creating (manually)
- Improve Zapier search logic (automated)
- Use consistent naming conventions
- Link related tasks in descriptions

### "Missing cultural context"

**Problem:** Extraction doesn't capture cultural nuances

**Solutions:**
- Explicitly mention cultural context in prompt
- Use international partner template for cross-cultural meetings
- Add cultural context manually after extraction
- Provide feedback to improve template

---

## Advanced Topics

### Quality Feedback Loop

(See separate documentation when implementing)

- Automated quality scoring
- User feedback capture
- Template improvement system
- A/B testing framework

### Pattern Library Development

As you accumulate intelligence:
- Extract recurring patterns
- Document in Pattern Library sections
- Reference patterns for new situations
- Build institutional knowledge

### Cross-Referencing Intelligence

Connect related entities:
- Stakeholder works at Partner organization
- Funder interested in Partnership
- Multiple Stakeholders from same organization
- Overlapping networks

### Custom Field Analytics

Use Asana reporting to analyze:
- Partnership success rates by type
- Funding win rates by funder type
- Relationship temperature trends
- Decision timeline patterns

---

## Roadmap & Future Enhancements

### Current Version (1.0)
- ✅ Manual intelligence extraction
- ✅ Three intelligence schemas
- ✅ 10 specialized templates
- ✅ Asana integration (manual)
- ✅ Zapier automation workflow

### Future Enhancements (1.x)
- Enhanced multi-language support (Spanish, other languages)
- CRM integration (link to contacts)
- Email signature extraction (auto-capture contact info)
- Calendar integration (auto-context from meeting invites)
- Voice note intelligence extraction

### Future Enhancements (2.0)
- Predictive intelligence (suggest next actions based on patterns)
- Relationship health scoring (automated risk detection)
- Network mapping (visualize stakeholder connections)
- Intelligence dashboards (trends, insights, alerts)
- Team collaboration features (shared intelligence, annotations)

---

## Getting Help

### Documentation
1. Read [SKILL.md](SKILL.md) for extraction details
2. Read [ASANA-SETUP.md](ASANA-SETUP.md) for database setup
3. Read [ZAPIER-INTEGRATION.md](ZAPIER-INTEGRATION.md) for automation
4. Check template files for meeting-specific guidance

### Support
- Create task in "Intelligence System Improvements" Asana project
- Document issues, suggestions, questions
- Share learnings with team

### Contributing
- Suggest template improvements based on usage
- Share successful extraction examples
- Document new patterns discovered
- Provide feedback on quality and usefulness

---

## License & Credits

**Created by:** 360 Social Ventures
**Version:** 1.0.0
**Date:** March 2025
**Powered by:** Claude (Anthropic), Asana, Zapier

---

## Final Thoughts

**Intelligence is the difference between reacting and anticipating.**

This system transforms scattered conversation notes into a structured intelligence asset. It helps you:

- **Remember** what matters from every conversation
- **Recognize** patterns across partnerships, funders, stakeholders
- **Respond** with culturally appropriate, strategically informed approaches
- **Build** institutional knowledge that persists beyond individual memory

Start small. Extract intelligence from one meeting. See the value. Build the habit. Scale gradually.

The intelligence you capture today becomes the insight that guides your decisions tomorrow.

**Ready to start? Pick a recent meeting transcript and use the intelligence-extractor skill.**

---

*Questions? Ideas? Feedback? Document in Asana or reach out to the team.*
