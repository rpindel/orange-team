import mysql.connector


def create_tables(cursor):
    ##create tables
    cursor.execute(
        """CREATE TABLE supply (Supplier_ID INT(11) NOT NULL, Name VARCHAR(45) NOT NULL, Street_Address_1 VARCHAR(35) NOT NULL, Street_Address_2 VARCHAR(35), Zip INT(5) NOT NULL, Contact_First_Name VARCHAR(25) NOT NULL, Contact_Last_Name VARCHAR(25) NOT NULL, Phone_Number VARCHAR(15) NOT NULL, Email_Address VARCHAR(45), Order_Method ENUM('Phone', 'Post', 'Online'), Order_Method_Details VARCHAR(45), Contract_Delivery_ETA BIT(1), Contract_Delivery_ETA_Details VARCHAR(45), Active BIT(1) NOT NULL, PRIMARY KEY(Supplier_ID);""")

    ##
    cursor.execute(
        "CREATE TABLE supplies (Supply_ID INT(11) NOT NULL, Name VARCHAR(25) NOT NULL, Description VARCHAR(45), Onhand_Quantity INT(11) NOT NULL, Unit_Price DECIMAL(6,2) NOT NULL, Supplier_ID INT(11) NOT NULL, Supply_Order_ID INT(20) NOT NULL, PRIMARY KEY(Supply_ID), CONSTRAINT fk_supplier FOREIGN KEY(Supplier_ID) REFERENCES supplier(Supplier_ID), CONSTRAINT fk_supply_order FOREIGN KEY(Supply_Order_ID) REFERENCES supply_order(Supply_Order_ID));")

    ##
    cursor.execute(
        "CREATE TABLE supply_order (Supply_Order_ID INT(20) NOT NULL, Total_Cost DECIMAL(10,2) NOT NULL, Order_Date DATETIME NOT NULL, Order_Method ENUM('Phone', 'Post', 'Online'), Order_Tracking_Number VARCHAR(30) NOT NULL, Order_Delivery_Carrier VARCHAR(10), Order_Estimated_Delivery_Date DATETIME, Order_Actual_Delivery_Date DATETIME NOT NULL, Supply_ID INT(11) NOT NULL, Supplier_ID INT(11) NOT NULL, PRIMARY KEY(Supply_Order_ID), CONSTRAINT fk_supplies FOREIGN KEY(Supply_ID) REFERENCES supplies(Supply_ID), CONSTRAINT fk_supplier FOREIGN KEY(Supplier_ID) REFERENCES supplier(Supplier_ID));")

    ##
    cursor.execute(
        "CREATE TABLE supply_order_details (PK_Supply_Order_ID INT(20) NOT NULL, PK_Supply_ID INT(11) NOT NULL, Quantity_Ordered INT(70) NOT NULL, PRIMARY KEY(Supply_Order_ID), PRIMARY KEY(Supply_ID));")

    ##
    cursor.execute(
        "CREATE TABLE wine (Wine_ID INT(11) NOT NULL, Name VARCHAR(45) NOT NULL, Style ENUM('Merlot', 'Cabernet', 'Chablis', 'Chardonnay') NOT NULL, Onhand_Quantity INT(7) NOT NULL, Batch_ID INT(20) NOT NULL, PRIMARY KEY(Wine_ID), CONSTRAINT fk_batch KEY(Batch_ID) REFERENCES batch(Batch_ID));")

    ##
    cursor.execute(
        "CREATE TABLE batch (Batch_ID INT(20) NOT NULL, Bottled_Date DATETIME, Expiration_Date DATETIME NOT NULL, Quantity INT(7) NOT NULL, Wine_ID INT(11) NOT NULL, PRIMARY KEY(Batch_ID), CONSTRAINT fk_wine FOREIGN KEY(Wine_ID) REFERENCES wine(Wine_ID));")

    ##
    cursor.execute(
        "CREATE TABLE wine_order (Wine_Order_ID INT(20) NOT NULL, Total_Cost DECIMAL(10, 2) NOT NULL, Order_Date DATETIME NOT NULL, Order_Method ENUM('Phone', 'Post', 'Online'), Order_Estimated_Delivery_Date DATETIME, Order_Actual_Delivery_Date DATETIME NOT NULL, FK_Wine_ID INT(11) NOT NULL, FK_Distributor_ID INT(11) NOT NULL, PRIMARY KEY(Wine_Order_ID), CONSTRAINT fk_wine FOREIGN KEY(Wine_ID) REFERENCES wine(Wine_ID), CONSTRAINT fk_distributor FOREIGN KEY(Distributor_ID) REFERENCES distributor(Distributor_ID));")

    ##
    cursor.execute(
        "CREATE TABLE wine_order_details (Wine_Order_ID INT(20) NOT NULL, Wine_ID INT(11) NOT NULL, Quantity_Ordered INT(7) NOT NULL, PRIMARY KEY(Wine_Order_ID), PRIMARY KEY(Wine_ID));")

    ##
    cursor.execute(
        "CREATE TABLE wine_distributor_details (PK_Wine_ID INT(11) NOT NULL, PK_Distributor_ID INT(11) NOT NULL, PRIMARY KEY(Wine_ID), PRIMARY KEY(Distributor_ID));")

    ##
    cursor.execute(
        "CREATE TABLE distributor (Distributor_ID INT(11) NOT NULL, Name VARCHAR(45) NOT NULL, Street_Address_1 VARCHAR(35) NOT NULL, Street_Address_2 VARCHAR(35), Zip INT(5) NOT NULL, Contact_First_Name VARCHAR(25) NOT NULL, Contact_Last_Name VARCHAR(25) NOT NULL, Phone_Number VARCHAR(15) NOT NULL, Email_Address VARCHAR(45), Active BIT(1) NOT NULL, FK_Wine_ID INT(11) NOT NULL, FK_Wine_Order_ID INT(20) NOT NULL, PRIMARY KEY(Distributor_ID), CONSTRAINT fk_wine FOREIGN KEY(Wine_ID) REFERENCES wine(Wine_ID), CONSTRAINT fk_wine_order FOREIGN KEY(Wine_Order_ID) REFERENCES wine_order(Wine_Order_ID));")

    ##
    cursor.execute(
        "CREATE TABLE employee (Employee_ID INT(11) NOT NULL, First_Name VARCHAR(25) NOT NULL, Last_Name VARCHAR(25) NOT NULL, Hire_Date DATE NOT NULL, Start_Date DATE, Active BIT(1) NOT NULL, Department_ID INT(5) NOT NULL, Position_ID INT(10) NOT NULL, PRIMARY KEY(Employee_ID), CONSTRAINT fk_department FOREIGN KEY(Department_ID) REFERENCES department(Department_ID), CONSTRAINT fk_position FOREIGN KEY(Position_ID) REFERENCES position(Position_ID));")

    ##
    cursor.execute(
        "CREATE TABLE employee_alternate (Street_Address_1 VARCHAR(35) NOT NULL, Street_Address_2 VARCHAR(35), Zip INT(5) NOT NULL, Phone_Number VARCHAR(15) NOT NULL, Email_Address VARCHAR(45), Term_Date DATE, Term_Reason VARCHAR(25), Rehireable BIT(1), SSN INT(9) NOT NULL, DOB DATE, Employee_ID INT(11) NOT NULL, CONSTRAINT fk_employee FOREIGN KEY(Employee_ID) REFERENCES employee(Employee_ID));")

    ##
    cursor.execute(
        "CREATE TABLE employe_time_worked (Date DATE NOT NULL, Clock_In_Shift TIME NOT NULL, Clock_Out_Shift TIME NOT NULL, Clock_Out_Break TIME, Clock_In_Break TIME, Clock_Out_Lunch TIME, Clock_In_Lunch TIME, Employee_ID INT(11) NOT NULL, CONSTRAINT fk_employee FOREIGN KEY(Employee_ID) REFERENCES employee(Employee_ID));")

    ##
    cursor.execute(
        "CREATE TABLE zip_lookup (Zip INT(5) NOT NULL, City VARCHAR(25) NOT NULL, State VARCHAR(10) NOT NULL, Country VARCHAR(20), PRIMARY KEY(Zip));")

    ##
    cursor.execute(
        "CREATE TABLE department (Department_ID INT(5) NOT NULL, Department_Name VARCHAR(15) NOT NULL, Department_Head INT(11), PRIMARY KEY(Department_ID));")

    ##
    cursor.execute(
        "CREATE TABLE position (PK_Position_ID INT(10) NOT NULL, Position_Title VARCHAR(25) NOT NULL, Pay_Grade INT(11), Hourly BIT(1), Supervisory BIT(1), PRIMARY KEY(Position_ID));")


def show_tables():
    cursor = db.cursor()

    cursor.execute("Show tables;")

    results = cursor.fetchall()

    for tables in results:
        print(tables)



def main():
    db = mysql.connector.connect(
        user="bacchus_user",
        password="mysqltest",
        host="localhost",
        database="bacchus_wine"
    )

    cursor = db.cursor()

    create_tables(cursor, "supply")

    newSupply = "INSERT INTO supply()"

    db.commit()
    cursor.execute(newSupply)


## drop statements
##cursor.execute("DROP DATABASE IF EXISTS 'bacchus_wine';")
##cursor.execute("DROP USER IF EXISTS 'bacchus_user'@'localhost';")
##cursor.execute("DROP TABLE IF EXISTS supplier;")
##cursor.execute("DROP TABLE IF EXISTS supplies;")
##cursor.execute("DROP TABLE IF EXISTS supply_order;")
##cursor.execute("DROP TABLE IF EXISTS supply_order_details;")
##cursor.execute("DROP TABLE IF EXISTS wine;")
##cursor.execute("DROP TABLE IF EXISTS batch;")
##cursor.execute("DROP TABLE IF EXISTS wine_order;")
##cursor.execute("DROP TABLE IF EXISTS wine_order_details;")
##cursor.execute("DROP TABLE IF EXISTS wine_distrbutor_details;")
##cursor.execute("DROP TABLE IF EXISTS distributor;")
##cursor.execute("DROP TABLE IF EXISTS employee;")
##cursor.execute("DROP TABLE IF EXISTS employe_alternate;")
##cursor.execute("DROP TABLE IF EXISTS employee_time_worked;")
##cursor.execute("DROP TABLE IF EXISTS zip_lookup;")
##cursor.execute("DROP TABLE IF EXISTS department;")
##cursor.execute("DROP TABLE IF EXISTS position;")


db.close()
