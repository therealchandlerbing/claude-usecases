#!/usr/bin/env python3
"""
Skill Structure Validation Script

Validates that all Claude skills follow the expected directory structure
and include required files with proper frontmatter.

Usage:
    python scripts/validate_skill_structure.py [--config CONFIG] [--verbose]

Exit codes:
    0 - All validations passed
    1 - Validation failures found
    2 - Script error (e.g., config file not found)
"""

import argparse
import fnmatch
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set

try:
    import yaml
except ImportError:
    print("❌ Error: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(2)


@dataclass
class ValidationResult:
    """Result of a single validation check."""
    skill_name: str
    check_type: str
    severity: str  # "error", "warning", "info"
    message: str
    file_path: Optional[str] = None


@dataclass
class SkillValidationSummary:
    """Summary of validation results for a skill."""
    skill_name: str
    skill_path: str
    skill_type: str  # "managed" or "user"
    errors: List[ValidationResult] = field(default_factory=list)
    warnings: List[ValidationResult] = field(default_factory=list)
    info: List[ValidationResult] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        """Returns True if no errors were found."""
        return len(self.errors) == 0

    @property
    def total_issues(self) -> int:
        """Total number of issues (errors + warnings)."""
        return len(self.errors) + len(self.warnings)


class SkillStructureValidator:
    """Validates Claude skill directory structure."""

    def __init__(self, config_path: str, verbose: bool = False):
        """
        Initialize validator with configuration.

        Args:
            config_path: Path to YAML configuration file
            verbose: Enable verbose output
        """
        self.config_path = Path(config_path)
        self.verbose = verbose
        self.config = self._load_config()
        self.project_root = self._find_project_root()

    def _find_project_root(self) -> Path:
        """Find the project root directory."""
        # Assume script is in scripts/ directory
        script_dir = Path(__file__).parent
        return script_dir.parent

    def _load_config(self) -> Dict:
        """Load and parse configuration file."""
        try:
            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)
            return config
        except FileNotFoundError:
            print(f"❌ Error: Configuration file not found: {self.config_path}")
            sys.exit(2)
        except yaml.YAMLError as e:
            print(f"❌ Error: Invalid YAML in configuration file: {e}")
            sys.exit(2)

    def _should_exclude(self, path: Path) -> bool:
        """Check if path matches any exclude pattern."""
        exclude_patterns = self.config['settings'].get('exclude_directories', [])
        path_str = str(path)

        for pattern in exclude_patterns:
            if fnmatch.fnmatch(path_str, f"*{pattern}*"):
                return True
        return False

    def _find_skills(self, directory: str) -> List[Path]:
        """
        Find all skill directories in the given directory.

        Args:
            directory: Directory to search (e.g., "skills/", ".claude/skills/")

        Returns:
            List of skill directory paths
        """
        skills = []
        skill_dir = self.project_root / directory

        if not skill_dir.exists():
            if self.verbose:
                print(f"⚠️  Directory not found: {skill_dir}")
            return skills

        for item in skill_dir.iterdir():
            if item.is_dir() and not self._should_exclude(item):
                skills.append(item)

        return skills

    def _extract_frontmatter(self, skill_md_path: Path) -> Optional[Dict]:
        """
        Extract YAML frontmatter from SKILL.md file.

        Args:
            skill_md_path: Path to SKILL.md file

        Returns:
            Dictionary of frontmatter fields or None if not found/invalid
        """
        try:
            with open(skill_md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Match YAML frontmatter (between --- markers)
            pattern = r'^---\s*\n(.*?)\n---\s*\n'
            match = re.match(pattern, content, re.DOTALL)

            if not match:
                return None

            frontmatter_yaml = match.group(1)
            frontmatter = yaml.safe_load(frontmatter_yaml)

            return frontmatter if isinstance(frontmatter, dict) else None

        except Exception as e:
            if self.verbose:
                print(f"⚠️  Error extracting frontmatter from {skill_md_path}: {e}")
            return None

    def _validate_file_presence(
        self,
        skill_path: Path,
        required_files: List[Dict],
        skill_type: str
    ) -> List[ValidationResult]:
        """
        Validate that required files are present.

        Args:
            skill_path: Path to skill directory
            required_files: List of required file configurations
            skill_type: "managed" or "user"

        Returns:
            List of validation results
        """
        results = []
        skill_name = skill_path.name

        for file_config in required_files:
            file_name = file_config['name']
            file_path = skill_path / file_name

            if not file_path.exists():
                msg = self.config['error_messages']['missing_required_file'].format(
                    file=file_name,
                    skill=skill_name
                )
                results.append(ValidationResult(
                    skill_name=skill_name,
                    check_type="file_presence",
                    severity="error",
                    message=msg,
                    file_path=str(file_path)
                ))
                continue

            # Check file size if specified
            validation = file_config.get('validation', [])
            for check in validation:
                if 'min_size_bytes' in check:
                    min_size = check['min_size_bytes']
                    actual_size = file_path.stat().st_size

                    if actual_size < min_size:
                        msg = self.config['error_messages']['file_too_small'].format(
                            file=file_name,
                            skill=skill_name,
                            size=actual_size,
                            min_size=min_size
                        )
                        # File too small is a warning, not an error
                        results.append(ValidationResult(
                            skill_name=skill_name,
                            check_type="file_size",
                            severity="warning",
                            message=msg,
                            file_path=str(file_path)
                        ))

        return results

    def _validate_recommended_files(
        self,
        skill_path: Path,
        recommended_files: List[Dict]
    ) -> List[ValidationResult]:
        """
        Check for recommended but not required files.

        Args:
            skill_path: Path to skill directory
            recommended_files: List of recommended file configurations

        Returns:
            List of validation results (warnings)
        """
        results = []
        skill_name = skill_path.name

        for file_config in recommended_files:
            file_name = file_config['name']
            file_path = skill_path / file_name

            if not file_path.exists():
                msg = self.config['warning_messages']['missing_recommended_file'].format(
                    file=file_name,
                    skill=skill_name
                )
                results.append(ValidationResult(
                    skill_name=skill_name,
                    check_type="recommended_file",
                    severity="warning",
                    message=msg,
                    file_path=str(file_path)
                ))

        return results

    def _validate_frontmatter_field(
        self,
        skill_name: str,
        field_config: Dict,
        frontmatter: Dict
    ) -> Optional[ValidationResult]:
        """
        Validate a single frontmatter field.

        Args:
            skill_name: Name of the skill
            field_config: Field configuration from config file
            frontmatter: Extracted frontmatter dictionary

        Returns:
            ValidationResult if validation fails, None otherwise
        """
        field_name = field_config['field']

        # Check if field exists
        if field_name not in frontmatter:
            msg = self.config['error_messages']['missing_frontmatter'].format(
                field=field_name,
                skill=skill_name
            )
            return ValidationResult(
                skill_name=skill_name,
                check_type="frontmatter",
                severity="error",
                message=msg
            )

        field_value = frontmatter[field_name]

        # Validate field type
        expected_type = field_config.get('type', 'string')
        if expected_type == 'string' and not isinstance(field_value, str):
            msg = self.config['error_messages']['invalid_frontmatter'].format(
                field=field_name,
                skill=skill_name,
                error=f"Expected string, got {type(field_value).__name__}"
            )
            return ValidationResult(
                skill_name=skill_name,
                check_type="frontmatter",
                severity="error",
                message=msg
            )

        # Validate minimum length
        if 'min_length' in field_config:
            min_length = field_config['min_length']
            if len(field_value) < min_length:
                msg = self.config['error_messages']['invalid_frontmatter'].format(
                    field=field_name,
                    skill=skill_name,
                    error=f"Length {len(field_value)} < minimum {min_length}"
                )
                return ValidationResult(
                    skill_name=skill_name,
                    check_type="frontmatter",
                    severity="error",
                    message=msg
                )

        # Validate pattern
        if 'pattern' in field_config:
            pattern = field_config['pattern']
            if not re.match(pattern, field_value):
                msg = self.config['error_messages']['invalid_frontmatter'].format(
                    field=field_name,
                    skill=skill_name,
                    error=f"Does not match pattern {pattern}"
                )
                return ValidationResult(
                    skill_name=skill_name,
                    check_type="frontmatter",
                    severity="error",
                    message=msg
                )

        # Validate allowed values
        if 'allowed_values' in field_config:
            allowed = field_config['allowed_values']
            if field_value not in allowed:
                msg = self.config['error_messages']['invalid_frontmatter'].format(
                    field=field_name,
                    skill=skill_name,
                    error=f"Value '{field_value}' not in allowed values: {allowed}"
                )
                return ValidationResult(
                    skill_name=skill_name,
                    check_type="frontmatter",
                    severity="error",
                    message=msg
                )

        return None

    def _validate_frontmatter(
        self,
        skill_path: Path,
        required_fields: List[Dict],
        recommended_fields: List[Dict],
        skill_type: str
    ) -> List[ValidationResult]:
        """
        Validate YAML frontmatter in SKILL.md.

        Args:
            skill_path: Path to skill directory
            required_fields: List of required field configurations
            recommended_fields: List of recommended field configurations
            skill_type: "managed" or "user"

        Returns:
            List of validation results
        """
        results = []
        skill_name = skill_path.name
        skill_md_path = skill_path / "SKILL.md"

        if not skill_md_path.exists():
            # This will be caught by file presence validation
            return results

        frontmatter = self._extract_frontmatter(skill_md_path)

        if frontmatter is None:
            msg = self.config['error_messages']['invalid_yaml'].format(
                skill=skill_name,
                error="No valid YAML frontmatter found"
            )
            results.append(ValidationResult(
                skill_name=skill_name,
                check_type="frontmatter",
                severity="error",
                message=msg,
                file_path=str(skill_md_path)
            ))
            return results

        # Validate required fields
        for field_config in required_fields:
            result = self._validate_frontmatter_field(
                skill_name, field_config, frontmatter
            )
            if result:
                results.append(result)

        # Check recommended fields
        for field_config in recommended_fields:
            field_name = field_config['field']
            if field_name not in frontmatter:
                msg = self.config['warning_messages']['missing_recommended_frontmatter'].format(
                    field=field_name,
                    skill=skill_name
                )
                results.append(ValidationResult(
                    skill_name=skill_name,
                    check_type="frontmatter",
                    severity="info",
                    message=msg
                ))

        return results

    def validate_skill(self, skill_path: Path, skill_type: str) -> SkillValidationSummary:
        """
        Validate a single skill directory.

        Args:
            skill_path: Path to skill directory
            skill_type: "managed" or "user"

        Returns:
            SkillValidationSummary with all validation results
        """
        skill_name = skill_path.name
        summary = SkillValidationSummary(
            skill_name=skill_name,
            skill_path=str(skill_path),
            skill_type=skill_type
        )

        # Get configuration for this skill type
        skill_config = self.config[f'{skill_type}_skills']

        # Validate required files
        if self.config['settings']['enable_file_presence_validation']:
            required_files = skill_config.get('required_files', [])
            file_results = self._validate_file_presence(
                skill_path, required_files, skill_type
            )

            for result in file_results:
                if result.severity == "error":
                    summary.errors.append(result)
                elif result.severity == "warning":
                    summary.warnings.append(result)
                else:
                    summary.info.append(result)

            # Check recommended files
            recommended_files = skill_config.get('recommended_files', [])
            rec_results = self._validate_recommended_files(
                skill_path, recommended_files
            )
            summary.warnings.extend(rec_results)

        # Validate frontmatter
        if self.config['settings']['enable_frontmatter_validation']:
            required_frontmatter = skill_config.get('required_frontmatter', [])
            recommended_frontmatter = skill_config.get('recommended_frontmatter', [])

            fm_results = self._validate_frontmatter(
                skill_path,
                required_frontmatter,
                recommended_frontmatter,
                skill_type
            )

            for result in fm_results:
                if result.severity == "error":
                    summary.errors.append(result)
                elif result.severity == "warning":
                    summary.warnings.append(result)
                else:
                    summary.info.append(result)

        return summary

    def validate_all(self) -> List[SkillValidationSummary]:
        """
        Validate all skills in configured directories.

        Returns:
            List of SkillValidationSummary for each skill
        """
        all_summaries = []

        skill_directories = self.config['settings']['skill_directories']

        for directory in skill_directories:
            # Determine skill type
            skill_type = "managed" if ".claude/skills" in directory else "user"

            # Find all skills in this directory
            skills = self._find_skills(directory)

            if self.verbose:
                print(f"\n🔍 Scanning {directory} ({len(skills)} skills found)")

            for skill_path in skills:
                summary = self.validate_skill(skill_path, skill_type)
                all_summaries.append(summary)

        return all_summaries

    def print_summary(self, summaries: List[SkillValidationSummary]) -> None:
        """
        Print validation summary to console.

        Args:
            summaries: List of validation summaries
        """
        total_skills = len(summaries)
        valid_skills = sum(1 for s in summaries if s.is_valid)
        invalid_skills = total_skills - valid_skills

        total_errors = sum(len(s.errors) for s in summaries)
        total_warnings = sum(len(s.warnings) for s in summaries)

        print("\n" + "=" * 70)
        print("SKILL STRUCTURE VALIDATION SUMMARY")
        print("=" * 70)

        # Print invalid skills first
        if invalid_skills > 0:
            print(f"\n❌ {invalid_skills} skill(s) with errors:\n")

            for summary in summaries:
                if not summary.is_valid:
                    print(f"  📁 {summary.skill_name} ({summary.skill_type})")

                    # Print errors
                    for error in summary.errors:
                        print(f"     {error.message}")

                    # Print warnings if verbose
                    if self.verbose and summary.warnings:
                        for warning in summary.warnings:
                            print(f"     {warning.message}")

                    print()

        # Print valid skills if verbose
        if self.verbose and valid_skills > 0:
            print(f"\n✅ {valid_skills} skill(s) with valid structure:\n")
            for summary in summaries:
                if summary.is_valid:
                    msg = self.config['success_messages']['skill_valid'].format(
                        skill=summary.skill_name
                    )
                    print(f"  {msg}")

                    # Print warnings
                    if summary.warnings:
                        for warning in summary.warnings:
                            print(f"     {warning.message}")

        # Overall summary
        print("\n" + "-" * 70)
        print(f"Total skills validated: {total_skills}")
        print(f"  ✅ Valid: {valid_skills}")
        print(f"  ❌ Invalid: {invalid_skills}")
        print(f"  🔴 Total errors: {total_errors}")
        print(f"  ⚠️  Total warnings: {total_warnings}")
        print("-" * 70)

        if invalid_skills == 0:
            msg = self.config['success_messages']['all_valid'].format(
                count=total_skills
            )
            print(f"\n{msg}\n")
        else:
            print(f"\n❌ Validation failed: {invalid_skills} skill(s) have structural errors\n")


def main():
    """Main entry point for the validation script."""
    parser = argparse.ArgumentParser(
        description="Validate Claude skill directory structure"
    )
    parser.add_argument(
        '--config',
        default='config/skill-structure-requirements.yaml',
        help='Path to configuration file (default: config/skill-structure-requirements.yaml)'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    # Initialize validator
    validator = SkillStructureValidator(
        config_path=args.config,
        verbose=args.verbose
    )

    # Run validation
    summaries = validator.validate_all()

    # Print results
    validator.print_summary(summaries)

    # Exit with appropriate code
    invalid_count = sum(1 for s in summaries if not s.is_valid)
    sys.exit(1 if invalid_count > 0 else 0)


if __name__ == '__main__':
    main()
