import logging
import threading
from flask import Flask, session, has_request_context
from datetime import datetime, timezone

class SessionFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.session_id = session.get("session_id", "unknown")
        else:
            record.session_id = f"{record.name}"
        
        record.thread_id = hex(threading.get_native_id())[2:10]
        return super().format(record)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

log = logging.getLogger()

# Disable the default stdout logging by removing all handlers
for handler in log.handlers:
    log.removeHandler(handler)

# Set file logger
fh = logging.FileHandler(f"unibar_server_{datetime.now(timezone.utc)}.log")
fh.setFormatter(SessionFormatter('%(asctime)s %(levelname)-4s (SID: %(session_id)-8s, THREAD: %(thread_id)-8s)  %(message)s'))
log.addHandler(fh)

# Set stdout logger
stdout = logging.StreamHandler()
stdout.setFormatter(SessionFormatter('%(asctime)s %(levelname)-4s  (SID: %(session_id)-8s, THREAD: %(thread_id)-8s)  %(message)s'))
log.addHandler(stdout)
