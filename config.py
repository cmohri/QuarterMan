import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ''' config file used for authentication with wtforms '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'the-wizard-of-oz'

    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_CLIENT_ID = ''
    GOOGLE_CLIENT_SECRET = ''
