import streamlit as st
from frontend.ui.hero import render as hero
from reports.report_generator import ReportGenerator


def status_card(title, icon, status="Ready"):

    color = "#10B981" if status == "Ready" else "#F59E0B"

    from frontend.ui.hero import render as hero


def render(df, profile):

    # ============================================================
    # Hero
    # ============================================================

    hero(
        title="Enterprise Report Center",
        subtitle="Generate professional AI-powered reports.",
        icon="📄"
    )

    # ============================================================
    # Check AI Report
    # ============================================================

    if "ai_report" not in st.session_state or st.session_state.ai_report is None:

        st.warning(
            "⚠️ Generate AI Insights before creating reports."
        )

        return

    # ============================================================
    # Report Status
    # ============================================================

    st.markdown("## 📋 Report Components")

    c1, c2 = st.columns(2)

    with c1:

        status_card(
            "Executive Summary",
            "📊"
        )

        status_card(
            "AI Insights",
            "🤖"
        )

        status_card(
            "Visualizations",
            "📈"
        )

    with c2:

        status_card(
            "ML Recommendation",
            "🧠"
        )

        status_card(
            "Dataset Profile",
            "📂"
        )

        status_card(
            "Professional PDF",
            "📄"
        )

    st.markdown("---")

    # ============================================================
    # Report Generation
    # ============================================================

    st.markdown("## 🚀 Generate Report")

    if st.button(
        "Generate Enterprise Report",
        use_container_width=True
    ):

        with st.spinner("Generating Enterprise AI Report..."):

            pdf_path = ReportGenerator.generate(
                df,
                profile,
                st.session_state.ai_report
            )

        st.session_state.generated_pdf = pdf_path

        st.success(
            "✅ Enterprise Report Generated Successfully"
        )

    # ============================================================
    # Downloads
    # ============================================================

    if "generated_pdf" in st.session_state:

        st.markdown("## ⬇ Download Reports")

        c1, c2 = st.columns(2)

        with c1:

            with open(
                st.session_state.generated_pdf,
                "rb"
            ) as pdf:

                st.download_button(
                    "📄 Download PDF Report",
                    pdf,
                    "Enterprise_AI_Report.pdf",
                    "application/pdf",
                    use_container_width=True,
                )

        with c2:

            st.download_button(
                "🤖 Download AI Insights",
                st.session_state.ai_report,
                "AI_Insights.md",
                "text/markdown",
                use_container_width=True,
            )

    # ============================================================
    # Footer
    # ============================================================

    st.markdown("---")

    st.info(
        "💡 Reports include dataset profiling, AI insights, visualizations, and machine learning recommendations."
    )