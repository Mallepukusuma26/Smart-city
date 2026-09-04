"""
Application Settings and Environment Configuration Classes.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_ROOT = BASE_DIR.parent

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "smart_city_super_secret_jwt_and_session_key_2026")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "smart_city_jwt_auth_secret_key_2026")
    JWT_ACCESS_TOKEN_EXPIRES = 86400  # 24 hours
    
    # Database Configuration
    DB_PATH = os.path.join(BASE_DIR, "smart_city.db")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "connect_args": {"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URI else {}
    }
    
    # Directory Paths
    DATASET_DIR = os.path.join(BASE_DIR, "datasets")
    TRAINED_MODELS_DIR = os.path.join(BASE_DIR, "trained_models")
    REPORTS_DIR = os.path.join(BASE_DIR, "reports_output")
    LOGS_DIR = os.path.join(BASE_DIR, "logs")
    
    # Static & Template Config for Frontend Serving
    FRONTEND_DIR = os.path.join(PROJECT_ROOT, "frontend")
    
    # Pagination Defaults
    DEFAULT_PAGE = 1
    DEFAULT_PER_PAGE = 20
    MAX_PER_PAGE = 100
    
    # Rate Limiting Defaults
    RATELIMIT_ENABLED = True
    RATELIMIT_DEFAULT = "200 per minute"
    
    # CORS Settings
    CORS_HEADERS = "Content-Type"
    CORS_SUPPORTS_CREDENTIALS = True

    @staticmethod
    def init_dirs():
        os.makedirs(Config.DATASET_DIR, exist_ok=True)
        os.makedirs(Config.TRAINED_MODELS_DIR, exist_ok=True)
        os.makedirs(Config.REPORTS_DIR, exist_ok=True)
        os.makedirs(Config.LOGS_DIR, exist_ok=True)


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    LOG_LEVEL = "DEBUG"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    LOG_LEVEL = "INFO"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    LOG_LEVEL = "WARNING"


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
