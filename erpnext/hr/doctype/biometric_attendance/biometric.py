import pyodbc
import mysql.connector

myDB = pyodbc.connect(
	DRIVER='{FreeTDS}',
	SERVER='114.143.174.98',
	PORT='999',
	DATABASE='etimetracklite1',
	UID="essl71",
	PWD='Zxcasqw@2019#$1@')

cHandler = myDB.cursor()
cHandler.execute('select UserId,C1,LogDate from DeviceLogs_10_2019')
   
connection=mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="_1bd3e0294da19198"
)

curs = connection.cursor() 

lst = []
result= cHandler.fetchall()
for row in result:
	print (row)
	lst.append(row)

sql = """INSERT INTO `biometric` (UserId,C1,LogDate) VALUES (%s,%s,%s)"""
curs.executemany(sql,lst)
#connection.commit()

