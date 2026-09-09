# Scrum Master Delivery Lab

A practical Scrum Master portfolio repository designed to demonstrate **how I operate an Agile delivery team**, not just that I know Scrum terminology.

## Why this repository exists

This portfolio connects four dimensions of experience:

- Hands-on Scrum Master experience
- Product Management experience
- PSM I and PSPO I certification
- Cross-functional delivery, stakeholder and backlog management

The repository uses a realistic product scenario and shows the artifacts, decisions, metrics and continuous-improvement practices a Scrum Master would use across a delivery cycle.

## Portfolio scenario

**Product:** Customer Self-Service Portal

**Goal:** Reduce avoidable support contacts by giving customers a simple way to search knowledge articles, raise service requests and track request status.

**Delivery model:** Scrum

**Sprint length:** 2 weeks

**Team:** Product Owner, Scrum Master, 5 Developers, shared UX/QA support

## What this demonstrates

| Capability | Evidence in this repo |
|---|---|
| Sprint planning | `docs/sprint-01-plan.md` |
| Backlog management | `data/product-backlog.csv` |
| User stories | Product backlog + story template |
| Definition of Ready | `docs/definition-of-ready.md` |
| Definition of Done | `docs/definition-of-done.md` |
| Daily Scrum / flow management | `docs/daily-scrum-guide.md` |
| Impediment removal | `data/impediment-log.csv` |
| Risk & dependency management | `data/risk-dependency-log.csv` |
| Stakeholder management | `docs/stakeholder-map.md` |
| Sprint Review | `docs/sprint-01-review.md` |
| Retrospective | `docs/sprint-01-retro.md` |
| Metrics | `docs/metrics.md` + `data/sprint-metrics.csv` |
| Continuous improvement | Retrospective actions + improvement backlog |
| Practical automation | `scripts/sprint_metrics.py` |
| Delivery governance | GitHub Actions validation |

## My Scrum Master operating model

**1. Enable clarity → 2. Facilitate flow → 3. Remove impediments → 4. Make progress visible → 5. Inspect & adapt**

The Scrum Master is not the team's task manager. The objective is to improve the team's ability to create value while protecting transparency, empiricism, focus and continuous improvement.

## Suggested interview walkthrough

Use this repository as a 10-minute story:

1. Start with the product goal.
2. Show how the Product Backlog was made transparent and ordered.
3. Explain the Sprint Goal.
4. Walk through one user story from refinement to acceptance.
5. Show an impediment and how it was resolved.
6. Explain the metrics without using them as a team-performance weapon.
7. Show the Sprint Review outcome.
8. Show one retrospective improvement and how it enters the next sprint.
9. Explain how stakeholder expectations are handled without bypassing the Product Owner.
10. Close with what changed in the team's delivery system.

## Personal positioning

My profile combines **Scrum Master + Product Owner/Product Management + delivery coordination** experience. My earlier Scrum Master experience included Sprint Planning, Reviews, Retrospectives, Daily Scrum, Backlog Refinement, Release Planning, Scrum of Scrums, impediment removal, Scrum metrics and backlog-management support. My current Product Management experience adds product roadmaps, requirements, epics, user stories, stakeholder communication and cross-functional delivery.

That combination is the core story this repository is designed to make visible.

## Repository structure

```text
scrum-master-delivery-lab/
├── README.md
├── LICENSE
├── .github/workflows/validate.yml
├── data/
│   ├── product-backlog.csv
│   ├── sprint-metrics.csv
│   ├── impediment-log.csv
│   └── risk-dependency-log.csv
├── docs/
│   ├── product-charter.md
│   ├── sprint-01-plan.md
│   ├── sprint-01-review.md
│   ├── sprint-01-retro.md
│   ├── definition-of-ready.md
│   ├── definition-of-done.md
│   ├── daily-scrum-guide.md
│   ├── stakeholder-map.md
│   ├── metrics.md
│   └── interview-walkthrough.md
├── scripts/
│   └── sprint_metrics.py
└── templates/
    ├── user-story.md
    ├── impediment.md
    └── retrospective.md
```

## Current repository layers

The portfolio has grown beyond the original Scrum artifact set and now includes:

```text
docs/
├── milestone-01.md ... milestone-10.md
├── milestone-10-1.md
├── recruiter-guide.md
├── capability-matrix.md
├── end-to-end-story.md
├── interview-demo.md
├── portfolio-scorecard.md
├── delivery leadership artifacts
└── transformation artifacts

data/
├── sprint and delivery metrics
├── impediments, risks and dependencies
├── stakeholder/coaching evidence
└── transformation and decision data

app.py
requirements.txt
.streamlit/config.toml
```

The exact file inventory is visible directly in GitHub and evolves as the portfolio expands.

## Disclaimer

This is a **portfolio simulation**, not a representation of confidential Wipro or client data. The scenario, metrics and artifacts are intentionally synthetic.

## Portfolio Navigation

## 👋 New here?

You do **not** need GitHub, Python or Streamlit knowledge to review this portfolio.

Think of the repository as two connected layers:

```text
                    SCRUM MASTER DELIVERY LAB
                              │
                ┌─────────────┴─────────────┐
                │                           │
          GitHub Repository          Streamlit App
                │                           │
        Evidence / Source              Presentation
                │                           │
        Markdown + CSV              Dashboards + Labs
                │                           │
                └─────────────┬─────────────┘
                              │
                              ↓
                    INTERVIEW NARRATIVE
```

### Who should start where?

| Visitor | Start here | What to look for |
|---|---|---|
| Recruiter | **Executive Recruiter Mode** | Leadership signals, delivery ownership and evidence |
| Interviewer | **Interview Simulation** | Facilitation, judgement and Scrum Master decision-making |
| Agile / Delivery Leader | **Delivery Leadership Command Center** | Release readiness, risks, dependencies and governance |
| Transformation Leader | **Agile Transformation Lab** | Maturity, operating model, roadmap and change |
| Technical Reviewer | **Run Locally** | Streamlit application structure and evidence integration |

### 5-minute portfolio tour

1. Read the **Recruiter Guide**.
2. Open the **Capability Matrix** to see how each capability is backed by evidence.
3. Review the **End-to-End Delivery Story**.
4. Run the Streamlit application and open **Executive Recruiter Mode**.
5. Try **Interview Simulation**.
6. Open **Delivery Leadership Command Center** and **Agile Transformation Lab**.
7. Use the GitHub files as the source evidence behind the presentation.

The goal is not to demonstrate that I can build a dashboard. The goal is to make my **Agile delivery judgement visible and easy to assess**.

## 🚀 Streamlit Command Center

The repository includes an interactive Streamlit application that presents the portfolio as a working Agile delivery command center.

### What the application contains

- Executive Overview
- Executive Recruiter Mode
- 10-milestone Agile delivery journey
- Delivery Dashboard
- Impediment Center
- Coaching Lab
- Evidence Explorer
- Interview Simulation
- Executive Delivery Command Center
- Agile Transformation Lab
- Transformation Decision Simulator

The application reads the portfolio's Markdown and CSV evidence from the repository. The current version does **not** require an external AI API key.

## ▶️ Run the portfolio locally

If you already have Python installed:

```bash
git clone https://github.com/aiwithsunnyuk/scrum-master-delivery-lab.git
cd scrum-master-delivery-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit address shown in the terminal.

To stop the application:

```text
Ctrl+C
```

### Windows note

The virtual-environment activation command is:

```text
.venv\\Scripts\\activate
```

The remaining commands are the same.

## ☁️ Deploy the Streamlit app for free

The easiest way to make the portfolio accessible to a recruiter or interviewer is **Streamlit Community Cloud**, which can deploy directly from GitHub.

### Before you deploy

The current application requires **no API key**.

You only need:

- A GitHub account with access to this repository
- The repository pushed to GitHub
- A Streamlit Community Cloud account connected to GitHub

### Deployment steps

1. Open Streamlit Community Cloud:
   https://share.streamlit.io/
2. Sign in with GitHub and authorize access.
3. Choose **Create app**.
4. Select:
   - **Repository:** `aiwithsunnyuk/scrum-master-delivery-lab`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Deploy the app.
6. Share the generated Streamlit app URL with recruiters or interviewers.

After deployment, future GitHub pushes can update the deployed application.

### Recommended deployment settings

The repository already contains:

```text
requirements.txt
app.py
.streamlit/config.toml
```

The application is designed to run with the dependency versions defined in `requirements.txt`.

## 🔐 About API keys and Streamlit Secrets

**Do not put an API key directly into `app.py`, `README.md`, CSV files or GitHub.**

The current portfolio does not need an API key. If a future version adds an AI capability, store the credential in Streamlit's **Secrets** configuration rather than committing it to the repository.

Example Streamlit Secret:

```toml
OPENAI_API_KEY = "your-api-key-here"
```

Example Python access:

```python
import streamlit as st

api_key = st.secrets["OPENAI_API_KEY"]
```

For local development, keep secrets in:

```text
.streamlit/secrets.toml
```

That file should remain excluded from Git.

**Important:** Streamlit Community Cloud is free to use, but an external AI provider's API may have separate pricing, quotas or free-tier rules. The two should not be treated as the same thing.

## 🧭 How to explain this repository in an interview

A simple explanation is:

> “This is an evidence-driven Scrum Master portfolio. GitHub is the evidence layer and Streamlit is the presentation layer. I started with product and backlog clarity, moved through sprint execution and impediment management, then added metrics, continuous improvement, stakeholder coaching, delivery leadership and Agile transformation. The interactive application lets an interviewer inspect those decisions rather than just read a list of Scrum responsibilities.”

### The underlying progression

```text
M1  Product Goal & Backlog
 ↓
M2  Sprint Execution & Adaptation
 ↓
M3  Impediment & Dependency Management
 ↓
M4  Metrics & Delivery Transparency
 ↓
M5  Inspect & Adapt
 ↓
M6  Coaching, Stakeholders & Conflict
 ↓
M7  End-to-End Portfolio
 ↓
M8  Interactive Streamlit Command Center
 ↓
M9  Delivery Leadership & Governance
 ↓
M10 Agile Transformation & Operating Model
 ↓
M10.1 Transformation Decision Simulator
```

This progression shows a move from **team-level Scrum facilitation** toward **delivery leadership, systems thinking and transformation capability**.

## 📌 Evidence-first design

The portfolio deliberately separates:

**Evidence → Presentation → Interview narrative**

That distinction matters.

- **Evidence:** Markdown documents, CSV datasets, decision logs and delivery artifacts.
- **Presentation:** Streamlit dashboards, scenario labs and decision simulators.
- **Interview narrative:** The reasoning behind the decisions, trade-offs and adaptations.

The Streamlit application should therefore be treated as a **window into the evidence**, not as the evidence itself.

### Start here
- [Recruiter Guide](docs/recruiter-guide.md)
- [Capability Matrix](docs/capability-matrix.md)
- [End-to-End Delivery Story](docs/end-to-end-story.md)
- [Interview Demo](docs/interview-demo.md)
- [Portfolio Scorecard](docs/portfolio-scorecard.md)

### Milestones
- Milestone 1 — Product Goal & Backlog
- Milestone 2 — Sprint Execution & Adaptation
- Milestone 3 — Impediment & Dependency Management
- Milestone 4 — Agile Metrics & Delivery Transparency
- Milestone 5 — Sprint Review, Retrospective & Improvement
- Milestone 6 — Coaching, Stakeholder Management & Conflict
- Milestone 7 — End-to-End Agile Delivery Portfolio
- Milestone 8 — Interactive Streamlit Command Center
- Milestone 9 — Delivery Leadership & Governance
- Milestone 10 — Agile Transformation & Operating Model
- Milestone 10.1 — Transformation Decision Simulator

## Final portfolio message

This repository is a practical simulation designed to demonstrate how I apply Scrum Master principles across product, delivery, stakeholder and continuous-improvement situations. All scenario data is synthetic and contains no confidential employer or client information.
