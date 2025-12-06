#!/usr/bin/env python3
"""
Check SKILL.md Frontmatter

Pre-commit hook script to validate that SKILL.md files have proper
YAML frontmatter with required fields.

Usage:
    python scripts/check_skill_frontmatter.py [file1.md] [file2.md] ...
"""

import sys
from pathlib import Path


def check_frontmatter(file_path: str) -> bool:
    """
    Validate that a SKILL.md file has proper frontmatter.

    Args:
        file_path: Path to the SKILL.md file

    Returns:
        True if valid, False otherwise
    """
    try:
        content = Path(file_path).read_text(encoding='utf-8')
    except (IOError, OSError) as e:
        print(f"Error reading {file_path}: {e}")
        return False

    # Check for opening frontmatter delimiter
    if not content.startswith('---'):
        print(f"Missing frontmatter: {file_path}")
        return False

    # Find closing delimiter
    end = content.find('\n---', 3)
    if end == -1:
        print(f"Unclosed frontmatter: {file_path}")
        return False

    # Extract and validate frontmatter content
    frontmatter = content[3:end]
    required_fields = ['name:', 'version:', 'description:']

    for field in required_fields:
        if field not in frontmatter:
            print(f"Missing {field} in frontmatter: {file_path}")
            return False

    return True


def main():
    """Main entry point for pre-commit hook."""
    if len(sys.argv) < 2:
        print("Usage: check_skill_frontmatter.py <file1> [file2] ...")
        sys.exit(0)

    files = sys.argv[1:]

    # Filter to only SKILL.md files
    skill_files = [f for f in files if f.endswith('SKILL.md')]

    if not skill_files:
        sys.exit(0)

    results = [check_frontmatter(f) for f in skill_files]
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
