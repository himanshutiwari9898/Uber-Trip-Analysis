import streamlit as st
from database import load_data
from utils import format_currency, format_number
from charts import revenue_trend

st.set_page_config(
    page_title="Home",
    layout="wide"
)

st.title("🚖 Uber Trip Analysis Dashboard")

# Load data
data = load_data()

kpi = data["kpi"]
daily = data["daily"]



# Safety check
if kpi.empty:
    st.error("KPI Summary file not loaded.")
    st.stop()

# Get first row
row = kpi.iloc[0]

# KPI Cards
c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Total Trips",
        format_number(row["total_trips"])
    )

with c2:
    st.metric(
        "Total Revenue",
        format_currency(row["total_revenue"])
    )

with c3:
    st.metric(
        "Average Fare",
        format_currency(row["avg_fare"])
    )

c4, c5, c6 = st.columns(3)

with c4:
    st.metric(
        "Average Distance",
        row["avg_distance"]
    )

with c5:
    st.metric(
        "Average Driver Rating",
        row["avg_driver_rating"]
    )

with c6:
    st.metric(
        "Cancelled Trips",
        row["cancelled_trips"]
    )

st.divider()
st.subheader("📊 KPI Summary")
st.dataframe(kpi)

st.subheader("📈 Daily Revenue Trend")
fig = revenue_trend(daily)
st.plotly_chart(fig, width="stretch")

from charts import revenue_trend, monthly_revenue
monthly = data["monthly"]
st.subheader("📅 Monthly Revenue")
fig = monthly_revenue(monthly)
st.plotly_chart(fig, width="stretch")

from charts import vehicle_chart
vehicle = data["vehicle"]
st.subheader("🚗 Vehicle Performance")
fig = vehicle_chart(vehicle)
st.plotly_chart(fig, width="stretch")

from charts import payment_chart
payment = data["payment"]
st.subheader("💳 Payment Method Distribution")
fig = payment_chart(payment)
st.plotly_chart(fig, width="stretch")

from charts import cancellation_chart
cancel = data["cancel"]
st.subheader("❌ Cancellation Analysis")
fig = cancellation_chart(cancel)
st.plotly_chart(fig, width="stretch")

from charts import top_driver_chart
top_driver = data["top_driver"]
st.subheader("🏆 Top Drivers")
fig = top_driver_chart(top_driver)
st.plotly_chart(fig, width="stretch")

from charts import top_customer_chart
top_customer = data["top_customer"]
st.subheader("👤 Top Customers")
fig = top_customer_chart(top_customer)
st.plotly_chart(fig, width="stretch")
