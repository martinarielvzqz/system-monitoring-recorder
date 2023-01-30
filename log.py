import logging
import sys
from pathlib import Path


LOG_FILENAME = "monitor.log"
LOG_PATH = Path("")


level = logging.INFO

formatter = logging.Formatter(fmt="[%(asctime)s] %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
logger.setLevel(level)

# console
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(level)
sh.setFormatter(formatter)

# file
fh = logging.FileHandler(Path(LOG_FILENAME), encoding='utf-8')
fh.setLevel(level)
fh.setFormatter(formatter)

logger.addHandler(sh)
logger.addHandler(fh)