# Implementation Guide

**Comprehensive technical knowledge base for the Executive Impact Presentation Generator skill.**

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Content Processing System](#content-processing-system)
3. [Template Structure](#template-structure)
4. [Branding System](#branding-system)
5. [Navigation Implementation](#navigation-implementation)
6. [Accessibility Framework](#accessibility-framework)
7. [Print Optimization](#print-optimization)
8. [Quality Validation](#quality-validation)
9. [Advanced Customization](#advanced-customization)
10. [Integration Patterns](#integration-patterns)

---

## Architecture Overview

### System Design

```
User Content Input
        ↓
Content Parser & Validator
        ↓
Content Schema Normalization
        ↓
    ┌───┴───┐
    ↓       ↓
Presentation  Executive
Template      Template
    ↓           ↓
Branding    Branding
Application Application
    ↓           ↓
Quality     Quality
Validation  Validation
    ↓           ↓
HTML Output HTML Output
```

### Core Components

**1. Content Processing Pipeline**
- Input parser (multiple format support)
- Schema validator (completeness checking)
- Content normalizer (standardize format)
- Metric formatter (units, percentages)

**2. Template Engine**
- Presentation template (fixed-slide layout)
- Executive template (continuous-scroll layout)
- Shared component library
- CSS variable system

**3. Branding System**
- Color customization engine
- Contrast validation
- Typography application
- Visual identity consistency

**4. Navigation System**
- Slide-based navigation (presentation)
- Section-based navigation (executive)
- Keyboard shortcuts
- Touch/mouse interactions

**5. Quality Assurance**
- Technical validation (HTML, CSS, JS)
- Content validation (completeness, accuracy)
- Accessibility validation (WCAG 2.1 AA)
- Visual validation (consistency, responsiveness)

---

## Content Processing System

### Input Format Support

**1. Structured Data (Preferred)**

```yaml
organization:
  name: "Acme Foundation"
  brand_color: "#0052CC"
  fiscal_year: "2025"

impact_overview:
  reach_metrics:
    - label: "Lives Impacted"
      value: "1.8M"
      description: "Comprehensive description"
```

**2. Semi-Structured Text**

```
Organization: Acme Foundation
Brand Color: #0052CC
Fiscal Year: 2025

IMPACT OVERVIEW
Reach Metrics:
- Lives Impacted: 1.8M (Comprehensive description)
- Countries: 14 (Geographic reach)
```

**3. Natural Language**

```
"We're Acme Foundation and we impacted 1.8 million lives
across 14 countries with $42M in capital..."
```

### Content Schema

**Organization Metadata:**
```typescript
interface Organization {
  name: string;                    // Required
  report_title?: string;           // Optional (default: "Executive Impact Report FY {year}")
  brand_color: string;             // Required (hex format: #RRGGBB)
  fiscal_year: string;             // Required
  report_date?: string;            // Optional (default: current month/year)
  audience?: string;               // Optional (default: "Board & Executives")
}
```

**Impact Overview:**
```typescript
interface ImpactOverview {
  reach_metrics: ReachMetric[];    // Exactly 3 required
  momentum: MomentumHighlight[];   // 3-4 recommended
}

interface ReachMetric {
  label: string;                   // E.g., "Lives Impacted"
  value: string;                   // E.g., "1.8M" (include units)
  description: string;             // < 100 characters recommended
}

interface MomentumHighlight {
  title: string;                   // E.g., "34% increase in high-intensity interventions"
  badge?: string | null;           // E.g., "Higher depth of support"
  badge_type?: 'success' | 'info' | 'warning' | null;
  description: string;             // < 150 characters recommended
}
```

**Regional Portfolio:**
```typescript
interface RegionalPortfolio {
  regions: Region[];               // Exactly 6 required
  strategic_priorities: Priority[]; // 3 recommended
}

interface Region {
  name: string;                    // E.g., "Latin America"
  percentage: string;              // E.g., "36%" (include % symbol)
  description: string;             // < 150 characters recommended
}

interface Priority {
  title: string;                   // < 50 characters recommended
  description: string;             // < 150 characters recommended
}
```

**Financial Performance:**
```typescript
interface FinancialPerformance {
  capital_overview: CapitalMetric[];  // 4-6 recommended
  capital_mix: CapitalCategory[];     // 3 categories (must total 100%)
  safeguards: Safeguard[];            // 2-3 recommended
}

interface CapitalMetric {
  metric: string;                  // E.g., "Capital mobilized"
  value: string;                   // E.g., "$42M"
  commentary: string;              // < 100 characters recommended
}

interface CapitalCategory {
  category: string;                // E.g., "Grants and Philanthropy"
  percentage: string;              // E.g., "34%" (must total 100%)
  description: string;             // < 150 characters recommended
}

interface Safeguard {
  title: string;                   // < 50 characters recommended
  description: string;             // < 150 characters recommended
}
```

**Program Outcomes:**
```typescript
interface ProgramOutcomes {
  pillars: ImpactPillar[];         // Exactly 3 required
  evaluation_approach: EvaluationPrinciple[];  // 3 recommended
}

interface ImpactPillar {
  name: string;                    // E.g., "Health Access"
  label?: string;                  // E.g., "Primary Pillar"
  metric_label: string;            // E.g., "Patients Served"
  metric_value: string;            // E.g., "847K"
  metric_change?: string;          // E.g., "+41% from FY 2024"
  outcomes: Outcome[];             // 3-4 recommended per pillar
}

interface Outcome {
  title: string;                   // < 30 characters recommended
  description: string;             // < 150 characters recommended
}

interface EvaluationPrinciple {
  title: string;                   // < 40 characters recommended
  description: string;             // < 150 characters recommended
}
```

**Partnership Ecosystem:**
```typescript
interface PartnershipEcosystem {
  statistics: PartnershipStat[];   // 3 recommended
  partner_categories: PartnerCategory[];  // 4-6 recommended
  flagship_partnerships: FlagshipPartnership[];  // 4-6 recommended
}

interface PartnershipStat {
  label: string;                   // E.g., "Active Partnerships"
  value: string;                   // E.g., "142"
  description: string;             // E.g., "Across 38 countries"
}

interface PartnerCategory {
  name: string;                    // E.g., "Foundation partners"
  count: number;                   // E.g., 42
  description: string;             // < 100 characters recommended
}

interface FlagshipPartnership {
  name: string;                    // E.g., "Global Health Alliance"
  status_badge?: string;           // E.g., "EXPANDED", "NEW", "ONGOING"
  status_type?: 'success' | 'info' | null;
  description: string;             // < 150 characters recommended
}
```

**Strategic Outlook:**
```typescript
interface StrategicOutlook {
  roadmap: Horizon[];              // Exactly 3 required
  leadership_asks: LeadershipAsk[];  // 3-4 recommended
}

interface Horizon {
  horizon: string;                 // E.g., "Horizon 1 · Next 6 months"
  description: string;             // < 200 characters recommended
}

interface LeadershipAsk {
  title: string;                   // < 50 characters recommended
  description: string;             // < 150 characters recommended
}
```

### Validation Rules

**Organization Validation:**
- `name`: Required, non-empty string
- `brand_color`: Required, valid hex format (`#RRGGBB`), contrast check
- `fiscal_year`: Required, non-empty string

**Content Validation:**
- All 6 sections present
- Required arrays have minimum element counts
- No placeholder text patterns (`[Organization]`, `TODO`, `XXX`)
- Percentages in capital_mix total 100% (±1% tolerance)
- All required fields populated

**Length Validation:**
- Metric descriptions: < 100 characters (warn), < 150 (error)
- Titles: < 50 characters (warn), < 80 (error)
- Descriptions: < 150 characters (warn), < 200 (error)
- Longer content may overflow presentation slides

---

## Template Structure

### Presentation Template Architecture

**HTML Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{organization_name} - Impact Report Presentation - {fiscal_year}</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    /* CSS Variables for branding */
    :root {
      --brand-color: {user_brand_color};
      --secondary-color: #FF6B35;
      --bg-dark: #1A1A1A;
      --bg-card: #2A2A2A;
      --text-primary: #FFFFFF;
      --text-secondary: #B0B0B0;
    }

    /* Presentation-specific styles */
    .presentation-container { /* Fixed-slide layout */ }
    .slide { /* 1050px × 700px slides */ }
    .slide-navigation { /* Arrows, dots */ }

    /* Print styles */
    @media print {
      @page { size: landscape; margin: 0; }
      .slide { page-break-after: always; }
      .slide-navigation { display: none; }
    }
  </style>
</head>
<body>
  <div class="presentation-container">
    <!-- Slide 0: Cover -->
    <div class="slide" data-slide="0">
      <!-- Cover content -->
    </div>

    <!-- Slide 1: Impact Overview -->
    <div class="slide" data-slide="1">
      <!-- Section content -->
    </div>

    <!-- Slides 2-6: Remaining sections -->

    <!-- Navigation -->
    <div class="slide-navigation">
      <!-- Arrows, dots, dropdown -->
    </div>
  </div>

  <script>
    /* Navigation JavaScript */
  </script>
</body>
</html>
```

**Key CSS Classes:**
- `.presentation-container`: Viewport-sized container
- `.slide`: Individual slides (1050px × 700px)
- `.slide-header`: Section title and label
- `.metric-card`: Metric display component
- `.content-card`: Generic content container
- `.bullet-list`: Styled bulleted lists
- `.badge`: Status indicators

### Executive Template Architecture

**HTML Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{organization_name} - Impact Report Executive - {fiscal_year}</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    /* CSS Variables (same as presentation) */

    /* Executive-specific styles */
    .executive-container { /* Continuous-scroll layout */ }
    .section { /* Unlimited height sections */ }
    .section-navigation { /* Dropdown navigation */ }

    /* Print styles */
    @media print {
      @page { size: portrait; margin: 0.5in; }
      .section { page-break-inside: avoid; }
      .section-navigation { display: none; }
    }
  </style>
</head>
<body>
  <div class="executive-container">
    <!-- Header with navigation -->
    <header>
      <select class="section-dropdown">
        <option value="overview">Impact Overview</option>
        <option value="regional">Regional Portfolio</option>
        <!-- ... -->
      </select>
    </header>

    <!-- Section 1: Impact Overview -->
    <section id="overview" class="section">
      <!-- Section content -->
    </section>

    <!-- Sections 2-6: Remaining sections -->
  </div>

  <script>
    /* Smooth scroll navigation */
  </script>
</body>
</html>
```

**Key CSS Classes:**
- `.executive-container`: Full-width scroll container
- `.section`: Individual sections (unlimited height)
- `.section-header`: Section title and navigation anchor
- `.metric-grid`: Grid layout for metrics
- `.content-flow`: Flexible content flow
- `.data-table`: Styled tables

### Shared Component Library

**Metric Display Component:**
```html
<div class="metric-card">
  <div class="metric-label">Lives Impacted</div>
  <div class="metric-value">1.8M</div>
  <div class="metric-description">
    Individuals reached across programs in health, skills, and income generation.
  </div>
</div>
```

**Content Card Component:**
```html
<div class="content-card">
  <div class="card-header">Regional Portfolio</div>
  <div class="card-body">
    <!-- Content here -->
  </div>
</div>
```

**Bulleted List Component:**
```html
<ul class="bullet-list">
  <li>
    <span class="bullet-title">Maternal health</span>
    <span class="bullet-description">92% of mothers received prenatal care within recommended windows.</span>
  </li>
</ul>
```

**Status Badge Component:**
```html
<span class="badge badge-success">✓ EXPANDED</span>
<span class="badge badge-info">✓ NEW</span>
<span class="badge badge-warning">! ATTENTION</span>
```

---

## Branding System

### Color Application

**CSS Variable System:**
```css
:root {
  /* User-provided brand color */
  --brand-color: #FF6B35;  /* Replaced with user's hex code */

  /* Fixed secondary accent */
  --secondary-color: #FF6B35;  /* Orange accent (complementary) */

  /* Dark theme base */
  --bg-dark: #1A1A1A;
  --bg-card: #2A2A2A;
  --text-primary: #FFFFFF;
  --text-secondary: #B0B0B0;
}
```

**Brand Color Usage:**
```css
/* Bullets and accents */
.bullet-list li::before {
  background: var(--brand-color);
}

/* Navigation elements */
.slide-dot.active {
  background: var(--brand-color);
}

/* Hover states */
.button:hover {
  background: var(--brand-color);
}

/* Status badges */
.badge-success {
  background: linear-gradient(135deg, var(--brand-color), var(--secondary-color));
}

/* Border accents */
.content-card {
  border-left: 3px solid var(--brand-color);
}
```

### Contrast Validation

**WCAG 2.1 AA Requirements:**
- Minimum contrast ratio: 4.5:1 for normal text
- Minimum contrast ratio: 3:1 for large text (18pt+)

**Validation Algorithm:**
```javascript
function validateContrast(brandColor, backgroundColor) {
  const brandRGB = hexToRGB(brandColor);
  const bgRGB = hexToRGB(backgroundColor);

  const brandLuminance = relativeLuminance(brandRGB);
  const bgLuminance = relativeLuminance(bgRGB);

  const contrastRatio = (Math.max(brandLuminance, bgLuminance) + 0.05) /
                        (Math.min(brandLuminance, bgLuminance) + 0.05);

  return contrastRatio >= 4.5;  // WCAG AA for normal text
}
```

**Fallback Strategy:**
- If brand color fails contrast check, use default (#FF6B35)
- Warn user about contrast issue
- Suggest lighter/darker alternatives

### Typography System

**Font Hierarchy:**
```css
/* H1: Section titles (presentation) */
h1 {
  font-size: 42px;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

/* H2: Section titles (executive) */
h2 {
  font-size: 28px;
  font-weight: 700;
  line-height: 1.3;
}

/* H3: Subsection titles */
h3 {
  font-size: 20px;
  font-weight: 600;
  line-height: 1.4;
}

/* Body text */
p, li {
  font-size: 16px;
  font-weight: 400;
  line-height: 1.6;
}

/* Metric values */
.metric-value {
  font-size: 48px;
  font-weight: 700;
  line-height: 1.1;
}
```

**Font Loading:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

---

## Navigation Implementation

### Presentation Format Navigation

**Slide-Based Navigation System:**

**1. Arrow Navigation:**
```javascript
// Previous slide
function previousSlide() {
  if (currentSlide > 0) {
    currentSlide--;
    showSlide(currentSlide);
  }
}

// Next slide
function nextSlide() {
  if (currentSlide < totalSlides - 1) {
    currentSlide++;
    showSlide(currentSlide);
  }
}

// Show specific slide
function showSlide(n) {
  const slides = document.querySelectorAll('.slide');
  slides.forEach((slide, index) => {
    slide.classList.toggle('active', index === n);
  });
  updateDots(n);
  updateDropdown(n);
}
```

**2. Keyboard Shortcuts:**
```javascript
document.addEventListener('keydown', (e) => {
  switch(e.key) {
    case 'ArrowLeft':
    case 'ArrowUp':
      previousSlide();
      break;
    case 'ArrowRight':
    case 'ArrowDown':
    case ' ':  // Spacebar
      nextSlide();
      break;
    case 'Home':
      showSlide(0);
      break;
    case 'End':
      showSlide(totalSlides - 1);
      break;
  }
});
```

**3. Dot Navigation:**
```javascript
function createDots() {
  const dotsContainer = document.querySelector('.slide-dots');
  for (let i = 0; i < totalSlides; i++) {
    const dot = document.createElement('button');
    dot.classList.add('slide-dot');
    dot.setAttribute('aria-label', `Go to slide ${i + 1}`);
    dot.addEventListener('click', () => showSlide(i));
    dotsContainer.appendChild(dot);
  }
}
```

**4. Dropdown Navigation:**
```html
<select class="slide-dropdown" onChange="handleDropdownChange(this.value)">
  <option value="0">Cover</option>
  <option value="1">Impact Overview</option>
  <option value="2">Regional Portfolio</option>
  <option value="3">Financial Performance</option>
  <option value="4">Program Outcomes</option>
  <option value="5">Partnership Ecosystem</option>
  <option value="6">Strategic Outlook</option>
</select>
```

### Executive Format Navigation

**Section-Based Navigation System:**

**1. Smooth Scroll to Section:**
```javascript
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    });
  }
}
```

**2. Dropdown Navigation:**
```javascript
const dropdown = document.querySelector('.section-dropdown');
dropdown.addEventListener('change', (e) => {
  scrollToSection(e.target.value);
});
```

**3. Intersection Observer (Auto-update dropdown):**
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const sectionId = entry.target.id;
      updateDropdown(sectionId);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('.section').forEach(section => {
  observer.observe(section);
});
```

---

## Accessibility Framework

### WCAG 2.1 AA Compliance

**Semantic HTML Structure:**
```html
<header role="banner">
  <nav role="navigation" aria-label="Section navigation">
    <!-- Navigation elements -->
  </nav>
</header>

<main role="main">
  <article aria-labelledby="section-title">
    <h2 id="section-title">Impact Overview</h2>
    <!-- Content -->
  </article>
</main>
```

**ARIA Labels:**
```html
<!-- Interactive elements -->
<button
  class="slide-arrow slide-arrow-prev"
  aria-label="Previous slide"
  onClick="previousSlide()">
  ←
</button>

<!-- Navigation dots -->
<button
  class="slide-dot"
  aria-label="Go to slide 2: Impact Overview"
  aria-current="false">
</button>

<!-- Dropdown -->
<select
  class="section-dropdown"
  aria-label="Navigate to section">
  <option value="overview">Impact Overview</option>
</select>
```

**Keyboard Navigation:**
- Tab: Navigate between interactive elements
- Enter/Space: Activate buttons and links
- Arrow keys: Navigate slides (presentation)
- Home: Go to first slide/section
- End: Go to last slide/section
- Escape: Close modals (if any)

**Focus Management:**
```css
/* Visible focus indicators */
button:focus,
a:focus,
select:focus {
  outline: 2px solid var(--brand-color);
  outline-offset: 2px;
}

/* Skip to content link */
.skip-to-content {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--brand-color);
  color: white;
  padding: 8px 16px;
  z-index: 100;
}

.skip-to-content:focus {
  top: 0;
}
```

**Screen Reader Support:**
```html
<!-- Live regions for dynamic content -->
<div
  role="status"
  aria-live="polite"
  aria-atomic="true"
  class="sr-only">
  Now showing slide {currentSlide + 1} of {totalSlides}
</div>

<!-- Screen reader only text -->
<span class="sr-only">
  Current section: Impact Overview
</span>
```

**Reduced Motion Support:**
```css
/* Respect prefers-reduced-motion */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  html {
    scroll-behavior: auto;
  }
}
```

---

## Print Optimization

### Presentation Format Print Styles

**Page Setup:**
```css
@media print {
  @page {
    size: landscape;
    margin: 0;
  }

  body {
    print-color-adjust: exact;
    -webkit-print-color-adjust: exact;
  }
}
```

**Slide Pagination:**
```css
@media print {
  .slide {
    page-break-after: always;
    page-break-inside: avoid;
    width: 100%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  /* Last slide: no page break */
  .slide:last-child {
    page-break-after: auto;
  }
}
```

**Hide Navigation:**
```css
@media print {
  .slide-navigation,
  .slide-arrow,
  .slide-dots,
  .slide-dropdown {
    display: none !important;
  }
}
```

### Executive Format Print Styles

**Page Setup:**
```css
@media print {
  @page {
    size: portrait;
    margin: 0.5in 0.75in;
  }

  body {
    print-color-adjust: exact;
    -webkit-print-color-adjust: exact;
  }
}
```

**Section Pagination:**
```css
@media print {
  .section {
    page-break-before: auto;
    page-break-after: auto;
    page-break-inside: avoid;
  }

  /* Prevent orphans and widows */
  h2, h3 {
    page-break-after: avoid;
  }

  .content-card,
  .metric-card {
    page-break-inside: avoid;
  }
}
```

**Hide Interactive Elements:**
```css
@media print {
  header,
  .section-dropdown,
  .back-to-top {
    display: none !important;
  }
}
```

### Print Quality Optimization

**Color Preservation:**
```css
/* Force color printing */
body {
  print-color-adjust: exact;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}

/* Ensure backgrounds print */
.slide,
.content-card,
.metric-card {
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
```

**Typography Adjustment:**
```css
@media print {
  /* Slightly smaller for print */
  body {
    font-size: 11pt;
  }

  h1 {
    font-size: 24pt;
  }

  h2 {
    font-size: 18pt;
  }

  h3 {
    font-size: 14pt;
  }
}
```

---

## Quality Validation

### Technical Validation Checklist

**HTML Validation:**
```javascript
// Pseudo-code for validation
function validateHTML(html) {
  const checks = {
    hasDoctype: html.startsWith('<!DOCTYPE html>'),
    hasLangAttribute: /<html[^>]*lang=/.test(html),
    hasViewport: /<meta[^>]*name="viewport"/.test(html),
    hasTitle: /<title>/.test(html),
    hasSemantic: /<(header|main|nav|article|section)/.test(html),
  };

  return Object.values(checks).every(check => check === true);
}
```

**CSS Validation:**
- All CSS variables defined
- No syntax errors
- Print styles present
- Responsive breakpoints configured
- Accessibility styles included

**JavaScript Validation:**
- Navigation functions defined
- Event listeners attached
- No console errors
- Keyboard shortcuts working
- Smooth scroll functional

### Content Validation Checklist

**Completeness Check:**
```javascript
function validateContent(content) {
  const required = {
    organization: ['name', 'brand_color', 'fiscal_year'],
    impact_overview: ['reach_metrics', 'momentum'],
    regional_portfolio: ['regions', 'strategic_priorities'],
    financial_performance: ['capital_overview', 'capital_mix', 'safeguards'],
    program_outcomes: ['pillars', 'evaluation_approach'],
    partnerships: ['statistics', 'partner_categories', 'flagship_partnerships'],
    strategic_outlook: ['roadmap', 'leadership_asks'],
  };

  // Check all required fields present
  // Check minimum array lengths
  // Check for placeholder text
  // Validate percentages total 100%
}
```

**Placeholder Detection:**
```javascript
const placeholderPatterns = [
  /\[Organization\]/gi,
  /\[Your Organization\]/gi,
  /\[Company Name\]/gi,
  /TODO/gi,
  /XXX/gi,
  /PLACEHOLDER/gi,
  /\[Year\]/gi,
];

function detectPlaceholders(text) {
  return placeholderPatterns.some(pattern => pattern.test(text));
}
```

### Accessibility Validation

**Automated Checks:**
- Contrast ratio validation
- ARIA attribute presence
- Semantic HTML structure
- Keyboard navigation functional
- Focus indicators visible
- Alt text on images (if any)
- Form labels present (if any)

**Manual Checks:**
- Screen reader testing (VoiceOver, NVDA, JAWS)
- Keyboard-only navigation
- High contrast mode compatibility
- Zoom to 200% readability
- Reduced motion respect

---

## Advanced Customization

### Logo Integration

**SVG Logo:**
```html
<div class="logo-container">
  <svg class="organization-logo" viewBox="0 0 100 100">
    <!-- User's logo SVG path -->
  </svg>
</div>
```

**CSS Styling:**
```css
.logo-container {
  position: absolute;
  top: 24px;
  right: 24px;
  width: 80px;
  height: 80px;
}

.organization-logo {
  width: 100%;
  height: 100%;
  fill: var(--brand-color);
}
```

### Custom Fonts

**Google Fonts:**
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
```

**CSS Override:**
```css
:root {
  --font-family: 'Montserrat', sans-serif;
}

body {
  font-family: var(--font-family);
}
```

### Layout Modifications

**Slide Dimensions:**
```css
.slide {
  width: 1200px;  /* Adjust width */
  height: 800px;  /* Adjust height */
  /* Maintain aspect ratio */
}
```

**Spacing Adjustments:**
```css
:root {
  --spacing-unit: 16px;
  --card-padding: calc(var(--spacing-unit) * 2);
  --section-gap: calc(var(--spacing-unit) * 4);
}
```

### Color Scheme Variants

**Light Mode (Advanced):**
```css
[data-theme="light"] {
  --bg-dark: #FFFFFF;
  --bg-card: #F5F5F5;
  --text-primary: #1A1A1A;
  --text-secondary: #666666;
}
```

**High Contrast Mode:**
```css
@media (prefers-contrast: high) {
  :root {
    --brand-color: #FFFF00;  /* High visibility yellow */
    --text-primary: #FFFFFF;
    --bg-dark: #000000;
  }
}
```

---

## Integration Patterns

### Google Sheets Integration

**Export to CSV:**
1. User maintains data in Google Sheets
2. Export sheet to CSV
3. Parse CSV into content schema
4. Generate reports

**Future: Direct API:**
```javascript
// Planned for v1.1
async function fetchFromGoogleSheets(sheetId, apiKey) {
  const url = `https://sheets.googleapis.com/v4/spreadsheets/${sheetId}/values/A1:Z1000?key=${apiKey}`;
  const response = await fetch(url);
  const data = await response.json();
  return parseSheetData(data.values);
}
```

### Airtable Integration

**Export to JSON:**
1. User maintains data in Airtable
2. Export base to JSON
3. Map Airtable fields to content schema
4. Generate reports

**Future: Direct API:**
```javascript
// Planned for v1.1
async function fetchFromAirtable(baseId, apiKey) {
  const url = `https://api.airtable.com/v0/${baseId}/Impact%20Data`;
  const response = await fetch(url, {
    headers: { 'Authorization': `Bearer ${apiKey}` }
  });
  const data = await response.json();
  return parseAirtableRecords(data.records);
}
```

### CMS Integration

**Headless CMS (Contentful, Strapi):**
1. Define content model matching schema
2. Fetch content via API
3. Transform to content schema
4. Generate reports automatically

---

## Performance Optimization

### File Size Optimization

**Current Size:**
- Presentation HTML: ~180KB
- Executive HTML: ~190KB
- Combined: ~370KB

**Optimization Strategies:**
- Inline critical CSS only
- Defer non-critical JavaScript
- Minify HTML/CSS/JS in production
- Use system fonts as fallback
- Optimize SVG assets

### Load Time Optimization

**Critical Rendering Path:**
1. HTML parsing (< 50ms)
2. CSS parsing and rendering (< 100ms)
3. JavaScript execution (< 50ms)
4. Font loading (< 200ms with display=swap)
5. Total: < 400ms (excluding network)

**Lazy Loading (Future):**
```javascript
// For executive format with many sections
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      loadSectionContent(entry.target);
    }
  });
});
```

---

## Troubleshooting Guide

### Common Issues and Solutions

**Issue: Brand color not applying**
- Check hex format: `#RRGGBB` (6 characters)
- Verify CSS variable updated
- Clear browser cache
- Inspect element to check computed styles

**Issue: Content overflowing slides**
- Reduce text length
- Use bullet points instead of paragraphs
- Move detailed content to executive format
- Adjust font size (advanced)

**Issue: Print layout broken**
- Use Chrome browser (most consistent)
- Check orientation setting
- Enable background graphics
- Verify page break CSS

**Issue: Navigation not working**
- Check JavaScript console for errors
- Verify `data-slide` attributes sequential
- Test in different browser
- Check event listeners attached

---

## Future Enhancements

### Roadmap

**v1.1 (Q1 2026):**
- Google Sheets direct integration
- Airtable integration
- Multiple brand themes
- Logo integration wizard

**v1.2 (Q2 2026):**
- Interactive charts (Chart.js)
- Real-time data connections
- Version history tracking
- Collaboration features

**v2.0 (Q3-Q4 2026):**
- AI-generated narratives
- Content optimization suggestions
- Multi-language support
- Advanced analytics

---

## Conclusion

This implementation guide provides comprehensive technical documentation for understanding, using, and extending the Executive Impact Presentation Generator skill.

For additional support:
- **SKILL.md** - Operational specification
- **README.md** - Overview and quick start
- **EXAMPLES.md** - Real-world case studies
- **QUICK-START.md** - 5-minute onboarding

**Questions?** Ask Claude for detailed explanations of any section or component.
