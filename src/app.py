#Flask App file
import os 
from flask import Flask, render_template, request, redirect, url_for, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MakeSecretKey'
Bootstrap(app)

#Initial page - Welcome
@app.route('/')
def index():
    return render_template('index.html')

#Form input
@app.route('/form_input')
def form_input():
    return render_template('form_input.html')

#Add Break
@app.route('/break_form')
def break_form():
    return render_template('break_form.html')

#Add Assignment
@app.route('/assign_form')
def assign_form():
    return render_template('assign_form.html')


if __name__=="__main__":
    app.run(debug=True)