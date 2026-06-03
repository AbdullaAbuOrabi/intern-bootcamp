# MongoDB Aggregation & Indexing Summary

## Task Objective

The goal of this task was to practice MongoDB aggregation pipelines and indexing. I used aggregation stages such as `$match`, `$lookup`, `$unwind`, `$group`, `$project`, and `$sort` to analyze event and product data.

## What I Completed

- Created `03_mongo/aggregations.json` to store the final aggregation pipeline.
- Created `03_mongo/run_aggregations.py` to run the pipeline from the JSON file.
- Built an aggregation pipeline to calculate estimated sales by product category.
- Used `$match` to filter only purchase events.
- Used `$lookup` to join purchase events with product details.
- Used `$unwind` to open the joined product details array.
- Used `$group` to group purchases by product category.
- Used `$project` to clean and rename output fields.
- Used `$sort` to order categories by estimated sales value.
- Created indexes on fields such as `event_type`, `product_id`, and `customer_id`.
- Created a compound index on `event_type` and `product_id`.
- Created a text index on `product_name` and `category`.
- Used `.explain()` to compare query performance before and after indexes.

## Aggregation Pipeline Explanation

The sales by product category pipeline starts from the `events` collection. It first filters only documents where `event_type` is `purchase`. Then it joins each purchase event with the matching product from the `products` collection using `product_id`.

After the join, `$unwind` is used to open the `product_details` array. Then the pipeline groups the data by product category, counts the number of purchases, and calculates an estimated sales value by summing product prices.

Because the events data does not contain a `quantity` field, I treated each purchase event as one product sold.

## Indexing Explanation

Indexes help MongoDB find documents faster. Without indexes, MongoDB may need to scan many documents one by one. With indexes, MongoDB can search more efficiently.

I created indexes on commonly used fields such as `event_type`, `product_id`, and `customer_id`. These fields are useful because they are used in filtering, joining, and grouping operations.

I also created a compound index on `event_type` and `product_id`, which helps queries that use both fields together.

## Text Search

I created a text index on `product_name` and `category`. This allows MongoDB to search product names and categories using text search.

Example searches included words such as `Electronics`, `Laptop`, and `Chair`.

## Findings

Using `.explain()`, I compared query performance before and after creating indexes. The most important fields to check were:

- `totalDocsExamined`
- `executionTimeMillis`

Because the dataset is small, the performance difference may not be large. However, the task helped me understand that indexes become much more important when collections contain thousands or millions of documents.

## Conclusion

This task helped me understand how MongoDB can be used for more than basic CRUD operations. Aggregation pipelines allow MongoDB to analyze data, join collections, group results, calculate values, and sort output. Indexes help improve query performance and text indexes allow searching inside text fields.