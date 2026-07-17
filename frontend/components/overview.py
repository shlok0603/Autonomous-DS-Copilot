import streamlit as st
from frontend.ui.hero import render as hero
from frontend.ui.stat_card import render as stat_card
from frontend.ui.info_card import render as info_card

from utils.problem_detector import ProblemDetector
from utils.domain_detector import DomainDetector


def render(df, profile):

    # ==================================================
    # Dashboard Header
    # ==================================================

    hero(
        title="Enterprise Dashboard",
        subtitle="Analyze datasets, generate AI insights and build ML models.",
        icon="📊"
    )

    # ==================================================
    # Dataset Statistics
    # ==================================================

    missing = int(profile["missing"].sum())

    domain = DomainDetector.detect(df)

    problem, target = ProblemDetector.detect(df)

    if profile["rows"] < 1000:
        dataset_size = "Small"
    elif profile["rows"] < 100000:
        dataset_size = "Medium"
    else:
        dataset_size = "Large"

    health = round(
        100
        - (
            missing
            / max(profile["rows"] * profile["columns"], 1)
        )
        * 100,
        1,
    )

    # ==================================================
    # KPI Cards
    # ==================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        stat_card(
            "Rows",
            f"{profile['rows']:,}",
            "📄",
            "#2563EB",
            "Dataset Records",
        )

    with c2:
        stat_card(
            "Columns",
            profile["columns"],
            "📊",
            "#10B981",
            "Available Features",
        )

    with c3:
        stat_card(
            "Missing",
            missing,
            "⚠️",
            "#F59E0B",
            "Null Values",
        )

    with c4:
        stat_card(
            "Health",
            f"{health}%",
            "💚",
            "#8B5CF6",
            "Dataset Quality",
        )

    # ==================================================
    # Executive Summary
    # ==================================================

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("## 🚀 Executive Summary")

    left, right = st.columns(2)

    with left:

        info_card(
            "Dataset Domain",
            domain,
            "🌍",
        )

        info_card(
            "Dataset Size",
            dataset_size,
            "📦",
        )

        info_card(
            "Problem Type",
            problem,
            "🧠",
        )

    with right:

        info_card(
            "Target Column",
            target if target else "Not Detected",
            "🎯",
        )

        info_card(
            "Dataset Health",
            f"{health}%",
            "💚",
        )

        info_card(
            "AI Status",
            "Ready",
            "🤖",
        )

    # ==================================================
    # Dataset Preview
    # ==================================================

    st.markdown("## 📄 Dataset Preview")

    with st.container(border=True):

        st.dataframe(
            df.head(10),
            use_container_width=True,
            height=420,
        )

    # ==================================================
    # Quick Actions
    # ==================================================

    st.markdown("## ⚡ AI Recommendations")

    st.markdown("## ⚡ AI Recommendations")

    pages = [
        ("🤖", "Generate AI Insights", "AI Insights"),
        ("📈", "Train AutoML", "AutoML"),
        ("📊", "Evaluate Models", "Evaluation"),
        ("📄", "Generate Report", "Reports"),
        ("💬", "Chat with Dataset", "AI Chat"),
    ]

    cols = st.columns(5)

    for col, (icon, title, page_name) in zip(cols, pages):

        with col:

            st.markdown(
                f"""
    <div class="glass-card" style="text-align:center;height:170px;">

    <div style="font-size:48px;margin-top:10px;">
    {icon}
    </div>

    <h4 style="margin-top:20px;color:white;">
    {title}
    </h4>

    </div>
    """,
                unsafe_allow_html=True,
            )

            if st.button(
                    "Open Module",
                    key=page_name,
                    use_container_width=True
            ):
                st.session_state.page = page_name
                st.rerun()

    # ==================================================
    # Dataset Health
    # ==================================================

    st.markdown("## 📈 Dataset Health")

    st.progress(health / 100)

    st.caption(f"Overall Dataset Quality Score : {health}%")


    # ==================================================
    # Footer Cards
    # ==================================================

    st.markdown("## ℹ️ Project Information")

    f1, f2 = st.columns(2)

    with f1:

        info_card(
            "Memory Usage",
            profile["memory"],
            "💾",
        )

    with f2:

        info_card(
            "AI Engine",
            "Gemini Connected",
            "🤖",
        )