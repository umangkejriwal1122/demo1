#!C:\Users\UMANG KEJRIWAL\AppData\Local\Programs\Python\Python38-32\python

print ()
import cgi
print ("Content-Type: text/html")
import requests
from bs4 import BeautifulSoup as bs

link = 'https://www.mohfw.gov.in/'


page = requests.get(link)


soup = bs(page.content, 'html.parser')

data = (soup.find_all('div', class_='data-table table-responsive'))

all_data_td = (soup.find_all('td'))

all_data_list = []
for i in range(0,len(all_data_td)):
    all_data_list.append(all_data_td[i].get_text())

states = []
for i in range(1,len(all_data_list),6):
  states.append(all_data_td[i].get_text())
states = states[:-4]

active = []
for i in range(2,len(all_data_list),6):
  active.append(all_data_td[i].get_text())
active = active[:-4]

cured = []
for i in range(3,len(all_data_list),6):
  cured.append(all_data_td[i].get_text())
cured = cured[:-4]

death = []
for i in range(4,len(all_data_list),6):
  death.append(all_data_td[i].get_text())
death = death[:-4]

confirmed = []
for i in range(5,len(all_data_list),6):
  confirmed.append(all_data_td[i].get_text())
confirmed = confirmed[:-4]

import pandas as pd
df = pd.DataFrame()
df['States'] = states
df['Confirmed'] = confirmed
df['Cured'] = cured
df['Death'] = death
df['Active'] = active

df.to_csv(r'C:\Users\UMANG KEJRIWAL\Desktop\covid.csv', index=False, encoding='utf-8')


import mysql.connector
import time

mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="covid"
)

mycursor = mydb.cursor()

sql_del = "delete from data"

mycursor.execute(sql_del)

sql = "INSERT INTO data (state,confirmed,death,recovered,active) VALUES (%s,%s,%s,%s,%s)"

for i in range(0,len(states)):
	s = states[i]
	c = confirmed[i]
	r = cured[i]
	d = death[i]
	a = active[i]
	mycursor.execute(sql, (s,c,d,r,a))

mydb.commit()

print(mycursor.rowcount, "record inserted.")



