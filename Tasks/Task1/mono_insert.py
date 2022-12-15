from postgress_to_mongo import *

import pymongo

# def get_con()

def mongo_db(query, table_name):
    # try:
    mongo_client= pymongo.MongoClient('mongodb://localhost:27017')
    mongo_client.list_database_names()
    db = mongo_client["demoDatabase"]
    mycol = db[table_name]
    mycol.delete_many({})
    json_output = query_db(query)
    # return json_output
    print(json_output)
    mycol.insert_many(json_output)
    return True        
    # except:
    #     return False





