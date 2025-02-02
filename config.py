from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'test': TestConfig,
    'development': DevelopmentConfig
}