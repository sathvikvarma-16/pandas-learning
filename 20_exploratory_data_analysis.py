# PHASE 20: EXPLORATORY DATA ANALYSIS (EDA)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a consistent plotting theme.
sns.set_theme(style="whitegrid")


# --------------------------------------------------
# 1. LOAD THE DATASET
# --------------------------------------------------

# Sample dataset for practice.
# In a real project, you can use:
# df = pd.read_csv("employees.csv")

df = pd.DataFrame({
    "employee_id": [
        101, 102, 103, 104, 105, 106,
        107, 108, 109, 110, 111, 111
    ],
    "department": [
        "IT", "HR", "IT", "Finance", "HR", "IT",
        "Finance", "IT", "HR", "Finance", "IT", "IT"
    ],
    "age": [
        23, 28, 25, 35, 30, 26,
        42, 24, 31, 38, 29, 29
    ],
    "salary": [
        35000, 42000, 39000, 60000, 45000, np.nan,
        75000, 36000, 48000, 68000, 50000, 50000
    ],
    "experience_years": [
        1, 4, 2, 10, 5, 3,
        15, 2, 6, 12, 5, 5
    ],
    "performance_score": [
        75, 82, 80, 90, 84, 78,
        95, 76, 85, 92, 88, 88
    ],
    "city": [
        "Vizag", "Chennai", "Vizag", "Hyderabad",
        "Chennai", "Vizag", "Hyderabad", "Vizag",
        "Chennai", None, "Vizag", "Vizag"
    ]
})

# Keep an untouched copy for comparison.
df_raw = df.copy()

print("Dataset loaded successfully!")
print(df.head())


# --------------------------------------------------
# 2. UNDERSTAND THE SHAPE
# --------------------------------------------------

# Number of rows and columns.
print("Shape:", df.shape)

# Number of rows.
print("Rows:", df.shape[0])

# Number of columns.
print("Columns:", df.shape[1])

# Total number of cells.
print("Total cells:", df.size)

# Column names.
print("Column names:", df.columns.tolist())

# Index.
print("Index:", df.index)


# --------------------------------------------------
# 3. INSPECT THE RECORDS
# --------------------------------------------------

# First five records.
print(df.head())

# First three records.
print(df.head(3))

# Last five records.
print(df.tail())

# Random sample of records.
print(df.sample(3, random_state=42))


# --------------------------------------------------
# 4. UNDERSTAND COLUMNS AND DATA TYPES
# --------------------------------------------------

# Concise summary of columns, non-null counts and types.
df.info()

# Data type of each column.
print(df.dtypes)

# Numerical columns.
print(df.select_dtypes(include="number").columns.tolist())

# Categorical or text columns.
print(df.select_dtypes(include=["object", "category"]).columns.tolist())

# Convert a numeric-looking column safely if needed.
# Example:
# df["salary"] = pd.to_numeric(df["salary"], errors="coerce")


# --------------------------------------------------
# 5. CHECK MISSING VALUES
# --------------------------------------------------

# Missing values in each column.
print(df.isna().sum())

# Total missing cells.
print("Total missing cells:", df.isna().sum().sum())

# Missing percentage per column.
missing_percentage = df.isna().mean().mul(100)

print("Missing percentage:")
print(missing_percentage.sort_values(ascending=False))

# Rows that contain at least one missing value.
print(df[df.isna().any(axis=1)])

# Investigate missing values before deciding how to handle them.


# --------------------------------------------------
# 6. CHECK DUPLICATES
# --------------------------------------------------

# Number of fully duplicated rows.
print("Duplicate rows:", df.duplicated().sum())

# Display duplicate rows.
print(df[df.duplicated(keep=False)])

# Check repeated employee IDs.
print("Repeated employee IDs:")
print(df[df.duplicated(subset=["employee_id"], keep=False)])

# Remove exact duplicate records only when appropriate.
df = df.drop_duplicates().copy()

print("Shape after exact duplicate removal:", df.shape)

# Check employee ID uniqueness.
print("Unique employee IDs:", df["employee_id"].nunique())
print("Total employee records:", len(df))

# Important:
# A repeated ID may be legitimate in transaction or history data.
# Confirm what one row represents before deleting duplicates.


# --------------------------------------------------
# 7. CHECK UNIQUE VALUES AND FREQUENCIES
# --------------------------------------------------

# Unique departments.
print(df["department"].unique())

# Number of distinct departments, excluding missing values.
print(df["department"].nunique())

# Frequency of each department.
print(df["department"].value_counts())

# Include missing categories in the frequency table.
print(df["city"].value_counts(dropna=False))

# Category percentages.
print(df["department"].value_counts(normalize=True) * 100)


# --------------------------------------------------
# 8. CLEAN THE DATA
# --------------------------------------------------

# Normalize text by removing extra spaces and
# applying consistent capitalization.
df["department"] = df["department"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()

# Make sure numerical columns have numerical types.
numeric_columns = [
    "age",
    "salary",
    "experience_years",
    "performance_score"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Check missing values again after conversions.
print("Missing values after type conversion:")
print(df.isna().sum())

# Fill missing salary using the median.
# This is a demonstration, not a universal rule.
salary_median = df["salary"].median()
df["salary"] = df["salary"].fillna(salary_median)


# Fill missing city using the most frequent city.
# Use this only if the choice is justified for your task.
city_mode = df["city"].mode()

if not city_mode.empty:
    df["city"] = df["city"].fillna(city_mode.iloc[0])

print("Missing values after selected imputation:")
print(df.isna().sum())

# Check values against reasonable example constraints.
# These ranges are illustrative and must match real business rules.
invalid_age = df[~df["age"].between(18, 100)]
invalid_salary = df[df["salary"] < 0]
invalid_experience = df[
    ~df["experience_years"].between(0, 80)
]
invalid_performance = df[
    ~df["performance_score"].between(0, 100)
]

print("Invalid ages:")
print(invalid_age)

print("Negative salaries:")
print(invalid_salary)

print("Invalid experience values:")
print(invalid_experience)

print("Invalid performance scores:")
print(invalid_performance)

# Do not automatically remove every flagged row.
# Investigate the records and apply domain-specific rules.


# --------------------------------------------------
# 9. SUMMARY STATISTICS
# --------------------------------------------------

# Summary of numerical columns.
print(df.describe())

# Summary of categorical columns.
print(df.describe(include="object"))
  
# Mean salary.
pr  nt("Mean salary:", df["salary"].mean())

# Median salary.
print("Median salary:", df["salary"].median())

# Standard deviation of salary.
print("Salary standard deviation:", df["salary"].std())

# Minimum and maximum salary.
print("Minimum salary:", df["salary"].min())
print("Maximum salary:", df["salary"].max())

# Quartiles.
print("Salary quartiles:")
print(df["salary"].quantile([0.25, 0.50, 0.75]))


# --------------------------------------------------
# 10. GROUP ANALYSIS
# --------------------------------------------------

# Number of employees in each department.
print(df.groupby("department").size())

# Average salary by department.
print(df.groupby("department")["salary"].mean())

# Multiple statistics by department.
department_summary = df.groupby("department").agg(
    employee_count=("employee_id", "count"),
    average_salary=("salary", "mean"),
    median_salary=("salary", "median"),
    highest_salary=("salary", "max"),
    average_performance=("performance_score", "mean")
)

print(department_summary.sort_values(
    "average_salary",
    ascending=False
))

# Average salary by city.
print(df.groupby("city")["salary"].mean())

# Compare department and city together.
print(
    df.groupby(["department", "city"], observed=True)
    ["salary"]
    .mean()
)


# --------------------------------------------------
# 11. RELATIONSHIPS BETWEEN NUMERICAL FEATURES
# --------------------------------------------------


numerical_features = [
    "age",
    "salary",
    "experience_years",
    "performance_score"
]

# Correlation matrix.
correlation_matrix = df[numerical_features].corr()
print(correlation_matrix)

# Covariance matrix.
print(df[numerical_features].cov())

# Example: relationship between experience and salary.
print(
    "Experience-salary correlation:",
    df["experience_years"].corr(df["salary"])
)

# Correlation indicates association, not causation.


# --------------------------------------------------
# 12. VISUALIZATION WITH MATPLOTLIB
# --------------------------------------------------

# A. Histogram: distribution of salaries.
plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=6, edgecolor="black")
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

# B. Bar chart: average salary by department.
average_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
plt.bar(
    average_salary.index,
    average_salary.values,
    edgecolor="black"
)
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.show()

# C. Scatter plot: experience vs salary.
plt.figure(figsize=(8, 5))
plt.scatter(
    df["experience_years"],
    df["salary"]
)
plt.title("Experience vs Salary")
plt.xlabel("Experience in Years")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()

# D. Box plot: salary spread.
plt.figure(figsize=(8, 5))
plt.boxplot(df["salary"])
plt.title("Salary Spread and Potential Outliers")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 13. VISUALIZATION WITH SEABORN
# --------------------------------------------------

# A. Histogram with a density curve.
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="salary",
    bins=6,
    kde=True
)
plt.title("Salary Distribution")
plt.tight_layout()
plt.show()

# B. Count plot: number of employees per department.
plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="department"
)
plt.title("Employees by Department")
plt.tight_layout()
plt.show()

# C. Box plot: compare salary distributions.
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="department",
    y="salary"
)
plt.title("Salary Distribution by Department")
plt.tight_layout()
plt.show()

# D. Scatter plot with a fitted trend line.
plt.figure(figsize=(8, 5))
sns.regplot(
    data=df,
    x="experience_years",
    y="salary"
)
plt.title("Experience vs Salary")
plt.tight_layout()
plt.show()

# E. Correlation heatmap.
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)
plt.title("Numerical Feature Correlations")
plt.tight_layout()
plt.show()

# F. Pair plot: compare several numerical variables.
sns.pairplot(
    df[numerical_features],
    diag_kind="hist"
)
plt.show()


# --------------------------------------------------
# 14. WRITE DATA-DRIVEN CONCLUSIONS
# --------------------------------------------------

# Use calculated values instead of guessing.

print("\nEDA CONCLUSIONS")

print("Number of records:", len(df))
print("Number of columns:", df.shape[1])

print(
    "Department with the most records:",
    df["department"].value_counts().idxmax()
)

print(
    "Department with the highest average salary:",
    df.groupby("department")["salary"].mean().idxmax()
)

print(
    "Average salary:",
    round(df["salary"].mean(), 2)
)

print(
    "Median salary:",
    round(df["salary"].median(), 2)
)
 
print(
    "Correlation between experience and salary:",
    round(df["experience_years"].corr(df["salary"]), 3)
)

print("Remaining missing values:")
print(df.isna().sum())

# Final reminder:
# Conclusions describe this sample, not necessarily
# the entire population.
# Record assumptions, limitations and cleaning decisions.
