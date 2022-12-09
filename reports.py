import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="bacchus_user",
    password="mysqltest",
    database="bacchus_wine"
)
mycursor = mydb.cursor()


def wine_orders():
    # Execute the script using the cursor
    mycursor.execute(
        "select w.name, w.onhand_quantity, wo.order_date, wo.wine_order_id"
        " from wine w inner join wine_order_details wod on w.wine_id = wod.wine_id "
        "inner join wine_order wo on wod.wine_order_id = wo.wine_order_id order by w.name")

    # Fetch and print the results
    results = mycursor.fetchall()
    for row in results:
        print(
            f"Wine Name: {row[0]}\nOnhand Quantity: {row[1]}\nOrder Date: {row[2]}\nWine Order ID: {row[3]}"
        )
        print("\n")


def employee_time():
    mycursor.execute(
        'select first_name, last_name, etw.date, '
        'timestampdiff(minute,etw.clock_in_shift,etw.clock_out_shift)/60 as "Total Shift (Hr)", '
        'timestampdiff(minute,etw.clock_out_break,etw.clock_in_break) as "Break (Min)", '
        'timestampdiff(minute,etw.clock_out_lunch,etw.clock_in_lunch) as"Lunch (Min)", '
        '((timestampdiff(minute,etw.clock_in_shift,etw.clock_out_shift)) '
        '-(timestampdiff(minute,etw.clock_out_break,etw.clock_in_break)) '
        '-(timestampdiff(minute,etw.clock_out_lunch,etw.clock_in_lunch)))/60 as "Total Worked (Hr)" '
        'from employee e '
        'inner join employee_time_worked etw '
        'on e.employee_id = etw.employee_id'
    )

    timeworked = mycursor.fetchall()

    for employee in timeworked:
        print(
            '''First Name:{}\nLast Name:{}\nDate:{}\nHours Worked:{}\n'''.format(employee[0], employee[1], employee[2],
                                                                                 employee[3]))


def inventory():
    mycursor.execute('select * from supplies')

    details = mycursor.fetchall()

    for detail in details:
        print('''Supply ID: {}\nName: {}\nDescription: {}\nOn-Hand Quantity: {}\nUnit_Price: {}\nSupplier ID: {}
        '''.format(detail[0], detail[1], detail[2], detail[3], detail[4], detail[5]))
        # print("\n")
