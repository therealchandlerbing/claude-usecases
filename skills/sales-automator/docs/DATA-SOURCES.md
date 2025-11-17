# Sales Automator Data Sources Guide

This skill pulls intelligence from multiple sources to personalize outreach. Here's how to set up and optimize each source.

## Overview

**Data Sources Used**:
1. **Asana** - Deal pipeline tracking, task management
2. **Gmail** - Email history, communication patterns
3. **Google Drive** - Case studies, proposals, sales assets
4. **Google Calendar** - Meeting history, relationship frequency
5. **Past Conversations** - Claude's memory of your discussions
6. **Web Search** - Company research, competitive intelligence

---

## 1. Asana Setup

### Purpose
Asana is your deal pipeline CRM. Every prospect, opportunity, and customer interaction is tracked here.

### Required Project: Sales Pipeline

**Project Structure**:
```
Sales Pipeline
├── Hot Leads (section)
├── Warm Leads (section)
├── Cold Leads (section)
├── Closed Won (section)
└── Closed Lost (section)
```

**Required Custom Fields**:

| Field Name | Type | Options/Format | Purpose |
|------------|------|----------------|---------|
| Deal Stage | Dropdown | Outreach, Discovery, Proposal, Negotiation, Closed-Won, Closed-Lost | Track deal progress |
| Deal Value | Number | $ amount | Forecast pipeline |
| Close Date | Date | YYYY-MM-DD | Timeline tracking |
| Lead Source | Dropdown | Inbound, Outbound Cold, Referral, Partnership, Event, Content | Attribution |
| Lead Score | Dropdown | Hot, Warm, Cold | Prioritization |
| Next Action | Text | Free text | What needs to happen next |

**Optional Custom Fields** (Recommended):
- **Primary Contact**: Person (Asana user or email)
- **Company Size**: Dropdown (1-10, 11-50, 51-200, 201-500, 500+)
- **Industry**: Dropdown (Your target industries)
- **Competitor**: Text (Who they're evaluating)
- **Deal Owner**: Person (Sales team member responsible)

### Task Naming Convention

```
[Company Name] - [Opportunity Type]

Examples:
- "Acme Corp - Partnership Agreement"
- "TechStart Inc - Consulting Engagement"
- "Global Solutions - Platform License"
```

### Task Description Template

```
## Company Overview
- Industry: [Industry]
- Size: [Employee Count]
- Location: [City, Country]
- Website: [URL]

## Decision-Makers
- Primary Contact: [Name, Title, Email]
- Economic Buyer: [Name, Title]
- Champion: [Name, Title]

## Opportunity
- Type: [Partnership, Consulting, License, etc.]
- Value: $[Amount]
- Expected Close: [Date]
- Competition: [Competitors they're evaluating]

## Current Status
[Brief description of where things stand]

## Next Steps
- [Action 1] by [Date]
- [Action 2] by [Date]
```

### Subtask Structure for Outreach Sequences

For each deal in Outreach stage, create subtasks:
```
[ ] Send Email 1: [Subject] (Due: Today)
[ ] Send Email 2: [Subject] (Due: +3 days)
[ ] Send Email 3: [Subject] (Due: +7 days)
[ ] Send Email 4: [Subject] (Due: +14 days)
[ ] Send Email 5: [Subject] (Due: +21 days)
```

### Stories/Comments Protocol

Use task comments to log:
- Email sent dates and responses
- Meeting notes
- Objections raised
- Decisions made
- Next steps agreed upon

**Format**:
```
📧 Email sent [Date]: [Subject]
📞 Call completed [Date]: [Key discussion points]
🤝 Meeting [Date]: [Attendees, outcomes, next steps]
⚠️ Blocker: [Description of what's stuck]
✅ Milestone: [What was accomplished]
```

### Asana Search Optimization

**For Claude to find deals efficiently**:

1. **Use consistent naming**: Always `[Company] - [Opportunity]`
2. **Tag with company name**: Add company name in task name and description
3. **Update stages regularly**: Keep Deal Stage custom field current
4. **Set due dates**: Helps Claude identify stuck deals
5. **Add followers**: Claude can notify relevant team members

---

## 2. Gmail Setup

### Purpose
Gmail provides email history, communication patterns, and relationship context.

### Access Requirements
- Gmail tool must be enabled in Claude
- Claude needs permission to read your sent and received mail

### How Claude Uses Gmail

**For New Prospects**:
- Searches: `from:@companyname.com OR to:@companyname.com`
- Checks: If you've ever emailed anyone at this company
- Identifies: Past proposals, introductions, rejections

**For Existing Relationships**:
- Searches: Specific email addresses
- Analyzes: Response patterns, tone, time between emails
- Extracts: Last discussed topics, pending items, objections raised

### Gmail Organization Tips

**Labels to Create** (optional but helpful):
- `Sales/Outbound` - Cold outreach emails
- `Sales/Prospects` - Active prospect conversations
- `Sales/Proposals Sent` - Proposals that went out
- `Sales/Closed Won` - Deals that closed
- `Sales/Closed Lost` - Deals that didn't close

**Why this helps**: Claude can search specific labels for better context.

### Email Template Storage

Store your email templates as Gmail drafts with specific subject lines:
- `TEMPLATE: Cold Outreach - Insight`
- `TEMPLATE: Follow-Up - Warm`
- `TEMPLATE: Proposal Introduction`

Claude can reference these when generating sequences.

---

## 3. Google Drive Setup

### Purpose
Google Drive stores your sales assets: case studies, proposals, testimonials, competitive analysis.

### Folder Structure

```
Sales Assets/
├── Case Studies/
│   ├── [Client Name] - [Result] Case Study.pdf
│   ├── [Client Name] - [Result] Case Study.pdf
│   └── [Industry] Case Study Collection.docx
├── Proposals/
│   ├── Template - Partnership Proposal.docx
│   ├── Template - Consulting Proposal.docx
│   └── [Sent Proposals by Company Name]/
├── Testimonials/
│   ├── Client Testimonials.docx
│   └── [Individual testimonial files]
├── Pitch Decks/
│   ├── [Your Company] Overview Deck.pptx
│   ├── [Your Company] Partnership Deck.pptx
│   └── [Industry-Specific Decks]/
├── Competitive Analysis/
│   ├── [Competitor A] Analysis.docx
│   ├── [Competitor B] Analysis.docx
│   └── Competitive Matrix.xlsx
└── ROI Calculators/
    ├── ROI Template.xlsx
    └── [Industry-Specific Calculators]/
```

### File Naming Convention

**Case Studies**:
```
[Client Name] - [Metric Result] Case Study
Example: "Acme Corp - 40% Revenue Increase Case Study"
```

**Proposals**:
```
[Date] - [Company Name] - [Opportunity Type] Proposal
Example: "2024-11-01 - TechStart - Consulting Proposal"
```

**Why naming matters**: Claude searches Drive by company name and keywords. Consistent naming = better search results.

### Case Study Template

Every case study should be a 1-2 page PDF or Google Doc with:
- Client name (or anonymized "Leading [Industry] Company")
- Challenge/Problem
- Solution/Approach
- Results (quantified metrics)
- Testimonial quote (if available)

Keep these updated with latest results.

### Proposal Template

Create reusable proposal templates with:
- Executive Summary section
- Approach/Methodology section
- Timeline section
- Investment/Pricing section
- Case Studies section
- Team Bios section

Claude can populate variables and customize for each prospect.

---

## 4. Google Calendar Setup

### Purpose
Calendar data shows meeting frequency, last interaction date, relationship warmth.

### Access Requirements
- Google Calendar tool must be enabled in Claude
- Claude needs permission to read your calendar events

### How Claude Uses Calendar

**Relationship Intelligence**:
- Last meeting date: "Haven't talked in 3 months" triggers different approach
- Meeting frequency: Weekly vs. quarterly changes relationship warmth assessment
- Upcoming meetings: "You have a call tomorrow" influences urgency

**Availability**:
- When suggesting meeting times, Claude can check your availability
- Avoids double-booking

### Calendar Best Practices

**Event Naming**:
```
[Type] - [Company Name]: [Topic]

Examples:
- "Discovery - Acme Corp: Partnership Discussion"
- "Proposal Presentation - TechStart: Platform Demo"
- "Check-in - Global Solutions: Q4 Planning"
```

**Event Descriptions**:
Include key details:
- Attendees with titles
- Meeting objective
- Preparation needed
- Follow-up items

**Why this matters**: Claude can search calendar by company name to find meeting history.

---

## 5. Past Conversations (Claude Memory)

### Purpose
Claude remembers what you've discussed in past conversations, including context about prospects, strategies, and commitments.

### How It Works

**Automatic**:
- Claude stores key information from your conversations
- Searches this memory when you mention company/person names
- Surfaces relevant context automatically

**Manual Optimization**:
You can tell Claude to remember specific things:
```
"Remember: Acme Corp's CFO is the decision-maker, not the CEO"
"Note: TechStart prefers pilot projects before full commitments"
"Remember: Global Solutions is evaluating us vs. Competitor X"
```

### What Gets Remembered

- Company names and industries you've discussed
- Key contacts and their roles
- Deal stage and status
- Objections or concerns raised
- Commitments made ("I'll send proposal by Friday")
- Strategic context ("They're going through acquisition")

### Memory Search Commands

```
"What do we know about Acme Corp?"
"Have I talked to you about TechStart before?"
"What did I commit to for Global Solutions?"
"Remind me about the XYZ partnership"
```

---

## 6. Web Search Integration

### Purpose
Research prospects, competitors, industry trends when internal data doesn't exist.

### What Claude Searches

**For New Prospects**:
1. Company overview: `"[Company Name] overview"`
2. Recent news: `"[Company Name] news OR announcements"`
3. Strategic priorities: `"[Company Name] strategic priorities OR initiatives"`
4. Leadership: `"[Company Name] leadership team OR executives"`
5. Competitors: `"[Company Name] competitors OR alternatives"`

**For Industry Context**:
1. Trends: `"[Industry] trends"`
2. Challenges: `"[Industry] challenges"`
3. Market size: `"[Industry] market size OR forecast"`

**For Competitive Positioning**:
1. Competitor features: `"[Competitor] features OR capabilities"`
2. Competitor pricing: `"[Competitor] pricing OR cost"`
3. Competitor reviews: `"[Competitor] reviews OR complaints"`

### Web Search Best Practices

**When Claude should search**:
- New prospect (no internal data)
- Haven't talked to this company in 6+ months
- Need competitive intelligence
- Industry context for positioning

**When Claude shouldn't search**:
- You have recent internal data
- Company is existing customer/partner
- Just need to update existing deal in Asana

### Optimizing Research Time

**For batch research**:
```
"Research these 5 companies for outreach: [Company 1], [Company 2], [Company 3], [Company 4], [Company 5]"
```

Claude will batch the web searches and deliver compiled intelligence brief.

---

## Data Flow Example

Here's how the data sources work together when you say:

```
"Create cold outreach for Acme Corp"
```

**Step 1: Check Past Conversations**
- Searches Claude's memory for "Acme Corp"
- Result: "We discussed them 2 months ago, interested in partnership but timing was off"

**Step 2: Search Gmail**
- Query: `from:@acmecorp.com OR to:@acmecorp.com`
- Result: "Exchanged 3 emails in September, last one was them saying 'Let's revisit in Q4'"

**Step 3: Check Calendar**
- Query: "Acme Corp"
- Result: "Had discovery call on Sept 15, no meetings since"

**Step 4: Search Drive**
- Query: "Acme Corp"
- Result: "Found September meeting notes and draft proposal"

**Step 5: Check Asana**
- Query: "Acme Corp"
- Result: "Deal exists in Sales Pipeline, stage: Discovery, marked 'Cold' due to no recent activity"

**Step 6: Web Search (if needed)**
- Query: "Acme Corp news OR announcements"
- Result: "They just announced $10M Series B funding last week"

**Step 7: Synthesize**
Claude now has complete context:
- Relationship history (2 months ago discussion)
- Current deal stage (Discovery, gone cold)
- Recent development (Series B funding = good timing to re-engage)
- Assets available (meeting notes, draft proposal)

**Step 8: Generate Outreach**
Email references:
- Past conversation ("When we talked in September...")
- Recent funding ("Congrats on the Series B...")
- Updated proposal ("I've refined the proposal based on our discussion...")
- Clear CTA ("Now that you're in Q4 and have new funding, does it make sense to revisit?")

**Result**: Hyper-personalized, contextually relevant outreach that doesn't feel generic.

---

## Data Maintenance Schedule

### Daily
- [ ] Update deal stages in Asana as conversations progress
- [ ] Log email sends and responses in Asana task comments
- [ ] Mark completed follow-up subtasks

### Weekly
- [ ] Review stuck deals (> threshold for stage)
- [ ] Update close dates for active proposals
- [ ] Archive closed deals (won or lost) to appropriate section

### Monthly
- [ ] Add new case studies to Drive (when projects complete)
- [ ] Update testimonials doc with new quotes
- [ ] Review and refresh proposal templates
- [ ] Audit Sales Pipeline for stale deals

### Quarterly
- [ ] Analyze win/loss reasons in closed deals
- [ ] Update competitive analysis docs
- [ ] Refresh industry research
- [ ] Review and optimize email templates based on performance

---

## Troubleshooting Data Issues

### Issue: Claude can't find information I know exists

**Diagnosis**:
1. Check spelling (exact company name matters)
2. Verify data source is connected (Gmail, Drive, Asana)
3. Check permissions (Claude has access to that Drive folder/Asana project)

**Solutions**:
- Use exact name: "Search Drive for 'Acme Corporation' not 'Acme'"
- Manually provide: "The deal is in Asana project 'Sales Pipeline', task ID [123456]"
- Share file directly: "Here's the proposal" [attach]

### Issue: Research is too generic or missing key details

**Diagnosis**:
- Limited public information available
- Company is stealth/pre-launch
- Industry is niche with little online presence

**Solutions**:
- Provide more context upfront: "They're in [specific niche], focus on [specific problem]"
- Share internal knowledge: "Based on our call, they mentioned [specific challenge]"
- Reference similar companies: "Think of them like [Known Company] but for [Different Market]"

### Issue: Outreach feels dated or stale

**Diagnosis**:
- Last interaction was months ago
- Data in Asana/Gmail is outdated
- Haven't updated case studies recently

**Solutions**:
- Update Asana task with latest context
- Do fresh web search: "Research Acme Corp recent news"
- Provide new information: "They just hired a new CTO, Sarah Smith"

---

## Advanced Data Optimization

### Custom Asana Fields for Deeper Insights

Beyond the required fields, consider:

**Engagement Score** (Formula custom field):
- Calculates based on: Email responses, meeting frequency, proposal stage
- Helps prioritize which deals to focus on

**Days in Stage** (Formula custom field):
- Auto-calculates how long deal has been in current stage
- Highlights stuck deals automatically

**Last Touchpoint** (Date field):
- Manually updated with last meaningful interaction
- Helps identify who needs follow-up

### Gmail Filters for Auto-Organization

Create filters that:
1. Auto-label outbound sales emails
2. Flag responses from prospects
3. Highlight urgent requests

Example:
- Filter: `to:(*@prospectdomain.com)` → Label: `Sales/Prospects`, Star
- Filter: `from:(*@prospectdomain.com) subject:Re:` → Label: `Sales/Responses`, Mark important

### Drive Automation with Apps Script

For advanced users, create Drive scripts that:
- Auto-rename uploaded case studies with standardized format
- Move completed proposals to "Sent Proposals" folder
- Update a master "Sales Assets Inventory" spreadsheet

---

## Data Privacy & Security

### What Data Claude Accesses

- **Asana**: Project and task data you explicitly search or that skill accesses
- **Gmail**: Email content when specifically searching for it (not all emails)
- **Drive**: Files when specifically searching or requested
- **Calendar**: Events when specifically searching
- **Past Conversations**: What you've discussed with Claude

### What Claude Doesn't Access

- Random browsing of your emails/files
- Data from other users' accounts
- Private/restricted Drive folders without permission
- Calendar events marked private

### Best Practices

1. **Use specific project/folder names**: Keeps searches focused
2. **Set Drive folder permissions carefully**: Only share what's needed
3. **Review Claude's memory periodically**: `"What have you remembered about my sales conversations?"`
4. **Clear sensitive info after use**: If you shared temporary data, you can ask Claude to forget it

---

## Data Sources Checklist

Before using sales-automator, verify:

- [ ] Asana workspace accessible
- [ ] Sales Pipeline project exists with custom fields
- [ ] Gmail access enabled in Claude
- [ ] Google Drive access enabled in Claude
- [ ] Google Calendar access enabled in Claude
- [ ] Sales Assets folder created in Drive
- [ ] At least 2-3 case studies uploaded
- [ ] Proposal templates created
- [ ] Competitive analysis docs available
- [ ] Test search: "Find my Sales Pipeline in Asana"
- [ ] Test search: "Search Drive for case studies"
- [ ] Test search: "Check my calendar for meetings this week"

**If all checkboxes complete, your data sources are optimized for sales automation.**
