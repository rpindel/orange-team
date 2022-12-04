import create_tables
import fill_tables
# import print_tables

# we make our functions in the other files and call them on this one
# main.py needs the following run manually on the MySQL instance first
# CREATE DATABASE bacchus_wine;
# DROP USER IF EXISTS 'bacchus_user'@'localhost';
# CREATE USER 'bacchus_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'mysqltest';
# GRANT ALL PRIVILEGES ON bacchus_wine.* TO 'bacchus_user'@'localhost';

# create_tables.drop_tables()
create_tables.create_tables()
fill_tables.fill_tables()
create_tables.foreign_key_constraints()
# print_tables.print_tables()  # tentative name for this function

