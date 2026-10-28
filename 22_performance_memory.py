"""
This phase teaches you how to make Pandas code faster, more memory-efficient, and practical for larger datasets. 
For AI/ML Engineering, this matters when datasets grow from thousands of rows to millions of rows and 
you need to prepare data without wasting RAM or time.


1. What you must master

Concept                          |                           What you need to know
---------------------------------|-----------------------------------------------------------------------------------
Vectorization	                 |      Apply operations to entire columns instead of looping through individual rows
Avoiding unnecessary loops	     |      Prefer built-in Pandas/NumPy operations where appropriate
Efficient column operations	     |      Select only the columns and rows you need
memory_usage()	                 |      Measure memory used by columns
Data types	                     |      Use appropriate types to avoid unnecessary memory use
category dtype	                 |      Efficiently represent columns with a small set of repeated values
usecols	                         |      Read only required columns from a file
chunksize	                     |      Process a large CSV in batches

"""

# PHASE 22: PERFORMANCE AND MEMORY IN PANDAS

import pandas as pd
import numpy as np

# --------------------------------------------------
# 1. CREATE A SAMPLE DATASET
# --------------------------------------------------

df = pd.DataFrame({
    "employee_id": range(1, 10001),
    "age": np.random.default_rng(42).integers(20, 60, 10000),
    "salary": np.random.default_rng(43).integers(25000, 100000, 10000),
    "department": np.random.default_rng(44).choice(
        ["IT", "HR", "Finance", "Sales"],
        size=10000
    ),
    "city": np.random.default_rng(45).choice(
        ["Vizag", "Chennai", "Hyderabad"],
        size=10000
    )
})

print(df.head())
print("Shape:", df.shape)


# --------------------------------------------------
# 2. VECTORIZE COLUMN OPERATIONS
# --------------------------------------------------

# Inefficient style: loop through individual rows.
# This creates a Python-level operation for each row.

bonus_loop = []

for salary in df["salary"]:
    bonus_loop.append(salary * 0.10)

# Preferred: operate on the entire column.
df["bonus"] = df["salary"] * 0.10

print(df[["salary", "bonus"]].head())

# Another vectorized operation.
df["salary_with_bonus"] = df["salary"] + df["bonus"]

# Conditional values with np.where.
df["salary_level"] = np.where(
    df["salary"] >= 60000,
    "High",
    "Standard"
)

print(df[["salary", "salary_level"]].head())


# --------------------------------------------------
# 3. AVOID UNNECESSARY ROW-WISE LOOPS
# --------------------------------------------------

# Avoid this when a direct column operation exists:
# for index, row in df.iterrows():
#     df.loc[index, "bonus"] = row["salary"] * 0.10

# Use vectorized operations instead:
df["bonus_check"] = df["salary"] * 0.10

# Use np.select when there are several conditions.
conditions = [
    df["salary"] < 40000,
    df["salary"].between(40000, 69999),
    df["salary"] >= 70000
]

choices = ["Low", "Medium", "High"]

df["salary_band"] = np.select(
    conditions,
    choices,
    default="Unknown"
)

print(df[["salary", "salary_band"]].head())


# --------------------------------------------------
# 4. EFFICIENT COLUMN SELECTION
# --------------------------------------------------

# Avoid carrying every column through a workflow
# when only a few are needed.

selected = df[["age", "salary", "department"]]

print(selected.head())

# Filter rows before performing expensive analysis
# when the filter is valid for the task.
high_salary = df.loc[
    df["salary"] >= 70000,
    ["employee_id", "salary", "department"]
]

print(high_salary.head())

# Do not create unnecessary copies of large DataFrames.
# Use .copy() when you need an independent working copy.
working_df = selected.copy()


# --------------------------------------------------
# 5. MEASURE MEMORY USAGE
# --------------------------------------------------

# Memory usage for each column.
print(df.memory_usage())

# Include the DataFrame index.
print(df.memory_usage(index=True))

# Include memory used by objects stored in columns.
memory_by_column = df.memory_usage(deep=True).sort_values(
    ascending=False
)

print(memory_by_column)

# Total approximate memory in megabytes.
total_bytes = df.memory_usage(deep=True).sum()
total_mb = total_bytes / (1024 ** 2)

print("Approximate DataFrame memory (MB):", round(total_mb, 3))

# Memory measurements can vary by data types and platform.


# --------------------------------------------------
# 6. INSPECT DATA TYPES
# --------------------------------------------------

print(df.dtypes)

# Integer types may use different amounts of memory.
print("Salary dtype:", df["salary"].dtype)

# Use appropriate data types for the values.
# Do not choose a small integer type if values may overflow.

# Example: downcast integer values where safe.
salary_compact = pd.to_numeric(
    df["salary"],
    downcast="integer"
)

print("Original dtype:", df["salary"].dtype)
print("Downcast dtype:", salary_compact.dtype)

# Downcasting can save memory, but check the resulting
# range and accuracy before using it in a real workflow.


# --------------------------------------------------
# 7. CATEGORY DTYPE
# --------------------------------------------------

# Department and city repeat many values.
# Category dtype can reduce memory for low-cardinality text.

before_category = df.memory_usage(deep=True).sum()

df["department"] = df["department"].astype("category")
df["city"] = df["city"].astype("category")

after_category = df.memory_usage(deep=True).sum()

print("Memory before category:", before_category)
print("Memory after category:", after_category)

print(df[["department", "city"]].dtypes)

# Category is most useful when a column has relatively few unique values compared with its number of rows.
# It may not save memory for mostly unique text columns.

# Check the number of distinct values.
print("Department unique:", df["department"].nunique())
print("City unique:", df["city"].nunique())


# --------------------------------------------------
# 8. READ ONLY REQUIRED CSV COLUMNS WITH usecols
# --------------------------------------------------

# Save sample data so this lesson runs independently.
df.to_csv("employees_sample.csv", index=False)


# Read only the columns needed for a task.
small_df = pd.read_csv(
    "employees_sample.csv",
    usecols=["age", "salary", "department"]
)

print(small_df.head())
print("Selected columns:", small_df.columns.tolist())

# Reading fewer columns reduces the amount of data loaded.


# --------------------------------------------------
# 9. OPTIMIZE TYPES WHILE READING
# --------------------------------------------------

optimized_df = pd.read_csv(
    "employees_sample.csv",
    usecols=["employee_id", "age", "salary", "department"],
    dtype={
        "employee_id": "int32",
        "age": "int8",
        "department": "category"
    }
)

print(optimized_df.dtypes)
print(optimized_df.head())

# Use explicit dtypes only when they can represent all expected values. Verify the source data first.


# --------------------------------------------------
# 10. PROCESS A LARGE CSV IN CHUNKS
# --------------------------------------------------

# chunksize returns an iterator of DataFrame batches.
# This avoids loading the entire CSV into memory at once.

total_rows = 0
salary_sum = 0

for chunk in pd.read_csv(
    "employees_sample.csv",
    usecols=["salary"],
    chunksize=1000
):
    total_rows += len(chunk)
    salary_sum += chunk["salary"].sum()

print("Rows processed:", total_rows)
print("Total salary:", salary_sum)
print("Average salary:", salary_sum / total_rows)


# --------------------------------------------------
# 11. CHUNK-WISE FILTERING
# --------------------------------------------------

high_salary_count = 0

for chunk in pd.read_csv(
    "employees_sample.csv",
    usecols=["salary", "department"],
    chunksize=1000
):
    filtered_chunk = chunk[chunk["salary"] >= 70000]
    high_salary_count += len(filtered_chunk)

print("Employees with salary >= 70000:", high_salary_count)


# --------------------------------------------------
# 12. CHUNK-WISE GROUP ANALYSIS
# --------------------------------------------------

# Accumulate partial sums and counts by department.
# Combine partial results before calculating the mean.

salary_sums = {}
salary_counts = {}

for chunk in pd.read_csv(
    "employees_sample.csv",
    usecols=["department", "salary"],
    chunksize=1000
):
    grouped = chunk.groupby("department", observed=True)["salary"].agg(
        ["sum", "count"]
    )

    for department, row in grouped.iterrows():
        salary_sums[department] = (
            salary_sums.get(department, 0) + row["sum"]
        )

        salary_counts[department] = (
            salary_counts.get(department, 0) + row["count"]
        )

average_salary_by_department = {
    department: salary_sums[department] / salary_counts[department]
    for department in salary_sums
}

print("Average salary by department:")
print(average_salary_by_department)


# --------------------------------------------------
# 13. WHEN CHUNKING IS NOT ENOUGH
# --------------------------------------------------

# Chunking works well for operations that can be calculated batch by batch, such as sums and counts.

# Exact medians, global sorting, and some complex joins may need additional algorithms or more memory.

# For those tasks, consider:
# - efficient filtering and column selection
# - carefully designed aggregation
# - a database or out-of-core processing tool
#
# Do not assume every operation can be done independently
# on chunks and combined afterward.


# --------------------------------------------------
# 14. FINAL MEMORY CHECK
# --------------------------------------------------

print("Final dtypes:")
print(df.dtypes)

print("Final memory usage by column:")
print(df.memory_usage(deep=True).sort_values(ascending=False))

print(
    "Final DataFrame memory (MB):",
    round(df.memory_usage(deep=True).sum() / (1024 ** 2), 3)
)

