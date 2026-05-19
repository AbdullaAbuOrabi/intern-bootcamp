from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# This forces MongoDB to actually test the connection
client.admin.command("ping")

db = client["intern_db"]

print("MongoDB connected successfully!")
print("Database name:", db.name)

client.close()
