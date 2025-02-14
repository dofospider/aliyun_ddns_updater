import time
import yaml
from loguru import logger
from pathlib import Path


class Logger:
    def __init__(self):
        config=self.load_config()
        log_path=Path(Path.cwd(),"log")
        log_time=time.strftime("%Y-%m-%d")
        self.log_file=f"{log_path}/ddns_updater{log_time}.log"
        self.rotation=config['logger']['rotation']
        self.retention=config['logger']['retention']
        self.enqueue=config['logger']['enqueue']
        self.level=config['logger']['level']
        # logger.add(self.log_file, rotation=self.rotation, retention=self.retention, enqueue=self.enqueue,level=self.level)
        logger.add(self.log_file, rotation=self.rotation, retention=self.retention, enqueue=self.enqueue,level=self.level,format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level:<8}</level> | {file}:{function}:{line} {message}")
        self.logger = logger

    def load_config(self):
        try:
            with open('logger_config.yaml', 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            return {
                'logger': {
                    'rotation': '50 MB',
                    'retention': '1 month',
                    'enqueue': True,
                    'level': 'DEBUG'
                }
            }

    def trace(self, message):
        self.logger.trace(message)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def success(self, message):
        self.logger.success(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
