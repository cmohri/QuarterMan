import datetime

from app import app, models, db
from flask import render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user
from flask_dance.contrib.google import make_google_blueprint, google

google_blueprint = make_google_blueprint(scope=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"])
app.register_blueprint(google_blueprint, url_prefix="/login")


@app.route("/login")
def student_login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    if not google.authorized:
        return redirect(url_for("google.login"))
    try:
        resp = google.get("/oauth2/v1/userinfo")
    except:
        return redirect(url_for("google.login"))
    u = models.User.query.filter_by(email=resp.json()["email"]).first()
    if not u:
        u = models.User(first_name=resp.json()["given_name"], last_name=resp.json()["family_name"], email=resp.json()["email"])
        db.session.add(u)
        db.session.commit()
    login_user(u)
    return redirect(url_for("index"))


@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template('home.html', a =str(datetime.datetime.now())[11:19])
