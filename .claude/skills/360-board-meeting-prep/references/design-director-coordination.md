# Design-Director Coordination Protocol

**Reference for integrating design-director skill with board meeting outputs**

---

## Overview

All board meeting prep outputs MUST be routed through design-director for professional visual elevation before delivery to user. This ensures consistent, publication-quality materials for governance use.

---

## Output-Specific Elevation

### DOCX Board Packet

**Exemplar**: Stripe + Swiss Design hybrid

**Elevation techniques**:
1. **Typography hierarchy**
   - Title: Arial 24pt Bold, #1a1a1a
   - Heading 1: Arial 14pt Bold, 18pt space before
   - Heading 2: Arial 12pt Bold, 12pt space before
   - Body: Calibri 11pt, 1.5 line height
   - Tables: Calibri 10pt

2. **Table formatting**
   - Meeting info: Gray labels (#ECF0F1), no borders
   - Motion tables: 1pt black borders, clear checkboxes
   - Data tables: Header row bold with #F5F5F5 fill, alternating row shading at 3%

3. **Spacing scale**
   - Use 8-point grid: 8, 16, 24, 32, 48px
   - Section dividers: 18pt before and after
   - Paragraph spacing: 6pt after

4. **Visual elements**
   - Section dividers: Centered "..." (not em-dashes)
   - Checkboxes: Unicode U+2610
   - Status indicators: Emoji supported

**Validation checklist**:
- [ ] Would fit in Stripe's document design system
- [ ] Typography creates 3+ visual hierarchy levels
- [ ] Spacing is consistent throughout
- [ ] Tables are scannable and aligned
- [ ] Print preview shows proper formatting

---

### HTML Financial Dashboard

**Exemplar**: Stripe dashboard

**Color palette**:
```css
--primary-bg: #1a1a1a;        /* Dark charcoal */
--secondary-bg: #2d2d2d;      /* Card background */
--text-primary: #ffffff;       /* White text */
--text-secondary: #a0a0a0;     /* Gray text */
--brand-accent: #FF6B35;       /* 360 orange */
--success: #22C55E;            /* Green */
--warning: #F59E0B;            /* Amber */
--danger: #EF4444;             /* Red */
--stripe-blue: #0A2540;        /* For trust elements */
```

**Typography**:
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
--title: 32px/1.2, font-weight: 700;
--heading: 20px/1.3, font-weight: 600;
--body: 14px/1.5, font-weight: 400;
--small: 12px/1.4, font-weight: 400;
```

**Layout**:
- 8-point grid system
- Card-based organization
- Generous padding (24px cards, 32px sections)
- Responsive breakpoints: 768px, 1024px, 1280px

**Data visualization**:
- Chart.js with custom colors matching palette
- Clean axes, minimal gridlines
- Data labels on hover
- Accessible contrast ratios

**Validation checklist**:
- [ ] Would fit in Stripe's dashboard design system
- [ ] Color palette limited to defined variables
- [ ] Typography creates clear hierarchy
- [ ] Charts are readable and meaningful
- [ ] Responsive design works on tablet/mobile
- [ ] Accessibility requirements met (4.5:1 contrast)

---

### HTML Portfolio Dashboard

**Exemplar**: Linear + Notion hybrid

**Specific techniques**:
- Status indicators using colored pills
- Relationship health as colored dots (green/yellow/red)
- Tier distribution as horizontal bar chart
- Client cards with hover effects
- Engagement sparklines

**Color for meaning**:
- Green (#22C55E): Healthy, active, on-track
- Amber (#F59E0B): Attention needed, warning
- Red (#EF4444): Critical, urgent, blocked
- Blue (#3B82F6): Information, neutral

---

### HTML Strategic Dashboard

**Exemplar**: Linear timeline/roadmap

**Specific techniques**:
- Timeline visualization for horizons
- Progress bars with percentage labels
- Partnership grid with status badges
- Risk matrix (impact vs likelihood)
- Priority cards with progress indicators

**Visual elements**:
- Timeline markers
- Connecting lines between related items
- Hover states for details
- Expandable sections

---

### PDF Exports

**Print optimization**:

1. **Portrait (document)**
   - Margins: 1 inch all sides
   - Headers: Organization name, date
   - Footers: Page numbers, confidentiality note
   - Page breaks: Before each major section

2. **Landscape (slides)**
   - One slide per page
   - Navigation hidden
   - Background graphics enabled
   - Margins: None for full-bleed

**Color adjustments for print**:
- Ensure text contrast for black/white printing
- Test charts in grayscale
- Avoid pure white on dark backgrounds

---

## Elevation Request Format

When handing off to design-director, use this format:

```
DESIGN-DIRECTOR ELEVATION REQUEST

Output Type: [DOCX/HTML Dashboard/PDF]
Document: [Specific document name]
Audience: Board of Directors
Quality Level: Publication-ready

Content Status:
- Functional foundation complete
- Data validated and accurate
- All sections populated

Elevation Needed:
1. [Specific technique needed]
2. [Specific technique needed]
3. [Specific technique needed]

Exemplar Reference: [Stripe/Linear/Swiss]

Special Requirements:
- [Any specific formatting rules]
- [User preferences]

Return:
- Elevated output file
- Confirmation of quality gates passed
```

---

## Quality Gates

Design-director must confirm before delivery:

### Interrogation Criteria

**Typography**:
- Font choices are deliberate
- 3+ hierarchy levels exist
- Line height appropriate (1.5-1.7x)
- Headings/body have meaningful relationship

**Color**:
- 2-3 colors maximum in palette
- Each color serves specific purpose
- Meets accessibility contrast (4.5:1)
- Taken from exemplar, not defaults

**Layout**:
- White space is deliberate
- Elements align to grid
- Spacing relationships consistent
- Breathing room around important elements

**Hierarchy**:
- 3 visual levels identifiable
- Most important info stands out
- Similar elements treated consistently

### Red Flags to Avoid

- Default fonts without consideration
- More than 4 colors
- No clear visual hierarchy
- Typography all one size/weight
- White space feels cramped
- Template-based appearance
- Could swap with generic template

### Portfolio-Ready Check

Final validation: "Would I include this in a design portfolio?"

---

## Timing

**Simple outputs** (single document): ~5-10 minutes
- Quick interrogation
- 1-2 techniques
- Fast application

**Complex outputs** (full packet + dashboards): ~15-20 minutes
- Thorough interrogation
- 3 techniques per output
- Comprehensive application
- Full validation

---

## Error Handling

**Design-director unavailable**:
1. Apply basic formatting from specifications
2. Note: "Design elevation not applied - recommend manual review"
3. Flag specific areas needing attention
4. Proceed with delivery

**Quality gates not passing**:
1. Identify specific failures
2. Apply additional techniques
3. Re-validate
4. If still failing, note limitations to user

---

## Success Criteria

Elevated board packet achieves:
- Professional, publication-quality appearance
- Consistent visual language across all outputs
- Appropriate exemplar alignment
- Hand-crafted, not template-based appearance
- Board members impressed by quality
- No manual cleanup required

---

*Reference for 360 Board Meeting Prep skill*
*Design-director coordination protocol v2.0*
