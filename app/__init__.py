from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os, config

def create_applicatrion():
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')
    app.config.from_object('config.TestingConfig')
    return app
application = create_applicatrion()
db = SQLAlchemy(application)
migrate = Migrate(application,db)
login_manager = LoginManager(application)
login_manager.login_view = 'login'

from . import views