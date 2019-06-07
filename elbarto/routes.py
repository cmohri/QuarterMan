from flask import render_template, url_for, redirect, flash, session, request
from os import urandom, listdir, path
import json, csv
import datetime
from elbarto import app, models, oauth, db
from .forms import ScheduleForm

from authlib.flask.client import OAuth
from loginpass import create_flask_blueprint, OAUTH_BACKENDS
from loginpass.google import Google

BASE_DIR = path.dirname(path.abspath(__file__))
classapath = path.join(BASE_DIR, "schedules.csv")

classbpath = path.join(BASE_DIR,"schedules")

# oauth stuff
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
    return datetime.time( int(i / 3600), int(( (i % 3600 )/ 60) % 60), 0)

app.jinja_env.filters['int_to_time'] = int_to_time

blueprint = create_flask_blueprint(Google, oauth, handle_authorize)
app.register_blueprint(blueprint, url_prefix='/google')

def load_schedules():
    schedule = {}
    with open(classapath, newline='\n') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for day in reader:
            schedule[day[0]] = {
                "A_or_B": day[1],
                "day_type": day[2]
            }
    for filename in listdir(classbpath):
        load_schedule(path.join("schedules", filename))
    return schedule


def load_schedule(filename):
    print("Loading schedule from %s" % filename)
    with open(filename, newline='\n') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')

        name = next(reader)[0]
        desc = next(reader)[0]
        if models.Schedule.query.filter_by(name=name).count() != 0:
            return

        new_schedule = models.Schedule(name=name, desc=desc, private=False)
        prev_node = None
        for row in list(reader):
            start = time_to_int(datetime.datetime.strptime(row[1], '%H:%M').time())
            end = time_to_int(datetime.datetime.strptime(row[2], '%H:%M').time())

            slot_node = models.ScheduleSlot(name=row[0], start=start, end=end)
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

daily_schedule = load_schedules()


@app.route("/")
def index():
    date = datetime.date.today().strftime("%m-%d-%Y")
    schedule_name = daily_schedule[date]["day_type"] if daily_schedule.get(date) else "Regular"
    day_type = daily_schedule[date]["A_or_B"] if daily_schedule.get(date) else ""
    schedule = models.Schedule.query.filter_by(name=schedule_name).one()
    return redirect(url_for("display_schedule", id=schedule.id, day_type=day_type))


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
    if request.method == "GET" or (not schedule_form.validate_on_submit()):
        return render_template("create_schedule.html", schedule_form=schedule_form)
    else:
        schedule = json.loads(request.form.get("schedule"))
        if len(schedule) == 0:
            flash("Error - You must enter at least one schedule slot")
            return render_template("create_schedule.html", schedule_form=schedule_form)
        prev_node = None

        is_private = request.form.get("private") == "y"
        new_schedule = models.Schedule(name=request.form.get("title"), desc=request.form.get("desc"), private=is_private, author_id=session.get("user").get("id"))
        for slot in schedule:
            try:
                start = time_to_int(datetime.datetime.strptime(slot["start"], '%H:%M').time())
                end = time_to_int(datetime.datetime.strptime(slot["end"], '%H:%M').time())
            except:
                flash("Error - Issue with entered time")
                return render_template("create_schedule.html", schedule_form=schedule_form)

            slot_node = models.ScheduleSlot(name=slot["name"], start=start, end=end)
            db.session.add(slot_node)
            db.session.commit()
            if slot_node.end == slot_node.start:
                flash("Error - Schedules cannot have same start and end times")
                return render_template("create_schedule.html", schedule_form=schedule_form)
            if slot_node.end < slot_node.start:
                flash("Error - Schedule cannot end before it starts")
                return render_template("create_schedule.html", schedule_form=schedule_form)
            if prev_node is not None:
                if slot_node.end == prev_node.end:
                    flash("Error - Schedules cannot overlap")
                    return render_template("create_schedule.html", schedule_form=schedule_form)
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
    if schedule.private is True and (not session.get("user") or schedule.author_id != session.get("user").get("id")):
        return redirect(url_for("index"))
    curr = models.ScheduleSlot.query.filter_by(id = schedule.head_slot).one()

    schedule_slots = [generate_slot_dict(curr)]
    while curr.next != -1:
        curr = models.ScheduleSlot.query.filter_by(id = curr.next).one()
        schedule_slots.append(generate_slot_dict(curr))
    return render_template("display.html", schedule = schedule_slots, name = schedule.name, day_type=request.args.get("day_type"))
