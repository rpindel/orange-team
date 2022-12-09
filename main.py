import create_tables
import fill_tables
import reports
import employee_time
import supply_report
import wine_orders


#import print_tables
#import time
#import reports

# we make our functions in the other files and call them on this one
# main.py needs to have the bacchus_wine_db_init.sql run first

print("I will load and display the tables for you...")
# Pause for two seconds for dramatic effect
#time.sleep(2)
# create_tables.drop_tables()
create_tables.create_tables()
fill_tables.fill_tables()
create_tables.foreign_key_constraints()
#print_tables.print_tables()  # tentative name for this function
while True:
    choice = input("Please Chose a report to look at. 'employee' for employee time, 'wine orders' for wine orders "
                   "over 1200, 'supply report' for the last option or q to quit:\n ").lower()
    print(choice)
    # Use an if-else statement to call the appropriate function
    if choice == 'employee':
        employee_time.employee_time()
    elif choice == 'wine orders':
        wine_orders.wine_orders()
    elif choice == 'supply report':
        supply_report.supply_report()
    elif choice == 'q':
        print("Goodbye!")
        quit()
    else:
        print("Invalid choice. Please try again.")
