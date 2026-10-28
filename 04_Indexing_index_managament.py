import pandas as pd


df = pd.DataFrame({
    "name": ["Ravi", "Rahul", "Anil", "Priya"],
    "age": [20, 21, 19, 22],
    "marks": [85, 92, 78, 88]
})


# 1. What is an index?
# Index identifies each row.
# By default, Pandas creates 0, 1, 2, 3...

print(df.index)

# Output:
# RangeIndex(start=0, stop=4, step=1)


# 2. Default index
print(df)

# Output:
#     name  age  marks
# 0   Ravi   20     85
# 1  Rahul   21     92
# 2   Anil   19     78
# 3  Priya   22     88


# 3. Custom index
df.index = ["S1", "S2", "S3", "S4"]
print(df)

# Output:
#     name  age  marks
# S1  Ravi   20     85
# S2  Rahul  21     92
# S3  Anil   19     78
# S4  Priya  22     88


# 4. set_index()
# Make an existing column the index.

df = pd.DataFrame({
    "name": ["Ravi", "Rahul", "Anil"],
    "age": [20, 21, 19],
    "marks": [85, 92, 78]
})

df = df.set_index("name")
print(df)

# Output:
#        age  marks
# name
# Ravi    20     85
# Rahul   21     92
# Anil    19     78


# 5. Select using the index
print(df.loc["Rahul"])

# Output:
# age      21
# marks    92
# Name: Rahul, dtype: int64


# 6. Select a specific value using the index
print(df.loc["Rahul", "marks"])

# Output:
# 92


# 7. reset_index()
# Move the index back into a normal column.
df = df.reset_index()

print(df)

# Output:
#     name  age  marks
# 0   Ravi   20     85
# 1  Rahul   21     92
# 2   Anil   19     78


# 8. sort_index()

df = pd.DataFrame({
    "name": ["Ravi", "Rahul", "Anil"],
    "marks": [85, 92, 78]
}, index=["C", "A", "B"])
print(df.sort_index())

# Output:
#     name  marks
# A  Rahul     92
# B   Anil     78
# C   Ravi     85



# 9. Sort index in descending order

print(df.sort_index(ascending=False))
# Output:
#     name  marks
# C   Ravi     85
# B   Anil     78
# A  Rahul     92


# 10. Index selection with loc

df = pd.DataFrame({
    "name": ["Ravi", "Rahul", "Anil"],
    "marks": [85, 92, 78]
}, index=["S1", "S2", "S3"])
print(df.loc["S1":"S2"])

# Output:
#     name  marks
# S1  Ravi     85
# S2  Rahul    92


# 11. Index vs position

# loc -> uses index label
print(df.loc["S2"])

# iloc -> uses row position
print(df.iloc[1])

# Both select Rahul's row.

# Output:
# name     Rahul
# marks        92
# Name: S2, dtype: object

# name     Rahul
# marks        92
# Name: S2, dtype: object



# 12. MultiIndex basics

df = pd.DataFrame({
    "student": ["Ravi", "Rahul", "Anil", "Priya"],
    "marks": [85, 92, 78, 88]
})

df = df.set_index(["student", "marks"])
print(df.index)

# Output:
# MultiIndex([
#     ('Ravi', 85),
#     ('Rahul', 92),
#     ('Anil', 78),
#     ('Priya', 88)
# ], names=['student', 'marks'])


# 13. Reset MultiIndex

df = df.reset_index()

print(df)

# Output:
#   student  marks
# 0    Ravi     85
# 1   Rahul     92
# 2    Anil     78
# 3   Priya     88


# 14. When indexes help

# Indexes are useful when:
# - Rows have meaningful identifiers
# - You frequently select rows by that identifier
# - Working with time-series data
# - Aligning/combining Pandas data

# Example:
# Student ID, Date, Product ID, etc.


# 15. When indexes don't need to be special

# For most ML datasets:
#
#       Age  Salary  Marks
# 0      20   20000     85
# 1      21   30000     92
# 2      19   25000     78
#
# The default 0, 1, 2... index is completely fine.
#
# Do NOT create a complicated index just because you can.


# Remember:

# index       -> identifies rows
# set_index() -> column → index
# reset_index() -> index → column
# sort_index() -> sort by index
# loc[]       -> index labels
# iloc[]      -> row positions
# MultiIndex  -> multiple levels of indexes
