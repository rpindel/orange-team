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
    supplier = "INSERT INTO" supplier (Supplier_ID, Name, Street_Address, Street_Address2, zip, Contact_First_Name, Contact_Last_Name)