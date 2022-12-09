import mysql.connector
def employee_time():

    db = mysql.connector.connect(
        user="bacchus_user",
        password="mysqltest",
        host="localhost",
        database="bacchus_wine"
    )

    cursor = db.cursor()

    cursor.execute('''select e.first_name, e.last_name, etw.date, 
timestampdiff(minute,etw.clock_in_shift,etw.clock_out_shift)/60 as "Total Shift (Hr)",
timestampdiff(minute,etw.clock_out_break,etw.clock_in_break) as "Break (Min)",
timestampdiff(minute,etw.clock_out_lunch,etw.clock_in_lunch) as"Lunch (Min)",
((timestampdiff(minute,etw.clock_in_shift,etw.clock_out_shift))
-(timestampdiff(minute,etw.clock_out_break,etw.clock_in_break))
-(timestampdiff(minute,etw.clock_out_lunch,etw.clock_in_lunch)))/60 as "Total Worked (Hr)"
from employee e
inner join employee_time_worked etw
on e.employee_id = etw.employee_id;
''')

    timeworked = cursor.fetchall()

    for employee in timeworked:
        print('''First Name:{}\nLast Name:{}\nDate:{}\nHours Worked:{}\n'''.format(employee[0], employee[1], employee[2], employee[3]))
