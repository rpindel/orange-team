import create_tables
import fill_tables
import print_tables
import time
import reports

# we make our functions in the other files and call them on this one
# main.py needs to have the bacchus_wine_db_init.sql run first

print("I will load and display the tables for you...")
# Pause for two seconds for dramatic effect
time.sleep(2)
# create_tables.drop_tables()
create_tables.create_tables()
fill_tables.fill_tables()
create_tables.foreign_key_constraints()
print_tables.print_tables()  # tentative name for this function
while True:
    choice = input("Please Chose a report to look at. 'employee' for employee time, 'wine orders' for wine orders "
                   "over 1200, 'option 3' for the last option or q to quit:\n ").lower()
    print(choice)
    # Use an if-else statement to call the appropriate function
    if choice == 'employee':
        reports_employee_time()
    elif choice == 'wine orders':
        wine_orders()
    elif choice == 'option 3':
        reports.option_3()
    elif choice == 'q':
        print("Goodbye!")
        quit()
    else:
        print("Invalid choice. Please try again.")
