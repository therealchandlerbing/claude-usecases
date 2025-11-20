# Tests

This directory contains all test files for the claude-usecases project.

## Quick Start

### Python Tests

```bash
# Install dependencies
pip install -r requirements-test.txt

# Run all tests
pytest

# Run with coverage
pytest --cov --cov-report=html

# Run specific tests
pytest tests/unit/python/test_example.py
pytest -m financial  # Run only financial tests
```

### TypeScript Tests

```bash
# Intelligence Dashboard
cd intelligence-dashboard
npm install
npm test

# Vianeo Persona Builder
cd skills/vianeo-persona-builder/powerups/interactive-dashboard
npm install
npm test
```

## Directory Structure

```
tests/
├── conftest.py              # Shared pytest fixtures and configuration
├── data/                    # Test data and fixtures
│   └── README.md
├── unit/                    # Unit tests
│   ├── python/              # Python unit tests
│   │   └── test_example.py
│   └── typescript/          # TypeScript unit tests (in project dirs)
├── integration/             # Integration tests
└── e2e/                     # End-to-end tests
```

## Test Markers

- `@pytest.mark.unit` - Unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.e2e` - End-to-end tests
- `@pytest.mark.financial` - Financial calculation tests (high priority)
- `@pytest.mark.compliance` - Regulatory compliance tests (high priority)
- `@pytest.mark.data_processing` - Data processing tests
- `@pytest.mark.api` - External API integration tests
- `@pytest.mark.slow` - Slow-running tests

## Available Fixtures

See `conftest.py` for all available fixtures, including:

- Path fixtures: `project_root`, `skills_dir`, `test_data_dir`, `temp_output_dir`
- Sample data: `sample_financial_data`, `sample_990_data`, `sample_persona_data`
- Mock responses: `mock_asana_response`, `mock_supabase_response`
- Content fixtures: `sample_markdown_content`, `sample_html_template`

## Documentation

See [TESTING.md](../TESTING.md) in the project root for comprehensive testing documentation, including:

- How to write tests
- Best practices
- CI/CD integration
- Troubleshooting

## Current Status

**Coverage:** Building from 0%

**Priority Areas:**
1. Financial & Compliance (IRS 990-EZ, financial modeling)
2. Executive Intelligence (CEO advisor, stakeholder analytics)
3. Data Processing (transformers, collectors)
4. UI Components (dashboards, visualizations)

## Contributing

When adding new tests:

1. Place unit tests in `unit/python/` or within the TypeScript project's `tests/` directory
2. Use appropriate markers to categorize tests
3. Add test data to `data/` if needed
4. Follow the AAA pattern (Arrange, Act, Assert)
5. Keep tests independent and fast
6. Document complex test scenarios

## Running Specific Test Categories

```bash
# Unit tests only
pytest -m unit

# Financial and compliance tests (high priority)
pytest -m "financial or compliance"

# All except slow tests
pytest -m "not slow"

# Integration tests only
pytest -m integration
```

## Coverage Reports

After running tests with coverage, view the reports:

**Python:**
```bash
pytest --cov --cov-report=html
open htmlcov/index.html  # or xdg-open on Linux
```

**TypeScript:**
```bash
npm run test:coverage
open coverage/index.html
```

## Example Test

See `tests/unit/python/test_example.py` for a comprehensive example showing:
- Fixture usage
- Markers
- Parametrized tests
- Exception testing
- Data validation tests
