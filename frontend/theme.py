import streamlit as st


def apply_theme():

    st.set_page_config(
        page_title="Autonomous Data Science Co-Pilot",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown(
        """
<style>

/* ==========================================================
GOOGLE FONT
========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

/* ==========================================================
APP
========================================================== */

.stApp{
    background:#0B1120;
    color:white;
}

/* ==========================================================
MAIN CONTAINER
========================================================== */

.block-container{
    max-width:94%;
    padding-top:1.5rem;
    padding-bottom:2rem;
}

/* ==========================================================
HEADINGS
========================================================== */

h1,h2,h3,h4,h5,h6{
    color:white !important;
    font-weight:800;
    letter-spacing:-.5px;
}

p,label,span{
    color:#CBD5E1;
}

/* ==========================================================
SIDEBAR
========================================================== */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #273449;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* ==========================================================
BUTTONS
========================================================== */

.stButton > button{

    width:100%;

    height:52px;

    border:none;

    border-radius:16px;

    font-weight:700;

    color:white;

    background:linear-gradient(
        90deg,
        #6366F1,
        #8B5CF6
    );

    transition:.25s;
}

.stButton > button:hover{

    transform:translateY(-3px);

    box-shadow:
    0 12px 28px rgba(99,102,241,.45);

}

/* ==========================================================
FILE UPLOADER
========================================================== */

[data-testid="stFileUploader"]{

    background:#1E293B;

    border:2px dashed #475569;

    border-radius:22px;

    padding:24px;

}

/* ==========================================================
DATAFRAME
========================================================== */

div[data-testid="stDataFrame"]{

    border-radius:18px;

    overflow:hidden;

    border:1px solid #334155;

}

/* ==========================================================
TABLE HEADER
========================================================== */

thead tr th{

    background:#312E81 !important;

    color:white !important;

}

/* ==========================================================
INPUTS
========================================================== */

.stTextInput input,
.stTextArea textarea{

    background:#1E293B !important;

    color:white !important;

    border-radius:12px;

}

.stSelectbox div[data-baseweb="select"]{

    background:#1E293B;

    border-radius:12px;

}

/* ==========================================================
METRIC
========================================================== */

div[data-testid="metric-container"]{

    background:#1E293B;

    border:1px solid #334155;

    border-radius:20px;

    padding:20px;

    box-shadow:
    0 10px 25px rgba(0,0,0,.30);

}

/* ==========================================================
SEGMENTED CONTROL
========================================================== */

button[kind="segmented_control"]{

    border-radius:12px;

}

/* ==========================================================
SUCCESS / INFO / WARNING
========================================================== */

.stSuccess,
.stInfo,
.stWarning,
.stError{

    border-radius:16px;

}

/* ==========================================================
CONTAINERS
========================================================== */

div[data-testid="stVerticalBlock"] > div:has(> div[data-testid="stHorizontalBlock"]){

    border-radius:20px;

}

/* ==========================================================
GLASS CARD
========================================================== */

.glass-card{

    background:rgba(30,41,59,.82);

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,.08);

    border-radius:24px;

    padding:24px;

    margin-bottom:22px;

    box-shadow:
    0 25px 45px rgba(0,0,0,.30);

    transition:.35s;

}

.glass-card:hover{

    transform:translateY(-5px);

    border:1px solid #6366F1;

    box-shadow:
    0 35px 60px rgba(99,102,241,.28);

}

.glass-title{

    font-size:22px;

    font-weight:700;

    color:white;

    margin-bottom:20px;

}

/* ==========================================================
STAT CARD
========================================================== */

.stat-card{

    background:linear-gradient(
        145deg,
        #1E293B,
        #111827
    );

    border-radius:22px;

    padding:24px;

    height:190px;

    border:1px solid rgba(255,255,255,.06);

    transition:.35s;

    box-shadow:
    0 15px 35px rgba(0,0,0,.35);

}

.stat-card:hover{

    transform:translateY(-6px);

    border-color:#6366F1;

}

.stat-icon{

    width:60px;

    height:60px;

    border-radius:18px;

    display:flex;

    align-items:center;

    justify-content:center;

    font-size:30px;

    margin-bottom:18px;

}

.stat-title{

    color:#94A3B8;

    font-size:15px;

}

.stat-value{

    color:white;

    font-size:34px;

    font-weight:800;

    margin-top:8px;

}

.stat-change{

    color:#22C55E;

    margin-top:10px;

    font-size:14px;

}

/* ==========================================================
SCROLLBAR
========================================================== */

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-track{
    background:#0F172A;
}

::-webkit-scrollbar-thumb{
    background:#6366F1;
    border-radius:20px;
}

</style>
""",
        unsafe_allow_html=True
    )