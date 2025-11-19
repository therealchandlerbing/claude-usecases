# Writing Style Guide

Comprehensive guide for tone, voice, formatting, and critical writing rules for 360 newsletters.

## Core Principle: Grounded + Visionary

Balance realism with possibility. Write clearly and professionally while leaving room for aspiration. Inspire with vision but anchor in practical insight.

## Tone Guidelines

### Professional but Accessible

**Do:**
- Use clear, direct language
- Explain jargon when necessary
- Write for intelligent but busy readers
- Assume reader context about 360's work

**Don't:**
- Use overly academic language
- Include unnecessary jargon
- Write clickbait headlines
- Assume deep technical knowledge

### Examples

**Good:**
> "The partnership positions 360 to influence technology transfer across Latin America, building on our proven track record in systematic innovation assessment."

**Bad:**
> "This partnership will revolutionize everything and make us the global leaders in innovation!" (too promotional)

**Good:**
> "Three enterprise opportunities advanced to negotiation, validating our approach to cross-border market expansion."

**Bad:**
> "The strategic paradigm shift in our go-to-market framework leverages synergistic cross-pollination of innovation ecosystems." (too jargony)

## Critical Formatting Rules

### NEVER Use Em Dashes (—)

Em dashes cause formatting issues. Use alternatives:

**Instead of em dash, use comma:**
```
❌ The deal — structured as a three-year commitment — includes professional services.
✅ The deal, structured as a three-year commitment, includes professional services.
```

**Instead of em dash, use period:**
```
❌ The deal includes professional services — it's structured as a three-year commitment.
✅ The deal includes professional services. It's structured as a three-year commitment.
```

**Instead of em dash, use parentheses:**
```
❌ The deal — structured as a three-year commitment — launches in Q1.
✅ The deal (structured as a three-year commitment) launches in Q1.
```

### Inline Stat Formatting

Always wrap numbers and metrics in `<span class="inline-stat">`:

```html
The partnership represents <span class="inline-stat">$1.2M</span> in initial pipeline.

We served <span class="inline-stat">280 founders</span> across
<span class="inline-stat">16 countries</span> last year.

Adoption reached <span class="inline-stat">67%</span> within three months.
```

### Status Badge Usage

Apply badges judiciously to stories requiring attention:

**CRITICAL** (red):
```html
<span class="status-badge status-critical">Critical</span>
```
Use for: Urgent action needed, high-stakes decisions, time-sensitive issues

**ACTION REQUIRED** (yellow):
```html
<span class="status-badge status-action">Action Required</span>
```
Use for: Response needed within days, decisions required soon

**MONITORING** (gray):
```html
<span class="status-badge status-monitoring">Monitoring</span>
```
Use for: Watching situation, may need action later

## Purpose-Driven Lens

Apply appropriately based on content type.

### When to Apply

**Partnership strategy:**
- Consider power dynamics
- Highlight mutual benefit
- Show ecosystem impact
- Note relationship health

Example:
> "The partnership advances equitable access to innovation support across underserved communities in Brazil."

**Program design:**
- Consider access and inclusion
- Highlight systems change potential
- Show community outcomes
- Note sustainability

Example:
> "The assessment methodology centers community needs, ensuring technology solutions address real barriers to access."

**Organizational decisions:**
- Consider community outcomes
- Note long-term sustainability
- Show stakeholder impact
- Highlight mission alignment

Example:
> "The team expansion enables us to serve more social entrepreneurs while maintaining our commitment to deep, personalized support."

**Impact metrics:**
- Show human outcomes, not just numbers
- Provide context for metrics
- Note systems change indicators
- Highlight lived experience

Example:
> "67 community organizations now have tools to assess innovation opportunities, strengthening their capacity to drive local solutions."

### When NOT to Apply

Don't force purpose-driven framing for:
- Routine operational tasks
- Technical specifications
- Financial calculations
- General process updates
- Infrastructure improvements

## International Awareness

### Time Zones

Always specify when relevant:
- **PT** (Pacific Time) for Seattle activities
- **BRT** (Brasília Time) for Brazil activities
- Note time differences when scheduling across regions

Example:
> "The board meeting is scheduled for Sunday, 12pm PT (4pm BRT for Brazil participants)."

### Cultural Considerations

**Brazil and Latin America:**
- Acknowledge relationship-building pace (often slower, more deliberate)
- Note formality preferences (more formal initially)
- Recognize different business practices
- Respect cultural communication styles

Example:
> "Partnership discussions with CNEN reflect Brazilian business culture's emphasis on relationship development before formal agreements."

**International partnerships generally:**
- Don't assume US-centric norms
- Acknowledge different decision-making processes
- Note language considerations when relevant
- Respect cultural approaches to partnership

### Language Context

Note when Portuguese is preferred or relevant:
> "All materials for the São Paulo workshop will be provided in Portuguese, recognizing the importance of mother-tongue learning for innovation methodology."

## Writing Structure

### For Each Story

#### 1. Headline (22px, 1-2 lines max)

**Characteristics:**
- Active voice
- Specific and concrete
- Newsworthy angle
- No clickbait or hype

**Good examples:**
- "SpacePlan Joint Venture Launches with $1.2M Initial Pipeline"
- "GenIP Integration Completes, Enabling 3-Week Technology Assessments"
- "Brazil Market Research Identifies Seven Priority Sectors"

**Bad examples:**
- "Amazing Partnership News!" (too vague, clickbait)
- "You Won't Believe What Happened with SpacePlan" (clickbait)
- "Partnership" (too short, not informative)

#### 2. Opening Paragraph

**Include:**
- Key facts (who, what, when, where, why)
- Context for understanding
- Inline metrics as `<span class="inline-stat">`
- Why this matters

**Structure:**
```
[MAIN DEVELOPMENT] combined with [CONTEXT] represents
[SIGNIFICANCE]. [KEY METRIC] demonstrates [IMPACT].
```

**Example:**
> "The SpacePlan joint venture formalized this week with signed MOU represents a strategic pivot toward consulting revenue. Initial pipeline of <span class="inline-stat">$1.2M</span> across <span class="inline-stat">12 prospective clients</span> validates the architectural innovation market opportunity."

#### 3. Development Paragraphs

**Include:**
- Evidence and supporting details
- Relevant data and metrics
- Stakeholder perspectives (when available)
- Strategic implications
- Connection to broader goals

**Keep paragraphs:**
- 2-4 sentences each
- Focused on single sub-topic
- Easy to scan
- Dense but readable

#### 4. Closing Insight

**Provide:**
- What this means going forward
- Connection to broader strategy
- Action items if applicable
- Next steps or milestones

**Example:**
> "The partnership positions 360 to scale technology transfer support across the Pacific Northwest, with initial focus on clean energy and aerospace innovations. First client engagement targets December launch."

#### 5. Desk Attribution + Read Time

```html
<div class="story-meta">
  Partnership desk • 3 min read
</div>
```

**Desk assignments:**
- **Innovation desk**: Programs, R&D, technology transfer, methodology
- **Partnership desk**: Business development, strategic alliances, ecosystem
- **Impact desk**: Community outcomes, social metrics, systems change
- **Operations desk**: Team, infrastructure, finance, capacity

## Voice Characteristics

### Active and Direct

**Do:**
```
✅ The team completed three assessments in two weeks.
✅ Partnership negotiations advanced to final terms.
✅ Board approved the merger structure.
```

**Don't:**
```
❌ Three assessments were completed by the team.
❌ Final terms are being negotiated.
❌ The merger structure was approved.
```

### Specific and Concrete

**Do:**
```
✅ Revenue increased 34% to $89K in Q3.
✅ The partnership includes 12 universities across Brazil.
✅ GenIP integration reduces assessment time from 6 weeks to 3 weeks.
```

**Don't:**
```
❌ Revenue increased significantly.
❌ The partnership includes many universities.
❌ GenIP integration makes things faster.
```

### Confident but Not Arrogant

**Do:**
```
✅ Our methodology enables rapid, rigorous technology assessment.
✅ We've successfully supported 280 founders across 16 countries.
✅ The partnership validates our approach to cross-border innovation.
```

**Don't:**
```
❌ We're the best in the world at technology assessment.
❌ No one else can do what we do.
❌ This proves we're better than everyone.
```

## Action-Oriented Language

### Flag Items Requiring Decisions

**Structure:**
```html
<div class="action-item">
  <div class="action-title">[SPECIFIC ACTION NEEDED]</div>
  <div class="action-detail">[CONTEXT AND DETAILS]</div>
  <div class="action-meta">
    <span><i class="fas fa-user"></i> [RESPONSIBLE]</span>
    <span><i class="fas fa-calendar"></i> Due [DATE]</span>
    <span><i class="fas fa-[icon]"></i> [STATUS]</span>
  </div>
</div>
```

**Be specific:**
```
✅ Finalize service package pricing model by Nov 20
✅ Schedule strategic planning session before Nov 17
✅ Consult with Walter on team transition by Nov 20
```

Not vague:
```
❌ Work on pricing
❌ Plan a meeting
❌ Talk to Walter
```

### Specify Next Steps

When known, always include:
- What happens next
- Who's responsible
- When it's due
- What success looks like

### Note Blockers and Dependencies

**Be clear about obstacles:**
```
✅ Limus case study blocked pending content approval from Evan.
   Critical path item for portfolio completion.

✅ Partnership advancement depends on board approval at Sunday meeting.
   Decision required before Q1 planning.
```

### Indicate Urgency Appropriately

**Use status indicators:**
- Critical: Immediate action required
- Urgent: Action needed this week
- Important: Action needed this month
- Routine: Standard timeline

## Common Patterns

### Partnership Announcements

```
[PARTNER NAME] [ACTION: signed/launched/formalized] [TYPE: agreement/MOU/partnership]
this [TIMEFRAME], [ESTABLISHING/CREATING/ENABLING] [OUTCOME]. [KEY TERMS/STRUCTURE]
positions 360 to [STRATEGIC BENEFIT]. Initial [METRIC: pipeline/clients/projects]
of [NUMBER] [DEMONSTRATES/VALIDATES] [MARKET/OPPORTUNITY].
```

### Project Completions

```
[PROJECT/DELIVERABLE] completed [TIMEFRAME] for [CLIENT], [DEMONSTRATING/SHOWING]
[CAPABILITY/OUTCOME]. [METHOD/APPROACH] enabled [SPEED/QUALITY/RESULT].
[CLIENT IMPACT: specific outcome for client]. [STRATEGIC IMPLICATION: what this
means for 360].
```

### Team Updates

```
[PERSON NAME] [ACTION: joins/transitions/departs] [TIMEFRAME],
[BRINGING/LEAVING] [EXPERTISE/CAPABILITY]. [BACKGROUND: relevant experience].
[ROLE: what they'll do]. [IMPACT: how this strengthens/affects team].
```

### Impact Metrics

```
[NUMBER] [BENEFICIARIES: people/organizations/communities] [OUTCOME: gained access/
improved capacity/achieved result] through [PROGRAM/PARTNERSHIP]. [SPECIFIC EXAMPLE:
story or quote]. [SYSTEMS CHANGE INDICATOR: broader implication].
```

## Quality Checks Before Publishing

### Content Quality

- [ ] No em dashes anywhere in text
- [ ] All metrics wrapped in `<span class="inline-stat">`
- [ ] Status badges applied appropriately
- [ ] Active voice throughout
- [ ] Specific, concrete details
- [ ] Purpose-driven lens applied where relevant
- [ ] International awareness shown where relevant

### Tone Quality

- [ ] Professional but accessible
- [ ] Confident but not arrogant
- [ ] Grounded in reality
- [ ] Visionary where appropriate
- [ ] Action-oriented
- [ ] Clear and direct

### Structural Quality

- [ ] Headlines are newsworthy
- [ ] Opening paragraphs have key facts
- [ ] Development paragraphs are focused
- [ ] Closing insights connect to strategy
- [ ] Desk attribution appropriate
- [ ] Read time estimated (if applicable)

## Examples by Section

### Executive Summary Card

```html
<div class="summary-card">
  <div class="summary-card-title">SpacePlan Joint Venture</div>
  <div class="summary-card-content">
    LOI signed Nov 13 with 5% royalty structure funding nonprofit work.
    Critical given <span class="inline-stat">$100K</span> federal funding
    loss. Strategic pivot from grants to consulting revenue model.
  </div>
</div>
```

### Partnership Insight

```html
<div class="card">
  <div class="card-header">
    <div class="card-title">
      <span class="card-title-bold">ScienceLink Brazil</span>
      delivers $15K qualified pipeline
    </div>
    <span class="status-chip status-action">
      <i class="fas fa-clock"></i> Decision Pending
    </span>
  </div>
  <p class="card-context">
    Two distinct opportunities emerged this week, one focused on
    innovation audit methodology, the other spanning eight project
    demands across chemical analysis and hardware development.
  </p>
  <ul class="card-bullets">
    <li><strong>EcoBriza engagement:</strong> Project structuring using
        11-question Innovation Intelligence Audit. Client completed
        pre-meeting discovery, strong qualification signals.</li>
  </ul>
</div>
```

### Action Item

```html
<div class="action-item">
  <div class="action-title">
    Finalize service package pricing model
  </div>
  <div class="action-detail">
    Three-tier model with clear deliverables, customizable by client
    type (universities, CVCs, incubators, corporate). Enable flexible
    positioning.
  </div>
  <div class="action-meta">
    <span><i class="fas fa-user"></i> Chandler & Walter</span>
    <span><i class="fas fa-calendar"></i> Due Nov 20</span>
    <span><i class="fas fa-spinner"></i> In Progress</span>
  </div>
</div>
```

---

**Next:** See [Chart Specifications](chart-specifications.md) for visual design guidelines.
