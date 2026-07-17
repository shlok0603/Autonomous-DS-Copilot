import streamlit as st

from utils.insight_generator import InsightGenerator
from utils.domain_detector import DomainDetector
from services.ai_service import AIService
from utils.problem_detector import ProblemDetector
from utils.ml_recommender import MLRecommender


def render(df):

    st.markdown(
        """
# 🤖 AI Copilot

Generate enterprise-grade AI insights powered by **Google Gemini**.
"""
    )

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

            st.subheader("🧠 AI Copilot Analysis")

            sections = st.session_state.ai_report.split("\n\n")

            for section in sections:

                section = section.strip()

                if not section:
                    continue

                lower = section.lower()

                if "executive" in lower:
                    st.success(section)

                elif (
                    "risk" in lower
                    or "issue" in lower
                    or "warning" in lower
                ):
                    st.warning(section)

                elif (
                    "recommend" in lower
                    or "suggest" in lower
                ):
                    st.info(section)

                else:
                    st.markdown(section)

                st.divider()

        st.download_button(
            label="📄 Download AI Report",
            data=st.session_state.ai_report,
            file_name="AI_Report.md",
            mime="text/markdown",
            use_container_width=True
        )