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
@app.route('/form_input', methods=['GET', 'POST'])
def form_input():
    #if submit is pressed then go to calender
    #add stuff 
    return render_template('form_input.html')

#Add Break
@app.route('/break_form', methods=['GET', 'POST'])
def break_form():
    if request.method == 'POST': #not working
        break_name = request.form['breakname']
        print("break: ", break_name)
    return render_template('break_form.html')

#Add Assignment
@app.route('/assign_form', methods=['GET', 'POST'])
def assign_form():
    #add stuff to handle user input
    return render_template('assign_form.html')


if __name__=="__main__":
    app.run(debug=True)