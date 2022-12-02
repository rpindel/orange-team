import mysql.connector
import create_tables
import fill_tables
import print_tables

# we make our functions in the other files and call them on this one
create_tables.create_tables()  # tentative names for this function
fill_tables.fill_tables()
print_tables.print_tables()  # tentative name for this function
