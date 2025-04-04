#Group sales data by region and sum sales
# Import necessary libraries

import pandas as pd
import numpy as np

# Create a DataFrame with sales data
# Initialize an empty DataFrame

df_sales = pd.DataFrame(columns=['date', 'region', 'sales'])
# Prompt user for number of records and input data

n = int(input("Enter number of records: "))
data = {'date': [], 'region': [], 'sales': []}

for i in range(n):
    date = input(f"Enter date for record {i+1} (YYYY-MM-DD): ")
    region = input(f"Enter region for record {i+1}: ")
    sales = float(input(f"Enter sales for record {i+1}: "))
    data['date'].append(date)
    data['region'].append(region)
    data['sales'].append(sales)

df_sales = pd.DataFrame(data)

# Group by region and sum sales
grouped_sales = df_sales.groupby('region')['sales'].sum()
print("\nTotal Sales by Region:\n", grouped_sales)