# # from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB', echo = True)

import pandas as pd 
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.sql import text

def select(table_name, columns, distinct=False):
    columns = str(columns).strip("[]").replace("'",'')
    if columns.casefold()=='all' or columns.casefold()=='*':
        if distinct:
            return f"SELECT DISTINCT * FROM {table_name};"
        else:
            return f"SELECT * FROM {table_name};"
    else:
        if distinct:
            return f"SELECT DISTINCT {columns}  FROM {table_name};"
        else:
            return f"SELECT {columns}  FROM {table_name};"



sql = select('clinic',"all",False)
print(sql)

# print(select('clinic',"all",False))
# print(select('clinic',["clinic_id's", "clinic_name"],True))
# print(select('clinic','*',True))

url = 'postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB'
engine = sqlalchemy.create_engine(url)

with engine.connect().execution_options(autocommit=True) as conn:
    query = conn.execute(text(sql))         
df = pd.DataFrame(query.fetchall())
print(df)