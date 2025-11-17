# Static Impact Report Template

**Fixed slide sizes, presentation-optimized, no scrolling**

## When to Use This Template

✅ **Perfect for:**
- Board presentations
- Executive briefings
- Investor decks
- Time-limited reviews (15-30 min)
- PDF export as primary deliverable
- Concise, high-level summaries

❌ **Not ideal for:**
- Detailed data-heavy reports
- Long-form content
- Web-first distribution
- Content that requires scrolling

---

## Key Features

### Slide Structure

**6 Content Slides:**
1. Impact Measurement (3 columns)
2. Partnership Ecosystem (stats + 2 columns)
3. Financial Overview (stats + 3 columns)
4. Program Outcomes (2 columns)
5. Strategic Priorities (3 columns)
6. Forward Outlook (2 columns)

### Fixed Dimensions

```css
.slide-container {
    min-height: 650px; /* Fixed height */
    overflow: hidden;   /* No scrolling */
}
```

**This means:**
- Content MUST fit within viewport
- Maximum vertical space used efficiently
- Predictable layout across devices
- Clean PDF export every time

---

## Content Limits

### Per Slide

| Layout | Max Items | Description Length |
|--------|-----------|-------------------|
| Three columns | 3 items per column | 10-15 words |
| Two columns | 4 items per column | 15-20 words |
| Stats row | 3 metrics | 2-5 word descriptions |

### Typography Hierarchy

```
Slide title:      3rem (48px) - One line maximum
Slide description: 1.125rem (18px) - 15-25 words
Column title:     0.95rem (15px) - ALL CAPS
Metric value:     3.5rem (56px) - Large numbers
Outcome title:    0.95rem (15px) - 3-6 words
Outcome text:     0.875rem (14px) - 10-15 words
```

---

## Quick Customization

### 1. Update Branding (2 minutes)

```html
<!-- Line 555: Organization name -->
<div class="org-name">360 Social Impact Studios</div>
<!-- Change to: -->
<div class="org-name">Your Organization</div>

<!-- Line 556: Report subtitle -->
<div class="report-subtitle">Executive Impact Report FY 2025</div>
<!-- Change to: -->
<div class="report-subtitle">Your Report Title</div>
```

### 2. Change Accent Color (1 minute)

```css
/* Line 29: Find this in <style> */
--accent-orange: #ff6b35;
/* Change to your brand color: */
--accent-orange: #your-hex-color;
```

**Test contrast:** Must be 4.5:1 against `#0a0e1a` background

### 3. Update Dropdown Menu (5 minutes)

```html
<!-- Lines 562-569: Update each option -->
<select id="pageSelect" onchange="goToPage(this.value)">
    <option value="1">1. Your Slide Title</option>
    <option value="2">2. Your Slide Title</option>
    <!-- etc. -->
</select>
```

---

## Layout Patterns

### Pattern 1: Three Columns with Metrics

**Use for:** Slide 1 (Impact Measurement), Slide 3 (Financial Overview), Slide 5 (Strategic Priorities)

```html
<div class="three-column">
    <div class="column-card">
        <div class="column-header">
            <h3 class="column-title">COLUMN TITLE</h3>
            <span class="pillar-tag">CATEGORY</span>
        </div>
        <div class="metric-label">METRIC LABEL</div>
        <div class="metric-value">847K</div>
        <div class="metric-change">+41% from FY 2024</div>

        <ul class="outcome-list">
            <li class="outcome-item">
                <div class="outcome-bullet"></div>
                <div class="outcome-content">
                    <h4>Outcome title</h4>
                    <p>Brief description in 10-15 words maximum.</p>
                </div>
            </li>
            <!-- 2-3 more items -->
        </ul>
    </div>
    <!-- 2 more column-cards -->
</div>
```

**Limits:**
- Exactly 3 columns
- 3-4 items per column max
- Metric + 3 outcomes = ideal

---

### Pattern 2: Stats Row + Two Columns

**Use for:** Slide 2 (Partnership Ecosystem)

```html
<!-- Stats row first -->
<div class="stats-row">
    <div class="stat-card">
        <div class="stat-label">STAT LABEL</div>
        <div class="stat-value">142</div>
        <div class="stat-description">Brief context</div>
    </div>
    <!-- 2 more stat-cards -->
</div>

<!-- Then two columns -->
<div class="two-column">
    <div class="column-card">
        <!-- Column content -->
    </div>
    <div class="column-card">
        <!-- Column content -->
    </div>
</div>
```

**Limits:**
- Exactly 3 stats
- 4 items per column max
- Descriptions 2-5 words

---

### Pattern 3: Two Columns Only

**Use for:** Slide 4 (Program Outcomes), Slide 6 (Forward Outlook)

```html
<div class="two-column">
    <div class="column-card">
        <div class="column-header">
            <h3 class="column-title">LEFT COLUMN</h3>
            <span class="pillar-tag">CATEGORY</span>
        </div>

        <ul class="outcome-list">
            <li class="outcome-item">
                <div class="outcome-bullet"></div>
                <div class="outcome-content">
                    <h4>Item title</h4>
                    <p>Description up to 20 words for two-column layout.</p>
                </div>
            </li>
            <!-- 3-4 more items -->
        </ul>
    </div>
    <!-- Second column-card -->
</div>
```

**Limits:**
- Exactly 2 columns
- 4 items per column max
- Slightly longer descriptions allowed

---

## Component Reference

### Metric Display

```html
<div class="metric-label">YOUR METRIC LABEL</div>
<div class="metric-value">123K</div>
<div class="metric-change">+15% from last year</div>
```

**Format numbers:**
- `847,234` → `847K`
- `1,234,567` → `1.2M`
- `$42,000,000` → `$42M`

### Status Badges

```html
<!-- Green "expanded" badge -->
<h4>Partnership Name <span class="status-badge expanded">✓ EXPANDED</span></h4>

<!-- Blue "new" badge -->
<h4>Partnership Name <span class="status-badge new">✓ NEW</span></h4>
```

**Use sparingly:** 1-2 per slide maximum

### Pillar Tags

```html
<span class="pillar-tag">PRIMARY PILLAR</span>
<span class="pillar-tag">BY TYPE</span>
<span class="pillar-tag">HIGHLIGHTED</span>
```

**Style:** Muted gray, subtle, categorization only

---

## Navigation

### Available Methods

1. **Arrow Keys:** `←` previous, `→` next
2. **Dot Indicators:** Click any dot to jump to slide
3. **Dropdown Menu:** Select slide from list
4. **Buttons:** `‹` and `›` buttons in footer

### JavaScript Functions

```javascript
// Available globally
nextSlide()      // Go to next slide
previousSlide()  // Go to previous slide
goToPage(num)    // Jump to specific slide (1-6)
```

### Initialization

```javascript
let currentSlide = 1;         // Starting slide
const totalSlides = 6;        // Total slides

initDots();   // Create dot indicators
updateSlide(); // Set initial state
```

---

## PDF Export

### Recommended Process

1. **Open in Chrome** (best rendering)
2. Press `Cmd+P` (Mac) or `Ctrl+P` (Windows)
3. **Destination:** Save as PDF
4. **Layout:** Landscape
5. **Paper size:** Letter or A4
6. **Margins:** Default
7. **Options:** ✓ Background graphics
8. Click **Save**

### Result

- **Pages:** 6 (one per slide)
- **Orientation:** Landscape
- **Content:** All slides print on separate pages
- **Quality:** High-resolution, print-ready

### Before Exporting

- [ ] All content fits within slides (no scrolling)
- [ ] Metrics formatted consistently
- [ ] No placeholder text remaining
- [ ] Brand color looks good
- [ ] Test print preview first

---

## Responsive Behavior

### Desktop (>1200px)
- Three columns side-by-side
- Full typography scale
- Optimized for presentation

### Tablet (768px - 1200px)
- Three columns stack vertically
- Slightly reduced font sizes
- Stats row may wrap

### Mobile (<768px)
- All content stacks
- Further font reduction
- Simplified navigation (no dots)

**Primary target:** Desktop presentation (1400px - 1920px)

---

## Troubleshooting

### Content Overflows Slide

**Problem:** Content extends past visible area

**Solutions:**
1. Remove one outcome item per column
2. Shorten descriptions to 10-12 words
3. Remove stats row (if present)
4. Split content across two slides

### Three Columns Too Cramped

**Problem:** Columns feel crowded

**Solutions:**
1. Switch to two-column layout
2. Reduce to 3 items per column (instead of 4)
3. Shorten outcome descriptions
4. Remove pillar tags if not essential

### Metrics Don't Fit

**Problem:** Large metric values overlap

**Solutions:**
1. Use abbreviated format (847K not 847,234)
2. Reduce font size in CSS (not recommended)
3. Use two columns instead of three
4. Simplify metric labels

### Navigation Broken

**Problem:** Slides don't advance

**Check:**
1. Browser console for JavaScript errors
2. `data-slide` attributes are `1, 2, 3, 4, 5, 6`
3. `totalSlides` variable is `6`
4. No duplicate slide numbers

---

## Performance

### Load Time
- **CSS:** Inline (no external requests)
- **Fonts:** Google Fonts CDN (~50KB)
- **JavaScript:** Inline (~2KB)
- **Total:** < 100KB (very fast)

### Rendering
- **CSS Grid:** Modern, efficient layouts
- **Transitions:** Hardware-accelerated
- **Animations:** Minimal, performant
- **No dependencies:** Pure HTML/CSS/JS

### Optimization Tips
- Pre-connect to fonts.googleapis.com (already included)
- Consider self-hosting Inter font for offline use
- Minify HTML for production (optional)
- Use image compression if adding logos

---

## Accessibility Checklist

- [x] Semantic HTML (`<header>`, `<main>`, `<article>`)
- [x] Proper heading hierarchy (h1 → h3 → h4)
- [x] ARIA labels on interactive elements
- [x] Keyboard navigation support
- [x] Color contrast: 4.5:1 minimum
- [x] Focus states visible
- [x] No keyboard traps

### Testing

```bash
# Manual tests
1. Tab through all interactive elements
2. Use arrow keys for navigation
3. Test with screen reader (NVDA/JAWS)
4. Verify in Chrome Lighthouse (Accessibility score)
```

---

## Version History

### v2.0 (Current)
- Fixed slide size optimization
- Improved responsive behavior
- Enhanced print styles
- Added accessibility features
- Refined content limits

### v1.0
- Initial static template
- Basic slide navigation
- Three layout patterns

---

## File Information

- **Filename:** `executive-impact-report-static.html`
- **Size:** ~75KB (unminified)
- **Lines:** ~1,200
- **Dependencies:** Google Fonts (Inter)
- **Browser Support:** Modern browsers (Chrome, Firefox, Safari, Edge)

---

## Quick Reference Card

```
SLIDE STRUCTURE
├─ 1. Impact Measurement     [3 col, metrics]
├─ 2. Partnership Ecosystem   [stats + 2 col]
├─ 3. Financial Overview      [stats + 3 col]
├─ 4. Program Outcomes        [2 col]
├─ 5. Strategic Priorities    [3 col]
└─ 6. Forward Outlook         [2 col]

CONTENT LIMITS
├─ Three columns: 3 items × 10-15 words
├─ Two columns:   4 items × 15-20 words
├─ Stats row:     3 metrics × 2-5 words
└─ Slide description: 15-25 words

NAVIGATION
├─ Arrow keys:   ← →
├─ Dot clicks:   Jump to slide
├─ Dropdown:     Select from menu
└─ Keyboard:     Tab for focus

CUSTOMIZATION
├─ Org name:     Line 555
├─ Accent color: Line 29 (CSS)
├─ Dropdown:     Lines 562-569
└─ Content:      Lines 579+ (slides)

EXPORT
├─ Chrome → Cmd/Ctrl+P
├─ Landscape orientation
├─ Background graphics ON
└─ Save as PDF (6 pages)
```

---

**Template Type:** Static (Fixed Slides)
**Version:** 2.0
**Last Updated:** November 2025
**Optimized For:** Presentations & PDF Export
