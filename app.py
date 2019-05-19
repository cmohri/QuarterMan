from flask import Flask, render_template, request, session, url_for, redirect, flash
from os import urandom
import datetime
from config import Config
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

import sqlite3
app = Flask(__name__)
app.secret_key = urandom(32)
app.config.from_object(Config)

class LoginForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    numpds = PasswordField('Number of Periods', validators=[DataRequired()])
    submit = SubmitField('Create Template')

@app.route("/", methods = ['GET', 'POST'])
def home():
    return render_template('home.html', a = str(datetime.datetime.now())[11:19])

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Create Template Schedule', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run()
