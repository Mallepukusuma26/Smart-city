"""
Logging Configuration Module.
"""
import logging
import os
from logging.handlers import RotatingFileHandler
from .settings import Config

def setup_logging(app=None, log_level="INFO"):
    Config.init_dirs()
    log_file = os.path.join(Config.LOGS_DIR, "smart_city.log")
    
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s (%(pathname)s:%(lineno)d): %(message)s"
    )
    
    file_handler = RotatingFileHandler(
        log_file, maxBytes=10485760, backupCount=5, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)
    
    if app:
        app.logger.addHandler(file_handler)
        app.logger.addHandler(stream_handler)
        app.logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
        
    return root_logger
