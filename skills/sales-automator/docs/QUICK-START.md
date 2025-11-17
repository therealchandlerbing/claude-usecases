# Sales Automator Quick Start Guide

Get up and running with sales automation in 15 minutes.

## Prerequisites

Before using this skill, ensure you have:

- ✓ Asana workspace with "Sales Pipeline" project set up
- ✓ Gmail access enabled in Claude
- ✓ Google Drive access enabled in Claude
- ✓ Google Calendar access enabled in Claude

## 5-Minute Setup

### Step 1: Create Sales Pipeline Project in Asana

1. Log into Asana
2. Create new project called "Sales Pipeline"
3. Add custom fields:
   - **Deal Stage** (Dropdown): Outreach, Discovery, Proposal, Negotiation, Closed-Won, Closed-Lost
   - **Deal Value** (Number)
   - **Close Date** (Date)
   - **Lead Source** (Dropdown): Inbound, Outbound Cold, Referral, Partnership, Event, Content
   - **Next Action** (Text)

4. Create default sections:
   - Hot Leads
   - Warm Leads
   - Cold Leads
   - Closed Won
   - Closed Lost

### Step 2: Prepare Email Templates

Copy the templates from [REFERENCE.md](../references/REFERENCE.md) into a Google Doc for easy reference.

### Step 3: Gather Case Studies

Create a folder in Google Drive called "Sales Assets" with:
- Case studies (1-pagers)
- Client testimonials
- Proposal templates
- Pitch decks

### Step 4: Test Connection

In Claude, try this command:
```
Hey Claude, use sales-automator to check my Sales Pipeline in Asana and tell me what deals are currently active.
```

Claude should:
1. Find your Asana workspace
2. Locate the Sales Pipeline project
3. List active deals

If this works, you're ready to go!

---

## Your First Campaign (10 Minutes)

### Scenario: Cold Outreach to New Prospect

**Step 1: Trigger the skill**
```
Claude, I need to create cold outreach for [Company Name]. They're a [industry] company and I want to pitch [your offering].
```

**Step 2: Provide context when asked**
Answer any questions Claude asks about:
- Target contact (if known)
- Your value proposition
- Similar customers you've worked with
- Urgency or timing

**Step 3: Review & refine**
Claude will deliver:
- Complete email sequence (5 touches)
- A/B tested subject lines
- Asana deal task created
- Follow-up schedule

Review and ask for adjustments:
```
Can you make Email 2 more concise?
Can you add a case study mention in Email 3?
Change the tone to be more casual.
```

**Step 4: Send & track**
1. Copy Email 1 into your email client
2. Send to prospect
3. Mark subtask "Email 1 Sent" as complete in Asana
4. Wait for response or scheduled follow-up date

---

## Common Use Cases

### Use Case 1: Cold Outreach Sequence

**Trigger**: "Create cold outreach for [Company]"

**What Claude does**:
1. Researches company via web search
2. Identifies decision-makers
3. Checks for past interactions
4. Generates 5-email sequence
5. Creates Asana deal task

**Your action**:
- Send emails according to schedule
- Update Asana when prospect responds
- Book discovery meeting if they engage

---

### Use Case 2: Follow-Up to Warm Lead

**Trigger**: "Follow up with [Name] at [Company] about [topic]"

**What Claude does**:
1. Searches past conversations for context
2. Checks Gmail for email history
3. Reviews Calendar for meeting history
4. Generates contextualized follow-up
5. Updates Asana deal task

**Your action**:
- Review Claude's research for accuracy
- Send follow-up email
- Schedule next touch if no response

---

### Use Case 3: Check Pipeline Health

**Trigger**: "What deals are stuck in pipeline?" OR "Check Sales Pipeline"

**What Claude does**:
1. Pulls all deals from Asana
2. Identifies deals exceeding time thresholds for stage
3. Suggests re-engagement approach for stuck deals
4. Generates pipeline health report

**Your action**:
- Review stuck deals
- Ask Claude to generate re-engagement sequences
- Update deal stages as needed

---

### Use Case 4: Generate Proposal

**Trigger**: "Create proposal for [Company] partnership"

**What Claude does**:
1. Searches past conversations for context
2. Pulls relevant case studies from Drive
3. Checks Asana for deal details
4. Generates structured proposal using template

**Your action**:
- Review and customize proposal
- Add pricing specifics
- Send to prospect
- Update deal stage to "Proposal" in Asana

---

### Use Case 5: Competitive Research

**Trigger**: "Research [Company] for partnership opportunity"

**What Claude does**:
1. Web search for company overview, news, leadership
2. Identifies strategic priorities
3. Researches competitors and positioning
4. Surfaces industry context
5. Generates intelligence brief

**Your action**:
- Review research
- Use insights to personalize outreach
- Ask Claude to generate email sequence with research incorporated

---

## Quick Command Reference

### Email Sequences
```
"Create cold outreach for [Company]"
"Generate warm follow-up for [Name]"
"Write re-engagement email for stuck deal with [Company]"
"Draft breakup email for [Prospect]"
```

### Research
```
"Research [Company] for partnership"
"Find decision-makers at [Company]"
"What's the competitive landscape for [Company]?"
"Analyze [Company]'s recent news"
```

### Pipeline Management
```
"Check Sales Pipeline"
"What deals are stuck?"
"Show me hot leads"
"Forecast pipeline for Q4"
"Update [Company] deal to Proposal stage"
```

### Proposals & Case Studies
```
"Create proposal for [Company]"
"Write one-pager case study for [Client]"
"Generate ROI calculation for [Prospect]"
```

### Performance Analysis
```
"Analyze outreach performance this month"
"What's our win rate?"
"Which emails are getting best response rates?"
"Show me conversion rates by stage"
```

---

## Pro Tips

### Tip 1: Always Let Claude Research First
Don't skip the intelligence gathering phase. The more context Claude has, the better the outreach.

```
✗ Bad: "Write a cold email to XYZ Corp"
✓ Good: "Create cold outreach for XYZ Corp" (then let Claude research)
```

### Tip 2: Build Your Case Study Library
Keep your Google Drive "Sales Assets" folder updated with:
- Recent case studies
- Updated metrics
- Client testimonials
- Competitive analysis

Claude will pull from these automatically.

### Tip 3: Update Deal Stages Regularly
Keep your Asana Sales Pipeline current. Claude uses this to:
- Identify stuck deals
- Trigger appropriate sequences
- Forecast pipeline accurately

### Tip 4: Track What Works
Ask Claude to analyze performance regularly:
```
"What subject lines are getting best open rates?"
"Which email in sequence gets most responses?"
"What's our average time in Discovery stage?"
```

Use these insights to optimize future campaigns.

### Tip 5: Batch Your Research
If you have 10 prospects to reach out to, ask:
```
"Research these 10 companies for outreach: [list]"
```

Claude will batch the research and provide a compiled brief.

---

## Troubleshooting

### Problem: Claude can't find my Sales Pipeline project

**Solution**:
1. Verify project name is exactly "Sales Pipeline" in Asana
2. Make sure project is in the correct workspace
3. Try: "Search Asana for project named Sales Pipeline"
4. Manually provide the project ID if needed

### Problem: Outreach emails feel too generic

**Solution**:
1. Provide more context about the prospect upfront
2. Share specific talking points or angles
3. Ask Claude to research deeper: "Find more about [Company]'s recent initiatives"
4. Give feedback: "Make this more specific to their industry"

### Problem: Deal tasks not being created

**Solution**:
1. Verify Sales Pipeline project has required custom fields
2. Check that you have edit access to the project
3. Manually create task, then ask Claude to update it

### Problem: Follow-up sequence feels too aggressive

**Solution**:
```
"Extend the sequence to 30 days instead of 21"
"Make the tone more casual and less salesy"
"Remove Email 4 from the sequence"
```

---

## Next Steps

Once you're comfortable with basics:

1. **Read [REFERENCE.md](../references/REFERENCE.md)** for comprehensive templates and examples
2. **Review [DATA-SOURCES.md](DATA-SOURCES.md)** to optimize your data setup
3. **Explore advanced workflows** in the main [SKILL.md](../SKILL.md)

---

## Need Help?

If you encounter issues:

1. Check that all data sources (Asana, Gmail, Drive, Calendar) are properly connected
2. Verify your Sales Pipeline project has required custom fields
3. Review the [SKILL.md](../SKILL.md) for detailed workflow explanations
4. Ask Claude: "Help me troubleshoot [specific issue]"

---

## Quick Wins Checklist

- [ ] Sales Pipeline project created in Asana with custom fields
- [ ] Gmail, Drive, Calendar access enabled in Claude
- [ ] Sales Assets folder created in Google Drive with case studies
- [ ] Test campaign created for one prospect
- [ ] First email sent and tracked in Asana
- [ ] Scheduled weekly pipeline review with Claude

**You're ready to automate sales with intelligence. Start with one prospect, refine your approach, then scale.**
