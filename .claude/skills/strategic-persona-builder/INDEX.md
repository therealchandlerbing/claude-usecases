# Strategic Persona Builder - File Index

Navigate all documentation, examples, and reference materials for the Strategic Persona Builder skill.

---

## Directory Structure

```
strategic-persona-builder/
├── README.md                               # Brief overview and getting started
├── SKILL.md                                # Complete operational specification
├── QUICK-START.md                          # 5-minute onboarding guide
├── INDEX.md                                # This file - navigation
├── references/                             # Deep-dive documentation
│   ├── vianeo-framework.md                 # Vianeo four-layer structure details
│   ├── scoring-rubric.md                   # Quality scoring criteria (1-5)
│   ├── interview-templates.md              # Research planning guides
│   └── frameworks-comparison.md            # JTBD, empathy mapping, hybrid
├── examples/                               # Sample personas at different quality levels
│   ├── partner-persona-validated.md        # Score 4 - Strong quality
│   └── innovator-persona-inferred.md       # Score 2 - Needs validation
└── templates/                              # Output format templates
    ├── strategic-version.md                # Full strategic output format
    └── platform-ready.md                   # Vianeo platform entry format
```

---

## Core Documentation

### README.md
**Purpose:** Entry point and brief overview
**Length:** ~1,000 words
**Read this for:** Quick understanding of capabilities, when to use, basic examples

### SKILL.md
**Purpose:** Complete operational specification
**Length:** ~3,500 words
**Read this for:** Full workflow, all frameworks, quality standards, integration details

### QUICK-START.md
**Purpose:** 5-minute onboarding guide
**Length:** ~1,500 words
**Read this for:** Fast path to first persona set, common invocations, troubleshooting

---

## Reference Documentation

### references/vianeo-framework.md
**Purpose:** Deep-dive on Vianeo four-layer structure
**Topics:** Layer details, field requirements, platform constraints, scoring alignment
**Read this when:** Building personas for Vianeo submissions, understanding structure depth

### references/scoring-rubric.md
**Purpose:** Quality scoring criteria and improvement pathways
**Topics:** Score 1-5 definitions, evidence requirements, gap identification, upgrade paths
**Read this when:** Assessing persona quality, planning research for score improvement

### references/interview-templates.md
**Purpose:** Research planning and interview design guides
**Topics:** Questions per framework layer, persona-type specific questions, sample scripts
**Read this when:** Planning validation interviews, designing research protocols

### references/frameworks-comparison.md
**Purpose:** Compare JTBD, empathy mapping, and hybrid approaches
**Topics:** Framework strengths, best-fit use cases, combining frameworks, output formats
**Read this when:** Choosing framework beyond Vianeo, designing hybrid approaches

---

## Examples

### examples/partner-persona-validated.md
**Type:** Partner persona
**Quality:** Score 4 (Strong)
**Sources:** 8 interviews
**Purpose:** Demonstrate high-quality validated persona with evidence tracking

**Features:**
- Complete Vianeo four-layer structure
- Evidence appendix with sourced quotes
- Quantified pain points
- Specific current solutions
- Quality assessment with justification

### examples/innovator-persona-inferred.md
**Type:** Innovator persona
**Quality:** Score 2 (Weak)
**Sources:** Project docs + behavioral data, no interviews
**Purpose:** Demonstrate inferred persona with validation gaps

**Features:**
- Heavy validation markers
- Hypothesis labeling
- Research gap identification
- Validation questions generated
- Improvement pathway documented

---

## Templates

### templates/strategic-version.md
**Purpose:** Full strategic persona output format
**Use for:** Internal strategy, team alignment, decision-making

**Sections:**
- Executive summary
- Individual personas (full framework structure)
- Evidence appendix
- Quality assessment
- Usage recommendations

### templates/platform-ready.md
**Purpose:** Vianeo platform entry format
**Use for:** Direct system entry, constraint compliance

**Features:**
- Condensed format
- Character count verification
- Copy-paste ready structure
- Validation badges

---

## Usage Workflows

### Workflow 1: Generate Personas from Research Data

**Steps:**
1. Read QUICK-START.md for invocation patterns
2. Gather interview transcripts or research data
3. Invoke skill with data and framework choice
4. Review both outputs (strategic + platform-ready)
5. Check quality score against references/scoring-rubric.md
6. Iterate based on recommendations

**Files needed:** QUICK-START.md, scoring-rubric.md

### Workflow 2: Plan Validation Research

**Steps:**
1. Read SKILL.md section on validation modes
2. Review examples/innovator-persona-inferred.md for gap patterns
3. Study references/interview-templates.md
4. Determine target score using references/scoring-rubric.md
5. Plan interview count and schedule
6. Conduct interviews using question templates
7. Re-invoke skill with validated data

**Files needed:** SKILL.md, interview-templates.md, scoring-rubric.md

### Workflow 3: Improve Existing Personas

**Steps:**
1. Compare personas to examples/partner-persona-validated.md
2. Use references/scoring-rubric.md to identify current score
3. Check improvement pathways in rubric
4. Use references/interview-templates.md for targeted validation
5. Collect additional data addressing specific gaps
6. Re-invoke skill with enhanced data

**Files needed:** scoring-rubric.md, interview-templates.md, partner-persona-validated.md

### Workflow 4: Choose Alternative Framework

**Steps:**
1. Read references/frameworks-comparison.md
2. Identify best-fit framework for use case
3. Review framework structure in SKILL.md
4. Invoke skill with chosen framework
5. Adjust based on output format needs

**Files needed:** frameworks-comparison.md, SKILL.md

---

## Quick Reference

### Common Invocations

| Use Case | Invocation |
|----------|------------|
| Vianeo submission | `"Build Vianeo partner personas with strategic and platform-ready versions"` |
| Product research | `"Create customer personas using Jobs-to-be-Done framework"` |
| Research planning | `"Generate hypothesis personas to guide interview design"` |
| Team alignment | `"Build empathy maps from this user research"` |
| Score improvement | `"Strengthen evidence for Persona 2's pain points"` |

### Supported Frameworks

| Framework | Best For |
|-----------|----------|
| Vianeo | Technology validation, platform submissions |
| Jobs-to-be-Done | Product development, feature prioritization |
| Empathy Mapping | Team alignment, design workshops |
| Hybrid | Custom needs, multiple perspectives |

### Quality Scoring

| Score | Interviews | Badge |
|-------|------------|-------|
| 5 | 10+ | Exceptional |
| 4 | 5-10 | Strong |
| 3 | 3-5 | Adequate |
| 2 | 1-2 | Needs Validation |
| 1 | 0 | Hypothesis Only |

### Persona Types

| Type | Description |
|------|-------------|
| Partner | Organizations you collaborate with |
| Innovator | Technology creators you're validating |
| Stakeholder | Decision-makers and funders |
| Beneficiary | End users and impact recipients |
| Customer | Buyers in commercial contexts |

---

## Skill Workflow

```
┌─────────────────┐
│  Data Input     │  Interviews, surveys, documents
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Data Assessment │  Inventory sources, assess quality
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Segment ID      │  Identify 3-5 distinct personas
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Framework       │  Apply Vianeo/JTBD/Empathy structure
│ Application     │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Quality         │  Validate evidence, distinctiveness
│ Validation      │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Gap Analysis    │  Score, identify gaps, recommend research
└────────┬────────┘
         │
         v
┌─────────────────────────────────┐
│        Dual Output              │
├─────────────────┬───────────────┤
│ Strategic       │ Platform-Ready│
│ Version         │ Version       │
└─────────────────┴───────────────┘
```

---

## Version Information

**Current Version:** 1.0.0
**Status:** Production
**Last Updated:** 2025-11-19

**Key Features:**
- Multi-framework support (Vianeo, JTBD, empathy mapping)
- Five persona types (partner, innovator, stakeholder, beneficiary, customer)
- Evidence-based validation tracking
- Quality scoring with improvement pathways
- Dual outputs (strategic + platform-ready)

---

## Getting Started by Role

### For Quick Users
1. Read QUICK-START.md
2. Gather your data
3. Use common invocation patterns
4. Review outputs and iterate

### For Understanding the Skill
1. Read README.md for overview
2. Read SKILL.md for full specification
3. Review examples for quality benchmarks
4. Check references for deep-dives

### For Customization
1. Study references/frameworks-comparison.md
2. Review templates for output formats
3. Use hybrid framework options
4. Adapt validation questions per use case

---

## Related Skills

- **Skill Orchestrator** - Complex multi-skill workflows
- **360 Client Portfolio Builder** - Portfolio pages informed by personas
- **Open Deep Research Team** - Deep-dive persona research
- **AI Ethics Advisor** - Diverse perspective representation
- **Sales Automator** - Customer personas inform outreach

---

## Maintenance

**To update this skill:**
1. Modify relevant files
2. Update version numbers
3. Update this INDEX.md
4. Test with actual data
5. Document changes in version history

---

**For questions or issues:** Refer to SKILL.md troubleshooting or contact skill maintainers.
