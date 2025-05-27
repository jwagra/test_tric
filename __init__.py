"""test_tric"""
import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)
APP.config.from_object(os.environ['APP_SETTINGS'])

DB = SQLAlchemy(APP)

migrate = Migrate(APP, DB)
