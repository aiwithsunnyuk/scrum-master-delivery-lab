# M8.1 UI/UX Enhancement

## Agile Delivery Command Center

M8.1 upgrades the Streamlit presentation layer from a functional dashboard into a recruiter-facing Agile Delivery Command Center.

### What changed

- Stronger visual hierarchy and recruiter-first landing page
- Delivery health signal based on Sprint Goal achievement and visible impediment load
- KPI strip with evidence-oriented metrics
- Seven-milestone journey with inspectable M1-M7 evidence
- Visual completed-vs-forecast delivery views without adding a Pandas runtime dependency
- Impediment operating model and visible register
- Coaching & stakeholder scenario lab
- Evidence Explorer with filtering and interview mapping
- Sprint Simulation with a reusable Inspect → Facilitate → Adapt → Experiment → Measure thinking model
- Session-state navigation buttons for a smoother recruiter journey
- Robust repository-relative evidence resolution
- Existing GitHub repository remains the source of truth

## Run

```bash
source .venv/bin/activate
streamlit run app.py
```

The app expects the existing M1-M7 evidence repository to remain intact.
