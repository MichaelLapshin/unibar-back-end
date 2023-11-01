import pymysql

from openapi_server import server_attr
from openapi_server.logger import log

class DB: 
    @property
    def conn(self):
        # Connect to the database
        _conn = None
        try:
            _conn = pymysql.connect(
                host=server_attr.rds_hostname,
                port=server_attr.rds_port,
                user=server_attr.rds_username,
                password=server_attr.rds_password,
                cursorclass=pymysql.cursors.DictCursor
            )

            if _conn is not None:
                log.debug("Connected to the MySQL database.")
            else:
                raise Exception("Failed to connect to the RDS MySQL database.")
            
            _conn.select_db(server_attr.rds_database)

        except pymysql.MySQLError as e:
            log.error(f"Error: {e}")
            _conn.close()
        
        return _conn

db = DB()
