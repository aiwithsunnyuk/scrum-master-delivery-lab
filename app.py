import csv
from pathlib import Path
import html
import streamlit as st

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"

st.set_page_config(
    page_title="Scrum Master Delivery Lab",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# Theme / UI system
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    :root {
        --bg: #080d1b;
        --panel: #10182a;
        --panel-2: #141f34;
        --panel-3: #0d1425;
        --line: #263653;
        --text: #f4f7fb;
        --muted: #98a7bd;
        --accent: #69d7ff;
        --accent-2: #9d8cff;
        --good: #63e6a5;
        --warn: #ffd166;
        --bad: #ff7d8a;
        --shadow: 0 20px 60px rgba(0,0,0,.22);
    }

    .stApp {
        background:
            radial-gradient(circle at 86% 4%, rgba(105,215,255,.09), transparent 22%),
            radial-gradient(circle at 5% 15%, rgba(157,140,255,.09), transparent 24%),
            linear-gradient(180deg, #080d1b 0%, #0a1020 55%, #080d1b 100%);
    }

    [data-testid="stSidebar"] {
        background: #0b1222;
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }

    .block-container {
        max-width: 1480px;
        padding-top: 1.55rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 { letter-spacing: -.03em; }
    h2 { margin-top: .2rem; }

    .brand {
        display:flex;
        align-items:center;
        gap:.55rem;
        margin-bottom:.15rem;
    }
    .brand-mark {
        width:30px;
        height:30px;
        display:grid;
        place-items:center;
        border:1px solid #38506f;
        border-radius:10px;
        background:linear-gradient(135deg,#172640,#101a2e);
        font-size:1rem;
    }
    .brand-name { font-weight:800; font-size:1.08rem; }
    .sidebar-sub { color:var(--muted); font-size:.76rem; margin-bottom:1rem; }
    .sidebar-section {
        color:#dbe5f4;
        font-size:.78rem;
        font-weight:750;
        text-transform:uppercase;
        letter-spacing:.09em;
        margin:.95rem 0 .4rem;
    }
    .sidebar-note {
        color:#7788a3;
        font-size:.72rem;
        line-height:1.55;
    }

    .hero {
        border:1px solid #283a59;
        border-radius:22px;
        padding:1.65rem 1.8rem 1.55rem;
        background:
            linear-gradient(135deg, rgba(17,28,48,.97), rgba(16,25,44,.86)),
            radial-gradient(circle at 90% 20%, rgba(105,215,255,.10), transparent 30%);
        box-shadow:var(--shadow);
        position:relative;
        overflow:hidden;
    }
    .hero:after {
        content:"";
        position:absolute;
        right:-80px;
        top:-110px;
        width:280px;
        height:280px;
        border:1px solid rgba(105,215,255,.10);
        border-radius:50%;
        box-shadow:0 0 0 35px rgba(105,215,255,.025), 0 0 0 70px rgba(105,215,255,.018);
    }
    .eyebrow {
        color:var(--accent);
        font-size:.68rem;
        font-weight:800;
        letter-spacing:.18em;
        text-transform:uppercase;
        margin-bottom:.45rem;
    }
    .hero h1 { margin:0; font-size:2.45rem; line-height:1.06; }
    .hero p { color:var(--muted); max-width:920px; margin:.65rem 0 0; line-height:1.55; }

    .section-head { margin:1.7rem 0 .7rem; }
    .section-kicker {
        color:#70839e;
        font-size:.66rem;
        font-weight:800;
        letter-spacing:.15em;
        text-transform:uppercase;
    }
    .section-title { font-size:1.45rem; font-weight:800; margin-top:.1rem; }
    .section-copy { color:var(--muted); font-size:.86rem; margin-top:.12rem; }

    .kpi {
        border:1px solid var(--line);
        border-radius:17px;
        background:linear-gradient(145deg, rgba(16,24,42,.94), rgba(13,20,36,.78));
        padding:1rem 1.05rem .9rem;
        min-height:124px;
        box-shadow:0 10px 30px rgba(0,0,0,.10);
    }
    .kpi-top { display:flex; justify-content:space-between; align-items:center; }
    .kpi-label { color:#8798b1; font-size:.66rem; font-weight:800; letter-spacing:.08em; }
    .kpi-dot { width:7px; height:7px; border-radius:50%; background:var(--accent); box-shadow:0 0 12px rgba(105,215,255,.65); }
    .kpi-value { font-size:2rem; font-weight:850; margin-top:.28rem; letter-spacing:-.04em; }
    .kpi-note { color:#73849d; font-size:.7rem; margin-top:.16rem; }

    .health {
        border:1px solid var(--line);
        border-radius:17px;
        background:rgba(14,22,39,.72);
        padding:.95rem 1rem;
        height:100%;
    }
    .health-title { font-weight:800; font-size:.9rem; }
    .health-copy { color:var(--muted); font-size:.75rem; margin-top:.25rem; line-height:1.45; }
    .health-pill {
        display:inline-block;
        margin-top:.55rem;
        padding:.25rem .55rem;
        border-radius:999px;
        font-size:.67rem;
        font-weight:800;
        letter-spacing:.04em;
        border:1px solid #2f4b66;
    }
    .health-good { color:var(--good); background:rgba(99,230,165,.07); }
    .health-watch { color:var(--warn); background:rgba(255,209,102,.07); }
    .health-risk { color:var(--bad); background:rgba(255,125,138,.07); }

    .journey-grid { display:grid; grid-template-columns:repeat(7,1fr); gap:.55rem; }
    .journey-card {
        border:1px solid var(--line);
        border-radius:15px;
        padding:.9rem .78rem;
        min-height:166px;
        background:linear-gradient(160deg, rgba(16,25,43,.96), rgba(12,19,34,.86));
        position:relative;
    }
    .journey-card:hover { border-color:#3a5376; }
    .journey-num { color:var(--accent); font-size:.64rem; font-weight:850; letter-spacing:.13em; }
    .journey-title { font-size:.84rem; font-weight:800; margin:.4rem 0 .45rem; line-height:1.25; }
    .journey-text { color:#8e9db3; font-size:.71rem; line-height:1.45; }
    .journey-link { color:#627895; font-size:.62rem; position:absolute; left:.78rem; bottom:.72rem; }

    .signal-card {
        border:1px solid var(--line);
        border-left:3px solid var(--accent);
        border-radius:0 14px 14px 0;
        padding:.85rem .95rem;
        background:rgba(17,27,46,.78);
        min-height:108px;
    }
    .signal-card h3 { font-size:.9rem; margin:0 0 .28rem; }
    .signal-card p { color:var(--muted); font-size:.75rem; line-height:1.5; margin:0; }

    .flow {
        border:1px solid var(--line);
        border-radius:16px;
        background:rgba(12,19,34,.72);
        padding:.8rem 1rem;
        color:#b7c4d7;
        font-size:.76rem;
        line-height:1.8;
    }
    .flow span { color:var(--accent); font-weight:800; }

    .bar-row {
        display:grid;
        grid-template-columns:78px 1fr 52px;
        gap:.65rem;
        align-items:center;
        margin:.62rem 0;
    }
    .bar-label,.bar-value { color:#93a2b8; font-size:.72rem; }
    .bar-value { text-align:right; font-weight:750; color:#c9d4e3; }
    .bar-track { height:10px; background:#1b2941; border-radius:999px; overflow:hidden; border:1px solid #22334f; }
    .bar-fill { height:100%; border-radius:999px; background:linear-gradient(90deg,var(--accent),var(--accent-2)); }

    .mini-card {
        border:1px solid var(--line);
        border-radius:15px;
        padding:.9rem;
        background:rgba(16,25,43,.74);
        min-height:112px;
    }
    .mini-label { color:#8192aa; font-size:.66rem; font-weight:800; letter-spacing:.08em; text-transform:uppercase; }
    .mini-value { font-size:1.45rem; font-weight:850; margin-top:.25rem; }
    .mini-note { color:#73849b; font-size:.7rem; margin-top:.1rem; }

    .evidence-card {
        border:1px solid var(--line);
        border-radius:15px;
        padding:1rem;
        background:linear-gradient(150deg, rgba(16,25,43,.92), rgba(12,19,34,.78));
        margin-bottom:.7rem;
    }
    .tag {
        display:inline-block;
        border:1px solid #304563;
        color:var(--accent);
        border-radius:999px;
        padding:.18rem .5rem;
        font-size:.61rem;
        font-weight:800;
        letter-spacing:.08em;
        margin-bottom:.4rem;
    }
    .evidence-card h3 { margin:.15rem 0 .35rem; font-size:1rem; }
    .evidence-card p { color:#a0aec1; font-size:.77rem; line-height:1.5; margin:.25rem 0; }
    .path { color:#667a96; font-size:.65rem; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; }

    .sim-card {
        border:1px solid #2b3d5b;
        border-radius:19px;
        padding:1.1rem;
        background:linear-gradient(145deg, rgba(18,29,49,.96), rgba(12,19,34,.84));
        box-shadow:0 15px 40px rgba(0,0,0,.14);
    }
    .decision {
        border:1px solid #2a3d5b;
        border-radius:13px;
        padding:.85rem .9rem;
        background:rgba(8,13,27,.48);
        margin:.5rem 0;
    }
    .decision-title { font-weight:800; font-size:.82rem; }
    .decision-body { color:#8999b0; font-size:.74rem; line-height:1.45; margin-top:.18rem; }

    .recruiter-banner {
        border:1px solid #23466b;
        border-radius:14px;
        background:linear-gradient(90deg, rgba(24,65,103,.72), rgba(25,47,82,.55));
        padding:.85rem 1rem;
        color:#cbeaff;
        font-size:.76rem;
        line-height:1.5;
    }

    .exec-hero {
        border:1px solid #31527a;
        border-radius:22px;
        padding:1.35rem 1.45rem;
        background:linear-gradient(135deg, rgba(19,35,60,.98), rgba(13,23,42,.90));
        margin-bottom:.9rem;
    }
    .exec-kicker { color:var(--accent); font-size:.66rem; font-weight:850; letter-spacing:.16em; text-transform:uppercase; }
    .exec-title { font-size:1.65rem; font-weight:850; margin:.35rem 0 .3rem; letter-spacing:-.03em; }
    .exec-copy { color:#a7b5c9; font-size:.82rem; line-height:1.55; max-width:900px; }
    .time-card {
        border:1px solid var(--line); border-radius:16px; padding:.95rem;
        background:rgba(15,24,42,.82); min-height:170px;
    }
    .time { color:var(--accent); font-size:.65rem; font-weight:850; letter-spacing:.12em; }
    .time-title { font-size:.95rem; font-weight:850; margin:.35rem 0 .35rem; }
    .time-copy { color:#94a4ba; font-size:.73rem; line-height:1.5; }
    .say-card {
        border:1px solid #2b4565; border-radius:15px; padding:1rem;
        background:linear-gradient(145deg, rgba(17,29,49,.92), rgba(11,19,34,.78));
    }
    .say-label { color:#7186a2; font-size:.62rem; font-weight:850; letter-spacing:.12em; text-transform:uppercase; }
    .say-text { color:#d7e0ec; font-size:.84rem; line-height:1.6; margin-top:.35rem; }
    .fit-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:.65rem; }
    .fit-card { border:1px solid var(--line); border-radius:15px; padding:.9rem; background:rgba(15,24,42,.78); min-height:125px; }
    .fit-title { font-weight:850; font-size:.82rem; margin-bottom:.3rem; }
    .fit-copy { color:#8fa0b6; font-size:.7rem; line-height:1.48; }
    .proof { color:var(--accent); font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:.62rem; margin-top:.55rem; }
    .exec-note { border-left:3px solid var(--accent); padding:.8rem 1rem; background:rgba(20,34,57,.72); border-radius:0 13px 13px 0; color:#b9c7d9; font-size:.75rem; line-height:1.55; }
    @media (max-width: 1050px) { .fit-grid { grid-template-columns:repeat(2,1fr); } }
    .lead-hero {
        border:1px solid #31527a; border-radius:22px; padding:1.35rem 1.45rem;
        background:linear-gradient(135deg, rgba(20,38,63,.98), rgba(13,23,42,.90));
        margin-bottom:.9rem;
    }
    .lead-kicker { color:var(--accent); font-size:.66rem; font-weight:850; letter-spacing:.16em; text-transform:uppercase; }
    .lead-title { font-size:1.7rem; font-weight:850; margin:.35rem 0 .3rem; letter-spacing:-.03em; }
    .lead-copy { color:#a7b5c9; font-size:.82rem; line-height:1.55; max-width:940px; }
    .lead-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:.65rem; }
    .lead-card { border:1px solid var(--line); border-radius:15px; padding:.9rem; background:rgba(15,24,42,.78); min-height:120px; }
    .lead-card-title { font-weight:850; font-size:.82rem; margin-bottom:.3rem; }
    .lead-card-copy { color:#8fa0b6; font-size:.7rem; line-height:1.48; }
    .rag { display:inline-block; padding:.2rem .5rem; border-radius:999px; font-size:.62rem; font-weight:850; letter-spacing:.06em; border:1px solid #304563; margin-top:.55rem; }
    .rag-green { color:var(--good); background:rgba(99,230,165,.07); }
    .rag-amber { color:var(--warn); background:rgba(255,209,102,.07); }
    .rag-red { color:var(--bad); background:rgba(255,125,138,.07); }
    .risk-row { border:1px solid var(--line); border-radius:13px; padding:.75rem .85rem; background:rgba(12,19,34,.68); margin:.45rem 0; }
    .risk-title { font-weight:800; font-size:.78rem; }
    .risk-copy { color:#8d9db4; font-size:.7rem; line-height:1.45; margin-top:.18rem; }
    .decision-box { border-left:3px solid var(--accent); padding:.8rem .95rem; background:rgba(20,34,57,.72); border-radius:0 13px 13px 0; margin:.5rem 0; }
    .decision-label { color:#7186a2; font-size:.61rem; font-weight:850; letter-spacing:.1em; text-transform:uppercase; }
    .decision-text { color:#c9d4e3; font-size:.75rem; line-height:1.5; margin-top:.2rem; }
    .sim-option {
        border:1px solid var(--line);
        border-radius:14px;
        padding:.75rem .9rem;
        background:rgba(12,19,34,.72);
        margin:.45rem 0;
    }
    .sim-option-best {
        border-color:#3c6b60;
        background:rgba(44,91,75,.12);
    }
    .sim-result {
        border:1px solid var(--line);
        border-radius:17px;
        padding:1rem 1.05rem;
        background:linear-gradient(145deg, rgba(17,28,48,.95), rgba(13,20,36,.82));
        margin-top:.75rem;
    }
    .sim-result-title { font-weight:850; font-size:1rem; margin:.2rem 0 .35rem; }
    .sim-result-copy { color:var(--muted); font-size:.77rem; line-height:1.55; }
    .sim-score { font-size:1.7rem; font-weight:850; }
    .decision-path {
        display:grid; grid-template-columns:repeat(4,1fr); gap:.55rem;
    }
    .decision-step {
        border:1px solid var(--line); border-radius:13px; padding:.7rem;
        background:rgba(12,19,34,.68); min-height:88px;
    }
    .decision-step .num { color:var(--accent); font-size:.62rem; font-weight:850; letter-spacing:.12em; }
    .decision-step .title { font-weight:800; font-size:.78rem; margin-top:.25rem; }
    .decision-step .copy { color:#8798b0; font-size:.67rem; line-height:1.4; margin-top:.18rem; }
    @media (max-width: 1050px) { .decision-path { grid-template-columns:repeat(2,1fr); } }
    @media (max-width: 1050px) { .lead-grid { grid-template-columns:repeat(2,1fr); } }
    .footer-note { color:#667792; font-size:.65rem; margin-top:2rem; }

    @media (max-width: 1050px) {
        .journey-grid { grid-template-columns:repeat(2,1fr); }
        .hero h1 { font-size:2rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# Data helpers
# -----------------------------------------------------------------------------
def read_csv(name):
    path = DATA / name
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as f:
            return list(csv.DictReader(f))
    except (OSError, UnicodeError):
        return []


def resolve_repo_file(name):
    raw = str(name).strip().replace("\\", "/")
    candidates = [ROOT / raw, DOCS / Path(raw).name, ROOT / "docs" / Path(raw).name, ROOT / "data" / Path(raw).name]
    for path in candidates:
        if path.exists() and path.is_file():
            return path
    return None


def read_md(name):
    path = resolve_repo_file(name)
    if not path:
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return ""


def num(value, default=0.0):
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return default


def pct(part, whole):
    return round((part / whole) * 100) if whole else 0


def goal_value(row):
    for key in ("goal_achieved", "sprint_goal_achieved", "sprint_goal", "goal"):
        if key in row and str(row.get(key, "")).strip():
            value = str(row.get(key, "")).strip().lower()
            return value in ("yes", "true", "1", "achieved", "y")
    return False


def safe_text(value):
    return html.escape(str(value or ""))


sprints = read_csv("sprint-metrics.csv")
impediments = read_csv("impediment-register.csv")
evidence = read_csv("evidence-traceability.csv")
defects = read_csv("defect-log.csv")

completed = [num(r.get("completed_points")) for r in sprints]
forecast = [num(r.get("forecast_points")) for r in sprints]
cycle = [num(r.get("median_cycle_days")) for r in sprints]
goals = [goal_value(r) for r in sprints]
velocity = completed[-1] if completed else 0
avg_completed = round(sum(completed) / len(completed), 1) if completed else 0
avg_cycle = round(sum(cycle) / len(cycle), 1) if cycle else 0
goal_pct = pct(sum(goals), len(goals))
open_impediments = [r for r in impediments if str(r.get("status", "")).strip().lower() not in ("closed", "resolved", "done")]

# Delivery health is a portfolio signal, not an individual score.
if not sprints:
    health_label, health_class, health_copy = "NO DATA", "health-watch", "Add sprint evidence to activate delivery health."
elif goal_pct >= 80 and len(open_impediments) <= 2:
    health_label, health_class, health_copy = "STABLE", "health-good", "Goals are mostly being achieved and the visible impediment load is contained."
elif goal_pct >= 60:
    health_label, health_class, health_copy = "WATCH", "health-watch", "Delivery is moving, with signals worth inspecting before they become systemic."
else:
    health_label, health_class, health_copy = "AT RISK", "health-risk", "Inspect the Sprint Goal, flow, impediments and quality signals before prescribing action."

# -----------------------------------------------------------------------------
# Navigation
# -----------------------------------------------------------------------------
pages = [
    "Executive Overview",
    "7-Milestone Journey",
    "Delivery Dashboard",
    "Impediment Center",
    "Coaching Lab",
    "Evidence Explorer",
    "Interview Simulation",
    "Executive Recruiter Mode",
    "Delivery Leadership Command Center",
    "Agile Transformation Lab",
    "Transformation Decision Simulator",
]

if "page" not in st.session_state:
    st.session_state.page = "Executive Overview"

# Navigation buttons request a page through a separate target key.
# This avoids mutating the state of the sidebar radio after its widget exists.
if "_page_target" in st.session_state:
    st.session_state.page_selector = st.session_state.pop("_page_target")

st.sidebar.markdown(
    '<div class="brand"><div class="brand-mark">🧭</div><div class="brand-name">Delivery Lab</div></div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown('<div class="sidebar-sub">Evidence-first Agile portfolio</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-section">Navigate</div>', unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigate",
    pages,
    index=pages.index(st.session_state.page),
    label_visibility="collapsed",
    key="page_selector",
)
st.session_state.page = page

st.sidebar.divider()
st.sidebar.markdown('<div class="sidebar-section">Portfolio principle</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-note"><b>GitHub</b> = source of truth<br><b>Streamlit</b> = presentation layer</div>', unsafe_allow_html=True)

with st.sidebar.expander("Local evidence status"):
    detected = sum(1 for i in range(1, 11) if (DOCS / f"milestone-{i:02d}.md").exists())
    st.write(f"M1-M10 docs detected: **{detected}/10**")
    st.write(f"Sprint metrics: **{'found' if (DATA / 'sprint-metrics.csv').exists() else 'missing'}**")
    st.write(f"Impediments: **{'found' if (DATA / 'impediment-register.csv').exists() else 'missing'}**")

st.sidebar.markdown('<div class="sidebar-section">Fast path</div>', unsafe_allow_html=True)
st.sidebar.caption("Journey → Dashboard → Evidence → Interview")
st.sidebar.markdown('<div class="sidebar-note">Synthetic portfolio scenarios. No confidential client information.</div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Shared components
# -----------------------------------------------------------------------------
def hero(title, subtitle, eyebrow="AGILE DELIVERY PORTFOLIO"):
    st.markdown(
        f'<div class="hero"><div class="eyebrow">{safe_text(eyebrow)}</div><h1>{safe_text(title)}</h1><p>{safe_text(subtitle)}</p></div>',
        unsafe_allow_html=True,
    )


def section(title, copy="", kicker=""):
    kicker_html = f'<div class="section-kicker">{safe_text(kicker)}</div>' if kicker else ""
    copy_html = f'<div class="section-copy">{safe_text(copy)}</div>' if copy else ""
    st.markdown(f'<div class="section-head">{kicker_html}<div class="section-title">{safe_text(title)}</div>{copy_html}</div>', unsafe_allow_html=True)


def kpi_row(items):
    cols = st.columns(len(items))
    for col, (label, value, note) in zip(cols, items):
        with col:
            st.markdown(
                f'<div class="kpi"><div class="kpi-top"><div class="kpi-label">{safe_text(label)}</div><div class="kpi-dot"></div></div><div class="kpi-value">{safe_text(value)}</div><div class="kpi-note">{safe_text(note)}</div></div>',
                unsafe_allow_html=True,
            )


def navigate(label, target, kind="secondary"):
    if st.button(label, use_container_width=True, type=kind):
        st.session_state._page_target = target
        st.rerun()

# -----------------------------------------------------------------------------
# Executive Overview
# -----------------------------------------------------------------------------
if page == "Executive Overview":
    hero(
        "Scrum Master Delivery Lab",
        "A practical, inspectable portfolio showing how Agile delivery is facilitated, measured, improved and coached.",
    )

    st.write("")
    kpi_row([
        ("SPRINTS ANALYSED", str(len(sprints)), "delivery evidence"),
        ("AVG COMPLETED", f"{avg_completed:g}", "story points / sprint"),
        ("GOAL ACHIEVEMENT", f"{goal_pct}%", "Sprint Goals achieved"),
        ("LATEST VELOCITY", f"{velocity:g}", "latest observed sprint"),
    ])

    st.write("")
    h1, h2 = st.columns([1.65, 1])
    with h1:
        st.markdown('<div class="health"><div class="health-title">Delivery health</div><div class="health-copy">A lightweight portfolio signal combining Sprint Goal achievement and visible impediment load. It is for inspection, not performance management.</div><span class="health-pill ' + health_class + '">' + health_label + '</span></div>', unsafe_allow_html=True)
    with h2:
        st.markdown('<div class="health"><div class="health-title">Evidence coverage</div><div class="health-copy">M1-M7 documentation is expected to remain in the repository so the presentation layer never becomes the source of truth.</div></div>', unsafe_allow_html=True)

    section("Delivery story", "One connected system from product intent to measurable improvement.", "PORTFOLIO SYSTEM")
    st.markdown('<div class="journey-grid">' + "".join(
        f'<div class="journey-card"><div class="journey-num">{n}</div><div class="journey-title">{safe_text(t)}</div><div class="journey-text">{safe_text(x)}</div><div class="journey-link">{safe_text(f)} ↗</div></div>'
        for n, t, f, x in [
            ("M1", "Product Goal & Backlog", "docs/milestone-01.md", "Value, backlog quality and refinement"),
            ("M2", "Sprint Execution", "docs/milestone-02.md", "Planning, execution and adaptation"),
            ("M3", "Impediments & Dependencies", "docs/milestone-03.md", "Visibility, escalation and dependency management"),
            ("M4", "Metrics & Transparency", "docs/milestone-04.md", "Evidence-based inspection of delivery"),
            ("M5", "Review, Retro & Improvement", "docs/milestone-05.md", "Feedback, learning and experiments"),
            ("M6", "Coaching & Stakeholders", "docs/milestone-06.md", "Conflict, coaching and influence"),
            ("M7", "Final Integration", "docs/milestone-07.md", "End-to-end Agile delivery portfolio"),
        ]
    ) + '</div>', unsafe_allow_html=True)

    section("What this demonstrates", "The portfolio is designed around observable Scrum Master behaviours.", "CAPABILITY SIGNALS")
    c1, c2, c3 = st.columns(3)
    for col, title, body in [
        (c1, "Facilitation", "Creates the conditions for productive Scrum events, shared understanding and team decisions."),
        (c2, "Transparency", "Uses delivery signals to make risks, impediments, dependencies and outcomes visible."),
        (c3, "Coaching", "Builds team ownership, stakeholder alignment and sustainable improvement rather than dependency on the Scrum Master."),
    ]:
        with col:
            st.markdown(f'<div class="signal-card"><h3>{title}</h3><p>{body}</p></div>', unsafe_allow_html=True)

    section("Portfolio access", "Jump directly to the evidence source or the in-app evidence view.", "RECRUITER ACCESS")
    a, b = st.columns(2)
    with a:
        st.link_button(
            "View GitHub repository ↗",
            "https://github.com/aiwithsunnyuk/scrum-master-delivery-lab",
            use_container_width=True,
        )
    with b:
        navigate("Open Evidence Explorer", "Evidence Explorer")

    section("Recruiter fast path", "A three-step route through the portfolio.", "INTERVIEW READY")
    st.markdown('<div class="recruiter-banner"><b>1 · Journey</b> understand the delivery narrative &nbsp;→&nbsp; <b>2 · Dashboard</b> inspect the evidence &nbsp;→&nbsp; <b>3 · Simulation</b> practice how the Scrum Master thinks under delivery pressure.</div>', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    with a: navigate("Explore the 7 milestones", "7-Milestone Journey", "primary")
    with b: navigate("Inspect delivery evidence", "Delivery Dashboard")
    with c: navigate("Run a Scrum Master scenario", "Interview Simulation")

# -----------------------------------------------------------------------------
# M8.3 Executive Recruiter Mode
# -----------------------------------------------------------------------------
elif page == "Executive Recruiter Mode":
    st.markdown(
        '<div class="exec-hero"><div class="exec-kicker">M8.3 · EXECUTIVE RECRUITER MODE</div><div class="exec-title">A 3-minute recruiter walkthrough</div><div class="exec-copy">A concise presentation mode designed to help a hiring manager understand the delivery capability, inspect the evidence, and see how the Scrum Master thinks under pressure.</div></div>',
        unsafe_allow_html=True,
    )

    section("The recruiter takeaway", "Lead with capability and evidence, not a tour of every file.", "EXECUTIVE SUMMARY")
    kpi_row([
        ("DELIVERY SYSTEM", "M1–M7", "end-to-end evidence"),
        ("LEADERSHIP SIGNAL", "Coaching", "influence without authority"),
        ("INSPECTION", "Metrics", "flow, predictability, quality"),
        ("INTERVIEW", "M8.2", "scenario-based practice"),
    ])

    section("Three-minute route", "Use this sequence when sharing the portfolio screen with a recruiter or hiring manager.", "WALKTHROUGH")
    cols = st.columns(4)
    steps = [
        ("0:00–0:40", "1 · Position", "State the problem you solve: create transparency, facilitate delivery, remove systemic friction and help teams improve."),
        ("0:40–1:25", "2 · Show the system", "Use M1–M7 as one delivery story: intent → backlog → Sprint → impediments → metrics → review/retro → coaching."),
        ("1:25–2:20", "3 · Prove it", "Open the Dashboard and Evidence Explorer. Point to real artifacts, not just claims: metrics, impediment ownership and improvement experiments."),
        ("2:20–3:00", "4 · Demonstrate judgement", "Run one M8.2 scenario. Explain the decision path, trade-offs and learning rather than reciting Scrum terminology."),
    ]
    for col, (time, title, body) in zip(cols, steps):
        with col:
            st.markdown(f'<div class="time-card"><div class="time">{time}</div><div class="time-title">{safe_text(title)}</div><div class="time-copy">{safe_text(body)}</div></div>', unsafe_allow_html=True)

    section("Your executive opening", "A short positioning statement you can use before navigating the portfolio.", "SPEAKER NOTE")
    st.markdown('<div class="say-card"><div class="say-label">Suggested 30–40 second opening</div><div class="say-text">“This portfolio is designed to show how I operate as a Scrum Master beyond facilitating ceremonies. I start with product intent and backlog quality, help the team execute and adapt inside the Sprint, make impediments and dependencies transparent, use delivery metrics for inspection, turn feedback into improvement experiments, and coach stakeholders and teams through conflict and pressure. The repository contains the evidence, while this interface makes the delivery story easy to inspect.”</div></div>', unsafe_allow_html=True)

    section("What a recruiter should be able to see", "Four capability signals to reinforce during the walkthrough.", "ROLE FIT")
    fit = [
        ("Facilitation", "Creates productive decision-making conditions instead of becoming the person who makes every decision.", "M2 · M6"),
        ("Delivery transparency", "Uses Sprint Goals, flow, impediments, quality and feedback to make delivery reality visible.", "M3 · M4"),
        ("Continuous improvement", "Converts retrospective observations into owned, measurable experiments and inspects the result.", "M5"),
        ("Leadership & coaching", "Handles stakeholder pressure, conflict and bypassing behaviour through coaching and clear accountabilities.", "M6 · M8.2"),
    ]
    st.markdown('<div class="fit-grid">' + ''.join(f'<div class="fit-card"><div class="fit-title">{safe_text(t)}</div><div class="fit-copy">{safe_text(b)}</div><div class="proof">Evidence: {safe_text(e)}</div></div>' for t,b,e in fit) + '</div>', unsafe_allow_html=True)

    section("Evidence-first navigation", "Move only when the conversation needs proof. Avoid clicking through every document.", "LIVE DEMO")
    st.markdown('<div class="exec-note"><b>Recommended sequence:</b> Executive Recruiter Mode → 7-Milestone Journey → Delivery Dashboard → one Evidence Explorer artifact → Interview Simulation. The objective is not to demonstrate the application itself; it is to demonstrate your judgement as a Scrum Master.</div>', unsafe_allow_html=True)
    a, b, c, d = st.columns(4)
    with a: navigate("Open the journey", "7-Milestone Journey", "primary")
    with b: navigate("Open dashboard", "Delivery Dashboard")
    with c: navigate("Open evidence", "Evidence Explorer")
    with d: navigate("Run interview", "Interview Simulation")

    section("Close with impact", "Finish by connecting evidence to the role rather than ending on the technology.", "30-SECOND CLOSE")
    st.markdown('<div class="say-card"><div class="say-label">Suggested close</div><div class="say-text">“The point of the portfolio is not that I can maintain Scrum artifacts. It is that I can make delivery transparent, facilitate difficult conversations, help teams resolve constraints, and turn evidence into better decisions. The same pattern is what I would bring into a new team or delivery environment.”</div></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# M9 Delivery Leadership Command Center
# -----------------------------------------------------------------------------
elif page == "Delivery Leadership Command Center":
    st.markdown(
        '<div class="lead-hero"><div class="lead-kicker">M9 · DELIVERY LEADERSHIP & TRANSFORMATION LAB</div><div class="lead-title">Executive Delivery Command Center</div><div class="lead-copy">A practical layer above Sprint-level Scrum: release readiness, delivery risk, cross-team dependencies, governance signals and executive decision support. The purpose is not to create more reporting. It is to make the right delivery conversations visible at the right level.</div></div>',
        unsafe_allow_html=True,
    )

    risks = read_csv("delivery-risks.csv")
    deps = read_csv("dependencies.csv")
    releases = read_csv("release-readiness.csv")
    decisions = read_csv("decision-log.csv")

    open_risks = [r for r in risks if str(r.get("status", "")).lower() not in ("closed", "resolved", "done")]
    active_deps = [r for r in deps if str(r.get("status", "")).lower() not in ("closed", "resolved", "done")]
    critical_risks = [r for r in open_risks if str(r.get("severity", "")).lower() in ("high", "critical", "red")]
    ready_count = sum(str(r.get("status", "")).lower() in ("ready", "green", "go") for r in releases)
    readiness_pct = round((ready_count / len(releases)) * 100) if releases else 0

    section("Leadership signal", "A compact view of what needs inspection, action or decision beyond the Sprint boundary.", "EXECUTIVE VIEW")
    kpi_row([
        ("RELEASE READINESS", f"{readiness_pct}%", "evidence-based readiness"),
        ("OPEN RISKS", str(len(open_risks)), f"{len(critical_risks)} high/critical"),
        ("ACTIVE DEPENDENCIES", str(len(active_deps)), "cross-team constraints"),
        ("DECISIONS LOGGED", str(len(decisions)), "traceable leadership decisions"),
    ])

    section("Four leadership lenses", "Use the lenses together. A single red metric rarely explains the delivery problem.", "DELIVERY SYSTEM")
    st.markdown('<div class="lead-grid">' + ''.join([
        '<div class="lead-card"><div class="lead-card-title">Release readiness</div><div class="lead-card-copy">Ask whether scope, quality, dependencies, operational readiness and ownership support the intended release decision.</div><span class="rag rag-amber">INSPECT</span></div>',
        '<div class="lead-card"><div class="lead-card-title">Delivery risk</div><div class="lead-card-copy">Separate known risk from active impediment. Give each material risk an owner, response and review point.</div><span class="rag rag-amber">MANAGE</span></div>',
        '<div class="lead-card"><div class="lead-card-title">Dependencies</div><div class="lead-card-copy">Make cross-team constraints visible early enough for teams to negotiate sequencing, ownership or escalation.</div><span class="rag rag-amber">COORDINATE</span></div>',
        '<div class="lead-card"><div class="lead-card-title">Governance</div><div class="lead-card-copy">Turn delivery signals into concise decisions, actions and support requests without creating ceremony theatre.</div><span class="rag rag-green">ENABLE</span></div>',
    ]) + '</div>', unsafe_allow_html=True)

    section("Release readiness", "Readiness is a conversation supported by evidence, not a decorative percentage.", "RELEASE")
    if releases:
        for r in releases:
            status = str(r.get("status", "Unknown")).strip()
            low = status.lower()
            cls = "rag-green" if low in ("ready", "green", "go") else "rag-red" if low in ("blocked", "red", "no-go") else "rag-amber"
            title = r.get("item") or r.get("release") or r.get("area") or "Readiness item"
            detail = r.get("evidence") or r.get("notes") or r.get("owner") or ""
            st.markdown(f'<div class="risk-row"><div class="risk-title">{safe_text(title)} <span class="rag {cls}">{safe_text(status.upper())}</span></div><div class="risk-copy">{safe_text(detail)}</div></div>', unsafe_allow_html=True)
    else:
        st.info("No release-readiness evidence detected yet.")

    section("Top delivery risks", "Focus leadership attention on exposure and response, not on creating a longer risk list.", "RISK REVIEW")
    if open_risks:
        for r in open_risks[:6]:
            sev = str(r.get("severity", "watch")).strip().lower()
            cls = "rag-red" if sev in ("high", "critical", "red") else "rag-amber"
            title = r.get("risk") or r.get("title") or r.get("description") or "Delivery risk"
            owner = r.get("owner") or "Owner not recorded"
            response = r.get("mitigation") or r.get("response") or r.get("next_action") or "Response not recorded"
            st.markdown(f'<div class="risk-row"><div class="risk-title">{safe_text(title)} <span class="rag {cls}">{safe_text(sev.upper())}</span></div><div class="risk-copy"><b>Owner:</b> {safe_text(owner)} · <b>Response:</b> {safe_text(response)}</div></div>', unsafe_allow_html=True)
    else:
        st.success("No open delivery risks detected.")

    section("Dependency watch", "A dependency becomes leadership-relevant when ownership, timing or impact threatens the delivery path.", "CROSS-TEAM")
    if active_deps:
        for d in active_deps[:6]:
            title = d.get("dependency") or d.get("description") or d.get("item") or "Dependency"
            owner = d.get("owner") or d.get("dependency_owner") or "Owner not recorded"
            due = d.get("due_date") or d.get("needed_by") or "Timing not recorded"
            impact = d.get("impact") or d.get("risk") or "Impact not recorded"
            st.markdown(f'<div class="risk-row"><div class="risk-title">{safe_text(title)}</div><div class="risk-copy"><b>Owner:</b> {safe_text(owner)} · <b>Needed by:</b> {safe_text(due)} · <b>Impact:</b> {safe_text(impact)}</div></div>', unsafe_allow_html=True)
    else:
        st.success("No active cross-team dependencies detected.")

    section("Decisions & executive support", "The Scrum Master should make decision needs explicit while preserving accountability with the right owner.", "GOVERNANCE")
    if decisions:
        for d in decisions[:6]:
            decision = d.get("decision") or d.get("request") or d.get("topic") or "Decision"
            owner = d.get("decision_owner") or d.get("owner") or "Decision owner not recorded"
            status = d.get("status") or "Open"
            st.markdown(f'<div class="decision-box"><div class="decision-label">{safe_text(status)} · {safe_text(owner)}</div><div class="decision-text">{safe_text(decision)}</div></div>', unsafe_allow_html=True)
    else:
        st.info("No decision-log evidence detected yet.")

    section("Executive communication pattern", "Keep the leadership conversation short, evidence-backed and decision-oriented.", "STATUS BRIEF")
    st.markdown('<div class="say-card"><div class="say-label">Suggested executive structure</div><div class="say-text"><b>1 · What changed?</b> State the delivery signal. <b>2 · Why does it matter?</b> Connect it to Sprint Goal, release scope, quality or timing. <b>3 · What is being done?</b> Name the owner and response. <b>4 · What decision or support is required?</b> Make the ask explicit. <b>5 · When will we inspect again?</b> Close the loop.</div></div>', unsafe_allow_html=True)

    section("Transformation scenario", "The environment is Agile on paper but still behaves like command-and-control. The Scrum Master must change the system, not merely facilitate more meetings.", "COACHING CHALLENGE")
    st.markdown('<div class="decision-box"><div class="decision-label">Scenario</div><div class="decision-text">A manager asks for daily individual status, a Product Owner is overloaded, stakeholders bypass the PO, and teams are being pressured to increase velocity. Your response should protect transparency, restore clear accountabilities, use evidence to challenge the request, and create a sustainable operating agreement.</div></div>', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    with a: navigate("Open M6 coaching evidence", "Coaching Lab", "primary")
    with b: navigate("Run an interview scenario", "Interview Simulation")
    with c: navigate("Return to recruiter mode", "Executive Recruiter Mode")

# -----------------------------------------------------------------------------
# M10 Agile Transformation Lab
# -----------------------------------------------------------------------------
elif page == "Agile Transformation Lab":
    st.markdown(
        '<div class="lead-hero"><div class="lead-kicker">M10 · AGILE TRANSFORMATION & OPERATING MODEL</div><div class="lead-title">Transformation Lab</div><div class="lead-copy">Move from managing delivery signals to improving the system around delivery. Assess maturity, diagnose constraints, design a target operating model, pilot changes and measure outcomes.</div></div>',
        unsafe_allow_html=True,
    )
    maturity = read_csv("agile-maturity.csv")
    roadmap = read_csv("transformation-roadmap.csv")
    section("Transformation model", "A transformation is a sequence of evidence-based changes, not a rollout of ceremonies.", "OPERATING MODEL")
    st.markdown('<div class="flow"><span>Assess</span> → <span>Diagnose</span> → <span>Design</span> → <span>Align</span> → <span>Pilot</span> → <span>Measure</span> → <span>Scale</span> → <span>Sustain</span></div>', unsafe_allow_html=True)

    section("Agile maturity baseline", "Use the baseline to start a conversation about system conditions. It is not an individual performance score.", "ASSESS")
    if maturity:
        for r in maturity:
            dim = r.get("dimension", "Dimension")
            cur = r.get("current_level", "-")
            target = r.get("target_level", "-")
            priority = r.get("priority", "Watch")
            evidence = r.get("evidence", "")
            cls = "rag-red" if priority.lower() == "high" else "rag-amber"
            st.markdown(f'<div class="risk-row"><div class="risk-title">{safe_text(dim)} <span class="rag {cls}">{safe_text(priority.upper())}</span></div><div class="risk-copy"><b>Current:</b> {safe_text(cur)}/5 · <b>Target:</b> {safe_text(target)}/5 · {safe_text(evidence)}</div></div>', unsafe_allow_html=True)

    section("Current-state diagnosis", "Start with observable behaviours and constraints before prescribing a solution.", "DIAGNOSE")
    st.markdown('<div class="lead-grid"><div class="lead-card"><div class="lead-card-title">Command-and-control signals</div><div class="lead-card-copy">Individual status requests, velocity pressure and stakeholder bypass routes can reduce autonomy and distort delivery signals.</div></div><div class="lead-card"><div class="lead-card-title">System constraints</div><div class="lead-card-copy">PO capacity, dependency timing and decision latency can create delays that a single team cannot solve alone.</div></div><div class="lead-card"><div class="lead-card-title">Transformation response</div><div class="lead-card-copy">Change accountabilities, decision paths and behaviours first. Add tools or ceremonies only when evidence shows they are needed.</div></div></div>', unsafe_allow_html=True)

    section("Target operating model", "Connect existing Scrum, delivery leadership and coaching practices into one lightweight operating system.", "DESIGN")
    st.markdown('<div class="decision-box"><div class="decision-label">TARGET STATE</div><div class="decision-text"><b>Product:</b> clear decision ownership. <b>Teams:</b> protected Sprint execution and visible flow. <b>Leadership:</b> concise evidence, risks and decisions. <b>Stakeholders:</b> structured feedback through the Product Owner and Sprint Review. <b>Cross-team:</b> dependencies surfaced early and owned explicitly.</div></div>', unsafe_allow_html=True)

    section("Transformation roadmap", "Every phase has a hypothesis, ownership and an inspection signal.", "CHANGE")
    for r in roadmap:
        st.markdown(f'<div class="risk-row"><div class="risk-title">{safe_text(r.get("phase", "Phase"))} <span class="rag rag-amber">{safe_text(r.get("timing", ""))}</span></div><div class="risk-copy"><b>Hypothesis:</b> {safe_text(r.get("hypothesis", ""))} · <b>Owner:</b> {safe_text(r.get("owner", ""))} · <b>Success:</b> {safe_text(r.get("success_signal", ""))}</div></div>', unsafe_allow_html=True)

    section("Coaching and change", "Transformation sticks when people change behaviour because the system supports the new behaviour.", "ENABLE")
    st.markdown('<div class="say-card"><div class="say-label">Coaching pattern</div><div class="say-text"><b>Observe</b> the behaviour → <b>Ask</b> questions → <b>Reflect</b> on impact → <b>Experiment</b> with a small change → <b>Inspect</b> evidence → <b>Reinforce</b> what works.</div></div>', unsafe_allow_html=True)

    section("Outcome measurement", "Transformation success is a balanced signal, not a single maturity score.", "MEASURE")
    kpi_row([
        ("FLOW", "Cycle time", "inspect stability"),
        ("OUTCOME", "Sprint Goals", "inspect value"),
        ("QUALITY", "Defects", "inspect built-in quality"),
        ("SYSTEM", "Decision latency", "inspect organisational flow"),
    ])
    st.markdown('<div class="exec-note"><b>Senior Scrum Master interview lens:</b> “I would not begin by declaring the organisation immature. I would establish evidence, identify the system constraint, align the right owners, run a small experiment and inspect whether the outcome improved.”</div>', unsafe_allow_html=True)
    a,b,c=st.columns(3)
    with a: navigate("Open M9 delivery leadership", "Delivery Leadership Command Center", "primary")
    with b: navigate("Open M6 coaching evidence", "Coaching Lab")
    with c: navigate("Return to recruiter mode", "Executive Recruiter Mode")

# -----------------------------------------------------------------------------
# M10.1 Transformation Decision Simulator
# -----------------------------------------------------------------------------
elif page == "Transformation Decision Simulator":
    hero(
        "Transformation Decision Simulator",
        "Practice evidence-based transformation judgement: diagnose the constraint, choose a focused intervention, inspect the consequence and decide what to do next.",
        "M10.1 · TRANSFORMATION JUDGEMENT",
    )
    decisions = read_csv("transformation-decisions.csv")
    scenario_names = []
    for row in decisions:
        name = str(row.get("scenario", "")).strip()
        if name and name not in scenario_names:
            scenario_names.append(name)

    if not decisions or not scenario_names:
        st.warning("data/transformation-decisions.csv was not found.")
    else:
        scenario_key = "tds_scenario"
        option_key = "tds_option"
        reveal_key = "tds_reveal"
        if scenario_key not in st.session_state:
            st.session_state[scenario_key] = scenario_names[0]
        if option_key not in st.session_state:
            st.session_state[option_key] = ""
        if reveal_key not in st.session_state:
            st.session_state[reveal_key] = False

        scenario = st.selectbox("Transformation scenario", scenario_names, key=scenario_key)
        rows = [r for r in decisions if str(r.get("scenario", "")).strip() == scenario]
        context = rows[0]

        section("Current-state evidence", "Start from observable symptoms and system constraints. Do not jump straight to a solution.", "INSPECT")
        st.markdown(f'<div class="sim-card"><div style="font-size:1.02rem;font-weight:800;line-height:1.55">{safe_text(context.get("situation", ""))}</div></div>', unsafe_allow_html=True)

        section("Decision point", "Choose the smallest intervention that addresses the demonstrated constraint. The simulator intentionally includes tempting but weak options.", "FACILITATE")
        options = [str(r.get("option", "")).strip() for r in rows]
        choice = st.radio("Select your first intervention", options, key=option_key, label_visibility="collapsed")

        selected_row = next((r for r in rows if str(r.get("option", "")).strip() == choice), rows[0])
        a,b,c = st.columns(3)
        with a:
            st.markdown(f'<div class="mini-card"><div class="mini-label">Decision quality</div><div class="sim-score">{safe_text(selected_row.get("quality", ""))}</div><div class="mini-note">practice signal</div></div>', unsafe_allow_html=True)
        with b:
            st.markdown(f'<div class="mini-card"><div class="mini-label">Primary constraint</div><div class="mini-value">{safe_text(context.get("constraint", ""))}</div><div class="mini-note">what the evidence points toward</div></div>', unsafe_allow_html=True)
        with c:
            st.markdown(f'<div class="mini-card"><div class="mini-label">Next inspection</div><div class="mini-value">{safe_text(selected_row.get("next_signal", ""))}</div><div class="mini-note">what should change if the intervention works</div></div>', unsafe_allow_html=True)

        if st.button("Inspect consequence", type="primary", use_container_width=True):
            st.session_state[reveal_key] = True

        if st.session_state[reveal_key]:
            quality = str(selected_row.get("quality", "")).strip().lower()
            best = quality == "strong"
            if best:
                st.success("Strong transformation judgement: the intervention addresses the demonstrated constraint without over-prescribing process.")
            elif quality == "mixed":
                st.warning("Mixed judgement: there is a useful element, but the intervention does not fully address the system constraint.")
            else:
                st.error("Weak first move: this treats a symptom or adds control without addressing the demonstrated constraint.")

            st.markdown(f'<div class="sim-result"><div class="section-kicker">RATIONALE</div><div class="sim-result-title">Why this choice matters</div><div class="sim-result-copy">{safe_text(selected_row.get("rationale", ""))}</div><br><div class="section-kicker">LIKELY CONSEQUENCE</div><div class="sim-result-title">What may happen next</div><div class="sim-result-copy">{safe_text(selected_row.get("consequence", ""))}</div><br><div class="section-kicker">INSPECTION</div><div class="sim-result-title">What to inspect</div><div class="sim-result-copy">{safe_text(selected_row.get("next_signal", ""))}</div></div>', unsafe_allow_html=True)

            section("Decision loop", "A transformation decision is not complete until the result is inspected and the response is adapted.", "ADAPT")
            st.markdown('<div class="decision-path"><div class="decision-step"><div class="num">01</div><div class="title">Inspect</div><div class="copy">Use evidence to identify the constraint.</div></div><div class="decision-step"><div class="num">02</div><div class="title">Intervene</div><div class="copy">Choose a focused change with clear ownership.</div></div><div class="decision-step"><div class="num">03</div><div class="title">Measure</div><div class="copy">Inspect an observable outcome signal.</div></div><div class="decision-step"><div class="num">04</div><div class="title">Adapt</div><div class="copy">Continue, change or stop based on evidence.</div></div></div>', unsafe_allow_html=True)

        section("Interviewer lens", "The simulator is designed to expose judgement, not memorised Agile vocabulary.", "INTERVIEW")
        st.markdown('<div class="exec-note"><b>Listen for:</b> system thinking, evidence before prescription, clear accountabilities, small experiments, explicit success signals and willingness to adapt when the intervention does not work.</div>', unsafe_allow_html=True)

        a,b,c = st.columns(3)
        with a: navigate("Return to M10 transformation", "Agile Transformation Lab", "primary")
        with b: navigate("Open M9 delivery leadership", "Delivery Leadership Command Center")
        with c: navigate("Run interview simulation", "Interview Simulation")

# -----------------------------------------------------------------------------
# Journey
# -----------------------------------------------------------------------------
elif page == "7-Milestone Journey":
    hero("The Agile Delivery Journey", "Ten capability milestones, connected as one delivery system rather than ten disconnected documents.", "PORTFOLIO STORY")
    section("From intent to improvement", "Each milestone answers a different delivery question and leaves inspectable evidence.", "SEVEN CAPABILITIES")

    journey = [
        ("M10", "Agile Transformation", "docs/milestone-10.md", "Assess the system, design an operating model and lead sustainable change."),
        ("M1", "Product Goal & Backlog", "docs/milestone-01.md", "Turn product intent into an actionable, refined backlog."),
        ("M2", "Sprint Execution", "docs/milestone-02.md", "Plan, execute, inspect and adapt inside the Sprint."),
        ("M3", "Impediments & Dependencies", "docs/milestone-03.md", "Make blockers visible, establish ownership and escalate deliberately."),
        ("M4", "Metrics & Transparency", "docs/milestone-04.md", "Use evidence to inspect flow, predictability, quality and outcomes."),
        ("M5", "Review, Retro & Improvement", "docs/milestone-05.md", "Convert feedback and delivery signals into experiments."),
        ("M6", "Coaching & Stakeholders", "docs/milestone-06.md", "Facilitate conflict, coach behaviour and influence without authority."),
        ("M7", "Final Integration", "docs/milestone-07.md", "Connect the artifacts into an interview-ready delivery narrative."),
    ]

    for i in range(0, len(journey), 2):
        cols = st.columns(2)
        for col, item in zip(cols, journey[i:i+2]):
            n, title, file, desc = item
            with col:
                st.markdown(f'<div class="evidence-card"><div class="tag">{n}</div><h3>{safe_text(title)}</h3><p>{safe_text(desc)}</p><div class="path">{safe_text(file)}</div></div>', unsafe_allow_html=True)
                with st.expander("Inspect evidence", expanded=False):
                    text = read_md(file)
                    if text:
                        st.markdown(text[:9000])
                    else:
                        st.warning(f"{file} was not found in this checkout. Confirm the M1-M7 docs are present under docs/.")

# -----------------------------------------------------------------------------
# Delivery Dashboard
# -----------------------------------------------------------------------------
elif page == "Delivery Dashboard":
    hero("Delivery Dashboard", "Inspect delivery signals without turning metrics into individual performance targets.", "DELIVERY HEALTH")
    kpi_row([
        ("AVERAGE COMPLETED", f"{avg_completed:g}", "points / sprint"),
        ("AVERAGE CYCLE", f"{avg_cycle:g}", "median days / sprint"),
        ("GOAL ACHIEVEMENT", f"{goal_pct}%", "Sprint Goals achieved"),
        ("OPEN IMPEDIMENTS", str(len(open_impediments)), "visible unresolved items"),
    ])

    section("Delivery flow", "A compact view of completed work across the five-sprint evidence sample.", "INSPECT")
    max_completed = max(completed) if completed else 1
    for row, value in zip(sprints, completed):
        st.markdown(f'<div class="bar-row"><div class="bar-label">{safe_text(row.get("sprint", "Sprint"))}</div><div class="bar-track"><div class="bar-fill" style="width:{(value/max_completed)*100:.1f}%"></div></div><div class="bar-value">{value:g}</div></div>', unsafe_allow_html=True)

    section("Forecast vs completed", "Useful for discussing predictability and Sprint Planning assumptions, not for grading a team.", "PREDICTABILITY")
    max_fc = max(forecast + completed) if (forecast or completed) else 1
    for row, fc, done in zip(sprints, forecast, completed):
        width = (done / max_fc) * 100 if max_fc else 0
        st.markdown(f'<div class="bar-row"><div class="bar-label">{safe_text(row.get("sprint", "Sprint"))}</div><div class="bar-track"><div class="bar-fill" style="width:{width:.1f}%"></div></div><div class="bar-value">{done:g}/{fc:g}</div></div>', unsafe_allow_html=True)

    section("Sprint inspection table", "The raw evidence remains visible beneath the visual summary.", "SOURCE DATA")
    if sprints:
        cols = ["sprint", "capacity", "forecast_points", "completed_points", "goal_achieved", "median_cycle_days", "spillover_points"]
        available = [c for c in cols if c in sprints[0]]
        st.dataframe([{c: r.get(c, "") for c in available} for r in sprints], use_container_width=True, hide_index=True)
    else:
        st.warning("sprint-metrics.csv was not found.")
    st.caption("Interpretation: metrics support inspection and adaptation. They are not individual performance targets.")

# -----------------------------------------------------------------------------
# Impediment Center
# -----------------------------------------------------------------------------
elif page == "Impediment Center":
    hero("Impediment Center", "A visible flow from detection to ownership, escalation, resolution and learning.", "FLOW & BLOCKERS")
    sev = {}
    for r in impediments:
        key = str(r.get("severity", "Unknown")).strip() or "Unknown"
        sev[key] = sev.get(key, 0) + 1

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f'<div class="mini-card"><div class="mini-label">Open impediments</div><div class="mini-value">{len(open_impediments)}</div><div class="mini-note">unresolved in current evidence</div></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="mini-card"><div class="mini-label">Total logged</div><div class="mini-value">{len(impediments)}</div><div class="mini-note">visible impediment register</div></div>', unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="mini-card"><div class="mini-label">Severity levels</div><div class="mini-value">{len(sev)}</div><div class="mini-note">classification signal</div></div>', unsafe_allow_html=True)

    section("Impediment operating model", "The Scrum Master facilitates the flow; ownership stays with the appropriate people or groups.", "MAKE BLOCKERS FLOW")
    st.markdown('<div class="flow"><span>Detect</span> → <span>Classify</span> → <span>Make transparent</span> → <span>Assign ownership</span> → <span>Facilitate resolution</span> → <span>Inspect aging</span> → <span>Close</span> → <span>Learn</span></div>', unsafe_allow_html=True)

    section("Visible register", "Use this view to discuss ownership, escalation and learning rather than simply counting blockers.", "EVIDENCE")
    if impediments:
        for r in impediments:
            status = str(r.get("status", "")).strip()
            closed = status.lower() in ("closed", "resolved", "done")
            badge = "RESOLVED" if closed else "OPEN"
            badge_class = "health-good" if closed else "health-watch"
            st.markdown(f'<div class="evidence-card"><div class="tag {badge_class}">{badge} · {safe_text(r.get("severity", ""))}</div><h3>{safe_text(r.get("id", ""))} · {safe_text(r.get("impediment", ""))}</h3><p><b>Sprint:</b> {safe_text(r.get("sprint", ""))} &nbsp; <b>Owner:</b> {safe_text(r.get("owner", ""))} &nbsp; <b>Status:</b> {safe_text(status)}</p><p><b>Next action:</b> {safe_text(r.get("next_action", ""))}</p></div>', unsafe_allow_html=True)
    else:
        st.info("impediment-register.csv was not found.")

# -----------------------------------------------------------------------------
# Coaching Lab
# -----------------------------------------------------------------------------
elif page == "Coaching Lab":
    hero("Coaching & Stakeholder Lab", "Practical scenarios for conflict facilitation, stakeholder pressure and influence without authority.", "SENIOR SCRUM MASTER")
    section("Four situations, four facilitation moves", "The focus is on behaviour, decision paths and ownership rather than heroics from the Scrum Master.", "COACHING PRACTICE")

    scenarios = [
        ("Stakeholder pressure", "A stakeholder requests mid-Sprint scope changes.", "Protect the Sprint Goal, make impact transparent, route prioritisation through the Product Owner and facilitate the trade-off."),
        ("PO vs Engineering conflict", "Product urgency and technical constraints are pulling in different directions.", "Create a shared problem statement, surface evidence and options, then facilitate a decision owned by the appropriate accountabilities."),
        ("Bypassing the Product Owner", "Developers feel requests are entering directly from stakeholders.", "Coach the team and stakeholders toward a clear decision path while preserving transparency and the Product Owner's accountability for value ordering."),
        ("Cross-team dependency", "Another team controls a dependency that threatens Sprint progress.", "Make the dependency visible, clarify ownership and next action, use cross-team coordination and escalate when the team cannot resolve it alone."),
    ]

    for title, situation, response in scenarios:
        with st.expander(title, expanded=False):
            st.markdown(f"**Situation**  \n{situation}")
            st.markdown(f"**Facilitation approach**  \n{response}")

    section("Coaching principle", "Sustainable Scrum Master impact increases when the team and stakeholders become more capable of solving problems themselves.", "OPERATING PRINCIPLE")
    st.success("Facilitate and coach rather than becoming the permanent owner of every problem.")

# -----------------------------------------------------------------------------
# Evidence Explorer
# -----------------------------------------------------------------------------
elif page == "Evidence Explorer":
    hero("Evidence Explorer", "Map a capability to its artifact, scenario and interview conversation.", "INTERVIEW READINESS")
    if not evidence:
        st.warning("data/evidence-traceability.csv was not found.")
    else:
        filter_text = st.text_input("Filter capability or scenario", placeholder="e.g. impediment, coaching, metrics")
        rows = evidence if not filter_text else [r for r in evidence if filter_text.lower() in " ".join(str(v) for v in r.values()).lower()]
        st.caption(f"Showing {len(rows)} of {len(evidence)} evidence mappings")
        for r in rows:
            capability = r.get("capability", "Capability")
            artifact = r.get("evidence_file", r.get("artifact", r.get("evidence", "")))
            question = r.get("interview_question", r.get("question", ""))
            scenario = r.get("scenario", "")
            st.markdown(f'<div class="evidence-card"><div class="tag">CAPABILITY</div><h3>{safe_text(capability)}</h3><p><b>Evidence:</b> {safe_text(artifact)}</p><p><b>Scenario:</b> {safe_text(scenario)}</p><p><b>Interview:</b> {safe_text(question)}</p></div>', unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# M8.2 Interactive Interview Simulation
# -----------------------------------------------------------------------------
elif page == "Interview Simulation":
    hero(
        "Interactive Interview Simulation",
        "Practice answering senior Scrum Master questions under delivery pressure, then inspect your answer against an evidence-based rubric.",
        "M8.2 · INTERVIEW SIMULATOR",
    )

    scenarios = [
        {
            "id": "SM-01",
            "difficulty": "Senior",
            "theme": "Stakeholder pressure",
            "prompt": "A senior stakeholder asks the Developers to add two urgent items during the Sprint. The Product Owner is unavailable for the next few hours. The stakeholder says, 'Just get it done.' What do you do?",
            "signals": ["Protect Sprint Goal", "Make impact transparent", "Route ordering through Product Owner", "Facilitate trade-off", "Avoid becoming gatekeeper"],
            "strong": "A strong answer protects the Sprint Goal without becoming rigid: clarify the request and urgency, make impact on the current Sprint transparent, connect the stakeholder and Product Owner decision path, and help the Developers avoid accepting unplanned work through an informal side channel.",
            "keywords": {
                "goal": ["sprint goal", "goal"],
                "transparency": ["impact", "transparent", "visibility", "trade-off", "tradeoff"],
                "po": ["product owner", "po", "ordering", "priorit"],
                "facilitation": ["facilitate", "conversation", "decision", "alignment"],
                "team": ["developers", "development team", "team"],
            },
        },
        {
            "id": "SM-02",
            "difficulty": "Senior",
            "theme": "Impediment escalation",
            "prompt": "A critical dependency owned by another team has blocked your Developers for three days. The dependency owner keeps saying it will be fixed 'soon'. How do you handle it?",
            "signals": ["Make impediment visible", "Clarify ownership", "Define next action", "Escalate deliberately", "Inspect aging"],
            "strong": "A strong answer makes the impediment explicit, confirms the impact and owner, agrees a concrete next action and date, facilitates cross-team resolution, and escalates when the team cannot resolve the constraint itself. The Scrum Master enables resolution rather than personally owning the dependency.",
            "keywords": {
                "visibility": ["visible", "transparen", "impediment", "blocker"],
                "ownership": ["owner", "ownership", "responsib"],
                "action": ["next action", "action", "date", "deadline", "commitment"],
                "escalation": ["escalat", "management", "leadership"],
                "learning": ["aging", "pattern", "root cause", "learn", "retrospective"],
            },
        },
        {
            "id": "SM-03",
            "difficulty": "Senior",
            "theme": "Metrics interpretation",
            "prompt": "Your team completed 16 points against a forecast of 20. Cycle time increased from 3.4 to 4.1 days and three defects escaped. A manager asks you to 'fix velocity'. How do you respond?",
            "signals": ["Outcome before metric", "Inspect flow and quality", "Avoid velocity as target", "Find contributing factors", "Adapt with experiment"],
            "strong": "A strong answer reframes the conversation from fixing velocity to understanding delivery. Inspect the Sprint Goal, flow, cycle time, spillover, impediments and quality signals, identify contributing factors, then choose a focused experiment. Velocity is evidence for planning, not an individual or team performance target.",
            "keywords": {
                "outcome": ["sprint goal", "outcome", "value"],
                "flow": ["cycle time", "flow", "wip", "spillover"],
                "quality": ["defect", "quality", "escaped"],
                "not_target": ["not a target", "not performance", "performance target", "not measure people", "don't target", "do not target"],
                "experiment": ["experiment", "improvement", "adapt", "action"],
            },
        },
        {
            "id": "SM-04",
            "difficulty": "Advanced",
            "theme": "PO vs Engineering conflict",
            "prompt": "The Product Owner wants a feature released immediately. Engineering says the architecture needs refactoring first. Both sides claim the other is blocking delivery. How would you facilitate the conflict?",
            "signals": ["Shared problem statement", "Surface evidence", "Explore options", "Clarify accountabilities", "Facilitate decision"],
            "strong": "A strong answer avoids deciding the technical or product question for them. Establish a shared problem statement, surface evidence and constraints, make options and trade-offs visible, clarify who owns the decision, and facilitate agreement on the next useful action.",
            "keywords": {
                "shared": ["shared problem", "common", "alignment", "understanding"],
                "evidence": ["evidence", "data", "risk", "constraint", "impact"],
                "options": ["options", "trade-off", "tradeoff", "alternative"],
                "accountability": ["accountab", "product owner", "engineering", "developers"],
                "facilitation": ["facilitate", "conversation", "decision", "agreement"],
            },
        },
        {
            "id": "SM-05",
            "difficulty": "Advanced",
            "theme": "Bypassing the Product Owner",
            "prompt": "Developers complain that stakeholders message them directly with requests. The Developers feel pressured to say yes, while the Product Owner feels excluded. What coaching intervention would you use?",
            "signals": ["Coach team and stakeholders", "Clarify decision path", "Protect transparency", "Preserve PO accountability", "Build sustainable ownership"],
            "strong": "A strong answer treats the situation as a system and behaviour problem, not simply a communication failure. Coach stakeholders and Developers on the decision path, make requests visible, preserve the Product Owner's accountability for value ordering, and help the team build the confidence to redirect requests without relying on the Scrum Master as a permanent gatekeeper.",
            "keywords": {
                "coach": ["coach", "coaching"],
                "decision": ["decision path", "product owner", "ordering", "priorit"],
                "transparency": ["visible", "transparent", "backlog", "request"],
                "ownership": ["ownership", "team", "self-manag", "empower"],
                "stakeholder": ["stakeholder", "customer"],
            },
        },
        {
            "id": "SM-06",
            "difficulty": "Advanced",
            "theme": "Retrospective to experiment",
            "prompt": "A retrospective identifies recurring dependency interruptions and escaped defects, but previous actions were never followed through. How do you turn the retrospective into measurable improvement?",
            "signals": ["Prioritise improvement", "Define experiment", "Owner and next action", "Baseline and target", "Inspect result"],
            "strong": "A strong answer converts observations into a small number of testable experiments. Establish a baseline, define a target signal, assign an owner and next action, agree when to inspect the result, and use the next Sprint to decide whether to continue, adapt or stop the experiment.",
            "keywords": {
                "experiment": ["experiment", "hypothesis", "test"],
                "baseline": ["baseline", "current", "starting point"],
                "target": ["target", "goal", "measure"],
                "owner": ["owner", "ownership", "responsible"],
                "inspect": ["inspect", "next sprint", "review", "adapt", "result"],
            },
        },
    ]

    # Keep simulation state separate from widget state so navigation remains safe.
    if "sim_score" not in st.session_state:
        st.session_state.sim_score = None
    if "sim_feedback" not in st.session_state:
        st.session_state.sim_feedback = []
    if "sim_answer" not in st.session_state:
        st.session_state.sim_answer = ""

    left, right = st.columns([1.45, 1])
    with left:
        selected_id = st.selectbox(
            "Interview scenario",
            [f"{s['id']} · {s['theme']} · {s['difficulty']}" for s in scenarios],
            key="sim_scenario_selector",
        )
    selected = scenarios[[f"{s['id']} · {s['theme']} · {s['difficulty']}" for s in scenarios].index(selected_id)]
    with right:
        st.markdown(
            f'<div class="mini-card"><div class="mini-label">Scenario</div><div class="mini-value">{safe_text(selected["id"])}</div><div class="mini-note">{safe_text(selected["difficulty"])} · {safe_text(selected["theme"])}</div></div>',
            unsafe_allow_html=True,
        )

    section("Interview prompt", "Answer as if you are speaking to a hiring manager. Aim for 60–90 seconds.", "QUESTION")
    st.markdown(f'<div class="sim-card"><div style="font-size:1.05rem;font-weight:800;line-height:1.55">{safe_text(selected["prompt"])}</div></div>', unsafe_allow_html=True)

    section("Answer builder", "A concise structure helps: inspect → facilitate → adapt → learn. Use your own words and real examples where appropriate.", "YOUR RESPONSE")
    answer = st.text_area(
        "Your interview answer",
        value=st.session_state.sim_answer if st.session_state.sim_answer else "",
        placeholder="I would first inspect...",
        height=210,
        key="sim_answer_input",
        label_visibility="collapsed",
    )

    a, b, c = st.columns(3)
    with a:
        evaluate = st.button("Evaluate my answer", type="primary", use_container_width=True)
    with b:
        reveal = st.button("Reveal strong-answer lens", use_container_width=True)
    with c:
        reset = st.button("Reset practice", use_container_width=True)

    if reset:
        st.session_state.sim_score = None
        st.session_state.sim_feedback = []
        st.session_state.sim_answer = ""
        st.rerun()

    if evaluate:
        text = (answer or "").strip().lower()
        if len(text) < 40:
            st.warning("Give a little more substance first. Aim for at least a few complete sentences.")
            st.session_state.sim_score = None
        else:
            feedback = []
            matched = 0
            for label, terms in selected["keywords"].items():
                hit = any(term in text for term in terms)
                if hit:
                    matched += 1
                    feedback.append((label.replace("_", " ").title(), "covered"))
                else:
                    feedback.append((label.replace("_", " ").title(), "missing"))
            score = round((matched / len(selected["keywords"])) * 100)
            st.session_state.sim_score = score
            st.session_state.sim_feedback = feedback
            st.session_state.sim_answer = answer

    if st.session_state.sim_score is not None:
        section("Interview signal check", "This is a practice aid, not an AI judgement or hiring score. It checks whether key concepts appear in your written response.", "FEEDBACK")
        score = st.session_state.sim_score
        if score >= 80:
            st.success(f"Strong coverage · {score}% of the scenario signals detected")
        elif score >= 60:
            st.warning(f"Good foundation · {score}% of the scenario signals detected. Tighten the missing areas.")
        else:
            st.error(f"Needs more evidence · {score}% of the scenario signals detected. Structure the answer before adding detail.")

        cols = st.columns(min(3, len(st.session_state.sim_feedback)))
        for idx, (label, status) in enumerate(st.session_state.sim_feedback):
            with cols[idx % len(cols)]:
                cls = "health-good" if status == "covered" else "health-watch"
                word = "COVERED" if status == "covered" else "MISSING"
                st.markdown(f'<div class="decision"><div class="tag {cls}">{word}</div><div class="decision-title">{safe_text(label)}</div><div class="decision-body">{("A relevant signal was detected in your answer." if status == "covered" else "Consider addressing this explicitly in your answer.")}</div></div>', unsafe_allow_html=True)

    if reveal:
        section("Strong-answer lens", "Use this after answering, not before. Compare the thinking pattern rather than memorising a script.", "MODEL THINKING")
        st.markdown(f'<div class="evidence-card"><h3>{safe_text(selected["theme"])}</h3><p>{safe_text(selected["strong"])}</p></div>', unsafe_allow_html=True)
        st.markdown("**Signals an interviewer can listen for**")
        st.write(" · ".join(selected["signals"]))

    section("Interview discipline", "The strongest Scrum Master answers show judgement, facilitation and learning, not a list of ceremonies.", "WHAT GOOD SOUNDS LIKE")
    c1, c2, c3, c4 = st.columns(4)
    for col, title, body in [
        (c1, "Inspect", "Start with the evidence, Sprint Goal, context and people involved."),
        (c2, "Facilitate", "Help the right people understand the problem and make the decision."),
        (c3, "Adapt", "Choose the smallest useful intervention rather than a heroic fix."),
        (c4, "Learn", "Turn the result into an observable improvement or coaching action."),
    ]:
        with col:
            st.markdown(f'<div class="signal-card"><h3>{safe_text(title)}</h3><p>{safe_text(body)}</p></div>', unsafe_allow_html=True)

    st.caption("Practice scenarios are synthetic and derived from the portfolio's existing delivery themes. The evaluator is keyword-assisted, intentionally transparent, and not a hiring assessment.")

st.markdown('<div class="footer-note">Scrum Master Delivery Lab · M10/M10.1 Agile Transformation Lab · Streamlit presentation layer over the existing evidence repository.</div>', unsafe_allow_html=True)
