import os

class Config(object):
    DEBUG = False
    TESTING = False
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL") or "redis://localhost:6379"
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND") or "redis://localhost:6379"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
