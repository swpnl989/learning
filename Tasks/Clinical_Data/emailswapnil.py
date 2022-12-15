import pandas as pd 
import numpy as np
import re




def check_email(emails):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    e = []
    for email in emails:
        email = str(email)   
        if(re.search(regex, email)):
                #print("Valid Email")
                e.append(email)
        else:
                # print("Invalid Email")
                # print(re.sub(r'([.])([\w]+)|[@]', r'@gmail.com',email))
                email = re.sub(r'([.])([\w]+)|[@]', r'@gmail.com',email)
                e.append(email)
    return e

def check_no(number):  
    o=[]
    for i in number:                 
        x=re.findall(r"\d+",i)
        y=re.sub(r"^[+][\d]{2}[-]?|^[0]\s|^\W\d{2}\W\s","",i)
        #print(x)
        #y=re.sub(" ","@gmail.com",x)
        
        if len(y)!=10 and y.startswith("0"):
            o.append(y.lstrip("0"))
        # elif len(y)!=10 and y.startswith("91"):
        #     o.append(y.lstrip("91"))    
        elif len(y)!=10:
            o.append(None)
        else:
            o.append(y)
    return o
    
def data_cleaning(df_final):
    df_final['email_ID']=check_email(list(df_final['email_ID']))
    df_final['Phone_Number'] = check_no(list(df_final['Phone_Number']))
    df_final.dropna(subset=['email_ID'])
    df_final= df_final[df_final != "None"]
    
    df_fianl= df_final.dropna(axis=0,inplace=True)
    
    return(df_final)
    



if __name__ == "__main__":
    df1 = pd.DataFrame({'Clinic_ID':[101,102,103,104,105,106,107,107,108],
                   'Clinic_name':['Lilavati','Wokhartks','OrangeCity','Vedanta','Sasun','GMC','SSM','SSM','ABC'],
                    'Doctor_name':['Dr.Mehta','Dr. Dubey','Dr. Shrama','Dr. Khan','Dr. Kohli','Dr. Batra','DR.Jay','DR.Jay','Dr.ABC'],                    
                   'longitute':[72.877655,79.088158,73.856743,77.102493,78.298039,75.876523,78.546378,78.546378,79.45678],
                  'Latitude':[19.075983,21.145800,18.520430,28.704060,30.378940,20.783709,21.65734,21.65734,20.54321],
                   'Postal_Code':[80000,85000,90000,95000,75000,75087,11054,11054,8000]})
 
    df2 = pd.DataFrame({'Clinic_ID':[101,102,103,104,105,106,107,107,108],
                    'Phone_Number':["+918000987689","8598785456","+91-9000890178","09571298701","(95) 7789816378", "8767342","9860496013","9860496013","9860496019"],
                    'email_ID':['lilavati@gmail.com','wokhartks.gmail','orangeCity@','vedanta@',None,'gmc@gmail.com','abc@yahho.com','abc@yahho.com','abc@abc.com']})            
                    

    df_final = pd.concat([df1,df2],axis=1)
    df_final = df_final.T.drop_duplicates().T
    df_final.to_csv('file1.csv',index=False)

    
    data_cleaning(df_final)
    
    # df_final['email_ID']=check_email(list(df_final['email_ID']))
    # df_final['Phone_Number'] = check_no(list(df_final['Phone_Number']))
    # df_final.dropna(subset=['email_ID'])
    # df_final= df_final[df_final != "None"]
    # df_fianl= df_final.dropna(axis=0,inplace=True)
    # df_final.to_csv('file1.csv')
    # print(df_final) 





