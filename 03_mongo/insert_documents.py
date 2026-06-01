from datetime import datetime

from pymongo import MongoClient


def get_database():
    """
    Connect to MongoDB running on the local machine.
    Then return the intern_db database.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["intern_db"]
    return db


def insert_customers(db):
    """
    Insert sample customer documents into the customers collection.
    """

    customers = [
        {
            "customer_id": 1,
            "name": "Ahmed Ali",
            "email": "ahmed@example.com",
            "city": "Abu Dhabi",
            "signup_date": "2025-01-10"
        },
        {
            "customer_id": 2,
            "name": "Sara Khan",
            "email": "sara@example.com",
            "city": "Dubai",
            "signup_date": "2025-02-15"
        },
        {
            "customer_id": 3,
            "name": "Omar Hassan",
            "email": "omar@example.com",
            "city": "Sharjah",
            "signup_date": "2025-03-20"
        }
    ]

    db.customers.delete_many({})
    db.customers.insert_many(customers)

    print("Customers inserted successfully.")


def insert_products(db):
    """
    Insert sample product documents into the products collection.
    """

    products = [
        {
            "product_id": 1,
            "product_name": "Laptop",
            "category": "Electronics",
            "price": 3200
        },
        {
            "product_id": 2,
            "product_name": "Headphones",
            "category": "Electronics",
            "price": 350
        },
        {
            "product_id": 3,
            "product_name": "Office Chair",
            "category": "Furniture",
            "price": 700
        }
    ]

    db.products.delete_many({})
    db.products.insert_many(products)

    print("Products inserted successfully.")


def insert_events(db):
    """
    Insert sample event documents into the events collection.
    Events represent customer activity.
    """

    events = [
        {
            "event_id": 1,
            "customer_id": 1,
            "event_type": "view_product",
            "product_id": 1,
            "timestamp": datetime.now()
        },
        {
            "event_id": 2,
            "customer_id": 2,
            "event_type": "add_to_cart",
            "product_id": 2,
            "timestamp": datetime.now()
        },
        {
            "event_id": 3,
            "customer_id": 1,
            "event_type": "purchase",
            "product_id": 1,
            "timestamp": datetime.now()
        }
    ]

    db.events.delete_many({})
    db.events.insert_many(events)

    print("Events inserted successfully.")


def main():
    db = get_database()

    insert_customers(db)
    insert_products(db)
    insert_events(db)

    print("All documents inserted successfully.")


if __name__ == "__main__":
    main()
