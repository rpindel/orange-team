import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "bacchus_user",
    password = "mysqltest",
    database = "bacchus_wine"
)
mycursor = mydb.cursor()
def fill_tables():
    # fill supplier table
    supplier = "INSERT INTO supplier (Supplier_ID, Name, Street_Address, Street_Address2, zip, Contact_First_Name, Contact_Last_Name, Phone_Number,Email_Address, order_method, active) VALUES (%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S,%S)"
    val = [
        (1,'Southern Glazer', '2400 SW 145th AVE', 'Suite200', 33027, 'Angel', 'Garay', '305-627-1202', 'angel.garay@shws.com', 'online', 'these are details', 'y')
    ]