from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_applicatrion():
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')
    app.config.from_object('config.TestingConfig')
    return app
application = create_applicatrion()
db = SQLAlchemy(application)
migrate = Migrate(application,db)

from . import views