import pandas as pd 
from sqlalchemy import create_engine
import csv


def fetch_data_sql():
    sql = "select * from more_50K_data"
    engine = create_engine('postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB')

    with engine.connect().execution_options() as conn:
        query = conn.execute(sql)        
    df = pd.DataFrame(query.fetchall())
    df.to_csv("output.csv",index=False)
    print(df)

fetch_data_sql()
