import pandas as pd
import random

products = ['Milk', 'Bread', 'Eggs', 'Butter', 'Cereal', 'Coffee', 'Diapers', 'Beer', 'Apple', 'Banana']
data = []

for i in range(1, 501):
    transaction_size = random.randint(2, 5)
    items = random.sample(products, transaction_size)
    data.append({'Transaction_ID': i, 'Items': ', '.join(items)})

df = pd.DataFrame(data)
df.to_csv('transactions.csv', index=False)
print("✅ Created transactions.csv with 500 records.")