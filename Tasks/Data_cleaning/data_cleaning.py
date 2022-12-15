import numpy as np
import pandas as pd

def data_cleaning(df):
    df['Dept'].replace(to_replace = ' ?', value = 'N/A', inplace=True)
    df['Occupation'].replace(to_replace = ' ?', value = 'N/A', inplace=True)
    df.replace(to_replace = ' ?', value = 'N/A', inplace=True)
    df_1 = df[df["Count"] == " <=50K"]
    df_2 = df[df["Count"] == " >50K"]
    df_1.to_csv("cleaned_csv/Less_50K_data.csv",index=False)
    df_2.to_csv("cleaned_csv/More_50K_data.csv",index=False)
    

df = pd.read_csv("adult.data.csv")
data_cleaning(df)










