# Chart Specifications

Complete guide for chart types, data requirements, visual design, and Chart.js implementation for 360 newsletters.

## Overview

Every newsletter must include **minimum 4 charts** showing:
1. Partnership portfolio distribution
2. Project/activity distribution
3. Trends over time
4. Strategic metrics

All charts use Chart.js (loaded via CDN) with professional, monochromatic styling.

## Chart Types

### 1. Doughnut/Pie Charts

**Best for:**
- Showing parts of a whole
- Portfolio composition
- Regional/geographic distribution
- Revenue source breakdown
- Time allocation by focus area

**Minimum data points:** 2 segments
**Optimal data points:** 3-6 segments
**Maximum recommended:** 8 segments (more becomes unreadable)

**Example use cases:**
- Partnership portfolio by sector
- Project distribution by region
- Revenue sources breakdown
- Team time allocation

#### Implementation Example

```javascript
new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Nuclear Tech', 'Biomaterials', 'Innovation Services',
                 'Space/Arch', 'Healthcare', 'Investment DD'],
        datasets: [{
            data: [15, 15, 25, 15, 15, 15],
            backgroundColor: [
                '#1e3a8a',  // Dark blue
                '#3b82f6',  // Medium blue
                '#60a5fa',  // Light blue
                '#93c5fd',  // Lighter blue
                '#dbeafe',  // Very light blue
                '#1e40af'   // Dark blue variant
            ],
            borderWidth: 2,
            borderColor: '#fff'
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                position: 'bottom',
                labels: {
                    font: { size: 10 },
                    padding: 8
                }
            }
        }
    }
});
```

### 2. Bar Charts

**Best for:**
- Comparing categories
- Pipeline stages
- Market fit scores
- Completion velocity
- Regional growth

**Minimum data points:** 2 categories
**Optimal data points:** 3-5 categories
**Maximum recommended:** 8 categories

**Example use cases:**
- Partnership pipeline by stage (Discovery, Scoping, Active, Renewal)
- Service package market fit
- Project completion by team member
- Revenue by quarter

#### Implementation Example (Horizontal)

```javascript
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Venture IQ\n(CVC)', 'Intelligence Audit\n(TTO)',
                 'Innovation Compass\n(Full Service)'],
        datasets: [{
            label: 'Market Fit Score',
            data: [85, 60, 100],
            backgroundColor: ['#1e3a8a', '#3b82f6', '#60a5fa'],
            borderRadius: 4
        }]
    },
    options: {
        indexAxis: 'y',  // Horizontal bars
        responsive: true,
        maintainAspectRatio: true,
        plugins: {
            legend: { display: false }
        },
        scales: {
            x: { display: false },
            y: {
                ticks: {
                    font: { size: 11 }
                }
            }
        }
    }
});
```

#### Implementation Example (Vertical)

```javascript
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Discovery', 'Scoping', 'Active', 'Renewal'],
        datasets: [{
            label: 'Pipeline Value ($K)',
            data: [150, 320, 580, 210],
            backgroundColor: ['#b0bec5', '#90a4ae', '#78909c', '#546e7a']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: { callback: value => '$' + value + 'K' }
            }
        }
    }
});
```

### 3. Radar Charts

**Best for:**
- Multi-dimensional comparisons
- Team capability assessment
- Service offering maturity
- Market positioning
- Strategic alignment

**Minimum data points:** 3 dimensions
**Optimal data points:** 5-7 dimensions
**Maximum recommended:** 10 dimensions

**Example use cases:**
- Team capabilities before/after hires
- Service offering maturity across dimensions
- Partnership health across criteria
- Strategic priority alignment

#### Implementation Example

```javascript
new Chart(ctx, {
    type: 'radar',
    data: {
        labels: ['Corp BD', 'AI/Tech', 'Multilingual',
                 'Strategic', 'Financial', 'Agritech'],
        datasets: [
            {
                label: 'Current Team',
                data: [50, 75, 60, 70, 50, 30],
                backgroundColor: 'rgba(30, 58, 138, 0.2)',
                borderColor: '#1e3a8a',
                pointBackgroundColor: '#1e3a8a',
                borderWidth: 2
            },
            {
                label: 'With New Hires',
                data: [90, 85, 95, 90, 90, 85],
                backgroundColor: 'rgba(96, 165, 250, 0.2)',
                borderColor: '#60a5fa',
                pointBackgroundColor: '#60a5fa',
                borderWidth: 2
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            r: {
                beginAtZero: true,
                max: 100,
                ticks: { font: { size: 10 } }
            }
        },
        plugins: {
            legend: {
                labels: { font: { size: 11 } }
            }
        }
    }
});
```

### 4. Line Charts

**Best for:**
- Trends over time
- Growth trajectories
- Completion velocity
- Revenue trends
- Metric evolution

**Minimum data points:** 2 time periods
**Optimal data points:** 4-6 time periods
**Maximum recommended:** 12 time periods (monthly over year)

**Example use cases:**
- Revenue trajectory (quarterly)
- Partnership pipeline growth (monthly)
- Task completion trends (weekly)
- Impact metrics over time (quarterly)

#### Implementation Example

```javascript
new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Q-2', 'Q-1', 'Current', 'Projected'],
        datasets: [{
            label: 'Revenue ($K)',
            data: [45, 62, 89, 110],
            borderColor: '#37474f',
            backgroundColor: 'rgba(55, 71, 79, 0.1)',
            tension: 0.4,
            fill: true,
            pointRadius: 4,
            pointBackgroundColor: '#37474f'
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: true }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: { callback: value => '$' + value + 'K' }
            }
        }
    }
});
```

## Data Requirements

### Minimum Data for Each Chart Type

| Chart Type | Minimum | Fallback if Insufficient |
|------------|---------|--------------------------|
| Doughnut/Pie | 2 segments | Stat card with single metric |
| Bar | 2 categories | Text-based summary |
| Radar | 3 dimensions | Bar chart or stat cards |
| Line | 2 time periods | Single period stat or narrative |

### Data Quality Checks

Before generating chart, verify:
1. **Data completeness**: All segments have values
2. **Data accuracy**: Numbers are from actual sources, not estimates
3. **Data relevance**: Chart shows meaningful information
4. **Data scale**: Values are appropriate for visualization type

### Fallback Strategies

**If chart data insufficient:**

**Option 1: Stat Card**
```html
<div class="stat-card">
    <div class="stat-value">12</div>
    <div class="stat-label">Active Partnerships</div>
</div>
```

**Option 2: Text-based Summary**
```html
<div class="chart-fallback">
    <h4>Partnership Distribution</h4>
    <ul>
        <li>Nuclear Technology: 2 partnerships</li>
        <li>Biomaterials: 3 partnerships</li>
        <li>Innovation Services: 5 partnerships</li>
    </ul>
</div>
```

**Option 3: Narrative Description**
```html
<p>Partnership portfolio remains concentrated in innovation services
(~40%), with emerging focus on nuclear technology and biomaterials
platforms representing 30% of active relationships.</p>
```

## Visual Design Specifications

### Color Palette

**Primary (Blues for partnerships):**
- `#1e3a8a` - Dark blue
- `#3b82f6` - Medium blue
- `#60a5fa` - Light blue
- `#93c5fd` - Lighter blue
- `#dbeafe` - Very light blue

**Secondary (Greens for operations):**
- `#10b981` - Emerald green
- `#34d399` - Light green
- `#6ee7b7` - Very light green

**Accent (Oranges for strategy):**
- `#f59e0b` - Amber
- `#fbbf24` - Yellow

**Neutrals (for general charts):**
- `#37474f` - Dark gray
- `#546e7a` - Medium gray
- `#78909c` - Gray
- `#90a4ae` - Light gray
- `#b0bec5` - Very light gray
- `#cfd8dc` - Lightest gray

### Typography

**Font families:**
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
             'Helvetica Neue', Arial, sans-serif;
```

**Font sizes:**
- Chart titles: 13px, weight 600
- Axis labels: 11px
- Legend labels: 10-11px
- Tooltips: 12px

**Color:**
- Titles: `#111827` (near-black)
- Labels: `#6b7280` (gray)
- Data values: `#111827`

### Styling Rules

**Grid lines:**
- Color: `#e5e7eb` (very light gray)
- Width: 1px
- Display: Minimal (only where necessary)

**Borders:**
- Chart borders: None
- Segment borders: 2px white (for doughnut/pie)
- Point borders: 2px matching segment color

**Spacing:**
- Padding inside chart: 18px
- Legend spacing: 8px between items
- Title margin bottom: 14px

**Shadows:**
- None (flat design)

**Animations:**
- Duration: 750ms
- Easing: 'easeInOutQuart'

## Chart Container Structure

### HTML Structure

```html
<div class="chart-container">
    <div class="chart-title">[Title]</div>
    <div class="chart-subtitle">[Subtitle/Context]</div>
    <canvas id="[chartId]"></canvas>
</div>
```

### CSS Styling

```css
.chart-container {
    margin: 20px 0;
    padding: 18px;
    background-color: #f9fafb;
    border-radius: 8px;
}

.chart-title {
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 4px;
    color: #111827;
}

.chart-subtitle {
    font-size: 12px;
    color: #6b7280;
    margin-bottom: 14px;
}

canvas {
    max-height: 220px;
}
```

## Required Charts by Newsletter Type

### Weekly Newsletter (4 charts minimum)

1. **Partnership Pipeline Distribution** (Bar)
   - Shows pipeline by stage
   - Data from Asana custom fields or sections

2. **Project Distribution by Region** (Doughnut)
   - Shows geographic spread
   - Data from Asana task analysis

3. **Recent Activity Trend** (Line)
   - Shows task completion velocity
   - Data from Asana completed tasks

4. **Team Capacity** (Radar or Bar)
   - Shows capability areas
   - Data from team composition

### Monthly Board Brief (6-8 charts recommended)

All weekly charts, plus:

5. **Revenue Trajectory** (Line)
   - Quarterly revenue trend
   - Data from Drive financial docs

6. **Impact Metrics Trend** (Line)
   - Social impact over time
   - Data from Drive impact reports

7. **Partnership Health** (Radar)
   - Multi-dimensional assessment
   - Data from Asana + Gmail + Drive

8. **Strategic Priority Alignment** (Bar)
   - Progress on strategic goals
   - Data from multiple sources

### Custom Focus Brief (As relevant)

Select charts that support the specific focus:
- Partnership focus → Pipeline, regional distribution, health
- Operations focus → Team capacity, task velocity, process metrics
- Impact focus → Outcomes trend, beneficiary reach, systems change

## Chart Data Sources

### Partnership Pipeline Distribution

**Data source:** Asana
**Collection method:**
```javascript
// Get tasks in Partnership Development project
// Group by custom field "Stage" or by section
// Count tasks per stage
// Calculate total value if available
```

**Chart type:** Horizontal bar
**Labels:** ['Discovery', 'Scoping', 'Active', 'Renewal']
**Data:** Count of partnerships in each stage
**Alternative data:** Pipeline value ($K) per stage

### Project Distribution by Region

**Data source:** Asana
**Collection method:**
```javascript
// Get all active tasks across projects
// Categorize by region keywords in name/tags
// North America: US, USA, Seattle, Washington, Canada
// Latin America: Brazil, São Paulo, LATAM, Argentina
// Europe: UK, Europe, EU, Germany, France
// Asia-Pacific: China, Australia, Japan, APAC
// Other: All remaining
```

**Chart type:** Doughnut
**Labels:** ['North America', 'Latin America', 'Europe', 'Asia-Pacific', 'Other']
**Data:** Percentage or count of projects per region

### Task Completion Velocity

**Data source:** Asana
**Collection method:**
```javascript
// Get completed tasks for last 4 weeks
// Count completions per week
// Calculate trend
```

**Chart type:** Line
**Labels:** ['Week -3', 'Week -2', 'Week -1', 'Current']
**Data:** Task completions per week

### Team Capacity Assessment

**Data source:** Mixed (Asana + manual assessment)
**Collection method:**
```javascript
// Assess team capabilities across dimensions
// Corporate BD, AI/Tech, Multilingual, Strategic, Financial, Sector expertise
// Score 0-100 per dimension
// Compare current vs with new hires (if applicable)
```

**Chart type:** Radar
**Labels:** ['Corp BD', 'AI/Tech', 'Multilingual', 'Strategic', 'Financial', 'Agritech']
**Data:** Two datasets (current vs future)

### Revenue Trajectory

**Data source:** Google Drive
**Collection method:**
```javascript
// Search for financial documents
// Extract quarterly revenue numbers
// Include projection if available
```

**Chart type:** Line
**Labels:** ['Q-2', 'Q-1', 'Current', 'Projected']
**Data:** Revenue in $K per quarter

### Impact Metrics Trend

**Data source:** Google Drive + Gmail
**Collection method:**
```javascript
// Search for impact reports and metrics
// Extract key metrics over time
// Could be: beneficiaries served, outcomes achieved, systems changed
```

**Chart type:** Line
**Labels:** ['Month -3', 'Month -2', 'Month -1', 'Current']
**Data:** Impact metric (people/orgs/communities served)

## Chart.js Configuration

### Global Options

```javascript
Chart.defaults.font.family = '-apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", Arial, sans-serif';
Chart.defaults.color = '#6b7280';
Chart.defaults.borderColor = '#e5e7eb';
```

### Responsive Configuration

```javascript
options: {
    responsive: true,
    maintainAspectRatio: true,
    aspectRatio: 2,  // Width:height ratio
}
```

### Tooltip Customization

```javascript
options: {
    plugins: {
        tooltip: {
            backgroundColor: 'rgba(17, 24, 39, 0.95)',
            titleColor: '#fff',
            bodyColor: '#fff',
            borderColor: '#374151',
            borderWidth: 1,
            padding: 12,
            displayColors: true,
            callbacks: {
                label: function(context) {
                    return context.dataset.label + ': ' +
                           context.formattedValue;
                }
            }
        }
    }
}
```

## Quality Assurance

### Before Publishing Charts

**Verify:**
- [ ] All charts render correctly
- [ ] Data is accurate and from real sources
- [ ] Labels are readable and properly formatted
- [ ] Colors follow monochromatic palette
- [ ] Legends display when needed
- [ ] Tooltips show correct information
- [ ] Charts are responsive
- [ ] Maximum height constraint applied
- [ ] Print-friendly (grayscale acceptable)

### Common Issues

**Chart too tall:**
```css
canvas { max-height: 220px; }
```

**Labels overlapping:**
- Reduce font size
- Rotate labels
- Use shorter labels
- Switch to horizontal layout (for bar charts)

**Too many data points:**
- Limit to top N categories
- Group small categories into "Other"
- Use different chart type
- Show data in table instead

**Colors not distinguishable:**
- Ensure sufficient contrast between segments
- Test in grayscale mode
- Use patterns if needed (advanced)

---

**Next:** See [Workflow Examples](workflow-examples.md) for complete generation walkthroughs including chart creation.
