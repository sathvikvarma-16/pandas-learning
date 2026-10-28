# PHASE 21: PANDAS FOR MACHINE LEARNING

import pandas as pd
import numpy as np

# Scikit-learn tools for splitting, preprocessing and modeling.
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# --------------------------------------------------
# 1. LOAD THE RAW DATASET
# --------------------------------------------------

# Sample data for practice.
# For a real dataset, use:
# df = pd.read_csv("employees.csv")

df = pd.DataFrame({
    "employee_id": range(101, 117),
    "age": [
        22, 25, 28, 32, 35, 29, 40, 24,
        31, 27, 36, 30, 26, 34, 38, 23
    ],
    "income": [
        25000, 30000, 35000, 50000, 55000, np.nan,
        75000, 28000, 45000, 32000, 65000, 48000,
        31000, 58000, 70000, 26000
    ],
    "experience": [
        0, 2, 4, 8, 10, 5, 15, 1,
        7, 3, 12, 6, 2, 9, 14, 1
    ],
    "department": [
        "IT", "HR", "IT", "Finance", "IT", "HR",
        "Finance", "IT", "Finance", "HR", "IT",
        "Finance", "HR", "IT", "Finance", "IT"
    ],
    "city": [
        "Vizag", "Chennai", "Vizag", "Hyderabad",
        "Chennai", "Vizag", "Hyderabad", "Vizag",
        "Chennai", "Vizag", "Hyderabad", "Chennai",
        "Vizag", "Hyderabad", "Chennai", "Vizag"
    ],
    "salary": [
        30000, 35000, 42000, 60000, 68000, 45000,
        90000, 32000, 58000, 38000, 80000, 55000,
        36000, 72000, 85000, 31000
    ]
})

print(df.head())
print("Shape:", df.shape)


# --------------------------------------------------
# 2. INSPECT THE DATA
# --------------------------------------------------

print(df.info())
print(df.describe())
print("Missing values:")
print(df.isna().sum())

print("Duplicate rows:", df.duplicated().sum())

# Understand categorical columns.
print(df["department"].value_counts())
print(df["city"].value_counts())


# --------------------------------------------------
# 3. CLEAN AND VALIDATE THE DATA
# --------------------------------------------------

# Remove exact duplicate rows only when appropriate.
df = df.drop_duplicates().copy()

# Employee IDs should be unique in this example.
# If IDs are missing or repeated, investigate before proceeding.
if df["employee_id"].isna().any():
    raise ValueError("Missing employee IDs found.")

if df["employee_id"].duplicated().any():
    raise ValueError("Duplicate employee IDs found.")

# Ensure numeric columns use numeric data types.
numeric_columns = [
    "age", "income", "experience", "salary"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Example business rule: retain adults with non-negative experience.
# Choose filters according to the real dataset and task.
df = df[
    (df["age"] > 18) &
    (df["experience"] >= 0)
].copy()

# Do not use df.dropna() automatically.
# Missing values can often be handled by imputers during preprocessing.
print("Shape after validation:", df.shape)


# --------------------------------------------------
# 4. SELECT FEATURES AND TARGET
# --------------------------------------------------

# Features are inputs used to make a prediction.
# Include both numerical and categorical input columns.
X = df[
    [
        "age",
        "income",
        "experience",
        "department",
        "city"
    ]
]


# Target is the value the model should predict.
y = df["salary"]

print("Feature shape:", X.shape)
print("Target shape:", y.shape)

print("Features:")
print(X.head())

print("Target:")
print(y.head())

# Do not include employee_id as a feature here.
# It is an identifier, not a meaningful salary predictor
# for this example.


# --------------------------------------------------
# 5. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES
# --------------------------------------------------

numeric_features = [
    "age",
    "income",
    "experience"
]

categorical_features = [
    "department",
    "city"
]

print("Numerical features:", numeric_features)
print("Categorical features:", categorical_features)


# --------------------------------------------------
# 6. SPLIT INTO TRAINING AND TESTING DATA
# --------------------------------------------------

# Split before fitting imputers, encoders or scalers.
# The test set is held back for final evaluation.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)


# --------------------------------------------------
# 7. PREPROCESS NUMERICAL FEATURES
# --------------------------------------------------

# Missing numerical values are replaced with the median learned from the training data.
# StandardScaler standardizes numerical features.

numeric_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])


# --------------------------------------------------
# 8. PREPROCESS CATEGORICAL FEATURES
# --------------------------------------------------

# Missing categories are replaced using the most
# frequent category learned from the training data.
# OneHotEncoder converts categories into numeric columns.
# handle_unknown="ignore" supports new categories at prediction time.

categorical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])


# --------------------------------------------------
# 9. COMBINE THE PREPROCESSING STEPS
# --------------------------------------------------

preprocessor = ColumnTransformer(transformers=[
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])


# --------------------------------------------------
# 10. CREATE THE COMPLETE ML PIPELINE
# --------------------------------------------------

# The pipeline learns preprocessing from training data,
# transforms the features, and trains the model.
# This keeps the steps together and helps prevent leakage.

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Fit only on the training data.
model.fit(X_train, y_train)


# --------------------------------------------------
# 11. MAKE PREDICTIONS
# --------------------------------------------------

predictions = model.predict(X_test)

results = pd.DataFrame({
    "actual_salary": y_test.to_numpy(),
    "predicted_salary": predictions
})

results["prediction_error"] = (
    results["actual_salary"] -
    results["predicted_salary"]
)

print(results)


# --------------------------------------------------
# 12. EVALUATE THE MODEL
# --------------------------------------------------

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", round(mae, 2))
print("R-squared:", round(r2, 3))

# MAE measures average absolute prediction error in salary units.

# R-squared measures performance relative to predicting
# the test target mean. It can be negative on test data.

# This dataset is tiny and artificial, so these metrics are only for learning the workflow, not judging a real model.


# --------------------------------------------------
# 13. PREDICT FOR A NEW EMPLOYEE
# --------------------------------------------------

new_employee = pd.DataFrame({
    "age": [29],
    "income": [40000],
    "experience": [5],
    "department": ["IT"],
    "city": ["Vizag"]
})

new_salary_prediction = model.predict(new_employee)

print(
    "Predicted salary:",
    round(new_salary_prediction[0], 2)
)

# Use the same trained pipeline for new data.
# Do not refit the scaler or encoder on the new employee.


# --------------------------------------------------
# 14. IMPORTANT MACHINE LEARNING RULES
# --------------------------------------------------

# 1. X contains the input features.
# 2. y contains the target to predict.
# 3. Split before fitting learned preprocessing.
# 4. Fit imputers, encoders and scalers on training data only.
# 5. Use the fitted pipeline to transform test/new data.
# 6. Never include the target in X for ordinary supervised
#    prediction of that same target.
# 7. Select features based on the prediction task and
#    information available at prediction time.
# 8. A high score on a tiny dataset does not prove that a model will generalize to real data.
