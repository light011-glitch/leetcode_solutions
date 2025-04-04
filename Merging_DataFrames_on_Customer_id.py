# Merging DataFrames on Customer_id


n1 = int(input("Enter number of records for customer details: "))
data1 = {'customer_id': [], 'name': []}

for i in range(n1):
    customer_id = int(input(f"Enter customer ID for record {i+1}: "))
    name = input(f"Enter customer name for record {i+1}: ")
    data1['customer_id'].append(customer_id)
    data1['name'].append(name)

df1 = pd.DataFrame(data1)

# Taking dynamic input for second DataFrame
n2 = int(input("Enter number of records for purchase data: "))
data2 = {'customer_id': [], 'purchase_amount': []}

for i in range(n2):
    customer_id = int(input(f"Enter customer ID for record {i+1}: "))
    purchase_amount = float(input(f"Enter purchase amount for record {i+1}: "))
    data2['customer_id'].append(customer_id)
    data2['purchase_amount'].append(purchase_amount)

df2 = pd.DataFrame(data2)

# Merging on 'customer_id'
merged_df = pd.merge(df1, df2, on='customer_id', how='inner')

print("\nMerged DataFrame:\n", merged_df)