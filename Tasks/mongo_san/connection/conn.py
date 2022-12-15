import pymongo

def set_conn(conn_str, database_name, table_name):
    myclient = pymongo.MongoClient(conn_str)
    mydb = myclient[database_name]
    mycol = mydb[table_name]
    return mycol