# Pandas Phase 16: Combining DataFrames

import pandas as pd

# ==================================================
# 1. UNDERSTANDING WHY WE COMBINE DATAFRAMES
# ==================================================

# In real-world projects, data is usually stored
# in multiple tables/files.
# Example:

# Customers
# +
# Orders
# ↓
# Merge
# ↓

# Complete dataset

# ==================================================
# 2. CREATE TWO DATAFRAMES
# ==================================================

customers = pd.DataFrame({
"customer_id": [1, 2, 3, 4],
"name": ["Sathvik", "Rahul", "Priya", "Anil"],
"city": ["Vizag", "Hyderabad", "Chennai", "Bangalore"]
})

orders = pd.DataFrame({
"order_id": [101, 102, 103, 104],
"customer_id": [1, 2, 2, 5],
"amount": [500, 800, 300, 1000]
})

print("CUSTOMERS:")
print(customers)
print("\nORDERS:")
print(orders)

# ==================================================
# 3. pd.concat()
# ==================================================

# pd.concat() is mainly used to put DataFrames
# together vertically or horizontally.

# --------------------------------------------------
# 3.1 CONCATENATE ROWS
# --------------------------------------------------

df1 = pd.DataFrame({
"name": ["A", "B"],
"age": [20, 21]
})

df2 = pd.DataFrame({
"name": ["C", "D"],
"age": [22, 23]
})

# axis=0 means combine rows

combined_rows = pd.concat(
[df1, df2],
axis=0
)

print("\nCONCAT ROWS:")
print(combined_rows)

# --------------------------------------------------
# 3.2 RESET INDEX AFTER CONCAT
# --------------------------------------------------

combined_rows = pd.concat(
[df1, df2],
ignore_index=True
)
print("\nCONCAT ROWS WITH RESET INDEX:")
print(combined_rows)

# ignore_index=True creates a fresh index:

#

# 0

# 1

# 2

# 3

# ==================================================
# 4. CONCATENATE COLUMNS
# ==================================================

df3 = pd.DataFrame({
"name": ["A", "B", "C"],
"age": [20, 21, 22]
})

df4 = pd.DataFrame({
"city": ["Vizag", "Hyderabad", "Chennai"],
"salary": [30000, 40000, 50000]
})

# axis=1 means combine columns

combined_columns = pd.concat(
[df3, df4],
axis=1
)
print("\nCONCAT COLUMNS:")
print(combined_columns)

# ==================================================
# 5. CONCAT WITH DIFFERENT COLUMNS
# ==================================================

df5 = pd.DataFrame({
"name": ["A", "B"],
"age": [20, 21]
})

df6 = pd.DataFrame({
"name": ["C", "D"],
"city": ["Vizag", "Chennai"]
})
combined = pd.concat(
[df5, df6],
ignore_index=True
)

print("\nCONCAT WITH DIFFERENT COLUMNS:")
print(combined)

# Pandas creates NaN where a column
# does not exist in one DataFrame.


# ==================================================
# 6. CONCAT: IMPORTANT IDEA
# ==================================================

# concat() asks:

# "Do I want to simply put DataFrames

# together?"

# If YES → concat()

# Example:

# DataFrame 1

# A
# B

# DataFrame 2

# C
# D

# concat()


# A
# B
# C
# D

# ==================================================
# 7. pd.merge()
# ==================================================

# merge() combines DataFrames using
# a common column called a KEY.

# Example:


# Customers

# customer_id | name

# 1           | Sathvik
# 2           | Rahul

# Orders

# order_id | customer_id | amount
# 101      | 1            | 500
# 102      | 2            | 800

# customer_id is the JOIN KEY.


# ==================================================
# 8. INNER JOIN
# ==================================================

# Inner join returns only rows

# that have matching keys in BOTH DataFrames.

inner = pd.merge(
customers,
orders,
on="customer_id",
how="inner"
)

print("\nINNER JOIN:")
print(inner)

# customer_id 1 matches
# customer_id 2 matches
# customer_id 3 has no order → removed
# customer_id 4 has no order → removed
# customer_id 5 has no customer → removed

# ==================================================
# 9. LEFT JOIN
# ==================================================

# Left join keeps ALL rows from the LEFT DataFrame.

left = pd.merge(
customers,
orders,
on="customer_id",
how="left"
)
print("\nLEFT JOIN:")
print(left)

# Customers 1, 2, 3, 4 remain.

#

# Customers without orders get NaN

# in the order columns.


# ==================================================
# 10. RIGHT JOIN
# ==================================================

# Right join keeps ALL rows from the RIGHT DataFrame.

right = pd.merge(
customers,
orders,
on="customer_id",
how="right"
)
print("\nRIGHT JOIN:")
print(right)

# All orders remain.
# customer_id 5 has an order
# but no matching customer.
# Customer information becomes NaN.


# ==================================================
# 11. OUTER JOIN
# ==================================================

# Outer join keeps ALL rows from BOTH DataFrames.

outer = pd.merge(
customers,
orders,
on="customer_id",
how="outer"
)
print("\nOUTER JOIN:")
print(outer)

# Matching rows are combined.
# Non-matching rows from either side are also retained.

# ==================================================
# 12. UNDERSTANDING THE FOUR JOINS
# ==================================================

# INNER

# Only matching rows


# LEFT
# Everything from left + matching right

# RIGHT
# Everything from right + matching left

# OUTER
# Everything from both

# inner → intersection
# left  → keep left
# right → keep right
# outer → keep everything


# ==================================================
# 13. JOIN KEY
# ==================================================

# A join key is the column used to connect two DataFrames.

# Here:
# customers.customer_id
# orders.customer_id
# are the same key.

result = pd.merge(
customers,
orders,
on="customer_id"
)

print("\nJOIN USING customer_id:")
print(result)

# ==================================================
# 14. DIFFERENT COLUMN NAMES
# ==================================================

# Sometimes the key columns have

# different names.

customers2 = pd.DataFrame({
"customer_id": [1, 2, 3],
"name": ["A", "B", "C"]
})

orders2 = pd.DataFrame({
"buyer_id": [1, 2, 3],
"amount": [500, 700, 900]
})

# left_on = key from left DataFrame

# right_on = key from right DataFrame

result = pd.merge(
customers2,
orders2,
left_on="customer_id",
right_on="buyer_id",
how="inner"
)

print("\nDIFFERENT KEY COLUMN NAMES:")
print(result)

# ==================================================
# 15. MULTIPLE KEYS
# ==================================================

# Sometimes one column is not enough to uniquely identify a relationship.

# Example:

# student_id + subject

students = pd.DataFrame({
"student_id": [1, 1, 2, 2],
"subject": ["Math", "Physics", "Math", "Physics"],
"student_name": ["A", "A", "B", "B"]
})
marks = pd.DataFrame({
"student_id": [1, 1, 2, 2],
"subject": ["Math", "Physics", "Math", "Physics"],
"marks": [90, 85, 80, 88]
})

# Use a list of columns as keys

result = pd.merge(
students,
marks,
on=["student_id", "subject"],
how="inner"
)
print("\nMULTIPLE KEYS:")
print(result)

# ==================================================
# 16. MERGE USING THREE KEYS
# ==================================================

# Multiple keys can contain more than two columns.

df_left = pd.DataFrame({
"student_id": [1, 2, 3],
"subject": ["Math", "Math", "Physics"],
"semester": [1, 1, 2],
"name": ["A", "B", "C"]
})
df_right = pd.DataFrame({
"student_id": [1, 2, 3],
"subject": ["Math", "Math", "Physics"],
"semester": [1, 1, 2],
"marks": [90, 85, 88]
})
result = pd.merge(
df_left,
df_right,
on=["student_id", "subject", "semester"],
how="inner"
)

print("\nMERGE USING THREE KEYS:")
print(result)


# ==================================================
# 17. merge() WITH suffixes
# ==================================================

# If both DataFrames contain columns
# with the same name, Pandas adds suffixes.

employees1 = pd.DataFrame({
"employee_id": [1, 2, 3],
"name": ["A", "B", "C"],
"salary": [30000, 40000, 50000]
})
employees2 = pd.DataFrame({
"employee_id": [1, 2, 3],
"name": ["A", "B", "C"],
"salary": [32000, 42000, 52000]
})

result = pd.merge(
employees1,
employees2,
on="employee_id",
suffixes=("_old", "_new")
)

print("\nMERGE WITH SUFFIXES:")
print(result)

# ==================================================
# 18. validate MERGE RELATIONSHIPS
# ==================================================

# validate can help check whether the merge relationship is what you expected.

customers3 = pd.DataFrame({
"customer_id": [1, 2, 3],
"name": ["A", "B", "C"]
})
orders3 = pd.DataFrame({
"order_id": [101, 102, 103],
"customer_id": [1, 2, 2]
})

result = pd.merge(
customers3,
orders3,
on="customer_id",
how="left",
validate="one_to_many"
)

print("\nVALIDATED MERGE:")
print(result)

# One customer can have many orders.

# Therefore:
# one_to_many
# is appropriate here.

# ==================================================
# 19. pd.merge() USING INDEX
# ==================================================

# Sometimes the join key is the index.

left_index = pd.DataFrame({
"name": ["A", "B", "C"]
}, index=[1, 2, 3])
right_index = pd.DataFrame({
"salary": [30000, 40000, 50000]
}, index=[1, 2, 3])

result = pd.merge(
left_index,
right_index,
left_index=True,
right_index=True
)

print("\nMERGE USING INDEX:")
print(result)

# ==================================================
# 20. join()
# ==================================================

# join() is another way to combine DataFrames.
# It is especially convenient when joining using indexes.

students = pd.DataFrame({
"name": ["A", "B", "C"]
}, index=[1, 2, 3])

marks = pd.DataFrame({
"marks": [90, 80, 95]
}, index=[1, 2, 3])

result = students.join(marks)

print("\nJOIN:")
print(result)

# ==================================================
# 21. join() WITH LEFT JOIN
# ==================================================

students = pd.DataFrame({
"name": ["A", "B", "C", "D"]
}, index=[1, 2, 3, 4])

marks = pd.DataFrame({
"marks": [90, 80, 95]
}, index=[1, 2, 3])

result = students.join(
marks,
how="left"
)
print("\nJOIN WITH LEFT JOIN:")
print(result)

# Student 4 remains.
# Since student 4 has no marks, marks becomes NaN.

# ==================================================
# 22. join() WITH INNER JOIN
# ==================================================

result = students.join(
marks,
how="inner"
)
print("\nJOIN WITH INNER JOIN:")
print(result)

# Only matching indexes remain.

# ==================================================
# 23. join() USING on
# ==================================================

# join() can also join using a column

# from the left DataFrame against

# the index of the right DataFrame.

students = pd.DataFrame({
"student_id": [1, 2, 3],
"name": ["A", "B", "C"]
})

marks = pd.DataFrame({
"marks": [90, 80, 95]
}, index=[1, 2, 3])

result = students.join(
marks,
on="student_id"
)

print("\nJOIN USING A COLUMN:")
print(result)

# ==================================================
# 24. CONCAT vs MERGE vs JOIN
# ==================================================

# CONCAT

# Used to simply combine DataFrames
# vertically or horizontally.

# Example:

# January data + February data
# Use concat()


# MERGE

# Used to combine DataFrames
# based on common key columns.

# Example:
# Customers + Orders
# customer_id
# Use merge()


# JOIN

# Mainly useful for combining DataFrames
# using their indexes.


# ==================================================
# 25. PRACTICAL CUSTOMER + ORDERS EXAMPLE
# ==================================================

customers = pd.DataFrame({
"customer_id": [1, 2, 3, 4, 5],
"name": [
"Sathvik",
"Rahul",
"Priya",
"Anil",
"Sneha"
],
"city": [
"Vizag",
"Hyderabad",
"Chennai",
"Bangalore",
"Delhi"
]
})

orders = pd.DataFrame({
"order_id": [101, 102, 103, 104, 105, 106],
"customer_id": [1, 2, 2, 3, 5, 2],
"product": [
"Laptop",
"Mouse",
"Keyboard",
"Monitor",
"Phone",
"Headphones"
],
"amount": [
60000,
1000,
2500,
15000,
30000,
2000
]
})

# Merge customers and orders

complete_data = pd.merge(
customers,
orders,
on="customer_id",
how="inner"
)
print("\nCOMPLETE CUSTOMER + ORDER DATA:")
print(complete_data)

# ==================================================
# 26. CUSTOMER ORDER SUMMARY
# ==================================================

# Now that the data is combined,

# we can perform analysis.

customer_summary = complete_data.groupby(
["customer_id", "name"]
)["amount"].sum()
print("\nTOTAL SPENDING BY CUSTOMER:")
print(customer_summary)

# ==================================================
# 27. LEFT MERGE FOR ALL CUSTOMERS
# ==================================================

# If we want every customer, even customers who never placed an order:

all_customers = pd.merge(
customers,
orders,
on="customer_id",
how="left"
)

print("\nALL CUSTOMERS WITH THEIR ORDERS:")
print(all_customers)


# ==================================================
# 28. FIND CUSTOMERS WITHOUT ORDERS
# ==================================================
# After a left merge, customers with no orders will have NaN in order_id.

customers_without_orders = all_customers[
all_customers["order_id"].isna()
]
print("\nCUSTOMERS WITHOUT ORDERS:")
print(customers_without_orders)



# ==================================================
# 29. PRACTICAL ML EXAMPLE
# ==================================================
# In ML, you may have:


# Customer features
# +
# Transaction information
# +
# Target/label


# These can be combined before creating the final training dataset.

customer_features = pd.DataFrame({
"customer_id": [1, 2, 3, 4],
"age": [20, 25, 30, 35],
"city": ["Vizag", "Hyderabad", "Chennai", "Delhi"]
})

customer_target = pd.DataFrame({
"customer_id": [1, 2, 3, 4],
"churn": [0, 1, 0, 1]
})

# Combine features and target

ml_dataset = pd.merge(
customer_features,
customer_target,
on="customer_id",
how="inner"
)

print("\nML DATASET:")
print(ml_dataset)


# ==================================================
# 30. MULTIPLE DATAFRAMES
# ==================================================
# concat() can combine more than two DataFrames.

jan = pd.DataFrame({
"month": ["January", "January"],
"sales": [1000, 1500]
})

feb = pd.DataFrame({
"month": ["February", "February"],
"sales": [2000, 2500]
})

march = pd.DataFrame({
"month": ["March", "March"],
"sales": [1800, 2200]
})

all_sales = pd.concat(
[jan, feb, march],
ignore_index=True
)

print("\nCOMBINING THREE DATAFRAMES:")
print(all_sales)



# ==================================================
# 31. IMPORTANT: DUPLICATES AFTER MERGE
# ==================================================
# A merge can create multiple rows
# when one key appears multiple times.

customers = pd.DataFrame({
"customer_id": [1, 2],
"name": ["A", "B"]
})

orders = pd.DataFrame({
"customer_id": [1, 1, 1, 2],
"amount": [100, 200, 300, 400]
})

result = pd.merge(
customers,
orders,
on="customer_id",
how="inner"
)

print("\nONE CUSTOMER WITH MULTIPLE ORDERS:")
print(result)

# Customer 1 appears three times
# because customer 1 has three orders.


# This is NOT automatically a duplicate error.


# It represents a one-to-many relationship.


# ==================================================
# 32. FINAL PRACTICE
# ==================================================


employees = pd.DataFrame({
"employee_id": [1, 2, 3, 4],
"name": ["A", "B", "C", "D"],
"department_id": [10, 20, 10, 30]
})

departments = pd.DataFrame({
"department_id": [10, 20, 30],
"department": [
"AI",
"Software",
"Data"
]
})

# Merge employee data with department data

final = pd.merge(
employees,
departments,
on="department_id",
how="left"
)

print("\nFINAL PRACTICE:")
print(final)




# ==================================================
# 33. QUICK REVISION
#==================================================

"""
CONCAT
Combine DataFrames vertically/horizontally
pd.concat([df1, df2])

MERGE
Combine using a key
pd.merge(df1, df2, on="id")


INNER
Matching rows only
how="inner"

LEFT
Keep everything from left
how="left"

RIGHT
Keep everything from right
how="right"

OUTER
Keep everything from both
how="outer"


MULTIPLE KEYS
on=["id", "subject"]


JOIN
Convenient for index-based combination
df1.join(df2)

"""

### 🔥 The core idea you must remember

# Think about two DataFrames:


'''
# CUSTOMERS
+----------------+
| customer_id    |
| name           |
| city           |
+----------------+

ORDERS
+----------------+
| order_id       |
| customer_id    |
| amount         |
+----------------+
        |
        | customer_id
        ↓
      MERGE
        ↓
+--------------------------------+
| customer_id | name | amount    |
+--------------------------------+

The customer_id is the join key.

The 3 functions you must clearly distinguish
Function      |	 Main purpose                     |	    Example
pd.concat()	    Put DataFrames together 	            Jan + Feb data
pd.merge()	    Combine using key columns	            Customers + Orders
join()	        Conveniently combine using indexes	    Student + Marks


🔥 Join types
INNER
Only matching
A ∩ B

LEFT
Everything from A
+ matching B

RIGHT
Everything from B
+ matching A

OUTER
Everything from A + B
The most important syntax to memorize:
'''

# Inner
pd.merge(df1, df2, on="id", how="inner")

# Left
pd.merge(df1, df2, on="id", how="left")

# Right
pd.merge(df1, df2, on="id", how="right")

# Outer
pd.merge(df1, df2, on="id", how="outer")

# Multiple keys
pd.merge(
    df1,
    df2,
    on=["id", "subject"],
    how="inner"
)

# Concatenate rows
pd.concat([df1, df2], ignore_index=True)

# Join
df1.join(df2)

'''
🎯 Phase 16 mastery target

Before moving to Phase 17, you should be able to look at:
Customers + Orders
and immediately understand:

"I need merge(), the common column is my key, and I choose 
inner/left/right/outer depending on which rows I need to preserve."

This is a core Pandas skill for ML Engineering, 
because later you'll use the same concept when combining features, 
labels, user information, transactions, and other datasets.
'''