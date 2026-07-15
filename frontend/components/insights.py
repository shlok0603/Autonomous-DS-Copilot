import streamlit as st

from utils.insight_generator import InsightGenerator
from services.ai_service import AIService


def render(df):

    st.subheader("🤖 AI Dataset Insights")

    if st.button("Generate AI Insights"):

        with st.spinner("Analyzing dataset..."):

            prompt = InsightGenerator.build_prompt(df)

            ai = AIService()

            response = ai.generate_insights(prompt)

            st.markdown(response)