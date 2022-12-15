from connection import conn
from select.select_query import connection, fetch_records
from insert.insert import insert_records

# setting the connection
host = "localhost"
port ="27017"
conn_str = f"mongodb://{host}:{port}/"
database_name = "demoDatabase" 
# database_name = input("Enter the database name")
table_name = str(input("Enter the table name/collection name: ") or "user_details")    #table_name --> user_details
mycol = conn.set_conn(conn_str, database_name, table_name)


# creating the empty parameters
column_name = []
where =  {} 
query_agg = []


# connection(mycol, column_name = [], where_clause = {}, query_agg = [])
# calling the insert of fetech records or insert data
select_insert = int(input("Do you want to fetch data or insert data: \n 1: Insert\n 2: Fetch "))
if select_insert == 1:
    insert_records(mycol)
elif select_insert == 2:
    fetch_records(mycol, query_agg, column_name, where)
else:
    print("You have entered wrong input")
