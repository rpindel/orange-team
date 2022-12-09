import mysql.connector

def supply_report():

    db = mysql.connector.connect(
        user="bacchus_user",
        password="mysqltest",
        host="localhost",
        database="bacchus_wine"
    )

    cursor = db.cursor()

    cursor.execute('''select s.name, so.supply_order_id, so.total_cost, so.order_date, 
	so.order_estimated_delivery_date,so.order_actual_delivery_date,
(timestampdiff(DAY,so.order_estimated_delivery_date,so.order_actual_delivery_date)) as "Actual vs Estimated Delivery"
from supplier s
inner join supply_order so
on s.supplier_id = so.supplier_id;

''')

    details = cursor.fetchall()

    for detail in details:
        print('''Supplier:{}\nSupply Orders:{}\nCost:{}\n'''.format(detail[0], detail[1], detail[2]))
