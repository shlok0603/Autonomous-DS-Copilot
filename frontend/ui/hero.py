import streamlit as st


def render(title, subtitle, icon="🚀"):

    st.markdown(
        f"""
<div style="
background:linear-gradient(135deg,#4338CA,#6D28D9,#7C3AED);
padding:38px;
border-radius:24px;
margin-bottom:28px;
position:relative;
overflow:hidden;
box-shadow:0 25px 55px rgba(99,102,241,.35);
">

<div style="
position:absolute;
right:-80px;
top:-80px;
width:220px;
height:220px;
background:rgba(255,255,255,.12);
border-radius:50%;
filter:blur(10px);
"></div>

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<div style="
display:inline-block;
padding:8px 16px;
background:rgba(255,255,255,.12);
border-radius:999px;
font-size:13px;
color:white;
margin-bottom:16px;
">

✨ Enterprise AI Platform

</div>

<h1 style="
margin:0;
color:white;
font-size:40px;
font-weight:800;
">

{icon} {title}

</h1>

<p style="
margin-top:14px;
font-size:18px;
color:#E9D5FF;
">

{subtitle}

</p>

</div>

<div style="
font-size:70px;
opacity:.18;
">

{icon}

</div>

</div>

</div>
""",
        unsafe_allow_html=True
    )