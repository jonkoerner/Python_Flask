from flask import Flask , redirect, render_template, session, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    print 2
    # Here's the line that changed. We're rendering a template from a post route now.
    return render_template('index.html')

@app.route('/us', methods=['POST'])
def second():
    print request.form
    return redirect('/')


app.run(debug=True, port=5002)
