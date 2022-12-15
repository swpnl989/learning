import pymongo

def mongo_agg(agg,mycol):
    if isinstance(agg,list):
        documents = []
    
        try:
            for document in  mycol.aggregate(agg):
                if len(document)==0:
                    continue
                documents.append(document)
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
    
    documents = []
    if isinstance(where_clause, dict):
        for document in mycol.find(where_clause,dict_field):
            if len(document)==0:
                continue
            documents.append(document)
    else:
        raise TypeError("Only dict are allowed in where")
    return(documents)



def insert_doc(conn_str,database_name,table_name,insert_record=[]):
    myclient = pymongo.MongoClient(conn_str)
    mydb = myclient[database_name]
    mycol = mydb[table_name] 

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
    database_name = "demoDatabase"
    table_name = "orders"
    column_name = []
    where = {} 
    agg = [
   {
     "$lookup":
       {
         "from": "inventory",
         "localField": "item",
         "foreignField": "sku",
         "as": "inventory_docs"
       }
      }
    ] 
    
   
  
    conn_str = f"mongodb://{host}:{port}/"
    
    #print(connection(conn_str,database_name,table_name))
    print(connection(conn_str,database_name,table_name,column_name,where,agg))
    #insert_doc(conn_str,database_name,table_name,insert_record)
    



# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["demoDatabase"]






# documents = mydb.orders.aggregate( [
#    {
#      "$lookup":
#        {
#          "from": "inventory",
#          "localField": "item",
#          "foreignField": "sku",
#          "as": "inventory_docs"
#        }
#   }
# ] )



# for document in documents:
    
#     print(document)