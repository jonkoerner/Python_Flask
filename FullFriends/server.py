from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'FullFriends')

@app.route("/")
def index():
    query = "SELECT * FROM Users"
    Users = mysql.query_db(query)
    return render_template("index.html", all_friends=Users)

@app.route("/add_friend", methods=["POST"])
def add_friend():
    print request.form["name"]
    print request.form["age"]

    query = "INSERT INTO Users (Name, Age, FriendSince) VALUES(:Name, :Age, NOW())"
    data = {
        'Name': request.form["name"],
        'Age': request.form["age"]
    }
    mysql.query_db(query, data)
    return redirect("/")

#print mysql.query_db("SELECT * FROM Users")


app.run(debug=True)
