# GroupBy & Aggregation

"""
High-priority Pandas topic for ML Engineering
This is one of the most important Pandas concepts because it helps you extract useful information from large datasets.
Imagine a company dataset containing employees from IT, HR, Sales, and Finance.
You want to know
Average salary of each department
Total salary paid by each department
Number of employees in each department
Highest and lowest salary in each department
Instead of calculating everything manually, use groupby() + aggregation.
"""


import pandas as pd


# ============================================================
# PHASE 12: GROUPBY & AGGREGATION
# ============================================================

df = pd.DataFrame({
    "name": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran", "Aman"],
    "department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "salary": [60000, 45000, 75000, 50000, 55000, 65000],
    "age": [24, 25, 28, 23, 27, 26]
})
print(df)


# ------------------------------------------------------------
# 1. BASIC groupby()
# ------------------------------------------------------------

# Group employees according to department.

result = df.groupby("department")
print(result)

# groupby() creates a grouped object.
# It does not immediately calculate a result.


# ------------------------------------------------------------
# 2. GROUP BY DEPARTMENT AND CALCULATE MEAN
# ------------------------------------------------------------

result = df.groupby("department")["salary"].mean()
print(result)

# Output:
# department
# HR       50000.0
# IT       67500.0
# Sales    57500.0


# Understand:
#
# HR:
# (45000 + 55000) / 2 = 50000
#
# IT:
# (60000 + 75000) / 2 = 67500
#
# Sales:
# (50000 + 65000) / 2 = 57500


# ------------------------------------------------------------
# 3. sum()
# ------------------------------------------------------------

result = df.groupby("department")["salary"].sum()
print(result)

# Output:
# HR        100000
# IT        135000
# Sales     115000


# ------------------------------------------------------------
# 4. mean()
# ------------------------------------------------------------

result = df.groupby("department")["age"].mean()
print(result)

# Average age of each department.


# ------------------------------------------------------------
# 5. median()
# ------------------------------------------------------------

result = df.groupby("department")["salary"].median()
print(result)

# Median salary for each department.


# ------------------------------------------------------------
# 6. min()
# ------------------------------------------------------------

result = df.groupby("department")["salary"].min()
print(result)

# Lowest salary in each department.


# ------------------------------------------------------------
# 7. max()
# ------------------------------------------------------------

result = df.groupby("department")["salary"].max()
print(result)

# Highest salary in each department.


# ------------------------------------------------------------
# 8. count()
# ------------------------------------------------------------

result = df.groupby("department")["salary"].count()
print(result)

# Counts non-missing salary values in each group.


# ------------------------------------------------------------
# 9. size()
# ------------------------------------------------------------

result = df.groupby("department").size()
print(result)

# Output:
# department
# HR       2
# IT       2
# Sales    2

# size() counts rows in each group.
# count() counts non-missing values in a selected column.


# ------------------------------------------------------------
# 10. GROUP BY MULTIPLE COLUMNS
# ------------------------------------------------------------

result = df.groupby(
    ["department", "age"]
)["salary"].mean()
print(result)

# Groups by department AND age.


# ------------------------------------------------------------
# 11. AGGREGATION WITH agg()
# ------------------------------------------------------------

# Calculate multiple statistics at once.

result = df.groupby("department")["salary"].agg(
    ["sum", "mean", "min", "max", "count"]
)
print(result)

# Output:
#             sum     mean    min    max  count
# department
# HR       100000  50000.0  45000  55000      2
# IT       135000  67500.0  60000  75000      2
# Sales    115000  57500.0  50000  65000      2



# ------------------------------------------------------------
# 12. agg() ON MULTIPLE COLUMNS
# ------------------------------------------------------------

result = df.groupby("department").agg({
    "salary": ["mean", "max"],
    "age": ["min", "max"]
})
print(result)

# Salary:
# Average and maximum
#
# Age:
# Minimum and maximum


# ------------------------------------------------------------
# 13. NAMED AGGREGATION
# ------------------------------------------------------------

result = df.groupby("department").agg(
    average_salary=("salary", "mean"),
    highest_salary=("salary", "max"),
    employee_count=("name", "count"),
    average_age=("age", "mean")
)
print(result)

# Creates readable output column names.


# ------------------------------------------------------------
# 14. RESET INDEX AFTER GROUPBY
# ------------------------------------------------------------

result = df.groupby("department")["salary"].mean().reset_index()
print(result)

# Department becomes a normal column again.


# ------------------------------------------------------------
# 15. SORT GROUP RESULTS    
# ------------------------------------------------------------

result = (
    df.groupby("department")["salary"]
    .mean()
    .sort_values(ascending=False)
)
print(result)

# Highest average salary department first.


# ------------------------------------------------------------
# 16. GROUPBY WITH FILTERING
# ------------------------------------------------------------

# First select employees earning above 50000.
# Then calculate average salary by department.

result = (
    df[df["salary"] > 50000]
    .groupby("department")["salary"]
    .mean()
)
print(result)


# ------------------------------------------------------------
# 17. GROUPBY WITH VALUE COUNTS
# ------------------------------------------------------------

result = df["department"].value_counts()
print(result)

# Counts the number of rows for each department.
# Useful for understanding category distribution.


# ------------------------------------------------------------
# 18. REAL-WORLD EXAMPLE: SALES
# ------------------------------------------------------------

sales = pd.DataFrame({
    "product": ["Laptop", "Phone", "Laptop", "Phone", "Tablet"],
    "region": ["South", "North", "North", "South", "South"],
    "revenue": [80000, 40000, 90000, 50000, 30000]
})

# Total revenue by product.

result = sales.groupby("product")["revenue"].sum()
print(result)

# Total revenue by region.

result = sales.groupby("region")["revenue"].sum()
print(result)

# Average revenue by product.

result = sales.groupby("product")["revenue"].mean()
print(result)


# ------------------------------------------------------------
# 19. COMPLETE ML-STYLE DATA ANALYSIS
# ------------------------------------------------------------

employees = pd.DataFrame({
    "department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "salary": [60000, 45000, 75000, 50000, 55000, 65000],
    "experience": [2, 1, 4, 2, 3, 5]
})

summary = employees.groupby("department").agg(
    average_salary=("salary", "mean"),
    median_salary=("salary", "median"),
    total_salary=("salary", "sum"),
    employee_count=("salary", "count"),
    average_experience=("experience", "mean")
)
print(summary)

# This produces a department-wise summary
# using multiple numerical features.


# ------------------------------------------------------------
# MOST IMPORTANT PATTERNS
# ------------------------------------------------------------

# Average salary:
# df.groupby("department")["salary"].mean()

# Total salary:
# df.groupby("department")["salary"].sum()

# Median:
# df.groupby("department")["salary"].median()

# Minimum:
# df.groupby("department")["salary"].min()

# Maximum:
# df.groupby("department")["salary"].max()

# Count non-missing values:
# df.groupby("department")["salary"].count()

# Count rows:
# df.groupby("department").size()

# Multiple statistics:
# df.groupby("department")["salary"].agg(
#     ["sum", "mean", "min", "max"]
# )

# Multiple columns:
# df.groupby("department").agg({
#     "salary": "mean",
#     "age": "max"
# })

# Named aggregation:
# df.groupby("department").agg(
#     average_salary=("salary", "mean"),
#     highest_salary=("salary", "max")
# )

# Convert group index to column:
# df.groupby("department")["salary"].mean().reset_index()


"""
Understand the most important difference
Function || What it calculates
sum() - Total
mean() - Average
median() - Middle value
min() - Lowest
max() - Highest
count() - Non-missing values
size() - Total rows
agg() - Multiple calculations together
"""