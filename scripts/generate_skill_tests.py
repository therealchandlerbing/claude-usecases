#!/usr/bin/env python3
"""
Skill Test Template Generator

Generates pytest test scaffolding for skills based on their SKILL.md structure.
Accelerates test coverage expansion by providing ready-to-fill test templates.

Usage:
    # Generate tests for a specific skill
    python scripts/generate_skill_tests.py --skill ceo-advisor

    # Generate tests for all untested skills
    python scripts/generate_skill_tests.py --all

    # Dry run (show what would be generated)
    python scripts/generate_skill_tests.py --skill ceo-advisor --dry-run

    # Specify output directory
    python scripts/generate_skill_tests.py --skill ceo-advisor --output tests/unit/python/
"""

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set

try:
    import yaml
except ImportError:
    yaml = None


@dataclass
class SkillCapability:
    """Represents a capability/phase of a skill."""
    name: str
    description: str = ""
    methods: List[str] = field(default_factory=list)


@dataclass
class SkillInfo:
    """Information extracted from a skill's SKILL.md."""
    name: str
    version: str
    description: str
    path: Path
    capabilities: List[SkillCapability] = field(default_factory=list)
    has_python_src: bool = False
    python_classes: List[str] = field(default_factory=list)
    category: str = "general"


def find_project_root() -> Path:
    """Find the project root directory."""
    script_dir = Path(__file__).parent
    return script_dir.parent


def extract_frontmatter(content: str) -> Optional[Dict]:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return None

    end_match = content.find("\n---", 3)
    if end_match == -1:
        return None

    frontmatter_text = content[3:end_match].strip()

    if yaml:
        try:
            return yaml.safe_load(frontmatter_text)
        except yaml.YAMLError:
            return None
    return None


def extract_capabilities(content: str) -> List[SkillCapability]:
    """Extract capabilities/phases from SKILL.md content."""
    capabilities = []

    # Pattern 1: Look for ## Phase N: or ## Capability: headers
    phase_pattern = r"##\s+(?:Phase\s+\d+[:\s]+|Capability[:\s]+)([^\n]+)"
    for match in re.finditer(phase_pattern, content, re.IGNORECASE):
        name = match.group(1).strip()
        capabilities.append(SkillCapability(name=name))

    # Pattern 2: Look for numbered workflow steps
    if not capabilities:
        step_pattern = r"^\d+\.\s+\*\*([^*]+)\*\*"
        for match in re.finditer(step_pattern, content, re.MULTILINE):
            name = match.group(1).strip()
            if len(name) > 5 and len(name) < 60:  # Reasonable step name
                capabilities.append(SkillCapability(name=name))

    # Pattern 3: Look for key workflow sections
    if not capabilities:
        section_pattern = r"###\s+([A-Z][^\n]+)"
        for match in re.finditer(section_pattern, content):
            name = match.group(1).strip()
            # Filter out common non-capability sections
            if name.lower() not in ["usage", "configuration", "examples", "troubleshooting",
                                     "prerequisites", "installation", "quick start"]:
                capabilities.append(SkillCapability(name=name))

    return capabilities[:10]  # Limit to 10 capabilities


def find_python_classes(skill_path: Path) -> List[str]:
    """Find Python class names in skill source directory."""
    classes = []
    src_dir = skill_path / "src"

    if not src_dir.exists():
        return classes

    for py_file in src_dir.glob("*.py"):
        try:
            content = py_file.read_text()
            # Find class definitions
            class_pattern = r"^class\s+(\w+)"
            for match in re.finditer(class_pattern, content, re.MULTILINE):
                classes.append(match.group(1))
        except (IOError, UnicodeDecodeError):
            pass

    return classes


def analyze_skill(skill_path: Path) -> Optional[SkillInfo]:
    """Analyze a skill directory and extract information."""
    skill_md = skill_path / "SKILL.md"

    if not skill_md.exists():
        return None

    try:
        content = skill_md.read_text()
    except (IOError, UnicodeDecodeError):
        return None

    # Extract frontmatter
    frontmatter = extract_frontmatter(content) or {}

    name = frontmatter.get("name", skill_path.name)
    version = frontmatter.get("version", "1.0.0")
    description = frontmatter.get("description", "")
    category = frontmatter.get("category", "general")

    # Extract capabilities
    capabilities = extract_capabilities(content)

    # Find Python classes
    python_classes = find_python_classes(skill_path)

    return SkillInfo(
        name=name,
        version=version,
        description=description,
        path=skill_path,
        capabilities=capabilities,
        has_python_src=(skill_path / "src").exists(),
        python_classes=python_classes,
        category=category
    )


def get_existing_tests(project_root: Path) -> Set[str]:
    """Get set of skills that already have test files."""
    tested_skills = set()
    test_dir = project_root / "tests" / "unit" / "python"

    if not test_dir.exists():
        return tested_skills

    for test_file in test_dir.glob("test_*.py"):
        # Extract skill name from test file name
        # e.g., test_990_orchestrator.py -> 990-ez-preparation
        # e.g., test_ceo_advisor.py -> ceo-advisor
        name = test_file.stem.replace("test_", "").replace("_", "-")
        tested_skills.add(name)

    # Also check subdirectories
    for subdir in test_dir.iterdir():
        if subdir.is_dir() and not subdir.name.startswith("__"):
            tested_skills.add(subdir.name.replace("_", "-"))

    return tested_skills


def sanitize_name(name: str) -> str:
    """Convert a name to a valid Python identifier."""
    # Replace hyphens and spaces with underscores
    result = re.sub(r"[-\s]+", "_", name)
    # Remove non-alphanumeric characters (except underscores)
    result = re.sub(r"[^\w]", "", result)
    # Ensure it starts with a letter
    if result and result[0].isdigit():
        result = "test_" + result
    return result.lower()


def generate_test_template(skill_info: SkillInfo) -> str:
    """Generate pytest test template for a skill."""
    skill_name_snake = sanitize_name(skill_info.name)

    # Determine test class names
    if skill_info.python_classes:
        primary_class = skill_info.python_classes[0]
    else:
        primary_class = "".join(word.title() for word in skill_info.name.split("-"))

    # Build imports section
    imports = [
        '"""',
        f"Tests for {skill_info.name} skill",
        "",
        f"Auto-generated test template for: {skill_info.name}",
        f"Version: {skill_info.version}",
        f"Description: {skill_info.description}",
        "",
        "TODO: Fill in test implementations based on skill requirements.",
        '"""',
        "",
        "import pytest",
        "from pathlib import Path",
        "from typing import Dict, Any",
        "",
    ]

    # Add skill-specific imports if Python source exists
    if skill_info.has_python_src:
        imports.extend([
            "# TODO: Update imports based on actual module structure",
            f"# from {skill_name_snake}.src.orchestrator import {primary_class}",
            "",
        ])

    # Build test classes
    test_classes = []

    # Add fixtures class
    fixtures = [
        "",
        "# ==============================================================================",
        "# Test Fixtures",
        "# ==============================================================================",
        "",
        "",
        "@pytest.fixture",
        f"def sample_{skill_name_snake}_config() -> Dict[str, Any]:",
        f'    """Sample configuration for {skill_info.name}."""',
        "    return {",
        '        # TODO: Add realistic configuration values',
        '        "enabled": True,',
        '        "mode": "standard",',
        "    }",
        "",
        "",
        "@pytest.fixture",
        f"def sample_{skill_name_snake}_input() -> Dict[str, Any]:",
        f'    """Sample input data for {skill_info.name}."""',
        "    return {",
        '        # TODO: Add realistic input data',
        '        "data": "sample",',
        "    }",
        "",
    ]
    test_classes.extend(fixtures)

    # Add main test class
    main_class = [
        "",
        "# ==============================================================================",
        "# Main Test Class",
        "# ==============================================================================",
        "",
        "",
        f"class Test{primary_class}:",
        f'    """Tests for {skill_info.name} main functionality."""',
        "",
        "    def test_initialization(self):",
        '        """Test that the skill initializes correctly."""',
        "        # TODO: Implement initialization test",
        "        # Example:",
        f"        # orchestrator = {primary_class}()",
        "        # assert orchestrator is not None",
        "        pass",
        "",
        f"    def test_initialization_with_config(self, sample_{skill_name_snake}_config):",
        '        """Test initialization with custom configuration."""',
        "        # TODO: Implement config initialization test",
        "        pass",
        "",
    ]
    test_classes.extend(main_class)

    # Add capability-specific test classes
    if skill_info.capabilities:
        test_classes.extend([
            "",
            "# ==============================================================================",
            "# Capability Tests",
            "# ==============================================================================",
        ])

        for i, capability in enumerate(skill_info.capabilities[:5]):  # Limit to 5
            cap_name = sanitize_name(capability.name)
            class_name = "".join(word.title() for word in cap_name.split("_"))

            test_classes.extend([
                "",
                "",
                f"class Test{class_name}:",
                f'    """Tests for {capability.name} capability."""',
                "",
                f"    def test_{cap_name}_basic(self):",
                f'        """Test basic {capability.name} functionality."""',
                "        # TODO: Implement basic test",
                "        pass",
                "",
                f"    def test_{cap_name}_with_valid_input(self, sample_{skill_name_snake}_input):",
                f'        """Test {capability.name} with valid input data."""',
                "        # TODO: Implement valid input test",
                "        pass",
                "",
                f"    def test_{cap_name}_error_handling(self):",
                f'        """Test {capability.name} error handling."""',
                "        # TODO: Implement error handling test",
                "        pass",
                "",
            ])

    # Add edge case and integration test classes
    edge_cases = [
        "",
        "# ==============================================================================",
        "# Edge Cases and Integration Tests",
        "# ==============================================================================",
        "",
        "",
        f"class Test{primary_class}EdgeCases:",
        f'    """Edge case tests for {skill_info.name}."""',
        "",
        "    def test_empty_input(self):",
        '        """Test behavior with empty input."""',
        "        # TODO: Implement empty input test",
        "        pass",
        "",
        "    def test_invalid_input(self):",
        '        """Test behavior with invalid input."""',
        "        # TODO: Implement invalid input test",
        "        pass",
        "",
        "    def test_large_input(self):",
        '        """Test behavior with large input data."""',
        "        # TODO: Implement large input test",
        "        pass",
        "",
    ]
    test_classes.extend(edge_cases)

    # Add markers based on category
    markers = []
    if skill_info.category in ["financial", "compliance"]:
        markers.append(f"@pytest.mark.{skill_info.category}")
    markers.append("@pytest.mark.unit")

    # Combine all parts
    template = "\n".join(imports + test_classes)

    return template


def get_all_skills(project_root: Path) -> List[Path]:
    """Get all skill directories from both locations."""
    skills = []

    # Managed skills
    managed_dir = project_root / ".claude" / "skills"
    if managed_dir.exists():
        for skill_dir in managed_dir.iterdir():
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                skills.append(skill_dir)

    # User skills
    user_dir = project_root / "skills"
    if user_dir.exists():
        for skill_dir in user_dir.iterdir():
            if skill_dir.is_dir() and skill_dir.name != "templates":
                if (skill_dir / "SKILL.md").exists():
                    skills.append(skill_dir)

    return skills


def find_skill(project_root: Path, skill_name: str) -> Optional[Path]:
    """Find a skill by name in either location."""
    # Check managed skills first
    managed_path = project_root / ".claude" / "skills" / skill_name
    if managed_path.exists() and (managed_path / "SKILL.md").exists():
        return managed_path

    # Check user skills
    user_path = project_root / "skills" / skill_name
    if user_path.exists() and (user_path / "SKILL.md").exists():
        return user_path

    return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate pytest test templates for skills"
    )
    parser.add_argument(
        "--skill",
        type=str,
        help="Generate tests for a specific skill"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Generate tests for all untested skills"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without writing files"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="tests/unit/python",
        help="Output directory for test files"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing test files"
    )
    args = parser.parse_args()

    if not args.skill and not args.all:
        parser.error("Either --skill or --all must be specified")

    project_root = find_project_root()
    output_dir = project_root / args.output
    existing_tests = get_existing_tests(project_root)

    print("=" * 60)
    print("Skill Test Template Generator")
    print("=" * 60)
    print(f"Project root: {project_root}")
    print(f"Output directory: {output_dir}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'GENERATE'}")
    print()

    skills_to_process = []

    if args.skill:
        skill_path = find_skill(project_root, args.skill)
        if not skill_path:
            print(f"Error: Skill '{args.skill}' not found")
            sys.exit(1)
        skills_to_process.append(skill_path)
    else:
        # Process all untested skills
        for skill_path in get_all_skills(project_root):
            skill_name = skill_path.name
            if skill_name not in existing_tests or args.force:
                skills_to_process.append(skill_path)

    if not skills_to_process:
        print("No skills to process.")
        print(f"Existing tests found for: {len(existing_tests)} skills")
        return

    print(f"Skills to process: {len(skills_to_process)}")
    print()

    generated_count = 0
    for skill_path in skills_to_process:
        skill_info = analyze_skill(skill_path)
        if not skill_info:
            print(f"⚠️  Could not analyze: {skill_path.name}")
            continue

        print(f"{'='*60}")
        print(f"Skill: {skill_info.name}")
        print(f"  Path: {skill_path}")
        print(f"  Version: {skill_info.version}")
        print(f"  Category: {skill_info.category}")
        print(f"  Capabilities found: {len(skill_info.capabilities)}")
        print(f"  Python classes: {skill_info.python_classes or 'None'}")

        # Generate test template
        template = generate_test_template(skill_info)
        test_filename = f"test_{sanitize_name(skill_info.name)}.py"
        test_path = output_dir / test_filename

        if args.dry_run:
            print(f"\n  Would write: {test_path}")
            print(f"  Template preview (first 30 lines):")
            for i, line in enumerate(template.split("\n")[:30]):
                print(f"    {line}")
            print("    ...")
        else:
            if test_path.exists() and not args.force:
                print(f"\n  ⚠️  Skipping (exists): {test_path}")
                continue

            output_dir.mkdir(parents=True, exist_ok=True)
            test_path.write_text(template)
            print(f"\n  ✅ Generated: {test_path}")
            generated_count += 1

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Skills analyzed: {len(skills_to_process)}")
    if not args.dry_run:
        print(f"Test files generated: {generated_count}")
    else:
        print("(Dry run - no files written)")


if __name__ == "__main__":
    main()
