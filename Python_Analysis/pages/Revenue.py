import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from database import load_data


import streamlit as st
from database import load_data
from utils import format_currency

from charts import (
    revenue_trend,
    monthly_revenue,
    vehicle_chart,
    payment_chart
)

# Page Setup
st.set_page_config(
    page_title="Revenue Analysis",
    layout="wide"
)
st.title("💰 Revenue Analysis Dashboard")

# Load Data
data = load_data()
kpi = data["kpi"]
daily = data["daily"]
monthly = data["monthly"]
vehicle = data["vehicle"]
payment = data["payment"]

# Revenue KPIs
row = kpi.iloc[0]
c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Total Revenue",
        format_currency(row["total_revenue"])
    )

with c2:
    st.metric(
        "Average Fare",
        format_currency(row["avg_fare"])
    )
    
# Daily Revenue
st.divider()
st.subheader("📈 Daily Revenue Trend")
st.plotly_chart(
    revenue_trend(daily),
    width="stretch"
)

# Monthly Revenue & Vehicle Revenue
col1, col2 = st.columns(2)
with col1:
    st.subheader("📅 Monthly Revenue")
    st.plotly_chart(
        monthly_revenue(monthly),
        width="stretch"
    )

with col2:
    st.subheader("🚗 Revenue by Vehicle")
    st.plotly_chart(
        vehicle_chart(vehicle),
        width="stretch"
    )

# Payment Method
st.divider()
st.subheader("💳 Revenue by Payment Method")
st.plotly_chart(
    payment_chart(payment),
    width="stretch"
)

# Revenue Table
st.divider()
st.subheader("📄 Monthly Revenue Data")
st.dataframe(monthly)

# CSV Download Button
csv = monthly.to_csv(index=False).encode("utf-8")
st.download_button(
    "⬇ Download Revenue Report",
    csv,
    "monthly_revenue.csv",
    "text/csv"
)
