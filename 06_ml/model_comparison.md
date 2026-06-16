# Model Comparison Summary

## Task Title

Week 3 Task 3 — Model Training and Hyperparameter Tuning

## Task Goal

The goal of this task was to train and compare multiple supervised machine learning models using the processed customer feature dataset. The models were trained to predict whether a customer will reorder based on customer behavior features such as total orders, total spending, average order amount, successful payments, and city information.

## Dataset Used

The main dataset used in this task was:

data/processed/features.csv

This dataset was created in the previous preprocessing task. The target column was:

will_reorder

The feature columns included:

- num__total_orders
- num__total_spent
- num__average_order_amount
- num__successful_payments
- cat__city_Abu Dhabi
- cat__city_Ajman
- cat__city_Dubai
- cat__city_Sharjah

## Models Trained

Three supervised classification models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest

The data was split into training and testing sets. The model learned from the training data and was evaluated using the testing data.

## Baseline Model Results

All three baseline models achieved high accuracy on the small processed dataset. Logistic Regression, Decision Tree, and Random Forest all reached strong test accuracy. Cross-validation was also used to test the models on multiple data splits instead of depending on only one train/test split.

The cross-validation results showed that Logistic Regression and Decision Tree performed the best, while Random Forest was slightly lower on the small dataset.

## Hyperparameter Tuning

GridSearchCV was used to tune the Decision Tree model. The purpose of GridSearchCV was to test different model settings and choose the best combination.

The best parameters for the original dataset were:

- max_depth: 2
- min_samples_leaf: 1
- min_samples_split: 2

The tuned Decision Tree achieved strong performance and was selected as the final model for the main task.

## Saved Model

The best model was saved using joblib.dump() as:

06_ml/best_model.pkl

This allows the trained model to be reused later without training it again.

## Extra Large Data Experiment

As extra work, a larger synthetic dataset was created to test the models on more data. The larger dataset was saved as:

data/processed/features_large.csv

This dataset contained 5,000 rows. The same three models were trained again:

- Logistic Regression
- Decision Tree
- Random Forest

On the larger dataset, Logistic Regression achieved lower accuracy, while Decision Tree and Random Forest both achieved perfect accuracy. Decision Tree was selected as the better practical model because it achieved the same accuracy as Random Forest but was faster and easier to explain.

The best parameters for the large-data Decision Tree were:

- max_depth: 3
- min_samples_leaf: 1
- min_samples_split: 2

The large-data model was saved as:

06_ml/best_model_large.pkl

## Final Conclusion

The tuned Decision Tree was selected as the best model because it achieved excellent accuracy, strong cross-validation performance, and simple explainable settings. It also worked well on the larger synthetic dataset, where it matched Random Forest performance while being faster and easier to understand.

This task helped me understand how to train multiple models, compare model performance, use cross-validation, tune hyperparameters with GridSearchCV, and save the final trained model using joblib.
