import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True

    SECRET_KEY = os.environ.get("SECRET_KEY") or "stuyalumni19"
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_OAUTH_CLIENT_ID = 'id'
    GOOGLE_OAUTH_CLIENT_SECRET = 'secret'