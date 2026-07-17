from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("Business Analytics Dashboard")

st.write(
    "Interactive dashboard for exploring sales, customers, "
    "and KPI performance."
)


# --------------------------------------------------
# File paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"


# --------------------------------------------------
# Load datasets
# --------------------------------------------------

@st.cache_data
def load_data():
    customers = pd.read_parquet(
        DATA_DIR / "customers_clean.parquet"
    )

    orders = pd.read_parquet(
        DATA_DIR / "orders_clean.parquet"
    )

    order_items = pd.read_parquet(
        DATA_DIR / "order_items_clean.parquet"
    )

    products = pd.read_parquet(
        DATA_DIR / "products_clean.parquet"
    )

    transactions = pd.read_parquet(
        DATA_DIR / "transactions_clean.parquet"
    )

    return (
        customers,
        orders,
        order_items,
        products,
        transactions,
    )


customers, orders, order_items, products, transactions = load_data()


# --------------------------------------------------
# Combine datasets
# --------------------------------------------------

dashboard_data = order_items.merge(
    products,
    on="product_id",
    how="left",
)

dashboard_data = dashboard_data.merge(
    orders,
    on="order_id",
    how="left",
)

dashboard_data = dashboard_data.merge(
    customers,
    on="customer_id",
    how="left",
)

dashboard_data = dashboard_data.merge(
    transactions,
    on="order_id",
    how="left",
)


# --------------------------------------------------
# Prepare date columns
# --------------------------------------------------

dashboard_data["order_date"] = pd.to_datetime(
    dashboard_data["order_date"],
    errors="coerce",
)

dashboard_data["transaction_date"] = pd.to_datetime(
    dashboard_data["transaction_date"],
    errors="coerce",
)

dashboard_data["signup_date"] = pd.to_datetime(
    dashboard_data["signup_date"],
    errors="coerce",
)


# --------------------------------------------------
# Clean payment-status values
# --------------------------------------------------

dashboard_data["payment_status_clean"] = (
    dashboard_data["payment_status"]
    .fillna("")
    .astype(str)
    .str.strip()
    .str.lower()
)

successful_statuses = {
    "success",
    "successful",
    "completed",
    "paid",
    "approved",
}


# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")


category_options = ["All"] + sorted(
    dashboard_data["category"]
    .dropna()
    .unique()
    .tolist()
)

selected_category = st.sidebar.selectbox(
    "Select Category",
    category_options,
)


city_options = ["All"] + sorted(
    dashboard_data["city"]
    .dropna()
    .unique()
    .tolist()
)

selected_city = st.sidebar.selectbox(
    "Select City",
    city_options,
)


valid_order_dates = dashboard_data["order_date"].dropna()

if valid_order_dates.empty:
    st.error("No valid order dates were found.")
    st.stop()


minimum_date = valid_order_dates.min().date()
maximum_date = valid_order_dates.max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(minimum_date, maximum_date),
    min_value=minimum_date,
    max_value=maximum_date,
)


# --------------------------------------------------
# Apply filters
# --------------------------------------------------

filtered_data = dashboard_data.copy()


if selected_category != "All":
    filtered_data = filtered_data[
        filtered_data["category"] == selected_category
    ]


if selected_city != "All":
    filtered_data = filtered_data[
        filtered_data["city"] == selected_city
    ]


if len(selected_dates) == 2:
    start_date, end_date = selected_dates

    filtered_data = filtered_data[
        (
            filtered_data["order_date"].dt.date
            >= start_date
        )
        &
        (
            filtered_data["order_date"].dt.date
            <= end_date
        )
    ]


if filtered_data.empty:
    st.warning("No data matches the selected filters.")
    st.stop()


# --------------------------------------------------
# Calculate KPIs
# --------------------------------------------------

total_revenue = filtered_data["total_price"].sum()

total_orders = filtered_data["order_id"].nunique()

total_items_sold = filtered_data["quantity"].sum()

average_order_value = (
    total_revenue / total_orders
    if total_orders > 0
    else 0
)


successful_payments = filtered_data[
    filtered_data["payment_status_clean"].isin(
        successful_statuses
    )
]["order_id"].nunique()


payment_success_rate = (
    successful_payments / total_orders * 100
    if total_orders > 0
    else 0
)


# --------------------------------------------------
# KPI cards
# --------------------------------------------------

st.subheader("Overview")

col1, col2, col3, col4, col5 = st.columns(5)


col1.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}",
)


col2.metric(
    "Total Orders",
    f"{total_orders:,}",
)


col3.metric(
    "Average Order Value",
    f"${average_order_value:,.2f}",
)


col4.metric(
    "Items Sold",
    f"{total_items_sold:,}",
)


col5.metric(
    "Payment Success Rate",
    f"{payment_success_rate:.1f}%",
)


# --------------------------------------------------
# Revenue line chart
# --------------------------------------------------

st.subheader("Trends")


revenue_by_date = (
    filtered_data
    .dropna(subset=["order_date"])
    .groupby(
        filtered_data["order_date"].dt.date,
        as_index=False,
    )["total_price"]
    .sum()
)

revenue_by_date.columns = [
    "order_date",
    "revenue",
]


line_chart = px.line(
    revenue_by_date,
    x="order_date",
    y="revenue",
    title="Revenue Over Time",
    markers=True,
    labels={
        "order_date": "Order Date",
        "revenue": "Revenue",
    },
)


st.plotly_chart(
    line_chart,
    use_container_width=True,
)


# --------------------------------------------------
# Revenue by category bar chart
# --------------------------------------------------

sales_by_category = (
    filtered_data
    .dropna(subset=["category"])
    .groupby(
        "category",
        as_index=False,
    )["total_price"]
    .sum()
    .sort_values(
        "total_price",
        ascending=False,
    )
)


bar_chart = px.bar(
    sales_by_category,
    x="category",
    y="total_price",
    title="Revenue by Category",
    labels={
        "category": "Category",
        "total_price": "Revenue",
    },
)


st.plotly_chart(
    bar_chart,
    use_container_width=True,
)


# --------------------------------------------------
# Scatter plot
# --------------------------------------------------

st.subheader("Insights")


scatter_chart = px.scatter(
    filtered_data,
    x="quantity",
    y="total_price",
    size="total_price",
    hover_data=[
        "product_name",
        "category",
        "city",
        "order_id",
    ],
    title="Quantity vs Total Price",
    labels={
        "quantity": "Quantity Purchased",
        "total_price": "Total Price",
    },
)


st.plotly_chart(
    scatter_chart,
    use_container_width=True,
)
