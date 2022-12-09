import create_tables
import fill_tables
#import print_tables
import sales
# we make our functions in the other files and call them on this one
# main.py needs to have the bacchus_wine_db_init.sql run first

# create_tables.drop_tables()
create_tables.create_tables()
fill_tables.fill_tables()
create_tables.foreign_key_constraints()
#print_tables.print_tables()  # tentative name for this function
sales.sales()