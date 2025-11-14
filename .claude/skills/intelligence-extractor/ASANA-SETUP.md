# Asana Implementation Guide
## 360 Partnership & Opportunity Intelligence System

This guide provides step-by-step instructions for setting up the three intelligence databases in Asana.

---

## Overview

Three Asana projects will house your intelligence:

1. **Partnership Intelligence Hub** - Organizations and collaboration opportunities
2. **Funding Opportunity Intelligence** - Grants, investors, and funding sources
3. **Stakeholder Intelligence Database** - Key individuals across all contexts

Each project uses:
- **Custom Fields** to capture structured data
- **Sections** to organize by stage/type
- **Task Templates** for consistent intelligence capture
- **Automation Rules** for workflow efficiency

---

## Project 1: Partnership Intelligence Hub

### Project Settings

- **Project Name:** Partnership Intelligence Hub
- **Project Type:** List (not Board or Timeline initially)
- **Privacy:** Private to 360 Team
- **Color:** Blue (or your preference)
- **Description:**
  ```
  Strategic intelligence about partnerships, collaborations, and alliances.

  Each task = one partnership opportunity
  Use templates for consistent intelligence capture
  Update relationship temperature and stage as partnerships evolve

  See Intelligence Extractor skill documentation for usage.
  ```

### Sections

Create these sections (in this order):

1. **Active Exploration** - Opportunities currently being explored
2. **Negotiation Stage** - Moving toward commitment or agreement
3. **Active Partnerships** - Signed and underway
4. **Closed-Won Archive** - Successful partnerships for pattern analysis
5. **Closed-Lost Archive** - Didn't work out (capture why for learning)
6. **Pattern Library** - Meta-level insights across partnerships

### Custom Fields

Create these custom fields (Project-level):

#### Partnership Type
- **Type:** Dropdown (single select)
- **Options:**
  - Brazilian Educational
  - Brazilian Corporate
  - US Corporate/VC
  - US Foundation
  - Asian Partner
  - European Impact
  - Government/Policy
  - Other

#### Relationship Temperature
- **Type:** Dropdown (single select)
- **Options:**
  - Cold
  - Warming
  - Hot
  - Active Partner
  - Stalled

#### Cultural Approach
- **Type:** Dropdown (single select)
- **Options:**
  - Relationship-First
  - Transaction-First
  - Hybrid
  - Hierarchical
  - Collaborative

#### Decision Timeline
- **Type:** Dropdown (single select)
- **Options:**
  - Fast (<3 months)
  - Deliberate (3-6 months)
  - Glacial (>6 months)
  - Unclear

#### Success Likelihood
- **Type:** Dropdown (single select)
- **Options:**
  - Low (25%)
  - Medium (50%)
  - High (75%)
  - Very High (90%)

#### Primary Owner
- **Type:** People (single select)
- **Options:** Your team members (Chandler, Eduardo, Felipe, etc.)

#### Last Interaction
- **Type:** Date
- **Purpose:** Track relationship freshness

#### Next Action Due
- **Type:** Date
- **Purpose:** When next touchpoint should happen

#### Estimated Value
- **Type:** Text
- **Purpose:** Budget range or strategic value description

#### Language
- **Type:** Dropdown
- **Options:**
  - English
  - Portuguese
  - Both
  - Spanish
  - Other

#### Stage Health
- **Type:** Dropdown
- **Options:**
  - On Track
  - At Risk
  - Blocked
  - Dead

#### Auto-Created
- **Type:** Checkbox
- **Purpose:** Track which tasks were created by automation vs. manual

### Task Template: Partnership Intelligence

Create a task template named "Partnership Intelligence Template":

**Task Name Format:** `[Organization Name] - [Partnership Type] - [Primary Contact]`

**Default Section:** Active Exploration

**Template Description:**
```markdown
## Partnership Overview
**Organization:**
**Primary Contact:**
**Secondary Contacts:**
**Partnership Focus:**

---

## Opening Opportunities
*What pain points or gaps are they trying to solve?*
-

*What strategic priorities are creating urgency?*
-

*Where is their current approach falling short?*
-

---

## Strategic Qualification Questions
*Questions that reveal decision-making authority and timeline:*
-

*Questions that surface budget reality vs. stated interest:*
-

*Questions that test cultural fit and values alignment:*
-

*Questions that identify systems-change appetite:*
-

---

## Common Hesitations & Responses
*Pattern: What they typically worry about*

**Hesitation:**
**Response Framework:**
**Proof Points:**

---

## Strategic Framing
*How to position 360's work in terms that resonate with their mission:*


*Cultural communication adjustments needed:*


*Key phrases that signal alignment vs. misalignment:*


---

## Walk-Away Signals
*When to disengage from this opportunity:*
- [ ] No clear decision authority or timeline
- [ ] Values misalignment on core issues
- [ ] Purely transactional in relationship-first culture
- [ ] Unrealistic expectations (timeline/scope/budget mismatch)
- [ ]

---

## Interaction Log
*Keep running notes of all meetings, emails, key moments*

**[Date]:**

---

## Partnership Success Patterns
*If this closes successfully, what patterns led to success?*
- Time from first contact to signed agreement:
- Number of relationship-building meetings before proposal:
- Key turning point:
- Decision-making process:
```

**Default Subtasks:**
1. Initial Research
2. First Contact Made
3. Discovery Conversation
4. Proposal Development (if appropriate)
5. Decision Timeline Confirmed
6. Agreement Signed
7. Post-Mortem Learning Capture

**Default Custom Field Values:**
- Relationship Temperature: Cold
- Stage Health: On Track
- Success Likelihood: Medium (50%)

### Project Views

Create these saved views:

#### View 1: Active Pipeline
- **Filter:** Section is "Active Exploration" OR "Negotiation Stage"
- **Sort:** Next Action Due (ascending)
- **Fields:** Partnership Type, Relationship Temperature, Success Likelihood, Next Action Due, Primary Owner
- **Purpose:** What needs attention now

#### View 2: By Partnership Type
- **Group By:** Partnership Type
- **Filter:** Section is NOT "Closed-Won Archive" AND NOT "Closed-Lost Archive"
- **Purpose:** See portfolio composition

#### View 3: Relationship Temperature
- **Group By:** Relationship Temperature
- **Sort:** Last Interaction (ascending)
- **Purpose:** What needs warming vs. what's hot

#### View 4: Success Patterns Archive
- **Filter:** Section is "Closed-Won Archive"
- **Sort:** Partnership Type
- **Purpose:** Learn from wins

#### View 5: Warning Signals
- **Filter:** Stage Health is "At Risk" OR "Blocked"
- **Purpose:** Immediate attention needed

### Automation Rules

#### Rule 1: Stale Relationship Alert
- **Trigger:** Last Interaction Date is more than 30 days ago AND Section is "Active Exploration"
- **Action:** Add comment "⚠️ No interaction in 30+ days. Time to check in or move to Closed-Lost?"

#### Rule 2: Next Action Overdue
- **Trigger:** Next Action Due date passes AND Section is NOT archive
- **Action:** Add comment "⏰ Next action overdue. What's the status?", notify Primary Owner

#### Rule 3: Won Deal Learning
- **Trigger:** Task moved to "Closed-Won Archive"
- **Action:** Add subtask "Capture success patterns in description", assign to Primary Owner

#### Rule 4: Lost Deal Learning
- **Trigger:** Task moved to "Closed-Lost Archive"
- **Action:** Add subtask "Document walk-away signals and lessons learned", assign to Primary Owner

---

## Project 2: Funding Opportunity Intelligence

### Project Settings

- **Project Name:** Funding Opportunity Intelligence
- **Project Type:** List
- **Privacy:** Private to 360 Team
- **Color:** Green
- **Description:**
  ```
  Track funding sources, application patterns, and decision-making intelligence.

  Each task = one funding opportunity
  Use for foundations, impact investors, government programs, corporate partnerships
  Track from research through application to decision

  See Intelligence Extractor skill for usage.
  ```

### Sections

1. **Research Stage** - Exploring potential fit
2. **Application In Progress** - Actively pursuing
3. **Under Review** - Submitted, awaiting decision
4. **Secured Funding** - Successful awards
5. **Not Funded Archive** - Declined or didn't pursue
6. **Renewal Tracking** - Existing funders coming up for renewal
7. **Funder Intelligence Library** - Patterns and insights

### Custom Fields

#### Funder Type
- **Type:** Dropdown
- **Options:**
  - Foundation
  - Impact Investor
  - Government Program
  - Corporate Partnership
  - Philanthropic Family Office
  - Multi-lateral Org
  - Other

#### Geographic Focus
- **Type:** Dropdown
- **Options:**
  - Global
  - North America
  - Latin America
  - Brazil-Specific
  - Europe
  - Asia-Pacific
  - Multi-Regional

#### Funding Amount Range
- **Type:** Dropdown
- **Options:**
  - <$50K
  - $50K-$250K
  - $250K-$1M
  - $1M-$5M
  - >$5M

#### Application Complexity
- **Type:** Dropdown
- **Options:**
  - Simple (LOI only)
  - Moderate (Narrative + Budget)
  - Complex (Full proposal + Theory of Change)
  - Intensive (Multi-stage + Site Visits)

#### Decision Speed
- **Type:** Dropdown
- **Options:**
  - Fast (<2 months)
  - Standard (2-4 months)
  - Slow (4-6 months)
  - Very Slow (>6 months)

#### Cultural Approach
- **Type:** Dropdown
- **Options:**
  - Trust-Based/Flexible
  - Process-Heavy/Structured
  - Relationship-Driven
  - Metrics-Driven
  - Hybrid

#### Reporting Requirements
- **Type:** Dropdown
- **Options:**
  - Light
  - Moderate
  - Heavy
  - Very Heavy

#### Application Deadline
- **Type:** Date

#### Decision Expected
- **Type:** Date

#### Fit Score
- **Type:** Dropdown
- **Options:**
  - Excellent Fit
  - Good Fit
  - Moderate Fit
  - Stretch
  - Poor Fit

#### Likelihood of Success
- **Type:** Dropdown
- **Options:**
  - Low (25%)
  - Medium (50%)
  - High (75%)
  - Very High (90%)

#### Primary Owner
- **Type:** People

#### Systems Change Appetite
- **Type:** Dropdown
- **Options:**
  - High (seeks systemic impact)
  - Moderate (open to it)
  - Low (programmatic focus only)

#### Auto-Created
- **Type:** Checkbox

### Task Template: Funding Opportunity

**Task Name Format:** `[Funder Name] - [Grant/Program Name] - [Cycle/Year]`

**Default Section:** Research Stage

**Template Description:**
```markdown
## Funder Overview
**Organization:**
**Program/Grant Name:**
**Website:**
**Program Officer:**

**Mission Alignment Check:**
- Their stated priorities:
- 360's alignment:
- Gap areas:

---

## Decision-Making Intelligence

**Typical Grantee Profile:**
- Who they've funded before:
- What they prioritize:
- What they avoid:

**Decision Process:**
- Number of stages:
- Key decision-makers:
- Decision timing:
- Political dynamics:

**Past Application History (if any):**
- Previous applications:
- Relationship history:

---

## Application Strategy

**Positioning Approach:**
*How to frame 360's work for this specific funder*
- Lead with:
- Emphasize:
- Downplay:
- Evidence needed:

**Competitive Landscape:**
*Who else is likely applying?*
- Similar organizations:
- Our differentiation:
- Their likely strengths:
- Our advantages:

**Budget & Scope Considerations:**
- What they'll fund:
- What they won't fund:
- Overhead/indirect rate:
- Multi-year possibility:

---

## Application Requirements Checklist

**Narrative Components:**
- [ ] Problem statement/context
- [ ] Proposed solution/approach
- [ ] Theory of change/logic model
- [ ] Impact metrics and evaluation plan
- [ ] Organizational capacity demonstration
- [ ] Sustainability/long-term vision
- [ ] Community voice/partnership approach

**Financial Components:**
- [ ] Project budget (detailed line items)
- [ ] Budget narrative/justification
- [ ] Organizational budget (operating)
- [ ] Other funding sources
- [ ] Financial statements
- [ ] 990 forms

**Supporting Materials:**
- [ ] Letters of support
- [ ] Board list and bios
- [ ] Key staff bios/CVs
- [ ] Evidence of impact
- [ ] IRS determination letter

---

## Red Flags & Walk-Away Signals

- [ ] Mission misalignment
- [ ] Unrealistic reporting burden
- [ ] IP restrictions or approach mandates
- [ ] Timeline doesn't align with capacity
- [ ] Funding too small for application effort
- [ ] Geographic/constituency restrictions we can't meet
- [ ] Past pattern of declining orgs like ours

---

## Success Factors for This Funder

*What increases likelihood of funding?*
- Prior relationship with program officer:
- Board connections or champions:
- Track record in their focus area:
- Geographic presence where they fund:
- Partnership approach:
- Innovation factor:
- Community engagement:

---

## Timeline & Milestones

**Pre-Application Phase:**
- [ ] Initial research and fit assessment complete
- [ ] Informational call with program officer
- [ ] Review of past funded projects
- [ ] Internal go/no-go decision

**Application Development Phase:**
- [ ] Narrative first draft complete
- [ ] Budget first draft complete
- [ ] Internal review and revision
- [ ] Gather support letters
- [ ] Final review
- [ ] Submit application

**Post-Submission Phase:**
- [ ] Follow-up note sent
- [ ] Expected decision notification
- [ ] If awarded: onboarding/contracting
- [ ] If not awarded: debrief call requested

---

## Learning Capture

**If Funded - Success Factors:**
- What made this successful:
- Unexpected elements that helped:
- Application elements that resonated:
- Relationship factors:

**If Not Funded - Lessons Learned:**
- Official reason given:
- Actual reason (if different):
- What we'd do differently:
- Should we try again:
- Pattern to note:

---

## Relationship Management

**Key Contacts:**
- Program Officer: [Name, last contact, relationship quality]
- Grants Manager:
- Board Member connections:
- Peer organization referrals:
```

**Default Subtasks:**
1. Fit Assessment
2. Intelligence Gathering
3. Relationship Development
4. Narrative Development
5. Budget Development
6. Internal Review
7. Final Materials Gathering
8. Submission
9. Post-Submission Follow-up
10. Learning Capture

### Project Views

#### View 1: Active Applications
- **Filter:** Section is "Application In Progress" OR "Under Review"
- **Sort:** Application Deadline
- **Purpose:** Current workload

#### View 2: Decision Calendar
- **View Type:** Timeline
- **Date Field:** Decision Expected
- **Purpose:** See when to expect news

#### View 3: By Funder Type
- **Group By:** Funder Type
- **Purpose:** Portfolio composition

#### View 4: High Priority Opportunities
- **Filter:** Fit Score is "Excellent" OR "Good", AND Likelihood is "High" OR "Very High"
- **Purpose:** Focus limited application energy

#### View 5: Renewal Pipeline
- **Filter:** Section is "Renewal Tracking"
- **Purpose:** Don't let renewals slip

### Automation Rules

#### Rule 1: Deadline Approaching
- **Trigger:** Application Deadline is 30 days away
- **Action:** Notify Primary Owner, add comment "30-day deadline warning"

#### Rule 2: Decision Overdue
- **Trigger:** Decision Expected date passes
- **Action:** Add comment "Decision date passed. Follow up?", notify owner

#### Rule 3: Successful Funding Learning
- **Trigger:** Task moved to "Secured Funding"
- **Action:** Add subtask "Capture success factors", notify team (celebrate!)

#### Rule 4: Renewal Timing Alert
- **Trigger:** Renewal Tracking task with Application Deadline in 90 days
- **Action:** Notify owner "Renewal approaching. Start cultivation/check-in"

---

## Project 3: Stakeholder Intelligence Database

### Project Settings

- **Project Name:** Stakeholder Intelligence Database
- **Project Type:** List
- **Privacy:** Private to 360 Team
- **Color:** Purple
- **Description:**
  ```
  Strategic intelligence about key individuals across partnerships, boards, clients, and networks.

  Each task = one stakeholder (person)
  Not a CRM - this is strategic intelligence about how people operate, decide, and influence
  Use templates for consistent profile creation

  See Intelligence Extractor skill for usage.
  ```

### Sections

1. **Board Members & Advisors** - Governance stakeholders
2. **Client Executives & Decision-Makers** - People hiring 360
3. **Partner Organization Leaders** - Heads of partner orgs
4. **Community Leaders & Champions** - Grassroots influence
5. **Policy Makers & Government Officials** - Public sector influence
6. **Funder Program Officers** - Foundation/investor contacts
7. **Academic & Research Partners** - Thought leaders, researchers
8. **Stakeholder Pattern Library** - Meta-insights about types

### Custom Fields

#### Stakeholder Type
- **Type:** Dropdown
- **Options:**
  - Board Member
  - Client Exec
  - Partner Leader
  - Community Champion
  - Policy Maker
  - Funder Contact
  - Academic/Researcher
  - Advisor
  - Other

#### Organization
- **Type:** Text
- **Purpose:** Where they work/lead

#### Decision Authority
- **Type:** Dropdown
- **Options:**
  - Final Decision-Maker
  - Strong Influence
  - Advisory Voice
  - Limited Influence
  - Unknown

#### Communication Style
- **Type:** Dropdown
- **Options:**
  - Direct & Efficient
  - Relational & Warm
  - Formal & Hierarchical
  - Collaborative & Inclusive
  - Data-Driven & Analytical
  - Visionary & Big-Picture

#### Cultural Context
- **Type:** Dropdown
- **Options:**
  - US Corporate
  - US Nonprofit
  - Brazilian
  - Latin American (other)
  - European
  - Asian
  - African
  - Multi-Cultural

#### Relationship Stage
- **Type:** Dropdown
- **Options:**
  - New Contact
  - Building Trust
  - Established Relationship
  - Close Collaborator
  - Champion/Advocate

#### Power Dynamics Awareness
- **Type:** Dropdown
- **Options:**
  - High (very conscious of equity/power)
  - Moderate (aware but inconsistent)
  - Low (not central to thinking)

#### Systems Change Orientation
- **Type:** Dropdown
- **Options:**
  - Deep Systems Thinker
  - Programmatic Focus
  - Hybrid
  - Transactional Orientation
  - Unknown

#### Response Time
- **Type:** Dropdown
- **Options:**
  - Very Fast (<24hrs)
  - Fast (1-3 days)
  - Moderate (3-7 days)
  - Slow (>1 week)
  - Inconsistent

#### Meeting Preference
- **Type:** Dropdown
- **Options:**
  - In-Person Priority
  - Video Comfortable
  - Phone Preferred
  - Email Primary
  - Flexible

#### Language Preference
- **Type:** Dropdown
- **Options:**
  - English
  - Portuguese
  - Spanish
  - Multilingual
  - Other

#### Last Interaction
- **Type:** Date

#### Relationship Owner
- **Type:** People

#### Auto-Created
- **Type:** Checkbox

### Task Template: Stakeholder Profile

**Task Name Format:** `[Full Name] - [Primary Role/Organization] - [Context]`

**Default Section:** (Varies by stakeholder type)

**Template Description:**
```markdown
## Basic Profile
**Full Name:**
**Title/Role:**
**Organization:**
**Location:**
**Contact Info:**
**LinkedIn/Website:**

**How We Know Them:**
- Connection origin:
- Relationship duration:
- Context of relationship:

---

## Communication Intelligence

**Preferred Communication Style:**
*How they like to interact*
- Meeting format preference:
- Optimal meeting length:
- Response patterns:
- Best time to reach:
- Language preference:

**Communication Red Flags:**
*What to avoid*
- Triggers or sensitive topics:
- Communication styles that don't work:
- Timing issues:

**How to Prepare for Meetings:**
- Background they appreciate:
- Meeting structure:
- Follow-up expectations:

---

## Decision-Making Intelligence

**How They Make Decisions:**
- Decision style:
- Information needs:
- Risk tolerance:
- Timeline patterns:

**Influence Mapping:**
*Who influences their thinking?*
- Whose opinion they seek:
- What evidence persuades them:
- Who has veto power over their decisions:

**Past Decision Patterns:**
*What can we learn from their history?*
- Decisions they've made well:
- Decisions they've struggled with:
- Values reflected in choices:

---

## Strategic Intelligence

**What They Care About:**
*Deep motivations and priorities*
- Core values:
- Success metrics:
- Legacy questions:
- Pressure points:

**Political Dynamics:**
*Power and relationships around them*
- Who they report to:
- Who they're accountable to:
- Internal allies:
- Internal skeptics:
- External relationships:

**Organizational Context:**
*What's happening in their world*
- Current organizational priorities:
- Pressures they're under:
- Recent changes:
- Upcoming transitions:

---

## Cultural & Relational Intelligence

**Cultural Considerations:**
- Cultural background:
- Communication norms:
- Relationship-building expectations:
- Time orientation:
- Decision-making culture:

**Relational Approach:**
*How to build and maintain relationship*
- Trust-building pace:
- Reciprocity expectations:
- Recognition needs:
- Boundary awareness:

**Red Flags & Cautions:**
- Known conflicts or tensions:
- Past disappointments:
- Credibility concerns:
- Scope creep tendencies:

---

## Engagement History

**Key Interactions Log:**

**[Date]:**

---

## Strategic Positioning

**How to Position 360 with This Person:**
- Frame we should use:
- Examples that resonate:
- Proof points needed:
- Connection to their priorities:

**Differentiation Points:**
- What makes us valuable to them specifically:
- Our unique value vs. others they work with:
- Gaps we fill for them:

**Collaboration Opportunities:**
- Immediate opportunities:
- Medium-term possibilities:
- Long-term vision:
- Mutual benefit model:

---

## Working With Them Best

**Do's:**
-
-

**Don'ts:**
-
-

**Preparation Checklist Before Engaging:**
- [ ] Review their current organizational context
- [ ] Check for recent news or changes
- [ ] Prepare materials in their preferred format
- [ ] Confirm communication channel they prefer
- [ ] Review past interaction notes

---

## Influence & Network

**Their Network (People They Trust):**
- Close advisors:
- Peer organizations:
- Board/supervisory connections:
- Community connections:

**Our Shared Network:**
- Mutual connections:
- Potential introducers:
- Coalition opportunities:

---

## Strategic Value Assessment

**Value to 360:**
- Strategic importance: [High/Medium/Low, why]
- Decision authority level:
- Network access:
- Resource potential:
- Mission alignment:

**Investment Level:**
- Relationship maintenance effort:
- Recommended engagement frequency:
- Relationship owner at 360:
- Team involvement:
```

**Default Subtasks:**
1. Initial Profile Creation
2. Communication Style Assessment
3. Decision-Making Pattern Analysis
4. Strategic Value Evaluation
5. Quarterly Relationship Check

### Project Views

#### View 1: Relationship Maintenance Calendar
- **Filter:** Last Interaction >60 days ago
- **Sort:** Strategic importance (custom)
- **Purpose:** Who needs a check-in

#### View 2: By Stakeholder Type
- **Group By:** Stakeholder Type
- **Purpose:** Portfolio across types

#### View 3: Decision-Makers Only
- **Filter:** Decision Authority is "Final Decision-Maker" OR "Strong Influence"
- **Purpose:** People who can green-light things

#### View 4: Champions & Advocates
- **Filter:** Relationship Stage is "Champion/Advocate"
- **Purpose:** Our strongest relationships

#### View 5: By Cultural Context
- **Group By:** Cultural Context
- **Purpose:** Culturally appropriate engagement

### Automation Rules

#### Rule 1: Relationship Check-In Reminder
- **Trigger:** Last Interaction >90 days ago AND Strategic Value custom field is "High"
- **Action:** Notify Relationship Owner, add comment "High-value relationship needs touch-base"

#### Rule 2: Relationship Stage Progression
- **Trigger:** Relationship Stage changes to "Champion/Advocate"
- **Action:** Add comment "This person is now a champion. How can we support them?", notify team

---

## Cross-Project Integration

### Linking Intelligence Across Projects

**Partnership ↔ Stakeholder:**
- When stakeholder works at partner organization, link tasks in descriptions
- Example: In partnership task, link to key stakeholder profiles
- In stakeholder task, link to their organization's partnership task

**Funding ↔ Stakeholder:**
- Program officer stakeholder profile linked to funding opportunity
- Funder organization linked to any partnership relationships

**Partnership ↔ Funding:**
- If partner organization is also potential funder
- If funder interested in broader partnership beyond just funding

**Best Practice:** Use Asana's task linking (paste task URL in description or comment)

---

## Getting Started: Implementation Phases

### Phase 1: Create Projects (Week 1)

1. Create all three projects in Asana
2. Set up sections in each
3. Add custom fields
4. Create templates
5. Invite team members

**Deliverable:** Empty infrastructure ready to populate

### Phase 2: Populate Pattern Libraries (Week 2)

1. Manually create 3-5 tasks in each Pattern Library section
2. Capture existing knowledge you have about:
   - Partnership patterns (Brazilian orgs need X meetings, etc.)
   - Funding patterns (Foundations in Q1 move faster, etc.)
   - Stakeholder patterns (Board dynamics, etc.)

**Deliverable:** Pattern knowledge documented

### Phase 3: Backfill Key Entities (Week 3-4)

1. Identify 10-15 most important:
   - Current or potential partners
   - Active funding opportunities
   - VIP stakeholders
2. Create tasks manually using templates
3. Populate with existing knowledge
4. Practice using the system

**Deliverable:** Core intelligence captured

### Phase 4: Integrate with Intelligence Extractor (Week 5+)

1. Start using Intelligence Extractor skill on new meetings
2. Review JSON outputs
3. Create/update Asana tasks from extractions
4. Provide feedback to improve extraction quality

**Deliverable:** Active, growing intelligence system

### Phase 5: Automation (Optional, Week 6+)

1. Set up Zapier workflows (see ZAPIER-INTEGRATION.md)
2. Automate extraction from meeting transcripts
3. Automatic task creation/updating
4. Quality tracking and feedback loops

**Deliverable:** Hands-free intelligence capture

---

## Maintenance Best Practices

### Weekly
- Review "Warning Signals" view in Partnership Hub
- Check upcoming deadlines in Funding Intelligence
- Scan "Relationship Maintenance Calendar" in Stakeholder DB
- Update Last Interaction dates after meetings

### Monthly
- Run all "Archive" views to extract pattern learnings
- Update Pattern Library tasks with new insights
- Review relationship temperatures and stages
- Assess portfolio composition (are we balanced across types?)

### Quarterly
- Strategic review: Where should we invest more deeply?
- Cleanup: Archive dead opportunities
- Celebrate wins: Review Closed-Won partnerships and Secured Funding
- Team calibration: Ensure consistent use of custom fields

---

## Training Your Team

### Onboarding New Users

1. **Read Documentation**
   - Intelligence Extractor SKILL.md
   - This Asana setup guide

2. **Tour the Projects**
   - Walk through each project
   - Explain purpose of each section
   - Review custom field meanings

3. **Create a Test Entry**
   - Use template to create one partnership, one funder, one stakeholder
   - Practice filling in fields
   - Get feedback

4. **Review Together**
   - Look at existing intelligence tasks
   - Discuss what good intelligence looks like
   - Calibrate on confidence levels, fit assessments, etc.

### Consistency Tips

- **Use templates** - Don't create tasks from scratch
- **Be specific** - Vague intelligence isn't useful intelligence
- **Update regularly** - Stale information is worse than no information
- **Link entities** - Show connections across projects
- **Capture patterns** - Add to Pattern Library when you notice recurring themes

---

## Questions & Support

For questions or issues:
1. Check SKILL.md documentation
2. Review examples in Pattern Library sections
3. Ask in team channel
4. Create task in "Intelligence System Improvements" project

---

*The intelligence you capture today informs the decisions you make tomorrow. Invest in quality now, benefit from insights later.*
