import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="bacchus_user",
    password="mysqltest",
    database="bacchus_wine"
)
mycursor = mydb.cursor()


def fill_tables():
    # fill supplier table
    supplier = ("INSERT INTO supplier (supplier_ID, name, Street_Address_1, Street_address_2, Zip, Contact_First_Name,"
                "Contact_Last_Name, Phone_Number, Email_Address, Order_Method, Order_Method_Details, Active)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    values = [
        (1, 'Southern Glazer', '2400 SW 145th AVE', 'Suite200', 33027, 'Angel', 'Garay', '305-627-1202',
         'angel.garay@shws.com', 'online', 'these are details', 1),
        (2, 'Republic National', '1114 Baldwin ST', 'and a half', 45678, 'Damian', 'Brown', '254-568-1245',
         'damian.brown@repubnat.com', 'phone', 'these are details', 0),
        (3, 'Breakthru', '4587 Somewhere RD', 'Null', 25896, 'Bob', 'Lasname', '896-456-2580',
         'blas@breakthru.com', 'post', 'prefers correspondace by mail', 1),
        (4, 'Young\'s market', '1 Young CIR', 'Suite 100', 56489, 'George', 'Young', '321-456-9870',
         'gyoung@youngsmarket.com', 'online', 'I\'m not really sure what should be here', 1),
            ]
    mycursor.executemany(supplier, values)
    mydb.commit()
    print(mycursor.rowcount, "was inserted into supplier table")

    # Supplies table
    supplies = ("INSERT INTO supplies (supply_ID, name, description, onhand_quantity, unit_price, Supplier_ID,"
                "Supply_order_ID)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    values = [
        (1, 'Corks', 'Environment Friendly', 1548, 0.25, 1, 0),
        (2, 'Bottles', '750 ML', 254, 1.20, 1, 0),
        (3, 'Labels', 'Display product on Bottle', 2455, 0.05, 4, 0),
        (4, 'Tubing', 'For Processing', 25, 25, 3, 0),
        (5, 'Vats', 'For Fermenting', 12, 2500, 3, 0),
        (6, 'Boxes', '6 bottle size', 1258, 2, 4, 0),
    ]
    mycursor.executemany(supplies, values)
    mydb.commit()
    print(mycursor.rowcount, "was inserted into supplier table")


