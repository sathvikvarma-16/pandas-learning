import pandas as pd


# 1. Create a Series

s = pd.Series([10, 20, 30, 40, 50])
print(s)

# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64


# 2. Values
# Get only the values from the Series
print(s.values)
# Output:
# [10 20 30 40 50]


# 3. Index
# Get the row labels
print(s.index) # RangeIndex(start=0, stop=5, step=1)


# 4. Custom index
s = pd.Series(
    [85, 90, 78],
    index=["Ravi", "Rahul", "Anil"]
)

print(s)

# Output:
# Ravi     85
# Rahul    90
# Anil     78
# dtype: int64


# 5. Access elements

print(s["Ravi"])
print(s["Rahul"])

# Output:
# 85
# 90


# 6. Access using position

print(s.iloc[0])
print(s.iloc[2])

# Output:
# 85
# 78


# 7. Slicing

s = pd.Series([10, 20, 30, 40, 50])
print(s[1:4])

# Output:
# 1    20
# 2    30
# 3    40
# dtype: int64


# 8. Arithmetic operations

s = pd.Series([10, 20, 30])
print(s + 5)
print(s * 2)
print(s ** 2)

# Output:
# 0    15
# 1    25
# 2    35
# dtype: int64

# 0    20
# 1    40
# 2    60
# dtype: int64

# 0    100
# 1    400
# 2    900
# dtype: int64


# 9. Series with another Series

a = pd.Series([10, 20, 30])
b = pd.Series([1, 2, 3])

print(a + b)
print(a * b)

# Output:
# 0    11
# 1    22
# 2    33
# dtype: int64

# 0    10
# 1    40
# 2    90
# dtype: int64


# 10. Comparisons
s = pd.Series([10, 25, 40, 15])
print(s > 20)

# Output:
# 0    False
# 1     True
# 2     True
# 3    False
# dtype: bool


# 11. Boolean filtering
print(s[s > 20])

# Output:
# 1    25
# 2    40
# dtype: int64


# 12. Multiple conditions
print(s[(s > 10) & (s < 40)])

# Output:
# 1    25
# 3    15
# dtype: int64


# 13. head()
# First 5 values by default
s = pd.Series([10, 20, 30, 40, 50, 60])

print(s.head())

# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64


# 14. head(n) # first 3 values
print(s.head(3))

# Output:
# 0    10
# 1    20
# 2    30
# dtype: int64


# 15. tail()
# Last 5 values by default
print(s.tail())

# Output:
# 1    20
# 2    30
# 3    40
# 4    50
# 5    60
# dtype: int64


# 16. tail(n)
print(s.tail(2))

# Output:
# 4    50
# 5    60
# dtype: int64


# 17. describe()
# Basic statistical summary
s = pd.Series([10, 20, 30, 40, 50])

print(s.describe())

# Output:
# count     5.000000
# mean     30.000000
# std      15.811388
# min      10.000000
# 25%      20.000000
# 50%      30.000000
# 75%      40.000000
# max      50.000000
# dtype: float64


# 18. Real-world example
marks = pd.Series(
    [85, 92, 76, 88, 95],
    index=["Ravi", "Rahul", "Anil", "Priya", "Kiran"]
)

print(marks[marks >= 90])

# Output:
# Rahul    92
# Kiran    95
# dtype: int64


# 19. Complete Series practice
sales = pd.Series([100, 250, 150, 300, 200])

print(sales.head(3))
print(sales.tail(2))
print(sales.mean())
print(sales[sales > 200])

# Output:
# 0    100
# 1    250
# 2    150
# dtype: int64

# 3    300
# 4    200
# dtype: int64

# 200.0
#
# 1    250
# 3    300
# dtype: int64
