# DOCX Formatting Specifications

**Complete formatting reference for board packet documents**

---

## Typography

### Font Specifications

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Document Title | Arial | 24pt | Bold | #000000 |
| Subtitle | Arial | 13pt | Regular | #666666 |
| Heading 1 | Arial | 14pt | Bold | #000000 |
| Heading 2 | Arial | 12pt | Bold | #000000 |
| Heading 3 | Arial | 11pt | Bold | #000000 |
| Body Text | Calibri | 11pt | Regular | #000000 |
| Table Text | Calibri | 10pt | Regular | #000000 |
| Small Text | Calibri | 9pt | Regular | #666666 |

### Spacing

| Element | Space Before | Space After | Line Height |
|---------|-------------|-------------|-------------|
| Title | 0pt | 12pt | 1.0 |
| Heading 1 | 18pt | 6pt | 1.15 |
| Heading 2 | 12pt | 6pt | 1.15 |
| Heading 3 | 6pt | 6pt | 1.15 |
| Body | 0pt | 6pt | 1.5 |
| List Item | 0pt | 3pt | 1.5 |

---

## Page Setup

### Margins

- Top: 1 inch
- Bottom: 1 inch
- Left: 1 inch
- Right: 1 inch

### Headers/Footers

**Header (optional)**:
- Organization name (left)
- Document title (center)
- Date (right)
- Font: Calibri 9pt

**Footer**:
- Page number (center): "Page X of Y"
- Confidentiality note (left): "Confidential - Board Use Only"
- Font: Calibri 9pt

---

## Meeting Information Table

### Structure

4 rows x 2 columns

| Label | Content |
|-------|---------|
| Date: | [Meeting date] |
| Time: | [Meeting time] |
| Location: | [Meeting location] |
| Meeting Type: | [Annual/Quarterly/Special] |

### Formatting

**Left column (labels)**:
- Background: #ECF0F1 (light gray)
- Font: Calibri 11pt Bold
- Alignment: Right
- Width: 25%

**Right column (content)**:
- Background: White
- Font: Calibri 11pt Regular
- Alignment: Left
- Width: 75%

**Table borders**: None (borderless clean look)

**Cell padding**: 8pt all sides

---

## Motion Tracking Tables

### Structure

2 rows x 1 column per motion

**Row 1: Title**
```
MOTION [#]: [Title]
```
- Font: Calibri 11pt Bold
- Background: White

**Row 2: Details**
```
"[Motion text in quotes]"

Moved by: ______________
Seconded by: ______________
Vote: ☐ Approved  ☐ Denied  ☐ Abstained
```
- Motion text: Calibri 11pt Italic
- Vote options: Calibri 11pt Regular
- Checkboxes: Unicode ☐ (U+2610)

### Formatting

- Borders: 1pt black all sides
- Cell padding: 10pt
- Spacing between motions: 12pt

---

## Data Tables

### Standard Data Table

**Header row**:
- Background: #F5F5F5
- Font: Calibri 10pt Bold
- Alignment: Match data alignment

**Data rows**:
- Background: White (or alternating #FAFAFA)
- Font: Calibri 10pt Regular
- Numeric columns: Right-aligned
- Text columns: Left-aligned

**Borders**:
- Header bottom: 1pt black
- Row separators: 0.5pt #E0E0E0
- Table outline: 1pt black

### Financial Table

**Columns**:
1. Category (left-aligned)
2. YTD Actual (right-aligned, currency)
3. Annual Budget (right-aligned, currency)
4. % of Budget (right-aligned, percentage)
5. Variance (right-aligned, currency with +/-)

**Totals row**:
- Background: #F5F5F5
- Font: Calibri 10pt Bold

---

## Section Dividers

### Centered Dots

```
• • •
```

- Font: Calibri 14pt
- Alignment: Center
- Space before: 18pt
- Space after: 18pt
- Color: #666666

**IMPORTANT**: Use bullet characters (•), NOT em-dashes

---

## Special Characters

### Checkboxes

- Empty: ☐ (U+2610)
- Checked: ☑ (U+2611)
- Crossed: ☒ (U+2612)

### Bullets

- Primary: • (U+2022)
- Secondary: ◦ (U+25E6)
- Tertiary: ‣ (U+2023)

### Flags

- Warning: ⚠️
- Critical: 🚨
- Info: ℹ️
- Success: ✓

---

## Color Palette

### Status Colors

| Status | Hex Code | Use |
|--------|----------|-----|
| Success/Green | #22C55E | On track, healthy |
| Warning/Amber | #F59E0B | Attention needed |
| Danger/Red | #EF4444 | Critical issue |
| Info/Blue | #3B82F6 | Informational |

### Table Colors

| Element | Hex Code |
|---------|----------|
| Header fill | #F5F5F5 |
| Alternate row | #FAFAFA |
| Border | #E0E0E0 |
| Label fill | #ECF0F1 |

---

## Python-docx Code Snippets

### Set Cell Background

```python
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_cell_background(cell, color_hex):
    """Set cell background color (without # prefix)"""
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), color_hex)
    cell._element.get_or_add_tcPr().append(shading_elm)

# Usage
set_cell_background(cell, 'ECF0F1')
```

### Create Motion Table

```python
def create_motion_table(doc, motion_num, title, motion_text):
    """Create formatted motion tracking table"""
    from docx.shared import Pt

    table = doc.add_table(rows=2, cols=1)
    table.style = 'Table Grid'

    # Row 1: Title
    title_cell = table.rows[0].cells[0]
    title_para = title_cell.paragraphs[0]
    title_run = title_para.add_run(f'MOTION {motion_num}: {title}')
    title_run.font.bold = True
    title_run.font.size = Pt(11)

    # Row 2: Details
    details_cell = table.rows[1].cells[0]

    # Motion text (italic)
    motion_para = details_cell.paragraphs[0]
    motion_run = motion_para.add_run(f'"{motion_text}"')
    motion_run.font.italic = True

    # Voting fields
    details_cell.add_paragraph()
    details_cell.add_paragraph('Moved by: ______________')
    details_cell.add_paragraph('Seconded by: ______________')
    vote_para = details_cell.add_paragraph('Vote: ')
    vote_para.add_run('☐ Approved  ☐ Denied  ☐ Abstained')

    return table
```

### Add Section Divider

```python
def add_section_divider(doc):
    """Add centered dot divider between sections"""
    from docx.shared import Pt
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    para = doc.add_paragraph('• • •')
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para.paragraph_format.space_before = Pt(18)
    para.paragraph_format.space_after = Pt(18)

    for run in para.runs:
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
```

### Apply Heading Style

```python
def apply_heading_style(para, level):
    """Apply consistent heading formatting"""
    from docx.shared import Pt
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    styles = {
        1: {'size': 14, 'before': 18, 'after': 6},
        2: {'size': 12, 'before': 12, 'after': 6},
        3: {'size': 11, 'before': 6, 'after': 6}
    }

    style = styles.get(level, styles[1])

    para.paragraph_format.space_before = Pt(style['before'])
    para.paragraph_format.space_after = Pt(style['after'])

    for run in para.runs:
        run.font.name = 'Arial'
        run.font.size = Pt(style['size'])
        run.font.bold = True
```

---

## Quality Checklist

Before saving DOCX:

- [ ] All headings use correct font (Arial, not Calibri)
- [ ] All body text uses Calibri
- [ ] Meeting info table has gray labels (#ECF0F1)
- [ ] Motion tables have 1pt black borders
- [ ] Section dividers use dots (•), not em-dashes
- [ ] Checkboxes use Unicode ☐
- [ ] Spacing is consistent (18pt before H1, etc.)
- [ ] Tables have proper alignment (numbers right, text left)
- [ ] No orphan headings at page bottoms
- [ ] Print preview shows expected formatting

---

*Reference for 360 Board Meeting Prep skill*
*DOCX formatting specifications v2.0*
