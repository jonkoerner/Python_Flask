
from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/")
def index():
    if len(request.form)== {}:
        pass
    else:
        print request.form["name"]
    return render_template('index.html')


app.run(debug=True, port= 5003)
