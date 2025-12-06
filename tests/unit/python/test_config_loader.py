"""
Tests for the shared config_loader module.

Tests cover:
- YAML loading with various scenarios
- Error handling for missing/invalid files
- Frontmatter extraction from markdown files
- Default value merging
- Required field validation
"""

import pytest
from pathlib import Path
from shared.config_loader import ConfigLoader, ConfigurationError


class TestLoadYaml:
    """Tests for ConfigLoader.load_yaml()"""

    def test_load_valid_yaml(self, tmp_path: Path):
        """Test loading a valid YAML file."""
        config_file = tmp_path / "config.yaml"
        config_file.write_text("key: value\nnumber: 42\n")

        result = ConfigLoader.load_yaml(config_file)

        assert result == {"key": "value", "number": 42}

    def test_load_empty_yaml(self, tmp_path: Path):
        """Test loading an empty YAML file returns empty dict."""
        config_file = tmp_path / "empty.yaml"
        config_file.write_text("")

        result = ConfigLoader.load_yaml(config_file)

        assert result == {}

    def test_load_yaml_with_nested_structure(self, tmp_path: Path):
        """Test loading YAML with nested structures."""
        config_file = tmp_path / "nested.yaml"
        config_file.write_text("""
database:
  host: localhost
  port: 5432
features:
  - auth
  - logging
""")

        result = ConfigLoader.load_yaml(config_file)

        assert result["database"]["host"] == "localhost"
        assert result["database"]["port"] == 5432
        assert result["features"] == ["auth", "logging"]

    def test_load_required_missing_file_raises_error(self, tmp_path: Path):
        """Test that missing required file raises ConfigurationError."""
        missing_file = tmp_path / "nonexistent.yaml"

        with pytest.raises(ConfigurationError) as exc_info:
            ConfigLoader.load_yaml(missing_file, required=True)

        assert "not found" in str(exc_info.value)
        assert exc_info.value.path == missing_file

    def test_load_optional_missing_file_returns_none(self, tmp_path: Path):
        """Test that missing optional file returns None."""
        missing_file = tmp_path / "nonexistent.yaml"

        result = ConfigLoader.load_yaml(missing_file, required=False)

        assert result is None

    def test_load_invalid_yaml_raises_error(self, tmp_path: Path):
        """Test that invalid YAML raises ConfigurationError."""
        invalid_file = tmp_path / "invalid.yaml"
        invalid_file.write_text("key: [unclosed bracket")

        with pytest.raises(ConfigurationError) as exc_info:
            ConfigLoader.load_yaml(invalid_file)

        assert "Invalid YAML" in str(exc_info.value)

    def test_load_yaml_accepts_string_path(self, tmp_path: Path):
        """Test that load_yaml accepts string paths."""
        config_file = tmp_path / "config.yaml"
        config_file.write_text("key: value\n")

        result = ConfigLoader.load_yaml(str(config_file))

        assert result == {"key": "value"}


class TestLoadYamlWithDefaults:
    """Tests for ConfigLoader.load_yaml_with_defaults()"""

    def test_file_values_override_defaults(self, tmp_path: Path):
        """Test that file values override default values."""
        config_file = tmp_path / "config.yaml"
        config_file.write_text("timeout: 60\n")

        defaults = {"timeout": 30, "retries": 3}
        result = ConfigLoader.load_yaml_with_defaults(config_file, defaults)

        assert result == {"timeout": 60, "retries": 3}

    def test_missing_optional_file_returns_defaults(self, tmp_path: Path):
        """Test that missing optional file returns only defaults."""
        missing_file = tmp_path / "nonexistent.yaml"
        defaults = {"timeout": 30, "retries": 3}

        result = ConfigLoader.load_yaml_with_defaults(
            missing_file, defaults, required=False
        )

        assert result == defaults

    def test_missing_required_file_raises_error(self, tmp_path: Path):
        """Test that missing required file raises ConfigurationError."""
        missing_file = tmp_path / "nonexistent.yaml"
        defaults = {"timeout": 30}

        with pytest.raises(ConfigurationError):
            ConfigLoader.load_yaml_with_defaults(
                missing_file, defaults, required=True
            )

    def test_empty_file_returns_defaults(self, tmp_path: Path):
        """Test that empty file returns only defaults."""
        empty_file = tmp_path / "empty.yaml"
        empty_file.write_text("")
        defaults = {"timeout": 30}

        result = ConfigLoader.load_yaml_with_defaults(empty_file, defaults)

        assert result == defaults

    def test_defaults_not_mutated(self, tmp_path: Path):
        """Test that original defaults dict is not mutated."""
        config_file = tmp_path / "config.yaml"
        config_file.write_text("new_key: new_value\n")
        defaults = {"timeout": 30}
        original_defaults = defaults.copy()

        ConfigLoader.load_yaml_with_defaults(config_file, defaults)

        assert defaults == original_defaults


class TestLoadFrontmatter:
    """Tests for ConfigLoader.load_frontmatter()"""

    def test_extract_valid_frontmatter(self, tmp_path: Path):
        """Test extracting valid YAML frontmatter from markdown."""
        md_file = tmp_path / "skill.md"
        md_file.write_text("""---
name: test-skill
version: 1.0.0
description: A test skill
---

# Test Skill

This is the content.
""")

        result = ConfigLoader.load_frontmatter(md_file)

        assert result == {
            "name": "test-skill",
            "version": "1.0.0",
            "description": "A test skill"
        }

    def test_no_frontmatter_returns_none(self, tmp_path: Path):
        """Test that file without frontmatter returns None."""
        md_file = tmp_path / "no_frontmatter.md"
        md_file.write_text("# Just Content\n\nNo frontmatter here.")

        result = ConfigLoader.load_frontmatter(md_file)

        assert result is None

    def test_unclosed_frontmatter_returns_none(self, tmp_path: Path):
        """Test that unclosed frontmatter delimiter returns None."""
        md_file = tmp_path / "unclosed.md"
        md_file.write_text("""---
name: test
# Missing closing delimiter

Content here.
""")

        result = ConfigLoader.load_frontmatter(md_file)

        assert result is None

    def test_missing_file_returns_none(self, tmp_path: Path):
        """Test that missing file returns None."""
        missing_file = tmp_path / "nonexistent.md"

        result = ConfigLoader.load_frontmatter(missing_file)

        assert result is None

    def test_invalid_frontmatter_yaml_raises_error(self, tmp_path: Path):
        """Test that invalid YAML in frontmatter raises ConfigurationError."""
        md_file = tmp_path / "invalid.md"
        md_file.write_text("""---
name: [unclosed
---

Content.
""")

        with pytest.raises(ConfigurationError) as exc_info:
            ConfigLoader.load_frontmatter(md_file)

        assert "Invalid YAML frontmatter" in str(exc_info.value)


class TestValidateRequiredFields:
    """Tests for ConfigLoader.validate_required_fields()"""

    def test_all_required_fields_present(self):
        """Test validation passes when all required fields are present."""
        config = {"name": "test", "version": "1.0.0", "description": "desc"}
        required = ["name", "version"]

        # Should not raise
        ConfigLoader.validate_required_fields(config, required)

    def test_missing_required_fields_raises_error(self):
        """Test validation fails when required fields are missing."""
        config = {"name": "test"}
        required = ["name", "version", "description"]

        with pytest.raises(ConfigurationError) as exc_info:
            ConfigLoader.validate_required_fields(config, required)

        error_msg = str(exc_info.value)
        assert "version" in error_msg
        assert "description" in error_msg

    def test_empty_required_list_always_passes(self):
        """Test validation passes with empty required list."""
        config = {}
        required = []

        # Should not raise
        ConfigLoader.validate_required_fields(config, required)

    def test_custom_context_in_error_message(self):
        """Test custom context appears in error message."""
        config = {}
        required = ["field"]
        context = "skill configuration"

        with pytest.raises(ConfigurationError) as exc_info:
            ConfigLoader.validate_required_fields(config, required, context)

        assert "skill configuration" in str(exc_info.value)


class TestConfigurationError:
    """Tests for ConfigurationError exception."""

    def test_error_stores_path(self):
        """Test that ConfigurationError stores the path."""
        path = Path("/some/config.yaml")
        error = ConfigurationError("Error message", path=path)

        assert error.path == path
        assert "Error message" in str(error)

    def test_error_without_path(self):
        """Test ConfigurationError works without path."""
        error = ConfigurationError("Error message")

        assert error.path is None
        assert "Error message" in str(error)
