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

section[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.25rem;
}

section[data-testid="stSidebar"] * {
    color: #FFF9EF !important;
    font-family: "Source Sans Pro", sans-serif;
}

/* Logo/header card */
.sidebar-brand {
    text-align: center;
    padding: 1rem .75rem 1.25rem .75rem;
    margin-bottom: 1rem;
    border-radius: 18px;
    background: rgba(255, 249, 239, .12);
    border: 1px solid rgba(255, 249, 239, .22);
}

.sidebar-brand img {
    width: 105px;
    border-radius: 12px;
    background: #FFF9EF;
    padding: .4rem;
    margin-bottom: .75rem;
}

.sidebar-brand-title {
    font-size: 1.05rem;
    font-weight: 800;
    color: #FFF9EF !important;
    line-height: 1.2;
}

.sidebar-brand-subtitle {
    font-size: .78rem;
    color: rgba(255, 249, 239, .82) !important;
    margin-top: .25rem;
}

/* Search title */
.sidebar-search-title {
    color: #F3A653 !important;
    font-weight: 800;
    font-size: 1rem;
    margin-top: .5rem;
    margin-bottom: .35rem;
}

/* Search box */
section[data-testid="stSidebar"] input {
    background: #FFF9EF !important;
    color: #1D5A3E !important;
    border: 1px solid #F3A653 !important;
    border-radius: 10px !important;
}

section[data-testid="stSidebar"] input::placeholder {
    color: #777777 !important;
}

/* Search result buttons */
section[data-testid="stSidebar"] button {
    border-radius: 10px !important;
    background: rgba(255, 249, 239, .12) !important;
    border: 1px solid rgba(255, 249, 239, .22) !important;
}

section[data-testid="stSidebar"] button:hover {
    background: rgba(243, 166, 83, .28) !important;
    border-color: #F3A653 !important;
}

/* Hide plain Navigation heading */
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p:has(span),
section[data-testid="stSidebarNav"] > div:first-child {
    display: none;
}

/* Navigation area */
[data-testid="stSidebarNav"] {
    padding-top: .25rem;
}

[data-testid="stSidebarNav"] ul {
    padding-left: 0;
}

[data-testid="stSidebarNav"] li {
    margin-bottom: .35rem;
}

/* Navigation links */
[data-testid="stSidebarNav"] a {
    border-radius: 12px !important;
    padding: .55rem .75rem !important;
    transition: all .2s ease;
}

/* Hover */
[data-testid="stSidebarNav"] a:hover {
    background: rgba(243, 166, 83, .20) !important;
}

/* Selected page */
[data-testid="stSidebarNav"] li[data-selected="true"] a {
    background: #F3A653 !important;
    color: #1D5A3E !important;
    font-weight: 800 !important;
}

[data-testid="stSidebarNav"] li[data-selected="true"] a * {
    color: #1D5A3E !important;
}

/* Divider */
section[data-testid="stSidebar"] hr {
    border-color: rgba(255, 249, 239, .25);
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

st.sidebar.markdown(
    """
<div class="sidebar-brand">
    <img src="app/static/logo.png">
    <div class="sidebar-brand-title">Tabby & Jack's</div>
    <div class="sidebar-brand-subtitle">Analytics Hub</div>
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="sidebar-search-title">:material/search: Find a Report</div>',
    unsafe_allow_html=True
)

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
    }
)

pg.run()