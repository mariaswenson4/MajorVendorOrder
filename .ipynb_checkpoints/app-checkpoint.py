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
section[data-testid="stSidebar"] {
    background: #5C8067;
    border-right: none;
}

section[data-testid="stSidebar"] * {
    color: #FFF9EF !important;
}

/* Search input */
section[data-testid="stSidebar"] input {
    background: #FFF9EF !important;
    color: #1D5A3E !important;
    border: 1px solid #F3A653 !important;
    border-radius: 10px !important;
}

section[data-testid="stSidebar"] input::placeholder {
    color: #777777 !important;
}

/* Sidebar links */
section[data-testid="stSidebar"] a {
    border-radius: 12px !important;
    padding: .45rem .65rem !important;
    text-decoration: none !important;
}

section[data-testid="stSidebar"] a:hover {
    background: rgba(243, 166, 83, .22) !important;
}

/* Divider */
section[data-testid="stSidebar"] hr {
    border-color: rgba(255, 249, 239, .25);
}

/* Keep header so sidebar can reopen */
header[data-testid="stHeader"] {
    background: transparent;
}

/* Hide Streamlit decoration/menu/footer */
[data-testid="stDecoration"] {
    display: none;
}

#MainMenu,
footer {
    visibility: hidden;
}
</style>
""",
    unsafe_allow_html=True
)

# Custom sidebar header
with st.sidebar:
    st.image("images/logo.png", width=115)

    st.markdown(
        """
        <div style="font-size:1.15rem; font-weight:800; line-height:1.2;">
            Tabby & Jack's
        </div>
        <div style="font-size:.85rem; opacity:.85; margin-bottom:1.25rem;">
            Analytics Hub
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🔎 Find a Report")
    search = st.text_input(
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

        st.markdown("**Results**")

        if filtered_reports:
            for report_name in filtered_reports:
                if st.button(f"Open {report_name}", use_container_width=True):
                    st.switch_page(report_links[report_name])
        else:
            st.caption("No matching reports found.")

    st.divider()

st.markdown("### Navigation")

if st.button("🏠 Home", use_container_width=True):
    st.switch_page("pages/home.py")

if st.button("🛒 Major Vendor Order", use_container_width=True):
    st.switch_page("pages/MVO.py")

if st.button("🧺 Small Vendor Order", use_container_width=True):
    st.switch_page("pages/SVO.py")

# Hide default Streamlit navigation
pg = st.navigation(
    [home, mvo, svo],
    position="hidden"
)

pg.run()