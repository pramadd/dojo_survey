from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def Name():
    name = request.form['name']
    dojolocation = request.form['dojolocation']
    language = request.form['language']
    comment =request.form['comment']

    if len(request.form['name'])<1:
        flash("Name cannot be empty!")
    else:
        flash("") 

    if len(request.form['comment']) >120 :
        flash("comments should be only 120 characters")
    else:
        flash("")        

    return render_template("result.html", name = name,dojolocation=dojolocation,language=language,comment=comment)
    return redirect("/")


app.run(debug = True)