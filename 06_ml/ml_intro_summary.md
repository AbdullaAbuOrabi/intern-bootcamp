# Week 3 Day 1 — Introduction to Machine Learning

## Task Goal

The goal of this task was to understand the basic machine learning workflow by building a simple baseline model.

The model was trained to predict whether a customer will reorder or not.

This is a classification problem because the target value has two possible classes:

- 1 = customer reordered
- 0 = customer did not reorder

## Dataset Used

The task used the existing customer, order, and transaction datasets:

- customers.csv
- orders.csv
- transactions.csv

These datasets were combined to create one machine learning dataset where each row represents one customer.

## Features Created

The following customer-level features were created:

- total_spent
- average_order_amount
- successful_payments

These features were used as the input information for the model.

## Target Variable

The target variable was:

- will_reorder

The target was created using this logic:

- If total_orders > 1, then will_reorder = 1
- If total_orders <= 1, then will_reorder = 0

## Model Used

A Logistic Regression model was used as the baseline model.

Logistic Regression was selected because it is a simple and common model for binary classification problems.

## Train/Test Split

The dataset was split into:

- 80% training data
- 20% testing data

The training data was used to teach the model.

The testing data was used to evaluate the model on customers it had not seen before.

## Evaluation Results

The model achieved the following results:

| Metric | Score |
|---|---:|
| Accuracy | 1.0 |
| F1 Score | 1.0 |

## Interpretation

The model correctly predicted all customers in the test set.

However, the result should be interpreted carefully because the dataset is small and synthetic. Also, the features are strongly related to customer order behavior, so the prediction problem may be easier than a real-world machine learning problem.

## What I Learned

In this task, I learned the basic machine learning workflow:

1. Load the data
2. Explore the data
3. Create features
4. Create a target variable
5. Split the data into training and testing sets
6. Train a baseline model
7. Make predictions
8. Evaluate the model using Accuracy and F1 Score

I also learned that features are the input information used by the model, while the target is the answer the model learns to predict.
