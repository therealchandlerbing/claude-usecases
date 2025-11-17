# Board Packet Cover Template

This template defines the cover page structure for 360 board packets.

---

## Cover Page Structure

### Title Block

**Organization Name** (Title style - Arial 24pt Bold)
360 SOCIAL IMPACT STUDIOS

**Meeting Type** (Subtitle style - Arial 13pt)
[Annual/Quarterly/Special] Board Meeting

**Date** (Subtitle style - Arial 13pt)
[Full Date, e.g., "Monday, November 17, 2025"]

---

### Meeting Information Table

4 rows × 2 columns, no borders, left column gray (#ECF0F1) background

| Label (Bold, Gray BG) | Content |
|-----------------------|---------|
| **Date:** | [Full date with day of week] |
| **Time:** | [Time range with timezone, e.g., "1:00-2:30 PM PST"] |
| **Location:** | [Physical address or "Online (Zoom)" or "Hybrid"] |
| **Meeting Type:** | [Annual Board Meeting / Quarterly Board Meeting / Special Board Meeting] |

---

## Python Implementation

```python
def create_cover_page(doc, meeting_info):
    """Create cover page with title block and meeting information table

    Args:
        doc: Document object
        meeting_info: Dict with keys: date, time, location, meeting_type
    """

    # Title: Organization name
    title = doc.add_paragraph('360 SOCIAL IMPACT STUDIOS')
    title.style = 'Title'
    title_format = title.paragraph_format
    title_format.space_after = Pt(6)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Subtitle: Meeting type
    subtitle1 = doc.add_paragraph(meeting_info['meeting_type'])
    subtitle1.style = 'Subtitle'
    subtitle1_format = subtitle1.paragraph_format
    subtitle1_format.space_after = Pt(6)
    subtitle1.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Subtitle: Date
    subtitle2 = doc.add_paragraph(meeting_info['full_date'])
    subtitle2.style = 'Subtitle'
    subtitle2_format = subtitle2.paragraph_format
    subtitle2_format.space_after = Pt(18)
    subtitle2.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Meeting Information Table
    create_meeting_info_table(doc, meeting_info)

    return doc
```

---

## Sample Data

```python
meeting_info_sample = {
    'meeting_type': 'Annual Board Meeting',
    'full_date': 'Monday, November 17, 2025',
    'date': 'Monday, November 17, 2025',
    'time': '1:00-2:30 PM PST',
    'location': 'Online (Zoom)',
    'meeting_type_short': 'Annual Board Meeting'
}
```

---

*End of Cover Template*
