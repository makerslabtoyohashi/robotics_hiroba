import sys
import threading

# original modules
import MyServer
import DBManager

#define
db = DBManager.MyDB('../data/sample.db')   # create table data(id integer primary key, log text);
port = '12345'

def myfunc(data):
    """ This function is executed when MyServer gets some data.
    Parameters
    ------
    data : str
        GET parameters.

    Returns
    ------
    message : str
        message to return to client
    """
    print('get data:', data)
    db.insert('data', 'log', data)
    message = 'ok'
    return message

if __name__ == '__main__':
    print('Server start')
    MyServer.start(port, myfunc)
    print('ctrl + c\nDataBase preview')
    db.print_db('data')
