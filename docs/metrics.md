# Agile Metrics

Metrics are used to support inspection and improvement, not to rank individuals.

## Example metrics

### Velocity
Completed story points per Sprint.

Useful for:
- Supporting forecasting discussions.

Not useful for:
- Comparing teams as if points were a universal productivity unit.

### Sprint Goal success
Did the team achieve the Sprint Goal?

This is often more meaningful than raw story-point completion.

### Spillover
Work forecast for a Sprint that is not Done by the end.

Use it to investigate system conditions, not to assign blame.

### Cycle time
Elapsed time from work starting to work becoming Done.

### Defect trend
Useful for understanding quality and whether speed is creating downstream cost.

## Current sample

See `data/sprint-metrics.csv`.

Run:

```bash
python scripts/sprint_metrics.py
```

The script prints a small delivery dashboard from the synthetic data.
