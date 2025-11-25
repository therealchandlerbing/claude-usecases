# Post-Meeting Wrap-Up

**Workflow Template**: Meeting intelligence capture and task creation

---

## Workflow Steps

Execute the following skills in sequence after any important meeting:

### Step 1: Extract Intelligence
**Skill**: `intelligence-extractor`

Analyze the meeting transcript/notes for:
- Partnership intelligence (organizations, collaboration opportunities)
- Funding signals (grants, investors, programs mentioned)
- Stakeholder intelligence (key people, decision-makers, influencers)
- Commitments made (by us and by them)
- Cross-references between entities

### Step 2: Create Action Items
**Skill**: `skill-orchestrator` → Asana integration

Transform extracted intelligence into actionable tasks:
- Create Asana tasks for each commitment/action item
- Assign owners and due dates
- Link to relevant projects
- Tag with meeting context

### Step 3: Generate Meeting Summary
**Skill**: `ceo-advisor` (Chief Intelligence Officer mode)

Produce executive summary including:
- Key decisions made
- Strategic implications
- Relationship temperature update
- Recommended follow-up timing
- Risk flags or opportunities identified

---

## Required Input

Provide one of:
- Meeting transcript (from Fathom, Otter, etc.)
- Meeting notes (manual or shared doc)
- Audio file path (if transcription needed)

---

## Output Deliverables

1. **Intelligence Extract** (JSON)
   - Structured data for database entry
   - Partnership/funding/stakeholder records

2. **Task List** (Asana-ready)
   - Action items with owners and dates
   - Follow-up reminders scheduled

3. **Executive Summary** (Markdown)
   - 1-page meeting debrief
   - Strategic context and implications

4. **Relationship Update** (if applicable)
   - Updated stakeholder temperature
   - Next engagement recommendation

---

## Execution Instructions

1. User provides meeting transcript or notes
2. Run intelligence extraction (5-10 min)
3. Review extracted items with user for accuracy
4. Create tasks in Asana (2-5 min)
5. Generate executive summary (3-5 min)
6. Update CRM/relationship tracker if relevant

---

## Customization Options

**Quick Mode** (10 min):
- Extract + task list only

**Standard Mode** (15-20 min):
- Full extraction + tasks + summary

**Deep Mode** (25-30 min):
- Everything + relationship database update + follow-up email drafts

---

## Trigger Phrases

- "Wrap up this meeting"
- "Process meeting transcript"
- "Extract action items from meeting"
- "Meeting follow-up"
- "What came out of that meeting?"

---

**Skills Used**: intelligence-extractor, skill-orchestrator, ceo-advisor
**Estimated Time**: 10-30 minutes depending on mode
**Best Time**: Immediately after meeting while context is fresh
