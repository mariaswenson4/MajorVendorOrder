import streamlit as st

st.title(":material/link: Helpful Links")

st.write("Easy access to commonly used websites and tools at Tabby & Jack's!")

st.divider()

# st.subheader("Ordering")

st.link_button(
     ":material/inventory_2: Inventory Schedule",
     "https://docs.google.com/spreadsheets/d/1xA57rmNrJncakYEKfHGBNdOwWs4yPEyrK3YzqTE4So8/edit?usp=sharing",
     use_container_width=True,
 )

# st.link_button(
#     "📦 Instacart Portal",
#     "https://your-instacart-url.com",
#     use_container_width=True,
# )

# st.divider()

# st.subheader("Communication")

# st.link_button(
#     "💬 Slack",
#     "https://slack.com",
#     use_container_width=True,
# )

# st.link_button(
#     "📅 Google Calendar",
#     "https://calendar.google.com",
#     use_container_width=True,
# )

# st.divider()

# st.subheader("Company")

# st.link_button(
#     "📊 Inventory Spreadsheet",
#     "https://docs.google.com/...",
#     use_container_width=True,
# )

# st.link_button(
#     "📁 Google Drive",
#     "https://drive.google.com",
#     use_container_width=True,
# )