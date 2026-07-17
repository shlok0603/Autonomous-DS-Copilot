import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
<div style="background:red;padding:20px;border-radius:10px;color:white;">
<h2>Hello HTML</h2>
<p>If this is a red box, HTML rendering is working.</p>
</div>
""",
    unsafe_allow_html=True
)