import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = ''

class DevConfig(Config):
    SECRET_KEY = os.urandom(32)