from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(
    page_title="Mini Analytics Project",
    page_icon="📊",
    layout="wide"
)

st.title("Customer Purchase Behavior and Sales Performance")

st.markdown(
    """
    This dashboard presents the main findings from the mini analytics project.
    It focuses on confirmed revenue, product performance, customer behavior,
    payment outcomes, and business recommendations.
    """
)
data_path = Path(__file__).resolve().parent.parent / "data" / "processed"

customers = pd.read_parquet(data_path / "customers_clean.parquet")
orders = pd.read_parquet(data_path / "orders_clean.parquet")
order_items = pd.read_parquet(data_path / "order_items_clean.parquet")
products = pd.read_parquet(data_path / "products_clean.parquet")
transactions = pd.read_parquet(data_path / "transactions_clean.parquet")

analytics_data = (
    order_items
    .merge(orders, on="order_id", how="left")
    .merge(customers, on="customer_id", how="left")
    .merge(products, on="product_id", how="left")
    .merge(transactions, on="order_id", how="left")
)
completed_order_ids = set(
    orders.loc[orders["status"] == "completed", "order_id"]
)

paid_order_ids = set(
    transactions.loc[transactions["payment_status"] == "paid", "order_id"]
)

fully_successful_order_ids = completed_order_ids.intersection(paid_order_ids)

successful_sales = analytics_data[
    analytics_data["order_id"].isin(fully_successful_order_ids)
].copy()
confirmed_revenue = successful_sales["total_price"].sum()
successful_orders = len(fully_successful_order_ids)
successful_order_rate = successful_orders / orders["order_id"].nunique() * 100
average_order_value = confirmed_revenue / successful_orders
total_items_sold = successful_sales["quantity"].sum()

successful_customer_orders = orders[
    orders["order_id"].isin(fully_successful_order_ids)
]

orders_per_customer = (
    successful_customer_orders
    .groupby("customer_id")["order_id"]
    .nunique()
)

successful_customers = orders_per_customer.shape[0]
returning_customers = (orders_per_customer > 1).sum()

returning_customer_rate = (
    returning_customers / successful_customers
) * 100

payment_success_rate = (
    (transactions["payment_status"] == "paid").sum()
    / transactions["transaction_id"].nunique()
) * 100
st.header("Executive KPI Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Confirmed Revenue",
    value=f"{confirmed_revenue:,.2f}"
)

col2.metric(
    label="Successful Orders",
    value=f"{successful_orders}"
)

col3.metric(
    label="Average Order Value",
    value=f"{average_order_value:,.2f}"
)

col4.metric(
    label="Total Items Sold",
    value=f"{total_items_sold}"
)

col5, col6, col7 = st.columns(3)

col5.metric(
    label="Successful Order Rate",
    value=f"{successful_order_rate:.2f}%"
)

col6.metric(
    label="Returning Customer Rate",
    value=f"{returning_customer_rate:.2f}%"
)

col7.metric(
    label="Payment Success Rate",
    value=f"{payment_success_rate:.2f}%"
)
st.header("Daily Confirmed Revenue")

successful_sales["order_day"] = successful_sales["order_date"].dt.date

daily_revenue = (
    successful_sales
    .groupby("order_day", as_index=False)["total_price"]
    .sum()
    .sort_values("order_day")
)

daily_revenue_fig = px.line(
    daily_revenue,
    x="order_day",
    y="total_price",
    markers=True,
    title="Daily Confirmed Revenue Trend"
)

daily_revenue_fig.update_layout(
    xaxis_title="Order Date",
    yaxis_title="Confirmed Revenue"
)

st.plotly_chart(daily_revenue_fig, use_container_width=True)
highest_revenue_day = daily_revenue.loc[daily_revenue["total_price"].idxmax()]
lowest_revenue_day = daily_revenue.loc[daily_revenue["total_price"].idxmin()]

st.subheader("What does this mean?")

st.markdown(
    f"""
    Daily confirmed revenue changes significantly across the analysis period.

    The highest revenue was **{highest_revenue_day['total_price']:,.2f}**
    on **{highest_revenue_day['order_day']}**, while the lowest was
    **{lowest_revenue_day['total_price']:,.2f}**
    on **{lowest_revenue_day['order_day']}**.

    This means revenue is concentrated on certain days rather than remaining
    consistent. The business should investigate the products, customers, or
    activities behind the strongest days and test similar strategies on weaker days.
    """
)
st.header("Confirmed Revenue by Product Category")

category_revenue = (
    successful_sales
    .groupby("category", as_index=False)["total_price"]
    .sum()
    .sort_values("total_price", ascending=False)
)

category_revenue_fig = px.bar(
    category_revenue,
    x="category",
    y="total_price",
    text_auto=".2s",
    title="Confirmed Revenue by Product Category"
)

category_revenue_fig.update_layout(
    xaxis_title="Product Category",
    yaxis_title="Confirmed Revenue"
)

st.plotly_chart(category_revenue_fig, use_container_width=True)
top_category = category_revenue.iloc[0]
lowest_category = category_revenue.iloc[-1]

st.subheader("What does this mean?")

st.markdown(
    f"""
    The **{top_category['category']}** category generated the highest confirmed
    revenue at **{top_category['total_price']:,.2f}**.

    The **{lowest_category['category']}** category generated the lowest confirmed
    revenue at **{lowest_category['total_price']:,.2f}**.

    This shows which product categories currently contribute most to successful
    sales. The business should maintain product availability in the strongest
    category and investigate promotions, bundles, or product positioning for
    weaker categories.
    """
)
st.header("Top Products by Confirmed Revenue")

product_revenue = (
    successful_sales
    .groupby("product_name", as_index=False)["total_price"]
    .sum()
    .sort_values("total_price", ascending=False)
    .head(10)
)

product_revenue_fig = px.bar(
    product_revenue.sort_values("total_price"),
    x="total_price",
    y="product_name",
    orientation="h",
    text_auto=".2s",
    title="Top 10 Products by Confirmed Revenue"
)

product_revenue_fig.update_layout(
    xaxis_title="Confirmed Revenue",
    yaxis_title="Product"
)

st.plotly_chart(product_revenue_fig, use_container_width=True)
top_product = product_revenue.iloc[0]

st.subheader("What does this mean?")

st.markdown(
    f"""
    **{top_product['product_name']}** generated the highest confirmed revenue
    at **{top_product['total_price']:,.2f}**.

    The chart shows that a small group of products contributes a large share of
    confirmed revenue. These products are important sales drivers.

    The business should maintain enough stock for the strongest products and
    investigate why customers prefer them. These products could also be used
    in promotions, recommendations, or bundles with related products.
    """
)
st.header("Confirmed Revenue by Customer City")

city_revenue = (
    successful_sales
    .groupby("city", as_index=False)["total_price"]
    .sum()
    .sort_values("total_price", ascending=False)
)

city_revenue_fig = px.bar(
    city_revenue,
    x="city",
    y="total_price",
    text_auto=".2s",
    title="Confirmed Revenue by Customer City"
)

city_revenue_fig.update_layout(
    xaxis_title="Customer City",
    yaxis_title="Confirmed Revenue"
)

st.plotly_chart(city_revenue_fig, use_container_width=True)
top_city = city_revenue.iloc[0]
lowest_city = city_revenue.iloc[-1]

st.subheader("What does this mean?")

st.markdown(
    f"""
    **{top_city['city']}** generated the highest confirmed revenue at
    **{top_city['total_price']:,.2f}**.

    **{lowest_city['city']}** generated the lowest confirmed revenue at
    **{lowest_city['total_price']:,.2f}**.

    This shows where the strongest customer markets are located. The business
    could focus marketing and customer-retention efforts in the highest-performing
    cities while investigating whether lower revenue in other cities is caused by
    fewer customers, lower order values, or weaker product demand.
    """
)
st.header("Payment Outcomes")

payment_distribution = (
    transactions["payment_status"]
    .value_counts()
    .rename_axis("payment_status")
    .reset_index(name="transaction_count")
)

payment_fig = px.bar(
    payment_distribution,
    x="payment_status",
    y="transaction_count",
    text="transaction_count",
    title="Transaction Count by Payment Status"
)

payment_fig.update_layout(
    xaxis_title="Payment Status",
    yaxis_title="Number of Transactions"
)

st.plotly_chart(payment_fig, use_container_width=True)
paid_transactions = payment_distribution.loc[
    payment_distribution["payment_status"] == "paid",
    "transaction_count"
].iloc[0]

failed_transactions = payment_distribution.loc[
    payment_distribution["payment_status"] == "failed",
    "transaction_count"
].iloc[0]

refunded_transactions = payment_distribution.loc[
    payment_distribution["payment_status"] == "refunded",
    "transaction_count"
].iloc[0]

st.subheader("What does this mean?")

st.markdown(
    f"""
    Only **{paid_transactions} transactions were paid successfully**, while
    **{failed_transactions} failed** and **{refunded_transactions} were refunded**.

    This means most transactions did not result in successful payment. The payment
    success rate is only **{payment_success_rate:.2f}%**, which may be limiting
    confirmed revenue.

    The business should investigate payment failures, checkout issues, refund
    reasons, customer cancellations, and payment-method reliability.
    """
)
st.header("Customer Retention")

customer_retention = pd.DataFrame({
    "customer_type": ["One-time customers", "Returning customers"],
    "customer_count": [
        successful_customers - returning_customers,
        returning_customers
    ]
})

retention_fig = px.bar(
    customer_retention,
    x="customer_type",
    y="customer_count",
    text="customer_count",
    title="Successful Customers by Customer Type"
)

retention_fig.update_layout(
    xaxis_title="Customer Type",
    yaxis_title="Number of Customers"
)

st.plotly_chart(retention_fig, use_container_width=True)
st.subheader("What does this mean?")

st.markdown(
    f"""
    Out of **{successful_customers} successful customers**,
    **{successful_customers - returning_customers} purchased only once**
    and only **{returning_customers} returned to purchase again**.

    The returning-customer rate is **{returning_customer_rate:.2f}%**,
    which shows that the business currently depends mostly on one-time customers.

    The business should consider loyalty rewards, follow-up offers,
    personalized recommendations, and promotions for previous customers
    to increase repeat purchases and long-term customer value.
    """
)
st.header("Business Recommendations")

st.markdown(
    """
    Based on the analysis, the business should:

    1. Investigate failed and refunded transactions to improve the payment success rate.
    2. Introduce loyalty programs and follow-up offers to increase repeat purchases.
    3. Maintain strong availability for the highest-performing products and categories.
    4. Focus marketing efforts on the strongest customer cities.
    5. Review the highest-revenue days to understand what caused the increase.
    """
)
st.header("Conclusion")

st.markdown(
    f"""
    The business generated **{confirmed_revenue:,.2f}** in confirmed revenue
    from **{successful_orders} completed and paid orders**.

    The strongest opportunities come from the highest-performing products,
    categories, and customer cities. However, the low successful-order rate,
    low payment-success rate, and low returning-customer rate show that payment
    performance and customer retention need improvement.

    Improving these areas could help the business achieve more stable and
    sustainable revenue.
    """
)
