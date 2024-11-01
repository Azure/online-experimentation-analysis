# Integration snapshot tests

These test cases check the analysis summary produced by specific data scenarios.
Each subdirectory corresponds to a single test case, which is executed by [`test_integration.py`](../../test_integration.py).
Each test case should have the following input files:

- **analysis.json:** A JSON file storing the analysis metadata.
- **scorecard.csv:** A CSV file storing the analysis metric data.
- **output.md:** A markdown file storing the analysis summary used as a reference.
  - This is automatically generated. See [snapshot testing](#snapshot-testing).

## Snapshot testing

A snapshot test ensures the output does not change unexpectedly by comparing to a reference output stored in a file.
The test fails if the two outputs do not match, which can be caused by a regression or an expected change.
If the change is expected, then the reference file must be updated and the test re-run:

```bash
python -m pytest --snapshot-update
python -m pytest
```
