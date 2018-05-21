from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    errors = []
    if (len(request.form["name"])) > 4:
        flash("this is a valid name!")
    else:
        print ('your name must be longer') 
    if request.form["name"] != "Jon":
        print ("this is not the right name")
    #do some validations here!
    print errors
    return redirect('/')


app.run(debug=True)
