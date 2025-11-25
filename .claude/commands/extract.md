# Extract Intelligence from Content

Extract structured intelligence from the provided content using the **Intelligence Extractor** skill.

## Instructions

Invoke the `intelligence-extractor` skill to analyze the provided content (meeting transcript, email thread, conversation notes, or document).

## What to Extract

Analyze for three intelligence categories:

1. **Partnership Intelligence**
   - Organizations mentioned
   - Collaboration opportunities
   - Relationship temperature (Cold/Warming/Hot/Active/Stalled)
   - Decision timelines

2. **Funding Opportunity Intelligence**
   - Grants, investors, programs mentioned
   - Funding amounts and deadlines
   - Application requirements
   - Contact information

3. **Stakeholder Intelligence**
   - Key individuals and their roles
   - Decision-makers and influencers
   - Communication preferences
   - Action items and commitments

## Output Format

Return valid JSON with:
- `extraction_summary` - Brief overview of findings
- `intelligence_items` - Structured data for each entity
- `flagged_for_review` - Items needing human verification
- `cross_references` - Connections between entities

## Usage

If no content is provided in the conversation, ask the user to:
1. Paste the transcript/email/notes
2. Or provide a file path to read

---

**Skill**: intelligence-extractor
**Trigger**: "Extract intelligence from this transcript" / "Analyze this meeting"
