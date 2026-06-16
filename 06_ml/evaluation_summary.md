# Model Evaluation Summary

## Task Overview

In this task, I evaluated the best machine learning model on unseen test data. The goal was to understand how well the model performs, where it makes mistakes, and which features are most important for prediction.

The model evaluated in this task was the saved best model from the larger dataset experiment:

- Model file: `best_model_large.pkl`
- Model type: Decision Tree Classifier
- Dataset used: `features_large.csv`
- Target column: `will_reorder`

## Evaluation Process

The dataset was split into features and target:

- `X`: customer behavior and city features
- `y`: whether the customer will reorder

The data was then split into training and test sets using an 80/20 split. The model was evaluated on the test set to simulate unseen data.

## Evaluation Metrics

The model achieved the following results on the test set:

- Accuracy: 1.00
- Precision: 1.00
- Recall: 1.00
- F1-score: 1.00
- ROC AUC: 1.00

These results show that the model correctly predicted all test examples in this experiment.

## Confusion Matrix Findings

The confusion matrix showed:

- 319 customers who will not reorder were predicted correctly.
- 681 customers who will reorder were predicted correctly.
- 0 false positives.
- 0 false negatives.

This means the model made no mistakes on the test set.

## ROC and Precision-Recall Curve Findings

The ROC curve showed a ROC AUC score of 1.00, meaning the model separated the two classes perfectly.

The Precision-Recall curve also showed very strong performance. The model had high precision and high recall when predicting customers who will reorder.

## Feature Importance Findings

The most important features were:

1. `num__total_orders`
2. `num__successful_payments`
3. `num__total_spent`

This means the model mainly used customer order activity, payment activity, and spending behavior to predict whether a customer will reorder.

The city features had zero importance, which means customer location did not strongly affect the prediction in this dataset.

## Interpretation

The model performed perfectly on the test data. This suggests that the features are highly predictive of the target.

However, perfect results should be reviewed carefully. A 100% score may mean the model learned a clear pattern, but it may also suggest possible data leakage or an overly simple target rule.

In a real project, the model should be tested on newer data or data from a different time period to confirm that it performs well outside this experiment.

## Possible Improvements

Possible improvements include:

- Testing the model on completely new future data.
- Checking how the target column `will_reorder` was created.
- Making sure no feature directly reveals the target.
- Comparing the Decision Tree with simpler and more complex models.
- Using cross-validation again to confirm stable performance.
- Adding more customer behavior features if available.

## Saved Figures

The following plots were saved in `reports/figures/`:

- `confusion_matrix.png`
- `roc_curve.png`
- `precision_recall_curve.png`
- `feature_importance.png`