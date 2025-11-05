from core.config_loader import ConfigLoader
from core.config.logger import setup_logger
from core.base_agent import BaseAgent

class DemoAgent(BaseAgent):
    def run(self):
        self.log(f"Starting demo agent {self.config.app['name']} v{self.config.app['version']}")
        # Ejemplo de lógica
        self.log("Running AI process simulation...")
        self.log("Agent finished successfully.")

if __name__ == "__main__":
    cfg = ConfigLoader().load()
    logger = setup_logger(cfg.logging["level"], cfg.logging["file"])

    agent = DemoAgent(cfg, logger)
    agent.run()
