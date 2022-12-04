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
         'blas@breakthru.com', 'post', 'prefers correspondence by mail', 1),
        (4, 'Young\'s market', '1 Young CIR', 'Suite 100', 56489, 'George', 'Young', '321-456-9870',
         'gyoung@youngsmarket.com', 'online', 'I\'m not really sure what should be here', 1),
    ]
    mycursor.executemany(supplier, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into supplier table")

    # Supplies table
    supplies = ("INSERT INTO supplies (supply_ID, name, description, onhand_quantity, unit_price, Supplier_ID,"
                "Supply_order_ID)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    values = [
        (1, 'Corks', 'Environment Friendly', 1548, 0.25, 1, 1111),
        (2, 'Bottles', '750 ML', 254, 1.20, 1, 2222),
        (3, 'Labels', 'Display product on Bottle', 2455, 0.05, 4, 3333),
        (4, 'Tubing', 'For Processing', 25, 25, 3, 4444),
        (5, 'Vats', 'For Fermenting', 12, 2500, 3, 5555),
        (6, 'Boxes', '6 bottle size', 1258, 2, 4, 6666),
    ]
    mycursor.executemany(supplies, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into supplies table")

    # Supply_order_details table
    supply_order_details = ("INSERT INTO supply_order_details (supply_order_ID, Supply_ID, quantity_ordered)"
                            "VALUES (%s, %s, %s)")
    values = [
        (1111, 1, 10000),
        (2222, 2, 10000),
        (3333, 3, 10000),
        (4444, 4, 100),
        (5555, 5, 10),
        (6666, 6, 10000),
    ]
    mycursor.executemany(supply_order_details, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into supply order details table")
    # Im not sure how to go about calculating sum of quantity from supply_order_details
    # and unit price from supplies I will double back to this
    # Supply_order table
    # supply_order = ("INSERT INTO supply_order (supply_order_ID, total_cost, Order_date, Order_Method,"
    #                "Order_tracking_number, Order_delivery_carrier, Order_Estimated_Delivery_date,"
    #               " Order_Actual_Delivery_Date, Supply_ID, Supplier_ID)"
    #              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

    # values = [
    #    (1111, SUM(bacchus_wine.), 'Environment Friendly', 1548, 0.25, 1, 1111),
    #    (2222, '', '750 ML', 254, 1.20, 1, 2222),
    #    (3333, '', 'Display product on Bottle', 2455, 0.05, 4, 3333),
    #    (4444, '', 'For Processing', 25, 25, 3, 4444),
    #    (5555, '', 'For Fermenting', 12, 2500, 3, 5555),
    #   (6666, '', '6 bottle size', 1258, 2, 4, 6666),
    # ]
    # mycursor.executemany(supply_order, values)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted into supply order table")

    # Wine table
    wine = "INSERT INTO Wine (Wine_ID, Name, Style, onhand_quantity, Batch_id, Cost) VALUES (%s, %s, %s, %s, %s, %s)"
    values = [
        (1, 'Dark and Red', 'Merlot', 300, 2022010101, 15.00),
        (2, 'Crimson Silk', 'Cabernet', 257, 2022010102, 15.00),
        (3, 'Bright and Bold', 'Chablis', 124, 2022010103, 12.00),
        (4, 'Clean and Smooth', 'Chardonnay', 272, 2022010104, 8.00),
        (5, 'Rare Velvet', 'Chardonnay', 90, 2022042701, 25.00),
        (6, 'Anniversary Cask', 'Merlot', 37, 2022021401, 40.00)
    ]
    mycursor.executemany(wine, values)
    mydb.commit()
    print(mycursor.rowcount, " rows were inserted into the Wine table")

 # Batch table
    batch = "INSERT INTO batch (Batch_ID, Bottled_date, Expiration_Date, Quantity, Wine_id) "
            "VALUES (%s, %s, %s, %s, %s)"
    values = [
        (2022010101, '2022-08-01', '2024-08-01', 200, 1),
        (2022010102, '2022-10-01', '2023-10-01', 200, 2),
        (2022010103, '2022-02-02', '2023-02-02', 200, 3),
        (2022010104, '2022-02-02', '2023-02-02', 200, 4),
        (2022042701, '2022-03-01', '2023-03-01', 100, 5),
        (2022021401, '2022-12-01', '2024-12-01', 100, 6)
    ]
    mycursor.executemany(batch, values)
    mydb.commit()
    print(mycursor.rowcount, " rows were inserted into the Batch table")