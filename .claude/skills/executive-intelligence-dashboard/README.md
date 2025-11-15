# Executive Intelligence Dashboard

**A production-grade system for generating weekly strategic intelligence briefs from operational data.**

## What This Skill Does

The Executive Intelligence Dashboard automatically synthesizes data from Asana, Gmail, and Google Drive into a sophisticated HTML briefing designed for board presentations, stakeholder communications, and executive decision-making. Instead of manually compiling status updates, you get a publication-quality intelligence brief that:

- **Elevates strategic signal above operational noise**: Automatically prioritizes partnership developments, team changes, and critical decisions over routine updates
- **Provides executive context**: Every significant development includes strategic implications, revenue impact, and decision requirements
- **Delivers visual intelligence**: Interactive Chart.js visualizations communicate team capacity, partnership portfolios, and service offerings at a glance
- **Maintains professional standards**: Enterprise-grade design with accessibility features, responsive layout, and print optimization suitable for board distribution

## Quick Start

**Basic Usage**:
```
Generate this week's 360 Impact Brief
```

**Custom Date Range**:
```
Generate an executive brief covering November 10-17, 2025
```

**Focused Brief**:
```
Generate a partnership-focused executive brief for the board meeting
```

**Emergency Brief** (when time-constrained):
```
Generate a condensed executive summary covering only critical developments this week
```

## What Gets Included

### Automatic Data Collection

The system queries:
- **Asana Workspace**: Projects, tasks completed this week, upcoming milestones, status updates, custom fields (priority, revenue impact, partnership type)
- **Gmail**: Partnership communications, client engagement, board correspondence, strategic discussions from the past 7-14 days
- **Google Drive**: Recent strategic documents, partnership proposals, board presentations, financial plans

### Content Sections

**Executive Summary**: Three high-level insights covering strategic inflection points, partnership momentum, and team evolution

**Partnerships & Business Development**:
- Lead story (most significant partnership development)
- Strategic partnership updates with context and revenue implications
- Active client engagements with deliverables and timelines
- Service development initiatives
- Assigned action items with owners and deadlines

**Operations & Team**:
- Team restructuring, hiring, or capacity changes
- Skills coverage and capability gaps
- Merger or acquisition integration
- Operational improvements
- Team-related action items

**Strategy & Governance**:
- Board meeting preparation and governance updates
- Strategic planning and roadmap development
- Financial position and sustainability pathway
- Decision frameworks for major choices
- Strategic action items

**Timeline**: Week-ahead view of critical meetings, deadlines, and milestones

### Visualizations

- **Service Package Analysis**: Horizontal bar chart showing market fit scores for different service offerings
- **Team Capacity Radar**: Six-dimension comparison of current vs. projected team capabilities
- **Custom Charts**: Additional visualizations based on available data (partnership portfolio, revenue distribution, etc.)

## Output Specifications

**Format**: Self-contained HTML file with embedded CSS and JavaScript

**File Size**: Typically 100-150KB (includes Chart.js and Font Awesome from CDN)

**Browser Compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge) with graceful degradation

**Print Optimization**: Professional print layout suitable for board distribution

**Accessibility**: WCAG AA compliant with skip links, semantic HTML, ARIA attributes, and keyboard navigation

**Responsive Design**: Adapts to desktop (1400px max-width), tablet (1024px), and mobile (640px) breakpoints

## Design System

The brief uses a refined professional design system:

**Color Palette**:
- Primary Blue: Executive summary and navigation
- Purple: Partnerships section
- Green: Operations section
- Amber: Strategy section
- Semantic colors for status badges (critical, warning, success, info)

**Typography**: Inter font family with systematic scale (14px body, 16px card titles, 24px section headers, 32px metrics)

**Spacing**: Consistent 8px-based scale for professional visual rhythm

**Components**: Reusable patterns for content cards, action items, metrics, charts, and timelines

## Best Practices

### For Best Results

**Be Specific About Context**: If preparing for a specific event (board meeting, investor call, strategy session), mention it. This helps prioritize relevant information.

**Provide Date Ranges When Helpful**: Default is the past week, but you can specify other ranges ("past two weeks," "month of November," etc.)

**Indicate Focus Areas**: If you want depth on specific partnerships or topics ("focus on CNEN and NanoBioPlus") rather than comprehensive coverage, say so.

**Review for Accuracy**: Always review the generated brief to ensure partnership status, team information, and financial details are current and accurate.

### Preparation Tips

**Before Requesting a Brief**:
- Ensure Asana projects and tasks are up to date
- Confirm recent partnership emails are in Gmail
- Upload any strategic documents to Google Drive
- Update project status in Asana if major milestones were reached

**Weekly Workflow**:
1. Thursday/Friday: Update Asana with week's accomplishments
2. Friday afternoon: Request the executive brief
3. Friday evening: Review and refine as needed
4. Sunday: Use for board meeting or weekly planning
5. Monday: Distribute to stakeholders as appropriate

## Customization Options

The skill can be adapted for:

**Different Time Horizons**: Weekly (standard), bi-weekly, monthly, or custom date ranges

**Focused Briefs**: Partnership-only, operations-only, or strategy-only views

**Event Preparation**: Board meetings, investor updates, quarterly reviews, strategic planning sessions

**Stakeholder-Specific**: Customized emphasis for different audiences (board vs. advisory committee vs. partnership review)

**Emergency Briefs**: Condensed versions highlighting only critical developments when time is limited

## Integration with Your Workflow

### Asana Best Practices

**Project Structure**:
- Tag strategic projects with custom fields (Partnership Type, Revenue Impact, Priority)
- Use project status updates to communicate major developments
- Assign clear owners to tasks representing action items
- Set realistic due dates for accurate timeline generation

**Task Management**:
- Mark tasks complete when achieved (drives "accomplishments" section)
- Use task comments for context that should appear in briefs
- Flag high-priority or blocked tasks appropriately
- Link related tasks to show dependencies

**Custom Fields to Leverage**:
- Priority (Critical, High, Medium, Low)
- Partnership Type (Strategic, Client, Development)
- Revenue Impact (Direct, Pipeline, None)
- Status (Active, On Hold, Completed)

### Email Organization

**Gmail Labels**: Consider labels for "Strategic," "Partnerships," "Board," or specific partner names to improve search precision

**Subject Line Clarity**: Use clear subject lines for important communications ("Partnership Proposal: CNEN Expansion" vs. "Quick Question")

**Thread Management**: Keep related communications in single threads for better context retrieval

### Document Management

**Google Drive Folders**: Organize by partnership, year, or document type (Proposals, Presentations, Contracts)

**Naming Conventions**: Use descriptive names with dates ("2025-11-15-Board-Presentation.pdf")

**Tags and Descriptions**: Add document descriptions to improve semantic search results

## Troubleshooting

**Brief Seems Incomplete**:
- Check that data sources are accessible (Asana workspace, Gmail, Google Drive)
- Verify date filters aren't too restrictive
- Ensure strategic information is captured in searchable locations

**Missing Partnership Information**:
- Check if partnership communications are in Gmail or Google Drive
- Update Asana project status if developments occurred
- Provide manual context in follow-up request

**Charts Not Displaying**:
- Refresh the browser (Chart.js loads from CDN)
- Check internet connection for external resources
- Try opening in a different browser

**Content Feels Too Generic**:
- Request more depth on specific areas
- Provide additional context about recent developments
- Ask for strategic analysis rather than just status reporting

## Advanced Usage

### Multi-Week Briefs

For board meetings or quarterly reviews:
```
Generate an executive brief covering the past month with focus on strategic milestones and major partnership developments
```

### Pre-Meeting Briefs

For specific events:
```
Generate a board meeting briefing covering merger status, team restructuring, and partnership portfolio for Sunday's meeting
```

### Comparative Analysis

For strategic planning:
```
Generate a brief comparing Q3 and Q4 partnership activity with team capacity analysis
```

## Support and Maintenance

### Skill Updates

The skill evolves based on:
- Changes in organizational structure or priorities
- New data sources or integration capabilities
- Design system refinements
- Stakeholder feedback on usefulness

### Quality Feedback

After each brief, consider noting:
- What information was most valuable
- What was missing or hard to find
- Whether prioritization felt accurate
- Visual or structural improvements needed

This feedback helps refine the skill over time.

## Technical Details

**Dependencies**:
- Chart.js 4.4.0 (loaded from CDN)
- Font Awesome 6.4.0 (loaded from CDN)
- Inter font from Google Fonts

**File Structure**:
- Single HTML file (self-contained)
- Embedded CSS in `<style>` block
- Embedded JavaScript for interactivity
- External resources loaded via CDN

**Performance**:
- Preconnect hints for CDN resources
- Deferred script loading
- Optimized CSS with minimal specificity
- Efficient DOM manipulation

**Accessibility**:
- Skip link to main content
- Semantic HTML5 structure
- ARIA labels and roles
- Keyboard navigation support
- WCAG AA color contrast

For detailed technical documentation, see IMPLEMENTATION-SUMMARY.md.

## Examples

See WORKFLOW-EXAMPLE.md for a complete walkthrough of generating an executive brief from start to finish, including sample queries, data collection strategy, and quality assurance steps.

## Questions?

**How long does it take?** Plan for 15-25 minutes for a complete brief with thorough data collection and analysis.

**Can I generate multiple versions?** Yes, request focused versions for different audiences or purposes.

**What if data is missing?** The brief will note information gaps and work with available data. You can provide additional context manually.

**How often should I generate briefs?** Weekly is standard, but adapt frequency to your board meeting schedule and stakeholder communication needs.

**Can I customize the design?** The design system is standardized for consistency, but content emphasis can be adjusted based on your needs.

## Related Resources

- **SKILL.md**: Complete technical specification for skill operation
- **QUICK-START.md**: Fast onboarding guide
- **IMPLEMENTATION-SUMMARY.md**: Technical architecture details
- **QUERY-GUIDE.md**: Data source query strategies
- **WORKFLOW-EXAMPLE.md**: Step-by-step example walkthrough
- **data-sources.json**: Configuration reference

---

**About This Skill**: Built for 360 Social Impact Studios to transform operational data into executive intelligence that enables strategic decision-making and stakeholder communication.
