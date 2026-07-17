import streamlit as st


def render(title, value, icon):

    st.markdown(
        f"""
<div class="glass-card">
<div class="glass-title">{icon} {title}</div>
<div style="color:#CBD5E1;font-size:16px;">
{value}
</div>
</div>
""",
        unsafe_allow_html=True
    )