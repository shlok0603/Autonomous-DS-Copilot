import streamlit as st


def render(
    title,
    value,
    icon="📊",
    subtitle="",
    color="#6366F1"
):

    st.markdown(
        f"""
<div style="

background:linear-gradient(
135deg,
#1E293B,
#111827);

padding:24px;

border-radius:22px;

border:1px solid rgba(255,255,255,.06);

box-shadow:
0 15px 35px rgba(0,0,0,.28);

height:175px;

">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div style="

width:58px;

height:58px;

border-radius:18px;

display:flex;

justify-content:center;

align-items:center;

font-size:28px;

background:{color};

">

{icon}

</div>

<div style="
color:#94A3B8;
font-size:14px;
">

{subtitle}

</div>

</div>

<div style="
margin-top:25px;
color:#CBD5E1;
font-size:15px;
">

{title}

</div>

<div style="
font-size:34px;
font-weight:800;
color:white;
margin-top:8px;
">

{value}

</div>

</div>
""",
        unsafe_allow_html=True
    )