
import pandas as pd
import numpy as np


# ============================================================
# PHASE 13: APPLY, MAP & TRANSFORM
# ============================================================


df = pd.DataFrame({
    "name": ["Rahul", "Priya", "Arjun", "Sneha"],
    "marks": [85, 92, 68, 75],
    "salary": [40000, 60000, 35000, 50000],
    "department": ["IT", "HR", "IT", "HR"]
})
print(df)


# ------------------------------------------------------------
# 1. lambda
# ------------------------------------------------------------

# lambda creates a small anonymous function.
square = lambda x: x * x
print(square(5))

# Output:
# 25


# Normal function:
def square_number(x):
    return x * x
print(square_number(5))

# Output:
# 25

# lambda is useful for short operations.


# ------------------------------------------------------------
# 2. map()
# ------------------------------------------------------------

# map() applies a function to every value in a Series.

df["marks_squared"] = df["marks"].map(
    lambda x: x * x
)
print(df[["marks", "marks_squared"]])

# Output:
#    marks  marks_squared
# 0     85           7225
# 1     92           8464
# 2     68           4624
# 3     75           5625


# ------------------------------------------------------------
# 3. map() WITH DICTIONARY
# ------------------------------------------------------------

df["department_code"] = df["department"].map({
    "IT": 1,
    "HR": 2
})
print(df[["department", "department_code"]])

# IT -> 1
# HR -> 2

# Values not present in the mapping become NaN.


# ------------------------------------------------------------
# 4. map() FOR TEXT
# ------------------------------------------------------------

df["name_upper"] = df["name"].map(
    lambda x: x.upper()
)
print(df[["name", "name_upper"]])


# ------------------------------------------------------------
# 5. apply() ON A SERIES
# ------------------------------------------------------------

# apply() applies a function to each Series value.

df["bonus"] = df["salary"].apply(
    lambda x: x * 0.10
)
print(df[["salary", "bonus"]])

# Bonus = 10% of salary.


# ------------------------------------------------------------
# 6. apply() WITH CONDITIONS
# ------------------------------------------------------------

df["result"] = df["marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)
print(df[["marks", "result"]])

# Marks >= 40 -> Pass
# Otherwise -> Fail


# ------------------------------------------------------------
# 7. apply() ROW-WISE
# ------------------------------------------------------------

# axis=1 means process one row at a time.

df["total_score"] = df.apply(
    lambda row: row["marks"] + row["salary"] / 10000,
    axis=1
)
print(df[["name", "marks", "salary", "total_score"]])

# Each row is passed to the function.
#
# row["marks"] -> marks of current student
# row["salary"] -> salary of current student


# ------------------------------------------------------------
# 8. apply() COLUMN-WISE
# ------------------------------------------------------------

# axis=0 means process each column.

numeric_df = df[["marks", "salary"]]
print(numeric_df.apply(max, axis=0))

# Output:
# marks       92
# salary   60000

# One result per column.


# ------------------------------------------------------------
# 9. DataFrame.map() 
# ------------------------------------------------------------

# Modern replacement for the old DataFrame.applymap().
# Applies a function to every individual cell.

small_df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})
result = small_df.map(lambda x: x * 10)
print(result)

# Output:
#     A   B
# 0  10  40
# 1  20  50
# 2  30  60


# ------------------------------------------------------------
# 10. applymap() HISTORICAL NOTE
# ------------------------------------------------------------

# Older Pandas code:
#
# small_df.applymap(lambda x: x * 10)
#
# In modern Pandas, use:
#
# small_df.map(lambda x: x * 10)
#
# applymap() was deprecated in Pandas 2.1
# and removed in Pandas 3.0.


# ------------------------------------------------------------
# 11. transform()
# ------------------------------------------------------------

# transform() returns results aligned to the original rows.

df["marks_plus_5"] = df["marks"].transform(
    lambda x: x + 5
)
print(df[["marks", "marks_plus_5"]])

# Output:
#    marks  marks_plus_5
# 0     85            90
# 1     92            97
# 2     68            73
# 3     75            80
 

# ------------------------------------------------------------
# 12. transform() WITH STANDARDIZATION
# ------------------------------------------------------------

# Standardization:
# (value - mean) / standard deviation

df["marks_standardized"] = df["marks"].transform(
    lambda x: (x - x.mean()) / x.std()
)
print(df[["marks", "marks_standardized"]])

# Each value is standardized using
# the mean and standard deviation of marks.


# ------------------------------------------------------------
# 13. GROUPBY + transform()
# ------------------------------------------------------------

# Calculate average salary within each department.
# Keep one result for every original employee.

df["department_avg_salary"] = (
    df.groupby("department")["salary"]
    .transform("mean")
)
print(df[["department", "salary", "department_avg_salary"]])

# Output:
#   department  salary  department_avg_salary
# 0          IT   40000                37500.0
# 1          HR   60000                55000.0
# 2          IT   35000                37500.0
# 3          HR   50000                55000.0


# ------------------------------------------------------------
# 14. GROUPBY + transform() FOR FEATURE ENGINEERING
# ------------------------------------------------------------

# Compare each employee salary with
# their department's average salary.

df["salary_vs_department_avg"] = (
    df["salary"] - df["department_avg_salary"]
)
print(df[[
    "department",
    "salary",
    "department_avg_salary",
    "salary_vs_department_avg"
]])

# Positive -> above department average
# Negative -> below department average
# Zero -> equal to department average


# ------------------------------------------------------------
# 15. GROUPBY + transform("max")
# ------------------------------------------------------------

df["department_max_salary"] = (
    df.groupby("department")["salary"]
    .transform("max")
)
print(df[["department", "salary", "department_max_salary"]])


# ------------------------------------------------------------
# 16. VECTORISED OPERATIONS
# ------------------------------------------------------------

# Prefer this:

df["salary_double"] = df["salary"] * 2

# Instead of:

# df["salary_double"] = df["salary"].apply(
#     lambda x: x * 2
# )

# Direct vectorized operations are usually
# simpler and faster for basic arithmetic.


# ------------------------------------------------------------
# 17. CONDITIONAL VECTORISED OPERATION
# ------------------------------------------------------------

df["status"] = np.where(
    df["marks"] >= 40,
    "Pass",
    "Fail"
)
print(df[["marks", "status"]])


# ------------------------------------------------------------
# 18. np.select() FOR MULTIPLE CONDITIONS
# ------------------------------------------------------------

conditions = [
    df["marks"] >= 90,
    df["marks"] >= 75,
    df["marks"] >= 40
]
choices = ["A", "B", "C"]
df["grade"] = np.select(
    conditions,
    choices,
    default="Fail"
)
print(df[["marks", "grade"]])

# 90 and above -> A
# 75 to 89 -> B
# 40 to 74 -> C
# Below 40 -> Fail


# ------------------------------------------------------------
# 19. COMPLETE FEATURE ENGINEERING EXAMPLE
# ------------------------------------------------------------

students = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "marks": [90, 75, 45, 30],
    "department": ["CSE", "CSE", "ECE", "ECE"]
})

# Feature 1: Pass/Fail
students["result"] = np.where(
    students["marks"] >= 40,
    "Pass",
    "Fail"
)

# Feature 2: Bonus marks
students["bonus_marks"] = students["marks"] + 5

# Feature 3: Department average
students["department_avg"] = (
    students.groupby("department")["marks"]
    .transform("mean")
)

# Feature 4: Difference from department average
students["difference"] = (
    students["marks"] - students["department_avg"]
)

print(students)


# ------------------------------------------------------------
# MOST IMPORTANT PATTERNS
# ------------------------------------------------------------

# Series mapping:
# df["marks"].map(lambda x: x * 2)

# Dictionary mapping:
# df["department"].map({"IT": 1, "HR": 2})

# Series apply:
# df["salary"].apply(lambda x: x * 0.1)

# Row-wise apply:
# df.apply(function, axis=1)

# Column-wise apply:
# df.apply(function, axis=0)

# Modern element-wise DataFrame mapping:
# df.map(lambda x: x * 2)

# Transform:
# df["marks"].transform(lambda x: x + 5)

# Group transformation:
# df.groupby("department")["salary"].transform("mean")

# Vectorized:
# df["salary"] * 2

# Conditional:
# np.where(df["marks"] >= 40, "Pass", "Fail")

