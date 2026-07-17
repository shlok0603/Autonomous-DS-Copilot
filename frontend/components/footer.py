import streamlit as st


def render():

    st.divider()

    st.markdown(
        """
<center>

<b>Autonomous Data Science Co-Pilot</b><br>

Version 2.0<br><br>

Powered by Gemini AI • Scikit-Learn • Plotly • Streamlit

<br><br>

Developed by <b>Shlok Nandwana</b>

</center>
""",
        unsafe_allow_html=True
    )