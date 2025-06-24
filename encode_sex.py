import pandas as pd
df = pd.read_csv('data/features/v2.csv')
df = pd.get_dummies(df, columns=['Sex'])
df.to_csv('data/features/v3.csv', index=False)
