# Apollo.io Workflow Examples

This document provides real-world examples of how to use Apollo.io integration with sales-automator for common prospecting and outreach scenarios.

---

## Example 1: Cold Outreach to a Specific Contact

### User Request
```
"Create cold outreach for sarah.jones@techstart.io"
```

### Workflow Execution

**Step 1: Apollo People Enrichment**
```
API Call: POST /api/v1/people/match
Payload: {
  "email": "sarah.jones@techstart.io"
}

Response:
{
  "person": {
    "id": "5f7b1b4b9d3e2a0017a1b0a1",
    "first_name": "Sarah",
    "last_name": "Jones",
    "name": "Sarah Jones",
    "title": "VP of Product",
    "email": "sarah.jones@techstart.io",
    "email_status": "verified",
    "linkedin_url": "linkedin.com/in/sarahjones",
    "organization": {
      "name": "TechStart Inc.",
      "domain": "techstart.io"
    },
    "employment_history": [
      {
        "organization_name": "TechStart Inc.",
        "title": "VP of Product",
        "current": true,
        "start_date": "2023-01"
      },
      {
        "organization_name": "Google",
        "title": "Senior Product Manager",
        "current": false,
        "start_date": "2019-06",
        "end_date": "2022-12"
      }
    ]
  }
}

Credits Used: 1
```

**Step 2: Apollo Organization Enrichment**
```
API Call: POST /api/v1/organizations/enrich
Payload: {
  "domain": "techstart.io"
}

Response:
{
  "organization": {
    "name": "TechStart Inc.",
    "domain": "techstart.io",
    "industry": "SaaS / Enterprise Software",
    "revenue_range": "$5M-$10M",
    "estimated_num_employees": 75,
    "funding_stage": "Series A",
    "total_funding": "$8M",
    "founded_year": 2020,
    "locations": ["San Francisco, CA", "Remote"],
    "technologies": ["AWS", "React", "Python", "PostgreSQL"]
  }
}

Credits Used: 1
```

**Step 3: Lead Scoring**
```
ICP Criteria Check:
✓ Employee count (75) → within 50-500 range (+10 points)
✓ Revenue ($5M-$10M) → within $5M-$50M range (+10 points)
✓ Industry (SaaS) → matches target industry (+10 points)
✓ Funding (Series A) → growth stage (+5 points)

Total Score: 35 points
Lead Classification: HOT LEAD
```

**Step 4: Intelligence Synthesis**
```
Intelligence Brief:

Contact Profile:
- Name: Sarah Jones
- Title: VP of Product
- Email: sarah.jones@techstart.io (VERIFIED ✓)
- LinkedIn: linkedin.com/in/sarahjones
- Background: 3.5 years at Google as Senior PM (enterprise product experience)
- Tenure at TechStart: 1.5 years (established, not too new)

Company Profile:
- Company: TechStart Inc.
- Stage: Series A ($8M raised)
- Size: 75 employees
- Industry: SaaS / Enterprise Software
- Tech Stack: AWS, React, Python (modern, cloud-native)
- Locations: SF + Remote

ICP Fit: HOT (35/35 points)
- Perfect employee count for our solution
- Revenue sweet spot
- Target industry (SaaS)
- Growth stage (Series A = buying mode)

Positioning Opportunities:
- Sarah has Google enterprise experience → understands complex products
- TechStart's tech stack aligns with our integrations (AWS, React)
- Series A timing → investing in tools/infrastructure
- Product-led company → VP of Product likely involved in tool decisions
```

**Step 5: Outreach Generation**

Generated Email Sequence:

**Email 1 (Day 0): Insight + Value**
```
Subject: Product infrastructure for Series A scaling [TechStart]

Hi Sarah,

I've been following TechStart's growth since your Series A - congrats on the $8M raise.

I saw you're building product infrastructure for a 75-person team. Based on your background at Google and what you're scaling at TechStart, I thought this might be relevant:

We helped [Similar SaaS Company] reduce their product feedback cycle time by 40% after their Series A by [specific approach relevant to TechStart's stack].

The challenge they faced: Too many product tools, data scattered across AWS services, hard to get signal from noise as they scaled past 50 people.

Sound familiar?

I'm not sure if this is on your radar, but figured it was worth 30 seconds to share.

Best,
[Your Name]

P.S. I noticed you're using React + AWS - we have native integrations that just work with your stack.
```

**Result:**
- Hyper-personalized (references Series A, Google background, tech stack)
- Credible (mentions specific technologies TechStart uses)
- Timely (Series A = scaling infrastructure)
- Relevant (similar company example for social proof)
- Low-pressure (soft ask)

**Total Credits Used:** 2 credits (1 person + 1 organization)

---

## Example 2: Find Decision-Makers at Target Company

### User Request
```
"Find the head of sales at Acme Corporation"
```

### Workflow Execution

**Step 1: Apollo People Search**
```
API Call: POST /api/v1/mixed_people/search
Payload: {
  "q_organization_name": "Acme Corporation",
  "person_titles": [
    "VP of Sales",
    "Head of Sales",
    "Chief Revenue Officer",
    "SVP of Sales",
    "Director of Sales"
  ],
  "per_page": 10
}

Response:
{
  "people": [
    {
      "id": "...",
      "name": "Michael Chen",
      "title": "VP of Sales",
      "email": "michael.chen@acmecorp.com",
      "email_status": "verified",
      "linkedin_url": "linkedin.com/in/michaelchen",
      "seniority": "VP",
      "organization_name": "Acme Corporation",
      "hired_at": "2022-08-01"
    },
    {
      "id": "...",
      "name": "Jennifer Martinez",
      "title": "Director of Sales",
      "email": "j.martinez@acmecorp.com",
      "email_status": "verified",
      "linkedin_url": "linkedin.com/in/jennifermartinez",
      "seniority": "Director",
      "organization_name": "Acme Corporation",
      "hired_at": "2021-03-15"
    },
    {
      "id": "...",
      "name": "David Park",
      "title": "Head of Enterprise Sales",
      "email": "david.park@acmecorp.com",
      "email_status": "guessed",
      "linkedin_url": "linkedin.com/in/davidpark",
      "seniority": "Director",
      "organization_name": "Acme Corporation",
      "hired_at": "2023-01-10"
    }
  ]
}

Credits Used: 1
```

**Step 2: Organization Enrichment (Auto-triggered)**
```
API Call: POST /api/v1/organizations/enrich
Payload: {
  "domain": "acmecorp.com"
}

Response:
{
  "organization": {
    "name": "Acme Corporation",
    "domain": "acmecorp.com",
    "industry": "Manufacturing",
    "estimated_num_employees": 350,
    "revenue_range": "$25M-$50M",
    "founded_year": 2010,
    "locations": ["Chicago, IL", "Dallas, TX"]
  }
}

Credits Used: 1
```

**Step 3: Contact Prioritization**
```
Decision-Maker Analysis:

Primary Contact:
✓ Michael Chen - VP of Sales
  - Email: Verified ✓
  - Seniority: VP (highest authority)
  - Tenure: 1.5 years (established, knows company well)
  - LinkedIn: Available for research

Secondary Contact:
✓ Jennifer Martinez - Director of Sales
  - Email: Verified ✓
  - Seniority: Director
  - Tenure: 2.5 years (longer tenure, might know pain points well)
  - LinkedIn: Available

Tertiary Contact:
⚠️ David Park - Head of Enterprise Sales
  - Email: Guessed (needs verification)
  - Seniority: Director
  - Tenure: 10 months (relatively new, might be open to new approaches)
  - Note: "Guessed" email - validate before using

Recommended Approach:
1. Primary outreach to Michael Chen (VP)
2. If no response in 7 days, secondary outreach to Jennifer Martinez
3. Multi-thread: Reach both with different angles after 14 days
```

**Step 4: Multi-Contact Campaign**
```
Campaign Structure:

Thread 1: Michael Chen (VP of Sales)
- Email 1 (Day 0): Executive-level value prop
- Email 2 (Day 7): Case study from similar manufacturing company
- Email 3 (Day 14): ROI calculator + meeting invite

Thread 2: Jennifer Martinez (Director)
- Email 1 (Day 10): Tactical pain point solution
- Email 2 (Day 17): Product demo offer

Both tracked in Asana:
- Task: "Acme Corporation - Sales Tool Partnership"
- Subtasks:
  - [ ] Email Michael Chen (Thread 1)
  - [ ] Follow-up Michael Chen
  - [ ] Email Jennifer Martinez (Thread 2)
- Custom Fields:
  - Lead Score: Warm (company size 350, revenue $25M-$50M)
  - Primary Contact: Michael Chen
  - Secondary Contact: Jennifer Martinez
```

**Total Credits Used:** 2 credits (1 search + 1 organization)

---

## Example 3: Build ABM Target Account List

### User Request
```
"Build a list of Series B SaaS companies with 200-500 employees in the United States"
```

### Workflow Execution

**Step 1: Apollo Organization Search**
```
API Call: POST /api/v1/mixed_companies/search
Payload: {
  "organization_num_employees_ranges": ["200-500"],
  "organization_industry_tag_ids": ["saas"],
  "funding_stages": ["Series B"],
  "organization_locations": ["United States"],
  "per_page": 50
}

Response:
{
  "organizations": [
    { "id": "...", "name": "CloudFlow Inc.", "domain": "cloudflow.io" },
    { "id": "...", "name": "DataPulse", "domain": "datapulse.com" },
    { "id": "...", "name": "WorkSync", "domain": "worksync.io" },
    ... (47 more companies)
  ],
  "total_count": 127
}

Credits Used: 1
```

**Step 2: Bulk Organization Enrichment (Top 25)**
```
API Call: POST /api/v1/organizations/bulk_enrich
Payload: {
  "domains": [
    "cloudflow.io",
    "datapulse.com",
    "worksync.io",
    ... (22 more)
  ]
}

Response: (25 enriched organization profiles)

Credits Used: 25 (bulk pricing)
```

**Step 3: ICP Scoring & Ranking**
```
Scoring Results:

Tier 1 (Hot - Score 30-35):
1. CloudFlow Inc. - Score: 35
   - Employees: 320 (+10)
   - Revenue: $20M-$50M (+10)
   - Industry: SaaS (+10)
   - Funding: Series B, $25M (+5)
   - Recent hiring surge in sales/eng teams (+bonus)

2. DataPulse - Score: 33
   - Employees: 280 (+10)
   - Revenue: $15M-$25M (+10)
   - Industry: Data/SaaS (+10)
   - Funding: Series B, $18M (+5)
   - Tech stack includes tools we integrate with (+bonus)

3. WorkSync - Score: 32
   - Employees: 410 (+10)
   - Revenue: $30M-$50M (+10)
   - Industry: Productivity SaaS (+10)
   - Funding: Series B, $30M (+5)

Tier 2 (Warm - Score 20-29):
4-10. [7 more companies]

Tier 3 (Lower Priority - Score <20):
11-25. [15 more companies]
```

**Step 4: Decision-Maker Discovery (Tier 1 Only)**
```
For each Tier 1 company, search for:
- VP/Director of Sales
- VP/Director of Revenue Operations
- Chief Revenue Officer

API Calls: 3 people searches × 10 companies = 30 searches

Sample Result (CloudFlow Inc.):
- Primary: "Jessica Wu - VP of Sales - verified ✓"
- Secondary: "Alex Thompson - Director of RevOps - verified ✓"
- Tertiary: "Mark Stevens - CRO - verified ✓"

Credits Used: 10 (people searches)
```

**Step 5: Asana Pipeline Creation**
```
For each Tier 1 account, create:

Task: "[Company Name] - ABM Outreach"
Custom Fields:
  - Deal Stage: Outreach
  - Deal Value: $50,000 (estimated based on company size)
  - Lead Score: Hot
  - Company Size: [from Apollo]
  - Industry: SaaS
  - Funding Stage: Series B
  - Lead Source: Outbound ABM

Task Description:
---
## Company Profile
- Employees: [from Apollo]
- Revenue: [from Apollo]
- Funding: [from Apollo]
- Tech Stack: [from Apollo]
- Locations: [from Apollo]

## Decision-Makers
- Primary: [Name, Title, Email, LinkedIn]
- Secondary: [Name, Title, Email, LinkedIn]

## ICP Fit Score: 35/35 ✓

## Positioning Strategy
[Auto-generated based on tech stack, industry, funding stage]

## Next Actions
- [ ] Send Email 1 to Primary contact (Day 0)
- [ ] LinkedIn connect request (Day 2)
- [ ] Send Email 2 (Day 7)
- [ ] Multi-thread to Secondary if no response (Day 14)
---

Subtasks:
- [ ] Email VP Sales - [Subject Line]
- [ ] Email Dir RevOps - [Subject Line]
- [ ] LinkedIn Connect CRO
```

**Step 6: Campaign Brief Generation**
```
ABM Campaign Summary:

Target List: Series B SaaS (200-500 employees)
Total Identified: 127 companies
Enriched & Scored: 25 companies
Tier 1 (Hot): 10 accounts
Tier 2 (Warm): 7 accounts
Tier 3 (Lower Priority): 8 accounts

Focus: Top 10 Tier 1 accounts
Decision-Makers Identified: 30 contacts across 10 companies
Outreach Timeline: 4-week multi-touch campaign

Asana Tasks Created: 10 (one per account)
Next Action: Launch outreach to Tier 1 starting [Date]

Estimated Conversion:
- 30% response rate = 3 meetings
- 30% meeting-to-opportunity = 1 opportunity
- $50K opportunity value
```

**Total Credits Used:** 36 credits
- 1 organization search
- 25 organization enrichments
- 10 people searches

---

## Example 4: Competitive Displacement Campaign

### User Request
```
"Find companies using [Competitor Product] that match our ICP"
```

### Workflow Execution

**Step 1: Apollo Technology Search**
```
API Call: POST /api/v1/mixed_companies/search
Payload: {
  "technologies": ["competitor-product-id"],
  "organization_num_employees_ranges": ["100-500"],
  "organization_revenue_ranges": ["5M-50M"],
  "per_page": 50
}

Response:
{
  "organizations": [50 companies using competitor product],
  "total_count": 143
}

Credits Used: 1
```

**Step 2: Bulk Enrichment + Tech Stack Analysis**
```
For top 25 companies, enrich to get full tech stack:

API Call: POST /api/v1/organizations/bulk_enrich (25 companies)

Analysis:
Company: FinFlow Systems
- Using Competitor: ✓
- Also using: Salesforce, HubSpot, AWS, PostgreSQL
- Integration opportunities:
  ✓ We integrate with Salesforce (they already use it)
  ✓ We integrate with HubSpot (they already use it)
  ✓ Native AWS support (they're on AWS)
- Tech stack gap: Missing [feature your product provides]
- Migration score: High (complementary tools, easy integration)

Company: PaymentCo
- Using Competitor: ✓
- Also using: Stripe, Segment, Google Cloud
- Integration opportunities:
  ⚠️ Different cloud provider (GCP vs our AWS focus)
  ✓ Stripe integration available
- Migration score: Medium

Credits Used: 25
```

**Step 3: Qualification + Prioritization**
```
Scoring Criteria:
- Recent funding (+10)
- Complementary tech stack (+5)
- Competitor product tier (basic = +10, enterprise = +5)
- Growth signals (hiring surge = +5)

Top 10 Qualified Accounts:
1. FinFlow Systems - Score 35
   - Series B (8 months ago) = fresh capital ✓
   - Using competitor's basic tier = switching easier ✓
   - Complementary tools (Salesforce, HubSpot) ✓
   - Hiring 15+ sales/eng roles = growth mode ✓

2. PaymentCo - Score 28
   - Profitably growing
   - Using competitor's mid tier
   - Some tech overlap
   - Moderate hiring

...
```

**Step 4: Decision-Maker Discovery**
```
For top 10 companies, find:
- VP/Director of Operations (likely product buyer)
- VP/Director of Engineering (technical decision-maker)
- VP/Director of Sales (end user/champion)

API Calls: 10 people searches

Sample (FinFlow Systems):
- Mark Johnson - VP of Operations (verified ✓)
- Lisa Chang - Director of Engineering (verified ✓)
- Tom Brady - VP of Sales (verified ✓)

Credits Used: 10
```

**Step 5: Competitive Displacement Messaging**
```
Email Campaign (FinFlow Systems):

Subject: Alternatives to [Competitor] for Series B scaling

Hi Mark,

I saw FinFlow raised $25M in March - congrats!

Quick question: As you scale past 250 people, are you finding [Competitor]'s basic tier limiting?

We've helped 3 fintech companies (including [Similar Company] at your stage) migrate from [Competitor] to [Your Product] because:

1. Native Salesforce + HubSpot integration (I saw you use both)
2. AWS-optimized (vs Competitor's generic cloud support)
3. [Key feature] that Competitor doesn't have in their basic tier

The migration took [Similar Company] 2 weeks and they're seeing [specific metric improvement].

Worth a quick call to see if there's a fit?

Best,
[Your Name]

P.S. If you're locked into a Competitor contract, we have a buyout program for Series B+ companies.
```

**Result:**
- Hyper-personalized (references funding, tech stack, tier)
- Credible (similar company proof point)
- Low-friction (2-week migration, buyout option)
- Timely (Series B = re-evaluating tools)

**Total Credits Used:** 36 credits
- 1 tech search
- 25 org enrichments
- 10 people searches

---

## Example 5: Re-Engage Cold Lead with New Context

### User Request
```
"We reached out to Acme Corp 6 months ago with no response. Should we try again?"
```

### Workflow Execution

**Step 1: Check Internal History**
```
Asana: Deal exists, stage = "Cold"
Gmail: Last email sent 6 months ago (no response)
Calendar: No meetings scheduled
```

**Step 2: Apollo Re-Enrichment**
```
API Call: POST /api/v1/organizations/enrich
Payload: { "domain": "acmecorp.com" }

NEW Data Since Last Enrichment (6 months ago):
- Employees: 150 → 280 (87% growth!)
- Revenue: $10M-$15M → $20M-$30M (significant growth)
- Funding: Series A → Series B ($30M raised 3 months ago)
- New C-Level hire: New CRO joined 2 months ago
- Tech stack additions: Added Salesforce, Slack, AWS

Credits Used: 1
```

**Step 3: Contact Re-Verification**
```
API Call: POST /api/v1/people/match
Payload: { "email": "john.doe@acmecorp.com" }

Response:
- John Doe: Still at Acme Corp ✓
- Title: Was "Director of Sales" → NOW "VP of Sales" (promoted!)
- Employment: Current ✓

NEW Decision-Maker:
- Sarah Williams: New CRO (joined 2 months ago)
- Email: sarah.williams@acmecorp.com (verified)
- Background: Previously CRO at [Known SaaS Company]

Credits Used: 1
```

**Step 4: Re-Engagement Analysis**
```
Re-Engagement Triggers:
✓ Series B funding ($30M) 3 months ago = buying mode
✓ 87% headcount growth = scaling pains
✓ New CRO hired = re-evaluating sales stack
✓ Original contact (John) promoted to VP = higher authority now
✓ Added Salesforce recently = investing in sales infrastructure

Recommendation: HIGH PRIORITY RE-ENGAGEMENT
- New CRO = fresh perspective, no prior rejection bias
- John's promotion = he has more decision-making authority now
- Series B + growth = budget + urgency
```

**Step 5: Re-Engagement Campaign**
```
Multi-Thread Approach:

Email 1: To Sarah Williams (New CRO)
Subject: Welcome to Acme - Sales infrastructure for 2x headcount growth

Hi Sarah,

Congrats on joining Acme as CRO! I saw your announcement on LinkedIn.

I reached out to Acme 6 months ago, but timing wasn't right (you were pre-Series B, smaller team).

A lot has changed:
- $30M Series B in April ✓
- Headcount 150 → 280 (incredible growth) ✓
- You're now building the RevOps infrastructure ✓

We help Series B companies scaling revenue teams manage [specific challenge].

Companies like [Similar Company at Your Previous Company] used us to [outcome].

15 minutes to explore if there's a fit?

Best,
[Your Name]

---

Email 2: To John Doe (Original Contact, Now VP)
Subject: Congrats on the promotion, John - following up

Hi John,

Congrats on the VP of Sales promotion! Well-deserved.

I reached out 6 months ago about [solution]. Timing wasn't quite right then (pre-Series B, smaller scale).

Now that you've 2x'd the team and have a new CRO focused on infrastructure, figured it was worth checking in.

We've helped [Similar Company] manage similar hypergrowth (150→280 headcount in 6 months is impressive!).

Worth reconnecting?

Best,
[Your Name]
```

**Result:**
- Fresh angle (new CRO, no rejection history)
- Credibility (acknowledges what changed)
- Timely (Series B, new exec, growth)
- Multi-threaded (2 contacts, higher success rate)

**Total Credits Used:** 2 credits

---

## Key Takeaways

### Credit Optimization
- **Basic enrichment**: 2 credits (person + org)
- **Decision-maker discovery**: 2-3 credits (search + enrichments)
- **ABM list building**: 30-40 credits for 10 quality accounts
- **Competitive research**: 35-40 credits for actionable intel

### Best Practices
1. **Always enrich before outreach** - 2 credits for personalized email = higher conversion
2. **Use bulk endpoints** - 25 individual calls = 25 credits, 1 bulk call (25 records) = 25 credits but faster
3. **Cache results** - Re-enriching same contact wastes credits
4. **Verify emails** - Only use "verified" emails for cold outreach (avoid bounces)
5. **Multi-source validation** - Cross-check Apollo data with LinkedIn for critical contacts

### ROI Calculation
- **Without Apollo**: Generic outreach, 2-5% response rate
- **With Apollo**: Personalized outreach, 15-30% response rate
- **Break-even**: If 2 credits ($0.20-$0.40) leads to even one extra meeting, ROI is positive
- **Typical conversion**: 100 credits/month → 50 enriched prospects → 15 responses → 5 meetings → 1 deal

---

**These examples demonstrate how Apollo.io transforms generic sales prospecting into highly targeted, personalized, data-driven outreach campaigns.**
