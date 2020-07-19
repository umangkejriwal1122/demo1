#!C:\Users\UMANG KEJRIWAL\AppData\Local\Programs\Python\Python38-32\python

print ()
import cgi
#pip install mysql-connector-python
#pip install mysql-connector
import mysql.connector
import time

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="iot"
)

mycursor = mydb.cursor()

sql = "INSERT INTO home (data_values) VALUES (%s)"
val = str(("John"))
mycursor.execute(sql, (val,))

mydb.commit()

print(mycursor.rowcount, "record inserted.")