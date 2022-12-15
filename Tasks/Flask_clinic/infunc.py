from cProfile import label
from operator import or_
from optparse import Values
from sqlalchemy.orm import sessionmaker
# import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func, select, text, Integer, String, Column, Float

# IMPORT THE REQUIRED LIBRARY
import sqlalchemy as db
Base = declarative_base()
# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine('postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB')
				
meta_data = db.MetaData(bind=engine)
db.MetaData.reflect(meta_data)
# # GET THE `category` TABLE FROM THE METADATA OBJECT
category_table = meta_data.tables['clinic_data']
# a = ["101", "108", "103"]
# # SELECT clinic_id, name FROM clinic_data
# query = db.select([category_table.c.clinic_id]).where(category_table.c.clinic_id.in_(a))

# # FETCH ALL THE RECORDS IN THE RESPONSE
# print(query,"--------------------------------------------")
# result = engine.execute(query).fetchall()

# # VIEW THE ENTRIES IN THE RESULT
# for record in result:
# 	print("\n", record)
class clinic_data(Base):

	__tablename__ = 'clinic_data'

	clinic_id = Column(String(50),primary_key=True)
	clinic_name = Column(String(50))
	Doctor_name = Column(String(50))
	longitute = Column(Float)
	Latitude = Column(Float)
	Postal_Code = Column(Integer)
	Phone_Number = Column(Integer)
	email_ID = Column(String)

import pandas as pd    
connection = engine.connect()					

# stmt = select(users_table).order_by(desc(users_table.c.name))
def order_by(table_name,columns):
	# columns = where_dict.keys()
	if isinstance(columns,str) and (columns.casefold()=='all' or columns.casefold()=='*'):
		columns = '*'
		a = [getattr(table_name,column.key) for column in table_name.__table__.columns]
		print(a,"----------------------------------")
		# columns = getattr(table_name, a)
		order_query = func.order_by(a)
		order_query = db.select([category_table.c.columns]).order_by(category_table.c.columns)
		print(order_query)
		return order_query

order_query = order_by(clinic_data,["clinic_name"])

#where_dict = {"clinic_name": {"operator": 'in', 'values': ('lilavati@gmail.com','wokhartks.gmail')}}

#order_query = db.select([category_table.c.doctor_name]).order_by(category_table.c.doctor_name)
print(order_query)	
# FETCH ALL THE RECORDS IN THE RESPONSE
# order_query = where_dict.keys()
result = engine.execute(order_query).fetchall()

df = pd.read_sql_query(order_query, connection)
print(df) 

# # VIEW THE ENTRIES IN THE RESULT
# # for record in result:
# # 	print("\n", record)
connection.close()




