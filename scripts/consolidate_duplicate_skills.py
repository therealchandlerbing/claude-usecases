#!/usr/bin/env python3
"""
Skill Consolidation Script

Safely consolidates duplicate skills from skills/ to .claude/skills/ by:
1. Identifying unique files in each location
2. Merging unique content to the canonical location (.claude/skills/)
3. Creating symlinks from skills/ to .claude/skills/

Usage:
    # Dry run (default) - shows what would happen
    python scripts/consolidate_duplicate_skills.py

    # Execute the consolidation
    python scripts/consolidate_duplicate_skills.py --execute

    # Consolidate specific skill only
    python scripts/consolidate_duplicate_skills.py --skill ceo-advisor --execute
"""

import argparse
import os
import platform
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Skills that exist in both locations
DUPLICATE_SKILLS = [
    "ceo-advisor",
    "design-director",
    "skill-orchestrator",
    "intelligence-extractor",
    "open-deep-research-team",
    "workflow-process-generator",
    "360-client-portfolio-builder",
    "executive-impact-presentation-generator",
]


def find_project_root() -> Path:
    """Find the project root directory."""
    script_dir = Path(__file__).parent
    return script_dir.parent


def compare_directories(
    user_skill: Path, managed_skill: Path
) -> Tuple[List[Path], List[Path], List[Path]]:
    """
    Compare two skill directories and find unique files.

    Returns:
        Tuple of (only_in_user, only_in_managed, different_files)
    """
    only_in_user = []
    only_in_managed = []
    different_files = []

    # Get all files in user skill
    user_files = set()
    if user_skill.exists():
        for file in user_skill.rglob("*"):
            if file.is_file():
                user_files.add(file.relative_to(user_skill))

    # Get all files in managed skill
    managed_files = set()
    if managed_skill.exists():
        for file in managed_skill.rglob("*"):
            if file.is_file():
                managed_files.add(file.relative_to(managed_skill))

    # Find unique files
    only_in_user = [user_skill / f for f in user_files - managed_files]
    only_in_managed = [managed_skill / f for f in managed_files - user_files]

    # Find different files (same name, different content)
    common_files = user_files & managed_files
    for rel_path in common_files:
        user_file = user_skill / rel_path
        managed_file = managed_skill / rel_path
        try:
            if user_file.read_bytes() != managed_file.read_bytes():
                different_files.append(rel_path)
        except (IOError, OSError) as e:
            print(f"Warning: Could not compare {user_file}. Error: {e}")

    return only_in_user, only_in_managed, different_files


def analyze_skill(skill_name: str, project_root: Path) -> Dict:
    """Analyze a duplicate skill and return consolidation plan."""
    user_skill = project_root / "skills" / skill_name
    managed_skill = project_root / ".claude" / "skills" / skill_name

    if not user_skill.exists():
        return {"status": "not_found", "skill": skill_name}

    if not managed_skill.exists():
        return {"status": "no_canonical", "skill": skill_name}

    only_in_user, only_in_managed, different = compare_directories(
        user_skill, managed_skill
    )

    # Calculate sizes
    user_size = sum(f.stat().st_size for f in user_skill.rglob("*") if f.is_file())
    managed_size = sum(
        f.stat().st_size for f in managed_skill.rglob("*") if f.is_file()
    )

    return {
        "status": "duplicate",
        "skill": skill_name,
        "user_path": str(user_skill),
        "managed_path": str(managed_skill),
        "user_size_kb": user_size // 1024,
        "managed_size_kb": managed_size // 1024,
        "only_in_user": [str(f.relative_to(user_skill)) for f in only_in_user],
        "only_in_managed": [
            str(f.relative_to(managed_skill)) for f in only_in_managed
        ],
        "different_files": [str(f) for f in different],
    }


def merge_unique_files(
    skill_name: str, project_root: Path, dry_run: bool = True
) -> List[str]:
    """Merge unique files from skills/ to .claude/skills/."""
    user_skill = project_root / "skills" / skill_name
    managed_skill = project_root / ".claude" / "skills" / skill_name

    actions = []
    only_in_user, _, _ = compare_directories(user_skill, managed_skill)

    for file_path in only_in_user:
        rel_path = file_path.relative_to(user_skill)
        dest_path = managed_skill / rel_path

        action = f"Copy: {file_path} -> {dest_path}"
        actions.append(action)

        if not dry_run:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file_path, dest_path)

    return actions


def check_symlink_support() -> bool:
    """Check if the current system supports symlinks without admin privileges."""
    if platform.system() != "Windows":
        return True

    # On Windows, try to create a test symlink
    import tempfile
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            test_target = Path(tmpdir) / "target"
            test_link = Path(tmpdir) / "link"
            test_target.mkdir()
            test_link.symlink_to(test_target)
            return True
    except OSError:
        return False


def create_symlink(skill_name: str, project_root: Path, dry_run: bool = True) -> str:
    """Replace skills/{skill} directory with symlink to .claude/skills/{skill}."""
    user_skill = project_root / "skills" / skill_name
    managed_skill = project_root / ".claude" / "skills" / skill_name

    # Relative path from skills/ to .claude/skills/
    rel_target = Path("..") / ".claude" / "skills" / skill_name

    action = f"Symlink: {user_skill} -> {rel_target}"

    if not dry_run:
        # Check Windows symlink support
        if platform.system() == "Windows" and not check_symlink_support():
            print(f"\n⚠️  WARNING: Windows symlink creation requires either:")
            print("    1. Administrator privileges, OR")
            print("    2. Developer Mode enabled (Settings > Update & Security > For developers)")
            print(f"\n    Skipping symlink creation for {skill_name}")
            print(f"    The backup was created at: skills/.{skill_name}.backup")
            return f"SKIPPED (Windows permissions): {action}"

        # Backup and remove the directory
        backup_path = project_root / "skills" / f".{skill_name}.backup"
        if user_skill.exists() and not user_skill.is_symlink():
            shutil.move(user_skill, backup_path)

        # Create symlink
        try:
            user_skill.symlink_to(rel_target)
        except OSError as e:
            print(f"\n❌ ERROR creating symlink for {skill_name}: {e}")
            # Restore from backup
            if backup_path.exists():
                shutil.move(backup_path, user_skill)
                print(f"    Restored original directory from backup")
            return f"FAILED: {action}"

    return action


def consolidate_skill(
    skill_name: str, project_root: Path, dry_run: bool = True
) -> Dict:
    """Consolidate a single skill."""
    analysis = analyze_skill(skill_name, project_root)

    if analysis["status"] != "duplicate":
        return analysis

    actions = []

    # Step 1: Merge unique files
    merge_actions = merge_unique_files(skill_name, project_root, dry_run)
    actions.extend(merge_actions)

    # Step 2: Create symlink (if not dry run and merge succeeded)
    symlink_action = create_symlink(skill_name, project_root, dry_run)
    actions.append(symlink_action)

    analysis["actions"] = actions
    analysis["dry_run"] = dry_run

    return analysis


def main():
    parser = argparse.ArgumentParser(
        description="Consolidate duplicate skills from skills/ to .claude/skills/"
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Actually perform the consolidation (default is dry run)",
    )
    parser.add_argument(
        "--skill",
        type=str,
        help="Consolidate only this specific skill",
    )
    parser.add_argument(
        "--analyze-only",
        action="store_true",
        help="Only analyze and report, don't show consolidation plan",
    )
    args = parser.parse_args()

    project_root = find_project_root()
    dry_run = not args.execute

    print("=" * 60)
    print("Skill Consolidation Report")
    print("=" * 60)
    print(f"Project root: {project_root}")
    print(f"Platform: {platform.system()}")
    print(f"Mode: {'DRY RUN' if dry_run else 'EXECUTE'}")

    # Windows symlink warning
    if not dry_run and platform.system() == "Windows":
        if not check_symlink_support():
            print("\n⚠️  WARNING: Running on Windows without symlink support.")
            print("    Symlinks require Administrator privileges or Developer Mode.")
            print("    Files will be merged, but symlinks may fail.")
            response = input("\n    Continue anyway? [y/N]: ")
            if response.lower() != 'y':
                print("    Aborted.")
                sys.exit(0)

    print()

    skills_to_process = [args.skill] if args.skill else DUPLICATE_SKILLS

    total_user_size = 0
    total_managed_size = 0
    results = []

    for skill_name in skills_to_process:
        if args.analyze_only:
            result = analyze_skill(skill_name, project_root)
        else:
            result = consolidate_skill(skill_name, project_root, dry_run)

        results.append(result)

        if result["status"] == "duplicate":
            total_user_size += result["user_size_kb"]
            total_managed_size += result["managed_size_kb"]

    # Print results
    for result in results:
        print(f"\n{'='*60}")
        print(f"Skill: {result['skill']}")
        print("-" * 40)

        if result["status"] == "not_found":
            print("  Status: Not found in skills/")
            continue

        if result["status"] == "no_canonical":
            print("  Status: No canonical version in .claude/skills/")
            continue

        print(f"  User version:    {result['user_size_kb']:>6} KB ({result['user_path']})")
        print(f"  Managed version: {result['managed_size_kb']:>6} KB ({result['managed_path']})")

        if result["only_in_user"]:
            print(f"\n  Files only in user version ({len(result['only_in_user'])}):")
            for f in result["only_in_user"][:5]:
                print(f"    - {f}")
            if len(result["only_in_user"]) > 5:
                print(f"    ... and {len(result['only_in_user']) - 5} more")

        if result["only_in_managed"]:
            print(f"\n  Files only in managed version ({len(result['only_in_managed'])}):")
            for f in result["only_in_managed"][:5]:
                print(f"    - {f}")
            if len(result["only_in_managed"]) > 5:
                print(f"    ... and {len(result['only_in_managed']) - 5} more")

        if result["different_files"]:
            print(f"\n  Files with differences ({len(result['different_files'])}):")
            for f in result["different_files"][:5]:
                print(f"    - {f}")
            if len(result["different_files"]) > 5:
                print(f"    ... and {len(result['different_files']) - 5} more")

        if "actions" in result and result["actions"]:
            print(f"\n  Planned actions:")
            for action in result["actions"]:
                print(f"    - {action}")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total user skills size:    {total_user_size:>6} KB")
    print(f"Total managed skills size: {total_managed_size:>6} KB")
    print(f"Potential savings:         {total_user_size:>6} KB")

    if dry_run and not args.analyze_only:
        print("\n⚠️  This was a DRY RUN. No changes were made.")
        print("    Run with --execute to perform the consolidation.")
        print("\n    RECOMMENDED: Review the above output before executing.")
        print("    Backups will be created as .{skill_name}.backup")


if __name__ == "__main__":
    main()
