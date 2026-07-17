import streamlit as st

from utils.insight_generator import InsightGenerator
from utils.domain_detector import DomainDetector
from services.ai_service import AIService
from utils.problem_detector import ProblemDetector
from utils.ml_recommender import MLRecommender


def render(df):
    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#4338CA,#6D28D9,#7C3AED);
    padding:38px;
    border-radius:24px;
    margin-bottom:30px;
    box-shadow:0 20px 45px rgba(99,102,241,.30);
    ">

    <div style="
    display:inline-block;
    padding:8px 16px;
    background:rgba(255,255,255,.12);
    border-radius:999px;
    color:white;
    font-size:13px;
    margin-bottom:16px;
    ">

    ✨ Google Gemini

    </div>

    <h1 style="color:white;margin:0;">
    🤖 AI Copilot
    </h1>

    <p style="color:#E9D5FF;font-size:18px;margin-top:12px;">

    Generate enterprise-grade AI insights powered by Gemini.

    </p>

    </div>
    """, unsafe_allow_html=True)

    # ----------------------------------------------------
    # Session State
    # ----------------------------------------------------

    if "ai_report" not in st.session_state:
        st.session_state.ai_report = None

    # ----------------------------------------------------
    # Generate Insights
    # ----------------------------------------------------

    if st.button(
        "🚀 Generate AI Insights",
        use_container_width=True
    ):

        with st.spinner("🤖 Gemini is analyzing your dataset..."):

            # Detect domain
            domain = DomainDetector.detect(df)

            # Build prompt
            prompt = InsightGenerator.build_prompt(df)

            prompt = f"""
Dataset Domain: {domain}

{prompt}
"""

            ai = AIService()

            response = ai.generate_insights(prompt)

            problem, target = ProblemDetector.detect(df)

            recommendation = MLRecommender.recommend(problem)

            st.session_state.ai_report = response

            st.success("✅ AI Analysis Completed Successfully")

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Domain", domain)
            c2.metric("Problem", problem)
            c3.metric("Target", target if target else "N/A")
            c4.metric("Engine", "Gemini")

            # ------------------------------------------------
            # Dataset Information
            # ------------------------------------------------

            with st.container(border=True):

                st.subheader("📌 Dataset Information")

                c1, c2 = st.columns(2)

                with c1:
                    st.info(f"🌍 Domain: **{domain}**")
                    st.info(f"🧠 Problem Type: **{problem}**")

                with c2:
                    st.info(
                        f"🎯 Target Column: **{target if target else 'Not Detected'}**"
                    )
                    st.info("🤖 Gemini Status: **Ready**")

            # ------------------------------------------------
            # Recommended Models
            # ------------------------------------------------

            with st.container(border=True):

                st.subheader("🤖 Recommended Models")

                for model in recommendation["models"]:
                    st.success(model)

            # ------------------------------------------------
            # Evaluation Metrics
            # ------------------------------------------------

            with st.container(border=True):

                st.subheader("📈 Recommended Evaluation Metrics")

                for metric in recommendation["metrics"]:
                    st.info(metric)

    # ----------------------------------------------------
    # Display AI Report
    # ----------------------------------------------------

    if st.session_state.ai_report:

        with st.container(border=True):

            st.markdown("## 🧠 Executive AI Report")

            sections = st.session_state.ai_report.split("\n\n")

            for section in sections:

                section = section.strip()

                if not section:
                    continue

                lower = section.lower()

                if "executive" in lower:
                    st.success("📌 Executive Summary")
                    st.markdown(section)

                elif (
                    "risk" in lower
                    or "issue" in lower
                    or "warning" in lower
                ):
                    st.warning("⚠ Risks Detected")
                    st.markdown(section)

                elif (
                    "recommend" in lower
                    or "suggest" in lower
                ):
                    st.info("💡 Recommendations")
                    st.markdown(section)

                else:
                    st.markdown("### 📊 Analysis")
                    st.write(section)

                st.divider()

        st.download_button(
            label="⬇ Download Enterprise AI Report",
            data=st.session_state.ai_report,
            file_name="AI_Report.md",
            mime="text/markdown",
            use_container_width=True
        )