import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from database import load_data

import streamlit as st

from database import load_data
from utils import format_number

from charts import (
    vehicle_chart,
    cancellation_chart,
    pickup_chart,
    drop_chart,
    route_chart,
    hourly_chart
)

st.set_page_config(
    page_title="Trip Analysis",
    layout="wide"
)

st.title("🚖 Trip Analysis Dashboard")

data = load_data()

kpi = data["kpi"]
hourly = data["hourly"]
vehicle = data["vehicle"]
cancel = data["cancel"]
pickup = data["pickup"]
drop = data["drop"]
route = data["route"]

row = kpi.iloc[0]

c1,c2=st.columns(2)

with c1:
    st.metric(
        "Total Trips",
        format_number(row["total_trips"])
    )

with c2:
    st.metric(
        "Cancelled Trips",
        format_number(row["cancelled_trips"])
    )

st.divider()

st.subheader("🕒 Hourly Demand")

st.plotly_chart(
    hourly_chart(hourly),
    use_container_width=True
)

col1,col2=st.columns(2)

with col1:

    st.subheader("🚗 Vehicle Performance")

    st.plotly_chart(
        vehicle_chart(vehicle),
        use_container_width=True
    )

with col2:

    st.subheader("❌ Cancellation Analysis")

    st.plotly_chart(
        cancellation_chart(cancel),
        use_container_width=True
    )

col3,col4=st.columns(2)

with col3:

    st.subheader("📍 Top Pickup Locations")

    st.plotly_chart(
        pickup_chart(pickup),
        use_container_width=True
    )

with col4:

    st.subheader("🏁 Top Drop Locations")

    st.plotly_chart(
        drop_chart(drop),
        use_container_width=True
    )

st.subheader("🛣️ Popular Routes")

st.plotly_chart(
    route_chart(route),
    use_container_width=True
)

st.divider()

st.subheader("Hourly Demand Data")

st.dataframe(hourly)