# Filter DataFrame based on specific conditions
# Importing pandas library

import pandas as pd

# Taking dynamic input
n = int(input("Enter number of records: "))
data = {'id': [], 'age': [], 'score': []}

for i in range(n):
    _id = int(input(f"Enter id for record {i+1}: "))
    age = int(input(f"Enter age for record {i+1}: "))
    score = int(input(f"Enter score for record {i+1}: "))
    data['id'].append(_id)
    data['age'].append(age)
    data['score'].append(score)

df = pd.DataFrame(data)

# Filtering rows where age > 25 and score > 80
filtered_df = df[(df['age'] > 25) & (df['score'] > 80)]
print("\nFiltered DataFrame:\n", filtered_df)