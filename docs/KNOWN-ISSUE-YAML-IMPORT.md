# Known Issue: YAML Module Import Error in CI

**Status**: Pre-existing issue
**Severity**: Low (does not block merges due to `continue-on-error`)
**First Observed**: Before skill consolidation PR
**Last Updated**: 2025-12-06

---

## Summary

The CI pipeline occasionally fails with `ModuleNotFoundError: No module named 'yaml'` even though `pyyaml` is listed as a dependency in `requirements-test.txt`. This is a CI environment configuration issue and is **not caused by any PR changes**.

## Symptoms

```
ModuleNotFoundError: No module named 'yaml'
```

This error appears in test runs that import `yaml`, particularly:
- `tests/unit/python/test_skill_structure_validator.py`
- Scripts that validate skill structure

## Affected CI Checks

The following checks may fail with this error:

1. **Python Tests** (`tests.yml` → `python-tests`)
2. **Skill Structure Validation** (`code-quality.yml` → `skill-structure-validation`)
3. **Code Quality checks** that run pylint on modules importing yaml

Note: Most of these checks have `continue-on-error: true` set, so they don't block PR merges.

## Root Cause Analysis

### The Dependency Chain

1. **`requirements-test.txt`** (line 34) correctly includes:
   ```
   pyyaml>=6.0.0                 # YAML configuration parsing
   ```

2. **CI workflows** install dependencies:
   - `tests.yml` (line 31): `pip install -r requirements-test.txt`
   - `code-quality.yml` (line 68): `pip install pyyaml` (explicit install)

### Potential Causes

| Cause | Likelihood | Details |
|-------|------------|---------|
| **Pip cache corruption** | Medium | GitHub Actions caches pip packages. A stale or corrupted cache could cause the package to appear installed but be non-functional. |
| **Race condition** | Low | Dependencies might not be fully installed before tests start running. |
| **Virtual environment isolation** | Medium | The GitHub-hosted runner might have environment isolation issues. |
| **Transient network failure** | Low | Package download could fail silently in some edge cases. |

### Code That Imports YAML

The following files import `yaml` and could trigger this error:

| File | Has Error Guard? |
|------|------------------|
| `scripts/validate_skill_structure.py` | Yes (lines 26-30) |
| `scripts/generate_skill_tests.py` | Yes (lines 29-32) |
| `scripts/generate_skill_docs.py` | Yes (lines 24-28) |
| `tests/unit/python/test_skill_structure_validator.py` | **No** (line 13) |
| `shared/config_loader.py` | No |
| `skills/990-ez-preparation/src/orchestrator.py` | No |

## Proposed Fixes

### Option 1: Clear Pip Cache in CI (Recommended)

Add cache invalidation to the workflow:

```yaml
- name: Set up Python
  uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'
    cache-dependency-path: requirements-test.txt  # Tie cache to requirements file
```

### Option 2: Add Explicit Verification Step

Add a verification step after installing dependencies:

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements-test.txt

- name: Verify yaml import
  run: python -c "import yaml; print(f'PyYAML version: {yaml.__version__}')"
```

### Option 3: Force Reinstall in CI

Use `--force-reinstall` for the critical package:

```yaml
- name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install -r requirements-test.txt
    pip install --force-reinstall pyyaml  # Ensure fresh install
```

### Option 4: Add Import Guards to Test Files

Add try/except guards to test files that import yaml:

```python
# In test_skill_structure_validator.py
try:
    import yaml
except ImportError:
    pytest.skip("PyYAML not installed - skipping yaml-dependent tests")
```

## Workarounds

### For Local Development

If you encounter this issue locally:

```bash
# Ensure pyyaml is installed
pip install pyyaml

# Or reinstall from requirements
pip install -r requirements-test.txt --force-reinstall
```

### For CI Failures

Since these checks have `continue-on-error: true`, they won't block your PR. However, if you need them to pass:

1. Re-run the failed workflow (sometimes transient)
2. Make a trivial commit to trigger a fresh CI run
3. Check if the pip cache needs clearing (GitHub Actions → Caches)

## Impact Assessment

| Impact Area | Assessment |
|-------------|------------|
| **PR Merges** | Not blocked (continue-on-error is set) |
| **Test Coverage** | Affected tests may be skipped |
| **Code Quality** | Pylint checks may be incomplete |
| **Skill Validation** | May not run on some PRs |

## Resolution Timeline

This issue should be addressed separately from feature PRs:

1. **Short-term**: Accept that these checks may fail intermittently
2. **Medium-term**: Implement Option 1 or 2 above
3. **Long-term**: Consider moving to a more robust dependency management (e.g., Poetry, pipenv)

## Related Files

- `.github/workflows/tests.yml`
- `.github/workflows/code-quality.yml`
- `requirements-test.txt`
- `scripts/validate_skill_structure.py`
- `tests/unit/python/test_skill_structure_validator.py`

## References

- [GitHub Actions: Caching dependencies](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows)
- [PyYAML on PyPI](https://pypi.org/project/PyYAML/)
- [Python import system](https://docs.python.org/3/reference/import.html)

---

**Note**: This documentation is for tracking a known issue. When a fix is implemented, update this document with the resolution details.
