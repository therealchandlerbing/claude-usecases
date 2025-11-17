# Executive Impact Report Templates

Professional, accessible HTML templates for creating executive-level impact reports with slide-based navigation.

## 📋 Quick Overview

This template system provides two production-ready variants:

| Template | Use Case | Best For |
|----------|----------|----------|
| **Static** | Fixed slide sizes, no scrolling | Presentations, board meetings, PDF export |
| **Dynamic** | Flexible content, with scrolling | Detailed reports, web viewing, comprehensive data |

Both templates share:
- ✅ Clean dark theme with customizable accent colors
- ✅ Responsive design (desktop, tablet, mobile)
- ✅ Keyboard navigation (arrow keys)
- ✅ Print-friendly PDF export
- ✅ Accessibility (WCAG AA compliant)
- ✅ Zero dependencies (pure HTML/CSS/JS)

---

## 🚀 Quick Start

### 1. Choose Your Template

**Static Template** (`static/executive-impact-report-static.html`)
```
✓ Fixed viewport slides (no scrolling)
✓ 6 content slides
✓ Optimized for presentations
✓ Best for concise, high-level summaries
```

**Dynamic Template** (`dynamic/executive-impact-report-dynamic.html`)
```
✓ Flexible content length
✓ Cover page + 6 content slides
✓ Can accommodate detailed data
✓ Best for comprehensive reports
```

### 2. Basic Customization

```html
<!-- Change organization name -->
<div class="org-name">Your Organization</div>

<!-- Change accent color (in CSS :root) -->
--accent-orange: #yourcolor; /* or --brand-orange for dynamic */

<!-- Update slide content -->
<div class="metric-value">Your Value</div>
```

### 3. Export to PDF

1. Open template in Chrome
2. Press `Cmd/Ctrl + P`
3. Select "Save as PDF"
4. Choose "Landscape" orientation
5. Save

---

## 📁 Directory Structure

```
impact-reports/
├── README.md                    # This file
├── static/
│   ├── executive-impact-report-static.html
│   └── README.md               # Static template docs
├── dynamic/
│   ├── executive-impact-report-dynamic.html
│   └── README.md               # Dynamic template docs
├── components/
│   ├── README.md               # Component library
│   └── examples/               # Reusable code snippets
└── docs/
    ├── customization-guide.md
    ├── visual-design-guide.md
    └── troubleshooting.md
```

---

## 🎨 Template Comparison

### Static Template Features

**Layout:**
- 6 slides with fixed height containers
- No scrolling within slides
- Content must fit viewport
- Optimized for 1400px max-width

**Navigation:**
- Arrow keys (← →)
- Dot indicators
- Page dropdown selector
- Direct slide jump

**Content Limits:**
- 3-4 bullet points per column
- Concise descriptions (10-15 words)
- Maximum 3 columns per slide
- Stats row: 3 metrics

**Best Use Cases:**
- Board presentations
- Executive summaries
- Investor decks
- Quick overviews
- Time-constrained reviews

---

### Dynamic Template Features

**Layout:**
- 7 slides (cover + 6 content)
- Flexible height (scrolling allowed)
- Can accommodate more data
- Cover page with CTA

**Navigation:**
- Same as static + Home/End keys
- Numbered dot navigation
- localStorage persistence
- Breadcrumb navigation

**Content Limits:**
- 4-6 bullet points per column
- Longer descriptions allowed
- Tables and detailed metrics
- Region cards and complex grids

**Best Use Cases:**
- Annual reports
- Comprehensive reviews
- Detailed portfolios
- Strategic planning docs
- Web-first distribution

---

## 🛠 Customization Options

### Brand Colors

**Static Template:**
```css
:root {
    --accent-orange: #ff6b35; /* Change this */
}
```

**Dynamic Template:**
```css
:root {
    --brand-orange: #FF6B35;  /* Primary accent */
    --brand-teal: #00D9C0;    /* Secondary accent */
}
```

**Recommended Colors by Sector:**
- **Nonprofit:** #FF6B35 (warm orange)
- **Healthcare:** #22C55E (medical green) or #3B82F6 (calm blue)
- **Environment:** #10B981 (earth green)
- **Finance:** #0052CC (professional blue)
- **Education:** #8B5CF6 (academic purple)
- **Technology:** #06B6D4 (tech cyan)

### Logo Integration

```html
<!-- Replace gradient logo with image -->
<div class="logo">
    <img src="your-logo.png" alt="Logo"
         style="width: 100%; height: 100%; object-fit: contain;">
</div>
```

### Content Structure

See `components/README.md` for reusable HTML snippets:
- Three-column layouts
- Two-column layouts
- Stats rows
- Metric displays
- Bullet lists
- Status badges
- Region cards

---

## 📊 Content Guidelines

### Metrics Formatting

```
Raw Number → Formatted
-----------------------
847,234    → 847K
1,234,567  → 1.2M
$42,123,456 → $42M
0.342      → 34%
```

### Text Length Limits

| Element | Character Limit | Recommendation |
|---------|-----------------|----------------|
| Slide title | 3-5 words | Be concise |
| Slide description | 15-25 words | One sentence |
| Metric label | 2-4 words | ALL CAPS |
| Outcome title | 3-6 words | Title Case |
| Outcome description | 10-20 words | One clear sentence |
| Stat description | 2-5 words | Context only |

### Writing Tips

**Do:**
- Use active voice
- Include specific metrics
- Provide context for numbers
- Keep sentences short
- Focus on outcomes, not activities

**Don't:**
- Use jargon without explanation
- Include vague statements
- Write long paragraphs
- Mix tenses
- Over-qualify numbers

---

## ♿ Accessibility Features

Both templates include:

- **Semantic HTML:** Proper heading hierarchy (h1, h2, h3, h4)
- **ARIA labels:** Screen reader support for navigation
- **Keyboard navigation:** Full keyboard control
- **Color contrast:** WCAG AA compliant (4.5:1 minimum)
- **Focus states:** Visible focus indicators
- **Skip links:** Jump to main content
- **Reduced motion:** Respects prefers-reduced-motion

**Testing Tools:**
- Chrome Lighthouse (Accessibility score)
- WAVE Browser Extension
- axe DevTools
- Keyboard-only navigation test

---

## 🖨 PDF Export Best Practices

### Recommended Settings

```
Browser: Chrome (best rendering)
Orientation: Landscape
Paper size: Letter or A4
Margins: Default
Background graphics: ON
Print headers/footers: OFF
```

### Before Exporting

- [ ] Review all slides for content overflow
- [ ] Check that all metrics are visible
- [ ] Verify color contrast acceptable for print
- [ ] Test print preview first
- [ ] Ensure proper page breaks

### Static vs Dynamic for PDF

**Static Template:**
- ✅ Designed for PDF export
- ✅ Fixed slide sizes
- ✅ Predictable page breaks
- ✅ No scrolling issues

**Dynamic Template:**
- ⚠️ Content may span pages
- ⚠️ Scrolling sections problematic
- ✅ Still exports cleanly
- 💡 Best for web viewing

---

## 🌐 Browser Support

| Browser | Version | Support |
|---------|---------|---------|
| Chrome | Latest 2 | ✅ Full |
| Firefox | Latest 2 | ✅ Full |
| Safari | Latest 2 | ✅ Full |
| Edge | Latest 2 | ✅ Full |
| Mobile Safari | iOS 14+ | ✅ Full |
| Chrome Mobile | Android 10+ | ✅ Full |

**Notes:**
- IE11 not supported (uses CSS Grid, modern JS)
- Templates use ES6+ JavaScript
- CSS custom properties (variables) required
- No polyfills included

---

## 🔧 Common Issues & Solutions

### Issue: Content Cuts Off

**Problem:** Too much content for viewport
**Solution:**
1. Reduce number of bullet points
2. Shorten descriptions
3. Use dynamic template instead
4. Split into two slides

### Issue: Colors Look Wrong

**Problem:** Accent color doesn't match brand
**Solution:**
1. Update CSS custom property
2. Test contrast (4.5:1 minimum)
3. Hard refresh browser (Cmd+Shift+R)
4. Check hex code format (#XXXXXX)

### Issue: Navigation Broken

**Problem:** Slide numbers don't match
**Solution:**
1. Verify `data-slide` attributes sequential
2. Check `totalSlides` variable correct
3. Review browser console for errors
4. Ensure all slides have unique numbers

### Issue: PDF Export Cuts Content

**Problem:** Content extends past page
**Solution:**
1. Use print preview to diagnose
2. Reduce content density
3. Check for `page-break-inside: avoid`
4. Test in Chrome (best PDF support)

---

## 📚 Additional Resources

### Documentation Files

- **`customization-guide.md`** - Detailed customization instructions
- **`visual-design-guide.md`** - Design principles and rationale
- **`components/README.md`** - Reusable component library
- **`troubleshooting.md`** - Common issues and fixes

### External Tools

- **WebAIM Contrast Checker** - Verify color accessibility
- **Google Fonts** - Inter font (included via CDN)
- **Chrome DevTools** - Debug and inspect
- **Figma/Sketch** - Design mockups before coding

### Related Skills

In the `/skills` directory:
- `360-client-portfolio-builder` - Automated portfolio generation
- `executive-intelligence-dashboard` - Data-driven dashboards

---

## 🤝 Contributing

### Reporting Issues

Found a bug? Please include:
- Template version (static/dynamic)
- Browser and version
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if visual issue

### Suggesting Improvements

Ideas for enhancements:
- Additional component patterns
- New layout variations
- Performance optimizations
- Accessibility improvements

---

## 📄 License

These templates are part of the 360 Social Impact Studios use case library.

---

## 📞 Support

For questions or assistance:
1. Check relevant README in `static/` or `dynamic/`
2. Review `docs/troubleshooting.md`
3. Inspect working examples in `components/`
4. Consult visual design guide for design decisions

---

## ✨ Quick Examples

### Changing Organization Name

```html
<!-- In header -->
<div class="org-name">360 Social Impact Studios</div>
<!-- Change to: -->
<div class="org-name">Your Organization Name</div>
```

### Updating a Metric

```html
<div class="metric-label">PATIENTS SERVED</div>
<div class="metric-value">847K</div>
<div class="metric-change">+41% from FY 2024</div>
<!-- Change to: -->
<div class="metric-label">YOUR METRIC</div>
<div class="metric-value">123K</div>
<div class="metric-change">+10% from last year</div>
```

### Adding a Status Badge

```html
<h4>Partnership Name <span class="status-badge expanded">✓ EXPANDED</span></h4>
<!-- Or: -->
<h4>Partnership Name <span class="status-badge new">✓ NEW</span></h4>
```

---

**Last Updated:** November 2025
**Version:** 2.0
**Templates:** Static & Dynamic Executive Impact Reports
