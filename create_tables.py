'''
Orange Group CSD-310 2022
'''

import mysql.connector
from mysql.connector import errorcode


config = {
    "user" : "bacchus_user",
    "password" : "mysqltest",
    "host" : "127.0.0.1",
    "database" : "bacchus_wine",
    "raise_on_warnings" : True
    }
    
db = mysql.connector.connect(**config)

cursor = db.cursor()


## create supplier table
cursor.execute("CREATE TABLE supplier (Supplier_ID INT NOT NULL, Name VARCHAR(45) NOT NULL, Street_Address_1 VARCHAR(35) NOT NULL, Street_Address_2 VARCHAR(35), Zip INT NOT NULL, Contact_First_Name VARCHAR(25) NOT NULL, Contact_Last_Name VARCHAR(25) NOT NULL, Phone_Number VARCHAR(15) NOT NULL, Email_Address VARCHAR(45), Order_Method ENUM('Phone', 'Post', 'Online'), Order_Method_Details VARCHAR(45), Active BIT(1) NOT NULL, PRIMARY KEY(Supplier_ID));")


## create supplies table
cursor.execute("CREATE TABLE supplies (Supply_ID INT NOT NULL, Name VARCHAR(25) NOT NULL, Description VARCHAR(45), Onhand_Quantity INT NOT NULL, Unit_Price DECIMAL(6,2) NOT NULL, Supplier_ID INT NOT NULL, Supply_Order_ID INT NOT NULL, PRIMARY KEY(Supply_ID));")


## create supply_order table
cursor.execute("CREATE TABLE supply_order (Supply_Order_ID INT NOT NULL, Total_Cost DECIMAL(10,2) NOT NULL, Order_Date DATETIME NOT NULL, Order_Method ENUM('Phone', 'Post', 'Online'), Order_Tracking_Number VARCHAR(30) NOT NULL, Order_Delivery_Carrier VARCHAR(10), Order_Estimated_Delivery_Date DATETIME, Order_Actual_Delivery_Date DATETIME NOT NULL, Supply_ID INT NOT NULL, Supplier_ID INT NOT NULL, PRIMARY KEY(Supply_Order_ID));")


## create supply_order_details table
cursor.execute("CREATE TABLE supply_order_details (Supply_Order_ID INT NOT NULL, Supply_ID INT NOT NULL, Quantity_Ordered INT NOT NULL, PRIMARY KEY(Supply_Order_ID, Supply_ID));")


## create wine table
cursor.execute("CREATE TABLE wine (Wine_ID INT NOT NULL, Name VARCHAR(45) NOT NULL, Style ENUM('Merlot', 'Cabernet', 'Chablis', 'Chardonnay') NOT NULL, Onhand_Quantity INT NOT NULL, Batch_ID INT NOT NULL, PRIMARY KEY(Wine_ID));")


## create batch table
cursor.execute("CREATE TABLE batch (Batch_ID INT NOT NULL, Bottled_Date DATETIME, Expiration_Date DATE NOT NULL, Quantity INT NOT NULL, Wine_ID INT NOT NULL, PRIMARY KEY(Batch_ID));")


## create wine_order table
cursor.execute("CREATE TABLE wine_order (Wine_Order_ID INT NOT NULL, Total_Cost DECIMAL(10, 2) NOT NULL, Order_Date DATETIME NOT NULL, Order_Method ENUM('Phone', 'Post', 'Online'), Order_Estimated_Delivery_Date DATETIME, Order_Actual_Delivery_Date DATETIME NOT NULL, Wine_ID INT NOT NULL, Distributor_ID INT NOT NULL, PRIMARY KEY(Wine_Order_ID));")


## create wine_order_details table
cursor.execute("CREATE TABLE wine_order_details (Wine_Order_ID INT NOT NULL, Wine_ID INT NOT NULL, Quantity_Ordered INT NOT NULL, PRIMARY KEY(Wine_Order_ID, Wine_ID));")


## create distributor_orders_details table
cursor.execute("CREATE TABLE wine_distributor_details (Wine_ID INT NOT NULL, Distributor_ID INT NOT NULL, PRIMARY KEY(Wine_ID, Distributor_ID));")


## create distributor table
cursor.execute("CREATE TABLE distributor (Distributor_ID INT NOT NULL, Name VARCHAR(45) NOT NULL, Street_Address_1 VARCHAR(35) NOT NULL, Street_Address_2 VARCHAR(35), Zip INT NOT NULL, Contact_First_Name VARCHAR(25) NOT NULL, Contact_Last_Name VARCHAR(25) NOT NULL, Phone_Number VARCHAR(15) NOT NULL, Email_Address VARCHAR(45), Active BIT(1) NOT NULL, Wine_ID INT NOT NULL, Wine_Order_ID INT NOT NULL, PRIMARY KEY(Distributor_ID));")


## create employee table
cursor.execute("CREATE TABLE employee (Employee_ID INT NOT NULL, First_Name VARCHAR(25) NOT NULL, Last_Name VARCHAR(25) NOT NULL, Hire_Date DATE NOT NULL, Start_Date DATE, Active BIT(1) NOT NULL, Department_ID INT NOT NULL, Position_ID INT NOT NULL, PRIMARY KEY(Employee_ID));")


## create employee_alternate table
cursor.execute("CREATE TABLE employee_alternate (Street_Address_1 VARCHAR(35) NOT NULL, Street_Address_2 VARCHAR(35), Zip INT NOT NULL, Phone_Number VARCHAR(15) NOT NULL, Email_Address VARCHAR(45), Term_Date DATE, Term_Reason VARCHAR(25), Rehireable BIT(1), SSN INT NOT NULL, DOB DATE, Employee_ID INT NOT NULL);")


## create employee_time_worked table
cursor.execute("CREATE TABLE employee_time_worked (Date DATE NOT NULL, Clock_In_Shift TIME NOT NULL, Clock_Out_Shift TIME NOT NULL, Clock_Out_Break TIME, Clock_In_Break TIME, Clock_Out_Lunch TIME, Clock_In_Lunch TIME, Employee_ID INT NOT NULL);")


## create zip_lookup table
cursor.execute("CREATE TABLE zip_lookup (Zip INT NOT NULL, City VARCHAR(25) NOT NULL, State VARCHAR(10) NOT NULL, Country VARCHAR(20), PRIMARY KEY(Zip));")


## create department_table
cursor.execute("CREATE TABLE department (Department_ID INT NOT NULL, Department_Name VARCHAR(15) NOT NULL, Department_Head INT, PRIMARY KEY(Department_ID));")


## create positions table
cursor.execute("CREATE TABLE positions (Position_ID INT NOT NULL, Position_Title VARCHAR(25) NOT NULL, Pay_Grade INT, Hourly BIT(1), Supervisory BIT(1), PRIMARY KEY(Position_ID));")


## create all foreign key constraints after all tables are created
cursor.execute("ALTER TABLE supply_order ADD CONSTRAINT fk_supply_order_supplies FOREIGN KEY(Supply_ID) REFERENCES supplies(Supply_ID);")
cursor.execute("ALTER TABLE supply_order ADD CONSTRAINT fk_supply_order_supplier FOREIGN KEY(Supplier_ID) REFERENCES supplier(Supplier_ID);")
cursor.execute("ALTER TABLE supplies ADD CONSTRAINT fk_supplies_supplier FOREIGN KEY(Supplier_ID) REFERENCES supplier(Supplier_ID);")
cursor.execute("ALTER TABLE supplies ADD CONSTRAINT fk_supplies_supply_order FOREIGN KEY(Supply_Order_ID) REFERENCES supply_order(Supply_Order_ID);")
cursor.execute("ALTER TABLE wine ADD CONSTRAINT fk_wine_batch FOREIGN KEY(Batch_ID) REFERENCES batch(Batch_ID);")
cursor.execute("ALTER TABLE batch ADD CONSTRAINT fk_batch_wine FOREIGN KEY(Wine_ID) REFERENCES wine(Wine_ID);")
cursor.execute("ALTER TABLE wine_order ADD CONSTRAINT fk_wine_order_wine FOREIGN KEY(Wine_ID) REFERENCES wine(Wine_ID);") 
cursor.execute("ALTER TABLE wine_order ADD CONSTRAINT fk_wine_order_distributor FOREIGN KEY(Distributor_ID) REFERENCES distributor(Distributor_ID);")
cursor.execute("ALTER TABLE distributor ADD CONSTRAINT fk_distributor_wine FOREIGN KEY(Wine_ID) REFERENCES wine(Wine_ID);")
cursor.execute("ALTER TABLE distributor ADD CONSTRAINT fk_distributor_wine_order FOREIGN KEY(Wine_Order_ID) REFERENCES wine_order(Wine_Order_ID);")
cursor.execute("ALTER TABLE employee ADD CONSTRAINT fk_employee_department FOREIGN KEY(Department_ID) REFERENCES department(Department_ID);")
cursor.execute("ALTER TABLE employee ADD CONSTRAINT fk_employee_positions FOREIGN KEY(Position_ID) REFERENCES positions(Position_ID);") 
cursor.execute("ALTER TABLE employee_alternate ADD CONSTRAINT fk_employee_alternate_employee FOREIGN KEY(Employee_ID) REFERENCES employee(Employee_ID);")
cursor.execute("ALTER TABLE employee_time_worked ADD CONSTRAINT fk_employee_time_worked_employee FOREIGN KEY(Employee_ID) REFERENCES employee(Employee_ID);")
cursor.execute("ALTER TABLE supplier ADD CONSTRAINT fk_supplier_zip_lookup FOREIGN KEY(Zip) REFERENCES zip_lookup(Zip);")
cursor.execute("ALTER TABLE distributor ADD CONSTRAINT fk_distributor_zip_lookup FOREIGN KEY(Zip) REFERENCES zip_lookup(Zip);")
cursor.execute("ALTER TABLE employee_alternate ADD CONSTRAINT fk_employee_alternate_zip_lookup FOREIGN KEY(Zip) REFERENCES zip_lookup(Zip);")

db.close()
