import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    SECRET_KEY = "bwfkkano2no214"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ##### настройка Flask-Mail #####
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'YOU_MAIL@gmail.com'
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    # MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'