# Design Standards - 360 Client Portfolio Builder

**Version:** 1.0.0
**Last Updated:** 2025-11-16
**Purpose:** Visual design specifications and standards for all portfolio pages

---

## Design Philosophy

### Editorial Sophistication Over Corporate Templates

Every portfolio should feel like it was crafted by a high-end innovation studio, not generated from a template. Think:
- **Stripe** - Clarity with subtle elegance
- **Linear** - Precision and purposeful spacing
- **Apple** - Product focus with refined typography
- **Notion** - Accessible sophistication
- **Swiss Design** - Grid systems used intentionally, then broken

### Avoid These Aesthetics

❌ Startup pitch deck (too much hype, gradient backgrounds)
❌ Corporate annual reports (sterile, overly formal)
❌ AI-generated gradients or obvious stock imagery
❌ Template-based layouts (cookie-cutter sections)
❌ Generic SaaS landing pages (feature lists, pricing tables)

---

## Core Design Principles

### 1. Asymmetry with Purpose

**Principle:** Don't default to centered layouts or rigid grids. Use asymmetry to create visual interest and guide the eye.

**Good Examples:**
```
┌─────────────────────────────────────┐
│                                     │
│  Text (60%)          Visual (40%)   │
│  Large heading       [Image or      │
│  Body content        Abstract       │
│  that flows          Element]       │
│                                     │
└─────────────────────────────────────┘
```

**Implementation:**
- Text occupies 60%, visual anchor 40% (or vice versa)
- Section widths vary (full-bleed, constrained to 680px, etc.)
- Headers offset left or right, not centered
- Images break grid boundaries intentionally

**Avoid:**
- Perfectly centered everything
- Rigid 3-column layouts repeated throughout
- Equal spacing between all sections
- Predictable left-right alternation

---

### 2. White Space as Design Element

**Principle:** Negative space isn't wasted space. It creates breathing room and signals sophistication.

**Spacing Scale (8px base):**
```css
--space-xs: 0.5rem;   /* 8px */
--space-sm: 1rem;     /* 16px */
--space-md: 1.5rem;   /* 24px */
--space-lg: 2rem;     /* 32px */
--space-xl: 3rem;     /* 48px */
--space-2xl: 4rem;    /* 64px */
--space-3xl: 5rem;    /* 80px */
--space-4xl: 6rem;    /* 96px */
--space-5xl: 8rem;    /* 128px */
```

**Section Padding:**
- Default: 80px top/bottom, 32px left/right
- Hero: 128px top/bottom
- Compact: 64px top/bottom
- Mobile: 64px top/bottom, 24px left/right

**Best Practices:**
- Generous padding around sections
- Variable spacing creates rhythm
- Strategic emptiness draws eye to focal points
- Margins frame content like a gallery

---

### 3. Typographic Hierarchy

**Principle:** Typography should create clear information hierarchy and establish editorial quality.

**Recommended Font Pairings:**

**Option 1: Classic Editorial**
- Display/Headers: **Crimson Pro** (serif, elegant)
- Body/UI: **Inter** (sans-serif, readable)
```html
<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

**Option 2: Modern Sophistication**
- Display/Headers: **Lora** (serif, refined)
- Body/UI: **Work Sans** (sans-serif, geometric)

**Option 3: Contemporary Tech**
- Display/Headers: **Fraunces** (serif, playful)
- Body/UI: **DM Sans** (sans-serif, warm)

**Type Scale (Modular Scale 1.25):**

| Size | rem | px | Use Case |
|------|-----|-----|----------|
| xs | 0.64rem | 10px | Captions, labels |
| sm | 0.8rem | 13px | Small text |
| base | 1rem | 16px | Body text |
| lg | 1.25rem | 20px | Large body |
| xl | 1.563rem | 25px | H4 |
| 2xl | 1.953rem | 31px | H3 |
| 3xl | 2.441rem | 39px | H2 |
| 4xl | 3.052rem | 49px | H1 |
| 5xl | 3.815rem | 61px | Display |

**Line Height:**
- Body text: 1.6-1.7 (optimal readability)
- Headers: 1.1-1.3 (tighter for impact)
- Large display: 1.0-1.1 (very tight)

**Font Weights:**
- Normal: 400
- Medium: 500
- Semibold: 600
- Bold: 700

---

### 4. Color as Accent, Not Decoration

**Principle:** Use color sparingly for emphasis and brand consistency. Let typography and layout do the heavy lifting.

**360 Brand Colors (Consistent Across All Portfolios):**

```css
:root {
  /* Primary 360 Brand */
  --360-sage: #87A878;        /* Primary brand color */
  --360-terracotta: #C97A63;  /* Secondary accent */
  --360-plum: #6B5B95;        /* Tertiary accent */
  --360-red: #C85A54;         /* Alert or emphasis */
  --360-gray: #4A5859;        /* Text and UI elements */
}
```

**Client Accent Colors by Sector:**

| Sector | Primary | Secondary | Use Case |
|--------|---------|-----------|----------|
| CleanTech | #047857 (Green) | #0EA5E9 (Blue) | Sustainability, energy |
| HealthTech | #3B82F6 (Blue) | #FB7185 (Coral) | Medical, wellness |
| EdTech | #9333EA (Purple) | #F59E0B (Yellow) | Learning, growth |
| FinTech | #1E3A8A (Navy) | #D97706 (Gold) | Finance, trust |
| Social Innovation | Use 360 sage | Use 360 terracotta | General impact |

**Neutral Base:**

```css
:root {
  --bg-primary: #FEFEFE;      /* Off-white (not pure white) */
  --bg-secondary: #F8F9FA;    /* Light gray for sections */
  --bg-dark: #1A1A1A;         /* Near-black (not pure black) */
  --text-primary: #1A1A1A;    /* Primary text */
  --text-secondary: #6B7280;  /* Supporting text */
  --text-tertiary: #9CA3AF;   /* De-emphasized text */
}
```

**System Colors:**

```css
--success: #10B981;  /* Green for positive states */
--warning: #F59E0B;  /* Amber for caution */
--error: #EF4444;    /* Red for errors */
--info: #3B82F6;     /* Blue for information */
```

**Color Usage Rules:**
- 360 brand colors in navigation, footer, subtle UI accents
- Client accent color (1-2 max) for primary actions and emphasis
- Neutral base for backgrounds and text
- Color signals interactivity (links, buttons, hover states)
- All combinations meet WCAG AA contrast (4.5:1 for body, 3:1 for large text)

**Accessibility Check:**
Use WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/

---

### 5. Interactions That Enhance, Not Distract

**Principle:** Every animation must serve a purpose. No motion for motion's sake.

**Approved Interactions:**

**Scroll-Triggered Fade-Ins:**
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
```

**Hover Effects:**
```css
/* Cards */
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    transition: all 0.3s ease-out;
}

/* Links */
a::after {
    width: 0;
    height: 2px;
    background: var(--accent-primary);
    transition: width 0.3s ease-out;
}

a:hover::after {
    width: 100%;
}
```

**Timing:**
- Fast: 200-300ms (subtle feedback)
- Standard: 300-400ms (most interactions)
- Slow: 400-500ms (emphasis)
- Never exceed 500ms (feels sluggish)

**Easing:**
- `ease-out` for most transitions
- `ease-in-out` for reversible states
- Avoid `linear` (feels robotic)

**Avoid:**
- Aggressive animations (PowerPoint effect)
- Overuse of parallax (motion sickness)
- Bouncing, spinning, or decorative motion
- Animations that delay usability
- Auto-playing videos or carousels

---

### 6. Hand-Crafted, Not Template-Based

**Principle:** Every portfolio should feel custom-designed for that specific venture.

**Achieve Through:**
- Varied section layouts (don't repeat same pattern)
- Custom visual elements (abstract shapes, unique compositions)
- Unexpected details (asymmetric cards, offset images)
- Client-specific color palette and imagery
- Organic flow rather than rigid structure

**Red Flags for Template Feel:**
- ❌ Same hero layout on every portfolio
- ❌ Identical section ordering
- ❌ Consistent card sizing throughout
- ❌ Generic stock imagery
- ❌ Predictable interactions
- ❌ Uniform spacing everywhere

**Quality Indicators:**
- ✅ Each section feels intentionally designed
- ✅ Visual rhythm varies throughout page
- ✅ Unexpected details show craft
- ✅ Layout adapts to content, not vice versa
- ✅ Client brand personality comes through

---

## Layout System

### Container Widths

```css
.container-wide {
  max-width: 1400px;
  margin: 0 auto;
  padding: 0 2rem;
}

.container-standard {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 2rem;
}

.container-narrow {
  max-width: 680px;
  margin: 0 auto;
  padding: 0 2rem;
}
```

**Usage:**
- **Wide (1400px):** Full-width sections with images or grids
- **Standard (1100px):** Most sections, balanced reading width
- **Narrow (680px):** Text-heavy content, mission statements

### Responsive Grid Patterns

**2-Column Grid:**
```css
.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}
```

**3-Column Grid:**
```css
.grid-3 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}
```

**4-Column Grid:**
```css
.grid-4 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}
```

### Asymmetric Layouts

**60/40 Split:**
```css
.layout-60-40 {
  display: grid;
  grid-template-columns: 60% 40%;
  gap: 3rem;
  align-items: center;
}
```

**40/60 Split:**
```css
.layout-40-60 {
  display: grid;
  grid-template-columns: 40% 60%;
  gap: 3rem;
  align-items: center;
}
```

**70/30 Split (Sidebar):**
```css
.layout-70-30 {
  display: grid;
  grid-template-columns: 70% 30%;
  gap: 3rem;
  align-items: start;
}
```

**Mobile Breakpoint:**
```css
@media (max-width: 768px) {
  .layout-60-40,
  .layout-40-60,
  .layout-70-30 {
    grid-template-columns: 1fr;
  }
}
```

---

## Component Specifications

### Cards

**Standard Card:**
```css
.card {
  background: var(--bg-primary);
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease-out, box-shadow 0.3s ease-out;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
}
```

**Card with Icon:**
```css
.card-icon {
  width: 48px;
  height: 48px;
  margin-bottom: 1rem;
  color: var(--accent-primary);
}
```

**Staggered Card Grid:**
```css
.card:nth-child(2) {
  margin-top: 2rem;
}

.card:nth-child(3) {
  margin-top: 4rem;
}
```

### Buttons

**Primary Button:**
```css
.btn-primary {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background: var(--accent-primary);
  color: white;
  border-radius: 8px;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.3s ease-out;
}

.btn-primary:hover {
  background: color-mix(in srgb, var(--accent-primary) 85%, black);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
```

**Secondary Button:**
```css
.btn-secondary {
  background: transparent;
  color: var(--accent-primary);
  border: 2px solid var(--accent-primary);
}

.btn-secondary:hover {
  background: var(--accent-primary);
  color: white;
}
```

### Badges

```css
.badge {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 16px;
  font-size: var(--text-sm);
  font-weight: 500;
  background: color-mix(in srgb, var(--accent-primary) 10%, transparent);
  color: var(--accent-primary);
}
```

### Navigation

**Fixed Navigation:**
```css
.site-nav {
  position: fixed;
  top: 0;
  width: 100%;
  background: rgba(254, 254, 254, 0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  z-index: 1000;
  padding: 1rem 2rem;
}
```

### Hero Patterns

**Asymmetric Hero:**
```
┌─────────────────────────────────────┐
│                                     │
│  [Venture Name]        [Logo/      │
│  Tagline text         Visual       │
│  [CTA Button]         Element]     │
│                                     │
│  360 Partnership Badge             │
└─────────────────────────────────────┘
```

**Centered Hero with Background:**
```
┌─────────────────────────────────────┐
│         [Background Element]        │
│                                     │
│        [Venture Name]              │
│         Tagline text               │
│        [CTA Button]                │
│                                     │
│    360 Partnership Badge           │
└─────────────────────────────────────┘
```

---

## Responsive Design Standards

### Breakpoints

```css
/* Mobile First Approach */

/* Mobile: Base styles (375px+) */
.element {
  padding: 1rem;
  font-size: 1rem;
}

/* Tablet: 768px+ */
@media (min-width: 768px) {
  .element {
    padding: 1.5rem;
    font-size: 1.125rem;
  }
}

/* Desktop: 1024px+ */
@media (min-width: 1024px) {
  .element {
    padding: 2rem;
    font-size: 1.25rem;
  }
}

/* Large Desktop: 1440px+ */
@media (min-width: 1440px) {
  .element {
    padding: 2.5rem;
    font-size: 1.5rem;
  }
}
```

### Mobile Optimization

**Requirements:**
- Test at 375px minimum (iPhone SE)
- Touch targets minimum 44x44px
- No horizontal scrolling
- Readable text without zooming
- Stack asymmetric layouts
- Reduce padding/spacing
- Simplify navigation to hamburger menu

**Typography Adjustments:**
```css
/* Desktop */
h1 { font-size: 3.052rem; }

/* Mobile */
@media (max-width: 768px) {
  h1 { font-size: 2.441rem; }
}
```

---

## Brand Balance: 360 + Client

### 360 Brand Presence

**Required Elements:**
- Logo or wordmark in navigation (top left or top right)
- Footer attribution: "Partnership with 360 Social Impact Studios"
- 360 brand colors in UI elements (nav, footer, subtle accents)
- "360 Partnership Context" section
- Optional: Link to 360 website

**Implementation:**
```html
<!-- Navigation -->
<nav class="site-nav">
  <img src="360-studios-logo.svg" alt="360 Social Impact Studios" class="nav-logo">
</nav>

<!-- Footer -->
<footer>
  <p>Partnership with <a href="https://360studios.org">360 Social Impact Studios</a></p>
</footer>
```

### Client Distinctiveness

**Requirements:**
- Client name/logo larger than 360
- Client-specific accent colors (not 360 palette)
- Sector-specific framing
- Client traction emphasized over 360 contributions
- Client CTA as primary action

**Critical Rule:** 360 creates cohesion across portfolio pages (identifiable visual system), but never overshadows the client venture being showcased.

---

## Quality Checklist

Before finalizing any portfolio design:

### Visual Quality
- [ ] Layout feels hand-crafted, not template-based
- [ ] Asymmetry is intentional and purposeful
- [ ] White space creates breathing room
- [ ] Typography hierarchy is immediately clear
- [ ] Color palette is cohesive (360 + client)
- [ ] No generic stock imagery
- [ ] Unexpected details show craft
- [ ] Visual rhythm guides eye naturally

### Brand Balance
- [ ] 360 logo visible in navigation
- [ ] Footer includes 360 attribution
- [ ] 360 brand colors used in UI
- [ ] Partnership section present
- [ ] Client remains hero, not overshadowed

### Responsiveness
- [ ] Works at 375px (iPhone SE)
- [ ] Works at 768px (iPad portrait)
- [ ] Works at 1024px (iPad landscape)
- [ ] Works at 1440px+ (desktop)
- [ ] All text readable without zooming
- [ ] Touch targets 44x44px minimum
- [ ] No horizontal scrolling

### Technical
- [ ] All colors meet WCAG AA contrast
- [ ] Animations enhance, don't distract
- [ ] Hover states on interactive elements
- [ ] Loading states for dynamic content
- [ ] No console errors

---

## Examples by Section

### Hero Section Variations

**Variation 1: Text-Dominant**
- Large heading (60% width)
- Supporting tagline
- CTA button
- Small logo/visual (40% width)

**Variation 2: Visual-Dominant**
- Large product image or illustration (60% width)
- Concise heading and tagline (40% width)
- Overlay CTA

**Variation 3: Centered Impact**
- Centered heading
- Centered tagline
- Background visual element
- Centered CTA

### Section Layout Variations

Don't repeat the same layout pattern. Vary between:
- Full-width (image backgrounds, statistics)
- Standard width (most content)
- Narrow width (long-form text)
- Asymmetric splits (60/40, 70/30)
- Grid layouts (2, 3, or 4 columns)
- Timeline layouts
- Card grids with staggered heights

---

## Anti-Patterns to Avoid

### Design Anti-Patterns

❌ **Gradient Overload:** Bright, multi-color gradients everywhere
✅ **Instead:** Subtle single-hue gradients sparingly

❌ **Stock Photo Generic:** Business people pointing at screens
✅ **Instead:** Custom illustrations, client product photos, abstract elements

❌ **Center Everything:** All text and elements centered
✅ **Instead:** Asymmetric layouts with purpose

❌ **Color Explosion:** Rainbow of competing colors
✅ **Instead:** Neutral base + 1-2 accent colors

❌ **Animation Overload:** Everything bounces and spins
✅ **Instead:** Subtle fade-ins and hover states only

❌ **Template Repetition:** Same section structure repeated
✅ **Instead:** Varied layouts throughout page

### Typography Anti-Patterns

❌ **Too Many Fonts:** 4+ different typefaces
✅ **Instead:** 2 fonts max (serif + sans-serif)

❌ **Poor Contrast:** Light gray on white
✅ **Instead:** WCAG AA minimum (4.5:1)

❌ **Inconsistent Sizing:** Random font sizes
✅ **Instead:** Modular scale (1.25 ratio)

❌ **Justified Text:** Awkward spacing
✅ **Instead:** Left-aligned with ragged right

---

## Tools & Resources

### Design Tools
- **Figma:** Design mockups and prototypes
- **Coolors:** Color palette generator
- **Google Fonts:** Typography selection
- **Font Pair:** Font combination suggestions

### Accessibility Tools
- **WebAIM Contrast Checker:** Color contrast validation
- **WAVE:** Accessibility evaluation
- **Lighthouse:** Chrome DevTools audit

### Testing Tools
- **BrowserStack:** Cross-browser testing
- **Responsively:** Responsive design testing
- **PageSpeed Insights:** Performance testing

---

## Version History

**v1.0.0 (2025-11-16):** Initial design standards documentation

---

**Next:** Review [content-strategy.md](content-strategy.md) for writing guidelines
