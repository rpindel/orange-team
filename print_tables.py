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

    print("\n***Suppliers***")

    for tables in results:
        print(
            f"Supplier ID: {tables[0]}\nName: {tables[1]}\nAddress: {tables[2]}\nAddress2: {tables[3]}\nZip code: {tables[4]}\nFirst name: {tables[5]}\nLast name: {tables[6]}\nPhone: {tables[7]}\nEmail: {tables[8]}\nOrder Method: {tables[9]}\nMisc: {tables[10]}\nActive: {tables[11]}\n")
        print("\n")

    cursor.execute("SELECT * FROM supplies;")

    results = cursor.fetchall()

    print("\n***Supplies***")

    for tables in results:
        print(
            f"Supply ID: {tables[0]}\nName: {tables[1]}\nDescription: {tables[2]}\nAvailable: {tables[3]}\nCost: {tables[4]}\nSupplier ID: {tables[5]}\nSupply Order ID: {tables[6]}")
        print("\n")
