import logging
import sys

logger = logging.getLogger("hikayeapp")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",
                                datefmt = "%Y-%m-%d %H:%M:%S")

handler.setFormatter(formatter)


if not logger.handlers:
    logger.addHandler(handler)

def get_logger(name: str = "hikayeapp"):
    return logger.getChild(name)





