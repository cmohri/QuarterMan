from flask import render_template, url_for, redirect, flash, session, request
from os import urandom
import json, csv
import datetime
from elbarto import app, models, oauth, db
from .forms import TemplateForm, ScheduleForm

from authlib.flask.client import OAuth
from loginpass import create_flask_blueprint, OAUTH_BACKENDS
from loginpass.google import Google

# oath stuff
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

def time_to_int(t):
    return t.hour * 3600 + t.minute * 60 + t.second

def int_to_time(i):
    #h = int(i/3600)

    return datetime.time(int(i / 3600), int(( (i % 3600 )/ 60) % 60), 0)

blueprint = create_flask_blueprint(Google, oauth, handle_authorize)
app.register_blueprint(blueprint, url_prefix='/google')

def load_schedule():
    schedule = {}
    with open('schedules.csv', newline='\n') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for day in reader:

            schedule[day[0]] = {
                "template": day[1],
                "day_type": day[2]
            }
    return schedule

daily_schedule = load_schedule()


@app.route("/")
def index():
    date = datetime.date.today().strftime("%m-%d-%Y")
    schedule_name = daily_schedule[date]["day_type"] if daily_schedule.get("date") else "Regular"
    schedule = models.Schedule.query.filter_by(name=schedule_name).one()
    return redirect(url_for("display_schedule", id=schedule.id))


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
        prev_node = None

        is_private = request.form.get("private") == "y"
        new_schedule = models.Schedule(name=request.form.get("title"), desc=request.form.get("desc"), private=is_private, author_id=session.get("user").get("id"))
        for slot in schedule:
            start = time_to_int(datetime.datetime.strptime(slot["start"], '%H:%M').time())
            end = time_to_int(datetime.datetime.strptime(slot["end"], '%H:%M').time())

            slot_node = models.ScheduleSlot(name=slot["name"], start=start, end=end)
            db.session.add(slot_node)
            db.session.commit()
            if prev_node is not None:
                if slot_node.start < prev_node.end:
                    return "Error - Make sense please"
                prev_node.next = slot_node.id
                db.session.add(prev_node)
            else:
                new_schedule.head_slot = slot_node.id
            prev_node = slot_node
        prev_node.next = -1;
        db.session.add(prev_node)
        db.session.add(new_schedule)
        db.session.commit()
        return redirect(url_for("display_schedule", id=new_schedule.id))


@app.route("/schedules/mine")
def private_gallery():
    schedules = models.Schedule.query.filter_by(author_id=session.get("user").get("id")).all()
    return render_template("lib.html", schedules=schedules)


@app.route("/schedules/browse")
def public_gallery():
    '''Displays gallery of created templates'''
    # get list of all templates please
    # create list:  (next line)
    schedules = models.Schedule.query.filter_by(private = False).all()
    print(schedules)
    # pass it as an argument
    return render_template("lib.html", schedules = schedules)


@app.route("/schedules/<int:id>")
def display_schedule(id):
    def generate_slot_dict(slot):
        return {
            "start": slot.start,
            "end": slot.end,
            "name": slot.name
        }

    schedule = models.Schedule.query.filter_by(id = id).one()
    curr = models.ScheduleSlot.query.filter_by(id = schedule.head_slot).one()

    schedule_slots = [generate_slot_dict(curr)]
    while curr.next != -1:
        curr = models.ScheduleSlot.query.filter_by(id = curr.next).one()
        schedule_slots.append(generate_slot_dict(curr))
    return render_template("display.html", schedule = schedule_slots, name = schedule.name)
