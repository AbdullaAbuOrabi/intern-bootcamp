import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


RAW_DATA_PATH = "data/raw"
os.makedirs(RAW_DATA_PATH, exist_ok=True)


# -----------------------------
# Customers
# -----------------------------
num_customers = 100

customers = pd.DataFrame({
    "customer_id": range(1, num_customers + 1),
    "first_name": [f"Customer{i}" for i in range(1, num_customers + 1)],
    "email": [f"customer{i}@example.com" for i in range(1, num_customers + 1)],
    "city": np.random.choice(
        ["Abu Dhabi", "Dubai", "Sharjah", "Ajman"],
        num_customers
    ),
    "signup_date": [
        datetime.today() - timedelta(days=random.randint(1, 365))
        for _ in range(num_customers)
    ]
})


# -----------------------------
# Products
# -----------------------------
num_products = 30

products = pd.DataFrame({
    "product_id": range(1, num_products + 1),
    "product_name": [f"Product{i}" for i in range(1, num_products + 1)],
    "category": np.random.choice(
        ["Electronics", "Clothing", "Books", "Home"],
        num_products
    ),
    "price": np.round(np.random.uniform(20, 1000, num_products), 2)
})


# -----------------------------
# Orders
# -----------------------------
num_orders = 200

orders = pd.DataFrame({
    "order_id": range(1, num_orders + 1),
    "customer_id": np.random.choice(customers["customer_id"], num_orders),
    "order_date": [
        datetime.today() - timedelta(days=random.randint(1, 180))
        for _ in range(num_orders)
    ],
    "status": np.random.choice(
        ["completed", "pending", "cancelled"],
        num_orders
    )
})


# -----------------------------
# Order Items
# -----------------------------
order_items_list = []
order_item_id = 1

for order_id in orders["order_id"]:
    number_of_items = random.randint(1, 4)

    for _ in range(number_of_items):
        product = products.sample(1).iloc[0]
        quantity = random.randint(1, 5)

        order_items_list.append({
            "order_item_id": order_item_id,
            "order_id": order_id,
            "product_id": product["product_id"],
            "quantity": quantity,
            "unit_price": product["price"],
            "total_price": round(quantity * product["price"], 2)
        })

        order_item_id += 1

order_items = pd.DataFrame(order_items_list)


# -----------------------------
# Transactions
# -----------------------------
transactions = pd.DataFrame({
    "transaction_id": range(1, num_orders + 1),
    "order_id": orders["order_id"],
    "payment_method": np.random.choice(
        ["card", "cash", "apple_pay", "bank_transfer"],
        num_orders
    ),
    "payment_status": np.random.choice(
        ["paid", "failed", "refunded"],
        num_orders
    ),
    "transaction_date": orders["order_date"],
    "amount": [
        round(order_items[order_items["order_id"]
              == order_id]["total_price"].sum(), 2)
        for order_id in orders["order_id"]
    ]
})


# -----------------------------
# Save CSV files
# -----------------------------
customers.to_csv(f"{RAW_DATA_PATH}/customers.csv", index=False)
products.to_csv(f"{RAW_DATA_PATH}/products.csv", index=False)
orders.to_csv(f"{RAW_DATA_PATH}/orders.csv", index=False)
order_items.to_csv(f"{RAW_DATA_PATH}/order_items.csv", index=False)
transactions.to_csv(f"{RAW_DATA_PATH}/transactions.csv", index=False)


print("Synthetic dataset generated successfully!")
print("Files saved inside data/raw/")
print("Created files:")
print("- customers.csv")
print("- products.csv")
print("- orders.csv")
print("- order_items.csv")
print("- transactions.csv")
