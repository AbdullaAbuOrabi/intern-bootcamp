from pathlib import Path
import json
from pymongo import MongoClient
from pprint import pprint


BASE_DIR = Path(__file__).resolve().parents[1]
AGGREGATIONS_FILE = BASE_DIR / "03_mongo" / "aggregations.json"

client = MongoClient("mongodb://localhost:27017/")
db = client["intern_db"]


with open(AGGREGATIONS_FILE, "r", encoding="utf-8") as file:
    pipelines = json.load(file)


print("Sales by Product Category")
print("-" * 40)

results = db.events.aggregate(pipelines["sales_by_product_category"])

for result in results:
    pprint(result)
