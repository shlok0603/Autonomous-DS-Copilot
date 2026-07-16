import streamlit as st

from reports.report_generator import ReportGenerator


def render(df, profile):

    st.subheader("Reports")

    # Check if AI insights have been generated
    if "ai_report" not in st.session_state:
        st.info("Please generate AI Insights first.")
        return

    if st.session_state.ai_report is None:
        st.info("Please generate AI Insights first.")
        return

    # Generate Reports
    if st.button("Generate Reports"):

        with st.spinner("Generating HTML and PDF Reports..."):

            html_path, pdf_path = ReportGenerator.generate(
                df,
                profile,
                st.session_state.ai_report
            )

        st.success("Reports Generated Successfully!")

        col1, col2 = st.columns(2)

        # Download PDF
        with col1:

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="Download PDF",
                    data=pdf_file,
                    file_name="AI_Report.pdf",
                    mime="application/pdf"
                )

        # Download HTML
        with col2:

            with open(html_path, "r", encoding="utf-8") as html_file:

                st.download_button(
                    label="Download HTML",
                    data=html_file.read(),
                    file_name="Analysis_Report.html",
                    mime="text/html"
                )