
import mysql.connector
from mysql.connector import Error

def connect():
    """THis function connects to database
    with password and root username
    it catches exeption when...."""

    try:
        mydb = mysql.connector.connect(host = "localhost", user = "root",
                               password = "root123456", database = "company")

        if mydb.is_connected():
            print('Connected to ' + mydb.database + " database")
            mycursor = mydb.cursor()
            mydb.close()

    except Error as e:
        print(e)

if __name__ == '__main__':
    print(connect.__doc__)
    #connect()