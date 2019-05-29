from flask import render_template, url_for, redirect, flash, session, request
from os import urandom
import json
import datetime
from config import Config
from app import app, models, oauth, db
from .forms import TemplateForm, ScheduleForm

from authlib.flask.client import OAuth
from loginpass import create_flask_blueprint, OAUTH_BACKENDS
from loginpass.google import Google


def handle_authorize(remote, token, user_info):
    ''' Handles authentication of user information '''
    q = models.User.query.filter_by(email=user_info.email)
    if q.count() == 0:
        # If user doesn't exist in our database yet, create user
        u = models.User(first_name=user_info.given_name, last_name=user_info.family_name, email=user_info.email)
        db.session.add(u)
        db.session.commit()
    else:
        u = q.one()
    session['user'] = {
        "id": u.id,
        "first_name": u.first_name,
        "last_name": u.last_name,
        "email": u.email
    }
    return redirect(url_for("index"))

blueprint = create_flask_blueprint(Google, oauth, handle_authorize)
app.register_blueprint(blueprint, url_prefix='/google')


@app.route("/")
def index():
    ''' Home route, loads standard schedule page on schedule '''
    return render_template("home.html")

@app.route("/logout", methods = ["GET"])
def logout():
    ''' Logs the user out, removing them from the current session '''
    session.pop("user")
    return redirect(url_for("index"))

@app.route("/schedules/create", methods=["GET", "POST"])
def create_schedule():
    if session.get("user") is None:
        return redirect("/google/login")
    schedule_form = ScheduleForm()
    if request.method == "GET":
        return render_template("create_schedule.html", schedule_form=schedule_form)
    else:
        schedule = json.loads(request.form.get("schedule"))





@app.route('/maketemp', methods = ['GET', 'POST'])
def maketemp():
    '''creates template for either public or private gallery use. Makes use
    of the TemplateForm object, which is created in forms.py and imported '''
    form = TemplateForm()
    if form.validate_on_submit():
        return render_template('template.html', form = form)
    return render_template('maketemp.html', title='Create Template Schedule', form=form)

@app.route("/template", methods = ['GET', 'POST'])
def template():
    '''Loads up the template created in maketemp '''
    form = TemplateForm()
    return render_template('template.html', form = form)
