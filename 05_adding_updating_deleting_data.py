import pandas as pd

df = pd.DataFrame({
    "name": ["Ravi", "Rahul", "Anil"],
    "age": [20, 21, 19],
    "marks": [85, 92, 78]
})

print(df)

# Output:
#     name  age  marks
# 0   Ravi   20     85
# 1  Rahul   21     92
# 2   Anil   19     78


# 1. Add a new column

df["salary"] = [20000, 30000, 25000]
print(df)

# Output:
#     name  age  marks  salary
# 0   Ravi   20     85   20000
# 1  Rahul   21     92   30000
# 2   Anil   19     78   25000


# 2. Add a calculated column

df["bonus"] = df["salary"] * 0.10
print(df["bonus"])

# Output:
# 0    2000.0
# 1    3000.0
# 2    2500.0
# Name: bonus, dtype: float64


# 3. Update a complete column

df["age"] = df["age"] + 1
print(df["age"])

# Output:
# 0    21
# 1    22
# 2    20
# Name: age, dtype: int64


# 4. Update one value
df.loc[0, "marks"] = 90
print(df.loc[0, "marks"])

# Output:
# 90


# 5. Update multiple values using a condition

df.loc[df["marks"] < 80, "marks"] = 80
print(df["marks"])

# Output:
# 0    90
# 1    92
# 2    80
# Name: marks, dtype: int64


# 6. Rename columns
df = df.rename(columns={
    "name": "student_name",
    "marks": "score"
})
print(df.columns)

# Output:
# Index(['student_name', 'age', 'score', 'salary', 'bonus'], dtype='object')


# 7. Drop a column

df = df.drop(columns="bonus")
print(df.columns)

# Output:
# Index(['student_name', 'age', 'score', 'salary'], dtype='object')


# 8. Drop multiple columns
df = df.drop(columns=["salary"])
print(df.columns)

# Output:
# Index(['student_name', 'age', 'score'], dtype='object')


# 9. Drop a row
df = df.drop(index=1)
print(df)

# Output:
#   student_name  age  score
# 0         Ravi   21     90
# 2         Anil   20     80


# 10. Drop multiple rows

df = pd.DataFrame({
    "name": ["Ravi", "Rahul", "Anil", "Priya"],
    "marks": [85, 92, 78, 88]
})

df = df.drop(index=[0, 2])
print(df)

# Output:
#     name  marks
# 1  Rahul     92
# 3  Priya     88


# 11. Add a row
df.loc[4] = ["Kiran", 95]
print(df)

# Output:
#    name    marks
# 1  Rahul     92
# 3  Priya     88
# 4  Kiran     95



# 12. Reorder columns
df = pd.DataFrame({
    "name": ["Ravi", "Rahul"],
    "age": [20, 21],
    "marks": [85, 92]
})

df = df[["name", "marks", "age"]]
print(df)

# Output:
#     name  marks  age
# 0   Ravi     85   20
# 1  Rahul     92   21



# 13. Complete modification example
df = pd.DataFrame({
    "name": ["Ravi", "Rahul", "Anil"],
    "age": [20, 21, 19],
    "marks": [85, 92, 78]
})

# Add column
df["passed"] = df["marks"] >= 40

# Update value
df.loc[2, "marks"] = 82

# Rename column
df = df.rename(columns={"marks": "score"})

# Drop column
df = df.drop(columns="age")

# Reorder columns
df = df[["name", "score", "passed"]]

print(df)

# Output:
#     name  score  passed
# 0   Ravi     85    True
# 1  Rahul     92    True
# 2   Anil     82    True
