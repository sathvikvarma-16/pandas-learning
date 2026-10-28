"""
This is the advanced Pandas stage. The goal is to write cleaner, more efficient data transformations 
and handle complex datasets confidently — especially for EDA, time-series analysis, and machine learning.

You do not need to memorize every method. Focus on understanding when to use each technique, 
how it works, and how to verify its output.
"""


"""
What you will master
------------------------------------------------------------------------------------------------------------
Section	|      Topic                  |         	       Why it matters
--------|-----------------------------|---------------------------------------------------------------------
1	    |   MultiIndex	              |      Work with hierarchical rows and columns
2	    |   Advanced groupby()	      |      Calculate multiple metrics and group-level insights
3	    |   Advanced merge()	      |          Join datasets safely and validate relationships
4	    |   Advanced pivot_table()	  |      Summarize data across multiple dimensions
5	    |   Rolling operations	      |      Calculate moving averages and recent trends
6	    |   Expanding operations	  |          Calculate cumulative statistics over all observations so far
7	    |   Window operations	      |      Apply calculations over defined ranges of observations
8	    |   Categoricals	          |         Store repeated labels efficiently and control category order
9	    |   Method chaining	          |     Build readable, step-by-step transformations
10	    |   pipe() and query()	      |     Reuse custom logic and express filters cleanly
11	    |   Efficient transformations |	    Reduce unnecessary loops, copies, and repeated work
------------------------------------------------------------------------------------------------------------
"""



import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 140)

# --------------------------------------------------
# 1. SAMPLE DATA
# --------------------------------------------------

df = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["Asha", "Rahul", "Priya", "Kiran", "Asha", "Rahul", "Priya", "Kiran"],
    "department": ["IT", "HR", "IT", "Sales", "HR", "IT", "Sales", "IT"],
    "city": ["Vizag", "Chennai", "Vizag", "Hyderabad", "Chennai", "Vizag", "Hyderabad", "Chennai"],
    "experience": [2, 5, 3, 7, 4, 6, 2, 8],
    "salary": [35000, 50000, 42000, 65000, 47000, 72000, 39000, 85000],
    "performance": [3.5, 4.2, 4.0, 4.5, 3.8, 4.7, 3.6, 4.8]
})

print("\nOriginal data:")
print(df)


# --------------------------------------------------
# 2. MULTIINDEX
# --------------------------------------------------

# A MultiIndex uses more than one level to identify rows.
# set_index() moves columns into the row index.

multi_df = df.set_index(["department", "employee_id"]).sort_index()

print("\nMultiIndex DataFrame:")
print(multi_df)

# Select all rows belonging to the IT department.
print("\nAll IT employees:")
print(multi_df.loc["IT"])

# Select a specific department and employee.
print("\nEmployee 106 in IT:")
print(multi_df.loc[("IT", 106)])

# Convert the index levels back into ordinary columns.
print("\nReset MultiIndex:")
print(multi_df.reset_index())

# MultiIndex is useful for hierarchical analysis,
# but ordinary columns are often simpler for ML preprocessing.


# --------------------------------------------------
# 3. ADVANCED GROUPBY
# --------------------------------------------------

# Multiple aggregation functions for multiple columns.

group_summary = df.groupby("department").agg(
    employee_count=("employee_id", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max"),
    average_experience=("experience", "mean"),
    average_performance=("performance", "mean")
)

print("\nDepartment summary:")
print(group_summary.round(2))

# Group by more than one column.
city_summary = df.groupby(["department", "city"]).agg(
    employee_count=("employee_id", "size"),
    average_salary=("salary", "mean")
)

print("\nDepartment and city summary:")
print(city_summary.round(2))

# transform() returns a result aligned with the original rows.
# Each employee gets their department's average salary.

df["department_avg_salary"] = (
    df.groupby("department 9")["salary"].transform("mean")
)

# Compare each employee's salary with their department average.
df["salary_vs_department_avg"] = (
    df["salary"] - df["department_avg_salary"]
)

print("\nSalary compared with department average:")
print(df[[
    "name",
    "department",
    "salary",
    "department_avg_salary",
    "salary_vs_department_avg"
]].round(2))

# filter() keeps or removes entire groups based on a condition.
# Keep only departments with at least two employees.

large_departments = df.groupby("department").filter(
    lambda group: len(group) >= 2
)

print("\nEmployees in departments with at least two employees:")
print(large_departments[["name", "department", "salary"]])

# Use observed=True when grouping categorical columns
# if you want only category combinations present in the data.


# --------------------------------------------------
# 4. ADVANCED MERGE
# --------------------------------------------------

# Create a separate department lookup table.

department_info = pd.DataFrame({
    "department": ["IT", "HR", "Sales"],
    "manager": ["Meera", "Arun", "Divya"],
    "budget": [500000, 250000, 400000]
})

# Many employee rows can match one department row.
# validate="many_to_one" checks that the right-side key is unique.

merged_df = df.merge(
    department_info,
    on="department",
    how="left",
    validate="many_to_one",
    indicator=True
)

print("\nEmployees with department information:")
print(merged_df[[
    "name", "department", "manager", "budget", "_merge"
]])

# indicator=True labels whether a row matched:
# both, left_only, or right_only.

# Find unmatched employee department values.
unmatched = merged_df.loc[
    merged_df["_merge"] == "left_only"
]

print("\nUnmatched employees:")
print(unmatched[["name", "department"]])

# Merge using different key names.

employee_codes = pd.DataFrame({
    "dept_code": ["IT", "HR", "Sales"],
    "location": ["Block A", "Block B", "Block C"]
})

code_merged = department_info.merge(
    employee_codes,
    left_on="department",
    right_on="dept_code",
    how="left",
    validate="one_to_one"
)

print("\nMerge using different key names:")
print(code_merged)


# --------------------------------------------------
# 5. ADVANCED PIVOT_TABLE
# --------------------------------------------------

# Summarize salary by department and city.
# Multiple aggregation functions can be used.

pivot = pd.pivot_table(
    df,
    index="department",
    columns="city",
    values="salary",
    aggfunc=["mean", "count"],
    fill_value=0,
    observed=True
)

print("\nPivot table with multiple aggregations:")
print(pivot.round(2))

# Multiple values and row dimensions.
pivot2 = pd.pivot_table(
    df,
    index=["department", "city"],
    values=["salary", "performance"],
    aggfunc={
        "salary": ["mean", "max"],
        "performance": "mean"
    },
    observed=True
)

print("\nPivot table with multiple row levels and values:")
print(pivot2.round(2))

# margins=True adds overall totals or aggregates.
salary_totals = pd.pivot_table(
    df,
    index="department",
    values="salary",
    aggfunc="mean",
    margins=True,
    margins_name="Overall Average",
    observed=True
)

print("\nDepartment and overall average salary:")
print(salary_totals.round(2))


# --------------------------------------------------
# 6. ROLLING OPERATIONS
# --------------------------------------------------

# Rolling calculations use a moving window.
# Sort observations in their actual time order first.

monthly = pd.DataFrame({
    "month": pd.date_range("2026-01-01", periods=8, freq="MS"),
    "sales": [100, 120, 90, 150, 170, 160, 200, 220]
})

monthly = monthly.sort_values("month")

# Average of the current month and previous two months.
monthly["rolling_3_month_avg"] = (
    monthly["sales"].rolling(window=3, min_periods=1).mean()
)

# Rolling maximum over the last three observations.
monthly["rolling_3_month_max"] = (
    monthly["sales"].rolling(window=3, min_periods=1).max()
)

print("\nRolling calculations:")
print(monthly.round(2))

# min_periods=1 allows results before the window is full.
# Without it, a 3-row window starts with two NaN results.


# --------------------------------------------------
# 7. EXPANDING OPERATIONS
# -------------------------------------------------- 

# Expanding calculations use every observation from the beginning up to the current row.

monthly["cumulative_avg_sales"] = (
    monthly["sales"].expanding(min_periods=1).mean()
)

monthly["cumulative_max_sales"] = (
    monthly["sales"].expanding(min_periods=1).max()
)

print("\nExpanding calculations:")
print(monthly.round(2))

# Rolling window=3:
# January-February-March, then February-March-April, etc.
#
# Expanding:
# January; January-February; January-February-March; etc.


# --------------------------------------------------
# 8. WINDOW OPERATIONS
# --------------------------------------------------

# shift() moves values between rows.
# diff() calculates the difference from the previous row.
# pct_change() calculates the fractional change from the previous row.

monthly["previous_month_sales"] = monthly["sales"].shift(1)

monthly["sales_change"] = monthly["sales"].diff()

monthly["sales_fractional_change"] = monthly["sales"].pct_change()

# Convert fractional change to percentage.
monthly["sales_change_percent"] = (
    monthly["sales"].pct_change() * 100
)

print("\nShift, difference, and percentage change:")
print(monthly.round(2))

# Centered rolling windows include observations on both sides of the current row.
monthly["centered_3_month_avg"] = (
    monthly["sales"].rolling(window=3, center=True).mean()
)

print("\nCentered rolling average:")
print(monthly[["month", "sales", "centered_3_month_avg"]].round(2))

# IMPORTANT:
# Centered windows and future information can cause data leakage
# if used carelessly to predict future outcomes.


# --------------------------------------------------
# 9. CATEGORICAL DATA
# --------------------------------------------------

# Convert repeated text values into a categorical dtype.

category_df = df[["name", "department", "city", "salary"]].copy()

category_df["department"] = category_df["department"].astype("category")
category_df["city"] = category_df["city"].astype("category")

print("\nCategorical data types:")
print(category_df.dtypes)

print("\nDepartment categories:")
print(category_df["department"].cat.categories)

# Define an explicit order for performance levels.

performance_levels = ["Needs Improvement", "Good", "Excellent"]

performance_data = pd.DataFrame(  {
    "employee": ["Asha", "Rahul", "Priya", "Kiran"],
    "performance_level": ["Good", "Excellent", "Good", "Needs Improvement"]
})

performance_data["performance_level"] = pd.Categorical(
    performance_data["performance_level"],
    categories=performance_levels,
    ordered=True
)

# Ordered categoricals follow the specified business order.
print("\nOrdered categorical values:")
print(performance_data.sort_values("performance_level"))

# Category dtype is most useful when values repeat frequently.
# High-cardinality text columns may not save memory.


# --------------------------------------------------
# 10. METHOD CHAINING
# --------------------------------------------------

# Method chaining connects operations into one readable workflow.
# Use parentheses to format each step on a separate line.

high_earners = (
    df
    .loc[:, ["name", "department", "city", "salary", "experience"]]
    .query("salary >= 45000 and experience >= 4")
    .assign(
        salary_in_lakhs=lambda data: data["salary"] / 100000,
        experience_group=lambda data: np.where(
            data["experience"] >= 6,
            "Experienced",
            "Developing"
        )
    )
    .sort_values("salary", ascending=False)
    .reset_index(drop=True)
)

print("\nHigh earners using method chaining:")
print(high_earners.round(3))

# Benefits:
# - Operations appear in the order they happen.
# - Intermediate variables are reduced.
# - The workflow is easier to review.
#
# Avoid making a chain so long that it becomes hard to debug.


# --------------------------------------------------
# 11. query()
# --------------------------------------------------

# query() filters rows using a readable expression.

experienced = df.query("experience >= 5")

print("\nEmployees with at least five years of experience:")
print(experienced[["name", "experience", "salary"]])

# Combine conditions with and/or inside query().
it_high_earners = df.query(
    "department == 'IT' and salary > 40000"
)

print("\nIT employees earning above 40000:")
print(it_high_earners[["name", "salary"]])

# Use @ to refer to a Python variable.
minimum_salary = 45000

filtered = df.query("salary >= @minimum_salary")

print("\nEmployees meeting the variable threshold:")
print(filtered[["name", "salary"]])

# For complex conditions, unusual column names,
# or complicated logic, normal boolean indexing is also fine.


# --------------------------------------------------
# 12. pipe()
# --------------------------------------------------

# pipe() passes a DataFrame into a custom function.
# It helps turn repeated cleaning logic into reusable steps.

def keep_valid_salaries(data):
    return data.loc[data["salary"].between(20000, 150000)].copy()


def add_salary_band(data):
    result = data.copy()

    result["salary_band"] = pd.cut(
        result["salary"],
        bins=[0, 40000, 60000, float("inf")],
        labels=["Low", "Medium", "High"]
    )

    return result


def add_experience_group(data):
    result = data.copy()

    result["experience_group"] = np.where(
        result["experience"] >= 5,
        "Experienced",
        "Early Career"
    )

    return result


processed = (
    df
    .pipe(keep_valid_salaries)
    .pipe(add_salary_band)
    .pipe(add_experience_group)
)

print("\nReusable transformations with pipe():")
print(processed[[
    "name", "salary", "salary_band",
    "experience", "experience_group"
]])

# Each function accepts a DataFrame and returns a DataFrame.
# This makes individual steps easier to test and reuse.


# --------------------------------------------------
# 13. EFFICIENT TRANSFORMATIONS
# --------------------------------------------------

# Prefer vectorized operations instead of row-by-row loops.

# Less efficient style:
# for index, row in df.iterrows():
#     print(row["salary"] * 12)

# Vectorized alternative:
df["annual_salary"] = df["salary"] * 12

# Use np.select() for multiple conditional rules.
conditions = [
    df["salary"] >= 70000,
    df["salary"] >= 45000
]

choices = ["High", "Medium"]

df["salary_level"] = np.select(
    conditions,
    choices,
    default="Low"
)

# Use transform() when the result must align with each original row.
df["department_median_salary"] = (
    df.groupby("department")["salary"].transform("median")
)

print("\nEfficient vectorized transformations:")
print(df[[
    "name",
    "salary",
    "annual_salary",
    "salary_level",
    "department_median_salary"
]])

# Select only the columns needed for a task.
model_columns = df[[
    "experience",
    "performance",
    "salary"
]].copy()

print("\nSelected model columns:")
print(model_columns.head())

# Avoid repeated expensive operations.
# Calculate once and reuse the result when appropriate.
department_means = df.groupby("department")["salary"].mean()

df["department_mean_reused"] = df["department"].map(department_means)

print("\nMapped department means:")
print(df[["department", "salary", "department_mean_reused"]].head())


# --------------------------------------------------
# 14. FINAL VALIDATION
# --------------------------------------------------

print("\nFinal shape:", df.shape)
print("\nMissing values:")
print(df.isna().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nFinal preview:")
print(df.head())

print("\nPHASE 23 COMPLETED")
