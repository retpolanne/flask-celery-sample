import os


class Config(object):
    ENV = os.getenv("ENV")
    DEBUG = False
    TESTING = False
    CELERY_BROKER_URL = os.getenv(
        "CELERY_BROKER_URL") or "redis://"
    CELERY_RESULT_BACKEND = os.getenv(
        "CELERY_RESULT_BACKEND") or "redis://"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    CELERY_BROKER_URL = os.getenv(
        "CELERY_BROKER_URL") or "redis://"
    CELERY_RESULT_BACKEND = os.getenv(
        "CELERY_RESULT_BACKEND") or "redis://"
