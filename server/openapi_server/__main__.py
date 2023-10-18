#!/usr/bin/env python3

import connexion
import datetime

from openapi_server import encoder
from openapi_server import server_attr

def main():
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
