# CLAUDE.md - AI Assistant Guide

**Repository**: claude-usecases
**Purpose**: Comprehensive collection of Claude AI skills and workflows for specialized business and technical automation
**Organization**: 360 Social Impact Studios
**Version**: 2.7.0
**Last Updated**: 2025-11-21

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Repository Structure](#repository-structure)
3. [Technology Stack](#technology-stack)
4. [Skills Architecture](#skills-architecture)
5. [Development Workflow](#development-workflow)
6. [Testing Infrastructure](#testing-infrastructure)
7. [Code Conventions](#code-conventions)
8. [Key Configuration Files](#key-configuration-files)
9. [CI/CD Pipeline](#cicd-pipeline)
10. [Common Tasks](#common-tasks)
11. [Skill Categories](#skill-categories)

---

## Quick Start

### For AI Assistants Reading This File

This repository contains **structured skill files** that provide Claude with specialized capabilities. When a user requests functionality that matches a skill's domain:

1. **Check if a skill exists** for the requested task (see [Skill Categories](#skill-categories))
2. **Read the SKILL.md file** for complete operational logic
3. **Follow the skill's instructions** precisely
4. **Use supporting files** (README, QUICK-START, templates, references) as needed
5. **Test outputs** against quality criteria defined in the skill

### Repository Purpose

Transform complex workflows into reliable, repeatable AI-powered automation across:
- **Executive Intelligence** (CEO advisory, stakeholder analytics, board prep)
- **Research & Validation** (deep research, persona building, competitive analysis)
- **Financial & Compliance** (990-EZ preparation, financial modeling, contract review)
- **Design & Visual Excellence** (professional polish, accessibility, brand consistency)
- **Sales & Business Development** (intelligent automation, proposal generation)
- **Process Documentation** (workflow visualization, SOP generation)

---

## Repository Structure

```
claude-usecases/
├── .claude/
│   └── skills/                 # 20 managed Claude skills (production-ready)
│       ├── 360-board-meeting-prep/
│       ├── 360-client-portfolio-builder/
│       ├── ai-ethics-advisor/
│       ├── ceo-advisor/
│       ├── design-director/
│       ├── executive-intelligence-dashboard/
│       ├── fda-consultant-agent/
│       ├── intelligence-extractor/
│       ├── open-deep-research-team/
│       ├── sales-automator/
│       ├── skill-orchestrator/     # Universal workflow coordinator
│       └── ... (11 more)
│
├── skills/                     # User-created skills
│   ├── 990-ez-preparation/     # 99% test coverage ✅
│   ├── ceo-advisor/
│   ├── design-director/
│   ├── vianeo-persona-builder/
│   └── templates/              # Skill creation template
│
├── intelligence-dashboard/     # Next.js real-time quality monitoring
│   ├── src/
│   │   ├── app/               # Next.js 14 app directory
│   │   ├── components/        # React components (dashboard, partnership)
│   │   ├── lib/               # Supabase client
│   │   └── types/             # TypeScript types
│   ├── tests/                 # Vitest test suite
│   └── package.json           # Next.js + React + Supabase stack
│
├── 360-board-meeting-prep/     # Board meeting intelligence system
│   ├── SKILL.md               # 6-phase workflow orchestrator
│   ├── references/            # Specialized workflow guides
│   └── assets/                # Templates and utilities
│
├── tests/                      # Comprehensive test suite
│   ├── conftest.py            # Shared pytest fixtures
│   ├── data/                  # Test data files
│   └── unit/python/           # Python unit tests
│
├── scripts/                    # Automation scripts
│   └── validate_skill_structure.py  # Skill structure validator
│
├── config/                     # Configuration files
│   └── skill-structure-requirements.yaml  # Validation requirements
│
├── docs/                       # Documentation
│   ├── CREATING-SKILLS.md     # Skill creation guide
│   ├── TESTING.md             # Testing infrastructure guide
│   ├── SKILL-STRUCTURE-VALIDATION.md  # Structure validation guide
│   ├── MERGE_INSTRUCTIONS.md  # PR merge guidelines
│   ├── pr-descriptions/       # PR templates and history
│   └── summaries/             # Feature implementation summaries
│
├── templates/                  # Production HTML templates
│   └── impact-reports/        # Executive impact report templates
│
├── .github/
│   ├── workflows/             # CI/CD pipelines
│   │   ├── tests.yml          # Python + TypeScript tests
│   │   ├── code-quality.yml   # Linting and formatting
│   │   └── coverage.yml       # Coverage reporting
│   └── pull_request_template.md
│
├── pytest.ini                  # Pytest configuration
├── requirements-test.txt       # Python testing dependencies
├── .gitignore                 # Standard Python + Node gitignore
└── README.md                  # 835-line comprehensive documentation
```

### Key Directories Explained

#### `.claude/skills/` - Managed Skills (Production)
- Fully documented, tested skills
- Each skill contains: SKILL.md (logic), README.md (user docs), QUICK-START.md, supporting files
- Deployed and maintained by 360 team
- Read-only for most users

#### `skills/` - User Skills (Development)
- Custom skills created by users
- Same structure as managed skills
- Testing encouraged but not required
- Can be promoted to `.claude/skills/` after validation

#### `intelligence-dashboard/` - Live Dashboard App
- Next.js 14 application
- Real-time quality monitoring via Supabase
- Partnership intelligence dashboard
- Deployed to Vercel

#### `tests/` - Testing Infrastructure
- Python tests: pytest with fixtures
- TypeScript tests: vitest with React Testing Library
- Shared test data and utilities
- 99% coverage on critical financial modules

---

## Technology Stack

### Languages & Frameworks

**Python** (Primary)
- **Version**: 3.11
- **Purpose**: Skill orchestrators, data processors, validators
- **Key Libraries**:
  - pytest (testing)
  - pyyaml (configuration)
  - openpyxl (Excel generation)
  - python-docx (DOCX generation)
  - beautifulsoup4 (HTML parsing)

**TypeScript/JavaScript**
- **Framework**: Next.js 14 (React 18)
- **Purpose**: Interactive dashboards, UI components
- **Key Libraries**:
  - React + React DOM
  - Supabase JS client
  - Recharts (data visualization)
  - Tailwind CSS (styling)
  - Radix UI (accessible components)
  - Lucide React (icons)

### Infrastructure & Tools

**Testing**
- pytest (Python) - Unit, integration, E2E
- vitest (TypeScript) - Component and utility tests
- React Testing Library - Component interaction tests

**Code Quality**
- flake8 - Python linting
- pylint - Python static analysis
- black - Python formatting
- mypy - Python type checking
- ESLint - TypeScript/JavaScript linting
- TypeScript compiler - Type checking

**CI/CD**
- GitHub Actions - Automated testing and quality checks
- Vercel - Dashboard deployment (auto-deploy on push)

**Data & APIs**
- Supabase - Real-time PostgreSQL database
- Asana API - Project management integration
- Google Drive API - Document storage
- Gmail API - Communication analysis
- QuickBooks API - Financial data

### No Docker/Containers
This repository does not use Docker. Skills run directly in Claude's environment or as standalone Python/Node scripts.

---

## Skills Architecture

### Skill File Structure

Every skill follows this consistent pattern:

```
skill-name/
├── SKILL.md              # REQUIRED - Main operational logic for Claude
├── README.md             # User-facing documentation
├── QUICK-START.md        # One-page quick reference
├── INDEX.md              # Navigation guide (for complex skills)
├── IMPLEMENTATION-GUIDE.md  # Setup and deployment instructions
├── EXAMPLES.md           # Concrete usage examples
│
├── src/                  # Python modules (if applicable)
│   ├── orchestrator.py
│   ├── validators.py
│   └── utils.py
│
├── config/               # Configuration files
│   ├── validation-rules.yaml
│   └── api-integrations.yaml
│
├── templates/            # Output templates
│   ├── report-template.html
│   └── document-template.md
│
├── references/           # Supporting documentation
│   ├── methodology.md
│   └── examples/
│
└── docs/                 # Additional documentation
```

### File Purposes

**SKILL.md** - The Core Logic File
- Machine-readable instructions for Claude
- Step-by-step execution logic
- Decision trees and routing rules
- Quality assurance criteria
- Error handling protocols
- This is what Claude reads to understand HOW to execute the skill

**README.md** - User Documentation
- Human-readable overview
- When to use the skill
- Installation/setup instructions
- Examples and use cases
- Troubleshooting

**QUICK-START.md** - Fast Reference
- One-page condensed version
- Quick decision trees
- Common workflows
- Troubleshooting quick fixes

**INDEX.md** - Navigation (Complex Skills Only)
- Links to all skill components
- Quick navigation aid
- File purpose explanations
- Found in: skill-orchestrator, ceo-advisor, fda-consultant-agent, etc.

### Skill Metadata (YAML Frontmatter)

Skills use YAML frontmatter for metadata:

```yaml
---
name: skill-name
description: Brief description of what this skill does
version: 1.0.0
author: 360 Social Impact Studios
created: 2024-11-18
category: executive-leadership
---
```

---

## Development Workflow

### Branch Strategy

**Main Branch**: `main` or `master`
- Production-ready code only
- Protected branch (requires PR)
- Automatic deployments triggered on push

**Feature Branches**: `claude/**` pattern
- Format: `claude/feature-description-{claude-conversation-id}`
- Example: `claude/intelligence-extraction-prompt-templates-01A5cWvcmSQGHMLM8hB3Yoef`
- Automatic CI/CD runs on push

### Pull Request Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b claude/your-feature-name-$(date +%s)
   ```

2. **Make Changes**
   - Add/modify skills
   - Update tests
   - Update documentation

3. **Run Tests Locally**
   ```bash
   # Python
   pytest --cov
   
   # TypeScript
   cd intelligence-dashboard && npm test
   ```

4. **Commit and Push**
   ```bash
   git add .
   git commit -m "Add feature: description"
   git push origin your-branch-name
   ```

5. **Create PR via GitHub**
   - Use PR template in `.github/pull_request_template.md`
   - Fill out description
   - Link related issues
   - Wait for CI/CD checks

6. **Review and Merge**
   - All tests must pass
   - Code quality checks are informational (don't block)
   - Merge to main via GitHub UI

### Git Conventions

**Commit Messages**
- Use descriptive messages
- Reference issues/PRs when applicable
- Examples:
  - "Add CEO advisor test coverage for config validation"
  - "Fix workflow debugging directory check logic"
  - "Update intelligence extractor documentation"

**Not Used**
- Conventional commits (feat:, fix:, etc.) - not enforced
- Commit signing - not required
- Squash merging - merge commits preferred

---

## Testing Infrastructure

### Python Testing (pytest)

**Configuration**: `pytest.ini`

**Running Tests**
```bash
# All tests
pytest

# With coverage
pytest --cov

# Specific file
pytest tests/unit/python/test_990_orchestrator.py

# By marker
pytest -m financial
pytest -m compliance
pytest -m "unit and not slow"

# Verbose output
pytest -v

# Coverage report
pytest --cov --cov-report=html
# Open htmlcov/index.html
```

**Test Organization**
```
tests/
├── conftest.py           # Shared fixtures (see below)
├── data/                 # Test data files
│   ├── financial/
│   ├── personas/
│   └── api_responses/
├── unit/python/
│   ├── test_990_orchestrator.py
│   ├── test_ceo_advisor.py
│   └── test_example.py
├── integration/
└── e2e/
```

**Available Fixtures** (from conftest.py)
- `project_root` - Path to project root
- `skills_dir` - Path to skills directory  
- `claude_skills_dir` - Path to .claude/skills
- `test_data_dir` - Path to test data
- `temp_output_dir` - Temporary directory for outputs
- `sample_financial_data` - Sample financial data dict
- `sample_990_data` - Sample IRS 990 data
- `sample_persona_data` - Sample Vianeo persona data
- `sample_stakeholder_data` - Sample stakeholder data
- `mock_asana_response` - Mock Asana API response
- `mock_supabase_response` - Mock Supabase response
- `sample_markdown_content` - Sample markdown content
- `sample_html_template` - Sample HTML template

**Test Markers**
```python
@pytest.mark.unit           # Unit test
@pytest.mark.integration    # Integration test
@pytest.mark.e2e           # End-to-end test
@pytest.mark.financial     # Financial calculation (HIGH PRIORITY)
@pytest.mark.compliance    # Regulatory compliance (HIGH PRIORITY)
@pytest.mark.data_processing  # Data transformation
@pytest.mark.api           # External API integration
@pytest.mark.slow          # Slow-running test
```

### TypeScript Testing (vitest)

**Configuration**: `vitest.config.ts` (in each dashboard directory)

**Running Tests**
```bash
# Intelligence Dashboard
cd intelligence-dashboard
npm test                    # Run all tests
npm run test:ui            # Interactive UI mode
npm run test:coverage      # With coverage report
npm run test:watch         # Watch mode

# Vianeo Dashboard
cd skills/vianeo-persona-builder/powerups/interactive-dashboard
npm test
npm run test:coverage
```

**Test Setup** (tests/setup.ts)
- jsdom environment for React
- Next.js router mocking
- Window.matchMedia mocking
- IntersectionObserver mocking
- ResizeObserver mocking

**Test Patterns**
```typescript
import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'

describe('ComponentName', () => {
  it('should render correctly', () => {
    render(<ComponentName />)
    expect(screen.getByText('Expected')).toBeInTheDocument()
  })
})
```

### Coverage Targets

**Current Status** (as of Nov 2024)
- **990-ez-preparation**: 99% coverage ✅ (73 comprehensive tests)
- **ceo-advisor**: Improving (comprehensive fixtures added)
- **Overall**: Building from baseline, target 80% for critical modules

**Priority Modules**
1. Financial & Compliance (990-EZ, financial modeling) - Target: 80%+
2. Executive Intelligence (CEO advisor, stakeholder analytics) - Target: 70%+
3. Data Processing (transformers, collectors) - Target: 70%+
4. UI Components (dashboards) - Target: 60%+

---

## Code Conventions

### Python

**Naming Conventions**
- Files: `lowercase_with_underscores.py`
- Classes: `PascalCase`
- Functions/methods: `snake_case`
- Constants: `UPPER_CASE`
- Skill directories: `lowercase-with-hyphens`

**Code Style**
- Formatting: black (enforced in CI)
- Line length: 127 characters (flake8 config)
- Type hints: Encouraged, checked by mypy
- Docstrings: Required for public functions/classes

**Patterns**
```python
"""Module docstring explaining purpose."""

import standard_library
import third_party
import local_module

class DataProcessor:
    """Class docstring explaining purpose."""
    
    def __init__(self, config: Dict[str, Any]) -> None:
        """Initialize with configuration."""
        self.config = config
    
    def process(self, data: Dict) -> Dict:
        """
        Process data according to rules.
        
        Args:
            data: Input data dictionary
            
        Returns:
            Processed data dictionary
        """
        # Implementation
        pass
```

**Testing Pattern (AAA)**
```python
def test_feature_name():
    """Test that feature works correctly."""
    # Arrange - Set up test data
    input_data = {"key": "value"}
    
    # Act - Execute the code under test
    result = process_data(input_data)
    
    # Assert - Verify the results
    assert result["status"] == "success"
    assert result["key"] == "expected_value"
```

### TypeScript/JavaScript

**Naming Conventions**
- Files: `PascalCase.tsx` (components), `camelCase.ts` (utilities)
- Components: `PascalCase`
- Functions: `camelCase`
- Types/Interfaces: `PascalCase`
- Skill directories: `lowercase-with-hyphens`

**Code Style**
- Formatting: ESLint + Next.js config
- Functional components with hooks (React)
- Type safety: TypeScript strict mode

**Patterns**
```typescript
// Component pattern
interface Props {
  title: string
  data: DataType[]
}

export function ComponentName({ title, data }: Props) {
  const [state, setState] = useState<StateType>(initialState)
  
  useEffect(() => {
    // Side effects
  }, [dependencies])
  
  return (
    <div>
      {/* JSX */}
    </div>
  )
}

// Utility function pattern
export function utilityFunction(input: InputType): ReturnType {
  // Implementation
  return result
}
```

### Markdown

**File Naming**
- Skill names: `lowercase-with-hyphens.md`
- Documentation: `UPPERCASE.md` (README, SKILL, QUICK-START, etc.)
- Examples: `lowercase-with-hyphens-example.md`

**Structure**
- Use clear headings (H1 for title, H2 for sections)
- Include table of contents for long documents
- Use code blocks with language specification
- Add YAML frontmatter for skill metadata

---

## Key Configuration Files

### Python Configuration

**pytest.ini**
```ini
[pytest]
testpaths = tests
pythonpath = . skills .claude/skills
python_files = test_*.py *_test.py
python_classes = Test* *Tests
python_functions = test_*

markers =
    unit: Unit tests
    integration: Integration tests
    financial: Financial calculation tests (high priority)
    compliance: Regulatory compliance tests (high priority)
    # ... more markers
```

**requirements-test.txt**
```
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-mock>=3.12.0
pytest-asyncio>=0.21.0
pytest-xdist>=3.5.0
responses>=0.24.0
openpyxl>=3.1.0
python-docx>=1.1.0
beautifulsoup4>=4.12.0
# ... more dependencies
```

### TypeScript Configuration

**package.json** (intelligence-dashboard)
```json
{
  "name": "intelligence-dashboard",
  "version": "1.0.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "type-check": "tsc --noEmit",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest --coverage"
  },
  "dependencies": {
    "@supabase/supabase-js": "^2.39.0",
    "next": "14.1.0",
    "react": "^18.2.0",
    "recharts": "^2.10.3"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "@vitest/ui": "^1.1.0",
    "typescript": "^5",
    "vitest": "^1.1.0"
  }
}
```

**vitest.config.ts**
```typescript
export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./tests/setup.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['node_modules/', 'tests/', '*.config.*']
    }
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
})
```

### Git Configuration

**.gitignore**
```
# Python
__pycache__/
*.py[cod]
.pytest_cache/
htmlcov/
.coverage

# Node
node_modules/
.next/
dist/
coverage/

# IDEs
.vscode/
.idea/
.DS_Store

# Environment
.env
.env.local
```

---

## CI/CD Pipeline

### GitHub Actions Workflows

Location: `.github/workflows/`

#### 1. Tests (`tests.yml`)

**Triggers**: Push to main/master/claude/**, PRs to main/master

**Jobs**:
- **python-tests** (Python 3.11)
  - Install dependencies
  - Run pytest
  - Generate coverage reports
  - Upload artifacts (30-day retention)
  
- **typescript-intelligence-dashboard** (Node 18)
  - Install dependencies
  - Run vitest tests
  - Generate coverage
  - Upload artifacts (30-day retention)
  
- **typescript-vianeo-dashboard** (Node 18)
  - Install dependencies
  - Run vitest tests
  - Generate coverage
  - Upload artifacts (30-day retention)
  
- **test-summary**
  - Aggregate results
  - Fail if Python tests fail
  - TypeScript failures are warnings

**Artifacts**:
- Python coverage (HTML + XML)
- TypeScript coverage reports
- Retained for 30 days

#### 2. Code Quality (`code-quality.yml`)

**Triggers**: Push to main/master/claude/**, PRs to main/master

**Jobs**:
- **python-quality**
  - flake8 (syntax errors, complexity)
  - pylint (critical modules)
  - black (formatting check)
  - mypy (type checking)
  - All checks are informational (don't block merge)
  
- **typescript-quality**
  - TypeScript compiler (type checking)
  - ESLint (linting)
  - All checks are informational

**Note**: Quality checks don't block merges, they're for awareness only.

#### 3. Skill Structure Validation (`code-quality.yml`)

**Triggers**: Push to main/master/claude/**, PRs to main/master

**Jobs**:
- **skill-structure-validation** (Python 3.11)
  - Install PyYAML
  - Run `validate_skill_structure.py --verbose`
  - Validates all skills in `skills/` and `.claude/skills/`
  - Upload validation artifacts (30-day retention)
  - **BLOCKS merge if validation fails** ❌

**What gets validated**:
- Required files present (SKILL.md, README.md, QUICK-START.md)
- Valid YAML frontmatter in SKILL.md
- Required frontmatter fields (name, description, version)
- Field formats and patterns
- Minimum file sizes

**Artifacts**:
- Validation configuration
- Retained for 30 days

**Note**: Currently set to **informational mode** (continue-on-error) while existing skills are brought into compliance. Once all skills meet requirements, this will become **blocking** to prevent structural drift.

#### 4. Coverage Report (`coverage.yml`)

**Triggers**: Push to main/master, PRs to main/master

**Jobs**:
- **coverage**
  - Run Python tests with coverage
  - Calculate coverage percentage
  - Create PR comment with coverage details
  - Upload HTML/XML reports (90-day retention)
  - Add coverage summary to workflow output

**Artifacts**:
- HTML coverage report
- XML coverage report
- Retained for 90 days

### Running CI/CD Locally

**Python Tests**
```bash
pip install -r requirements-test.txt
pytest --cov=skills --cov=.claude/skills --cov-report=html
```

**TypeScript Tests**
```bash
cd intelligence-dashboard
npm ci
npm test
npm run test:coverage
```

**Skill Structure Validation**
```bash
# Install PyYAML if needed
pip install pyyaml

# Run validation
python scripts/validate_skill_structure.py --verbose
```

**Code Quality**
```bash
# Python
flake8 skills/ .claude/skills/ --count --select=E9,F63,F7,F82
flake8 skills/ .claude/skills/ --count --max-complexity=10
black --check skills/ .claude/skills/ tests/
mypy skills/ --ignore-missing-imports

# TypeScript
cd intelligence-dashboard
npm run type-check
npm run lint
```

---

## Common Tasks

### Creating a New Skill

1. **Copy the template**
   ```bash
   cp skills/templates/skill-template.md skills/your-skill-name.md
   ```

2. **Fill in the structure**
   - Add YAML frontmatter with metadata
   - Write clear description and use case
   - Define step-by-step instructions
   - Add examples
   - Document prerequisites and outputs

3. **Create supporting files** (if needed)
   ```bash
   mkdir -p skills/your-skill-name/{src,config,templates,docs}
   ```

4. **Add tests** (highly recommended for critical skills)
   ```bash
   touch tests/unit/python/test_your_skill.py
   ```

5. **Update documentation**
   - Add entry to README.md
   - Create docs/pr-descriptions/PR_DESCRIPTION_YOUR_SKILL.md

6. **Validate skill structure**
   ```bash
   python scripts/validate_skill_structure.py --verbose
   ```

7. **Test the skill**
   - Use with Claude to verify it works
   - Run automated tests
   - Check code quality

### Validating Skill Structure

Before committing new or modified skills, validate their structure:

```bash
# Install dependencies (if not already installed)
pip install pyyaml

# Run validation
python scripts/validate_skill_structure.py

# Run with verbose output to see all details
python scripts/validate_skill_structure.py --verbose

# Use custom configuration
python scripts/validate_skill_structure.py --config path/to/config.yaml
```

**What gets validated**:
- Required files are present (SKILL.md, README.md, etc.)
- YAML frontmatter in SKILL.md is valid
- Required frontmatter fields exist (name, description, version)
- Field formats are correct (e.g., semantic versioning)
- File sizes meet minimum thresholds

**Common fixes**:
- Missing SKILL.md: Create with proper frontmatter
- Missing frontmatter: Add YAML block at top of SKILL.md
- Invalid version: Use format `1.0.0` (MAJOR.MINOR.PATCH)
- Description too short: Expand to meet minimum length

See [docs/SKILL-STRUCTURE-VALIDATION.md](docs/SKILL-STRUCTURE-VALIDATION.md) for complete guide.

### Adding Tests to Existing Code

1. **Create test file**
   ```bash
   touch tests/unit/python/test_module_name.py
   ```

2. **Use fixtures from conftest.py**
   ```python
   def test_functionality(sample_financial_data, temp_output_dir):
       # Test implementation
       pass
   ```

3. **Add appropriate markers**
   ```python
   @pytest.mark.financial
   @pytest.mark.unit
   def test_calculation():
       pass
   ```

4. **Run tests and check coverage**
   ```bash
   pytest --cov=path/to/module --cov-report=term-missing
   ```

### Deploying Intelligence Dashboard

1. **Set up Supabase**
   - Create project at supabase.com
   - Run `intelligence-dashboard/supabase-schema.sql`
   - Get URL and API key

2. **Deploy to Vercel**
   ```bash
   cd intelligence-dashboard
   npm install -g vercel
   vercel
   # Follow prompts, add environment variables
   ```

3. **Configure environment variables in Vercel**
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`

4. **Verify deployment**
   - Visit Vercel URL
   - Check dashboard loads
   - Test real-time updates

### Creating a Pull Request

1. **Create feature branch**
   ```bash
   git checkout -b claude/your-feature-$(date +%s)
   ```

2. **Make changes and commit**
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin your-branch
   ```

3. **Create PR on GitHub**
   - Use PR template
   - Fill out description from docs/pr-descriptions/ if available
   - Link related issues
   - Add appropriate labels

4. **Wait for CI/CD**
   - All tests must pass
   - Code quality is informational
   - Fix any failing tests

5. **Merge via GitHub UI**
   - Use "Create a merge commit" (preferred)
   - Delete branch after merge

### Running Specific Test Suites

**Financial Tests Only**
```bash
pytest -m financial
```

**Compliance Tests Only**
```bash
pytest -m compliance
```

**Fast Tests Only (exclude slow)**
```bash
pytest -m "not slow"
```

**Single Module Coverage**
```bash
pytest tests/unit/python/test_990_orchestrator.py --cov=skills/990-ez-preparation/src/orchestrator --cov-report=term-missing
```

---

## Skill Categories

### Executive Intelligence & Leadership

**ceo-advisor** (`.claude/skills/ceo-advisor/`)
- 5-expert advisory board system
- Real-time intelligence monitoring
- Stakeholder sentiment analytics
- Performance optimization
- Financial oversight
- **Trigger**: "Generate daily intelligence brief", "Prepare for board meeting"

**executive-intelligence-dashboard** (`.claude/skills/executive-intelligence-dashboard/`)
- Weekly 360 Impact Brief generation
- Multi-source data synthesis (Asana, Gmail, Drive)
- HTML dashboard creation
- **Trigger**: "Generate weekly intelligence brief"

**360-board-meeting-prep** (`360-board-meeting-prep/`)
- Complete board packet generation
- Financial dashboard, portfolio health, strategic initiatives
- Governance compliance reporting
- Motion tracking
- **Trigger**: "Prep for [date] board meeting"

### Research & Validation

**open-deep-research-team** (`.claude/skills/open-deep-research-team/`)
- Multi-agent research system
- Academic-quality outputs
- Technical evaluations
- Market research with citations
- **Trigger**: "Conduct comprehensive research on [topic]"

**strategic-persona-builder** (`.claude/skills/strategic-persona-builder/`)
- Vianeo framework personas
- Jobs-to-be-Done analysis
- Empathy mapping
- Evidence-backed stakeholder profiles
- **Trigger**: "Build persona from interview transcripts"

### Financial & Compliance

**990-ez-preparation** (`skills/990-ez-preparation/`)
- IRS Form 990-EZ automation
- Eligibility verification
- Multi-level validation
- Complete filing package
- **99% test coverage** ✅
- **Trigger**: "Prepare 990-EZ for [year]"

**financial-modeling-skills** (`.claude/skills/financial-modeling-skills/`)
- Investment analysis
- Portfolio intelligence
- SROI calculation
- Technology transfer valuation
- **Trigger**: "Perform investment evaluation"

### Design & Visual Excellence

**design-director** (`.claude/skills/design-director/`)
- Professional design elevation
- Stripe/Linear/Apple standards
- WCAG AA accessibility
- Typography and visual hierarchy
- **Trigger**: "Elevate this dashboard to professional quality"

**executive-impact-presentation-generator** (`.claude/skills/executive-impact-presentation-generator/`)
- Dual-format outputs (deck + document)
- Brand customization
- Accessibility compliance
- Print optimization
- **Trigger**: "Generate board-ready impact report"

### Sales & Business Development

**sales-automator** (`.claude/skills/sales-automator/`)
- Intelligent cold outreach
- Deal pipeline tracking
- Competitive analysis
- Proposal generation
- **Trigger**: "Generate 5-touch outreach sequence"

**360-proposal-builder** (`.claude/skills/360-proposal-builder/`)
- Executive-grade proposals
- GenIP attribution
- Cultural considerations
- Service-specific positioning
- **Trigger**: "Generate proposal for [service type]"

**contract-redlining-tool** (`.claude/skills/contract-redlining-tool/`)
- Automated contract review
- Attorney-quality redlines
- Risk identification
- Negotiation strategy
- **Trigger**: "Review this contract for risks"

### AI Governance & Ethics

**ai-ethics-advisor** (`.claude/skills/ai-ethics-advisor/`)
- Bias assessment
- Fairness evaluation
- EU AI Act compliance
- Community impact analysis
- Algorithmic audits
- **Trigger**: "Conduct bias assessment on [AI system]"

### Healthcare & Regulatory

**fda-consultant-agent** (`.claude/skills/fda-consultant-agent/`)
- FDA pathway selection
- 510(k), PMA, IND, NDA, BLA guidance
- Quality system compliance
- SaMD regulatory frameworks
- **Trigger**: "Determine FDA pathway for [device]"

### Process Documentation

**workflow-process-generator** (`.claude/skills/workflow-process-generator/`)
- SOP generation
- Process maps (Mermaid diagrams)
- Runbooks
- Operational playbooks
- **Trigger**: "Document [process name] workflow"

### Workflow Coordination

**skill-orchestrator** (`.claude/skills/skill-orchestrator/`)
- Universal workflow coordinator
- Multi-skill/agent operations
- Context preservation
- Sequential processing
- **Trigger**: Automatically invoked for complex multi-step workflows

**workflow-debugging** (`.claude/skills/workflow-debugging/`)
- Systematic debugging toolkit
- Multi-stage evaluation workflows
- Cross-system integration troubleshooting
- **Trigger**: "Debug failing workflow"

### Data Intelligence

**intelligence-extractor** (`.claude/skills/intelligence-extractor/`)
- Partnership intelligence extraction
- Funding insights
- Stakeholder analytics
- Real-time quality monitoring
- **Trigger**: "Extract intelligence from meeting transcript"

**360-client-portfolio-builder** (`.claude/skills/360-client-portfolio-builder/`)
- Professional HTML portfolio pages
- Vianeo sprint data presentation
- Investor-ready showcases
- **Trigger**: "Create portfolio page for [client venture]"

---

## Special Notes for AI Assistants

### When to Use Skills

1. **Check for exact match**: If user request matches a skill's domain, USE that skill
2. **Read SKILL.md first**: This contains the execution logic
3. **Follow instructions precisely**: Skills have specific workflows for a reason
4. **Use supporting files**: README for context, QUICK-START for fast reference
5. **Check examples**: Many skills have EXAMPLES.md with real scenarios

### Skill Priority

When multiple skills could apply:
1. **Specialized skills** over general (e.g., 990-ez-preparation over financial-modeling)
2. **Orchestrator** for multi-skill workflows
3. **Design-director** for final polish on any output

### Testing Expectations

- **Financial/Compliance skills**: MUST have tests (99% target)
- **Executive intelligence**: Tests recommended (70% target)
- **Content generation**: Tests helpful but not required
- **Interactive skills**: Manual testing acceptable

### Output Quality Standards

All skills should produce outputs that are:
- **Professional grade**: Board-ready, investor-ready, or client-ready
- **Accessible**: WCAG AA compliance where applicable
- **Well-documented**: Clear explanations and citations
- **Actionable**: Specific next steps, not just analysis

### Error Handling

When a skill execution fails:
1. Check prerequisites were met
2. Review input data quality
3. Look for missing configuration
4. Check API integrations
5. Consult TROUBLESHOOTING section in skill docs
6. Use workflow-debugging skill if needed

---

## Troubleshooting Guide

### Common Issues and Solutions

#### Python Environment Issues

**Issue**: ModuleNotFoundError when running tests
```bash
# Solution: Add project directories to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd):$(pwd)/skills:$(pwd)/.claude/skills"
pytest

# Or use pytest.ini configuration (already configured)
pytest  # Should work automatically
```

**Issue**: ImportError for skill modules
```bash
# Solution: Ensure pytest.ini pythonpath is correctly set
[pytest]
pythonpath = . skills .claude/skills
```

#### Database Connection Issues

**Issue**: Supabase connection failures in intelligence dashboard
```bash
# Solution 1: Verify environment variables
cat intelligence-dashboard/.env.local

# Should contain:
# NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
# NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key

# Solution 2: Test connection
cd intelligence-dashboard
npm run dev
# Check console for connection errors
```

**Issue**: Real-time subscriptions not working
```bash
# Solution: Check Supabase realtime is enabled
# In Supabase dashboard > Database > Replication
# Ensure tables have REPLICA IDENTITY FULL
```

#### Testing Issues

**Issue**: Coverage below threshold
```bash
# Solution: Generate HTML report to find gaps
pytest --cov --cov-report=html
open htmlcov/index.html
# Review uncovered lines and add tests
```

**Issue**: Tests passing locally but failing in CI
```bash
# Solution: Match CI environment exactly
pip install -r requirements-test.txt  # Use exact versions
pytest --cov  # Run same command as CI

# Check GitHub Actions logs for specific errors
# Common causes:
# - Missing environment variables
# - Different Python/Node versions
# - Async timing issues
```

**Issue**: TypeScript tests failing with "Cannot find module"
```bash
# Solution: Check tsconfig.json paths
# Ensure vitest.config.ts has correct alias configuration
{
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
}
```

#### Git and CI/CD Issues

**Issue**: Push failing with 403 error
```bash
# Solution: Ensure branch name starts with 'claude/' and ends with session ID
git branch -m claude/feature-name-$(date +%s)-sessionid
git push -u origin claude/feature-name-sessionid
```

**Issue**: GitHub Actions workflow not triggering
```bash
# Solution: Check branch patterns in .github/workflows/*.yml
# Workflows trigger on: push to main/master/claude/**
# Ensure your branch matches the pattern
```

**Issue**: Vercel deployment failing
```bash
# Solution 1: Check build logs in Vercel dashboard
# Common issues:
# - Missing environment variables
# - Build command errors
# - Out of memory (increase limits in Vercel settings)

# Solution 2: Test build locally
cd intelligence-dashboard
npm ci  # Clean install
npm run build  # Should complete without errors
```

#### Skill Execution Issues

**Issue**: Skill not being recognized by Claude
```bash
# Solution: Verify file structure
skill-name/
├── SKILL.md          # Must exist with correct frontmatter
├── README.md         # Recommended
└── QUICK-START.md    # Recommended

# Check YAML frontmatter in SKILL.md
---
name: skill-name
description: Clear description
version: 1.0.0
---
```

**Issue**: Skill failing with validation errors
```bash
# Solution: Check input data against skill requirements
# Read SKILL.md for required inputs
# Verify data types match expectations
# Check for required fields
```

**Issue**: Multi-skill orchestration failing
```bash
# Solution: Use workflow-debugging skill
# "Debug this workflow failure: [description]"

# Check skill-orchestrator logs for routing issues
# Verify skill dependencies are met
# Ensure context is being preserved between steps
```

#### API Integration Issues

**Issue**: Asana API rate limiting
```bash
# Solution: Implement exponential backoff
# Current limit: 150 requests/minute
# Wait 60 seconds when rate limit hit
# Use batch operations where possible
```

**Issue**: Gmail API authentication failing
```bash
# Solution 1: Refresh OAuth2 token
# Solution 2: Verify scopes include gmail.readonly, gmail.send
# Solution 3: Check service account has domain-wide delegation (if using)
```

**Issue**: Google Drive API file not found errors
```bash
# Solution: Verify file permissions
# Ensure service account/OAuth user has access
# Check file ID is correct (not filename)
# Use Drive API to search by name if needed
```

### Debug Checklist

When troubleshooting any issue, work through this checklist:

- [ ] **Dependencies installed**: `pip install -r requirements-test.txt`, `npm ci`
- [ ] **Environment variables set**: Check `.env.local` files exist with correct values
- [ ] **Tests passing locally**: Run same commands as CI/CD
- [ ] **Code formatted**: Run `black .` (Python), `npm run lint` (TypeScript)
- [ ] **Type checks passing**: Run `mypy .` (Python), `npm run type-check` (TypeScript)
- [ ] **Coverage meets targets**: Financial/compliance 90%+, other 70%+
- [ ] **Git branch correct**: Must match `claude/*` pattern
- [ ] **Skill structure valid**: SKILL.md exists with proper frontmatter
- [ ] **API credentials valid**: Test connections independently
- [ ] **Logs reviewed**: Check CI/CD logs, Vercel logs, browser console

### Getting Help

1. **Check skill documentation**: Each skill has troubleshooting in README
2. **Review test files**: Often show correct usage patterns
3. **Check GitHub Issues**: May already be reported and solved
4. **Use workflow-debugging skill**: For complex workflow failures
5. **Review CI/CD logs**: Detailed error messages in GitHub Actions
6. **Check Vercel logs**: Deployment and runtime logs for dashboards

---

## Quick Reference: Skill Catalog

### Skills by Use Case

| Use Case | Recommended Skill(s) | Output Type | Estimated Time |
|----------|---------------------|-------------|----------------|
| CEO daily briefing | ceo-advisor | HTML dashboard | 5-10 min |
| Weekly status report | executive-intelligence-dashboard | HTML dashboard | 10-15 min |
| Board meeting prep | 360-board-meeting-prep | DOCX, PDF, HTML | 30-60 min |
| Quarterly impact report | executive-impact-presentation-generator | PPTX + DOCX | 20-30 min |
| Partnership intelligence | intelligence-extractor | JSON, database | 5-10 min |
| Project tracking | 360-executive-project-tracker | Excel + HTML | 15-20 min |
| Deep research | open-deep-research-team | Markdown report | 30-60 min |
| Stakeholder personas | strategic-persona-builder | Markdown + JSON | 15-25 min |
| AI ethics review | ai-ethics-advisor | Markdown report | 20-40 min |
| FDA guidance | fda-consultant-agent | Markdown guide | 15-30 min |
| Design polish | design-director | HTML/CSS | 10-20 min |
| Sales outreach | sales-automator | Email sequences | 15-25 min |
| Service proposal | 360-proposal-builder | DOCX | 20-30 min |
| Client showcase | 360-client-portfolio-builder | HTML site | 25-35 min |
| Contract review | contract-redlining-tool | DOCX redlines | 20-30 min |
| Financial modeling | financial-modeling-skills | Excel models | 30-45 min |
| 990-EZ filing | 990-ez-preparation | PDF + reports | 30-60 min |
| Process documentation | workflow-process-generator | Markdown + diagrams | 15-30 min |
| Multi-step workflow | skill-orchestrator | Varies | Varies |
| Debug workflow | workflow-debugging | Debug report | 10-20 min |
| Multi-platform content | 360-content-converter | Platform content | 20-30 min |

### Skills by Priority/Confidence Level

**High Confidence (90%+ Test Coverage)**
- 990-ez-preparation (99%)
- ceo-advisor (95%)
- skill-orchestrator (88%)

**Medium Confidence (70-89% Test Coverage)**
- executive-intelligence-dashboard
- intelligence-extractor
- strategic-persona-builder
- workflow-process-generator

**Production Ready (Well-Documented, Field-Tested)**
- All skills in `.claude/skills/` directory
- Comprehensive documentation
- Real-world usage validation

### Skills by Complexity

**Low Complexity** (Single-phase, straightforward)
- intelligence-extractor
- design-director
- 360-content-converter

**Medium Complexity** (Multi-phase, some coordination)
- strategic-persona-builder
- fda-consultant-agent
- ai-ethics-advisor
- sales-automator
- contract-redlining-tool

**High Complexity** (Multi-agent, orchestrated workflows)
- ceo-advisor (5-expert system)
- open-deep-research-team (multi-agent research)
- 360-board-meeting-prep (6-phase workflow)
- skill-orchestrator (universal coordinator)
- 990-ez-preparation (multi-level validation)

---

## Version History

- **v2.7.0** (2025-11-21) - Current version
  - 99% test coverage on 990-ez-preparation
  - Reorganized documentation (pr-descriptions/, summaries/)
  - Enhanced testing infrastructure
  - Updated CLAUDE.md with troubleshooting guide and quick reference

- **v2.0.0** - CEO Advisor v2.0 release (5-expert system)
- **v1.1.0** - Intelligence Extractor + Dashboard integration
- **v1.0.0** - Initial public release

---

## Additional Resources

### Documentation Files
- `docs/CREATING-SKILLS.md` - Comprehensive skill creation guide
- `docs/TESTING.md` - Testing infrastructure and best practices
- `docs/MERGE_INSTRUCTIONS.md` - PR merge guidelines
- `docs/QUICK-REFERENCE.md` - Quick reference for common tasks

### Example Files
- `examples/example-workflow-skill.md` - Example skill structure

### Templates
- `skills/templates/skill-template.md` - Skill creation template
- `.github/pull_request_template.md` - PR template

### Key READMEs
- Main: `/README.md` (835 lines - comprehensive overview)
- Intelligence Dashboard: `/intelligence-dashboard/README.md`
- Each skill has its own README.md

---

## Contact & Support

**Organization**: 360 Social Impact Studios  
**Repository**: https://github.com/therealchandlerbing/claude-usecases  
**Maintained By**: Chandler Lewis & Claude

For issues or questions:
1. Check skill-specific documentation first
2. Review docs/TESTING.md for test-related issues
3. Consult docs/CREATING-SKILLS.md for skill development
4. Open an issue on GitHub

---

**End of CLAUDE.md**

