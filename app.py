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

/* Hide Streamlit top bar */
header[data-testid="stHeader"] {
    display: none;
}

/* Hide Share, GitHub, edit, star, menu icons */
[data-testid="stToolbar"] {
    display: none;
}

/* Hide orange/red decoration line */
[data-testid="stDecoration"] {
    display: none;
}

/* Hide old Streamlit menu */
#MainMenu {
    visibility: hidden;
}

/* Hide footer */
footer {
    visibility: hidden;
}

/* Pull content up after hiding header */
.block-container {
    padding-top: 1rem;
}
</style>
""",
    unsafe_allow_html=True
)