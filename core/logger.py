import logging
from pathlib import Path

def setup_logger(log_level="INFO", log_file="logs/app.log"):
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
