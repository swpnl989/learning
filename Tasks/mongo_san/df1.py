import pymongo
from query_generator import *
import csv
import pandas as pd 
import json


class conn():
    def __init__(self, conn_str, database_name, table_name):
        self.myclient = pymongo.MongoClient(conn_str)
        self.mydb = self.myclient[database_name]
        self.mycol = self.mydb[table_name]


    def mongo_query(self, query_agg):
        if isinstance(query_agg, list):
            print(query_agg)
            documents = []
            try:
                for document in  self.mycol.aggregate(query_agg):
                    if len(document)==0:
                        continue
                    documents.append(document)
                return documents
            except Exception as e:
                return e 


    def get_csv_from_mongo_query(self, documents):
        df = pd.DataFrame(documents)
        w_csv_name = input("Want to give custom csv name press Y or N").lower()
        if w_csv_name == 'y':
            name_csv = input("Enter csv name without extension")
            df.to_csv(name_csv+".csv", index=False)
        else:
            df.to_csv("output.csv", index=False)             


    def connection(self, column_name, where_clause={}, query_agg=[]):
        if query_agg:
            return self.mongo_query(query_agg)
        dict_field = {"_id":0}
        if isinstance(column_name, list):
            for column in column_name:
                dict_field[column]=1
        else:
            raise TypeError("Only list are allowed")                              

        sort_limit = input("Want to sort and limit press Y/N: ").lower()
        if sort_limit == 'y':
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
            return documents    

        limit_only = input("Want to limit only press Y/N: ").lower()
        if limit_only=='y':
            
            l_no = int(input("Enter limit : "))
            # where_clause = {'married': {'$eq': True}}
            where_clause = boolean_func("y")
            
            documents = []                       
            if isinstance(where_clause, dict):   
                for document in self.mycol.find(where_clause,dict_field).limit(l_no):
                    if len(document)==0:
                        continue
                    documents.append(document)
            else:
                raise TypeError("Only dict are allowed in where") 
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
            return documents


    def create_dic_insert(self, list1, list2): 
        if len(list1) == len(list2): 
            print("True") 
        else: 
            print("False") 
            
        res = {list1[i]: list2[i] for i in range(len(list1))} 
        return res    


    def insert_list(self, list_1):
        if isinstance(list_1, list):
            try:
                self.mycol.insert_many(list_1)
            except Exception as e:
                print(e)
        else:
            raise TypeError("Only list are allowed in where")


    def insert_doc(self, list1, insert_record=[]):
        list3 = []
        for i in range(len(list1)):
            list2 = input(f"Enter values for {list1[i]}\t: ").split(",")
            if len(list2) == 1:
                list2=list2[0]
                if list2 == 'true' or list2 == 'false':
                    list3.append(bool(list2))                      
                    print(type(list3),'_____________')
                else:
                    list3.append(list2)
            else:
                list3.append(list2)
                
        insert_record = [sm.create_dic_insert(list1, list3)]
        print(insert_record)
        if isinstance(insert_record, list):
            try:
                self.mycol.insert_many(insert_record)
            except Exception as e:
                print(e)
        else:
            raise TypeError("Only list are allowed in where")


    def fetch_records():
        option = int(input("Do you want to fetch data for hard coded press 1, aggrigation press 2, find function press 3: "))
        if option == 1:
            query_agg = input("Entry hard coaded query: ")
            fetch_data = sm.mongo_query(query_agg)

        elif option == 2:
            query_agg = query_generator()
            fetch_data = sm.connection(column_name, where, query_agg)

        elif option == 3:
            fetch_data = sm.connection(column_name,where_clause={},query_agg=[])
            


        csv_save = input("Want to save data in csv press y/n: ").lower()
        if csv_save == 'y':
            sm.get_csv_from_mongo_query(fetch_data)
        else:
            print(fetch_data)


if __name__=="__main__":
    host = "localhost"
    port ="27017"
    conn_str = f"mongodb://{host}:{port}/"
    database_name = "demoDatabase"
    table_name = str(input("Enter the table name/collection name: ") or "user_details")    #table_name --> user_details
    
    column_name = []
    where =  {} 
    query_agg = []
    sm = conn(conn_str, database_name, table_name)
    insert_select = input("Do you want to fetch data or insert data for fetch press  1 and insert press 2: ").lower()

    fetch_records():
        hard_coded = input("Do you want to fetch data for hard coded press 1, aggrigation press 2, find function press 3: ").lower()
        if hard_coded=='1':
            query_agg = input("Entry hard coaded query: ")
            fetch_data = sm.mongo_query(query_agg)

        elif hard_coded=='2':
            
            query_agg = query_generator()
            fetch_data = sm.connection(column_name,where,query_agg)

        elif hard_coded=='3':
            fetch_data = sm.connection(column_name,where_clause={},query_agg=[])
            


        csv_save = input("Want to save data in csv press y/n: ").lower()
        if csv_save == 'y':
            sm.get_csv_from_mongo_query(fetch_data)
        else:
            print(fetch_data)

    
    elif insert_select=='2':
        insert_csv_data = input("Do you wnat to inser CSV Y or N : ").lower()
        if insert_csv_data == "y":
            myclient = pymongo.MongoClient(conn_str)
            mydb = myclient[database_name]
            mycol = mydb[table_name]
            csv_name = input("Enter csv name : ")
            df = pd.read_csv(csv_name)
            data = df.to_dict(orient ="records")
            mycol.insert_many(data)
        else:
            insert_record = []
            insert_data = input("Do you want to insert data press Y or N: ").lower()
            if insert_data == "y":
                list1 = input("Enter required column/fields name\t: ").split(",")
                while True:
                    sm.insert_doc(list1)
                    ex= input("Want to exit press or enter data Y/N").lower()
                    if ex=='y':
                        break
            else:
                insert_list = input("Do you want to insert list of document press Y or N: ").lower()
                list_1 = (input("enter a list "))
                no_of_dict = 0
                l_new = []
                while no_of_dict<=list_1.count("{"):
                    a=list_1.find('{')
                    b=list_1.find('}')
                    l_new.append(list_1[a+1:b])
                    list_1=list_1[b+1:]
                    no_of_dict+=1
                list_1 = []
                for items in l_new:
                    di = {}
                    for sub_i in items.split(','):
                        key,value = sub_i.split(":")
                        if value.lower()=='true':
                            value=True
                        elif value.lower() == 'false':
                            value = False
                        di[key]=value
                    list_1.append(di)
                if insert_list == "y":
                    sm.insert_list(list_1)               
    else:
        print("you entered wrong input")
    
 #[{name:Ak,age:19,adress:jammgao,married:False},{name:kl,age:9,adress:Mul,married:false}]  