def sales():

    db = mysql.connector.connect(
        user="bacchus_user",
        password="mysqltest",
        host="localhost",
        database="bacchus_wine"
    )

    cursor = db.cursor()

    cursor.execute('''SELECT Supplier_ID, Supplier_name, order_method,
    Supply_ID, Supply_name, Unit_Price from Supplier inner
    join supplies on supplier.Supplier_ID=supplies.Dupplier_ID inner
    join supply_order;''')

    supplies = cursor.fetchall()

    for supply in supplies:
        print('''Supplier ID:{}\nSupplier Name:{}\nOrder Method:{}\nSupply ID:{}\nSupply Name:{}\n
        Unit Price:{}\n'''.format(supply[0], supply[1], supply[2], supply[3], supply[4], supply[5]))
