import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='@Alda0969166236'
    )

    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print('Database "alx_book_store" created sucessfully!')

except mysql.connector.Error as e:
    print(f'Error: Could not connect to MYSQL server or create database: {e}')

finally:
    if mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MYSQL connection closed.")