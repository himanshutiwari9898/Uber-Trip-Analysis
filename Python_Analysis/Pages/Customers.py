import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


import streamlit as st
from database import load_data
from charts import (
    top_customer_chart,
    customer_spending_chart,
    customer_rating_chart
)

st.set_page_config(
    page_title="Customer Analysis",
    layout="wide"
)

st.title("👤 Customer Analysis Dashboard")

data = load_data()

customer = data["customer"]
top_customer = data["top_customer"]

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Total Customers",
        len(customer)
    )

with col2:
    st.metric(
        "Average Customer Rating",
        round(customer["avg_rating"].mean(),2)
    )

st.divider()

st.subheader("🏆 Top Customers")

st.plotly_chart(
    top_customer_chart(top_customer),
    use_container_width=True
)

col3,col4 = st.columns(2)

with col3:

    st.subheader("💰 Customer Spending")

    st.plotly_chart(
        customer_spending_chart(customer),
        use_container_width=True
    )

with col4:

    st.subheader("⭐ Customer Ratings")

    st.plotly_chart(
        customer_rating_chart(customer),
        use_container_width=True
    )

st.divider()

st.subheader("Customer Summary")

st.dataframe(customer)
