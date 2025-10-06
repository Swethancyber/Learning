import pandas as pd 
import numpy as np

# Load the data
s = pd.read_csv("Google_data.csv")

# Read first 3 rows
c = s.head(3)
print("First 3 rows:\n", c)

# List last 3 rows
z = s.tail(3)
print("Last 3 rows:\n", z)

# Get info of the table
info = s.info()
print("Data Info:\n", info)

# Find and sum missing values
ms_value = s.isnull().sum()
print("Missing values per column:\n", ms_value)

# Imputation: fill missing 'Rating' values with mean
mean_va = s["Rating"].mean()
print("Mean Rating:", mean_va)

# Summary statistics (transposed)
summary_transposed = s.describe().T
print("Summary Statistics (Transposed):\n", summary_transposed)

# Summary statistics (default)
summary = s.describe()
print("Summary Statistics:\n", summary)

# Summary for object (categorical) columns
object_summary = s.describe(include=["object"])
print("Object Column Summary:\n", object_summary)

# Transposed summary for object columns
object_summary_transposed = s.describe(include=["object"]).T
print("Object Column Summary (Transposed):\n", object_summary_transposed)

# Count duplicate rows
duplicate_count = s.duplicated().sum()
print("Number of duplicate rows:", duplicate_count)

# Drop duplicate rows
s.drop_duplicates(inplace=True)
print("Duplicates dropped.")

# Value counts for 'Category' column
category_counts = s['Category'].value_counts()
print("Category Value Counts:\n", category_counts)

# Unique values in 'Category' column
unique_categories = s['Category'].unique()
print("Unique Categories:\n", unique_categories)

# Drop rows with missing 'Category'
s.dropna(subset=["Category"], inplace=True)
print("Rows with missing 'Category' dropped.")