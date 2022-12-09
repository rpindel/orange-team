import mysql.connector

def wine_orders():

    db = mysql.connector.connect(
        user="bacchus_user",
        password="mysqltest",
        host="localhost",
        database="bacchus_wine"
    )

    cursor = db.cursor()

    cursor.execute('''select d.name as Distributor, w.wine_order_id, w.total_cost, w.order_date, w.order_method, w.order_estimated_delivery_date, w.order_actual_delivery_date,     (TIMESTAMPDIFF(MINUTE,w.order_date,w.order_estimated_delivery_date))/60/24 "Estimated Shipping Time Total DAYS",     (TIMESTAMPDIFF(MINUTE,w.order_date,w.order_actual_delivery_date))/60/24 "Actual Shipping Time Total DAYS"
from wine_order w
inner join distributor d on w.distributor_id = d.distributor_id
;
''')

    details = cursor.fetchall()

    for detail in details:
        print('''Distributor:{}\nWine Orders:{}\nPrice:{}\nOrder Date and Time:{}\n'''.format(detail[0], detail[1], detail[2], detail[3]))
