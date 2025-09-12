Homework 1
import pandas as pd
import numpy as np

# Create DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Rename column names
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})

# 2. Print the first 3 rows
print("First 3 rows:")
print(df.head(3), "\n")

# 3. Mean age
print("Mean age:", df['age'].mean(), "\n")

# 4. Select and print only 'first_name' and 'City'
print("Name and City columns:")
print(df[['first_name', 'City']], "\n")

# 5. Add new column 'Salary' with random values
df['Salary'] = np.random.randint(40000, 80000, size=len(df))
print("With Salary column:")
print(df, "\n")

# 6. Summary statistics
print("Summary statistics:")
print(df.describe(include='all'))

✅ Homework 2
# Create DataFrame
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# 1. Max
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max(), "\n")

# 2. Min
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min(), "\n")

# 3. Average
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

✅ Homework 3
# Create DataFrame
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# Set 'Category' as index
expenses = expenses.set_index('Category')

# 1. Max expense per category
print("Maximum expenses:")
print(expenses.max(axis=1), "\n")

# 2. Min expense per category
print("Minimum expenses:")
print(expenses.min(axis=1), "\n")

# 3. Average expense per category
print("Average expenses:")
print(expenses.mean(axis=1))
