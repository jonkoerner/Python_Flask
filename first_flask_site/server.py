from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_num = []
    for i in range(10):
        my_num.append(i)
    return render_template("index.html", mydata = my_num )
    
@app.route('/dashboard')
def dashboard():
    return "Hello Dashboard"

app.run(debug= True)