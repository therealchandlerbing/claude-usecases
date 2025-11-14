# Example: Process Documentation Generator

## Description
This skill guides you through creating comprehensive process documentation from raw information or existing workflows.

## Use Case
Use this skill when you need to document a business process, technical workflow, or operational procedure in a standardized format that is clear, actionable, and maintainable.

## Prerequisites
- Understanding of the process to be documented
- Access to subject matter experts (if needed)
- Examples of inputs/outputs for the process
- List of tools or systems involved

## Instructions

### Step 1: Gather Process Information
Collect the following information about the process:
- Process name and purpose
- Trigger events (what initiates the process)
- Key stakeholders and roles
- Required inputs
- Expected outputs
- Dependencies on other processes or systems

### Step 2: Map the Process Flow
Create a step-by-step breakdown:
1. Identify the starting point
2. List each major step in sequence
3. Note decision points and branches
4. Document alternative paths for exceptions
5. Define the end state(s)

### Step 3: Document Each Step
For each step in the process, document:
- **Action**: What needs to be done
- **Actor**: Who performs the action
- **Tools**: Systems or tools required
- **Duration**: Estimated time to complete
- **Success Criteria**: How to know the step is complete

### Step 4: Add Context and Examples
Enhance the documentation with:
- Real-world examples
- Common pitfalls and how to avoid them
- Tips for efficiency
- Related processes or dependencies
- FAQs

### Step 5: Review and Validate
- Share with stakeholders for feedback
- Test the documentation with someone unfamiliar with the process
- Refine based on feedback
- Add version control information

## Expected Outputs
- Structured process documentation in markdown format
- Clear step-by-step instructions
- Decision trees or flowcharts (if applicable)
- Examples and edge cases documented
- Version-controlled documentation ready for distribution

## Examples

### Example 1: Documenting a Customer Onboarding Process

**Input Information:**
- Process: New customer account setup
- Trigger: Sales team closes a deal
- Stakeholders: Sales, Operations, IT
- Tools: CRM, Email, Access Management System

**Expected Result:**
```markdown
# Customer Onboarding Process

## Purpose
Ensure smooth setup of new customer accounts within 48 hours of deal closure.

## Trigger
Sales representative marks opportunity as "Closed Won" in CRM

## Steps
1. **Sales Notification** (Sales Rep, 5 min)
   - Mark opportunity as won in CRM
   - Complete customer information form
   - Notify operations team

2. **Account Creation** (Operations, 30 min)
   - Create customer record in billing system
   - Set up access credentials
   - Configure initial settings

...
```

### Example 2: Technical Deployment Process

**Input Information:**
- Process: Application deployment to production
- Trigger: Release approval from QA
- Stakeholders: Development, DevOps, QA
- Tools: Git, CI/CD pipeline, Monitoring dashboard

**Expected Result:**
Detailed deployment runbook with commands, rollback procedures, and verification steps.

## Notes
- Keep documentation living and up-to-date
- Use clear, jargon-free language where possible
- Include visual aids (diagrams, screenshots) when helpful
- Version control is critical for process documentation
- Regular reviews ensure documentation stays relevant

## Related Skills
- workflow-analysis.md
- technical-documentation.md
- stakeholder-interviewing.md

## Version History
- v1.0 - 2025-11-14 - Initial example creation
