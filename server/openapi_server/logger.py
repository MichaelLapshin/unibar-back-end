import logging
from datetime import datetime, timezone

# Setup logging
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)

log = logging.getLogger()
fh = logging.FileHandler(f"unibar_server_{datetime.now(timezone.utc)}.log")
log.addHandler(fh)
