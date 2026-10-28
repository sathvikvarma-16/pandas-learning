import pandas as pd
import numpy as np


# ============================================================
# PHASE 9: DATA CLEANING & QUALITY
# ============================================================


# ------------------------------------------------------------
# 1. MESSY REAL-WORLD DATA
# ------------------------------------------------------------

df = pd.DataFrame({
    "Name": [" Rahul ", "PRIYA", " arjun", "Sneha "],
    "Age": [20, 21, -5, 200],
    "City": ["vizag", "VIZAG", "Vizag ", "HYDERABAD"],
    "Gender": ["Male", "female", "MALE", "unknown"],
    "Marks": [85, 90, 105, 78]
})

print(df)

# Real-world data can contain:
# - Extra spaces
# - Different capitalization
# - Invalid values
# - Impossible values
# - Inconsistent categories
# - Outliers


# ------------------------------------------------------------
# 2. WHITESPACE
# ------------------------------------------------------------

# Extra spaces can cause matching problems.

df["Name"] = df["Name"].str.strip()
print(df["Name"])

# " Rahul " -> "Rahul"
# " arjun"  -> "arjun"
# "Sneha "  -> "Sneha"


# ------------------------------------------------------------
# 3. LOWERCASE
# ------------------------------------------------------------

df["City"] = df["City"].str.lower()
print(df["City"])

# Output:
# vizag
# vizag
# vizag
# hyderabad


# ------------------------------------------------------------
# 4. UPPERCASE
# ------------------------------------------------------------

df["Gender"] = df["Gender"].str.upper()
print(df["Gender"])

# Output:
# MALE
# FEMALE
# MALE
# UNKNOWN


# ------------------------------------------------------------
# 5. STANDARDIZE VALUES
# ------------------------------------------------------------

# Different spellings/capitalizations can represent
# the same category.

df["City"] = df["City"].str.strip().str.lower()
print(df["City"])

# "vizag"
# "VIZAG"
# "Vizag "
#
# All become:
# "vizag"


# ------------------------------------------------------------
# 6. replace()
# ------------------------------------------------------------

# Replace incorrect/inconsistent values.
df["City"] = df["City"].replace({
    "vizag": "Visakhapatnam",
    "hyderabad": "Hyderabad"
})
print(df["City"])

# Output:
# Visakhapatnam
# Visakhapatnam
# Visakhapatnam
# Hyderabad


# ------------------------------------------------------------
# 7. REPLACE INCORRECT CATEGORIES
# ------------------------------------------------------------

df["Gender"] = df["Gender"].replace({
    "UNKNOWN": "OTHER"
})
print(df["Gender"])

# Output:
# MALE
# FEMALE
# MALE
# OTHER


# ------------------------------------------------------------
# 8. INVALID CATEGORIES
# ------------------------------------------------------------

# Suppose valid categories are:
# MALE, FEMALE, OTHER

valid_gender = ["MALE", "FEMALE", "OTHER"]
invalid_gender = ~df["Gender"].isin(valid_gender)
print(df[invalid_gender])

# If any rows appear here,
# those values need to be cleaned.


# ------------------------------------------------------------
# 9. isin()
# ------------------------------------------------------------

# Check whether values belong to allowed categories.

print(df["Gender"].isin(["MALE", "FEMALE", "OTHER"]))

# True  = valid category
# False = invalid category


# ------------------------------------------------------------
# 10. IMPOSSIBLE VALUES
# ------------------------------------------------------------

# Age cannot normally be negative.

df["Age"] = df["Age"].mask(
    (df["Age"] < 0) | (df["Age"] > 100),
    np.nan
)
print(df["Age"])

# Invalid values:
# -5
# 200

# They are converted to NaN.


# ------------------------------------------------------------
# 11. IMPOSSIBLE MARKS
# ------------------------------------------------------------

# Suppose marks must be between 0 and 100.

df["Marks"] = df["Marks"].mask(
    (df["Marks"] < 0) | (df["Marks"] > 100),
    np.nan
)

print(df["Marks"])

# 105 is impossible,
# so it becomes NaN.


# ------------------------------------------------------------
# 12. INCORRECT VALUES
# ------------------------------------------------------------

# Example:
# Salary = -50000
# Age = -10
# Percentage = 150

# These values are not normal missing values.
# They are DATA QUALITY PROBLEMS.


# ------------------------------------------------------------
# 13. OUTLIERS BASICS
# ------------------------------------------------------------

# An outlier is a value that is unusually far from most other values.

salary = pd.Series([30000, 32000, 35000, 34000, 1000000])
print(salary)

# 1000000 is much larger than the other values.
# It may be an outlier.


# ------------------------------------------------------------
# 14. OUTLIER DOES NOT ALWAYS MEAN ERROR
# ------------------------------------------------------------

# Example:

# Salaries:
# 30,000
# 32,000
# 35,000
# 34,000
# 10,00,000
#
# 10,00,000 could be:
# - A real high salary
# - A typing error
# - A different population

# Therefore:
# NEVER automatically delete every outlier.


# ------------------------------------------------------------
# 15. SIMPLE OUTLIER CHECK USING DESCRIBE()
# ------------------------------------------------------------

print(salary.describe())

# Look at:
# mean
# min
# max
# 25%
# 50%
# 75%


# ------------------------------------------------------------
# 16. IQR OUTLIER BASICS
# ------------------------------------------------------------

Q1 = salary.quantile(0.25)
Q3 = salary.quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = salary[
    (salary<lower) | (salary > upper)
]
print(outliers)
 
# Values outside:
# lower bound
# upper bound
# are considered potential outliers.


# ------------------------------------------------------------
# 17. CLEANING COLUMN NAMES
# ------------------------------------------------------------

messy = pd.DataFrame({
    " Student Name ": ["Rahul", "Priya"],
    "Student Age": [20, 21],
    "Total Marks ": [85, 90]
})
print(messy.columns)

# Column names contain:
# - Extra spaces
# - Spaces between words


# Remove leading/trailing spaces.
messy.columns = messy.columns.str.strip()
print(messy.columns)


# ------------------------------------------------------------
# 18. STANDARDIZE COLUMN NAMES
# ------------------------------------------------------------

messy.columns = (
    messy.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print(messy.columns)

# Output:
# Index(['student_name', 'student_age', 'total_marks'], dtype='object')


# ------------------------------------------------------------
# 19. rename()
# ------------------------------------------------------------

df2 = pd.DataFrame({
    "student_name": ["Rahul", "Priya"],
    "student_age": [20, 21]
})

df2 = df2.rename(columns={
    "student_name": "name",
    "student_age": "age"
})

print(df2)

# Column names are now:
# name
# age


# ------------------------------------------------------------
# 20. CLEANING TEXT PROPERLY
# ------------------------------------------------------------

students = pd.DataFrame({
    "Name": [" Rahul ", "PRIYA ", " arjun"],
    "City": [" VIZAG", "vizag ", "Vizag"]
})

students["Name"] = (
    students["Name"]
    .str.strip()
    .str.title()
)

students["City"] = (
    students["City"]
    .str.strip()
    .str.lower()
)

students["City"] = students["City"].replace({
    "vizag": "Visakhapatnam"
})

print(students)

# Output:
#     Name           City
# 0  Rahul  Visakhapatnam
# 1  Priya  Visakhapatnam
# 2  Arjun  Visakhapatnam


# ------------------------------------------------------------
# 21. COMPLETE DATA CLEANING WORKFLOW
# ------------------------------------------------------------

df = pd.DataFrame({
    " Student Name ": [" Rahul ", "PRIYA", " arjun "],
    "Age": [20, -5, 21],
    "City": [" VIZAG ", "vizag", "HYDERABAD"],
    "Marks": [85, 90, 105]
})

# STEP 1: Clean column names

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# STEP 2: Clean text

df["student_name"] = (
    df["student_name"]
    .str.strip()
    .str.title()
)

df["city"] = (
    df["city"]
    .str.strip()
    .str.lower()
)

# STEP 3: Standardize categories

df["city"] = df["city"].replace({
    "vizag": "Visakhapatnam",
    "hyderabad": "Hyderabad"
})

# STEP 4: Find impossible Age values

df["age"] = df["age"].mask(
    (df["age"] < 0) | (df["age"] > 100),
    np.nan
)

# STEP 5: Find impossible Marks

df["marks"] = df["marks"].mask(
    (df["marks"] < 0) | (df["marks"] > 100),
    np.nan
)

print(df)

# Result:
# Column names are clean
# Names are standardized
# Cities are standardized
# Invalid Age becomes NaN
# Invalid Marks becomes NaN


# ------------------------------------------------------------
# 22. FINAL QUALITY CHECK
# ------------------------------------------------------------

print(df.info())
print(df.describe())
print(df.isna().sum())
print(df.duplicated().sum()) # Check for duplicates & remove if necessary returns True/False for each row at last output is the sum of all True values


# ------------------------------------------------------------
# IMPORTANT CLEANING PATTERNS
# ------------------------------------------------------------

# Remove whitespace:
# df["Name"] = df["Name"].str.strip()

# Lowercase:
# df["Name"] = df["Name"].str.lower()

# Uppercase:
# df["Name"] = df["Name"].str.upper()

# Title case:
# df["Name"] = df["Name"].str.title()

# Replace values:
# df["City"] = df["City"].replace(old, new)

# Rename columns:
# df = df.rename(columns={"old": "new"})

# Check valid categories:
# df["Gender"].isin(["MALE", "FEMALE", "OTHER"])

# Detect duplicates:
# df.duplicated()

# Remove duplicates:
# df.drop_duplicates()


# ------------------------------------------------------------
# ML ENGINEERING THINKING
# ------------------------------------------------------------

# Raw Dataset
#      ↓
# Inspect
#      ↓
# Detect incorrect values
#      ↓
# Detect inconsistent values
#      ↓
# Remove whitespace
#      ↓
# Standardize text/categories
#      ↓
# Detect impossible values
#      ↓
# Investigate outliers
#      ↓
# Handle missing values
#      ↓
# Quality check
#      ↓
# Reliable Dataset
#      ↓
# Feature Engineering
#      ↓
# Machine Learning