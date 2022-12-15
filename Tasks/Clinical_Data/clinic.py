
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# app = FastAPI()
# templates = Jinja2Templates(directory="templates/")
# @app.get("/item")
# async def read_item(request: Request, pin_code):

#     df= pd.read_csv("file1.csv")
#     if (int(pin_code) in list(df["Postal_Code"])):
#         var= df[df["Postal_Code"] == int(pin_code)]
#         # print(type(var))
#         var = var.to_dict('records')
#         # return var

#         return templates.TemplateResponse("cluster.html", context={'request': request, 'result': var })
#         # return {"data":var}
        
#     else:
#         return "sorry"
# if __name__ == "__main__":

#     print(read_item(80000))  

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pandas as pd
import emailswapnil


app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get('/')
def read_form():
    return {'messege':'hello world'}


@app.get("/form")
def form_post(request: Request):
    result = "Hospital Information"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    
    
    df=pd.read_csv("file1.csv")
    # print(df)
    df =emailswapnil.data_cleaning(df)
    # df.drop_duplicates(subset='Postal_Code')
    print(df)
    if (int(num) in list(df["Postal_Code"])):
        var= df[df["Postal_Code"] == int(num)].drop_duplicates()
        # print(var)
        var = var.to_dict('records')
        # if len(list(var))==1:
        
        return templates.TemplateResponse("form.html", context={'request': request, 'result': var })
        # else:
            # return templates.TemplateResponse("table.html", context={'request': request, 'result': list(var)[0] })
        # return {"data":var}
        
    else:
        return "SORRY HOSPITAL Info Not found"