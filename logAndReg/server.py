from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re
import bcrypt

app = Flask(__name__)
app.secret_key = "Whatever"
mysql = MySQLConnector(app, 'the_wall')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	# print(request.form)
	valid = True

	if len(request.form["first_name"]) < 2:
		valid = False
		flash("First name must be at least 2 characters long", "ERROR")

	if len(request.form["last_name"]) < 2:
		valid = False
		flash("Last name must be at least 2 characters long", "ERROR")

	if len(request.form["email"]) < 1:
		valid = False
		flash("Email is required", "ERROR")
	elif not EMAIL_REGEX.match(request.form["email"]):
		valid = False
		flash("Invalid Email", "ERROR")
	else:
		query = "SELECT * FROM users WHERE email=:email"
		user_list = mysql.query_db(query, request.form)
		if len(user_list) > 0:
			valid = False
			flash("Email already in use", "ERROR")

	if len(request.form["password"]) < 8:
		valid = False
		flash("Password must be 8 or more characters", "ERROR")
	elif request.form["password"] != request.form["confirm_password"]:
		valid = False
		flash("Password must match Confirm Password", "ERROR")

	if valid:
		flash("You successfully registered, good job!", "SUCCESS")
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW());"
		data = {
			"first_name": request.form["first_name"],
			"last_name": request.form["last_name"],
			"email": request.form["email"],
			"password": bcrypt.hashpw(request.form["password"].encode(), bcrypt.gensalt())
		}
		user_id = mysql.query_db(query, data)
		session["username"] = request.form["first_name"]
		session["id"] = user_id
		return redirect("/the_wall")
	else:
		return redirect("/")

@app.route("/login", methods=["POST"])
def login():
	# print(request.form)

	valid = True

	if len(request.form["email"]) < 1:
		valid = False
		flash("Email is required", "ERROR")
	elif not EMAIL_REGEX.match(request.form["email"]):
		valid = False
		flash("Invalid Email", "ERROR")
	else:
		query = "SELECT * FROM users WHERE email=:email"
		user_list = mysql.query_db(query, request.form)
		if len(user_list) < 1:
			valid = False
			flash("Unknown email", "ERROR")

	if len(request.form["password"]) < 8:
		valid = False
		flash("Password must be 8 or more characters", "ERROR")

	if valid:
		if bcrypt.checkpw(request.form["password"].encode(), user_list[0]["password"].encode()):
			flash("You successfully logged in, good job!", "SUCCESS")
			session["username"] = user_list[0]["first_name"]
			session["id"] = user_list[0]["id"]
			return redirect("/the_wall")
		else:
			flash("Incorrect password", "ERROR")

	return redirect("/")

@app.route("/the_wall")
def the_wall():
	if "id" not in session:
		flash("You have to log in first!", "ERROR")
		return redirect("/")
	return render_template("the_wall.html")

@app.route("/logout")
def logout():
	session.clear()
	flash("You successfully logged out, good job!", "SUCCESS")	
	return redirect("/")



app.run(debug=True)