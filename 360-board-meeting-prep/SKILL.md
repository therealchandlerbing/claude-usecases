# 360 Board Meeting Prep Agent

## Skill Identity

**Name**: 360-board-meeting-prep
**Version**: 1.0
**Created**: November 2025
**For**: Chandler Lewis, 360 Social Impact Studios

## Skill Purpose

This skill transforms scattered organizational data into polished, governance-ready board meeting packets. It synthesizes financial, operational, strategic, and governance intelligence from Asana, QuickBooks, Gmail, and Google Drive into five professional documents that follow 360's exact formatting standards.

## When to Activate This Skill

Trigger this skill when the user requests:
- "Help me prep for the [date] board meeting"
- "Create a board packet for [date]"
- "Build board meeting materials"
- "Generate board documents"
- "I need to prepare for the board meeting"
- Any variation requesting board governance materials

Also trigger proactively:
- 10 days before scheduled board meeting dates (if calendar integrated)
- When user mentions "board meeting" in planning context

## Core Capabilities

1. **Multi-Source Data Intelligence**: Automatically pulls and synthesizes data from Asana, QuickBooks, Gmail, Google Drive
2. **Five Professional Documents**: Generates Financial Dashboard, Client Portfolio Health, Strategic Initiatives, Governance & Compliance, Motion Tracking
3. **Format Compliance**: Applies exact DOCX formatting per 360's technical specifications
4. **Quality Assurance**: Cross-document consistency checks, data validation, gap flagging
5. **Interactive Review**: Presents drafts for user approval before final generation
6. **Governance Tracking**: Creates action items in Asana post-meeting

## Skill Architecture

### Main Workflow (This File)
Orchestrates the 6-phase process from data collection to post-meeting follow-up.

### Specialized Reference Files
Load just-in-time when generating each document:
- `references/financial-dashboard.md` - Revenue, expenses, pipeline, cash flow logic
- `references/client-portfolio-health.md` - Relationship assessment, capacity analysis
- `references/strategic-initiatives.md` - Partnership tracking, strategic priorities
- `references/governance-compliance.md` - Action items, filings, board composition
- `references/motion-preparation.md` - Motion drafting and tracking protocols

### Document Templates
- `assets/templates/board_packet_cover.md` - Cover page structure
- `assets/templates/financial_dashboard_template.md` - Financial report layout
- `assets/templates/motion_sheet_template.md` - Voting record format

## 6-Phase Workflow

### Phase 1: Initial Consultation & Data Collection (T-10 days)

**Step 1.1: Gather Meeting Parameters**

Ask user:
1. What is the meeting date?
2. What type of meeting is this? (Annual, Quarterly, Special)
3. What are the key agenda topics?
4. Do you need motion tracking? (usually yes)
5. Are there any special topics requiring appendices?

**Step 1.2: Confirm Data Sources**

Check access to:
- Asana Client Delivery Hub: https://app.asana.com/0/portfolio/1211711475492498/1211712180134240
- Asana Board/Governance: https://app.asana.com/1/1210382795871981/project/1211794887178220/list/1211795122169239
- QuickBooks (via MCP or request CSV export)
- Gmail (automatic via integration)
- Google Drive (automatic via integration)

If QuickBooks MCP unavailable, say: "I'll need a QuickBooks export (Revenue, Expenses, AR Aging, Cash Position). Can you provide the most recent monthly data?"

**Step 1.3: Pull Base Data**

Execute data collection in parallel:

```python
# Asana Pipeline Data
pipeline_projects = asana_get_portfolio_items(portfolio_gid="1211712180134240")
# Extract: contract_value, probability, stage, client_tier, last_updated

# Asana Action Items
governance_tasks = asana_get_tasks(project_gid="1211794887178220", completed=False)
# Extract: task name, assignee, due_date, status

# Gmail Communication Patterns (last 60 days)
strategic_partners = ["SpacePlan", "GenIP", "ScienceLink", "NanoBioPlus", "CNEN"]
for partner in strategic_partners:
    interaction_count = search_gmail_messages(query=f"from:*{partner}* OR to:*{partner}*", after="60 days ago")

# Google Drive Historical Context
prior_packets = google_drive_search(query="Board Packet", folder="Board Materials")

# QuickBooks Financial Data
if quickbooks_mcp_available:
    revenue_ytd = quickbooks_query("revenue", year=2025)
    expenses_ytd = quickbooks_query("expenses", year=2025)
    ar_aging = quickbooks_query("ar_aging")
    cash_position = quickbooks_query("cash")
else:
    # User will provide CSV, process when received
    prompt_for_quickbooks_export()
```

**Step 1.4: Data Validation & Gap Identification**

Check for:
- Projects not updated in >14 days (flag for user clarification)
- Missing custom fields in Asana (contract_value, probability)
- Incomplete financial data
- Strategic partners with <2 email interactions (relationship health flag)

Present gaps to user: "I found [X] projects that haven't been updated recently. Can you provide status on: [list]?"

---

### Phase 2: Draft Document Generation (T-7 days)

**Step 2.1: Generate Financial Dashboard**

Load `references/financial-dashboard.md` for detailed logic.

Key sections:
- Executive Summary (1 paragraph synthesizing overall financial health)
- Revenue Analysis (YTD vs. $40K target, by source)
- Expense Analysis (by category, variance from budget)
- Cash Flow & Receivables (AR aging, cash runway)
- Pipeline Valuation (weighted by probability)
- Risk Assessment (flags for >60 day AR, <6 month runway, >20% variance)

Output: Draft Financial Dashboard (MD format for review)

**Step 2.2: Generate Client Portfolio Health Report**

Load `references/client-portfolio-health.md` for detailed logic.

Key sections:
- Executive Summary
- Tier 1 Strategic Partner Deep Dives (SpacePlan, GenIP, ScienceLink, NanoBioPlus, CNEN)
- Major Clients Summary Table
- Portfolio Analytics (concentration, retention, acquisition)
- Capacity Analysis (team utilization)

For each Tier 1 partner:
- Relationship status (green/yellow/red)
- Recent activity summary
- Contract value and stage
- Next milestones
- Risks/opportunities

Output: Draft Client Portfolio Health Report (MD format)

**Step 2.3: Generate Strategic Initiatives Update**

Load `references/strategic-initiatives.md` for detailed logic.

Key sections:
- Executive Summary (4 strategic priorities)
- Initiative Deep Dives (major partnerships, programs)
- Strategic Priority Dashboard

Four priorities from Motion #7:
1. Expand program reach
2. Diversify funding sources
3. Build strategic partnerships (Brazil, China, technology)
4. Convert pipeline to revenue

Output: Draft Strategic Initiatives Update (MD format)

**Step 2.4: Generate Governance & Compliance Report**

Load `references/governance-compliance.md` for detailed logic.

Key sections:
- Action Item Status (from prior meeting)
- Filing & Compliance Calendar (Form 990-EZ, conflict forms)
- Board Composition & Officers
- Committee Activity (if applicable)

Output: Draft Governance & Compliance Report (MD format)

**Step 2.5: Generate Motion Tracking Sheet**

Load `references/motion-preparation.md` for detailed logic.

Based on meeting type and agenda, create pre-drafted motions:
- Standard motions (approve agenda, officer elections if annual, adjournment)
- Context-specific motions (strategic decisions requiring approval)

Output: Draft Motion Tracking Sheet (MD format)

**Step 2.6: Cross-Document Consistency Check**

Validate:
- Financial revenue = sum of client portfolio contract values
- Strategic initiatives capacity matches client portfolio utilization
- Governance action items referenced in relevant sections
- Motion language matches agenda items

Flag any inconsistencies for user review.

**Step 2.7: Present Drafts to User**

Display all 5 draft documents with:
- Executive summaries highlighted
- Gaps flagged with "⚠️" markers
- Questions for user clarification
- Cross-references between documents

Say: "I've generated draft board materials. Please review the following documents and provide any corrections, additions, or context I'm missing:

1. **Financial Dashboard** - [summary]
2. **Client Portfolio Health** - [summary]
3. **Strategic Initiatives** - [summary]
4. **Governance & Compliance** - [summary]
5. **Motion Tracking Sheet** - [summary]

Key questions for you:
- [List specific gaps or clarification needs]

Would you like to review these now, or should I proceed with any immediate corrections you have?"

---

### Phase 3: Review & Refinement (T-7 to T-2 days)

**Step 3.1: Receive User Feedback**

Listen for:
- Corrections: "Actually, the SpacePlan delay is because..."
- Additions: "Add a note about the NanoBioPlus CuriBio partnership"
- Context: "The CNEN relationship is stronger than emails suggest - we had in-person meeting"
- Approval: "Looks good" or "Ready for final generation"

**Step 3.2: Update Drafts**

For each piece of feedback:
1. Update the relevant document section
2. Check if update affects other documents (cross-document consistency)
3. Re-run validation checks
4. Present updated section to user

**Step 3.3: Iterative Refinement**

Continue review cycles until user approves all 5 documents.

Track changes: "Updated sections: [list]. Remaining questions: [list]."

**Step 3.4: Final Approval Confirmation**

When user signals readiness, confirm: "All 5 documents approved for final generation. I'll now create the professionally formatted DOCX files and store them in Google Drive. This will take about 10 minutes. Proceed?"

---

### Phase 4: Final DOCX Generation (T-2 days)

**Step 4.1: Prepare Python Environment**

Ensure python-docx library available:
```python
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
```

**Step 4.2: Create Complete Board Packet**

Generate single master DOCX file containing all sections:

1. **Cover Page** (from template)
2. **Meeting Information Table** (4x2, gray labels)
3. **Motion Tracking Sheet** (if applicable)
4. Section divider (• • •)
5. **Financial Dashboard** (full content)
6. Section divider (• • •)
7. **Client Portfolio Health Report** (full content)
8. Section divider (• • •)
9. **Strategic Initiatives Update** (full content)
10. Section divider (• • •)
11. **Governance & Compliance Report** (full content)
12. Appendices (if applicable)

**Step 4.3: Apply Exact Formatting**

Use formatting specifications from user's guides:

**Typography**:
- Title: Arial 24pt Bold
- Subtitle: Arial 13pt Regular
- Heading 1: Arial 14pt Bold (18pt before, 6pt after)
- Heading 2: Arial 12pt Bold (12pt before, 6pt after)
- Heading 3: Arial 11pt Bold (6pt before, 6pt after)
- Body: Calibri 11pt Regular

**Meeting Information Table**:
```python
def create_meeting_info_table(doc, date, time, location, meeting_type):
    table = doc.add_table(rows=4, cols=2)
    table.style = 'Table Grid'

    info = [
        ("Date:", date),
        ("Time:", time),
        ("Location:", location),
        ("Meeting Type:", meeting_type)
    ]

    for i, (label, content) in enumerate(info):
        row = table.rows[i]

        # Left cell (gray background, bold)
        left_cell = row.cells[0]
        left_cell.text = label
        set_cell_background(left_cell, 'ECF0F1')
        left_cell.paragraphs[0].runs[0].font.bold = True

        # Right cell (white background)
        right_cell = row.cells[1]
        right_cell.text = content

    # Remove table borders
    for row in table.rows:
        for cell in row.cells:
            set_cell_border(cell, top={"sz": 0}, bottom={"sz": 0},
                          start={"sz": 0}, end={"sz": 0})

    return table

def set_cell_background(cell, color_hex):
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), color_hex)
    cell._element.get_or_add_tcPr().append(shading_elm)
```

**Motion Tracking Tables**:
```python
def create_motion_table(doc, motion_num, title, motion_text):
    doc.add_paragraph()  # Spacing

    table = doc.add_table(rows=2, cols=1)
    table.style = 'Table Grid'

    # Row 1: Title (bold)
    title_cell = table.rows[0].cells[0]
    title_para = title_cell.paragraphs[0]
    title_run = title_para.add_run(f'MOTION {motion_num}: {title}')
    title_run.font.bold = True

    # Row 2: Details
    details_cell = table.rows[1].cells[0]

    # Motion text (italic, quoted)
    motion_para = details_cell.paragraphs[0]
    motion_run = motion_para.add_run(f'"{motion_text}"')
    motion_run.font.italic = True

    details_cell.add_paragraph()
    details_cell.add_paragraph('Moved by: ______________')
    details_cell.add_paragraph('Seconded by: ______________')
    vote_para = details_cell.add_paragraph('Vote: ')
    vote_para.add_run('☐ Approved  ☐ Denied  ☐ Abstained')

    return table
```

**Section Dividers**:
```python
def add_section_divider(doc):
    para = doc.add_paragraph('• • •')
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_format = para.paragraph_format
    para_format.space_before = Pt(18)
    para_format.space_after = Pt(18)
```

**Step 4.4: Quality Check Before Save**

Verify:
- [ ] All headings use correct styles (not manual formatting)
- [ ] Meeting info table has gray labels (#ECF0F1)
- [ ] Motion tables have 1pt black borders
- [ ] Section dividers are centered (• • •)
- [ ] Spacing is consistent (18pt before H1, etc.)
- [ ] Checkboxes use Unicode ☐ (U+2610)
- [ ] No em dashes (critical user preference)
- [ ] Cross-document data consistency maintained

**Step 4.5: Save and Store**

File naming: `360_Board_Packet_[Month]_[Year]_Professional.docx`

Save locations:
1. Local: `/mnt/user-data/outputs/`
2. Google Drive: `/Board Materials/[YYYY-MM]/` (create folder if needed)

**Step 4.6: Provide Download Link**

Say: "Board packet generated successfully!

**File**: `360_Board_Packet_[Month]_[Year]_Professional.docx`

**Sections included**:
1. Cover page with meeting information
2. Motion tracking sheet ([X] motions)
3. Financial Dashboard
4. Client Portfolio Health Report
5. Strategic Initiatives Update
6. Governance & Compliance Report
[7. Appendices - if applicable]

**Download**: [provide local path]
**Google Drive**: [provide Drive link if uploaded]

**Summary**:
- [Brief executive summary of key points]
- [Any flags or items requiring board attention]

Would you like me to make any adjustments before you distribute this to the board?"

---

### Phase 5: Meeting Support (Meeting Day)

**Step 5.1: Pre-Meeting Readiness**

If user requests, provide:
- Quick summary of key decisions needed
- Motion sequence reminder
- Action item tracking template

**Step 5.2: Real-Time Support (Optional)**

If user shares screen or transcript during meeting:
- Track which motions have been voted on
- Note any amendments to motions
- Capture ad hoc motions not in original tracking sheet
- Record vote results

**Step 5.3: Motion Tracking Completion**

After meeting, ask: "Would you like me to help complete the motion tracking sheet with the vote results?"

If yes, request:
- Who moved each motion
- Who seconded
- Vote result (Approved/Denied/Abstained)
- Any amendments to motion language

Update DOCX file with completed information.

---

### Phase 6: Post-Meeting Follow-Up (T+2 days)

**Step 6.1: Action Item Extraction**

From completed motion tracking sheet and any meeting notes:
1. Identify all approved motions requiring action
2. Extract specific action items with owners and deadlines
3. Note any new governance requirements

**Step 6.2: Create Asana Tasks**

For each action item, create task in Board/Governance project:
```python
asana_create_task(
    project_gid="1211794887178220",
    name="[Action item description]",
    assignee="[owner]",
    due_date="[deadline]",
    notes="From Board Meeting [date], Motion #[X]: [context]"
)
```

**Step 6.3: Meeting Minutes Support (Optional)**

If user requests: "Would you like me to draft meeting minutes based on the motion tracking sheet and discussion notes?"

If yes, create minutes document:
- Meeting logistics (date, time, attendees)
- Motions presented and vote results
- Key discussion points (from notes)
- Action items assigned
- Next meeting date

**Step 6.4: Archive Final Materials**

1. Save completed motion tracking sheet (with vote results)
2. Update Google Drive folder with final versions
3. Create summary document: "Board_Meeting_[Date]_Summary.md" with:
   - Motions passed/failed
   - Action items created
   - Key decisions
   - Follow-up needed

**Step 6.5: Confirmation to User**

Say: "Post-meeting follow-up complete!

**Action items created in Asana**: [X] tasks
- [List tasks with owners]

**Materials archived**:
- Completed motion tracking sheet
- [Meeting minutes - if created]
- Executive summary

**Next board meeting**: [date from governance calendar]

Is there anything else you need from this meeting cycle?"

---

## Data Source Integration Specifications

### Asana

**Client Delivery Hub Portfolio**:
- URL: https://app.asana.com/0/portfolio/1211711475492498/1211712180134240
- Tools: `asana_get_items_for_portfolio`, `asana_get_project`
- Expected custom fields: `contract_value`, `probability`, `stage`, `client_tier`
- Fallback: If custom fields missing, prompt user for manual data

**Board/Governance Project**:
- URL: https://app.asana.com/1/1210382795871981/project/1211794887178220/list/1211795122169239
- Tools: `asana_get_tasks`, `asana_search_tasks`, `asana_create_task`
- Used for: Action item tracking, compliance calendar, governance tasks

### QuickBooks

**Preferred: MCP Integration**
- Real-time financial data
- No manual exports
- Automatic currency conversion if needed

**Fallback: CSV Export**
- Request from user when MCP unavailable
- Expected exports: Revenue, Expenses, AR Aging, Cash Position
- Flag data source age in reports

**Data Points**:
- Revenue YTD by category
- Expenses YTD by category
- Accounts receivable aging (0-30, 31-60, 61-90, 90+ days)
- Cash position
- Budget vs. actual (if available)

### Gmail

**Communication Pattern Analysis**:
- Tool: `search_gmail_messages`, `read_gmail_thread`
- Search timeframe: Last 60 days
- Strategic partners: SpacePlan, GenIP, ScienceLink, NanoBioPlus, CNEN
- Metrics: Interaction count, last contact date
- Privacy: Metadata only (count, dates), not content

**Health Flags**:
- <2 interactions/month for Tier 1 partner = yellow flag
- 0 interactions in 60 days for Tier 1 = red flag

### Google Drive

**Historical Context**:
- Tool: `google_drive_search`, `google_drive_fetch`
- Search: Prior board packets in `/Board Materials/`
- Extract: Budget figures, prior strategic commitments, action items
- Use: Year-over-year comparison, commitment tracking

**Storage**:
- Tool: `google_drive_upload`
- Destination: `/Board Materials/[YYYY-MM]/`
- Create folder if doesn't exist

---

## Quality Assurance Framework

### Automated Checks (Run Before Final Generation)

**Cross-Document Consistency**:
```python
def validate_consistency(financial_data, portfolio_data, strategic_data):
    checks = []

    # Revenue alignment
    financial_revenue = sum(financial_data['revenue_by_source'].values())
    portfolio_revenue = sum([p['contract_value'] for p in portfolio_data if p['stage'] == 'Signed'])
    if abs(financial_revenue - portfolio_revenue) > 1000:
        checks.append(f"⚠️ Revenue mismatch: Financial={financial_revenue}, Portfolio={portfolio_revenue}")

    # Capacity alignment
    strategic_capacity = strategic_data['team_utilization']
    portfolio_capacity = calculate_portfolio_capacity(portfolio_data)
    if abs(strategic_capacity - portfolio_capacity) > 5:
        checks.append(f"⚠️ Capacity mismatch: Strategic={strategic_capacity}%, Portfolio={portfolio_capacity}%")

    return checks
```

**Data Integrity**:
- Revenue sources sum to total
- Pipeline math correct (value × probability)
- Receivables aging adds up to total AR
- Capacity utilization ≤100%
- All percentages between 0-100

**Completeness**:
- All 4 strategic priorities addressed
- All Tier 1 partners covered
- All prior action items accounted for
- All agenda items have motions (if motion tracking included)

**Flag Criteria**:
- ⚠️ Budget variance >20%
- ⚠️ Receivables >60 days outstanding
- ⚠️ Cash runway <6 months
- ⚠️ Asana project not updated in >14 days
- ⚠️ Low engagement with Tier 1 partner
- ⚠️ Capacity utilization >90%
- ⚠️ Action item overdue

### User Review Checklist

Present before final generation:

"Please verify before I create final documents:

**Financial**:
□ Revenue numbers match your understanding
□ Major variances are explained
□ Pipeline probabilities are realistic
□ Cash position is accurate

**Client Portfolio**:
□ Partner statuses reflect reality
□ Relationship health indicators are correct
□ Capacity numbers account for all commitments
□ No surprises for the board

**Strategic**:
□ Progress updates are accurate
□ Next milestones are achievable
□ Risks are surfaced appropriately
□ Board decisions are clearly flagged

**Governance**:
□ All action items are accounted for
□ Compliance deadlines are correct
□ Board composition is current
□ No governance gaps

**Motions**:
□ Language is specific enough to execute
□ Terms and conditions are accurate
□ All agenda items are covered
□ Sequence makes sense

Ready to generate final board packet?"

---

## Error Handling & Fallback Strategies

### Data Source Unavailable

**QuickBooks MCP Down**:
- Prompt user for CSV export
- Flag in all financial documents: "Using QuickBooks export from [date]"
- Proceed with available data

**Asana API Issues**:
- Use cached data if available
- Prompt user for manual updates on critical projects
- Flag: "Asana data as of [last successful pull]"

**Gmail/Drive Unavailable**:
- Skip communication pattern analysis
- Request manual input on partner engagement
- Use prior board packet data if available

### Incomplete Data

**Missing Custom Fields**:
- Notify user which fields are missing
- Provide manual entry template
- Continue with available data, flag gaps

**Stale Project Data**:
- List projects not updated in >14 days
- Ask user for status update
- Proceed with last known data if user unavailable

### Format Generation Errors

**DOCX Library Issues**:
- Fall back to rich markdown format
- Provide conversion instructions
- Note: "Please convert to DOCX using Word's markdown import"

**Table Formatting Problems**:
- Use simplified table structure
- Maintain data integrity over perfect formatting
- Note issue for future resolution

---

## Customization & Flexibility

### User Can Request

**Format Changes**:
- "Make the financial dashboard a table instead of narrative"
- "Add a fundraising section"
- "Omit governance report this time"

**Detail Level**:
- "Give me a deeper dive on NanoBioPlus partnership"
- "Simplify the financial section"
- "Expand the strategic initiatives appendix"

**Reordering**:
- "Put strategic initiatives before financials"
- "Move motion tracking to the end"

**Additional Sections**:
- "Add a fundraising progress section"
- "Include a program impact summary"
- "Add an appendix on the Brazil partnership"

### Template Editing

User can modify templates in `assets/templates/` for persistent changes:
- Adjust section structure
- Add/remove standard sections
- Change formatting preferences (within style guide bounds)

---

## Success Metrics

A successful board packet achieves:
- ✓ Generated in <10 minutes from user input
- ✓ Matches reference formatting exactly
- ✓ Requires no manual cleanup
- ✓ Can be used immediately in meeting
- ✓ Looks professionally produced
- ✓ Follows all user preferences
- ✓ Passes quality checklist
- ✓ Board members can find any information in <30 seconds
- ✓ Recording secretary can complete motion tracking without confusion
- ✓ Action items flow seamlessly to Asana

---

## Progressive Loading Strategy

To manage context efficiently, load reference files only when needed:

**Generating Financial Dashboard**:
```
Load references/financial-dashboard.md
Follow specialized logic
Unload when complete
```

**Generating Client Portfolio**:
```
Load references/client-portfolio-health.md
Follow specialized logic
Unload when complete
```

This keeps the active context lean while maintaining deep domain expertise.

---

## User Communication Style

### During Data Collection:
"Pulling data from Asana, QuickBooks, and Gmail. This will take about 2 minutes..."

### Presenting Gaps:
"I found [X] items that need your input:
- [Specific question 1]
- [Specific question 2]

Can you clarify these before I generate drafts?"

### During Review:
"Here's the draft Financial Dashboard. Key highlights:
- Revenue: $[X] vs $40K target ([X]%)
- Cash runway: [X] months
- Pipeline: $[X] weighted

⚠️ Flagged items:
- [Issue 1]
- [Issue 2]

What changes or additions do you need?"

### Confirming Actions:
"I'm about to:
1. Generate 5 professional DOCX documents
2. Store in Google Drive /Board Materials/November-2025/
3. Create motion tracking sheet with [X] pre-drafted motions

This will take about 10 minutes. Proceed?"

### Celebrating Success:
"Board packet complete! All 5 documents ready for distribution. Key highlights for the board:
- [Insight 1]
- [Insight 2]
- [Insight 3]

Download link: [path]"

---

## Integration with Other Skills

### design-director (if available):
After DOCX generation, optionally apply enhanced visual design:
"Would you like me to apply enhanced visual design to the packet? This will add professional typography refinements and spacing optimizations."

### meeting-transcript-processor (if available):
Post-meeting: "I can process the meeting transcript to extract action items automatically. Share the transcript or recording?"

### weekly-tracker-generator (if available):
Cross-reference client status for consistency: "I'm checking the weekly tracker to ensure client statuses align with the board packet. One moment..."

---

## Skill Maintenance & Evolution

### Version History
- v1.0 (Nov 2025): Initial release with 5 core documents

### Update Triggers
- User feedback on formatting
- New organizational priorities
- Additional data sources
- Improved automation capabilities

### Continuous Improvement
After each board meeting, ask: "What worked well in this board packet? What should I improve for the next meeting?"

Store feedback in skill metadata for iterative refinement.

---

## Final Checklist Before Delivery

Before presenting final board packet, verify:

**Content Quality**:
- [ ] All data points are accurate and current
- [ ] Executive summaries are crisp and actionable
- [ ] Flags/risks are clearly surfaced
- [ ] Cross-document consistency maintained
- [ ] No TK/TODO placeholders remaining

**Format Quality**:
- [ ] All Word styles applied correctly
- [ ] Tables formatted per specifications
- [ ] Spacing consistent throughout
- [ ] No em dashes (critical preference)
- [ ] Checkboxes are Unicode ☐
- [ ] Section dividers centered (• • •)

**Governance Quality**:
- [ ] All motions align with agenda
- [ ] Motion language is specific and actionable
- [ ] Action items from prior meeting addressed
- [ ] Compliance deadlines accurate
- [ ] Next meeting date confirmed

**Delivery Quality**:
- [ ] File saved to correct location
- [ ] Google Drive upload successful (if applicable)
- [ ] Download link provided
- [ ] Executive summary presented
- [ ] User questions answered

---

## Ready to Activate

This skill is now ready to generate world-class board meeting packets for 360 Social Impact Studios.

**Next step**: User says "Help me prep for the [date] board meeting" and the workflow begins.

---

*Built with care for Chandler Lewis and 360 Social Impact Studios*
*Skill version 1.0 | November 2025*
