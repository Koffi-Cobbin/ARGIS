__author__ = 'Koffi Cobbin'
import MySQLdb 
from MySQLdb.cursors import DictCursor
from config import mysql


class Database(object):
    ''' This is a code base for handling MySQL instructions '''

    @staticmethod
    def connect(query):
        cursor = mysql.connection.cursor(cursorclass=DictCursor) # The cursorclass arg was passed to override the default tuple output as a dict
        cursor.execute(f''' {query}''') # f string was used bc passing just the query wasn't working, it needed the quotes to execute
        mysql.connection.commit()
        return cursor

    @staticmethod
    def disconnect(cursor):
        cursor.close()
        return "Done!"

    @staticmethod
    def insert(table_name, data):
        ''' This piec of code generates a query based on the args given to pass to the db 
            :data = list of values to insert
            :table = table_name to insert data into 
        '''
        query = '''INSERT INTO ''' + table_name + ''' VALUES('''
        for value in data:
            if (value == data[len(data)-1]):
                query = query + "'"+ value + "')" if (type(value) == str) else query + str(value) + ")"
            else:
                query = query + "'"+ value + "'," if type(value) == str else query + str(value) + ","
        return Database.disconnect(Database.connect(query))


    @staticmethod
    def select_from_where(columns, table_name, data=None):
        query = ''' SELECT '''
        if type(columns)==list:
            for column in columns:
                query = query + column if column == columns[len(columns)-1] else query + column + ", "
        else:
            query = query + columns  

        if data:
            query = query + ''' FROM ''' + table_name + ''' WHERE ''' + data
        else:
            query = query + ''' FROM ''' + table_name 
        cursor = Database.connect(query)
        result = cursor.fetchall()
        val = Database.disconnect(cursor)
        return result

    @staticmethod
    def update(table_name, values, condition):
        query = '''UPDATE ''' + table_name + ''' SET ''' + values + ''' WHERE ''' + condition
        cursor = Database.connect(query)
        val = Database.disconnect(cursor)
        return "Done!!"

    @staticmethod
    def find_one(table, query):
        return None
 
    

    @staticmethod
    def remove(table, query):
        None

    
        
