# SAP Cloud ALM AI Copilot

> A lightweight Python/FastAPI project that analyzes SAP Cloud ALM-style project, task, risk, dependency, and workstream data and exposes delivery-risk intelligence through REST APIs and Swagger UI.

## 1. What is this project?

**SAP Cloud ALM AI Copilot** is a practical AI/automation-oriented backend prototype for project and delivery management.

The current implementation takes structured project data such as:

- Projects
- Workstreams
- Tasks
- Risks
- Dependencies

and turns it into useful delivery intelligence, including:

- Task-level risk scores
- Risk classification
- Risk reasons
- Recommended actions
- Project risk summaries
- Workstream health
- High-risk and blocked-task identification
- Early-warning indicators

The goal is to evolve this from a local FastAPI prototype into a reusable **SAP Cloud ALM delivery intelligence / AI Copilot platform** that can eventually consume real SAP Cloud ALM data and support an executive or project-manager-facing UI.

---

## 2. Current capabilities

The API currently exposes the following capabilities.

| Endpoint | Purpose |
|---|---|
| `GET /health` | Application health check |
| `GET /projects` | List projects |
| `GET /tasks` | List tasks |
| `GET /risks` | List risks |
| `GET /dependencies` | List dependencies |
| `GET /tasks/{task_id}/risk` | Calculate risk for one task |
| `GET /risks/summary` | Executive project risk summary |
| `GET /workstreams/summary` | Workstream-level risk summary |
| `GET /projects/{project_id}/summary` | Project-level summary |
| `GET /workstreams/{workstream_id}/health` | Explain workstream health |
| `GET /api/v1/early-warnings` | Identify early-warning conditions |

The application also exposes interactive OpenAPI/Swagger documentation through FastAPI.

---

## 3. High-level architecture

```text
                    +----------------------+
                    |      User / UI       |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |   FastAPI REST API   |
                    |      app/api.py      |
                    +----------+-----------+
                               |
              +----------------+----------------+
              |                |                |
              v                v                v
      +---------------+ +-------------+ +---------------+
      | Project       | | Risk Engine | | Health        |
      | Services      | |             | | Explainer     |
      +---------------+ +-------------+ +---------------+
              |                |                |
              +----------------+----------------+
                               |
                               v
                    +----------------------+
                    |      JSON Data       |
                    | data/tasks.json      |
                    | data/risks.json      |
                    | data/dependencies... |
                    +----------------------+
```

### Current processing flow

```text
Project / Task Data
        |
        v
Risk calculation
        |
        +----> Task risk score
        |
        +----> Risk level
        |
        +----> Risk reasons
        |
        +----> Recommendations
        |
        v
Workstream aggregation
        |
        +----> Critical / High / Medium / Low
        |
        +----> Average risk score
        |
        +----> Blocked tasks
        |
        +----> Highest-risk task
        |
        v
Health explanation
        |
        +----> Health status
        +----> Key drivers
        +----> Recommended actions
```

---

# 4. Repository structure

The current repository is organized approximately as follows:

```text
sap-cloud-alm-ai-copilot/
│
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── config.py
│   ├── main.py
│   │
│   ├── agents/
│   │   └── __init__.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── domain.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── health_explainer.py
│       ├── project_service.py
│       └── risk_engine.py
│
├── data/
│   ├── tasks.json
│   ├── risks.json
│   └── dependencies.json
│
├── README.md
└── ...
```

### Important modules

#### `app/api.py`

Contains the FastAPI application and REST endpoints.

#### `app/services/risk_engine.py`

Contains the core task-risk calculation and risk-summary logic.

#### `app/services/health_explainer.py`

Converts workstream risk information into human-readable:

- Health explanation
- Key drivers
- Recommended actions

#### `app/services/project_service.py`

Provides project/task/dependency data services.

#### `app/models/domain.py`

Contains domain-level models and enumerations used by the application.

#### `data/`

Contains the current demo dataset.

The data is intentionally local and deterministic so that another developer can clone the repository and run the project without needing SAP credentials.

---

# 5. Prerequisites

A user should have:

- Python 3.10+ recommended
- Git
- macOS, Linux, or Windows
- A terminal
- Internet access for the initial Python package installation

No SAP Cloud ALM tenant is required for the current demo implementation.

Real SAP Cloud ALM integration can be added later.

---

# 6. Clone the repository

Replace the URL below with the repository URL if the repository is moved or renamed.

```bash
git clone https://github.com/aiwithsunnyuk/sap-cloud-alm-ai-copilot.git
cd sap-cloud-alm-ai-copilot
```

Verify:

```bash
pwd
```

You should be inside:

```text
sap-cloud-alm-ai-copilot
```

---

# 7. Create a Python virtual environment

Creating a virtual environment prevents this project from interfering with other Python projects.

## macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, the terminal should normally show:

```text
(.venv)
```

Verify Python:

```bash
python --version
```

---

# 8. Install dependencies

If the repository contains `requirements.txt`:

```bash
pip install -r requirements.txt
```

If you are setting up the current lightweight prototype from scratch, the minimum FastAPI runtime is:

```bash
pip install fastapi uvicorn
```

It is recommended that future versions of the repository maintain a committed `requirements.txt` so that every user gets a reproducible environment.

To create one from the active environment:

```bash
pip freeze > requirements.txt
```

Review the file before committing it.

---

# 9. Start the application

From the repository root:

```bash
uvicorn app.api:app --reload
```

You should see Uvicorn start on:

```text
http://127.0.0.1:8000
```

Keep this terminal running.

---

# 10. Open Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides an interactive API explorer.

Each endpoint can be expanded and executed directly from the browser.

Typical workflow:

```text
Expand endpoint
      ↓
Try it out
      ↓
Enter parameters if required
      ↓
Execute
      ↓
Inspect Response body
```

---

# 11. Swagger test sequence

The recommended order is:

## 11.1 Health

```text
GET /health
```

Expected result:

```json
{
  "status": "healthy"
}
```

---

## 11.2 Projects

```text
GET /projects
```

Use this to verify project data loading.

---

## 11.3 Tasks

```text
GET /tasks
```

Use this to verify task data loading.

---

## 11.4 Risks

```text
GET /risks
```

Use this to verify risk data loading.

---

## 11.5 Dependencies

```text
GET /dependencies
```

Use this to verify dependency data loading.

---

## 11.6 Individual task risk

```text
GET /tasks/{task_id}/risk
```

Example:

```text
TASK-006
```

This endpoint returns the calculated risk for the selected task.

The response includes fields such as:

```json
{
  "task_id": "TASK-006",
  "task_name": "...",
  "workstream_id": "WS-INT",
  "owner": "...",
  "priority": "...",
  "status": "...",
  "completion": 0,
  "risk_score": 100,
  "risk_level": "Critical",
  "reasons": [],
  "recommendations": []
}
```

---

# 12. Risk summary

Run:

```text
GET /risks/summary
```

This is the executive-level risk view.

It aggregates task-level calculations into information such as:

- Total tasks
- Critical risks
- High risks
- Medium risks
- Low risks
- Average risk score
- Blocked tasks
- Highest-risk task

This endpoint is intended to become a foundation for an executive dashboard.

---

# 13. Workstream summary

Run:

```text
GET /workstreams/summary
```

The endpoint groups tasks by workstream.

A workstream summary includes:

- Workstream ID
- Total tasks
- Critical count
- High count
- Medium count
- Low count
- Average risk score
- Blocked-task count
- Highest-risk task
- Overall health

Health is currently represented as:

```text
Green
Amber
Red
```

The current logic is:

```text
Critical risk exists -> Red
Otherwise high risk exists -> Amber
Otherwise -> Green
```

---

# 14. Project summary

Run:

```text
GET /projects/{project_id}/summary
```

Example:

```text
PRJ-001
```

This endpoint provides a project-level aggregation of delivery risk.

---

# 15. Workstream health explanation

Run:

```text
GET /workstreams/{workstream_id}/health
```

Example:

```text
WS-INT
```

The response provides:

```json
{
  "health_explanation": "...",
  "key_drivers": [
    "...",
    "..."
  ],
  "recommended_actions": [
    "...",
    "..."
  ]
}
```

This is an important part of the Copilot concept.

Instead of forcing a project manager to interpret raw risk numbers, the service converts those numbers into an explanation.

For example:

```text
Health:
RED

Why:
Critical-risk task identified.
Blocked task exists.
Average risk score is high.

Recommended actions:
1. Prioritize critical-risk tasks immediately.
2. Resolve blocking dependencies.
3. Review the highest-risk task with its owner.
4. Escalate the workstream for management review.
```

---

# 16. Early warnings

Run:

```text
GET /api/v1/early-warnings
```

The purpose of this endpoint is to detect delivery conditions that should receive attention before they become major project problems.

The long-term goal is to evolve early warnings from simple deterministic rules into an intelligent prediction layer.

Potential future signals include:

- Increasing risk score
- Repeated blocked status
- Missed milestones
- Dependency concentration
- Low completion with high risk
- Critical risks without mitigation progress
- Workstream health deterioration
- Risk trends over time

---

# 17. Understanding the risk engine

The current risk engine uses deterministic scoring.

A task can receive additional risk based on factors such as:

- Priority
- Status
- Completion
- Related risks
- Dependency relationships

Risk levels are classified using the calculated score.

Current classification:

```text
75 - 100  -> Critical
50 - 74   -> High
30 - 49   -> Medium
0 - 29    -> Low
```

The score is capped at:

```text
100
```

This makes the current implementation predictable and easy to test.

The architecture is intentionally designed so that this deterministic engine can later be enhanced with:

- Statistical models
- LLM reasoning
- SAP Cloud ALM data
- Historical project data
- Agentic workflows

---

# 18. Why deterministic logic first?

The first version deliberately avoids making an LLM responsible for basic calculations.

Risk scoring should be:

- Repeatable
- Explainable
- Testable
- Auditable

The AI/Copilot layer should add interpretation and decision support rather than replacing simple arithmetic with an opaque model.

A future architecture can therefore look like:

```text
SAP Cloud ALM
      |
      v
Data ingestion
      |
      v
Deterministic risk engine
      |
      v
Early-warning engine
      |
      v
AI reasoning / Copilot
      |
      +---- Explain
      +---- Recommend
      +---- Prioritize
      +---- Ask for approval
      |
      v
User / Project Manager
```

---

# 19. API documentation

FastAPI automatically provides:

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

### OpenAPI specification

```text
http://127.0.0.1:8000/openapi.json
```

The OpenAPI JSON can later be used to generate:

- Client SDKs
- Frontend API clients
- API documentation
- Integration tests
- External integrations

---

# 20. Why Swagger may only show HTTPValidationError and ValidationError

FastAPI automatically creates validation schemas.

If an endpoint currently returns ordinary Python dictionaries rather than explicit Pydantic response models, Swagger has limited information about the exact response structure.

Therefore the Schemas section may currently show mainly:

```text
HTTPValidationError
ValidationError
```

This does **not** mean the API is broken.

The endpoints can still execute normally.

A future improvement is to introduce explicit response models such as:

```text
TaskRiskResponse
RiskSummaryResponse
WorkstreamSummaryResponse
HealthExplanationResponse
EarlyWarningResponse
ProjectSummaryResponse
```

Then Swagger will display meaningful domain schemas.

---

# 21. Testing from the terminal

Swagger is useful for interactive testing, but APIs should also be testable using `curl`.

Health:

```bash
curl http://127.0.0.1:8000/health
```

Risk summary:

```bash
curl http://127.0.0.1:8000/risks/summary
```

Workstream health:

```bash
curl http://127.0.0.1:8000/workstreams/WS-INT/health
```

Individual task risk:

```bash
curl http://127.0.0.1:8000/tasks/TASK-006/risk
```

Early warnings:

```bash
curl http://127.0.0.1:8000/api/v1/early-warnings
```

---

# 22. Running Python syntax checks

Before committing changes:

```bash
python -m py_compile app/api.py
python -m py_compile app/services/risk_engine.py
python -m py_compile app/services/health_explainer.py
python -m py_compile app/services/project_service.py
```

If the command returns without an error, Python compilation succeeded.

---

# 23. Git workflow for contributors

After making changes:

```bash
git status
```

Review changed files.

Then:

```bash
git diff
```

Stage the intended files:

```bash
git add .
```

Review the staged changes:

```bash
git diff --cached
```

Commit:

```bash
git commit -m "Describe the change"
```

Push:

```bash
git push origin main
```

Verify:

```bash
git status
```

A clean working tree should report:

```text
nothing to commit, working tree clean
```

And the branch should be up to date with:

```text
origin/main
```

---

# 24. Recommended feature-development workflow

Every new feature should follow this sequence:

```text
1. Define the business problem
        ↓
2. Define the API contract
        ↓
3. Update domain models if required
        ↓
4. Implement service logic
        ↓
5. Add API endpoint
        ↓
6. Compile / lint
        ↓
7. Start FastAPI
        ↓
8. Test with Swagger
        ↓
9. Test with curl
        ↓
10. Review git diff
        ↓
11. Commit
        ↓
12. Push to GitHub
        ↓
13. Verify repository state
```

This keeps every feature reproducible.

---

# 25. How another developer can use this repository

A new developer should be able to do:

```bash
git clone https://github.com/aiwithsunnyuk/sap-cloud-alm-ai-copilot.git
cd sap-cloud-alm-ai-copilot

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.api:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

At that point the developer can explore and execute the API without needing to understand the internal implementation first.

---

# 26. Demo data

The current prototype uses local JSON files.

Typical files:

```text
data/tasks.json
data/risks.json
data/dependencies.json
```

This is intentional.

It allows the project to be:

- Easy to clone
- Easy to run
- Easy to demonstrate
- Easy to test
- Independent of SAP credentials
- Suitable for development and experimentation

Do not place real SAP credentials, client secrets, tokens, or confidential customer data into these files.

---

# 27. Future SAP Cloud ALM integration

The next major architectural step is to replace or supplement the local JSON data layer with real SAP Cloud ALM APIs.

A future flow can be:

```text
SAP Cloud ALM
      |
      | OAuth 2.0
      v
SAP Cloud ALM API
      |
      v
Integration / Data Service
      |
      v
Risk Engine
      |
      v
Early Warning Engine
      |
      v
AI Copilot
      |
      v
Dashboard / API / Notifications
```

SAP Cloud ALM API credentials should be stored securely as environment variables or through an appropriate secrets-management mechanism.

Never commit:

```text
client_secret
client_id
password
access_token
service_key
private_key
```

to Git.

---

# 28. Environment variables

When external integrations are introduced, use environment variables.

Example:

```bash
export SAP_CALM_API_URL="..."
export SAP_CALM_CLIENT_ID="..."
export SAP_CALM_CLIENT_SECRET="..."
export SAP_CALM_TOKEN_URL="..."
```

Do not commit `.env` files containing real credentials.

Recommended `.gitignore` entries:

```text
.venv/
__pycache__/
*.pyc
.env
.DS_Store
```

---

# 29. Security principles

This project is intended to evolve into an enterprise-oriented tool.

Important principles:

1. Never commit secrets.
2. Do not expose internal credentials through API responses.
3. Validate API input.
4. Use authentication before exposing production APIs.
5. Use HTTPS in deployed environments.
6. Apply authorization to sensitive project data.
7. Log important operations without logging credentials.
8. Separate demo data from production data.
9. Treat AI-generated recommendations as decision support, not automatic authorization.
10. Require explicit approval before future agentic actions that modify enterprise systems.

---

# 30. Production roadmap

## Phase 1 - Foundation

- [x] FastAPI application
- [x] Project/task/risk/dependency data
- [x] Risk engine
- [x] Risk summary
- [x] Workstream summary
- [x] Workstream health explanation
- [x] Early-warning endpoint
- [x] Swagger documentation

## Phase 2 - API quality

- [ ] Pydantic response models
- [ ] Consistent API response contracts
- [ ] Error handling
- [ ] Unit tests
- [ ] Integration tests
- [ ] API versioning
- [ ] Better OpenAPI documentation

## Phase 3 - Intelligence

- [ ] Risk trend analysis
- [ ] Early-warning improvements
- [ ] Historical risk analysis
- [ ] AI-generated explanations
- [ ] Recommendation prioritization
- [ ] Natural-language project queries

## Phase 4 - SAP Cloud ALM integration

- [ ] SAP Cloud ALM authentication
- [ ] SAP Cloud ALM API client
- [ ] Project/task synchronization
- [ ] Risk synchronization
- [ ] Real tenant data ingestion
- [ ] Configurable tenant connection

## Phase 5 - Agentic AI

- [ ] Copilot conversation layer
- [ ] Tool calling
- [ ] Risk investigation agent
- [ ] Dependency analysis agent
- [ ] Early-warning agent
- [ ] Project status agent
- [ ] Human approval workflow
- [ ] Audit trail

## Phase 6 - User experience

- [ ] Executive dashboard
- [ ] Project manager dashboard
- [ ] Workstream dashboard
- [ ] Risk heatmap
- [ ] Early-warning cards
- [ ] AI Copilot chat interface
- [ ] Notification integration

---

# 31. Design philosophy

The project follows a simple principle:

> **Calculate first. Explain second. Act only with approval.**

The system should be able to answer:

### What is happening?

Risk and delivery metrics.

### Why is it happening?

Dependencies, blockers, risk drivers, and trends.

### What should we do?

Recommended actions.

### Should the system act automatically?

Only when the action is explicitly authorized and governed.

This separation is important for enterprise AI because project-management decisions can have operational and financial consequences.

---

# 32. Troubleshooting

## Port 8000 already in use

Find the process:

```bash
lsof -i :8000
```

Then stop it if appropriate.

Alternatively start on another port:

```bash
uvicorn app.api:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001/docs
```

---

## ModuleNotFoundError

Make sure the virtual environment is activated:

```bash
source .venv/bin/activate
```

Then reinstall dependencies:

```bash
pip install -r requirements.txt
```

Run Uvicorn from the repository root:

```bash
uvicorn app.api:app --reload
```

---

## Endpoint returns 404

Check:

```bash
curl http://127.0.0.1:8000/openapi.json
```

If the endpoint appears in the OpenAPI document, the application has registered it.

If it does not appear, verify the route exists in `app/api.py`.

---

## Swagger opens but an endpoint fails

Check:

1. The Uvicorn terminal.
2. The endpoint URL.
3. Required path parameters.
4. JSON data files.
5. Python compilation.

Run:

```bash
python -m py_compile app/api.py
```

---

## Git shows unexpected files

Run:

```bash
git status
```

Review:

```bash
git diff
```

Make sure virtual-environment and Python cache directories are ignored.

---

# 33. Contributing

Contributions are welcome.

A good contribution should:

1. Solve one clearly defined problem.
2. Keep the API backward compatible where possible.
3. Include tests for new logic.
4. Update this README when behavior changes.
5. Avoid committing credentials or customer data.
6. Use a descriptive commit message.

Suggested commit format:

```text
Add early warning API
Improve workstream health explanation
Add risk response models
Add SAP Cloud ALM integration
Add project dashboard API
```

---

# 34. License

Add the project's chosen open-source license before publishing it for broad reuse.

For example, an MIT-licensed project should include a `LICENSE` file containing the official MIT license text.

Do not describe the repository as MIT-licensed until the LICENSE file has actually been added.

---

# 35. Current project status

The repository currently represents a working **FastAPI-based SAP Cloud ALM delivery intelligence prototype**.

The backend can:

```text
Load project data
      ↓
Calculate task risk
      ↓
Aggregate project/workstream risk
      ↓
Identify blockers and highest-risk tasks
      ↓
Explain workstream health
      ↓
Generate recommended actions
      ↓
Expose results through REST APIs
      ↓
Expose APIs through Swagger/OpenAPI
```

The next major engineering improvements are:

1. Formal Pydantic response schemas.
2. Automated tests.
3. Stronger early-warning logic.
4. SAP Cloud ALM API integration.
5. AI/Copilot reasoning.
6. A user-facing dashboard.
7. Governed agentic actions.

---

# 36. Quick start

For someone who only wants to run the application:

```bash
git clone https://github.com/aiwithsunnyuk/sap-cloud-alm-ai-copilot.git
cd sap-cloud-alm-ai-copilot

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.api:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

Start with:

```text
GET /health
GET /projects
GET /tasks
GET /risks/summary
GET /workstreams/summary
GET /workstreams/WS-INT/health
GET /api/v1/early-warnings
```

You now have the SAP Cloud ALM AI Copilot backend running locally.

---

## Project direction

This repository is intentionally being built incrementally.

The target is not simply another REST API.

The longer-term objective is to build a **project-delivery intelligence layer for SAP Cloud ALM** that can:

> **Observe → Analyze → Explain → Predict → Recommend → Ask → Act**

with enterprise governance and human approval built into the final agentic workflow.
