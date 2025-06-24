import pandas as pd
df = pd.read_csv('data/features/v1.csv')
df['Age'].fillna(df['Age'].mean(), inplace=True)
df.to_csv('data/features/v2.csv', index=False)
