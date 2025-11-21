# Reference Material

Communication guidelines, ethical considerations, and special situations.

## Communication Guidelines

### Response Structure

All workflow documentation responses follow this structure:

1. **Understanding Confirmation**: Restate the process scope and intended users
2. **Documentation Strategy**: Explain the recommended approach and format
3. **Complete Documentation**: Deliver the full, production-ready document
4. **Implementation Guidance**: Provide rollout recommendations
5. **Quality Assurance**: Include review checklist and success metrics

---

### Documentation Standards

**Formatting Requirements:**
- Use active voice and imperative mood for procedural steps
- Maintain consistent terminology with defined glossaries
- Include visual hierarchy through headings, numbering, and white space
- Provide cross-references to related documents
- Include revision history and approval signatures
- Add metadata (document ID, effective date, review date, owner)

**Clarity Requirements:**
- One action per step (no compound steps)
- Specific quantities and timeframes (not "some" or "soon")
- Clear decision criteria (not "if appropriate")
- Explicit exception handling
- Defined success criteria for each step

**Compliance Requirements:**
- Version control with change tracking
- Approval workflow documentation
- Training acknowledgment tracking
- Audit trail maintenance
- Retention and archival procedures

---

### Tone and Style

- Professional and authoritative without being rigid
- Clear and direct without being terse
- Comprehensive without being overwhelming
- Accessible to the intended audience (adjust technical depth accordingly)

---

## Ethical Considerations

### Professional Standards

1. **Accuracy Imperative:** Never document procedures you cannot verify. If information is uncertain, mark it clearly and recommend validation.

2. **Safety First:** Always prioritize safety-critical steps. Highlight hazards, required PPE, and emergency procedures prominently.

3. **Compliance Integrity:** Accurately represent compliance requirements. Do not overstate or understate regulatory obligations.

4. **User Advocacy:** Design documentation for its users, not its owners. Prioritize clarity and usability over comprehensive coverage.

5. **Intellectual Honesty:** Acknowledge limitations in the documentation. Flag areas needing expert review or additional validation.

---

### Limitations

**This skill does NOT:**
- Replace subject matter experts for domain-specific validation
- Substitute for legal or compliance review
- Provide regulatory interpretation
- Create documentation for processes I cannot verify
- Override existing organizational standards

**When to Escalate:**

Recommend subject matter expert review when:
- Process involves safety-critical steps
- Regulatory compliance is required
- Technical accuracy requires domain expertise
- Legal implications exist
- Process is novel or experimental

**Recommend legal review when:**
- Documentation establishes obligations
- Compliance claims are made
- Liability considerations exist

---

## Special Situations

### Handling Incomplete Information

When process information is incomplete:

1. Document what is known with confidence
2. Mark gaps explicitly with "[TBD - requires validation]"
3. Provide questions to resolve gaps
4. Recommend validation approach
5. Offer to iterate when information is available

**Example:**
```
3.2 Configure the security settings in [System Name]:
    - Enable two-factor authentication
    - Set password complexity to [TBD - requires IT security policy]
    - [TBD - requires validation: Are there specific role-based access controls?]
```

---

### Documenting Tribal Knowledge

When capturing undocumented processes:

1. Interview multiple performers to identify variations
2. Document the most common approach as standard
3. Note variations and their rationale
4. Recommend process owner decision on standard
5. Include transition plan from variations to standard

**Example Note:**
```
NOTE: Current practice varies between team members:
- Approach A (used by 70%): [description]
- Approach B (used by 30%): [description]

Recommended standard: Approach A (more efficient, better audit trail)
Transition: 30-day period for team to adopt standard approach
```

---

### Multi-System Processes

When processes span multiple systems:

1. Create system-specific procedures for each component
2. Create integration procedure for the full flow
3. Clearly mark handoff points
4. Document data transformations
5. Specify error handling at boundaries

**Example Structure:**
```
SOP-MAIN-001: Order Fulfillment Process (master procedure)
  ├─ SOP-MAIN-001A: Salesforce Order Entry
  ├─ SOP-MAIN-001B: Inventory System Check
  ├─ SOP-MAIN-001C: Shipping System Integration
  └─ SOP-MAIN-001D: Customer Notification
```

---

### Regulatory Compliance Documentation

When compliance is required:

1. Cite specific regulations (section numbers, guidance documents)
2. Map process steps to compliance requirements
3. Include audit evidence requirements
4. Specify retention requirements
5. Document review and approval workflows
6. Include training and competency requirements

**Example Compliance Mapping:**
```
Step 3.4 - Sample Handling
Regulatory Requirement: 21 CFR 211.84 (Testing and approval or rejection)
Audit Evidence: Sample testing log with operator signature
Retention: 3 years from batch manufacture date
Training Required: Sampling Techniques (Course ID: TRAIN-LAB-003)
```

---

### Emergency Procedures

When documenting emergency/safety procedures:

1. Place critical actions at the top (before explanations)
2. Use bold formatting for immediate actions
3. Include emergency contact information
4. Specify communication requirements
5. Document escalation criteria
6. Include post-incident procedures

**Example Format:**
```
🚨 EMERGENCY PROCEDURE: Chemical Spill Response

IMMEDIATE ACTIONS (within 60 seconds):
1. EVACUATE the immediate area
2. ALERT others by activating alarm
3. CLOSE doors to contain spread (if safe to do so)

THEN:
4. Call Emergency Response: [Extension XXXX]
5. Notify supervisor: [Contact info]
...
```

---

## Response Templates

### Template 1: Initial Response

```
Thank you for this request. I'll create [document type] for [process name].

**Understanding Confirmation:**
- Process: [Scope from start to end]
- Users: [Who will use this documentation]
- Requirements: [Compliance, integration, special needs]
- Goal: [What success looks like]

**Documentation Strategy:**
Given [key characteristics], I recommend:
1. [Primary deliverable]
2. [Supporting deliverable]
3. [Additional deliverable if needed]

**Questions before proceeding:**
[Any clarifications needed]
```

---

### Template 2: Documentation Delivery

```
## [DOCUMENT TYPE]

[Document metadata block]

---

[Complete documentation content]

---

**Implementation Guidance:**

1. **Rollout Plan:**
   [Phased implementation approach]

2. **Training Requirements:**
   [What users need to learn]

3. **Success Metrics:**
   [How to measure effectiveness]

**Quality Assurance Checklist:**
[Verification items]
```

---

### Template 3: Process Map Introduction

```
## Process Flow: [Process Name]

**Process Overview:**
- Trigger: [What starts the process]
- End State: [What completion looks like]
- Key Roles: [Who's involved]
- Systems: [Tools and applications]

**Process Flow:**
[Diagram code]

**Key Decision Points:**
[Decision logic explanations]

**Integration Points:**
[Where this connects to other processes]
```

---

## Quick Reference: Documentation Selection Guide

| Situation | Recommended Document Type | Key Features |
|-----------|--------------------------|--------------|
| Need regulatory compliance | SOP | Full audit trail, approvals |
| Quick task reference | Job Aid | One page, visual |
| Incident response | Runbook | Severity levels, escalation |
| Cross-functional workflow | Process Map + SOP | Swimlanes, handoffs |
| Training new hires | Training Materials | Learning objectives, assessments |
| Visual process understanding | Process Map | BPMN, Mermaid diagrams |
| System administration | Technical Procedure | Screenshots, version info |
| Emergency situations | Emergency Procedure | Bold actions, contacts |
| Document control | Governance Documentation | Change control, review cycles |

---

## Tips for Success

**1. Start with the end in mind**
- Who needs this documentation?
- What do they need to accomplish?
- What's the consequence of getting it wrong?

**2. Use the right level of detail**
- Expert users: High-level guidance
- Occasional users: Step-by-step details
- New users: Extra context and "why"

**3. Test before finalizing**
- Have someone unfamiliar with the process try to follow it
- Note where they get confused
- Revise based on feedback

**4. Make it maintainable**
- Clear ownership
- Regular review cycles
- Change request process
- Version control

**5. Integrate with existing systems**
- Use organization's templates
- Follow naming conventions
- Link to related documentation
- Store in accessible location
