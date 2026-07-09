import streamlit as st

st.set_page_config(
    page_title="Uber Trip Analysis",
    layout="wide"
)

st.title("🚖 Uber Trip Analysis Dashboard")

st.write(
"""
👈 Select a page from the sidebar.

Pages Available:

- Home
- Revenue
- Trips
- Drivers
- Customers
- Locations
"""
)