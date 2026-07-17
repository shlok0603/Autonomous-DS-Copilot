import streamlit as st

from frontend.theme import apply_theme
apply_theme()

from frontend.ui.hero import render as hero

from utils.loader import DatasetLoader
from utils.profiler import DataProfiler

from frontend.components.header import render as render_header
from frontend.components.footer import render as render_footer

from streamlit_option_menu import option_menu

from frontend.components import (
    overview,
    quality,
    visualization,
    insights,
    cleaning,
    chat,
    automl,
    evaluation,
    explainability,
    forecasting,
    reports
)

# =========================================================
# HEADER
# =========================================================

render_header()

# =========================================================
# LANDING PAGE
# =========================================================

hero(
    title="Autonomous Data Science Co-Pilot",
    subtitle="Enterprise AI Platform for Analytics, AutoML, Explainability and Forecasting.",
    icon="🚀"
)

st.markdown("## ✨ Platform Features")

f1, f2, f3, f4 = st.columns(4)

with f1:
    st.success("🤖 AI Insights")

with f2:
    st.success("📈 AutoML")

with f3:
    st.success("🧠 Explainability")

with f4:
    st.success("📄 Enterprise Reports")

st.divider()

# =========================================================
# DATASET UPLOAD
# =========================================================

st.markdown("## 📂 Upload Dataset")

uploaded_file = st.file_uploader(
    "",
    type=["csv", "xlsx", "json"],
    label_visibility="collapsed"
)

# =========================================================
# WAIT FOR DATASET
# =========================================================

if uploaded_file is None:

    st.info("👆 Upload a dataset to start the AI analysis.")

    render_footer()

    st.stop()

# =========================================================
# LOAD DATA
# =========================================================

df = DatasetLoader.load(uploaded_file)

profile = DataProfiler.profile(df)

# Navigation from Dashboard Cards
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("# 🚀 Co-Pilot")

    st.success("Dataset Loaded")

    st.metric("Rows", profile["rows"])

    st.metric("Columns", profile["columns"])

    st.metric("Memory", profile["memory"])

    st.divider()

    page = option_menu(

        menu_title=None,

        options=[
            "Dashboard",
            "Data Quality",
            "Visualizations",
            "AI Insights",
            "Cleaning",
            "AI Chat",
            "AutoML",
            "Evaluation",
            "Explainability",
            "Forecasting",
            "Reports"
        ],

        icons=[
            "house-fill",
            "clipboard-data",
            "bar-chart-fill",
            "robot",
            "magic",
            "chat-dots-fill",
            "cpu-fill",
            "graph-up",
            "lightbulb-fill",
            "calendar3",
            "file-earmark-pdf-fill"
        ],

        default_index=[
            "Dashboard",
            "Data Quality",
            "Visualizations",
            "AI Insights",
            "Cleaning",
            "AI Chat",
            "AutoML",
            "Evaluation",
            "Explainability",
            "Forecasting",
            "Reports",
        ].index(st.session_state.page),

        styles={
            "container": {
                "padding": "5px",
                "background-color": "#111827"
            },
            "icon": {
                "color": "#8B5CF6",
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "15px",
                "font-weight": "600",
                "text-align": "left",
                "margin": "4px",
                "border-radius": "12px",
                "--hover-color": "#1E293B",
            },
            "nav-link-selected": {
                "background-color": "#6366F1",
                "color": "white",
            },
        },
    )
    st.session_state.page = page

st.success("✅ Dataset Loaded Successfully")

# =========================================================
# ROUTING
# =========================================================

if page == "Dashboard":
    overview.render(df, profile)

elif page == "Data Quality":
    quality.render(df, profile)

elif page == "Visualizations":
    visualization.render(df)

elif page == "AI Insights":
    insights.render(df)

elif page == "Cleaning":
    cleaning.render(df)

elif page == "AI Chat":
    chat.render(df)

elif page == "AutoML":
    automl.render(df)

elif page == "Evaluation":
    evaluation.render(df)

elif page == "Explainability":
    explainability.render(df)

elif page == "Forecasting":
    forecasting.render(df)

elif page == "Reports":
    reports.render(df, profile)

# =========================================================
# FOOTER
# =========================================================

render_footer()