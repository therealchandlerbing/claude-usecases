# Intelligence Extractor

**Category:** Data Intelligence & Quality Monitoring
**Purpose:** Extract structured partnership, funding, and stakeholder intelligence from meeting transcripts, emails, and conversations with built-in quality tracking and real-time dashboard.

## Overview

The Intelligence Extractor is a comprehensive system for capturing, structuring, and monitoring intelligence from various types of organizational interactions. It combines:

1. **10 Meeting-Type Specific Prompt Templates** - Optimized extraction prompts for different contexts
2. **Live Quality Dashboard** - Real-time web dashboard for monitoring extraction quality
3. **Automated Quality Tracking** - Confidence scoring, completeness analysis, and improvement feedback loops

## Key Features

### Template-Based Extraction
- **10 specialized templates** for different meeting types
- Context-specific extraction priorities
- Cultural intelligence capture
- Pattern recognition guides
- Confidence calibration

### Quality Monitoring
- Real-time metrics dashboard
- Completeness scoring
- Template performance tracking
- Automated quality analysis
- Continuous improvement feedback

### Data Pipeline
- Zapier integration for automation
- Supabase (PostgreSQL) for data storage
- Real-time updates via subscriptions
- Asana integration for intelligence tasks

### Cross-Linking Architecture
- **Three-System Integration** - Partnership, Funding, and Stakeholder Intelligence work together as an interconnected ecosystem
- **Task Relationships** - Explicit links between related intelligence items in Asana
- **Shared Custom Fields** - Consistent fields across all systems for portfolio views
- **Information Flow Patterns** - Structured workflows for discovery cascades and updates
- **Dashboard Views** - Cross-system intelligence queries and portfolio management

See [Cross-Linking Architecture](references/cross-linking-architecture.md) for complete implementation guide.

## Quick Start

### 1. Choose the Right Template

See [Template Selection Guide](templates/00-template-selection-guide.md) for quick reference:

- New partnership meeting → Template 1
- Existing partnership check-in → Template 2
- Funder initial contact → Template 3
- Grant application discussion → Template 4
- Board/governance meeting → Template 5
- Client sprint/planning → Template 6
- Community stakeholder meeting → Template 7
- International partner meeting → Template 8
- Conference/networking → Template 9
- Crisis/problem-solving → Template 10

### 2. Extract Intelligence

1. Get meeting transcript (from Fathom, Zoom, etc.)
2. Select appropriate template from `templates/`
3. Fill in meeting context
4. Paste transcript
5. Send to Claude
6. Receive structured JSON output

### 3. Monitor Quality

Access the [live dashboard](../../intelligence-dashboard/README.md) to:
- Track extraction quality metrics
- Monitor template performance
- Review flagged items
- Analyze trends over time

## Directory Structure

```
intelligence-extractor/
├── README.md                          # This file
├── INDEX.md                           # Complete file index
├── templates/
│   ├── 00-template-selection-guide.md # Quick reference for choosing templates
│   ├── 01-partnership-new.md          # New partnership exploration
│   ├── 02-partnership-existing.md     # Existing partnership check-in
│   ├── 03-funder-initial.md           # Funder initial contact
│   ├── 04-funder-application.md       # Grant application discussion
│   ├── 05-board-governance.md         # Board/governance meetings
│   ├── 06-client-sprint.md            # Client engagement sessions
│   ├── 07-community-stakeholder.md    # Community meetings
│   ├── 08-international-partner.md    # Cross-cultural meetings
│   ├── 09-conference-networking.md    # Brief networking interactions
│   └── 10-crisis-problem-solving.md   # Crisis/conflict meetings
├── references/
│   ├── intelligence-schemas.md        # JSON schemas for outputs
│   ├── cross-linking-architecture.md  # How the three systems interconnect
│   ├── quality-framework.md           # Quality assessment framework
│   └── cultural-intelligence.md       # Cross-cultural guidance
└── examples/
    ├── partnership-extraction-example.md
    ├── funder-extraction-example.md
    └── stakeholder-extraction-example.md
```

## Templates Overview

### Template 1: New Partnership Exploration
**When to Use:** First or second meeting with potential partner organization

**Extraction Priorities:**
- Organization intelligence (problems, urgency, past attempts)
- Cultural & communication patterns
- Fit assessment signals
- Decision process intelligence
- Next steps clarity

**Output:** Partnership Intelligence + Stakeholder Intelligence for each participant

---

### Template 2: Existing Partnership Check-in
**When to Use:** Follow-up meetings with established partners

**Extraction Priorities:**
- Relationship evolution signals
- Operational intelligence (what's working/not working)
- Strategic opportunities
- Changes since last meeting
- Stakeholder updates

**Output:** Partnership Intelligence (update) + Stakeholder updates

---

### Template 3: Funder Initial Contact
**When to Use:** First conversation with potential funding source

**Extraction Priorities:**
- Program fit assessment
- Decision process intelligence
- What they really care about
- Relationship & political intelligence
- Application strategy intelligence

**Output:** Funding Intelligence + Program Officer stakeholder profile

---

### Template 4: Grant Application Discussion
**When to Use:** LOI feedback, proposal development, clarification meetings

**Extraction Priorities:**
- Application intelligence (feedback, guidance)
- Decision process updates
- Budget & scope intelligence
- Strategic positioning updates
- Relationship development

**Output:** Funding Intelligence (update) + Success likelihood assessment

---

### Template 5: Board or Governance Meeting
**When to Use:** Board meetings, advisory board meetings, governance discussions

**Extraction Priorities:**
- Individual board member profiles
- Board dynamics intelligence
- Strategic priority signals
- Decision process observations
- Governance effectiveness

**Output:** Stakeholder Intelligence for EACH board member + Board dynamics

---

### Template 6: Client Sprint or Planning Session
**When to Use:** Working sessions with clients, strategic planning, project kickoffs

**Extraction Priorities:**
- Client organization intelligence
- Stakeholder deep dive (working styles, decision-making)
- Engagement intelligence
- Outcomes & impact focus
- Sustainability & capacity

**Output:** Partnership Intelligence (update) + Detailed stakeholder profiles

---

### Template 7: Community Stakeholder Meeting
**When to Use:** Meetings with grassroots leaders, community organizations

**Extraction Priorities:**
- Community context intelligence
- Power & trust dynamics
- Stakeholder profiles (legitimacy, authority)
- Cultural intelligence
- Partnership viability assessment

**Output:** Stakeholder Intelligence + Community context patterns

---

### Template 8: International Partner Meeting
**When to Use:** Cross-cultural contexts (Brazil, Latin America, Europe, Asia-Pacific)

**Extraction Priorities:**
- Cultural communication intelligence
- Cross-cultural partnership dynamics
- Organizational context (local)
- Strategic alignment & differences
- Partnership logistics intelligence

**Output:** Partnership Intelligence (with cultural lens) + Cultural stakeholder profiles

---

### Template 9: Conference or Networking Event
**When to Use:** Brief conversations at conferences, convenings, networking events

**Extraction Priorities:**
- Initial impression intelligence
- Work & context intelligence
- Alignment assessment
- Networking intelligence
- Follow-up strategy

**Output:** Lightweight stakeholder profile + Follow-up plan

---

### Template 10: Crisis or Problem-Solving Meeting
**When to Use:** Emergency meetings, conflict resolution, partnership problems

**Extraction Priorities:**
- Crisis intelligence (root cause vs. symptoms)
- Relationship stress dynamics
- Capacity under pressure
- Values under pressure
- Relationship viability assessment

**Output:** Partnership/Stakeholder updates + Crisis assessment

---

## Intelligence Types

The system extracts three types of intelligence:

### 1. Partnership Intelligence
Information about organizations you partner with:
- Relationship status and temperature
- Strategic opportunities
- Decision-making processes
- Cultural approaches
- Opening opportunities

### 2. Funding Intelligence
Information about funding sources:
- Program fit and requirements
- Decision processes and timelines
- Success factors and red flags
- Positioning strategies
- Budget considerations

### 3. Stakeholder Intelligence
Information about individual people:
- Communication styles
- Decision-making approaches
- What they care about
- Power and influence
- Relationship dynamics

### How They Work Together

**Stakeholders are the connective tissue.** Every partnership and funding opportunity involves specific people. Understanding those people (Stakeholder Intelligence) makes you more effective at both partnership development and fundraising.

The three intelligence systems work together as an interconnected ecosystem:
- **Stakeholder Intelligence (WHO layer)** informs both Partnership and Funding Intelligence
- **Partnership Intelligence (HOW layer)** and **Funding Intelligence (RESOURCES layer)** inform each other
- Cross-linking enables portfolio views, relationship health monitoring, and strategic opportunity spotting

For complete implementation details, see [Cross-Linking Architecture](references/cross-linking-architecture.md).

## Quality Framework

The system includes built-in quality monitoring:

### Completeness Scoring
- **Required fields**: 70% weight
- **Optional fields**: 30% weight
- Target: >75% overall completeness

### Confidence Calibration
- **High confidence**: >85% completeness, clear signals
- **Medium confidence**: 60-85% completeness, some ambiguity
- **Low confidence**: <60% completeness, unclear signals

### Automated Flags
System automatically flags extractions for review when:
- Confidence/completeness mismatch detected
- Critical fields missing
- Parsing errors occur
- Multiple warnings present

See [Quality Framework](references/quality-framework.md) for details.

## Live Dashboard

The system includes a professional web dashboard for real-time monitoring:

### Dashboard Features
- **Metrics Cards**: Total extractions, avg completeness, ratings, flags
- **Quality Trends**: 30-day visualization
- **Template Performance**: Compare all templates
- **Recent Activity**: Live extraction feed

### Technology Stack
- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS
- **Backend**: Supabase (PostgreSQL with real-time)
- **Hosting**: Vercel (auto-deploy from GitHub)
- **Cost**: Free tier available

### Quick Links
- [Dashboard Documentation](../../intelligence-dashboard/README.md)
- [Deployment Guide](../../intelligence-dashboard/DEPLOYMENT_GUIDE.md)
- [Live Dashboard Summary](../../INTELLIGENCE_DASHBOARD_SUMMARY.md)

## Integration Workflow

```
Meeting Transcript (Fathom/Zoom)
         ↓
   Google Drive
         ↓
      Zapier ───────→ Claude API (with template)
         ↓                       ↓
   Supabase ←──── JSON Output ──┘
         ↓
   Dashboard (real-time update)
         ↓
   Asana Tasks (intelligence items)
```

## Usage Examples

### Example 1: New Partnership Meeting

```markdown
Meeting with InovaEduK (Brazilian EdTech)
- Used Template 1 (Partnership New)
- Extracted: 1 Partnership Intelligence, 3 Stakeholder profiles
- Completeness: 82%
- Confidence: High
- Key insights: Strong values alignment, decision involves 2 more people
```

### Example 2: Funder Call

```markdown
Call with Imaginable Futures
- Used Template 3 (Funder Initial)
- Extracted: 1 Funding Intelligence, 1 Program Officer profile
- Completeness: 76%
- Confidence: Medium
- Key insights: Strong fit for education innovation, competitive process
```

See [examples/](examples/) for complete extraction examples.

## Best Practices

### Template Selection
1. **Match meeting type precisely** - Each template optimized for specific contexts
2. **When in doubt, use Template 1** - Most general, works for initial meetings
3. **Combine templates if needed** - E.g., Board Meeting + Crisis for emergency board session

### Context Provision
1. **Always fill in meeting context** - Helps Claude calibrate extraction
2. **Specify cultural context** - Especially for international meetings
3. **Note previous interactions** - Helps with relationship evolution tracking

### Quality Review
1. **Review flagged extractions** - System flags potential issues
2. **Rate extraction quality** - Helps improve template performance
3. **Provide feedback** - System learns from corrections

## Advanced Features

### A/B Template Testing
- Run experiments on template variations
- Track performance metrics
- Deploy winning versions
- See dashboard for experiment tracking

### Automated Analysis
- Weekly quality summaries
- Template performance reports
- Improvement recommendations
- Trend analysis

### Cultural Intelligence
- Cross-cultural communication patterns
- Power dynamics awareness
- Relationship-building pace tracking
- Language and formality indicators

See [Cultural Intelligence Guide](references/cultural-intelligence.md)

## Troubleshooting

### Low Completeness Scores
- Check if transcript is complete
- Verify template matches meeting type
- Ensure context section is filled out
- Review if meeting covered expected topics

### Confidence Mismatches
- High confidence + low completeness = Template may be over-confident
- Low confidence + high completeness = Template may be too conservative
- Flag for template improvement

### Missing Intelligence
- Check template extraction priorities
- Verify transcript quality
- Consider if meeting actually covered the topic
- May need different template

## Contributing

### Improving Templates
1. Review extraction quality metrics
2. Identify patterns in low-performing extractions
3. Propose template modifications
4. A/B test changes
5. Deploy improvements

### Adding New Templates
1. Identify unmet meeting type
2. Draft template based on standard structure
3. Test on sample transcripts
4. Track performance metrics
5. Iterate based on quality data

## Support

- **Dashboard Issues**: See `intelligence-dashboard/README.md`
- **Template Questions**: Review template-specific guidance
- **Integration Help**: Check Zapier integration code
- **Quality Concerns**: See Quality Framework reference

## Version History

- **v1.1** (2025-11-15) - Cross-Linking Architecture Integration
  - Comprehensive cross-linking architecture documentation
  - Intelligence schemas for all three intelligence types
  - Integration patterns and workflow examples
  - Dashboard views for cross-system intelligence
  - Implementation roadmap and success metrics

- **v1.0** (2025-01-15) - Initial release with 10 templates and live dashboard
  - 10 meeting-type specific templates
  - Real-time quality dashboard
  - Supabase + Vercel deployment
  - Automated quality tracking

## License

[Add license information]

---

**Quick Links:**
- [Template Selection Guide](templates/00-template-selection-guide.md) ← Start here
- [Complete File Index](INDEX.md)
- [Live Dashboard](../../intelligence-dashboard/README.md)
- [Deployment Guide](../../intelligence-dashboard/DEPLOYMENT_GUIDE.md)
- [Cross-Linking Architecture](references/cross-linking-architecture.md) ⭐ NEW
- [Intelligence Schemas](references/intelligence-schemas.md) ⭐ NEW
- [Quality Framework](references/quality-framework.md)
