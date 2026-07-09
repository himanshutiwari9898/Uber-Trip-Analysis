import streamlit as st
import pandas as pd
from pathlib import Path

# Data folder path
DATA_PATH = Path(__file__).resolve().parent.parent / "data"

@st.cache_data
def load_csv(filename):
    file_path = DATA_PATH / filename

    if file_path.exists():
        return pd.read_csv(file_path)
    else:
        st.error(f"File not found: {filename}")
        return pd.DataFrame()

@st.cache_data
def load_data():

    data = {
        "kpi": load_csv("Kpi_summary.csv"),
        "daily": load_csv("daily_revenue_summary.csv"),
        "monthly": load_csv("monthly_revenue.csv"),
        "vehicle": load_csv("vehicle_performace.csv"),
        "driver": load_csv("driver_performance.csv"),
        "customer": load_csv("customers_summary.csv"),
        "payment": load_csv("payment_method.csv"),
        "cancel": load_csv("cancellation_summary.csv"),
        "hourly": load_csv("hourly_demand.csv"),
        "city": load_csv("city_performance.csv"),
        "pickup": load_csv("top_pickup_locations.csv"),
        "drop": load_csv("top_drop_locations.csv"),
        "route": load_csv("popular_routes.csv"),
        "top_driver": load_csv("top_drivers.csv"),
        "top_customer": load_csv("top_customers.csv")
    }

    return data

