# Test Data Directory

This directory contains test fixtures, sample data, and mock files used by the test suite.

## Directory Structure

```
tests/data/
├── README.md                              # This file
│
├── financial/                             # Financial data files
│   ├── sample_990_eligible.json           # 990-EZ eligible organization (< thresholds)
│   └── sample_990_ineligible.json         # 990-EZ ineligible organization (> thresholds)
│
├── personas/                              # Vianeo persona examples
│   └── sample_innovator_persona.json      # Innovation Director persona (Jobs-to-be-Done)
│
├── api_responses/                         # Mock API responses
│   ├── asana_tasks_response.json          # Sample Asana API task list
│   └── supabase_partners_response.json    # Sample Supabase partnership data
│
├── governance/                            # Governance and compliance data
│   └── sample_board_structure.json        # Board composition and policies
│
└── html/                                  # HTML templates and outputs
    └── sample_dashboard_template.html     # Executive dashboard template
```

## File Descriptions

### Financial Data (`financial/`)

| File | Description | Use Case |
|------|-------------|----------|
| `sample_990_eligible.json` | Complete nonprofit profile eligible for 990-EZ | Testing 990-EZ eligibility validation, form generation |
| `sample_990_ineligible.json` | Organization exceeding 990-EZ thresholds | Testing threshold validation, form 990 routing |

**Key thresholds tested:**
- Gross receipts: $200,000 limit
- Total assets: $500,000 limit

### Personas (`personas/`)

| File | Description | Use Case |
|------|-------------|----------|
| `sample_innovator_persona.json` | Innovation Director persona with Jobs-to-be-Done | Testing persona builders, strategic analysis |

**Includes:**
- Demographic profile
- Functional, emotional, and social jobs
- Pain points with evidence quotes
- Decision criteria and communication preferences

### API Responses (`api_responses/`)

| File | Description | Use Case |
|------|-------------|----------|
| `asana_tasks_response.json` | Mock Asana API response with tasks | Testing Asana integration, task parsing |
| `supabase_partners_response.json` | Mock Supabase query with partner data | Testing partnership dashboard, intelligence extraction |

### Governance (`governance/`)

| File | Description | Use Case |
|------|-------------|----------|
| `sample_board_structure.json` | Board composition, officers, policies | Testing board meeting prep, governance compliance |

**Includes:**
- Board member profiles
- Committee structure
- Governance policies (conflict of interest, whistleblower, etc.)
- Financial oversight configuration

### HTML Templates (`html/`)

| File | Description | Use Case |
|------|-------------|----------|
| `sample_dashboard_template.html` | Executive dashboard with template variables | Testing HTML generation, report styling |

## Usage

Test data files in this directory are available to tests via the `test_data_dir` fixture:

```python
import json

def test_load_sample_data(test_data_dir):
    sample_file = test_data_dir / "financial" / "sample_990_eligible.json"
    data = json.loads(sample_file.read_text())

    assert data["eligibility"]["is_eligible_for_990ez"] is True
    assert data["eligibility"]["gross_receipts"] < 200000
```

### Loading JSON Files

```python
def test_api_response_parsing(test_data_dir):
    response_file = test_data_dir / "api_responses" / "asana_tasks_response.json"
    response = json.loads(response_file.read_text())

    tasks = response["data"]
    assert len(tasks) == 3
```

### Using with Fixtures

```python
@pytest.fixture
def loaded_990_data(test_data_dir):
    """Load 990 eligible organization data."""
    file_path = test_data_dir / "financial" / "sample_990_eligible.json"
    return json.loads(file_path.read_text())

def test_eligibility_check(loaded_990_data):
    assert loaded_990_data["eligibility"]["is_eligible_for_990ez"]
```

## Guidelines

1. **Keep files small**: Test data should be minimal but representative
2. **Use realistic data**: Data should reflect actual use cases but be anonymized
3. **Version control**: All test data should be committed to git
4. **Documentation**: Add comments to complex test data files
5. **Consistency**: Use consistent naming and structure across similar files
6. **No secrets**: Never include real credentials, API keys, or PII

## Adding New Test Data

1. Create the file in the appropriate subdirectory
2. Use JSON for structured data, YAML for configuration
3. Add an entry to this README
4. Consider creating a pytest fixture if the data will be reused

## Related Fixtures

The following fixtures are defined in `conftest.py` and provide in-memory test data:

| Fixture | Description |
|---------|-------------|
| `sample_financial_data` | Basic financial dict |
| `sample_990_data` | IRS 990 summary data |
| `sample_persona_data` | Vianeo persona dict |
| `sample_stakeholder_data` | Stakeholder relationship data |
| `mock_asana_response` | Asana API response dict |
| `mock_supabase_response` | Supabase query response dict |
| `sample_markdown_content` | Markdown content string |
| `sample_html_template` | HTML template string |

---

*Updated: November 2025*
