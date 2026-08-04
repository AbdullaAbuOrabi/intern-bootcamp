from pathlib import Path
import subprocess
import sys

import altair as alt
import pandas as pd
import psycopg2
import streamlit as st


st.set_page_config(
    page_title="Customer Insights Assistant",
    page_icon="📊",
    layout="wide",
)


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "processed"
SUMMARY_PATH = BASE_DIR / "analytics" / "weekly_summary.md"


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

    return customers, orders, order_items, products, transactions


@st.cache_data
def load_predictions():
    connection = psycopg2.connect(
        dbname="intern_db",
        user="postgres",
        password="Abdulla11-11",
        host="localhost",
        port="5432",
    )

    query = """
        SELECT
            customer_id,
            prediction,
            probability,
            prediction_timestamp
        FROM customer_predictions
        ORDER BY probability DESC;
    """

    try:
        predictions = pd.read_sql(query, connection)
    finally:
        connection.close()

    return predictions


customers, orders, order_items, products, transactions = load_data()
predictions = load_predictions()


st.title("Customer Insights and Sales Analytics Assistant")

st.write(
    "This dashboard combines sales analytics, customer insights, "
    "machine-learning predictions, and AI-generated summaries."
)


# -------------------------------------------------
# Pipeline control
# -------------------------------------------------

st.subheader("Pipeline Control")

pipeline_script = BASE_DIR / "run_endtoend_pipeline.py"


if st.button("Run Full Pipeline"):
    if not pipeline_script.exists():
        st.error(
            f"Pipeline file was not found: {pipeline_script}"
        )
    else:
        with st.spinner(
            "Running pipeline, predictions, and data refresh..."
        ):
            result = subprocess.run(
                [
                    sys.executable,
                    str(pipeline_script),
                ],
                cwd=BASE_DIR.parent,
                capture_output=True,
                text=True,
            )

        if result.returncode == 0:
            st.cache_data.clear()

            st.success(
                "Pipeline completed successfully. "
                "The dashboard will now reload the latest data."
            )

            if result.stdout.strip():
                with st.expander("View pipeline output"):
                    st.code(result.stdout)

        else:
            st.error("Pipeline execution failed.")

            if result.stdout.strip():
                with st.expander("View pipeline output"):
                    st.code(result.stdout)

            if result.stderr.strip():
                with st.expander("View pipeline errors"):
                    st.code(result.stderr)

st.divider()


# -------------------------------------------------
# Dataset overview
# -------------------------------------------------

st.subheader("Dataset Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Customers",
    f"{len(customers):,}",
)

col2.metric(
    "Orders",
    f"{len(orders):,}",
)

col3.metric(
    "Order Items",
    f"{len(order_items):,}",
)

col4.metric(
    "Products",
    f"{len(products):,}",
)

col5.metric(
    "Transactions",
    f"{len(transactions):,}",
)

st.divider()


# -------------------------------------------------
# Sales performance
# -------------------------------------------------

st.subheader("Sales Performance")

completed_orders = orders[
    orders["status"].str.lower() == "completed"
]

paid_transactions = transactions[
    transactions["payment_status"].str.lower() == "paid"
]

successful_sales = completed_orders.merge(
    paid_transactions,
    on="order_id",
    how="inner",
)

total_revenue = successful_sales["amount"].sum()

successful_orders = successful_sales[
    "order_id"
].nunique()

average_order_value = (
    total_revenue / successful_orders
    if successful_orders > 0
    else 0
)

successful_customer_orders = (
    successful_sales[["order_id"]]
    .merge(
        orders[["order_id", "customer_id"]],
        on="order_id",
        how="left",
    )
)

returning_customers = (
    successful_customer_orders
    .groupby("customer_id")["order_id"]
    .nunique()
    .gt(1)
    .sum()
)

total_customers = customers[
    "customer_id"
].nunique()

returning_customer_rate = (
    returning_customers / total_customers * 100
    if total_customers > 0
    else 0
)

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}",
)

kpi2.metric(
    "Successful Orders",
    f"{successful_orders:,}",
)

kpi3.metric(
    "Average Order Value",
    f"${average_order_value:,.2f}",
)

kpi4.metric(
    "Returning Customer Rate",
    f"{returning_customer_rate:.1f}%",
)

st.divider()


# -------------------------------------------------
# Revenue by category
# -------------------------------------------------

st.subheader("Revenue by Product Category")

category_revenue = (
    order_items
    .merge(
        products[["product_id", "category"]],
        on="product_id",
        how="left",
    )
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

st.bar_chart(
    category_revenue,
    x="category",
    y="total_price",
)


# -------------------------------------------------
# Revenue trend
# -------------------------------------------------

st.subheader("Revenue Trend Over Time")

revenue_trend = successful_sales.copy()

revenue_trend["transaction_date"] = pd.to_datetime(
    revenue_trend["transaction_date"]
)

revenue_trend = (
    revenue_trend
    .groupby(
        "transaction_date",
        as_index=False,
    )["amount"]
    .sum()
    .sort_values("transaction_date")
)

st.line_chart(
    revenue_trend,
    x="transaction_date",
    y="amount",
)


# -------------------------------------------------
# Payment status distribution
# -------------------------------------------------

st.subheader("Payment Status Distribution")

payment_status_counts = (
    transactions["payment_status"]
    .value_counts()
    .rename_axis("payment_status")
    .reset_index(name="count")
)

payment_chart = (
    alt.Chart(payment_status_counts)
    .mark_bar()
    .encode(
        x=alt.X(
            "payment_status:N",
            title="Payment Status",
            sort="-y",
        ),
        y=alt.Y(
            "count:Q",
            title="Number of Transactions",
            scale=alt.Scale(domainMin=0),
        ),
        tooltip=[
            alt.Tooltip(
                "payment_status:N",
                title="Status",
            ),
            alt.Tooltip(
                "count:Q",
                title="Transactions",
            ),
        ],
    )
)

st.altair_chart(
    payment_chart,
    use_container_width=True,
)

st.divider()


# -------------------------------------------------
# Customer reorder predictions
# -------------------------------------------------

st.subheader("Customer Reorder Predictions")

predicted_reorders = (
    predictions["prediction"] == 1
).sum()

predicted_non_reorders = (
    predictions["prediction"] == 0
).sum()

average_probability = (
    predictions["probability"].mean() * 100
    if not predictions.empty
    else 0
)

prediction_col1, prediction_col2, prediction_col3 = st.columns(3)

prediction_col1.metric(
    "Likely to Reorder",
    f"{predicted_reorders:,}",
)

prediction_col2.metric(
    "Unlikely to Reorder",
    f"{predicted_non_reorders:,}",
)

prediction_col3.metric(
    "Average Reorder Probability",
    f"{average_probability:.1f}%",
)

prediction_display = predictions.copy()

prediction_display["prediction_label"] = (
    prediction_display["prediction"]
    .map(
        {
            1: "Likely to Reorder",
            0: "Unlikely to Reorder",
        }
    )
)

prediction_display["probability"] = (
    prediction_display["probability"] * 100
)

prediction_display = prediction_display[
    [
        "customer_id",
        "prediction_label",
        "probability",
        "prediction_timestamp",
    ]
].rename(
    columns={
        "customer_id": "Customer ID",
        "prediction_label": "Prediction",
        "probability": "Probability (%)",
        "prediction_timestamp": "Prediction Time",
    }
)

prediction_filter = st.selectbox(
    "Filter customers by prediction",
    [
        "All Customers",
        "Likely to Reorder",
        "Unlikely to Reorder",
    ],
)

if prediction_filter != "All Customers":
    prediction_display = prediction_display[
        prediction_display["Prediction"]
        == prediction_filter
    ]

st.dataframe(
    prediction_display,
    use_container_width=True,
    hide_index=True,
)

st.divider()


# -------------------------------------------------
# AI-generated summary
# -------------------------------------------------

st.subheader("AI-Generated Weekly Summary")

st.caption(
    "This summary was generated by Gemini using the Day 3 "
    "analytics results."
)

if SUMMARY_PATH.exists():
    weekly_summary = SUMMARY_PATH.read_text(
        encoding="utf-8"
    )

    st.markdown(weekly_summary)

    st.download_button(
        label="Download Weekly Summary",
        data=weekly_summary,
        file_name="weekly_summary.md",
        mime="text/markdown",
    )
else:
    st.warning(
        "The weekly summary file could not be found."
    )
