import sqlite3
from contextlib import closing

class MyDB:
    def __init__(self, path):
        self.path = path
        
    def insert(self, name_table, name_column, data):
        with closing(sqlite3.connect(self.path)) as connection:
            cursor = connection.cursor()
            try :
                cursor.execute("INSERT INTO %s(%s) VALUES('%s')"%(name_table, name_column, data))
            except sqlite3.Error as e:
                print('sqlite3.Error occurred:', e.args[0])
            connection.commit()

    def print_db(self, table_name):
        with closing(sqlite3.connect(self.path)) as connection:
            cursor = connection.cursor()
            try :
                cursor.execute("SELECT * FROM %s"%table_name)
                for row in cursor.execute("SELECT * FROM %s"%table_name):
                    print(row)
            except sqlite3.Error as e:
                print('sqlite3.Error occurred:', e.args[0])
            connection.commit()
