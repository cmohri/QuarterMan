from elbarto import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    '''Creates db for user '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), index=True)
    last_name = db.Column(db.String(128), index=True)
    email = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return "<%s %s %s>" % (self.first_name, self.last_name, self.email)

# basically nodes in linked list of Schedule
class ScheduleSlot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    next = db.Column(db.Integer)  # stores id of next slot in schedule

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    desc = db.Column(db.String)
    head_slot = db.Column(db.Integer) # stores id of head of schedule slot linked list
    private = db.Column(db.Boolean)
