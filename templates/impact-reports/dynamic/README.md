# Dynamic Impact Report Template

**Flexible content, scrolling enabled, web-optimized**

## When to Use This Template

✅ **Perfect for:**
- Annual reports
- Comprehensive reviews
- Detailed portfolio presentations
- Web-first distribution
- Interactive online viewing
- Reports with extensive data

❌ **Not ideal for:**
- Time-limited presentations
- Print-primary deliverables
- Simple executive summaries
- Bandwidth-constrained environments

---

## Key Features

### Slide Structure

**7 Total Slides:**
0. Cover Page (with CTA)
1. Impact and Outcomes (executive overview)
2. Impact by Region (portfolio view)
3. Financial Performance (capital & efficiency)
4. Program Outcomes (impact measurement)
5. Partnership Ecosystem (collaborative impact)
6. Looking Forward (strategic outlook)

### Flexible Layout

```css
.slides-container {
    min-height: 70vh; /* Minimum height */
    /* No max-height - can scroll */
}
```

**This means:**
- Content can exceed viewport
- Scrolling within slides allowed
- More data per slide possible
- Responsive to content needs

---

## Key Differences from Static

| Feature | Static | Dynamic |
|---------|--------|---------|
| **Slides** | 6 content | Cover + 6 content |
| **Scrolling** | No | Yes |
| **Content density** | Limited | Flexible |
| **Best for** | Presentations | Web viewing |
| **PDF export** | Excellent | Good |
| **Cover page** | No | Yes |
| **Navigation** | Basic | Enhanced |
| **LocalStorage** | No | Yes (remembers position) |

---

## Content Capacity

### Per Slide

| Layout | Max Items | Description Length |
|--------|-----------|-------------------|
| Three columns | 4-6 items per column | 15-25 words |
| Two columns | 5-7 items per column | 20-30 words |
| Stats row | 3 metrics | 5-10 word descriptions |
| Tables | Full data tables | No strict limits |

### Typography Hierarchy

```
Cover title:      3.5rem (56px) - Statement piece
Page title:       2.25rem (36px) - Clear hierarchy
Page subtitle:    1.125rem (18px) - Context setting
Card title:       1.125rem (18px) - Section headers
Metric value:     1.875-2.25rem (30-36px) - Large but not overwhelming
List title:       1rem (16px) - Clear readability
List description: 0.875rem (14px) - Detail level
```

---

## Quick Customization

### 1. Update Branding (3 minutes)

```html
<!-- Header: Organization name -->
<div class="org-name">360 Social Impact Studios</div>
<!-- Change to: -->
<div class="org-name">Your Organization</div>

<!-- Header: Report title -->
<h1 class="report-title">FY 2025 Impact Report · Executive Edition</h1>
<!-- Change to: -->
<h1 class="report-title">Your Report Title</h1>

<!-- Cover page: Organization name -->
<div class="cover-org-name">360 Social Impact Studios</div>
<!-- Change to: -->
<div class="cover-org-name">Your Organization</div>
```

### 2. Change Brand Colors (2 minutes)

```css
/* Find in <style> :root section */
--brand-orange: #FF6B35;  /* Primary accent */
--brand-teal: #00D9C0;    /* Secondary accent */

/* Change to your colors: */
--brand-orange: #your-primary-hex;
--brand-teal: #your-secondary-hex;
```

**Where colors appear:**
- `brand-orange`: Buttons, bullets, hover states, badges
- `brand-teal`: Highlight text accents, secondary elements

### 3. Update View Selector (5 minutes)

```html
<!-- In header -->
<select class="view-selector" id="viewSelect">
    <option value="0">Cover</option>
    <option value="1">1. Your Slide Title</option>
    <option value="2">2. Your Slide Title</option>
    <!-- etc. -->
</select>
```

---

## Layout Patterns

### Pattern 1: Cover Page

**Use for:** Slide 0 (required)

```html
<article class="slide active" id="slide0" data-slide="0">
    <div class="cover-page">
        <div class="cover-logo" aria-hidden="true">
            <!-- Logo SVG or image -->
        </div>

        <div class="cover-org-name">Organization Name</div>
        <h1 class="cover-title">Report Title</h1>
        <div class="cover-subtitle">Fiscal Year</div>

        <div class="cover-meta">
            <div class="cover-meta-item">
                <div class="cover-meta-label">Label</div>
                <div class="cover-meta-value">Value</div>
            </div>
            <!-- More meta items -->
        </div>

        <div class="cover-cta">
            <button class="btn-start" onclick="goToSlide(1)">
                Begin Report →
            </button>
        </div>
    </div>
</article>
```

**Styling:**
- Gradient background with subtle animation
- Centered layout
- Call-to-action button
- Metadata display

---

### Pattern 2: Content Grid with Cards

**Use for:** Most content slides

```html
<article class="slide" id="slide1" data-slide="1">
    <!-- Page meta badges -->
    <div class="page-meta">
        <span class="badge">
            <span class="badge-dot" style="color: var(--brand-teal);"></span>
            Category
        </span>
        <span class="page-number">Page 1 of 6</span>
    </div>
    <p class="page-hint">Optional hint text for users</p>

    <!-- Section header -->
    <div class="section-label">SECTION CATEGORY</div>
    <h2 class="page-title">Page Title</h2>
    <p class="page-subtitle">Descriptive subtitle in one sentence.</p>

    <!-- Content cards -->
    <div class="card">
        <div class="card-header">
            <h3 class="card-title">Card Title</h3>
            <span class="card-label">Label</span>
        </div>

        <!-- Card content: metrics, lists, etc. -->
    </div>
</article>
```

---

### Pattern 3: Region Grid

**Use for:** Slide 2 (Impact by Region)

```html
<div class="region-grid">
    <div class="region-card">
        <div class="region-name">Latin America</div>
        <div class="region-percentage">36%</div>
        <div class="region-description">
            Brief description of regional activities and focus.
        </div>
    </div>
    <!-- 5 more region cards -->
</div>
```

**Styling:**
- Gradient background per card
- Hover effect (raise on hover)
- Large percentage display
- Responsive (3 → 2 → 1 columns)

---

### Pattern 4: Data Table

**Use for:** Slide 3 (Financial Performance)

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
            <td>Total capital under active management this year.</td>
        </tr>
        <!-- More rows -->
    </tbody>
</table>
```

**Styling:**
- Rounded corners
- Subtle borders
- Header row styled distinctly
- First column bold

---

### Pattern 5: Highlight Text

**Use for:** Emphasis and key takeaways

```html
<p class="highlight-text">
    This year we delivered <span class="accent">measurable, compounding value</span>
    across our ecosystem while preserving a disciplined approach to risk and inclusion.
</p>
```

**Styling:**
- Gradient background
- Orange left border
- Larger text (1.125rem)
- `.accent` class uses teal color

---

## Component Reference

### Metric Groups

```html
<div class="metric-group">
    <div class="metric-label">Lives Impacted</div>
    <div class="metric-value large">1.8M</div>
    <div class="metric-description">
        Individuals reached across programs in health, skills, and income generation.
    </div>
</div>
```

**Sizes:**
- `metric-value`: 1.875rem (default)
- `metric-value large`: 2.25rem (for emphasis)

### Content Lists

```html
<ul class="content-list">
    <li class="list-item">
        <span class="list-marker"></span>
        <div class="list-content">
            <div class="list-title">Title with optional <span style="color: var(--status-success);">▲ badge</span></div>
            <div class="list-description">Detailed description text here.</div>
        </div>
    </li>
    <!-- More items -->
</ul>
```

**Status Colors:**
- `--status-success`: #10b981 (green)
- `--status-warning`: #f59e0b (amber)
- `--status-info`: #3b82f6 (blue)

### Page Meta Badges

```html
<div class="page-meta">
    <span class="badge">
        <span class="badge-dot" style="color: var(--brand-teal);"></span>
        FY 2025
    </span>
    <span class="badge">
        <span class="badge-dot" style="color: var(--brand-orange);"></span>
        Category
    </span>
    <span class="page-number">Page X of 6</span>
</div>
```

---

## Navigation

### Available Methods

1. **Arrow Keys:** `←` / `→` for prev/next
2. **Page Keys:** `PageUp` / `PageDown`
3. **Home/End:** Jump to first/last slide
4. **Dot Indicators:** Click to jump (labeled C, 1, 2, 3, 4, 5, 6)
5. **View Selector:** Dropdown in header
6. **Navigation Buttons:** `‹` and `›` in footer

### Enhanced Features

**LocalStorage Persistence:**
```javascript
// Remembers last viewed slide
// Returns to same slide on page reload
localStorage.setItem('360_impact_current_slide', slideNumber);
```

**Transition Lock:**
```javascript
// Prevents rapid slide changes
state.isTransitioning = true;
setTimeout(() => { state.isTransitioning = false; }, 300);
```

### JavaScript API

```javascript
// Available globally
goToSlide(num)  // Jump to slide 0-6
// Internal functions
showSlide(num)      // Core navigation
updateNavigation()  // Sync UI state
```

---

## PDF Export

### Process

1. **Open in Chrome**
2. Press `Cmd+P` / `Ctrl+P`
3. **Destination:** Save as PDF
4. **Layout:** Landscape
5. **Paper:** Letter or A4
6. **Margins:** Default
7. **Options:** ✓ Background graphics
8. Click **Save**

### Result

- **Pages:** 7 (cover + 6 content)
- **Quality:** High-resolution
- **Colors:** Accurate rendering
- **Content:** All slides on separate pages

### Considerations

⚠️ **Dynamic template and PDF:**
- Scrolling content may span pages
- Tables might break across pages
- Cover page renders well
- Best for web viewing (PDF is secondary)

**For PDF-primary:** Consider using static template instead.

---

## Responsive Behavior

### Desktop (>1024px)
- Full feature set
- All navigation options
- Optimized layout

### Tablet (768px - 1024px)
- Region grid: 2 columns
- Content grids: stack to 1 column
- Navigation dots hidden
- Simplified footer

### Mobile (<768px)
- All content stacks vertically
- Navigation dots hidden
- Header wraps
- Cover page simplified

**Primary target:** Desktop/tablet web viewing

---

## BUG FIX: Initialization Issue

### Problem (v1.0)

Multiple slides had `class="active"` in HTML:
- Cover page: `<article class="slide active">`
- Slide 1: `<article class="slide active">`

**Result:** Both showed on load, causing scroll/overlap.

### Solution (v2.0)

Added explicit cleanup in `init()` function:

```javascript
function init() {
    // CRITICAL BUG FIX: Remove ALL active classes first
    slides.forEach(slide => {
        slide.classList.remove('active');
    });

    // Now set correct slide
    showSlide(state.currentSlide);
}
```

**Result:** Only one slide shows, regardless of HTML state.

---

## Accessibility

### Enhancements Over Static

- **Skip link:** Jump to main content
- **ARIA landmarks:** `role="banner"`, `role="main"`, `role="navigation"`
- **ARIA live regions:** For navigation state changes
- **Tab list pattern:** Dot navigation uses proper ARIA
- **Semantic articles:** Each slide is `<article>`

### Screen Reader Support

```html
<button aria-label="Previous slide">‹</button>
<button role="tab" aria-selected="true">1</button>
<select aria-label="Select view">...</select>
```

### Keyboard Navigation

All interactive elements accessible via:
- Tab/Shift+Tab
- Arrow keys
- Enter/Space
- Home/End/PageUp/PageDown

---

## Performance

### Load Time
- **CSS:** Inline (~15KB)
- **Fonts:** Google Fonts CDN (~50KB)
- **JavaScript:** Inline (~4KB)
- **Total:** ~75KB (very fast)

### Runtime
- **State management:** Minimal overhead
- **Transitions:** CSS-based (GPU accelerated)
- **LocalStorage:** Async, non-blocking
- **Event listeners:** Delegated where possible

### Optimization Tips

1. **Font loading:**
   ```html
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   ```
   ✅ Already included

2. **Consider self-hosting fonts** for offline/intranet use

3. **Minify for production:**
   ```bash
   # Optional - reduces file size by ~30%
   html-minifier --collapse-whitespace --remove-comments input.html -o output.html
   ```

---

## Advanced Customization

### Adding a New Slide

1. **Copy existing slide HTML**
2. **Update `data-slide` attribute** (increment number)
3. **Update JavaScript:**
   ```javascript
   const state = {
       totalSlides: 8,  // Was 7, now 8
   };
   ```
4. **Add to navigation:**
   ```html
   <!-- View selector -->
   <option value="7">7. Your New Slide</option>

   <!-- Nav dots -->
   <button class="nav-dot" data-slide="7">7</button>
   ```

### Removing a Slide

1. **Delete slide HTML block**
2. **Update JavaScript:**
   ```javascript
   const state = {
       totalSlides: 6,  // Was 7, now 6
   };
   ```
3. **Update navigation** (remove from selector and dots)

### Custom Color Scheme

```css
:root {
    /* Override these */
    --brand-orange: #your-primary;
    --brand-teal: #your-secondary;

    /* Optionally customize backgrounds */
    --bg-app: #your-darkest;
    --bg-primary: #your-medium;
    --bg-elevated: #your-lightest;
}
```

**Test thoroughly:** Ensure contrast ratios maintained.

---

## Troubleshooting

### Multiple Slides Showing

**Problem:** Cover and Slide 1 both visible

**Solution:** Already fixed in v2.0 - `init()` removes all `.active` classes first.

### LocalStorage Not Working

**Problem:** Slide position not remembered

**Check:**
1. Browser allows localStorage
2. Not in private/incognito mode
3. No browser extensions blocking

**Test:**
```javascript
localStorage.setItem('test', '1');
console.log(localStorage.getItem('test')); // Should log '1'
```

### Navigation Dots Not Updating

**Problem:** Dots don't reflect current slide

**Check:**
1. `data-slide` attributes are `0, 1, 2, 3, 4, 5, 6`
2. `state.totalSlides` is `7`
3. No JavaScript errors in console

### Content Overflows Badly

**Problem:** Content extends way past viewport

**Solutions:**
1. This template allows scrolling (expected)
2. If too much, split across two slides
3. Remove less critical content
4. Use more concise language

---

## Version History

### v2.0 (Current)
- ✅ Fixed initialization bug (multiple active slides)
- ✅ Enhanced accessibility (ARIA, skip links)
- ✅ LocalStorage persistence
- ✅ Improved responsive design
- ✅ Better print styles

### v1.0
- Initial dynamic template
- Cover page + 6 content slides
- Basic navigation
- ⚠️ Had initialization bug

---

## File Information

- **Filename:** `executive-impact-report-dynamic.html`
- **Size:** ~85KB (unminified)
- **Lines:** ~1,400
- **Dependencies:** Google Fonts (Inter)
- **Browser Support:** Modern browsers (ES6+, CSS Grid)

---

## Quick Reference Card

```
SLIDE STRUCTURE
├─ 0. Cover Page              [Hero layout]
├─ 1. Impact at a glance      [Cards + metrics]
├─ 2. Impact by region        [Region grid]
├─ 3. Financial performance   [Table + metrics]
├─ 4. Program outcomes        [3-column cards]
├─ 5. Partnership ecosystem   [Metrics + lists]
└─ 6. Looking forward         [2-column cards]

CONTENT CAPACITY
├─ Three columns: 4-6 items × 15-25 words
├─ Two columns:   5-7 items × 20-30 words
├─ Stats row:     3 metrics × 5-10 words
├─ Tables:        No strict limits
└─ Cover meta:    3-4 items

NAVIGATION
├─ Arrow keys:    ← →
├─ Page keys:     PageUp PageDown
├─ Home/End:      First/last slide
├─ Dot clicks:    Jump to slide (C,1-6)
├─ View selector: Dropdown in header
└─ LocalStorage:  Remembers position

CUSTOMIZATION
├─ Org name:      Header + cover page
├─ Brand colors:  :root CSS variables
├─ View selector: <select> in header
└─ Content:       Slides 0-6

EXPORT
├─ Chrome → Cmd/Ctrl+P
├─ Landscape orientation
├─ Background graphics ON
└─ Save as PDF (7 pages)

BUG FIX v2.0
└─ init() now removes all .active classes first
   (fixes multiple slides showing on load)
```

---

**Template Type:** Dynamic (Flexible Content)
**Version:** 2.0
**Last Updated:** November 2025
**Optimized For:** Web Viewing & Interactive Reports
