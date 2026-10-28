import pandas as pd


# ============================================================
# PHASE 10: FILTERING & CONDITIONAL DATA
# ============================================================


df = pd.DataFrame({
    "name": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran"],
    "age": [19, 22, 25, 21, 30],
    "salary": [30000, 55000, 70000, 45000, 90000],
    "city": ["Vizag", "Hyderabad", "Vizag", "Chennai", "Vizag"]
})
print(df)


# ------------------------------------------------------------
# 1. SIMPLE CONDITION
# ------------------------------------------------------------

# Select people whose age is greater than 20.
result = df[df["age"] > 20]
print(result)

# Output:
#     name  age  salary        city
# 1  Priya   22   55000   Hyderabad
# 2  Arjun   25   70000       Vizag
# 3  Sneha   21   45000     Chennai
# 4  Kiran   30   90000       Vizag


# ------------------------------------------------------------
# 2. UNDERSTAND WHAT HAPPENS
# ------------------------------------------------------------

condition = df["age"] > 20
print(condition)

# Output:
# 0     False
# 1     True
# 2     True
# 3     True
# 4     True

# Pandas checks every row.

# True  -> keep the row
# False -> remove the row


# ------------------------------------------------------------
# 3. GREATER THAN
# ------------------------------------------------------------

print(df[df["salary"] > 50000])

# Salary greater than 50000.


# ------------------------------------------------------------
# 4. LESS THAN
# ------------------------------------------------------------

print(df[df["age"] < 25])

# Age less than 25.


# ------------------------------------------------------------
# 5. EQUAL TO
# ------------------------------------------------------------

print(df[df["city"] == "Vizag"])

# Only people from Vizag.


# ------------------------------------------------------------
# 6. NOT EQUAL TO
# ------------------------------------------------------------

print(df[df["city"] != "Vizag"])

# People who are NOT from Vizag.


# ------------------------------------------------------------
# 7. AND (&)
# ------------------------------------------------------------

# Both conditions must be TRUE.

result = df[
    (df["age"] > 20) &
    (df["salary"] > 50000)
]
print(result)

# Output:
#     name  age  salary       city
# 1  Priya   22   55000  Hyderabad
# 2  Arjun   25   70000      Vizag
# 4  Kiran   30   90000      Vizag

# Meaning:
# age > 20
# AND
# salary > 50000


# ------------------------------------------------------------
# 8. OR (|)
# ------------------------------------------------------------

# At least one condition must be TRUE.

result = df[
    (df["age"] > 25) |
    (df["salary"] > 80000)
]

print(result)

# Kiran satisfies both conditions.
#
# OR means:
# condition 1 OR condition 2


# ------------------------------------------------------------
# 9. NOT (~)
# ------------------------------------------------------------

# ~ reverses True and False.

result = df[
    ~(df["city"] == "Vizag")
]

print(result)

# Same idea as:
# city != "Vizag"


# ------------------------------------------------------------
# 10. MULTIPLE CONDITIONS
# ------------------------------------------------------------

result = df[
    (df["age"] > 20) &
    (df["salary"] > 40000) &
    (df["city"] == "Vizag")
]

print(result)

# All three conditions must be TRUE.


# ------------------------------------------------------------
# 11. isin()
# ------------------------------------------------------------

# Check whether a value belongs to a list.

result = df[
    df["city"].isin(["Vizag", "Chennai"])
]
print(result)

# Output:
#     name  age  salary     city
# 0  Rahul   19   30000    Vizag
# 2  Arjun   25   70000    Vizag
# 3  Sneha   21   45000  Chennai


# ------------------------------------------------------------
# 12. isin() WITH NUMBERS
# ------------------------------------------------------------

result = df[
    df["age"].isin([21, 25, 30])
]
print(result)

# Select rows where age is exactly
# 21 OR 25 OR 30.


# ------------------------------------------------------------
# 13. between()
# ------------------------------------------------------------

# Select values between two limits.
result = df[
    df["age"].between(20, 25)
]
print(result)

# By default, both boundaries are included.
# 20 <= age <= 25


# ------------------------------------------------------------
# 14. between() WITH SALARY
# ------------------------------------------------------------

result = df[
    df["salary"].between(40000, 70000)
]
print(result)

# Salary between 40000 and 70000.


# ------------------------------------------------------------
# 15. query()
# ------------------------------------------------------------

# query() allows conditions to be written
# in a SQL-like style.

result = df.query("age > 20")
print(result)


# ------------------------------------------------------------
# 16. query() WITH AND
# ------------------------------------------------------------

result = df.query(
    "age > 20 and salary > 50000"
)
print(result)

# Same idea as:
# (df["age"] > 20) &
# (df["salary"] > 50000)


# ------------------------------------------------------------
# 17. query() WITH OR
# ------------------------------------------------------------

result = df.query(
    "age > 25 or salary > 80000"
)
print(result)


# ------------------------------------------------------------
# 18. query() WITH EQUALITY
# ------------------------------------------------------------

result = df.query(
    'city == "Vizag"'
)
print(result)


# ------------------------------------------------------------
# 19. query() WITH NOT
# ------------------------------------------------------------

result = df.query(
    'city != "Vizag"'
)
print(result)


# ------------------------------------------------------------
# 20. MULTIPLE CONDITIONS USING query()
# ------------------------------------------------------------

result = df.query(
    'age > 20 and salary > 40000 and city == "Vizag"'
)
print(result)


# ------------------------------------------------------------
# 21. SELECT SPECIFIC COLUMNS AFTER FILTERING
# ------------------------------------------------------------

result = df[
    df["salary"] > 50000
][["name", "salary"]]

print(result)

# First:
# Filter rows
#
# Then:
# Select required columns


# ------------------------------------------------------------
# 22. FILTER + isin()
# ------------------------------------------------------------

result = df[
    (df["age"] > 20) &
    (df["city"].isin(["Vizag", "Hyderabad"]))
]
print(result)


# ------------------------------------------------------------
# 23. FILTER + between()
# ------------------------------------------------------------

result = df[
    df["age"].between(20, 30) &
    df["salary"].between(40000, 80000)
]
print(result)


# ------------------------------------------------------------
# 24. IMPORTANT: USE & | ~
# ------------------------------------------------------------

# Pandas uses:
#
# AND -> &
# OR  -> |
# NOT -> ~
#
# Do NOT use:
#
# and
# or
# not
#
# inside normal DataFrame boolean filtering.


# ------------------------------------------------------------
# 25. ALWAYS USE PARENTHESES
# ------------------------------------------------------------

# Correct:

result = df[
    (df["age"] > 20) &
    (df["salary"] > 50000)
]

# Incorrect:

# df[df["age"] > 20 & df["salary"] > 50000]
# Put each condition inside parentheses.


# ------------------------------------------------------------
# 26. REAL-WORLD EXAMPLE
# ------------------------------------------------------------

employees = pd.DataFrame({
    "name": ["A", "B", "C", "D", "E"],
    "age": [22, 28, 35, 24, 40],
    "salary": [40000, 60000, 90000, 50000, 120000],
    "department": [
        "IT", "HR", "IT", "Sales", "IT"
    ]
})

# Find IT employees earning more than 50000.

result = employees[
    (employees["department"] == "IT") &
    (employees["salary"] > 50000)
]
print(result)

# Output:
#   name  age  salary department
# 2    C   35   90000         IT
# 4    E   40  120000         IT


# ------------------------------------------------------------
# 27. COMPLETE FILTERING THINKING
# ------------------------------------------------------------

# DataFrame
#     ↓
# Write condition
#     ↓
# True / False for every row
#     ↓
# Keep True rows
#     ↓
# Filtered DataFrame


# Example:
#
# df["age"] > 20
#
# becomes:
#
# False
# True
# True
# True
# True
#
# df[condition]
#
# keeps only True rows.


# ------------------------------------------------------------
# MOST IMPORTANT PATTERNS
# ------------------------------------------------------------

# Greater than:
# df[df["age"] > 20]

# Less than:
# df[df["age"] < 20]

# Equal:
# df[df["city"] == "Vizag"]

# Not equal:
# df[df["city"] != "Vizag"]

# AND:
# df[(df["age"] > 20) & (df["salary"] > 50000)]

# OR:
# df[(df["age"] > 25) | (df["salary"] > 80000)]

# NOT:
# df[~(df["city"] == "Vizag")]

# Multiple allowed values:
# df[df["city"].isin(["Vizag", "Chennai"])]

# Range:
# df[df["age"].between(20, 30)]

# SQL-like filtering:
# df.query("age > 20 and salary > 50000")
