from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), index=True)
    last_name = db.Column(db.String(128), index=True)
    profile = db.Column(db.String(1024))
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<%s %s %s>" % (self.role, self.first_name, self.last_name)


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    description = db.Column(db.String(1024))
    head = db.Column(db.Integer)


class ScheduleSlot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prev = db.Column(db.Integer)
    next = db.Column(db.Integer)
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))