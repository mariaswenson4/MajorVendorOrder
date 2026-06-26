import streamlit as st


st.set_page_config(
    page_title="Tabby & Jack's Analytics",
    page_icon="images/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


PAGES = {
    "Home": {
        "path": "pages/home.py",
        "icon": "🏠",
        "category": "Home",
        "enabled": True,
    },
    "Major Vendor Order": {
        "path": "pages/MVO.py",
        "icon": "🛒",
        "category": "Ordering Reports",
        "enabled": True,
    },
    "Small Vendor Order": {
        "path": "pages/SVO.py",
        "icon": "🧾",
        "category": "Ordering Reports",
        "enabled": True,
    },
    "Dusty Report Transfer": {
        "path": "pages/dusty.py",
        "icon": "📦",
        "category": "Inventory Reports",
        "enabled": False,
    },
    "Sales by Brand": {
        "path": "pages/brandsale.py",
        "icon": "🏷️",
        "category": "Inventory Reports",
        "enabled": False,
    },
}


st.markdown(
    """
<style>
section[data-testid="stSidebar"] {
    background-color: #FFF9EF;
    border-right: 1px solid #D7C8A4;
}

section[data-testid="stSidebar"] h3 {
    color: #1D5A3E;
}

section[data-testid="stSidebar"] button {
    border-radius: 12px;
    border: 1px solid #D7C8A4;
    background-color: #FFF7EA;
    color: #1D5A3E;
    font-weight: 700;
}

section[data-testid="stSidebar"] button:hover {
    background-color: #EF8B1D;
    color: white;
}
</style>
""",
    unsafe_allow_html=True,
)


if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"


st.sidebar.markdown("### 🔎 Search Reports")

search = st.sidebar.text_input(
    "Search",
    placeholder="Search tools...",
    label_visibility="collapsed"
)

if search:
    matches = [
        name for name, info in PAGES.items()
        if search.lower() in name.lower()
        or search.lower() in info["category"].lower()
    ]

    if matches:
        for name in matches:
            info = PAGES[name]

            if info["enabled"]:
                if st.sidebar.button(
                    f"{info['icon']} {name}",
                    use_container_width=True,
                    key=f"search_{name}"
                ):
                    st.session_state.current_page = name
                    st.rerun()
            else:
                st.sidebar.button(
                    f"{info['icon']} {name} · Coming Soon",
                    disabled=True,
                    use_container_width=True,
                    key=f"search_disabled_{name}"
                )
    else:
        st.sidebar.caption("No matching tools found.")

st.sidebar.divider()


st.sidebar.markdown("### Navigation")

for category in ["Home", "Ordering Reports", "Inventory Reports"]:
    category_pages = {
        name: info for name, info in PAGES.items()
        if info["category"] == category
    }

    if category_pages:
        st.sidebar.markdown(f"**{category}**")

        for name, info in category_pages.items():
            label = f"{info['icon']} {name}"

            if name == st.session_state.current_page:
                label = f"➤ {label}"

            if info["enabled"]:
                if st.sidebar.button(
                    label,
                    use_container_width=True,
                    key=f"nav_{name}"
                ):
                    st.session_state.current_page = name
                    st.rerun()
            else:
                st.sidebar.button(
                    f"{label} · Coming Soon",
                    disabled=True,
                    use_container_width=True,
                    key=f"nav_disabled_{name}"
                )


page_path = PAGES[st.session_state.current_page]["path"]

with open(page_path, "r", encoding="utf-8") as file:
    page_code = file.read()

exec(page_code)