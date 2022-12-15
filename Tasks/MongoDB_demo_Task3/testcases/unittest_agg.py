import unittest
from demo import connection



class TestStringMethods(unittest.TestCase):
    
    def test_1(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = []
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'smt', 'age': '30', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}, {'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': ['Cooking', 'Sports']}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'Viola', 'address': 'Sideway 1633'}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '28', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26'}, {'name': 'jayant', 'age': '16'}, {'name': 'jayant', 'age': '23'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}])
    
    
    def test_2(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = [{ "$unset": ["_id"] },{'$match': {'age': "30"}}]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'smt', 'age': '30', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}])

    def test_3(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = [{ "$unset": ["_id"] },{ "$sort": { "address" : -1 } }]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'Viola', 'address': 'Sideway 1633'}, {'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '28', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'smt', 'age': '30', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': ['Cooking', 'Sports']}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26'}, {'name': 'jayant', 'age': '16'}, {'name': 'jayant', 'age': '23'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}])

    def test_4(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = [{ "$unset": ["_id"] },{ "$sort" : { "age" : 1,"_id": 1 } } ]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'Viola', 'address': 'Sideway 1633'}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', 'age': '16'}, {'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jayant', 'age': '23'}, {'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26'}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': ['Cooking', 'Sports']}, {'name': 'jk', 'age': '28', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'smt', 'age': '30', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': ['news', 'Sports']}])





    def test_5(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = ([{ "$unset": ["_id"] },{"$unwind":"$hobbies"}])
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': 'news'}, {'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': 'Sports'}, {'name': 'smt', 'age': '30', 'address': 'Nagpur', 'hobbies': 'news'}, {'name': 'smt', 'age': '30', 'address': 'Nagpur', 'hobbies': 'Sports'}, {'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': 'Football'}, {'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': 'cooking'}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': 'Cricket'}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': 'Football'}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': 'Cooking'}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': 'Sports'}, {'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': 'news'}, {'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': 'Sports'}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': 'news'}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': 'Sports'}, {'name': 'sl', 'hobbies': 'news'}, {'name': 'sl', 'hobbies': 'Sports'}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': 'news'}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': 'Sports'}, {'name': 'sl', 'hobbies': 'news'}, {'name': 'sl', 'hobbies': 'Sports'}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': 'news'}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': 'Sports'}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': 'news'}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': 'Sports'}, {'name': 'jk', 'age': '28', 'address': 'Pune', 'hobbies': 'news'}, {'name': 'jk', 'age': '28', 'address': 'Pune', 'hobbies': 'Sports'}])

    def test_6(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = ([{"$project":{"name": 1,"age": 1,"_id": 0}}])
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'abc', 'age': '26'}, {'name': 'smt', 'age': '30'}, {'name': 'bbb', 'age': '20'}, {'name': 'ggg', 'age': '26'}, {'name': 'xyz', 'age': '27'}, {'name': 'Chuck'}, {'name': 'Viola'}, {'name': 'Chuck'}, {'name': 'jk', 'age': '32'}, {'name': 'jk', 'age': '26'}, {'name': 'sl'}, {'name': 'jk', 'age': '22'}, {'name': 'sl'}, {'name': 'jk', 'age': '26'}, {'name': 'jk', 'age': '26'}, {'name': 'jk', 'age': '28'}, {'name': 'jk', 'age': '26'}, {'name': 'jayant', 'age': '16'}, {'name': 'jayant', 'age': '23'}, {'name': 'jayant'}, {'name': 'jayant'}, {'name': 'jayant'}])

    def test_7(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = ([{ "$unset": ["_id"] },{"$match":{"age":{"$lt":"25"}}}])
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jayant', 'age': '16'}, {'name': 'jayant', 'age': '23'}])


    def test_8(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = ([{ "$unset": ["_id"] },{"$match":{"age":{"$gt":"30"}}}])
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': ['news', 'Sports']}])



    def test_9(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = ([{ "$unset": ["_id"] },{"$match":{"age":{"$ne":"26"}}}])
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'smt', 'age': '30', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}, {'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': ['Cooking', 'Sports']}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'Viola', 'address': 'Sideway 1633'}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '28', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jayant', 'age': '16'}, {'name': 'jayant', 'age': '23'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}])

    def test_10(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = ([{ "$unset": ["_id"] },{"$match":{"age":{"$eq":"20"}}}])
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}])

    # def test_11(self):
    #     host = "localhost"
    #     port ="27017"
    #     database_name = "demoDatabase"
    #     table_name = "user_details"
    #     column_name = []
    #     where = {}
    #     agg = [{"$group" : {"_id": "$age", "TotalRecords": {"$sum" : 1}}}] 
    #     conn_str = f"mongodb://{host}:{port}/"


    #     self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'_id': '32', 'TotalRecords': 1}, {'_id': '26', 'TotalRecords': 6}, {'_id': '16', 'TotalRecords': 1}, {'_id': '23', 'TotalRecords': 1}, {'_id': '20', 'TotalRecords': 1}, {'_id': None, 'TotalRecords': 8}, {'_id': '28', 'TotalRecords': 1}, {'_id': '22', 'TotalRecords': 1}, {'_id': '27', 'TotalRecords': 1}, {'_id': '30', 'TotalRecords': 1}])

    def test_12(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = [{ "$group" : { "_id":"null", "min": { "$min" : "$age" }}}]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'_id': 'null', 'min': '16'}])

    def test_13(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = [{ "$group" : { "_id":"null", "max": { "$max" : "$age" }}}]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'_id': 'null', 'max': '32'}])


    def test_14(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = [{"$match": {"age": {"$gt": "27"}}},{"$count": "matured age"}]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'matured age': 3}])
    
    def test_15(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = ([{"$project":{"name": 1,"age": 1,"ageEq30": { "$eq": [ "$age", "30" ] },"_id": 0}}])
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'abc', 'age': '26', 'ageEq30': False}, {'name': 'smt', 'age': '30', 'ageEq30': True}, {'name': 'bbb', 'age': '20', 'ageEq30': False}, {'name': 'ggg', 'age': '26', 'ageEq30': False}, {'name': 'xyz', 'age': '27', 'ageEq30': False}, {'name': 'Chuck', 'ageEq30': False}, {'name': 'Viola', 'ageEq30': False}, {'name': 'Chuck', 'ageEq30': False}, {'name': 'jk', 'age': '32', 'ageEq30': False}, {'name': 'jk', 'age': '26', 'ageEq30': False}, {'name': 'sl', 'ageEq30': False}, {'name': 'jk', 'age': '22', 'ageEq30': False}, {'name': 'sl', 'ageEq30': False}, {'name': 'jk', 'age': '26', 'ageEq30': False}, {'name': 'jk', 'age': '26', 'ageEq30': False}, {'name': 'jk', 'age': '28', 'ageEq30': False}, {'name': 'jk', 'age': '26', 'ageEq30': False}, {'name': 'jayant', 'age': '16', 'ageEq30': False}, {'name': 'jayant', 'age': '23', 'ageEq30': False}, {'name': 'jayant', 'ageEq30': False}, {'name': 'jayant', 'ageEq30': False}, {'name': 'jayant', 'ageEq30': False}])
    
    # def test_16(self):
    #     host = "localhost"
    #     port ="27017"
    #     database_name = "demoDatabase"
    #     table_name = "user_details"
    #     column_name = []
    #     where = {}
    #     agg = ([{"$group": {"_id":"$name",  "min_age":{"$min":"$age"} } }])
    #     conn_str = f"mongodb://{host}:{port}/"


    #     self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'_id': 'xyz', 'min_age': '27'}, {'_id': 'Chuck', 'min_age': None}, {'_id': 'Viola', 'min_age': None}, {'_id': 'ggg', 'min_age': '26'}, {'_id': 'abc', 'min_age': '26'}, {'_id': 'bbb', 'min_age': '20'}, {'_id': 'jayant', 'min_age': '16'}, {'_id': 'jk', 'min_age': '22'}, {'_id': 'smt', 'min_age': '30'}, {'_id': 'sl', 'min_age': None}])

    def test_17(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = [{ "$unset": ["_id"] },{'$group': {'_id': "$_id","min": { "$min" : "$age" }}}]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'_id': None, 'min': '16'}])

    def test_18(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = [{ "$unset": ["_id"] },{'$group': {'_id': "$_id","max": { "$max" : "$age" }}}]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'_id': None, 'max': '32'}])

    def test_19(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = ([{ "$unset": ["_id"] },{"$match":{"name":"jk"}},{'$sort': {'age': -1}},{"$limit":1}])
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': ['news', 'Sports']}])
    
    def test_20(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = ([{ "$unset": ["_id"] },{"$match":{"name":"jk"}},{'$sort': {'age': 1}},{"$limit":3}])
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}])

   
    def test_21(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {}
        agg = [{ "$unset": ["_id"] },{"$match" : {"age" : {"$gt" : "20", "$lt" : "30"}}}] #between
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where,agg),[{'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': ['Cooking', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '28', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26'}, {'name': 'jayant', 'age': '23'}])

if __name__ == '__main__':
    unittest.main()