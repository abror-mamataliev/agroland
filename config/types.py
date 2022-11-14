from decouple import config
from os.path import dirname


class BaseConfig:

    PROJECT_FOLDER: str = dirname(dirname(__file__))

    SECRET_KEY = config("SECRET_KEY")

    DATABASE_ENGINE = config("DATABASE_ENGINE")
    DATABASE_NAME = config("DATABASE_NAME")
    if DATABASE_ENGINE == "sqlite":
        SQLALCHEMY_DATABASE_URI: str = f"{DATABASE_ENGINE}:///database/{DATABASE_NAME}.db"
    elif DATABASE_ENGINE == "postgresql":
        DATABASE_HOST = config("DATABASE_HOST")
        DATABASE_PORT = config("DATABASE_PORT", cast=int)
        DATABASE_USER = config("DATABASE_USER")
        DATABASE_PASSWORD = config("DATABASE_PASSWORD")
        SQLALCHEMY_DATABASE_URI: str = f"{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


class DevConfig(BaseConfig):

    DEBUG: bool = True

    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class ProdConfig(BaseConfig):

    DEBUG: bool = False
