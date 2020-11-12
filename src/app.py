#Flask App file
import os 
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MakeSecretKey'
Bootstrap(app)

#Initial page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_input', methods=['GET', 'POST'])
def form_input():
    return render_template('form_input.html')

if __name__=="__main__":
    app.run(debug=True)