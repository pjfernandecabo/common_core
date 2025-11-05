import yaml
from pathlib import Path
from pydantic import BaseModel, ValidationError

class AppConfig(BaseModel):
    app: dict
    logging: dict
    ai: dict
    database: dict

class ConfigLoader:
    """Carga y valida settings.yaml"""
    def __init__(self, path: str = "settings.yaml"):
        self.path = Path(path)
        self.config = None

    def load(self) -> AppConfig:
        if not self.path.exists():
            raise FileNotFoundError(f"Config file not found: {self.path}")
        with open(self.path, "r") as f:
            data = yaml.safe_load(f)
        try:
            self.config = AppConfig(**data)
        except ValidationError as e:
            raise ValueError(f"Invalid config: {e}")
        return self.config
