# Workflow Process Generator - File Index

Complete navigation guide for the Workflow Process Generator skill.

---

## Core Documentation

### [README.md](README.md) ⭐ Start Here
**Primary skill documentation** - Executive summary, quick start, workflow categories, quality standards, and usage examples.

**When to Read:** First time using the skill or need overview of capabilities.

---

## Reference Documentation

### Extraction & Data Sources

#### [data-extraction-guide.md](references/data-extraction-guide.md)
**Comprehensive extraction methodology** for pulling workflow data from Asana, Google Drive, and Gmail.

**Sections:**
- Asana Integration Patterns (project templates, task sequences, custom fields)
- Drive Integration Patterns (sequential language, decision terminology, role assignments)
- Gmail Integration Patterns (email sequences, handoffs, timeline clustering)
- Extraction process walkthroughs for each source
- Data-to-workflow mapping examples

**When to Read:** Before extracting workflow data from operational tools.

---

### Visual Standards & Generation

#### [mermaid-generation-standards.md](references/mermaid-generation-standards.md)
**Complete Mermaid diagram standards** including 360 brand colors, diagram type selection, and node formatting.

**Sections:**
- 360 Brand Color Palette (strictly enforced)
- Diagram Type Selection (flowchart, Gantt, sequence, Sankey)
- Node Content Structure (phase names, descriptions, owners, timelines)
- Styling Standards (theme configuration, edge formatting)
- Example diagrams for each type

**When to Read:** Before generating Mermaid visualizations.

---

#### [html-visualization-guide.md](references/html-visualization-guide.md)
**Advanced HTML generation** for executive presentations and interactive workflows.

**Sections:**
- When to Use HTML vs Mermaid
- Professional Typography Standards
- 360 Color Palette Implementation
- Interactive Elements (hover, zoom, pan, modals)
- HTML File Structure Template
- Complete Code Examples

**When to Read:** Creating executive presentations or board-ready materials.

---

### Workflow Categories

#### [workflow-categories.md](references/workflow-categories.md)
**Detailed descriptions** of the five workflow categories with patterns, decision points, and data sources.

**Categories:**
1. Partnership Development (2-12 months)
2. Client Engagement (1-6 months)
3. Innovation Assessment (2-8 weeks)
4. Ecosystem Mapping (3-12 weeks)
5. Internal Operations (varies)

**When to Read:** Understanding which workflow category applies to your use case.

---

### Process & Quality

#### [generation-workflow-guide.md](references/generation-workflow-guide.md)
**Complete 6-step generation process** from workflow identification to final artifact creation.

**Steps:**
1. Identify Workflow Type (clarifying questions)
2. Extract Source Data (systematic extraction)
3. Structure Data into JSON (standardized schema)
4. Generate Mermaid Diagram (visual creation)
5. Create Artifact (packaging and documentation)
6. Provide Context & Next Steps (insights and recommendations)

**When to Read:** Following the complete workflow generation process.

---

#### [quality-checklist.md](references/quality-checklist.md)
**Quality standards** for content completeness, visual quality, and data quality validation.

**Checklists:**
- Content Completeness (decision points, roles, timelines, metrics)
- Visual Quality (color coding, readability, spacing)
- Data Quality (source validation, cross-referencing, citations)

**When to Read:** Before finalizing any workflow visualization.

---

### Usage & Scenarios

#### [usage-scenarios.md](references/usage-scenarios.md)
**Common use cases** with detailed examples of skill application.

**Scenarios:**
- Team Onboarding (client engagement workflow)
- Board Meeting Preparation (partnership development)
- Partnership Documentation (external collaboration)
- Process Optimization (bottleneck analysis)
- Ecosystem Mapping Workshop (network visualization)
- Error handling and edge cases

**When to Read:** Understanding how to apply the skill to specific situations.

---

#### [maintenance-guide.md](references/maintenance-guide.md)
**Living documentation approach** for keeping workflows current and version control best practices.

**Sections:**
- Update Triggers (when to regenerate)
- Update Process (systematic regeneration)
- Version Control Best Practices
- Storage Strategy (GitHub repository structure)

**When to Read:** Maintaining and updating existing workflow documentation.

---

### Reference Examples

#### [vianeo-reference.md](references/vianeo-reference.md)
**Gold standard example** - The Vianeo Business Model Evaluation workflow as quality benchmark.

**Highlights:**
- Professional typography and visual design
- Interactive features (zoom, pan, hover, modals)
- 10-step workflow with three execution paths
- Time investments and prerequisites
- Comprehensive modal content

**When to Read:** Understanding the quality bar for executive presentations.

---

## Examples

### [partnership-development.md](examples/partnership-development.md)
**Complete partnership workflow** with annotations showing 6-phase process from initial contact to integration.

**Includes:**
- Mermaid flowchart with 360 brand colors
- Phase details (duration, owner, activities)
- Decision criteria at each gate
- Volume distribution percentages
- Common issues and success metrics
- Cultural considerations for international partnerships

**Use For:** Template for partnership documentation, board presentations on partnership pipeline.

---

### [client-engagement.md](examples/client-engagement.md)
**8-phase client workflow** from inquiry to delivery with conversion metrics.

**Includes:**
- Complete engagement lifecycle
- Qualification criteria checklist
- Service tier paths (Fast Track, Standard, Complete)
- 42% conversion rate and success metrics
- Common bottlenecks and optimization opportunities

**Use For:** Onboarding client-facing team members, proposal process documentation.

---

### [innovation-assessment.md](examples/innovation-assessment.md)
**Assessment workflow** integrating Vianeo framework with 360 Innovation Compass.

**Includes:**
- Methodology selection decision tree
- 10-step Vianeo process with three execution paths
- Evidence requirements and threshold gates
- Parallel evaluation dimensions (LDAFV framework)
- Time investments by assessment depth

**Use For:** Assessment process documentation, university TTO collaboration guides.

---

### [ecosystem-mapping.md](examples/ecosystem-mapping.md)
**Network visualization example** for stakeholder mapping and value network analysis.

**Includes:**
- Stakeholder categorization (5 positions)
- Relationship type mapping
- Sankey diagram for value flows
- Network diagram showing connections
- Color-coded acceptability (favorable/neutral/unfavorable)

**Use For:** Regional ecosystem documentation, stakeholder engagement planning.

---

## Templates

### Mermaid Templates

#### [mermaid-flowchart.md](templates/mermaid-flowchart.md)
**Reusable flowchart template** with 360 color palette and decision diamond structure.

**Use For:** Decision-heavy workflows, branching processes.

---

#### [mermaid-gantt.md](templates/mermaid-gantt.md)
**Gantt timeline template** for sequential processes with overlapping activities.

**Use For:** Partnership timelines, project execution phases.

---

#### [mermaid-sequence.md](templates/mermaid-sequence.md)
**Sequence diagram template** for multi-stakeholder workflows with handoffs.

**Use For:** Client engagement, partnership negotiations, ecosystem coordination.

---

### HTML & Data Templates

#### [html-interactive.html](templates/html-interactive.html)
**Interactive HTML template** with zoom, pan, and modal functionality.

**Use For:** Executive presentations, board meetings, partner-facing documentation.

---

#### [workflow-json-schema.json](templates/workflow-json-schema.json)
**Standardized data structure** for workflow information.

**Use For:** Structuring extracted workflow data before visualization generation.

---

## Quick Reference by Task

### "I need to document a workflow"
1. Read [README.md](README.md) for overview
2. Check [workflow-categories.md](references/workflow-categories.md) to identify category
3. Follow [generation-workflow-guide.md](references/generation-workflow-guide.md)
4. Use [quality-checklist.md](references/quality-checklist.md) before finalizing

### "I need to extract workflow from Asana"
1. Read [data-extraction-guide.md](references/data-extraction-guide.md) - Asana section
2. Use extraction patterns and API calls
3. Structure data with [workflow-json-schema.json](templates/workflow-json-schema.json)

### "I need to create a visual workflow"
1. Read [mermaid-generation-standards.md](references/mermaid-generation-standards.md)
2. Choose appropriate diagram type
3. Use templates in [templates/](templates/)
4. Apply 360 color palette

### "I need an executive presentation"
1. Read [html-visualization-guide.md](references/html-visualization-guide.md)
2. Review [vianeo-reference.md](references/vianeo-reference.md) for quality standard
3. Use [html-interactive.html](templates/html-interactive.html) template
4. Customize with workflow-specific content

### "I need examples for reference"
1. Browse [examples/](examples/) directory
2. Find workflow type matching your use case
3. Adapt structure and content to your workflow

---

## File Reading Order Recommendations

### For First-Time Users (60 minutes)
1. [README.md](README.md) - 15 min
2. [workflow-categories.md](references/workflow-categories.md) - 10 min
3. [generation-workflow-guide.md](references/generation-workflow-guide.md) - 20 min
4. [partnership-development.md](examples/partnership-development.md) - 15 min

### For Quick Workflow Creation (30 minutes)
1. [README.md](README.md) - Quick Start section - 5 min
2. [mermaid-generation-standards.md](references/mermaid-generation-standards.md) - 10 min
3. [mermaid-flowchart.md](templates/mermaid-flowchart.md) - 5 min
4. [quality-checklist.md](references/quality-checklist.md) - 10 min

### For Executive Presentations (90 minutes)
1. [vianeo-reference.md](references/vianeo-reference.md) - 20 min
2. [html-visualization-guide.md](references/html-visualization-guide.md) - 30 min
3. [partnership-development.md](examples/partnership-development.md) - 20 min
4. [html-interactive.html](templates/html-interactive.html) - 20 min

### For Data Extraction Focus (45 minutes)
1. [data-extraction-guide.md](references/data-extraction-guide.md) - 30 min
2. [workflow-json-schema.json](templates/workflow-json-schema.json) - 5 min
3. [usage-scenarios.md](references/usage-scenarios.md) - 10 min

---

## Document Status

### Complete ✅
- README.md
- INDEX.md

### In Progress 🚧
- references/ (8 files to be created)
- examples/ (4 files to be created)
- templates/ (5 files to be created)

### Planned 📋
- Integration guides with other 360 skills
- Video walkthroughs of workflow generation
- Workflow repository structure recommendations

---

## Version

**Index Version:** 1.0
**Last Updated:** 2025-11-15
**Next Review:** 2026-02-15

---

**Navigation Tip:** Use Ctrl+F (Cmd+F on Mac) to search this index for specific topics or file names.
