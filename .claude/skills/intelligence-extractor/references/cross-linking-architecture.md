# Cross-Linking Architecture: Three Intelligence Systems

**Purpose:** Defines how Partnership Intelligence, Funding Intelligence, and Stakeholder Intelligence interconnect to create a comprehensive relationship management ecosystem.

**Last Updated:** November 2025

---

## Table of Contents

1. [Conceptual Relationship Model](#conceptual-relationship-model)
2. [Technical Linking Mechanisms](#technical-linking-mechanisms)
3. [Information Flow Patterns](#information-flow-patterns)
4. [Workflow Integration Examples](#workflow-integration-examples)
5. [Dashboard Views](#dashboard-views)
6. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
7. [Implementation Roadmap](#implementation-roadmap)
8. [Success Metrics](#success-metrics)

---

## Conceptual Relationship Model

### The Three Layers

```
┌──────────────────────────────────────────────────────────────┐
│                    STAKEHOLDER INTELLIGENCE                   │
│                        (WHO layer)                            │
│  Individual people, their patterns, relationships, influence  │
└────────┬────────────────────────┬────────────────────────────┘
         │                        │
         │ Informs both           │ Informs both
         │                        │
         v                        v
┌─────────────────────┐    ┌─────────────────────┐
│   PARTNERSHIP       │◄───┤   FUNDING           │
│   INTELLIGENCE      │───►│   OPPORTUNITY       │
│   (HOW layer)       │    │   INTELLIGENCE      │
│                     │    │   (RESOURCES layer) │
│  Organizations,     │    │                     │
│  collaboration      │    │  Money, grants,     │
│  patterns, synergy  │    │  investor patterns  │
└─────────────────────┘    └─────────────────────┘
```

### Core Principle

**Stakeholders are the connective tissue.** Every partnership and funding opportunity involves specific people. Understanding those people (Stakeholder Intelligence) makes you more effective at both partnership development and fundraising.

### Why This Architecture Matters

1. **Partnership Intelligence** answers: *What organizations should we work with?*
2. **Funding Intelligence** answers: *What resources can we access?*
3. **Stakeholder Intelligence** answers: *Who are the people who make it happen?*

Without linking these systems, you miss critical insights:
- You meet a program officer but don't connect them to the partnership they could enable
- You pursue a partnership without realizing which funder cares about it
- You know a stakeholder but don't see how they connect multiple opportunities

---

## Technical Linking Mechanisms

### 1. Task Relationships (Primary Connection Method)

Use Asana's built-in task relationships to create explicit links between the three intelligence systems.

#### From Partnership Task → Related Items

Link to:
- **Relevant Stakeholder tasks** (key contacts at partner organization)
- **Relevant Funding tasks** (if partnership could unlock funding)

**Example:**
```
Partnership Task: "InovaEduK - Educational Systems Partnership"
  ├─ Links to Stakeholder: "Maria Silva (CEO, InovaEduK)"
  ├─ Links to Stakeholder: "Roberto Santos (CTO, InovaEduK)"
  └─ Links to Funding: "Omidyar Network - Brazil Education Systems Grant"
```

#### From Funding Task → Related Items

Link to:
- **Relevant Stakeholder tasks** (program officer, decision-makers)
- **Relevant Partnership tasks** (partnerships that strengthen application)

**Example:**
```
Funding Task: "Gates Foundation - Systems Change RFP"
  ├─ Links to Stakeholder: "Jennifer Chen (Program Officer, Gates)"
  ├─ Links to Partnership: "Coalition for Educational Equity"
  └─ Links to Partnership: "MinEduc Brazil Collaboration"
```

#### From Stakeholder Task → Related Items

Link to:
- **All Partnerships** where this person is involved
- **All Funding opportunities** where this person is decision-maker or influencer

**Example:**
```
Stakeholder Task: "Roberto Santos (CTO, InovaEduK)"
  ├─ Links to Partnership: "InovaEduK - Educational Systems Partnership"
  ├─ Links to Partnership: "MinEduc Brazil Collaboration" (advisory role)
  └─ Links to Funding: "BNDES Social Impact Fund" (technical reviewer)
```

#### Implementation in Asana

1. **Use the "Add relationships" feature** on each task
2. **Relationship types available:**
   - "Related to" (most common)
   - "Blocks" (when one item blocks progress on another)
   - "Blocked by" (when progress depends on another item)
3. **Create custom relationship labels** if needed for clarity

---

### 2. Shared Custom Fields (Secondary Connection Method)

Certain fields should exist across all three systems to enable cross-filtering and portfolio views.

#### Universal Fields Present in All Three Systems

| Field Name | Purpose | Cross-System Value |
|------------|---------|-------------------|
| **Geographic Region** | Filter by where work happens | Enables regional portfolio view across partnerships, funding, stakeholders |
| **Cultural Approach** | How relationships work in context | Consistent framework for navigating all three types |
| **Primary Owner (360 Team)** | Who manages this relationship | See all your partnerships, funders, stakeholders in one view |
| **Last Interaction Date** | Relationship recency tracking | Identify cold relationships across all systems |
| **Language** | Communication considerations | Filter bilingual opportunities across systems |
| **Stage Health** | Current status | Dashboard view of what's at risk everywhere |

#### System-Specific Fields with Cross-Reference Value

**In Partnership Intelligence:**
- `Key Stakeholders` (text field listing names) → Reference Stakeholder Intelligence tasks
- `Potential Funders` (text field listing names) → Reference Funding Intelligence tasks

**In Funding Intelligence:**
- `Supporting Partnerships` (text field listing orgs) → Reference Partnership Intelligence tasks
- `Decision-Makers` (text field listing people) → Reference Stakeholder Intelligence tasks

**In Stakeholder Intelligence:**
- `Associated Partnerships` (text field listing orgs) → Reference Partnership Intelligence tasks
- `Funding Influence` (text field listing grants/funders) → Reference Funding Intelligence tasks

---

### 3. Naming Conventions for Searchability

Consistent naming enables quick cross-referencing without opening multiple tasks.

#### Organization Names
Use **identical spelling** across all systems:

✅ **Correct:**
- Partnership task: `InovaEduK - Educational Systems Partnership`
- Funding task: `InovaEduK Foundation - Community Schools Grant`
- Stakeholder task: `Maria Silva (CEO, InovaEduK)`

❌ **Incorrect:**
- Partnership: `InovaEduK`
- Funding: `Inova-EduK Foundation`
- Stakeholder: `Maria Silva (InovaEduK CEO)`

#### People Names
Format as **`FirstName LastName (Role, Organization)`**

✅ **Correct:**
- `Maria Silva (CEO, InovaEduK)`
- `Roberto Santos (CTO, InovaEduK)`
- `Jennifer Chen (Program Officer, Gates Foundation)`

Benefits:
- Always searchable across projects
- Enables quick lookup when reviewing partnerships or funding opportunities
- Clear role context without opening the task

#### Geographic Tags
Use **same terminology** consistently:

✅ **Correct:**
- `Brazil - São Paulo`
- `US - San Francisco`
- `Portugal - Lisbon`

❌ **Incorrect:**
- `Brazil/Sao Paulo` in one place
- `São Paulo, Brazil` in another
- `SF, USA` in another

---

## Information Flow Patterns

### Pattern 1: New Partnership Discovery → Cascade

```
1. Meet potential partner organization
   ↓
2. Create Stakeholder Intelligence tasks for key contacts
   → Capture: communication style, decision authority, cultural context
   ↓
3. Create Partnership Intelligence task
   → Link to Stakeholder tasks
   → Note: "Strategic fit areas", "Opening opportunities"
   ↓
4. Research potential Funding opportunities this partnership could unlock
   ↓
5. Create or update Funding Intelligence tasks
   → Link to Partnership task
   → Link to Stakeholder tasks (if you know the program officers)
   → Note: "Partnership with [org] strengthens application because..."
```

**Example in Practice:**

After meeting with InovaEduK (Brazilian EdTech):
1. Create stakeholder tasks for Maria Silva (CEO) and Roberto Santos (CTO)
2. Create partnership task "InovaEduK - Educational Systems Partnership"
3. Link partnership to both stakeholder tasks
4. Identify that this partnership strengthens Omidyar Network application
5. Create/update funding task for Omidyar, linking to partnership and stakeholders

---

### Pattern 2: New Funding Opportunity → Reverse Cascade

```
1. Discover grant or investor opportunity
   ↓
2. Research who makes decisions
   ↓
3. Create or update Stakeholder Intelligence for program officer/investor
   → Capture: priorities, communication style, past funding patterns
   ↓
4. Create Funding Intelligence task
   → Link to Stakeholder task
   ↓
5. Identify partnerships that strengthen your case
   ↓
6. Create or update Partnership Intelligence tasks
   → Link to Funding task
   → Note: "This partnership makes us stronger for [Grant Name]"
   ↓
7. Update Partnership tasks with "Potential Funders" field
```

**Example in Practice:**

After discovering Gates Foundation Systems Change RFP:
1. Research program officer Jennifer Chen
2. Create stakeholder task for Jennifer Chen with her priorities
3. Create funding task for Gates RFP, link to Jennifer's stakeholder task
4. Identify that Coalition for Educational Equity partnership strengthens application
5. Update partnership task, add link to Gates funding opportunity
6. Add "Gates Foundation" to partnership's "Potential Funders" field

---

### Pattern 3: Existing Stakeholder Relationship Deepens → Expansion

```
1. Relationship with stakeholder evolves
   (they change roles, organizations, priorities)
   ↓
2. Update Stakeholder Intelligence task
   → New role, new organization, new scope of influence
   ↓
3. Check: Does this create new Partnership opportunities?
   → Create new Partnership task if yes
   → Link to Stakeholder task
   ↓
4. Check: Does this create new Funding access?
   → Create new Funding task if yes
   → Link to Stakeholder task
   ↓
5. Update existing Partnership and Funding tasks where this person was involved
   → Adjust strategy based on their new position/influence
```

**Example in Practice:**

Maria Silva moves from InovaEduK CEO to Education Ministry Advisor:
1. Update Maria's stakeholder task with new role
2. Recognize this creates new partnership opportunity with Ministry
3. Create "Ministry of Education - Policy Partnership" task, link to Maria
4. Recognize this creates new funding access (government grants)
5. Create funding task for government education fund, link to Maria
6. Update InovaEduK partnership task (Maria now external advisor, not decision-maker)

---

## Workflow Integration Examples

### Scenario 1: Preparing for Strategic Partnership Meeting

You have a meeting with a potential partner organization.

**Cross-System Workflow:**

1. **Start with Stakeholder Intelligence**
   - Pull up tasks for everyone attending the meeting
   - Review: communication styles, decision patterns, cultural considerations, past interactions
   - **Prep briefing:** "Maria prefers relationship-building before business talk. Roberto is direct and data-driven. Meeting in Portuguese."

2. **Reference Partnership Intelligence**
   - Pull up the partnership opportunity task
   - Review: strategic fit, opening opportunities, common hesitations
   - **Identify:** What you need to learn in this meeting to advance the partnership

3. **Check Funding Intelligence**
   - Pull up any funding opportunities this partnership could unlock
   - **Prep talking points:** "If we partner on X, we could jointly apply for Y grant"
   - Note decision timeline alignment

**Post-Meeting Update Workflow:**

1. Update Stakeholder Intelligence tasks (new insights about individuals)
2. Update Partnership Intelligence task (progress on partnership, next steps)
3. Update or create Funding Intelligence tasks (if new opportunities emerged)
4. Add task relationships between all three as appropriate

**Time saved:** From 30+ minutes of scattered note-searching to <2 minutes with linked intelligence

---

### Scenario 2: Preparing Grant Application

You're applying for a major grant.

**Cross-System Workflow:**

1. **Start with Funding Intelligence**
   - Review the funder's decision patterns, past grantees, priorities
   - **Identify:** What they value, what proof points you need

2. **Reference Stakeholder Intelligence**
   - Pull up program officer task (if you know them)
   - Review: their priorities, communication style, what resonates with them
   - Pull up tasks for any board members or advisors you know at the funder
   - **Strategy:** Who could make warm introduction? Who could provide reference?

3. **Check Partnership Intelligence**
   - Identify partnerships that strengthen your application
   - Pull quotes, outcomes, collaboration evidence from partnership tasks
   - **Add partnerships as evidence** of collaborative capacity

**Update tasks with application status:**

1. Funding task: move to "Application In Progress" section
2. Partnership tasks: note in comments "Referenced in [Grant Name] application"
3. Stakeholder tasks: note any outreach for references or support

**Outcome:** Stronger application with clear evidence, warm connections, and tracked relationships

---

### Scenario 3: Quarterly Portfolio Review

You want to assess your overall strategic position.

**Cross-System Workflow:**

1. **Partnership Portfolio Analysis**
   - Filter by Stage, Temperature, Success Likelihood
   - **Question:** Where are partnerships strongest? Where are gaps?

2. **Cross-reference with Stakeholder Intelligence**
   - For each key partnership, review stakeholder tasks
   - **Question:** Are relationships with key contacts healthy? Any at risk?
   - **Identify:** Which stakeholders connect across multiple partnerships?

3. **Cross-reference with Funding Intelligence**
   - For each major funding pursuit, check partnership strength
   - **Question:** Do we have the collaborative relationships to be competitive?
   - **Identify:** Which partnerships could unlock new funding? Which funding could enable new partnerships?

**Synthesis Analysis:**

- **Geographic balance:** Are stakeholder relationships, partnerships, and funding aligned regionally?
- **Capacity check:** Are you over-invested in any one stakeholder, partner, or funder?
- **Strategic gaps:** Where do you have funding but weak partnerships? Partnerships but no funding?

**Time saved:** From days of manual portfolio analysis to 1-2 hours of strategic review

---

## Dashboard Views

Create these Asana saved searches for cross-system intelligence:

### 1. "Brazil Ecosystem View"

**Filter:** Geographic Region = "Brazil" OR "Latin America"

**Include tasks from:** Partnership Intelligence, Funding Intelligence, Stakeholder Intelligence

**Result:** Complete view of all Brazilian relationships, opportunities, and funding in one place

**Use when:** Planning Brazil trip, regional strategy review, identifying ecosystem gaps

---

### 2. "Relationship Health Scan"

**Filter:** Last Interaction Date > 3 months ago AND Stage Health ≠ "Dead"

**Include tasks from:** All three projects

**Result:** Relationships going cold across partnerships, funding, stakeholders

**Use when:** Weekly relationship maintenance, identifying neglected connections

---

### 3. "Hot Opportunities Cross-Check"

**Filter:**
- Partnership Intelligence where Temperature = "Hot"
- OR Funding Intelligence where Likelihood = "High/Very High"

**Cross-reference:** Which stakeholders are involved? Are they healthy relationships?

**Result:** Focus on highest-potential opportunities with relationship health check

**Use when:** Prioritizing where to invest time and resources

---

### 4. "My Active Portfolio" (by team member)

**Filter:** Primary Owner = [Your Name]

**Include tasks from:** All three projects

**Result:** Everything you're managing across partnerships, funding, stakeholders

**Use when:** Weekly planning, workload assessment, handoff preparation

---

### 5. "Decision-Makers at Risk"

**Filter:**
- Stakeholder Intelligence where Power/Influence = "High"
- AND Last Interaction > 2 months
- AND Associated Partnerships OR Funding Influence is not empty

**Result:** Important relationships going cold that affect active opportunities

**Use when:** Prioritizing relationship maintenance, preventing opportunity loss

---

## Anti-Patterns to Avoid

### ❌ Don't: Duplicate information across systems

**Wrong:** Copy entire stakeholder bio into partnership task description

**Right:** Brief reference + link to stakeholder task

**Example:**
```
Partnership Task: "InovaEduK Partnership"

Description:
❌ Wrong: "Maria Silva is the CEO of InovaEduK. She has 15 years
         experience in education technology. She prefers
         relationship-first communication..."

✅ Right: "Key contacts: Maria Silva (CEO - see stakeholder task)
         and Roberto Santos (CTO - see stakeholder task)"
```

---

### ❌ Don't: Let links break when things change

**Wrong:** Person changes organizations, links to old partnership stay unchanged

**Right:** Update stakeholder task, review all linked partnerships and funding tasks, update or remove links as appropriate

**Process:**
1. Stakeholder moves from Company A to Company B
2. Update stakeholder task with new organization
3. Check all linked partnership tasks (search "Related to" for this stakeholder)
4. Update partnership tasks (they may now be an advisor, not decision-maker)
5. Check all linked funding tasks (they may have new funding access)
6. Create new partnership/funding opportunities if relevant

---

### ❌ Don't: Create orphan tasks (no cross-links)

**Wrong:** Add a stakeholder with no links to partnerships or funding

**Right:** Every stakeholder should link to at least one partnership or funding opportunity (if they don't, why are they in the system?)

**Valid exception:** New stakeholder added during networking event, with follow-up task to explore partnership/funding potential

---

### ❌ Don't: Over-link everything

**Wrong:** Link every stakeholder to every funding opportunity "just in case"

**Right:** Only link where there's a meaningful relationship (they're a decision-maker, influencer, or key reference)

**Guideline:**
- **Decision-maker:** Must link (they control the outcome)
- **Influencer:** Should link (they significantly affect the outcome)
- **Aware of the opportunity:** Don't link (too weak a connection)

---

### ✅ Do: Link liberally but meaningfully

**When to create a link:**
- If a stakeholder is mentioned in a partnership conversation → link them
- If a partnership strengthens a funding application → link it
- If a program officer's priorities align with a partnership → link them

**When to skip the link:**
- Stakeholder has only tangential connection
- Partnership is mentioned in passing but not relevant
- Connection is speculative with no clear relationship

---

### ✅ Do: Use comments to explain relationships

When you create a link, add a comment explaining why.

**Example:**
```
Comment on Partnership Task → Stakeholder link:
"Linked to Roberto Santos because he's the key decision-maker on their
side and his communication style (direct, data-driven) should inform how
we present our proposal"

Comment on Funding Task → Partnership link:
"Linked to Coalition partnership because Gates RFP prioritizes
collaborative approaches, and this partnership demonstrates our
capacity for multi-sector collaboration"
```

**Benefits:**
- Future you remembers why the link exists
- Team members understand the strategic relationship
- Easy to evaluate if link is still relevant during reviews

---

### ✅ Do: Review and prune quarterly

**Dead partnerships:** Unlink stakeholders who are no longer relevant

**Lost funding:** Unlink partnerships that were only relevant to that opportunity

**Departed stakeholders:** Update their tasks, update all linked items

**Process:**
1. Filter by "Last updated > 3 months ago"
2. Review each task: still relevant?
3. Remove or update outdated links
4. Mark tasks as "Dead" if no longer active
5. Archive completed opportunities

---

### ✅ Do: Create "bridge" tasks when needed

If a stakeholder connects two partnerships in an important way, create a Pattern Library task explaining the dynamic.

**Example:**
```
Task: "Maria Silva as Coalition Broker"

Description:
"Maria's influence across InovaEduK and MinEduc creates opportunity
for multi-sector partnerships. She can broker introductions and
facilitate collaboration between tech sector and government."

Links to:
- Partnership: InovaEduK
- Partnership: MinEduc
- Stakeholder: Maria Silva
- Funding: Government Innovation Fund (she can vouch for us)
```

---

## Implementation Roadmap

### Week 1: Foundation

**Tasks:**
1. Create the three Asana projects (Partnership, Funding, Stakeholder Intelligence)
2. Set up custom fields (start with universal fields, add system-specific ones)
3. Import 3-5 existing relationships into each system as tests
4. Practice creating links between related tasks

**Success criteria:**
- ✅ All three projects exist with custom fields configured
- ✅ Sample tasks created with cross-links working
- ✅ Team can navigate between linked tasks

---

### Week 2-3: Build Critical Mass

**Tasks:**
1. Add 10-15 stakeholders (your most important relationships)
2. Add 5-10 active partnerships
3. Add 3-5 current funding pursuits
4. Link them all appropriately
5. Test: Can you pull up a stakeholder and see all their related partnerships and funding?

**Success criteria:**
- ✅ Enough data to be useful for real work
- ✅ Cross-links enable quick intelligence gathering
- ✅ Team starts using system for meeting prep

---

### Week 4: Workflow Integration

**Tasks:**
1. Use all three systems to prep for one real meeting
2. Use all three systems to develop one real grant application
3. Identify friction points and refine
4. Train team members on cross-linking approach

**Success criteria:**
- ✅ System provides value in real-world scenarios
- ✅ Friction points identified and resolved
- ✅ Team adopts new workflows

---

### Month 2: Automation Layer

**Tasks:**
1. Set up Zapier + Claude workflows to auto-populate from transcripts
2. Configure rules to suggest links (e.g., when person X is mentioned in transcript, link to their stakeholder task)
3. Create saved searches for key dashboard views
4. Set up weekly review routine

**Success criteria:**
- ✅ Intelligence extraction automated
- ✅ Dashboard views enable portfolio management
- ✅ Weekly review rhythm established

---

### Month 3: Pattern Recognition

**Tasks:**
1. Review 30 days of data
2. Identify patterns: Which stakeholder types unlock which partnership types? Which partnerships lead to which funding?
3. Create Pattern Library tasks capturing these insights
4. Use patterns to guide future relationship strategy

**Success criteria:**
- ✅ Patterns documented in Pattern Library
- ✅ Strategic insights informing relationship development
- ✅ System proving ROI through better decisions

---

## Success Metrics

### You'll know the system is working when:

✅ **Speed:** Before any meeting, you can pull complete intelligence in under 2 minutes (stakeholder background + partnership context + related funding opportunities)

✅ **Discoverability:** When someone asks "Who do we know at [Organization]?", you can answer immediately by searching Stakeholder Intelligence

✅ **Application Quality:** When preparing a grant application, you can instantly identify which partnerships to highlight and which stakeholders to approach for references

✅ **Pattern Recognition:** Quarterly reviews reveal patterns you wouldn't have seen without cross-system linking (e.g., "All our successful Brazilian partnerships involved stakeholders with relationship-first cultural approach")

✅ **Handoff Quality:** Team members can seamlessly hand off relationships because all three systems are linked and documented

✅ **Opportunity Spotting:** You spot opportunities faster because stakeholder updates trigger "wait, this could help partnership X" or "this person could open funding door Y" insights

✅ **Portfolio Health:** You can quickly assess relationship health across all three systems and identify risks before they become problems

✅ **Strategic Alignment:** You can see geographic, thematic, and capacity balance across partnerships, funding, and stakeholders

---

## Quick Reference

### When creating a new...

**Partnership Task:**
1. Create stakeholder tasks for key contacts
2. Link partnership to stakeholder tasks
3. Check if partnership unlocks funding opportunities
4. Link to relevant funding tasks
5. Add "Key Stakeholders" and "Potential Funders" fields

**Funding Task:**
1. Research decision-makers
2. Create/update stakeholder tasks for program officers
3. Link funding to stakeholder tasks
4. Identify partnerships that strengthen application
5. Link to relevant partnership tasks
6. Add "Decision-Makers" and "Supporting Partnerships" fields

**Stakeholder Task:**
1. Identify all partnerships where this person is involved
2. Link stakeholder to partnership tasks
3. Identify all funding where this person has influence
4. Link stakeholder to funding tasks
5. Add "Associated Partnerships" and "Funding Influence" fields

---

## Related Documentation

- [Intelligence Extractor README](../README.md) - Overview of the intelligence extraction system
- [Template Selection Guide](../templates/00-template-selection-guide.md) - Choosing the right extraction template
- [Intelligence Schemas](intelligence-schemas.md) - JSON structure for all three intelligence types
- [Quality Framework](quality-framework.md) - How quality is measured and tracked

---

**Document Version:** 1.0
**Last Updated:** November 2025
**Maintained by:** 360 Intelligence Systems Team
