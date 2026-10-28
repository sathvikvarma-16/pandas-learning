import pandas as pd

# Check Pandas version
print(pd.__version__)

# Pandas is a Python library used for:
# - Loading data
# - Cleaning data
# - Analyzing data
# - Manipulating tables
# - Preparing data for Machine Learning

# NumPy vs Pandas

# NumPy -> mainly works with numerical arrays
# Pandas -> works with structured/tabular data

# NumPy:
# [10, 20, 30, 40]

# Pandas:
# Name    Age    Marks
# Ravi    20     85
# Rahul   21     90


# Series
# A Series is a 1-dimensional labeled data structure.

marks = pd.Series([80, 90, 75, 95])
print(marks)

# Output:
# 0    80
# 1    90
# 2    75
# 3    95
# dtype: int64


# DataFrame
# A DataFrame is a 2-dimensional table.
# It contains rows and columns.

data = {
    "Name": ["Ravi", "Rahul", "Anil"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)

# Output:
#     Name  Age  Marks
# 0   Ravi   20     85
# 1  Rahul   21     90
# 2   Anil   19     78


# Index
# Index identifies each row.

print(df.index)

# Output:
# RangeIndex(start=0, stop=3, step=1)


# Columns
# Columns represent variables/features.

print(df.columns)

# Output:
# Index(['Name', 'Age', 'Marks'], dtype='object')


# Access a column

print(df["Marks"])

# Output:
# 0    85
# 1    90
# 2    78
# Name: Marks, dtype: int64


# Vectorized operation
# Perform an operation on an entire column without a loop.

df["Marks"] = df["Marks"] + 5
print(df["Marks"])

# Output:
# 0    90
# 1    95
# 2    83
# Name: Marks, dtype: int64


# Mental model:

# Python
#   ↓
# NumPy
#   ↓
# Pandas
#   ↓
# Data Cleaning
#   ↓
# EDA
#   ↓
# Machine Learning

# NumPy -> numerical arrays
# Pandas -> structured/tabular data
# Pandas is built on top of NumPy concepts.

