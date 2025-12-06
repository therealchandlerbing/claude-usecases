#!/usr/bin/env python3
"""
Skill Initialization Script
Creates new financial skill with proper structure and templates
"""

import os
import sys
import argparse
from datetime import datetime
from pathlib import Path

# Import yaml with guard for helpful error message
try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

# Skill template with financial modeling focus
SKILL_MD_TEMPLATE = """---
name: {skill_name}
description: {description}
---

# {skill_title}

{summary}

## Core Capabilities

This skill provides comprehensive {domain} workflows including:
- [Capability 1]
- [Capability 2]
- [Capability 3]

## Workflow Architecture

### Phase 1: Data Gathering
[Describe data collection process]

### Phase 2: Analysis
[Describe analytical process]

### Phase 3: Output Generation
[Describe deliverables creation]

## Data Collection Protocol

### Required Data Points
```python
# Define data requirements
required_data = {{
    'financial': [],
    'operational': [],
    'market': []
}}
```

### Data Sources
- Internal systems (Asana, Drive, etc.)
- Financial platforms (S&P, Daloopa, etc.)
- Market research (Web search, reports)

## Analysis Framework

### Methodology
[Describe analytical approach]

### Key Calculations
[Define core calculations and formulas]

### Quality Checks
[List validation requirements]

## Output Standards

### Deliverable Format
[Describe output format and structure]

### Formatting Requirements
[Define visual and formatting standards]

### Distribution
[Specify how outputs are shared]

## Using Bundled Resources

### Scripts
- `scripts/[script1].py` - [Description]
- `scripts/[script2].py` - [Description]

### References
- `references/[ref1].md` - [Description]
- `references/[ref2].md` - [Description]

### Assets
- `assets/[asset1]` - [Description]
- `assets/[asset2]` - [Description]

## Quality Assurance

### Validation Checklist
- [ ] Data completeness verified
- [ ] Calculations accuracy confirmed
- [ ] Formatting standards met
- [ ] Output reviewed for errors

## Advanced Techniques

[Describe any advanced features or methods]

## Troubleshooting

### Common Issues and Solutions
[List typical problems and resolutions]
"""

EXAMPLE_SCRIPT_TEMPLATE = '''#!/usr/bin/env python3
"""
{script_description}
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Optional

class {class_name}:
    """
    {class_description}
    """

    def __init__(self):
        """Initialize the {lower_name}."""
        pass

    def execute(self, data: Dict) -> Dict:
        """
        Execute the main {lower_name} workflow.

        Args:
            data: Input data dictionary

        Returns:
            Processed results dictionary
        """
        # Implementation here
        results = {{}}

        return results

    def validate(self, data: Dict) -> bool:
        """Validate input data."""
        # Add validation logic
        return True

def main():
    """Example usage."""
    # Example implementation
    processor = {class_name}()

    # Sample data
    sample_data = {{}}

    # Execute processing
    results = processor.execute(sample_data)

    print("Processing complete")
    return results

if __name__ == "__main__":
    main()
'''

REFERENCE_TEMPLATE = """# {reference_title}

## Overview

This reference provides guidance for {topic}.

## Key Concepts

### Concept 1
[Description]

### Concept 2
[Description]

## Detailed Information

### Section 1
[Detailed content]

### Section 2
[Detailed content]

## Examples

### Example 1
```python
# Example code or content
```

### Example 2
```python
# Example code or content
```

## Best Practices

1. [Practice 1]
2. [Practice 2]
3. [Practice 3]

## Additional Resources

- [Resource 1]
- [Resource 2]
"""

def create_skill_structure(skill_name: str, skill_path: Path):
    """Create the directory structure for a new skill."""

    # Create main skill directory
    skill_dir = skill_path / skill_name
    skill_dir.mkdir(parents=True, exist_ok=True)

    # Create subdirectories
    (skill_dir / "scripts").mkdir(exist_ok=True)
    (skill_dir / "references").mkdir(exist_ok=True)
    (skill_dir / "assets").mkdir(exist_ok=True)

    print(f"✓ Created skill directory structure at: {skill_dir}")

    return skill_dir

def create_skill_md(skill_dir: Path, skill_name: str, description: str, domain: str):
    """Create the SKILL.md file with template content."""

    skill_title = skill_name.replace('-', ' ').title()

    # Prepare template variables
    template_vars = {
        'skill_name': skill_name,
        'description': description,
        'skill_title': skill_title,
        'summary': f"Transform {domain} from manual processes into systematic workflows with professional outputs.",
        'domain': domain
    }

    # Generate SKILL.md content
    skill_content = SKILL_MD_TEMPLATE.format(**template_vars)

    # Write SKILL.md
    skill_md_path = skill_dir / "SKILL.md"
    with open(skill_md_path, 'w') as f:
        f.write(skill_content)

    print(f"✓ Created SKILL.md with frontmatter and template content")

    return skill_md_path

def create_example_scripts(skill_dir: Path, skill_name: str):
    """Create example Python scripts for the skill."""

    scripts_dir = skill_dir / "scripts"

    # Create main processing script
    script_name = f"process_{skill_name.replace('-', '_')}.py"
    class_name = ''.join(word.capitalize() for word in skill_name.split('-')) + "Processor"

    script_content = EXAMPLE_SCRIPT_TEMPLATE.format(
        script_description=f"Main processing script for {skill_name}",
        class_name=class_name,
        class_description=f"Handles {skill_name} processing workflow",
        lower_name=skill_name.replace('-', ' ')
    )

    script_path = scripts_dir / script_name
    with open(script_path, 'w') as f:
        f.write(script_content)

    # Make script executable
    os.chmod(script_path, 0o755)

    print(f"✓ Created example script: {script_name}")

    # Create additional utility scripts based on skill type
    utility_scripts = [
        ("data_collector.py", "Data collection utilities"),
        ("calculator.py", "Financial calculation functions"),
        ("formatter.py", "Output formatting utilities"),
        ("validator.py", "Data validation functions")
    ]

    for script_file, description in utility_scripts[:2]:  # Create 2 utility scripts
        create_utility_script(scripts_dir, script_file, description)

def create_utility_script(scripts_dir: Path, filename: str, description: str):
    """Create a utility script with basic structure."""

    content = f'''#!/usr/bin/env python3
"""
{description}
"""

def main():
    """Main function."""
    print("{description}")

if __name__ == "__main__":
    main()
'''

    script_path = scripts_dir / filename
    with open(script_path, 'w') as f:
        f.write(content)

    os.chmod(script_path, 0o755)
    print(f"  - Created utility script: {filename}")

def create_example_references(skill_dir: Path, skill_name: str):
    """Create example reference documentation."""

    references_dir = skill_dir / "references"

    # Create methodology reference
    methodology_content = REFERENCE_TEMPLATE.format(
        reference_title=f"{skill_name.replace('-', ' ').title()} Methodology",
        topic=f"{skill_name} analysis and calculation methods"
    )

    with open(references_dir / "methodology.md", 'w') as f:
        f.write(methodology_content)

    # Create frameworks reference
    frameworks_content = REFERENCE_TEMPLATE.format(
        reference_title="Analytical Frameworks",
        topic="frameworks and models used in this skill"
    )

    with open(references_dir / "frameworks.md", 'w') as f:
        f.write(frameworks_content)

    print("✓ Created example reference documents")

def create_example_assets(skill_dir: Path, skill_name: str):
    """Create example asset files."""

    assets_dir = skill_dir / "assets"

    # Create a README for assets
    readme_content = f"""# Assets for {skill_name}

This directory contains templates and resources used by the skill:

- Excel templates (.xlsx)
- Document templates (.docx)
- HTML templates (.html)
- Configuration files (.json)
- Style sheets (.css)

Add your specific asset files here as needed.
"""

    with open(assets_dir / "README.md", 'w') as f:
        f.write(readme_content)

    # Create example configuration
    config_content = f'''{{{
    "skill_name": "{skill_name}",
    "version": "1.0.0",
    "created": "{datetime.now().isoformat()}",
    "settings": {{
        "default_format": "excel",
        "calculation_precision": 4,
        "currency": "USD"
    }}
}}'''

    with open(assets_dir / "config.json", 'w') as f:
        f.write(config_content)

    print("✓ Created example asset files")

def main():
    """Main function to initialize a new financial skill."""

    parser = argparse.ArgumentParser(
        description="Initialize a new financial modeling skill"
    )
    parser.add_argument(
        "skill_name",
        help="Name of the skill (use hyphens for spaces, e.g., 'risk-analysis')"
    )
    parser.add_argument(
        "--path",
        default="./skills",
        help="Path where skill should be created (default: ./skills)"
    )
    parser.add_argument(
        "--description",
        default="",
        help="Description of what the skill does"
    )
    parser.add_argument(
        "--domain",
        default="financial analysis",
        help="Domain or area of focus (e.g., 'valuation', 'risk assessment')"
    )

    args = parser.parse_args()

    # Validate skill name
    if not args.skill_name.replace('-', '').replace('_', '').isalnum():
        print("Error: Skill name should only contain letters, numbers, hyphens, and underscores")
        sys.exit(1)

    # Convert path to Path object
    base_path = Path(args.path)

    # Generate description if not provided
    if not args.description:
        args.description = f"Financial modeling and analysis for {args.skill_name.replace('-', ' ')}"

    print(f"\nInitializing new skill: {args.skill_name}")
    print(f"Domain: {args.domain}")
    print(f"Location: {base_path / args.skill_name}\n")

    try:
        # Create directory structure
        skill_dir = create_skill_structure(args.skill_name, base_path)

        # Create SKILL.md
        create_skill_md(skill_dir, args.skill_name, args.description, args.domain)

        # Create example scripts
        create_example_scripts(skill_dir, args.skill_name)

        # Create example references
        create_example_references(skill_dir, args.skill_name)

        # Create example assets
        create_example_assets(skill_dir, args.skill_name)

        print(f"\n✅ Successfully initialized skill: {args.skill_name}")
        print(f"\nNext steps:")
        print(f"1. Edit {skill_dir}/SKILL.md to define your skill's functionality")
        print(f"2. Add scripts to {skill_dir}/scripts/")
        print(f"3. Add reference docs to {skill_dir}/references/")
        print(f"4. Add templates to {skill_dir}/assets/")
        print(f"5. Package with: python scripts/package_skill.py {skill_dir}")

    except Exception as e:
        print(f"\n❌ Error initializing skill: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
