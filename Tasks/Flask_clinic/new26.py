from cProfile import label
from operator import or_
from optparse import Values
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func, select, text, Integer, String, Column, Float
# from sqlalchemy_filters import apply_filters

Base = declarative_base()
# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine('postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB')
# Base.metadata.create_all(engine)
# CREATE THE TABLE MODEL TO USE IT FOR QUERYING
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
	


def get_select(table_name, columns, distinct=False,aggrigations=None,label=None):
    query1 = [] # columns = str(columns).strip("[]").replace("'",'')
    if isinstance(columns,str) and (columns.casefold()=='all' or columns.casefold()=='*'):
        columns = '*'
        if distinct:
            # return db.select([func.distinct(table_name.columns)])
            a = [getattr(table_name,column.key) for column in table_name.__table__.columns]
            query = func.distinct(a)
            # print(text(query),"--------------------------------------")
            query1.append(query)
            
        # else:
        #     return f"* FROM {table_name.__tablename__}"
            # # query = db.select([table_name])
            # return a
            # return f"SELECT * FROM {table_name};"     # db.select([table_name]) 
    else:
        if distinct:
            for a in columns:
                column = getattr(table_name, a)
                query =  func.distinct(column)
                query.append(query)
        else:
            for a in columns:
                column = getattr(table_name, a)
                # return db.select([column])     
                query = column
                query1.append(query)
    if aggrigations != None:
        list1 = aggrigations.keys()
    # else:
    #     list1 = []    
        for x in list1:
            columns = x
            aggrigation = aggrigations[x].get("agg")
            id = aggrigations[x].get("label")

            if aggrigation == "sum":
                column = getattr(table_name, columns)
                query=  func.sum(column).label(id) 
                query1.append(query)
            elif aggrigation == "max":
                column = getattr(table_name, columns)
                query=  func.max(column).label(id)
                query1.append(query)
            elif  aggrigation == "min": 
                column = getattr(table_name, columns)
                query=  func.min(column).label(id)
                query1.append(query)
            elif aggrigation == "count":      
                column = getattr(table_name, columns)
                query=  func.count(column).label(id)
                query1.append(query)
        return query1

            
def get_where(table_name,where_dict):
    columns = where_dict.keys()
    for key1,values1 in where_dict.items():
        if 'in' in values1.values() and 'values' in values1.keys():
            x = values1.get('values')
            for key1 in columns:
                column = getattr(table_name, key1) 
            return f"{column} in {x}"
           
        elif '=' in values1.values() and'values' in values1.keys():
            x = values1.get('values')
            for key1 in columns:
                column = getattr(table_name, key1)
            return f"{column} = {x}"

        elif '!=' in values1.values() and'values' in values1.keys():
            x = values1.get('values')
            for key1 in columns:
                column = getattr(table_name, key1)
            return f"{column} != {x}"    

        elif 'like' in values1.values() and'values' in values1.keys():
            x = values1.get('values')
            for key1 in columns:
                column = getattr(table_name, key1) 
            return f"""{column} LIKE "{x}" """                  

import pandas as pd    
connection = engine.connect()

def get_groupby(columns):
    column_list1 = ""
    column_list1=column_list1.join(columns)
    return column_list1


def sql_query(b,user):#columns,aggregation,):
    
    query = get_select(clinic_data,'all',False)#,aggregation)
    if "where" in user and "groupby" in user:
        colmn_list= ['clinic_id']
        query2 = get_groupby(colmn_list)
        query3 = get_where(clinic_data,b)
        return select(query).where(text(query3)).group_by(text(query2))
    elif "where" in user:
        query3 = get_where(clinic_data,b)
        return select(query).where(text(query3))
    elif "groupby" in user:
        colmn_list= ['clinic_id']
        query2 = get_groupby(colmn_list)
        return select(query).group_by(text(query2))
    else: 
        query = get_select(clinic_data,"all",False)
        #print(select(query),"----------------------------------")
        return select(text(query))
# columns = ['clinic_name', 'longitute','Latitude']     
# aggregation = {"clinic_id": {"agg": "min", "label": "id"}}
user= "where"#["where","groupby"]       
b = {"clinic_id": {"operator": 'in', 'values': (102,108)}}
try:
    query1 = sql_query(b,user)
    df = pd.read_sql_query(query1, connection)
    print(query1) 
    print(df) 
except Exception as  e:
    print(e)
    print("Input incorrect")

connection.close()