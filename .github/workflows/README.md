# GitHub Actions Workflows

This directory contains automated CI/CD workflows for the claude-usecases repository.

## Workflows

### 1. Tests (`tests.yml`)

**Triggers:**
- Push to `main`, `master`, or any `claude/**` branch
- Pull requests to `main` or `master`

**Jobs:**
- **python-tests**: Runs all Python tests with pytest
  - Python 3.11
  - Installs dependencies from `requirements-test.txt`
  - Runs tests with coverage reporting
  - Uploads coverage artifacts

- **typescript-intelligence-dashboard**: Tests for Intelligence Dashboard
  - Node.js 18
  - Runs vitest tests
  - Generates coverage reports

- **typescript-vianeo-dashboard**: Tests for Vianeo Persona Builder
  - Node.js 18
  - Runs vitest tests for dataTransformer and components
  - Generates coverage reports

- **test-summary**: Aggregates results from all test jobs

**Artifacts:**
- Python coverage reports (HTML + XML)
- TypeScript coverage reports
- Retained for 30 days

**Status Badge:**
```markdown
![Tests](https://github.com/therealchandlerbing/claude-usecases/workflows/Tests/badge.svg)
```

### 2. Code Quality (`code-quality.yml`)

**Triggers:**
- Push to `main`, `master`, or any `claude/**` branch
- Pull requests to `main` or `master`

**Jobs:**
- **python-quality**: Code quality checks for Python
  - flake8 (syntax errors and code complexity)
  - pylint (critical modules)
  - black (code formatting)
  - mypy (type checking)

- **typescript-quality**: Code quality checks for TypeScript
  - TypeScript compiler type checking
  - ESLint linting

**Note:** Quality checks are informational and don't block merges.

### 3. Coverage Report (`coverage.yml`)

**Triggers:**
- Push to `main` or `master`
- Pull requests to `main` or `master`

**Jobs:**
- **coverage**: Generates detailed coverage reports
  - Python test coverage
  - Coverage percentage calculation
  - Creates PR comment with coverage details
  - Uploads coverage reports as artifacts

**Artifacts:**
- HTML coverage report
- XML coverage report
- Coverage comment (for PRs)
- Retained for 90 days

## Running Workflows Locally

### Python Tests

```bash
# Install dependencies
pip install -r requirements-test.txt

# Run tests
python -m pytest --verbose

# Run with coverage
python -m pytest \
  --cov=skills \
  --cov=.claude/skills \
  --cov-report=html \
  --cov-report=term-missing
```

### TypeScript Tests

**Intelligence Dashboard:**
```bash
cd intelligence-dashboard
npm ci
npm test
npm run test:coverage
```

**Vianeo Persona Builder:**
```bash
cd skills/vianeo-persona-builder/powerups/interactive-dashboard
npm ci
npm test
npm run test:coverage
```

### Code Quality Checks

**Python:**
```bash
# Syntax errors
flake8 skills/ .claude/skills/ --count --select=E9,F63,F7,F82

# Code complexity
flake8 skills/ .claude/skills/ --count --max-complexity=10

# Formatting
black --check skills/ .claude/skills/ tests/

# Type checking
mypy skills/ --ignore-missing-imports
```

**TypeScript:**
```bash
# Type checking
cd intelligence-dashboard && npm run type-check

# Linting
cd intelligence-dashboard && npm run lint
```

## Workflow Configuration

### Caching

All workflows use dependency caching to speed up runs:
- Python: pip cache
- TypeScript: npm cache

### Matrix Strategies

Workflows use matrix strategies where appropriate:
- Python: Version 3.11 (can expand to 3.10, 3.12)
- TypeScript: Separate jobs for each project

### Artifact Retention

- Test artifacts: 30 days
- Coverage reports: 90 days

## Viewing Results

### In GitHub UI

1. Go to the **Actions** tab
2. Select a workflow run
3. View job details and artifacts
4. Download coverage reports

### In Pull Requests

- Check status at the bottom of PR
- View detailed logs by clicking "Details"
- Download artifacts from workflow run

### Coverage Reports

1. Navigate to workflow run
2. Download `coverage-report` artifact
3. Extract and open `htmlcov/index.html` in browser

## Troubleshooting

### Tests Failing Locally But Passing in CI

- Check Python version (CI uses 3.11)
- Ensure all dependencies installed: `pip install -r requirements-test.txt`
- Clear pytest cache: `rm -rf .pytest_cache`

### TypeScript Tests Failing

- Delete node_modules and reinstall: `rm -rf node_modules && npm ci`
- Clear vitest cache
- Check Node.js version (CI uses 18)

### Coverage Not Generating

- Ensure pytest-cov is installed
- Check that source paths are correct in coverage commands
- Verify pytest.ini configuration

## Adding New Tests

When adding new test files:

1. **Python**: Place in `tests/unit/python/` or appropriate subdirectory
2. **TypeScript**: Place in project's `tests/` directory
3. **Markers**: Use appropriate pytest markers (`@pytest.mark.financial`, etc.)
4. **Naming**: Follow naming conventions (`test_*.py`, `*.test.ts`)

Workflows will automatically discover and run new tests.

## Modifying Workflows

### Adding a New Workflow

1. Create new YAML file in `.github/workflows/`
2. Define triggers (`on:`)
3. Add jobs with steps
4. Test locally if possible
5. Commit and push to see it run

### Updating Existing Workflows

1. Edit YAML file
2. Test syntax with YAML validator
3. Commit changes
4. Monitor first run carefully

### Best Practices

- Use descriptive job and step names
- Add comments for complex logic
- Use `continue-on-error: true` for informational checks
- Upload artifacts for debugging
- Use GitHub Actions' native caching
- Keep workflows DRY with reusable actions

## Status Badges

Add to README.md:

```markdown
![Tests](https://github.com/therealchandlerbing/claude-usecases/workflows/Tests/badge.svg)
![Code Quality](https://github.com/therealchandlerbing/claude-usecases/workflows/Code%20Quality/badge.svg)
![Coverage](https://github.com/therealchandlerbing/claude-usecases/workflows/Coverage%20Report/badge.svg)
```

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [pytest Documentation](https://docs.pytest.org/)
- [vitest Documentation](https://vitest.dev/)
- [Coverage.py Documentation](https://coverage.readthedocs.io/)

---

**Last Updated:** 2025-11-20
**Maintained By:** 360 Social Impact Studios
