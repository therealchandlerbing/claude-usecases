# 360 Board Meeting Prep Agent

**Version**: 1.0
**Created**: November 2025
**For**: Chandler Lewis, 360 Social Impact Studios

---

## What This Skill Does

The 360 Board Meeting Prep Agent transforms scattered organizational data into polished, governance-ready board meeting packets. It:

1. **Pulls data** from Asana, QuickBooks, Gmail, and Google Drive
2. **Synthesizes insights** across financial, operational, strategic, and governance dimensions
3. **Generates 5 professional documents** following exact 360 formatting standards
4. **Conducts quality checks** to ensure cross-document consistency
5. **Supports meeting execution** with motion tracking and post-meeting follow-up

---

## Skill Structure

```
360-board-meeting-prep/
├── SKILL.md                    # Main orchestrator (6-phase workflow)
├── README.md                   # This file
├── references/                 # Specialized workflow guides
│   ├── financial-dashboard.md
│   ├── client-portfolio-health.md
│   ├── strategic-initiatives.md
│   ├── governance-compliance.md
│   └── motion-preparation.md
└── assets/
    ├── templates/              # Document templates
    │   ├── board_packet_cover.md
    │   └── motion_sheet_template.md
    └── docx_utilities.py       # Python DOCX generation utilities
```

---

## The 5 Documents Generated

1. **Financial Dashboard**: Revenue, expenses, cash flow, pipeline valuation
2. **Client Portfolio Health Report**: Relationship status, capacity utilization, portfolio analytics
3. **Strategic Initiatives Update**: Progress on 4 strategic priorities, major partnerships
4. **Governance & Compliance Report**: Action items, compliance calendar, board composition
5. **Motion Tracking Sheet**: Pre-drafted motions for board voting

---

## Installation

### Option 1: Upload as .skill file

1. Package the skill directory as a .skill archive
2. Upload to Claude via Skills menu
3. Skill becomes available immediately

### Option 2: Manual setup

1. Create a skill directory in your Claude workspace
2. Copy all files maintaining the directory structure
3. Claude will detect the SKILL.md file automatically

---

## Usage

### Basic Usage

**Trigger phrase**: "Help me prep for the [date] board meeting"

The skill will:
1. Ask for meeting parameters (date, type, agenda topics)
2. Pull data from all sources (Asana, QuickBooks, Gmail, Drive)
3. Generate draft documents
4. Present for your review
5. Create final DOCX files after your approval
6. Store in Google Drive and provide download links

### Advanced Usage

**Generate single document**: "Generate just the financial dashboard for the board"

**Strategic update only**: "Pull a SpacePlan JV update for the board"

**Post-meeting follow-up**: "Extract action items from this meeting transcript"

---

## Data Sources

| Source | What It Accesses | How |
|--------|-----------------|-----|
| **Asana** | Client Delivery Hub portfolio, Board/Governance project | Automatic via MCP |
| **QuickBooks** | Revenue, expenses, AR aging, cash position | MCP (preferred) or CSV export |
| **Gmail** | Communication patterns with strategic partners | Automatic via integration |
| **Google Drive** | Prior board packets, historical context | Automatic via integration |

---

## Workflow Overview

### Phase 1: Data Collection (T-10 days)
- Query all data sources in parallel
- Validate data quality
- Flag gaps for user clarification

### Phase 2: Draft Generation (T-7 days)
- Generate all 5 documents
- Run cross-document consistency checks
- Present drafts with executive summaries

### Phase 3: Review & Refinement (T-7 to T-2 days)
- User reviews and provides feedback
- Iterative updates based on input
- Final approval confirmation

### Phase 4: Final DOCX Generation (T-2 days)
- Apply professional formatting
- Create complete board packet
- Save locally and to Google Drive

### Phase 5: Meeting Support (Meeting Day)
- Real-time motion tracking (optional)
- Live note-taking support (optional)

### Phase 6: Post-Meeting Follow-Up (T+2 days)
- Extract action items from votes
- Create Asana tasks
- Archive final materials

---

## Key Features

### Intelligent Synthesis
- Doesn't just report data, synthesizes insights
- Flags risks and opportunities proactively
- Cross-checks consistency across documents

### Format Compliance
- Exact adherence to 360's typography and spacing standards
- Professional DOCX output using python-docx
- Meeting information tables, motion tracking tables, section dividers

### Quality Assurance
- Cross-document consistency validation
- Data integrity checks
- Completeness verification
- Automated flag generation

### Interactive Review
- Presents drafts before finalizing
- Asks clarifying questions when data is ambiguous
- Incorporates user feedback iteratively
- Never ships without approval

---

## Configuration

### Required Asana Custom Fields

For optimal operation, ensure your Asana Client Delivery Hub has these custom fields:
- `contract_value` (Currency)
- `probability` (Number, 0-100)
- `stage` (Enum: Proposal, Negotiation, Signed, Delivered, Invoiced, Paid)
- `client_tier` (Enum: Tier 1 Strategic, Tier 2 Major, Tier 3 Standard)

**Fallback**: If custom fields are missing, the skill will prompt you for manual data entry.

### QuickBooks Integration

**Preferred**: MCP integration for real-time financial data

**Fallback**: Monthly CSV export (skill will prompt when needed)

---

## Customization

### Modify Templates

Edit files in `assets/templates/` to change default structures:
- `board_packet_cover.md` - Cover page layout
- `motion_sheet_template.md` - Motion tracking format

Changes persist across board meetings.

### Adjust Workflows

Edit reference files in `references/` to modify logic:
- `financial-dashboard.md` - Financial analysis rules
- `client-portfolio-health.md` - Health scoring criteria
- `strategic-initiatives.md` - Priority assessment logic
- `governance-compliance.md` - Compliance calendar
- `motion-preparation.md` - Motion drafting rules

### Change Formatting

Edit `assets/docx_utilities.py` to adjust:
- Typography (fonts, sizes, spacing)
- Table formatting
- Color schemes
- Document structure

---

## Troubleshooting

### "QuickBooks data unavailable"
**Solution**: Provide CSV export, skill will use that instead

### "Asana project hasn't been updated"
**Solution**: Skill will flag, you provide manual update in review phase

### "Can't find prior board materials"
**Solution**: Normal for first board packet, skill will note

### "Strategic partner status unclear"
**Solution**: Skill will ask specific clarifying questions

---

## Success Metrics

A successful board packet achieves:
- ✓ Generated in <10 minutes from user input
- ✓ Matches reference formatting exactly
- ✓ Requires no manual cleanup
- ✓ Can be used immediately in meeting
- ✓ Looks professionally produced
- ✓ Follows all user preferences (no em dashes!)
- ✓ Passes quality checklist

---

## Version History

**v1.0 (November 2025)**: Initial release
- 5 core documents
- 6-phase workflow
- Asana/QuickBooks/Gmail/Drive integration
- Professional DOCX formatting
- Quality assurance framework

---

## Support

**During use**: Ask Claude "I'm having trouble with [specific issue]"

**For modifications**: "Can you update [template/workflow] to include [X]?"

**For questions**: "What does the skill need from me right now?"

---

## License & Attribution

Built with care for Chandler Lewis and 360 Social Impact Studios
November 2025

This skill embodies 360's values:
- **Grounded + Visionary**: Data-driven but strategically synthesized
- **Clear and Reflective**: Professional communication without fluff
- **Substance Over Style**: Functional design serving governance excellence
- **Action-Ready**: Every output designed for immediate use

---

## Files Included

**Core**:
- `SKILL.md` - Main orchestration logic (6-phase workflow)

**References** (loaded just-in-time):
- `references/financial-dashboard.md` - Financial analysis workflow
- `references/client-portfolio-health.md` - Portfolio assessment workflow
- `references/strategic-initiatives.md` - Strategic progress tracking workflow
- `references/governance-compliance.md` - Governance tracking workflow
- `references/motion-preparation.md` - Motion drafting protocols

**Templates**:
- `assets/templates/board_packet_cover.md` - Cover page structure
- `assets/templates/motion_sheet_template.md` - Motion tracking format

**Utilities**:
- `assets/docx_utilities.py` - Python DOCX generation with proper formatting

**Documentation**:
- `README.md` - This file

---

## Quick Start

1. **Install the skill** (upload .skill file or copy directory)
2. **Trigger**: "Help me prep for the November 17 board meeting"
3. **Provide context**: Meeting type, agenda topics
4. **Review drafts**: Claude presents 5 draft documents
5. **Approve**: Claude generates final DOCX files
6. **Download**: Files ready in `/mnt/user-data/outputs/` and Google Drive

---

## Next Steps

After installation:
1. Run a test board prep cycle
2. Review output quality
3. Provide feedback for refinement
4. Adjust templates/workflows to your preferences
5. Use for February board meeting with improvements

---

*Skill designed to make board governance excellent, efficient, and strategic.*
