import pandas as pd

df = pd.DataFrame({
    "name": ["Ravi", "Rahul", "Anil", "Priya"],
    "age": [20, 21, 19, 22],
    "marks": [85, 92, 78, 88],
    "city": ["Vizag", "Hyderabad", "Vizag", "Chennai"]
})

# 1. Select one column
print(df["name"])

# Output:
# 0     Ravi
# 1    Rahul
# 2     Anil
# 3    Priya
# Name: name, dtype: object


# 2. Select multiple columns
print(df[["name", "age"]])

# Output:
#     name  age
# 0   Ravi   20
# 1  Rahul   21
# 2   Anil   19
# 3  Priya   22


# 3. loc[]
# loc uses labels.
print(df.loc[0])

# Output:
# name      Ravi
# age         20
# marks       85
# city     Vizag
# Name: 0, dtype: object

  
# 4. Select specific row using loc

print(df.loc[1])

# Output:
# name        Rahul
# age            21
# marks          92
# city      Hyderabad
# Name: 1, dtype: object


# 5. Select specific cell using loc

print(df.loc[1, "marks"])

# Output:
# 92


# 6. Select rows and columns using loc
print(df.loc[0:2, ["name", "marks"]])

# Output:
#     name  marks
# 0   Ravi     85
# 1  Rahul     92
# 2   Anil     78


# 7. Row range using loc
# loc includes the ending label.

print(df.loc[1:3])

# Output:
#     name  age  marks       city
# 1  Rahul   21     92  Hyderabad
# 2   Anil   19     78      Vizag
# 3  Priya   22     88    Chennai


# 8. iloc[]
# iloc uses integer positions.

print(df.iloc[0])

# Output:
# name      Ravi
# age         20
# marks       85
# city     Vizag
# Name: 0, dtype: object


# 9. Select a specific cell using iloc

print(df.iloc[1, 2])

# Output:
# 92


# 10. Select rows using iloc
print(df.iloc[1:3])

# Output:
#     name  age  marks       city
# 1  Rahul   21     92  Hyderabad
# 2   Anil   19     78      Vizag


# 11. Select rows and columns using iloc
print(df.iloc[0:3, 0:2])

# Output:
#     name  age
# 0   Ravi   20
# 1  Rahul   21
# 2   Anil   19


# 12. Select specific rows and columns
print(df.iloc[[0, 2], [0, 2]])

# Output:
#    name  marks
# 0  Ravi     85
# 2  Anil     78


# 13. Select a column range using iloc
print(df.iloc[:, 1:3])

# Output:
#    age  marks
# 0   20     85
# 1   21     92
# 2   19     78
# 3   22     88


# 14. Select all rows and one column using iloc
print(df.iloc[:, 2])

# Output:
# 0    85
# 1    92
# 2    78
# 3    88
# Name: marks, dtype: int64


# 15. Conditional selection
print(df[df["marks"] > 85])

# Output:
#     name  age  marks       city
# 1  Rahul   21     92  Hyderabad
# 3  Priya   22     88    Chennai


# 16. Conditional selection with specific columns
print(df.loc[df["marks"] > 85, ["name", "marks"]])

# Output:
#     name  marks
# 1  Rahul     92
# 3  Priya     88


# 17. Multiple conditions
print(df[(df["age"] > 19) & (df["marks"] >= 85)])

# Output:
#     name  age  marks       city
# 0   Ravi   20     85      Vizag
# 1  Rahul   21     92  Hyderabad
# 3  Priya   22     88    Chennai


# 18. OR condition
print(df[(df["city"] == "Vizag") | (df["marks"] > 90)])

# Output:
#     name  age  marks       city
# 0   Ravi   20     85      Vizag
# 1  Rahul   21     92  Hyderabad
# 2   Anil   19     78      Vizag


# 19. Select rows based on one column
print(df.loc[df["city"] == "Vizag"])

# Output:
#    name  age  marks   city
# 0  Ravi   20     85  Vizag
# 2  Anil   19     78  Vizag


# 20. Select one specific value
print(df.loc[2, "name"])

# Output:
# Anil


# 21. The most important difference

# df["marks"]
# -> Select column by column name

# df.loc[1, "marks"]
# -> Select using row label + column name

# df.iloc[1, 2]
# -> Select using row position + column position


# 22. Quick automatic practice

print(df["marks"])                    # One column
print(df[["name", "marks"]])           # Multiple columns
print(df.loc[1])                       # One row
print(df.loc[1, "marks"])              # One cell
print(df.iloc[1, 2])                   # One cell by position
print(df.loc[1:3, ["name", "age"]])    # Row + column range
print(df.iloc[1:3, 0:2])               # Position ranges
print(df[df["marks"] >= 90])           # Condition

# Output:
# These produce the corresponding selections from df.


# REMEMBER

# df["name"]
# -> column

# df[["name", "age"]]
# -> multiple columns

# df.loc[row_label, column_label]
# -> label-based selection

# df.iloc[row_position, column_position]
# -> position-based selection

# loc[1:3]
# -> includes 3

# iloc[1:3]
# -> stops before 3

# Conditional:
# df[df["marks"] > 85]

# Multiple conditions:
# (condition1) & (condition2)
# (condition1) | (condition2)
