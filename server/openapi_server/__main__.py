#!/usr/bin/env python3

import connexion
import datetime
import os

from openapi_server import encoder
from openapi_server import server_attr

def main():
    # Save the PID into a file
    print("PID:", os.getpid())
    with open('latest_deployment_pid.txt', 'w') as f:
        f.write(str(os.getpid()))

    # Launch the server
    server_attr.start_time = datetime.datetime.now()
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'UniBar API'},
                pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
