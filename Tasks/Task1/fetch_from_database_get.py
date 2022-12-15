
import psycopg2
import pymongo

def get_data(source='mongodb',tablename=None,limit_no=None):
    if source=="mongodb":
        data = mongo(tablename,limit_no=20)
        count = len(data)
        print(count)
    else:
        data= postsql(tablename,limit_no=limit_no)
        count = len(data)
        print(count)

    
    return data, count
    


def postsql(tablename,limit_no):
    conn = psycopg2.connect(database="PracticeDB", user='postgres', password='smt9860', host='localhost', port= '5432')
    cursor = conn.cursor()
    cursor.execute('''SELECT * from {} limit {}'''.format(tablename,limit_no))
    result = cursor.fetchall()
    conn.close()
    return result

def mongo(tablename,limit_no):
    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["demoDatabase"]
    
    print(type(tablename),tablename)
    mycol = mydb[tablename]
  
    list_data = []
    # print (mycol.find().limit(limit_no))
    for x in mycol.find().limit(limit_no):
        list_data.append(x)                             
        print(list_data)
    return list_data

# def user_input():
# source = input("Enter source: ").lower()
# tablename= input("Enter table name: ").lower()
# limit_no = input("Enter limit: ").lower()

# data = get_data(source,tablename,limit_no)
# print(data)
# # return limit_no, data
























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
# cursor.execute('''SELECT*from "More_50K_data"''')
# result = cursor.fetchall()
# print(result)