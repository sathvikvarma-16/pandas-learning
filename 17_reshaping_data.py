# Reshaping data 
# This phase teaches you how to change the structure of a DataFrame without changing the meaning of its data.

# Pandas Phase 17: Reshaping Data

import pandas as pd

# ==================================================
# 1. UNDERSTANDING DATA RESHAPING
# ==================================================

# Reshaping means changing the structure of data.
# Example:
# Wide format:
# name    Math    Science    English
# A       90      85         80
# B       75      88         92

# Long format:
# name    subject    marks
# A       Math       90
# A       Science    85
# A       English    80
# B       Math       75
# B       Science    88
# B       English    92

# Wide -> Long = melt()
# Long -> Wide = pivot() / pivot_table()


# ==================================================
# 2. CREATE A WIDE DATAFRAME
# ==================================================

students = pd.DataFrame({
"student": ["A", "B", "C"],
"Math": [90, 75, 88],
"Science": [85, 88, 92],
"English": [80, 92, 78]
})

print("WIDE DATAFRAME:")
print(students)

# Each subject is stored in a separate column.

# ==================================================
# 3. melt()
# ==================================================

# melt() converts wide data into long data.
# id_vars:
# Columns that should remain unchanged.
# value_vars:
# Columns that should be converted into rows.
# var_name:
# Name of the new column containing old column names.
# value_name:
# Name of the new column containing values.

long_data = pd.melt(
students,
id_vars=["student"],
value_vars=["Math", "Science", "English"],
var_name="subject",
value_name="marks"
)

print("\nWIDE TO LONG USING melt():")
print(long_data)

# ==================================================
# 4. melt() WITHOUT value_vars
# ==================================================

# If value_vars is omitted,
# all columns except id_vars are melted.

long_data2 = pd.melt(
students,
id_vars=["student"],
var_name="subject",
value_name="marks"
)

print("\nMELT WITHOUT value_vars:")
print(long_data2)

# ==================================================
# 5. melt() WITH MULTIPLE ID COLUMNS
# ==================================================

students2 = pd.DataFrame({
"student_id": [101, 102, 103],
"name": ["Sathvik", "Rahul", "Priya"],
"department": ["CSE", "ECE", "CSE"],
"Math": [90, 75, 88],
"Science": [85, 88, 92]
})

long_data3 = pd.melt(
students2,
id_vars=["student_id", "name", "department"],
var_name="subject",
value_name="marks"
)
print("\nMELT WITH MULTIPLE ID COLUMNS:")
print(long_data3)

# ==================================================
# 6. pivot()
# ==================================================

# pivot() converts long data into wide data.
# index: Which column should identify rows?
# columns: Which column should become new columns?
# values: Which column should fill the cells?

wide_data = long_data.pivot(
index="student",
columns="subject",
values="marks"
)
print("\nLONG TO WIDE USING pivot():")
print(wide_data)

# ==================================================
# 7. RESET INDEX AFTER PIVOT
# ==================================================

# pivot() uses the selected index column
# as the resulting DataFrame index.
# reset_index() converts it back into a normal column.

wide_data = wide_data.reset_index()
print("\nPIVOT WITH RESET INDEX:")
print(wide_data)

# ==================================================
# 8. pivot() WITH MULTIPLE VALUE COLUMNS
# ==================================================

data = pd.DataFrame({
"student": ["A", "A", "B", "B"],
"subject": ["Math", "Science", "Math", "Science"],
"marks": [90, 85, 75, 88],
"attendance": [95, 90, 85, 92]
})

result = data.pivot(
index="student",
columns="subject",
values=["marks", "attendance"]
)
print("\nPIVOT WITH MULTIPLE VALUE COLUMNS:")
print(result)

# ==================================================
# 9. IMPORTANT: pivot() AND DUPLICATES
# ==================================================

# pivot() requires each combination of
# index + columns to be unique.
# If repeated combinations exist,
# pivot() raises a ValueError.

duplicate_data = pd.DataFrame({
"student": ["A", "A", "A", "B"],
"subject": ["Math", "Math", "Science", "Math"],
"marks": [90, 95, 85, 75]
})

# Do not run this directly because it raises an error:
# duplicate_data.pivot(
# index="student",
# columns="subject",
# values="marks"
# )

#
# Use pivot_table() when duplicate combinations
# need to be aggregated.

# ==================================================
# 10. pivot_table()
# ==================================================

# pivot_table() is similar to pivot(),
# but it can aggregate duplicate values.
# aggfunc specifies the calculation.
# Default aggregation is mean.

result = pd.pivot_table(
duplicate_data,
index="student",
columns="subject",
values="marks",
aggfunc="mean"
)

print("\nPIVOT TABLE WITH MEAN:")
print(result)

# Student A has two Math marks:
# 90 and 95
# Mean = 92.5

# ==================================================
# 11. pivot_table() WITH SUM
# ==================================================

sales = pd.DataFrame({
"employee": ["A", "A", "A", "B", "B", "B"],
"month": ["Jan", "Jan", "Feb", "Jan", "Feb", "Feb"],
"sales": [1000, 500, 2000, 1500, 1200, 800]
})

result = pd.pivot_table(
sales,
index="employee",
columns="month",
values="sales",
aggfunc="sum"
)

print("\nPIVOT TABLE WITH SUM:")
print(result)

# Employee A January sales:
# 1000 + 500 = 1500

# ==================================================
# 12. pivot_table() WITH DIFFERENT AGGREGATIONS
# ==================================================

# mean
mean_table = pd.pivot_table(
sales,
index="employee",
columns="month",
values="sales",
aggfunc="mean"
)
print("\nMEAN TABLE:")
print(mean_table)

# sum

sum_table = pd.pivot_table(
sales,
index="employee",
columns="month",
values="sales",
aggfunc="sum"
)
print("\nSUM TABLE:")
print(sum_table)

# count

count_table = pd.pivot_table(
sales,
index="employee",
columns="month",
values="sales",
aggfunc="count"
)
print("\nCOUNT TABLE:")
print(count_table)

# ==================================================
# 13. pivot_table() WITH MULTIPLE AGGREGATIONS
# ==================================================

result = pd.pivot_table(
sales,
index="employee",
columns="month",
values="sales",
aggfunc=["sum", "mean", "max"]
)
print("\nMULTIPLE AGGREGATIONS:")
print(result)

# ==================================================
# 14. pivot_table() WITH MULTIPLE INDEXES
# ==================================================

data = pd.DataFrame({
"department": ["CSE", "CSE", "ECE", "ECE", "CSE"],
"year": [1, 2, 1, 2, 1],
"gender": ["M", "F", "M", "F", "F"],
"marks": [90, 85, 80, 88, 95]
})
result = pd.pivot_table(
data,
index=["department", "year"],
columns="gender",
values="marks",
aggfunc="mean"
)
print("\nMULTIPLE INDEXES:")
print(result)

# ==================================================
# 15. pivot_table() WITH fill_value
# ==================================================

# Missing combinations normally show NaN.
# fill_value replaces missing output cells.

result = pd.pivot_table(
sales,
index="employee",
columns="month",
values="sales",
aggfunc="sum",
fill_value=0
)
print("\nPIVOT TABLE WITH fill_value=0:")
print(result)

# ==================================================
# 16. pivot_table() WITH margins
# ==================================================

# margins=True adds total rows and columns.
# Useful for summary reports.

result = pd.pivot_table(
sales,
index="employee",
columns="month",
values="sales",
aggfunc="sum",
fill_value=0,
margins=True
)

print("\nPIVOT TABLE WITH TOTALS:")
print(result)


# ==================================================
# 17. melt() AFTER PIVOT
# ==================================================

# We can convert wide data back into long format.

wide = pd.DataFrame({
"student": ["A", "B"],
"Math": [90, 75],
"Science": [85, 88]
})

long = wide.melt(
id_vars=["student"],
var_name="subject",
value_name="marks"
)
print("\nWIDE DATA:")
print(wide)

print("\nMELTED DATA:")
print(long)


# ==================================================
# 18. stack()
# ==================================================

# stack() moves column labels into an inner index.
# It converts a wide structure into a more vertically arranged structure.
wide = pd.DataFrame({
"Math": [90, 75],
"Science": [85, 88]
}, index=["A", "B"])
print("\nBEFORE STACK:")
print(wide)
stacked = wide.stack()
print("\nAFTER STACK:")
print(stacked)

# ==================================================
# 19. unstack()
# ==================================================

# unstack() moves an index level back into columns.
# It is commonly used to reverse stack().

unstacked = stacked.unstack()
print("\nAFTER UNSTACK:")
print(unstacked)


# ==================================================
# 20. stack() WITH NAMED INDEX
# ==================================================

data = pd.DataFrame({
"Math": [90, 75],
"Science": [85, 88]
}, index=pd.Index(["A", "B"], name="student"))
stacked = data.stack()
print("\nSTACKED WITH NAMED INDEX:")
print(stacked)

# Convert back into DataFrame

stacked_df = stacked.reset_index()
stacked_df.columns = ["student", "subject", "marks"]
print("\nSTACKED AS DATAFRAME:")
print(stacked_df)

# ==================================================
# 21. unstack() WITH MULTIINDEX
# ==================================================

data = pd.DataFrame({
"student": ["A", "A", "B", "B"],
"subject": ["Math", "Science", "Math", "Science"],
"marks": [90, 85, 75, 88]
})
# Create a MultiIndex using set_index()
indexed = data.set_index(["student", "subject"])
print("\nMULTIINDEX DATA:")
print(indexed)

# Move subject index level into columns
result = indexed.unstack()
print("\nAFTER UNSTACK:")
print(result)

# ==================================================
# 22. stack() VS unstack()
# ==================================================

# stack()
# Columns -> Inner index level
# Wide -> Long-like structure
# unstack()
# Inner index level -> Columns
# Long-like structure -> Wide

# ==================================================
# 23. PRACTICAL SALES DATASET
# ==================================================

# Imagine a company stores monthly sales
# in separate columns.

sales_wide = pd.DataFrame({
"product": ["Laptop", "Phone", "Tablet"],
"January": [50000, 30000, 20000],
"February": [55000, 35000, 25000],
"March": [60000, 40000, 30000]
})

print("\nSALES WIDE FORMAT:")
print(sales_wide)

# Convert to long format

sales_long = sales_wide.melt(
id_vars=["product"],
var_name="month",
value_name="sales"
)

print("\nSALES LONG FORMAT:")
print(sales_long)

# ==================================================
# 24. ANALYZE LONG DATA
# ==================================================

# Now we can easily group by product or month.

monthly_total = sales_long.groupby(
"month"
)["sales"].sum()

print("\nTOTAL SALES BY MONTH:")
print(monthly_total)

# Product total

product_total = sales_long.groupby(
"product"
)["sales"].sum()

print("\nTOTAL SALES BY PRODUCT:")
print(product_total)

# ==================================================
# 25. CONVERT LONG DATA BACK TO WIDE
# ==================================================

sales_wide_again = sales_long.pivot(
index="product",
columns="month",
values="sales"
)

print("\nCONVERTED BACK TO WIDE:")
print(sales_wide_again)

# ==================================================
# 26. PRACTICAL ML DATASET
# ==================================================

# Suppose a dataset contains marks for multiple subjects in wide format.
ml_wide = pd.DataFrame({
"student_id": [101, 102, 103],
"Math": [90, 75, 88],
"Science": [85, 88, 92],
"English": [80, 92, 78]
})

# Convert to long format

ml_long = ml_wide.melt(
id_vars=["student_id"],
var_name="subject",
value_name="marks"
)

print("\nML LONG DATASET:")
print(ml_long)

# Example: calculate average marks by subject

subject_average = ml_long.groupby(
"subject"
)["marks"].mean()

print("\nAVERAGE MARKS BY SUBJECT:")
print(subject_average)

# ==================================================
# 27. IMPORTANT DIFFERENCE
# ==================================================

# pivot()
# Reshapes data.
# Requires unique index + column combinations.
# Does not aggregate duplicates.

# pivot_table()
# Reshapes and aggregates.
# Handles repeated combinations.
# Supports mean, sum, count, max, min, etc.

# melt()
# Converts wide -> long.
# stack()
# Moves columns into an index level.

# unstack()
# Moves an index level into columns.

# ==================================================
# 28. FINAL QUICK REVISION
# ==================================================

# Wide -> Long
# df.melt(...)

# Long -> Wide
# df.pivot(...)

# Long -> Wide with aggregation
# pd.pivot_table(...)

# Columns -> Index
# df.stack()

# Index -> Columns
# df.unstack()

# The two most important patterns

# 1. melt()

df.melt(
    id_vars=["student"],
    var_name="subject",
    value_name="marks"
)


# 2. pivot_table()

pd.pivot_table(
    df,
    index="student",
    columns="subject",
    values="marks",
    aggfunc="mean"
)

# Important distinction
# pivot() expects unique combinations of index and column keys.
# pivot_table() can handle repeated combinations by aggregating them.
# melt() is particularly useful when datasets have separate columns for months, subjects, years, or measurements.

