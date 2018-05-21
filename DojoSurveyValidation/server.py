# from __future__ import division
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = "dakjshdkjsah"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["post"])
def results():
    print(request.form)
    session["data"] = request.form
    session["Ibelieve"]="hello"
    return redirect("/display_results")

@app.route("/display_results")
def display_results():

    return render_template("results.html", name="Jon", email="koernerj@gmail.com")

app.run(debug=True)
