# Handaling missing values in a DataFrame.
# This code snippet demonstrates how to handle missing values in a DataFrame using pandas.
import pandas as pd
import numpy as np

n = int(input("Enter number of records: "))
data = {'id': [], 'value': []}

for i in range(n):
    _id = int(input(f"Enter id for record {i+1}: "))
    value = input(f"Enter value for record {i+1} (leave blank for missing): ")
    data['id'].append(_id)
    data['value'].append(float(value) if value else np.nan)

df = pd.DataFrame(data)

# Handling missing values
print("\nOriginal DataFrame:\n", df)
print("\nDataFrame after filling missing values with 0:\n", df.fillna(0))
print("\nDataFrame after dropping missing values:\n", df.dropna())