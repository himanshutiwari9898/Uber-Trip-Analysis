import streamlit as st

from database import load_data
from charts import (
    top_driver_chart,
    driver_rating_chart,
    driver_revenue_chart
)

st.set_page_config(
    page_title="Driver Analysis",
    layout="wide"
)

st.title("👨‍✈️ Driver Performance Dashboard")

data = load_data()

driver = data["driver"]
top_driver = data["top_driver"]

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Drivers", len(driver))

with col2:
    st.metric(
        "Average Driver Rating",
        round(driver["avg_rating"].mean(), 2)
    )

st.divider()

st.subheader("🏆 Top Drivers")

st.plotly_chart(
    top_driver_chart(top_driver),
    use_container_width=True
)

col3, col4 = st.columns(2)

with col3:

    st.subheader("⭐ Driver Ratings")

    st.plotly_chart(
        driver_rating_chart(driver),
        use_container_width=True
    )

with col4:

    st.subheader("💰 Driver Revenue")

    st.plotly_chart(
        driver_revenue_chart(driver),
        use_container_width=True
    )

st.divider()

st.subheader("Driver Performance Data")

st.dataframe(driver)