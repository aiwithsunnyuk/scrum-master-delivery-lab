import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sprint-metrics.csv"

rows = list(csv.DictReader(DATA.open()))

def pct(a, b):
    return (a / b * 100) if b else 0

print("\nScrum Master Delivery Dashboard")
print("=" * 34)

for r in rows:
    planned = int(r["planned_points"])
    completed = int(r["completed_points"])
    spill = int(r["spillover_points"])
    success = r["sprint_goal_success"]
    defects = int(r["defects"])
    cycle = float(r["cycle_time_days"])

    print(
        f'{r["sprint"]}: '
        f'{completed}/{planned} points '
        f'({pct(completed, planned):.0f}%), '
        f'spillover={spill}, '
        f'goal={success}, '
        f'defects={defects}, '
        f'cycle={cycle:.1f}d'
    )

print("\nInterpretation prompts:")
print("- Is the Sprint Goal consistently being achieved?")
print("- What system conditions explain spillover?")
print("- Is cycle time improving?")
print("- Are defects creating downstream cost?")
print("- What improvement should be inspected next Sprint?")
