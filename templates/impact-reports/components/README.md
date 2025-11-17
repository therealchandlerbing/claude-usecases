# Component Library

**Reusable HTML components for both Static and Dynamic templates**

This library provides copy-paste ready components that work in both template variants. Each component is production-tested and follows the established design system.

---

## Table of Contents

1. [Layout Containers](#layout-containers)
2. [Content Cards](#content-cards)
3. [Metrics & Statistics](#metrics--statistics)
4. [Lists & Bullets](#lists--bullets)
5. [Badges & Tags](#badges--tags)
6. [Navigation Elements](#navigation-elements)
7. [Utility Components](#utility-components)

---

## Layout Containers

### Three-Column Grid

**Compatible:** Static, Dynamic
**Use for:** Main impact areas, strategic pillars

```html
<div class="three-column">
    <div class="column-card">
        <!-- First column content -->
    </div>
    <div class="column-card">
        <!-- Second column content -->
    </div>
    <div class="column-card">
        <!-- Third column content -->
    </div>
</div>
```

**Notes:**
- Automatically stacks on mobile
- Equal width columns
- 2rem gap between columns

---

### Two-Column Grid

**Compatible:** Static, Dynamic
**Use for:** Comparisons, detailed sections

```html
<div class="two-column">
    <div class="column-card">
        <!-- Left column content -->
    </div>
    <div class="column-card">
        <!-- Right column content -->
    </div>
</div>
```

**Notes:**
- Stacks on tablet and mobile
- 50/50 split on desktop
- Same 2rem gap

---

### Stats Row

**Compatible:** Static, Dynamic
**Use for:** Key performance indicators

```html
<div class="stats-row">
    <div class="stat-card">
        <div class="stat-label">METRIC LABEL</div>
        <div class="stat-value">142</div>
        <div class="stat-description">Brief context</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">ANOTHER METRIC</div>
        <div class="stat-value">37</div>
        <div class="stat-description">More context</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">THIRD METRIC</div>
        <div class="stat-value">89</div>
        <div class="stat-description">Final context</div>
    </div>
</div>
```

**Styling:**
- 3 metrics maximum
- Equal width distribution
- Transparent background
- Stacks on mobile

---

### Content Grid (Dynamic Only)

**Compatible:** Dynamic only
**Use for:** Card layouts with flexible sizing

```html
<div class="content-grid grid-3">
    <div class="metric-group">
        <!-- Content -->
    </div>
    <div class="metric-group">
        <!-- Content -->
    </div>
    <div class="metric-group">
        <!-- Content -->
    </div>
</div>
```

**Variants:**
- `.grid-2` - Two columns
- `.grid-3` - Three columns

---

## Content Cards

### Basic Column Card

**Compatible:** Static, Dynamic
**Use for:** Most content sections

```html
<div class="column-card">
    <div class="column-header">
        <h3 class="column-title">CARD TITLE</h3>
        <span class="pillar-tag">CATEGORY</span>
    </div>

    <!-- Card content here -->
    <!-- Can include metrics, lists, paragraphs, etc. -->
</div>
```

**Styling:**
- Subtle background elevation
- Rounded corners (12px)
- Internal padding (2rem vertical, 1.75rem horizontal)
- Optional header with tag

---

### Card with Metric (Static/Dynamic)

**Use for:** Impact areas, program outcomes

```html
<div class="column-card">
    <div class="column-header">
        <h3 class="column-title">HEALTH ACCESS</h3>
        <span class="pillar-tag">PRIMARY PILLAR</span>
    </div>

    <div class="metric-label">PATIENTS SERVED</div>
    <div class="metric-value">847K</div>
    <div class="metric-change">+41% from FY 2024</div>

    <ul class="outcome-list">
        <!-- Outcome items -->
    </ul>
</div>
```

---

### Dynamic Card Component

**Compatible:** Dynamic only
**Use for:** Elevated card styling

```html
<div class="card">
    <div class="card-header">
        <h3 class="card-title">Who we reach</h3>
        <span class="card-label">Annual snapshot</span>
    </div>

    <p style="color: var(--text-secondary); margin-bottom: var(--space-xl);">
        Descriptive text providing context for the card content.
    </p>

    <!-- Card content: grids, lists, metrics, etc. -->
</div>
```

**Difference from column-card:**
- Uses `card` class (dynamic template)
- Different styling variables
- Hover effect (raises on hover)

---

### Region Card (Dynamic Only)

**Compatible:** Dynamic only
**Use for:** Geographic breakdowns

```html
<div class="region-grid">
    <div class="region-card">
        <div class="region-name">Latin America</div>
        <div class="region-percentage">36%</div>
        <div class="region-description">
            Deepening work in Brazil and the region, combining innovation management,
            workforce development, and digital health.
        </div>
    </div>
    <div class="region-card">
        <div class="region-name">Africa</div>
        <div class="region-percentage">26%</div>
        <div class="region-description">
            Focus on climate resilience, digital public goods, and inclusive finance
            with local partners.
        </div>
    </div>
    <!-- 4 more cards for 3×2 grid -->
</div>
```

**Styling:**
- Gradient background
- Large percentage display (teal/orange)
- Hover effect
- Responsive grid (3→2→1 columns)

---

## Metrics & Statistics

### Large Metric Display (Static)

**Compatible:** Static
**Use for:** Hero metrics in column cards

```html
<div class="metric-label">PATIENTS SERVED</div>
<div class="metric-value">847K</div>
<div class="metric-change">+41% from FY 2024</div>
```

**Styling:**
- Label: 0.75rem, uppercase, muted
- Value: 3.5rem, bold, white
- Change: 0.875rem, accent color

---

### Metric Group (Dynamic)

**Compatible:** Dynamic
**Use for:** Dashboard-style metrics

```html
<div class="metric-group">
    <div class="metric-label">Lives Impacted</div>
    <div class="metric-value large">1.8M</div>
    <div class="metric-description">
        Individuals reached across programs in health, skills, and income generation.
    </div>
</div>
```

**Size variants:**
- `metric-value` - Default (1.875rem)
- `metric-value large` - Emphasized (2.25rem)

---

### Stat Card (Static/Dynamic)

**Use for:** Stats row components

```html
<div class="stat-card">
    <div class="stat-label">ACTIVE PARTNERSHIPS</div>
    <div class="stat-value">142</div>
    <div class="stat-description">Across 38 countries</div>
</div>
```

**Styling:**
- Transparent background
- Large value (3rem)
- Compact layout

---

## Lists & Bullets

### Outcome List (Static)

**Compatible:** Static
**Use for:** Impact outcomes, program results

```html
<ul class="outcome-list">
    <li class="outcome-item">
        <div class="outcome-bullet"></div>
        <div class="outcome-content">
            <h4>Maternal health</h4>
            <p>92% of mothers received prenatal care within recommended windows.</p>
        </div>
    </li>
    <li class="outcome-item">
        <div class="outcome-bullet"></div>
        <div class="outcome-content">
            <h4>Chronic disease management</h4>
            <p>68% reduction in emergency visits for diabetes and hypertension patients.</p>
        </div>
    </li>
    <li class="outcome-item">
        <div class="outcome-bullet"></div>
        <div class="outcome-content">
            <h4>Telemedicine expansion</h4>
            <p>Reached 127 remote communities previously without consistent access.</p>
        </div>
    </li>
</ul>
```

**Styling:**
- 6px orange bullet
- Flexbox layout
- 1.25rem gap between items
- Title: 0.95rem, semi-bold
- Description: 0.875rem, secondary color

---

### Content List (Dynamic)

**Compatible:** Dynamic
**Use for:** Detailed list items with longer descriptions

```html
<ul class="content-list">
    <li class="list-item">
        <span class="list-marker"></span>
        <div class="list-content">
            <div class="list-title">34% increase in high-intensity interventions</div>
            <div class="list-description">
                More participants are receiving integrated services across health, skills,
                and income, rather than single-touch engagements.
            </div>
        </div>
    </li>
    <li class="list-item">
        <span class="list-marker"></span>
        <div class="list-content">
            <div class="list-title">22% reduction in cost per outcome</div>
            <div class="list-description">
                Process redesign, digital tools, and better partner alignment are reducing
                cost per verified outcome while preserving quality.
            </div>
        </div>
    </li>
</ul>
```

**Styling:**
- 8px orange marker (vs 6px in static)
- More spacing (1.5rem gap)
- Larger text (1rem title, 0.875rem description)

---

### List with Inline Badges

**Compatible:** Both
**Use for:** Lists with status indicators

```html
<li class="outcome-item">
    <div class="outcome-bullet"></div>
    <div class="outcome-content">
        <h4>Partnership Name <span class="status-badge expanded">✓ EXPANDED</span></h4>
        <p>5-year, $12M commitment supporting maternal and child health.</p>
    </div>
</li>
```

Or for dynamic template:

```html
<li class="list-item">
    <span class="list-marker"></span>
    <div class="list-content">
        <div class="list-title">
            Global Health Alliance
            <span style="color: var(--status-success); font-size: var(--text-xs);">✓ EXPANDED</span>
        </div>
        <div class="list-description">
            5-year, $12M commitment supporting maternal and child health across 8 countries.
        </div>
    </div>
</li>
```

---

## Badges & Tags

### Status Badges (Static)

**Compatible:** Static
**Use for:** Partnership/program status

```html
<!-- Green "expanded" badge -->
<span class="status-badge expanded">✓ EXPANDED</span>

<!-- Blue "new" badge -->
<span class="status-badge new">✓ NEW</span>
```

**Usage:**
```html
<h4>Tech for Good Initiative <span class="status-badge new">✓ NEW</span></h4>
```

**Styling:**
- Expanded: Green background (#22c55e)
- New: Blue background (#38bdf8)
- Uppercase text
- Small (0.7rem)

---

### Pillar Tags (Static/Dynamic)

**Compatible:** Both
**Use for:** Categorization in card headers

```html
<span class="pillar-tag">PRIMARY PILLAR</span>
<span class="pillar-tag">BY TYPE</span>
<span class="pillar-tag">HIGHLIGHTED</span>
<span class="pillar-tag">FY 2025 RESULTS</span>
```

**Styling:**
- Light background (rgba(255, 255, 255, 0.05))
- Subtle border
- Muted text color
- Rounded (12px)
- Small (0.7rem)

---

### Page Meta Badges (Dynamic Only)

**Compatible:** Dynamic
**Use for:** Page metadata and navigation

```html
<div class="page-meta">
    <span class="badge">
        <span class="badge-dot" style="color: var(--brand-teal);"></span>
        FY 2025
    </span>
    <span class="badge">
        <span class="badge-dot" style="color: var(--brand-orange);"></span>
        Impact and outcomes
    </span>
    <span class="page-number">Page 1 of 6</span>
</div>
```

**Styling:**
- Inline-flex layout
- Colored dot indicator
- Uppercase text
- Subtle background

---

### Card Labels (Dynamic Only)

**Compatible:** Dynamic
**Use for:** Small categorization labels

```html
<span class="card-label">Annual snapshot</span>
<span class="card-label">Year on year</span>
<span class="card-label">Methodology</span>
```

**Styling:**
- Very small (0.75rem)
- Uppercase
- Dark background
- Rounded corners

---

## Navigation Elements

### Navigation Buttons

**Compatible:** Both
**HTML:**

```html
<button class="nav-button" id="prevBtn" onclick="previousSlide()">‹</button>
<button class="nav-button" id="nextBtn" onclick="nextSlide()">›</button>
```

**Styling:**
- 40px × 40px (static) or 2.5rem × 2.5rem (dynamic)
- Rounded corners
- Hover: accent color
- Disabled state: reduced opacity

---

### Page Dots (Static)

**Compatible:** Static
**Generated via JavaScript:**

```javascript
function initDots() {
    const dotsContainer = document.getElementById('pageDots');
    for (let i = 1; i <= totalSlides; i++) {
        const dot = document.createElement('div');
        dot.className = 'dot' + (i === 1 ? ' active' : '');
        dot.onclick = () => goToPage(i);
        dotsContainer.appendChild(dot);
    }
}
```

**HTML container:**
```html
<div class="page-dots" id="pageDots"></div>
```

---

### Nav Dots (Dynamic)

**Compatible:** Dynamic
**HTML:**

```html
<div class="nav-dots" role="tablist">
    <button class="nav-dot active" data-slide="0" role="tab">C</button>
    <button class="nav-dot" data-slide="1" role="tab">1</button>
    <button class="nav-dot" data-slide="2" role="tab">2</button>
    <button class="nav-dot" data-slide="3" role="tab">3</button>
    <button class="nav-dot" data-slide="4" role="tab">4</button>
    <button class="nav-dot" data-slide="5" role="tab">5</button>
    <button class="nav-dot" data-slide="6" role="tab">6</button>
</div>
```

**Difference:**
- Labeled (C for Cover, 1-6 for slides)
- Larger (2.5rem × 2.5rem)
- ARIA tab list pattern

---

### Page Selector Dropdown (Static)

**Compatible:** Static
**HTML:**

```html
<div class="page-select-wrapper">
    <select id="pageSelect" onchange="goToPage(this.value)">
        <option value="1">1. Impact Measurement</option>
        <option value="2">2. Partnership Ecosystem</option>
        <option value="3">3. Financial Overview</option>
        <option value="4">4. Program Outcomes</option>
        <option value="5">5. Strategic Priorities</option>
        <option value="6">6. Forward Outlook</option>
    </select>
</div>
```

**Styling:**
- Custom dropdown arrow (::after pseudo-element)
- Min-width: 200px
- Matches header styling

---

### View Selector (Dynamic)

**Compatible:** Dynamic
**HTML:**

```html
<select class="view-selector" id="viewSelect">
    <option value="0">Cover</option>
    <option value="1">1. Impact and outcomes</option>
    <option value="2">2. Impact by region</option>
    <option value="3">3. Financial performance</option>
    <option value="4">4. Program outcomes</option>
    <option value="5">5. Partnership Ecosystem</option>
    <option value="6">6. Looking forward</option>
</select>
```

**Difference:**
- Includes cover page (value="0")
- No wrapper div needed
- Different class name

---

## Utility Components

### Slide Header (Static)

**Compatible:** Static
**HTML:**

```html
<div class="slide-eyebrow">IMPACT MEASUREMENT</div>
<h1 class="slide-title">Program outcomes</h1>
<p class="slide-description">
    Lives changed, communities strengthened, and systems shifted across three impact areas.
</p>
```

**Styling:**
- Eyebrow: 0.75rem, uppercase, accent color
- Title: 3rem, bold, white
- Description: 1.125rem, secondary color

---

### Page Header (Dynamic)

**Compatible:** Dynamic
**HTML:**

```html
<div class="section-label">Executive Overview</div>
<h2 class="page-title">Impact at a glance</h2>
<p class="page-subtitle">
    A concise snapshot of our reach, depth of outcomes, and financial leverage,
    tailored for board and executive review.
</p>
```

**Styling:**
- Label: 0.75rem, uppercase, accent color
- Title: 2.25rem, bold, white (h2 not h1)
- Subtitle: 1.125rem, secondary color

---

### Highlight Text (Dynamic Only)

**Compatible:** Dynamic
**HTML:**

```html
<p class="highlight-text">
    This year we delivered <span class="accent">measurable, compounding value</span>
    across our ecosystem while preserving a disciplined approach to risk and inclusion.
</p>
```

**Styling:**
- Gradient background
- Orange left border (3px)
- Larger text (1.125rem)
- `.accent` class uses teal color

---

### Data Table (Dynamic Only)

**Compatible:** Dynamic
**HTML:**

```html
<table class="data-table">
    <thead>
        <tr>
            <th>Metric</th>
            <th>Value</th>
            <th>Commentary</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Capital mobilized</td>
            <td>$42M</td>
            <td>Total capital under active management this year, including multi-year commitments.</td>
        </tr>
        <tr>
            <td>Percent deployed to Global South</td>
            <td>78%</td>
            <td>Majority of capital directed to low and middle-income contexts, consistent with mission.</td>
        </tr>
    </tbody>
</table>
```

**Styling:**
- Rounded corners (border-radius on table)
- Elevated background
- Subtle borders between rows
- First column bold

---

### Skip Link (Dynamic Only)

**Compatible:** Dynamic
**HTML:**

```html
<a href="#main" class="skip-link">Skip to content</a>
```

**Styling:**
- Hidden by default (off-screen)
- Visible on keyboard focus
- Jumps to main content
- Accessibility best practice

---

## CSS Variables Reference

### Static Template

```css
:root {
    /* Colors */
    --bg-primary: #0a0e1a;
    --bg-secondary: #151922;
    --bg-card: #1a1f2e;
    --text-primary: #ffffff;
    --text-secondary: #9ca3af;
    --text-muted: #6b7280;
    --accent-orange: #ff6b35;

    /* Spacing (not named variables, but consistent values) */
    /* Use: 0.25rem, 0.5rem, 0.75rem, 1rem, 1.25rem, 1.5rem, 2rem, 3rem */
}
```

### Dynamic Template

```css
:root {
    /* Brand colors */
    --brand-orange: #FF6B35;
    --brand-teal: #00D9C0;

    /* Background layers */
    --bg-app: #0a0e1a;
    --bg-primary: #141824;
    --bg-elevated: #1a1f2e;

    /* Text hierarchy */
    --text-primary: #ffffff;
    --text-secondary: #b4bac5;
    --text-muted: #6b7280;

    /* Status colors */
    --status-success: #10b981;
    --status-warning: #f59e0b;
    --status-info: #3b82f6;

    /* Spacing scale */
    --space-xs: 0.25rem;
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    --space-xl: 2rem;
    --space-2xl: 3rem;
    --space-3xl: 4rem;

    /* Typography scale */
    --text-xs: 0.75rem;
    --text-sm: 0.875rem;
    --text-base: 1rem;
    --text-lg: 1.125rem;
    --text-xl: 1.25rem;
    --text-2xl: 1.5rem;
    --text-3xl: 1.875rem;
    --text-4xl: 2.25rem;

    /* Radius */
    --radius-sm: 0.375rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-xl: 1rem;

    /* Transitions */
    --transition-fast: 150ms ease;
    --transition-base: 200ms ease;
}
```

---

## Usage Examples

### Building a Complete Slide (Static)

```html
<div class="slide" data-slide="1">
    <!-- Header -->
    <div class="slide-eyebrow">YOUR CATEGORY</div>
    <h1 class="slide-title">Your Title</h1>
    <p class="slide-description">Your one-sentence description here.</p>

    <!-- Stats row (optional) -->
    <div class="stats-row">
        <!-- 3 stat-cards -->
    </div>

    <!-- Main content -->
    <div class="three-column">
        <div class="column-card">
            <div class="column-header">
                <h3 class="column-title">COLUMN 1</h3>
                <span class="pillar-tag">TAG</span>
            </div>
            <div class="metric-label">METRIC</div>
            <div class="metric-value">123K</div>
            <div class="metric-change">+10%</div>
            <ul class="outcome-list">
                <!-- 3-4 outcome-items -->
            </ul>
        </div>
        <!-- Repeat for columns 2 and 3 -->
    </div>
</div>
```

---

### Building a Complete Slide (Dynamic)

```html
<article class="slide" id="slide1" data-slide="1">
    <!-- Page meta -->
    <div class="page-meta">
        <span class="badge">
            <span class="badge-dot" style="color: var(--brand-teal);"></span>
            Category
        </span>
        <span class="page-number">Page 1 of 6</span>
    </div>

    <!-- Header -->
    <div class="section-label">SECTION NAME</div>
    <h2 class="page-title">Page Title</h2>
    <p class="page-subtitle">Your one-sentence description.</p>

    <!-- Card -->
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Card Title</h3>
            <span class="card-label">Label</span>
        </div>

        <!-- Content grid -->
        <div class="content-grid grid-3">
            <div class="metric-group">
                <!-- Metric content -->
            </div>
            <!-- Repeat 2 more times -->
        </div>

        <!-- Highlight text -->
        <p class="highlight-text">
            Key takeaway with <span class="accent">emphasized text</span>.
        </p>
    </div>
</article>
```

---

## Component Compatibility Matrix

| Component | Static | Dynamic | Notes |
|-----------|:------:|:-------:|-------|
| three-column | ✅ | ✅ | Identical |
| two-column | ✅ | ✅ | Identical |
| stats-row | ✅ | ✅ | Identical |
| column-card | ✅ | ❌ | Static only |
| card | ❌ | ✅ | Dynamic only |
| outcome-list | ✅ | ❌ | Static only |
| content-list | ❌ | ✅ | Dynamic only |
| metric-label/value/change | ✅ | ✅ | Identical |
| metric-group | ❌ | ✅ | Dynamic only |
| status-badge | ✅ | ✅ | Different styling |
| pillar-tag | ✅ | ✅ | Identical |
| region-grid/card | ❌ | ✅ | Dynamic only |
| data-table | ❌ | ✅ | Dynamic only |
| highlight-text | ❌ | ✅ | Dynamic only |
| page-meta badges | ❌ | ✅ | Dynamic only |

---

## Best Practices

### Component Selection

**For concise content:**
- Use Static template components
- Stick to 3-4 items per list
- Keep descriptions under 15 words

**For detailed content:**
- Use Dynamic template components
- Can use 5-7 items per list
- Descriptions can be 20-30 words

### Nesting Rules

**Do:**
```html
<div class="three-column">
    <div class="column-card">
        <ul class="outcome-list">
            <li class="outcome-item">...</li>
        </ul>
    </div>
</div>
```

**Don't:**
```html
<!-- Don't nest grids -->
<div class="three-column">
    <div class="two-column">...</div>
</div>
```

### Responsive Considerations

- All grid layouts automatically stack on mobile
- Test at 768px, 1024px, 1440px breakpoints
- Ensure text remains readable when stacked
- Check that metrics don't wrap awkwardly

---

**Component Library v2.0 | November 2025**
**Compatible with:** Static & Dynamic Impact Report Templates
