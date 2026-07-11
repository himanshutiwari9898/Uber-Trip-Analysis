#  Demo Link
https://uber-trip-analysiss.streamlit.app/

# 🚖 Uber Trip Analysis Dashboard

An end-to-end Data Analytics project that analyzes Uber trip data using **SQL**, **Python**, and **Streamlit**. The project focuses on data cleaning, business intelligence, KPI reporting, and interactive dashboard development to uncover trends in trip bookings, revenue, customer behavior, and driver performance.

---

## 📌 Project Overview

This project simulates a real-world analytics workflow by processing raw Uber trip data, cleaning it using SQL, generating business insights through advanced SQL queries, and visualizing key performance indicators in an interactive Streamlit dashboard.

The objective is to demonstrate practical data analysis skills that are commonly used in business and product analytics roles.

---

## 🎯 Objectives

* Clean and preprocess raw Uber trip data using SQL.
* Perform exploratory data analysis and generate business insights.
* Analyze booking trends, revenue, cancellations, and customer behavior.
* Build an interactive dashboard for business stakeholders.
* Showcase SQL and Python skills through an end-to-end analytics project.

---

## 🛠️ Tech Stack

* **SQL (MySQL)**
* **Python**
* **Pandas**
* **Streamlit**
* **Plotly**
* **SQLAlchemy**
* **PyMySQL**

---

## 📂 Project Structure

```text
Uber Trip Analysis/
│
├── data/
│   ├── customers.csv
│   ├── drivers.csv
│   ├── trips.csv
│
├── sql/
│
│
└── Python_Analysis/
│   ├── database.py
│   ├── app.py
│   └── pages/
│        ├──1_Home.py
│        ├──Customers.py
│        ├──Drivers.py
│        ├──Loctions.py
│        ├──Revenue.py
│        ├──Trip.py
│
├── dashboard_screenshots/
│
├── requirements.txt
│
└── README.md
```

---

## 🗃️ Database Schema

### Trips Table

| Column          |
| --------------- |
| Trip ID         |
| Customer ID     |
| Driver ID       |
| Pickup Datetime |
| Pickup Location |
| Drop Location   |
| Distance (km)   |
| Fare            |
| Vehicle Type    |
| Payment Method  |
| Trip Status     |
| Booking Date    |
| Booking Time    |
| Rating          |

### Drivers Table

* Driver ID
* Driver Name
* Vehicle Number
* City
* Joining Date

### Customers Table

* Customer ID
* Customer Name
* Gender
* Age
* City

---

## 🧹 Data Cleaning

The following SQL operations were performed:

* Removed duplicate records using `ROW_NUMBER()`
* Handled missing values
* Removed invalid fares
* Removed zero-distance trips
* Standardized payment methods
* Converted datetime formats
* Extracted trip date and pickup hour
* Created analysis-ready tables

---

## 📊 SQL Concepts Used

* SELECT
* WHERE
* GROUP BY
* HAVING
* ORDER BY
* CASE WHEN
* Aggregate Functions
* Date Functions
* Common Table Expressions (CTEs)
* JOINs
* Window Functions
* RANK()
* DENSE_RANK()
* ROW_NUMBER()

---

## 📈 Business Insights Generated

* Total Revenue
* Total Trips
* Average Fare
* Average Trip Distance
* Peak Booking Hours
* Revenue by Vehicle Type
* Top Pickup Locations
* Top Drop Locations
* Monthly Revenue Trend
* Driver Performance Ranking
* Customer Lifetime Value
* Cancellation Analysis
* Average Driver Ratings
* Payment Method Distribution

---

## 📊 Dashboard Features

### KPI Cards

* Total Trips
* Total Revenue
* Average Fare
* Average Rating
* Cancellation Rate

### Interactive Charts

* Revenue Trend
* Trips by Hour
* Trips by Vehicle Type
* Revenue by Vehicle Type
* Top Pickup Locations
* Top Drop Locations
* Trip Status Distribution
* Driver Revenue
* Customer Spending
* Monthly Revenue Trend
* Fare Distribution
* Rating Distribution

---

## 🎛️ Dashboard Filters

* Date Range
* Vehicle Type
* Pickup Location
* Driver
* Customer
* Payment Method
* Trip Status

---

## 📸 Dashboard Preview

> Add your dashboard screenshots inside the **dashboard_screenshots** folder and update this section with images.

---

## 🚀 How to Run

### Clone the Repository

```bash
git clone https://github.com/yourusername/Uber-Trip-Analysis.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

* Create a MySQL database.
* Run the SQL scripts in the `sql/` folder.
* Import the dataset into the `trips`, `drivers`, and `customers` tables.
* Update the database credentials in `database.py`.

### Launch the Dashboard

```bash
streamlit run python/app.py
```

---

## 📌 Key Learnings

* SQL Data Cleaning
* Relational Database Design
* Business KPI Development
* Advanced SQL Analytics
* Window Functions
* Data Visualization
* Interactive Dashboard Development
* Business Insight Generation
* End-to-End Data Analytics Workflow

---

## 📚 Future Improvements

* Predict trip demand using Machine Learning
* Driver performance prediction
* Revenue forecasting
* Geographic heatmaps
* Real-time dashboard integration
* User authentication
* Cloud deployment (Render, AWS, or Azure)

---

## 👨‍💻 Author

**Himanshu Tiwari**

* B.Tech (Information Technology)
* JSS Academy of Technical Education, Noida

If you found this project useful, consider giving the repository a ⭐.
