import unittest
from demo import insert_doc



class TestStringMethods(unittest.TestCase):
    def test_1(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        insert_record =[{'name': 'jayant', '': '26'}]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(insert_doc(conn_str,database_name,table_name,insert_record),[{'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'smt', 'age': '30', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}, {'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': ['Cooking', 'Sports']}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'Viola', 'address': 'Sideway 1633'}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '28', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26'}, {'name': 'jayant', 'age': '16'}, {'name': 'jayant', 'age': '23'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}])

    
    def test_2(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        insert_record =[{'name': 'jayant', '': '26'},{'name': 'jayant', '': '26'}]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(insert_doc(conn_str,database_name,table_name,insert_record),[{'name': 'abc', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'smt', 'age': '30', 'address': 'Nagpur', 'hobbies': ['news', 'Sports']}, {'name': 'bbb', 'age': '20', 'address': 'Solapur', 'hobbies': ['Football', 'cooking']}, {'name': 'ggg', 'age': '26', 'address': 'Nagpur', 'hobbies': ['Cricket', 'Football']}, {'name': 'xyz', 'age': '27', 'address': 'Mumbai', 'hobbies': ['Cooking', 'Sports']}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'Viola', 'address': 'Sideway 1633'}, {'name': 'Chuck', 'address': 'Main Road 989'}, {'name': 'jk', 'age': '32', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '22', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'sl', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '28', 'address': 'Pune', 'hobbies': ['news', 'Sports']}, {'name': 'jk', 'age': '26'}, {'name': 'jayant', 'age': '16'}, {'name': 'jayant', 'age': '23'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'}, {'name': 'jayant', '': '26'},{'name': 'jayant', '': '26'}])


    def test_3(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        insert_record =[]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(insert_doc(conn_str,database_name,table_name,insert_record),[])


    def test_4(self):
        host = "localhost"
        port ="27017"
        database_name = "demoDatabase"
        table_name = "user_details"
        insert_record =[()]
        conn_str = f"mongodb://{host}:{port}/"


        self.assertEqual(insert_doc(conn_str,database_name,table_name,insert_record),[()])    


if __name__ == '__main__':
    unittest.main()        