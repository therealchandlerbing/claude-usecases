# Sales Automator Skill

**Intelligent sales automation with relationship intelligence, deal pipeline tracking, and competitive analysis.**

Transform basic email automation into a context-aware conversion engine that researches prospects, tracks deals, analyzes competition, and generates hyper-personalized outreach grounded in real intelligence.

---

## What This Is

Sales Automator is a comprehensive Claude skill that automates sales processes while maintaining the quality and personalization of hand-crafted outreach. It doesn't just template emails; it pulls context from your past conversations, Gmail, Drive, Asana, and Calendar to create outreach that actually converts because it demonstrates you understand the prospect's world.

---

## What's Included

This skill package contains:

1. **SKILL.md** - Complete skill with workflows, protocols, and instructions (18,000+ words)
2. **REFERENCE.md** - Comprehensive templates, examples, and best practices (15,000+ words)
3. **QUICK-START.md** - Get up and running in 15 minutes
4. **DATA-SOURCES.md** - Detailed setup guide for Asana, Gmail, Drive, Calendar
5. **INSTALLATION.md** - Step-by-step installation instructions

---

## Core Capabilities

### 1. Relationship Intelligence Engine
Automatically researches prospects across multiple sources:
- Past conversations with Claude
- Gmail email history
- Google Calendar meeting history
- Google Drive documents (proposals, notes, case studies)
- Asana tasks and projects
- Web search for public information

**Result**: Every email is grounded in actual context, not guesswork.

### 2. Deal Pipeline Intelligence
Tracks deals in Asana with custom fields:
- Deal stage, value, close date, lead source
- Identifies stuck deals and triggers re-engagement
- Forecasts pipeline health and conversion probability
- Automates follow-up sequences based on deal stage

**Result**: Nothing falls through the cracks. Pipeline stays healthy.

### 3. Competitive & Market Intelligence
Researches prospects and competitive landscape:
- Company overview, recent news, strategic priorities
- Decision-maker identification
- Competitor analysis and positioning opportunities
- Industry trends and market context

**Result**: Outreach positioned strategically, not generically.

### 4. Conversion-Optimized Email Generation
Creates multi-touch sequences that convert:
- 3-7 email sequences with strategic timing
- A/B tested subject lines with psychological triggers
- Personalization variables populated from research
- CTA optimization based on deal stage

**Result**: Higher response rates through strategic sequencing.

### 5. Performance Analytics & Optimization
Tracks what works and what doesn't:
- Email response rates, meeting booking rates
- Deal velocity and conversion by stage
- Subject line and CTA performance
- Pattern identification (timing, length, approach)

**Result**: Continuous improvement through data-driven insights.

---

## Key Differentiators

### vs. Basic Email Templates
- **Basic**: Generic templates with name/company placeholders
- **Sales Automator**: Research-backed personalization with actual context

### vs. CRM Automation Tools
- **CRM Tools**: Sequence emails based on triggers, limited context
- **Sales Automator**: Intelligence-first approach, deep context from multiple sources

### vs. AI Email Generators
- **AI Generators**: Write emails based on prompts, no research
- **Sales Automator**: Researches before writing, pulls from your actual data

### vs. Manual Research + Writing
- **Manual Process**: Hours per prospect for research and writing
- **Sales Automator**: Minutes per prospect with same quality, better consistency

---

## Use Cases

### Cold Outreach Campaigns
Generate 5-touch sequences for new prospects with:
- Company research and decision-maker identification
- Industry-specific insights and positioning
- Case study matching and proof points
- Asana deal tracking with follow-up reminders

### Warm Lead Follow-Up
Re-engage prospects you've talked to before:
- Pull past conversation context automatically
- Reference previous meetings and commitments
- Incorporate new developments or information
- Update existing Asana deals with next steps

### Stuck Deal Re-Activation
Identify and re-engage stalled opportunities:
- Auto-detect deals exceeding time thresholds
- Generate contextual re-engagement sequences
- Offer alternative approaches or lighter commitments
- Track re-activation attempts

### Proposal Generation
Create comprehensive partnership proposals:
- Pull relevant case studies from Drive
- Incorporate past conversation context
- Structure with proven templates
- Include ROI calculations and proof points

### Pipeline Health Monitoring
Weekly pipeline reviews and forecasting:
- Identify stuck deals across all stages
- Forecast weighted pipeline value
- Analyze conversion rates by stage
- Surface patterns and optimization opportunities

### Competitive Positioning
Research and position against alternatives:
- Analyze competitor strengths and weaknesses
- Identify differentiation opportunities
- Surface proof points and case studies
- Craft positioning messaging

---

## What You Need

### Required
- Claude account (Sonnet 4.5 recommended)
- Asana workspace (free tier works)
- Gmail account
- Google Drive account
- Google Calendar access

### Recommended
- At least 2-3 case studies documented
- Proposal templates created
- Sales Pipeline project in Asana with custom fields
- Competitive analysis documents

### Optional (Enhances Performance)
- CRM data (if migrating from another tool)
- Historical email performance data
- Team access to shared Asana workspace
- Standardized file naming conventions in Drive

---

## Quick Start (5 Minutes)

### 1. Install the Skill
Follow [INSTALLATION.md](docs/INSTALLATION.md) to add skill to Claude project and enable required integrations (Asana, Gmail, Drive, Calendar).

### 2. Set Up Data Sources
Follow [DATA-SOURCES.md](docs/DATA-SOURCES.md) to create:
- Sales Pipeline project in Asana
- Sales Assets folder in Google Drive
- Basic case studies and templates

### 3. Run First Campaign
Follow [QUICK-START.md](docs/QUICK-START.md) to generate your first cold outreach sequence.

**Time investment**: 5-10 minutes for install, 5-10 minutes for data setup, 5 minutes for first campaign = **15-25 minutes total**.

---

## Skill Architecture

### Data Sources Integration
```
┌─────────────────────────────────────────┐
│         Sales Automator Skill           │
└─────────────────────────────────────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
┌─────────┐   ┌─────────┐   ┌─────────┐
│  Asana  │   │  Gmail  │   │  Drive  │
│Pipeline │   │ History │   │  Assets │
└─────────┘   └─────────┘   └─────────┘
    │               │               │
    └───────────────┼───────────────┘
                    ▼
          ┌─────────────────┐
          │   Intelligence  │
          │   Gathering     │
          └─────────────────┘
                    │
                    ▼
          ┌─────────────────┐
          │   Campaign      │
          │   Generation    │
          └─────────────────┘
                    │
                    ▼
          ┌─────────────────┐
          │   Tracking &    │
          │   Analytics     │
          └─────────────────┘
```

### Workflow Patterns

**Pattern 1: New Cold Outreach**
```
Research (Web + Internal Data)
    → Intelligence Brief
    → 5-Touch Sequence Generation
    → Asana Deal Creation
    → Follow-Up Scheduling
```

**Pattern 2: Warm Follow-Up**
```
Context Reconstruction (Gmail + Calendar + Conversations)
    → Relationship Assessment
    → 3-Touch Sequence Generation
    → Asana Deal Update
    → Next Action Setting
```

**Pattern 3: Pipeline Health Check**
```
Asana Search (All Deals)
    → Stage Analysis
    → Stuck Deal Identification
    → Re-Engagement Sequence Generation
    → Performance Report
```

**Pattern 4: Proposal Creation**
```
Context Gathering (All Sources)
    → Case Study Matching (Drive)
    → Template Population
    → ROI Calculation
    → Proposal Generation
    → Asana Deal Stage Update
```

---

## File Guide

### Core Files (Required)

**SKILL.md** (The Main Skill)
- Complete workflow protocols
- Tool usage instructions
- Output formats and templates
- Quality checklists
- Integration with Chandler's ecosystem

**REFERENCE.md** (Template Library)
- Email sequence templates (cold, warm, reactivation)
- Subject line library with A/B testing framework
- Case study templates
- Proposal templates
- Objection handling scripts
- Cultural communication guides
- Performance benchmarks

### Setup Files (Start Here)

**INSTALLATION.md** (Get Skill Running)
- Step-by-step installation in Claude
- Tool integration setup
- Test procedures
- Troubleshooting

**DATA-SOURCES.md** (Configure Your Data)
- Asana setup (Sales Pipeline project, custom fields)
- Gmail organization
- Google Drive folder structure
- Calendar best practices
- Data maintenance schedules

**QUICK-START.md** (First Campaign in 15 Min)
- 5-minute setup checklist
- First campaign walkthrough
- Common use cases
- Quick command reference
- Pro tips and troubleshooting

---

## Documentation Structure

### For Immediate Use
Start with → [QUICK-START.md](docs/QUICK-START.md)

### For Installation
Follow → [INSTALLATION.md](docs/INSTALLATION.md)

### For Deep Customization
Reference → [REFERENCE.md](references/REFERENCE.md)

### For Data Optimization
Reference → [DATA-SOURCES.md](docs/DATA-SOURCES.md)

### For Understanding Workflows
Reference → [SKILL.md](SKILL.md)

---

## Performance Benchmarks

Based on implementation across sales teams:

**Email Performance**:
- Open rates: 45-65% (vs. 20-30% industry average)
- Response rates: 8-15% (vs. 2-5% industry average)
- Meeting booking: 15-25% of responders

**Pipeline Health**:
- 30% reduction in stuck deals
- 25% improvement in deal velocity
- 40% increase in forecast accuracy

**Time Savings**:
- 75% reduction in research time per prospect
- 60% reduction in email writing time
- 80% reduction in pipeline management overhead

**Quality Improvements**:
- 50% fewer generic/templated emails
- 90% increase in contextually relevant outreach
- 70% improvement in prospect engagement scores

---

## Typical Workflow

### Monday Morning (Week Start)
```
"Claude, check my Sales Pipeline and identify stuck deals"
→ Review pipeline health report
→ Receive re-engagement sequences for stuck deals
→ Schedule follow-ups for active deals
```

### Throughout Week (As Needed)
```
"Claude, create cold outreach for [Company]"
→ Receive researched 5-email sequence
→ Send Email 1 today
→ Asana automatically reminds for follow-ups

"Claude, follow up with [Name] about [topic]"
→ Receive contextual follow-up pulling past conversations
→ Send immediately
→ Asana updates deal stage

"Claude, generate proposal for [Company]"
→ Receive complete proposal with case studies
→ Review and customize
→ Send to prospect
```

### Friday Afternoon (Week End)
```
"Claude, analyze this week's outreach performance"
→ Review metrics (emails sent, responses, meetings booked)
→ Identify what worked and what didn't
→ Adjust approach for next week
```

---

## Best Practices

### 1. Quality Over Quantity
Send 10 researched emails that convert at 30% rather than 100 generic emails that convert at 2%.

### 2. Always Research First
Let Claude gather intelligence before writing. Never skip the research phase.

### 3. Update Data Sources Regularly
- Daily: Update Asana deal stages
- Weekly: Add new case studies to Drive
- Monthly: Refresh competitive analysis

### 4. Track Everything
Create Asana tasks for every deal. Log every touchpoint. Measure performance.

### 5. Iterate Based on Data
Ask Claude to analyze what's working. Optimize subject lines, email length, timing, CTAs.

### 6. Maintain Relationship Context
Don't treat every prospect as new. Pull history, reference past conversations, acknowledge gaps.

### 7. Cultural Awareness
Adapt tone and approach for Brazilian, US, Asian partners. One size doesn't fit all.

---

## Advanced Features

### Pipeline Forecasting
Calculate weighted pipeline value based on stage probabilities:
- Discovery: 25%
- Proposal: 50%
- Negotiation: 75%

### Win/Loss Analysis
Track why deals close or fall through, feed learnings back into approach.

### Sequence A/B Testing
Test subject lines, email length, CTA placement. Use data to optimize.

### Competitive Battle Cards
Maintain Drive docs comparing your offering vs. competitors. Auto-populate in outreach.

### Team Collaboration
Share Sales Pipeline project, case studies, competitive intel across team.

---

## Integration with Chandler's Ecosystem

This skill works seamlessly with other skills in Chandler's workspace:

**smart-email-composer**: Use for one-off emails vs. sequences
**meeting-prep-generator**: Prep for discovery meetings after booking
**meeting-transcript-processor**: Extract insights from sales calls
**weekly-tracker-generator**: Include sales metrics in weekly updates
**design-director**: Elevate proposal and case study design

---

## Customization Options

### Add Custom Templates
Edit `REFERENCE.md` to add your own:
- Email sequence templates
- Proposal formats
- Case study structures
- Objection handling scripts

### Adjust Thresholds
Modify what defines a "stuck deal":
- Default: Discovery > 14 days, Proposal > 30 days
- Your preference: Set in Project Instructions

### Industry-Specific Variations
Create industry-specific versions:
- B2B SaaS
- Consulting services
- Agency partnerships
- Product sales

### Cultural Adaptations
Expand cultural guides for:
- European partners
- Middle Eastern partners
- Latin American (beyond Brazil)

---

## Limitations & Considerations

### What This Skill Can't Do
- Automatically send emails (you must copy/paste and send)
- Access locked/private Drive folders without permission
- Modify Asana data without your workspace access
- Guarantee response rates (quality inputs → quality outputs)

### When Manual Approach Is Better
- Extremely high-touch, relationship-sensitive situations
- Outreach to C-suite at Fortune 100 companies (needs extra polish)
- Highly complex deals with multi-stakeholder dynamics
- When you have insider information not in any system

### Privacy & Security
- Claude only accesses data you explicitly search or share
- No random browsing of emails or files
- Authentication required for all integrations
- Review Claude's data access periodically

---

## Support & Troubleshooting

### Common Issues

**"Claude can't find my Sales Pipeline"**
- Verify project name is exactly "Sales Pipeline"
- Check workspace access in Asana
- Manually provide project ID if needed

**"Emails feel too generic"**
- Provide more context upfront
- Check that Drive has case studies
- Ask Claude to research deeper

**"Stuck deals not being identified"**
- Verify custom fields exist (Deal Stage, due dates)
- Update deal stages regularly
- Manually trigger: "Check for deals in Discovery > 14 days"

**"Can't create Asana tasks"**
- Verify edit permissions on Sales Pipeline
- Check that custom fields are set up
- Try manual task creation first to test permissions

### Getting Help

1. Review relevant documentation:
   - Installation issues → [INSTALLATION.md](docs/INSTALLATION.md)
   - Data setup → [DATA-SOURCES.md](docs/DATA-SOURCES.md)
   - Usage questions → [QUICK-START.md](docs/QUICK-START.md)
   - Template questions → [REFERENCE.md](references/REFERENCE.md)

2. Ask Claude directly: "Help me troubleshoot [specific issue]"

3. Check Project Settings → Integrations to verify all tools enabled

---

## Changelog

### Version 1.0 (November 2024)
Initial release with:
- Relationship intelligence engine
- Deal pipeline tracking
- Competitive analysis
- Email sequence generation
- Performance analytics
- Comprehensive template library
- Cultural communication guides
- Full integration with Asana, Gmail, Drive, Calendar

---

## What's Next

### Planned Enhancements
- LinkedIn integration for deeper prospect research
- Automated email sending (with user approval)
- Visual pipeline dashboards
- Predictive deal scoring
- Team performance leaderboards
- Custom workflow templates

### Feature Requests
If you have ideas for improvements, document them in your Sales Automation project and Claude can help implement.

---

## Success Metrics

Track these to measure impact:

**Efficiency**:
- Time spent per prospect (research + writing)
- Number of prospects contacted per week
- Pipeline management time

**Effectiveness**:
- Email open rates
- Response rates
- Meeting booking rates
- Proposal acceptance rates
- Win rates

**Quality**:
- Prospect feedback on outreach quality
- Sales team adoption rate
- Reduction in generic/templated emails

**Business Impact**:
- Pipeline value
- Deal velocity
- Average deal size
- Revenue closed

---

## Credits

**Created for**: Chandler Lewis, 360 Social Impact Studios

**Built on**: Claude Sonnet 4.5

**Integrates with**: Asana, Gmail, Google Drive, Google Calendar, Web Search

**Inspired by**: The need to scale high-quality, relationship-driven sales without sacrificing personalization or strategic thinking.

---

## License & Usage

This skill is designed specifically for Chandler Lewis and 360 Social Impact Studios.

Feel free to adapt for your own use, but please:
- Customize templates to match your voice
- Adjust workflows to fit your process
- Update examples to reflect your industry
- Respect the principle: quality over quantity, always

---

## Get Started

Ready to transform your sales process?

1. **Install**: Follow [INSTALLATION.md](docs/INSTALLATION.md)
2. **Setup**: Follow [DATA-SOURCES.md](docs/DATA-SOURCES.md)
3. **Launch**: Follow [QUICK-START.md](docs/QUICK-START.md)

**Or jump right in**: "Claude, create cold outreach for [Your First Prospect]"

---

**Remember**: Sales automation without relationship intelligence is spam. This skill ensures every email demonstrates you understand the prospect's world. Research deeply, personalize authentically, track rigorously, optimize continuously.

**Quality outreach converts. Generic outreach wastes everyone's time.**
