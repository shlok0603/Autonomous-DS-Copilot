import streamlit as st


def start(title=None):

    st.markdown(
        f"""
<div class="glass-card">

{f'<div class="glass-title">{title}</div>' if title else ""}
""",
        unsafe_allow_html=True,
    )


def end():

    st.markdown(
        """
</div>
""",
        unsafe_allow_html=True,
    )