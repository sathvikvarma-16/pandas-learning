import pandas as pd
import numpy as np


# 1. Create a DataFrame from a dictionary

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


# 2. Create DataFrame from a list

data = [
    ["Ravi", 20, 85],
    ["Rahul", 21, 90],
    ["Anil", 19, 78]
]

df = pd.DataFrame(data, columns=["Name", "Age", "Marks"])
print(df)

# Output:
#     Name  Age  Marks
# 0   Ravi   20     85
# 1  Rahul   21     90
# 2   Anil   19     78


# 3. Create DataFrame from NumPy array

arr = np.array([
    [20, 85],
    [21, 90],
    [19, 78]
])

df = pd.DataFrame(arr, columns=["Age", "Marks"])

print(df)

# Output:
#    Age  Marks
# 0   20     85
# 1   21     90
# 2   19     78


# 4. DataFrame from structured data

data = {
    "Name": ["Ravi", "Rahul", "Anil", "Priya"],
    "Age": [20, 21, 19, 20],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(data)


# 5. Shape
# (rows, columns)

print(df.shape)

# Output:
# (4, 3)


# 6. Size
# Total number of elements

print(df.size)

# Output:
# 12


# 7. Number of dimensions

print(df.ndim)

# Output:
# 2


# 8. Column names

print(df.columns)

# Output:
# Index(['Name', 'Age', 'Marks'], dtype='object')


# 9. Row index

print(df.index)

# Output:
# RangeIndex(start=0, stop=4, step=1)


# 10. Data types of columns

print(df.dtypes)

# Output:
# Name     object
# Age       int64
# Marks     int64
# dtype: object


# 11. Complete DataFrame information

df.info()

# Output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 3 columns):
# Name     4 non-null
# Age      4 non-null
# Marks    4 non-null
# dtype: object


# 12. Statistical summary

print(df.describe())

# Output:
#              Age      Marks
# count   4.000000   4.000000
# mean   20.000000  86.250000
# std     0.816497   6.238095
# min    19.000000  78.000000
# 25%    19.750000  83.250000
# 50%    20.000000  87.500000
# 75%    20.250000  90.500000
# max    21.000000  92.000000


# 13. Access a column

print(df["Marks"])

# Output:
# 0    85
# 1    90
# 2    78
# 3    92
# Name: Marks, dtype: int64


# 14. Access multiple columns

print(df[["Name", "Marks"]])

# Output:
#     Name  Marks
# 0   Ravi     85
# 1  Rahul     90
# 2   Anil     78
# 3  Priya     92


# 15. Access a row using iloc

print(df.iloc[0])

# Output:
# Name     Ravi
# Age        20
# Marks      85
# Name: 0, dtype: object


# 16. Change column names

df.columns = ["Student", "Age", "Score"]
print(df.columns)

# Output:
# Index(['Student', 'Age', 'Score'], dtype='object')


# 17. Basic DataFrame inspection

print(df.shape)
print(df.size)
print(df.ndim)
print(df.columns)
print(df.index)
print(df.dtypes)

# Output:
# (4, 3)
# 12
# 2
# Index(['Student', 'Age', 'Score'], dtype='object')
# RangeIndex(start=0, stop=4, step=1)
# Student    object
# Age         int64
# Score       int64
# dtype: object
