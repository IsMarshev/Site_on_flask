from flask import Flask
import os, config

def create_application():
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')
    app.config.from_object('config.TestingConfig')
    return app

application = create_application()

from . import views