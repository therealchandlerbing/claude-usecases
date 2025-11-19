# 360 Impact Brief - Weekly Production Skill File

## Purpose
This skill file defines how to produce the 360 Impact Brief dashboard every week with:
- Consistent structure and design
- Minimal copy-paste risk
- Clear mapping from content to the HTML artifact

Use this with the companion file `360-impact-brief-weekly-template.md`, which you fill in with the current week's content.

## Roles
- **Content Owner**: Chandler (or delegate). Sets narrative, priorities, and data.
- **Producer**: EA or ops person. Updates weekly Markdown, then updates HTML.
- **Reviewer**: Chandler. Final sign-off before sharing.

## Weekly Workflow

### 1. Clone last week
- Copy last week's `360-impact-brief-weekly-template.md`.
- Rename to `360-impact-brief-YYYY-MM-DD.md` (use Monday of the week).

### 2. Fill the template
Work only in the Markdown template. Update:
- Week metadata
- Snapshot cards
- Anchor cards
- Metrics
- Charts data (percentages or scores)
- Timeline events

### 3. Review the story
Check against governance rules:
- Snapshot cards: max 2 sentences each.
- Anchor cards: max 3 bullets.
- No paragraph longer than 3 lines on desktop.
- Each story lives in one section. Reference, do not repeat.

### 4. Update the HTML dashboard
Use the Markdown template as the single source of truth. Update the HTML in these areas:
- Executive Snapshot section
- Partnerships section (cards + chart data)
- Operations section (cards, metrics, chart, action items)
- Strategy & Finance section (cards, metrics, chart)
- Timeline JavaScript configuration

### 5. Run quality checks
- Visual scan on desktop and mobile.
- Click through nav links.
- Collapse and expand sections.
- Toggle timeline views.
- Confirm chart labels and values match the Markdown.

### 6. Archive
Save:
- Weekly Markdown file
- Final HTML (or link to it)
- Optional: note key decisions for traceability.

## Content Governance Rules (Enforced Weekly)
Use these as hard constraints, not suggestions.

### Layout and story

#### Executive Snapshot
Exactly 4 cards:
1. People
2. Revenue
3. Partnerships
4. Risk

Each card:
- 1 short label (1 to 2 words)
- 1 value line (headline)
- 1 detail line (max 2 sentences)

#### Anchor cards ("This Week in ...")
- 3 bullets maximum.
- Each bullet:
  - Start with a strong label in bold.
  - 1 sentence, at most 2 short clauses.

#### Supporting cards
- Max 3 per section.
- Max 5 bullets or sentences per card.
- Use short, declarative sentences.

#### Charts
- Do not change chart types or order without an intentional design decision.
- Only update labels and data values.

#### Timeline
Every item has:
- A date label
- One or more event lines
- Optional priority tag (critical, high, or empty)

### Voice and tone
Lead with impact, then detail. Example:
> "Runway solid through Q2. Hiring increases burn but unlocks capacity for 2 to 3 additional client projects."

Avoid:
- Jargon that adds no clarity.
- Overlapping stories across sections.

## Mapping: Template Fields to HTML

Use this map when you transfer content from the filled Markdown into the HTML.

### 1. Global week metadata

**Template fields:**
- `week_of_label`
- `week_range_label` (optional, mostly for internal reference)

**HTML:**
- Sidebar: `#current-week` text
  - Updated automatically to "Week of {Today}" by JavaScript.
  - If you need a specific week instead of "today", override the `updateCurrentWeek` function or hardcode the text.
- Main hero title in Executive Snapshot:
  ```html
  <h1 class="snapshot-title">Week of November 15, 2025</h1>
  ```
  Replace with the new week label, e.g. `Week of March 3, 2026`.

### 2. Executive Snapshot

**Template section:**
```
## Executive Snapshot
Snapshot cards:
- People
- Revenue
- Partnerships
- Risk

Key insights:
- Decisions
- Risks
- Metrics
```

**HTML locations:**
- Four `.snapshot-card` blocks:
  - `snapshot-card-label` → label (People, Revenue, etc.)
  - `snapshot-card-value` → headline value
  - `snapshot-card-detail` → 1 to 2 sentences from template.

- Key insights:
  - Three `.insight-item` blocks:
    - `.insight-label` → "Decisions", "Risks", "Metrics"
    - `.insight-value` → short line from template.

### 3. Partnerships section

**Template section:**
```
## Partnerships
This Week in Partnerships bullets (3)
Cards:
- Card 1: CVC offering
- Card 2: TTO offering
- Card 3: Full-service offering

Chart: Service Package Market Fit
- Labels and values
```

**HTML locations:**
- Anchor card:
  ```html
  <h3 class="anchor-title">This Week in Partnerships</h3>
  <ul class="anchor-bullets"> → 3 <li> elements.
  ```

- Info cards:
  - Each `.info-card`:
    - `.card-title` → card title.
    - `.card-badge` class and text → "Hot", "Warm", "High Value".
    - `.card-content` → description paragraph.
    - `.card-meta span` items → price range, number of conversations, timing, etc.

- Chart data (Service Package Market Fit):
  - In `initializeCharts()` for `serviceChart`:
    ```javascript
    labels: [
      'Venture IQ\n(CVC)',
      'Intelligence Audit\n(TTO)',
      'Innovation Compass\n(Full Service)'
    ],
    data: [85, 60, 100],
    ```
    - Update label text as needed.
    - Update data array to your new market fit scores (0 to 100).

- Chart insight:
  - `.chart-insight` text for Partnerships chart. Keep as 1 to 2 sentences.

### 4. Operations section

**Template section:**
```
## Operations
This Week in Operations bullets (3)
Metrics:
- Current Team Capacity
- Post-Hire Capacity
- Monthly Investment
- ROI Timeline

Chart: Team Capability Analysis
Action items:
- 2 to 3 items with priority, owner, due date.
```

**HTML locations:**
- Anchor card:
  ```html
  <h3 class="anchor-title">This Week in Operations</h3>
  <ul class="anchor-bullets"> → 3 bullets.
  ```

- Metrics:
  - Four `.metric-card` elements in Operations:
    - `.metric-label` → label
    - `.metric-value` → main number or text
    - `.metric-detail` → subtext
    - `.metric-trend` → choose `trend-up`, `trend-down`, or `trend-neutral` and adjust text.

- Chart data (Team Capability Analysis):
  - In `initializeCharts()` for `capacityChart`:
    ```javascript
    labels: ['Corp BD', 'AI/Tech', 'Multilingual', 'Strategic', 'Financial', 'Agritech'],
    datasets: [
      {
        label: 'Current Team',
        data: [50, 75, 60, 70, 50, 30],
      },
      {
        label: 'With Nadia & Leo',
        data: [90, 85, 95, 90, 90, 85],
      }
    ]
    ```
    Update:
    - `labels` if competencies change.
    - `data` arrays with values 0 to 100.

- Action items:
  - Each `.action-item` block:
    - Add `priority-critical` or `priority-high` class as needed.
    - `.action-title` → title from template.
    - `.action-detail` → single paragraph description.
    - `.action-meta` spans:
      - Owner
      - Due date
      - Priority label.

### 5. Strategy & Finance section

**Template section:**
```
## Strategy & Finance
This Week in Strategy bullets (3)
Metrics:
- Year-End Projection
- Active Pipeline
- Recent Contract
- Monthly Burn

Chart: Revenue Distribution
Info cards:
- Integration work
- Q targets and objectives
```

**HTML locations:**
- Anchor card:
  ```html
  <h3 class="anchor-title">This Week in Strategy</h3>
  <ul class="anchor-bullets"> → 3 bullets.
  ```

- Metrics:
  - Four `.metric-card` elements in Strategy section:
    - Same pattern as Operations metrics.

- Chart data (Revenue Distribution):
  - In `initializeCharts()` for `revenueChart`:
    ```javascript
    labels: ['Venture IQ', 'Intelligence Audit', 'Innovation Compass', 'Consulting'],
    datasets: [{
      data: [35, 25, 30, 10],
    }]
    ```
    Update:
    - Label list to reflect your offerings.
    - Data array to reflect percent distribution. These do not have to sum to 100 exactly, but they should be close.

- Chart insight:
  - `.chart-insight` under Revenue chart.

- Info cards:
  - Two `.info-card` blocks:
    - Card 1: integration / structural changes.
    - Card 2: forward objectives and targets.

### 6. Timeline

**Template section:**
```
## Timeline
Views:
- view: week
- view: twoweeks

For each view, list:
- Date label
- Events with text and priority
```

**HTML locations:**
- JavaScript `timelineConfig` object:
  ```javascript
  const timelineConfig = {
    week: {
      label: 'Week Ahead: Nov 15-22',
      data: [ ...day blocks... ]
    },
    twoweeks: {
      label: 'Next Two Weeks: Nov 17-30',
      data: [ ...day blocks... ]
    }
  };
  ```

## Best Practices

### Writing for Executives

**DO:**
- Lead with impact and decisions
- Use active voice ("Hired Nadia" not "Nadia was hired")
- Quantify when possible ("$26K contract" not "major contract")
- Connect dots ("Hiring enables pipeline conversion")
- Flag risks early and clearly

**DON'T:**
- Bury the lede with context
- Use passive voice or vague language
- Present data without interpretation
- Assume prior knowledge of details
- Hide bad news in positive framing

### Data Visualization

**Chart Selection:**
- Doughnut/Pie: Composition, market share, distribution
- Radar: Multi-dimensional comparison (team capacity)
- Bar: Ranking, comparison, market fit scoring
- Line: Trends over time, projections
- Stacked Bar: Part-to-whole over categories

**Chart Insights:** Always include insight boxes that:
- Interpret the data (what does it mean?)
- Connect to strategy (why does it matter?)
- Suggest action (what should we do?)

### Timeline Management

**Event Classification:**
- CRITICAL (Red): Board meetings, contract deadlines, critical hires
- HIGH (Orange): Key client meetings, important milestones
- NORMAL (No color): Regular recurring items, standard activities

**Event Descriptions:**
- Start with action verb when possible
- Include time if meeting/call
- Add location if travel involved
- Keep to 8 words maximum

## Quality Assurance Checklist

### Before distributing each week's brief:

#### Content Review
- [ ] Executive snapshot updated
- [ ] All sections current
- [ ] Metrics accurate
- [ ] Timeline shows correct dates
- [ ] Action items have owners

#### Technical Check
- [ ] Timeline toggle works
- [ ] All charts render
- [ ] Navigation functional
- [ ] No console errors
- [ ] Mobile responsive

#### Quality Check
- [ ] Spelling and grammar
- [ ] Word limits respected
- [ ] Links work
- [ ] Print preview clean
- [ ] Professional appearance

## Troubleshooting

### Timeline Not Updating
**Symptoms:** Clicking toggle buttons doesn't change timeline content

**Solutions:**
- Check `data-view` attributes on buttons match data keys
- Verify `timelineData` object has both `week` and `twoweeks` properties
- Check browser console for JavaScript errors
- Ensure `initializeTimeline()` called in `initialize()` function

### Charts Not Rendering
**Symptoms:** Blank spaces where charts should appear

**Solutions:**
- Verify Chart.js loaded from CDN (check Network tab)
- Check canvas elements have correct IDs
- Ensure chart initialization wrapped in try-catch
- Check data arrays have valid numbers (not strings)
- Verify chart initialization happens after DOM ready

### Sections Not Collapsing
**Symptoms:** Clicking headers doesn't toggle sections

**Solutions:**
- Check `section-header` class on clickable elements
- Verify closest `.section` has proper structure
- Check `collapsed` class defined in CSS
- Ensure `initializeSections()` called properly

### Navigation Not Scrolling
**Symptoms:** Clicking nav items doesn't scroll to sections

**Solutions:**
- Verify section IDs match nav href values
- Check `scrollIntoView` supported in browser
- Ensure `initializeNavigation()` called
- Check for CSS scroll-behavior conflicts

## Version History

- **v1.0** (2025-11-15) - Initial production release
  - Complete functionality verified
  - Timeline toggle fully operational
  - All accessibility features implemented
  - Print optimization included
  - Comprehensive documentation

---

**Ready to create your weekly brief?** Fill in the template and follow the mapping guide above.
