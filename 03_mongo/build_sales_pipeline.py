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
    },
    {
        "$unwind": "$product_details"
    },
    {
        "$group": {
            "_id": "$product_details.category",
            "number_of_purchases": {
                "$sum": 1
            },
            "estimated_sales_value": {
                "$sum": "$product_details.price"
            }
        }
    },
    {
        "$project": {
            "_id": 0,
            "category": "$_id",
            "number_of_purchases": 1,
            "estimated_sales_value": 1
        }
    },
    {
        "$sort": {
            "estimated_sales_value": -1
        }
    }
]

print("Step 6: Final sales by product category")
print("-" * 40)

for result in events.aggregate(pipeline):
    pprint(result)
