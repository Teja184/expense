import os

class DevConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "very strong secret"


class ProdConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "very strong secret"

config_dict = {
     "development": DevConfig,
     "production": ProdConfig,
     "default": DevConfig,  # Default fallback
 }