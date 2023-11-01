#!/usr/bin/env python3

import os

from openapi_server.server import server_thread
from openapi_server.logger import log
from openapi_server.database.db_rds import db

def main():
    # Save the PID into a file
    log.info("PID: %s", os.getpid())
    with open('latest_deployment_pid.txt', 'w') as f:
        f.write(str(os.getpid()))

    # Start the server
    server_thread.start()
    server_thread.join()

if __name__ == '__main__':
    main()
