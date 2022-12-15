def boolean_func(boolean):
                                   
        agg = {}
        column_name = input("Enter column name(fields) to chech True or False: ").strip()
        dict_name = column_name
        agg[dict_name] = {}
        sub_column_name = input("Enter a condition  1.Equal to,2.Not equal:")
        while True:   
            value =  input("Enter a value True or False: ").lower()           
            if value == "true" or value=="false":
                yn = False if value == 'false' else True
                if sub_column_name == "1":
                    sub_dict = {f"$eq" : yn}  
                    agg[dict_name] = sub_dict
                    
                    return agg

                else:                                                   #[{'married': {'$eq': True}}]
                    sub_dict = {f"$ne" : yn}  
                    agg[dict_name] = sub_dict
                    return agg
            # agg_list.append(agg)   
            else:
                print("Enter valid input only : True or false is accepted")

                
# boolean = str(input("Enter Y or N TRUE OR FALSE for bool:")).lower()
# if boolean == "y":
#     agg = boolean_func(boolean)
#     agg_list.extend(agg)
def get_unset_boolean(unset_boolean):
    agg_list = []                                   
    agg = {}
    dict_name = "$unset"
    agg[dict_name] = {}
    column_name = input("Enter single or multiple columns names(each name should be sperated by comma symbol) to unset --> to hide columns(fields): ").strip().split(",")
    agg[dict_name] = column_name
    agg_list.append(agg)
    return agg_list

def get_match_boolean(match_boolean):
    agg_list = []
    size =  int(input("How many columns you need for match/filter ?: "))
    for i in range(size):
        agg = {}
        dict_name = "$match"
        agg[dict_name] = {}
        column_name = str(input(f"Enter column {i+1} name for match: "))
        value = input("Enter the value name: ")
        agg[dict_name][column_name] = value
        
        if value.isdigit():
            
            sub_column_name = (input("Enter a condition name --> 1.Equal to,2.Not equal,3.Greater than, 4.Less than,5.Greater than equal, 6.Less than equal:"))           
            if sub_column_name == "1":
                    sub_dict = {f"$eq" : value}  
                    agg[dict_name][column_name] = sub_dict
                        
            elif sub_column_name ==  "2":
                    sub_dict = {f"$ne" : value}
                    agg[dict_name][column_name] = sub_dict    
                        
            elif sub_column_name == "3":
                    sub_dict = {f"$gt" : value}
                    agg[dict_name][column_name] = sub_dict
                        
            elif sub_column_name == "4":
                    sub_dict = {f"$lt" : value}
                    agg[dict_name][column_name] = sub_dict
                        
            elif sub_column_name == "5":
                    sub_dict = {f"$gte" : value}
                    agg[dict_name][column_name] = sub_dict
                        
            elif sub_column_name == "6":
                    sub_dict = {f"$lte" : value}
                    agg[dict_name][column_name] = sub_dict


        agg_list.append(agg)    
# boolean = str(input("Enter Y or N TRUE OR FALSE for bool:")).lower()
# if boolean=="y":
#     agg_list.extend(boolean_func(boolean))

    return agg_list

def get_sort_boolean(sort_boolean):
    agg_list = []
    agg = {}
    dict_name = "$sort"
    agg[dict_name] = {}
    column_name = input("Enter a column name sort: ")
    value = input(("Enter 1 for ascending order OR Enter -1 for descending order : ") or "1") #check
    if value == "1":
            pass
    elif value == "-1":
        pass
    else:
        value = 1   
    if not isinstance(value, str) and value == "-1" or "1":
        value = int(value)
        agg[dict_name][column_name] = value
        
    else:
        agg[dict_name][column_name] = 1
    agg_list.append(agg)
    print(agg_list,"-------------> Used to sort the document that is rearranging them")
    return agg_list

def get_limit_boolean(limit_boolean):   
    agg_list = []
    agg = {}
    column_name = "$limit"
    value = int(input("Enter limit to restrict how many documents you want to fetch : ")or "10")
    agg[column_name]= value
    agg_list.append(agg)

    return agg_list


def get_project_boolean(project_boolean):
    agg_list = []
    agg = {}
    dict_name = "$project"
    agg[dict_name]={}
    # for_project_stage = str(input("Do you want to show specific columns Y or N : ")).lower()
    column_name = input("Enter a column name project to show specific columns(fields): ").split(",")
    sub_dict={}
    for column in column_name:
        column = column.strip()
        sub_dict[column]= 1
    agg[dict_name]=sub_dict
    agg_list.append(agg)
                                                                 
    return agg_list                                    #  Diffence between project and unset #
                                        # {"$project":{"name": 1,"age": 1} <--> {'$unset': ['_id', 'age']} #
        

def get_group_boolean(total_records,column_name,condition,sub_condition):
    if sub_condition.isdigit():
        sub_condition = int(sub_condition)
    else:
        sub_condition = "$" + sub_condition
    agg_list = []
    agg = {}
    dict_name = '$group'
    agg[dict_name] = {}
    column_name1 = "_id"
    
    agg[dict_name][column_name1] = "$"+column_name
    
    condition = "$"+condition
    value2 = {condition:sub_condition}
    agg[dict_name][total_records] = value2
    agg_list.append(agg)    
    return agg_list       

           
def query_generator():
    agg_list = []

    unset_boolean = str(input("Enter Y or N for unset to hide columns(fields):")).lower()
    if unset_boolean == "y":
        agg = get_unset_boolean(unset_boolean)
        agg_list.extend(agg)

    match_boolean = str(input("Enter Y or N for match used for filtering the documents based on columns:")).lower()
    if match_boolean == "y":
        agg = get_match_boolean(match_boolean)
        agg_list.extend(agg)

    sort_boolean = str(input("Enter Y or N for sort Document rearrangment into ascending or descending order:")).lower()
    if sort_boolean == "y":
        agg = get_sort_boolean(sort_boolean)
        
        agg_list.extend(agg)

    limit_boolean = str(input("Enter Y or N for limit to restrict how many documents you want to fetch: ")).lower()
    if limit_boolean == "y":
        agg = get_limit_boolean(limit_boolean)
        
        agg_list.extend(agg)

    project_boolean = str(input("Do you want to show specific columns?, default-all (Y/N)")).lower()
    if project_boolean == "y":
        agg = get_project_boolean(project_boolean)
        agg_list.extend(agg)

    group_boolean = str(input("Enter Y or N for group used to group documents based on some value :")).lower()
    if group_boolean == "y":
        total_records = "total records"                           #in $group _id is Mandatory field
        column_name = input("Enter the column name to group:")
        condition =input("Enter the condition:")
        sub_condition = input("Enter the value for the condition:")
        agg = get_group_boolean(total_records,column_name,condition,sub_condition)
        agg_list.extend(agg) 
    print(agg_list,"<------------------->")
    return agg_list
        
# agg=[{"$group" : {"_id": "$address","TotalRecords": {"$max" :"$age" }}}]
    
# print(query_generator())
  
   
   

                            
     

                                                    
                                                   

