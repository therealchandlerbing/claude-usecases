# Phase 2: Template Population (3-5 minutes)

## Step 1: Parse Content

- Convert user input into standard content schema
- Normalize metrics and percentages
- Apply formatting conventions
- Generate badges and status indicators
- Validate required fields present

## Step 2: Apply Branding

- Insert organization name throughout
- Apply brand color to CSS variables
- Validate color contrast (4.5:1 ratio requirement)
- Configure visual identity elements
- Fallback to default if invalid color provided

## Step 3: Populate Presentation Format

- Insert content into fixed-slide template
- Validate content fits within slide boundaries (1050px × 700px per slide)
- Configure navigation (7 slides: cover + 6 sections)
- Test all navigation methods (arrows, dots, keyboard, dropdown)
- Verify print styles

## Step 4: Populate Executive Format

- Insert content into continuous-scroll template
- Allow content to expand naturally (unlimited height)
- Configure section navigation
- Test smooth scrolling
- Verify print styles

## Technical Details

**Format 1: Presentation (Slide Deck)**
- Fixed-slide layout (1050px × 700px per slide)
- Landscape orientation
- One slide per page when printed
- Slide-based navigation

**Format 2: Executive (Continuous Document)**
- Continuous-scroll sections with unlimited height
- Portrait orientation
- Multi-page document when printed
- Section-based navigation

**Shared Foundation:**
- Same content source feeds both formats
- Consistent branding and visual identity
- Self-contained HTML with embedded CSS
- Google Fonts only external dependency
- Works fully offline after initial load
