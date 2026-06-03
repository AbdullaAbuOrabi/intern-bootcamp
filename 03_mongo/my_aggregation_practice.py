from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["intern_db"]

events = db["events"]

pipeline = [
    {
        "$match": {
            "event_type": "purchase"
        }
    },
    {
        "$lookup": {
            "from": "products",
            "localField": "product_id",
            "foreignField": "product_id",
            "as": "product_details"
        }
    }
]

print("Step 2: Purchase events with product details")
print("-" * 40)

for result in events.aggregate(pipeline):
    pprint(result)

pipeline_match = [
    {
        "$match": {
            "event_type": "purchase"
        }

    }
]
for result in events.aggregate(pipeline_match):
    pprint(result)

pipeline_project = [
    {
        "$project": {
            "$_id:"0,
            "$product_name:"1,
            "$category:"1,
            "$price:"1
        }

    }
]
for result in products.aggregate(pipeline_project):
    pprint(result)

pipeline_sort = [
    {
        "$sort": {
            "price:" - 1
        }
    }
]
for result in products.aggregate(pipeline_sort):
    pprint(result)

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

    pipeline_group2 = [
        {
            "$group": {
                "_id": "customer_id",
                "total _events": {
                    "$sum": 1
                }
            }
        }
    ]

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
