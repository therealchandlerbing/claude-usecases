"""
Unit tests for skill structure validation script.

Tests the validate_skill_structure.py script to ensure it correctly
validates skill directory structure and frontmatter.
"""

import os
import tempfile
from pathlib import Path

import pytest

# Import yaml with guard to prevent CI failures
try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

# Skip all tests in this module if yaml is not available
pytestmark = pytest.mark.skipif(
    yaml is None,
    reason="PyYAML not installed - skipping yaml-dependent tests"
)

# Add scripts directory to path
import sys
scripts_dir = Path(__file__).parent.parent.parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

# Guard the import - validate_skill_structure.py calls sys.exit(2) if yaml is missing
# which would kill pytest during test collection. We need to prevent that.
if yaml is not None:
    from validate_skill_structure import (
        SkillStructureValidator,
        ValidationResult,
        SkillValidationSummary
    )
else:
    # Provide dummy classes so module can load (tests will be skipped anyway)
    SkillStructureValidator = None  # type: ignore
    ValidationResult = None  # type: ignore
    SkillValidationSummary = None  # type: ignore


@pytest.fixture
def temp_project_root(tmp_path):
    """Create a temporary project structure."""
    # Create directory structure
    (tmp_path / "skills").mkdir()
    (tmp_path / ".claude" / "skills").mkdir(parents=True)
    (tmp_path / "config").mkdir()

    return tmp_path


@pytest.fixture
def sample_config(temp_project_root):
    """Create a sample configuration file."""
    config = {
        'settings': {
            'skill_directories': ['skills/', '.claude/skills/'],
            'exclude_directories': ['skills/templates', '*/__pycache__'],
            'enable_frontmatter_validation': True,
            'enable_file_presence_validation': True,
            'enable_content_validation': False
        },
        'managed_skills': {
            'required_files': [
                {
                    'name': 'SKILL.md',
                    'description': 'Main operational logic',
                    'validation': [{'check_frontmatter': True, 'min_size_bytes': 100}]
                },
                {
                    'name': 'README.md',
                    'description': 'User documentation',
                    'validation': [{'min_size_bytes': 50}]
                }
            ],
            'recommended_files': [
                {'name': 'QUICK-START.md', 'description': 'Quick reference'}
            ],
            'required_frontmatter': [
                {'field': 'name', 'type': 'string'},
                {'field': 'description', 'type': 'string', 'min_length': 10},
                {'field': 'version', 'type': 'string', 'pattern': r'^\d+\.\d+\.\d+$'}
            ],
            'recommended_frontmatter': [
                {'field': 'author', 'type': 'string'},
                {'field': 'category', 'type': 'string'}
            ]
        },
        'user_skills': {
            'required_files': [
                {
                    'name': 'SKILL.md',
                    'description': 'Main operational logic',
                    'validation': [{'check_frontmatter': True, 'min_size_bytes': 50}]
                }
            ],
            'recommended_files': [
                {'name': 'README.md', 'description': 'Documentation'}
            ],
            'required_frontmatter': [
                {'field': 'name', 'type': 'string'},
                {'field': 'description', 'type': 'string', 'min_length': 5}
            ],
            'recommended_frontmatter': [
                {'field': 'version', 'type': 'string'}
            ]
        },
        'error_messages': {
            'missing_required_file': '❌ Required file \'{file}\' is missing in skill \'{skill}\'',
            'missing_frontmatter': '❌ Required frontmatter field \'{field}\' is missing in {skill}/SKILL.md',
            'invalid_frontmatter': '❌ Frontmatter field \'{field}\' in {skill}/SKILL.md: {error}',
            'file_too_small': '⚠️  File \'{file}\' in skill \'{skill}\' is only {size} bytes (minimum: {min_size})',
            'invalid_yaml': '❌ Invalid YAML frontmatter in {skill}/SKILL.md: {error}'
        },
        'success_messages': {
            'skill_valid': '✅ Skill \'{skill}\' structure is valid',
            'all_valid': '✅ All {count} skills have valid structure'
        },
        'warning_messages': {
            'missing_recommended_file': '⚠️  Recommended file \'{file}\' is missing in skill \'{skill}\'',
            'missing_recommended_frontmatter': '⚠️  Recommended frontmatter field \'{field}\' is missing in {skill}/SKILL.md'
        }
    }

    config_path = temp_project_root / "config" / "skill-structure-requirements.yaml"
    with open(config_path, 'w') as f:
        yaml.dump(config, f)

    return config_path


@pytest.fixture
def validator(sample_config, temp_project_root, monkeypatch):
    """Create a validator instance with sample config."""
    # Monkeypatch the _find_project_root method to return our temp directory
    def mock_find_project_root(self):
        return temp_project_root

    monkeypatch.setattr(
        SkillStructureValidator,
        '_find_project_root',
        mock_find_project_root
    )

    return SkillStructureValidator(config_path=str(sample_config), verbose=False)


def create_skill(
    skill_path: Path,
    include_skill_md: bool = True,
    include_readme: bool = True,
    frontmatter: dict = None,
    skill_md_size: int = 200,
    readme_size: int = 100
):
    """
    Helper function to create a skill directory with files.

    Args:
        skill_path: Path to skill directory
        include_skill_md: Whether to create SKILL.md
        include_readme: Whether to create README.md
        frontmatter: Dictionary of frontmatter fields
        skill_md_size: Size of SKILL.md content
        readme_size: Size of README.md content
    """
    skill_path.mkdir(parents=True, exist_ok=True)

    if include_skill_md:
        content = ""

        if frontmatter:
            fm_yaml = yaml.dump(frontmatter)
            content = f"---\n{fm_yaml}---\n\n"

        # Pad to minimum size
        content += "# Skill Documentation\n\n"
        content += "This is a test skill. " * (skill_md_size // 20)

        (skill_path / "SKILL.md").write_text(content)

    if include_readme:
        readme_content = "# README\n\n" + ("Test content. " * (readme_size // 10))
        (skill_path / "README.md").write_text(readme_content)


class TestSkillStructureValidator:
    """Test suite for SkillStructureValidator."""

    def test_load_config(self, validator):
        """Test that configuration is loaded correctly."""
        assert validator.config is not None
        assert 'settings' in validator.config
        assert 'managed_skills' in validator.config
        assert 'user_skills' in validator.config

    def test_find_skills_in_directory(self, validator, temp_project_root):
        """Test finding skills in a directory."""
        # Create some test skills
        (temp_project_root / "skills" / "test-skill-1").mkdir(parents=True)
        (temp_project_root / "skills" / "test-skill-2").mkdir(parents=True)
        (temp_project_root / "skills" / "templates").mkdir(parents=True)  # Should be excluded

        skills = validator._find_skills("skills/")

        assert len(skills) == 2
        skill_names = [s.name for s in skills]
        assert "test-skill-1" in skill_names
        assert "test-skill-2" in skill_names
        assert "templates" not in skill_names  # Excluded

    def test_extract_frontmatter_valid(self, validator, temp_project_root):
        """Test extracting valid YAML frontmatter."""
        skill_path = temp_project_root / "skills" / "test-skill"
        frontmatter = {
            'name': 'test-skill',
            'description': 'A test skill for validation',
            'version': '1.0.0'
        }

        create_skill(skill_path, frontmatter=frontmatter)

        extracted = validator._extract_frontmatter(skill_path / "SKILL.md")

        assert extracted is not None
        assert extracted['name'] == 'test-skill'
        assert extracted['description'] == 'A test skill for validation'
        assert extracted['version'] == '1.0.0'

    def test_extract_frontmatter_missing(self, validator, temp_project_root):
        """Test extracting frontmatter when it's missing."""
        skill_path = temp_project_root / "skills" / "test-skill"
        create_skill(skill_path, frontmatter=None)

        extracted = validator._extract_frontmatter(skill_path / "SKILL.md")

        assert extracted is None

    def test_validate_file_presence_all_present(self, validator, temp_project_root):
        """Test file presence validation when all files are present."""
        skill_path = temp_project_root / ".claude" / "skills" / "test-skill"
        create_skill(skill_path, include_skill_md=True, include_readme=True)

        required_files = [
            {'name': 'SKILL.md', 'validation': []},
            {'name': 'README.md', 'validation': []}
        ]

        results = validator._validate_file_presence(skill_path, required_files, "managed")

        assert len(results) == 0  # No errors

    def test_validate_file_presence_missing_file(self, validator, temp_project_root):
        """Test file presence validation when a file is missing."""
        skill_path = temp_project_root / ".claude" / "skills" / "test-skill"
        create_skill(skill_path, include_skill_md=True, include_readme=False)

        required_files = [
            {'name': 'SKILL.md', 'validation': []},
            {'name': 'README.md', 'validation': []}
        ]

        results = validator._validate_file_presence(skill_path, required_files, "managed")

        assert len(results) == 1
        assert results[0].severity == "error"
        assert "README.md" in results[0].message
        assert "missing" in results[0].message.lower()

    def test_validate_file_size_too_small(self, validator, temp_project_root):
        """Test file size validation when file is too small."""
        skill_path = temp_project_root / ".claude" / "skills" / "test-skill"
        create_skill(skill_path, skill_md_size=50)  # Below minimum

        required_files = [
            {
                'name': 'SKILL.md',
                'validation': [{'min_size_bytes': 100}]
            }
        ]

        results = validator._validate_file_presence(skill_path, required_files, "managed")

        # Should have a warning about file size
        size_warnings = [r for r in results if "bytes" in r.message]
        assert len(size_warnings) == 1
        assert size_warnings[0].severity == "warning"

    def test_validate_frontmatter_valid(self, validator, temp_project_root):
        """Test frontmatter validation with valid data."""
        skill_path = temp_project_root / ".claude" / "skills" / "test-skill"
        frontmatter = {
            'name': 'test-skill',
            'description': 'A comprehensive test skill',
            'version': '1.0.0',
            'author': 'Test Author'
        }

        create_skill(skill_path, frontmatter=frontmatter)

        required_fields = [
            {'field': 'name', 'type': 'string'},
            {'field': 'description', 'type': 'string', 'min_length': 10},
            {'field': 'version', 'type': 'string', 'pattern': r'^\d+\.\d+\.\d+$'}
        ]

        recommended_fields = [
            {'field': 'author', 'type': 'string'}
        ]

        results = validator._validate_frontmatter(
            skill_path, required_fields, recommended_fields, "managed"
        )

        # Should have no errors (author is present, so no warnings either)
        errors = [r for r in results if r.severity == "error"]
        assert len(errors) == 0

    def test_validate_frontmatter_missing_required_field(self, validator, temp_project_root):
        """Test frontmatter validation with missing required field."""
        skill_path = temp_project_root / ".claude" / "skills" / "test-skill"
        frontmatter = {
            'name': 'test-skill',
            # Missing 'description'
            'version': '1.0.0'
        }

        create_skill(skill_path, frontmatter=frontmatter)

        required_fields = [
            {'field': 'name', 'type': 'string'},
            {'field': 'description', 'type': 'string', 'min_length': 10},
            {'field': 'version', 'type': 'string'}
        ]

        results = validator._validate_frontmatter(
            skill_path, required_fields, [], "managed"
        )

        errors = [r for r in results if r.severity == "error"]
        assert len(errors) == 1
        assert "description" in errors[0].message
        assert "missing" in errors[0].message.lower()

    def test_validate_frontmatter_invalid_pattern(self, validator, temp_project_root):
        """Test frontmatter validation with invalid version pattern."""
        skill_path = temp_project_root / ".claude" / "skills" / "test-skill"
        frontmatter = {
            'name': 'test-skill',
            'description': 'A test skill',
            'version': 'v1.0'  # Invalid pattern
        }

        create_skill(skill_path, frontmatter=frontmatter)

        required_fields = [
            {'field': 'name', 'type': 'string'},
            {'field': 'description', 'type': 'string'},
            {'field': 'version', 'type': 'string', 'pattern': r'^\d+\.\d+\.\d+$'}
        ]

        results = validator._validate_frontmatter(
            skill_path, required_fields, [], "managed"
        )

        errors = [r for r in results if r.severity == "error"]
        assert len(errors) == 1
        assert "version" in errors[0].message
        assert "pattern" in errors[0].message.lower()

    def test_validate_frontmatter_description_too_short(self, validator, temp_project_root):
        """Test frontmatter validation with description below minimum length."""
        skill_path = temp_project_root / ".claude" / "skills" / "test-skill"
        frontmatter = {
            'name': 'test-skill',
            'description': 'Short',  # Too short
            'version': '1.0.0'
        }

        create_skill(skill_path, frontmatter=frontmatter)

        required_fields = [
            {'field': 'name', 'type': 'string'},
            {'field': 'description', 'type': 'string', 'min_length': 10},
            {'field': 'version', 'type': 'string'}
        ]

        results = validator._validate_frontmatter(
            skill_path, required_fields, [], "managed"
        )

        errors = [r for r in results if r.severity == "error"]
        assert len(errors) == 1
        assert "description" in errors[0].message
        assert "length" in errors[0].message.lower()

    def test_validate_skill_complete_valid(self, validator, temp_project_root):
        """Test complete skill validation with valid skill."""
        skill_path = temp_project_root / ".claude" / "skills" / "test-skill"
        frontmatter = {
            'name': 'test-skill',
            'description': 'A comprehensive test skill for validation',
            'version': '1.0.0',
            'author': 'Test Author',
            'category': 'testing'
        }

        create_skill(
            skill_path,
            frontmatter=frontmatter,
            skill_md_size=200,
            readme_size=100
        )

        summary = validator.validate_skill(skill_path, "managed")

        assert summary.is_valid
        assert len(summary.errors) == 0
        assert summary.skill_name == "test-skill"
        assert summary.skill_type == "managed"

    def test_validate_skill_multiple_errors(self, validator, temp_project_root):
        """Test skill validation with multiple errors."""
        skill_path = temp_project_root / ".claude" / "skills" / "test-skill"
        frontmatter = {
            'name': 'test-skill',
            # Missing description
            'version': 'invalid'  # Invalid pattern
        }

        create_skill(
            skill_path,
            frontmatter=frontmatter,
            include_readme=False  # Missing README.md
        )

        summary = validator.validate_skill(skill_path, "managed")

        assert not summary.is_valid
        assert len(summary.errors) >= 2  # Missing README + frontmatter errors

        error_messages = [e.message for e in summary.errors]
        assert any("README.md" in msg for msg in error_messages)
        assert any("description" in msg for msg in error_messages)

    def test_validate_all_skills(self, validator, temp_project_root):
        """Test validating all skills in repository."""
        # Create valid managed skill
        managed_skill = temp_project_root / ".claude" / "skills" / "managed-skill"
        create_skill(
            managed_skill,
            frontmatter={
                'name': 'managed-skill',
                'description': 'A managed skill for testing',
                'version': '1.0.0'
            }
        )

        # Create valid user skill
        user_skill = temp_project_root / "skills" / "user-skill"
        create_skill(
            user_skill,
            frontmatter={
                'name': 'user-skill',
                'description': 'A user skill',
            },
            include_readme=False  # Not required for user skills
        )

        # Create invalid skill (missing files)
        invalid_skill = temp_project_root / "skills" / "invalid-skill"
        invalid_skill.mkdir(parents=True)

        summaries = validator.validate_all()

        assert len(summaries) == 3

        # Check managed skill is valid
        managed_summary = next(s for s in summaries if s.skill_name == "managed-skill")
        assert managed_summary.is_valid
        assert managed_summary.skill_type == "managed"

        # Check user skill is valid
        user_summary = next(s for s in summaries if s.skill_name == "user-skill")
        assert user_summary.is_valid
        assert user_summary.skill_type == "user"

        # Check invalid skill has errors
        invalid_summary = next(s for s in summaries if s.skill_name == "invalid-skill")
        assert not invalid_summary.is_valid
        assert len(invalid_summary.errors) > 0


@pytest.mark.unit
class TestValidationResult:
    """Test ValidationResult dataclass."""

    def test_create_validation_result(self):
        """Test creating a ValidationResult."""
        result = ValidationResult(
            skill_name="test-skill",
            check_type="file_presence",
            severity="error",
            message="Test error message",
            file_path="/path/to/file"
        )

        assert result.skill_name == "test-skill"
        assert result.check_type == "file_presence"
        assert result.severity == "error"
        assert result.message == "Test error message"
        assert result.file_path == "/path/to/file"


@pytest.mark.unit
class TestSkillValidationSummary:
    """Test SkillValidationSummary dataclass."""

    def test_is_valid_no_errors(self):
        """Test is_valid returns True when no errors."""
        summary = SkillValidationSummary(
            skill_name="test-skill",
            skill_path="/path/to/skill",
            skill_type="managed"
        )

        assert summary.is_valid

    def test_is_valid_with_errors(self):
        """Test is_valid returns False when errors exist."""
        summary = SkillValidationSummary(
            skill_name="test-skill",
            skill_path="/path/to/skill",
            skill_type="managed",
            errors=[
                ValidationResult(
                    skill_name="test-skill",
                    check_type="file",
                    severity="error",
                    message="Error"
                )
            ]
        )

        assert not summary.is_valid

    def test_total_issues(self):
        """Test total_issues calculation."""
        summary = SkillValidationSummary(
            skill_name="test-skill",
            skill_path="/path/to/skill",
            skill_type="managed",
            errors=[
                ValidationResult("test", "file", "error", "Error 1"),
                ValidationResult("test", "file", "error", "Error 2")
            ],
            warnings=[
                ValidationResult("test", "file", "warning", "Warning 1")
            ]
        )

        assert summary.total_issues == 3
