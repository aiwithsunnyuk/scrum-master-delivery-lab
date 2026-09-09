# M8.3.1 · Executive Overview Navigation Integrity Fix

This patch restores the quick-access controls that were present in the earlier Streamlit presentation layer and were lost during later navigation/state-management corrections.

## Restored controls

- **View GitHub repository**: opens the GitHub repository, which remains the portfolio source of truth.
- **Open Evidence Explorer**: routes directly to the in-app evidence explorer.

## Why this is a patch, not a new capability milestone

M8.3 Executive Recruiter Mode already established the recruiter-facing presentation layer. M8.3.1 restores navigation/UX continuity without changing the underlying Scrum Master evidence, metrics, scenarios, or repository structure.

## Validation

`app.py` passes Python syntax compilation with:

```bash
python3 -m py_compile app.py
```
