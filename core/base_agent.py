from abc import ABC, abstractmethod
import logging

class BaseAgent(ABC):
    """Clase base para todos los agentes AI o sistemas autónomos"""

    def __init__(self, config, logger: logging.Logger):
        self.config = config
        self.logger = logger

    @abstractmethod
    def run(self):
        """Ejecuta la lógica principal del agente"""
        pass

    def log(self, message: str, level: str = "info"):
        getattr(self.logger, level.lower())(message)
