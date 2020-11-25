from flask import Flask, render_template, request
from schedule import Schedule
import sys

app = Flask(__name__)

schedule = Schedule()

# Initial page - Welcome


@app.route('/')
def index():
    return render_template('index.html')

# Form input
@app.route('/form_input', methods=['GET', 'POST'])
def form_input():
    # if submit is pressed then go to calender
    # add stuff
    return render_template('form_input.html')


# Add Break
@app.route('/break_form', methods=['GET', 'POST'])
def break_form():
    if request.method == 'POST':
        break_name = request.form['breakname']
        break_start = request.form['startTime']
        break_end = request.form['endTime']
        if break_start > break_end:
            return render_template("time_input_error.html")
        else:
            start = break_start.split(':')
            end = break_end.split(':')
            if int(end[1]) <= 30:
                break_end = end[0] + ":30"
            else:
                break_end = str(int(end[0]) + 1)
            if int(start[1]) > 30:
                break_start = start[0] + ":30"
            else:
                break_start = start[0]
        breakdays = request.form.getlist('weekday')
        for day in breakdays:
            schedule.add_break(day, break_name, break_start, break_end)
        return render_template('submitted_break.html')
    else:
        return render_template('break_form.html')


# Add Assignment
@app.route('/assign_form', methods=['GET', 'POST'])
def assign_form():
    # add stuff to handle user input
    return render_template('assign_form.html')

if __name__ == "__main__":
    app.run(debug=True)
