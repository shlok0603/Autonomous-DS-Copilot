import streamlit as st

from utils.loader import DatasetLoader
from utils.profiler import DataProfiler

from frontend.components import (
    overview,
    quality,
    visualization,
    insights,
    reports
)

st.set_page_config(
    page_title="Autonomous Data Science Co-Pilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Autonomous Data Science Co-Pilot")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx", "json"]
)

if uploaded_file:

    # Load Dataset
    df = DatasetLoader.load(uploaded_file)

    # Generate Profile
    profile = DataProfiler.profile(df)

    st.success("Dataset Loaded Successfully")

    # Create Tabs
    overview_tab, quality_tab, visualization_tab, insights_tab, reports_tab = st.tabs(
        [
            "Overview",
            "Data Quality",
            "Visualizations",
            "AI Insights",
            "Reports"
        ]
    )

    # Overview Tab
    with overview_tab:
        overview.render(df, profile)

    # Data Quality Tab
    with quality_tab:
        quality.render(profile)

    # Visualization Tab
    with visualization_tab:
        visualization.render(df)

    # AI Insights Tab
    with insights_tab:
        insights.render()

    # Reports Tab
    with reports_tab:
        reports.render()