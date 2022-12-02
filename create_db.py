import mysql.connector

db = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
)

cursor=db.cursor()

cursor.execute('''CREATE DATABASE 'bacchus_wine';''')


