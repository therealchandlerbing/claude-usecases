# Testing Guide

This document provides comprehensive information about the testing infrastructure, how to run tests, and how to write new tests for the claude-usecases project.

## Table of Contents

1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Test Infrastructure](#test-infrastructure)
4. [Running Tests](#running-tests)
5. [Writing Tests](#writing-tests)
6. [Test Organization](#test-organization)
7. [Coverage Requirements](#coverage-requirements)
8. [CI/CD Integration](#cicd-integration)
9. [Best Practices](#best-practices)

---

## Overview

The claude-usecases project uses two testing frameworks:

- **pytest** for Python code (skills, orchestrators, utilities)
- **vitest** for TypeScript/React code (dashboards, UI components)

### Current Status

The repository currently includes:

- **Python unit tests** for the CEO advisor skill, 990 orchestrator helpers, placeholder behaviors, and a general example suite.
- **TypeScript unit tests** for the Intelligence Dashboard (Supabase utilities) and the Vianeo Persona Builder interactive dashboard (data transformer utilities).

Coverage is still being expanded. Near-term focus areas remain:

1. **Financial & Compliance** (IRS 990-EZ workflows, financial modeling)
2. **Executive Intelligence** (CEO advisor, stakeholder analytics)
3. **Data Processing** (transformers, collectors)
4. **UI Components** (dashboards, visualizations)

---

## Quick Start

### Install Dependencies

**Python Testing:**
```bash
pip install -r requirements-test.txt
```

**TypeScript Testing (Intelligence Dashboard):**
```bash
cd intelligence-dashboard
npm install
```

**TypeScript Testing (Vianeo Persona Builder):**
```bash
cd skills/vianeo-persona-builder/powerups/interactive-dashboard
npm install
```

### Run Tests

**Python:**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test file
pytest tests/unit/python/test_example.py

# Run tests with specific marker
pytest -m financial
```

**TypeScript (Intelligence Dashboard):**
```bash
cd intelligence-dashboard

# Run all tests
npm test

# Run with UI
npm run test:ui

# Run with coverage
npm run test:coverage

# Run in watch mode
npm run test:watch
```

**TypeScript (Vianeo Persona Builder):**
```bash
cd skills/vianeo-persona-builder/powerups/interactive-dashboard

# Run all tests
npm test

# Run with coverage
npm run test:coverage
```

---

## Test Infrastructure

### Python (pytest)

**Configuration:** `pytest.ini`

Key features:
- Coverage reporting (HTML, terminal, XML)
- Custom markers for organizing tests (unit, integration, financial, compliance)
- Shared fixtures in `tests/conftest.py`
- Automatic test discovery

**Fixtures Available:**

- `project_root` - Path to project root directory
- `skills_dir` - Path to skills directory
- `claude_skills_dir` - Path to .claude/skills directory
- `test_data_dir` - Path to test data directory
- `temp_output_dir` - Temporary directory for test outputs
- `sample_financial_data` - Sample financial data
- `sample_990_data` - Sample IRS 990 data
- `sample_persona_data` - Sample Vianeo persona data
- `sample_stakeholder_data` - Sample stakeholder data
- `mock_asana_response` - Mock Asana API response
- `mock_supabase_response` - Mock Supabase response
- `sample_markdown_content` - Sample markdown content
- `sample_html_template` - Sample HTML template

### TypeScript (vitest)

**Configuration:**
- `intelligence-dashboard/vitest.config.ts`
- `skills/vianeo-persona-builder/powerups/interactive-dashboard/vitest.config.ts`

Key features:
- jsdom environment for React component testing
- Coverage with v8 provider
- UI mode for interactive testing
- React Testing Library integration

**Setup Files:**
- Next.js router mocking
- Window.matchMedia mocking
- IntersectionObserver mocking
- ResizeObserver mocking
- Environment variable mocking

---

## Running Tests

### Test Selection

**By File:**
```bash
# Python
pytest tests/unit/python/test_example.py

# TypeScript
npm test -- dataTransformer.test.ts
```

**By Marker:**
```bash
pytest -m unit          # Run only unit tests
pytest -m financial     # Run only financial tests
pytest -m integration   # Run only integration tests
```

**By Test Name:**
```bash
pytest -k "test_revenue"  # Run tests matching "test_revenue"
```

### Verbose Output

```bash
# Python
pytest -v

# TypeScript
npm run test:ui  # Opens interactive UI
```

### Coverage Reports

**Python:**
```bash
pytest --cov --cov-report=html
# Open htmlcov/index.html in browser
```

**TypeScript:**
```bash
npm run test:coverage
# Open coverage/index.html in browser
```

---

## Writing Tests

### Python Unit Test Template

```python
"""
Test module for [module_name].
"""

import pytest


class Test[ModuleName]:
    """Tests for [module_name] functionality."""

    def test_basic_functionality(self):
        """Test basic functionality."""
        # Arrange
        input_data = {"key": "value"}

        # Act
        result = process_data(input_data)

        # Assert
        assert result is not None
        assert result["key"] == "expected_value"

    def test_error_handling(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            process_invalid_data(None)

    @pytest.mark.financial
    def test_financial_calculation(self, sample_financial_data):
        """Test financial calculation logic."""
        result = calculate_net_income(sample_financial_data)
        assert result == 25000.00
```

### TypeScript Component Test Template

```typescript
import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import { userEvent } from '@testing-library/user-event'
import { ComponentName } from '../src/components/ComponentName'

describe('ComponentName', () => {
  it('should render correctly', () => {
    render(<ComponentName />)

    expect(screen.getByText('Expected Text')).toBeInTheDocument()
  })

  it('should handle user interaction', async () => {
    const user = userEvent.setup()
    render(<ComponentName />)

    const button = screen.getByRole('button', { name: 'Click Me' })
    await user.click(button)

    expect(screen.getByText('Clicked!')).toBeInTheDocument()
  })
})
```

### TypeScript Utility Test Template

```typescript
import { describe, it, expect } from 'vitest'
import { utilityFunction } from '../src/utils/utilityFunction'

describe('utilityFunction', () => {
  it('should transform input correctly', () => {
    const input = 'test input'
    const result = utilityFunction(input)

    expect(result).toBe('expected output')
  })

  it('should handle edge cases', () => {
    expect(utilityFunction('')).toBe('')
    expect(utilityFunction(null)).toBe(null)
  })
})
```

---

## Test Organization

### Directory Structure

```
tests/
├── conftest.py              # Shared pytest fixtures
├── data/README.md           # Notes for adding shared test data
└── unit/                    # Unit tests
    └── python/
        ├── test_990_orchestrator.py
        ├── test_ceo_advisor.py
        ├── test_example.py
        └── test_placeholder.py
```

TypeScript unit tests live inside their respective project directories:

- `intelligence-dashboard/tests/` (e.g., `supabase.test.ts`)
- `skills/vianeo-persona-builder/powerups/interactive-dashboard/tests/` (e.g., `dataTransformer.test.ts`)

### Test Markers

Use markers to organize and categorize tests:

```python
@pytest.mark.unit           # Unit test
@pytest.mark.integration    # Integration test
@pytest.mark.e2e           # End-to-end test (marker registered, tests to be added)
@pytest.mark.financial     # Financial calculation (high priority)
@pytest.mark.compliance    # Regulatory compliance (high priority)
@pytest.mark.data_processing  # Data processing test
@pytest.mark.api           # External API test
@pytest.mark.slow          # Slow-running test
```

Run specific categories:
```bash
pytest -m "financial and not slow"
pytest -m "unit or integration"
```

---

## Coverage Requirements

### Current Targets

Starting from 0% coverage, we're building coverage incrementally:

**Phase 1 (Weeks 1-2):** Critical path coverage
- Financial modules: Target 80%+
- Compliance modules: Target 80%+
- Data transformers: Target 70%+

**Phase 2 (Weeks 3-4):** Integration coverage
- Multi-module workflows: Target 60%+
- API integrations: Target 70%+

**Phase 3 (Weeks 5-6):** UI coverage
- React components: Target 60%+
- User interactions: Target 50%+

**Long-term Goal:** 80% overall coverage for critical modules

### Checking Coverage

```bash
# Python - view overall coverage
pytest --cov

# Python - view line-by-line coverage
pytest --cov --cov-report=term-missing

# TypeScript
npm run test:coverage
```

### Coverage Configuration

Coverage thresholds are currently set to 0% to allow gradual improvement. Update these in:
- `pytest.ini` (Python)
- `vitest.config.ts` (TypeScript)

---

## CI/CD Integration

### GitHub Actions (Future)

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  python-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements-test.txt
      - run: pytest --cov --cov-report=xml
      - uses: codecov/codecov-action@v3

  typescript-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: cd intelligence-dashboard && npm install
      - run: cd intelligence-dashboard && npm test
      - run: cd intelligence-dashboard && npm run test:coverage
```

---

## Best Practices

### 1. Test Naming

**Be descriptive:**
```python
# Good
def test_calculate_net_income_returns_correct_value():
    pass

# Bad
def test_calculation():
    pass
```

### 2. AAA Pattern

Organize tests with Arrange-Act-Assert:

```python
def test_data_transformation():
    # Arrange
    input_data = create_test_data()

    # Act
    result = transform_data(input_data)

    # Assert
    assert result["status"] == "success"
```

### 3. Test Independence

Each test should be independent:

```python
# Good - uses fixture
def test_with_fresh_data(sample_financial_data):
    modify_data(sample_financial_data)
    assert check_result(sample_financial_data)

# Bad - relies on global state
global_data = {}
def test_modifies_global():
    modify_data(global_data)  # Affects other tests!
```

### 4. Use Fixtures

Leverage fixtures for common setup:

```python
@pytest.fixture
def configured_orchestrator():
    orchestrator = Orchestrator()
    orchestrator.configure(test_settings)
    return orchestrator

def test_orchestration(configured_orchestrator):
    result = configured_orchestrator.run()
    assert result.success
```

### 5. Test Edge Cases

```python
def test_parse_quality_score():
    # Normal cases
    assert parseQualityScore("score: 4") == 4

    # Edge cases
    assert parseQualityScore("") == 3  # default
    assert parseQualityScore("invalid") == 3
    assert parseQualityScore("score: 0") == 0
    assert parseQualityScore("score: 5") == 5
```

### 6. Mock External Dependencies

```python
def test_api_integration(mocker):
    # Mock external API
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.json.return_value = {"status": "ok"}

    result = fetch_data()
    assert result["status"] == "ok"
```

### 7. Test Error Paths

```python
def test_handles_missing_required_field():
    with pytest.raises(ValueError, match="Missing required field"):
        process_data({})  # Missing required data
```

### 8. Keep Tests Fast

- Mock slow operations (API calls, file I/O)
- Use in-memory databases for integration tests
- Mark slow tests with `@pytest.mark.slow`

### 9. Document Complex Tests

```python
def test_complex_financial_scenario(sample_990_data):
    """
    Test 990-EZ eligibility for edge case where:
    - Gross receipts are exactly at threshold
    - Organization has foreign assets
    - Tax year spans 2024-2025
    """
    # Test implementation...
```

### 10. Continuous Improvement

- Review coverage reports regularly
- Add tests when fixing bugs
- Refactor tests as code evolves
- Delete obsolete tests

---

## Troubleshooting

### Common Issues

**Import errors:**
```bash
# Ensure Python path is set
export PYTHONPATH="${PYTHONPATH}:${PWD}"
pytest
```

**Module not found:**
```bash
# Install test dependencies
pip install -r requirements-test.txt
```

**Coverage not working:**
```bash
# Reinstall coverage
pip install --upgrade pytest-cov coverage
```

**TypeScript tests fail:**
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

---

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [vitest Documentation](https://vitest.dev/)
- [React Testing Library](https://testing-library.com/react)
- [Testing Best Practices](https://testingjavascript.com/)

---

## Getting Help

- Check existing tests in `tests/unit/python/test_example.py`
- Review fixture definitions in `tests/conftest.py`
- Ask in team chat or open an issue

---

**Last Updated:** November 20, 2024
**Status:** Testing infrastructure established, building coverage
