# Implement Architecture Review Recommendations

You are tasked with implementing the recommendations from the comprehensive architecture review at `docs/ARCHITECTURE_REVIEW.md` (version 2.0.0).

## Context

This repository (`claude-usecases`) contains Claude AI skills and workflows for 360 Social Impact Studios. An expert architecture review identified **~6,600+ lines of duplicate code** and **~6,000+ lines of untested production code** across Python and TypeScript components.

## Pre-Implementation Checklist

Before starting any task:
1. Read `docs/ARCHITECTURE_REVIEW.md` to understand the full context
2. Run existing tests to establish baseline: `pytest && cd intelligence-dashboard && npm test`
3. Create a feature branch from main: `git checkout -b claude/implement-arch-fixes-<session-id>`

## Implementation Tasks (in priority order)

Execute these tasks sequentially. After each task, commit with a descriptive message and verify tests still pass.

---

### Task 1: Fix Broken Type Guards (30 min)
**File:** `skills/vianeo-persona-builder/powerups/interactive-dashboard/src/types.ts`

**Problem:** `isLayer1Content` and `isLayer2Content` are identical functions that cannot distinguish between Layer 1 and Layer 2 content.

**Solution:**
1. Read the current type guards at lines 164-178
2. Since Layer1 and Layer2 are structurally identical (both have `fields`), combine them:
```typescript
export function isFieldBasedLayer(content: LayerContent): content is Layer1Content | Layer2Content {
  return 'fields' in content && Array.isArray((content as Layer1Content).fields);
}
```
3. Update any imports/usages in `LayerContent.tsx` to use the new combined guard
4. Run tests: `cd skills/vianeo-persona-builder/powerups/interactive-dashboard && npm test`

**Commit:** `fix(types): combine identical Layer1/Layer2 type guards into isFieldBasedLayer`

---

### Task 2: Add pyproject.toml (30 min)
**Create:** `pyproject.toml` in repository root

**Content:**
```toml
[project]
name = "claude-usecases"
version = "2.8.0"
description = "Claude AI skills and workflows for 360 Social Impact Studios"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [{name = "360 Social Impact Studios"}]
dependencies = [
    "pyyaml>=6.0",
    "python-docx>=1.1.0",
    "openpyxl>=3.1.0",
    "beautifulsoup4>=4.12.0",
]

[project.optional-dependencies]
test = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-mock>=3.12.0",
    "pytest-asyncio>=0.21.0",
    "responses>=0.24.0",
]
dev = [
    "black>=23.0.0",
    "mypy>=1.0.0",
    "ruff>=0.1.0",
]

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = [".", "skills", ".claude/skills"]

[tool.black]
line-length = 127

[tool.mypy]
python_version = "3.11"
ignore_missing_imports = true
```

**Verification:** `pip install -e . && pytest`

**Commit:** `build: add pyproject.toml for formal dependency management`

---

### Task 3: Extract Shared Constants (1 hour)
**Create:** `skills/vianeo-persona-builder/powerups/interactive-dashboard/src/constants.ts`

**Steps:**
1. Extract `personaTypeColors` from `VianeoPersonaExplorer.tsx`
2. Extract `validationStatusConfig` from `LayerContent.tsx`
3. Create centralized constants file
4. Update imports in all components
5. Run tests to verify

**Commit:** `refactor(vianeo): extract shared constants to eliminate duplication`

---

### Task 4: Add relationship-intelligence to CI/CD (2 hours)
**File:** `.github/workflows/tests.yml`

**Steps:**
1. Read current workflow structure
2. Add new job `typescript-relationship-intelligence` following the pattern of `typescript-intelligence-dashboard`
3. Update `test-summary` job to include the new test job
4. Create minimal test file: `relationship-intelligence/dashboard/tests/setup.ts`
5. Add vitest config: `relationship-intelligence/dashboard/vitest.config.ts`
6. Add test script to `relationship-intelligence/dashboard/package.json`

**Commit:** `ci: add relationship-intelligence dashboard to test workflow`

---

### Task 5: Implement transformMarkdownToData() (4 hours)
**File:** `skills/vianeo-persona-builder/powerups/interactive-dashboard/src/utils/dataTransformer.ts`

**Steps:**
1. Read existing parsing utilities (parsePersonaType, extractQuotes, etc.)
2. Implement `transformMarkdownToData(markdown: string, personaId: string): Partial<DashboardData>`
3. Parse markdown sections for each layer
4. Extract structured data using existing utilities
5. Add comprehensive tests in `tests/dataTransformer.test.ts`
6. Update documentation

**Commit:** `feat(vianeo): implement transformMarkdownToData for markdown-to-JSON conversion`

---

### Task 6: Designate Canonical Make.com Blueprint (1 hour)
**Location:** `relationship-intelligence/`

**Steps:**
1. Compare all three blueprint files to understand differences
2. Determine which is most current/correct (likely `make-blueprint-corrected.json`)
3. Rename canonical version to `make-blueprint.json` (backup originals first)
4. Create `relationship-intelligence/BLUEPRINT_VERSIONS.md` documenting the decision
5. Delete or archive non-canonical versions

**Commit:** `chore: designate canonical Make.com blueprint and document decision`

---

### Task 7: Add Tests for Untested Python Modules (3-5 days)
**Priority modules:**

1. **workflow-debugging** (665 lines) - Start here, smallest scope
   - Create `tests/unit/python/test_workflow_debugger.py`
   - Test core debugging functions

2. **ai-ethics-advisor** (823 lines) - Critical business logic
   - Create `tests/unit/python/ai_ethics/test_bias_monitoring.py`
   - Create `tests/unit/python/ai_ethics/test_explainability.py`
   - Create `tests/unit/python/ai_ethics/test_privacy_preserving.py`

3. **financial-modeling-skills** (1,305 lines)
   - Create `tests/unit/python/test_financial_modeling.py`

4. **360-executive-project-tracker** (1,976 lines)
   - Create `tests/unit/python/project_tracker/` directory with tests for each script

**Approach:**
- Use existing fixtures from `tests/conftest.py`
- Focus on public API and critical paths first
- Mark with appropriate pytest markers (`@pytest.mark.financial`, etc.)

**Commit per module:** `test(<module>): add unit tests for <module_name>`

---

### Task 8: Add Vianeo Component Tests (2-3 days)
**Location:** `skills/vianeo-persona-builder/powerups/interactive-dashboard/tests/`

**Create tests for:**
- `VianeoPersonaExplorer.test.tsx` - Main container, state management
- `PersonaCard.test.tsx` - Selection, active state
- `LayerNavigation.test.tsx` - Layer switching
- `LayerContent.test.tsx` - Conditional rendering for all 4 layer types
- `ValidationBadge.test.tsx` - Status display
- `EvidenceQuote.test.tsx` - Quote rendering

**Commit:** `test(vianeo): add comprehensive component test coverage`

---

### Task 9: Consolidate CEO Advisor Locations (2-3 days)
**Problem:** Duplicate modules in `skills/ceo-advisor/src/` and `.claude/skills/ceo-advisor/src/`

**Steps:**
1. Compare files to identify any differences
2. Designate `.claude/skills/ceo-advisor/` as canonical
3. Convert `skills/ceo-advisor/` to routing skill (like vianeo-persona-builder)
4. Update `skills/ceo-advisor/SKILL.md` to route to managed skill
5. Delete duplicate Python files from `skills/ceo-advisor/src/`
6. Run all CEO advisor tests to verify

**Commit:** `refactor(ceo-advisor): consolidate to single managed skill location`

---

### Task 10: Consolidate Vianeo Implementations (3-5 days)
**Problem:** 3 implementations totaling ~3,600 lines

**Steps:**
1. Ensure modular TypeScript version is feature-complete
2. Add build script to generate standalone HTML:
   - Create `vite.standalone.config.ts`
   - Add `build:standalone` script
3. Add build script to generate portable JSX:
   - Use esbuild for single-file output
   - Add `build:portable` script
4. Test generated outputs match originals
5. Delete manual implementations from `examples/`
6. Update documentation

**Commit:** `refactor(vianeo): consolidate implementations with build pipeline`

---

### Task 11-16: Lower Priority Items

See `docs/ARCHITECTURE_REVIEW.md` for details on:
- Task 11: Package Python skills as modules
- Task 12: Add tests for relationship-intelligence
- Task 13: Extract CSS to shared stylesheet
- Task 14: Add JSON validation
- Task 15: Add accessibility testing
- Task 16: Add Python type hints/mypy

---

## Constraints

1. **Do NOT drop features** - All existing functionality must be preserved
2. **Run tests after each change** - Never commit broken tests
3. **Commit incrementally** - One logical change per commit
4. **Flag uncertain changes** - If a refactor might alter behavior, add tests first
5. **Update documentation** - Keep ARCHITECTURE_REVIEW.md current as issues are resolved

## Verification Checklist

After all tasks:
- [ ] All Python tests pass: `pytest`
- [ ] All TypeScript tests pass in all 3 dashboards
- [ ] CI/CD runs successfully
- [ ] No new linting errors
- [ ] ARCHITECTURE_REVIEW.md updated with resolved items

## Success Criteria

- Duplicate code reduced from ~6,600 lines to <500 lines
- Test coverage for previously untested ~6,000 lines of code
- All 3 dashboards included in CI/CD
- Single canonical source for CEO advisor, Vianeo implementations, and Make.com blueprint
