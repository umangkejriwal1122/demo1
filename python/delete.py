#!C:\Users\UMANG KEJRIWAL\AppData\Local\Programs\Python\Python38-32\python

print ()
import cgi
print ("Content-Type: text/html")

import mysql.connector
import time

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="covid"
)

mycursor = mydb.cursor()

sql = "delete from data"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "Deleted")





