
# import pymongo
# from query_generator import *
# import pandas as pd 
# import json
# import csv

# def get_csv_from_mongo_query(conn_str,database_name,table_name,query_agg):
#     myclient = pymongo.MongoClient(conn_str)
#     mydb = myclient[database_name]
#     mycol = mydb[table_name]
#     mycol.aggregate(query_agg).toCsv()
#     print(mycol.aggregate(query_agg).toCsv())
#     headers = [i for i in cursor[0]]
#     print(headers,"---------------------------gudfsrfsfs")
#     with open('output_1.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(headers)
#         for doc in cursor:
#             row = [doc.get(header) for header in headers]
#             writer.writerow(row)
#             print(doc,"<-----------")

# if __name__=="__main__":
#     host = "localhost"
#     port ="27017"
#     database_name = "demoDatabase"
#     table_name = "user_details"   
    
#     query_agg =[{'$match': {'name': 'abc'}}, {'$match': {'age': '26'}}]
    

 
#     conn_str = f"mongodb://{host}:{port}/"

#     print( get_csv_from_mongo_query(conn_str,database_name,table_name,query_agg))
    
    


# class abc:
#    def __init__(self,name,age):
    
#     self.name =name
#     self.age  = age

#    def abc_func(self):
#     return self.name

# a = abc("swap",27)
# d=a.abc_func()
# print(d)

# def connection(conn_str,database_name,table_name,column_name=[],where_clause={},agg =[]):
#     myclient = pymongo.MongoClient(conn_str)
#     mydb = myclient[database_name]
#     mycol = mydb[table_name]
#     documents = []
#     dict_field = {}
#     if isinstance(where_clause, dict):
#         for document in mycol.find(where_clause,dict_field):
#             if len(document)==0:
#                 continue
#             documents.append(document)
# import pymongo


# class conn():
#     def __init__(self,conn_str,database_name,table_name):
#         self.myclient = pymongo.MongoClient(conn_str)
#         self.mydb = self.myclient[database_name]
#         self.mycol = self.mydb[table_name]


#     def daa(self):
#         documents = []
#         for document in self.mycol.find({},{}):
#             if len(document)==0:
#                 continue
#             documents.append(document)
#         return documents







# def get_csv_from_mongo_query(query_agg):
#     cursor = query_agg.find()
#     headers = [i for i in cursor[0]]
#     with open('output.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(headers)
#         for doc in cursor:
#             row = [doc[header] for header in headers]
#             writer.writerow(row)


# import pymongo
# from query_generator import *
# import pandas as pd 
# import json
# import csv

# def get_csv_from_mongo_query(conn_str,database_name,table_name,query_agg):
#     myclient = pymongo.MongoClient(conn_str)
#     mydb = myclient[database_name]
#     mycol = mydb[table_name]
#     mycol.aggregate(query_agg).toCsv()
#     print(mycol.aggregate(query_agg).toCsv())

# def download_from_final_query(conn_str,database_name,table_name,column_name=[],where_clause={}):
#     myclient = pymongo.MongoClient(conn_str)
#     mydb = myclient[database_name]
#     mycol = mydb[table_name]
#     dict_field = {}
#     if isinstance(column_name, dict):
#         for column in column_name:
#             dict_field[column]=1
#         else:
#             raise TypeError("Only list are allowed")
#     documents =[]       
#     if isinstance(where_clause, list):   
#         for document in mycol.find(where_clause,dict_field):
#             if len(document)==0:
#                 continue
#             documents.append(document)
#         else:
#             raise TypeError("Only dict are allowed in where")
#     return documents
# def mongo_query(mycol,query_agg):
#         if isinstance(query_agg,list):
#             documents = []
#             try:
#                 for document in  mycol.aggregate(query_agg):
#                     if len(document)==0:
#                         continue
#                     documents.append(document)
#                 return documents
#             except Exception as e:
#                 return e 

# if __name__=="__main__":
#     host = "localhost"
#     port ="27017"
#     conn_str = f"mongodb://{host}:{port}/"
#     database_name = "demoDatabase"
#     table_name = "user_details"
#     column_name = []   
#     where= {}
#     query_agg =[{'$match': {'name': 'abc'}}, {'$match': {'age': '26'}}]
#     query_agg=input().split(',')
#     print(list(query_agg))
    

 
#     conn_str = f"mongodb://{host}:{port}/"
#     myclient = pymongo.MongoClient(conn_str)
#     mydb = myclient[database_name]
#     mycol = mydb[table_name]

#     print(mongo_query(mycol,query_agg))
            




# insert_list = input("Do you want to insert list of document press Y or N: ").lower()
# list_1 = ("[{name:BBBBBB,age:2323,adress:Jalgao,married:True},{name:CCCCC,age:20,adress:Jalgao,married: True}]")
# print(list_1,"]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
# dict_1 = {}
# for i in list_1.split(","):
#     key1,value1 = i.split(":")
#     dict_1[key1]=value1
# list_1 = [dict_1]
# print(list_1,"--------------------------",print(len(list_1)))

list_1 = ("[{name:BBBBBB,age:2323,adress:Jalgao,married:True},{name:CCCCC,age:20,adress:Jalgao,married: True}]")
list_1.split('{')

print(list_1)