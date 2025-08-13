import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (without selecting a DB yet)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
