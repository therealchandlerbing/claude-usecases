# Make.com Blueprint Version History

This document explains the Make.com blueprint versioning and designates the canonical source.

## Canonical Blueprint

**`make-blueprint.json`** is the canonical, production-ready blueprint.

This blueprint was previously named `make-blueprint-v2.json` and represents the most refined version of the Fathom Intelligence Pipeline.

## Version Comparison

| Version | Lines | Status | Notes |
|---------|-------|--------|-------|
| `make-blueprint.json` (v2) | 213 | **Canonical** | Simplified, production-ready |
| `archive/make-blueprint-v1-original.json` | 653 | Archived | Original iteration |
| `archive/make-blueprint-v1-corrected.json` | 753 | Archived | Bug-fixed original |

## Decision Rationale

**v2 was designated canonical because:**

1. **Simplicity**: 7 well-organized modules vs. more complex flow in v1
2. **Clarity**: Clean prompt structure with explicit JSON output format
3. **Modern**: Uses latest Claude model (`claude-sonnet-4-20250514`)
4. **Completeness**: Proper webhook field expectations defined
5. **Maintainability**: Easier to understand and modify

**Why not v1-corrected?**

While v1-corrected fixed bugs in the original, it retained the more complex flow structure. The v2 redesign addressed the same issues while simplifying the overall architecture.

## Blueprint Features

The canonical blueprint implements:

1. **Webhook Receiver** - Accepts Fathom transcript data
2. **Claude API Call** - Extracts relationship intelligence from transcripts
3. **JSON Parser** - Parses Claude's structured response
4. **Supabase Inserts** (4 modules):
   - Relationships table
   - Interactions table
   - Commitments table
   - Signals table

## Required Configuration

Before deploying, replace these placeholders:

| Placeholder | Description |
|-------------|-------------|
| `YOUR_ANTHROPIC_API_KEY` | Anthropic API key for Claude |
| `YOUR_SUPABASE_ANON_KEY` | Supabase anonymous key |

The Supabase URL is pre-configured for the 360 instance.

## Archived Versions

Previous versions are preserved in `archive/` for reference:

- `archive/make-blueprint-v1-original.json` - First implementation
- `archive/make-blueprint-v1-corrected.json` - Bug-fixed first version

These should NOT be used in production.

---

*Last updated: 2025-12-04*
*Decision made during architecture review implementation*
