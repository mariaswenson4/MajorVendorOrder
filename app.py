import streamlit as st


st.set_page_config(
    page_title="Tabby & Jack's Analytics",
    page_icon="images/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Pages
home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

mvo = st.Page(
    "pages/MVO.py",
    title="Major Vendor Order",
    icon="🛒"
)

svo = st.Page(
    "pages/SVO.py",
    title="Small Vendor Order",
    icon="🧾"
)


# Sidebar styling
# Sidebar styling
st.markdown(
    """
<style>
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
</style>
""",
    unsafe_allow_html=True
)

# Search shortcut
st.sidebar.markdown("### 🔎 Find a Report")

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


# Main built-in sidebar navigation
pg = st.navigation(
    {
        "🏠 Home": [home],
        "📦 Ordering Reports": [mvo, svo],
    }
)

pg.run()