from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["intern_db"]

events = db["events"]
products = db["products"]


print("\n1. $match example: purchase events only")
print("-" * 50)

pipeline_match = [
    {
        "$match": {
            "event_type": "purchase"
        }
    }
]

for result in events.aggregate(pipeline_match):
    pprint(result)


print("\n2. $group example: count events by type")
print("-" * 50)

pipeline_group = [
    {
        "$group": {
            "_id": "$event_type",
            "total_events": {
                "$sum": 1
            }
        }
    }
]

for result in events.aggregate(pipeline_group):
    pprint(result)


print("\n3. $project example: show selected product fields")
print("-" * 50)

pipeline_project = [
    {
        "$project": {
            "_id": 0,
            "product_name": 1,
            "category": 1,
            "price": 1
        }
    }
]

for result in products.aggregate(pipeline_project):
    pprint(result)


print("\n4. $sort example: products by highest price")
print("-" * 50)

pipeline_sort = [
    {
        "$sort": {
            "price": -1
        }
    }
]

for result in products.aggregate(pipeline_sort):
    pprint(result)


print("\n5. $lookup example: connect events with products")
print("-" * 50)

pipeline_lookup = [
    {
        "$lookup": {
            "from": "products",
            "localField": "product_id",
            "foreignField": "product_id",
            "as": "product_details"
        }
    }
]

for result in events.aggregate(pipeline_lookup):
    pprint(result)
