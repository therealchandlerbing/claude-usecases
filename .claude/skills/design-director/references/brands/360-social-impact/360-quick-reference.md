# 360 Social Impact Studios - Quick Reference

**Fast lookup for Design Director integration**

---

## Color Palette

### Primary Colors

| Color | Hex | RGB | Use Case |
|-------|-----|-----|----------|
| **Navy Blue** | `#1E4D6B` | 30, 77, 107 | Headers, formal text, primary brand |
| **Bright Blue** | `#00A7E1` | 0, 167, 225 | Accents, energy, interactive elements |
| **White** | `#FFFFFF` | 255, 255, 255 | Backgrounds, negative space |
| **Black** | `#231F20` | 35, 31, 32 | Body text |

### Accent Colors

| Color | Hex | RGB | Use Case |
|-------|-----|-----|----------|
| **Lime Green** | `#7AC143` | 122, 193, 67 | Growth, sustainability, success |
| **Magenta** | `#E6007E` | 230, 0, 126 | Impact, community, attention |
| **Red** | `#ED1C24` | 237, 28, 36 | Urgency, key metrics, errors |
| **Orange** | `#FF8C00` | 255, 140, 0 | Warmth, collaboration, warnings |
| **Yellow** | `#FFD100` | 255, 209, 0 | Innovation, opportunity (BG only!) |
| **Light Gray** | `#F5F5F5` | 245, 245, 245 | Subtle backgrounds, dividers |

### Color Combinations

**Professional:**
- Navy Blue + Bright Blue + White

**Sustainability:**
- Lime Green + Bright Blue + White

**Community/Energy:**
- Magenta + Orange + White

**Global/Brazil:**
- Orange + Magenta + Yellow (warm)

---

## Logo Selection Matrix

| Document Type | Logo File | Placement | Size |
|---------------|-----------|-----------|------|
| **Reports** | `LOGO_White_BG_1.png` | Top left | 2-2.5" |
| **Presentations (title)** | `LOGO_White_BG_1.png` | Top center | 3-4" |
| **Presentations (slides)** | `Circle__Logo_White_BG.png` | Top right | 1-1.5" |
| **One-pagers** | `LOGO_White_BG_1.png` | Top center | 2.5-3" |
| **Footer badges** | `Circle__Logo_White_BG.png` | Bottom left | 0.75-1" |
| **Dark backgrounds** | `*_BlackBG` versions | As appropriate | Same as above |

### Logo File Reference

```
/mnt/project/LOGO_White_BG_1.png         # Primary - white background
/mnt/project/LOGO_BlackBG_1.png          # Primary - dark background
/mnt/project/Circle__Logo_White_BG.png   # Badge - white background
/mnt/project/Circle__Logo__BlackBG.png   # Badge - dark background
/mnt/project/Graphic_LOGO_whiteBG_1.png  # Symbol - white background
/mnt/project/GraphicLOGO_BlackBG_1.png   # Symbol - dark background
```

---

## Typography Hierarchy

| Level | Size | Weight | Color | Use Case |
|-------|------|--------|-------|----------|
| **L1 Titles** | 28-36pt | Bold (700) | Navy Blue or Black | Document titles, main headers |
| **L2 Headers** | 18-22pt | Bold/SemiBold (600-700) | Navy Blue or Bright Blue | Section headers, slide titles |
| **L3 Subheaders** | 14-16pt | SemiBold (600) | Navy Blue or Black | Subsections |
| **Body Text** | 10-12pt | Regular (400) | Black | Paragraphs, content |
| **Captions** | 8-9pt | Regular (400) | Gray | Footnotes, image captions |

### Font Stack

```css
/* Headings */
font-family: 'Montserrat', Arial, sans-serif;
font-weight: 700;

/* Body */
font-family: 'Open Sans', Arial, sans-serif;
font-weight: 400;
line-height: 1.6;
```

---

## Audience-Specific Color Palettes

| Audience | Primary Colors | Accent Colors | Notes |
|----------|---------------|---------------|-------|
| **Partners (Corporate)** | Navy + Bright Blue + White | Minimal accents | Conservative, professional |
| **Partners (Brazil)** | Orange + Magenta | Yellow accents | Warm, vibrant, cultural |
| **Board** | Navy + Bright Blue + White | None or minimal | Conservative, data-focused |
| **Community** | Any brand colors | All accents welcome | Vibrant, inclusive, energetic |
| **Internal** | Any appropriate | Functional | Collaborative, clear |

---

## Data Visualization Color Sequences

**Single Series:**
```
Bright Blue (#00A7E1)
```

**2-3 Series:**
```
1. Navy Blue (#1E4D6B)
2. Bright Blue (#00A7E1)
3. Lime Green (#7AC143)
```

**4-6 Series:**
```
1. Navy Blue (#1E4D6B)
2. Bright Blue (#00A7E1)
3. Lime Green (#7AC143)
4. Magenta (#E6007E)
5. Orange (#FF8C00)
6. Yellow (#FFD100)
```

**Positive/Negative:**
```
Positive: Lime Green (#7AC143)
Negative: Red (#ED1C24)
Neutral: Light Gray (#F5F5F5)
```

---

## Page Setup Standards

### Reports/Documents

```
Margins: 1 inch all sides
Size: 8.5 x 11 inches (US Letter)
Orientation: Portrait
Logo: Top left, 2 inches
Footer: Page numbers, optional circle badge
```

### Presentations

```
Format: 16:9 widescreen
Title slide logo: Center, 3-4 inches
Content slide logo: Top right, 1-1.5 inches (circle badge)
Min text size: 16pt (readable from distance)
```

### One-Pagers

```
Logo: Top center, 2.5-3 inches
Layout: 2-3 columns
Callouts: 16-18pt with accent colors
Footer: Contact info + small circle badge
```

---

## CSS Quick Copy

```css
:root {
  /* Primary Colors */
  --navy: #1E4D6B;
  --bright-blue: #00A7E1;
  --white: #FFFFFF;
  --black: #231F20;

  /* Accent Colors */
  --lime-green: #7AC143;
  --magenta: #E6007E;
  --red: #ED1C24;
  --orange: #FF8C00;
  --yellow: #FFD100;
  --light-gray: #F5F5F5;

  /* Typography */
  --font-heading: 'Montserrat', Arial, sans-serif;
  --font-body: 'Open Sans', Arial, sans-serif;
}

/* Headings */
h1, h2, h3 {
  font-family: var(--font-heading);
  font-weight: 700;
  color: var(--navy);
}

h1 { font-size: 2.5rem; }      /* 40px at 16px base */
h2 { font-size: 1.75rem; }     /* 28px */
h3 { font-size: 1.25rem; }     /* 20px */

/* Body */
body {
  font-family: var(--font-body);
  font-size: 1rem;              /* 16px */
  line-height: 1.6;
  color: var(--black);
}

/* Utilities */
.accent-blue { color: var(--bright-blue); }
.accent-green { color: var(--lime-green); }
.accent-magenta { color: var(--magenta); }
.bg-light { background-color: var(--light-gray); }
```

---

## Python Quick Copy

```python
# 360 Brand Colors
colors_360 = {
    # Primary
    'navy': '#1E4D6B',
    'bright_blue': '#00A7E1',
    'white': '#FFFFFF',
    'black': '#231F20',

    # Accent
    'lime_green': '#7AC143',
    'magenta': '#E6007E',
    'red': '#ED1C24',
    'orange': '#FF8C00',
    'yellow': '#FFD100',
    'light_gray': '#F5F5F5'
}

# Logo paths
logos_360 = {
    'primary': '/mnt/project/LOGO_White_BG_1.png',
    'primary_dark': '/mnt/project/LOGO_BlackBG_1.png',
    'circle': '/mnt/project/Circle__Logo_White_BG.png',
    'circle_dark': '/mnt/project/Circle__Logo__BlackBG.png',
    'graphic': '/mnt/project/Graphic_LOGO_whiteBG_1.png',
    'graphic_dark': '/mnt/project/GraphicLOGO_BlackBG_1.png'
}

# Data visualization sequences
viz_colors_360 = {
    'single': ['#00A7E1'],
    'duo': ['#1E4D6B', '#00A7E1'],
    'trio': ['#1E4D6B', '#00A7E1', '#7AC143'],
    'multi': ['#1E4D6B', '#00A7E1', '#7AC143', '#E6007E', '#FF8C00', '#FFD100'],
    'diverging': {
        'positive': '#7AC143',
        'negative': '#ED1C24',
        'neutral': '#F5F5F5'
    }
}
```

---

## Accessibility Checklist

### WCAG AA Compliance

✅ **Safe for text on white:**
- Navy Blue (#1E4D6B)
- Bright Blue (#00A7E1)
- Lime Green (#7AC143)
- Magenta (#E6007E)
- Black (#231F20)

❌ **NOT safe for text on white:**
- Yellow (#FFD100) - Use for backgrounds only

### Minimum Sizes

- Body text: **10pt minimum** (12pt preferred)
- Captions: **8pt minimum**
- Presentations: **16pt minimum**
- Touch targets (web): **44x44px minimum**

### Best Practices

- ✅ Use proper heading hierarchy (H1 > H2 > H3)
- ✅ Provide alt text for all images
- ✅ Include focus states (never remove outlines)
- ✅ Don't rely on color alone (use icons, labels)
- ✅ Test with screen readers
- ✅ Ensure PDFs are accessible

---

## Common Pitfalls

### ❌ DON'T

- Use yellow text on white backgrounds
- Stretch or distort logos
- Change logo colors
- Use logos smaller than minimums
- Mix more than 3 accent colors per section
- Forget clear space around logos
- Use generic "professional blue" instead of 360 navy
- Apply 3D effects or shadows to logos

### ✅ DO

- Use exact hex codes for colors
- Maintain logo aspect ratios
- Follow logo size and placement rules
- Limit accent colors to 2-3 per section
- Maintain clear space around all logos
- Reference 360 navy (#1E4D6B) specifically
- Keep logos clean and unmodified

---

## Quick Decision Matrix

| If creating... | Use this logo | Use these colors | Typography |
|----------------|--------------|------------------|------------|
| **Board deck** | Full logo (title), Circle (slides) | Navy + Bright Blue only | Conservative hierarchy |
| **Partnership brief** | Full logo | Navy + Bright Blue or Orange + Magenta (Brazil) | Professional, strategic |
| **Community flyer** | Full logo | All accent colors | Bold, accessible, large |
| **Internal report** | Circle badge | Any appropriate | Functional, clear |
| **One-pager** | Full logo (centered) | 2-3 accent colors | Strong hierarchy, bold callouts |

---

## Document Checklist

Before finalizing any 360 document:

- [ ] Logo present and correctly sized
- [ ] Logo has adequate clear space
- [ ] Colors match exact hex codes from this guide
- [ ] Fonts follow specified hierarchy
- [ ] Text meets WCAG AA contrast standards
- [ ] Headers use navy blue or bright blue
- [ ] Audience-appropriate color palette used
- [ ] Tone matches audience (professional, warm, vibrant, etc.)
- [ ] No yellow text on white backgrounds
- [ ] Typography follows Design Director best practices
- [ ] Visual hierarchy is clear and intentional
- [ ] White space is deliberate, not default

---

## Emergency Fallbacks

**If custom fonts unavailable:**
- Use Arial for all text (widely available)
- Maintain size and weight hierarchy

**If logo files unavailable:**
- Use text: "360 SOCIAL IMPACT STUDIOS" in Arial Black
- Include note that official logo will be added

**If color palette unavailable:**
- Use Navy Blue (#1E4D6B) and white only
- Add accent colors when available

---

## Version

**Version:** 1.0.0
**Last Updated:** 2025-11-22
**Maintained By:** 360 Social Impact Studios

---

## Related Resources

- [360 Brand Standards (Complete)](360-brand-standards.md) - Full specification
- [360 Integration Guide](360-integration-guide.md) - How to use with Design Director
- [360 Quality Checklist](360-quality-checklist.md) - Pre-delivery validation
- [Design Director SKILL.md](../../SKILL.md) - Parent skill documentation

---

**Print or bookmark this page for fast reference when creating 360 materials.**
