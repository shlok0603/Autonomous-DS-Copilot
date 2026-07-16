import streamlit as st

from utils.insight_generator import InsightGenerator
from services.ai_service import AIService


def render(df):

    st.subheader("AI Dataset Insights")

    # Store AI response
    if "ai_report" not in st.session_state:
        st.session_state.ai_report = None

    # Generate Report
    if st.button("Generate AI Insights"):

        with st.spinner("Analyzing dataset..."):

            prompt = InsightGenerator.build_prompt(df)

            ai = AIService()

            response = ai.generate_insights(prompt)

            st.session_state.ai_report = response

    # Display Report
    if st.session_state.ai_report:

        with st.container(border=True):

            st.markdown(st.session_state.ai_report)

        st.download_button(
            label="Download AI Report",
            data=st.session_state.ai_report,
            file_name="AI_Report.md",
            mime="text/markdown"
        )