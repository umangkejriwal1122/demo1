#!C:\Users\UMANG KEJRIWAL\AppData\Local\Programs\Python\Python38-32\python
print('Content-type:text/html')
print ()
import cgi
#pip install mysql-connector-python
#pip install mysql-connector
print("<h1>Hello</h1>")
import mysql.connector
import time

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="test"
)

form = cgi.FieldStorage()
n = form.getvalue("name");

mycursor = mydb.cursor()

sql = "INSERT INTO data (name) VALUES (%s)"
val = str(n)
mycursor.execute(sql, (val,))
mydb.commit()
print(mycursor.rowcount, "record inserted.")
redirectURL = "http://www.google.com"
print('<html>')
print('<head>')
print('<meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('</head>')
print('</html>')
