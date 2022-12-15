# # import pymongo
# # import pandas as pd 
# # import json

# # client = pymongo.MongoClient("mongodb://localhost:27017")

# # df = pd.read_csv("insert.csv")

# # data = df.to_dict(orient ="records")

# # print(data)

	
# # db = client["demoDatabase"]

# # db.employee.insert_many(data)
# # print(db.employee.insert_many(data))



# # l = [1,2,3,4,5]

# # print("original list: ",l)

# # pos = int(input("Enter the position to insert list: "))

# # l1 = [101,102,103]

# # l[pos-1:pos-1] = l1

# # print("After inserting list at specific position: ",


# def __init__(self,conn_str,database_name,table_name):
#         self.myclient = pymongo.MongoClient(conn_str)
#         self.mydb = self.myclient[database_name]
#         self.mycol = self.mydb[table_name]

#     def mongo_agg(self,agg):
#         if isinstance(agg,list):
#             documents = []
#             print(self.mycol.aggregate(agg))
#             try:
#                 for document in  self.mycol.aggregate(agg):
#                     if len(document)==0:
#                         continue
#                     documents.append(document)
#                 # print(documents,"----------------------------------")
#                 return documents
#             except Exception as e:
#                 return e   

#     def connection(self,where_clause={},agg =[]):
#         if agg:
#             return self.mongo_agg(agg)
#         dict_field = {"_id":0}
#         if isinstance(column_name, list):
#             for column in column_name:
#                 dict_field[column]=1
#         else:
#             raise TypeError("Only list are allowed")

#         sort_limit = input("Want to sort and limit press Y/N: ").lower()
#         if sort_limit=='y':
#             s_col = input("Enter sort column with boolean(for sort and limit) :")
#             l_no = int(input("Enter limit : "))
#             # where_clause = {'married': {'$eq': True}}
#             where_clause =  boolean_func("y")
#             documents = []                       #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).limit(2)
#             if isinstance(where_clause, dict):   #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).sort({"name":1,"age":1}).limit(2)
#                 for document in self.mycol.find(where_clause,dict_field).sort(s_col).limit(l_no):
#                     if len(document)==0:
#                         continue
#                     documents.append(document)
#             else:
#                 raise TypeError("Only dict are allowed in where")
#             return documents

#         sort_only = input("Want to sort only press Y/N: ").lower()
#         if sort_only=='y':
#             s_col = input("Enter sort column with boolean sort only :")
            
#             where_clause =  boolean_func("y")
#             documents = []                       #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).limit(2)
#             if isinstance(where_clause, dict):   #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).sort({"name":1,"age":1}).limit(2)
#                 for document in self.mycol.find(where_clause,dict_field).sort(s_col):
#                     if len(document)==0:
#                         continue
#                     documents.append(document)
#             else:
#                 raise TypeError("Only dict are allowed in where")
#             return documents    

#         limit_only = input("Want to limit only press Y/N: ").lower()
#         if limit_only=='y':
            
#             l_no = int(input("Enter limit : "))
#             # where_clause = {'married': {'$eq': True}}
#             where_clause =  boolean_func("y")
            
#             documents = []                       #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).limit(2)
#             if isinstance(where_clause, dict):   #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).sort({"name":1,"age":1}).limit(2)
#                 for document in self.mycol.find(where_clause,dict_field).limit(l_no):
#                     if len(document)==0:
#                         continue
#                     documents.append(document)
#             else:
#                 raise TypeError("Only dict are allowed in where")
#             return documents        
#         else:    
#             documents = []                       #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).limit(2)
#             if isinstance(where_clause, dict):   #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).sort({"name":1,"age":1}).limit(2)
#                 for document in self.mycol.find(where_clause,dict_field):
#                     if len(document)==0:
#                         continue
#                     documents.append(document)
#             else:
#                 raise TypeError("Only dict are allowed in where")
#             return documents

#     def create_dic_insert(list1, list2): 
        
#         if len(list1) == len(list2): 
#             print("True") 
#         else: 
#             print("False") 
            
#         res = {list1[i]: list2[i] for i in range(len(list1))} 
#         return res    



#     def insert_doc(self,list1,insert_record=[]):
#         list2 = input("Enter values\t: ").split(",")
#         list3 = []
#         for i in range(len(list2)):
            
#             if i == len(list2)-1:
#                 list3.append(bool(list2[i]))
#                 print(type(list3[i]),'_____________')
#             else:
#                 list3.append(list2[i])
                
#         insert_record = [self.create_dic_insert(list1, list3)]
#         print(insert_record)
#         if isinstance(insert_record,list):
#             try:
#                 self.mycol.insert_many(insert_record)
#             except Exception as e:
#                 print(e)
#         else:
#             raise TypeError("Only list are allowed in where")



# if __name__=="__main__":
#     host = "localhost"
#     port ="27017"
#     conn_str = f"mongodb://{host}:{port}/"
#     database_name = "demoDatabase"
#     table_name = str(input("Enter the table name/collection name: ") or "user_details")    #table_name --> user_details
#     sm = conn(conn_str,database_name,table_name)
#     column_name = []
#     where =  {} 
#     agg = []
#     agg_required = input("Do you want to fetch specific data using query (Agg Pipeline) press Y or N: ").lower()
#     if agg_required=='y':
#         agg = query_generator()
#     sm = conn(conn_str,database_name,table_name)    

#     print(sm.connection(column_name,where,agg))

#     insert_csv_data = input("Do you wnat to inser CSV Y or N : ").lower()
#     if insert_csv_data == "y":
#         myclient = pymongo.MongoClient(conn_str)
#         mydb = myclient[database_name]
#         mycol = mydb[table_name]
#         csv_name = input("Enter csv name : ")
#         df = pd.read_csv(csv_name)
#         data = df.to_dict(orient ="records")
#         mycol.insert_many(data)

# where_clause = {}
# column_name = input("Enter column name(fields) to chech True or False: ").strip()
# dict_name = column_nam








import csv


def get_csv_from_mongo_query(self,documents):
    csv_download = input("Want to download CSV press Y/N: ").lower()
    where_clause = input("want to download with specific column name ad value Y or N ")
    if where_clause == "y":
        where_clause = {}
        column_name = input("Enter column name(fields) to chech True or False: ").strip()
        dict_name = column_name
        sub_column_name = input("Enter the value:")
        where_clause[dict_name] = sub_column_name
        print(where_clause)
    dict_field = input("want to hide or show specific column for download: ")

    if csv_download =='y':
        dict_field = {}
        if isinstance(column_name, list):
            for column in column_name:
                dict_field[column]=1                                      # .find({"name":"jk", "age":"26"},{"_id":0,"hobbied":0})
            cursor = self.mycol.find(where_clause,dict_field)
            headers = [i for i in cursor[0]]
            with open('output.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(headers)
                for doc in cursor:
                    row = [doc[header] for header in headers]
                    writer.writerow(row) 
                      