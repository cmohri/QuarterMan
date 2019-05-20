from flask import Flask
from config import Config
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from app import routes, models