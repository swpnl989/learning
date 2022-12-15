import json
import psycopg2

def db_sql(database_name='PracticeDB'):
    return psycopg2.connect(database=database_name, user='postgres', password='smt9860', host='localhost', port= '5432')

def query_db(query, args=(), one=False):
    cur = db_sql().cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r

# input_qury = '''SELECT*from clinic_data'''
input_qury = '''SELECT*from "More_50K_data"'''

















































# def run(input_qury):
#     my_query = query_db(input_qury)     #("select * from clinic_datalimit %s", (3,))
#     json_output = json.dumps(my_query) 
#     return json_output
    # print(json_output)


# run(input_qury)

# import pymongo
# mongo_client= pymongo.MongoClient('mongodb://localhost:27017')
# # mongo_client.list_database_names()
# db = mongo_client["demoDatabase"]
# mycol = db['orders']


# def insert_list(json_output):
#     mycol.insert_many(json_output)
    
# cursor = db.mycol.find()
# for record in cursor:
# 	print(record)



# # Python code to illustrate
# # inserting data in MongoDB
# from pymongo import MongoClient

# try:
# 	conn = MongoClient()
# 	print("Connected successfully!!!")
# except:
# 	print("Could not connect to MongoDB")

# # database
# # myclient = pymongo.MongoClient(conn_str)
# # conn_str = mongodb://localhost:27017/"
# # # myclient = pymongo.MongoClient(conn_str)
# # mydb = myclient['demoDatabase']
# # mycol = db['orders']


# # Insert Data
# db.orders.insert_many(json_output)


# print("Data inserted with record ids" )

# Printing the data inserted
# cursor = db.orders.find()
# for record in cursor:
# 	print(record)




# import psycopg2

# #establishing the connection

# conn = psycopg2.connect(
#    database="PracticeDB", user='postgres', password='smt9860', host='localhost', port= '5432'
# )

# #Setting auto commit false
# conn.autocommit = True

# #Creating a cursor object using the cursor() method
# cursor = conn.cursor()

# #Retrieving data
# cursor.execute('''SELECT * from clinic_data''')
# result = cursor.fetchall()
# print(result)