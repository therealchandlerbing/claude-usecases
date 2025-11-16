# Technical Specifications - 360 Client Portfolio Builder

**Version:** 1.0.0
**Last Updated:** 2025-11-16
**Purpose:** HTML, CSS, and JavaScript implementation patterns and standards

---

## Technology Stack

### Core Technologies

**Required:**
- HTML5 (semantic markup)
- CSS3 (custom properties, grid, flexbox)
- Vanilla JavaScript (no frameworks)

**Optional:**
- Chart.js (data visualization)
- Font Awesome (icons)
- Google Fonts (typography)
- Intersection Observer API (scroll animations)

**Hosting:**
- Netlify (recommended, free tier available)
- GitHub Pages (free, limited features)
- Custom hosting (any static host)

### Browser Support

**Target Browsers:**
- Chrome 90+ (released April 2021)
- Safari 14+ (released September 2020)
- Firefox 88+ (released April 2021)
- Edge 90+ (released April 2021)

**Mobile:**
- iOS Safari 14+
- Chrome Mobile 90+
- Samsung Internet 14+

**Progressive Enhancement:**
- Core functionality works without JavaScript
- CSS Grid with flexbox fallback
- Modern features with graceful degradation

---

## HTML Structure

### Document Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="[Client tagline - 120-155 characters]">
    <meta name="keywords" content="[sector], social impact, 360 studios">
    <meta name="author" content="360 Social Impact Studios">

    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="[Client Name] | Social Impact Venture">
    <meta property="og:description" content="[Client tagline]">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://[domain].com">
    <meta property="og:image" content="https://[domain].com/og-image.jpg">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="[Client Name] | Social Impact Venture">
    <meta name="twitter:description" content="[Client tagline]">
    <meta name="twitter:image" content="https://[domain].com/og-image.jpg">

    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">

    <title>[Client Name] | Partnership with 360 Social Impact Studios</title>

    <!-- Preconnect to External Domains -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=[FontFamily]&display=swap" rel="stylesheet">

    <!-- Font Awesome (Optional) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-..." crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- Embedded Styles -->
    <style>
        /* All CSS embedded here for single-file deployment */
    </style>
</head>
<body>
    <!-- Content structure -->
    <script>
        /* All JavaScript embedded here */
    </script>
</body>
</html>
```

### Semantic Markup Patterns

**Use Semantic HTML5 Elements:**

```html
<!-- Navigation -->
<nav class="site-nav" role="navigation" aria-label="Main navigation">
    <!-- Nav content -->
</nav>

<!-- Main Content -->
<main id="main-content">
    <!-- Hero -->
    <section id="hero" aria-labelledby="hero-heading">
        <h1 id="hero-heading">[Venture Name]</h1>
    </section>

    <!-- Other Sections -->
    <section id="mission" aria-labelledby="mission-heading">
        <h2 id="mission-heading">Our Mission</h2>
        <article>
            <!-- Content -->
        </article>
    </section>
</main>

<!-- Footer -->
<footer class="site-footer" role="contentinfo">
    <!-- Footer content -->
</footer>
```

**Heading Hierarchy:**

```html
<!-- Correct: Logical hierarchy -->
<h1>Venture Name</h1>
    <h2>Section: Mission</h2>
        <h3>Subsection: Problem</h3>
        <h3>Subsection: Solution</h3>
    <h2>Section: Traction</h2>

<!-- Incorrect: Skipping levels -->
<h1>Venture Name</h1>
    <h3>Mission</h3>  <!-- ❌ Skipped H2 -->
```

**Lists:**

```html
<!-- Unordered List -->
<ul>
    <li>First item</li>
    <li>Second item</li>
</ul>

<!-- Ordered List -->
<ol>
    <li>First step</li>
    <li>Second step</li>
</ol>

<!-- Definition List -->
<dl>
    <dt>Term</dt>
    <dd>Definition</dd>
</dl>
```

---

## CSS Architecture

### CSS Custom Properties (Variables)

**Define All Variables at :root:**

```css
:root {
    /* 360 Brand Colors */
    --360-sage: #87A878;
    --360-terracotta: #C97A63;
    --360-plum: #6B5B95;
    --360-red: #C85A54;
    --360-gray: #4A5859;

    /* Client Accent Colors (change per portfolio) */
    --accent-primary: #047857;
    --accent-secondary: #0EA5E9;

    /* Neutral Base */
    --bg-primary: #FEFEFE;
    --bg-secondary: #F8F9FA;
    --bg-dark: #1A1A1A;
    --text-primary: #1A1A1A;
    --text-secondary: #6B7280;
    --text-tertiary: #9CA3AF;

    /* Typography */
    --font-display: 'Crimson Pro', serif;
    --font-body: 'Inter', sans-serif;

    /* Font Sizes (Modular Scale 1.25) */
    --text-xs: 0.64rem;
    --text-sm: 0.8rem;
    --text-base: 1rem;
    --text-lg: 1.25rem;
    --text-xl: 1.563rem;
    --text-2xl: 1.953rem;
    --text-3xl: 2.441rem;
    --text-4xl: 3.052rem;
    --text-5xl: 3.815rem;

    /* Spacing (8px base) */
    --space-xs: 0.5rem;
    --space-sm: 1rem;
    --space-md: 1.5rem;
    --space-lg: 2rem;
    --space-xl: 3rem;
    --space-2xl: 4rem;
    --space-3xl: 5rem;
    --space-4xl: 6rem;
    --space-5xl: 8rem;

    /* Transitions */
    --transition-fast: 200ms ease-out;
    --transition-base: 300ms ease-out;
    --transition-slow: 400ms ease-out;
}
```

### CSS Reset & Base Styles

```css
/* Box Sizing */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* Root */
html {
    font-size: 16px;
    scroll-behavior: smooth;
}

/* Body */
body {
    font-family: var(--font-body);
    font-size: var(--text-base);
    line-height: 1.6;
    color: var(--text-primary);
    background: var(--bg-primary);
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-display);
    line-height: 1.2;
    margin-bottom: 1rem;
}

h1 { font-size: var(--text-4xl); font-weight: 700; }
h2 { font-size: var(--text-3xl); font-weight: 600; }
h3 { font-size: var(--text-2xl); font-weight: 600; }
h4 { font-size: var(--text-xl); font-weight: 500; }

/* Paragraphs */
p {
    margin-bottom: 1rem;
}

/* Links */
a {
    color: var(--accent-primary);
    text-decoration: none;
    transition: color var(--transition-base);
}

a:hover {
    color: color-mix(in srgb, var(--accent-primary) 70%, black);
}

a:focus {
    outline: 2px solid var(--accent-primary);
    outline-offset: 2px;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
}

/* Buttons */
button {
    font-family: inherit;
    cursor: pointer;
}
```

### Layout Patterns

**Container System:**

```css
.container-wide {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 var(--space-lg);
}

.container-standard {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 var(--space-lg);
}

.container-narrow {
    max-width: 680px;
    margin: 0 auto;
    padding: 0 var(--space-lg);
}

@media (max-width: 768px) {
    .container-wide,
    .container-standard,
    .container-narrow {
        padding: 0 var(--space-md);
    }
}
```

**Grid Layouts:**

```css
/* 2-Column Responsive Grid */
.grid-2 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-lg);
}

/* 3-Column Responsive Grid */
.grid-3 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--space-md);
}

/* 4-Column Responsive Grid */
.grid-4 {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: var(--space-md);
}

/* Asymmetric Layouts */
.layout-60-40 {
    display: grid;
    grid-template-columns: 60% 40%;
    gap: var(--space-xl);
    align-items: center;
}

.layout-40-60 {
    display: grid;
    grid-template-columns: 40% 60%;
    gap: var(--space-xl);
    align-items: center;
}

/* Mobile: Stack All Layouts */
@media (max-width: 768px) {
    .layout-60-40,
    .layout-40-60 {
        grid-template-columns: 1fr;
    }
}
```

**Flexbox Utilities:**

```css
.flex {
    display: flex;
}

.flex-column {
    flex-direction: column;
}

.flex-center {
    justify-content: center;
    align-items: center;
}

.flex-between {
    justify-content: space-between;
    align-items: center;
}

.flex-gap-sm { gap: var(--space-sm); }
.flex-gap-md { gap: var(--space-md); }
.flex-gap-lg { gap: var(--space-lg); }
```

---

## Component Patterns

### Navigation

```css
.site-nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background: rgba(254, 254, 254, 0.95);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(0, 0, 0, 0.05);
    padding: var(--space-md) var(--space-lg);
}

.nav-container {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-logo {
    height: 32px;
    width: auto;
}

.nav-links {
    display: flex;
    gap: var(--space-lg);
    list-style: none;
}

.nav-link {
    color: var(--text-primary);
    font-weight: 500;
    transition: color var(--transition-base);
}

.nav-link:hover {
    color: var(--360-sage);
}

/* Mobile Nav */
@media (max-width: 768px) {
    .nav-links {
        display: none; /* Or implement hamburger menu */
    }
}
```

### Hero Section

```css
.hero {
    min-height: 80vh;
    display: flex;
    align-items: center;
    padding: var(--space-5xl) var(--space-lg);
    position: relative;
    overflow: hidden;
}

.hero-content {
    max-width: 1400px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 60% 40%;
    gap: var(--space-xl);
    align-items: center;
}

.hero h1 {
    font-size: var(--text-5xl);
    margin-bottom: var(--space-md);
}

.hero .tagline {
    font-size: var(--text-lg);
    color: var(--text-secondary);
    margin-bottom: var(--space-lg);
}

.hero .cta-button {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    background: var(--accent-primary);
    color: white;
    border-radius: 8px;
    font-weight: 500;
    transition: all var(--transition-base);
}

.hero .cta-button:hover {
    background: color-mix(in srgb, var(--accent-primary) 85%, black);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

@media (max-width: 768px) {
    .hero {
        min-height: 60vh;
        padding: var(--space-3xl) var(--space-md);
    }

    .hero-content {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: var(--text-3xl);
    }
}
```

### Cards

```css
.card {
    background: var(--bg-primary);
    border-radius: 12px;
    padding: var(--space-lg);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}

.card-icon {
    width: 48px;
    height: 48px;
    margin-bottom: var(--space-md);
    color: var(--accent-primary);
}

.card h3 {
    margin-bottom: var(--space-sm);
}

.card p {
    color: var(--text-secondary);
    line-height: 1.7;
}

.card .badge {
    display: inline-block;
    margin-top: var(--space-sm);
    padding: 0.25rem 0.75rem;
    border-radius: 16px;
    font-size: var(--text-sm);
    font-weight: 500;
    background: color-mix(in srgb, var(--accent-primary) 10%, transparent);
    color: var(--accent-primary);
}
```

### Buttons

```css
.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    font-weight: 500;
    text-align: center;
    transition: all var(--transition-base);
    cursor: pointer;
    border: none;
    font-family: var(--font-body);
}

.btn-primary {
    background: var(--accent-primary);
    color: white;
}

.btn-primary:hover {
    background: color-mix(in srgb, var(--accent-primary) 85%, black);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.btn-secondary {
    background: transparent;
    color: var(--accent-primary);
    border: 2px solid var(--accent-primary);
}

.btn-secondary:hover {
    background: var(--accent-primary);
    color: white;
}

.btn-large {
    padding: 1rem 2rem;
    font-size: var(--text-lg);
}

.btn-small {
    padding: 0.5rem 1rem;
    font-size: var(--text-sm);
}
```

---

## JavaScript Patterns

### Scroll Animations (Intersection Observer)

```javascript
// Initialize Intersection Observer for fade-in animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const fadeInObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            // Optional: Unobserve after animation triggers once
            fadeInObserver.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all elements with fade-in class
document.querySelectorAll('.fade-in').forEach(el => {
    fadeInObserver.observe(el);
});
```

**CSS for Fade-In:**

```css
.fade-in {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.fade-in.visible {
    opacity: 1;
    transform: translateY(0);
}

/* Stagger delays for multiple elements */
.fade-in:nth-child(1) { transition-delay: 0.1s; }
.fade-in:nth-child(2) { transition-delay: 0.2s; }
.fade-in:nth-child(3) { transition-delay: 0.3s; }
```

### Smooth Scroll for Anchor Links

```javascript
// Smooth scroll for internal anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));

        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
```

### Mobile Menu Toggle

```javascript
// Mobile navigation toggle
const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('.nav-menu');

if (navToggle) {
    navToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        navToggle.classList.toggle('active');

        // Update ARIA attribute
        const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
        navToggle.setAttribute('aria-expanded', !isExpanded);
    });
}
```

**HTML:**

```html
<button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
    <span class="hamburger"></span>
</button>

<nav class="nav-menu">
    <!-- Navigation links -->
</nav>
```

**CSS:**

```css
.nav-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
}

@media (max-width: 768px) {
    .nav-toggle {
        display: block;
    }

    .nav-menu {
        display: none;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        background: white;
        padding: var(--space-lg);
    }

    .nav-menu.active {
        display: block;
    }
}
```

---

## Performance Optimization

### Image Optimization

**Lazy Loading:**

```html
<!-- Native lazy loading -->
<img src="image.jpg" alt="Description" loading="lazy">

<!-- With picture element for responsive images -->
<picture>
    <source srcset="image-large.webp" type="image/webp" media="(min-width: 1024px)">
    <source srcset="image-medium.webp" type="image/webp" media="(min-width: 768px)">
    <source srcset="image-small.webp" type="image/webp">
    <img src="image.jpg" alt="Description" loading="lazy">
</picture>
```

**Responsive Images:**

```html
<img
    srcset="image-320w.jpg 320w,
            image-640w.jpg 640w,
            image-1024w.jpg 1024w"
    sizes="(max-width: 768px) 100vw,
           (max-width: 1024px) 50vw,
           33vw"
    src="image-640w.jpg"
    alt="Description"
    loading="lazy">
```

### CSS Optimization

**Critical CSS (Inline in <head>):**

```html
<head>
    <style>
        /* Critical above-the-fold CSS */
        :root { /* Variables */ }
        *, *::before, *::after { /* Reset */ }
        body { /* Base styles */ }
        .hero { /* Hero section styles */ }
        /* ... other critical styles */
    </style>
</head>
```

**Minification:**

Use online tools or build processes to minify CSS:
- Remove whitespace
- Remove comments
- Combine selectors
- Shorten values

### JavaScript Optimization

**Defer Non-Critical JavaScript:**

```html
<!-- Defer script execution -->
<script defer src="script.js"></script>

<!-- Or place at bottom of <body> -->
<body>
    <!-- Content -->
    <script>
        // JavaScript here
    </script>
</body>
```

**Reduce DOM Manipulation:**

```javascript
// Bad: Multiple DOM updates
items.forEach(item => {
    list.appendChild(createItem(item));
});

// Good: Single DOM update
const fragment = document.createDocumentFragment();
items.forEach(item => {
    fragment.appendChild(createItem(item));
});
list.appendChild(fragment);
```

---

## Accessibility Implementation

### Semantic HTML

```html
<!-- Use semantic elements -->
<nav>...</nav>
<main>...</main>
<article>...</article>
<aside>...</aside>
<footer>...</footer>

<!-- Not generic divs -->
<div class="nav">...</div>  <!-- ❌ -->
<div class="main">...</div>  <!-- ❌ -->
```

### ARIA Attributes

```html
<!-- Navigation -->
<nav role="navigation" aria-label="Main navigation">
    <ul>
        <li><a href="#mission" aria-current="page">Mission</a></li>
    </ul>
</nav>

<!-- Buttons -->
<button aria-label="Close dialog" aria-expanded="false">
    <span class="icon" aria-hidden="true">×</span>
</button>

<!-- Skip Link -->
<a href="#main-content" class="skip-link">Skip to main content</a>
```

### Keyboard Navigation

```css
/* Focus Styles */
a:focus,
button:focus,
input:focus {
    outline: 2px solid var(--accent-primary);
    outline-offset: 2px;
}

/* Skip Link */
.skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: var(--accent-primary);
    color: white;
    padding: 8px;
    text-decoration: none;
    z-index: 100;
}

.skip-link:focus {
    top: 0;
}
```

### Color Contrast

```javascript
// Check contrast ratios using WebAIM Contrast Checker
// https://webaim.org/resources/contrastchecker/

// Minimum requirements (WCAG AA):
// - Body text: 4.5:1
// - Large text (18pt+): 3:1
// - UI components: 3:1
```

### Alt Text

```html
<!-- Good: Descriptive -->
<img src="solar-panel.jpg" alt="Solar panel installation on rural home in Kenya">

<!-- Bad: Not descriptive -->
<img src="solar-panel.jpg" alt="Image">

<!-- Decorative: Empty alt -->
<img src="pattern.svg" alt="" role="presentation">
```

---

## Testing & Validation

### Browser Testing Checklist

- [ ] Chrome (latest)
- [ ] Safari (latest)
- [ ] Firefox (latest)
- [ ] Edge (latest)
- [ ] Mobile Safari (iOS)
- [ ] Chrome Mobile (Android)

### Performance Testing

**Tools:**
- Google PageSpeed Insights
- Lighthouse (Chrome DevTools)
- WebPageTest
- GTmetrix

**Target Metrics:**
- First Contentful Paint: < 1.8s
- Largest Contentful Paint: < 2.5s
- Total Blocking Time: < 200ms
- Cumulative Layout Shift: < 0.1

### Accessibility Testing

**Tools:**
- WAVE Browser Extension
- axe DevTools
- Lighthouse Accessibility Audit
- Screen Reader (NVDA, JAWS, VoiceOver)

**Manual Tests:**
- [ ] Keyboard navigation (Tab, Shift+Tab, Enter, Space)
- [ ] Screen reader announces content correctly
- [ ] Color contrast meets WCAG AA
- [ ] All images have alt text
- [ ] Form labels associated correctly

### HTML Validation

Use W3C Validator: https://validator.w3.org/

---

## Deployment Checklist

### Pre-Deployment

- [ ] Minify CSS and JavaScript
- [ ] Optimize and compress images
- [ ] Test on all target browsers
- [ ] Validate HTML
- [ ] Check accessibility (WCAG AA)
- [ ] Test mobile responsiveness
- [ ] Verify all links work
- [ ] Set up analytics (if needed)
- [ ] Configure meta tags
- [ ] Test loading speed

### Post-Deployment

- [ ] Verify live site loads correctly
- [ ] Test on real devices (mobile, tablet)
- [ ] Check SSL/HTTPS
- [ ] Verify meta tags render in social shares
- [ ] Set up custom domain (if applicable)
- [ ] Configure CDN (if applicable)
- [ ] Monitor performance

---

## Common Issues & Solutions

### Issue: Layout Breaks on Mobile

**Solution:**
```css
/* Use mobile-first responsive design */
.container {
    padding: 1rem;
}

@media (min-width: 768px) {
    .container {
        padding: 2rem;
    }
}

/* Stack grid layouts on mobile */
@media (max-width: 768px) {
    .grid-layout {
        grid-template-columns: 1fr;
    }
}
```

### Issue: Slow Page Load

**Solutions:**
1. Optimize images (compress, use WebP)
2. Inline critical CSS
3. Defer JavaScript
4. Lazy load images
5. Use CDN for external resources

### Issue: Accessibility Errors

**Solutions:**
1. Add alt text to all images
2. Use semantic HTML
3. Ensure color contrast meets WCAG AA
4. Test keyboard navigation
5. Add ARIA labels where needed

---

## Code Quality Standards

### CSS Best Practices

```css
/* ✅ Good: Organized and readable */
.card {
    /* Layout */
    display: flex;
    flex-direction: column;
    gap: var(--space-md);

    /* Box Model */
    padding: var(--space-lg);

    /* Visual */
    background: var(--bg-primary);
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);

    /* Animation */
    transition: transform var(--transition-base);
}

/* ❌ Bad: Disorganized */
.card {
    padding: 2rem;
    transition: transform 0.3s;
    background: white;
    gap: 1.5rem;
    flex-direction: column;
    display: flex;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    border-radius: 12px;
}
```

### JavaScript Best Practices

```javascript
// ✅ Good: Clear, commented, error handling
function initScrollAnimations() {
    const elements = document.querySelectorAll('.fade-in');

    if (!elements.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(el => observer.observe(el));
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollAnimations);
} else {
    initScrollAnimations();
}

// ❌ Bad: No error handling, unclear purpose
document.querySelectorAll('.fade-in').forEach(el => {
    new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            entry.target.classList.add('visible');
        });
    }).observe(el);
});
```

---

## Resources

### Documentation
- [MDN Web Docs](https://developer.mozilla.org/)
- [CSS-Tricks](https://css-tricks.com/)
- [Web.dev](https://web.dev/)

### Tools
- [Can I Use](https://caniuse.com/) - Browser support
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)

### Testing
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [WAVE Accessibility Tool](https://wave.webaim.org/)
- [W3C Validator](https://validator.w3.org/)

---

## Version History

**v1.0.0 (2025-11-16):** Initial technical specifications

---

**Next:** Review [sector-positioning.md](sector-positioning.md) for industry-specific guidance
