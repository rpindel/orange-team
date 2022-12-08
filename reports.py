import mysql.connector
import os
import subprocess

mydb = mysql.connector.connect(
    host="localhost",
    user="bacchus_user",
    password="mysqltest",
    database="bacchus_wine"
)
mycursor = mydb.cursor()


# These Functions only work if the appropriate SQL script exists in the same folder as our python program
def wine_orders():
    # Set the location of the MySQL script
    wine_orders_path = './wine_order_report.sql'

    # Check if the script exists
    if os.path.exists(wine_orders_path):
        # Run the MySQL script using the subprocess module
        subprocess.call(
            ['mysql', '-u', 'bacchus_user', '-p', 'mysqltest', '-h', 'localhost', 'bacchus_wine', '<'
                , wine_orders_path])
    else:
        print('MySQL script not found.')


def employee_time():
    # Set the location of the MySQL script
    employee_time_path = './employee_time_report.sql'

    # Check if the script exists
    if os.path.exists(employee_time_path):
        # Run the MySQL script using the subprocess module
        subprocess.call(
            ['mysql', '-u', 'bacchus_user', '-p', 'mysqltest', '-h', 'localhost', 'bacchus_wine', '<',
             employee_time_path])
    else:
        print('MySQL script not found.')


def option_3():
    """ this is a call an external sql script option
    # Set the location of the MySQL script
    script_path = './option_3.sql'

    # Check if the script exists
    if os.path.exists(script_path):
        # Run the MySQL script using the subprocess module
        subprocess.call(
            ['mysql', '-u', 'bacchus_user', '-p', 'mysqltest', '-h', 'localhost', 'bacchus_wine', '<', script_path])
    else:
        print('MySQL script not found.') """

    """ this is the 'pure' python option
    
    mycursor.execute(# this is where sql statement goes)
    option_3_report = mycursor.fetchall()
    for row in option_3_report:
        print(
           # this is where print statement goes
        )"""