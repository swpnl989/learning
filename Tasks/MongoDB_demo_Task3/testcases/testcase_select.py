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

        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where), [{'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'smt', 'age': '26', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}, {'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': ['Cooking', 'Sports']}])

    def test_2(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = ["name"]
        where = {}

        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where),[{'name': 'abc'}, {'name': 'smt'}, {'name': 'bbb'}, {'name': 'ggg'}, {'name': 'xyz'}])



    def test_3(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = ["name","address"]
        where = {}

        conn_str = f"mongodb://{host}:{port}/"

        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where),[{'name': 'abc', 'address': 'Pune'}, {'name': 'smt', 'address': 'Nagpur'}, {'name': 'bbb', 'address': 'Solapur'}, {'name': 'ggg', 'address': 'Nagpur'}, {'name': 'xyz', 'address': 'Mumbai'}])

    def test_4(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {"age":"20"}

        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where),[{'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}])

    def test_5(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {"age":"26","address":"Nagpur"}

        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where),[{'name': 'smt', 'age': '26', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}])

    def test_6(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = ["address"]
        where = {"age":"26"}

        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where),[{'address': 'Pune'}, {'address': 'Nagpur'}, {'address': 'Nagpur'}])

    def test_7(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = ["name","hobbies"]
        where = {"age":"26","address":"Nagpur"}

        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where),[{'name': 'smt', 'hobbies': ['news', 'Sports']}, {'name': 'ggg', 'hobbies': ['Cricket', 'Football']}])

    def test_8(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {"hobbies":"Football"}

        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where),[{'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}])

    def test_9(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {"age":"26","hobbies":["Football","cooking"]}

        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where),[])

    def test_10(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        conn_str = f"mongodb://{host}:{port}/"

        self.assertEqual(connection(conn_str,database_name,table_name),[{'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'smt', 'age': '26', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}, {'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': ['Cooking', 'Sports']}] )

    def test_11(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = []
        where = {"age":""}

        conn_str = f"mongodb://{host}:{port}/"

        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where), [])

    def test_12(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = ["address"]
        where = {"age":""}

        conn_str = f"mongodb://{host}:{port}/"

        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where), []) 

    def test_13(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = ["name","address"]
        where = {"age":""}

        conn_str = f"mongodb://{host}:{port}/"

        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where), [])      

    def test_14(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = ["1234","SSSSS"]
        where = {"age":""}

        conn_str = f"mongodb://{host}:{port}/"

        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where), [])      

    def test_15(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        column_name = ["name"]
        where ={"age":26}

        conn_str = f"mongodb://{host}:{port}/"

        self.assertEqual(connection(conn_str,database_name,table_name,column_name,where),[])      
     
    



if __name__ == '__main__':
    unittest.main()

# def main():
#     TestStringMethods




