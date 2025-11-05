import pytest
from core.config_loader import ConfigLoader

def test_config_loads_correctly():
    cfg = ConfigLoader("settings.yaml").load()
    assert "app" in cfg.app
    assert cfg.logging["level"] in ["INFO", "DEBUG", "WARNING"]

def test_logger_initializes(tmp_path):
    from core.config.logger import setup_logger
    log_file = tmp_path / "test.log"
    logger = setup_logger("INFO", str(log_file))
    logger.info("test message")
    assert log_file.exists()
