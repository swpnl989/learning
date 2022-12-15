import pandas as pd


def create_csv_from_mongo_query(documents):
    df = pd.DataFrame(documents)
    w_csv_name = input("Want to give custom csv name press Y or N").lower()
    if w_csv_name == 'y':
        name_csv = input("Enter csv name without extension")
        df.to_csv(name_csv+".csv", index=False)
    else:
        df.to_csv("output.csv", index=False)


def create_dic_insert(list1, list2): 
    if len(list1) == len(list2): 
        print("True") 
    else: 
        print("False") 
        
    res = {list1[i]: list2[i] for i in range(len(list1))} 
    return res    


def insert_list(mycol, list_1):
    if isinstance(list_1, list):
        try:
            mycol.insert_many(list_1)
        except Exception as e:
            print(e)
    else:
        raise TypeError("Only list are allowed in where")


def insert_doc(mycol, list1, insert_record=[]):
    list3 = []
    for i in range(len(list1)):
        list2 = input(f"Enter values for {list1[i]}\t: ").split(",")
        if len(list2) == 1:
            list2=list2[0]
            if list2 == 'true' or list2 == 'false':
                list3.append(bool(list2))                      
                print(type(list3),'_____________')
            else:
                list3.append(list2)
        else:
            list3.append(list2)
            
    insert_record = [create_dic_insert(list1, list3)]
    print(insert_record)
    if isinstance(insert_record, list):
        try:
            mycol.insert_many(insert_record)
        except Exception as e:
            print(e)
    else:
        raise TypeError("Only list are allowed in where")


def insert_csv(mycol, csv_name):
    df = pd.read_csv(csv_name)
    data = df.to_dict(orient ="records")
    mycol.insert_many(data)