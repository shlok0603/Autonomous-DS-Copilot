import streamlit as st


def render(title, value, icon, color="#6366F1", subtitle=""):

    st.markdown(
        f"""
<div class="stat-card">
<div class="stat-icon" style="background:linear-gradient(135deg,{color},#8B5CF6);">
{icon}
</div>

<div class="stat-title">
{title}
</div>

<div class="stat-value">
{value}
</div>

<div class="stat-change">
{subtitle}
</div>

</div>
""",
        unsafe_allow_html=True
    )