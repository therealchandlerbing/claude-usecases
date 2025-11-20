# Test Data Directory

This directory contains test fixtures, sample data, and mock files used by the test suite.

## Organization

```
tests/data/
├── financial/          # Sample financial data, 990 forms, etc.
├── personas/           # Sample Vianeo persona markdown files
├── html/              # Sample HTML templates and outputs
├── xlsx/              # Sample Excel files for testing
├── api_responses/     # Mock API responses (Asana, Supabase, etc.)
└── README.md          # This file
```

## Usage

Test data files in this directory are available to tests via the `test_data_dir` fixture:

```python
def test_load_sample_data(test_data_dir):
    sample_file = test_data_dir / "financial" / "sample_990.json"
    data = json.loads(sample_file.read_text())
```

## Guidelines

1. **Keep files small**: Test data should be minimal but representative
2. **Use realistic data**: Data should reflect actual use cases but be anonymized
3. **Version control**: All test data should be committed to git
4. **Documentation**: Add comments to complex test data files
5. **Cleanup**: Remove unused test data files regularly
