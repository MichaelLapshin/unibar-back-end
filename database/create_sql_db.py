import pymysql
from pymysql import Error

# Confirmation to proceed
if input("Are you sure you want to create new database tables? (y/n)") != 'y' or \
    input("All data previously in the database will be erased. Are you sure you want to continue? (y/n)") != 'y':
    print("Aborting the SQL database table creation program.")
    exit(1)

# Parameters
print("=== Enter the following information about the database ===")
host = input("Hostname: ")
port = int(input("Port: "))
user = input("User: ")
password = input("Password: ")
database = input("Database: ")
print("==========================================================")

# Connect to database
try:
    conn = pymysql.connect(host=host, port=port, user=user, password=password)
    conn.select_db(database)
except pymysql.Error as e:
    print("Failed to connect to the database: ", e)
    exit(1)

# Create the database schema and tables
# TODO
