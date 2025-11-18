# Sales Automator Installation Guide

Step-by-step instructions for adding the Sales Automator skill to your Claude workspace.

## Installation Method

This skill is installed as a **Claude Project Skill**. It will be available whenever you're working in that specific project.

---

## Step 1: Create a New Claude Project

1. Open Claude at [claude.ai](https://claude.ai)
2. Click "Projects" in the left sidebar
3. Click "+ New Project"
4. Name it: **"Sales Automation"** (or your preferred name)
5. (Optional) Add a description: "Sales outreach automation with relationship intelligence, deal pipeline tracking, and competitive research"

---

## Step 2: Add the Skill Files

### Option A: Upload as Project Files (Recommended)

1. In your Sales Automation project, click "Add Content" → "Upload Files"
2. Upload these files from the `sales-automator` folder:
   - `SKILL.md`
   - `README.md`
   - `docs/QUICK-START.md`
   - `docs/DATA-SOURCES.md`
   - `references/REFERENCE.md`
   - (Optional) `docs/INSTALLATION.md` (this file)

### Option B: Create Skill Manually

1. In your Sales Automation project, click "Project Knowledge"
2. Click "+ Add Knowledge"
3. Select "Create Document"
4. Copy the contents of `SKILL.md` into the document
5. Name it: "sales-automator"
6. Repeat for `README.md`, `QUICK-START.md`, `DATA-SOURCES.md`, `REFERENCE.md`

---

## Step 3: Configure Project Settings

1. Click "Project Settings" (gear icon)
2. Under "Model", select: **Claude Sonnet 4.5** (recommended for best performance)
3. Under "Instructions", add:

```
This project is for sales automation. Always use the sales-automator skill when:
- User asks to create outreach or email sequences
- User requests research on prospects or companies
- User asks to check pipeline or track deals
- User wants to generate proposals or case studies
- User asks about sales performance or metrics

Reference SKILL.md for complete workflow details.
Reference REFERENCE.md for templates and examples.
Reference DATA-SOURCES.md for data setup guidance.
```

4. Save settings

---

## Step 4: Enable Required Tools

The sales-automator skill requires these Claude tools to be enabled in your project:

### Enable Asana Integration

1. In Project Settings → Integrations
2. Find "Asana" and click "Enable"
3. Authenticate your Asana account
4. Grant Claude permission to:
   - Read workspaces, projects, tasks
   - Create and update tasks
   - Search across your workspace

**Test it**:
```
In your Sales Automation project, type:
"List my Asana workspaces"
```
You should see your workspace(s) returned.

### Enable Gmail Integration

1. In Project Settings → Integrations
2. Find "Gmail" and click "Enable"
3. Authenticate your Google account
4. Grant Claude permission to:
   - Read emails
   - Search email
   - Read profile information

**Test it**:
```
"Show me my Gmail profile"
```
You should see your email address and account info.

### Enable Google Drive Integration

1. In Project Settings → Integrations
2. Find "Google Drive" and click "Enable"
3. Authenticate your Google account (same account as Gmail)
4. Grant Claude permission to:
   - Read files and folders
   - Search across Drive

**Test it**:
```
"Search my Drive for files modified this week"
```
You should see recent files.

### Enable Google Calendar Integration

1. In Project Settings → Integrations
2. Find "Google Calendar" and click "Enable"
3. Authenticate your Google account (same account as Gmail/Drive)
4. Grant Claude permission to:
   - Read calendar events
   - Search events

**Test it**:
```
"Show me my calendar events for today"
```
You should see today's events.

### Enable Web Search

1. In Project Settings → Integrations
2. Find "Web Search" and click "Enable"
3. No authentication needed

**Test it**:
```
"Search the web for recent news about Tesla"
```
You should see search results.

---

## Step 5: Set Up Data Sources

Follow the [DATA-SOURCES.md](DATA-SOURCES.md) guide to set up:

1. **Asana Sales Pipeline project** with custom fields
2. **Google Drive Sales Assets folder** with case studies and templates
3. **Gmail organization** (optional labels)
4. **Calendar naming conventions**

**Quick setup checklist**:
- [ ] Create "Sales Pipeline" project in Asana
- [ ] Add custom fields: Deal Stage, Deal Value, Close Date, Lead Source, Next Action
- [ ] Create "Sales Assets" folder in Google Drive
- [ ] Add at least 2 case studies to Drive
- [ ] Create proposal template in Drive

---

## Step 6: Test the Installation

Once everything is set up, test the skill with these commands:

### Test 1: Pipeline Check
```
Check my Sales Pipeline in Asana
```

**Expected**: Claude finds your Sales Pipeline project and lists active deals (or confirms it's empty if you haven't added any yet).

### Test 2: Research Capability
```
Research Tesla for a partnership opportunity
```

**Expected**: Claude uses web search to research Tesla, provides company overview, recent news, strategic priorities.

### Test 3: Drive Search
```
Search my Drive for case studies
```

**Expected**: Claude finds your Sales Assets folder and lists case studies available.

### Test 4: Email Sequence Generation
```
Create cold outreach for SpaceX
```

**Expected**: Claude:
1. Researches SpaceX via web search
2. Checks if you have any past interactions (Gmail, conversations)
3. Generates 5-email sequence with personalization
4. Creates deal task in Asana (or asks if you want to)

If all 4 tests pass, your installation is complete!

---

## Step 7: Optional Customizations

### Custom Project Instructions

You can add specific instructions to your Project Settings → Instructions:

**Example additions**:
```
For outreach emails:
- Always include a case study mention by Email 2
- Keep emails under 150 words
- Use subject lines that create curiosity, not hype
- Never use "reach out" or "circle back" phrases

For proposals:
- Always include ROI calculation
- Reference at least 2 case studies
- Include 3 pricing tiers when possible

For pipeline tracking:
- Flag any deal in Discovery > 14 days as stuck
- Flag any deal in Proposal > 30 days as stuck
- Weekly pipeline review every Monday
```

### Custom Email Templates

Add your own templates to the REFERENCE.md file:
1. Edit REFERENCE.md in your project files
2. Add your templates under "Email Sequence Templates"
3. Save changes

Claude will now have access to your custom templates.

### Integration with Other Skills

If you have other skills in your workspace, you can reference them:

**Example**:
```
When generating proposals, also use design-director skill to elevate the visual quality of the proposal document.

When research is needed for international partners, consider cultural context from smart-email-composer skill.
```

Add these instructions to Project Settings → Instructions.

---

## Troubleshooting Installation

### Issue: Claude doesn't recognize the skill

**Diagnosis**: Skill file not uploaded correctly

**Solution**:
1. Verify `SKILL.md` is in Project Knowledge
2. Check that file name is exactly `SKILL.md` (case-sensitive)
3. Re-upload if necessary
4. Try explicitly: "Use the sales-automator skill to check my pipeline"

### Issue: Tools not working (Asana, Gmail, etc.)

**Diagnosis**: Integration not enabled or authentication failed

**Solution**:
1. Go to Project Settings → Integrations
2. Verify each required tool shows as "Enabled"
3. If not, click "Enable" and complete authentication
4. Test each tool individually with simple commands
5. If still failing, disconnect and reconnect the integration

### Issue: Claude can't find Asana project or Drive files

**Diagnosis**: Permissions or naming mismatch

**Solution**:
1. **For Asana**:
   - Verify project name is exactly "Sales Pipeline"
   - Check that you have access to the workspace
   - Try: "Search Asana for all projects" to see what's available

2. **For Drive**:
   - Verify folder is not in "Shared with me" (needs to be in "My Drive")
   - Check folder permissions
   - Try: "Search Drive for all folders" to see what's accessible

### Issue: Outreach emails are too generic

**Diagnosis**: Not enough context provided or data sources not populated

**Solution**:
1. Ensure Drive has case studies uploaded
2. Provide more context in your request: "Create outreach for [Company] focusing on [specific value prop]"
3. Ask Claude to research deeper: "Find more details about [Company]'s recent initiatives"

### Issue: Can't create deals in Asana

**Diagnosis**: Missing custom fields or permissions

**Solution**:
1. Verify Sales Pipeline project has all required custom fields
2. Check that you have edit permissions on the project
3. Try creating a task manually first to verify permissions
4. Manually provide task details if automation fails

---

## Maintenance & Updates

### Updating the Skill

When you want to update the skill with new features or templates:

1. Edit `SKILL.md`, `REFERENCE.md`, or other files in Project Knowledge
2. Save changes
3. Changes take effect immediately (no need to restart)

### Adding New Templates

1. Edit `REFERENCE.md` in Project Knowledge
2. Add your new template under appropriate section
3. Save
4. Test: "Show me the new [template name] template"

### Removing the Skill

If you need to remove or disable the skill:

1. Go to Project Knowledge
2. Find skill files (`SKILL.md`, etc.)
3. Click "..." → "Delete"
4. Confirm deletion

---

## Advanced Setup

### Multi-Project Setup

If you have multiple Claude projects and want sales-automator in all of them:

**Option 1: Duplicate Project**
1. In Projects view, find your Sales Automation project
2. Click "..." → "Duplicate"
3. Rename duplicated project
4. All skills and settings are copied

**Option 2: Create Shared Skills Folder**
1. Store skill files in Google Drive "Claude Skills" folder
2. Share Drive folder with Claude in each project
3. Add as Project Knowledge source
4. Skills available across all projects with access

### Team Setup

If multiple team members use Claude for sales:

1. **Shared Asana Workspace**:
   - Create shared Sales Pipeline project
   - Everyone has access to same deals

2. **Shared Drive Assets**:
   - Create team Drive folder for Sales Assets
   - Everyone uses same case studies, templates

3. **Individual Gmail/Calendar**:
   - Each person connects their own accounts
   - Personal email history and calendar

4. **Standardized Skill**:
   - Share same `SKILL.md` file across team
   - Everyone uses consistent approach

---

## Installation Checklist

Before marking installation complete, verify:

- [ ] Claude Project created
- [ ] Skill files uploaded (`SKILL.md`, `README.md`, `QUICK-START.md`, `DATA-SOURCES.md`, `REFERENCE.md`)
- [ ] Project settings configured (model, instructions)
- [ ] Asana integration enabled and authenticated
- [ ] Gmail integration enabled and authenticated
- [ ] Google Drive integration enabled and authenticated
- [ ] Google Calendar integration enabled and authenticated
- [ ] Web Search enabled
- [ ] Sales Pipeline project created in Asana with custom fields
- [ ] Sales Assets folder created in Drive with case studies
- [ ] Test 1 passed (Pipeline check)
- [ ] Test 2 passed (Research capability)
- [ ] Test 3 passed (Drive search)
- [ ] Test 4 passed (Email sequence generation)

**If all items checked, installation is complete. Proceed to [QUICK-START.md](QUICK-START.md) for your first campaign.**

---

## Getting Help

If you encounter issues during installation:

1. Review [DATA-SOURCES.md](DATA-SOURCES.md) for data setup troubleshooting
2. Review [QUICK-START.md](QUICK-START.md) for usage guidance
3. Check Project Settings → Integrations to verify all tools are enabled
4. Try commands incrementally (test each tool individually before complex workflows)
5. Ask Claude directly: "Help me troubleshoot [specific issue]"

---

## Next Steps After Installation

1. **Complete Quick Setup**: Follow [QUICK-START.md](QUICK-START.md) 5-minute setup
2. **Run First Campaign**: Use Quick Start guide to create your first outreach sequence
3. **Explore Templates**: Review [REFERENCE.md](../references/REFERENCE.md) for comprehensive examples
4. **Optimize Data Sources**: Deep dive into [DATA-SOURCES.md](DATA-SOURCES.md) for advanced setup
5. **Schedule Regular Reviews**: Set weekly pipeline reviews with Claude

**Welcome to intelligent sales automation.**
