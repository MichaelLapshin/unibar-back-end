# Defines the server thread
import threading
import connexion
import datetime
from waitress import serve

from openapi_server import encoder, server_attr

# For launching the server on a seperate thread
class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.srv = None
        self.daemon = True

    def run(self):
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

server_thread = ServerThread()
