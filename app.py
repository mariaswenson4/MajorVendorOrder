import streamlit as st

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

mvo = st.Page(
    "pages/mvo.py",
    title="Major Vendor Order",
    icon="📦"
)

map_page = st.Page(
    "pages/map.py",
    title="MAP Price Update",
    icon="🏷️"
)

pg = st.navigation([home, mvo, map_page])
pg.run()