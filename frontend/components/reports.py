import streamlit as st

from frontend.ui.hero import render as hero
from reports.report_generator import ReportGenerator


def status_card(title, icon, status="Ready"):

    color = "#10B981" if status == "Ready" else "#F59E0B"

    st.markdown(
        f"""
<div style="
background:#1E293B;
padding:20px;
border-radius:18px;
margin-bottom:15px;
display:flex;
justify-content:space-between;
align-items:center;
border:1px solid rgba(255,255,255,.08);
box-shadow:0 10px 25px rgba(0,0,0,.20);
">

<div style="
font-size:16px;
font-weight:600;
color:white;
">

{icon} {title}

</div>

<div style="
background:{color};
padding:8px 16px;
border-radius:999px;
color:white;
font-size:13px;
font-weight:600;
">

{status}

</div>

</div>
""",
        unsafe_allow_html=True,
    )


def render(df, profile):

    # ============================================================
    # Hero
    # ============================================================

    hero(
        title="Enterprise Report Center",
        subtitle="Generate professional AI-powered reports with one click.",
        icon="📄"
    )

    # ============================================================
    # AI Report Check
    # ============================================================

    if (
        "ai_report" not in st.session_state
        or st.session_state.ai_report is None
    ):

        st.warning(
            "⚠️ Please generate AI Insights before creating reports."
        )

        return

    # ============================================================
    # Dashboard Metrics
    # ============================================================

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Sections", "6")

    with c2:
        st.metric("Format", "PDF")

    with c3:
        st.metric("AI Engine", "Gemini")

    st.divider()

    # ============================================================
    # Report Components
    # ============================================================

    st.markdown("## 📋 Report Components")

    left, right = st.columns(2)

    with left:

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

    with right:

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

    st.divider()

    # ============================================================
    # Generate Report
    # ============================================================

    st.markdown("## 🚀 Enterprise Report Generator")

    if st.button(
        "📄 Generate Enterprise Report",
        use_container_width=True
    ):

        with st.spinner(
            "🤖 Gemini is generating your enterprise report..."
        ):

            pdf_path = ReportGenerator.generate(
                df,
                profile,
                st.session_state.ai_report
            )

        st.session_state.generated_pdf = pdf_path

        st.balloons()

        st.success(
            "🎉 Enterprise Report Generated Successfully!"
        )

    # ============================================================
    # Download Center
    # ============================================================

    if "generated_pdf" in st.session_state:

        st.divider()

        st.markdown("## 📥 Download Center")

        c1, c2 = st.columns(2)

        with c1:

            with open(
                st.session_state.generated_pdf,
                "rb"
            ) as pdf:

                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf,
                    file_name="Enterprise_AI_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

        with c2:

            st.download_button(
                label="🤖 Download AI Insights",
                data=st.session_state.ai_report,
                file_name="AI_Insights.md",
                mime="text/markdown",
                use_container_width=True
            )

    # ============================================================
    # Footer
    # ============================================================

    st.divider()

    st.success(
        "✨ Your report includes dataset profiling, AI insights, visualizations, AutoML recommendations, and enterprise-ready documentation."
    )