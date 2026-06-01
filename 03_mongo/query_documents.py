from pymongo import MongoClient


def get_database():
    """
    Connect to MongoDB running on the local machine.
    Then return the intern_db database.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["intern_db"]
    return db


def show_all_customers(db):
    """
    Read and display all documents from the customers collection.
    """

    print("\nAll customers:")

    for customer in db.customers.find():
        print(customer)


def filter_customers_by_city(db):
    """
    Find customers who are from Abu Dhabi.
    """

    print("\nCustomers from Abu Dhabi:")

    for customer in db.customers.find({"city": "Abu Dhabi"}):
        print(customer)


def project_customer_names(db):
    """
    Show only customer names and emails.
    Hide the MongoDB _id field.
    """

    print("\nCustomer names and emails only:")

    for customer in db.customers.find({}, {"_id": 0, "name": 1, "email": 1}):
        print(customer)


def sort_products_by_price(db):
    """
    Show products sorted by price from highest to lowest.
    """

    print("\nProducts sorted by price descending:")

    for product in db.products.find().sort("price", -1):
        print(product)


def find_purchase_events(db):
    """
    Find events where the event type is purchase.
    """

    print("\nPurchase events:")

    for event in db.events.find({"event_type": "purchase"}):
        print(event)


def main():
    db = get_database()

    show_all_customers(db)
    filter_customers_by_city(db)
    project_customer_names(db)
    sort_products_by_price(db)
    find_purchase_events(db)


if __name__ == "__main__":
    main()
