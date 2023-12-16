import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root123'
)

#prepare a cursor object

cursorObject = dataBase.cursor()


#create a db
cursorObject.execute("CREATE DATABASE djangocrm")

print("DB Created")
