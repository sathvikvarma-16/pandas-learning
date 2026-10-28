import pandas as pd

# 1. Check data types

df = pd.DataFrame({
    "age": [20, 21, 19],
    "salary": [25000.5, 30000.0, 28000.5],
    "name": ["Ravi", "Rahul", "Anil"],
    "passed": [True, True, False]
})
print(df.dtypes)

# Output:
# age         int64
# salary    float64
# name       object
# passed       bool
# dtype: object


# 2. Main data types
# int       -> whole numbers
# float     -> decimal numbers
# object    -> usually text/string
# bool      -> True / False
# datetime  -> date and time
# category  -> repeated categorical values


# 3. Convert using astype()
df["age"] = df["age"].astype(float)
print(df["age"].dtype)

# Output:
# float64


# Convert float to integer
df["age"] = df["age"].astype(int)
print(df["age"].dtype)

# Output:
# int64


# Convert numbers to strings
df["age"] = df["age"].astype(str)
print(df["age"].dtype)

# Output:
# object


# 4. pd.to_numeric()
# Useful when numbers are stored as text.

df = pd.DataFrame({
    "marks": ["85", "90", "78"]
})
df["marks"] = pd.to_numeric(df["marks"])

print(df.dtypes)

# Output:
# marks    int64
# dtype: object


# Handle invalid values
df = pd.DataFrame({
    "marks": ["85", "90", "unknown"]
})

df["marks"] = pd.to_numeric(
    df["marks"],
    errors="coerce"
)
print(df)

# Output:
#    marks
# 0   85.0
# 1   90.0
# 2    NaN


# 5. pd.to_datetime()
dates = pd.Series([
    "2026-01-10",
    "2026-02-15",
    "2026-03-20"
])

dates = pd.to_datetime(dates)
print(dates)

# Output:
# 0   2026-01-10
# 1   2026-02-15
# 2   2026-03-20
# dtype: datetime64[ns]


# 6. Extract date information
print(dates.dt.year)
print(dates.dt.month)
print(dates.dt.day)

# Output:
# 0    2026
# 1    2026
# 2    2026

# 0    1
# 1    2
# 2    3

# 0    10
# 1    15
# 2    20


# 7. Categorical data

df = pd.DataFrame({
    "city": ["Vizag", "Hyderabad", "Vizag", "Chennai"]
})
df["city"] = df["city"].astype("category")
print(df.dtypes)

# Output:
# city    category
# dtype: object


# 8. Why correct data types matter
df = pd.DataFrame({
    "salary": ["20000", "30000", "40000"]
})

# This is text, NOT numerical data.
print(df["salary"].dtype)

# Output:
# object


# Convert it
df["salary"] = pd.to_numeric(df["salary"])

print(df["salary"].dtype)

# Output:
# int64


# Now mathematical operations work correctly.
print(df["salary"].mean())

# Output:
# 30000.0


# 9. ML problem caused by wrong type

# If numerical values are stored as strings:

# "100" + "200"
# -> "100200"

# instead of:
# 100 + 200
# -> 300

# ML models generally require numerical features
# in appropriate numerical formats.


# 10. Complete type-checking workflow

df = pd.DataFrame({
    "age": ["20", "21", "19"],
    "salary": ["25000", "30000", "28000"],
    "joined": ["2026-01-10", "2026-02-15", "2026-03-20"]
})
print(df.dtypes)

df["age"] = pd.to_numeric(df["age"])
df["salary"] = pd.to_numeric(df["salary"])
df["joined"] = pd.to_datetime(df["joined"])

print(df.dtypes)

# Output:
# age                  int64
# salary               int64
# joined      datetime64[ns]
# dtype: object


# Remember:

# df.dtypes
# -> check data types

# df["age"].astype(int)
# -> direct conversion

# pd.to_numeric()
# -> convert values to numbers

# pd.to_datetime()
# -> convert values to dates

# category
# -> useful for categorical/repeated values


# ML workflow:

# Raw Data
#    ↓
# Check dtypes
#    ↓
# Fix incorrect types
#    ↓
# Clean Data
#    ↓
# Feature Engineering
#    ↓
# Machine Learning

