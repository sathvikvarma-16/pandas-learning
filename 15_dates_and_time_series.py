# Pandas Phase 15: Dates & Time Series

# Import Pandas

import pandas as pd

# --------------------------------------------------
# 1. CREATE A DATAFRAME WITH DATE DATA
# --------------------------------------------------

data = {
"employee": ["A", "B", "C", "D", "E", "F"],
"joining_date": [
"2024-01-15",
"2024-03-20",
"2024-06-10",
"2025-01-05",
"2025-05-18",
"2025-09-25"
],
"salary": [30000, 35000, 40000, 45000, 50000, 55000]
}
  
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# --------------------------------------------------
# 2. pd.to_datetime()
# --------------------------------------------------

# Convert a column from string/object to datetime

df["joining_date"] = pd.to_datetime(df["joining_date"])
print("\nAfter converting to datetime:")
print(df)
print("\nData types:")
print(df.dtypes)

# Now joining_date is a datetime column

# --------------------------------------------------
# 3. EXTRACT YEAR
# --------------------------------------------------

# .dt.year extracts the year from each date

df["year"] = df["joining_date"].dt.year
print("\nYear:")
print(df[["joining_date", "year"]])

# --------------------------------------------------
# 4. EXTRACT MONTH
# --------------------------------------------------

# .dt.month extracts the month number

df["month"] = df["joining_date"].dt.month
print("\nMonth:")
print(df[["joining_date", "month"]])

# --------------------------------------------------
# 5. EXTRACT DAY
# --------------------------------------------------

# .dt.day extracts the day of the month

df["day"] = df["joining_date"].dt.day
print("\nDay:")
print(df[["joining_date", "day"]])

# --------------------------------------------------
# 6. EXTRACT DAY NAME
# --------------------------------------------------

# .dt.day_name() gives the weekday name

df["day_name"] = df["joining_date"].dt.day_name()
print("\nDay name:")
print(df[["joining_date", "day_name"]])

# --------------------------------------------------
# 7. OTHER USEFUL DATE COMPONENTS
# --------------------------------------------------

# These are useful in practical ML/data projects

df["month_name"] = df["joining_date"].dt.month_name()
df["day_of_week"] = df["joining_date"].dt.dayofweek
df["quarter"] = df["joining_date"].dt.quarter
df["day_of_year"] = df["joining_date"].dt.dayofyear
print("\nUseful date components:")
print(
df[
[
"joining_date",
"month_name",
"day_of_week",
"quarter",
"day_of_year"
]
]
)

# --------------------------------------------------
# 8. DATE FILTERING
# --------------------------------------------------

# Select employees who joined after January 1, 2025

result = df[df["joining_date"] > "2025-01-01"]
print("\nEmployees who joined after 2025-01-01:")
print(result)

# Select employees who joined before January 1, 2025

result = df[df["joining_date"] < "2025-01-01"]

print("\nEmployees who joined before 2025:")
print(result)

# Select employees between two dates

result = df[
(df["joining_date"] >= "2024-01-01") &
(df["joining_date"] <= "2024-12-31")
]
print("\nEmployees who joined during 2024:")
print(result)

# --------------------------------------------------
# 9. FILTER USING pd.Timestamp
# --------------------------------------------------

# pd.Timestamp represents a specific date/time

start_date = pd.Timestamp("2024-01-01")
end_date = pd.Timestamp("2024-12-31")
result = df[
(df["joining_date"] >= start_date) &
(df["joining_date"] <= end_date)
]
print("\nUsing pd.Timestamp:")
print(result)


# --------------------------------------------------
# 10. DATE DIFFERENCES
# --------------------------------------------------

# Create another date column

df["today"] = pd.Timestamp("2025-12-31")

# Subtract two datetime values

df["days_since_joining"] = (
df["today"] - df["joining_date"]
).dt.days

print("\nDays since joining:")
print(
df[
[
"employee",
"joining_date",
"today",
"days_since_joining"
]
]
)

# --------------------------------------------------
# 11. DATE DIFFERENCE IN WEEKS
# --------------------------------------------------

# Convert days into weeks

df["weeks_since_joining"] = (
df["days_since_joining"] / 7
)
print("\nWeeks since joining:")
print(
df[
[
"employee",
"days_since_joining",
"weeks_since_joining"
]
]
)

# --------------------------------------------------
# 12. DATE DIFFERENCE BETWEEN TWO COLUMNS
# --------------------------------------------------

data2 = {
"employee": ["A", "B", "C", "D"],
"start_date": [
"2024-01-10",
"2024-02-15",
"2024-04-01",
"2024-06-20"
],
"end_date": [
"2024-01-20",
"2024-03-01",
"2024-04-15",
"2024-07-01"
]
}

df2 = pd.DataFrame(data2)
# Convert both columns to datetime
df2["start_date"] = pd.to_datetime(df2["start_date"])
df2["end_date"] = pd.to_datetime(df2["end_date"])

# Find difference

df2["duration_days"] = (
df2["end_date"] - df2["start_date"]
).dt.days

print("\nDate difference between two columns:")
print(df2)



# --------------------------------------------------
# 13. SORTING BY DATE
# --------------------------------------------------

# Create an unsorted DataFrame

data3 = {
"employee": ["A", "B", "C", "D"],
"joining_date": [
"2025-09-25",
"2024-01-15",
"2025-01-05",
"2024-06-10"
]
}
df3 = pd.DataFrame(data3)
df3["joining_date"] = pd.to_datetime(df3["joining_date"])

# Sort from oldest to newest

df_sorted = df3.sort_values("joining_date")
print("\nSorted from oldest to newest:")
print(df_sorted)

# Sort from newest to oldest

df_sorted = df3.sort_values(
"joining_date",
ascending=False
)
print("\nSorted from newest to oldest:")
print(df_sorted)

# --------------------------------------------------
# 14. SET DATE AS INDEX
# --------------------------------------------------

# Time series data often uses dates as the index

df3 = df3.sort_values("joining_date")
df3 = df3.set_index("joining_date")
print("\nDate as index:")
print(df3)



# --------------------------------------------------
# 15. TIME-BASED GROUPING
# --------------------------------------------------

# Create a sales dataset

sales_data = {
"date": [
"2025-01-05",
"2025-01-15",
"2025-02-10",
"2025-02-20",
"2025-03-05",
"2025-03-25",
"2025-04-10",
"2025-04-20"
],
"sales": [
1000,
1500,
1200,
1800,
2000,
2200,
2500,
2700
]
}

sales = pd.DataFrame(sales_data)
sales["date"] = pd.to_datetime(sales["date"])
print("\nSales data:")
print(sales)

# Group sales by year

yearly_sales = sales.groupby(
sales["date"].dt.year
)["sales"].sum()
print("\nYearly sales:")
print(yearly_sales)

# Group sales by month

monthly_sales = sales.groupby(
sales["date"].dt.month
)["sales"].sum()
print("\nMonthly sales:")
print(monthly_sales)

# Group by year and month together

sales["year"] = sales["date"].dt.year
sales["month"] = sales["date"].dt.month
monthly_sales = sales.groupby(
["year", "month"]
)["sales"].sum()

print("\nSales grouped by year and month:")
print(monthly_sales)

# --------------------------------------------------
# 16. pd.Grouper FOR TIME-BASED GROUPING
# --------------------------------------------------

# pd.Grouper is useful when working with dates

sales_by_month = sales.groupby(
pd.Grouper(key="date", freq="ME")
)["sales"].sum()
print("\nSales grouped by month using pd.Grouper:")
print(sales_by_month)


# --------------------------------------------------
# 17. RESAMPLING BASICS
# --------------------------------------------------

# Resampling means changing the time frequency

# Example:

# Daily data -> Monthly data

# Daily data -> Weekly data

# Monthly data -> Yearly data

sales = sales.set_index("date")

# Monthly sales

monthly = sales["sales"].resample("ME").sum()
print("\nMonthly resampled sales:")
print(monthly)

# Weekly sales

weekly = sales["sales"].resample("W").sum()
print("\nWeekly resampled sales:")
print(weekly)

# Quarterly sales

quarterly = sales["sales"].resample("QE").sum()
print("\nQuarterly resampled sales:")
print(quarterly)


# --------------------------------------------------
# 18. RESAMPLING WITH DIFFERENT OPERATIONS
# --------------------------------------------------

# Monthly average

monthly_mean = sales["sales"].resample("ME").mean()
print("\nMonthly average sales:")
print(monthly_mean)

# Monthly maximum

monthly_max = sales["sales"].resample("ME").max()

print("\nMonthly maximum sales:")
print(monthly_max)

# Monthly minimum

monthly_min = sales["sales"].resample("ME").min()
print("\nMonthly minimum sales:")
print(monthly_min)


# --------------------------------------------------
# 19. ROLLING BASICS
# --------------------------------------------------

# Rolling calculates a moving value over a fixed window.
# Example:
# Window = 3
# First 3 values -> average
# Then next 3 values -> average
# And so on

sales["rolling_mean_3"] = (
sales["sales"]
.rolling(window=3)
.mean()
)
print("\n3-period rolling mean:")
print(
sales[
[
"sales",
"rolling_mean_3"
]
]
)


# --------------------------------------------------
# 20. ROLLING SUM
# --------------------------------------------------

sales["rolling_sum_3"] = (
sales["sales"]
.rolling(window=3)
.sum()
)
print("\n3-period rolling sum:")
print(
sales[
[
"sales",
"rolling_sum_3"
]
]
)

# --------------------------------------------------
# 21. ROLLING MAXIMUM
# --------------------------------------------------

sales["rolling_max_3"] = (
sales["sales"]
.rolling(window=3)
.max()
)
print("\n3-period rolling maximum:")
print(
sales[
[
"sales",
"rolling_max_3"
]
]
)

# --------------------------------------------------
# 22. ROLLING WITH min_periods
# --------------------------------------------------

# By default, window=3 needs 3 values
# before calculating the result.
# min_periods=1 allows calculation
# even when fewer values are available.

sales["rolling_mean"] = (
sales["sales"]
.rolling(
window=3,
min_periods=1
)
.mean()
)
print("\nRolling mean with min_periods=1:")
print(
sales[
[
"sales",
"rolling_mean"
]
]
)

# --------------------------------------------------
# 23. PRACTICAL ML FEATURE ENGINEERING
# --------------------------------------------------

# Dates themselves are often not directly useful
# to an ML model.

#

# We can extract useful features from them.

feature_data = {
"date": [
"2025-01-05",
"2025-02-10",
"2025-03-15",
"2025-04-20",
"2025-05-25"
],
"sales": [100, 150, 120, 200, 180]
}
features = pd.DataFrame(feature_data)
features["date"] = pd.to_datetime(features["date"])

# Extract useful date features

features["year"] = features["date"].dt.year
features["month"] = features["date"].dt.month
features["day"] = features["date"].dt.day
features["day_of_week"] = features["date"].dt.dayofweek
features["quarter"] = features["date"].dt.quarter
print("\nDate features for ML:")
print(features)

# --------------------------------------------------
# 24. PRACTICAL EXAMPLE
# --------------------------------------------------

# Suppose we have daily sales data.

# We want to:

# 1. Convert date
# 2. Sort by date
# 3. Extract month
# 4. Calculate monthly sales
# 5. Calculate rolling average

practical_data = {
"date": [
"2025-03-05",
"2025-01-10",
"2025-02-15",
"2025-01-20",
"2025-03-20",
"2025-02-25"
],
"sales": [
500,
300,
450,
350,
600,
550
]
}

practical = pd.DataFrame(practical_data)

# Convert date
practical["date"] = pd.to_datetime(
practical["date"]
)

# Sort by date

practical = practical.sort_values("date")
# Extract month

practical["month"] = practical["date"].dt.month
print("\nPractical dataset:")
print(practical)

# Monthly total

monthly_total = practical.groupby(
"month"
)["sales"].sum()
print("\nMonthly total sales:")
print(monthly_total)

# Set date as index

practical = practical.set_index("date")
# Rolling 3-period average

practical["rolling_average"] = (
practical["sales"]
.rolling(window=3)
.mean()
)

print("\nFinal practical dataset:")
print(practical)


