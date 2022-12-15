from mongo_query import mongo_query
from query_generator import query_generator, boolean_func
from util import create_csv_from_mongo_query


def connection(mycol, column_name = [], where_clause = {}, query_agg = []):
    if query_agg:
        return mongo_query(mycol, query_agg)
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
        where_clause = boolean_func("y")
        
        documents = []                       
        if isinstance(where_clause, dict):   
            for document in mycol.find(where_clause,dict_field).limit(l_no):
                if len(document)==0:
                    continue
                documents.append(document)
        else:
            raise TypeError("Only dict are allowed in where") 
        return documents        
    else:    
        documents = []                       
        if isinstance(where_clause, dict):   
            for document in mycol.find(where_clause, dict_field):
                if len(document)==0:
                    continue
                documents.append(document)
        else:
            raise TypeError("Only dict are allowed in where")
        return documents


def fetch_records(mycol, query_agg, column_name, where):
    option = int(input("Do you want to fetch data:\n 1. hard coded press\n 2. aggrigation\n 3. find function\n"))
    if option == 1:
        query_agg = input("Entry hard coaded query: ")
        fetch_data = mongo_query(mycol, query_agg)
    elif option == 2:
        query_agg = query_generator()
        fetch_data = connection(mycol, column_name, where, query_agg)
    elif option == 3:
        fetch_data = connection(mycol, column_name,where_clause={},query_agg=[])

    csv_save = input("Want to save data in csv press y/n: ").lower()
    if csv_save == 'y':
        create_csv_from_mongo_query(fetch_data)
    else:
        print(fetch_data)
