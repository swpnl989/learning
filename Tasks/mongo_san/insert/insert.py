import pandas as pd
from query_generator import *
from util import insert_csv, insert_doc


def insert_records(mycol):
    print(type(mycol))
    insert_csv_data = input("Do you wnat to inser CSV Y or N : ").lower()
    if insert_csv_data == "y":
        csv_name = input("Enter csv name : ")
        insert_csv(mycol, csv_name)
        return
    else:
        insert_data = input("Do you want to insert data press Y or N: ").lower()
        if insert_data == "y":
            list1 = input("Enter required column/fields name\t: ").split(",")
            while True:
                insert_doc(list1)
                ex= input("Want to exit press or enter data Y/N").lower()
                if ex=='y':
                    break
        else:
            insert_list = input("Do you want to insert list of document press Y or N: ").lower()
            if insert_list == "y":
                list_1 = (input("enter a list "))
                no_of_dict = 0
                l_new = []
                while no_of_dict<=list_1.count("{"):
                    a=list_1.find('{')
                    b=list_1.find('}')
                    l_new.append(list_1[a+1:b])
                    list_1=list_1[b+1:]
                    no_of_dict+=1
                list_1 = []
                for items in l_new:
                    di = {}
                    for sub_i in items.split(','):
                        key,value = sub_i.split(":")
                        if value.lower()=='true':
                            value=True
                        elif value.lower() == 'false':
                            value = False
                        di[key]=value
                    list_1.append(di)
                if insert_list == "y":
                    insert_list(list_1)