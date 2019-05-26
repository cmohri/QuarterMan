from flask import render_template, url_for, redirect, flash, jsonify, session, request
from os import urandom
import datetime
from config import Config
from app import app, models, oauth, db
from forms import TemplateForm

from authlib.flask.client import OAuth
from loginpass import create_flask_blueprint, OAUTH_BACKENDS
from loginpass.google import Google


def handle_authorize(remote, token, user_info):
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
    print(user_info)
    return redirect(url_for("index"))

blueprint = create_flask_blueprint(Google, oauth, handle_authorize)
app.register_blueprint(blueprint, url_prefix='/google')


@app.route("/")
def index():
    return render_template("home.html")

@app.route("/logout", methods = ["GET"])
def logout():
    session.pop("user")
    return redirect(request.referrer)

@app.route('/maketemp', methods = ['GET', 'POST'])
def maketemp():
    form = TemplateForm()
    if form.validate_on_submit():
        return render_template('template.html', form = form)
    return render_template('maketemp.html', title='Create Template Schedule', form=form)

@app.route("/template", methods = ['GET', 'POST'])
def template():
    form = TemplateForm()
    return render_template('template.html', form = form)