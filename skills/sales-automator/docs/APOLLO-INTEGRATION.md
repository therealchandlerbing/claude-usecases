# Apollo.io Integration Guide for Sales Automator

## Overview

This guide explains how to set up and use the Apollo.io integration with your sales-automator skill to enhance prospect research, contact discovery, and lead qualification.

## What Apollo.io Adds

Apollo.io provides access to 210M+ contacts and 35M+ companies with structured data that complements your existing sales intelligence sources:

| Without Apollo | With Apollo |
|----------------|-------------|
| Manual LinkedIn lookup for job titles | Automated contact enrichment with current roles |
| Web search for company size/revenue | Instant firmographic data (revenue, employees, funding) |
| Guessing decision-makers | Targeted search for specific roles with verified emails |
| Generic outreach | ICP-scored leads with tech stack insights |

## Prerequisites

Before setting up Apollo integration:

1. **Apollo.io Account**
   - You need a paid Apollo.io account (free plans don't have API access)
   - Plans start at $49/month for basic API access
   - Sign up at: https://www.apollo.io/pricing

2. **API Key Generation**
   - Log into Apollo.io
   - Navigate to: Settings → Integrations → API
   - Click "Generate API Key"
   - Copy and securely store your API key

3. **Credit Budget Planning**
   - Each API call consumes credits from your plan
   - Typical usage: 50-100 enrichments/day for active sales prospecting
   - Set budget limits in configuration to avoid overuse

## Setup Instructions

### Step 1: Configure API Key

You have two options for providing your Apollo API key:

**Option A: Environment Variable (Recommended)**
```bash
# Add to your ~/.bashrc or ~/.zshrc
export APOLLO_API_KEY="your-api-key-here"

# Or set for current session
export APOLLO_API_KEY="your-api-key-here"
```

**Option B: MCP Configuration**
If using Model Context Protocol (MCP), add to your MCP settings:
```json
{
  "apollo": {
    "api_key": "your-api-key-here"
  }
}
```

**Option C: Direct Configuration**
Add to `skills/sales-automator/config/.env`:
```
APOLLO_API_KEY=your-api-key-here
```

### Step 2: Test API Connection

Verify your API key works:

```bash
curl -H "X-Api-Key: YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     https://api.apollo.io/api/v1/auth/health
```

Expected response:
```json
{
  "status": "healthy"
}
```

### Step 3: Configure Integration Settings

Review and adjust settings in `config/pipeline-config.yaml`:

```yaml
apollo:
  enabled: true  # Set to false to disable

  # Credit Management (Important!)
  credit_management:
    daily_limit: 100        # Adjust based on your plan
    warn_threshold: 80      # Get warning at 80% usage
    priority_prospects_only: false  # true = only enrich hot/warm leads

  # Enrichment Preferences
  enrichment:
    reveal_personal_emails: false  # Costs +1 credit per reveal
    reveal_phone_numbers: false    # Costs +1 credit per reveal
    auto_enrich_new_prospects: true  # Auto-enrich when creating outreach
    enrich_on_pipeline_add: true   # Auto-enrich when adding to Asana

  # Data Quality
  data_preferences:
    minimum_confidence_score: 0.7  # Only use high-confidence matches
    include_employment_history: true
    include_funding_data: true
    include_technology_stack: true

  # Use Cases (enable/disable features)
  use_for:
    cold_outreach: true
    contact_discovery: true
    lead_qualification: true
    data_validation: true
    competitive_intelligence: true
```

### Step 4: Define Your ICP (Ideal Customer Profile)

Apollo works best when it knows your ideal customer profile. Add this to your configuration:

```yaml
# Add to pipeline-config.yaml
ideal_customer_profile:
  employee_count:
    min: 50
    max: 500
    preferred: [100, 200, 300]  # Sweet spot ranges

  revenue:
    min: 5000000   # $5M
    max: 50000000  # $50M

  industries:
    - "SaaS"
    - "Enterprise Software"
    - "FinTech"
    - "HealthTech"

  funding_stages:
    - "Series A"
    - "Series B"
    - "Growth Stage"

  decision_maker_titles:
    - "VP of Sales"
    - "Chief Revenue Officer"
    - "Head of Revenue Operations"
    - "VP of Business Development"

  geographic_focus:
    - "United States"
    - "Canada"
    - "United Kingdom"
```

## Usage Workflows

### Workflow 1: Enrich a Specific Contact

**User Request:**
```
"Create cold outreach for john.smith@acmecorp.com"
```

**What Happens:**

1. **Apollo People Enrichment**
   - API call to enrich john.smith@acmecorp.com
   - Returns: Current job title, company, LinkedIn, employment history, email verification

2. **Apollo Organization Enrichment**
   - Automatically enriches Acme Corp using domain from email
   - Returns: Industry, size, revenue, funding, tech stack

3. **Lead Scoring**
   - Compares firmographics against your ICP
   - Calculates score: Employee count (50-500) +10, Revenue ($10M-$50M) +10, Industry (SaaS) +10, Funding (Series B) +5 = 35 points
   - Result: **Hot Lead** (25-35 points)

4. **Outreach Generation**
   - Uses enriched data to personalize email
   - References John's specific role (VP of Sales)
   - Mentions Acme Corp's Series B funding and growth stage
   - Includes tech stack compatibility (they use Salesforce, you integrate with it)

**Credits Used:** 2 credits (1 for person, 1 for organization)

### Workflow 2: Find Decision-Makers at Target Company

**User Request:**
```
"Find the head of sales at TechStart Inc"
```

**What Happens:**

1. **Apollo People Search**
   - Searches for contacts at TechStart Inc with titles: "VP of Sales", "Head of Sales", "Chief Revenue Officer", "SVP of Sales"
   - Returns top 5 matches with:
     - Current job titles
     - Email addresses (verified status)
     - LinkedIn profiles
     - Tenure at company

2. **Results Ranking**
   - Prioritizes by: Email verification status, seniority, tenure
   - Flags: "Sarah Johnson - VP of Sales - Verified email ✓ - 1.5 years tenure"

3. **Automatic Organization Enrichment**
   - Enriches TechStart Inc to provide context
   - You get: Industry, size, funding stage for better positioning

**Credits Used:** 2 credits (1 for search, 1 for organization enrichment)

### Workflow 3: Build ABM Target Account List

**User Request:**
```
"Build a list of Series B SaaS companies with 200-500 employees in the US"
```

**What Happens:**

1. **Apollo Organization Search**
   - Filters: Employee count 200-500, Industry = SaaS, Funding = Series B, Location = US
   - Returns: 50-100 companies matching criteria

2. **Bulk Organization Enrichment**
   - Enriches top 25 companies (using bulk endpoint for efficiency)
   - Gets full firmographics for each: revenue, tech stack, funding details, growth signals

3. **ICP Scoring**
   - Scores each company against your ideal customer profile
   - Ranks by best fit: Score 30-35 = Tier 1, Score 20-29 = Tier 2, <20 = Tier 3

4. **Decision-Maker Discovery**
   - For top 10 companies (Tier 1), finds VP/Director level decision-makers
   - Returns 3-5 contacts per company with verified emails

5. **Asana Pipeline Population**
   - Creates deal tasks in Asana for top 10 accounts
   - Populates custom fields: Company Size, Industry, Lead Score, Decision-Maker contacts
   - Sets due dates for initial outreach

**Credits Used:** ~40 credits (1 org search + 25 org enrichments + 10 people searches + 4 decision-maker enrichments)

### Workflow 4: Competitive Displacement

**User Request:**
```
"Find companies using [Competitor Product] that match our ICP"
```

**What Happens:**

1. **Apollo Organization Search with Tech Filter**
   - Filters: Technologies used = "competitor-product", Employee count 50-500, Revenue $5M-$50M
   - Returns: Companies currently using your competitor's product

2. **Tech Stack Analysis**
   - Enriches companies to see full tech stack
   - Identifies: Integration opportunities, tech stack gaps, migration candidates

3. **Qualification**
   - Scores based on:
     - Recent funding (Series A/B = higher switching likelihood) +10
     - Complementary tech (integrations you support) +5
     - Growth signals (hiring, revenue growth) +5

4. **Outreach Strategy**
   - For qualified accounts, generates competitive displacement campaign
   - Messaging references: Their current solution, your differentiation, integration benefits
   - Timing trigger: Use funding announcements or tech stack gaps

**Credits Used:** ~25 credits (1 org search + 20 org enrichments + 4 people searches)

## Best Practices

### 1. Credit Budget Management

**Track Daily Usage:**
```
Daily Credit Budget: 100 credits
Allocation:
- 50 credits → Cold outreach enrichment (priority)
- 30 credits → Decision-maker discovery
- 20 credits → Lead qualification for Asana deals
```

**When to Skip Apollo:**
- Existing customers (you already have accurate data)
- Recent enrichments (<30 days, use cached)
- Low-priority prospects (save credits for hot leads)
- After reaching daily limit (falls back to web search)

### 2. Data Quality Checks

**Always Verify:**
- Email status = "verified" before sending cold emails
- `current: true` flag in employment history (person still works there)
- Confidence score ≥ 0.7 for contact matches
- Cross-reference Apollo data with LinkedIn for critical contacts

**Red Flags:**
- Email status = "guessed" → Validate with separate email verification tool
- No LinkedIn URL → May be inaccurate match
- Confidence score < 0.5 → Don't use for outreach

### 3. Multi-Source Validation

Apollo provides structured data, but complement with:

| Apollo Provides | Complement With |
|----------------|-----------------|
| Current job title | LinkedIn profile (verify, check tenure) |
| Company revenue range | Recent news (acquisitions, funding rounds) |
| Tech stack | Web search (new tool adoptions not in Apollo yet) |
| Employee count | LinkedIn company page (verify growth) |

**Example Validation Workflow:**
1. Apollo says: "John Doe, VP of Sales at Acme Corp"
2. LinkedIn confirms: VP of Sales (current), 2 years tenure ✓
3. Gmail shows: Last emailed 6 months ago when he was Director (promoted since!) ✓
4. Web search: Acme Corp raised Series B 3 months ago (good timing) ✓

### 4. Enrichment Timing Strategy

**Real-time Enrichment (Recommended):**
- When user requests: "Create outreach for [email/company]"
- When adding deal to Asana pipeline
- When qualifying inbound lead

**Batch Enrichment (Cost-Efficient):**
- Weekly ABM list updates (enrich 50-100 companies)
- Monthly customer data refresh (verify employment)
- Quarterly ICP analysis (identify new target accounts)

**Skip Enrichment:**
- Existing customer outreach (use internal CRM data)
- Personal/network contacts (you know them)
- Non-business contacts
- Re-enrichment within 30 days (use cached data)

### 5. ICP-Based Routing

Configure automatic lead scoring:

```yaml
# In pipeline-config.yaml
lead_scoring_rules:
  hot_lead_criteria:  # Score 25-35
    - employee_count: [100, 200, 300, 400, 500]
    - revenue_range: ["10M-50M", "50M-100M"]
    - funding_stage: ["Series B", "Series C"]
    - industry: ["SaaS", "FinTech"]

  warm_lead_criteria:  # Score 15-24
    - employee_count: [50, 100, 500, 1000]
    - revenue_range: ["5M-10M", "50M-100M"]
    - funding_stage: ["Series A", "Series B", "Profitable"]

  cold_lead_criteria:  # Score < 15
    - employee_count: [1, 50, 1000, 5000]
    - revenue_range: ["0-5M", "100M+"]
```

**Auto-Actions Based on Score:**
- **Hot (25-35):** Immediate outreach, multi-threaded campaign, exec intro
- **Warm (15-24):** Standard outreach sequence, nurture campaign
- **Cold (<15):** Long-term nurture, content marketing, skip immediate outreach

## Troubleshooting

### Issue: "API authentication failed"

**Cause:** Invalid or expired API key

**Solution:**
1. Verify API key is correct: `echo $APOLLO_API_KEY`
2. Re-generate API key in Apollo dashboard
3. Test connection: `curl -H "X-Api-Key: YOUR_KEY" https://api.apollo.io/api/v1/auth/health`
4. Check for typos or extra spaces in environment variable

### Issue: "No match found" for contact enrichment

**Cause:** Apollo doesn't have data on this contact, or matching parameters insufficient

**Solutions:**
1. Provide more parameters: email + first_name + last_name + organization_name
2. Try organization enrichment instead (get company data first, then search for people)
3. Check for typos in email address
4. Fall back to LinkedIn manual lookup + web search

### Issue: "Daily credit limit reached"

**Cause:** Exceeded your configured daily credit limit

**Solutions:**
1. Increase `daily_limit` in config (if your plan supports it)
2. Enable `priority_prospects_only: true` (only enrich hot/warm leads)
3. Use bulk enrichment endpoints (10 at once = more efficient)
4. Cache results for 30 days (avoid re-enriching same contacts)
5. Wait until tomorrow (limits reset daily)

### Issue: Data is outdated (person no longer at company)

**Cause:** Apollo data lags real-time employment changes

**Solutions:**
1. Check `employment_history` array for `current: true` flag
2. Verify with LinkedIn profile (manual check for critical contacts)
3. Check Gmail/Calendar for recent interactions (overrides Apollo if conflicting)
4. Report inaccuracy to Apollo support (helps improve database)

### Issue: Too many search results (overwhelming)

**Cause:** Search filters too broad

**Solutions:**
1. Add more filters: combine title + seniority + location + company size
2. Use `q_keywords` for more specific matching
3. Reduce `page_size` from 100 to 10-25 (get top matches only)
4. Add industry filter to narrow companies
5. Filter by recent job changes (`hired_at_organization_since` parameter)

### Issue: Enrichment returns wrong person/company

**Cause:** Low confidence match with insufficient parameters

**Solutions:**
1. Check `confidence_score` in response (should be ≥ 0.7)
2. Provide more identifying information (full name + company + location)
3. Cross-validate with LinkedIn before using data
4. Set higher `minimum_confidence_score` in config (0.8 or 0.9)

## Credit Cost Reference

| Action | Credits Used | Example |
|--------|--------------|---------|
| People Enrichment | 1 credit | Enrich john@acme.com |
| Organization Enrichment | 1 credit | Enrich acme.com |
| People Search | 1 credit | Find "VP Sales" at Acme Corp |
| Organization Search | 1 credit | Find fintech companies 100-500 employees |
| Bulk People Enrichment (10 people) | 10 credits | Enrich 10 contacts at once |
| Bulk Org Enrichment (10 orgs) | 10 credits | Enrich 10 companies at once |
| Reveal Personal Email | +1 credit | Additional per person |
| Reveal Phone Number | +1 credit | Additional per person |

**Example Campaign Costs:**

**Cold Outreach Campaign (1 prospect):**
- 1 person enrichment = 1 credit
- 1 organization enrichment = 1 credit
- **Total: 2 credits**

**ABM List Building (25 target accounts):**
- 1 organization search = 1 credit
- 25 organization enrichments (bulk) = 25 credits
- 10 people searches (top companies) = 10 credits
- 30 people enrichments (3 contacts × 10 companies) = 30 credits
- **Total: 66 credits**

**Competitive Displacement Research:**
- 1 tech stack search = 1 credit
- 50 organization enrichments = 50 credits
- 20 people searches = 20 credits
- **Total: 71 credits**

## Advanced Strategies

### Strategy 1: Waterfall Enrichment

Optimize credit usage with prioritized enrichment:

```
1. Check Asana (existing deal data) → Free
2. Check Gmail (past interactions) → Free
3. [If incomplete] Apollo Enrichment → 1-2 credits
4. [If Apollo fails] Web Search → Free
```

Only use Apollo if internal sources don't have sufficient data.

### Strategy 2: Enrichment Caching

Save credits by caching Apollo results:

```yaml
# In config
apollo:
  fallback:
    cache_results_days: 30  # Cache for 30 days
```

When enriching john@acme.com:
1. Check cache (was it enriched in last 30 days?)
2. If yes → Use cached data (0 credits)
3. If no → Call Apollo API (1 credit), cache result

### Strategy 3: Selective Enrichment

Only enrich high-value prospects:

```yaml
apollo:
  credit_management:
    priority_prospects_only: true  # Only enrich hot/warm leads

  enrichment:
    enrich_on_pipeline_add: true   # Auto-enrich when added to Asana
    auto_enrich_new_prospects: false  # Manual trigger only
```

Workflow:
1. User says: "Add Acme Corp to pipeline as Hot lead"
2. System automatically enriches Acme Corp via Apollo
3. User says: "Should we pursue XYZ Corp?"
4. System DOES NOT auto-enrich (manual request required)

### Strategy 4: ICP-Based Filtering

Pre-filter before enriching to save credits:

```
1. User: "Build list of fintech companies"
2. Apollo Organization Search (filters: fintech, 100-500 employees, Series A/B)
3. Get 100 companies (1 credit)
4. Filter by location/other criteria (free, client-side)
5. Narrow to top 25 matches (free, client-side)
6. Enrich only top 25 (25 credits) instead of all 100 (100 credits)
```

**Savings:** 75 credits per campaign

## Integration Checklist

Before going live with Apollo integration:

- [ ] Apollo.io paid account active
- [ ] API key generated and tested
- [ ] API key stored in environment variable or MCP config
- [ ] `pipeline-config.yaml` Apollo section configured
- [ ] Daily credit limit set (aligned with your plan)
- [ ] Ideal Customer Profile (ICP) defined
- [ ] Lead scoring rules configured
- [ ] Enrichment cache enabled (30 day default)
- [ ] Priority prospects filter configured (if using)
- [ ] Fallback to web search enabled
- [ ] Test enrichment: "Enrich test@example.com" works
- [ ] Test search: "Find VP of Sales at [test company]" works
- [ ] Monitor credit usage for first week
- [ ] Adjust daily limit based on actual usage patterns

## Support & Resources

**Apollo.io Documentation:**
- API Docs: https://docs.apollo.io/
- Support: help@apollo.io
- Status Page: https://status.apollo.io/

**Sales-Automator Support:**
- Issues: Create GitHub issue in repository
- Questions: Ask Claude during sales automation sessions

**Credit Optimization:**
- Review weekly usage: Monitor Apollo dashboard
- Adjust daily limits: Based on ROI of enriched leads
- Optimize workflows: Use caching, selective enrichment, ICP filtering

---

**You're now ready to use Apollo.io integration to supercharge your sales automation with structured, verified prospect data!**
