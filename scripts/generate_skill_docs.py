#!/usr/bin/env python3
"""
Skill Documentation Generator

Generates standardized documentation from Jinja2 templates for skills.
Reduces boilerplate and ensures consistency across skill documentation.

Usage:
    # Generate docs from a skill definition YAML
    python scripts/generate_skill_docs.py --config skill-definition.yaml --output skills/my-skill/

    # Preview generated docs without writing
    python scripts/generate_skill_docs.py --config skill-definition.yaml --dry-run

    # Generate only README
    python scripts/generate_skill_docs.py --config skill-definition.yaml --only README
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, Any, Optional

try:
    import yaml
except ImportError:
    yaml = None
    print("Warning: PyYAML not installed. Install with: pip install pyyaml")

try:
    from jinja2 import Environment, FileSystemLoader, TemplateNotFound
except ImportError:
    Environment = None
    print("Warning: Jinja2 not installed. Install with: pip install jinja2")


def find_project_root() -> Path:
    """Find the project root directory."""
    script_dir = Path(__file__).parent
    return script_dir.parent


def load_skill_definition(config_path: Path) -> Dict[str, Any]:
    """Load skill definition from YAML file."""
    if not yaml:
        raise RuntimeError("PyYAML is required. Install with: pip install pyyaml")

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file not found: {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Invalid YAML in configuration file: {e}")
        sys.exit(1)


def create_sample_definition() -> Dict[str, Any]:
    """Create a sample skill definition for demonstration."""
    return {
        "skill": {
            "name": "Sample Skill",
            "version": "1.0.0",
            "description": "A sample skill to demonstrate the documentation generator.",
            "category": "utility",
            "author": "360 Social Impact Studios",
            "created": "2024-01-01",
            "trigger_phrase": "Run the sample skill",
            "tags": ["sample", "demo", "utility"],
            "features": [
                {"name": "Feature 1", "description": "First feature description"},
                {"name": "Feature 2", "description": "Second feature description"},
            ],
            "use_cases": [
                "When you need to demonstrate documentation generation",
                "When creating new skills as a reference",
            ],
            "prerequisites": [
                "Python 3.11+",
                "Required dependencies installed",
            ],
            "triggers": [
                "User requests skill demonstration",
                "User asks to generate sample documentation",
            ],
            "phases": [
                {
                    "name": "Initialization",
                    "description": "Set up the skill environment",
                    "inputs": [
                        {"name": "config", "description": "Configuration dictionary", "required": False}
                    ],
                    "steps": ["Load configuration", "Validate inputs", "Initialize components"],
                    "outputs": [
                        {"name": "initialized", "description": "Whether initialization succeeded"}
                    ],
                },
                {
                    "name": "Execution",
                    "description": "Run the main skill logic",
                    "steps": ["Process input data", "Generate output", "Validate results"],
                    "outputs": [
                        {"name": "result", "description": "The skill execution result"}
                    ],
                },
            ],
            "config_options": [
                {"name": "verbose", "type": "boolean", "default": "false", "description": "Enable verbose logging"},
                {"name": "timeout", "type": "integer", "default": "30", "description": "Operation timeout in seconds"},
            ],
            "quality_criteria": [
                "Output matches expected format",
                "All required fields are populated",
                "No errors during execution",
            ],
            "examples": [
                {
                    "title": "Basic Usage",
                    "description": "Simple example of skill usage",
                    "input": '{"data": "sample"}',
                    "input_format": "json",
                    "output": '{"result": "success"}',
                    "output_format": "json",
                }
            ],
            "common_workflows": [
                {
                    "name": "Standard Workflow",
                    "description": "The most common usage pattern",
                    "steps": ["Trigger the skill", "Provide input", "Review output"],
                }
            ],
            "quick_actions": [
                {"name": "Run skill", "trigger": "Execute sample skill"},
                {"name": "Get status", "trigger": "Sample skill status"},
            ],
            "quick_fixes": [
                {"issue": "Skill not found", "solution": "Check skill is installed correctly"},
                {"issue": "Invalid input", "solution": "Verify input format matches schema"},
            ],
            "outputs": [
                {"format": "JSON", "description": "Structured result data"},
                {"format": "Markdown", "description": "Human-readable summary"},
            ],
            "has_implementation_guide": False,
            "has_examples": True,
        }
    }


def setup_jinja_env(template_dir: Path) -> 'Environment':
    """Set up Jinja2 environment with custom filters."""
    if not Environment:
        raise RuntimeError("Jinja2 is required. Install with: pip install jinja2")

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )

    # Add custom filters
    env.filters['default'] = lambda x, d='': x if x is not None else d

    return env


def generate_docs(
    skill_def: Dict[str, Any],
    template_dir: Path,
    output_dir: Path,
    templates: Optional[list] = None,
    dry_run: bool = False
) -> Dict[str, str]:
    """Generate documentation from templates."""
    env = setup_jinja_env(template_dir)
    generated = {}

    template_files = {
        "README": ("README.template.md", "README.md"),
        "SKILL": ("SKILL.template.md", "SKILL.md"),
        "QUICK-START": ("QUICK-START.template.md", "QUICK-START.md"),
    }

    # Filter templates if specified
    if templates:
        template_files = {k: v for k, v in template_files.items() if k in templates}

    for name, (template_file, output_file) in template_files.items():
        try:
            template = env.get_template(template_file)
            content = template.render(**skill_def)
            generated[name] = content

            if not dry_run:
                output_path = output_dir / output_file
                output_dir.mkdir(parents=True, exist_ok=True)
                output_path.write_text(content, encoding='utf-8')
                print(f"  ✅ Generated: {output_path}")
            else:
                print(f"  [DRY RUN] Would generate: {output_dir / output_file}")

        except TemplateNotFound:
            print(f"  ⚠️  Template not found: {template_file}")
        except Exception as e:
            print(f"  ❌ Error generating {name}: {e}")

    return generated


def main():
    parser = argparse.ArgumentParser(
        description="Generate skill documentation from Jinja2 templates"
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to skill definition YAML file"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output directory for generated docs"
    )
    parser.add_argument(
        "--templates",
        type=str,
        default="templates/skill-docs",
        help="Path to template directory"
    )
    parser.add_argument(
        "--only",
        type=str,
        nargs="+",
        choices=["README", "SKILL", "QUICK-START"],
        help="Generate only specific templates"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without writing files"
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Generate sample documentation"
    )
    args = parser.parse_args()

    project_root = find_project_root()
    template_dir = project_root / args.templates

    print("=" * 60)
    print("Skill Documentation Generator")
    print("=" * 60)
    print(f"Template directory: {template_dir}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'GENERATE'}")
    print()

    # Load or create skill definition
    if args.sample:
        print("Using sample skill definition...")
        skill_def = create_sample_definition()
        output_dir = project_root / "skills" / "sample-skill"
    elif args.config:
        config_path = Path(args.config)
        if not config_path.is_absolute():
            config_path = project_root / config_path
        print(f"Loading skill definition from: {config_path}")
        skill_def = load_skill_definition(config_path)
        output_dir = Path(args.output) if args.output else config_path.parent
    else:
        parser.error("Either --config or --sample must be specified")
        return

    if args.output:
        output_dir = Path(args.output)
        if not output_dir.is_absolute():
            output_dir = project_root / output_dir

    print(f"Output directory: {output_dir}")
    print()

    # Generate documentation
    generated = generate_docs(
        skill_def,
        template_dir,
        output_dir,
        templates=args.only,
        dry_run=args.dry_run
    )

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Templates processed: {len(generated)}")
    if not args.dry_run:
        print(f"Files written to: {output_dir}")
    else:
        print("(Dry run - no files written)")


if __name__ == "__main__":
    main()
