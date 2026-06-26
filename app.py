import streamlit as st

st.set_page_config(
    page_title="Tabby & Jack's Analytics",
    page_icon="images/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

pages = {
    "Home": st.Page(
        "pages/home.py",
        title="Home",
        icon=":material/home:",
        default=True
    ),
    "Major Vendor Order": st.Page(
        "pages/MVO.py",
        title="Major Vendor Order",
        icon=":material/shopping_cart:"
    ),
    "Small Vendor Order": st.Page(
        "pages/SVO.py",
        title="Small Vendor Order",
        icon=":material/shopping_basket:"
    ),
}

report_links = {
    "Major Vendor Order": "pages/MVO.py",
    "Small Vendor Order": "pages/SVO.py",
}

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

section[data-testid="stSidebar"] input {
    background: #FFF9EF !important;
    color: #1D5A3E !important;
    border: 1px solid #F3A653 !important;
    border-radius: 10px !important;
}

section[data-testid="stSidebar"] input::placeholder {
    color: #777777 !important;
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255, 249, 239, .25);
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button {
    background-color: #D18936 !important;
    color: #FFF9EF !important;
    border: 1px solid #D18936 !important;
    border-radius: 12px !important;
    height: 42px !important;
    font-weight: 800 !important;
}

section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
    background-color: #F3A653 !important;
    color: #1D5A3E !important;
    border-color: #F3A653 !important;
}

header[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stDecoration"] {
    display: none;
}

button[data-testid="stBaseButton-headerNoPadding"] {
    display: none !important;
}

#MainMenu,
footer {
    visibility: hidden;
}
</style>
""",
    unsafe_allow_html=True
)


def sidebar_nav_button(label, page):
    if st.button(label, use_container_width=True):
        st.switch_page(page)


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

    st.markdown("### :material/search: Find a Report")

    search = st.text_input(
        "Search",
        placeholder="Search reports...",
        label_visibility="collapsed"
    )

    if search:
        st.markdown("**Results**")

        matches = {
            name: page
            for name, page in report_links.items()
            if search.lower() in name.lower()
        }

        if matches:
            for name, page in matches.items():
                sidebar_nav_button(f"Open {name}", page)
        else:
            st.caption("No matching reports found.")

    st.divider()

    st.markdown("### Navigation")

    sidebar_nav_button(":material/home: Home", "pages/home.py")
    sidebar_nav_button(":material/shopping_cart: Major Vendor Order", "pages/MVO.py")
    sidebar_nav_button(":material/shopping_basket:", "pages/SVO.py")


pg = st.navigation(
    list(pages.values()),
    position="hidden"
)

pg.run()