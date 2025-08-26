import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

# prepare cursor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE {database name}")

print("All Done!!")
