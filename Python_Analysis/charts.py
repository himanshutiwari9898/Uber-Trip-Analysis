import plotly.express as px


def revenue_trend(df):

    fig = px.line(
        df,
        x="trip_date",
        y="total_revenue",
        markers=True,
        title="Daily Revenue Trend"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    return fig

def monthly_revenue(df):

    fig = px.bar(
        df,
        x="month_name",
        y="revenue",
        title="Monthly Revenue"
    )
    fig.update_layout(
        template="plotly_white",
        height=420
    )
    return fig

def vehicle_chart(df):

    fig = px.bar(
        df,
        x="vehicle_type",
        y="revenue",
        color="vehicle_type",
        title="Revenue by Vehicle"
    )
    fig.update_layout(
        template="plotly_white",
        height=420,
        showlegend=False
    )
    return fig

def payment_chart(df):

    fig = px.pie(
        df,
        names="payment_method",
        values="total_transactions",
        hole=0.5,
        title="Payment Method Distribution"
    )
    fig.update_layout(
        template="plotly_white",
        height=420
    )
    return fig

def cancellation_chart(df):

    fig = px.pie(
        df,
        names="cancellation_reason",
        values="total",
        hole=0.5,
        title="Cancellation Analysis"
    )
    fig.update_layout(
        template="plotly_white",
        height=420
    )
    return fig

def top_driver_chart(df):

    fig = px.bar(
        df,
        x="driver_id",
        y="revenue",
        color="rating",
        title="Top 10 Drivers by Revenue"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    return fig

def top_customer_chart(df):

    fig = px.bar(
        df,
        x="customer_id",
        y="total_spent",
        title="Top 10 Customers"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    return fig

# Hourly Demand
def hourly_chart(df):

    fig = px.line(
        df,
        x="booking_hour",
        y="total_trips",
        markers=True,
        title="Trips by Hour"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    return fig

# Pickup Locations
def pickup_chart(df):

    fig = px.bar(
        df.head(10),
        x="pickup_location",
        y="total_pickups",
        color="total_pickups",
        title="Top Pickup Locations"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    return fig

# Drop Locations
def drop_chart(df):

    fig = px.bar(
        df.head(10),
        x="drop_location",
        y="total_dropoffs",
        color="total_dropoffs",
        title="Top Drop Locations"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    return fig

# Popular Routes
def route_chart(df):

    fig = px.bar(
        df.head(10),
        x="pickup_location",
        y="trips",
        color="drop_location",
        title="Popular Routes"
    )
    fig.update_layout(
        template="plotly_white",
        height=500
    )
    return fig

# Driver Rating Chart
def driver_rating_chart(df):

    fig = px.bar(
        df.head(10),
        x="driver_name",
        y="avg_rating",
        color="avg_rating",
        title="Driver Ratings"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig

# Driver Revenue Chart
def driver_revenue_chart(df):

    fig = px.bar(
        df.head(10),
        x="driver_name",
        y="revenue",
        color="revenue",
        title="Driver Revenue"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    return fig

# Customer Spending
def customer_spending_chart(df):

    fig = px.bar(
        df.head(10),
        x="customer_name",
        y="total_spent",
        color="total_spent",
        title="Customer Spending"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    return fig

# Customer Rating
def customer_rating_chart(df):

    fig = px.bar(
        df.head(10),
        x="customer_name",
        y="avg_rating",
        color="avg_rating",
        title="Customer Ratings"
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    return fig

# Location chart
def city_chart(df):

    fig = px.bar(
        df,
        x="city",
        y="revenue",
        color="revenue",
        title="Revenue by City"
    )

    fig.update_layout(
        template="plotly_white",
        height=450
    )

    return fig