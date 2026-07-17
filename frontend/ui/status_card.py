import streamlit as st


def render(title, status="Ready"):

    colors = {
        "Ready": "#22C55E",
        "Warning": "#F59E0B",
        "Error": "#EF4444"
    }

    color = colors.get(
        status,
        "#22C55E"
    )

    st.markdown(
        f"""
<div style="

background:#1E293B;

padding:18px;

border-radius:18px;

margin-bottom:14px;

display:flex;

justify-content:space-between;

align-items:center;

">

<div style="
font-weight:600;
color:white;
">

{title}

</div>

<div style="

background:{color};

padding:8px 18px;

border-radius:18px;

color:white;

font-size:13px;

">

{status}

</div>

</div>
""",
        unsafe_allow_html=True
    )