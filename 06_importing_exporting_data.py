import pandas as pd

# 1. Read a CSV file

df = pd.read_csv("students.csv")
print(df)

# Output:
#     name  age  marks
# 0   Ravi   20     85
# 1  Rahul   21     92
# 2   Anil   19     78


# 2. File path
df = pd.read_csv("data/students.csv")

# Windows path:
# df = pd.read_csv(r"C:\Users\Sathvik\data\students.csv")
# r before the path prevents backslash problems.


# 3. Read an Excel file

df = pd.read_excel("students.xlsx")
print(df.head())

# Output:
#     name  age  marks
# 0   Ravi   20     85
# 1  Rahul   21     92
# 2   Anil   19     78


# 4. Read a JSON file
df = pd.read_json("students.json")
print(df)

# Output:
#     name  age  marks
# 0   Ravi   20     85
# 1  Rahul   21     92
# 2   Anil   19     78


# 5. CSV without a header
df = pd.read_csv(
    "students.csv",
    header=None,
    names=["name", "age", "marks"]
)
print(df)

# Output:
#     name  age  marks
# 0   Ravi   20     85
# 1  Rahul   21     92
# 2   Anil   19     78



# 6. Select columns while reading
df = pd.read_csv(
    "students.csv",
    usecols=["name", "marks"]
)

print(df)

# Output:
#     name  marks
# 0   Ravi     85
# 1  Rahul     92
# 2   Anil     78


# 7. Delimiter
# Normal CSV uses comma:
# name,age,marks

# If the file uses | instead:
df = pd.read_csv("students.txt", sep="|")


# 8. Encoding

df = pd.read_csv(
    "students.csv",
    encoding="utf-8"
)
# UTF-8 is the normal choice for most files.


# 9. Export DataFrame to CSV
df.to_csv("output.csv", index=False)

# index=False prevents Pandas from writing
# the DataFrame index as an extra column.


# 10. Export to Excel
df.to_excel("output.xlsx", index=False)


# 11. Export to JSON
df.to_json("output.json", orient="records", indent=4)


# 12. Complete CSV workflow
df = pd.read_csv("students.csv")
print(df.head())

# Clean/select data
df = df[["name", "marks"]]

# Export result
df.to_csv("clean_students.csv", index=False)


# 13. Large CSV basics
# Do NOT always load a huge CSV completely into memory.

# Read only required columns:
df = pd.read_csv(
    "large_data.csv",
    usecols=["age", "salary", "score"]
)

# Read data in chunks:
for chunk in pd.read_csv("large_data.csv", chunksize=10000):
    print(chunk.shape)

# Each chunk contains 10,000 rows.


# 14. File handling → Pandas
# Traditional Python:

# File
#   ↓
# open()
#   ↓
# read()
#   ↓
# process manually

# With Pandas:

# CSV / JSON / Excel
#       ↓
#  pd.read_csv()
#  pd.read_json()
#  pd.read_excel()
#       ↓
#    DataFrame
#       ↓
# Clean / Analyze / ML


# 15. Important patterns

df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")


# Remember:

# read_csv()   -> CSV → DataFrame
# read_excel() -> Excel → DataFrame
# read_json()  -> JSON → DataFrame

# to_csv()     -> DataFrame → CSV
# to_excel()   -> DataFrame → Excel
# to_json()    -> DataFrame → JSON

# index=False  -> don't save DataFrame index
# usecols      -> read only required columns
# sep          -> specify delimiter
# encoding     -> specify text encoding
# chunksize    -> process large files in pieces
