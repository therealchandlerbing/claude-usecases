"""
Example Python unit tests demonstrating pytest setup and fixtures.

This file serves as a template and validation for the pytest configuration.
"""

import pytest
from pathlib import Path


class TestPytestSetup:
    """Test that pytest is configured correctly."""

    def test_basic_assertion(self):
        """Verify basic assertions work."""
        assert True
        assert 1 + 1 == 2
        assert "hello" == "hello"

    def test_fixture_usage(self, project_root):
        """Verify fixtures are available."""
        assert isinstance(project_root, Path)
        assert project_root.exists()
        assert (project_root / "pytest.ini").exists()

    def test_test_data_dir_fixture(self, test_data_dir):
        """Verify test data directory fixture works."""
        assert isinstance(test_data_dir, Path)
        assert test_data_dir.exists()

    def test_temp_output_dir_fixture(self, temp_output_dir):
        """Verify temporary output directory fixture works."""
        assert isinstance(temp_output_dir, Path)
        assert temp_output_dir.exists()

        # Write a test file to temp directory
        test_file = temp_output_dir / "test.txt"
        test_file.write_text("test content")
        assert test_file.read_text() == "test content"


class TestSampleDataFixtures:
    """Test that sample data fixtures work correctly."""

    def test_sample_financial_data(self, sample_financial_data):
        """Verify financial data fixture."""
        assert "revenue" in sample_financial_data
        assert "expenses" in sample_financial_data
        assert sample_financial_data["revenue"] == 150000.00
        assert sample_financial_data["expenses"] == 125000.00

    def test_sample_990_data(self, sample_990_data):
        """Verify 990 data fixture."""
        assert "organization_name" in sample_990_data
        assert "ein" in sample_990_data
        assert sample_990_data["tax_year"] == 2024
        assert sample_990_data["gross_receipts"] == 175000.00

    def test_sample_persona_data(self, sample_persona_data):
        """Verify persona data fixture."""
        assert sample_persona_data["name"] == "Innovation Director"
        assert sample_persona_data["layer"] == "Surface"
        assert sample_persona_data["validation_status"] == "Validated"
        assert len(sample_persona_data["evidence_quotes"]) == 2

    def test_sample_stakeholder_data(self, sample_stakeholder_data):
        """Verify stakeholder data fixture."""
        assert sample_stakeholder_data["name"] == "John Smith"
        assert sample_stakeholder_data["relationship_strength"] == 0.85
        assert sample_stakeholder_data["engagement_level"] == "high"


class TestMarkdownParsing:
    """Example tests for markdown parsing functionality."""

    def test_parse_markdown_headers(self, sample_markdown_content):
        """Test parsing markdown headers."""
        assert "# Innovation Director" in sample_markdown_content
        assert "## Layer: Surface" in sample_markdown_content

    def test_parse_markdown_lists(self, sample_markdown_content):
        """Test parsing markdown lists."""
        lines = sample_markdown_content.split("\n")
        bullet_lines = [line for line in lines if line.strip().startswith("-") or line.strip().startswith("*")]
        assert len(bullet_lines) > 0


@pytest.mark.unit
class TestMarkers:
    """Test that markers work correctly."""

    def test_unit_marker(self):
        """This test should have the unit marker."""
        assert True


@pytest.mark.financial
class TestFinancialCalculations:
    """Example financial calculation tests (marked as financial priority)."""

    def test_revenue_calculation(self, sample_financial_data):
        """Test revenue calculation."""
        revenue = sample_financial_data["revenue"]
        expenses = sample_financial_data["expenses"]
        net_income = revenue - expenses

        assert net_income == 25000.00

    def test_990_eligibility_threshold(self, sample_990_data):
        """Test 990-EZ eligibility based on gross receipts."""
        gross_receipts = sample_990_data["gross_receipts"]

        # 990-EZ threshold is $200,000
        threshold = 200000.00

        if gross_receipts < threshold:
            assert True, "Organization qualifies for 990-EZ"
        else:
            assert False, "Organization must file full 990"


class TestDataValidation:
    """Example data validation tests."""

    def test_ein_format(self, sample_990_data):
        """Test EIN format validation."""
        ein = sample_990_data["ein"]

        # EIN should be in format XX-XXXXXXX
        assert len(ein) == 10
        assert ein[2] == "-"
        assert ein[:2].isdigit()
        assert ein[3:].isdigit()

    def test_required_fields(self, sample_990_data):
        """Test that required fields are present."""
        required_fields = [
            "organization_name",
            "ein",
            "tax_year",
            "gross_receipts",
            "total_revenue",
            "total_expenses"
        ]

        for field in required_fields:
            assert field in sample_990_data, f"Required field {field} is missing"

    def test_data_types(self, sample_990_data):
        """Test that data types are correct."""
        assert isinstance(sample_990_data["organization_name"], str)
        assert isinstance(sample_990_data["ein"], str)
        assert isinstance(sample_990_data["tax_year"], int)
        assert isinstance(sample_990_data["gross_receipts"], (int, float))


class TestHTMLTemplate:
    """Example HTML template tests."""

    def test_html_structure(self, sample_html_template):
        """Test basic HTML structure."""
        assert "<!DOCTYPE html>" in sample_html_template
        assert "<html>" in sample_html_template
        assert "</html>" in sample_html_template

    def test_html_content(self, sample_html_template):
        """Test HTML contains expected content."""
        assert "Executive Dashboard" in sample_html_template
        assert "Revenue" in sample_html_template
        assert "$150,000" in sample_html_template


# Test that can be skipped conditionally
@pytest.mark.skip(reason="Example of a skipped test")
def test_skipped_example():
    """This test will be skipped."""
    assert False


# Test that expects an exception
def test_exception_handling():
    """Test exception handling."""
    with pytest.raises(ValueError):
        raise ValueError("Expected error")


# Parametrized test example
@pytest.mark.parametrize("input_value,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
])
def test_parametrized_example(input_value, expected):
    """Example of parametrized tests."""
    assert input_value * 2 == expected
