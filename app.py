from flask import Flask, render_template, request, redirect, url_for, session
from schedule import Schedule
from assignment import Assignment
import sys

app = Flask(__name__)
app.secret_key = "b\r\t\xe01\x0c$\x8b\\\x99\x169\xa3Z\x11\x90c\xf5 \xf9y\x0bZ\x9c\x8b"

def dict2Sched(dictobj):
    schedule = Schedule()
    schedule.assignments_objs = dictobj["assignments_objs"]
    schedule.assignments_dicts = dictobj["assignments_dicts"]
    schedule.schedule = dictobj["schedule"]
    schedule.unassigned = dictobj["unassigned"]
    schedule.priority = dictobj["priority"]
    schedule.matrix = dictobj["matrix"]
    return schedule

@app.route("/")
def index():
    session["schedule"] = Schedule().__dict__
    return render_template("index.html")

# Form input
@app.route("/form_input", methods=["GET", "POST"])
def form_input():
    # if submit is pressed then go to calender
    # add stuff
    if request.method == "POST":
        schedule = dict2Sched(session["schedule"])
        schedule.create_calendar()
        session.pop("schedule")
        return render_template("output.html")
    else:
        return render_template("form_input.html")


# Add Break
@app.route("/break_form", methods=["GET", "POST"])
def break_form():
    if request.method == "POST":
        break_name = request.form["breakname"]
        break_start = request.form["startTime"]
        break_end = request.form["endTime"]
        breakdays = request.form.getlist("weekday")
        if break_start > break_end:
            return render_template("time_input_error.html")
        else:
            start = break_start.split(":")
            end = break_end.split(":")
            if int(end[1]) <= 30:
                break_end = end[0] + ":30"
            else:
                break_end = str(int(end[0]) + 1)
            if int(start[1]) > 30:
                break_start = start[0] + ":30"
            else:
                break_start = start[0]
        sched = session["schedule"]
        schedule = dict2Sched(sched)
        for day in breakdays:
            schedule.add_break(day, break_name, break_start, break_end)
        session["schedule"] = schedule.__dict__
        return redirect(url_for("form_input"))
        
    else:
        return render_template("break_form.html")


# Add Assignment
@app.route("/assign_form", methods=["GET", "POST"])
def assign_form():
    if request.method == "POST":
        assign_name = request.form["assign_name"]
        est_time = request.form["est_time"]
        percent = request.form["percentage"]
        priority = request.form["priority"]
        day = request.form["day"]
        time = request.form["time"]
        timeL = time.split(":")
        if int(timeL[1]) < 30:
            time = timeL[0]
        else:
            time = timeL[0] + ":30"
        assignment = Assignment(assign_name, int(percent), int(est_time), (day, time), int(priority))
        sched = session["schedule"]
        schedule = dict2Sched(sched)
        schedule.add_assignment(assignment.__dict__)
        session["schedule"] = schedule.__dict__
        return redirect(url_for("form_input"))
    else:
        return render_template("assign_form.html")

#Priority Survey
@app.route("/priority_survey", methods=["GET", "POST"])
def priority_survey():
    if request.method == "POST":
        priority = request.form["priority"]
        matrix = request.form["matrix"]
        sleep_start = request.form["sleep_start"]
        sleep_end = request.form["sleep_end"]
        start = sleep_start.split(":")
        end = sleep_end.split(":")
        if int(end[1]) > 30:
            sleep_end = end[0] + ":30"
        else:
            sleep_end = end[0]
        if int(start[1]) > 30:
            sleep_start = start[0] + ":30"
        else:
            sleep_start = start[0]
        sched = session["schedule"]
        schedule = dict2Sched(sched)
        for days in schedule.days:
            schedule.add_sleep(days, sleep_start, sleep_end)
        schedule.priority = priority
        schedule.matrix = matrix
        session["schedule"] = schedule.__dict__
        return redirect(url_for("form_input"))
    else:
        return render_template("priority_survey.html")

if __name__ == "__main__":
    app.run(debug=True)
