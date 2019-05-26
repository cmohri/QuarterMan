import os

from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authlib.flask.client import OAuth

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
oauth = OAuth(app)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from app import routes, models, db