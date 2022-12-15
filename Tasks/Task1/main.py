from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from mono_insert import mongo_db
from fetch_from_database_get import*
from postgress_to_mongo import*

app = FastAPI()



@app.get('/')
def read_form():
    return 'hello world'


@app.get("/run")
def form_get(input_table:str,output_table:str):

    table_name = input_table
    query = f'''SELECT*from {table_name}'''
   
    table_name2 = output_table
    request = mongo_db(query,table_name2)
    
    result = f"Data pushed from {table_name} to {table_name2}"
    if True:
        return {"success" : request, "message": result} 
       
    


@app.get("/get_data")
def get_data_(source: str ='mongodb',tablename: str=None,limit_no: int=None):
    # if source=="mongodb":
    #     data = mongo(tablename,limit_no=20)
    # else:
    #     data= postsql(tablename,limit_no=20)

    data,count = get_data(source,tablename,limit_no)

    return {'data' : data, "count": count}
