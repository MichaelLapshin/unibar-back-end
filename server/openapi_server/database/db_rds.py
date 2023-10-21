import pymysql
import logging
from openapi_server import server_attr

log = logging.getLogger()

class DB:
    def connect(self):
        # Connect to the database
        self._conn = None
        try:
            self._conn = pymysql.connect(
                host=server_attr.rds_hostname,
                port=server_attr.rds_port,
                user=server_attr.rds_username,
                password=server_attr.rds_password,
                cursorclass=pymysql.cursors.DictCursor
            )

            if self._conn is not None:
                log.info("Connected to the MySQL database.")
            else:
                raise Exception("Failed to connect to the RDS MySQL database.")
            
            self._conn.select_db(server_attr.rds_database)

        except pymysql.MySQLError as e:
            log.error(f"Error: {e}")
            self._conn.close()

    def conn(self):
        if self._conn == None:
            log.error("RDS DB connection is None!")
        return self._conn

    def close(self):
        # Close the database connection
        self._conn.close()

db = DB()
