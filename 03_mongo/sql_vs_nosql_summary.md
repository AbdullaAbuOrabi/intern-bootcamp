# When to Use SQL vs NoSQL

## Introduction

This document explains the difference between SQL databases such as PostgreSQL and NoSQL databases such as MongoDB.

During Week 1, PostgreSQL was used to store structured ecommerce data in tables. In Week 2, MongoDB was introduced to store flexible document-based data.

## SQL Databases

SQL databases store data in tables with rows and columns.

They are best when the data has a clear structure and strong relationships.

Examples of SQL databases include:

- PostgreSQL
- MySQL
- SQL Server
- Oracle Database

## NoSQL Databases

NoSQL databases store data in a more flexible way.

MongoDB is a NoSQL database that stores data as documents. These documents look similar to JSON objects or Python dictionaries.

A MongoDB document can contain nested data, arrays, and fields that may differ from one document to another.

## SQL vs NoSQL Comparison

| Feature | SQL / PostgreSQL | NoSQL / MongoDB |
|---|---|---|
| Data format | Tables | Documents |
| Record type | Row | Document |
| Structure | Fixed schema | Flexible schema |
| Relationships | Strong, uses joins | Usually embedded or referenced |
| Query language | SQL | MongoDB query syntax |
| Best for | Structured relational data | Flexible or nested data |

## When to Use SQL

Use SQL when:

- The data has many relationships.
- The structure is clear and stable.
- You need joins between tables.
- You need strong validation rules.
- Accuracy and consistency are very important.

Example use cases:

- Banking systems
- Payment systems
- Inventory systems
- Ecommerce orders and transactions
- Student registration systems

## When to Use NoSQL

Use NoSQL when:

- The data structure changes often.
- The data is nested.
- You need to store JSON-like documents.
- You are working with logs, events, or user activity.
- You do not need many joins.

Example use cases:

- Chat messages
- User activity events
- Product catalogs
- App logs
- User profiles
- Content management systems

## Example from This Project

In PostgreSQL, customer data is stored in a table:

| customer_id | name | email | city |
|---|---|---|---|
| 1 | Ahmed Ali | ahmed@example.com | Abu Dhabi |

In MongoDB, the same customer can be stored as a document:

```json
{
  "customer_id": 1,
  "name": "Ahmed Ali",
  "email": "ahmed@example.com",
  "city": "Abu Dhabi"
}

## PostgreSQL to MongoDB Import Comparison

As part of this task, a small dataset from the PostgreSQL customers table was imported into MongoDB.

In PostgreSQL, the data was stored as rows inside a customers table.

In MongoDB, the same data was stored as documents inside a postgres_customers collection.

This helped demonstrate that the same data can be represented in two different formats:

- PostgreSQL: table, rows, and columns
- MongoDB: collection, documents, and fields

This comparison helped me understand the difference between relational storage and document-based storage.