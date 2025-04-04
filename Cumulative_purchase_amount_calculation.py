# Cumulative purchase amount calculation for each customer
# using pandasDataFrame and groupby function

import pandas as pd

# Create a DataFrame with customer ID and purchase amounts
# and calculate cumulative purchase amount for each customer

n = int(input("Enter number of purchase records: "))
data = {'customer_id': [], 'purchase_amount': [], 'date_of_purchase': []}

for i in range(n):
    customer_id = int(input(f"Enter customer ID for record {i+1}: "))
    purchase_amount = float(input(f"Enter purchase amount for record {i+1}: "))
    date_of_purchase = input(f"Enter date of purchase for record {i+1} (YYYY-MM-DD): ")
    
    data['customer_id'].append(customer_id)
    data['purchase_amount'].append(purchase_amount)
    data['date_of_purchase'].append(date_of_purchase)

df = pd.DataFrame(data)

# Convert date column to datetime and sort
df['date_of_purchase'] = pd.to_datetime(df['date_of_purchase'])
df = df.sort_values(by=['customer_id', 'date_of_purchase'])

# Add cumulative sum column
df['cumulative_purchase'] = df.groupby('customer_id')['purchase_amount'].cumsum()

print("\nDataFrame with Cumulative Purchase Amount:\n", df)