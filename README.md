## Credit Card Defaulter Prediction

## Problem Statement

Credit card default is a common problem for financial institutions. When customers do not pay their credit card bills on time, it can cause financial loss.

The aim of this project is to predict whether a customer is likely to default on their credit card payment using their personal, credit, repayment, bill, and payment information.

This is a binary classification problem where the model predicts whether a customer will default or not.

## Objective

The main objective of this project is to build a machine learning model that can predict credit card default.

The specific objectives are:

* To understand and analyze the customer data.
* To clean and prepare the dataset.
* To handle categorical and numerical data.
* To divide the data into training and testing sets.
* To build a Random Forest classification model.
* To predict whether a customer will default.
* To evaluate the performance of the model.
* To save the trained model for future use.

## Project Scope

This project focuses on predicting credit card default using machine learning.

The project includes:

* Data collection and data analysis.
* Data cleaning and preprocessing.
* Feature encoding and scaling.
* Model training.
* Model prediction.
* Model evaluation.
* Saving the trained model.

## Proposed Solution

The proposed solution uses customer credit card data to train a machine learning model.

First, the data is cleaned and prepared. Categorical values are converted into numerical values using `OrdinalEncoder`, and numerical features are scaled using `StandardScaler`.

After preprocessing, the data is used to train a `Random Forest Classifier`. The trained model is then used to predict whether a customer is likely to default.

## Methodology

The project follows these steps:

1. Load the dataset.
2. Explore and understand the data.
3. Clean the data and handle incorrect values.
4. Remove unnecessary columns such as customer ID.
5. Separate the input features and target variable.
6. Split the data into training and testing sets.
7. Encode categorical features.
8. Scale the numerical features.
9. Train the Random Forest Classifier.
10. Make predictions on the test data.
11. Evaluate the model.
12. Save the trained model and scaler.

## Machine Learning Model

The project uses the **Random Forest Classifier**.

Random Forest uses multiple decision trees to make predictions. It is useful for classification problems and can work with different types of customer information.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Jupyter Notebook

## Expected Outcome

The expected outcome of this project is a machine learning model that can predict whether a credit card customer is likely to default based on their available information.

The saved model can also be used later to make predictions on new customer data.

## Conclusion

This project shows how machine learning can be used to predict credit card default.

The project includes important steps such as data cleaning, preprocessing, feature transformation, model training, prediction, and evaluation. A Random Forest Classifier is used to make the predictions.

The trained model and preprocessing components are saved using Joblib so that they can be used for future predictions and further development.
