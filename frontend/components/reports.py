import streamlit as st

from reports.report_generator import ReportGenerator


def render(profile):

    st.subheader("Reports")

    if st.session_state.get("ai_report") is None:

        st.info("Generate AI Insights first.")

        return

    if st.button("Generate PDF Report"):

        with st.spinner("Generating PDF..."):

            pdf_path = ReportGenerator.generate(
                profile,
                st.session_state.ai_report
            )

        st.success("PDF Generated Successfully")

        with open(pdf_path, "rb") as file:

            st.download_button(
                "Download PDF",
                file,
                "AI_Report.pdf",
                mime="application/pdf"
            )