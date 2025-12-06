# Known Issue: Intermittent CI Test Failures

**Status**: Under Investigation
**Severity**: Medium
**First Observed**: 2025-12-06
**Last Updated**: 2025-12-06

---

## Summary

The CI pipeline occasionally reports test failures even when all tests pass locally. This document tracks the investigation and remediation of these failures.

## Current Status

As of 2025-12-06:
- **18 checks passing**
- **3 checks failing**:
  - Coverage Report / Generate Coverage Report
  - Tests / Python Tests (3.11)
  - Tests / Test Summary

## Symptoms

CI jobs fail with various errors, potentially including:
- Test assertion failures
- Import errors
- Timeout issues
- Coverage generation issues

## Investigation Findings

### Tests Pass Locally

All 383 Python tests pass locally:
```
======================== 383 passed, 1 skipped in 1.48s ========================
```

### CI Configuration Issues Fixed

The following CI configuration issues have been identified and fixed:

1. **Duplicate Test Runs** (Fixed)
   - `tests.yml` was running pytest twice (once without coverage, once with)
   - Removed duplicate run to improve efficiency

2. **Missing HTML Coverage Report** (Fixed)
   - `coverage.yml` tried to upload `htmlcov/` but wasn't generating it
   - Added `--cov-report=html` to pytest command

3. **YAML Import Guards** (Fixed)
   - Added import guards to all files that import `yaml`
   - Added `pytestmark` skipif for test files that require yaml
   - Added `require_yaml` fixture in conftest.py

### Files Modified

**CI Workflows:**
- `.github/workflows/tests.yml` - Removed duplicate test run
- `.github/workflows/coverage.yml` - Added HTML coverage report generation

**Test Files with YAML Import Guards:**
- `tests/unit/python/test_skill_structure_validator.py`
- `tests/unit/python/test_990_orchestrator.py`
- `tests/conftest.py` - Added `yaml_available` and `require_yaml` fixtures

**Script Files with YAML Import Guards:**
- `skills/990-ez-preparation/src/orchestrator.py`
- `.claude/skills/financial-modeling-skills/scripts/init_skill.py`
- `.claude/skills/financial-modeling-skills/scripts/package_skill.py`

## Potential Root Causes

| Cause | Likelihood | Status |
|-------|------------|--------|
| YAML import issues | High | Fixed |
| Duplicate test runs | Medium | Fixed |
| Missing coverage report | Medium | Fixed |
| Environment differences | Medium | Under investigation |
| Flaky tests | Low | Not observed |
| Race conditions | Low | Not observed |

## Next Steps

1. **Monitor CI runs** after deploying fixes
2. **Review CI logs** when failures occur to identify specific errors
3. **Compare environments** between local and CI if issues persist
4. **Add more verbose logging** to CI if needed

## Workarounds

### For PR Authors

If your PR shows failing checks:

1. **Check if failures are pre-existing** - Compare with main branch CI status
2. **Re-run failed jobs** - Sometimes transient failures resolve on retry
3. **Review CI logs** - Look for specific error messages
4. **Run tests locally** - Verify tests pass on your machine:
   ```bash
   pip install -r requirements-test.txt
   python -m pytest --verbose
   ```

### For Maintainers

If persistent failures occur:

1. **Clear GitHub Actions cache** - Go to Actions > Caches and delete stale caches
2. **Check requirements-test.txt** - Ensure all dependencies have version pins
3. **Review recent changes** - Look for environment-sensitive code

## Related Issues

- [KNOWN-ISSUE-YAML-IMPORT.md](./KNOWN-ISSUE-YAML-IMPORT.md) - YAML import error documentation (RESOLVED)

## Resolution Criteria

This issue will be considered resolved when:
- [ ] All CI checks pass consistently for 5+ consecutive PRs
- [ ] No YAML import errors in CI logs
- [ ] Coverage reports generate successfully
- [ ] Test Summary job completes without failure

## Files to Monitor

- `.github/workflows/tests.yml`
- `.github/workflows/coverage.yml`
- `tests/conftest.py`
- `requirements-test.txt`

---

**Note**: This document should be updated as more information becomes available about the root cause and resolution of CI test failures.
