import streamlit as st


def render():

    st.markdown(
        """
<style>

.header{

    background:linear-gradient(
        135deg,
        #1E293B,
        #0F172A
    );

    border:1px solid rgba(255,255,255,.08);

    border-radius:24px;

    padding:28px;

    margin-bottom:28px;

    box-shadow:
        0 25px 45px rgba(0,0,0,.35);

}

.header-row{

    display:flex;

    justify-content:space-between;

    align-items:center;

}

.logo{

    display:flex;

    align-items:center;

    gap:18px;

}

.logo-icon{

    width:70px;

    height:70px;

    border-radius:20px;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:34px;

    background:linear-gradient(
        135deg,
        #6366F1,
        #8B5CF6
    );

    box-shadow:
        0 15px 35px rgba(99,102,241,.45);

}

.title{

    color:white;

    font-size:32px;

    font-weight:800;

    margin:0;

}

.subtitle{

    color:#94A3B8;

    font-size:16px;

    margin-top:6px;

}

.right-panel{

    display:flex;

    gap:15px;

    align-items:center;

}

.status{

    background:#111827;

    border:1px solid #334155;

    color:white;

    border-radius:15px;

    padding:12px 18px;

    font-size:14px;

}

.profile{

    width:52px;

    height:52px;

    border-radius:50%;

    display:flex;

    align-items:center;

    justify-content:center;

    background:linear-gradient(
        135deg,
        #10B981,
        #22D3EE
    );

    font-size:22px;

}

</style>

<div class="header">

<div class="header-row">

<div class="logo">

<div class="logo-icon">

🚀

</div>

<div>

<p class="title">

Autonomous Data Science Co-Pilot

</p>

<p class="subtitle">

Enterprise AI Analytics Platform

</p>

</div>

</div>

<div class="right-panel">

<div class="status">

🟢 Gemini Connected

</div>

<div class="status">

Version 2.0

</div>

<div class="profile">

👤

</div>

</div>

</div>

</div>
        """,
        unsafe_allow_html=True
    )