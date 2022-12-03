

import mysql.connector

mydb= mysql.connector.connect()
config = {
    "user": "bacchus_user",
    "password": "bacchus_wine",
    "host": "localhost",
    "database": "bacchus_wine",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

mycursor = db.cursor()

# create employee table
# cursor.execute("CREATE TABLE employee (Employee_ID INT NOT NULL, First_Name VARCHAR(25) NOT NULL, Last_Name VARCHAR(25) NOT NULL, Hire_Date DATE NOT NULL, Start_Date DATE, Active BIT(1) NOT NULL, Department_ID INT NOT NULL, Position_ID INT NOT NULL, PRIMARY KEY(Employee_ID));")

def fill_tables():
    # fill employee table
    employee = ("INSERT INTO employee (Employee_ID, First_Name VARCHAR(25), Last_Name VARCHAR(25), Hire_Date DATE, Start_Date DATE, Active BIT(1), Department_ID INT, Position_ID INT)" 
                "VALUES (%s,%s, %s,%s,%s,%s,%s)")

    values = [
        (6930090, 'Stan', 'Bacchus',	'2019-12-04',	'2019-12-04',	'Y', 1000, 100,),
        (1380275, 'Davis', 'Bacchus', '2019-12-04', '2019-12-04', 'Y', 1000, 100),
        (8613677, 'Elyse', 'Bailey', '1983-08-04', '1983-08-05', 'Y', 4000, 120),
        (4059962, 'Emmanuel', 'Ramsey', '2016-10-07', '2016-10-15', 'Y', 3000, 120),
        (1842386, 'Keira', 'Peck', '1992-08-25', '1992-08-26', 'Y', 6000, 200),
        (5937994, 'Mia', 'Frost', '1999-09-15', '1999-09-16', 'Y', 5000, 200),
        (9685338, 'Amaya', 'Hebert', '2014-01-14', '2014-01-15', 'Y', 2000, 200),
        (7480510, 'Roz', 'Murphy', '2010-03-10', '2010-03-15', 'Y', 3000, 220),
        (8995741, 'Bob', 'Ulrich', '2011-04-25', '2011-04-26', 'Y', 3000, 220),
        (5687918, 'Antwan', 'Cline', '1985-04-16', '1985-04-17', 'Y', 3000, 220),
        (3695025, 'Anyiah', 'Vincent', '1997-11-14', '1997-11-15', 'Y', 3000, 220),
        (5667699, 'Davian', 'Clark', '2003-04-28', '2003-04-29', 'Y', 3000, 220),
        (4180563, 'Deborah', 'Harrell', '2007-08-13', '2007-08-17', 'Y', 3000, 220),
        (9855487, 'Leon', 'Gibbins', '2022-05-19', '2022-05-26', 'Y', 3000, 220),
        (7767463, 'Henry', 'Doyle', '1982-04-02', '1982-04-03', 'Y', 5000, 300),
        (5939049, 'Sara', 'Esparza', '2020-01-22', '2020-01-26', 'Y', 2000, 320),
        (5823178, 'Jordyn', 'Aguilar', '2007-03-05', '2007-03-06', 'Y', 4000, 400),
        (7863543, 'Santiago', 'Branch', '2020-01-29', '2020-02-05', 'Y', 5000, 400),
        (4916879, 'Marley', 'Herring', '2007-09-27', '2007-09-28', 'Y', 5000, 420),
        (5307392, 'Vivian', 'Caldwell', '2011-07-27', '2011-07-28', 'Y', 4000, 420),
        (6383017, 'Janet', 'Collins', '2017-05-15', '2017-05-17', 'Y', 2000, 500),
        (2795091, 'Alisa', 'Franklin', '1988-06-16', '1988-06-17', 'Y', 2000, 500),
        (2799911, 'Trenton', 'Bird', '1990-12-14', '1990-12-15', 'Y', 2000, 500),
        (3021812, 'Adriana', 'Randolph', '2002-02-08', '2002-02-09', 'Y', 2000, 500),
        (7579383, 'Alexus', 'Calhoun', '2006-08-30', '2006-09-05', 'Y', 2000, 500),
        (1944186, 'Maria', 'Costanza', '1983-06-17', '1983-06-18', 'Y', 6000, 600),
        (1314667, 'Carlos', 'Horne', '1995-02-17', '1995-02-18', 'Y', 5000, 600),
        (4145223, 'Parker', 'Hart', '2006-11-02', '2006-11-03', 'Y', 5000, 600)
    ]
    mycursor.executemany(employee, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were insert into employees table")

    # fill employee time worked table

    employee_time_worked = ("INSERT INTO employee_time_worked (Date_Worked DATE, Clock_In_Shift TIME, Clock_Out_Shift TIME, Clock_Out_Break TIME, Clock_In_Break TIME, Clock_Out_Lunch TIME, Clock_In_Lunch TIME, Employee_ID INT)"
                            "VALUES(%s,%s, %s,%s,%s,%s,%s)")

    values = [
    ('2022-11-01',  '07:00:00',  '11:00:00',    'NULL',       'NULL',      'NULL',      'NULL',        '4916879'),
    ('2022-11-02',  '07:00:00',	 '12:00:00',	'10:00:00',	  '10:15:00',  'NULL',	    'NULL',	      '5307392'),
    ('2022-11-03',  '08:00:00',  '16:00:00',    '11:00:00'    '11:15:00',  '13:00:00',  '13:30:00',    '6383017'),
    ('2022-11-04',  '10:00:00',  '15:00:00',    '13:00:00',   '13:15:00',  'NULL',      'NULL',        '2795091'),
    ('2022-11-05',  '10:00:00',  '18:00:00',    '13:00:00',   '13:15:00',  '15:00:00',  '15:30:00',    '2799911'),
    ('2022-11-06',  '11:00:00',  '19:00:00',    '14:00:00',   '14:15:00',  '16:00:00',  '16:30:00',    '3021812'),
    ('2022-11-07',  '13:00:00',  '17:00:00',    'NULL',       'NULL',      'NULL',      'NULL',        '7579383'),
    ('2022-11-08',  '13:00:00',  '21:00:00',    '16:00:00',   '16:15:00',  '18:00:00'   '18:30:00',    '1944186'),
    ('2022-11-09',  '15:00:00',  '20:00:00',    '18:00:00',   '18:15:00',  'NULL',      'NULL',         '1314667'),
    ('2022-11-10',  '17:00:00',  '21:00:00',    'NULL',       'NULL',      'NULL',      'NULL',         '4145223'),

    ]
    mycursor.executemany(employee_time_worked, values)
    mydb.commit()
    print(mycursor.rowcount, "rows were inserted into Employee Time Worked Table")

    # fill position table

    position = ("INSERT INTO position (Position_ID, Position_Title VARCHAR(25), Pay_Grade INT, Hourly BIT(1), Supervisory BIT(1))" 
                "VALUES (%s,%s, %s,%s,%s)")

    values = [
        (100, 'Owner', 'Null', 'N','Y'),
        (120, 'Administrative Assistant', 20, 'Y', 'N'),
        (200, 'Sales', 30, 'N', 'N'),
        (220, 'Marketing', 25, 'N', 'N'),
        (300, 'Production Manager', 23, 'Y', 'Y'),
        (320, 'Production Laborer', 20, 'Y', 'N'),
        (400, 'Maintenance', 20, 'Y', 'N'),
        (420, 'Environmental', 15, 'Y', 'N'),
        (500, 'Accounting / Payroll', 30, 'Y', 'N'),
        (600, 'Logistics', 25, 'Y', 'N'),
    ]
    mycursor.executemany(position, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into position table")

# fill zip code table

    zip_lookup = ("INSERT INTO zip_lookup(Zip INT, City VARCHAR(25), State VARCHAR(10), Country VARCHAR(20))"
                  "VALUES (%s, %s,%s,%s)")

    values = [
        (68111, 'Omaha', 'NE', 'USA'),
        (50310, 'Des Moines', 'IA', 'USA'),
        (53188, 'Waukesha', 'WI', 'USA'),
        (27513, 'Cary', 'NC', 'USA'),
        (52501, 'Ottumwa', 'IA', 'USA'),
        (51537, 'Harland', 'IA', 'USA'),
    ]

    mycursor.executemany(zip_lookup, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into zip table")

# fill department table
    deparment = ("INSERT INTO department(Department_ID INT, Department_Name VARCHAR(15), Department_Head INT (Employee_ID))"
                  "VALUES (%s, %s,%s,%s)")

    values = [
        (1000, 'owners', '6930090'),
        (2000, 'Finance', 6383017),
        (3000, 'Marketing', 748051),
        (4000, 'Facilites', 5307392),
        (5000, 'Production', 7767463),
        (6000, 'Distribution', 1944186),
    ]

    mycursor.executemany(deparment, values)
    mydb.commit()
    print(mycursor.rowcount, "row were inserted into department table")