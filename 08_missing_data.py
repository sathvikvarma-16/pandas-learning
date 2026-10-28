import pandas as pd
import numpy as np


# ============================================================
# PHASE 8: MISSING DATA
# ============================================================

# Missing values are usually represented by:
# NaN = Not a Number
# None = Python missing value
# NaT = Missing datetime value


# ------------------------------------------------------------
# 1. CREATE DATA WITH MISSING VALUES
# ------------------------------------------------------------

df = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran"],
    "Age": [20, np.nan, 22, np.nan, 21],
    "Marks": [85, 90, np.nan, 78, 88],
    "City": ["Vizag", "Hyderabad", None, "Chennai", "Vizag"]
})
print(df)

# Output:
#      Name   Age  Marks        City
# 0   Rahul  20.0   85.0       Vizag
# 1   Priya   NaN   90.0   Hyderabad
# 2   Arjun  22.0    NaN        None
# 3   Sneha   NaN   78.0     Chennai
# 4   Kiran  21.0   88.0       Vizag


# ------------------------------------------------------------
# 2. isna()
# ------------------------------------------------------------

# Checks whether each value is missing.

print(df.isna())

# Output:
#      Name    Age  Marks   City
# 0   False  False  False  False
# 1   False   True  False  False
# 2   False  False   True   True
# 3   False   True  False  False
# 4   False  False  False  False


# ------------------------------------------------------------
# 3. isnull()
# ------------------------------------------------------------

# isnull() does the same thing as isna().
print(df.isnull())

# Output:
# Same result as isna()


# ------------------------------------------------------------
# 4. notna()
# ------------------------------------------------------------

# Checks whether values are NOT missing.
print(df.notna())

# Output:
# True  = value exists
# False = value is missing


# ------------------------------------------------------------
# 5. COUNT MISSING VALUES
# ------------------------------------------------------------

# isna() gives True/False.
# sum() counts True as 1.

print(df.isna().sum())

# Output:
# Name     0
# Age      2
# Marks    1
# City     1


# ------------------------------------------------------------
# 6. TOTAL NUMBER OF MISSING VALUES
# ------------------------------------------------------------

print(df.isna().sum().sum())

# Output:
# 4


# ------------------------------------------------------------
# 7. MISSING VALUES IN ONE COLUMN
# ------------------------------------------------------------

print(df["Age"].isna().sum())

# Output:
# 2


# ------------------------------------------------------------
# 8. FIND ROWS WITH MISSING VALUES
# ------------------------------------------------------------

print(df[df["Age"].isna()])

# Output:
#     Name  Age  Marks       City
# 1  Priya  NaN   90.0  Hyderabad
# 3  Sneha  NaN   78.0    Chennai


# ------------------------------------------------------------
# 9. dropna()
# ------------------------------------------------------------

# Removes rows containing missing values.

clean_df = df.dropna()
print(clean_df)

# Output:
#     Name   Age  Marks   City
# 0  Rahul  20.0   85.0  Vizag
# 4  Kiran  21.0   88.0  Vizag


# ------------------------------------------------------------
# 10. DROP ROWS BASED ON ONE COLUMN
# ------------------------------------------------------------

clean_age = df.dropna(subset=["Age"])
print(clean_age)

# Rows where Age is missing are removed.


# ------------------------------------------------------------
# 11. REMOVE COLUMNS WITH MISSING VALUES
# ------------------------------------------------------------

# axis=1 means columns.

drop_columns = df.dropna(axis=1)
print(drop_columns)

# Columns containing missing values are removed.


# ------------------------------------------------------------
# 12. fillna()
# ------------------------------------------------------------

# Instead of removing missing values,
# we can replace them.

filled = df["Age"].fillna(25)
print(filled)

# Output:
# 0    20.0
# 1    25.0
# 2    22.0
# 3    25.0
# 4    21.0


# ------------------------------------------------------------
# 13. FILL MISSING VALUES WITH MEAN
# ------------------------------------------------------------

mean_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(mean_age)
print(df["Age"])

# Mean:
# (20 + 22 + 21) / 3 = 21

# Output:
# 0    20.0
# 1    21.0
# 2    22.0
# 3    21.0
# 4    21.0


# ------------------------------------------------------------
# 14. FILL WITH MEDIAN
# ------------------------------------------------------------

df2 = pd.DataFrame({
    "Age": [20, 21, np.nan, 22, 100]
})
median_age = df2["Age"].median()
df2["Age"] = df2["Age"].fillna(median_age)
print(df2)

# Median is useful when data contains outliers.

# Ages:
# 20, 21, 22, 100

# Median = 21.5


# ------------------------------------------------------------
# 15. FILL WITH MODE
# ------------------------------------------------------------

df3 = pd.DataFrame({
    "City": ["Vizag", "Chennai", "Vizag", np.nan, "Vizag"]
})
mode_city = df3["City"].mode()[0]
df3["City"] = df3["City"].fillna(mode_city)
print(df3)

# Output:
#       City
# 0    Vizag
# 1    Chennai
# 2    Vizag
# 3    Vizag
# 4    Vizag


# ------------------------------------------------------------
# 16. FORWARD FILL
# ------------------------------------------------------------

df4 = pd.DataFrame({
    "Temperature": [30, np.nan, np.nan, 35, np.nan]
})

df4["Temperature"] = df4["Temperature"].ffill()
print(df4)

# Output:
#    Temperature
# 0         30.0
# 1         30.0
# 2         30.0
# 3         35.0
# 4         35.0

# ffill = use the previous available value.


# ------------------------------------------------------------
# 17. BACKWARD FILL
# ------------------------------------------------------------

df5 = pd.DataFrame({
    "Temperature": [30, np.nan, np.nan, 35, np.nan]
})
df5["Temperature"] = df5["Temperature"].bfill()
print(df5)

# Output:
#    Temperature
# 0         30.0
# 1         35.0
# 2         35.0
# 3         35.0
# 4          NaN

# bfill = use the next available value.


# ------------------------------------------------------------
# 18. WHICH STRATEGY SHOULD WE USE?
# ------------------------------------------------------------

# Numerical column:
# Mean   -> useful when data has no strong outliers
# Median -> useful when outliers exist
#
# Categorical column:
# Mode   -> common choice
#
# Time-series data:
# Forward fill / Backward fill
#
# Very few missing rows:
# dropna() may be suitable
#
# Too many missing values:
# Consider removing the column


# ------------------------------------------------------------
# 19. IMPORTANT ML THINKING
# ------------------------------------------------------------

# Example:
#
# Missing Age
#      |
#      ↓
# Understand WHY it is missing
#      |
#      ↓
# Check how much data is missing
#      |
#      ↓
# Choose strategy
#      |
#      ├── Mean
#      ├── Median
#      ├── Mode
#      ├── Forward Fill
#      ├── Backward Fill
#      └── Drop
#      |
#      ↓
# Clean dataset
#      |
#      ↓
# Machine Learning


# ------------------------------------------------------------
# 20. COMPLETE MISSING DATA WORKFLOW
# ------------------------------------------------------------

df = pd.DataFrame({
    "Age": [20, np.nan, 22, np.nan, 21],
    "Salary": [30000, 40000, np.nan, 35000, 32000],
    "City": ["Vizag", "Vizag", np.nan, "Chennai", "Vizag"]
})

# Step 1: Detect
print(df.isna())

# Step 2: Count
print(df.isna().sum())

# Step 3: Handle numerical column
df["Age"] = df["Age"].fillna(df["Age"].median())

# Step 4: Handle numerical column
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

# Step 5: Handle categorical column
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Step 6: Check again
print(df.isna().sum())

# Output:
# Age       0
# Salary    0
# City      0


# ------------------------------------------------------------
# MOST IMPORTANT PATTERNS TO REMEMBER
# ------------------------------------------------------------

# Detect:
# df.isna()

# Same as:
# df.isnull()

# NOT missing:
# df.notna()

# Count missing:
# df.isna().sum()

# Remove missing rows:
# df.dropna()

# Remove missing columns:
# df.dropna(axis=1)

# Fill:
# df.fillna(value)

# Mean:
# df["Age"].fillna(df["Age"].mean())

# Median:
# df["Age"].fillna(df["Age"].median())

# Mode:
# df["City"].fillna(df["City"].mode()[0])

# Forward fill:
# df["Age"].ffill()

# Backward fill:
# df["Age"].bfill()
