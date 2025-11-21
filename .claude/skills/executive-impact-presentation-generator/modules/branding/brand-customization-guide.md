# Brand Customization Guide

## Color System

### Recommended Colors by Sector

| Sector | Color Name | Hex Code | Use Case |
|--------|-----------|----------|----------|
| Nonprofit/Social Impact | Vibrant Orange | `#FF6B35` | Default, warm and impactful |
| Corporate/Professional | Professional Blue | `#0052CC` | Business and corporate settings |
| Healthcare | Medical Green | `#22C55E` | Health and wellness organizations |
| Environment | Earth Green | `#10B981` | Environmental and sustainability |
| Education | Academic Purple | `#8B5CF6` | Educational institutions |
| Technology | Tech Cyan | `#06B6D4` | Tech companies and startups |
| Finance | Corporate Red | `#DC2626` | Financial institutions |
| Arts/Culture | Creative Pink | `#EC4899` | Arts and cultural organizations |

### Color Application

The brand color is applied to:
- Bullet markers and list indicators
- Section labels and badges
- Navigation elements (dots, arrows)
- Hover and active states
- Border accents on cards
- Status indicators
- Interactive element highlighting

### Color Validation

**Automatic contrast checking:**
- 4.5:1 ratio requirement against dark backgrounds
- Invalid colors fall back to default (#FF6B35)
- Warning provided if contrast insufficient

**Color Format Requirements:**
- Must be hex code format: `#RRGGBB`
- Always include `#` prefix
- Use 6-character hex codes (not 3-character shorthand)
- Examples: `#FF6B35`, `#0052CC`, `#22C55E`

## Visual Identity

**Organization Branding:**
- Organization name appears throughout headers
- Consistent typography hierarchy
- Professional spacing and alignment
- Dark theme aesthetic (charcoal background)
- Orange secondary accent (complementary to brand color)

**Typography Hierarchy:**
- Level 1: 42px (main headings)
- Level 2: 28px (section titles)
- Level 3: 20px (subsection titles)
- Body: 16px (content text)
- Font: Inter (Google Fonts)

## Customization Options

### Standard Customization (Included)
- Primary brand color (required)
- Organization name (required)
- Fiscal year (required)
- Report date (required)

### Advanced Customization (Optional)
- Logo integration (SVG or PNG format)
- Custom font selection (via font-family override)
- Modified spacing/layout (CSS variables)
- Alternative color schemes (secondary colors)
- Custom card styles
- Modified slide dimensions

### Logo Integration (Optional)

**Requirements:**
- SVG or PNG format
- Automatic sizing and positioning
- Maintains aspect ratio
- Placed in cover slide and header areas

**Placement:**
- Presentation format: Top-left of cover slide
- Executive format: Header area of each section
- Print output: Appears on all pages

### Typography Customization (Optional)

**Default:** Inter (Google Fonts)

**Custom Font Support:**
- Override via font-family CSS variable
- Maintain hierarchy: 42px / 28px / 20px / 16px
- Ensure web font availability
- Test readability in both formats

### Layout Modifications (Optional)

**Adjustable via CSS Variables:**
- Spacing (padding, margins)
- Card padding and borders
- Slide dimensions (presentation format)
- Section padding (executive format)
- Navigation placement
- Color scheme variations
