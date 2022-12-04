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
            f"Supply ID: {tables[0]}\nName: {tables[1]}\nDescription: {tables[2]}\nAvailable: {tables[3]}\nCost: {tables[4]}\nSupplier ID: {tables[5]}")
        print("\n")

    cursor.execute("SELECT * FROM supply_order_details;")

    results = cursor.fetchall()

    print("\n***Supply Order Details")

    for tables in results:
        print(
            f"Supply Order ID: {tables[0]}\nSupply ID: {tables[1]}\nQuantity Ordered: {tables[2]}\n")

    cursor.execute("SELECT * FROM supply_order;")

    results = cursor.fetchall()

    print("\n***Supply Order***")

    for tables in results:
        print(
            f"Supply Order ID: {tables[0]}\nTotal Cost: {tables[1]}\nOrder Date: {tables[2]}\nOrder Method: {tables[3]}\nTracking Number: {tables[4]}\nCarrier: {tables[5]}\nEstimated Delivery Date: {tables[6]}\nActual Delivery Date: {tables[7]}\nSupplier ID: {tables[8]}\n")

    cursor.execute("SELECT * FROM wine;")

    results = cursor.fetchall()

    print("\n***Wine***")

    for tables in results:
        print(
            f"Wine ID: {tables[0]}\nName: {tables[1]}\nStyle {tables[2]}\nOn-Hand: {tables[3]}\nBatch ID: {tables[4]}\nCost: {tables[5]}\n")

    cursor.execute("SELECT * FROM batch;")

    results = cursor.fetchall()

    print("\n***Batch***")

    for tables in results:
        print(
            f"Batch ID: {tables[0]}\nBottled On: {tables[1]}\nExpiration: {tables[2]}\nBatch Quantity: {tables[3]}\nWine ID: {tables[4]}\n")

    cursor.execute("SELECT * FROM wine_order;")

    results = cursor.fetchall()

    print("\n***Wine Orders***")

    for tables in results:
        print(
            f"Wine Order ID: {tables[0]}\nTotal Cost: {tables[1]}\nOrder Date: {tables[2]}\nOrder Method: {tables[3]}\nEstimated Delivery Date: {tables[4]}\nActual Delivery Date: {tables[5]}\nDistributor ID: {tables[6]}\n")

    cursor.execute("SELECT * FROM wine_order_details;")

    results = cursor.fetchall()

    print("\n***Wine Order Details***")

    for tables in results:
        print(
            f"Wine Order ID: {tables[0]}\nWine ID{tables[1]}\nQuantity Ordered: {tables[2]}\n")

    cursor.execute("SELECT * FROM distributor;")

    results = cursor.fetchall()

    print("\n***Distributors***")

    for tables in results:
        print(
            f"Distributor ID: {tables[0]}\nName: {tables[1]}\nAddress 1: {tables[2]}\nAddress 2: {tables[3]}\nZip Code: {tables[4]}\nFirst Name: {tables[5]}\nLast Name: {tables[6]}\nPhone: {tables[7]}\nEmail: {tables[8]}\nActive: {tables[9]}")

    cursor.execute("SELECT * FROM wine_distributor_details;")

    results = cursor.fetchall()

    print("\n***Wine Distributor Details")

    for tables in results:
        print(
            f"Wine ID: {tables[0]}\nDistributor ID: {tables[1]}\n")
