import mysql.connector

def print_tables():

    db = mysql.connector.connect(
        user="bacchus_user",
        password="mysqltest",
        host="localhost",
        database="bacchus_wine"
    )

    cursor = db.cursor()
    
        cursor.execute("Show tables;")

    results = cursor.fetchall()

    for tables in results:
        print(tables)
