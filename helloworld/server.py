from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ():
    return 'Hello World!'

app.run(debug=True)