"""
Pytest configuration and shared fixtures for claude-usecases tests.

This file provides common fixtures, test utilities, and configuration
that are available to all test files.
"""

import os
import sys
from pathlib import Path
from typing import Any, Dict

import pytest

# Check yaml availability at module level for use in fixtures and markers
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    yaml = None  # type: ignore
    YAML_AVAILABLE = False

# Add project root and skill directories to Python path
PROJECT_ROOT = Path(__file__).parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
CLAUDE_SKILLS_DIR = PROJECT_ROOT / ".claude" / "skills"
SHARED_DIR = PROJECT_ROOT / "shared"

sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(SKILLS_DIR))
sys.path.insert(0, str(CLAUDE_SKILLS_DIR))
sys.path.insert(0, str(SHARED_DIR))


# ============================================================================
# Path Fixtures
# ============================================================================

@pytest.fixture(scope="session")
def project_root() -> Path:
    """Return the project root directory."""
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def skills_dir() -> Path:
    """Return the skills directory."""
    return SKILLS_DIR


@pytest.fixture(scope="session")
def claude_skills_dir() -> Path:
    """Return the .claude/skills directory."""
    return CLAUDE_SKILLS_DIR


@pytest.fixture(scope="session")
def test_data_dir() -> Path:
    """Return the test data directory."""
    data_dir = PROJECT_ROOT / "tests" / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir


@pytest.fixture
def temp_output_dir(tmp_path) -> Path:
    """Provide a temporary directory for test outputs."""
    output_dir = tmp_path / "output"
    output_dir.mkdir(exist_ok=True)
    return output_dir


# ============================================================================
# Dependency Availability Fixtures
# ============================================================================

@pytest.fixture(scope="session")
def yaml_available() -> bool:
    """Check if PyYAML is available for tests that require it."""
    return YAML_AVAILABLE


@pytest.fixture
def require_yaml():
    """Skip test if PyYAML is not available."""
    if not YAML_AVAILABLE:
        pytest.skip("PyYAML not installed - skipping yaml-dependent test")


# ============================================================================
# Sample Data Fixtures
# ============================================================================

@pytest.fixture
def sample_financial_data() -> Dict[str, Any]:
    """Provide sample financial data for testing."""
    return {
        "revenue": 150000.00,
        "expenses": 125000.00,
        "assets": 500000.00,
        "liabilities": 200000.00,
        "contributions": 75000.00,
        "grants_paid": 50000.00,
    }


@pytest.fixture
def sample_990_data() -> Dict[str, Any]:
    """Provide sample IRS 990-EZ data for testing."""
    return {
        "organization_name": "Test Nonprofit Organization",
        "ein": "12-3456789",
        "tax_year": 2024,
        "gross_receipts": 175000.00,
        "total_revenue": 150000.00,
        "total_expenses": 125000.00,
        "total_assets": 500000.00,
        "total_liabilities": 200000.00,
    }


@pytest.fixture
def sample_persona_data() -> Dict[str, Any]:
    """Provide sample Vianeo persona data for testing."""
    return {
        "name": "Innovation Director",
        "layer": "Surface",
        "validation_status": "Validated",
        "evidence_quotes": [
            "We need to innovate faster to stay competitive",
            "Budget constraints are limiting our ability to experiment"
        ],
        "pain_points": [
            "Limited innovation budget",
            "Resistance to change from leadership"
        ],
    }


@pytest.fixture
def sample_stakeholder_data() -> Dict[str, Any]:
    """Provide sample stakeholder data for testing."""
    return {
        "name": "John Smith",
        "organization": "ABC Foundation",
        "relationship_strength": 0.85,
        "sentiment_score": 0.72,
        "last_contact": "2024-11-15",
        "engagement_level": "high",
    }


# ============================================================================
# Mock API Fixtures
# ============================================================================

@pytest.fixture
def mock_asana_response():
    """Provide mock Asana API response."""
    return {
        "data": {
            "tasks": [
                {
                    "gid": "12345",
                    "name": "Complete project plan",
                    "completed": False,
                    "due_on": "2024-11-30",
                }
            ]
        }
    }


@pytest.fixture
def mock_supabase_response():
    """Provide mock Supabase query response."""
    return {
        "data": [
            {
                "id": 1,
                "partner_name": "Test Partner",
                "partner_type": "Strategic",
                "quality_score": 0.87,
            }
        ],
        "error": None,
    }


# ============================================================================
# File Fixtures
# ============================================================================

@pytest.fixture
def sample_markdown_content() -> str:
    """Provide sample markdown content for testing parsers."""
    return """# Innovation Director

## Layer: Surface

### Validation Status: Validated

#### Evidence Quotes
- "We need to innovate faster to stay competitive"
- "Budget constraints are limiting our ability to experiment"

#### Pain Points
* Limited innovation budget
* Resistance to change from leadership
"""


@pytest.fixture
def sample_html_template() -> str:
    """Provide sample HTML template content."""
    return """<!DOCTYPE html>
<html>
<head>
    <title>Test Dashboard</title>
</head>
<body>
    <h1>Executive Dashboard</h1>
    <div id="metrics">
        <div class="metric">
            <span class="label">Revenue</span>
            <span class="value">$150,000</span>
        </div>
    </div>
</body>
</html>
"""


# ============================================================================
# Test Markers and Configuration
# ============================================================================

def pytest_configure(config):
    """Configure pytest with custom settings."""
    config.addinivalue_line(
        "markers", "unit: Unit tests"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests"
    )
    config.addinivalue_line(
        "markers", "e2e: End-to-end tests"
    )
    config.addinivalue_line(
        "markers", "financial: Financial calculation tests"
    )
    config.addinivalue_line(
        "markers", "compliance: Regulatory compliance tests"
    )


def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "e2e" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)


# ============================================================================
# Cleanup Fixtures
# ============================================================================

@pytest.fixture(autouse=True)
def cleanup_test_outputs(request):
    """Automatically clean up test outputs after each test."""
    yield
    # Cleanup code runs after the test
    # Add any necessary cleanup logic here
