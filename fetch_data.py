import os
import pandas as pd
from catboost.datasets import titanic

os.makedirs('data/raw', exist_ok=True)

train_df, test_df = titanic()  
full_df = pd.concat([train_df, test_df], ignore_index=True)
full_df.to_csv('data/raw/titanic.csv', index=False)
