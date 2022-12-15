from emailswapnil import data_cleaning
import pandas as pd

df = pd.read_csv('file1.csv')
df = data_cleaning(df)
print(df)
