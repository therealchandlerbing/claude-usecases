# Technique Catalog

**Part 3 of 5 - Design Director Reference Documentation**

Specific visual techniques organized by what they achieve. Use these as reference when elevating designs.

## Typography Techniques

### Establishing Hierarchy

**Size relationships (not just bigger)**
- Headlines 2.5-3x body size (not 1.5x)
- Subheadings 1.5-1.8x body size
- Body text 14-16px for web, 15-18px for documents
- Small text/captions 12-13px minimum

**Weight relationships**
- Headlines: 600-700 weight (semibold/bold)
- Subheadings: 500-600 weight (medium/semibold)
- Body: 400 weight (regular)
- Emphasis: 500-600 weight within body
- De-emphasis: 400 weight at 70-80% opacity

**Letter spacing (tracking)**
- Headlines: -0.02em to -0.04em (tighter)
- All caps: +0.05em to +0.15em (must increase)
- Body text: 0 to +0.01em (default or slightly loose)
- Small text: +0.01em to +0.02em (looser for legibility)

**Line height (leading)**
- Headlines: 1.1-1.3x font size (tighter)
- Subheadings: 1.3-1.4x font size
- Body text: 1.5-1.7x font size (comfortable reading)
- Captions: 1.4-1.5x font size

### Creating Distinction

**Font pairing**
- Serif headline + sans-serif body (classic, readable)
- Sans-serif headline + sans-serif body in different weights (modern, clean)
- Monospace for code/data (technical, precise)

**Specific combinations that work:**
- Inter (sans-serif, modern, tech) - use everywhere or as primary
- SF Pro (Apple's font, excellent hierarchy)
- Segoe UI (Windows, professional, accessible)
- Georgia + Inter (warm + modern)
- Playfair Display + Inter (elegant + clean)

### Readability Optimization

**Optimal line length**
- 50-75 characters per line ideal
- 45-90 characters acceptable range
- Use max-width to constrain if needed

**Paragraph spacing**
- 1.5-2x line height between paragraphs
- Or use first-line indent (1-2em) with no spacing

**Text color for hierarchy**
- Primary text: Pure black (#000000) or dark gray (#1a1a1a)
- Secondary text: 70% opacity or medium gray (#666666)
- Tertiary text: 50% opacity or light gray (#999999)
- Never pure black on pure white (slightly soften both)

## Color Techniques

### Building Palettes

**Monochromatic (single hue, multiple tints/shades)**
- Base color at full saturation
- Lighter versions: 10%, 20%, 30%, 40% of base
- Darker versions: +10%, +20%, +30% saturation
- Example: Stripe's blues (#0A2540, #0074D9, #B2D9F5)

**Analogous (adjacent hues)**
- Primary + one adjacent hue
- Example: Blue (#0074D9) + Blue-green (#00BFA5)

**Complementary accent (opposite hue for emphasis)**
- Primary blue (#0074D9) + accent orange (#FF6B35)
- Use accent sparingly (5-10% of design)

### Specific Palettes to Reference

**Stripe-inspired (financial, trustworthy)**
- Primary: #0A2540 (deep blue)
- Accent: #00D4FF (bright cyan)
- Neutral: #F6F9FC (soft white)
- Text: #1A1F36 (dark blue-gray)
- Success: #00D924 (bright green)

**Linear-inspired (product, modern)**
- Primary: #5E6AD2 (medium purple-blue)
- Accent: #8B5CF6 (purple)
- Background: #FCFCFC (warm white)
- Text: #16161D (near black)
- Border: #E4E4E7 (light gray)

**Apple-inspired (minimal, elegant)**
- Text: #000000 (true black)
- Secondary: #86868B (mid gray)
- Background: #FFFFFF (pure white)
- Accent: #007AFF (iOS blue) or #FF9500 (iOS orange)

**Swiss-inspired (systematic, clean)**
- Text: #000000 (black)
- Accent: #FF0000 (pure red)
- Background: #FFFFFF (white)
- Grid lines: #CCCCCC (light gray)

### Color Application Patterns

**Status colors (semantic meaning)**
- Success: Green (#10B981 or similar)
- Warning: Amber (#F59E0B or similar)
- Error: Red (#EF4444 or similar)
- Info: Blue (#3B82F6 or similar)
- Always include icon or text, not just color

**Data visualization colors**
- Use distinct hues, not tints of one color
- Ensure sufficient contrast between adjacent values
- Reference: #0074D9, #00BFA5, #FF6B35, #9B59B6, #F39C12
- Avoid: Excel defaults, traffic light (red/yellow/green)

**Background strategies**
- Solid white (#FFFFFF) for minimal
- Warm white (#FAFAFA or #F8F9FA) for softer
- Subtle gradient (5-10% variation) for depth
- Colored section backgrounds at 5-10% opacity

## Layout Techniques

### Grid Systems

**Column grids**
- 12 columns for complex layouts (web standard)
- 6 columns for medium complexity
- 4 columns for simple layouts
- Always include gutter (gap between columns)

**Baseline grid**
- Set line height as base unit (e.g., 24px)
- All elements align to multiples of base (24, 48, 72, 96px)
- Creates vertical rhythm

**8-point grid**
- All spacing in multiples of 8px (8, 16, 24, 32, 40, 48, 56, 64, 72, 80px)
- Or 4-point for tighter control (4, 8, 12, 16, 20, 24, 28, 32px)
- Ensures consistency across entire design

### Spacing Patterns

**Scale-based spacing**
- XS: 8px (tight elements)
- S: 16px (related items)
- M: 24px (standard separation)
- L: 32px (section spacing)
- XL: 48px (major sections)
- XXL: 64px+ (distinct areas)

**Optical spacing (adjust by eye)**
- Circles and curves need more visual space
- All-caps text needs more letter spacing
- White space around text should feel generous
- Padding inside containers should breathe

**Proximity for grouping**
- Related items: 8-16px apart
- Separate groups: 32-48px apart
- Major sections: 64px+ apart
- Use space to show relationships

### Alignment Strategies

**Left-aligned (most common)**
- Easiest to read for large blocks
- Creates strong vertical edge
- Professional, trustworthy

**Centered (use sparingly)**
- Headlines and short phrases only
- Creates formal, balanced feeling
- Don't center body text

**Right-aligned (rare)**
- Numbers in tables (for decimal alignment)
- Navigation or metadata
- Creates tension, use deliberately

**Justified (avoid for screen)**
- Can create rivers of white space
- Only use for print with proper hyphenation
- Not recommended for digital

## Visual Elements

### Shadows and Depth

**Subtle elevation**
- Light: 0 1px 3px rgba(0,0,0,0.05)
- Medium: 0 4px 6px rgba(0,0,0,0.07)
- High: 0 10px 24px rgba(0,0,0,0.10)

**Dramatic depth (use rarely)**
- 0 20px 40px rgba(0,0,0,0.15)
- Only for modals or key CTAs

**Inner shadows (subtle inset)**
- inset 0 1px 2px rgba(0,0,0,0.05)
- For form inputs or pressed states

### Borders and Dividers

**Minimal borders**
- 1px solid #E5E7EB (light gray)
- Use sparingly, prefer spacing
- Only where boundaries are ambiguous

**Accent borders**
- 2-3px solid color for emphasis
- Left border on cards/quotes (vertical accent)
- Top border on sections (horizontal separation)

**No borders**
- Use background color change instead
- Use increased spacing instead
- Use subtle shadow instead

### Rounding and Corners

**Border radius scale**
- XS: 2-4px (subtle, buttons/inputs)
- S: 6-8px (cards, containers)
- M: 12-16px (modals, large cards)
- L: 24px+ (hero sections, dramatic)
- Full: 50% or 9999px (circles, pills)

**Consistency matters**
- Use same radius throughout design
- Or use scale above consistently

## Data Visualization

### Chart Selection

**Show trends over time**
- Line chart (continuous data)
- Area chart (cumulative/volume)
- Column chart (comparing periods)

**Compare categories**
- Bar chart (horizontal, many categories)
- Column chart (vertical, few categories)
- Avoid pie charts (hard to compare)

**Show parts of whole**
- Stacked bar (comparing parts across categories)
- Treemap (hierarchical proportions)
- Avoid: Pie charts, donut charts (use only if <5 slices)

**Show relationships**
- Scatter plot (correlation)
- Bubble chart (three variables)
- Heatmap (two-dimensional density)

### Chart Styling

**Clean axes**
- Remove unnecessary gridlines (keep major only)
- Light gray for gridlines (#E5E7EB)
- Hide axis lines if gridlines present
- Label axes clearly, remove redundancy

**Effective legends**
- Position near relevant data
- Use direct labels on chart when possible
- Remove legend if only one series

**Color in charts**
- Use color to highlight insight
- Gray out less important data
- Ensure sufficient contrast
- Reference Stripe/Linear dashboards

### Table Enhancement

**Zebra striping**
- Alternate row colors at 3-5% opacity
- Or use borders between rows (1px)
- Not both, choose one

**Column alignment**
- Text: left-aligned
- Numbers: right-aligned (helps compare)
- Headers: match column alignment
- Dates: consider left or right based on format

**Visual hierarchy in tables**
- Header row: bold + background color
- Total rows: bold + border or background
- Highlight cells: background at 10-20% opacity
- Sorting indicators: subtle arrows

## Interaction Design (Web/HTML)

### Button Hierarchy

**Primary action**
- Solid background color
- High contrast text
- Most prominent size/weight

**Secondary action**
- Outline or ghost style
- Less prominent but visible
- Same size as primary

**Tertiary action**
- Text-only, no background
- Smallest of the three
- Subtle underline on hover

### Interactive States

**Hover**
- Darken color by 5-10%
- Or lighten background
- Subtle transition (150-200ms)

**Active/Pressed**
- Darken by 10-15%
- Optional: reduce size by 2-3%
- Or add inner shadow

**Disabled**
- Reduce opacity to 40-50%
- Or use light gray
- Consider removing from view entirely

**Focus (accessibility critical)**
- Outline: 2-3px solid color
- Offset: 2-4px from element
- High contrast, visible
- Never remove focus styles

## Output-Specific Techniques

### Presentations

**Slide layouts**
- Title + single image (powerful simplicity)
- Title + 3-5 bullet points (information delivery)
- Title + large number + context (impact)
- Title + 2-3 columns (comparison)
- Full-bleed image + text overlay (emotion)

**Transitions between slides**
- Create visual rhythm with recurring elements
- Use consistent positioning for titles
- Vary layout to maintain attention
- Save dramatic layouts for key moments

### Spreadsheets

**Conditional formatting**
- Color scales: use 2-3 colors maximum
- Data bars: subtle, don't overwhelm numbers
- Icons: sparingly, for status indication
- Always keep numbers readable

**Cell styling**
- Headers: bold + background fill + center align
- Important cells: border or background
- Calculations: italic or different color
- Never mix too many styles

### HTML/Web

**Responsive breakpoints**
- Mobile: <640px
- Tablet: 641-1024px
- Desktop: >1024px
- Adjust layout, not just size

**Performance considerations**
- Optimize images (WebP, appropriate size)
- Use system fonts when possible
- Minimize custom font variants
- Consider load time in design choices

## Application Strategy

When elevating a design:
1. Choose 2-3 techniques from this catalog
2. Apply them consistently throughout
3. Ensure techniques work together, not against each other
4. Reference exemplars (Stripe, Linear, Apple) to validate
5. Test against interrogation checklist
