import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'the-wizard-of-oz'

    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_CLIENT_ID = '380938917381-p3u1a6qdrh4b72nlqjti8tlcbb30drhp.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'QM2mPPMW1BvwEBZDD9iIgWXL'