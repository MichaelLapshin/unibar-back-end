import pymysql
import logging
from openapi_server import server_attr

conn = None
log = logging.getLogger()

def connect():
    # Connect to the database
    try:
        conn = pymysql.connect(
            host=server_attr.rds_hostname,
            port=server_attr.rds_port,
            user=server_attr.rds_username,
            password=server_attr.rds_password,
            cursorclass=pymysql.cursors.DictCursor
        )

        if conn is not None:
            log.info("Connected to the MySQL database.")
        else:
            raise Exception("Failed to connect to the RDS MySQL database.")
        
        conn.select_db(server_attr.rds_database)

    except pymysql.MySQLError as e:
        log.error(f"Error: {e}")
        conn.close()

def close():
    # Close the database connection
    conn.close()
