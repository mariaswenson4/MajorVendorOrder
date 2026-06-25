import streamlit as st

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

map_page = st.Page(
    "pages/SVO.py",
    title="Small Vendor Order",
    icon="📦"
)

pg = st.navigation([home, mvo, map_page])
pg.run()