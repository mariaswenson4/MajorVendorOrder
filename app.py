import streamlit as st

st.set_page_config(
    page_title="Tabby & Jack's Analytics",
    page_icon="images/logo.png",
    layout="wide"
)

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

mvo = st.Page(
    "pages/MVO.py",
    title="Major Vendor Order",
    icon="📦"
)

svo = st.Page(
    "pages/SVO.py",
    title="Small Vendor Order",
    icon="📦"
)

pg = st.navigation(
    {
        "Home": [home],
        "Reports": [mvo, svo],
    }
)

pg.run()