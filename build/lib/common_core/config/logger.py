import logging
from pathlib import Path

from loguru import logger
import sys
import os


logger.remove()
logger.add(sys.stderr, level="INFO", format="<green>{time}</green> | <level>{message}</level>")

def get_logger(name: str):
    return logger.bind(name=name)


def setup_logger(log_dir: str = "logs", level: str = "INFO"):
    os.makedirs(log_dir, exist_ok=True)
    logger.remove()
    logger.add(sys.stdout, level=level)
    logger.add(f"{log_dir}/app.log", rotation="1 day", level=level)
    return logger



def setup_logger_OLD(log_level="INFO", log_file="logs/app.log"):
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=getattr(logging, log_level.upper(), "INFO"),
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger("app_logger")
    logger.info(f"Logger initialized: level={log_level}, file={log_file}")
    return logger
