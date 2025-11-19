#!/usr/bin/env python3
"""
Skill Packaging Script
Validates and packages financial skills for distribution
"""

import os
import sys
import argparse
import zipfile
import json
import yaml
from pathlib import Path
from datetime import datetime
import hashlib
import re

class SkillValidator:
    """Validates skill structure and content before packaging."""

    def __init__(self, skill_path: Path):
        self.skill_path = skill_path
        self.skill_name = skill_path.name
        self.errors = []
        self.warnings = []

    def validate(self) -> bool:
        """Run all validation checks."""

        print(f"Validating skill: {self.skill_name}")
        print("=" * 50)

        # Run validation checks
        self._check_structure()
        self._check_skill_md()
        self._check_scripts()
        self._check_references()
        self._check_assets()
        self._check_naming_conventions()
        self._check_file_sizes()

        # Report results
        if self.errors:
            print("\n❌ Validation Errors:")
            for error in self.errors:
                print(f"  - {error}")

        if self.warnings:
            print("\n⚠️  Validation Warnings:")
            for warning in self.warnings:
                print(f"  - {warning}")

        if not self.errors:
            print("\n✅ Validation passed!")

        return len(self.errors) == 0

    def _check_structure(self):
        """Check required directory structure."""

        # Check for SKILL.md
        skill_md = self.skill_path / "SKILL.md"
        if not skill_md.exists():
            self.errors.append("Missing required SKILL.md file")

        # Check directories (optional but recommended)
        recommended_dirs = ['scripts', 'references', 'assets']
        for dir_name in recommended_dirs:
            dir_path = self.skill_path / dir_name
            if not dir_path.exists():
                self.warnings.append(f"Missing recommended directory: {dir_name}/")

        print("  ✓ Structure check complete")

    def _check_skill_md(self):
        """Validate SKILL.md content and frontmatter."""

        skill_md_path = self.skill_path / "SKILL.md"
        if not skill_md_path.exists():
            return

        try:
            with open(skill_md_path, 'r') as f:
                content = f.read()

            # Check for frontmatter
            if not content.startswith('---'):
                self.errors.append("SKILL.md missing YAML frontmatter")
                return

            # Parse frontmatter
            parts = content.split('---', 2)
            if len(parts) < 3:
                self.errors.append("Invalid SKILL.md frontmatter format")
                return

            frontmatter_str = parts[1].strip()
            try:
                frontmatter = yaml.safe_load(frontmatter_str)
            except yaml.YAMLError as e:
                self.errors.append(f"Invalid YAML in frontmatter: {e}")
                return

            # Check required fields
            if 'name' not in frontmatter:
                self.errors.append("Missing 'name' field in frontmatter")
            elif frontmatter['name'] != self.skill_name:
                self.errors.append(f"Skill name mismatch: '{frontmatter['name']}' != '{self.skill_name}'")

            if 'description' not in frontmatter:
                self.errors.append("Missing 'description' field in frontmatter")
            elif len(frontmatter['description']) < 20:
                self.warnings.append("Description seems too short (< 20 characters)")
            elif len(frontmatter['description']) > 500:
                self.warnings.append("Description is very long (> 500 characters)")

            # Check description quality
            description = frontmatter.get('description', '')
            if description and not any(trigger_word in description.lower() for trigger_word in
                                      ['use when', 'use for', 'provides', 'enables', 'generates']):
                self.warnings.append("Description should indicate when to use the skill")

            # Check body content
            body = parts[2].strip()
            if len(body) < 100:
                self.warnings.append("SKILL.md body seems too short")

            # Check for recommended sections
            recommended_sections = ['## Core Capabilities', '## Workflow', '## Using Bundled Resources']
            for section in recommended_sections:
                if section not in body:
                    self.warnings.append(f"Missing recommended section: {section}")

            # Check line count
            line_count = len(body.split('\n'))
            if line_count > 500:
                self.warnings.append(f"SKILL.md body is long ({line_count} lines). Consider moving content to references/")

            print("  ✓ SKILL.md validation complete")

        except Exception as e:
            self.errors.append(f"Error reading SKILL.md: {e}")

    def _check_scripts(self):
        """Validate Python scripts."""

        scripts_dir = self.skill_path / "scripts"
        if not scripts_dir.exists():
            return

        python_files = list(scripts_dir.glob("*.py"))

        for script_file in python_files:
            # Check syntax
            try:
                with open(script_file, 'r') as f:
                    code = f.read()
                compile(code, script_file.name, 'exec')
            except SyntaxError as e:
                self.errors.append(f"Syntax error in {script_file.name}: {e}")

            # Check for docstrings
            if '"""' not in code and "'''" not in code:
                self.warnings.append(f"Missing docstring in {script_file.name}")

            # Check file size
            size_mb = script_file.stat().st_size / (1024 * 1024)
            if size_mb > 1:
                self.warnings.append(f"{script_file.name} is large ({size_mb:.1f} MB)")

        if python_files:
            print(f"  ✓ Validated {len(python_files)} Python scripts")

    def _check_references(self):
        """Validate reference documentation."""

        references_dir = self.skill_path / "references"
        if not references_dir.exists():
            return

        md_files = list(references_dir.glob("*.md"))

        for ref_file in md_files:
            with open(ref_file, 'r') as f:
                content = f.read()

            # Check for headers
            if not re.search(r'^#\s+.+', content, re.MULTILINE):
                self.warnings.append(f"{ref_file.name} missing header")

            # Check size
            if len(content) > 50000:
                self.warnings.append(f"{ref_file.name} is very large (>50k characters)")

        if md_files:
            print(f"  ✓ Validated {len(md_files)} reference documents")

    def _check_assets(self):
        """Validate asset files."""

        assets_dir = self.skill_path / "assets"
        if not assets_dir.exists():
            return

        # Check for large files
        for asset_file in assets_dir.rglob("*"):
            if asset_file.is_file():
                size_mb = asset_file.stat().st_size / (1024 * 1024)
                if size_mb > 10:
                    self.warnings.append(f"Large asset file: {asset_file.name} ({size_mb:.1f} MB)")
                elif size_mb > 50:
                    self.errors.append(f"Asset file too large: {asset_file.name} ({size_mb:.1f} MB)")

    def _check_naming_conventions(self):
        """Check file naming conventions."""

        # Skill name should be lowercase with hyphens
        if not re.match(r'^[a-z0-9-]+$', self.skill_name):
            self.errors.append("Skill name should be lowercase with hyphens only")

        # Check for spaces in filenames
        for file_path in self.skill_path.rglob("*"):
            if " " in file_path.name:
                self.warnings.append(f"Filename contains spaces: {file_path.name}")

    def _check_file_sizes(self):
        """Check total skill size."""

        total_size = sum(f.stat().st_size for f in self.skill_path.rglob("*") if f.is_file())
        total_mb = total_size / (1024 * 1024)

        if total_mb > 100:
            self.errors.append(f"Skill is too large ({total_mb:.1f} MB). Maximum is 100 MB")
        elif total_mb > 50:
            self.warnings.append(f"Skill is large ({total_mb:.1f} MB). Consider optimizing")

        print(f"  ✓ Total skill size: {total_mb:.1f} MB")


class SkillPackager:
    """Packages validated skills into distributable .skill files."""

    def __init__(self, skill_path: Path, output_dir: Path):
        self.skill_path = skill_path
        self.output_dir = output_dir
        self.skill_name = skill_path.name

    def package(self) -> Path:
        """Create .skill package file."""

        print(f"\nPackaging skill: {self.skill_name}")
        print("=" * 50)

        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Create package filename
        timestamp = datetime.now().strftime("%Y%m%d")
        package_name = f"{self.skill_name}_{timestamp}.skill"
        package_path = self.output_dir / package_name

        # Create manifest
        manifest = self._create_manifest()

        # Create zip file with .skill extension
        with zipfile.ZipFile(package_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Add manifest
            zf.writestr(f"{self.skill_name}/manifest.json",
                       json.dumps(manifest, indent=2))

            # Add all skill files
            file_count = 0
            for file_path in self.skill_path.rglob("*"):
                if file_path.is_file():
                    arcname = f"{self.skill_name}/{file_path.relative_to(self.skill_path)}"
                    zf.write(file_path, arcname)
                    file_count += 1
                    print(f"  Added: {file_path.relative_to(self.skill_path)}")

        # Calculate package hash
        package_hash = self._calculate_hash(package_path)

        # Create metadata file
        metadata_path = package_path.with_suffix('.json')
        metadata = {
            'skill_name': self.skill_name,
            'package_name': package_name,
            'created': datetime.now().isoformat(),
            'hash': package_hash,
            'size_bytes': package_path.stat().st_size,
            'file_count': file_count,
            'manifest': manifest
        }

        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)

        print(f"\n✅ Successfully packaged skill!")
        print(f"  Package: {package_path}")
        print(f"  Metadata: {metadata_path}")
        print(f"  Size: {package_path.stat().st_size / 1024:.1f} KB")
        print(f"  Files: {file_count}")
        print(f"  Hash: {package_hash[:12]}...")

        return package_path

    def _create_manifest(self) -> dict:
        """Create skill manifest with metadata."""

        # Read SKILL.md frontmatter
        skill_md_path = self.skill_path / "SKILL.md"
        with open(skill_md_path, 'r') as f:
            content = f.read()

        parts = content.split('---', 2)
        frontmatter = yaml.safe_load(parts[1].strip())

        # Count resources
        scripts = len(list((self.skill_path / "scripts").glob("*.py"))) if (self.skill_path / "scripts").exists() else 0
        references = len(list((self.skill_path / "references").glob("*.md"))) if (self.skill_path / "references").exists() else 0
        assets = sum(1 for _ in (self.skill_path / "assets").rglob("*") if _.is_file()) if (self.skill_path / "assets").exists() else 0

        manifest = {
            'version': '1.0.0',
            'skill_name': frontmatter['name'],
            'description': frontmatter['description'],
            'created': datetime.now().isoformat(),
            'author': '360 Social Impact Studios',
            'resources': {
                'scripts': scripts,
                'references': references,
                'assets': assets
            },
            'requirements': {
                'python': '>=3.8',
                'libraries': ['pandas', 'numpy', 'openpyxl']
            },
            'tags': ['financial-modeling', 'investment-analysis', '360-impact']
        }

        return manifest

    def _calculate_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of package file."""

        sha256_hash = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b''):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()


def main():
    """Main function to package a financial skill."""

    parser = argparse.ArgumentParser(
        description="Package a financial skill for distribution"
    )
    parser.add_argument(
        "skill_path",
        help="Path to the skill directory to package"
    )
    parser.add_argument(
        "output_dir",
        nargs='?',
        default="./dist",
        help="Output directory for packaged skill (default: ./dist)"
    )
    parser.add_argument(
        "--skip-validation",
        action="store_true",
        help="Skip validation checks (not recommended)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Package even if validation has warnings"
    )

    args = parser.parse_args()

    # Convert paths
    skill_path = Path(args.skill_path).resolve()
    output_dir = Path(args.output_dir).resolve()

    # Check if skill path exists
    if not skill_path.exists():
        print(f"Error: Skill path does not exist: {skill_path}")
        sys.exit(1)

    if not skill_path.is_dir():
        print(f"Error: Skill path is not a directory: {skill_path}")
        sys.exit(1)

    # Validate skill
    if not args.skip_validation:
        validator = SkillValidator(skill_path)
        is_valid = validator.validate()

        if not is_valid:
            print("\n❌ Skill validation failed. Fix errors before packaging.")
            sys.exit(1)

        if validator.warnings and not args.force:
            print("\n⚠️  Validation completed with warnings.")
            response = input("Continue packaging? (y/N): ")
            if response.lower() != 'y':
                print("Packaging cancelled.")
                sys.exit(0)

    # Package skill
    packager = SkillPackager(skill_path, output_dir)

    try:
        package_path = packager.package()

        print("\n📦 Packaging complete!")
        print("\nTo install this skill:")
        print(f"  1. Share the .skill file: {package_path}")
        print(f"  2. Users can upload to Claude via the skills interface")

    except Exception as e:
        print(f"\n❌ Error packaging skill: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
