# Pandas Phase 18: Duplicates & Data Validation

'''
This phase is especially important for ML Engineering. Before training a model, you must verify whether the dataset is reliable.
For example:
Does every customer have a valid ID?
Are there duplicate records?
Are ages within a valid range?
Are required columns present?
Are there unexpected categories?
Do related columns agree with each other?
'''

# Pandas Phase 18: Duplicates & Data Validation

import pandas as pd

# ==================================================
# 1. CREATE A SAMPLE DATASET
# ==================================================

data = {
"customer_id": [101, 102, 103, 103, 104, 105, 105],
"name": ["Sathvik", "Rahul", "Priya", "Priya", "Anil", "Sneha", "Sneha"],
"age": [20, 22, 25, 25, 150, 21, 21],
"city": ["Vizag", "Hyderabad", "Chennai", "Chennai", "Delhi", "Vizag", "Vizag"],
"salary": [30000, 40000, 50000, 50000, 60000, -5000, -5000]
}
df = pd.DataFrame(data)
print("ORIGINAL DATASET:")
print(df)

# ==================================================
# 2. duplicated()
# ==================================================

# duplicated() identifies duplicate rows.

# It returns:
# True  -> duplicate
# False -> not duplicate

print("\nDUPLICATED ROWS:")
print(df.duplicated())

# ==================================================
# 3. COUNT DUPLICATE ROWS
# ==================================================

duplicate_count = df.duplicated().sum()
print("\nNUMBER OF DUPLICATE ROWS:")
print(duplicate_count)

# ==================================================
# 4. DISPLAY DUPLICATE ROWS
# ==================================================

duplicates = df[df.duplicated()]
print("\nDUPLICATE RECORDS:")
print(duplicates)

# ==================================================
# 5. duplicated(keep="first")
# ==================================================

# By default, keep="first".

# The first occurrence is marked False.
# Later repeated occurrences are marked True.

print("\nKEEP FIRST:")
print(df.duplicated(keep="first"))

# ==================================================
# 6. duplicated(keep="last")
# ==================================================

# The last occurrence is preserved.
# Earlier repeated occurrences are marked True.

print("\nKEEP LAST:")
print(df.duplicated(keep="last"))

# ==================================================
# 7. duplicated(keep=False)
# ==================================================

# Marks ALL occurrences of duplicate rows as True.

print("\nMARK ALL DUPLICATES:")
print(df.duplicated(keep=False))
all_duplicates = df[df.duplicated(keep=False)]
print("\nALL DUPLICATE RECORDS:")
print(all_duplicates)

# ==================================================
# 8. DROP DUPLICATES
# ==================================================

# drop_duplicates() removes duplicate rows.
# It keeps the first occurrence by default.

clean_df = df.drop_duplicates()
print("\nAFTER DROP DUPLICATES:")
print(clean_df)

# ==================================================
# 9. drop_duplicates(keep="last")
# ==================================================

clean_last = df.drop_duplicates(keep="last")
print("\nKEEP LAST OCCURRENCE:")
print(clean_last)

# ==================================================
# 10. drop_duplicates(keep=False)
# ==================================================

# Removes every row belonging to a duplicate group.

clean_unique = df.drop_duplicates(keep=False)
print("\nREMOVE ALL DUPLICATE GROUPS:")
print(clean_unique)


# ==================================================
# 11. DUPLICATES BASED ON ONE COLUMN
# ==================================================

# Sometimes entire rows are different, but an ID is repeated.

print("\nDUPLICATE CUSTOMER IDS:")
print(df["customer_id"].duplicated())

# Display rows with repeated IDs

duplicate_ids = df[
df["customer_id"].duplicated(keep=False)
]

print("\nROWS WITH DUPLICATE CUSTOMER IDS:")
print(duplicate_ids)

# ==================================================
# 12. DROP DUPLICATES BASED ON ID
# ==================================================

# Keep one row per customer_id.

unique_customers = df.drop_duplicates(
subset=["customer_id"],
keep="first"
)

print("\nUNIQUE CUSTOMER IDS:")
print(unique_customers)

# IMPORTANT:
# Do not blindly drop duplicate IDs.
# A customer may legitimately have multiple transactions.
# First decide what one row represents.

# ==================================================
# 13. DUPLICATES BASED ON MULTIPLE COLUMNS
# ==================================================

orders = pd.DataFrame({
"customer_id": [101, 101, 102, 102, 103],
"product": ["Laptop", "Laptop", "Mouse", "Keyboard", "Phone"],
"amount": [50000, 50000, 1000, 1500, 30000]
})
print("\nORDERS:")
print(orders)


# Check duplicates using customer_id + product

print("\nDUPLICATE CUSTOMER-PRODUCT COMBINATIONS:")
print(
orders.duplicated(
subset=["customer_id", "product"],
keep=False
)
)

# Remove repeated customer-product combinations

unique_orders = orders.drop_duplicates(
subset=["customer_id", "product"],
keep="first"
)
print("\nUNIQUE CUSTOMER-PRODUCT COMBINATIONS:")
print(unique_orders)

# ==================================================
# 14. UNIQUE IDS
# ==================================================

# A unique ID identifies one entity or record.

customers = pd.DataFrame({
"customer_id": [101, 102, 103, 104],
"name": ["A", "B", "C", "D"]
})
print("\nUNIQUE CUSTOMER IDS:")
print(customers["customer_id"].is_unique)

# True means every ID is unique.
# False means at least one value is repeated.

# ==================================================
# 15. CHECK DUPLICATE IDS
# ==================================================

print("\nDUPLICATE ID CHECK:")
print(customers["customer_id"].duplicated().sum())

# ==================================================
# 16. FIND DUPLICATE IDS
# ==================================================

customers_bad = pd.DataFrame({
"customer_id": [101, 102, 103, 103, 104],
"name": ["A", "B", "C", "C", "D"]
})

duplicate_ids = customers_bad[
customers_bad["customer_id"].duplicated(keep=False)
]

print("\nDUPLICATE ID RECORDS:")
print(duplicate_ids)

# ==================================================
# 17. VALID RANGES
# ==================================================

# Example:
# Age should be between 0 and 120.
# Salary should not be negative.

people = pd.DataFrame({
"name": ["A", "B", "C", "D", "E"],
"age": [20, 25, -5, 150, 35],
"salary": [30000, 40000, 50000, -1000, 60000]
})

print("\nPEOPLE DATA:")
print(people)

# Check valid age range

valid_age = people["age"].between(0, 120)
print("\nVALID AGE:")
print(valid_age)

# Display invalid ages
invalid_age = people[~valid_age]

print("\nINVALID AGE RECORDS:")
print(invalid_age)

# Check valid salary
valid_salary = people["salary"] >= 0
print("\nVALID SALARY:")
print(valid_salary)

# Display invalid salary
invalid_salary = people[~valid_salary]

print("\nINVALID SALARY RECORDS:")
print(invalid_salary)

# ==================================================
# 18. VALIDATE MULTIPLE CONDITIONS
# ==================================================

# Age must be between 0 and 120.
# Salary must be non-negative.

valid_records = (
people["age"].between(0, 120) &
(people["salary"] >= 0)
)
print("\nVALID RECORD MASK:")
print(valid_records)
print("\nVALID RECORDS:")
print(people[valid_records])

# Invalid records
print("\nINVALID RECORDS:")
print(people[~valid_records])

# ==================================================
# 19. REQUIRED COLUMNS
# ==================================================

# A dataset may be missing an important column.

df_required = pd.DataFrame({
"customer_id": [101, 102],
"name": ["A", "B"],
"age": [20, 25]
})

required_columns = [
"customer_id",
"name",
"age",
"salary"
]

# Find missing required column
missing_columns = [
col for col in required_columns
if col not in df_required.columns
]

print("\nMISSING REQUIRED COLUMNS:")
print(missing_columns)


# Check whether all required columns exist

all_columns_present = all(
col in df_required.columns
for col in required_columns
)
print("\nALL REQUIRED COLUMNS PRESENT:")
print(all_columns_present)

# ==================================================
# 20. MISSING IDENTIFIERS
# ==================================================

# IDs should generally not be missing
# when they are required to identify records.

data = {
"customer_id": [101, None, 103, 104, None],
"name": ["A", "B", "C", "D", "E"],
"age": [20, 25, 30, 35, 40]
}
df_ids = pd.DataFrame(data)
print("\nDATA WITH MISSING IDS:")
print(df_ids)

# Find missing IDs
missing_ids = df_ids["customer_id"].isna()
print("\nMISSING ID MASK:")
print(missing_ids)

# Display rows with missing IDs
print("\nROWS WITH MISSING IDS:")
print(df_ids[missing_ids])

# Count missing IDs
print("\nMISSING ID COUNT:")
print(df_ids["customer_id"].isna().sum())


# ==================================================
# 21. UNEXPECTED CATEGORIES
# ==================================================

# Suppose the allowed departments are: CSE, ECE, EEE, MECH

students = pd.DataFrame({
"name": ["A", "B", "C", "D", "E"],
"department": ["CSE", "ECE", "CSE", "XYZ", "EEE"]
})

allowed_categories = ["CSE", "ECE", "EEE", "MECH"]

# Check whether each category is allowed
valid_category = students["department"].isin(
allowed_categories
)

print("\nVALID CATEGORY MASK:")
print(valid_category)

# Display unexpected categories
unexpected = students[~valid_category]
print("\nUNEXPECTED CATEGORIES:")
print(unexpected)

# Find unique categories
print("\nALL OBSERVED CATEGORIES:")
print(students["department"].unique())

# Count category frequencies
print("\nCATEGORY COUNTS:")
print(students["department"].value_counts())

# ==================================================
# 22. DATA CONSISTENCY
# ==================================================

# Data consistency means related values should agree with each other.

orders = pd.DataFrame({
"quantity": [2, 3, 1, 4],
"unit_price": [100, 200, 500, 150],
"total_amount": [200, 600, 500, 700]
})
print("\nORDER DATA:")
print(orders)

# Calculate expected total
orders["expected_total"] = (
orders["quantity"] * orders["unit_price"]
)

print("\nEXPECTED TOTAL:")
print(orders)

# Compare expected and stored totals

orders["is_consistent"] = (
orders["total_amount"] == orders["expected_total"]
)

print("\nCONSISTENCY CHECK:")
print(orders)

# Find inconsistent records
inconsistent = orders[~orders["is_consistent"]]
print("\nINCONSISTENT RECORDS:")
print(inconsistent)

# ==================================================
# 23. STRING CONSISTENCY
# ==================================================

# Categories may have inconsistent spelling, whitespace, or capitalization.

data = pd.DataFrame({
"city": [
"Vizag",
"vizag",
" Vizag ",
"HYDERABAD",
"Hyderabad"
]
})

print("\nORIGINAL CITIES:")
print(data)

# Remove extra spaces
data["city"] = data["city"].str.strip()

# Standardize capitalization
data["city"] = data["city"].str.title()

print("\nSTANDARDIZED CITIES:")
print(data)

# Check categories after cleaning
print("\nUNIQUE CITIES:")
print(data["city"].unique())


# ==================================================
# 24. REQUIRED VALUES
# ==================================================

# Some columns must not contain missing values.

data = pd.DataFrame({
"customer_id": [101, 102, None, 104],
"name": ["A", "B", "C", None],
"age": [20, 25, 30, 35]
})

required_fields = ["customer_id", "name"]

# Check missing values in required columns
missing_required = data[required_fields].isna()

print("\nMISSING REQUIRED VALUES:")
print(missing_required)

# Count missing values per required column
print("\nMISSING REQUIRED VALUE COUNTS:")
print(missing_required.sum())

# Rows with any missing required value
invalid_required_rows = data[
missing_required.any(axis=1)
]

print("\nROWS WITH MISSING REQUIRED VALUES:")
print(invalid_required_rows)


# ==================================================
# 25. DATA VALIDATION SUMMARY
# ==================================================

# Create a simple validation report.

data = pd.DataFrame({
"customer_id": [101, 102, 102, None, 105],
"age": [20, 25, 25, 150, 30],
"city": ["Vizag", "Delhi", "Delhi", "XYZ", "Chennai"]
})

print("\nVALIDATION DATA:")
print(data)

# Total rows
total_rows = len(data)

# Missing IDs
missing_id_count = data["customer_id"].isna().sum()

# Duplicate non-missing IDs
duplicate_id_count = data["customer_id"].dropna().duplicated().sum()

# Invalid ages
invalid_age_count = (~data["age"].between(0, 120)).sum()

# Unexpected categories
allowed_cities = ["Vizag", "Delhi", "Chennai", "Hyderabad"]

unexpected_city_count = (
~data["city"].isin(allowed_cities)
).sum()

print("\nVALIDATION REPORT:")
print("Total rows:", total_rows)
print("Missing IDs:", missing_id_count)
print("Duplicate IDs:", duplicate_id_count)
print("Invalid ages:", invalid_age_count)
print("Unexpected cities:", unexpected_city_count)

# ==================================================
# 26. PRACTICAL ENGINEERING VALIDATION
# ==================================================

# Create a realistic customer dataset.

customers = pd.DataFrame({
"customer_id": [101, 102, 103, 103, None, 106],
"name": ["A", "B", "C", "C", "E", "F"],
"age": [20, 25, 30, 30, 22, 140],
"city": ["Vizag", "Delhi", "Chennai", "Chennai", "XYZ", "Hyderabad"],
"salary": [30000, 40000, 50000, 50000, 35000, -5000]
})

print("\nORIGINAL CUSTOMER DATA:")
print(customers)

# Step 1: Check required columns
required = ["customer_id", "name", "age", "city", "salary"]
missing_columns = [
col for col in required
if col not in customers.columns
]

print("\nMISSING COLUMNS:")
print(missing_columns)

# Step 2: Check missing IDs
missing_id_rows = customers[
customers["customer_id"].isna()
]

print("\nMISSING ID ROWS:")
print(missing_id_rows)

# Step 3: Check duplicate IDs
duplicate_id_rows = customers[
customers["customer_id"].notna() &
customers["customer_id"].duplicated(keep=False)
]

print("\nDUPLICATE ID ROWS:")
print(duplicate_id_rows)

# Step 4: Check age range
invalid_age_rows = customers[
~customers["age"].between(0, 120)
]

print("\nINVALID AGE ROWS:")
print(invalid_age_rows)

# Step 5: Check salary
invalid_salary_rows = customers[
customers["salary"] < 0
]

print("\nINVALID SALARY ROWS:")
print(invalid_salary_rows)

# Step 6: Check categories
allowed_cities = [
"Vizag",
"Delhi",
"Chennai",
"Hyderabad"
]

unexpected_city_rows = customers[
~customers["city"].isin(allowed_cities)
]

print("\nUNEXPECTED CITY ROWS:")
print(unexpected_city_rows)

# ==================================================
# 27. CREATE A VALID DATASET
# ==================================================

# This is an example policy:
# Keep only rows with:
# - A present customer ID
# - Unique customer ID
# - Valid age
# - Non-negative salary
# - Allowed city

valid_mask = (
customers["customer_id"].notna() &
~customers["customer_id"].duplicated(keep="first") &
customers["age"].between(0, 120) &
(customers["salary"] >= 0) &
customers["city"].isin(allowed_cities)
)
clean_customers = customers[valid_mask].copy()
print("\nVALIDATED CUSTOMER DATA:")
print(clean_customers)

# IMPORTANT:
# This is only one possible cleaning policy.
# In real projects, investigate invalid records
# before deleting or modifying them.

# ==================================================
# 28. FINAL ENGINEERING CHECKLIST
# ==================================================

# Before trusting a dataset, ask:

# 1. Are required columns present?
# 2. Are IDs missing?
# 3. Are IDs unique where required?
# 4. Are complete rows duplicated?
# 5. Are numerical values within valid ranges?
# 6. Are categories expected?
# 7. Are data types correct?
# 8. Are related columns consistent?
# 9. Are missing values understood?
# 10. Is the cleaning policy documented?


# Data validation is not just removing errors.
# It is proving that the dataset meets the requirements of the task.
