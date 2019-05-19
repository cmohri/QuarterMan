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
    p1title  = PasswordField('Period 1 Title', validators=[DataRequired()])
    p1time = PasswordField('Period 1 Time', validators=[DataRequired()])
    p2title = PasswordField('Period 2 Title', validators=[DataRequired()])
    p2time = PasswordField('Period 2 Time', validators=[DataRequired()])
    p3title = PasswordField('Period 3 Title', validators=[DataRequired()])
    p3time = PasswordField('Period 3 Time', validators=[DataRequired()])
    submit = SubmitField('Create Template')

@app.route("/", methods = ['GET', 'POST'])
def home():
    return render_template('home.html', a = str(datetime.datetime.now())[11:19])

@app.route('/maketemp', methods = ['GET', 'POST'])
def maketemp():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('maketemp.html', title='Create Template Schedule', form=form)

@app.route("/template", methods = ['GET', 'POST'])
def template():
    return render_template('template.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run()
