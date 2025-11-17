# Motion Tracking Sheet Template

This template defines the structure for motion tracking sheets used during board meetings.

---

## Sheet Structure

### Header Section

**MOTION TRACKING SHEET** (Heading 1 - Arial 14pt Bold, uppercase)

### Instructions Paragraph

"This sheet contains pre-drafted motions for board consideration. During the meeting:

1. The Chair will call for a motion using the language provided
2. A board member moves (their name recorded in "Moved by")
3. Another board member seconds (their name recorded in "Seconded by")
4. Discussion occurs if needed
5. The Chair calls for a vote
6. The Secretary marks the appropriate box and records the vote"

---

## Motion Entry Format

Each motion consists of a 2-row, 1-column table with 1pt black border:

**Row 1** (Title row):
- **Format**: "MOTION [#]: [Title]"
- **Style**: Bold, 11pt
- **Example**: "MOTION 1: Approve Meeting Agenda"

**Row 2** (Details row):
Contains the following elements with proper spacing:

1. **Motion Text** (Italic, in quotes)
   - Format: "[Full motion text]"
   - Example: "I move that we approve the agenda for the Annual Board Meeting of November 17, 2025"

2. **Blank line** (spacing)

3. **Moved by field**
   - Format: "Moved by: ______________"
   - 12-14 underscores for signature

4. **Seconded by field**
   - Format: "Seconded by: ______________"
   - 12-14 underscores for signature

5. **Vote field**
   - Format: "Vote: ☐ Approved  ☐ Denied  ☐ Abstained"
   - Unicode checkboxes (U+2610)
   - Two spaces between options

**Table spacing**: 12pt space after each motion table

---

## Section Divider

Between major sections, use centered bullet divider:

**Format**: • • •
**Alignment**: Center
**Spacing**: 18pt before and after

---

## Ad Hoc Motions Section

After all pre-drafted motions, include section for ad hoc motions:

**Header**: "Ad Hoc Motions" (Heading 2 - Arial 12pt Bold)

**Instruction**: "*Space for motions arising during the meeting that were not pre-drafted*"

**Blank Motion Templates**: 2-3 blank motion entry tables with:
- "MOTION [#]: ___________________________"
- Blank lines for motion text
- Standard moved by/seconded by/vote fields

---

## Meeting Conclusion Section

At end of motion tracking sheet:

**Header**: "Meeting Conclusion" (Heading 2 - Arial 12pt Bold)

**Fields** (each on separate line):
- Meeting called to order at: ______________
- Meeting adjourned at: ______________
- Total motions considered: ______________
- Motions approved: ______________
- Motions denied: ______________
- Motions tabled: ______________

**Signature Lines**:
- **Recording Secretary**: ___________________________ **Date**: ______________
- **Board Chair**: ___________________________ **Date**: ______________

---

## Python Implementation

```python
def create_motion_tracking_sheet(doc, motions):
    """Create complete motion tracking sheet

    Args:
        doc: Document object
        motions: List of motion dicts with keys: number, title, text
    """

    # Header
    header = doc.add_paragraph('MOTION TRACKING SHEET')
    header.style = 'Heading 1'

    # Instructions
    instructions = doc.add_paragraph()
    instructions.add_run('This sheet contains pre-drafted motions for board consideration. During the meeting:\n\n')
    instructions.add_run('1. The Chair will call for a motion using the language provided\n')
    instructions.add_run('2. A board member moves (their name recorded in "Moved by")\n')
    instructions.add_run('3. Another board member seconds (their name recorded in "Seconded by")\n')
    instructions.add_run('4. Discussion occurs if needed\n')
    instructions.add_run('5. The Chair calls for a vote\n')
    instructions.add_run('6. The Secretary marks the appropriate box and records the vote')

    doc.add_paragraph()  # Spacing

    # Add section divider
    add_section_divider(doc)

    # Pre-drafted motions
    for motion in motions:
        create_motion_table(doc, motion['number'], motion['title'], motion['text'])

    # Section divider before ad hoc
    add_section_divider(doc)

    # Ad hoc motions section
    adhoc_header = doc.add_paragraph('Ad Hoc Motions')
    adhoc_header.style = 'Heading 2'

    adhoc_note = doc.add_paragraph('Space for motions arising during the meeting that were not pre-drafted')
    adhoc_note.runs[0].font.italic = True

    # 3 blank ad hoc motion templates
    for i in range(3):
        create_blank_motion_table(doc, motion_number=len(motions) + 1 + i)

    # Section divider before conclusion
    add_section_divider(doc)

    # Meeting conclusion
    conclusion_header = doc.add_paragraph('Meeting Conclusion')
    conclusion_header.style = 'Heading 2'

    doc.add_paragraph('Meeting called to order at: ______________')
    doc.add_paragraph('Meeting adjourned at: ______________')
    doc.add_paragraph()
    doc.add_paragraph('Total motions considered: ______________')
    doc.add_paragraph('Motions approved: ______________')
    doc.add_paragraph('Motions denied: ______________')
    doc.add_paragraph('Motions tabled: ______________')
    doc.add_paragraph()

    sig1 = doc.add_paragraph()
    sig1.add_run('Recording Secretary: ___________________________   ')
    sig1.add_run('Date: ______________')

    sig2 = doc.add_paragraph()
    sig2.add_run('Board Chair: ___________________________   ')
    sig2.add_run('Date: ______________')

    return doc


def create_blank_motion_table(doc, motion_number):
    """Create blank motion table for ad hoc use"""

    doc.add_paragraph()  # Spacing

    table = doc.add_table(rows=2, cols=1)
    table.style = 'Table Grid'

    # Row 1: Blank title
    title_cell = table.rows[0].cells[0]
    title_para = title_cell.paragraphs[0]
    title_run = title_para.add_run(f'MOTION {motion_number}: ___________________________')
    title_run.font.bold = True

    # Row 2: Blank details
    details_cell = table.rows[1].cells[0]

    details_cell.add_paragraph('_____________________________________________')
    details_cell.add_paragraph('_____________________________________________')
    details_cell.add_paragraph()
    details_cell.add_paragraph('Moved by: ______________')
    details_cell.add_paragraph('Seconded by: ______________')
    vote_para = details_cell.add_paragraph('Vote: ')
    vote_para.add_run('☐ Approved  ☐ Denied  ☐ Abstained')

    return table
```

---

## Sample Motion Data

```python
sample_motions = [
    {
        'number': 1,
        'title': 'Approve Meeting Agenda',
        'text': 'I move that we approve the agenda for the Annual Board Meeting of November 17, 2025'
    },
    {
        'number': 2,
        'title': 'Confirm Board of Directors',
        'text': 'I move that we confirm the following individuals as the Board of Directors of 360 Social Impact Studios for the term January 1, 2026 through December 31, 2026:\n- Chandler Lewis\n- [Board Member 2]\n- [Board Member 3]'
    },
    {
        'number': 13,
        'title': 'Adjournment',
        'text': 'I move to adjourn this meeting'
    }
]
```

---

*End of Motion Tracking Sheet Template*
