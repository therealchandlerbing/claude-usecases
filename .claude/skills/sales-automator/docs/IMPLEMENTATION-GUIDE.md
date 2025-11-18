# Sales Automator - Implementation Guide

**Version:** 1.0.0
**Last Updated:** 2025-11-18
**Audience:** Sales operations, Revenue teams, Implementation specialists

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Data Architecture](#data-architecture)
3. [Integration Deep Dive](#integration-deep-dive)
4. [Pipeline Configuration](#pipeline-configuration)
5. [Quality Assurance System](#quality-assurance-system)
6. [Advanced Workflows](#advanced-workflows)
7. [Performance Optimization](#performance-optimization)
8. [Troubleshooting Guide](#troubleshooting-guide)
9. [Scaling Considerations](#scaling-considerations)
10. [Future Evolution](#future-evolution)

---

## Architecture Overview

### System Components

The Sales Automator operates as a five-phase intelligence system:

```
┌─────────────────────────────────────────────────────────────────┐
│                    SALES AUTOMATOR ARCHITECTURE                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: INTELLIGENCE GATHERING                                  │
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │Conversa- │  │  Gmail   │  │  Drive   │  │ Calendar │        │
│  │tion Srch │  │ History  │  │ Assets   │  │ Meetings │        │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘        │
│       │             │             │             │                │
│  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐                       │
│  │  Asana   │  │  Apollo  │  │   Web    │                       │
│  │ Pipeline │  │  .io     │  │ Research │                       │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘                       │
│       │             │             │                              │
│       └─────────────┴─────────────┘                              │
│                     │                                            │
│              ┌──────▼──────┐                                     │
│              │ INTELLIGENCE │                                    │
│              │    BRIEF     │                                    │
│              └──────┬───────┘                                    │
└─────────────────────┼───────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│ PHASE 2: CAMPAIGN DESIGN                                         │
│                                                                  │
│  ┌──────────────────────────────────────────────────────┐       │
│  │ Sequence Selection Engine                             │       │
│  │                                                       │       │
│  │  New Prospect → Cold (5 touch, 21 days)              │       │
│  │  Warm Lead → Warm (3 touch, 14 days)                 │       │
│  │  Stuck Deal → Re-engagement (3 touch, 10 days)       │       │
│  │  Closed-Lost → Reactivation (2 touch, 7 days)        │       │
│  └──────────────────────────────────────────────────────┘       │
└─────────────────────┬───────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│ PHASE 3: CONTENT GENERATION                                      │
│                                                                  │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐                 │
│  │ Template   │  │ Variable   │  │ Quality    │                 │
│  │ Selection  │→ │ Population │→ │ Scoring    │                 │
│  └────────────┘  └────────────┘  └────────────┘                 │
└─────────────────────┬───────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│ PHASE 4: PIPELINE MANAGEMENT                                     │
│                                                                  │
│  Asana Deal Creation → Custom Field Population → Subtask Gen    │
└─────────────────────┬───────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│ PHASE 5: DELIVERY & TRACKING                                     │
│                                                                  │
│  Campaign Brief → Quality Assessment → Metrics Setup → Delivery │
└─────────────────────────────────────────────────────────────────┘
```

### Decision Flow

```
User Request
     │
     ▼
┌─────────────┐
│ Parse Intent│
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────────┐
│ What type of request?                    │
├──────────────┬──────────────┬───────────┤
│ Outreach     │ Pipeline     │ Analysis  │
│ Generation   │ Health       │ Request   │
└──────┬───────┴──────┬───────┴─────┬─────┘
       │              │             │
       ▼              ▼             ▼
┌──────────┐   ┌──────────┐   ┌──────────┐
│ Full     │   │ Pipeline │   │ Perf.    │
│ Workflow │   │ Audit    │   │ Analysis │
│ Phases   │   │ Workflow │   │ Workflow │
│ 1-5      │   │          │   │          │
└──────────┘   └──────────┘   └──────────┘
```

---

## Data Architecture

### Data Source Priority Matrix

When gathering intelligence, query sources in this order for efficiency:

| Priority | Source | Data Type | Use Case |
|----------|--------|-----------|----------|
| 1 | Conversation Search | Relationship history, context | Always first - captures internal knowledge |
| 2 | Apollo.io | Firmographics, contacts | New prospects - enrichment data |
| 3 | Asana | Deal status, pipeline | Existing relationships |
| 4 | Gmail | Communication history | Email threads, commitments |
| 5 | Calendar | Meeting history | Relationship warmth, frequency |
| 6 | Drive | Documents, proposals | Case studies, past proposals |
| 7 | Web Search | Public info, news | External context, recent developments |

### Data Flow Model

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA FLOW MODEL                           │
└─────────────────────────────────────────────────────────────┘

INPUT LAYER
├─ User Request: "Create outreach for [Company]"
├─ Context Variables: Company name, individual, opportunity type
└─ Historical Context: Past conversations, tool state

ENRICHMENT LAYER
├─ Apollo Enrichment
│  ├─ People Match: Email → Full profile, employment history
│  ├─ Org Enrichment: Domain → Firmographics, tech stack
│  └─ Lead Search: Titles → Decision-maker discovery
│
├─ Internal Systems
│  ├─ Asana: Pipeline status, deal history, tasks
│  ├─ Gmail: Threads, response patterns, open loops
│  ├─ Calendar: Meeting frequency, last touchpoint
│  └─ Drive: Proposals, case studies, competitive docs
│
└─ External Research
   ├─ Web Search: News, strategic initiatives
   └─ Social: LinkedIn, company blog, press releases

SYNTHESIS LAYER
├─ Relationship Classification
│  ├─ New (no prior contact)
│  ├─ Warm (prior contact, positive)
│  ├─ Cold (prior contact, stale)
│  └─ Reactivation (closed-lost, time passed)
│
├─ Lead Scoring (Apollo-powered)
│  ├─ ICP Fit: Employee count, revenue, industry
│  ├─ Engagement: Meeting history, email response rate
│  └─ Timing: Funding, hiring, growth signals
│
└─ Intelligence Brief Compilation

OUTPUT LAYER
├─ Email Sequence: 2-5 emails with personalization
├─ Pipeline Update: Asana deal creation/update
├─ Tracking Setup: Follow-up subtasks, metrics
└─ Quality Assessment: Grade A-D with improvement areas
```

### Data Quality Standards

**Required for Grade A Campaign:**

| Data Point | Source | Validation |
|------------|--------|------------|
| Company name (exact) | Apollo/Web | Verify spelling, parent/subsidiary |
| Primary contact | Apollo | Email verified, current role confirmed |
| Industry classification | Apollo | NAICS/SIC code matched |
| Company size | Apollo | Employee count range validated |
| Recent news (< 90 days) | Web | Dated, source credible |
| Decision-maker priorities | Research synthesis | Multiple source corroboration |
| Past interaction summary | Internal systems | All touchpoints captured |
| Competitive landscape | Web/Drive | Current positioning understood |

---

## Integration Deep Dive

### Apollo.io Integration

Apollo provides the foundation for prospect intelligence. Configure these workflows:

#### People Enrichment Workflow

```
Trigger: User provides email or LinkedIn URL
Action: POST /api/v1/people/match

Required fields:
- email (primary) OR
- linkedin_url OR
- first_name + last_name + organization_name

Response extraction:
{
  "full_name": "→ {{first_name}} {{last_name}}",
  "title": "→ {{title}}",
  "organization": {
    "name": "→ {{company_name}}",
    "industry": "→ {{industry}}",
    "estimated_num_employees": "→ {{company_size}}"
  },
  "email_status": "→ verified/guessed/unavailable",
  "employment_history": "→ Previous roles for context"
}

Quality gate: Only use "verified" emails for cold outreach
```

#### Organization Enrichment Workflow

```
Trigger: User provides company name or domain
Action: POST /api/v1/organizations/enrich

Required fields:
- domain (primary) OR
- name + location

Response extraction:
{
  "name": "→ {{company_name}}",
  "industry": "→ {{industry}}",
  "estimated_num_employees": "→ {{company_size}}",
  "annual_revenue": "→ {{revenue_range}}",
  "technologies": "→ Tech stack for positioning",
  "funding_stage": "→ Growth stage context",
  "latest_funding_amount": "→ Recent investment"
}

Application:
- Match case studies by company size/industry
- Identify tech stack for displacement opportunities
- Use funding stage for urgency signals
```

#### Lead Search Workflow

```
Trigger: Need to find decision-makers at target company
Action: POST /api/v1/mixed_people/search

Filters:
{
  "organization_domains": ["target-company.com"],
  "person_titles": ["VP", "Director", "Head of"],
  "person_seniorities": ["director", "vp", "c_suite"],
  "email_status": ["verified"]
}

Response: Top 3-5 contacts ranked by relevance

Application:
- Multi-threading strategy
- Champion identification
- Org chart mapping
```

### Asana Pipeline Integration

#### Project Structure

```
Sales Pipeline (Project)
├─ Sections (Deal Stages)
│  ├─ Outreach
│  ├─ Discovery
│  ├─ Proposal
│  ├─ Negotiation
│  ├─ Closed-Won
│  └─ Closed-Lost
│
├─ Custom Fields
│  ├─ Deal Value (Number)
│  ├─ Close Date (Date)
│  ├─ Lead Source (Dropdown)
│  ├─ Lead Score (Dropdown: Hot/Warm/Cold)
│  ├─ Next Action (Text)
│  └─ Loss Reason (Dropdown) - for Closed-Lost
│
└─ Views
   ├─ By Stage (Board view)
   ├─ My Deals (List, filtered by assignee)
   ├─ Closing This Month (Calendar)
   └─ Stuck Deals (List, filtered by age > threshold)
```

#### Task Creation Schema

```json
{
  "name": "[Company Name] - [Opportunity Type]",
  "assignee": "sales_owner_gid",
  "projects": ["sales_pipeline_gid"],
  "section": "section_gid_based_on_stage",
  "due_date": "target_close_date",
  "custom_fields": {
    "deal_value_gid": 50000,
    "lead_source_gid": "lead_source_enum_gid",
    "lead_score_gid": "hot_enum_gid",
    "next_action_gid": "Send Email 1 of cold sequence"
  },
  "notes": "Intelligence brief summary + key research findings"
}
```

#### Subtask Schema for Sequences

```json
{
  "parent_task": "deal_task_gid",
  "subtasks": [
    {
      "name": "Send Email 1: [Subject]",
      "due_date": "today",
      "notes": "Full email content here"
    },
    {
      "name": "Send Email 2: [Subject]",
      "due_date": "+3 days",
      "notes": "Full email content here"
    },
    {
      "name": "Send Email 3: [Subject]",
      "due_date": "+7 days",
      "notes": "Full email content here"
    }
  ]
}
```

### Gmail Integration

#### Search Patterns

```
# All communication with company
from:@company.com OR to:@company.com

# Specific contact history
from:contact@company.com OR to:contact@company.com

# Proposals sent
to:@company.com subject:proposal

# Meeting scheduling
to:@company.com (calendar OR meeting OR schedule)

# Last 90 days only
after:2025-08-20 from:@company.com
```

#### Thread Analysis

When reading threads, extract:
- Communication frequency (response time patterns)
- Topics discussed (for continuity)
- Open loops (unanswered questions, pending items)
- Tone and formality level (mirror in outreach)
- Decision-makers CC'd (org chart intel)

### Drive Integration

#### Folder Structure

```
Sales Assets/
├─ Case Studies/
│  ├─ By Industry/
│  │  ├─ Healthcare/
│  │  ├─ Technology/
│  │  └─ Financial Services/
│  └─ By Outcome/
│     ├─ Revenue Growth/
│     ├─ Cost Reduction/
│     └─ Operational Efficiency/
│
├─ Proposals/
│  ├─ Templates/
│  └─ Sent/
│     └─ [Company Name]/
│
├─ Competitive Intelligence/
│  ├─ Battle Cards/
│  └─ Competitor Profiles/
│
└─ Industry Research/
   └─ [Industry]/
      └─ Trends & Reports/
```

#### Search Strategy

```
# Find case studies by industry
query: "type:document industry:[target_industry] case study"

# Find proposals for similar companies
query: "type:document in:proposals [similar_company_size] [similar_industry]"

# Find competitive positioning
query: "type:document in:competitive [competitor_name]"

# Find recent research
query: "type:document modifieddate>2025-08-01 [industry] trends"
```

---

## Pipeline Configuration

### Stage Thresholds

Configure alerts for deals exceeding these thresholds:

| Stage | Max Days | Action |
|-------|----------|--------|
| Outreach | 21 | Move to Closed-Lost if no response |
| Discovery | 14 | Trigger re-engagement sequence |
| Proposal | 30 | Check for objections, offer alternatives |
| Negotiation | 21 | Escalate, identify blockers |

### Weighted Pipeline Calculation

```
Pipeline Forecast = Σ (Deal Value × Stage Probability)

Stage Probabilities:
- Outreach: 10%
- Discovery: 25%
- Proposal: 50%
- Negotiation: 75%
- Closed-Won: 100%

Example:
Deal A: $100K in Discovery = $100K × 0.25 = $25K
Deal B: $50K in Proposal = $50K × 0.50 = $25K
Deal C: $75K in Negotiation = $75K × 0.75 = $56.25K

Weighted Pipeline = $106.25K
```

### Lead Scoring Model

Apollo data feeds automatic lead scoring:

| Factor | Points | Source |
|--------|--------|--------|
| Employee count matches ICP | +10 | Apollo Org |
| Revenue range matches ICP | +10 | Apollo Org |
| Industry alignment | +10 | Apollo Org |
| Funding stage (Series A/B) | +5 | Apollo Org |
| Growth signals (hiring, expansion) | +5 | Apollo/Web |
| Email verified | +5 | Apollo People |
| Decision-maker access | +5 | Apollo People |

**Score Interpretation:**
- Hot (25-35): Ready for aggressive pursuit
- Warm (15-24): Good fit, needs nurturing
- Cold (<15): Low priority or poor fit

---

## Quality Assurance System

### Pre-Send Validation Checklist

```
## Pre-Send Validation: [Company Name]

RESEARCH VALIDATION
□ All 7 data sources queried (or N/A justified)
□ Intelligence brief synthesized
□ Lead score calculated
□ Relationship status determined

PERSONALIZATION VALIDATION
□ All {{variables}} populated with research
□ Company-specific insight included
□ Decision-maker priorities addressed
□ Recent news/development referenced
□ Cultural awareness applied (if international)

SEQUENCE VALIDATION
□ Sequence type appropriate for relationship
□ Timing between touches strategic
□ Value-first approach in email 1
□ Clear single CTA per email
□ A/B subject variants created

PIPELINE VALIDATION
□ Asana task created/updated
□ All custom fields populated
□ Follow-up subtasks created
□ Due dates set correctly

CONTENT VALIDATION
□ Chandler's voice maintained
□ No em dashes
□ Subject lines < 50 characters
□ Email body < 150 words per email
□ Professional signature included

FINAL APPROVAL
□ Quality grade >= C (60+)
□ No blockers identified
□ Ready for send

Validated by: _______________
Date: _______________
```

### Quality Review Cadence

**Daily:**
- Review any campaigns marked "needs improvement"
- Check for stuck deals exceeding thresholds

**Weekly:**
- Analyze campaign quality grade distribution
- Identify patterns in Grade C/D campaigns
- Pipeline health review

**Monthly:**
- Win/loss analysis with quality correlation
- Template performance review
- Process improvement identification

**Quarterly:**
- Full quality framework review
- Benchmark updates based on performance
- Training needs identification

---

## Advanced Workflows

### Workflow 1: Account-Based Campaign

Multi-contact outreach to single account with coordinated messaging:

```
1. Account Research
   - Org enrichment via Apollo
   - Identify 3-5 decision-makers/influencers
   - Map org structure and priorities

2. Contact Prioritization
   - Primary: Economic buyer
   - Secondary: Champion (day-to-day contact)
   - Tertiary: Influencers (technical, operations)

3. Coordinated Sequence
   - Contact 1: C-suite message (strategic value)
   - Contact 2: Practitioner message (operational value)
   - Contact 3: Technical message (integration value)
   - Timing: Stagger by 2 days

4. Unified Tracking
   - Single parent task for account
   - Subtasks per contact
   - Shared notes on account progress

5. Multi-Thread Follow-Up
   - Reference conversations across contacts
   - "I mentioned to [other contact]..."
   - Create internal alignment urgency
```

### Workflow 2: Event-Triggered Outreach

Automated sequences triggered by prospect actions:

```
TRIGGER: Funding announcement
SEQUENCE: Congratulations + Growth Partnership
- Email 1: Congratulate, offer relevant resource
- Email 2: Case study of similar post-funding company
- Email 3: Offer strategic planning session

TRIGGER: Leadership change
SEQUENCE: Transition Support
- Email 1: Welcome, offer industry insights
- Email 2: Common challenges in first 90 days
- Email 3: Offer diagnostic/assessment

TRIGGER: Competitor churned
SEQUENCE: Alternative Solution
- Email 1: Acknowledge change, position differentiation
- Email 2: Migration case study
- Email 3: Low-friction pilot offer

TRIGGER: Content engagement
SEQUENCE: Interest Expansion
- Email 1: Related content recommendation
- Email 2: Deeper dive resource
- Email 3: Live consultation offer
```

### Workflow 3: Win-Back Campaign

Re-engage closed-lost opportunities:

```
1. Qualification Check (3-6 months post-loss)
   - Original loss reason still valid?
   - Any changes at company?
   - Any changes in our offering?

2. Approach Selection
   - Pricing issue: New packaging/options
   - Timing issue: Check if timing better now
   - Competitor won: What's changed since
   - Bad fit: Product updates addressing gaps

3. Reactivation Sequence
   - Email 1: Acknowledge history, share what's new
   - Email 2: Specific change addressing their concern
   - Wait 7 days
   - If no response: Close loop, set 6-month reminder

4. If Engaged
   - Fast-track to Discovery (skip basic qualification)
   - Address previous objections proactively
   - Offer low-friction proof (pilot, assessment)
```

---

## Performance Optimization

### Response Rate Optimization

**Subject Line Optimization:**
- Test 2-3 variants per campaign
- Track open rates by category (curiosity, value, direct)
- Maintain winning patterns library

**Send Time Optimization:**
- B2B: Tuesday-Thursday, 9-11am recipient timezone
- C-suite: Early morning (7-8am) or after hours (6-7pm)
- Track response time by send time, adjust

**Email Length Optimization:**
- Email 1: 100-125 words (insight + tease)
- Email 2-3: 75-100 words (proof + ask)
- Email 4-5: 50-75 words (decision request)

### Pipeline Velocity Optimization

**Stage Transition Acceleration:**

| From | To | Accelerator |
|------|-----|-------------|
| Outreach | Discovery | Strong CTA, calendar link, low friction |
| Discovery | Proposal | Clear next steps, fast proposal turnaround |
| Proposal | Negotiation | Proactive objection handling, ROI clarity |
| Negotiation | Close | Decision timeline, implementation support |

**Stuck Deal Recovery:**

```
Days in Stage > Threshold:
1. Review last touchpoint
2. Identify likely blocker:
   - Champion gone dark → Find alternative contact
   - Competing priorities → Create urgency/deadline
   - Budget/approval → Offer phased approach
   - Technical concerns → Bring in technical resources
3. Execute targeted re-engagement
4. If no response in 7 days, move to Closed-Lost
```

### Conversion Rate Benchmarking

Track these rates weekly, compare to benchmarks:

| Metric | Target | Good | Needs Work |
|--------|--------|------|------------|
| Open Rate (Cold) | 50%+ | 40-50% | <40% |
| Response Rate (Cold) | 10%+ | 5-10% | <5% |
| Open Rate (Warm) | 70%+ | 60-70% | <60% |
| Response Rate (Warm) | 25%+ | 15-25% | <15% |
| Discovery → Proposal | 40%+ | 30-40% | <30% |
| Proposal → Close | 50%+ | 40-50% | <40% |
| Overall Win Rate | 3%+ | 1-3% | <1% |

---

## Troubleshooting Guide

### Common Issues

**Issue: "Claude can't find my Sales Pipeline"**
```
Diagnosis:
1. Check project name exact match: "Sales Pipeline"
2. Verify workspace access permissions
3. Confirm project not archived

Resolution:
- Rename project to exact name
- Share project with Claude integration
- Use manual project GID: "Use project ID [GID]"
```

**Issue: "Apollo enrichment returns no data"**
```
Diagnosis:
1. Check API key validity
2. Verify domain/email format
3. Confirm credits available

Resolution:
- Regenerate API key if expired
- Use primary domain (not subdomain)
- Check Apollo dashboard for credit balance
- Fall back to web research if Apollo unavailable
```

**Issue: "Emails feel too generic"**
```
Diagnosis:
1. Check research depth (how many sources queried)
2. Review personalization variable population
3. Assess insight specificity

Resolution:
- Force deeper research: "Research [Company] thoroughly before writing"
- Provide specific context: "They just announced [X]"
- Reference specific case study: "Use [Case Study] as proof point"
- Request A/B variants: "Generate 3 subject line options"
```

**Issue: "Sequence type doesn't match relationship"**
```
Diagnosis:
1. Check conversation history for past interactions
2. Verify Gmail/Calendar searched
3. Confirm relationship classification

Resolution:
- Explicitly state relationship: "This is a warm lead, we met at [Event]"
- Provide context: "Last contact was 3 months ago about [Topic]"
- Override sequence: "Use warm sequence, not cold"
```

**Issue: "Pipeline not being updated"**
```
Diagnosis:
1. Check Asana integration permissions
2. Verify custom field names match exactly
3. Confirm section names match

Resolution:
- Re-authorize Asana integration
- Provide manual GIDs: "Update task [GID] to [Stage]"
- Create task manually, have Claude populate
```

### Error Recovery Patterns

**Partial Research Failure:**
```
If one data source fails:
1. Document which source failed
2. Proceed with available sources
3. Note limitation in intelligence brief
4. Reduce quality score accordingly
5. Recommend follow-up research later
```

**Campaign Generation Failure:**
```
If content generation fails mid-sequence:
1. Save completed emails
2. Document failure point
3. Retry specific email that failed
4. If persistent, use simpler template
5. Note in campaign brief for follow-up
```

**Pipeline Sync Failure:**
```
If Asana update fails:
1. Save task data locally
2. Provide manual creation instructions
3. Retry after user confirms permissions
4. Log for integration debugging
```

---

## Scaling Considerations

### Team Implementation

**Individual Contributor Setup:**
- Personal Asana workspace view
- Individual email tracking
- Personal quality dashboard

**Team Setup:**
- Shared Sales Pipeline project
- Distributed deal ownership
- Team performance analytics
- Shared template library
- Collaborative competitive intelligence

**Enterprise Setup:**
- Multiple pipelines (by region/segment)
- Role-based access control
- Manager dashboards
- Cross-team reporting
- Integration with CRM (future)

### Volume Handling

**Low Volume (< 10 campaigns/week):**
- Full research on each prospect
- Maximum personalization
- Individual quality reviews

**Medium Volume (10-50 campaigns/week):**
- Template optimization for efficiency
- Batch similar prospects
- Sampling quality reviews

**High Volume (50+ campaigns/week):**
- Segment-based templates
- Automated quality scoring
- Exception-based reviews
- Consider dedicated sales automation platform

### Data Management

**Retention:**
- Campaign data: Retain indefinitely for optimization
- Email content: Retain 2 years for compliance
- Pipeline data: Sync with source systems

**Privacy:**
- Apollo data: Subject to Apollo's data policies
- Gmail data: Accessed only on search, not stored
- Drive data: Accessed only on search, not stored

**Security:**
- All integrations use OAuth 2.0
- No credentials stored in skill
- API keys managed by user

---

## Future Evolution

This skill is designed to evolve with your sales operations. Planned enhancements:

### Phase 1: Foundation (Current - v1.0)
- Core relationship intelligence
- Pipeline management
- Email sequence generation
- Quality grading framework

### Phase 2: Automation (v1.5)
- Automated stuck deal detection and re-engagement
- Scheduled pipeline health reports
- Proactive campaign suggestions
- Email performance auto-analysis

### Phase 3: Intelligence (v2.0)
- Predictive deal scoring (AI-powered)
- Win probability forecasting
- Optimal send time prediction
- Churn risk identification

### Phase 4: Integration (v2.5)
- CRM sync (Salesforce, HubSpot)
- LinkedIn Sales Navigator integration
- Email sending with approval workflows
- Calendar booking automation

### Phase 5: Team Performance (v3.0)
- Team leaderboards and benchmarks
- Coaching recommendations
- Playbook optimization
- Revenue attribution analytics

### Extensibility Points

The skill architecture supports these customization points:

**Custom Templates:**
- Add industry-specific sequences
- Create persona-based variations
- Build event-triggered templates

**Custom Scoring:**
- Adjust ICP criteria weights
- Add company-specific factors
- Integrate proprietary signals

**Custom Workflows:**
- Define new trigger conditions
- Create approval workflows
- Build custom reporting

**Custom Integrations:**
- Add new data sources
- Connect to internal systems
- Build API extensions

---

## Support Resources

### Documentation
- SKILL.md - Complete operational specification
- README.md - Overview and quick start
- QUICK-START.md - Get running in 15 minutes
- DATA-SOURCES.md - Integration setup details
- REFERENCE.md - Template library and best practices
- APOLLO-INTEGRATION.md - Apollo.io deep dive

### Getting Help
1. Review relevant documentation section
2. Check troubleshooting guide above
3. Ask Claude: "Help me troubleshoot [specific issue]"
4. Review Project Settings → Integrations for connection status

### Feedback & Improvements
Document enhancement requests and issues in a dedicated Asana project. Claude can help implement customizations and optimizations based on your feedback.

---

**Version History:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-11-18 | Initial release with full feature set |

---

*Sales Automator - Transforming relationship intelligence into revenue.*
