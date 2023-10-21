#!/usr/bin/env python3

import connexion
import datetime
import os
from waitress import serve

from openapi_server import encoder, server_attr
from openapi_server.logger import log
from openapi_server.database.db_rds import db

def main():
    # Save the PID into a file
    log.info("PID: %s", os.getpid())
    with open('latest_deployment_pid.txt', 'w') as f:
        f.write(str(os.getpid()))

    # Connect to the databas
    db.connect()

    # Launch the server
    server_attr.start_time = datetime.datetime.now()
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'UniBar API'},
                pythonic_params=True,
                strict_validation=True)

    # Securely run the server
    serve(app, host="0.0.0.0", port=80)

    # Close the databse
    db.close()

if __name__ == '__main__':
    main()
