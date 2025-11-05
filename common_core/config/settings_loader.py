import yaml
from pydantic import BaseModel
from pathlib import Path

class AppSettings(BaseModel):
    app_name: str = "default_app"
    log_level: str = "INFO"

def load_settings(path: str = "settings.yaml") -> AppSettings:
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file {path} not found")
    with open(config_path, "r") as f:
        data = yaml.safe_load(f)
    return AppSettings(**data)
