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
7. **Apollo.io** - Contact enrichment, company data, decision-maker discovery

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

## 7. Apollo.io Integration

### Purpose
Apollo.io provides structured contact and company data from a database of 210M+ contacts and 35M+ companies. Use Apollo to enrich prospect data, discover decision-makers, and qualify leads with firmographic intelligence.

### Access Requirements
- Active Apollo.io paid account (not available on free plan)
- API key generated from Apollo.io dashboard
- API key configured in your environment or MCP settings

### How Claude Uses Apollo

**For Contact Enrichment**:
- Input: Email address, name, or LinkedIn URL
- Output: Job title, company, LinkedIn profile, employment history, email verification status
- Use case: Verify contact data before outreach, find current job title

**For Company Enrichment**:
- Input: Company domain or name
- Output: Industry, revenue, employee count, funding data, locations, technologies used
- Use case: Qualify leads, understand company size and maturity

**For Decision-Maker Discovery**:
- Input: Company name + job title/department
- Output: List of contacts matching criteria with emails and LinkedIn profiles
- Use case: "Find the VP of Sales at Acme Corp"

**For Lead Qualification**:
- Input: Company domain
- Output: Firmographic data (size, revenue, funding stage, growth signals)
- Use case: Score leads based on ideal customer profile (ICP)

### Apollo API Endpoints Used

**1. People Enrichment**
```
POST https://api.apollo.io/api/v1/people/match
```
**Parameters**:
- `email`: Email address to enrich
- `first_name`, `last_name`: Name (if email unknown)
- `organization_name`: Company name (helps matching)
- `reveal_personal_emails`: Boolean (costs extra credits)
- `reveal_phone_number`: Boolean (costs extra credits)

**Returns**:
- Contact details (name, title, company)
- LinkedIn profile URL
- Employment history
- Email verification status
- Social media profiles

**2. Organization Enrichment**
```
POST https://api.apollo.io/api/v1/organizations/enrich
```
**Parameters**:
- `domain`: Company website domain (e.g., "acmecorp.com")
- `name`: Company name (if domain unknown)

**Returns**:
- Industry classification
- Revenue range
- Employee count
- Funding information
- Office locations
- Technologies used
- Corporate phone numbers

**3. People Search**
```
POST https://api.apollo.io/api/v1/mixed_people/search
```
**Parameters**:
- `person_titles`: Array of job titles (e.g., ["VP of Sales", "Sales Director"])
- `person_seniorities`: Array (e.g., ["VP", "Director", "C-Level"])
- `organization_ids`: Search within specific companies
- `person_locations`: Array of locations
- `q_keywords`: Free text search

**Returns**:
- List of contacts matching filters (up to 100 per search)
- Each with full contact details

**4. Organization Search**
```
POST https://api.apollo.io/api/v1/mixed_companies/search
```
**Parameters**:
- `organization_num_employees_ranges`: Employee count ranges
- `organization_revenue_ranges`: Revenue ranges
- `organization_industry_tag_ids`: Industry filters
- `organization_locations`: Geographic filters

**Returns**:
- List of companies matching filters (up to 50,000 records total)

### When Apollo Should Be Used

**Priority 1: Contact Discovery**
User says: "Find the CTO at TechStart Inc"
- Use Apollo People Search with company + title filters
- Return top 3-5 matches with LinkedIn URLs and emails

**Priority 2: Prospect Enrichment (Cold Outreach)**
User says: "Create cold outreach for john.doe@acmecorp.com"
- Before researching, use Apollo to enrich contact
- Get current job title, verify employment, check LinkedIn
- Then continue with normal outreach workflow

**Priority 3: Company Qualification**
User says: "Should we pursue Acme Corp?"
- Use Apollo Organization Enrichment to get firmographics
- Compare against ICP criteria (size, revenue, industry, funding)
- Provide qualification recommendation

**Priority 4: Lead Scoring**
When adding deal to pipeline:
- Auto-enrich company via Apollo
- Score based on: employee count, revenue, funding stage, growth signals
- Set Lead Score custom field (Hot/Warm/Cold)

### When NOT to Use Apollo

**Skip Apollo when**:
- Existing customer/partner (you already have accurate data)
- Recently enriched (< 30 days ago, use cached data)
- Free contact discovery tools suffice (LinkedIn manual search)
- Credit budget exhausted for the day

**Use Web Search instead when**:
- Need narrative context (recent news, strategy, announcements)
- Looking for qualitative information (company culture, values)
- Searching for content (blog posts, case studies, press releases)

### Apollo Credit Management

**Credit Costs**:
- People Enrichment: 1 credit per person
- Organization Enrichment: 1 credit per company
- People Search: 1 credit per search (not per result)
- Revealing personal email: +1 credit
- Revealing phone number: +1 credit

**Daily Budget Strategy**:
```yaml
# Configure in pipeline-config.yaml
apollo:
  credit_management:
    daily_limit: 100
    warn_threshold: 80
    priority_prospects_only: false
```

**Recommended Allocation**:
- 50 credits: Cold outreach contact enrichment
- 30 credits: Decision-maker discovery searches
- 20 credits: Company qualification/lead scoring

### Apollo Workflow Integration

**Integrated into Phase 1: Intelligence Gathering**

Updated workflow when Apollo is enabled:

```
1. Check Past Conversations (existing context)
2. Check Asana (existing deal data)
3. [NEW] Apollo Enrichment
   a. If email provided: Enrich contact via Apollo
   b. If company only: Enrich organization via Apollo
   c. If finding decision-maker: Search Apollo for contacts
4. Search Gmail (email history)
5. Check Calendar (meeting history)
6. Search Drive (proposals, case studies)
7. Web Search (narrative context, recent news)
```

**Example: Cold Outreach with Apollo**

User: "Create cold outreach for sarah.jones@techstart.io"

**Step 1: Apollo People Enrichment**
```
POST /api/v1/people/match
{
  "email": "sarah.jones@techstart.io"
}
```
**Returns**:
- Name: Sarah Jones
- Title: VP of Product
- Company: TechStart Inc.
- LinkedIn: linkedin.com/in/sarahjones
- Employment History: Previously at Google, Microsoft
- Email Status: Verified

**Step 2: Apollo Organization Enrichment**
```
POST /api/v1/organizations/enrich
{
  "domain": "techstart.io"
}
```
**Returns**:
- Industry: SaaS / Enterprise Software
- Employee Count: 50-200
- Revenue: $5M-$10M
- Funding: Series A ($8M raised)
- Locations: San Francisco, Remote
- Technologies: AWS, React, Python

**Step 3: Synthesize Apollo Data**
Claude now knows:
- Sarah is VP of Product (target persona ✓)
- TechStart is Series A startup (good timing for sales)
- Company uses modern tech stack (relevant for your solution)
- 50-200 employees (fits ICP)
- Sarah has big tech experience (understands enterprise solutions)

**Step 4: Continue Normal Workflow**
- Search Gmail for past TechStart emails
- Check Calendar for TechStart meetings
- Web search for "TechStart news OR announcements"
- Generate personalized outreach referencing Sarah's background and TechStart's stage

**Result**: Hyper-personalized outreach that references:
- Sarah's VP Product role specifically
- TechStart's Series A stage and growth trajectory
- Relevant pain points for 50-200 person product teams
- Credibility via mentioning her Google/Microsoft background

### Apollo Search Strategies

**Strategy 1: Decision-Maker Discovery**

User: "Find the head of sales at companies in the fintech industry with 100-500 employees"

```
1. Organization Search (find fintech companies 100-500 employees)
   POST /api/v1/mixed_companies/search
   {
     "organization_num_employees_ranges": ["100-500"],
     "organization_industry_tag_ids": ["fintech"]
   }

2. People Search (find sales leaders at those companies)
   POST /api/v1/mixed_people/search
   {
     "person_titles": ["VP of Sales", "Head of Sales", "Chief Revenue Officer"],
     "organization_ids": [results from step 1]
   }
```

**Returns**: List of 25-100 sales leaders at fintech companies matching criteria

**Strategy 2: Account-Based Marketing (ABM) List Building**

User: "Build an ABM list for Series B SaaS companies in the US with 200-1000 employees"

```
1. Organization Search
   POST /api/v1/mixed_companies/search
   {
     "organization_num_employees_ranges": ["200-1000"],
     "organization_industry_tag_ids": ["saas"],
     "organization_locations": ["United States"],
     "funding_stage": ["Series B"]
   }

2. For each company: Organization Enrichment
   (Get detailed firmographics, technologies, funding details)

3. For each qualified company: People Search
   (Find decision-makers: CEO, VP Product, CTO, etc.)

4. Create Asana tasks for top 20-50 accounts
   (Populate with Apollo enriched data)
```

**Strategy 3: Competitive Intelligence**

User: "Find companies using [Competitor Product] that might be good prospects"

```
1. Organization Search
   POST /api/v1/mixed_companies/search
   {
     "technologies_used": ["competitor-product-id"],
     "organization_num_employees_ranges": ["50-500"]  # Your ICP
   }

2. Enrich top 50 companies
   (Understand their tech stack, see what else they use)

3. Find decision-makers at qualified accounts
   (People Search for titles matching your buyer persona)
```

### Apollo Data Quality Best Practices

**1. Verify Before Outreach**
- Apollo provides `email_status` field (verified, guessed, unavailable)
- Only use "verified" emails for cold outreach
- "Guessed" emails: Validate with email verification tool first

**2. Employment History Validation**
- Apollo includes employment history with dates
- Check `current` flag to ensure person still works there
- Outdated data = wasted outreach

**3. Confidence Scoring**
```yaml
# In pipeline-config.yaml
data_preferences:
  minimum_confidence_score: 0.7
```
- Apollo returns confidence scores for matches
- Only use data with >70% confidence for outreach

**4. Multi-Source Validation**
- Cross-reference Apollo data with LinkedIn (manual check)
- Verify company data with web search (recent news)
- Check calendar/Gmail for any past interactions (overrides Apollo)

### Apollo + Other Data Sources

**Apollo complements other sources**:

| Source | Best For | Apollo Adds |
|--------|----------|-------------|
| **Gmail** | Email history, past communication | Current job title, employment verification |
| **Drive** | Case studies, proposals | Firmographics to match best case study |
| **Calendar** | Meeting history | Decision-maker's current role (may have changed) |
| **Web Search** | News, narrative context | Structured data (revenue, funding, employee count) |
| **Asana** | Deal tracking | Auto-enrichment when deal created |

**Example Combined Use**:
Gmail shows you emailed someone at Acme Corp 6 months ago, but Apollo reveals they've since left the company. This prevents outreach to outdated contact.

### Apollo Setup Checklist

Before using Apollo integration:

- [ ] Apollo.io paid account active
- [ ] API key generated (Settings > Integrations > API)
- [ ] API key stored in environment variable `APOLLO_API_KEY`
- [ ] Or API key configured in MCP settings
- [ ] Test API connection: `curl -H "X-Api-Key: YOUR_KEY" https://api.apollo.io/api/v1/auth/health`
- [ ] Set daily credit limit in `pipeline-config.yaml`
- [ ] Enable auto-enrichment features (or disable if manual only)
- [ ] Configure fallback to web search if Apollo fails
- [ ] Review credit costs to optimize budget

### Troubleshooting Apollo Integration

**Issue: "No match found" for contact enrichment**

**Solutions**:
- Provide more parameters (first_name, last_name, organization_name)
- Try organization enrichment instead (get company data, then search for people)
- Fall back to web search + LinkedIn manual lookup

**Issue: "Daily credit limit reached"**

**Solutions**:
- Increase daily limit in config
- Enable `priority_prospects_only: true` (only enrich hot/warm leads)
- Cache results for 30 days (avoid re-enriching same contacts)
- Use bulk enrichment endpoint (10 at once = more efficient)

**Issue: Data is outdated or incorrect**

**Solutions**:
- Cross-reference with LinkedIn (Apollo pulls from LinkedIn, but may lag)
- Use `current` flag in employment history to verify active employment
- Supplement with web search for recent job changes
- Report data issues to Apollo support (improves database quality)

**Issue: Too many results from search**

**Solutions**:
- Add more filters (seniority, location, company size)
- Use `q_keywords` for more specific matching
- Reduce `page_size` to get top matches only
- Combine filters (title + seniority + location)

### Advanced Apollo Workflows

**Workflow 1: Automated Lead Enrichment**

Trigger: User adds new deal to Asana Sales Pipeline

```
1. Extract company domain from deal task
2. Apollo Organization Enrichment (domain)
3. Extract employee count, revenue, industry
4. Calculate lead score:
   - Employee count 50-500: +10 points
   - Revenue $5M-$50M: +10 points
   - Industry = target industry: +10 points
   - Funding stage = Series A/B: +5 points
5. Update Asana custom fields:
   - Lead Score: Hot (25-35), Warm (15-24), Cold (<15)
   - Industry: From Apollo
   - Company Size: From Apollo
6. Add enriched data to task description
```

**Workflow 2: Multi-Contact Outreach Sequence**

User: "Create outreach campaign for TechStart Inc."

```
1. Apollo People Search: Find 3-5 decision-makers at TechStart
   - VP of Sales
   - Head of Revenue Operations
   - CTO (if product-led growth)

2. For each contact: Apollo People Enrichment
   - Get current title, LinkedIn, email verification

3. Prioritize contacts:
   - Verified emails first
   - Decision-making authority (VP > Director > Manager)
   - Recent job changes (new in role = open to new solutions)

4. Create multi-thread outreach:
   - Email 1 to VP of Sales (primary)
   - Email 2 to Head of RevOps (secondary, 3 days later)
   - Email 3 to CTO (if no response, 7 days later)

5. Track all in Asana with subtasks per contact
```

**Workflow 3: Competitive Displacement**

User: "Find companies using [Competitor] that match our ICP"

```
1. Apollo Organization Search:
   - Technologies used: [Competitor product]
   - Employee count: 100-500
   - Revenue: $5M-$50M
   - Industry: SaaS

2. For each company (top 50):
   - Apollo Organization Enrichment (full firmographics)
   - Check funding stage (Series A/B = growth mode = switching openness)
   - Analyze tech stack (what else they use, integration opportunities)

3. Qualify companies:
   - Score based on ICP fit
   - Flag companies with recent funding (buying window)
   - Identify companies with complementary tech stack

4. For top 20 qualified companies:
   - Apollo People Search (find decision-makers)
   - Enrich top 3-5 contacts per company
   - Create Asana deal tasks with enriched data

5. Generate personalized outreach:
   - Reference their current solution (Competitor)
   - Position based on tech stack gaps
   - Use funding news as timing trigger
```

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
