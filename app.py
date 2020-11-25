from flask import Flask, render_template, request, redirect, url_for, session
from schedule import Schedule
from assignment import Assignment
import sys

app = Flask(__name__)

session["schedule"] = Schedule()

# Initial page - Welcome


@app.route("/")
def index():
    session["schedule"] = Schedule()
    return render_template("index.html")

# Form input
@app.route("/form_input", methods=["GET", "POST"])
def form_input():
    # if submit is pressed then go to calender
    # add stuff
    return render_template("form_input.html")


# Add Break
@app.route("/break_form", methods=["GET", "POST"])
def break_form():
    if request.method == "POST":
        break_name = request.form["breakname"]
        break_start = request.form["startTime"]
        break_end = request.form["endTime"]
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
        breakdays = request.form.getlist("weekday")
        for day in breakdays:
            session["schedule"].add_break(day, break_name, break_start, break_end)
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
        session["schedule"].add_assignment(assignment)
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
        for days in schedule.days:
            session["schedule"].add_sleep(days, sleep_start, sleep_end)
        schedule.priority = priority
        schedule.matrix = matrix
        session["schedule"].create_calendar()
        return render_template("output.html")
    else:
        return render_template("priority_survey.html")

if __name__ == "__main__":
    app.run(debug=True)
