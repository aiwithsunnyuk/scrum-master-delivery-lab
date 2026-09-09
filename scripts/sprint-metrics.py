#!/usr/bin/env python3
"""Generate a compact Markdown delivery-metrics summary.

Usage:
    python scripts/sprint-metrics.py data/sprint-metrics.csv
"""

import csv
import statistics
import sys
from pathlib import Path

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/sprint-metrics.csv")

with path.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

completed = [int(r["completed_points"]) for r in rows]
cycle = [float(r["median_cycle_days"]) for r in rows]
goals = [r["sprint_goal_achieved"].lower() == "yes" for r in rows]

print("# Sprint Metrics Summary")
print()
print(f"- Sprints analysed: {len(rows)}")
print(f"- Average completed points: {statistics.mean(completed):.1f}")
print(f"- Average median cycle time: {statistics.mean(cycle):.1f} days")
print(f"- Sprint Goal achievement: {sum(goals)}/{len(goals)} ({sum(goals)/len(goals):.0%})")
print(f"- Latest observed velocity: {completed[-1]} points")
print()
print("> Metrics support inspection and adaptation. They are not individual performance targets.")
