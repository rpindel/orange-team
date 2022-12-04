import mysql.connector

def print_tables():

    db = mysql.connector.connect(
        user="bacchus_user",
        password="mysqltest",
        host="localhost",
        database="bacchus_wine"
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM supplier;")

    results = cursor.fetchall()

    print("\n***{}***".format(title))

    for tables in results:
        print("Supplier ID: {}\nName: {}\nAddress: {}\nAddress2: {}\nZip code: {}\nFirst name: {}\nLast name: {}\nPhone: {}\nEmail: {}\nOrder Method: {}\nMisc: {}\nActive: {}\n".format(tables[0], tables[1], tables[2], tables[3], tables[4], tables[5], tables[6], tables[7], tables[8], tables[9], tables[10], tables[11], tables[12]))
        print("\n")