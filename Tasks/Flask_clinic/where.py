# import json
# from typing import Any

# from flask_sqlalchemy import Model
# from sqlalchemy import String, cast, func
# from sqlalchemy.sql.elements import BinaryExpression

# FILTERING_OPERATORS = {
#     "in": "in_",
#     "eq": "__eq__",
#     "not": "__ne__",
#     "gte": "__ge__",
#     "lte": "__le__",
#     "gt": "__gt__",
#     "lt": "__lt__",
#     "like": "like",
# }


# def build_magic_filter_operation(
#     model: Model, attribute_name: str, value: Any, possible_operator: str
# ) -> BinaryExpression:
#     """
#     This returns a ready-to-use SQLAlchemy operation that can be passed to query.filter

#     :param model: SQLAlchemy model containing the attribute to filter on
#     :param attribute_name: name of the attribute to filter on
#     :param value: value to filter with
#     :param possible_operator: possible operator string

#     """
#     column = getattr(model, attribute_name)
#     revert, operator = _strip_not_operator(possible_operator)

#     # if operator is "in", we need to cast the string value as a list
#     if operator == "in":
#         try:
#             value = json.loads(value.replace("'", '"'))
#         except:
#             logger.debug(value)
#             logger.exception("Couldn't parse filter for __in operator:")
#             if not isinstance(value, list):
#                 value = []

#     # make string filtering case insensitive
#     if isinstance(column.property.columns[0].type, String):
#         # lower database stored value, and cast it as string (avoid error on enum fields)
#         column = func.lower(cast(column, String))
#         # lower query value
#         if operator == "in":
#             # if operator is in, we need to lower every element of the list
#             value = [e.lower() for e in value]
#         else:
#             value = func.lower(value)

#     if operator == "isnull":
#         usable_operator = "is_" if value in [True, "True", "true"] else "isnot"
#         value = None
#     else:
#         usable_operator = FILTERING_OPERATORS.get(operator, "__eq__")

#     operation = getattr(column, usable_operator)(value)
#     if revert:
#         operation = ~operation
#     return operation




















































# # from cProfile import label
# # from optparse import Values
# # from sqlalchemy.orm import sessionmaker
# # import sqlalchemy as db
# # from sqlalchemy.ext.declarative import declarative_base
# # from sqlalchemy import func, select, text, Integer, String, Column, Float
# # # from sqlalchemy_filters import apply_filters

# # Base = declarative_base()
# # # DEFINE THE ENGINE (CONNECTION OBJECT)
# # engine = db.create_engine('postgresql+psycopg2://postgres:smt9860@localhost/PracticeDB')
# # # Base.metadata.create_all(engine)
# # # CREATE THE TABLE MODEL TO USE IT FOR QUERYING
# # class Clinic(Base):

# # 	tablename = 'clinic_data'

# # 	clinic_id = Column(String(50),primary_key=True)
# # 	clinic_name = Column(String(50))
# # 	Doctor_name = Column(String(50))
# # 	longitute = Column(Float)
# # 	Latitude = Column(Float)
# # 	Postal_Code = Column(Integer)
# # 	Phone_Number = Column(Integer)
# # 	email_ID = Column(String)
    
# #     def get_where(where_dict):
# #         # query5 = []
# #         columns = where_dict.keys()
# #         for key1,values1 in where_dict.items():
        
# #             if 'in' in values1.values() and 'values' in values1.keys():
# #                 x = values1.get('values')
# #                 for key1 in columns:
# #                     column = getattr(table_name, key1)
# #                 # print(column,"====================================================")
# #                 # query =  func.filter(column)  
# #                 # query5.append(query)
# #                 return f"{column} in {x}"
            
            
# #             elif '=' in values1.values() and'values' in values1.keys():
# #                 x = values1.get('values')
# #                 for key1 in columns:
# #                     column = getattr(table_name, key1)
               
# #                 return f"{column} == {x}"

# #             elif '!=' in values1.values() and'values' in values1.keys():
# #                 x = values1.get('values')
# #                 for key1 in columns:
# #                     column = getattr(table_name, key1)
               
# #                 return f"{column} != {x}"    

# #             elif 'like' in values1.values() and'values' in values1.keys():
# #                 x = values1.get('values')
# #                 for a in columns:
# #                     column = getattr(table_name, key1)
                
# #                 return f"""{column} LIKE '%{x}%' """                 

# # def get_select(table_name, columns, distinct=False,aggrigations=None,label=None):
# #     query1 = []
# #     # columns = str(columns).strip("[]").replace("'",'')
# #     if isinstance(columns,str) and (columns.casefold()=='all' or columns.casefold()=='*'):
# #         columns = '*'
# #         if distinct:
# #             # return db.select([func.distinct(table_name.columns)])
# #             a = [getattr(table_name,column.key) for column in table_name.__table__.columns]
# #             query = func.distinct(a)
# #             query1.append(query)
# #         # else:
# #             # a = [getattr(table_name,column.key) for column in table_name.__table__.columns]
# #             # # query = db.select([table_name])
# #             # return a
# #             # return f"SELECT * FROM {table_name};"     # db.select([table_name])
# #     else:
# #         if distinct:
# #             for a in columns:
# #                 column = getattr(table_name, a)
# #                 query =  func.distinct(column)
# #                 # print(query,"bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")  
# #                 query.append(query)
# #         else:
# #             for a in columns:
# #                 column = getattr(table_name, a)
# #                 # print(column)

# #                 # return db.select([column])     
# #                 query = column
# #                 query1.append(query)


# #     list1 = aggrigations.keys()
# #     for x in list1:
# #         # print(key,"*************************")
# #         # print(values,"+++++++++++")
# #         print(list1)
# #         columns = x
# #         aggrigation = aggrigations[x].get("agg")
        
# #         id = aggrigations[x].get("label")
        
        
# #         if aggrigation == "sum":
# #             column = getattr(table_name, columns)
# #             query=  func.sum(column).label(id) 
# #             query1.append(query)
# #         elif aggrigation == "max":
# #             column = getattr(table_name, columns)
# #             query=  func.max(column).label(id)#.group_by(column)
# #             query1.append(query)
# #         elif  aggrigation == "min": 
# #             column = getattr(table_name, columns)
# #             query=  func.min(column).label(id)#.group_by(column)
# #             query1.append(query)
# #         elif aggrigation == "count":      
# #             column = getattr(table_name, columns)
# #             query=  func.count(column).label(id)#.group_by(column)
# #             query1.append(query)
# #         return query1


 

# # import pandas as pd    
# # connection = engine.connect()

# # def get_groupby(columns):
# #     column_list1 = ""
# #     column_list1=column_list1.join(columns)
# #     return column_list1


# # aggregation = {"Doctor_name": {"agg": "max", "label": "id"}}

# # query = get_select(Clinic,['clinic_name'],False,aggregation)

# # colmn_list= ['clinic_name']
# # query2 = get_groupby(colmn_list)

# # # where_dict = {'clinic_id': {"operator": 'in', 'values': [1,2]}}
# # class_object = Clinic()
# # query3 = class_object.get_where({"Doctor_name": {"operator": 'in', 'values': 2}})



# # query1 = (select(query)).where(text(query3)).group_by(text(query2))    #.filter(table_name.column_name == " ")

# # print(query1)

# # # df = pd.read_sql_query(query1, connection)
# # # print(query, df)
# # connection.close()



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
	


def get_select(table_name, columns, distinct=False):
    # print(type(columns),"----------------------------")
    if isinstance(columns,list):
        column = ",".join(columns)
        return f"SELECT {column} FROM {table_name.__tablename__}"
    query1 = [] # columns = str(columns).strip("[]").replace("'",'')
    if isinstance(columns,str) and (columns.casefold()=='all' or columns.casefold()=='*'):
        columns = '*'
        if distinct:
            # return db.select([func.distinct(table_name.columns)])
            a = [getattr(table_name,column.key) for column in table_name.__table__.columns]
            query = func.distinct(a)
            # print(text(query),"--------------------------------------")
            query1.append(query)
            
        else:
            return f"SELECT * FROM {table_name.__tablename__}"
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
import pandas as pd    
connection = engine.connect()    
query1 = get_select(clinic_data,['clinic_id','clinic_name','email_ID'],False)  #['clinic_id','clinic_name']
df = pd.read_sql_query(query1, connection)
print(query1) 
print(df) 
