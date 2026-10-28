import pandas as pd


# ============================================================
# PHASE 11: SORTING & RANKING
# ============================================================

df = pd.DataFrame({
    "name": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran"],
    "age": [22, 20, 25, 21, 23],
    "marks": [85, 95, 78, 95, 88],
    "salary": [40000, 60000, 35000, 75000, 50000]
})
print(df)


# ------------------------------------------------------------
# 1. sort_values()
# ------------------------------------------------------------

# Sort rows based on a column.

result = df.sort_values("marks")
print(result)

# Default: ascending=True
# Lowest marks -> Highest marks


# ------------------------------------------------------------
# 2. ASCENDING ORDER
# ------------------------------------------------------------

result = df.sort_values("salary", ascending=True)
print(result)

# Salary:
# 35000
# 40000
# 50000
# 60000
# 75000


# ------------------------------------------------------------
# 3. DESCENDING ORDER
# ------------------------------------------------------------

result = df.sort_values("salary", ascending=False)
print(result)

# Salary:
# 75000
# 60000
# 50000
# 40000
# 35000


# ------------------------------------------------------------
# 4. SORT BY AGE
# ------------------------------------------------------------

result = df.sort_values("age")
print(result)

# Youngest -> Oldest


# ------------------------------------------------------------
# 5. MULTIPLE-COLUMN SORTING
# ------------------------------------------------------------

result = df.sort_values(
    ["marks", "age"]
)

print(result)

# First:
# Sort by marks in ascending order.

# If marks are equal:
# Sort those rows by age in ascending order.


# ------------------------------------------------------------
# 6. MULTIPLE-COLUMN SORTING WITH DIFFERENT ORDERS
# ------------------------------------------------------------

result = df.sort_values(
    ["marks", "age"],
    ascending=[False, True]
)
print(result)

# First:
# Marks descending (highest first)
#
# Second:
# Age ascending (youngest first)
#
# Secondary sorting is used when marks are tied.


# ------------------------------------------------------------
# 7. SORTING BY MULTIPLE COLUMNS DESCENDING
# ------------------------------------------------------------

result = df.sort_values(
    ["salary", "marks"],
    ascending=[False, False]
)
print(result)

# Highest salary first.
# If salary is equal, highest marks first.


# ------------------------------------------------------------
# 8. sort_index()
# ------------------------------------------------------------

# Sort rows according to their index labels.

df2 = pd.DataFrame(
    {
        "name": ["Rahul", "Priya", "Arjun"],
        "marks": [85, 95, 78]
    },
    index=[3, 1, 2]
)
print(df2)
result = df2.sort_index()
print(result)

# Index order:
# 1
# 2
# 3


# ------------------------------------------------------------
# 9. sort_index() DESCENDING
# ------------------------------------------------------------

result = df2.sort_index(ascending=False)
print(result)

# Index order:
# 3
# 2
# 1


# ------------------------------------------------------------
# 10. SORT COLUMNS BY THEIR NAMES
# ------------------------------------------------------------

result = df.sort_index(axis=1)
print(result)

# axis=1 means sort column labels.
# axis=0 means sort row index labels.


# ------------------------------------------------------------
# 11. nlargest()
# ------------------------------------------------------------

# Find the top 3 marks.

result = df.nlargest(3, "marks")
print(result)

# Output:
#      name  age  marks  salary
# 1   Priya   20     95   60000
# 3   Sneha   21     95   75000
# 4   Kiran   23     88   50000


# ------------------------------------------------------------
# 12. nsmallest()
# ------------------------------------------------------------

# Find the 2 lowest marks.

result = df.nsmallest(2, "marks")
print(result)

# Output:
#     name  age  marks  salary
# 2  Arjun   25     78   35000
# 0  Rahul   22     85   40000


# ------------------------------------------------------------
# 13. TOP 3 SALARIES
# ------------------------------------------------------------

result = df.nlargest(3, "salary")
print(result)

# Highest salaries first.


# ------------------------------------------------------------
# 14. LOWEST 2 AGES
# ------------------------------------------------------------

result = df.nsmallest(2, "age")
print(result)

# Youngest two people.


# ------------------------------------------------------------
# 15. RANKING
# ------------------------------------------------------------

# rank() assigns a numerical rank to values.

df["rank"] = df["marks"].rank()
print(df)

# Default:
# Lowest value gets rank 1.
# Highest value gets the largest rank.


# ------------------------------------------------------------
# 16. RANK DESCENDING
# ------------------------------------------------------------

df["rank"] = df["marks"].rank(ascending=False)
print(df[["name", "marks", "rank"]])

# Highest marks get rank 1.


# ------------------------------------------------------------
# 17. RANKING WITH TIED VALUES
# ------------------------------------------------------------

# Priya and Sneha both scored 95.

print(df["marks"].rank(ascending=False))

# Default method is average.
#
# Both 95 values share ranks 1 and 2.
# Their assigned rank is:
# (1 + 2) / 2 = 1.5


# ------------------------------------------------------------
# 18. RANK METHOD: MIN
# ------------------------------------------------------------

df["rank_min"] = df["marks"].rank(
    ascending=False,
    method="min"
)
print(df[["name", "marks", "rank_min"]])

# Tied values receive the lowest rank in their group.
# 95, 95 -> 1, 1
# Next value -> 3


# ------------------------------------------------------------
# 19. RANK METHOD: DENSE
# ------------------------------------------------------------

df["rank_dense"] = df["marks"].rank(
    ascending=False,
    method="dense"
)
print(df[["name", "marks", "rank_dense"]])

# 95, 95 -> 1, 1
# 88 -> 2
# 85 -> 3
# 78 -> 4   


# ------------------------------------------------------------
# 20. RANK METHOD: FIRST
# ------------------------------------------------------------

df["rank_first"] = df["marks"].rank(
    ascending=False,
    method="first"
)
print(df[["name", "marks", "rank_first"]])

# Ties are ranked according to their original row order.


# ------------------------------------------------------------
# 21. SORT AFTER RANKING
# ------------------------------------------------------------

df["rank"] = df["marks"].rank(
    ascending=False,
    method="dense"
)
result = df.sort_values("rank")
print(result[["name", "marks", "rank"]])

# Highest marks first, with rank.


# ------------------------------------------------------------
# 22. REAL-WORLD EXAMPLE: STUDENT RANK LIST
# ------------------------------------------------------------

students = pd.DataFrame({
    "student": ["A", "B", "C", "D", "E"],
    "marks": [90, 85, 98, 90, 76]
})
students["rank"] = students["marks"].rank(
    ascending=False,
    method="dense"
)

students = students.sort_values("rank")
print(students)

# Highest marks receive rank 1.
# Equal marks receive the same dense rank.


# ------------------------------------------------------------
# MOST IMPORTANT PATTERNS
# ------------------------------------------------------------

# Ascending:
# df.sort_values("marks")

# Descending:
# df.sort_values("marks", ascending=False)

# Multiple columns:
# df.sort_values(["marks", "age"])

# Different sorting directions:
# df.sort_values(
#     ["marks", "age"],
#     ascending=[False, True]
# )

# Sort index:
# df.sort_index()

# Top 3:
# df.nlargest(3, "marks")

# Bottom 3:
# df.nsmallest(3, "marks")

# Rank:
# df["rank"] = df["marks"].rank()

# Highest gets rank 1:
# df["rank"] = df["marks"].rank(ascending=False)

# Dense ranking:
# df["rank"] = df["marks"].rank(
#     ascending=False,
#     method="dense"
# )
