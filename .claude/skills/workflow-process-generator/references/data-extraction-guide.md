# Data Extraction Guide

Complete methodology for extracting workflow data from Asana, Google Drive, and Gmail.

---

## Overview

**Purpose:** Systematically extract workflow intelligence from operational tools to generate accurate, evidence-based process documentation.

**Data Sources:**
1. **Asana** - Structured workflow templates and active project data
2. **Google Drive** - Process documentation and operational guides
3. **Gmail** - Communication patterns revealing implicit workflows

**Extraction Philosophy:** Pull from actual operational data rather than assumed processes. What people actually do > what they think they do.

---

## Asana Integration: The Source of Truth for Active Workflows

### What to Extract

#### 1. Project Structure
**Sections** represent workflow phases
- Section ordering shows sequence
- Section names indicate phase purpose
- Section count suggests workflow complexity

**Example Mapping:**
```
Asana Section: "Initial Contact"     → Workflow Phase 1
Asana Section: "Qualification"       → Workflow Phase 2
Asana Section: "Proposal Development" → Workflow Phase 3
```

#### 2. Task Sequences
**Tasks** reveal detailed activities within phases
- Dependencies create flow logic
- Task completion shows progression
- Subtasks reveal detailed activities

**Example Mapping:**
```
Task: "Conduct alignment call"         → Activity in Phase 1
Dependency: "After alignment approved" → Flow prerequisite
Subtask: "Prepare call agenda"         → Detailed activity
```

#### 3. Custom Fields
**Custom fields** indicate decision points and metrics
- Stage/Status fields → Decision points
- Priority/Effort fields → Volume indicators
- Approval fields → Gate criteria

**Example Mapping:**
```
Custom Field "Stage": [Inquiry | Qualified | Proposed | Won | Lost]
  → Decision point with 5 possible outcomes
  → Track conversion percentages

Custom Field "Priority": [High | Medium | Low]
  → Volume distribution indicator
  → Resource allocation signal
```

#### 4. Task Details
**Descriptions and comments** contain process knowledge
- Descriptions: Detailed activity instructions
- Comments: Edge cases and issues
- Attachments: Supporting documentation links

**Example Usage:**
```
Task Description: "Check alignment on 3 criteria: mission, capability, resources"
  → Extracts qualification criteria

Comment: "Brazil partnerships often need 2-3 extra touchpoints"
  → Captures cultural variation
```

#### 5. People Data
**Assignees and followers** show ownership and stakeholders
- Assignees → Phase owners/roles
- Followers → Stakeholders
- Activity patterns → Handoff sequences

**Example Mapping:**
```
Assignee: Business Development  → Phase owner
Follower: Legal Team            → Stakeholder in phase
Assignee change: BD → Legal     → Handoff point
```

#### 6. Timeline Data
**Dates** establish duration and identify bottlenecks
- Due dates → Phase duration
- Start dates → Phase timing
- Date patterns → Bottleneck identification

**Example Analysis:**
```
Phase 1 tasks: 7-day span (consistent)
Phase 4 tasks: 28-56 day span (high variance) → Bottleneck
```

---

### Extraction Process

#### Step 1: Discover Projects
```
Tool: asana_typeahead_search

asana_typeahead_search(
  workspace_gid="[360_workspace_id]",
  query="[workflow_name]",
  resource_type="project"
)

Returns: List of matching projects with IDs

Example:
Query: "partnership development"
Returns: [
  {id: "123", name: "Partnership Development Template"},
  {id: "456", name: "GenIP Partnership Project"}
]
```

#### Step 2: Get Full Project Data
```
Tool: asana_get_project

asana_get_project(
  project_id="[found_id]",
  opt_fields="sections,custom_fields,owner,members,archived,notes"
)

Returns: Complete project configuration

Key Fields:
- sections: Phase structure
- custom_fields: Decision logic
- owner: Process owner
- notes: Process documentation
```

#### Step 3: Map Phase Structure
```
Tool: asana_get_project_sections

asana_get_project_sections(
  project_id="[project_id]"
)

Returns: Ordered list of sections (phases)

Example Output:
[
  {id: "sec1", name: "Initial Contact", index: 0},
  {id: "sec2", name: "Qualification", index: 1},
  {id: "sec3", name: "Proposal", index: 2}
]

Workflow Interpretation:
Phase 1: Initial Contact
Phase 2: Qualification
Phase 3: Proposal
```

#### Step 4: Get Tasks by Phase
```
Tool: asana_get_tasks

asana_get_tasks(
  project="[project_id]",
  section="[section_id]"
)

Returns: Tasks within specific phase

Example for "Initial Contact" phase:
[
  {id: "task1", name: "Research organization"},
  {id: "task2", name: "Schedule alignment call"},
  {id: "task3", name: "Document alignment assessment"}
]
```

#### Step 5: Get Task Details
```
Tool: asana_get_task

asana_get_task(
  task_id="[task_id]",
  opt_fields="custom_fields,dependencies,dependents,assignee,due_on,notes,tags"
)

Returns: Complete task configuration

Key Data Points:
- custom_fields: Decision criteria, stage
- dependencies: Prerequisites
- assignee: Role/owner
- due_on: Timeline
- notes: Detailed instructions
```

#### Step 6: Get Activity History (Optional)
```
Tool: asana_get_stories_for_task

asana_get_stories_for_task(
  task_id="[task_id]"
)

Returns: Comments, status changes, timeline

Use For:
- Understanding common issues (from comments)
- Identifying typical timeline (from completion patterns)
- Discovering edge cases (from problem discussions)
```

---

### Asana → Workflow Mapping

**Systematic Translation:**

```json
{
  "sections": "workflow_phases",
  "section_order": "phase_sequence",
  "tasks_in_section": "activities_within_phase",
  "custom_field_stage": "decision_point_or_status",
  "custom_field_priority": "volume_indicator",
  "custom_field_approval": "gate_criteria",
  "dependencies": "flow_sequence_and_prerequisites",
  "assignee": "phase_owner_or_role",
  "due_dates": "timeline_and_duration_data",
  "tags": "workflow_categorization",
  "comments": "edge_cases_and_issues"
}
```

---

### Complete Example: Client Engagement Workflow

**Step-by-Step Extraction:**

```
1. Search for project
   asana_typeahead_search("client engagement template")

   Result: Project ID "789"

2. Get project structure
   asana_get_project("789", opt_fields="sections,custom_fields")

   Result: 8 sections found
   - Inquiry
   - Qualification
   - Proposal Development
   - Proposal Review
   - Contract Negotiation
   - Project Kickoff
   - Execution
   - Delivery & Closeout

3. Get tasks for each section
   asana_get_tasks(project="789", section="inquiry_section_id")

   Inquiry Section Tasks:
   - Capture client details (5 min)
   - Initial needs assessment (15 min)
   - Send acknowledgment email (5 min)

   Qualification Section Tasks:
   - Budget verification
   - Timeline alignment
   - Scope fit assessment
   - Decision: Proceed or decline

4. Extract custom fields
   Custom field "Stage": [Inquiry, Qualified, Proposed, Won, Lost]
   Custom field "Service Tier": [Fast Track, Standard, Complete]

5. Map to workflow structure
   Phase 1: Inquiry (3 tasks, ~25 min)
     → Decision: Qualified? (custom field)
     → Branches: Yes (60%) → Phase 2, No (40%) → Decline

   Phase 2: Qualification (4 tasks, ~2 hours)
     → Activities: Budget, timeline, scope, fit
     → Decision: Proceed? (custom field)
     → Branches: Yes (75%) → Phase 3, No (25%) → Decline

6. Calculate metrics
   From 100 completed projects:
   - 60% pass qualification → 60 proposals
   - Of 60 proposals, 70% accepted → 42 projects executed
   - Overall conversion: 42% inquiry → completion
```

---

## Google Drive Integration: Document-Based Process Intelligence

### What to Extract

#### 1. Sequential Language
**Pattern words** indicating process flow:
- "first," "then," "next," "finally"
- "step 1," "phase 2," numbered lists
- "before," "after," "during"

**Example:**
```
Document text: "First, conduct initial alignment call. Then, if aligned,
               schedule scoping workshop within 2 weeks."

Extracted:
  Phase 1: Initial Alignment Call
  Decision: Aligned?
  Phase 2: Scoping Workshop (within 2 weeks if aligned)
```

#### 2. Decision Terminology
**Conditional language** revealing branching logic:
- "if," "when," "depending on"
- "branches," "paths," "options"
- "criteria," "threshold," "gate"

**Example:**
```
Document text: "If mission alignment score > 7/10 AND capability fit
               confirmed, proceed to scoping. Otherwise, polite decline."

Extracted:
  Decision Criteria: Mission alignment > 7/10 AND capability fit
  Branch 1: Met → Proceed to scoping
  Branch 2: Not met → Polite decline
```

#### 3. Role Assignments
**Ownership language** identifying who does what:
- "team responsible," "owner," "lead"
- "stakeholder," "approver," "reviewer"
- Named individuals or job titles

**Example:**
```
Document text: "Business Development leads initial contact. Legal team
               reviews all partnership agreements. Executive approval
               required for commitments >$50K."

Extracted:
  Phase 1 Owner: Business Development
  Phase 4 Owner: Legal Team
  Gate: Executive approval (threshold: $50K+)
```

#### 4. Timeline Markers
**Temporal indicators** establishing duration:
- "week 1," "day 3," "month 2"
- "after approval," "before kickoff"
- Duration estimates ("typically 2-4 weeks")

**Example:**
```
Document text: "Legal review typically takes 4-8 weeks. After legal
               approval, formalization is completed within 1-2 weeks."

Extracted:
  Phase 4 Duration: 4-8 weeks (Legal Review)
  Phase 5 Duration: 1-2 weeks (Formalization)
  Dependency: Phase 5 starts after Phase 4 completion
```

#### 5. Success Criteria
**Deliverable language** defining phase completion:
- "deliverable," "milestone," "completion criteria"
- "must have," "required," "critical"
- "output," "artifact," "result"

**Example:**
```
Document text: "Scoping phase is complete when both parties have signed
               the scope agreement and resource commitments are documented."

Extracted:
  Phase 3 Success Criteria:
  - Scope agreement signed by both parties
  - Resource commitments documented
```

#### 6. Edge Cases
**Problem language** revealing common issues:
- "common issues," "failure modes"
- "alternatives," "workarounds"
- "what if," "exception," "special case"

**Example:**
```
Document text: "If Brazil partnership, expect 2-4 additional touchpoints
               for relationship building. Cultural context gathering
               critical for success."

Extracted:
  Geographic Variation: Brazil partnerships
  Phase 2 Duration Adjustment: +2-4 weeks
  Required Activity: Cultural context gathering
```

---

### Extraction Process

#### Step 1: Search by Workflow Type
```
Tool: google_drive_search

google_drive_search(
  api_query="name contains '[workflow_name]' and mimeType='application/vnd.google-apps.document'",
  semantic_query="process workflow steps methodology"
)

Returns: Matching documents

Example:
Query: "partnership process"
Returns: [
  "GenIP Partnership Development Guide.docx",
  "Partnership Workflow SOP.gdoc",
  "Brazil Partnership Best Practices.pdf"
]
```

#### Step 2: Fetch Document Contents
```
Tool: google_drive_fetch

google_drive_fetch(
  document_ids=["[doc_id_1]", "[doc_id_2]"]
)

Returns: Full text content of documents
```

#### Step 3: Parse for Process Indicators

**Pattern Matching:**
```
Sequential Indicators:
  Regex: (first|then|next|after|before|step \d+|phase \d+)

Decision Indicators:
  Regex: (if|when|depending on|branches|criteria|threshold)

Role Indicators:
  Regex: (responsible|owner|lead|team|stakeholder|approver)

Timeline Indicators:
  Regex: (week \d+|day \d+|month \d+|\d+-\d+ weeks|\d+ hours)
```

**Extraction Example:**
```
Document Section:
"Partnership Development Process

Step 1: Initial Contact (1-2 weeks)
The Business Development team conducts initial research and schedules
an alignment call. If mission alignment is strong (score 7+), proceed
to relationship building phase.

Step 2: Relationship Building (2-8 weeks)
Partnership Lead facilitates minimum 3 touchpoints. Brazil partnerships
typically require 4-8 weeks due to cultural relationship building.

Success Criteria:
- Trust established between teams
- Clear collaboration areas identified
- Stakeholder buy-in secured"

Extracted Structure:
{
  "phases": [
    {
      "id": "phase1",
      "name": "Initial Contact",
      "duration": "1-2 weeks",
      "owner": "Business Development",
      "activities": ["Research", "Alignment call"],
      "decision": {
        "criteria": "Mission alignment score 7+",
        "options": ["Proceed to Phase 2", "Exit"]
      }
    },
    {
      "id": "phase2",
      "name": "Relationship Building",
      "duration": "2-8 weeks",
      "duration_variation": "Brazil: 4-8 weeks",
      "owner": "Partnership Lead",
      "activities": ["Minimum 3 touchpoints"],
      "success_criteria": [
        "Trust established",
        "Collaboration areas identified",
        "Stakeholder buy-in"
      ]
    }
  ]
}
```

#### Step 4: Structure into Standardized Format
```json
{
  "workflow_name": "[Extracted from document title]",
  "workflow_type": "[Inferred from content]",
  "phases": [
    {
      "name": "[Phase name]",
      "duration": "[Duration range]",
      "owner": "[Role/team]",
      "activities": ["[Activity 1]", "[Activity 2]"],
      "decision": {
        "question": "[Decision to make]",
        "criteria": "[Decision criteria]",
        "options": ["[Option 1]", "[Option 2]"]
      }
    }
  ]
}
```

---

### Key Search Patterns by Workflow Type

#### Partnership Workflows
**Search Terms:**
- "partnership process," "collaboration stages," "joint venture workflow"
- "agreement process," "partnership development," "relationship building"

**Look For:**
- Cultural considerations (international vs domestic)
- Legal review processes
- Relationship building timeline
- Structure options (JV, licensing, distribution)

#### Assessment Workflows
**Search Terms:**
- "evaluation process," "scoring methodology," "assessment steps"
- "framework," "validation," "due diligence process"

**Look For:**
- Methodology selection criteria (Vianeo vs 360 Compass)
- Scoring rubrics and thresholds
- Evidence requirements
- Quality gates

#### Client Workflows
**Search Terms:**
- "engagement process," "project phases," "delivery stages"
- "proposal process," "client onboarding," "service delivery"

**Look For:**
- Service tiers and paths (Fast Track, Standard, Complete)
- Qualification criteria
- Proposal templates
- Deliverable requirements

---

### Complete Example: GenIP Partnership Process

**Document Found:**
"GenIP Partnership Development Guide.docx"

**Extracted Content Analysis:**

```
Document Structure:
Section 1: Overview
Section 2: Initial Alignment
Section 3: Scoping Process
Section 4: Agreement Development
Section 5: Operational Integration

Extraction Results:

Phase 1: Initial Alignment
  Duration: "typically 2-3 weeks for first meeting and follow-up"
  Owner: "Business Development Lead"
  Activities:
    - "Research GenIP mission and current portfolio"
    - "Schedule introductory call with GenIP leadership"
    - "Assess alignment on 5 criteria: mission, geography, capability, resources, culture"
  Decision Point:
    "If 4 out of 5 criteria met, proceed to scoping. If 3 or fewer, respectful decline."

Phase 2: Scoping Workshop
  Duration: "half-day to full-day workshop, scheduled 2-4 weeks after alignment"
  Owner: "Joint working group (360 + GenIP teams)"
  Activities:
    - "Define collaboration areas (tech assessment, ecosystem mapping, training)"
    - "Identify resource commitments from each party"
    - "Draft preliminary terms"
  Success Criteria:
    - "Both parties commit to specific collaboration areas in writing"
    - "Resource commitments documented and approved internally"

Phase 3: Legal Review
  Duration: "4-6 weeks typically, but has ranged 2-10 weeks historically"
  Owner: "Legal teams (both sides)"
  Common Issues:
    - "IP ownership negotiations (add 1-2 weeks)"
    - "Liability terms (add 1 week)"
  Decision Point:
    "If terms acceptable to both legal teams, proceed to finalization.
     If significant disagreement, return to scoping or exit."
```

**Workflow Visualization Created:**
6-phase partnership process with 2 major decision gates, 3-7 month timeline, and documented common bottleneck (legal review averaging 5 weeks vs planned 4).

---

## Gmail Integration: Implicit Workflow Discovery

### What to Extract

#### 1. Email Sequences Showing Progression
**Thread evolution** reveals phase transitions:
- Subject line changes → Workflow stage shifts
- Time gaps between messages → Phase boundaries
- Participant changes → Handoffs

**Example:**
```
Thread 1: "GenIP Partnership - Initial Discussion" (Jan 5-8)
  Participants: Chandler, GenIP contact
  → Phase 1: Initial Contact

Thread 2: "RE: GenIP Partnership - Scoping Prep" (Jan 22)
  Participants: Chandler, GenIP contact, 360 team, GenIP team
  Subject change indicates new phase
  2-week gap suggests Phase 1 duration
  → Phase 2: Scoping Preparation

Thread 3: "GenIP Scope Agreement - Draft for Review" (Feb 1)
  Attachment: Scope agreement draft
  → Phase 3: Formalization
```

#### 2. Decision Points in Discussions
**Decision language** in email content:
- "approved," "declined," "needs revision"
- "moving forward with," "holding on"
- Conditional statements ("if X, then Y")

**Example:**
```
Email: "After discussion, we've decided to proceed with the joint
       venture structure rather than licensing. Legal will draft
       terms based on our scoping workshop notes."

Extracted:
  Decision Made: Structure selection
  Option Selected: Joint venture
  Alternative Considered: Licensing
  Next Phase: Legal drafting (owner: Legal team)
```

#### 3. Handoff Language
**Transition indicators** showing role changes:
- "passing to," "next step with," "looping in"
- "taking over," "transferring," "handing off"
- CC pattern changes

**Example:**
```
Email: "Thanks for the scoping work, team. I'm looping in Legal
       (cc'd) to begin agreement review. They'll take it from here."

Extracted:
  Handoff Point: After scoping completion
  From: Business Development / Partnership Lead
  To: Legal Team
  Phase Transition: Scoping → Legal Review
```

#### 4. Timeline Information
**Date patterns** revealing phase duration:
- Thread start/end dates → Phase duration
- Response time patterns → Urgency level
- Follow-up intervals → Dependency timing

**Example:**
```
Thread Analysis:
  Initial email: March 1
  First response: March 2 (1 day - high priority)
  Second round: March 8 (6 days - normal pace)
  Final email: March 22 (2 weeks later)

Interpretation:
  Phase Duration: ~3 weeks
  Urgency: High initial, normal ongoing
  Pattern: Quick kickoff, standard execution
```

#### 5. Stakeholder Involvement Patterns
**Participant changes** showing ecosystem:
- New participants added → Stakeholder involvement
- CC additions → Approval requirements
- External parties → Partnership ecosystem

**Example:**
```
Thread Evolution:
  Email 1: Chandler ↔ Client
  Email 3: Chandler ↔ Client (cc: 360 technical team)
  Email 5: Chandler ↔ Client (cc: 360 team, Partner org)

Interpretation:
  Phase 1: Direct business development
  Phase 2: Technical team involvement (feasibility check)
  Phase 3: Partner coordination (collaborative delivery)
```

#### 6. Issue Resolution Pathways
**Problem threads** revealing edge cases:
- Problem identification emails
- Discussion of solutions/workarounds
- Resolution confirmation

**Example:**
```
Thread: "GenIP Partnership - Legal Review Delay"

Email 1: "Legal review taking longer than expected due to IP concerns"
Email 2: "Could we fast-track by using our standard IP template?"
Email 3: "Legal approved template approach, back on track"

Extracted Edge Case:
  Common Issue: Legal review delays due to IP negotiations
  Typical Cause: Custom IP terms vs standard template
  Workaround: Use pre-approved standard template when possible
  Time Saved: 1-2 weeks
```

---

### Extraction Process

#### Step 1: Search for Process-Related Threads
```
Tool: search_gmail_messages

search_gmail_messages(
  q="subject:[process_name] OR [related_keywords]"
)

Returns: Matching email threads

Example:
Query: "subject:partnership OR collaboration OR joint venture"
Returns: 47 threads related to partnership development
```

#### Step 2: Read Complete Threads
```
Tool: read_gmail_thread

read_gmail_thread(
  thread_id="[thread_id]",
  include_full_messages=true
)

Returns: Full thread with all messages, timestamps, participants, attachments

Analysis Focus:
- First message date → Phase start
- Last message date → Phase end
- Participant list → Roles involved
- Subject line → Phase identifier
- Attachments → Deliverables
```

#### Step 3: Identify Workflow Patterns

**Multi-Participant Threads (Handoffs):**
- Look for threads with 3+ participants
- Participant changes indicate phase transitions
- CC patterns show approval requirements

**Example:**
```
Thread Participants Analysis:
  Messages 1-3: Chandler, Client (2 people)
  Messages 4-6: Chandler, Client, Legal (3 people - Legal added)
  Messages 7-9: Legal, Client Legal (2 people - Chandler drops off)

Workflow Extraction:
  Phase 1: Business Development (Chandler ↔ Client)
  Handoff: Add Legal to thread
  Phase 2: Legal Review (Legal teams coordinate)
```

**Date Clustering (Phase Transitions):**
- Gaps of 1+ weeks often indicate phase boundaries
- Rapid exchanges indicate active work within phase
- Follow-up patterns reveal dependencies

**Example:**
```
Thread Timeline:
  Jan 5-8: 5 emails (rapid - active phase)
  Jan 9-21: silence (phase transition / waiting)
  Jan 22-25: 4 emails (rapid - new phase active)
  Jan 26-Feb 10: silence (waiting / dependency)
  Feb 11-15: 3 emails (final phase)

Phase Interpretation:
  Phase 1: Jan 5-8 (4 days active work)
  Waiting: Jan 9-21 (13 days - likely internal decision)
  Phase 2: Jan 22-25 (4 days active work)
  Waiting: Jan 26-Feb 10 (16 days - likely external dependency)
  Phase 3: Feb 11-15 (5 days - completion)
```

**Subject Line Evolution (Workflow Progression):**
- Subject changes track workflow stages
- "Re: [Original]" vs "[New Subject]" indicates shift
- Keywords in subject reveal current phase

**Example:**
```
Subject Evolution:
  "CNEN Partnership Inquiry" → Phase 1: Initial Contact
  "RE: CNEN - Assessment Scope Discussion" → Phase 2: Scoping
  "CNEN Assessment - Framework Selection" → Phase 3: Methodology
  "CNEN Draft Report Ready" → Phase 4: Delivery

Workflow Extraction:
  4 distinct phases identified from subject line keywords
  Progression: Inquiry → Scope → Execution → Delivery
```

**Attachment Patterns (Deliverable Stages):**
- First attachments: Requirements or briefs
- Middle attachments: Drafts and iterations
- Final attachments: Approved deliverables

**Example:**
```
Attachment Timeline:
  Jan 5: "Assessment Requirements.pdf"
  Jan 22: "CNEN Tech Descriptions.zip"
  Feb 1: "Draft Assessment Results.xlsx"
  Feb 8: "Draft Assessment Results v2.xlsx"
  Feb 15: "Final CNEN Assessment Report.docx"

Workflow Interpretation:
  Phase 1: Requirements gathering (Jan 5)
  Phase 2: Information collection (Jan 22)
  Phase 3: Analysis and iteration (Feb 1-8, 2 draft versions)
  Phase 4: Final delivery (Feb 15)

Total Duration: 6 weeks
Iteration Count: 2 draft versions suggest standard review process
```

---

### Complete Example: CNEN Assessment Workflow

**Gmail Search:**
```
Query: "subject:CNEN OR (nuclear AND assessment)"
Results: 8 threads spanning January-February 2025
```

**Thread Analysis:**

**Thread 1: "CNEN Nuclear Technology Assessment - Inquiry"**
- Date Range: Jan 15-18 (4 days)
- Participants: Chandler, CNEN contact, 360 team
- Attachments: 5 PDF files (technology descriptions)
- **Identified Phase:** Intake & Requirements Gathering

**Thread 2: "CNEN Assessment - Framework Selection" (Internal)**
- Date Range: Jan 22-25 (4 days)
- Participants: 360 assessment team only (internal discussion)
- Content: Discussion of Vianeo vs 360 Compass framework
- Decision Email: "Going with Vianeo for comprehensive business validation"
- **Identified Phase:** Methodology Selection (Decision Point)

**Thread 3: "CNEN Assessment - Progress Update"**
- Date Range: Feb 1-15 (2 weeks)
- Participants: Chandler ↔ CNEN contact
- Attachments: Draft assessment results (Feb 1, Feb 8)
- **Identified Phase:** Evaluation Execution with 2-iteration review cycle

**Thread 4: "CNEN Final Report - Ready for Review"**
- Date: Feb 20
- Participants: Chandler, CNEN contact, CNEN leadership (added to CC)
- Attachments: Final DOCX report
- **Identified Phase:** Delivery & Review

**Workflow Extracted:**

```
CNEN Assessment Workflow (6 weeks total)

Phase 1: Intake (3 days)
  Duration: Jan 15-18
  Owner: Business Development
  Activities: Capture requirements, receive tech descriptions
  Output: 5 technology description files

Decision Point: Methodology Selection (4 days)
  Duration: Jan 22-25
  Owner: 360 Assessment Team (internal)
  Options: Vianeo Business Validation vs 360 Innovation Compass
  Decision: Vianeo (selected for comprehensive business model evaluation)
  Rationale: Nuclear tech requires full market validation

Phase 2: Evaluation Execution (2 weeks)
  Duration: Feb 1-15
  Owner: 360 Technical Team
  Activities: Technology assessment using Vianeo framework
  Iteration: 2 draft versions (Feb 1, Feb 8)
  Review Cycle: 1 week between drafts

Phase 3: Report Delivery (1 day)
  Duration: Feb 20
  Owner: Business Development
  Activities: Final report delivery to CNEN leadership
  Output: Final assessment report (DOCX)

Success Metrics:
  Total Timeline: 6 weeks (inquiry to delivery)
  Iteration Count: 2 drafts (standard for this workflow type)
  Stakeholder Satisfaction: Leadership added to final email (escalation signal = high importance)

Common Pattern Identified:
  Assessment workflows follow 3-phase pattern:
  1. Intake (3-5 days)
  2. Evaluation (2-3 weeks with 2 iterations)
  3. Delivery (1-2 days)

Bottleneck Noted:
  Gap between Phase 1 and Phase 2 (4 days for methodology selection)
  → Opportunity: Pre-define methodology based on technology type to eliminate delay
```

---

## Data Source Selection Guide

### When to Use Each Source

**Use Asana When:**
- ✅ Workflow has established project template
- ✅ Need structured phase and task data
- ✅ Want duration and timeline estimates
- ✅ Seeking decision logic from custom fields
- ✅ Need to understand designed/planned workflow

**Use Google Drive When:**
- ✅ Workflow is documented but not in Asana
- ✅ Need narrative descriptions of process
- ✅ Extracting from partnership agreements or SOPs
- ✅ Understanding rationale and context
- ✅ Discovering success criteria and edge cases

**Use Gmail When:**
- ✅ Workflow is implicit (not formally documented)
- ✅ Need to understand actual practice vs designed process
- ✅ Identifying bottlenecks and delays
- ✅ Discovering handoff points and stakeholder involvement
- ✅ Understanding real timeline (vs planned)
- ✅ Finding edge cases from problem resolution threads

---

## Multi-Source Synthesis

**Best Practice:** Combine multiple sources for comprehensive workflow mapping.

**Example Workflow:**
1. **Extract from Asana** → Get designed workflow structure (8 phases, planned timeline)
2. **Validate with Gmail** → Compare actual timeline (Phase 4 consistently takes 2x planned time)
3. **Enhance with Drive** → Add detailed criteria and edge cases from SOPs

**Result:** Workflow showing both designed process and actual execution with identified bottlenecks and optimization opportunities.

---

## Quality Validation

**After Extraction, Validate:**

1. **Completeness Check**
   - [ ] All phases have owners
   - [ ] Duration estimates are provided
   - [ ] Decision criteria are clear
   - [ ] Activities are actionable

2. **Accuracy Check**
   - [ ] Cross-reference multiple sources
   - [ ] Confirm with workflow owner if possible
   - [ ] Flag assumptions vs confirmed data
   - [ ] Cite specific sources

3. **Currency Check**
   - [ ] Source data is recent (within 6 months ideal)
   - [ ] Process hasn't evolved since data capture
   - [ ] Asana projects not archived
   - [ ] Drive documents are latest version

**Data Quality Indicators:**
- High: Multiple sources confirm same workflow
- Medium: Single authoritative source (recent Asana template)
- Low: Inferred from limited/old data

**Always flag data quality level in final workflow documentation.**

---

## Version History

- **v1.0** - 2025-11-15 - Initial creation with comprehensive extraction methodology for Asana, Drive, and Gmail

---

**Next:** [Mermaid Generation Standards](mermaid-generation-standards.md) - Learn how to visualize extracted workflow data
