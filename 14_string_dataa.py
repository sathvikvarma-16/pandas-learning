"""
This phase teaches you to clean, search, standardize, and extract information from text columns.
Real datasets contain names, emails, addresses, product descriptions, categories, and other text fields. These often need cleaning before analysis or ML preprocessing.
Core idea: .str lets you perform string operations across an entire Pandas Series.
"""


import pandas as pd

# ============================================================
# PHASE 14: STRING DATA
# ============================================================

df = pd.DataFrame({
    "name": [" Rahul ", "PRIYA", " arjun ", "Sneha"],
    "email": [
        "RAHUL@GMAIL.COM ",
        "priya@yahoo.com",
        " ARJUN@GMAIL.COM",
        "sneha@outlook.com"
    ],
    "city": ["vizag", "HYDERABAD", "Vizag ", "Chennai"],
    "department": ["CSE", "ECE", "CSE", "IT"]
})
print(df)


# ------------------------------------------------------------
# 1. .str
# ------------------------------------------------------------

# .str provides string operations on a Series.

print(df["name"].str.lower())

# Every name becomes lowercase.


# ------------------------------------------------------------
# 2. str.lower()
# ------------------------------------------------------------

df["name_lower"] = df["name"].str.lower()
print(df["name_lower"])

# Rahul  -> rahul
# PRIYA  -> priya
# arjun  -> arjun


# ------------------------------------------------------------
# 3. str.upper()
# ------------------------------------------------------------

df["name_upper"] = df["name"].str.upper()
print(df["name_upper"])

# Rahul -> RAHUL
# PRIYA -> PRIYA


# ------------------------------------------------------------
# 4. str.title()
# ------------------------------------------------------------

df["name_title"] = df["name"].str.strip().str.title()
print(df["name_title"])

# Rahul
# Priya
# Arjun
# Sneha


# ------------------------------------------------------------
# 5. str.strip()
# ------------------------------------------------------------

# Removes leading and trailing whitespace.

df["name"] = df["name"].str.strip()
print(df["name"])

# " Rahul " -> "Rahul"
# " arjun " -> "arjun"


# ------------------------------------------------------------
# 6. CLEAN EMAIL ADDRESSES
# ------------------------------------------------------------

df["email"] = (
    df["email"]
    .str.strip()
    .str.lower()
)
print(df["email"])

# rahul@gmail.com
# priya@yahoo.com
# arjun@gmail.com
# sneha@outlook.com


# ------------------------------------------------------------
# 7. str.replace()
# ------------------------------------------------------------

# Replace text inside strings.

df["city"] = (
    df["city"]
    .str.strip()
    .str.lower()
    .str.replace("vizag", "visakhapatnam")
)
print(df["city"])

# vizag -> visakhapatnam
# HYDERABAD -> hyderabad


# ------------------------------------------------------------
# 8. str.contains()
# ------------------------------------------------------------

# Check whether text contains a pattern.

result = df[df["email"].str.contains("gmail")]
print(result[["name", "email"]])

# Select Gmail users.


# ------------------------------------------------------------
# 9. str.contains() WITH CASE INSENSITIVITY
# ------------------------------------------------------------

result = df[
    df["email"].str.contains("GMAIL", case=False)
]
print(result)

# case=False means uppercase/lowercase
# differences are ignored.


# ------------------------------------------------------------
# 10. str.startswith()
# ------------------------------------------------------------

result = df[
    df["email"].str.startswith("rahul")
]
print(result)

# Select emails beginning with "rahul".


# ------------------------------------------------------------
# 11. str.endswith()
# ------------------------------------------------------------

result = df[
    df["email"].str.endswith("gmail.com")
]
print(result)

# Select Gmail addresses.


# ------------------------------------------------------------
# 12. str.split()
# ------------------------------------------------------------

# Split a string using a separator.

df["first_name"] = df["name"].str.split(" ").str[0]
print(df[["name", "first_name"]])

# Splits at spaces.
# .str[0] selects the first part.


# ------------------------------------------------------------
# 13. SPLIT EMAIL INTO PARTS
# ------------------------------------------------------------

df["email_provider"] = (
    df["email"]
    .str.split("@")
    .str[1]
)
print(df[["email", "email_provider"]])

# rahul@gmail.com -> gmail.com
# priya@yahoo.com -> yahoo.com


# ------------------------------------------------------------
# 14. EXTRACT USERNAME FROM EMAIL
# ------------------------------------------------------------

df["email_username"] = (
    df["email"]
    .str.split("@")
    .str[0]
)
print(df[["email", "email_username"]])


# ------------------------------------------------------------
# 15. str.len()
# ------------------------------------------------------------

# Count characters in each string.

df["name_length"] = df["name"].str.len()
print(df[["name", "name_length"]])

# Rahul -> 5
# Priya -> 5
# Arjun -> 5
# Sneha -> 5


# ------------------------------------------------------------
# 16. FIND INVALID EMAILS: BASIC CHECK
# ------------------------------------------------------------

valid_email = df["email"].str.contains(
    "@",
    na=False
)
print(valid_email)

# True means the string contains @.
# This is only a basic check, not full email validation.


# ------------------------------------------------------------
# 17. str.extract()
# ------------------------------------------------------------

# Extract information using a regular expression.

df["email_domain"] = df["email"].str.extract(
    r"@(.+)$"
)
print(df[["email", "email_domain"]])

# rahul@gmail.com -> gmail.com
# priya@yahoo.com -> yahoo.com


# ------------------------------------------------------------
# 18. EXTRACT EMAIL USERNAME AND DOMAIN
# ------------------------------------------------------------

df[["username", "domain"]] = df["email"].str.extract(
    r"^([^@]+)@(.+)$"
)
print(df[["email", "username", "domain"]])

# First capture group -> username
# Second capture group -> domain


# ------------------------------------------------------------
# 19. EXTRACT NUMBERS FROM TEXT
# ------------------------------------------------------------

products = pd.DataFrame({
    "product": [
        "Laptop 16GB",
        "Phone 8GB",
        "Tablet 4GB"
    ]
})
products["ram"] = products["product"].str.extract(
    r"(\d+)GB"
)

products["ram"] = products["ram"].astype(int)
print(products)

# Output:
#       product  ram
# 0  Laptop 16GB   16
# 1   Phone 8GB    8
# 2  Tablet 4GB    4


# ------------------------------------------------------------
# 20. EXTRACT CATEGORIES
# ------------------------------------------------------------

students = pd.DataFrame({
    "course": [
        "CSE-AI",
        "ECE-ML",
        "CSE-DS",
        "IT-ML"
    ]
})
students["branch"] = students["course"].str.extract(
    r"^([A-Z]+)"
)
print(students)

# CSE-AI -> CSE
# ECE-ML -> ECE
# CSE-DS -> CSE
# IT-ML -> IT


# ------------------------------------------------------------
# 21. SEARCH TEXT
# ------------------------------------------------------------

reviews = pd.DataFrame({
    "review": [
        "Excellent product",
        "Poor quality",
        "Good performance",
        "Excellent service"
    ]
})
result = reviews[
    reviews["review"].str.contains(
        "excellent",
        case=False,
        na=False
    )
]
print(result)

# Finds reviews containing "excellent".


# ------------------------------------------------------------
# 22. str.replace() WITH REGEX
# ------------------------------------------------------------

phone = pd.Series([
    "987-654-3210",
    "912 345 6780"
])
clean_phone = phone.str.replace(
    r"\D",
    "",
    regex=True
)
print(clean_phone)

# Removes non-digit characters.
#
# Output:
# 9876543210
# 9123456780


# ------------------------------------------------------------
# 23. CLEANING A COMPLETE TEXT DATASET
# ------------------------------------------------------------

data = pd.DataFrame({
    " Student Name ": [" Rahul ", "PRIYA ", " arjun"],
    "Email Address": [
        " RAHUL@GMAIL.COM ",
        "PRIYA@YAHOO.COM",
        " ARJUN@GMAIL.COM"
    ],
    "City": [" VIZAG ", "vizag", "HYDERABAD"]
})

# Step 1: Clean column names

data.columns = (
    data.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Step 2: Clean names

data["student_name"] = (
    data["student_name"]
    .str.strip()
    .str.title()
)

# Step 3: Clean email addresses

data["email_address"] = (
    data["email_address"]
    .str.strip()
    .str.lower()
)

# Step 4: Standardize cities

data["city"] = (
    data["city"]
    .str.strip()
    .str.lower()
    .replace({
        "vizag": "visakhapatnam",
        "hyderabad": "hyderabad"
    })
)

# Step 5: Extract email domain

data["email_domain"] = data["email_address"].str.extract(
    r"@(.+)$"
)

print(data)


# ------------------------------------------------------------
# IMPORTANT STRING PATTERNS
# ------------------------------------------------------------

# Lowercase:
# df["name"].str.lower()

# Uppercase:
# df["name"].str.upper()

# Title case:
# df["name"].str.title()

# Remove spaces:
# df["name"].str.strip()

# Replace:
# df["city"].str.replace("vizag", "visakhapatnam")

# Search:
# df["email"].str.contains("gmail", na=False)

# Starts with:
# df["email"].str.startswith("rahul", na=False)

# Ends with:
# df["email"].str.endswith("gmail.com", na=False)

# Split:
# df["email"].str.split("@")

# First split part:
# df["email"].str.split("@").str[0]

# String length:
# df["name"].str.len()

# Extract using regex:
# df["email"].str.extract(r"@(.+)$")
