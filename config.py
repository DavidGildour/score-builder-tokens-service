from credentials import jwt_secret


class Config:
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = jwt_secret
    JWT_BLACKLIST_ENABLED = True


class DevelopmentConfig(Config):
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PROPAGATE_EXCEPTIONS = True
