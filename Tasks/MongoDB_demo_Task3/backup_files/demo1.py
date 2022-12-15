
import pymongo
from query_generator import *
import csv
import pandas as pd 
import json


class conn():
    def __init__(self,conn_str,database_name,table_name):
        self.myclient = pymongo.MongoClient(conn_str)
        self.mydb = self.myclient[database_name]
        self.mycol = self.mydb[table_name]

    def mongo_query(self,query_agg):
        if isinstance(query_agg,list):
            documents = []
            try:
                for document in  self.mycol.aggregate(query_agg):
                    if len(document)==0:
                        continue
                    documents.append(document)
                csv_save = input("Want to save data in csv press y/n: ").lower()
                if csv_save == 'y':
                   self.get_csv_from_mongo_query(documents) 
                return documents
            except Exception as e:
                return e 

    def connection(self,column_name,where_clause={},query_agg=[]):
        if query_agg:
            return self.mongo_query(query_agg)
        dict_field = {"_id":0}
        if isinstance(column_name, list):
            for column in column_name:
                dict_field[column]=1
        else:
            raise TypeError("Only list are allowed")

        sort_limit = input("Want to sort and limit press Y/N: ").lower()
        if sort_limit=='y':
            s_col = input("Enter sort column with boolean(for sort and limit) :")
            l_no = int(input("Enter limit : "))
            # where_clause = {'married': {'$eq': True}}
            where_clause =  boolean_func("y")
            documents = []                       #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).limit(2)
            if isinstance(where_clause, dict):   #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).sort({"name":1,"age":1}).limit(2)
                for document in self.mycol.find(where_clause,dict_field).sort(s_col).limit(l_no):
                    if len(document)==0:
                        continue
                    documents.append(document)
            else:
                raise TypeError("Only dict are allowed in where")
            csv_save = input("Want to save data in csv press y/n: ").lower()
            if csv_save == 'y':
                self.get_csv_from_mongo_query(documents) 
            return documents

        sort_only = input("Want to sort only press Y/N: ").lower()
        if sort_only=='y':
            s_col = input("Enter sort column with boolean sort only :")
            
            where_clause =  boolean_func("y")
            documents = []                       #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).limit(2)
            if isinstance(where_clause, dict):   #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).sort({"name":1,"age":1}).limit(2)
                for document in self.mycol.find(where_clause,dict_field).sort(s_col):
                    if len(document)==0:
                        continue
                    documents.append(document)
            else:
                raise TypeError("Only dict are allowed in where")
            csv_save = input("Want to save data in csv press y/n: ").lower()
            if csv_save == 'y':
                self.get_csv_from_mongo_query(documents) 
            return documents    

        limit_only = input("Want to limit only press Y/N: ").lower()
        if limit_only=='y':
            
            l_no = int(input("Enter limit : "))
            # where_clause = {'married': {'$eq': True}}
            where_clause = boolean_func("y")
            
            documents = []                       #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).limit(2)
            if isinstance(where_clause, dict):   #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).sort({"name":1,"age":1}).limit(2)
                for document in self.mycol.find(where_clause,dict_field).limit(l_no):
                    if len(document)==0:
                        continue
                    documents.append(document)
            else:
                raise TypeError("Only dict are allowed in where")
            csv_save = input("Want to save data in csv press y/n: ").lower()
            if csv_save == 'y':
                self.get_csv_from_mongo_query(documents) 
            return documents        
        else:    
            documents = []                       
            if isinstance(where_clause, dict):   
                for document in self.mycol.find(where_clause,dict_field):
                    if len(document)==0:
                        continue
                    documents.append(document)
            else:
                raise TypeError("Only dict are allowed in where")
            csv_save = input("Want to save data in csv press y/n: ").lower()
            if csv_save == 'y':
                self.get_csv_from_mongo_query(documents) 
            return documents

    def get_csv_from_mongo_query(self,documents):
        df = pd.DataFrame(documents)
        df.to_csv("output.csv",index=False)
        print(df)        


    def create_dic_insert(self,list1, list2): 
        
        if len(list1) == len(list2): 
            print("True") 
        else: 
            print("False") 
            
        res = {list1[i]: list2[i] for i in range(len(list1))} 
        return res    



    def insert_doc(self,list1,insert_record=[]):
        list3 = []
        for i in range(len(list1)):
            list2 = input(f"Enter values for {list1[i]}\t: ").split(",")
            if len(list2) == 1:
                list2=list2[0]
                if list2=='true' or list2=='false':
                    list3.append(bool(list2))                      
                    print(type(list3),'_____________')
                else:
                    list3.append(list2)
            else:
                list3.append(list2)
                
        insert_record = [sm.create_dic_insert(list1, list3)]
        print(insert_record)
        if isinstance(insert_record,list):
            try:
                self.mycol.insert_many(insert_record)
            except Exception as e:
                print(e)
        else:
            raise TypeError("Only list are allowed in where")



if __name__=="__main__":
    host = "localhost"
    port ="27017"
    conn_str = f"mongodb://{host}:{port}/"
    database_name = "demoDatabase"
    table_name = str(input("Enter the table name/collection name: ") or "user_details")    #table_name --> user_details
    
    column_name = []
    where =  {} 
    query_agg = []
    agg_required = input("Do you want to fetch specific data using query (Agg Pipeline) press Y or N: ").lower()
    if agg_required=='y':
        query_agg = query_generator()
    sm = conn(conn_str,database_name,table_name)    
    #sm.get_csv_from_mongo_query(table_name)
    print(sm.connection(column_name,where,query_agg),"=============================")

    insert_csv_data = input("Do you wnat to inser CSV Y or N : ").lower()
    if insert_csv_data == "y":
        myclient = pymongo.MongoClient(conn_str)
        mydb = myclient[database_name]
        mycol = mydb[table_name]
        csv_name = input("Enter csv name : ")
        df = pd.read_csv(csv_name)
        data = df.to_dict(orient ="records")
        mycol.insert_many(data)
    insert_record = []
    insert_data = input("Do you want to insert data press Y or N: ").lower()
    if insert_data == "y":
        list1 = input("Enter required column/fields name\t: ").split(",")
        while True:
            sm.insert_doc(list1)
            ex= input("Want to exit press Y/N").lower()
            if ex=='y':
                break

        print(sm.connection())
    