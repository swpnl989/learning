import pymongo
from query_generator import *
import pandas as pd 
import json



def mongo_agg(agg,mycol):
    if isinstance(agg,list):
        documents = []
        print(mycol.aggregate(agg))
        try:
            for document in  mycol.aggregate(agg):
                if len(document)==0:
                    continue
                documents.append(document)
            # print(documents,"----------------------------------")
            return documents
        except Exception as e:
            return e   

def connection(conn_str,database_name,table_name,column_name=[],where_clause={},agg =[]):
    myclient = pymongo.MongoClient(conn_str)
    mydb = myclient[database_name]
    mycol = mydb[table_name]
    if agg:
        return mongo_agg(agg,mycol)
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
            for document in mycol.find(where_clause,dict_field).sort(s_col).limit(l_no):
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
            for document in mycol.find(where_clause,dict_field).sort(s_col):
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
        where_clause =  boolean_func("y")
        
        documents = []                       #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).limit(2)
        if isinstance(where_clause, dict):   #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).sort({"name":1,"age":1}).limit(2)
            for document in mycol.find(where_clause,dict_field).limit(l_no):
                if len(document)==0:
                    continue
                documents.append(document)
        else:
            raise TypeError("Only dict are allowed in where")
        return documents        
    else:    
        documents = []                       #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).limit(2)
        if isinstance(where_clause, dict):   #mycol.find.find({{'married': {'$eq': 'True'}}},{_id:0}).sort({"name":1,"age":1}).limit(2)
            for document in mycol.find(where_clause,dict_field):
                if len(document)==0:
                    continue
                documents.append(document)
        else:
            raise TypeError("Only dict are allowed in where")
        return documents

def create_dic_insert(list1, list2): 
    
    if len(list1) == len(list2): 
        print("True") 
    else: 
        print("False") 
          
    res = {list1[i]: list2[i] for i in range(len(list1))} 
    return res    



def insert_doc(conn_str,database_name,table_name,list1,insert_record=[]):
    myclient = pymongo.MongoClient(conn_str)
    mydb = myclient[database_name]
    mycol = mydb[table_name]

       
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
            
    insert_record = [create_dic_insert(list1, list3)]
    print(insert_record)
    if isinstance(insert_record,list):
        try:
            mycol.insert_many(insert_record)
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
    agg = []
    agg_required = input("Do you want to fetch specific data using query (Agg Pipeline) press Y or N: ").lower()
    if agg_required=='y':
        agg = query_generator()

    print(connection(conn_str,database_name,table_name,column_name,where,agg))

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
            insert_doc(conn_str,database_name,table_name,list1)
            ex= input("Want to exit press Y/N").lower()
            if ex=='y':
                break

        print(connection(conn_str,database_name,table_name))
    
    
    
    #[{'name': 'kj', 'age': '27', 'address': 'Pune', 'hobbies': [cooking,cricket] ,married:True}]












  