# PHASE 19: NUMERICAL AND DATA ANALYSIS WITH PANDAS

import pandas as pd
import numpy as np

# --------------------------------------------------
# 1. CREATE A SAMPLE DATASET
# --------------------------------------------------

df = pd.DataFrame({
    "student": ["A", "B", "C", "D", "E", "F"],
    "hours_studied": [2, 3, 4, 5, 6, 8],
    "sleep_hours": [8, 7, 7, 6, 6, 5],
    "marks": [45, 50, 60, 65, 75, 95],
    "department": ["CSE", "ECE", "CSE", "IT", "ECE", "CSE"]
})

print(df)


# --------------------------------------------------
# 2. SUMMARY STATISTICS
# --------------------------------------------------

# Describe numerical columns using common statistics.
print(df.describe())

# Select only numerical columns.
numeric_df = df.select_dtypes(include="number")

# Number of non-missing values in each column.
print(numeric_df.count())

# Mean of each numerical column.
print(numeric_df.mean())

# Median of each numerical column.
print(numeric_df.median())

# Minimum and maximum.
print(numeric_df.min())
print(numeric_df.max())

# Range = maximum - minimum.
print(numeric_df.max() - numeric_df.min())


# --------------------------------------------------
# 3. MEAN
# --------------------------------------------------

# Mean = sum of values / number of values.

print(df["marks"].mean())
# Output: 65.0

# Mean is sensitive to extreme values.
marks_with_outlier = pd.Series([45, 50, 60, 65, 75, 200])

print(marks_with_outlier.mean())
# Output: 82.5


# --------------------------------------------------
# 4. MEDIAN
# --------------------------------------------------

# Median is the middle value after sorting.
# For an even number of values, it is the mean of
# the two middle values.

print(df["marks"].median())
# Output: 62.5

print(marks_with_outlier.median())
# Output: 62.5

# Compare mean and median when outliers exist.
print("Mean:", marks_with_outlier.mean())
print("Median:", marks_with_outlier.median())


# --------------------------------------------------
# 5. STANDARD DEVIATION
# --------------------------------------------------

# Standard deviation measures how spread out values are.
# A larger standard deviation means greater variability.
# Pandas uses sample standard deviation by default: ddof=1.

print(df["marks"].std())

# Population standard deviation.
print(df["marks"].std(ddof=0))

# Sample standard deviation.
print(df["marks"].std(ddof=1))


# --------------------------------------------------
# 6. VARIANCE
# --------------------------------------------------

# Variance measures spread using squared deviations
# from the mean.
# Sample variance uses ddof=1 by default.

print(df["marks"].var())

# Population variance.
print(df["marks"].var(ddof=0))

# Relationship:
# Standard deviation = square root of variance.

print(np.sqrt(df["marks"].var()))
# Same as df["marks"].std()


# --------------------------------------------------
# 7. QUANTILES AND PERCENTILES
# --------------------------------------------------

# Quantile 0.25 = 25th percentile.
# Quantile 0.50 = 50th percentile (median).
# Quantile 0.75 = 75th percentile.

print(df["marks"].quantile(0.25))
print(df["marks"].quantile(0.50))
print(df["marks"].quantile(0.75))

# Calculate several quantiles together.
print(df["marks"].quantile([0, 0.25, 0.50, 0.75, 1]))

# The interquartile range (IQR) measures the spread
# of the middle 50% of observations.
q1 = df["marks"].quantile(0.25)
q3 = df["marks"].quantile(0.75)

iqr = q3 - q1
print("IQR:", iqr)

# Common IQR-based potential outlier boundaries.
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

potential_outliers = df[
    (df["marks"] < lower_bound) |
    (df["marks"] > upper_bound)
]

print(potential_outliers)


# --------------------------------------------------
# 8. CORRELATION
# --------------------------------------------------

# Correlation measures the strength and direction of a linear relationship between numerical columns.
# Pearson correlation ranges from -1 to +1.

# +1: perfect positive linear relationship.
#  0: no linear correlation.
# -1: perfect negative linear relationship.

corr_matrix = df[[
    "hours_studied",
    "sleep_hours",
    "marks"
]].corr()

print(corr_matrix)

# Correlation between two specific columns.
print(df["hours_studied"].corr(df["marks"]))
print(df["sleep_hours"].corr(df["marks"]))

# Sort correlations with marks, excluding marks itself.
correlations_with_marks = (
    corr_matrix["marks"]
    .drop("marks")
    .sort_values(ascending=False)
)

print(correlations_with_marks)

# Important:
# Correlation does not prove causation.
# A relationship does not establish that one variable causes another variable to change.


# --------------------------------------------------
# 9. COVARIANCE
# --------------------------------------------------

# Covariance describes whether two variables tend to move in the same or opposite directions.
# Its magnitude depends on the variables' units.

cov_matrix = df[[
    "hours_studied",
    "sleep_hours",
    "marks"
]].cov()

print(cov_matrix)

# Covariance between two columns.
print(df["hours_studied"].cov(df["marks"]))

# Positive covariance: variables tend to move together.
# Negative covariance: one tends to rise as the other falls.
# Near-zero covariance: little linear co-movement.


# --------------------------------------------------
# 10. FREQUENCY TABLES
# --------------------------------------------------

# Count each unique category.
print(df["department"].value_counts())

# Include missing values in the frequency table.
print(df["department"].value_counts(dropna=False))

# Relative frequency as proportions.
print(df["department"].value_counts(normalize=True))

# Relative frequency as percentages.
print(df["department"].value_counts(normalize=True) * 100)

# Frequency table including categories that do not occur.
department_order = pd.Categorical(
    df["department"],
    categories=["CSE", "ECE", "IT", "MECH"]
)

print(department_order.value_counts(sort=False))


# --------------------------------------------------
# 11. FREQUENCY TABLES WITH GROUPBY
# --------------------------------------------------

# Count records in each department.
print(df.groupby("department").size())

# Average marks in each department.
print(df.groupby("department")["marks"].mean())

# Multiple statistics for each department.
department_summary = df.groupby("department").agg(
    student_count=("student", "count"),
    average_marks=("marks", "mean"),
    highest_marks=("marks", "max"),
    lowest_marks=("marks", "min")
)

print(department_summary)


# --------------------------------------------------
# 12. DISTRIBUTION BASICS
# --------------------------------------------------

# A distribution describes how values are spread out.
# Look at the center, spread, shape and possible outliers.

print(df["marks"].describe())

# Skewness describes asymmetry.
# Positive skew: longer tail toward higher values.
# Negative skew: longer tail toward lower values.
# Near zero: approximately symmetric, though not guaranteed.

print("Skewness:", df["marks"].skew())

# Kurtosis describes tail heaviness relative to a normal distribution under Pandas' default excess-kurtosis convention.
print("Excess kurtosis:", df["marks"].kurt())

# Frequency of each exact mark.
print(df["marks"].value_counts().sort_index())

# Group marks into intervals (bins).
mark_bins = pd.cut(
    df["marks"],
    bins=[0, 50, 60, 70, 80, 100],
    right=True
)

print(mark_bins.value_counts().sort_index())

# Plot a histogram to inspect the distribution.
# Run this in an environment with plotting support.

df["marks"].plot.hist(
    bins=5,
    title="Distribution of Marks",
    xlabel="Marks"
)


# --------------------------------------------------
# 13. ANALYZE MISSING NUMERICAL DATA
# --------------------------------------------------

df_missing = df.copy()
df_missing.loc[2, "marks"] = np.nan

# Pandas statistical methods generally skip NaN values.
print(df_missing["marks"].mean())
print(df_missing["marks"].median())
print(df_missing["marks"].std())

# Count missing values in each column.
print(df_missing.isna().sum())

# Correlation uses available paired observations.
print(df_missing[[
    "hours_studied",
    "marks"
]].corr())
 

# --------------------------------------------------
# 14. PRACTICAL DATA ANALYSIS QUESTIONS
# --------------------------------------------------

# Question 1: What is the average mark?
print("Average marks:", df["marks"].mean())

# Question 2: What is the median mark?
print("Median marks:", df["marks"].median())

# Question 3: Which student scored the maximum?
top_student = df.loc[df["marks"].idxmax()]
print("Top student:")
print(top_student)

# Question 4: Which student studied the most?
most_studied = df.loc[df["hours_studied"].idxmax()]
print("Most study hours:")
print(most_studied)

# Question 5: What is the relationship between study hours
# and marks?
print(
    "Study hours vs marks correlation:",
    df["hours_studied"].corr(df["marks"])
)

# Question 6: Which department has the highest average marks?
average_by_department = (
    df.groupby("department")["marks"]
    .mean()
    .sort_values(ascending=False)
)

print(average_by_department)

# Question 7: What percentage of students belong to each department?
print(df["department"].value_counts(normalize=True) * 100)

# Question 8: What is the spread of marks?
print("Standard deviation:", df["marks"].std())
print("Variance:", df["marks"].var())
print("Range:", df["marks"].max() - df["marks"].min())

# Question 9: What marks define the middle 50%?
print("Q1:", df["marks"].quantile(0.25))
print("Q3:", df["marks"].quantile(0.75))
print("IQR:", df["marks"].quantile(0.75) -
      df["marks"].quantile(0.25))


# --------------------------------------------------
# 15. MACHINE LEARNING DATA ANALYSIS PATTERN
# --------------------------------------------------

# Numerical features for a simple dataset.
features = df[["hours_studied", "sleep_hours"]]
target = df["marks"]

# Understand feature distributions.
print(features.describe())

# Understand feature relationships.
print(features.corr())

# Understand each feature's variability.
print(features.std())

# Check missing values before model training.
print(features.isna().sum())
print(target.isna().sum())

# This is exploratory analysis, not model training.
# Correlation alone is not enough to select features.


"""
A. Mean vs median

Consider these salaries: [25000, 28000, 30000, 32000, 200000]

- Mean: increases significantly because of the unusually high salary.
- Median: stays closer to what a typical person in this group earns.

For ML engineering, remember:
- Use the mean when it reasonably represents the data.
- Consider the median when data contains strong outliers or is skewed.
- Do not automatically remove outliers. They might be genuine observations.

B. Variance vs standard deviation

Function	Meaning	Unit
var()	Measures squared spread around the mean	Squared units
std()	Square root of variance	Original units

For example, if marks are measured in points, standard deviation is measured in points, while variance is measured in squared points.

Pandas uses sample variance and sample standard deviation by default (ddof=1).
Use ddof=0 when calculating population statistics for the entire population of interest.


C. Quantiles

Example: sorted marks
45

Minimum
50

Q1 60

Median area 65

Median area 75

Q3 95

Maximum
Quantiles divide sorted observations into portions. 
Exact quantile values can be interpolated, so they do not always equal an observed value.

- quantile(0.25) gives the 25th percentile.
- quantile(0.50) gives the median.
- quantile(0.75) gives the 75th percentile.
- IQR = Q3 - Q1 measures the spread of the middle 50% of the data.

These concepts are useful for outlier investigation and understanding feature distributions before ML training.

D. Correlation vs covariance

            Correlation	                             Covariance
Always between -1 and +1 for Pearson correlation |	No fixed range
Standardized measure	                         |   Depends on the units of the variables
Easier to compare relationships between features |	Shows whether variables tend to move together

Important: A strong correlation does not prove causation. Also, a correlation near zero does not rule out a nonlinear relationship.
E. Distribution basics

When you analyze a numerical column, ask four questions:

1. Center: What are its mean and median?
2. Spread: What are its standard deviation, range and IQR?
3. Shape: Is it approximately symmetric or skewed?
4. Outliers: Are there unusual values that require investigation?

Use describe(), skew(), kurt(), value_counts() and histograms to investigate these questions.


4. The Pandas methods to remember
Method	Main purpose
describe()       	Quick numerical summary
mean() / median()	Central tendency
std() / var()	    Variability
min() / max()	    Extreme values
quantile()	        Percentiles and quartiles
corr() / cov()   	Relationships between numerical variables
value_counts()	    Frequency of values or categories
groupby().agg()	    Compare statistics across groups
skew() / kurt()    	Distribution shape
plot.hist()	        Visualize a numerical distribution


5. What matters for your AI/ML Engineering career

Focus on being able to take an unfamiliar dataset and answer practical questions, not merely memorize methods.

- Identify numerical and categorical features.
- Summarize numerical columns and examine missing values.
- Detect skewness and investigate potential outliers.
- Compare features using correlation while understanding its limitations.
- Analyze categories and groups using frequency tables and groupby.
- Decide what needs further investigation before preprocessing and model training.
Your Phase 19 completion target: Given an unfamiliar CSV file, 
you should be able to load it, summarize its numerical features, 
analyze distributions, investigate outliers, calculate correlations, and explain the findings in plain language.

You do not need advanced statistical theory yet. 
Master these Pandas techniques first, then build on them when you study probability, 
hypothesis testing, feature engineering and model evaluation.
"""