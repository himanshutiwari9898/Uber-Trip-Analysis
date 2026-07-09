import streamlit as st

from database import load_data

from charts import (
    pickup_chart,
    drop_chart,
    city_chart,
    route_chart
)

st.set_page_config(
    page_title="Location Analysis",
    layout="wide"
)

st.title("📍 Location Analysis Dashboard")

data = load_data()

pickup = data["pickup"]
drop = data["drop"]
city = data["city"]
route = data["route"]

# ----------------------------
# Pickup & Drop
# ----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📍 Top Pickup Locations")

    st.plotly_chart(
        pickup_chart(pickup),
        use_container_width=True
    )

with col2:

    st.subheader("🏁 Top Drop Locations")

    st.plotly_chart(
        drop_chart(drop),
        use_container_width=True
    )

# ----------------------------
# City Performance
# ----------------------------

st.divider()

st.subheader("🌆 City Performance")

st.plotly_chart(
    city_chart(city),
    use_container_width=True
)

# ----------------------------
# Popular Routes
# ----------------------------

st.divider()

st.subheader("🛣️ Popular Routes")

st.plotly_chart(
    route_chart(route),
    use_container_width=True
)

# ----------------------------
# Table
# ----------------------------

st.divider()

st.subheader("Location Summary")

st.dataframe(city)