import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Load Data
df = pd.read_csv('transactions.csv')

# 2. Transform data for AI (One-Hot Encoding)
# We turn the list of items into columns of 0s and 1s
basket = df['Items'].str.get_dummies(sep=', ').astype(bool)

# 3. Find Frequent Itemsets
frequent_itemsets = apriori(basket, min_support=0.05, use_colnames=True)

# 4. Generate Association Rules (The "If-Then" patterns)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

print("✅ Analysis Complete! Top product associations found:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head())