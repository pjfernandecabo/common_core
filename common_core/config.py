from pydantic import BaseModel
from pathlib import Path

class AppConfig(BaseModel):
    app_name: str = "default_app"
    log_level: str = "INFO"
    data_dir: Path = Path("./data")

config = AppConfig()
