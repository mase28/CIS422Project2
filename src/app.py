#Flask App file
import os 
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

#Initial page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_input', methods=['GET', 'POST'])
def form_input():
    if request.method == 'POST':
        #do stuff when the form is submitted

        # redirect to end the POST handling
        #go to calendar
        return redirect(url_for('calendar.html'))
    return render_template('form_input.html')
'''
@app.route('/calendar')
def '''