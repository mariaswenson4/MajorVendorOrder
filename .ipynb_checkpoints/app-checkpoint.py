import streamlit as st


st.set_page_config(
    page_title="Tabby & Jack's Analytics",
    page_icon="images/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

home = st.Page(
    "pages/home.py",
    title="Home",
    icon=":material/home:",
    default=True
)

mvo = st.Page(
    "pages/MVO.py",
    title="Major Vendor Order",
    icon=":material/shopping_cart:"
)

svo = st.Page(
    "pages/SVO.py",
    title="Small Vendor Order",
    icon=":material/shopping_basket:"
)

st.markdown(
    """
<style>
/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #FFF9EF;
    border-right: 1px solid #D7C8A4;
}

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #1D5A3E;
}

section[data-testid="stSidebar"] input {
    border-color: #D7C8A4;
}

/* Do NOT hide the whole header or sidebar button breaks */
header[data-testid="stHeader"] {
    background: transparent;
}

/* Hide app toolbar icons */
[data-testid="stToolbar"] {
    display: none !important;
}

/* Hide deploy/share area */
[data-testid="stStatusWidget"] {
    display: none !important;
}

/* Hide decoration */
[data-testid="stDecoration"] {
    display: none !important;
}

/* Hide main menu/footer */
#MainMenu,
footer {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
}
</style>
""",
    unsafe_allow_html=True
)
st.sidebar.markdown("### :material/search: Find a Report")
search = st.sidebar.text_input(
    "Search",
    placeholder="Search reports...",
    label_visibility="collapsed"
)

report_links = {
    "Major Vendor Order": "pages/MVO.py",
    "Small Vendor Order": "pages/SVO.py",
}

if search:
    filtered_reports = [
        name for name in report_links
        if search.lower() in name.lower()
    ]

    st.sidebar.markdown("**Results**")

    if filtered_reports:
        for report_name in filtered_reports:
            if st.sidebar.button(f"Open {report_name}", use_container_width=True):
                st.switch_page(report_links[report_name])
    else:
        st.sidebar.caption("No matching reports found.")

st.sidebar.divider()

pg = st.navigation(
    {
        "Navigation": [
            home,
            mvo,
            svo,
        ]
    },
    position="sidebar"
)

pg.run()