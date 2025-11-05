from datetime import datetime
from pathlib import Path
from typing import Union
import json

def current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def ensure_dir(path: Union[str, Path]):
    Path(path).mkdir(parents=True, exist_ok=True)
    #Path(path).mkdir(parents=True, exist_ok=True)

def timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def save_json(data, path: str):
    ensure_dir(Path(path).parent)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
